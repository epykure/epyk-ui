"""

TODO: Split the component_properties class attribute into two decorators
TODO: Change the model to get Option as an interface of two sub classes .js and .html to remove the _config...

@js_option =>  self._report._jsStyles
@html_option =>  self._attrs
"""

import sys
import json

from typing import Any, Union, List
from epyk.core.py import primitives

from epyk.core.data.DataClass import DataClass
from epyk.core.js import JsUtils


class Options(DataClass):
    component_properties = ()
    with_builder = True
    _struct__schema = None

    def __init__(self, component: primitives.HtmlModel, attrs: dict = None, options: dict = None, js_tree: dict = None,
                 page: primitives.PageModel = None):
        super(Options, self).__init__(component, attrs, options, page=page)
        self.js_type, self.__config_sub_levels, self.__config_sub__enum_levels = {}, set(), set()
        self.value_enums = {}
        # By default, it is the component dictionary
        self.js_tree = self.component._jsStyles if js_tree is None else js_tree
        self.js = None
        # Set the default options for a component
        for c in self.component_properties:
            setattr(self, c, getattr(self, c))
        if attrs is not None:
            for k, v in attrs.items():
                if hasattr(self, k):
                    self._try_setattr(self, k, v)
                else:
                    self.js_tree[k] = v

    def _try_setattr(self, opt, field, value):
        """Try to set a specific value for a given field to the option definition.

        :param opt: Option object
        :param field: option field to be set
        :param value: value to set for the specified field
        """
        try:
            setattr(opt, field, value)
        except AttributeError:
            if isinstance(value, dict):
                new_opt = getattr(opt, field)
                for k, v in value.items():
                    self._try_setattr(new_opt, k, v)

    def set_defaults(self, attrs_path: List[tuple]):
        """
        Set default attributes for a given component.

        Usage::

          c = page.ui.charts.highcharts.line(y_columns=["rating", 'change'], x_axis='index')
          c.options.set_defaults([("chart", "options3d", "enabled")])

        :param attrs_path: Attributes / Options path
        """
        for attr_path in attrs_path:
            opt = self
            for k in attr_path[:-1]:
                if not hasattr(opt, k):
                    break

                opt = getattr(opt, k)
            else:
                setattr(opt, attr_path[-1], getattr(opt, attr_path[-1]))

    def set_attrs(self, vals: dict):
        """Set the object internal attributes.

        :param vals: All the attributes to be added to the component
        """
        self.js_tree.update(vals)

    def from_json(self, vals: dict, schema: dict = None):
        """Load the option schema for a component from a json string.

        TODO: add more feature to handle functions and enumeration

        :param vals: The input schema
        :param schema: The full object schema
        """
        if schema is None:
            schema = self._struct__schema
        for k, v in vals.items():
            if hasattr(self, k):
                if schema is not None and k in schema:
                    prop = getattr(self, k, schema[k])
                    prop.from_json(v)
                else:
                    setattr(self, k, v)
            else:
                self._config(v, k, hasattr(v, "toStr"))

    def rset(self, vals: dict, js_check: bool = True):
        """Recursive options setter

        :param vals: The input schema
        :param js_check: Flag to automatically check the JavaScript expression starting with function
        """

        def deep_set(object, rval: dict):
            for k, v in rval.items():
                if hasattr(object, k):
                    if isinstance(v, dict):
                        sub_object = getattr(object, k)
                        if issubclass(sub_object.__class__, Options):
                            deep_set(sub_object, v)
                        else:
                            setattr(object, k, v)
                    else:
                        if js_check and isinstance(v, str) and v.startswith("function"):
                            setattr(object, k, JsUtils.jsWrap(v))
                        else:
                            setattr(object, k, v)
                else:
                    object._config(v, k)

        deep_set(self, vals)

    def remove(self, name: str = None) -> bool:
        """Remove a field from the option configuration if it exists.

        :param name: Optional. The attribute name
        """
        name = name or sys._getframe().f_back.f_code.co_name
        if name in self.js_tree:
            del self.js_tree[name]
            return True

        return False

    def _config_get(self, dflt: Any = None, name: str = None):
        """Get the option attribute to be added on the Javascript side during the component build.

        Unlike the usual get from dict this method will take the default value as first parameter as
        the name is by default the property name using it.

        :param dflt: Optional. The default value for this category
        :param name: Optional. The attribute name (default the function property)
        """
        return self.js_tree.get(name or sys._getframe().f_back.f_code.co_name, dflt)

    def _config(self, value: Any, name: str = None, js_type: bool = False):
        """
        Set the option attribute to be added on the Javascript side during the component build.

        This method take the value as first parameter because the name is by default the property name if
        not defined. Very often the only information to supply if the value.

        :param Any value: The value for the name
        :param name: Optional. The attribute name. Default is the property name
        :param js_type: Optional. Specify if the parameter is a JavaScript fragment
        """
        self.js_tree[name or sys._getframe().f_back.f_code.co_name] = value
        if js_type:
            self.js_type[name or sys._getframe().f_back.f_code.co_name] = True

    def _config_func(self, js_funcs, profile = None, func_ref: bool = False, name: str = None, append: bool = True,
                     params_expr = "param"):
        """
        Add a JavaScript expression to the configuration.

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param func_ref: Optional. Specify if js_funcs point to an external function
        :param name: Optional. The attribute name. Default is the parent function name
        :param append: Optional.
        :param params_expr: Optional. String with the list of arguments for the JavaScript callback
        """
        name = name or sys._getframe().f_back.f_code.co_name
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
        if self.js_tree.get(name) is not None and append:
            opt_func = self.js_tree[name]
            self.js_tree[name] = opt_func[:-1] + ";" + str_func + "}"
        else:
            if not str_func.startswith("function(%s)" % params_expr) and not func_ref:
                str_func = "function(%s){%s}" % (params_expr, str_func)
            self._config(str_func, js_type=True, name=name)

    def _config_group_get(self, group: str, dflt: Any = None, name: str = None):
        """
        Get second level configuration options.

        :param group: The group attribute name
        :param dflt: Optional. The group default value
        :param name: Optional. The attribute name
        """
        return self.js_tree.get(group, {}).get(name or sys._getframe().f_back.f_code.co_name, dflt)

    def _config_group(self, group: str, value: Any, name: str = None):
        """
        Set second level configuration options.

        :param group: The group name
        :param value: The value for the name
        :param name: Optional. The attribute name
        """
        if group not in self.js_tree:
            self.js_tree[group] = {}
        self.js_tree[group][name or sys._getframe().f_back.f_code.co_name] = value

    def _config_sub_data(self, name: str, clsObj=None):
        """
        Create a nested structure for the JavaScript configuration layer.

        This is required for Charts and Tables configurations.

        :param name: The key to be added to the internal data dictionary
        :param clsObj: Options. The object which will be added to the nested data structure
        """
        if name in self.js_tree:
            return self.js_tree[name]

        self.__config_sub_levels.add(name)
        if clsObj is None:
            clsObj = Options
        self.js_tree[name] = clsObj(self.component, js_tree={})
        return self.js_tree[name]

    def _config_sub_data_enum(self, name: str, cls_obj=None):
        """
        Add sub group with enumeration.

        :param name: The key to be added to the internal data dictionary
        :param cls_obj: Class. Object. The object which will be added to the nested data structure
        """
        if cls_obj is None:
            cls_obj = Enums
        if issubclass(cls_obj, Enums):
            enum_data = cls_obj(self, name=name, js_tree={})
        else:
            self.__config_sub__enum_levels.add(name)
            enum_data = cls_obj(self.component, js_tree={})
            self.js_tree.setdefault(name, []).append(enum_data)
        return enum_data

    def update_config(self, attrs: dict):
        """
        Update the option configuration.

        :param attrs: The attributes to set
        """
        for k, v in attrs.items():
            if hasattr(self, k):
                setattr(self, k, v)
            else:
                self._config(v, name=k)
        return self

    def custom_config(self, name: str, value: Any, js_type: bool = False):
        """
        Add a custom JavaScript configuration.

        Usage::

          chart = page.ui.charts.apex.scatter()
          chart.options.chart.zoom.custom_config("test", False)

        :param name: The key to be added to the attributes
        :param value: String or JString. The value of the defined attributes
        :param js_type: Optional. Specify if the parameter is a JavaScript fragment
        """
        if js_type:
            self.js_type[name] = True
        self.js_tree[name] = value
        return self

    def isJsContent(self, property_name: str):
        """
        Check if the content of a property is defined to always be a JavaScript fragment.

        Thus the framework will not convert it to a Json content.

        Usage::

          div = page.ui.div()
          print(div.options.isJsContent("inline"))

        :param property_name: The property name
        """
        return self.js_type.get(property_name, False)

    def has_attribute(self, cls_obj, name: str = None):
        """
        Add an extra sub layer to the data structure.

        The key in the object representation will be the function name.

        :param cls_obj: Class. The sub data class used in the structure definition
        :param name: The sub attribute name
        """
        name = name or sys._getframe().f_back.f_code.co_name
        if issubclass(cls_obj, Enums):
            self.__config_sub_levels.add(name)
            return self._config_sub_data_enum(name, cls_obj)

        return self.sub_data(name, cls_obj)

    @property
    def managed(self):
        """
        Boolean flag to set if the component needs to be added to the page.

        If set to False the component has to be managed manually in the page.

        Usage::

          but = page.ui.button()
          but.options.managed = False

        :prop bool: Flag to specify if this component is automatically managed by the page
        """
        return self.get(True)

    @managed.setter
    def managed(self, flag: bool):
        self.set(flag)

    @property
    def verbose(self):
        """
        Boolean flag to set if extra logs need to be displayed.

        This could help in debugging, default is the page verbose flag (default is false).

        Usage::

          but = page.ui.button()
          but.options.verbose = True

        :prop flag: Boolean. Flag to display / hide warning logs generated by the framework.
        """
        return self.get(self.component.page.verbose)

    @verbose.setter
    def verbose(self, flag: bool):
        self.set(flag)

    @property
    def profile(self):
        """
        Boolean flag to set if extra logs need to be displayed.

        This could help in debugging, default is the page verbose flag (default is false).

        Usage::

          but = page.ui.button()
          but.options.verbose = True

        :prop flag: Flag to display / hide warning logs generated by the framework.
        """
        return self.get(self.component.page.verbose)

    @profile.setter
    def profile(self, flag: bool):
        self.set(flag)

    @property
    def builder(self):
        """
        Add a JavaScript Builder function to the options.

        This will be used to automatically map the Python component to its corresponding JavaScript builder
        function used by the build method.

        Usage::

          but = page.ui.button()
          but.options.builder = "Button"

        :prop value: The JavaScript builder function name.
        """
        return self._config_get(None)

    @builder.setter
    def builder(self, value: Union[str, primitives.JsDataModel]):
        if self.with_builder:
            self.js_type["builder"] = True
            if hasattr(value, "toStr"):
                value = value.toStr()
            self._config(value)

    @property
    def style(self):
        """
        Change some CSS attributes to the internal HTML component.

        Related Pages:

          https://www.w3schools.com/cssref/

        :prop values: The CSS attributes.
        """
        return self._config_get({})

    @style.setter
    def style(self, values: dict):
        self._config(values)

    @property
    def config_default(self):
        """
        The default value for the configuration in case of template.

        Default value is an empty string.

        Usage::

          component.options.config_default = {"value": "test"}
        """
        return self.get("")

    @config_default.setter
    def config_default(self, values: dict):
        self.set(values)

    def details(self):
        """
        Retrieve the defined properties details.

        This function will return a dictionary with all the component attributes (required and optional) ones.
        It will provide the full available description of those components.

        Usage::

          but = page.ui.button()
          pprint.pprint(but.options.details(), indent=4)
        """
        prop_details = {}
        for prop_name in self.component_properties:
            prop = getattr(self, prop_name)
            prop_details[prop_name] = {
                "type": 'mandatory', "name": prop_name, 'value': prop,
                'doc': getattr(self.__class__, prop_name).__doc__}

        # Add the value of the system attributes
        prop_details["verbose"] = {"name": "verbose", "value": self.verbose, "type": "system"}
        prop_details["managed"] = {"name": "managed", "value": self.managed, "type": "system"}
        for k, v in vars(self.__class__).items():
            if k not in prop_details and isinstance(v, property):
                prop_details[k] = {
                    "type": 'optional', "name": k, 'value': getattr(self, k), 'doc': getattr(self.__class__, k).__doc__}
        return prop_details

    def required(self):
        """
        Return all the mandatory / required options with the default values.

        Those options are added by the framework to provide a default for the HTML components but they can be changed.

        System options are also added to this category as they are always available in any HTML components.

        To get the full definition of options the details method should be used.

        Usage::

          but = page.ui.button()
          pprint.pprint(but.options.required(), indent=4)
        """
        props = self.details()
        result = [v for k, v in props.items() if v["type"] != "optional"]
        return result

    def optional(self):
        """
        Return all options not added to the HTML component by default.

        Those are options which will impact either the Python or the JavaScript builders.

        To get the full definition of options the details method should be used.

        Usage::

          but = page.ui.button()
          pprint.pprint(but.options.optional(), indent=4)
        """
        props = self.details()
        result = [v for k, v in props.items() if v["type"] == "optional"]
        return result

    def config_js(self, attrs: dict = None):
        """
        Return the JavaScript options used by the builders functions.

        Builder functions can be defined in the framework or external from the various packages.

        The returned dictionary is a copy so it can be changed or used in other processes.
        To change the internal component property, the options property should be used.

        :param attrs: Optional. The extra or overridden options
        """

        def _process_sub_items(v: dict) -> str:
            """ Allow recursive check for sub components """
            items = []
            for sk, sv in v.items():
                if isinstance(sv, dict):
                    items.append("%s: %s" % (sk, _process_sub_items(sv)))
                elif hasattr(sv, 'toStr'):
                    items.append("%s: %s" % (sk, JsUtils.jsConvertData(sv, None)))
                else:
                    items.append("%s: %s" % (sk, json.dumps(sv)))
            return "{%s}" % ",".join(items)

        js_attrs, attrs = [], attrs or {}
        if self.__config_sub_levels:
            tmp_tree = dict(self.js_tree)
            for k, v in attrs.items():
                if k not in tmp_tree:
                    tmp_tree[k] = v
            for k, v in tmp_tree.items():
                if k in self.value_enums:
                    v = self.value_enums[k].join(v)
                if k not in self.value_enums and k in self.__config_sub_levels:
                    js_attrs.append("%s: %s" % (k, v.config_js(attrs=attrs.get(k, {})).toStr()))
                elif k in self.__config_sub__enum_levels:
                    js_attrs.append(
                        "%s: [%s]" % (k, ", ".join([s.config_js(attrs=attrs.get(k, {})).toStr() for s in v])))
                else:
                    if k in attrs:
                        if hasattr(attrs[k], "toStr"):
                            v = attrs[k].toStr()
                            self.js_type[k] = True
                        else:
                            v = attrs[k]
                    if k in self.js_type or hasattr(v, 'toStr'):
                        # Improve this when all options are moved to the js_type model
                        if v is None:
                            js_attrs.append("%s: %s" % (k, json.dumps(v)))
                        elif hasattr(v, 'toStr'):
                            js_attrs.append("%s: %s" % (k, JsUtils.jsConvertData(v, None)))
                        else:
                            js_attrs.append("%s: %s" % (k, v))
                    else:
                        if isinstance(v, dict):
                            js_attrs.append("%s: %s" % (k, _process_sub_items(v)))
                        else:
                            js_attrs.append("%s: %s" % (k, json.dumps(v)))
            return JsUtils.jsWrap("{%s}" % ", ".join(js_attrs))

        tmp_tree = dict(self.js_tree)
        if not JsUtils.isJsData(attrs):
            tmp_tree.update(attrs)
        for k, v in tmp_tree.items():
            if k in self.js_type:
                js_attrs.append("%s: %s" % (k, v))
            elif hasattr(v, 'toStr'):
                js_attrs.append("%s: %s" % (k, v.toStr()))
            else:
                if k in self.__config_sub__enum_levels:
                    js_attrs.append(
                        "%s: [%s]" % (k, ", ".join([s.config_js(attrs=attrs.get(k, {})).toStr() for s in v])))
                else:
                    js_attrs.append("%s: %s" % (k, json.dumps(v)))

        if JsUtils.isJsData(attrs):
            return JsUtils.jsWrap(
                "Object.assign({}, {%s}, %s)" % (", ".join(js_attrs), JsUtils.jsConvertData(attrs, None)))

        return JsUtils.jsWrap("{%s}" % ", ".join(js_attrs))

    def config_html(self):
        """
        Return the HTML options used by the python and passed to the HTML.

        Those options will not be available in the JavaScript layer and they are only defined either
        to build the HTML from Python or to set some HTML properties.

        The returned dictionary is a copy so it can be changed or used in other processes.
        To change the internal component property, the options property should be used.
        """
        html_attrs = {}
        for k, v in self._attrs.items():
            if k not in self.js_tree:
                html_attrs[k] = v
        return html_attrs

    def __str__(self):
        return str(self.config_js())


