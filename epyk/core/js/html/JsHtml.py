#!/usr/bin/python
# -*- coding: utf-8 -*-

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
from epyk.core.js.packages import packageImport


class FmtNumber(object):

  def __init__(self, report, selector, value):
    self._report, self._val = report, value
    self.selector = selector

  def toFixed(self, value=None):
    """
    Description:
    -----------
    The toFixed() method converts a number into a string, keeping a specified number of decimals.

    Related Pages:

      https://www.w3schools.com/jsref/jsref_tofixed.asp

    Attributes:
    ----------
    :param value: Integer. The number of digit to be displayed
    """
    if value is None:
      return JsObjects.JsObjects.get("%s = %s.toFixed()" % (self.selector, self._val))

    return JsObjects.JsObjects.get("%s = %s.toFixed(%s)" % (self.selector, self._val, value))

  def toPrecision(self, value=None):
    """
    Description:
    -----------
    The toPrecision() method formats a number to a specified length.

    Related Pages:

      https://www.w3schools.com/jsref/jsref_toprecision.asp

    Attributes:
    ----------
    :param value: Integer. The number of digit to be displayed
    """
    if value is None:
      return JsObjects.JsObjects.get("%s = %s.toPrecision()" % (self.selector, self._val))

    return JsObjects.JsObjects.get("%s = %s.toPrecision(%s)" % (self.selector, self._val, value))

  def toExponential(self):
    """
    Description:
    -----------
    The toExponential() method converts a number into an exponential notation.

    Related Pages:

      https://www.w3schools.com/jsref/jsref_toexponential.asp
    """
    return JsObjects.JsObjects.get("%s = %s.toExponential()" % (self.selector, self._val))


class Formatters(object):

  def __init__(self, report, selector):
    self._report = report
    self.selector = selector

  @property
  def number(self):
    """
    Description:
    -----------
    Standard conversion to number

    Related Pages:

      https://www.w3schools.com/jsref/jsref_obj_number.asp
    """
    return FmtNumber(self._report, self.selector, "parseFloat(%s)" % self.selector)

  @packageImport("accounting")
  def toNumber(self, digit=0, thousand_sep="."):
    """
    Description:
    -----------
    Convert to number using the accounting Javascript module

    Related Pages:

      https://openexchangerates.github.io/accounting.js/

    Attributes:
    ----------
    :param digit: Integer. The number of digit to be displayed
    :param thousand_sep: String. The thousand symbol separator
    """
    thousand_sep = JsUtils.jsConvertData(thousand_sep, None)
    return JsObjects.JsObjects.get("%s = accounting.formatNumber(%s, %s, %s)" % (self.selector, self.selector, digit, thousand_sep))

  @packageImport("accounting")
  def toMoney(self, symbol="", digit=0, thousand_sep=".", decimal_sep=","):
    """
    Description:
    -----------
    Convert to number with a symbol using the accounting Javascript module

    Related Pages:

      https://openexchangerates.github.io/accounting.js/

    Attributes:
    ----------
    :param symbol: String. The currency sympol
    :param digit: Integer. The number of digit to be displayed
    :param thousand_sep: String. The thousand symbol separator
    :param decimal_sep: String. The decimal symbol separator
    """
    symbol = JsUtils.jsConvertData(symbol, None)
    thousand_sep = JsUtils.jsConvertData(thousand_sep, None)
    decimal_sep = JsUtils.jsConvertData(decimal_sep, None)
    return JsObjects.JsObjects.get("%s = accounting.formatMoney(%s, %s, %s, %s, %s)" % (self.selector, self.selector, symbol, digit, thousand_sep, decimal_sep))


