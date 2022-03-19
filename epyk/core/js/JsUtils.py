#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import json
import functools
from typing import Union, Optional, List, Any
from epyk.core.py import primitives

from epyk.core.js import Imports
from epyk.core.js.primitives import JsObject

PROFILE_COUNT = 0


# --------------------------------------------------------------------------------------------------------------
#                                                       DECORATORS
#
def incompatibleBrowser(browsers: List[str]):
  """
  Description:
  ------------
  Decorator to send a warning for functions or packages which are restricted to some browsers.

  Attributes:
  ----------
  :param List[str] browsers: Incompatible browsers.
  """
  def decorator(func):
    @functools.wraps(func)
    def decorated(*args, **kwargs):
      print("Warning: This function - %s - is not compatible with %s" % (func.__name__, ", ".join(browsers)))
      return func(*args, **kwargs)

    return decorated

  return decorator


def fromVersion(data: dict):
  """
  Description:
  ------------
  This system decorate will decorate a component function to specify during the Python execution
  if a method is not yet available in the current state of the Javascript modules.

  Usage::

    .fromVersion({'jqueryui': '1.12.0'})

  Attributes:
  ----------
  :param dict data: Set the minimum version of a package for a specific function.

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
  """
  Description:
  ------------
  This system decorate will decorate a component function to specify during the Python execution
  if a method is not available since the current state of the Javascript modules.
  Indeed as it is possible to override JS version on the fly it is also important to get notify with functions
  are not compatible anymore.
  This decorator will also propose an alternative with the new feature to.

  Usage::

      .untilVersion({'jqueryui': '1.12.0'}, "new function")

  Attributes:
  ----------
  :param dict data: The maximum version number for a function by packages.
  :param str new_feature: The new function name.

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
  """
  Description:
  ------------
  Common function to check if the object exists in Python.

  Usage::

     JsUtils.isJsData(attr)

  Attributes:
  ----------
  :param js_data: The Python Javascript data.
  """
  return hasattr(js_data, 'toStr')


def jsConvertData(js_data: Union[str, primitives.JsDataModel, float, dict, list], js_funcs: Optional[Union[list, str]],
                  depth: bool = False) -> str:
  """
  Description:
  ------------
  Generic conversion function for any data in the internal framework.
  This will convert to String any data coming from the Javascript Python interface.

  Any pure Python object will be converted using the json function to be then written as a string
  to the resulting page.

  Attributes:
  ----------
  :param Union[str, primitives.JsDataModel, float, dict, list] js_data: The Python Javascript data.
  :param Optional[Union[list, str]] js_funcs: Optional. The conversion function (not used).
  :param bool depth: Optional. Set to true of it is a nested object.
  """
  if not hasattr(js_data, 'varData') and not hasattr(js_data, 'fncName'):
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
  Description:
  ------------


  Attributes:
  ----------
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


def jsWrap(data: Any):
  """
  Description:
  ------------
  Shortcut to wrap a python object to a generic JavaScript object.
  This will avoid the automatic conversion to string if it is a variable.

  Attributes:
  ----------
  :param Any data: Object. A python object to be serialised.
  """
  return JsObject.JsObject.get(data)


def getJsValid(value: str, fail: bool = True):
  """
  Description:
  ------------
  Return an error if the variable name is not valid following the Javascript naming conventions.
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

  Related Pages:

      https://www.w3schools.com/js/js_conventions.asp

  Attributes:
  ----------
  :param str value: The Javascript variable name.
  :param bool fail: Optional. Flat to raise an exception if the name is not valid on the Javascript side.

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


def jsConvertFncs(js_funcs: Union[List[Union[str, primitives.JsDataModel]], str], is_py_data: bool = False,
                  jsFncVal=None, toStr: bool = False, profile: Optional[Union[bool, dict]] = False):
  """
  Description:
  ------------
  Generic conversion function for all the PyJs functions.

  Attributes:
  ----------
  :param Union[List[Union[str, primitives.JsDataModel]], str] js_funcs: The PyJs functions.
  :param bool is_py_data: Optional. A flag to force the Python conversion using json.
  :param jsFncVal:
  :param bool toStr: Optional. A flag to specify if the result should be aggregated.
  :param Optional[Union[bool, dict]] profile. Optional.
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
  """
  Description:
  ------------
  Try to remove as much as possible all the characters in order to speed up the javascript
  Indeed most of the browsers are using minify Javascript to make the page less heavy.

  Thus pre-stored function code can be written to be easier to read.

  Attributes:
  ----------
  :param fnc: The Javascript String.

  :return: Return a cleaned a minify Javascript String.
  """
  return "".join([r.strip() for r in fnc.strip().split('\n')])


def isNotDefined(varName: str):
  """
  Description:
  ------------
  Check if a variable is defined.

  Usage::

    JsUtils.isNotDefined(varId)

  Attributes:
  ----------
  :param str varName: The varName.

  :return: A string in Python and a Boolean in Javascript.
  """
  return "typeof %s === 'undefined'" % varName


class JsFile:

  def __init__(self, script_name: Optional[str] = None, path: Optional[str] = None):
    self.script_name, self.path = script_name, path
    self.file_path = os.path.join(path, "js") # all the files will be put in a common directory
    if not os.path.exists(self.file_path):
      os.mkdir(self.file_path)
    self.__data = []

  def writeJs(self, js_funcs: Union[list, str]):
    """
    Description:
    ------------
    Write the Javascript piece of code to the file.

    Usage::

      dt = JsDate.new("2019-05-03")
      f.writeJs([dt,
        Js.JsConsole().log(dt.getDay()),
        Js.JsConsole().log(dt.getFullYear())])

    Attributes:
    ----------
    :param Union[list, str] js_funcs: The Javascript fragments.

    :return: The File object
    """
    self.__data.extend(jsConvertFncs(js_funcs))
    return self

  def writeReport(self, page: primitives.PageModel):
    """
    Description:
    ------------
    Write the Javascript content of a report to a structure .js file.
    This could help on the investigation and can be directly used in Codepen for testing.

    Attributes:
    ----------
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
    """
    Description:
    ------------
    Send the piece of Javascript to Codepen for testing.

    Related Pages:

      https://codepen.io/

    Attributes:
    ----------
    :param Any js_base: A Js or out Browser object.
    :param primitives.CssClsModel css_obj: The internal CSS object from the page.
    :param str target: A string flag to specify the target page in the browser.
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

  def close(self, js_obj=None):
    """
    Description:
    ------------
    Write the file and close the buffer.

    Attributes:
    ----------
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
