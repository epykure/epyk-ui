#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

from epyk.core.js import JsUtils
from epyk.core.html import Defaults
from epyk.core.js.statements import JsIf
from epyk.core.js.fncs import JsFncs

from epyk.core.js.objects import JsNodeDom
from epyk.core.js import JsMediaRecorder
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

    Usage:
    -----

    Related Pages:

      https://www.w3schools.com/jsref/jsref_tofixed.asp

    Attributes:
    ----------
    :param value: Integer. Optional. The number of digit to be displayed.
    """
    if value is None:
      return JsObjects.JsObjects.get("%s = %s.toFixed()" % (self.selector, self._val))

    return JsObjects.JsObjects.get("%s = %s.toFixed(%s)" % (self.selector, self._val, value))

  def toPrecision(self, value=None):
    """
    Description:
    -----------
    The toPrecision() method formats a number to a specified length.

    Usage:
    -----

    Related Pages:

      https://www.w3schools.com/jsref/jsref_toprecision.asp

    Attributes:
    ----------
    :param value: Integer. Optional. The number of digit to be displayed.
    """
    if value is None:
      return JsObjects.JsObjects.get("%s = %s.toPrecision()" % (self.selector, self._val))

    return JsObjects.JsObjects.get("%s = %s.toPrecision(%s)" % (self.selector, self._val, value))

  def toExponential(self):
    """
    Description:
    -----------
    The toExponential() method converts a number into an exponential notation.

    Usage:
    -----

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
    Standard conversion to number.

    Usage:
    -----

    Related Pages:

      https://www.w3schools.com/jsref/jsref_obj_number.asp
    """
    return FmtNumber(self._report, self.selector, "parseFloat(%s)" % self.selector)

  @packageImport("accounting")
  def toNumber(self, digit=0, thousand_sep="."):
    """
    Description:
    -----------
    Convert to number using the accounting Javascript module.

    Usage:
    -----

    Related Pages:

      https://openexchangerates.github.io/accounting.js/

    Attributes:
    ----------
    :param digit: Integer. Optional. The number of digit to be displayed.
    :param thousand_sep: String. Optional. The thousand symbol separator.
    """
    thousand_sep = JsUtils.jsConvertData(thousand_sep, None)
    return JsObjects.JsObjects.get("%s = accounting.formatNumber(%s, %s, %s)" % (self.selector, self.selector, digit, thousand_sep))

  @packageImport("accounting")
  def toMoney(self, symbol="", digit=0, thousand_sep=".", decimal_sep=","):
    """
    Description:
    -----------
    Convert to number with a symbol using the accounting Javascript module.

    Usage:
    -----

    Related Pages:

      https://openexchangerates.github.io/accounting.js/

    Attributes:
    ----------
    :param symbol: String. Optional. The currency symbol.
    :param digit: Integer. Optional. The number of digit to be displayed.
    :param thousand_sep: String. Optional. The thousand symbol separator.
    :param decimal_sep: String. Optional. The decimal symbol separator.
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
    Convert markwdown to HTML string.

    Usage:
    -----

      t.dom.content.fromMarkdown()

    Related Pages:

      https://github.com/showdownjs/showdown

    Attributes:
    ----------
    :param options: Dictionary. Optional. Options allowed in the showdown module.
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
    Convert to number using the accounting Javascript module.

    Usage:
    -----

    Related Pages:

      https://openexchangerates.github.io/accounting.js/

    Attributes:
    ----------
    :param digit: Integer. Optional. The number of digit to be displayed.
    :param thousand_sep: String. Optional. The thousand symbol separator.
    """
    thousand_sep = JsUtils.jsConvertData(thousand_sep, None)
    return JsObjects.JsObjects.get("accounting.formatNumber(%s, %s, %s)" % (self.selector, digit, thousand_sep))

  @packageImport("accounting")
  def toMoney(self, symbol="", digit=0, thousand_sep=".", decimal_sep=","):
    """
    Description:
    ------------
    Convert to number with a symbol using the accounting Javascript module.

    Usage:
    -----

    Related Pages:

      https://openexchangerates.github.io/accounting.js/

    Attributes:
    ----------
    :param symbol: String. Optional. The currency symbol.
    :param digit: Integer. Optional. The number of digit to be displayed.
    :param thousand_sep: String. Optional. The thousand symbol separator.
    :param decimal_sep: String. Optional. The decimal symbol separator.
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
    parse a value from any formatted number/currency string.

    Usage:
    -----

    Related Pages:

      http://openexchangerates.github.io/accounting.js/
    """
    return JsObjects.JsNumber.JsNumber("accounting.unformat(%s)" % self.selector)

  @property
  def number(self):
    """
    Description:
    ------------
    Standard conversion to number.

    Usage:
    -----
    """
    return JsObjects.JsNumber.JsNumber("parseFloat(%s)" % self.selector)

  @property
  def string(self):
    """
    Description:
    ------------
    Standard conversion to string.

    Usage:
    -----
    """
    return JsObjects.JsString.JsString("String(%s)" % self.selector, isPyData=False)

  @property
  def date(self):
    """
    Description:
    ------------
    Standard conversion to Date object.

    Usage:
    -----
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
    Return a Javascript val object.

    Usage:
    -----

    """
    return JsObjects.JsObjects.get("{%s: {value: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (self.htmlCode, self.content.toStr()))

  @property
  def by_name(self):
    """
    Description:
    -----------

    Usage:
    -----

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
    Check if the component is in the visible part of the page (the viewpport).

    Usage:
    -----

    :rtype: JsObject.JsObject

    :return: A Javascript boolean
    """
    bool = JsBoolean.JsBoolean("!(rect.bottom < 0 || rect.top - viewHeight >= 0)", varName="visibleFlag", setVar=True, isPyData=False)
    bool._js.insert(0, self._report.js.viewHeight.setVar('viewHeight'))
    bool._js.insert(0, self.getBoundingClientRect().setVar("rect"))
    return JsFncs.JsAnonymous(bool.r).return_("visibleFlag").call()

  def onViewPort(self, js_funcs):
    """
    Description:
    -----------
    Trigger some code when the component is visible on the visible part of the page (the viewpport).

    Usage:
    -----

    Attributes:
    ----------
    :param js_funcs: List | String. The Javascript events.
    """
    return self._src.js.if_(self.isInViewPort, js_funcs)

  @property
  def content(self):
    """
    Description:
    -----------

    Usage:
    -----
    """
    return ContentFormatters(self._report, "%s.value" % self.varName)

  def empty(self):
    """
    Description:
    -----------

    Usage:
    -----
    """
    return '%s.value = ""' % self.varName

  @property
  def events(self):
    """
    Description:
    -----------
    Link to the events attached to a Javascript DOM object.

    Usage:
    -----

    :rtype: JsNodeDom.JsDomEvents
    """
    return JsNodeDom.JsDomEvents(self._src)

  @property
  def jquery(self):
    """
    Description:
    -----------
    Link to the JQuery functions.

    Usage:
    -----

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
    Wrapper to the D3 library.

    Usage:
    -----

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
    Wrapper to the JqueryUI component.

    Usage:
    -----

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
    Interface to the main Javascript Classes and Primitives.

    Usage:
    -----

    """
    return JsObjects.JsObjects(self)

  @property
  def crossfilter(self):
    """
    Description:
    -----------
    Interface to CrossFilter package.

    Usage:
    -----

    Related Pages:

      https://github.com/square/crossfilter/wiki/API-Reference#group_all
    """
    return JsCrossFilter.CrossFilter

  @property
  def format(self):
    """
    Description:
    ------------
    Specific formatters for the HTML components.

    Usage:
    -----
    """
    return Formatters(self._report, self.content.toStr())

  def style(self, attrs):
    """
    Description:
    -----------
    Style property to change from the javascript the CSS attributes of an HTML object.

    Usage:
    -----

      button.js.style({"backgroundColor": 'red'})
      button.js.style({"backgroundColor": None})

    Related Pages:

      https://www.w3.org/TR/DOM-Level-2-Style/css.html#CSS-CSSStyleRule-style

    Attributes:
    ----------
    :param attrs: Dictionary. The CSS attributes.
    """
    styles = []
    for k, v in attrs.items():
      if "-" in k:
        split_css = k.split("-")
        k = "%s%s" % (split_css[0], "".join([c.title() for c in split_css[1:]]))
      styles.append("this.style.%s = %s" % (k, json.dumps(v)))
    return ";".join(styles)

  def registerFunction(self, fnc_name, js_funcs, pmts=None):
    """
    Description:
    -----------
    Javascript Framework extension.

    Register a predefined Javascript function.
    This is only dedicated to specific Javascript transformation functions.

    Usage:
    -----

    Attributes:
    ----------
    :param fnc_name: String. The function name.
    :param js_funcs: String | List. The Javascript function definition.
    :param pmts: List. Optional. The parameters for the function.

    :return: The JsObject
    """
    js_funcs = JsUtils.jsConvertFncs(js_funcs)
    self._src._props.setdefault('js', {}).setdefault('functions', {})[fnc_name] = {'content': ";".join(js_funcs), 'pmt': pmts}
    return self

  def hide(self):
    """
    Description:
    -----------
    Hide the component.

    Usage:
    -----

      input.js.hide()

    Related Pages:

      https://gomakethings.com/how-to-show-and-hide-elements-with-vanilla-javascript/
    """
    return self.css("display", "none")

  def show(self, inline=None, duration=None, display_value=None):
    """
    Description:
    -----------
    Display the component.

    Usage:
    -----

      input.js.show()

    Related Pages:

      https://gomakethings.com/how-to-show-and-hide-elements-with-vanilla-javascript/

    Attributes:
    ----------
    :param inline: String. Optional.
    :param duration: Integer. Optional. A time in second for the component display.
    :param display_value: String. Optional. The display value. Default inline-block.
    """
    display_value = display_value or self.display_value
    if duration is not None:
      return super(JsHtml, self).show('inline-block' if inline else display_value, duration)

    return JsUtils.jsConvertData(self.css("display", 'inline-block' if inline else display_value), None)

  def visible(self, data, inline=None, display_value=None):
    """
    Description:
    -----------

    Usage:
    -----

    Attributes:
    ----------
    :param data: Boolean.
    :param inline: String. Optional.
    :param display_value: String. Optional.
    """
    data = JsUtils.jsConvertData(data, None)
    return JsObjects.JsVoid("if(%s){%s} else{%s}" % (data, self.show(inline, display_value=display_value).r, self.hide().r))

  def select(self):
    """
    Description:
    -----------
    Select the content of the HTMl component.

    Usage:
    -----

    """
    return JsObjects.JsObjects.get("%s.select()" % self.varName)

  def toggle(self, attr="display", jsVal1=None, jsVal2="none"):
    """
    Description:
    ------------
    Toggle (hide / show) the display of the component.

    Usage:
    -----

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

    Usage:
    -----

      s.dom.highlight()
      s.dom.highlight(css_attrs={"background": "red"}),

    Attributes:
    ----------
    :param css_attrs: Dictionary. Optional. he CSS attributes.
    :param time_event: Integer. Optional. The time of the event.
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

  def loadHtml(self, components, append=False):
    """
    Description:
    ------------
    Load during a Javascript event a component within the one using this method.
    This cannot be tested during the Python execution and should be tested in the browser.

    Tip: It is possible to add a break point to debug in the browser by adding.

    Usage:
    -----

      d = rptObj.ui.div().css({"border": "1px solid black"})
      b = rptObj.ui.button("test")
      b.click([
        rptObj.js.console.debugger,
        d.dom.loadHtml(rptObj.ui.texts.label("test label").css({"color": 'blue', 'float': 'none'}))
      ])

    Attributes:
    ----------
    :param components: List. The different HTML objects to be added to the component.
    :param append: Boolean. Mention if the component should replace or append the data.

    :return: The Javascript string to be added to the page
    """
    if not isinstance(components, list):
      components = [components]

    js_funcs = []
    for i, h in enumerate(components):
      h.options.managed = False
      js_funcs.append(self._report.js.objects.new(str(h), isPyData=True, varName="obj_%s" % i))
      js_funcs.append(self.innerHTML(self._report.js.objects.get("obj_%s" % i), append=append).r)
    return JsUtils.jsConvertFncs(js_funcs, toStr=True)

  def options(self, options=None):
    """
    Description:
    ------------
    Return the builder options used to generate the object on the Javascript side.
    This is not necessarily the same object than the component options as some can be only used on the Python side.

    This will not change the original option object used during the first object creation.

    Usage:
    -----

    Attributes:
    ----------
    :param options: Dictionary. Optional. The value to be changed.
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
    Return the val object.

    Usage:
    -----

    """
    values = ["'%s': %s" % (k, self._report.components[k].dom.content.toStr()) for k in self._src._internal_components]
    return JsObjects.JsObjects.get(
      "{%s, offset: new Date().getTimezoneOffset()}" % ", ".join(values))

  @property
  def content(self):
    """
    Description:
    -----------

    Usage:
    -----

    """
    return ContentFormatters(self._report, "(function(domObl){if(domObl.hasAttribute('data-value')){ return domObl.getAttribute('data-value')} else {return domObl.innerHTML}})(%(varName)s)" % {"varName": self.varName})

  def toggleContent(self, currentVal, newVal, currentJsFncs=None, newJsFncs2=None):
    """
    Description:
    -----------
    Toggle (change) the content of the HTML component.

    Usage:
    -----

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
    Select the content of the HTMl component.

    Usage:
    -----

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

    Usage:
    -----

    Attributes:
    ----------
    :param value:
    :param new_line: Boolean. Optional.
    :param options: Dictionary. Optional.
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
    Empty the content of the HTML component using the innerHTML JavaScript property.

    Usage:
    -----
    """
    return '%s.innerHTML = ""' % self.varName


