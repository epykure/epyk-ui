#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union, Optional, List
from epyk.core.py import primitives

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


class FmtNumber:

  def __init__(self, report: primitives.PageModel, selector: str, value):
    self._report, self._val = report, value
    self.selector = selector

  def toFixed(self, value: Optional[int] = None):
    """
    Description:
    -----------
    The toFixed() method converts a number into a string, keeping a specified number of decimals.

    Related Pages:

      https://www.w3schools.com/jsref/jsref_tofixed.asp

    Attributes:
    ----------
    :param Optional[int] value: Optional. The number of digit to be displayed.
    """
    if value is None:
      return JsObjects.JsObjects.get("%s = %s.toFixed()" % (self.selector, self._val))

    return JsObjects.JsObjects.get("%s = %s.toFixed(%s)" % (self.selector, self._val, value))

  def toPrecision(self, value: Optional[int] = None):
    """
    Description:
    -----------
    The toPrecision() method formats a number to a specified length.

    Related Pages:

      https://www.w3schools.com/jsref/jsref_toprecision.asp

    Attributes:
    ----------
    :param Optional[int] value: Optional. The number of digit to be displayed.
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


class Formatters:

  def __init__(self, report: primitives.PageModel, selector: str):
    self._report = report
    self.selector = selector

  @property
  def number(self):
    """
    Description:
    -----------
    Standard conversion to number.

    Related Pages:

      https://www.w3schools.com/jsref/jsref_obj_number.asp
    """
    return FmtNumber(self._report, self.selector, "parseFloat(%s)" % self.selector)

  @packageImport("accounting")
  def toNumber(self, digit: int = 0, thousand_sep: List[Union[str, primitives.JsDataModel]] = "."):
    """
    Description:
    -----------
    Convert to number using the accounting Javascript module.

    Related Pages:

      https://openexchangerates.github.io/accounting.js/

    Attributes:
    ----------
    :param int digit: Optional. The number of digit to be displayed.
    :param str thousand_sep: Optional. The thousand symbol separator.
    """
    thousand_sep = JsUtils.jsConvertData(thousand_sep, None)
    return JsObjects.JsObjects.get("%s = accounting.formatNumber(%s, %s, %s)" % (
      self.selector, self.selector, digit, thousand_sep))

  @packageImport("accounting")
  def toMoney(self, symbol: str = "", digit: int = 0, thousand_sep: str = ".", decimal_sep: str = ","):
    """
    Description:
    -----------
    Convert to number with a symbol using the accounting Javascript module.

    Related Pages:

      https://openexchangerates.github.io/accounting.js/

    Attributes:
    ----------
    :param str symbol: Optional. The currency symbol.
    :param int digit: Optional. The number of digit to be displayed.
    :param str thousand_sep: Optional. The thousand symbol separator.
    :param str decimal_sep: Optional. The decimal symbol separator.
    """
    symbol = JsUtils.jsConvertData(symbol, None)
    thousand_sep = JsUtils.jsConvertData(thousand_sep, None)
    decimal_sep = JsUtils.jsConvertData(decimal_sep, None)
    return JsObjects.JsObjects.get("%s = accounting.formatMoney(%s, %s, %s, %s, %s)" % (
      self.selector, self.selector, symbol, digit, thousand_sep, decimal_sep))


class ContentFormatters:

  def __init__(self, report: primitives.PageModel, selector: str):
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

  def __truediv__(self, obj):
    return JsObjects.JsObjects.get("%s / %s" % (self.selector, JsUtils.jsConvertData(obj, None)))

  def __floordiv__(self, obj):
    return JsObjects.JsObjects.get("%s // %s" % (self.selector, JsUtils.jsConvertData(obj, None)))

  def isTrue(self):
    return JsObjects.JsObjects.get("%s == true" % self.selector)

  @packageImport("showdown")
  def fromMarkdown(self, options: Optional[dict] = None):
    """
    Description:
    ------------
    Convert markdown to HTML string.

    Usage::

      t.dom.content.fromMarkdown()

    Related Pages:

      https://github.com/showdownjs/showdown

    Attributes:
    ----------
    :param Optional[dict] options: Optional. Options allowed in the showdown module.
    """
    options = JsUtils.jsConvertData(options or {}, None)
    return JsObjects.JsObjects.get(
      "%s = (function(){ var conv = new showdown.Converter(%s); return conv.makeHtml(%s)})()" % (
        self.selector, options, self.selector))

  @packageImport("accounting")
  def toNumber(self, digit: int = 0, thousand_sep: str = "."):
    """
    Description:
    -----------
    Convert to number using the accounting Javascript module.

    Related Pages:

      https://openexchangerates.github.io/accounting.js/

    Attributes:
    ----------
    :param int digit: Optional. The number of digit to be displayed.
    :param str thousand_sep: Optional. The thousand symbol separator.
    """
    thousand_sep = JsUtils.jsConvertData(thousand_sep, None)
    return JsObjects.JsObjects.get("accounting.formatNumber(%s, %s, %s)" % (self.selector, digit, thousand_sep))

  @packageImport("accounting")
  def toMoney(self, symbol: str = "", digit: int = 0, thousand_sep: str = ".", decimal_sep: str = ","):
    """
    Description:
    ------------
    Convert to number with a symbol using the accounting Javascript module.

    Related Pages:

      https://openexchangerates.github.io/accounting.js/

    Attributes:
    ----------
    :param str symbol: Optional. The currency symbol.
    :param int digit: Optional. The number of digit to be displayed.
    :param str thousand_sep: Optional. The thousand symbol separator.
    :param str decimal_sep: Optional. The decimal symbol separator.
    """
    symbol = JsUtils.jsConvertData(symbol, None)
    thousand_sep = JsUtils.jsConvertData(thousand_sep, None)
    decimal_sep = JsUtils.jsConvertData(decimal_sep, None)
    return JsObjects.JsObjects.get("accounting.formatMoney(%s,%s, %s, %s, %s)" % (
      self.selector, symbol, digit, thousand_sep, decimal_sep))

  @packageImport("accounting")
  def unformat(self):
    """
    Description:
    ------------
    parse a value from any formatted number/currency string.

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
    """
    return JsObjects.JsNumber.JsNumber("parseFloat(%s)" % self.selector)

  @property
  def string(self):
    """
    Description:
    ------------
    Standard conversion to string.
    """
    return JsObjects.JsString.JsString("String(%s)" % self.selector, isPyData=False)

  @property
  def date(self):
    """
    Description:
    ------------
    Standard conversion to Date object.
    """
    return JsObjects.JsDate.JsDate("new Date(%s)" % self.selector)

  def toStr(self):
    return self.selector

  @property
  def dict(self):
    return JsObjects.JsObject.JsObject.get("%s" % self.selector)

  @property
  def toJson(self):
    """ Cast the Javascript object to a Json object """
    return JsObjects.JsObject.JsObject.get("JSON.parse(%s)" % self.selector)


class JsHtml(JsNodeDom.JsDoms):
  display_value = "inline-block"

  def __init__(self, htmlObj, varName: Optional[str] = None, setVar: bool = True, isPyData: bool = True, report=None):
    self.htmlCode = varName if varName is not None else htmlObj.htmlCode
    self.varName, self.varData, self.__var_def = "document.getElementById('%s')" % self.htmlCode, "", None
    self._src, self._report = htmlObj, report
    self.component, self.page = htmlObj, report
    self._js = []
    self._jquery, self._jquery_ui, self._d3 = None, None, None

  @property
  def val(self):
    """
    Description:
    -----------
    Return a Javascript val object.
    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
        self.htmlCode, self.content.toStr()))

  @property
  def by_name(self):
    """
    Description:
    -----------

    :rtype: JsNodeDom.JsDomsList
    """
    if self._src.attr.get('name') is not None:
      return JsNodeDom.JsDomsList(
        None, "document.getElementsByName('%s')" % self._src.attr.get('name'), report=self._report)

    return self

  @property
  def isInViewPort(self):
    """
    Description:
    -----------
    Check if the component is in the visible part of the page (the viewpport).

    :rtype: JsObject.JsObject

    :return: A Javascript boolean
    """
    bool = JsBoolean.JsBoolean(
      "!(rect.bottom < 0 || rect.top - viewHeight >= 0)", varName="visibleFlag", setVar=True, isPyData=False)
    bool._js.insert(0, self._report.js.viewHeight.setVar('viewHeight'))
    bool._js.insert(0, self.getBoundingClientRect().setVar("rect"))
    return JsFncs.JsAnonymous(bool.r).return_("visibleFlag").call()

  def onViewPort(self, js_funcs: Union[list, str]):
    """
    Description:
    -----------
    Trigger some code when the component is visible on the visible part of the page (the viewpport).

    Attributes:
    ----------
    :param Union[list, str] js_funcs: The Javascript events.
    """
    return self._src.js.if_(self.isInViewPort, js_funcs)

  def copyToClipboard(self, include_html: bool = False):
    """
    Description:
    -----------
    Copy the component content to the clipboard.

    Attributes:
    ----------
    :param bool include_html: Optional. Store the full HTML (Default False).
    """
    if include_html:
      return self.page.js.clipboard(self.innerHTML())

    return self.page.js.clipboard(self.innerText())

  @property
  def content(self):
    """
    Description:
    -----------

    """
    if self._src.attr.get('type') == "number":
      return ContentFormatters(self._report, "parseFloat(%s.value)" % self.varName)

    return ContentFormatters(self._report, "%s.value" % self.varName)

  def empty(self):
    """
    Description:
    -----------

    """
    return '%s.value = ""' % self.varName

  @property
  def events(self):
    """
    Description:
    -----------
    Link to the events attached to a Javascript DOM object.

    :rtype: JsNodeDom.JsDomEvents
    """
    return JsNodeDom.JsDomEvents(self._src)

  @property
  def jquery(self):
    """
    Description:
    -----------
    Link to the JQuery functions.

    :rtype: JsQuery.JQuery
    """
    if self._jquery is None:
      self._jquery = JsQuery.JQuery(
        src=self._src, selector=JsQuery.decorate_var("#%s" % self._src.htmlCode), setVar=False)
    return self._jquery

  @property
  def d3(self):
    """
    Description:
    -----------
    Wrapper to the D3 library.

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

    :rtype: JsQueryUi.JQueryUI
    """
    if self._jquery_ui is None:
      self._jquery_ui = JsQueryUi.JQueryUI(
        self._src, selector=JsQuery.decorate_var("#%s" % self._src.htmlCode), setVar=False)
    return self._jquery_ui

  @property
  def objects(self):
    """
    Description:
    -----------
    Interface to the main Javascript Classes and Primitives.
    """
    return JsObjects.JsObjects(self)

  @property
  def crossfilter(self):
    """
    Description:
    -----------
    Interface to CrossFilter package.

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
    """
    return Formatters(self._report, self.content.toStr())

  def style(self, attrs: dict):
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
    :param dict attrs: The CSS attributes.
    """
    styles = []
    for k, v in attrs.items():
      if "-" in k:
        split_css = k.split("-")
        k = "%s%s" % (split_css[0], "".join([c.title() for c in split_css[1:]]))
      styles.append("this.style.%s = %s" % (k, json.dumps(v)))
    return ";".join(styles)

  def registerFunction(self, fnc_name: str, js_funcs: Union[list, str], pmts: Optional[list] = None,
                       profile: Optional[Union[dict, bool]] = None):
    """
    Description:
    -----------
    Javascript Framework extension.

    Register a predefined Javascript function.
    This is only dedicated to specific Javascript transformation functions.

    Attributes:
    ----------
    :param str fnc_name: The function name.
    :param Union[list, str] js_funcs: The Javascript function definition.
    :param Optional[list] pmts: Optional. The parameters for the function.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.

    :return: The JsObject
    """
    js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    self._src._props.setdefault('js', {}).setdefault('functions', {})[fnc_name] = {
      'content': js_funcs, 'pmt': pmts}
    return self

  def hide(self):
    """
    Description:
    -----------
    Hide the component.

    Usage::

      input.js.hide()

    Related Pages:

      https://gomakethings.com/how-to-show-and-hide-elements-with-vanilla-javascript/
    """
    return self.css("display", "none")

  def show(self, inline: Optional[str] = None, duration: Optional[int] = None, display_value: Optional[str] = None):
    """
    Description:
    -----------
    Show the component.

    This will use the display attribute of the component.

    Usage::

      input.js.show()

    Related Pages:

      https://gomakethings.com/how-to-show-and-hide-elements-with-vanilla-javascript/

    Attributes:
    ----------
    :param Optional[str] inline: Optional. Set the CSS display attribute to inline-block instead of block.
    :param Optional[int] duration: Optional. A time in second for the component display.
    :param Optional[str] display_value: Optional. The display value. Default inline-block.
    """
    display_value = display_value or self.display_value
    if duration is not None:
      return super(JsHtml, self).show('inline-block' if inline else display_value, duration)

    return JsUtils.jsConvertData(self.css("display", 'inline-block' if inline else display_value), None)

  def display(self, flag: bool, inline: Optional[str] = None, display_value: Optional[str] = None):
    """
    Description:
    -----------
    Change the CSS display attribute.

    Related Pages:

      https://www.w3schools.com/cssref/pr_class_display.asp

    Attributes:
    ----------
    :param bool flag: A flag to specify the display type show or None.
    :param Optional[str] inline: Optional. Set the CSS display attribute to inline-block instead of block.
    :param Optional[str] display_value:  Optional. The default CSS attribute for this component.
    """
    flag = JsUtils.jsConvertData(flag, None)
    return JsObjects.JsVoid("if(%s){%s} else{%s}" % (
      flag, self.show(inline, display_value=display_value).r, self.hide().r))

  def visible(self, flag: bool = True, inverse: bool = False):
    """
    Description:
    -----------
    The visibility property specifies whether or not an element is visible.

    Tip: Hidden elements take up space on the page. Use the display property to both hide and remove an element from
    the document layout!

    Related Pages:

      https://www.w3schools.com/cssref/pr_class_visibility.asp

    Usage::

      mode_switch = page.ui.fields.toggle({"off": 'hidden', "on": "visible"}, is_on=True, label="", htmlCode="switch")
      mode_switch.input.click([
        icon.dom.visible(mode_switch.input.dom.content)
      ])

    Attributes:
    ----------
    :param bool flag: Optional. specify the state of the component. Default True.
    :param bool inverse: Optional. To specify the effect of the data flag.
    """
    flag = JsUtils.jsConvertData(flag, None)
    if inverse:
      return self.css("visibility", JsObjects.JsVoid(
        "(function(flag){if(flag){ return 'hidden' } else {return 'visible'}})(%s)" % flag)).r

    return self.css("visibility", JsObjects.JsVoid(
      "(function(flag){if(!flag){ return 'hidden' } else {return 'visible'}})(%s)" % flag)).r

  def invisible(self):
    """
    Description:
    -----------
    The visibility property specifies whether or not an element is visible.

    Tip: Hidden elements take up space on the page. Use the display property to both hide and remove an element from
    the document layout!

    Related Pages:

      https://www.w3schools.com/cssref/pr_class_visibility.asp

    Usage::

      icon = page.web.bs.icons.danger()
      icon.style.css.invisble()
    """
    return self.css("visibility", "hidden").r

  def select(self):
    """
    Description:
    -----------
    Select the content of the HTMl component.
    """
    return JsObjects.JsObjects.get("%s.select()" % self.varName)

  def toggle(self, attr: str = "display", jsVal1: Optional[str] = None, jsVal2: str = "none"):
    """
    Description:
    ------------
    Toggle (hide / show) the display of the component.

    Usage::

      input.js.toggle()
      input.js.toggle("background", "red", "blue")

    Related Pages:

      https://gomakethings.com/how-to-show-and-hide-elements-with-vanilla-javascript/

    Attributes:
    ----------
    :param str attr:
    :param Optional[str] jsVal1:
    :param str jsVal2:

    :return: A Javascript if statement
    """
    if attr == 'display' and jsVal1 is None:
      jsVal1 = self.display_value
    return JsIf.JsIf(self.css(attr) == jsVal2, [self.css(attr, jsVal1)]).else_([self.css(attr, jsVal2)])

  def highlight(self, css_attrs: Optional[dict] = None, time_event: int = 1000):
    """
    Description:
    ------------

    Usage::

      s.dom.highlight()
      s.dom.highlight(css_attrs={"background": "red"}),

    Attributes:
    ----------
    :param Optional[dict] css_attrs:  Optional. The CSS attributes.
    :param int time_event: Optional. The time of the event.
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

  def loadHtml(self, components: list, append: bool = False, profile: Optional[Union[dict, bool]] = None):
    """
    Description:
    ------------
    Load during a Javascript event a component within the one using this method.
    This cannot be tested during the Python execution and should be tested in the browser.

    Tip: It is possible to add a break point to debug in the browser by adding.

    Usage::

      d = page.ui.div().css({"border": "1px solid black"})
      b = page.ui.button("test")
      b.click([
        page.js.console.debugger,
        d.dom.loadHtml(page.ui.texts.label("test label").css({"color": 'blue', 'float': 'none'}))
      ])

    Attributes:
    ----------
    :param list components: The different HTML objects to be added to the component.
    :param bool append: Mention if the component should replace or append the data.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.

    :return: The Javascript string to be added to the page
    """
    if not isinstance(components, list):
      components = [components]

    js_funcs = []
    for i, h in enumerate(components):
      h.options.managed = False
      js_funcs.append(self._report.js.objects.new(str(h), isPyData=True, varName="obj_%s" % i))
      js_funcs.append(self.innerHTML(self._report.js.objects.get("obj_%s" % i), append=append).r)
    return JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)

  def options(self, options: Optional[dict] = None):
    """
    Description:
    ------------
    Return the builder options used to generate the object on the Javascript side.
    This is not necessarily the same object than the component options as some can be only used on the Python side.

    This will not change the original option object used during the first object creation.

    Attributes:
    ----------
    :param Optional[dict] options: Optional. The value to be changed.
    """
    opt = dict(self._src._jsStyles)
    if options is not None:
      opt.update(options)
    return opt

  def trigger(self, event: str):
    """
    Description:
    ------------
    Shortcut to the trigger event.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/Document/createEvent

    Attributes:
    ----------
    :param str event: The event to be triggered for the component.
    """
    return self.events.trigger(event)


