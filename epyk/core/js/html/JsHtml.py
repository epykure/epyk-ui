"""
Javascript Dom element for the HTML Components
"""

import json

from epyk.core.js import JsUtils
from epyk.core.html import Defaults
from epyk.core.js.statements import JsIf
from epyk.core.js.fncs import JsFncs

from epyk.core.js.objects import JsNodeDom
from epyk.core.js.primitives import JsObjects
from epyk.core.js.packages import JsQuery
from epyk.core.js.packages import JsQueryUi
from epyk.core.js.packages import JsCrossFilter


class JsHtml(JsNodeDom.JsDoms):
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
    return JsObjects.JsObjects.get("{%s: {value: %s.value, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (self.htmlId, self.varName))

  @property
  def content(self):
    return JsObjects.JsObjects.get("%s.value" % self.varName)

  def empty(self): return '%s.value = ""' % self.varName

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
    self._src._props.setdefault('js', {}).setdefault('functions', {})[fncName] = {'content': ";".join(jsData), 'pmt': pmts}
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

  def highlight(self, css_attrs=None, time_event=1000):
    """

    Example
    s.dom.highlight()
    s.dom.highlight(css_attrs={"background": "red"}),

    :param css_attrs: A dictionary with the CSS attributes
    :param time_event: Integer. The time of the event
    """
    if css_attrs is None:
      css_attrs, css_attrs_origin = {}, {}
      for k, v in Defaults.HTML_HIGHLIGHT.items():
        if isinstance(v, dict):
          dyn_attrs, dyn_attrs_orign = {}, {}
          if 'color' in v:
            dyn_attrs['color'] = self._report.getColor(*v['color'])
            dyn_attrs_orign['color'] = self._report.getColor("greys", 0)
          css_attrs[k] = v['attr'] % dyn_attrs
          css_attrs_origin[k] = self._src.attr[k] if k in self._src.attr else v['attr'] % dyn_attrs_orign
        else:
          css_attrs[k] = v
          css_attrs_origin[k] = self._src.attr[k] if k in self._src.attr else "none"
    else:
      css_attrs_origin = {}
      for k in css_attrs.keys():
        if k in self._src.attr:
          css_attrs_origin[k] = self._src.attr[k]
        else:
          css_attrs_origin[k] = "none"
    return '''%s; setTimeout(function(){%s}, %s)
      ''' % (self.css(css_attrs).r, self.css(css_attrs_origin).r, time_event)


class JsHtmlRich(JsHtml):
  @property
  def val(self):
    """

    :return:
    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s.innerHTML, timestamp: Date.now(), offset: new Date().getTimezoneOffset()} }" % (self.htmlId, self.varName))

  @property
  def content(self):
    return JsObjects.JsObjects.get("%s.innerHTML" % self.varName)

  def empty(self): return '%s.innerHTML = ""' % self.varName


class JsHtmlIcon(JsHtml):
  @property
  def val(self):
    """

    :return:
    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (self.htmlId, self._src.dom.getAttribute("class")))

  @property
  def content(self):
    return JsObjects.JsObjects.get(self._src.dom.getAttribute("class"))




