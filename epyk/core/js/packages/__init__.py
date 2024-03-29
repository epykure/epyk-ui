import sys
from typing import Any, List, Tuple, Union, Optional
from epyk.core.py import primitives
from epyk.core.py import types

from epyk.core.js.primitives import JsString
from epyk.core.js.primitives import JsObjects
from epyk.core.js import JsUtils


def packageImport(js_package: str = None, css_package: str = None, if_true: bool = False):
    """
    Simple decorator to allow people to declare packages that need to be imported when they are manipulating
    HTML components. The alias for the package needs to be defined in the Import.py module.

    Usage::

      import epyk.core.js.packages
      @packageImport('myJsPackage', 'myCssPackage')
      def myHtmlComponent():
        pass

    :param js_package: Optional. JavaScript package alias
    :param css_package: Optional. CSS Package alias
    :param if_true: Optional. Add packages only if they exist in the internal definition
    """

    def wrap(func):
        def inner(page, *args, **kwargs):
            report = getattr(page, 'page') if getattr(page, 'page', None) else page
            add_package = True
            if if_true and not args[0]:
                add_package = False
            if add_package and js_package:
                report.jsImports.add(js_package)
            if add_package and css_package:
                report.cssImport.add(css_package)
            return func(page, *args, **kwargs)

        return inner

    return wrap


def from_version(current_versions: List[str], first_version: str, included: bool = True) -> Tuple[bool, str]:
    """
    Check a feature based on the package version.

    :usages:

      is_valid, msg = from_version(self.page.imports.pkgs.chart_js.version, "4")

    :param current_versions: The current versions defined for the package
    :param first_version: The first version for this package and feature
    :param included: Flag to specify how to consider the last version
    """
    split_vr = list(map(lambda x: int(x), first_version.split(".")))
    is_valid, msg = True, ""
    for vr in current_versions:
        vrs = list(map(lambda x: int(x), vr.split(".")))
        for i, r in enumerate(split_vr):
            if not included:
                if r <= vrs[i]:
                    if r == vrs[i]:
                        is_valid = False
                        msg = "cannot be used with version %s (min allowed: %s)" % (vr, first_version)
                    elif r < vrs[i]:
                        is_valid = True
                        msg = ""
                        continue

                    else:
                        return False, "cannot be used with version %s (min allowed: %s)" % (vr, first_version)

            if r > vrs[i]:
                return False, "cannot be used with version %s (min allowed: %s)" % (vr, first_version)

    return is_valid, msg


def until_version(current_versions: List[str], last_version: str, included: bool = False) -> Tuple[bool, str]:
    """
    Check a feature based on the package version.

    :usages:

      is_valid, msg = until_version(self.page.imports.pkgs.chart_js.version, "4")

    :param current_versions: The current versions defined for the package
    :param last_version: The last version for this package and feature
    :param included: Flag to specify how to consider the last version
    """
    split_vr = list(map(lambda x: int(x), last_version.split(".")))
    is_valid, msg = True, ""
    for vr in current_versions:
        vrs = list(map(lambda x: int(x), vr.split(".")))
        for i, r in enumerate(split_vr):
            if not included:
                if r >= vrs[i]:
                    if r == vrs[i]:
                        is_valid = False
                        msg = "cannot be used with version %s (max allowed: %s)" % (vr, last_version)
                    elif r > vrs[i]:
                        is_valid = True
                        msg = ""
                        continue

                    else:
                        return False, "cannot be used with version %s (max allowed: %s)" % (vr, last_version)

            else:
                if r > vrs[i]:
                    return False, "cannot be used with version %s (max allowed: %s)" % (vr, last_version)

    return is_valid, msg


