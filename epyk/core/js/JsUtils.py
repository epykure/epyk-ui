#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import json
import logging
import functools
from pathlib import Path
from typing import Union, Optional, List, Any
from epyk.core.py import primitives
from epyk.core.py import types

from epyk.conf import global_settings
from epyk.core.js import treemap
from epyk.core.js import Imports
from epyk.core.js.primitives import JsObject

PROFILE_COUNT = 0


# --------------------------------------------------------------------------------------------------------------
#                                                       DECORATORS
#
def incompatibleBrowser(browsers: List[str]):
    """Decorator to send a warning for functions or packages which are restricted to some browsers.

    :param browsers: Incompatible browsers
    """
    def decorator(func):
        @functools.wraps(func)
        def decorated(*args, **kwargs):
            print("Warning: This function - %s - is not compatible with %s" % (func.__name__, ", ".join(browsers)))
            return func(*args, **kwargs)

        return decorated

    return decorator


def fromVersion(data: dict):
    """This system decorate will decorate a component function to specify during the Python execution
    if a method is not yet available in the current state of the Javascript modules.

    Usage::

      .fromVersion({'jqueryui': '1.12.0'})

    :param data: Set the minimum version of a package for a specific function

    :return: The decorated function
    """

    def decorator(func):
        @functools.wraps(func)
        def decorated(*args, **kwargs):
            for k, v in data.items():
                if k in Imports.JS_IMPORTS:
                    for mod in Imports.JS_IMPORTS[k]['modules']:
                        if mod.get('version', Imports.JS_IMPORTS[k]['version']) < v:
                            raise ValueError("Function %s can only be used from %s version %s (current %s)" % (
                                func.__name__, k, v, mod['version']))

            return func(*args, **kwargs)

        return decorated

    return decorator


def untilVersion(data: dict, new_feature: str):
    """This system decorate will decorate a component function to specify during the Python execution
    if a method is not available since the current state of the Javascript modules.
    Indeed as it is possible to override JS version on the fly it is also important to get notify with functions
    are not compatible anymore.
    This decorator will also propose an alternative with the new feature to.

    Usage::

        .untilVersion({'jqueryui': '1.12.0'}, "new function")

    :param data: The maximum version number for a function by packages
    :param new_feature: The new function name

    :return: The decorated function.
    """

    def decorator(func):
        @functools.wraps(func)
        def decorated(*args, **kwargs):
            for k, v in data.items():
                if k in Imports.JS_IMPORTS:
                    for mod in Imports.JS_IMPORTS[k]['modules']:
                        if mod.get('version', Imports.JS_IMPORTS[k]['version']) > v:
                            raise ValueError(
                                "Function %s can only be used since %s version %s (current %s). It has been replaced by %s" % (
                                    func.__name__, k, v, mod['version'], new_feature))

            return func(*args, **kwargs)

        return decorated

    return decorator


# --------------------------------------------------------------------------------------------------------------
#                                                       FUNCTIONS
#
def isJsData(js_data: Union[str, primitives.JsDataModel, float, dict, list]):
    """Common function to check if the object exists in Python.

    Usage::

       JsUtils.isJsData(attr)

    :param js_data: The Python Javascript data
    """
    return hasattr(js_data, 'toStr')


def jsConvertData(js_data: Union[str, primitives.JsDataModel, float, dict, list], js_funcs: Optional[Union[list, str]],
                  depth: bool = False, force: bool = False) -> Union[str, JsObject.JsObject]:
    """Generic conversion function for any data in the internal framework.
    This will convert to String any data coming from the Javascript Python interface.

    Any pure Python object will be converted using the json function to be then written as a string
    to the resulting page.

    :param js_data: The Python Javascript data
    :param js_funcs: Optional. The conversion function (not used)
    :param depth: Optional. Set to true of it is a nested object
    :param force: Optional. Whatever the object received force the string conversion
    """
    if ((not getattr(js_data, 'varData', None) or getattr(js_data, 'varData', None) == "None") and not getattr(js_data, 'fncName', None)) or force:
        if hasattr(js_data, 'toStr'):
            return js_data.toStr()

        else:
            try:
                if depth:
                    if isinstance(js_data, dict):
                        result = []
                        for k, v in js_data.items():
                            result.append("%s: %s" % (k, jsConvertData(v, js_funcs, depth=depth)))
                        return "{%s}" % ", ".join(result)

                    else:
                        result = [jsConvertData(v, js_funcs, depth=depth) for v in js_data]
                        return "[%s]" % ", ".join(result)

                if force:
                    return json.dumps(js_data)

                return JsObject.JsObject(json.dumps(js_data))

            except TypeError as err:
                return str(js_data)

            except Exception as err:
                if isinstance(js_data, range):
                    return JsObject.JsObject(json.dumps(list(js_data)))

                raise

    return js_data


