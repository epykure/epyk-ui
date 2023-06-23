#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from typing import Any, Union
from epyk.core.py import primitives
from epyk.core.js import JsUtils


class DataClass:

  def __init__(self, component: primitives.HtmlModel = None, attrs: dict = None, options: dict = None,
               page: primitives.PageModel = None):
    self.component, self.options, self._attrs, self.page = component, options, dict(attrs or {}), page
    if component is not None:
      self.page = component.page
    self.__sub_levels, self.__sub__enum_levels = set(), set()

  def __getitem__(self, i: int):
    return self._attrs[i]

  def update(self, vals: dict):
    """
    Update the object internal attributes.

    :param vals: All the attributes to be added to the component
    """
    self._attrs.update(vals)

  def attrs(self):
    """

    """
    return self._attrs.items()

  def custom(self, name: str, value: Any):
    """
    Custom function to add a bespoke attribute to a class.

    This entry point will not be able to display any documentation but it is a shortcut to test new features.
    If the value is a Javascript object, the PyJs object must be used.

    :param name: The key to be added to the attributes
    :param value: The value of the defined attributes

    :return: The DataAttrs to allow the chains
    """
    self._attrs[name] = value
    return self

  def attr(self, name: str, value: Any):
    """
    Add an attribute to the Javascript underlying dictionary.

    :param name: The attribute name
    :param value: The attribute value

    :return: "Self" to allow the chains on the Python side
    """
    self._attrs[name] = value
    return self

  def has_attribute(self, cls_obj):
    """
    Add an extra sub layer to the data structure.

    The key in the object representation will be the function name.

    :param cls_obj: Class. The sub data class used in the structure definition
    """
    return self.sub_data(sys._getframe().f_back.f_code.co_name, cls_obj)

  def get(self, dfl: Union[str, bool, int, dict, list, float] = None, name: str = None):
    """
    Get the attribute to the underlying attributes dictionary.

    :param dfl: Optional. The default value of this attribute
    :param name: Optional. The attribute name. default the name of the function
    """
    return self._attrs.get(name or sys._getframe().f_back.f_code.co_name, dfl)

  def set(self, value: Any, name: str = None):
    """
    Add an attribute to the Javascript underlying dictionary.

    :param value: The attribute value
    :param name: Optional. The attribute name. default the name of the functin.

    :return: "Self" to allow the chains on the Python side
    """
    return self.attr(name or sys._getframe().f_back.f_code.co_name, value)

  def sub_data(self, name: str, cls_obj):
    """
    Add an extra sub layer to the data structure.
    The key in the object representation will be the function name.

    Should use has_attribute is the name can be deduced from the parent function.

    :param name: The key to be added to the internal data dictionary
    :param cls_obj: Class. Object. The object which will be added to the nested data structure
    """
    if name in self._attrs:
      return self._attrs[name]

    self.__sub_levels.add(name)
    self._attrs[name] = cls_obj(self.component)
    return self._attrs[name]

  def add(self, name: str, value: Any):
    """
    Add the key and value to the final result object.

    :param name: The key in the final data dictionary.
    :param value: The value in the final data dictionary.
    """
    self.__sub_levels.add(name)
    self._attrs[name] = JsUtils.jsConvertData(value, None)
    return self

  def sub_data_enum(self, name: str, cls_obj):
    """
    Add key to a sub dictionary.
    This will create an attribute object with a nested structure.

    :param name: The key to be added to the internal data dictionary
    :param cls_obj: Class. Object. The object which will be added to the nested data structure
    """
    self.__sub__enum_levels.add(name)
    enum_data = cls_obj(self.component)
    self._attrs.setdefault(name, []).append(enum_data)
    return enum_data

  def config_js(self, options: dict = None) -> str:
    if options is not None:
      self._attrs.update(options)
    return self.__str__()

  def config_attrs(self, options: dict = None) -> str:
    """
    Get the attributes in a string.

    :param options: Dictionary with specific attributes to be set
    """
    if options is not None:
      self._attrs.update(options)
    result = ["%s: %s" % (s, str(self._attrs[s])) for s in self.__sub_levels]
    for s in self.__sub__enum_levels:
      result.append("%s: [%s]" % (s, ",".join([str(k) for k in self._attrs[s]])))
    result.extend([
      "%s: %s" % (k, JsUtils.jsConvertData(v, None)) for k, v in self._attrs.items() if
      k not in self.__sub_levels and k not in self.__sub__enum_levels])
    return "{%s}" % ", ".join(result)

  def __str__(self):
    result = ["%s: %s" % (s, str(self._attrs[s])) for s in self.__sub_levels]
    for s in self.__sub__enum_levels:
      result.append("%s: [%s]" % (s, ",".join([str(k) for k in self._attrs[s]])))
    result.extend([
      "%s: %s" % (k, JsUtils.jsConvertData(v, None)) for k, v in self._attrs.items() if k not in self.__sub_levels and k not in self.__sub__enum_levels])
    return "{%s}" % ", ".join(result)


class DataEnum:

  dflt = None
  js_conversion = False

  def __init__(self, component, value: Any = None):
    self.page, self.__value = component.page, value or self.dflt
    self.component = component

  def set(self, value: Union[str, primitives.JsDataModel] = None):
    """ Set the selected value in this enumeration.
    The last function call will be persisted.

    :param value: Optional. The value to be set (default is the function name).
    """
    if value is None:
      value = sys._getframe().f_back.f_code.co_name
    if self.js_conversion:
      value = value.toStr() if hasattr(value, "toStr") else JsUtils.jsConvertData(value, None).toStr()
    self.__value = value

  def custom(self, value: str):
    """ Set a custom value.This will not use any specific conversion.

    :param value: The value to be set.
    """
    self.__value = value

  def __str__(self):
    return self.__value


class DataGroup:

  def __init__(self, page: primitives.PageModel, attrs: dict, parent=None):
    self._attrs, self.page, self._parent = attrs, page, parent


class DataEnumMulti:

  dflt = None
  js_conversion = False
  delimiter = ","

  def __init__(self, page: primitives.PageModel, value: Any = None):
    self.page = page
    value = value or self.dflt
    self.__value = set() if value is None else set([value])

  def set(self, value: str = None):
    """ Set the selected value in this enumeration.
    The last function call will be persisted.

    :param value: Optional. The value to be set (default is the function name).
    """
    if value is None:
      value = sys._getframe().f_back.f_code.co_name
    self.__value.add(value)

  def custom(self, value: str):
    """ Set a custom value.This will not use any specific conversion.

    :param value: The value to be set.
    """
    self.__value.add(value)

  def __str__(self):
    result = self.delimiter.join(list(self.__value))
    if self.js_conversion:
      return JsUtils.jsConvertData(result, None).toStr()

    return result