class JsHtmlImg(JsHtml):

  @property
  def content(self):
    """
    Description:
    -----------

    Usage:
    -----

    """
    return ContentFormatters(self._report, "%s.src" % self.varName)

  def src(self, image):
    """
    Description:
    -----------

    Usage:
    -----

    Attributes:
    ----------
    :param image: String.
    """
    image = JsUtils.jsConvertData(image, None)
    return JsFncs.JsFunctions("%s.src = %s" % (self.varName, image))


class JsHtmlButton(JsHtml):

  @property
  def val(self):
    """
    Description:
    -----------

    Usage:
    -----

    """
    return JsObjects.JsObjects.get('''{%s: {value: %s.innerHTML, timestamp: Date.now(), 
      offset: new Date().getTimezoneOffset(), locked: %s === 'true', name: %s}}
      ''' % (self.htmlCode, self.varName, self.getAttribute('data-locked'), self.getAttribute('name')))

  @property
  def content(self):
    """
    Description:
    -----------

    Usage:
    -----

    """
    return ContentFormatters(self._report, "%s.innerHTML" % self.varName)

  def loading(self, flag, multiple=False):
    """
    Description:
    -----------
    Add a loading icon to the button.

    Usage:
    -----

      b = rptObj.ui.button("test")
      b.click([
        b.dom.loading(True),
        rptObj.js.window.setTimeout([
          b.dom.loading(False)
        ], 5000),
      ])

    Attributes:
    ----------
    :param flag: Boolean. Optional.
    :param multiple: Boolean. Optional.
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

    Usage:
    -----

    Attributes:
    ----------
    :param time:
    :param color: String. Optional.
    """
    return JsFncs.JsFunction("var bgColor = %s.style.borderColor; %s.style.borderColor = '%s'; setTimeout(function() {%s.style.borderColor = bgColor}, %s)" % (self.varName, self.varName, color, self.varName, time))

  def disable(self, flag=True):
    """
    Description:
    -----------

    Usage:
    -----

    Attributes:
    ----------
    :param flag: Boolean. Optional.
    """
    flag = JsUtils.jsConvertData(flag, None)
    return JsFncs.JsFunctions("%s.disabled = %s" % (self.varName, flag))

  def release(self, by_name=False):
    """
    Description:
    -----------

    Usage:
    -----

    Attributes:
    ----------
    :param by_name: Boolean. Optional.
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

    Usage:
    -----

    Attributes:
    ----------
    :param not_allowed: Boolean. Optional.
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

  def empty(self):
    """
    Description:
    -----------

    Usage:
    -----

    """
    return '%s.innerHTML = ""' % self.varName


class JsHtmlButtonChecks(JsHtml):

  @property
  def val(self):
    """
    Description:
    -----------
    Get the full content of the list.

    This will return the current list status. Selected items but also the full content.
    It will return also the common parameters.

    Usage:
    -----

    """
    return ""

  @property
  def content(self):
    """
    Description:
    -----------
    Get the content of the list.

    This will return all the selected items in a list.

    Usage:
    -----

    """
    return ""

  def disable(self):
    """
    Description:
    -----------

    Usage:
    -----

    """
    return JsObjects.JsObjects.get('''
      ''')

  def add(self, jsData, is_unique=True, css_style=None, position="bottom"):
    """
    Description:
    -----------
    Add an item to the list.

    THis will add the item at the end of the list by default.
    By default the list will not add duplicated entries.

    Usage:
    -----

    Attributes:
    ----------
    :param jsData: List of dict | JsObj.
    :param is_unique: Boolean. Optional. Flag to specify if only distinct values should be added (no duplicates).
    :param css_style: Dictionary. Optional. The CSS style of the added item.
    :param position: String. Optional. The position of the new item in the list (bottom or top).
    """
    css_style = css_style or {'margin': 0, 'display': 'block', 'position': 'relative', 'cursor': 'pointer'}
    is_unique = JsUtils.jsConvertData(is_unique, None)
    jsData = JsUtils.jsConvertData(jsData, None)
    css_style = JsUtils.jsConvertData(css_style, None)
    return JsObjects.JsObjects.get('''
      var existingCols = {}; var options = %(options)s;
      if (%(unique)s){%(jqId)s.find('span').each(function(){
        var pItem = $(this); existingCols[pItem.data('content')] = true})};
      %(jsData)s.forEach(function(rec){
        if ((!%(unique)s) || (%(unique)s && (!(rec.value in existingCols))) ){
          var style = %(styls)s;
          var strCss = []; for (key in style) {strCss.push(key + ":" + style[key])}; checkData = '&nbsp;';
          if (rec.color != undefined){style.color = rec.color};
          if (rec.name == undefined) {rec.name = rec.value};
          if (rec.checked){var checkData = '<i class="'+ options.icon + '" style="margin:2px"></i>'};
          var spanContent = '<span data-content="'+ rec.value + '" style="width:16px;display:inline-block;float:left;margin:0">'+ checkData +'</span><p style="margin:0" title="'+ rec.dsc + '">' + rec.name + '</p>';
          %(jqId)s.append($('<label style="' + strCss.join(";") + '">'+ spanContent +'</label>'))}
      }) ''' % {"styls": css_style, "options": {}, "jqId": self.jquery.varId, "unique": is_unique, "jsData": jsData})

  def empty(self):
    """
    Description:
    -----------
    Empty the list content.

    Usage:
    -----
    """
    return '%s.empty()' % self.jquery.varId

  def delete(self, jsData):
    """
    Description:
    -----------

    Usage:
    -----

    Attributes:
    ----------
    :param jsData:
    """
    jsData = JsUtils.jsConvertData(jsData, None)
    return JsObjects.JsObjects.get('''
      var compData = %(jsData)s;
      if (compData === true) {%(jqId)s.empty()}
      else {%(jqId)s.find('span').each(function(){
          if (compData.indexOf($(this).data('content')) > -1){$(this).parent().remove()}
      })}''' % {"jsData": jsData, "jqId": self.jquery.varId})

  def check(self, jsData):
    """
    Description:
    -----------

    Usage:
    -----

    Attributes:
    ----------
    :param jsData:
    """
    jsData = JsUtils.jsConvertData(jsData, None)
    return JsObjects.JsObjects.get('''
      var compData = %(jsData)s;
      %(jqId)s.find('span').each(function(){
        var itemCode = $(this).data('content');
        if(typeof compData === "boolean"){
          if (compData === true && $(this).find("i").attr("class") === undefined){$(this).trigger("click")}
          if (!compData && $(this).find("i").attr("class") !== undefined){$(this).trigger("click")}}
        else if (compData.indexOf(itemCode) > -1){if ($(this).find("i").attr("class") === undefined){$(this).trigger("click")}}
      })''' % {"jsData": jsData, "jqId": self.jquery.varId})

  @property
  def current(self):
    """
    Description:
    -----------
    Return the current value in the list.

    Usage:
    -----

    """
    return JsObjects.JsVoid("$(this).find('p').text()")

  def css_label(self, jsData, attrs):
    """
    Description:
    -----------

    Usage:
    -----

    Attributes:
    ----------
    :param jsData:
    :param attrs: Dictionary.
    """
    jsData = JsUtils.jsConvertData(jsData, None)
    attrs = JsUtils.jsConvertData(attrs, None)
    return JsObjects.JsObjects.get('''
      var compData = %(jsData)s; var compAttrs = %(attrs)s;
      %(jqId)s.find('span').each(function(){
        var itemCode = $(this).data('content');
        if (compData.indexOf(itemCode) > -1){$(this).parent().find("p").css(compAttrs)}
      }) ''' % {"jsData": jsData, "jqId": self.jquery.varId, "attrs": attrs})


class JsHtmlButtonMenu(JsHtmlButton):

  @property
  def val(self):
    """
    Description:
    -----------

    Usage:
    -----

    """
    return JsObjects.JsObjects.get('''
        {%s: {value: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset(), label: %s.innerHTML, name: %s}}
        ''' % (self.htmlCode, self.content.toStr(), self._src.label.dom.varName, self.getAttribute('name')))

  @property
  def content(self):
    """
    Description:
    -----------

    Usage:
    -----

    """
    check = self._src.options.icon_check.split(" ")[-1]
    return ContentFormatters(self._report, "%s.querySelector('i').classList.contains('%s')" % (self.varName, check))


class JsHtmlIcon(JsHtml):

  @property
  def val(self):
    """
    Description:
    -----------

    Usage:
    -----

    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (self.htmlCode, self._src.dom.getAttribute("class")))

  @property
  def content(self):
    """
    Description:
    -----------

    Usage:
    -----

    """
    return self._src.dom.getAttribute("class")


