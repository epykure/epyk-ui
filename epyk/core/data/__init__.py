from . import Data

from epyk.core.js import JsUtils


class DataClass(object):
  def __init__(self, report, attrs=None, oprions=None):
    self._report, self.oprions, self._attrs = report, oprions, attrs or {}
    self.__sub_levels, self.__sub__enum_levels = set(), set()

  def __getitem__(self, i):
    return self._attrs[i]

  def items(self):
    return self._attrs.items()

  def custom(self, name, value):
    """
    Description:
    ------------
    Custom function to add a bespoke attribute to a class.

    This entry point will not be able to display any documentation but it is a shortcut to test new features.
    If the value is a Javascript object, the PyJs object must be used

    Attributes:
    ----------
    :param name: String. The key to be added to the attributes
    :param value: String or JString. The value of the defined attributes

    :return: The DataAttrs to allow the chains
    """
    self._attrs[name] = value
    return self

  def attr(self, name, value):
    """
    Description:
    ------------
    Add an attribute to the Javascript underlying dictionary

    Attributes:
    ----------
    :param name: String. The attribute name
    :param value: Object. The attribute value

    :return: "Self" to allow the chains on the Python side
    """
    self._attrs[name] = value
    return self

  def sub_data(self, name, clsObj):
    """

    :param data:
    :return:
    """
    if name in self._attrs:
      return self._attrs[name]

    self.__sub_levels.add(name)
    self._attrs[name] = clsObj(self._report)
    return self._attrs[name]

  def sub_data_enum(self, name, clsObj):
    """

    :param data:
    :return:
    """
    if name in self._attrs:
      return self._attrs[name]

    self.__sub__enum_levels.add(name)
    self._attrs.setdefault(name, []).append(clsObj(self._report))
    return self._attrs[name]

  def __str__(self):
    result = []
    for s in self.__sub_levels:
      result.append("%s: %s" % (s, str(self._attrs[s])))
    for s in self.__sub__enum_levels:
      result.append("%s: [%s]" % (s, ",".join([str(k) for k in self._attrs[s]])))
    result.extend(["%s: %s" % (k, JsUtils.jsConvertData(v, None)) for k, v in self._attrs.items() if k not in self.__sub_levels and k not in self.__sub__enum_levels])
    return "{%s}" % ", ".join(result)