class JsPackage(primitives.JsDataModel):
    lib_alias, lib_selector, lib_set_var = None, None, True

    def __init__(self, component: primitives.HtmlModel = None, page: primitives.PageModel = None, js_code: str = None,
                 selector: str = None, data: Any = None, set_var: bool = None):
        self.component, self.page = component, page
        if page is None and component is not None:
            self.page = component.page
        self._selector = selector if selector is not None else self.lib_selector
        self.varName, self.setVar = js_code, self.lib_set_var if set_var is None else set_var
        self._data, self._container = data, self.element
        self._js, self._u, self._js_enums = [[]], {}, {}  # a list of lists of objects definition
        self.__js_uniq_fncs = {}
        if self.lib_alias is not None:
            if component is not None:
                if 'css' in self.lib_alias:
                    self.component.cssImport.add(self.lib_alias['css'])
                if 'js' in self.lib_alias:
                    self.component.jsImports.add(self.lib_alias['js'])
            elif self.page is not None:
                if 'css' in self.lib_alias:
                    self.page.cssImport.add(self.lib_alias['css'])
                if 'js' in self.lib_alias:
                    self.page.jsImports.add(self.lib_alias['js'])

    def add_to_imports(self):
        """
        Base function to force the package to be added to the imports.
        This can be used when module is required in some plain JavaScript text and not wrapped within an internal function.
        """
        ...

    @property
    def container(self):
        """ Return the container level for the HTML component """
        if self.component is not None:
            return self._container

    @property
    def element(self):
        """ Return always the real DOM element. """
        if self.component is not None:
            return "document.getElementById(%s)" % JsUtils.jsConvertData(self.component.html_code, None)

    @property
    def varId(self):
        """ The Javascript and Python reference ID. """
        return self._selector if self.varName is None else self.varName

    def version(self, tag: str, js: dict = None, css: dict = None):
        """Change the package version number.

        Usage::

          bar.chart.version("1.11.0")

        :param tag: The package versions example 1.11.0
        :param js: Optional. The JavaScript packages to be added
        :param css: Optional. The CSS packages to be added
        """
        self.page.imports.setVersion(self.lib_alias, tag, js, css)
        return self

    def fnc(self, data: Any, unique: bool = False):
        """Base function to allow the object chain.

        This will add the elements to the current section in the object structure.
        All the items at the same level wil be chained.

        :param data: The Javascript fragment to be added
        :param unique: Ensure the function is available one time in the chain. If not the last call we will present

        :return: "Self" to allow the chains
        """
        if unique:
            fnc_name = data.split("(")[0]
            if fnc_name in self.__js_uniq_fncs:
                i, j = self.__js_uniq_fncs[fnc_name]
                self._js[i].pop(j)
            self.__js_uniq_fncs[fnc_name] = (len(self._js) - 1, self._js[-1])
        self._js[-1].append(data)
        return self

    def fnc_enum(self, name: str, data_class):
        """Base function to allow the creation of function with parameters which are list of dataclasses.
        Basically this will be then transpiled to a list of dictionary.

        :param name: The function Name
        :param data_class: The Python Data class
        """
        index = len(self._js) - 1
        if index not in self._js_enums:
            self._js_enums[index] = {name: []}
            self._js[-1].append(name)
        elif name not in self._js_enums[index]:
            self._js_enums[index][name] = []
            self._js[-1].append(name)
        self._js_enums[index][name].append(data_class(self.page))
        return self._js_enums[index][name][-1]

    def fnc_closure(self, data: str, check_undefined: bool = False, unique: bool = False):
        """Add the function string to the existing object definition but create a new entry point for the next ones.
        This structure will allow the chain on the Javascript side but also on the Python side.

        Thanks to this Python can always keep the same structure and produce the correct Javascript definition.
        There will be no chain in the Javascript side.

        :param data: The Javascript fragment to be added
        :param check_undefined: Add a check on the variable definition
        :param unique: Ensure the function is available one time in the chain. If not the last call we will present

        :return: The "self" to allow the chains
        """
        if unique:
            fnc_name = data.split("(")[0]
            if fnc_name in self.__js_uniq_fncs:
                i, j = self.__js_uniq_fncs[fnc_name]
                self._js[i].pop(j)
            self.__js_uniq_fncs[fnc_name] = (len(self._js) - 1, self._js[-1])

        self._js[-1].append(data)
        if check_undefined:
            self._u[len(self._js) - 1] = check_undefined
        self._js.append([])
        return self

    def fnc_closure_in_promise(self, data: str, check_undefined: bool = False):
        """Base function to allow the creation of a promise.

        A Js promise is an event attached toa function which will be only executed after the function.
        In case of success the then will be triggered otherwise the exception will be caught.

        :param data: The Javascript fragment to be added
        :param check_undefined: Add a check on the variable definition

        :return: The promise
        """
        self._js[-1].append(JsObjects.JsPromise(data))
        if check_undefined:
            self._u[len(self._js) - 1] = check_undefined
        self._js.append([])
        return data

    @property
    def var(self) -> JsString.JsString:
        """Property to return the variable name as a valid pyJs object."""
        return JsString.JsString(self.varId, is_py_data=False)

    def set_var(self, flag: bool):
        """Change the flag to define if the variable should be defined on the Javascript side.
        Default this is set to True.

        :param flag: A python boolean

        :return: This in order to allow js chains
        """
        self.setVar = flag
        return self

    def getStr(self, empty_stack: bool = True) -> str:
        """Get the current string representation for the object and remove the stack.

        :param empty_stack: Emtpy the various JavaScript fragments stored for this object
        """
        js_stack = None
        if not empty_stack:
            js_stack = list(self._js)
        content = self.toStr()
        if not empty_stack:
            self._js = js_stack
        if not content:
            return self.varId

        return content

    def _mapVarId(self, func: types.JS_FUNCS_TYPES, js_code: str):
        """Special function used for some external packages used to fix the problem of function override.
        Indeed in Datatable row.add is used as a class method compare to the other functions used at object level.

        :param func: The function string
        :param js_code: The object reference

        :return: The converted object reference
        """
        return js_code

    def custom(self, func_nam: str, *argv):
        """Generic function to call any missing function form a package.
        This will automatically convert the object to JavaScript and also put the right object reference.

        :param func_nam: The function name
        :param argv: Optional. The function arguments on the JavasScript side
        """
        js_args = []
        for arg in argv:
            js_args.append(str(JsUtils.jsConvertData(arg, None)))
        return JsObjects.JsObject.JsObject.get("%s.%s(%s)" % (self.varId, func_nam, ", ".join(js_args)))

    def callback_data(self, data, keys, js_funcs, comparator: Union[dict, str] = None, html_codes: List[str] = None,
                      profile: Optional[Union[bool, dict]] = None) -> types.JS_EXPR_TYPES:
        """JavaScript's expression to define a data callback function.

        :param data: The data object
        :param keys: The keys / depth structure within the object
        :param js_funcs: The callback methods if
        :param comparator: Optional. The comparator rule. By default, it will just check if key exist
        :param html_codes: Optional. The components required to run the expression
        :param profile: Optional. Set to true to get the profile for the function on the Javascript console
        """
        if self.page is None:
            return ""

        return self.page.js.callback_data(data, keys, js_funcs, comparator, html_codes, profile)

    def toStr(self) -> str:
        """Javascript representation """
        if self._selector is None:
            raise ValueError("Selector not defined, use this() or new() first")

        obj_content = []
        # TODO find better way to check emtpy js structure
        if self._js != [[]]:
            for i, js in enumerate(self._js):
                if len(js) == 0:
                    continue

                fnc_frg = []
                for d in js:
                    if hasattr(d, "toStr"):
                        fnc_frg.append(d.toStr())
                    else:
                        if i in self._js_enums and d in self._js_enums[i]:
                            fnc_frg.append("%s([%s])" % (d, ",".join([str(s) for s in self._js_enums[i][d]])))
                        else:
                            fnc_frg.append(d)
                str_fnc = ".".join(fnc_frg)
                if self.setVar:
                    if str_fnc:
                        str_fnc = "var %s = %s.%s" % (self.varId, self._selector, str_fnc)
                    else:
                        str_fnc = "var %s = %s" % (self.varId, self._selector)
                    self.setVar = False
                else:
                    if str_fnc:
                        if i in self._u:  # to avoid raising an error when the variable is not defined
                            str_fnc = "if(%s !== undefined){%s.%s}" % (self.varId, self.varId, str_fnc)
                        else:
                            str_fnc = "%s.%s" % (self._mapVarId(str_fnc, self.varId), str_fnc)
                    else:
                        str_fnc = self.varId
                obj_content.append(str_fnc)
        else:
            if self.setVar:
                obj_content = ["var %s = %s" % (self.varId, self._selector)]
                self.setVar = False
            else:
                obj_content.append(self.varId)
        self._js = [[]]  # empty the stack
        return "; ".join(obj_content)