class JsHtmlList(JsHtml):

  @property
  def val(self):
    """
    Description:
    ------------
    Return the standard value object with the fields (value, timestamp, offset).

    Usage:
    -----

    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s.querySelector('[data-select=true]').innerHTML, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (self.htmlCode, self.varName))

  @property
  def content(self):
    """
    Description:
    ------------
    Return the values of the items in the list.

    Usage:
    -----

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

    Usage:
    -----

    """
    return self._src.dom.getAttribute("class")

  def add(self, item, unique=True, draggable=False):
    """
    Description:
    ------------
    Add a new item to the list.

    Usage:
    -----


    Attributes:
    ----------
    :param item: String. The Item to be added to the list.
    :param unique: Boolean. optional. Only add the item if it is not already in the list.
    :param draggable: Boolean. Optional. Set the new entry as draggable.
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

    Usage:
    -----

    """
    return JsObjects.JsVoid("%s.innerHTML = ''" % self._src.dom.varName)

  @property
  def dropped_value(self):
    """
    Description:
    ------------
    Get the current dropped values to the list.
    Object can be structure (DOM) so the text content is wrapped in a specific variable.
    """
    return JsObjects.JsString.JsString.get("wrapper.innerText")


class JsHtmlBackground(JsHtml):

  @property
  def val(self):
    """
    Description:
    -----------

    Usage:
    -----


    """
    return JsObjects.JsObjects.get("{%s: {value: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
      self.htmlCode, self.content.toStr()))

  @property
  def content(self):
    """
    Description:
    -----------

    Usage:
    -----

    """
    return ContentFormatters(self._report, self._src.dom.querySelector("div").css("backgroundColor").toStr())


class JsHtmlNumeric(JsHtmlRich):

  def to(self, number, timer=1):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param number: Float.
    :param timer: Integer. the ppend of the increase in millisecond.
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
    Add a value to the component value.

    Usage:
    -----

    Attributes:
    ----------
    :param item: Float. The value to be added.
    """
    return JsObjects.JsVoid('''
      %(component)s.innerText = parseFloat(%(component)s.innerText) + %(value)s
      ''' % {'value': item, 'component': self._src.dom.varName})


