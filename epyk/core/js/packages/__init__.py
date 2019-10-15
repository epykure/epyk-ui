"""
Base class for all the Javascript Packages.

This class must be extended
"""

from epyk.core.js.primitives import JsString
from epyk.core.js import JsUtils


class JsPackage(object):
  lib_alias = None

  class __internal(object):
    # By default it will attach eveything to the body
    jqId, jsImports, cssImport = '', set([]), set([])

  def __init__(self, src=None, varName=None, selector=None, data=None, setVar=True):
    self.src = src if src is not None else self.__internal()
    self._selector = selector if selector is not None else self.src.jqId
    self.varName, self.setVar = varName, setVar
    self._data = data
    self._js = [[]] # a list of list of object definition
    if self.lib_alias is not None:
      if 'css' in self.lib_alias:
        self.src.cssImport.add(self.lib_alias['css'])
      if 'js' in self.lib_alias:
        self.src.jsImports.add(self.lib_alias['js'])

  @property
  def varId(self):
    """
    The Javascript and Python reference ID
    """
    return self._selector if self.varName is None else self.varName

  def version(self, ver):
    """
    Change the package version number

    Example
    bar.chart.version("1.11.0")

    :param ver: String. The package versions example 1.11.0
    """
    self.src._props.setdefault("packages", {})[self.lib_alias] = ver
    return self

  def fnc(self, fnc_str):
    """
    Base function to allow the object chain.
    THis will add the elements to the current section in the object structure
    All the items at the same level wil be chained

    :param fnc_str: THe Javascript fragment to be added

    :return: "Self" to allow the chains
    """
    self._js[-1].append(fnc_str)
    return self

  def fnc_closure(self, fnc_str):
    """
    Add the function string to the existing object definition but create a new entry point for the next ones.
    This structure will allow the chain on the Javascript side but also on the Python side.

    Thanks to this Python can always keep the same structure and produce the correct Javascript definition
    There will be no chain in the Javascript side

    Example

    :param fnc_str: String. The Javascript fragment to be added

    :return: The "self" to allow the chains
    """
    self._js[-1].append(fnc_str)
    self._js.append([])
    return self

  @property
  def var(self):
    """
    Property to return the variable name as a valid pyJs object
    """
    return JsString.JsString(self.varId, isPyData=False)

  def set_var(self, flag):
    """
    Change the flag to define if the variable should be defined on the Javascript side.
    Default this is set to True

    :param flag: A python boolean

    :return: This in order to allow js chains
    """
    self.setVar = flag
    return self

  def toStr(self):
    """
    Javascript representation

    :return: Return the Javascript String
    """
    if self._selector is None:
      raise Exception("Selector not defined, use this() or new() first")

    obj_content = []
    for js in self._js:
      if len(js) == 0:
        continue

      str_fnc = ".".join(js)
      if self.setVar:
        if str_fnc:
          str_fnc = "var %s = %s.%s" % (self.varId, self._selector, str_fnc)
        else:
          str_fnc = "var %s = %s" % (self.varId, self._selector)
        self.setVar = False
      else:
        if str_fnc:
          str_fnc = "%s.%s" % (self.varId, str_fnc)
        else:
          str_fnc = self.varId
      obj_content.append(str_fnc)
    self._js = [[]] # empty the stack
    return "; ".join(obj_content)


class DataAttrs(object):
  def __init__(self, report, attrs=None, oprions=None):
    self._report, self.oprions, self._attrs = report, oprions, attrs or {}

  def custom(self, name, value):
    """
    Custom function to add a bespoke attribute to a class.

    This entry point will not be able to display any documentation but it is a shortcut to test new features.
    If the value is a Javascript object, the PyJs object must be used

    :param name: String. The key to be added to the attributes
    :param value: String or JString. The value of the defined attributes

    :return: The DataAttrs to allow the chains
    """
    self._attrs[name] = JsUtils.jsConvertData(value, None)
    return self

  def attr(self, name, value):
    """
    Add an attribute to the Javascript underlying dictionary

    :param name: String. The attribute name
    :param value: Object. The attribute value

    :return: "Self" to allow the chains on the Python side
    """
    self._attrs[name] = value
    return self

  def __str__(self):
    """
    Produce the resulting string to be added to the Javascript section of the web page
    """
    return "{%s}" % ", ".join(["%s: %s" % (k, v) for k, v in self._attrs.items()])
