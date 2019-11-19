"""

"""

from epyk.core.js.objects import JsNodeDom

from epyk.core.js.packages import JsQueryUi


class JsHtmlDatePicker(JsNodeDom.JsDoms):
  def __init__(self, htmlObj, varName=None, setVar=True, isPyData=True, report=None):
    self.htmlId = varName if varName is not None else htmlObj.htmlId
    self.varName, self.varData, self.__var_def = "document.getElementById('%s')" % self.htmlId, "", None
    self._src, self._report = htmlObj, report
    self._js = []
    self._jquery, self._jquery_ui = None, None

  @property
  def jqueryui(self):
    """

    :return:
    :rtype: JsQueryUi.JQueryUiDatePicker
    """
    if self._jquery_ui is None:
      self._jquery_ui = JsQueryUi.JQueryUiDatePicker(self._src)
    return self._jquery_ui


class JsHtmlProgressBar(JsNodeDom.JsDoms):
  def __init__(self, htmlObj, varName=None, setVar=True, isPyData=True, report=None):
    self.htmlId = varName if varName is not None else htmlObj.htmlId
    self.varName, self.varData, self.__var_def = "document.getElementById('%s')" % self.htmlId, "", None
    self._src, self._report = htmlObj, report
    self._js = []
    self._jquery, self._jquery_ui = None, None

  @property
  def jqueryui(self):
    """

    :return:
    :rtype: JsQueryUi.JsHtmlProgressBar
    """
    if self._jqueryui is None:
      self._jqueryui = JsQueryUi.JQueryUiProgressBar(self._src)
    return self._jqueryui

  @property
  def val(self):
    return '%s.progressbar("value")' % self._src.dom.jquery.varId