def jsConvert(data: Any, jsDataKey: Union[str, primitives.JsDataModel], isPyData: bool, js_funcs: Union[list, str]):
    """

    :param data:
    :param jsDataKey:
    :param bool isPyData:
    :param Optional[Union[list, str]] js_funcs: The Javascript functions.
    """
    if isPyData:
        if hasattr(data, 'toStr'):
            return data.toStr()

        else:
            try:
                return json.dumps(data)

            except Exception as err:
                if isinstance(data, range):
                    return json.dumps(list(data))

                raise

    if jsDataKey is not None:
        data = "%s[%s]" % (data, jsConvertData(jsDataKey, None))
    if js_funcs is not None:
        data = "%s(%s)" % (js_funcs, data)
    return data


def jsWrap(data: Any, profile: bool = None):
    """Shortcut to wrap a python object to a generic JavaScript object.
    This will avoid the automatic conversion to string if it is a variable.

    :param data: Object. A python object to be serialised
    :param profile: Wrap content the return profiling information
    """
    global PROFILE_COUNT

    if profile is not None:
        wrapped_data = [
            "var t%s = performance.now()" % PROFILE_COUNT,
            "let result = %s" % data]
        if isinstance(profile, dict):
            profile["id"] = PROFILE_COUNT
            wrapped_data.append("console.log('%(name)s, start: ' + t%(id)s + ' ms')" % profile)
            wrapped_data.append("console.log('%(name)s, process: ' + (performance.now() - t%(id)s) + ' ms')" % profile)
        else:
            wrapped_data.append("console.log(performance.now() - t%s)" % PROFILE_COUNT)
        PROFILE_COUNT += 1
        return JsObject.JsObject.get("(function(){%s; return result})()" % ";".join(wrapped_data))

    return JsObject.JsObject.get(data)


def getJsValid(value: str, fail: bool = True):
    """Return an error if the variable name is not valid following the Javascript naming conventions.
    Even if the function will fail it will propose a valid name to replace the one passed in input

    Usage::

      >>> getJsValid("test-js", False)
      'testjs'

      >>> getJsValid("234@test-js", False)
      'js234testjs'

      >>> getJsValid("234@test-js", True)
      Traceback (most recent call last):
          ...
      Exception: Javascript Variable name 234@test-js, for example you could use js234testjs instead

    `w3schools <https://www.w3schools.com/js/js_conventions.asp>`_

    :param value: The Javascript variable name
    :param fail: Optional. Flat to raise an exception if the name is not valid on the Javascript side

    :return: The input variable name or a suggested one.
    """
    regex = re.compile('[^a-zA-Z0-9_]')
    clean_name = regex.sub('', value.strip())
    is_valid = not value[0].isdigit() and clean_name == value
    if fail and not is_valid:
        raise ValueError("Javascript Variable name %s, for example you could use js%s instead" % (value, clean_name))

    if clean_name[0].isdigit():
        clean_name = "js%s" % clean_name
    return clean_name


def jsConvertFncs(js_funcs: types.JS_FUNCS_TYPES, is_py_data: bool = False,
                  jsFncVal=None, toStr: bool = False, profile: Optional[Union[bool, dict]] = False):
    """Generic conversion function for all the PyJs functions.

    :param js_funcs: The PyJs functions.
    :param is_py_data: Optional. A flag to force the Python conversion using json
    :param jsFncVal:
    :param toStr: Optional. A flag to specify if the result should be aggregated
    :param profile. Optional.
    """
    global PROFILE_COUNT

    if not isinstance(js_funcs, list):
        js_funcs = [js_funcs]

    cnv_funcs = []
    for f in js_funcs:
        if f is None:
            continue

        if hasattr(f, 'toStr'):
            str_func = f.toStr()
            if jsFncVal is not None:
                str_func = str_func.replace("trans_val", jsFncVal)
            cnv_funcs.append(str_func)
        else:
            if is_py_data:
                str_val = json.dumps(f)
                if jsFncVal is not None:
                    str_val = str_val.replace("trans_val", jsFncVal)
                cnv_funcs.append(str_val)
            else:
                if jsFncVal is not None:
                    f = str(f).replace("trans_val", jsFncVal)
                cnv_funcs.append(f)
    if profile is not None and profile:
        cnv_funcs.insert(0, "var t%s = performance.now()" % PROFILE_COUNT)
        if isinstance(profile, dict):
            profile["id"] = PROFILE_COUNT
            cnv_funcs.append("console.log('%(name)s, start: ' + t%(id)s + ' ms')" % profile)
            cnv_funcs.append("console.log('%(name)s, process: ' + (performance.now() - t%(id)s) + ' ms')" % profile)
        else:
            cnv_funcs.append("console.log(performance.now() - t%s)" % PROFILE_COUNT)
        PROFILE_COUNT += 1
    if toStr:
        return ";".join(cnv_funcs)

    return cnv_funcs