class JsHtmlRich(JsHtml):

  @property
  def val(self):
    """
    Description:
    -----------
    Return the val object.
    """
    values = ["'%s': %s" % (k, self._report.components[k].dom.content.toStr()) for k in self._src._internal_components]
    return JsObjects.JsObjects.get(
      "{%s, offset: new Date().getTimezoneOffset()}" % ", ".join(values))

  @property
  def content(self):
    """
    Description:
    -----------

    """
    if hasattr(self.component.options, "markdown") and self.component.options.markdown:
      self.page.jsImports.add("showdown") # Add the import in case it is not defined in the component
      return ContentFormatters(self._report, '''(function(domObl){const converter = new showdown.Converter();
        if(domObl.hasAttribute('data-value')){return converter.makeMarkdown(domObl.getAttribute('data-value'))} 
        else {return converter.makeMarkdown(domObl.innerHTML)}})(%(varName)s)''' % {"varName": self.varName})
    else:
      return ContentFormatters(self._report, '''(function(domObl){
        if(domObl.hasAttribute('data-value')){ return domObl.getAttribute('data-value')} 
        else {return domObl.innerHTML}})(%(varName)s)''' % {"varName": self.varName})

  @property
  def format(self):
    """
    Description:
    ------------
    Specific formatters for the HTML components.
    """
    return Formatters(self._report, "%s.innerHTML" % self.varName)

  def toggleContent(self, current_val: str, new_val: str, current_funcs: Optional[list] = None,
                    new_funcs: Optional[list] = None, profile: Optional[Union[dict, bool]] = None):
    """
    Description:
    -----------
    Toggle (change) the content of the HTML component.

    Attributes:
    ----------
    :param str current_val: The content of the HTML component.
    :param str new_val: The new content of the HTML component.
    :param Optional[list] current_funcs: Optional. The functions to be triggered when currentVal is visible.
    :param Optional[list] new_funcs: Optional. The functions to be triggered when newVal is visible.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    content = JsUtils.jsConvertData(current_val, None)
    content2 = JsUtils.jsConvertData(new_val, None)
    return JsObjects.JsVoid('''
      if(%(varName)s.innerHTML == %(content)s){%(varName)s.innerHTML = %(content2)s; %(jsFncs)s}
      else {%(varName)s.innerHTML = %(content)s; %(jsFncs2)s}
      ''' % {'varName': self.varName, 'content2': content2, 'content': content,
             'jsFncs': JsUtils.jsConvertFncs(current_funcs, toStr=True, profile=profile),
             'jsFncs2': JsUtils.jsConvertFncs(new_funcs, toStr=True, profile=profile)
             })

  def select(self):
    """
    Description:
    -----------
    Select the content of the HTMl component.
    """
    return JsObjects.JsObjects.get('''
     (function(node){
      if (document.body.createTextRange) {
        const range = document.body.createTextRange(); range.moveToElementText(node); range.select();
      } else if (window.getSelection) {
        const selection = window.getSelection(); const range = document.createRange(); range.selectNodeContents(node);
        selection.removeAllRanges(); selection.addRange(range); }
     }(%s))''' % self.varName)

  def append(self, value, new_line: bool = True, options: Optional[dict] = None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param value:
    :param bool new_line: Boolean. Optional.
    :param Optional[dict] options: Optional.
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
    """
    return '%s.innerHTML = ""' % self.varName


