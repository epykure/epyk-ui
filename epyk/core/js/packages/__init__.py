"""
Base class for all the Javascript Packages.

This class must be extended
"""


class JsPackage(object):
  lib_alias = None

  def version(self, ver):
    """
    Change the package version number

    Example
    bar.chart.version("1.11.0")

    :param ver: String. The package versions example 1.11.0
    """
    self.src._props.setdefault("packages", {})[self.lib_alias] = ver
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