def cleanFncs(fnc):
    """Try to remove as much as possible all the characters in order to speed up the javascript
    Indeed most of the browsers are using minify Javascript to make the page less heavy.

    Thus pre-stored function code can be written to be easier to read.

    :param fnc: The Javascript String

    :return: Return a cleaned a minify Javascript String.
    """
    return "".join([r.strip() for r in fnc.strip().split('\n')])


def isNotDefined(varName: str):
    """Check if a variable is defined.

    Usage::

      JsUtils.isNotDefined(varId)

    :param varName: The varName

    :return: A string in Python and a Boolean in Javascript.
    """
    return "typeof %s === 'undefined'" % varName


def dataFlows(data: Any, flow: Optional[dict], page: primitives.PageModel = None) -> str:
    """All the chaining of data flow transformation to feed the various widgets.
    flow must point to function with the following signature (data, {obj1, obj2, .... objN=0})

    TODO: Add Aggs and Filters

    usage::

        i_var = page.ui.inputs.input("test", html_code="invar")
        i_var2 = page.ui.inputs.input(html_code="invar2")
        i_var2.validation(required=True)
        i_var3 = page.ui.inputs.input(html_code="invar3")
        btn = page.ui.button("ok")

        page.properties.js.add_text('''function TestFunc(data, {d=1, a, b=0, c=0}){
            console.log('a='+ a);console.log('b='+ b);console.log('c='+ c);console.log('d='+ d);
            return c}''')

        btn.click([
            i_var.build(15, dataflows=[
                {"name": "TestFunc", "parameters": {
                    "a": 1,
                    "c": i_var2.dom.valid,
                    "d": i_var3.dom.content,
                }}
            ])
        ])

    :param data: Input data
    :param flow: Data flow processes (name and parameters)
    :param page: Page object with the full context
    """
    data_expr = jsConvertData(data, None, force=True)
    if not flow:
        if hasattr(data_expr, "toStr"):
            return data_expr.toStr()

        return data_expr

    for dataflow in flow:
        if dataflow.get("level") == "item":
            # shortcut to simple transforms on items on dataset
            dataflow["name"] = "function(dataset){dataset.forEach(function(item){%s}); return dataset}" % dataflow["name"]
        if "file" in dataflow:
            ext_js_file = Path(dataflow["file"])
            if page is not None:
                page.js.customFile(ext_js_file.name, path=ext_js_file.parent)
        if "parameters" in dataflow:
            pmt_expr = []
            # simple parameter translation for methods or components
            for k, v in dataflow["parameters"].items():
                if hasattr(v, "dom"):
                    pmt_expr.append("%s:%s" % (k, v.dom.content.toStr()))
                elif hasattr(v, "toStr"):
                    pmt_expr.append("%s:%s" % (k, v.toStr()))
                else:
                    pmt_expr.append("%s:%s" % (k, v))
            if "class" in dataflow:
                data_expr = "new %s({%s}).%s(%s)" % (
                    dataflow["class"], ", ".join(pmt_expr), dataflow.get("name", "transform"), data_expr)
            else:
                data_expr = "%s(%s, {%s})" % (dataflow["name"], data_expr, ", ".join(pmt_expr))
        else:
            if "class" in dataflow:
                data_expr = "%s().%s(%s)" % (dataflow["class"], dataflow["name"], data_expr)
            else:
                data_expr = "%s(%s)" % (dataflow["name"], data_expr)
    return data_expr