class JsHtmlImg(JsHtml):

  @property
  def content(self):
    """
    Description:
    -----------

    """
    return ContentFormatters(self._report, "%s.src" % self.varName)

  def src(self, image: str):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param str image:
    """
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
    """
    Description:
    -----------

    """
    return ContentFormatters(self._report, "%s.innerHTML" % self.varName)

  def loading(self, flag: bool, multiple: bool = False):
    """
    Description:
    -----------
    Add a loading icon to the button.

    Usage::

      b = component.ui.button("test")
      b.click([
        b.dom.loading(True),
        rptObj.js.window.setTimeout([
          b.dom.loading(False)
        ], 5000),
      ])

    Attributes:
    ----------
    :param bool flag:
    :param bool multiple: Optional.
    """
    i_loading = '<i class="fas fa-spinner fa-spin" style="margin-right:5px"></i>'
    fnc = self.disable(False) if multiple else self.disable(flag)
    if flag:
      fnc.append("%s.innerHTML = '%s' + %s.innerHTML" % (self.varName, i_loading, self.varName))
    else:
      fnc.append("%s.innerHTML = %s.innerHTML.replace('%s', '')" % (self.varName, self.varName, i_loading))
    return fnc

  def error(self, time: int, color: str = "red"):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param int time:
    :param str color: Optional.
    """
    return JsFncs.JsFunction("var bgColor = %s.style.borderColor; %s.style.borderColor = '%s'; setTimeout(function() {%s.style.borderColor = bgColor}, %s)" % (self.varName, self.varName, color, self.varName, time))

  def disable(self, flag: bool = True):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param bool flag: Optional.
    """
    flag = JsUtils.jsConvertData(flag, None)
    return JsFncs.JsFunctions("%s.disabled = %s" % (self.varName, flag))

  def release(self, by_name: bool = False):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param bool by_name: Optional.
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

  def lock(self, not_allowed: bool = True):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param bool not_allowed: Optional.
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
    """
    return ""

  @property
  def content(self):
    """
    Description:
    -----------
    Get the content of the list.

    This will return all the selected items in a list.
    """
    return ""

  def disable(self):
    """
    Description:
    -----------

    """
    return JsObjects.JsObjects.get('''
      ''')

  def add(self, jsData, is_unique: bool = True, css_style: Optional[dict] = None, position: str = "bottom"):
    """
    Description:
    -----------
    Add an item to the list.

    THis will add the item at the end of the list by default.
    By default the list will not add duplicated entries.

    Attributes:
    ----------
    :param jsData: List of dict | JsObj.
    :param bool is_unique: Optional. Flag to specify if only distinct values should be added (no duplicates).
    :param Optional[dict] css_style: Optional. The CSS style of the added item.
    :param str position: Optional. The position of the new item in the list (bottom or top).
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
    """
    return '%s.empty()' % self.jquery.varId

  def delete(self, jsData):
    """
    Description:
    -----------

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
    """
    return JsObjects.JsVoid("$(this).find('p').text()")

  def css_label(self, jsData, attrs: dict):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsData:
    :param dict attrs:
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

    """
    return JsObjects.JsObjects.get('''
        {%s: {value: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset(), label: %s.innerHTML, name: %s}}
        ''' % (self.htmlCode, self.content.toStr(), self._src.label.dom.varName, self.getAttribute('name')))

  @property
  def content(self):
    """
    Description:
    -----------

    """
    check = self._src.options.icon_check.split(" ")[-1]
    return ContentFormatters(self._report, "%s.querySelector('i').classList.contains('%s')" % (self.varName, check))


class JsHtmlIcon(JsHtml):

  @property
  def val(self):
    """
    Description:
    -----------

    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
        self.htmlCode, self._src.dom.getAttribute("class")))

  @property
  def content(self):
    """
    Description:
    -----------

    """
    return self._src.dom.getAttribute("class")

  def spin(self, status: bool = True):
    """
    Description:
    -----------
    Add spin class to the font awesome.

    Attributes:
    ----------
    :param bool status: Optional. The spin status.
    """
    if status:
      return self._src.dom.classList.add("fa-spin")

    return self._src.dom.classList.remove("fa-spin")

  def pulse(self, status: bool = True):
    """
    Description:
    -----------
    Add pulse class to the font awesome.

    Attributes:
    ----------
    :param bool status: Optional. The spin status.
    """
    if status:
      return self._src.dom.classList.add("fa-pulse")

    return self._src.dom.classList.remove("fa-pulse")