class ContentFormatters(object):

  def __init__(self, report, selector):
    self._report = report
    self.selector = selector

  def __ge__(self, obj):
    return "%s >= %s" % (self.selector, JsUtils.jsConvertData(obj, None))

  def __gt__(self, obj):
    return "%s > %s" % (self.selector, JsUtils.jsConvertData(obj, None))

  def __le__(self, obj):
    return "%s <= %s" % (self.selector, JsUtils.jsConvertData(obj, None))

  def __lt__(self, obj):
    return "%s < %s" % (self.selector, JsUtils.jsConvertData(obj, None))

  def __eq__(self, obj):
    return "%s == %s" % (self.selector, JsUtils.jsConvertData(obj, None))

  def __ne__(self, obj):
    return "%s <> %s" % (self.selector, JsUtils.jsConvertData(obj, None))

  @packageImport("showdown")
  def fromMarkdown(self, options=None):
    """
    Description:
    ------------
    Convert markwdown to HTML string

    Usage::

      t.dom.content.fromMarkdown()

    Related Pages:

      https://github.com/showdownjs/showdown

    Attributes:
    ----------
    :param options: Dictionary. Options allowed in the showdown module
    """
    options = JsUtils.jsConvertData(options or {}, None)
    return JsObjects.JsObjects.get(
      "%s = (function(){ var conv = new showdown.Converter(%s); return conv.makeHtml(%s)})()" % (
        self.selector, options, self.selector))

  @packageImport("accounting")
  def toNumber(self, digit=0, thousand_sep="."):
    """
    Description:
    -----------
    Convert to number using the accounting Javascript module-

    Usage::

      Related Pages:

      https://openexchangerates.github.io/accounting.js/

    Attributes:
    ----------
    :param digit: Integer. The number of digit to be displayed
    :param thousand_sep:  The thousand symbol separator
    """
    thousand_sep = JsUtils.jsConvertData(thousand_sep, None)
    return JsObjects.JsObjects.get("accounting.formatNumber(%s, %s, %s)" % (self.selector, digit, thousand_sep))

  @packageImport("accounting")
  def toMoney(self, symbol="", digit=0, thousand_sep=".", decimal_sep=","):
    """
    Description:
    ------------
    Convert to number with a symbol using the accounting Javascript module

    Related Pages:

      https://openexchangerates.github.io/accounting.js/

    Attributes:
    ----------
    :param symbol: String. The currency sympol
    :param digit: Integer. The number of digit to be displayed
    :param thousand_sep: String. The thousand symbol separator
    :param decimal_sep: String. The decimal symbol separator
    """
    symbol = JsUtils.jsConvertData(symbol, None)
    thousand_sep = JsUtils.jsConvertData(thousand_sep, None)
    decimal_sep = JsUtils.jsConvertData(decimal_sep, None)
    return JsObjects.JsObjects.get("accounting.formatMoney(%s,%s, %s, %s, %s)" % (self.selector, symbol, digit, thousand_sep, decimal_sep))

  @packageImport("accounting")
  def unformat(self):
    """
    Description:
    ------------
    parse a value from any formatted number/currency string

    Related Pages:

      http://openexchangerates.github.io/accounting.js/
    """
    return JsObjects.JsNumber.JsNumber("accounting.unformat(%s)" % self.selector)

  @property
  def number(self):
    """
    Description:
    ------------
    Standard conversion to number
    """
    return JsObjects.JsNumber.JsNumber("parseFloat(%s)" % self.selector)

  @property
  def string(self):
    """
    Description:
    ------------
    Standard conversion to string
    """
    return JsObjects.JsString.JsString("String(%s)" % self.selector)

  @property
  def date(self):
    """
    Description:
    ------------
    Standard conversion to Date object
    """
    return JsObjects.JsDate.JsDate("new Date(%s)" % self.selector)

  def toStr(self):
    return self.selector

  @property
  def dict(self):
    return JsObjects.JsObject.JsObject.get("%s" % self.selector)