class JsHtmlLink(JsHtml):

  @property
  def content(self):
    """
    Description:
    -----------

    Usage:
    -----

    """
    return ContentFormatters(self._report, "%s.innerText" % self.varName)

  def url(self, url):
    """
    Description:
    -----------
    The href attribute specifies the URL of the page the link goes to.

    Usage:
    -----

    Related Pages:
    --------------

      https://www.w3schools.com/tags/att_a_href.asp

    Attributes:
    ----------
    :param url: String. The url path.
    """
    url = JsUtils.jsConvertData(url, None)
    return JsFncs.JsFunctions("%s.href = %s" % (self.varName, url))

  def href(self, url):
    """
    Description:
    -----------
    The href attribute specifies the URL of the page the link goes to.

    Usage:
    -----

    Related Pages:
    --------------

      https://www.w3schools.com/tags/att_a_href.asp

    Attributes:
    ----------
    :param url: String. The url path.
    """
    url = JsUtils.jsConvertData(url, None)
    return JsFncs.JsFunctions("%s.href = %s" % (self.varName, url))

  def target(self, name):
    """
    Description:
    -----------
    The target attribute specifies where to open the linked document.

    Usage:
    -----

    Related Pages:
    --------------

      https://www.w3schools.com/tags/att_a_target.asp

    Attributes:
    ----------
    :param name: String. The target name.
    """
    name = JsUtils.jsConvertData(name, None)
    return JsFncs.JsFunctions("%s.target = %s" % (self.varName, name))


