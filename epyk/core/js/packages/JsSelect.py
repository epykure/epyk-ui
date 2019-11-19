"""
Wrapper to the Jquery UI package

https://api.jqueryui.com/
"""

import json

from epyk.core.js import JsUtils

from epyk.core.js.objects import JsNodeDom
from epyk.core.js.packages import JsPackage
from epyk.core.js.primitives import JsObjects
from epyk.core.js.packages import JsQuery
from epyk.core.js.packages import JsQueryUi


class JSelect(JsPackage):
  lib_alias = {"js": 'jqueryui', 'css': 'jqueryui'}
  lib_selector = 'jQuery("body")'
  lib_set_var = False

  def __init__(self, htmlObj, varName=None, setVar=True, isPyData=True, report=None):
    self.htmlId = varName if varName is not None else htmlObj.htmlId
    self.varName, self.varData, self.__var_def = "document.getElementById('%s')" % self.htmlId, "", None
    self._src, self._report = htmlObj, report
    self._js = []
    self._jquery, self._jquery_ui = None, None

  @property
  def val(self):
    """

    :return:
    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s.value, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
      self.htmlId, self.varName))

  @property
  def content(self):
    return JsObjects.JsObjects.get("%s.value" % self.varName)

  @property
  def events(self):
    """

    :rtype: JsNodeDom.JsDomEvents
    :return:
    """
    return JsNodeDom.JsDomEvents(self._src)

  @property
  def jquery(self):
    """

    :return:
    :rtype: JsQuery.JQuery
    """
    if self._jquery is None:
      self._jquery = JsQuery.JQuery(src=self._src, selector=JsQuery.decorate_var("#%s" % self._src.htmlId))
    return self._jquery

  @property
  def jquery_ui(self):
    """

    :return:
    :rtype: JsQuery.JQuery
    """
    if self._jquery_ui is None:
      self._jquery_ui = JsQueryUi.JQueryUI(self._src, selector=JsQuery.decorate_var("#%s" % self._src.htmlId))
    return self._jquery_ui
