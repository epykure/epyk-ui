"""

"""

from epyk.core.js.objects import JsNodeDom

from epyk.core.js.packages import JsQueryUi


class JsHtmlDatePicker(JsNodeDom.JsDoms):
  def __init__(self, htmlObj):
    super(JsHtmlDatePicker, self).__init__(htmlObj)
    self._jqueryui = None

  @property
  def jqueryui(self):
    """

    :return:
    :rtype: JsQueryUi.JQueryUiDatePicker
    """
    if self._jqueryui is None:
      self._jqueryui = JsQueryUi.JQueryUiDatePicker(self._src)
    return self._jqueryui


class JsHtmlProgressBar(JsHtml):
  def __init__(self, htmlObj, varName=None, setVar=True, isPyData=True, report=None):
    super(JsHtmlProgressBar, self).__init__(htmlObj)
    self._jqueryui = None

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