class DataAttrs(primitives.JsDataModel):

    def __init__(self, page: primitives.PageModel, attrs: dict = None, options: dict = None):
        self.page, self.options, self._attrs = page, options, attrs or {}

    def custom(self, name: str, value: types.JS_DATA_TYPES):
        """
        Custom function to add a bespoke attribute to a class.

        This entry point will not be able to display any documentation but it is a shortcut to test new features.
        If the value is a Javascript object, the PyJs object must be used.

        :param name: The key to be added to the attributes
        :param value: The value of the defined attributes

        :return: The DataAttrs to allow the chains
        """
        self._attrs[name] = JsUtils.jsConvertData(value, None)
        return self

    def attr(self, name: str, value: Any):
        """
        Add an attribute to the Javascript underlying dictionary.

        :param name: The attribute name.
        :param value: The attribute value.

        :return: "Self" to allow the chains on the Python side
        """
        self._attrs[name] = value
        return self

    def attrs(self, values: dict):
        """
        Set multiple attributes to the underlying data directly from a dictionary.

        :param values: The data to set

        :return: "Self" to allow the chains on the Python side
        """
        self._attrs.update(values)
        return self

    def set_val(self, value: Any, name: str = None, js_type: bool = False):
        """
        Default way to set values for properties.

        This will manage functions in the case of callback within strings.

        :param value: The property value
        :param name: The property name
        :param js_type: For the process to consider the value as JavaScript
        """
        if (hasattr(value, "startswith") and value.startswith("function(")) or js_type:
            value = JsUtils.jsWrap(value)
        self.attr(name or sys._getframe().f_back.f_code.co_name, value)

    def __str__(self):
        """ Produce the resulting string to be added to the Javascript section of the web page. """
        return "{%s}" % ", ".join(["%s: %s" % (k, v) for k, v in self._attrs.items()])

    def toStr(self) -> str:
        """ Serialise the object. """
        return "{%s}" % ", ".join(["%s: %s" % (k, JsUtils.jsConvertData(v, None)) for k, v in self._attrs.items()])