class JsMedia(JsHtml):

  # TODO: Implement properly this with JsMediaRecorder

  def start(self):
    """
    Description:
    -----------
    Start the cmera.
    This can only work with https and localhost urls.

    Usage:
    -----

    Related Pages:
    --------------

      https://developer.mozilla.org/fr/docs/WebRTC/Prendre_des_photos_avec_la_webcam
    """
    return '''
      var mediaConfig =  { video: true };
    if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
              navigator.mediaDevices.getUserMedia(mediaConfig).then(function(stream) {
      %(varId)s.srcObject = stream; %(varId)s.play();});
      }
    else if(navigator.getUserMedia) { 
      navigator.getUserMedia(mediaConfig, function(stream) {
        %(varId)s.src = stream; %(varId)s.play();
      }, errBack);
    } else if(navigator.webkitGetUserMedia) {
      navigator.webkitGetUserMedia(mediaConfig, function(stream){
        %(varId)s.src = window.webkitURL.createObjectURL(stream); %(varId)s.play();
      }, errBack);
    } else if(navigator.mozGetUserMedia) {
      navigator.mozGetUserMedia(mediaConfig, function(stream){
        %(varId)s.src = window.URL.createObjectURL(stream); %(varId)s.play();
      }, errBack);
    } ''' % {"varId": self.varId}

  def stop(self):
    """
    Description:
    -----------

    Usage:
    -----

    Related Pages:
    --------------

      https://developer.mozilla.org/fr/docs/WebRTC/Prendre_des_photos_avec_la_webcam
    """
    return '''
      var stream = %s.srcObject; var tracks = stream.getTracks();
      for (var i = 0; i < tracks.length; i++) {
        var track = tracks[i]; track.stop()}
      video.srcObject = null;
      ''' % self.varId

  def play(self):
    return '''%s.play()''' % self.varId

  def takepicture(self, width=50, height=50):
    """
    Description:
    -----------

    Usage:
    -----

    Related Pages:
    --------------

      https://developer.mozilla.org/fr/docs/WebRTC/Prendre_des_photos_avec_la_webcam
    """
    return '''
      var canvas = document.createElement("canvas");
      canvas.width = %(width)s; canvas.height = %(height)s;
      canvas.getContext('2d').drawImage(%(varId)s, 0, 0, canvas.width, canvas.height);
      var data = canvas.toDataURL('image/png');
      photo.setAttribute('src', data);
      ''' % {"varId": self.varId, "width": width, "height": height}

  def record(self, start=True):
    """
    Description:
    -----------

    Usage:
    -----

    Related Pages:
    --------------

      https://developer.mozilla.org/fr/docs/WebRTC/Prendre_des_photos_avec_la_webcam
    """
    if not start:
      return '''
        window.recorder.stop()
        '''

    return '''
      var stream = %(varId)s.srcObject;
      window.recorder = new MediaRecorder(stream, {mimeType: 'video/webm'});
      
      const chunks = [];
      window.recorder.ondataavailable = e => chunks.push(e.data);
      window.recorder.onstop = e => {
          const blob = new Blob(chunks, { type: chunks[0].type });
          stream.getVideoTracks()[0].stop();
      
          filename="yourCustomFileName"
          if(window.navigator.msSaveOrOpenBlob) {
              window.navigator.msSaveBlob(blob, filename);
          }
          else{
              var elem = window.document.createElement('a');
              elem.href = window.URL.createObjectURL(blob);
              elem.download = filename;        
              document.body.appendChild(elem);
              elem.click();        
              document.body.removeChild(elem);
          }
          };
      window.recorder.start();
      ''' % {"varId": self.varId}