class JsHtmlList(JsHtml):

  @property
  def val(self):
    """
    Description:
    ------------
    Return the standard value object with the fields (value, timestamp, offset).
    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s.querySelector('[data-select=true]').innerHTML, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
        self.htmlCode, self.varName))

  @property
  def content(self):
    """
    Description:
    ------------
    Return the values of the items in the list.
    """
    return JsObjects.JsArray.JsArray.get('''
      (function(){
         var values = []; %(component)s.querySelectorAll("%(item)s").forEach(function(dom){values.push(dom.innerText)});
         return values
      })()''' % {"component": self._src.dom.varName, "item": self._src.options.item_type})

  @property
  def classList(self):
    """
    Description:
    ------------
    Return the class name of the list item.
    """
    return self._src.dom.getAttribute("class")

  def add(self, item: str, unique: bool = True, draggable: bool = False):
    """
    Description:
    ------------
    Add a new item to the list.

    Attributes:
    ----------
    :param str item: The Item to be added to the list.
    :param bool unique: Optional. Only add the item if it is not already in the list.
    :param bool draggable: Optional. Set the new entry as draggable.
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

  @property
  def dropped_value(self):
    """
    Description:
    ------------
    Get the current dropped values to the list.
    Object can be structure (DOM) so the text content is wrapped in a specific variable.
    """
    return JsObjects.JsString.JsString.get("wrapper.innerText")

  def unactive(self, current_index: int = -1):
    """
    Description:
    -----------
    Set to unactive all the items in the list.

    Usage::

      bnts = page.web.bs.lists.buttons(["US", "ES", "IT"], html_code="cty")
      for i, bnt in enumerate(bnts):
        bnt.click([bnts.dom.unactive(i)])

    Attributes:
    ----------
    :param int current_index: Optional. The item of the current item.
    """
    return JsObjects.JsVoid('''
let list_items = %(comp)s.children; for (var i = 0; i < list_items.length; i++) { 
  if (list_items[i].classList.contains('active') && (i != %(current_index)s)){list_items[i].classList.remove('active')}
}''' % {"comp": self._src.dom.varName, "current_index": current_index})


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
    """
    Description:
    -----------

    """
    return ContentFormatters(self._report, self._src.dom.querySelector("div").css("backgroundColor").toStr())


