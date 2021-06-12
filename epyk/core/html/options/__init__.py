"""

TODO: Split the component_properties class attribute into two decorators
TODO: Change the model to get Option as an interface of two sub classes .js and .html to remove the _config...

@js_option =>  self._report._jsStyles
@html_option =>  self._attrs
"""

import sys
import json

from epyk.core.data.DataClass import DataClass
from epyk.core.js import JsUtils


class Options(DataClass):
  component_properties = ()

  def __init__(self, report, attrs=None, options=None, js_tree=None):
    super(Options, self).__init__(report, attrs, options)
    self.js_type, self.__config_sub_levels, self.__config_sub__enum_levels = {}, set(), set()
    # By default it is the component dictionary
    self.js_tree = self._report._jsStyles if js_tree is None else js_tree
    self.js = None
    # Set the default options for a component
    for c in self.component_properties:
      setattr(self, c, getattr(self, c))
    if attrs is not None:
      for k, v in attrs.items():
        if hasattr(self, k):
          setattr(self, k, v)
        else:
          self.js_tree[k] = v

  def _config_get(self, dflt=None, name=None):
    """
    Description:
    ------------
    Get the option attribute to be added on the Javascript side during the component build.
    Unlike the usual get from dict this method will take the default value as first parameter as
    the name is by default the property name using it.

    Attributes:
    ----------
    :param dflt: String. Optional. The default value for this category.
    :param name: String. Optional. The attribute name (default the function property).
    """
    return self.js_tree.get(name or sys._getframe().f_back.f_code.co_name, dflt)

  def _config(self, value, name=None, js_type=False):
    """
    Description:
    ------------
    Set the option attribute to be added on the Javascript side during the component build.

    This method take the value as first parameter because the name is by default the property name if
    not defined. Very often the only information to supply if the value.

    Attributes:
    ----------
    :param value: Object. The value for the name
    :param name: String. Optional. The attribute name. Default is the property name.
    :param js_type: Boolean. Optional. Specify if the parameter is a JavaScript fragment.
    """
    self.js_tree[name or sys._getframe().f_back.f_code.co_name] = value
    if js_type:
      self.js_type[name or sys._getframe().f_back.f_code.co_name] = True

  def _config_group_get(self, group, dflt=None, name=None):
    """
    Description:
    ------------
    Get second level configuration options.

    Attributes:
    ----------
    :param group: String. The group attribute name.
    :param dflt: String. Optional.
    :param name: String. Optional. The attribute name
    """
    return self.js_tree.get(group, {}).get(name or sys._getframe().f_back.f_code.co_name, dflt)

  def _config_group(self, group, value, name=None):
    """
    Description:
    ------------
    Set second level configuration options.

    Attributes:
    ----------
    :param group: String. The group name.
    :param value: Object. The value for the name.
    :param name: String. Optional. The attribute name.
    """
    if group not in self.js_tree:
      self.js_tree[group] = {}
    self.js_tree[group][name or sys._getframe().f_back.f_code.co_name] = value

  def _config_sub_data(self, name, clsObj):
    """
    Description:
    ------------
    Create a nested structure for the JavaScript configuration layer.
    This is required for Charts and Tables configurations.

    Usage:
    -----

    Attributes:
    ----------
    :param name: String. The key to be added to the internal data dictionary.
    :param clsObj: Options. The object which will be added to the nested data structure.
    """
    if name in self.js_tree:
      return self.js_tree[name]

    self.__config_sub_levels.add(name)
    self.js_tree[name] = clsObj(self._report, js_tree={})
    return self.js_tree[name]

  def _config_sub_data_enum(self, name, clsObj):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param name: String. The key to be added to the internal data dictionary.
    :param clsObj: Class. Object. The object which will be added to the nested data structure.
    """
    self.__config_sub__enum_levels.add(name)
    enum_data = clsObj(self._report, js_tree={})
    self.js_tree.setdefault(name, []).append(enum_data)
    return enum_data

  def custom_config(self, name, value, js_type=False):
    """
    Description:
    ------------
    Add a custom JavaScript configuration.

    Usage:
    -----

      chart = page.ui.charts.apex.scatter()
      chart.options.chart.zoom.custom_config("test", False)

    Attributes:
    ----------
    :param name: String. The key to be added to the attributes.
    :param value: String or JString. The value of the defined attributes.
    :param js_type: Boolean. Optional. Specify if the parameter is a JavaScript fragment.
    """
    if js_type:
      self.js_type[name] = True
    self.js_tree[name] = value
    return self

  def isJsContent(self, property_name):
    """
    Description:
    ------------
    Check if the content of a property is defined to always be a JavaScript fragment.
    Thus the framework will not convert it to a Json content.

    Usage:
    -----

      div = page.ui.div()
      print(div.options.isJsContent("inline"))

    Attributes:
    ----------
    :param property_name: String. The property name.
    """
    return self.js_type.get(property_name, False)

  @property
  def managed(self):
    """
    Description:
    ------------
    Boolean flag to set if the component needs to be added to the page.
    If set to False the component has to be managed manually in the page.

    Usage:
    -----

      but = page.ui.button()
      but.options.managed = False

    Attributes:
    ----------
    :prop bool: Boolean. Flag to specify if this component is automatically managed by the page
    """
    return self.get(True)

  @managed.setter
  def managed(self, flag):
    self.set(flag)

  @property
  def verbose(self):
    """
    Description:
    ------------
    Boolean flag to set if extra logs need to be displayed.
    This could help in debugging, default is the page verbose flag (default is false).

    Usage:
    -----

      but = page.ui.button()
      but.options.verbose = True

    Attributes:
    ----------
    :prop flag: Boolean. Flag to display / hide warning logs generated by the framework.
    """
    return self.get(self.component.page.verbose)

  @verbose.setter
  def verbose(self, flag):
    self.set(flag)

  @property
  def profile(self):
    """
    Description:
    ------------
    Boolean flag to set if extra logs need to be displayed.
    This could help in debugging, default is the page verbose flag (default is false).

    Usage:
    -----

      but = page.ui.button()
      but.options.verbose = True

    Attributes:
    ----------
    :prop flag: Boolean. Flag to display / hide warning logs generated by the framework.
    """
    return self.get(self.component.page.verbose)

  @profile.setter
  def profile(self, flag):
    self.set(flag)

  @property
  def builder(self):
    """
    Description:
    ------------
    Add a JavaScript Builder function to the options.
    This will be used to automatically map the Python component to its corresponding JavaScript builder
    function used by the build method.

    Usage:
    -----

      but = page.ui.button()
      but.options.builder = "Button"

    Attributes:
    ----------
    :prop value: String. The JavaScript builder function name.
    """
    return self._config_get(None)

  @builder.setter
  def builder(self, value):
    self.js_type["builder"] = True
    self._config(value)

  @property
  def style(self):
    """
    Description:
    -----------
    Change some CSS attributes to the internal HTML component.

    Related Pages:

      https://www.w3schools.com/cssref/

    Attributes:
    ----------
    :prop values: Dictionary. The CSS attributes.
    """
    return self._config_get({})

  @style.setter
  def style(self, values):
    self._config(values)

  def details(self):
    """
    Description:
    ------------
    Retrieve the defined properties details.

    This function will return a dictionary with all the component attributes (required and optional) ones.
    It will provide the full available description of those components.

    Usage:
    -----

      but = page.ui.button()
      pprint.pprint(but.options.details(), indent=4)
    """
    prop_details = {}
    for prop_name in self.component_properties:
      prop = getattr(self, prop_name)
      prop_details[prop_name] = {
        "type": 'mandatory', "name": prop_name, 'value': prop, 'doc':  getattr(self.__class__, prop_name).__doc__}

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
    Description:
    ------------
    Return all the mandatory / required options with the default values.
    Those options are added by the framework to provide a default for the HTML components but they can be changed.

    System options are also added to this category as they are always available in any HTML components.

    To get the full definition of options the details method should be used.

    Usage:
    -----

      but = page.ui.button()
      pprint.pprint(but.options.required(), indent=4)
    """
    props = self.details()
    result = [v for k, v in props.items() if v["type"] != "optional"]
    return result

  def optional(self):
    """
    Description:
    ------------
    Return all options not added to the HTML component by default.
    Those are options which will impact either the Python or the JavaScript builders.

    To get the full definition of options the details method should be used.

    Usage:
    -----

      but = page.ui.button()
      pprint.pprint(but.options.optional(), indent=4)
    """
    props = self.details()
    result = [v for k, v in props.items() if v["type"] == "optional"]
    return result

  def config_js(self, attrs=None):
    """
    Description:
    ------------
    Return the JavaScript options used by the builders functions.
    Builder functions can be defined in the framework or external from the various packages.

    The returned dictionary is a copy so it can be changed or used in other processes.
    To change the internal component property, the options property should be used.

    Usage:
    -----

    Attributes:
    ----------
    :param attrs: Dictionary. Optional. The extra or overridden options.
    """
    js_attrs, attrs = [], attrs or {}
    if self.__config_sub_levels:
      tmp_tree = dict(self.js_tree)
      for k, v in attrs.items():
        if k not in tmp_tree:
          tmp_tree[k] = v
      for k, v in tmp_tree.items():
        if k in self.__config_sub_levels:
          js_attrs.append("%s: %s" % (k, v.config_js(attrs=attrs.get(k, {})).toStr()))
        elif k in self.__config_sub__enum_levels:
          js_attrs.append("%s: [%s]" % (k, ", ".join([s.config_js(attrs=attrs.get(k, {})).toStr() for s in v])))
        else:
          if k in attrs:
            v = attrs[k]
          if k in self.js_type or hasattr(v, 'toStr'):
            js_attrs.append("%s: %s" % (k, v))
          else:
            js_attrs.append("%s: %s" % (k, json.dumps(v)))
      return JsUtils.jsWrap("{%s}" % ", ".join(js_attrs))

    #
    tmp_tree = dict(self.js_tree)
    tmp_tree.update(attrs)
    for k, v in tmp_tree.items():
      if k in self.js_type:
        js_attrs.append("%s: %s" % (k, v))
      elif hasattr(v, 'toStr'):
        js_attrs.append("%s: %s" % (k, v.toStr()))
      else:
        if k in self.__config_sub__enum_levels:
          js_attrs.append("%s: [%s]" % (k, ", ".join([s.config_js(attrs=attrs.get(k, {})).toStr() for s in v])))
        else:
          js_attrs.append("%s: %s" % (k, json.dumps(v)))
    return JsUtils.jsWrap("{%s}" % ", ".join(js_attrs))

  def config_html(self):
    """
    Description:
    ------------
    Return the HTML options used by the python and passed to the HTML.
    THose options will not be available in the JavaScript layer and they are only defined either
    to build the HTML from Python or to set some HTML properties.

    The returned dictionary is a copy so it can be changed or used in other processes.
    To change the internal component property, the options property should be used.

    Usage:
    -----
    """
    html_attrs = {}
    for k, v in self._attrs.items():
      if k not in self.js_tree:
        html_attrs[k] = v
    return html_attrs

  def __str__(self):
    return str(self.config_js())
