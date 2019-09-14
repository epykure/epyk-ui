"""
DC.js API

http://dc-js.github.io/dc.js/docs/html/
"""

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects


class DC(object):
  class __internal(object):
    jqId, htmlId, jsImports, cssImport = '', 'chart', set([]), set([])

  def __init__(self, src=None):
    self.src = src if src is not None else self.__internal()
    self.selector = "dc.seriesChart('#%s')" % self.src.htmlId
    self.src.jsImports.add('dc')
    self.src.cssImport.add('dc')
    self._js = []

  def width(self, size):
    """

    :param size:
    :return:
    """
    self._js.append("%s.width(%s)" % (self.toStr(), size))
    return self

  def height(self, size):
    """

    :param size:
    :return:
    """
    self._js.append("%s.height(%s)" % (self.toStr(), size))
    return self

  def yAxisLabel(self, val):
    """

    :return:
    """
    self._js.append("%s.yAxisLabel(%s)" % (self.toStr(), val))
    return self

  def toStr(self):
    """
    Javascript representation

    :return: Return the Javascript String
    """
    if self.selector is None:
      raise Exception("Selector not defined, use this() or new() first")

    if len(self._js) == 0:
      return self.selector

    strData = "%(jqId)s.%(items)s" % {'jqId': self.selector, 'items': ".".join(self._js)}
    self._js = [] # empty the stack
    return JsObjects.JsObject.JsObject.get(strData)