def convertOptions(options: Any, varId: str) -> str:
    """Convert options to valid objects for JavaScript to pick up.
    Base on the input data transformation will be either performed in Python or in JavaScript.

    :param options: The new options for the JavaScript object
    :param varId: The JavaScript object to be updated
    """
    if isJsData(options):
        return '''(function (ops, obj){
function dictToExpr(a, b){Object.entries(a).forEach(([k, v]) => {if (
typeof v == "object" && !Array.isArray(v)){if(b[k]){dictToExpr(v, b[k])}} else {b[k] = v}})}; return dictToExpr(ops, obj)
})(%s, %s)''' % (options.toStr(), varId)

    result = []

    def dict_to_expr(options, result, varId: str):
        for k, v in options.items():
            if isinstance(v, dict):
                if isinstance(k, int):
                    dict_to_expr(v, result, "%s[%s]" % (varId, k))
                else:
                    dict_to_expr(v, result, "%s.%s" % (varId, k))
            else:
                if isinstance(k, int):
                    result.append("%s[%s] = %s" % (varId, k, jsConvertData(v, None)))
                else:
                    result.append("%s.%s = %s" % (varId, k, jsConvertData(v, None)))
    dict_to_expr(options, result, varId)
    return ";".join(result)


class JsFile:

    def __init__(self, script_name: Optional[str] = None, path: Optional[str] = None):
        self.script_name, self.path = script_name, path
        self.file_path = os.path.join(path, "js")  # all the files will be put in a common directory
        if not os.path.exists(self.file_path):
            os.mkdir(self.file_path)
        self.__data = []

    def writeJs(self, js_funcs: Union[list, str]):
        """Write the Javascript piece of code to the file.

        Usage::

          dt = JsDate.new("2019-05-03")
          f.writeJs([dt,
            Js.JsConsole().log(dt.getDay()),
            Js.JsConsole().log(dt.getFullYear())])

        :param js_funcs: The Javascript fragments

        :return: The File object
        """
        self.__data.extend(jsConvertFncs(js_funcs))
        return self

    def writeReport(self, page: primitives.PageModel):
        """Write the Javascript content of a report to a structure .js file.
        This could help on the investigation and can be directly used in Codepen for testing.

        :param primitives.PageModel page: The report object
        """
        props = page._src._props if hasattr(page, '_src') else page._props
        for data_id, data in props.get("data", {}).get('sources', {}).items():
            self.__data.append("var data_%s = %s" % (data_id, json.dumps(data)))

        for k, v in props.get('js', {}).get('functions', {}).items():
            s_pmt = "(%s)" % ", ".join(list(v["pmt"])) if "pmt" in v else "{}"
            self.__data.append("function %s%s{%s}" % (k, s_pmt, v["content"].strip()))

        for c, d in props.get('js', {}).get("constructors", {}).items():
            self.__data.append(d)

        for c, d in props.get('js', {}).get("datasets", {}).items():
            self.__data.append(d)

        for b in props.get('js', {}).get("builders", []):
            self.__data.append(b)

        keyboard_shortcuts = props.get('js', {}).get('keyboard', {})
        if keyboard_shortcuts:
            self.__data.append("document.addEventListener('keydown', function(e){var code = e.keyCode || e.which")
            for k, v in keyboard_shortcuts.items():
                self.__data.append("if(%s){%s}" % (k, v))
            self.__data.append("})")

    def codepen(self, js_base: Any, css_obj: primitives.CssClsModel = None, target: str = '_self'):
        """Send the piece of Javascript to Codepen for testing.

        `codepen <https://codepen.io/>`_

        :param js_base: A Js or out Browser object
        :param css_obj: The internal CSS object from the page
        :param target: A string flag to specify the target page in the browser
        """
        import webbrowser

        if hasattr(js_base, '_to_html_obj'):
            results = js_base._to_html_obj(content_only=True)
            js_external = re.findall('<script language="javascript" type="text/javascript" src="(.*?)"></script>',
                                     results['jsImports'])
            result = {"js": results["jsFrgs"], "js_external": ";".join(js_external)}
        else:
            self.writeReport(js_base)
            import_obj = Imports.ImportManager()
            import_obj.online = True
            css_external = import_obj.cssURLs(import_obj.cssResolve(js_base.page.cssImport))
            js_external = import_obj.jsURLs(import_obj.jsResolve(js_base.page.jsImports))
            result = {"js": ";".join(self.__data), "js_external": ";".join(js_external),
                      "css_external": ";".join(css_external)}
        if css_obj is not None:
            result["css"] = str(css_obj)
        data = js_base.location.postTo("https://codepen.io/pen/define/", {"data": json.dumps(result)}, target=target)
        out_file = open(os.path.join(self.file_path, "CodePenJsLauncher.html"), "w")
        out_file.write('<html><body></body><script>%s</script></html>' % data.replace("\\\\n", ""))
        webbrowser.open(out_file.name)

    def close(self, js_obj=None) -> str:
        """Write the file and close the buffer.

        :param js_obj: The internal JsObject
        """
        src_obj = js_obj.page if hasattr(js_obj, 'page') else js_obj
        out_file = open(os.path.join(self.file_path, "%s.js" % self.script_name), "w")
        js_external = ""
        if js_obj is not None:
            out_file.write("//Javascript Prototype extensions \n\n")
            for fnc, details in src_obj._props.get('js', {}).get('prototypes', {}).items():
                out_file.write("%s = function(%s){%s};" % (fnc, ",".join(details.get('pmts', [])), details["content"]))
            out_file.write("\n\n//Javascript Global functions \n\n")
            for fnc, details in src_obj._props.get('js', {}).get('functions', {}).items():
                out_file.write("function %s(%s){%s}" % (fnc, ",".join(details.get('pmt', [])), details["content"]))
            import_obj = Imports.ImportManager()
            import_obj.online = True
            js_external = import_obj.jsResolve(src_obj.jsImports)
        out_file.write("\n\n")
        out_file.write("//Javascript Data\n\n")
        for data_id, data in src_obj._props.get("data", {}).get('sources', {}).items():
            out_file.write("var data_%s = %s" % (data_id, json.dumps(data)))
        out_file.write("\n\n")
        out_file.write("//Javascript functions\n\n")
        if len(src_obj._props.get('js', {}).get('onReady', [])) > 0:
            out_file.write("%s;" % jsConvertFncs(src_obj._props.get('js', {}).get('onReady', []), toStr=True))
        out_file.write(";".join(self.__data))
        out_file.close()
        with open(r"%s\Launche_%s.html" % (self.path, self.script_name), "w") as f:
            f.write('<html><head></head><body></body>%s<script src="js/%s.js"></script></html>' % (
                js_external, self.script_name))
        return r"%s\Launche_%s.html" % (self.path, self.script_name)


