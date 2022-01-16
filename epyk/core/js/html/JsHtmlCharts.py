#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from typing import Union, Optional

from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtml
from epyk.core.js.fncs import JsFncs
from epyk.core.js.statements import JsIf

from epyk.core.js.packages import JsQuery
from epyk.core.js.packages import JsD3

from epyk.core.js.primitives import JsObjects
from epyk.core.js.objects import JsCanvas
from epyk.core.js.objects import JsNodeDom
from epyk.core.js.primitives import JsBoolean

from epyk.core.html import Defaults as Defaults_html


class ChartJs(JsCanvas.Canvas):
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
      return JsNodeDom.JsDomsList(None, "document.getElementsByName('%s')" % self._src.attr.get('name'),
                                        report=self._report)

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
    flag = JsBoolean.JsBoolean("!(rect.bottom < 0 || rect.top - viewHeight >= 0)", varName="visibleFlag", setVar=True,
                               isPyData=False)
    flag._js.insert(0, self._report.js.viewHeight.setVar('viewHeight'))
    flag._js.insert(0, self.getBoundingClientRect().setVar("rect"))
    return JsFncs.JsAnonymous(flag.r).return_("visibleFlag").call()

  def onViewPort(self, js_funcs: Union[list, str]):
    """
    Description:
    -----------
    Trigger some code when the component is visible on the visible part of the page (the viewpport).

    Attributes:
    ----------
    :param Union[list, str] js_funcs: The Javascript events
    """
    return self._src.js.if_(self.isInViewPort, js_funcs)

  @property
  def content(self):
    """
    Description:
    -----------

    """
    return JsHtml.ContentFormatters(self._report, "%s.value" % self.varName)

  def empty(self):
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
      self._jquery = JsQuery.JQuery(src=self._src, selector=JsQuery.decorate_var("#%s" % self._src.htmlCode),
                                    setVar=False)
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
  def objects(self):
    """
    Description:
    -----------
    Interface to the main Javascript Classes and Primitives.
    """
    return JsObjects.JsObjects(self)

  @property
  def format(self):
    """
    Description:
    ------------
    Specific formatters for the HTML components.
    """
    return JsHtml.Formatters(self._report, self.content.toStr())

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

  def registerFunction(self, func_name: str, js_funcs: Union[list, str], pmts: Optional[dict] = None,
                       profile: Optional[Union[dict, bool]] = None):
    """
    Description:
    -----------
    Javascript Framework extension

    Register a predefined Javascript function.
    This is only dedicated to specific Javascript transformation functions.

    Attributes:
    ----------
    :param str func_name: The function name.
    :param Union[list, str] js_funcs: The Javascript function definition.
    :param dict pmts:
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.

    :return: The JsObject
    """
    js_data = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    self._src._props.setdefault('js', {}).setdefault('functions', {})[func_name] = {'content': js_data, 'pmt': pmts}
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
    Display the component.

    Usage::

      input.js.show()

    Related Pages:

      https://gomakethings.com/how-to-show-and-hide-elements-with-vanilla-javascript/

    Attributes:
    ----------
    :param Optional[str] inline:
    :param Optional[int] duration: A time in second for the component display
    :param Optional[str] display_value: Optional. The value to display. Default inline-block
    """
    display_value = display_value or self.display_value
    if duration is not None:
      return super(JsHtml, self).show('inline-block' if inline else display_value, duration)

    return JsUtils.jsConvertData(self.css("display", 'inline-block' if inline else display_value), None)

  def visible(self, data, inline: Optional[str] = None, display_value: Optional[str] = None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param data: Boolean.
    :param Optional[str] inline:
    :param Optional[str] display_value:
    """
    data = JsUtils.jsConvertData(data, None)
    return JsObjects.JsVoid(
      "if(%s){%s} else{%s}" % (data, self.show(inline, display_value=display_value).r, self.hide().r))

  def select(self):
    """
    Description:
    -----------
    Select the content of the HTMl component.
    """
    return JsObjects.JsObjects.get("%s.select()" % self.varName)

  def toggle(self, attr: str = "display", js_val1: Optional[str] = None, js_val2: str = "none"):
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
    :param str attr:
    :param Optional[str] js_val1:
    :param str js_val2:

    :return: A Javascript if statement
    """
    if attr == 'display' and js_val1 is None:
      js_val1 = self.display_value
    return JsIf.JsIf(self.css(attr) == js_val2, [self.css(attr, js_val1)]).else_([self.css(attr, js_val2)])

  def highlight(self, css_attrs: Optional[dict] = None, time_event: int = 1000):
    """
    Description:
    ------------

    Usage::

      s.dom.highlight()
      s.dom.highlight(css_attrs={"background": "red"}),

    Attributes:
    ----------
    :param Optional[dict] css_attrs: A dictionary with the CSS attributes.
    :param int time_event: The time of the event.
    """
    if css_attrs is None:
      css_attrs, css_attrs_origin = {}, {}
      for k, v in Defaults_html.HTML_HIGHLIGHT.items():
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

  def copyToClipboard(self, clipboardCopySelector=None, with_header=True):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param clipboardCopySelector:
    :param with_header:
    """
    return JsObjects.JsVoid("(function(canvas){var image = new Image(); image.src = canvas.toDataURL('image/png'); return image})(%s)" % self.varName)
