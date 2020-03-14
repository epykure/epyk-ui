
import json

from epyk.core.js import JsUtils
from epyk.core.html import Defaults
from epyk.core.js.statements import JsIf
from epyk.core.js.fncs import JsFncs

from epyk.core.js.objects import JsNodeDom
from epyk.core.js.primitives import JsBoolean
from epyk.core.js.primitives import JsObjects
from epyk.core.js.packages import JsQuery
from epyk.core.js.packages import JsD3
from epyk.core.js.packages import JsQueryUi
from epyk.core.js.packages import JsCrossFilter


class JsHtml(JsNodeDom.JsDoms):
  def __init__(self, htmlObj, varName=None, setVar=True, isPyData=True, report=None):
    self.htmlId = varName if varName is not None else htmlObj.htmlId
    self.varName, self.varData, self.__var_def = "document.getElementById('%s')" % self.htmlId, "", None
    self._src, self._report = htmlObj, report
    self._js = []
    self._jquery, self._jquery_ui, self._d3 = None, None, None

  @property
  def val(self):
    """

    :return:
    """
    return JsObjects.JsObjects.get("{%s: {value: %s.value, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (self.htmlId, self.varName))

  @property
  def by_name(self):
    """

    :rtype: JsNodeDom.JsDomsList
    """
    if self._src.attr.get('name') is not None:
      return JsNodeDom.JsDomsList(None, "document.getElementsByName('%s')" % self._src.attr.get('name'), report=self._report)

    return self

  @property
  def inViewPort(self):
    """
    Description:
    -----------

    """
    bool = JsBoolean.JsBoolean("!(rect.bottom < 0 || rect.top - viewHeight >= 0)", varName="visibleFlag", setVar=True, isPyData=False)
    bool._js.insert(0, self._report.js.viewHeight.setVar('viewHeight'))
    bool._js.insert(0, self.getBoundingClientRect().setVar("rect"))
    return JsFncs.JsAnonymous(bool.r).return_("visibleFlag").call()

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
  def d3(self):
    """

    :return:
    :rtype: JsD3.D3Select
    """
    if self._d3 is None:
      self._d3 = JsD3.D3Select(src=self._src, id=self._src.htmlId)
    return self._d3

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

  def show(self, inline=True):
    """
    Usage:
    ------
    input.js.show()

    Related Pages:
    --------------
    https://gomakethings.com/how-to-show-and-hide-elements-with-vanilla-javascript/

    Attributes:
    ----------
    :param inline: String

    :return:
    """
    return JsUtils.jsConvertData(self.css("display", 'inline-block' if inline else 'block'), None)

  def toggle(self, attr="display", jsVal1="inline-block", jsVal2="none"):
    """
    Description:
    ------------

    Usage:
    ------
    input.js.toggle()
    input.js.toggle("background", "red", "blue")

    Related Pages:
    --------------
    https://gomakethings.com/how-to-show-and-hide-elements-with-vanilla-javascript/

    Attributes:
    ----------
    :param attr:
    :param jsVal1:
    :param jsVal2:

    :return: A Javascript if statement
    """
    return JsIf.JsIf(self.css(attr) == jsVal2, [self.css(attr, jsVal1)]).else_([self.css(attr, jsVal2)])

  def highlight(self, css_attrs=None, time_event=1000):
    """
    Description:
    ------------

    Usage:
    ------
    s.dom.highlight()
    s.dom.highlight(css_attrs={"background": "red"}),

    Attributes:
    ----------
    :param css_attrs: A dictionary with the CSS attributes
    :param time_event: Integer. The time of the event
    """
    if css_attrs is None:
      css_attrs, css_attrs_origin = {}, {}
      for k, v in Defaults.HTML_HIGHLIGHT.items():
        if isinstance(v, dict):
          dyn_attrs, dyn_attrs_orign = {}, {}
          if 'color' in v:
            dyn_attrs['color'] = getattr(self._report.theme, *v['color'])
            dyn_attrs_orign['color'] = self._report.theme.greys[0]
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

  def loadHtml(self, htmlObjs, append=False):
    """
    Description:
    ------------
    Load during a Javascript event a component within the one using this method.
    This cannot be tested during the Python execution and should be tested in the browser.

    Tip: It is possible to add a break point to debug in the browser by adding

    Usage:
    ------
    d = rptObj.ui.div().css({"border": "1px solid black"})
    b = rptObj.ui.button("test")
    b.click([
      rptObj.js.console.debugger,
      d.dom.loadHtml(rptObj.ui.texts.label("test label").css({"color": 'blue', 'float': 'none'}))
    ])

    Attributes:
    ----------
    :param htmlObjs: List. The different HTML objects to be added to the component
    :param append: Boolean. Mention if the component should replace or append the data

    :return: The Javascript string to be added to the page
    """
    if not isinstance(htmlObjs, list):
      htmlObjs = [htmlObjs]

    jsFncs = []
    for i, h in enumerate(htmlObjs):
      h.inReport = False
      jsFncs.append(self._report.js.objects.new(str(h), isPyData=True, varName="obj_%s" % i))
      jsFncs.append(self.innerHTML(self._report.js.objects.get("obj_%s" % i), append=append).r)
    return JsUtils.jsConvertFncs(jsFncs, toStr=True)


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

  def append(self, text, new_line=False):
    """

    Example
    pre.dom.append("ok", new_line=True)

    :param text:
    :param new_line: Boolean

    """
    if new_line:
      return ";".join(JsUtils.jsConvertFncs("%s.append('\\n' + %s)" % (self.varName, JsUtils.jsConvertData(text, None))))

    return ";".join(JsUtils.jsConvertFncs("%s.append(%s)" % (self.varName, JsUtils.jsConvertData(text, None))))

  def empty(self): return '%s.innerHTML = ""' % self.varName


class JsHtmlButton(JsHtml):
  @property
  def val(self):
    """

    :return:
    """
    return JsObjects.JsObjects.get('''{%s: {value: %s.innerHTML, timestamp: Date.now(), 
      offset: new Date().getTimezoneOffset(), locked: %s === 'true', name: %s}}
      ''' % (self.htmlId, self.varName, self.getAttribute('data-locked'), self.getAttribute('name')))

  @property
  def content(self):
    return JsObjects.JsObjects.get("%s.innerHTML" % self.varName)

  def loading(self, flag, multiple=False):
    """
    Add a loading icon to the button

    Example
    b = rptObj.ui.button("test")
    b.click([
      b.dom.loading(True),
      rptObj.js.window.setTimeout([
        b.dom.loading(False)
      ], 5000),
    ])

    :param flag:
    :param multiple:
    :return:
    """
    i_loading = '<i class="fas fa-spinner fa-spin" style="margin-right:5px"></i>'
    fnc = self.disable(False) if multiple else self.disable(flag)
    if flag:
      fnc.append("%s.innerHTML = '%s' + %s.innerHTML" % (self.varName, i_loading, self.varName))
    else:
      fnc.append("%s.innerHTML = %s.innerHTML.replace('%s', '')" % (self.varName, self.varName, i_loading))
    return fnc

  def error(self, time, color="red"):
    """

    :param time:
    :param color:
    :return:
    """
    return JsFncs.JsFunction("var bgColor = %s.style.borderColor; %s.style.borderColor = '%s'; setTimeout(function() {%s.style.borderColor = bgColor}, %s)" % (self.varName, self.varName, color, self.varName, time))

  def disable(self, bool=True):
    bool = JsUtils.jsConvertData(bool, None)
    return JsFncs.JsFunctions("%s.disabled = %s" % (self.varName, bool))

  def release(self, by_name=False):
    """

    :param by_name:
    :return:
    """
    if by_name:
      fncs = JsFncs.JsFunctions(self.by_name.css("color", ''))
      fncs.append(self.by_name.css("background-color", ''))
      fncs.append(self.by_name.css("cursor", "pointer"))
      fncs.append(self.by_name.attr('data-locked', False))
    else:
      fncs = JsFncs.JsFunctions(self.css("color", ''))
      fncs.append(self.css("background-color", ''))
      fncs.append(self.css("cursor", "pointer"))
      fncs.append(self.attr('data-locked', False))
    return fncs

  def lock(self, not_allowed=True):
    """

    :param lock:
    """
    fncs = JsFncs.JsFunctions(self.css("color", self.getComputedStyle('color')))
    fncs.append(self.css("background-color", self.getComputedStyle('background-color')))
    if not_allowed:
      fncs.append(self.css("cursor", "not-allowed"))
      fncs.append(self.attr('data-locked', True))
    else:
      fncs.append(self.css("cursor", "default"))
      fncs.append(self.attr('data-locked', True))
    return fncs

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
    return self._src.dom.getAttribute("class")


class JsHtmlList(JsHtml):
  @property
  def val(self):
    """

    :return:
    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s.querySelector('[data-select=true]').innerHTML, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (self.htmlId, self.varName))

  @property
  def content(self):
    return self._src.dom.getAttribute("class")



