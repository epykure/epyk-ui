"""
Javascript Dom element for the HTML Components
"""


import json

from epyk.core.js import JsUtils
from epyk.core.js.statements import JsIf
from epyk.core.js.fncs import JsFncs

from epyk.core.js.objects import JsNodeDom
from epyk.core.js.primitives import JsObjects
from epyk.core.js.packages import JsQuery
from epyk.core.js.packages import JsQueryUi
from epyk.core.js.packages import JsTabulator
from epyk.core.js.packages import JsCrossFilter


class JsHtml(JsNodeDom.JsDoms):
  def __init__(self, htmlObj, varName=None, setVar=True, isPyData=True, report=None):
    self.htmlId = varName if varName is not None else htmlObj.htmlId
    self.varName, self.varData, self.__var_def = "document.getElementById('%s')" % self.htmlId, "", None
    self.__src, self._report = htmlObj, report
    self._js = []
    self._jquery, self._jquery_ui = None, None

  def val(self):
    return JsObjects.JsObjects.get("%s.val()" % self.varName)

  @property
  def events(self):
    """

    :rtype: JsNodeDom.JsDomEvents
    :return:
    """
    return JsNodeDom.JsDomEvents(self.__src)

  @property
  def jquery(self):
    """

    :return:
    :rtype: JsQuery.JQuery
    """
    if self._jquery is None:
      self._jquery = JsQuery.JQuery(self.__src)
    return self._jquery

  @property
  def jquery_ui(self):
    """

    :return:
    :rtype: JsQuery.JQuery
    """
    if self._jquery_ui is None:
      self._jquery_ui = JsQueryUi.JQueryUI(self.__src)
    return self._jquery_ui

  @property
  def objects(self):
    """
    Interface to the main Javascript Classes and Primitives

    Documentation

    :return:
    """
    return JsObjects.JsObjects(self)

  @property
  def crossfilter(self):
    """
    Interface to CrossFilter package

    Documentation
    https://github.com/square/crossfilter/wiki/API-Reference#group_all

    :return:
    """
    return JsCrossFilter.CrossFilter

  def style(self, attrs):
    """
    Style property to change from the javascript the CSS attributes of an HTML object.

    Examples
    button.js.style({"backgroundColor": 'red'})
    button.js.style({"backgroundColor": None})

    Documentation
    https://www.w3.org/TR/DOM-Level-2-Style/css.html#CSS-CSSStyleRule-style

    :param attrs:
    :return:
    """
    styles = []
    for k, v in attrs.items():
      styles.append("this.style.%s = %s" % (k, json.dumps(v)))
    return ";".join(styles)

  def registerFunction(self, fncName, jsFncs, pmts=None):
    """
    Javascript Framework extension

    Register a predefined Javascript function
    This is only dedicated to specific Javascript transformation functions

    Example


    :param fncName: The function name
    :param jsFncs: The Javascript function definition
    :return: The JsObject
    """
    jsData = JsUtils.jsConvertFncs(jsFncs)
    self.__src._props.setdefault('js', {}).setdefault('functions', {})[fncName] = {'content': ";".join(jsData), 'pmt': pmts}
    return self

  def hide(self):
    """

    Example
    input.js.hide()

    Documentation
    https://gomakethings.com/how-to-show-and-hide-elements-with-vanilla-javascript/

    :return:
    """
    return self.css("display", "none")

  def show(self):
    """
    Example
    input.js.show()

    Documentation
    https://gomakethings.com/how-to-show-and-hide-elements-with-vanilla-javascript/

    :return:
    """
    return JsUtils.jsConvertData(self.css("display", "block"), None)

  def toggle(self, attr="display", jsVal1="block", jsVal2="none"):
    """

    Example
    input.js.toggle()
    input.js.toggle("background", "red", "blue")

    Documentation
    https://gomakethings.com/how-to-show-and-hide-elements-with-vanilla-javascript/

    :param attr:
    :param jsVal1:
    :param jsVal2:
    :return:
    """
    return JsIf.JsIf(self.css(attr) == jsVal2, [self.css(attr, jsVal1)]).else_([self.css(attr, jsVal2)])


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
      self._jqueryui = JsQueryUi.JQueryUiDatePicker(self.__src)
    return self._jqueryui


class JsHtmlTimePicker(JsNodeDom.JsDoms):
  def __init__(self, htmlObj):
    super(JsHtmlTimePicker, self).__init__(htmlObj)
    self._jqueryui = None


class JsHtmlTabulator(JsNodeDom.JsDoms):
  def __init__(self, htmlObj):
    super(JsHtmlTabulator, self).__init__(htmlObj)
    self._tabulator = None

  @property
  def tabulator(self):
    """

    :return:
    :rtype: JsTabulator.Tabulator
    """
    if self._tabulator is None:
      self._tabulator = JsTabulator.Tabulator(self.__src)
    return self._tabulator
