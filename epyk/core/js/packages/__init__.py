"""
Base class for all the Javascript Packages.

This class must be extended
"""

from epyk.core.js.primitives import JsString


class JsPackage(object):
  lib_alias = None

  class __internal(object):
    # By default it will attach eveything to the body
    jqId, jsImports, cssImport = '', set([]), set([])

  def __init__(self, src=None, varName=None, setVar=True):
    self.src = src if src is not None else self.__internal()
    self._selector = self.src.jqId
    self.varName, self.setVar = varName, setVar
    self._js = []

  def version(self, ver):
    """
    Change the package version number

    Example
    bar.chart.version("1.11.0")

    :param ver: String. The package versions example 1.11.0
    """
    self.src._props.setdefault("packages", {})[self.lib_alias] = ver
    return self

  @property
  def var(self):
    """
    Property to return the variable name as a valid pyJs object
    """
    return JsString.JsString(self.varName, isPyData=False)

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

    strData = ".".join(self._js)
    if self.setVar:
      strData = "var %s = %s.%s" % (self.varName, self._selector, strData)
      self.setVar = False
    else:
      strData = "%s.%s" % (self.varName, strData)
    self._js = [] # empty the stack
    return strData
