"""
DC.js API

http://dc-js.github.io/dc.js/docs/html/
"""

from epyk.core.js import JsUtils
from epyk.core.js.packages import JsPackage


class DC(JsPackage):
  lib_alias = {'css': 'dc', 'js': 'dc'}

  def width(self, n):
    """

    :param n:

    :return: Return 'self' to allow the cnains on the Python side
    """
    n = JsUtils.jsConvertData(n, None)
    return self.fnc_closure("width(%s)" % n)

  def height(self, n):
    """

    :param n:
    :return:
    """
    n = JsUtils.jsConvertData(n, None)
    return self.fnc_closure("height(%s)" % n)

  def yAxisLabel(self, val):
    """

    :param val:

    :return:
    """
    val = JsUtils.jsConvertData(val, None)
    return self.fnc_closure("yAxisLabel(%s)" % val)


if __name__ == "__main__":
  dc = DC(selector="Ok", setVar=False).yAxisLabel("test").height(20).width(30)
  print(dc.toStr())