def urlInputs(key: str, dflt: str = "") -> JsObject.JsObject:
    """Helper to get variable from the url input.

    :param key: The key to extract from the url.
    :param dflt: The default value to set if not defined
    """
    return JsObject.JsObject.get('''(function(key, dflt){
const urlParams = new URLSearchParams(window.location.search); return urlParams.get(key)  || dflt })(%s, %s)''' % (
    jsConvertData(key, None), jsConvertData(dflt, None)))


def addJsResources(constructors: dict, file_nam: str, sub_folder: str = None, full_path: str = None,
                   required_funcs: List[str] = None) -> bool:
    """Add chained resources to the page.
    required_funcs must be defined in the internal treemap mapping to be added to the JavaScript resources.
    If it is a bespoke mapping definition the function `ek.treemap_add` must be used.

    :param constructors; Global constructor
    :param file_nam; JavaScript filename (with the extension_
    :param sub_folder; The sub folder for relative path definition
    :param full_path; The full path for absolute path definition
    :param required_funcs: List of required functions defined in the treemap
    """
    possible_paths = []
    if global_settings.PRIMARY_RESOURCE_PATHS:
        possible_paths.extend(global_settings.PRIMARY_RESOURCE_PATHS)
    if global_settings.NATIVE_JS_PATH:
        possible_paths.append(global_settings.NATIVE_JS_PATH)
    if sub_folder is not None:
        possible_paths.append(Path(Path(__file__).resolve().parent, "..", "js", "native", sub_folder))
    else:
        possible_paths.append(Path(Path(__file__).resolve().parent, "..", "js", "native"))
    if required_funcs:
        for req in required_funcs:
            if req in treemap._FUNCTIONS_MAP:
                f = treemap._FUNCTIONS_MAP[req]
                addJsResources(
                    constructors, f["file"], sub_folder=f.get("folder"), full_path=f.get("path"),
                    required_funcs=f.get("required_funcs"))
            else:
                logging.warn("NATIVE | JS | Definition not found for %s - use ek.treemap_add" % req)
    if full_path:
        js_file = Path(full_path, file_nam)
        if js_file.exists():
            with open(js_file) as fp:
                constructors[file_nam] = fp.read()
    else:
        for p in possible_paths:
            js_file = Path(p, file_nam)
            if js_file.exists():
                with open(js_file) as fp:
                    constructors[file_nam] = fp.read()
                return True
        else:
            logging.warn("NATIVE | JS | File not loaded %s" % file_nam)

    return False