class Enums:
    delimiter = None
    js_conversion = False

    def __init__(self, options: Options, name: str, js_tree: bool = None,
                 page: primitives.PageModel = None):
        self.__option = options
        self.component = options.component
        self.page = page or options.component.page
        self.__name = name

    @property
    def key(self):
        """ Returns the predefined enumeration key which will be added with this object. """
        return self.__name

    @property
    def item(self):
        """ Return the option object on which the key, value will be added. """
        return self.__option

    def _set_value(self, name: str = None, value: Any = None, js_type: bool = None):
        """
        Set the option value for a class with different functions.

        This function should be derived in the various package options to create static and documented enumerations.

        :param name: Optional. The key to be added to the attributes
        :param value: Optional. The value to be added to the attributes
        :param js_type: Optional. Specify if the parameter is a JavaScript fragment
        """
        self.item._config(value or sys._getframe().f_back.f_code.co_name, name or self.__name)
        if js_type is not None:
            if js_type:
                self.__option.js_type[name or self.__name] = True
        elif self.js_conversion:
            self.__option.js_type[name or self.__name] = True
        return self

    def _add_value(self, name: str = None, value: str = None, js_type: bool = None):
        """

        :param name: Optional. The key to be added to the attributes
        :param value: Optional. The value to be added to the attributes
        :param js_type: Optional. Specify if the parameter is a JavaScript fragment
        """
        key = name or self.__name
        if key not in self.__option.js_tree:
            self.__option.js_tree[key] = []

        if js_type is None:
            js_type = self.js_conversion
        if js_type:
            self.__option.js_tree[key].append(value)
        else:
            self.__option.js_tree[key].append(JsUtils.jsConvertData(value, None))
        self.__option.value_enums[key] = self.delimiter
        return self


class OptionsWithTemplates(Options):

    @property
    def template(self):
        return self._config_get(None)

    @template.setter
    def template(self, value: str):
        self._config("function(data){return %s}" % value, js_type=True)

    @property
    def templateLoading(self):
        return self._config_get(None)

    @templateLoading.setter
    def templateLoading(self, value: str):
        self._config("function(data){return %s}" % value, js_type=True)

    @property
    def templateError(self):
        return self._config_get(None)

    @templateError.setter
    def templateError(self, value: str):
        self._config("function(data){return %s}" % value, js_type=True)