class JsHtml(JsNodeDom.JsDoms):
  display_value = "inline-block"

  def __init__(self, htmlObj, varName=None, setVar=True, isPyData=True, report=None):
    self.htmlCode = varName if varName is not None else htmlObj.htmlCode
    self.varName, self.varData, self.__var_def = "document.getElementById('%s')" % self.htmlCode, "", None
    self._src, self._report = htmlObj, report
    self._js = []
    self._jquery, self._jquery_ui, self._d3 = None, None, None

  @property
  def val(self):
    """
    Description:
    -----------
    Return a Javascript val object
    """
    return JsObjects.JsObjects.get("{%s: {value: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (self.htmlCode, self.content.toStr()))

  @property
  def by_name(self):
    """
    Description:
    -----------

    :rtype: JsNodeDom.JsDomsList
    """
    if self._src.attr.get('name') is not None:
      return JsNodeDom.JsDomsList(None, "document.getElementsByName('%s')" % self._src.attr.get('name'), report=self._report)

    return self

  @property
  def isInViewPort(self):
    """
    Description:
    -----------
    Check if the component is in the visible part of the page (the viewpport)

    :rtype: JsObject.JsObject

    :return: A Javascript boolean
    """
    bool = JsBoolean.JsBoolean("!(rect.bottom < 0 || rect.top - viewHeight >= 0)", varName="visibleFlag", setVar=True, isPyData=False)
    bool._js.insert(0, self._report.js.viewHeight.setVar('viewHeight'))
    bool._js.insert(0, self.getBoundingClientRect().setVar("rect"))
    return JsFncs.JsAnonymous(bool.r).return_("visibleFlag").call()

  def onViewPort(self, jsFncs):
    """
    Description:
    -----------
    Trigger some code when the component is visible on the visible part of the page (the viewpport)

    Attributes:
    ----------
    :param jsFncs: List. The Javascript events
    """
    return self._src.js.if_(self.isInViewPort, jsFncs)

  @property
  def content(self):
    """
    Description:
    -----------

    """
    return ContentFormatters(self._report, "%s.value" % self.varName)

  def empty(self): return '%s.value = ""' % self.varName

  @property
  def events(self):
    """
    Description:
    -----------
    Link to the events attached to a Javascript DOM object

    :rtype: JsNodeDom.JsDomEvents
    """
    return JsNodeDom.JsDomEvents(self._src)

  @property
  def jquery(self):
    """
    Description:
    -----------
    Link to the JQuery functions

    :rtype: JsQuery.JQuery
    """
    if self._jquery is None:
      self._jquery = JsQuery.JQuery(src=self._src, selector=JsQuery.decorate_var("#%s" % self._src.htmlCode), setVar=False)
    return self._jquery

  @property
  def d3(self):
    """
    Description:
    -----------
    Wrapper to the D3 library

    :rtype: JsD3.D3Select
    """
    if self._d3 is None:
      self._d3 = JsD3.D3Select(src=self._src, selector="d3.select('#%s')" % self._src.htmlCode)
    return self._d3

  @property
  def jquery_ui(self):
    """
    Description:
    -----------
    Wrapper to the JqueryUI component

    :rtype: JsQueryUi.JQueryUI
    """
    if self._jquery_ui is None:
      self._jquery_ui = JsQueryUi.JQueryUI(self._src, selector=JsQuery.decorate_var("#%s" % self._src.htmlCode), setVar=False)
    return self._jquery_ui

  @property
  def objects(self):
    """
    Description:
    -----------
    Interface to the main Javascript Classes and Primitives
    """
    return JsObjects.JsObjects(self)

  @property
  def crossfilter(self):
    """
    Description:
    -----------
    Interface to CrossFilter package

    Related Pages:

      https://github.com/square/crossfilter/wiki/API-Reference#group_all
    """
    return JsCrossFilter.CrossFilter

  @property
  def format(self):
    """
    Description:
    ------------
    Specific formatters for the HTML components
    """
    return Formatters(self._report, self.content.toStr())

  def style(self, attrs):
    """
    Description:
    -----------
    Style property to change from the javascript the CSS attributes of an HTML object.

    Usage::

      button.js.style({"backgroundColor": 'red'})
    button.js.style({"backgroundColor": None})

    Related Pages:

      https://www.w3.org/TR/DOM-Level-2-Style/css.html#CSS-CSSStyleRule-style

    Attributes:
    ----------
    :param attrs: Dictionary. The CSS attributes
    """
    styles = []
    for k, v in attrs.items():
      if "-" in k:
        split_css = k.split("-")
        k = "%s%s" % (split_css[0], "".join([c.title() for c in split_css[1:]]))
      styles.append("this.style.%s = %s" % (k, json.dumps(v)))
    return ";".join(styles)

  def registerFunction(self, fncName, jsFncs, pmts=None):
    """
    Description:
    -----------
    Javascript Framework extension

    Register a predefined Javascript function
    This is only dedicated to specific Javascript transformation functions

    Usage::

      Attributes:
    ----------
    :param fncName: String. The function name
    :param jsFncs: String or List. The Javascript function definition
    :param pmts:

    :return: The JsObject
    """
    jsData = JsUtils.jsConvertFncs(jsFncs)
    self._src._props.setdefault('js', {}).setdefault('functions', {})[fncName] = {'content': ";".join(jsData), 'pmt': pmts}
    return self

  def hide(self):
    """
    Description:
    -----------
    Hide the component

    Usage::

      input.js.hide()

    Related Pages:

      https://gomakethings.com/how-to-show-and-hide-elements-with-vanilla-javascript/
    """
    return self.css("display", "none")

  def show(self, inline=None, duration=None, display_value=None):
    """
    Description:
    -----------
    Display the component

    Usage::

      input.js.show()

    Related Pages:

      https://gomakethings.com/how-to-show-and-hide-elements-with-vanilla-javascript/

    Attributes:
    ----------
    :param inline: String
    :param duration: Integer. A time in second for the component display
    :param display_value: String. Optional. The display value. Default inline-block
    """
    display_value = display_value or self.display_value
    if duration is not None:
      return super(JsHtml, self).show('inline-block' if inline else display_value, duration)

    return JsUtils.jsConvertData(self.css("display", 'inline-block' if inline else display_value), None)

  def visible(self, data, inline=None, display_value=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param data: Boolean.
    :param inline: String.
    :param display_value: String.
    """
    data = JsUtils.jsConvertData(data, None)
    return JsObjects.JsVoid("if(%s){%s} else{%s}" % (data, self.show(inline, display_value=display_value).r, self.hide().r))

  def select(self):
    """
    Description:
    -----------
    Select the content of the HTMl component
    """
    return JsObjects.JsObjects.get("%s.select()" % self.varName)

  def toggle(self, attr="display", jsVal1=None, jsVal2="none"):
    """
    Description:
    ------------
    Toggle (hide / show) the display of the component

    Usage::

      input.js.toggle()
    input.js.toggle("background", "red", "blue")

    Related Pages:

      https://gomakethings.com/how-to-show-and-hide-elements-with-vanilla-javascript/

    Attributes:
    ----------
    :param attr: String.
    :param jsVal1:
    :param jsVal2:

    :return: A Javascript if statement
    """
    if attr == 'display' and jsVal1 is None:
      jsVal1 = self.display_value
    return JsIf.JsIf(self.css(attr) == jsVal2, [self.css(attr, jsVal1)]).else_([self.css(attr, jsVal2)])

  def highlight(self, css_attrs=None, time_event=1000):
    """
    Description:
    ------------

    Usage::

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

    Usage::

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
      h.options.managed = False
      jsFncs.append(self._report.js.objects.new(str(h), isPyData=True, varName="obj_%s" % i))
      jsFncs.append(self.innerHTML(self._report.js.objects.get("obj_%s" % i), append=append).r)
    return JsUtils.jsConvertFncs(jsFncs, toStr=True)

  def options(self, options=None):
    """
    Description:
    ------------
    Return the builder options used to generate the object on the Javascript side.
    This is not necessarily the same object than the component options as some can be only used on the Python side.

    This will not change the original option object used during the first obhect creation.
    
    Attributes:
    ----------
    :param options: Dictionary. Optional. The value to be changed
    """
    opt = dict(self._src._jsStyles)
    if options is not None:
      opt.update(options)
    return opt


class JsHtmlRich(JsHtml):

  @property
  def val(self):
    """
    Description:
    -----------
    Return the val object
    """
    values = ["'%s': %s" % (k, self._report.components[k].dom.content.toStr()) for k in self._src._internal_components]
    return JsObjects.JsObjects.get(
      "{%s, offset: new Date().getTimezoneOffset()}" % ", ".join(values))

  @property
  def content(self):
    return ContentFormatters(self._report, "(function(domObl){if(domObl.hasAttribute('data-value')){ return domObl.getAttribute('data-value')} else {return domObl.innerHTML}})(%(varName)s)" % {"varName": self.varName})

  def toggleContent(self, currentVal, newVal, currentJsFncs=None, newJsFncs2=None):
    """
    Description:
    -----------
    Toggle (change) the content of the HTML component

    Attributes:
    ----------
    :param currentVal: String. The content of the HTML component
    :param newVal: String. The new content of the HTML component
    :param currentJsFncs: List. Optional. The functions to be triggered when currentVal is visible
    :param newJsFncs2: List. Optional. The functions to be triggered when newVal is visible
    """
    content = JsUtils.jsConvertData(currentVal, None)
    content2 = JsUtils.jsConvertData(newVal, None)
    return JsObjects.JsVoid('''
      if(%(varName)s.innerHTML == %(content)s){%(varName)s.innerHTML = %(content2)s; %(jsFncs)s}
      else {%(varName)s.innerHTML = %(content)s; %(jsFncs2)s}
      ''' % {'varName': self.varName, 'content2': content2, 'content': content,
             'jsFncs': JsUtils.jsConvertFncs(currentJsFncs, toStr=True),
             'jsFncs2': JsUtils.jsConvertFncs(newJsFncs2, toStr=True)
             })

  def select(self):
    """
    Description:
    -----------
    Select the content of the HTMl component
    """
    return JsObjects.JsObjects.get('''
     (function(node){
      if (document.body.createTextRange) {const range = document.body.createTextRange(); range.moveToElementText(node); range.select();
      } else if (window.getSelection) {
        const selection = window.getSelection(); const range = document.createRange(); range.selectNodeContents(node);
        selection.removeAllRanges(); selection.addRange(range); }
     }(%s))''' % self.varName)

  def append(self, value, new_line=True, options=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param value:
    :param new_line:
    :param options:
    """
    value = JsUtils.jsConvertData(value, None)
    if options is not None and options.get('showdown') is not None:
      self._report.jsImports.add("showdown")
      value = '''(function(d){ var conv = new showdown.Converter(%s); 
                    let frag = document.createRange().createContextualFragment(conv.makeHtml(d)); 
                    frag.firstChild.style.display = 'inline-block';frag.firstChild.style.margin = 0;  
                    return frag.firstChild.outerHTML})(%s)''' % (json.dumps({}), value)
    if new_line:
      return JsObjects.JsObjects.get("%s.innerHTML += (%s+'<br />')" % (self.htmlCode, value))
      #return JsObjects.JsObjects.get("%s.innerHTML += (%s+'\\r\\n')" % (self.htmlCode, value))

    return JsObjects.JsObjects.get("%s.innerHTML += %s" % (self.htmlCode, value))

  def empty(self):
    """
    Description:
    ------------
    Empty the content of the HTML component using the innerHTML JavaScript property
    """
    return '%s.innerHTML = ""' % self.varName


class JsHtmlImg(JsHtml):

  @property
  def content(self):
    return ContentFormatters(self._report, "%s.src" % self.varName)

  def src(self, image):
    image = JsUtils.jsConvertData(image, None)
    return JsFncs.JsFunctions("%s.src = %s" % (self.varName, image))


class JsHtmlButton(JsHtml):

  @property
  def val(self):
    """
    Description:
    -----------

    """
    return JsObjects.JsObjects.get('''{%s: {value: %s.innerHTML, timestamp: Date.now(), 
      offset: new Date().getTimezoneOffset(), locked: %s === 'true', name: %s}}
      ''' % (self.htmlCode, self.varName, self.getAttribute('data-locked'), self.getAttribute('name')))

  @property
  def content(self):
    return ContentFormatters(self._report, "%s.innerHTML" % self.varName)

  def loading(self, flag, multiple=False):
    """
    Description:
    -----------
    Add a loading icon to the button

    Example
    b = rptObj.ui.button("test")
    b.click([
      b.dom.loading(True),
      rptObj.js.window.setTimeout([
        b.dom.loading(False)
      ], 5000),
    ])

    Attributes:
    ----------
    :param flag:
    :param multiple:
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
    Description:
    -----------

    Attributes:
    ----------
    :param time:
    :param color:
    """
    return JsFncs.JsFunction("var bgColor = %s.style.borderColor; %s.style.borderColor = '%s'; setTimeout(function() {%s.style.borderColor = bgColor}, %s)" % (self.varName, self.varName, color, self.varName, time))

  def disable(self, bool=True):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param bool:
    """
    bool = JsUtils.jsConvertData(bool, None)
    return JsFncs.JsFunctions("%s.disabled = %s" % (self.varName, bool))

  def release(self, by_name=False):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param by_name:
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
    Description:
    -----------

    Attributes:
    ----------
    :param not_allowed:
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


class JsHtmlButtonMenu(JsHtmlButton):

  @property
  def val(self):
    """
    Description:
    -----------

    """
    return JsObjects.JsObjects.get('''
        {%s: {value: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset(), label: %s.innerHTML, name: %s}}
        ''' % (self.htmlCode, self.content.toStr(), self._src.label.dom.varName, self.getAttribute('name')))

  @property
  def content(self):
    return ContentFormatters(self._report, "%s.querySelector('i').classList.contains('fa-check')" % self.varName)


class JsHtmlIcon(JsHtml):

  @property
  def val(self):
    """
    Description:
    -----------
    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (self.htmlCode, self._src.dom.getAttribute("class")))

  @property
  def content(self):
    return self._src.dom.getAttribute("class")


class JsHtmlList(JsHtml):

  @property
  def val(self):
    """
    Description:
    ------------
    Return the standard value object with the fields (value, timestamp, offset).
    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s.querySelector('[data-select=true]').innerHTML, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (self.htmlCode, self.varName))

  @property
  def content(self):
    """
    Description:
    ------------
    Return the values of the items in the list.
    """
    return JsObjects.JsArray.JsArray.get('''
      (function(){
         var values = []; %(component)s.querySelectorAll("li").forEach(function(dom){values.push(dom.innerText)});
         return values
      })()''' % {"component": self._src.dom.varName})

  @property
  def classList(self):
    """
    Description:
    ------------
    Return the class name of the list item.
    """
    return self._src.dom.getAttribute("class")

  def add(self, item, unique=True, draggable=False):
    """
    Description:
    ------------
    Add a new item to the list.

    Attributes:
    ----------
    :param item: String. The Item to be added to the list.
    :param unique: Boolean. optional. Only add the item if it is not already in the list.
    :param draggable: Boolean. Optional. Set the new entry as draggable
    """
    if hasattr(item, 'dom'):
      item = item.dom.content
    item = JsUtils.jsConvertData(item, None)
    unique = JsUtils.jsConvertData(unique, None)
    draggable = JsUtils.jsConvertData(draggable, None)
    options = JsUtils.jsConvertData(self._src.options, None)
    return JsObjects.JsVoid('''
      var listItems = %(item)s; 
      var listItemOptions = %(options)s; 
      var lenCurrentItems = %(component)s.querySelectorAll("li").length;
      if(!Array.isArray(listItems)){listItems = [listItems]};
      if ((typeof listItemOptions.max === 'undefined') || (listItemOptions.max === null) || (lenCurrentItems < listItemOptions.max)){
        listItems.forEach(function(item){
          var li = document.createElement("li");
          if(typeof listItemOptions.li_css !== 'undefined'){
            Object.keys(listItemOptions.li_css).forEach(function(key){li.style[key] = listItemOptions.li_css[key]})}
          if (%(draggable)s){
            li.setAttribute('draggable', true);
            li.addEventListener('dragstart', function(event){event.dataTransfer.setData("text", event.target.innerHTML)})
          }
          if(%(unique)s){
            var hasItems = false;
            %(component)s.querySelectorAll("li").forEach(function(dom){if (dom.innerText == item){hasItems = true}})
            if(!hasItems){
              li.appendChild(document.createTextNode(item)); li.style.cursor = "pointer"; li.style['text-align'] = "left";
              li.addEventListener("dblclick", function(){this.remove()});
              %(component)s.appendChild(li)}
          }else{
            li.appendChild(document.createTextNode(item)); li.style.cursor = "pointer"; li.style['text-align'] = "left";
            li.addEventListener("dblclick", function(){this.remove()}); %(component)s.appendChild(li)
          }
      })}''' % {"item": item, "component": self._src.dom.varName, 'unique': unique, 'draggable': draggable, "options": options})

  def clear(self):
    """
    Description:
    ------------
    Clear all the items in the list.
    """
    return JsObjects.JsVoid("%s.innerHTML = ''" % self._src.dom.varName)


class JsHtmlBackground(JsHtml):

  @property
  def val(self):
    """
    Description:
    -----------

    """
    return JsObjects.JsObjects.get("{%s: {value: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
      self.htmlCode, self.content.toStr()))

  @property
  def content(self):
    return ContentFormatters(self._report, self._src.dom.querySelector("div").css("backgroundColor").toStr())


class JsHtmlNumeric(JsHtmlRich):

  def to(self, number, timer=1):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param number:
    :param timer: Integer. the spped of the increase in millisecond
    """
    return JsUtils.jsConvertFncs([
      self._report.js.objects.number(self.content.unformat(), varName="%s_counter" % self.htmlCode, setVar=True),
      self._report.js.window.setInterval([
        self._report.js.if_(
          self._report.js.objects.number.get("window.%s_counter" % self.htmlCode) < number, [
            self._report.js.objects.number(
              self._report.js.objects.number.get("window.%s_counter" % self.htmlCode) + 1,
              varName="window.%s_counter" % self.htmlCode, setVar=True),
            self._src.build(self._report.js.objects.number.get("window.%s_counter" % self.htmlCode))
          ]).else_(self._report.js.window.clearInterval("%s_interval" % self.htmlCode))
      ], "%s_interval" % self.htmlCode, timer)
    ], toStr=True)

  def add(self, item):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param item:
    """
    return JsObjects.JsVoid('''
      %(component)s.innerText = parseFloat(%(component)s.innerText) + %(value)s
      ''' % {'value': item, 'component': self._src.dom.varName})


class JsHtmlLink(JsHtml):

  @property
  def content(self):
    return ContentFormatters(self._report, "%s.innerText" % self.varName)

  def url(self, url):
    """
    Description:
    -----------
    The href attribute specifies the URL of the page the link goes to.

    Related Pages:
    --------------
    https://www.w3schools.com/tags/att_a_href.asp

    :param url:
    """
    url = JsUtils.jsConvertData(url, None)
    return JsFncs.JsFunctions("%s.href = %s" % (self.varName, url))

  def href(self, url):
    """
    Description:
    -----------
    The href attribute specifies the URL of the page the link goes to.

    Related Pages:
    --------------
    https://www.w3schools.com/tags/att_a_href.asp

    :param url:
    """
    url = JsUtils.jsConvertData(url, None)
    return JsFncs.JsFunctions("%s.href = %s" % (self.varName, url))

  def target(self, name):
    """
    Description:
    -----------
    The target attribute specifies where to open the linked document.

    Related Pages:
    --------------
    https://www.w3schools.com/tags/att_a_target.asp

    :param url:
    """
    name = JsUtils.jsConvertData(name, None)
    return JsFncs.JsFunctions("%s.target = %s" % (self.varName, name))
