"""

TODO: Split the component_properties class attribute into two decorators
@js_option =>  self._report._jsStyles
@html_option =>  self._attrs
"""

import sys

from epyk.core.data.DataClass import DataClass


class Options(DataClass):
  component_properties = ()

  def __init__(self, report, attrs=None, options=None):
    super(Options, self).__init__(report, attrs, options)
    self.js_type = {}
    # Set the default options for a component
    for c in self.component_properties:
      setattr(self, c, getattr(self, c))
    if attrs is not None:
      for k, v in attrs.items():
        if hasattr(self, k):
          setattr(self, k, v)
        else:
          self._report._jsStyles[k] = v

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
    return self._report._jsStyles.get(name or sys._getframe().f_back.f_code.co_name, dflt)

  def _config(self, value, name=None):
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
    """
    self._report._jsStyles[name or sys._getframe().f_back.f_code.co_name] = value

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
    return self._report._jsStyles.get(group, {}).get(name or sys._getframe().f_back.f_code.co_name, dflt)

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
    if not group in self._report._jsStyles:
      self._report._jsStyles[group] = {}
    self._report._jsStyles[group][name or sys._getframe().f_back.f_code.co_name] = value

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
    """
    return self.get(True)

  @managed.setter
  def managed(self, bool):
    self.set(bool)

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
    """
    return self.get(self._report._report.verbose)

  @verbose.setter
  def verbose(self, bool):
    self.set(bool)

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
      prop_details[prop_name] = {"type": 'mandatory', "name": prop_name, 'value': prop, 'doc':  getattr(self.__class__, prop_name).__doc__}

    # Add the value of the system attributes
    prop_details["verbose"] = {"name": "verbose", "value": self.verbose, "type": "system"}
    prop_details["managed"] = {"name": "managed", "value": self.managed, "type": "system"}
    for k, v in vars(self.__class__).items():
      if k not in prop_details and isinstance(v, property):
        prop_details[k] = {"type": 'optional', "name": k, 'value': getattr(self, k), 'doc': getattr(self.__class__, k).__doc__}
    return prop_details

  def required(self):
    """
    Description:
    ------------
    Return all the mandatory / required options with the default values.
    Those options are added by the framework in order to provide a default for the HTML components but they can be changed.

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