class JsHtmlNumeric(JsHtmlRich):

  def to(self, number: float, timer: int = 1, profile: Optional[Union[dict, bool]] = None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param float number:
    :param int timer: The time spent for the increase in millisecond.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
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
    ], toStr=True, profile=profile)

  def add(self, item: float):
    """
    Description:
    ------------
    Add a value to the component value.

    Attributes:
    ----------
    :param float item: The value to be added.
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

    """
    return ContentFormatters(self._report, "%s.innerText" % self.varName)

  def url(self, url: str):
    """
    Description:
    -----------
    The href attribute specifies the URL of the page the link goes to.

    Related Pages:
    --------------

      https://www.w3schools.com/tags/att_a_href.asp

    Attributes:
    ----------
    :param str url: The url path.
    """
    url = JsUtils.jsConvertData(url, None)
    return JsFncs.JsFunctions("%s.href = %s" % (self.varName, url))

  def href(self, url: str):
    """
    Description:
    -----------
    The href attribute specifies the URL of the page the link goes to.

    Related Pages:
    --------------

      https://www.w3schools.com/tags/att_a_href.asp

    Attributes:
    ----------
    :param url: String. The url path.
    """
    url = JsUtils.jsConvertData(url, None)
    return JsFncs.JsFunctions("%s.href = %s" % (self.varName, url))

  def target(self, name: str):
    """
    Description:
    -----------
    The target attribute specifies where to open the linked document.

    Related Pages:
    --------------

      https://www.w3schools.com/tags/att_a_target.asp

    Attributes:
    ----------
    :param str name: The target name.
    """
    name = JsUtils.jsConvertData(name, None)
    return JsFncs.JsFunctions("%s.target = %s" % (self.varName, name))


