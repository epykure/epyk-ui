#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from epyk.core.js import JsUtils


class DataClass:

  def __init__(self, component, attrs=None, options=None):
    self._report, self.options, self._attrs = component, options, dict(attrs or {})
    self.component = self._report
    self.__sub_levels, self.__sub__enum_levels = set(), set()

  def __getitem__(self, i):
    return self._attrs[i]

  def update(self, vals):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param vals: Dictionary. All the attributes to be added to the component.
    """
    self._attrs.update(vals)

  def attrs(self):
    """
    Description:
    ------------

    Usage::

    """
    return self._attrs.items()

  def custom(self, name, value):
    """
    Description:
    ------------
    Custom function to add a bespoke attribute to a class.

    This entry point will not be able to display any documentation but it is a shortcut to test new features.
    If the value is a Javascript object, the PyJs object must be used.

    Usage::

    Attributes:
    ----------
    :param name: String. The key to be added to the attributes.
    :param value: String or JString. The value of the defined attributes.

    :return: The DataAttrs to allow the chains
    """
    self._attrs[name] = value
    return self

  def attr(self, name, value):
    """
    Description:
    ------------
    Add an attribute to the Javascript underlying dictionary.

    Usage::

    Attributes:
    ----------
    :param name: String. The attribute name.
    :param value: Object. The attribute value.

    :return: "Self" to allow the chains on the Python side
    """
    self._attrs[name] = value
    return self

  def has_attribute(self, clsObj):
    """
    Description:
    ------------
    Add an extra sub layer to the data structure.
    The key in the object representation will be the function name.

    Usage::

    Attributes:
    ----------
    :param clsObj: Class. The sub data class used in the structure definition
    """
    return self.sub_data(sys._getframe().f_back.f_code.co_name, clsObj)

  def get(self, dflt=None, name=None):
    """
    Description:
    ------------
    Get tje attribute to the underlying attributes dictionary.

    Usage::

    Attributes:
    ----------
    :param dflt: string. Optional. The default value of this attribute.
    :param name: String. Optional. The attribute name. default the name of the function.
    """
    return self._attrs.get(name or sys._getframe().f_back.f_code.co_name, dflt)

  def set(self, value, name=None):
    """
    Description:
    ------------
    Add an attribute to the Javascript underlying dictionary.

    Usage::

    Attributes:
    ----------
    :param value: Object. The attribute value.
    :param name: String. Optional. The attribute name. default the name of the function.

    :return: "Self" to allow the chains on the Python side
    """
    return self.attr(name or sys._getframe().f_back.f_code.co_name, value)

  def sub_data(self, name, clsObj):
    """
    Description:
    ------------
    Add an extra sub layer to the data structure.
    The key in the object representation will be the function name.

    Should use has_attribute is the name can be deduced from the parent function.

    Usage::

    Attributes:
    ----------
    :param name: String. The key to be added to the internal data dictionary.
    :param clsObj: Class. Object. The object which will be added to the nested data structure.
    """
    if name in self._attrs:
      return self._attrs[name]

    self.__sub_levels.add(name)
    self._attrs[name] = clsObj(self._report)
    return self._attrs[name]

  def add(self, name, value):
    """
    Description:
    ------------
    Add the key and value to the final result object.

    Usage::

    Attributes:
    ----------
    :param name: String. The key in the final data dictionary.
    :param value: Object. The value in the final data dictionary.
    """
    self.__sub_levels.add(name)
    self._attrs[name] = JsUtils.jsConvertData(value, None)
    return self

  def sub_data_enum(self, name, clsObj):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param name: String. The key to be added to the internal data dictionary.
    :param clsObj: Class. Object. The object which will be added to the nested data structure.
    """
    self.__sub__enum_levels.add(name)
    enum_data = clsObj(self._report)
    self._attrs.setdefault(name, []).append(enum_data)
    return enum_data

  def __str__(self):
    result = ["%s: %s" % (s, str(self._attrs[s])) for s in self.__sub_levels]
    for s in self.__sub__enum_levels:
      result.append("%s: [%s]" % (s, ",".join([str(k) for k in self._attrs[s]])))
    result.extend(["%s: %s" % (k, JsUtils.jsConvertData(v, None)) for k, v in self._attrs.items() if k not in self.__sub_levels and k not in self.__sub__enum_levels])
    return "{%s}" % ", ".join(result)


class DataEnum:

  dflt = None
  js_conversion = False

  def __init__(self, component, value=None):
    self._report, self.__value = component, value or self.dflt
    self.component = self._report

  def set(self, value=None):
    """
    Description:
    ------------
    Set the selected value in this enumeration.
    The last function call will be persisted.

    Usage::

    Attributes:
    ----------
    :param value: String. Optional. The value to be set (default is the function name).
    """
    if value is None:
      value = sys._getframe().f_back.f_code.co_name
    if self.js_conversion:
      value = value.toStr() if hasattr(value, "toStr") else JsUtils.jsConvertData(value, None).toStr()
    self.__value = value

  def custom(self, value):
    """
    Description:
    ------------
    Set a custom value.This will not use any specific conversion.

    Usage::

    Attributes:
    ----------
    :param value: String. The value to be set.
    """
    self.__value = value

  def __str__(self):
    return self.__value


class DataGroup:

  def __init__(self, report, attrs, parent=None):
    self._attrs, self._report, self._parent = attrs, report, parent


class DataEnumMulti:

  dflt = None
  js_conversion = False
  delimiter = ","

  def __init__(self, report, value=None):
    self._report = report
    value = value or self.dflt
    self.__value = set() if value is None else set([value])

  def set(self, value=None):
    """
    Description:
    ------------
    Set the selected value in this enumeration.
    The last function call will be persisted.

    Usage::

    Attributes:
    ----------
    :param value: String. Optional. The value to be set (default is the function name).
    """
    if value is None:
      value = sys._getframe().f_back.f_code.co_name
    self.__value.add(value)

  def custom(self, value):
    """
    Description:
    ------------
    Set a custom value.This will not use any specific conversion.

    Usage::

    Attributes:
    ----------
    :param value: String. The value to be set
    """
    self.__value.add(value)

  def __str__(self):
    result = self.delimiter.join(list(self.__value))
    if self.js_conversion:
      return JsUtils.jsConvertData(result, None).toStr()

    return result