class JsMedia(JsHtml):

  # TODO: Implement properly this with JsMediaRecorder

  def start(self):
    """
    Description:
    -----------
    Start the camera.
    This can only work with https and localhost urls.

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

  def takepicture(self, width: int = 50, height: int = 50):
    """
    Description:
    -----------


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

  def record(self, start: bool = True):
    """
    Description:
    -----------

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


class JsHtmlButtonFilter(JsHtml):

  @property
  def content(self):
    """
    Description:
    -----------

    """
    if self.component.options.is_number:
      return ContentFormatters(
        self._report, "{filter: %s, input: parseFloat(%s), radio: %s, filter2: %s, input2: parseFloat(%s)}" % (
          self.component.select.dom.content.toStr(),
          self.component.input.dom.content.toStr(),
          self.component.radios.dom.content.toStr(),
          self.component.select2.dom.content.toStr(),
          self.component.input2.dom.content.toStr()))
    return ContentFormatters(self._report, "{filter: %s, input: %s, radio: %s, filter2: %s, input2: %s}" % (
      self.component.select.dom.content.toStr(),
      self.component.input.dom.content.toStr(),
      self.component.radios.dom.content.toStr(),
      self.component.select2.dom.content.toStr(),
      self.component.input2.dom.content.toStr()))


class JsHtmlTable(JsHtml):

  @property
  def content(self):
    return JsObjects.JsArray.JsArray.get('''
      (function(){
         var values = []; 
         %(component)s.querySelectorAll("tr").forEach(function(row){
            var rec = []; row.childNodes.forEach(function(cell){
              rec.push(cell.innerText)}); values.push(rec)
         });return values })()''' % {"component": self._src.dom.varName})


class JsHtmlLi(JsHtmlRich):

  def has_state(self, state: str, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = None):
    """
    Description:
    -----------
    Check if the item in the list has a specific class.
    If it is the case it will run the function.

    Attributes:
    ----------
    :param str state: The CSS class.
    :param Union[list, str] js_funcs: The function to run if the state is defined.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    return self._src.js.if_("%s.classList.contains(%s)" % (
      self.varName, JsUtils.jsConvertData(state, None)), js_funcs, profile=profile)

  def is_active(self, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = None):
    """
    Description:
    -----------
    Check if the item in the list has the class active.

    Attributes:
    ----------
    :param Union[list, str] js_funcs: The function to run if the state is defined.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    return self.has_state("active", js_funcs, profile=profile)
