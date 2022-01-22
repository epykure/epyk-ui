#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union, Optional, Any
from epyk.core.py import primitives

from epyk.core.html import Html
from epyk.core.js.html import JsHtml
from epyk.core.html.options import OptText


class ExternalLink(Html.Html):
  name = 'External link'
  _option_cls = OptText.OptionsLink

  def __init__(self, report: primitives.PageModel, text: str, url: str, icon: str, helper: str, height: tuple,
               decoration: bool, html_code: Optional[str], options: Optional[dict], profile: Optional[Union[bool, dict]]):
    super(ExternalLink, self).__init__(report, {"text": text, "url": url}, html_code=html_code, options=options,
                                       css_attrs={'height': height}, profile=profile)
    # Add the internal components icon and helper
    self.add_icon(icon, html_code=self.htmlCode, family=options.get("icon_family"))
    self.add_helper(helper)
    self.decoration, self.__url = decoration, {}
    if 'url' not in self.val:
      self.options.url = self.val['text']
    else:
      self.options.url = self.val['url']

  @property
  def dom(self) -> JsHtml.JsHtmlLink:
    """
    Description:
    ------------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    :return: A Javascript Dom object

    :rtype: JsHtml.JsHtmlLink
    """
    if self._dom is None:
      self._dom = JsHtml.JsHtmlLink(self, report=self.page)
    return self._dom

  @property
  def options(self) -> OptText.OptionsLink:
    """
    Description:
    ------------
    Property to set all the possible object for a button.

    :rtype: OptText.OptionsLink
    """
    return super().options

  _js__builder__ = '''
      if(typeof data === 'undefined'){data = {text: ''}}
      var text = "";
      if((typeof data.text !== 'undefined') && (data.text)){text = data.text} 
      else if (data.text) {text = data.text}
      else {text = data}
      if (options.type_number == 'money'){
        text = accounting.formatMoney(text, options.symbol, options.digits, options.thousand_sep, 
        options.decimal_sep, options.format)}
      else if (options.type_number == 'number'){
        text = accounting.formatNumber(text, options.digits, options.thousand_sep, options.decimal_sep)}
      if(typeof data.icon !== 'undefined'){
        htmlObj.innerHTML = '<i class="'+ data.icon +'" style="margin-right:5px"></i>'+ text;}
      else {htmlObj.innerHTML = text}; if(typeof data.url !== 'undefined'){htmlObj.href = data.url}'''

  def anchor(self, component: Html.Html):
    """
    Description:
    ------------
    Create a link to an HTML component defined in the page.
    This will create a shortcut to directly scroll to this component.

    Attributes:
    ----------
    :param Html.Html component: A link to this HTML component.
    """
    self.val["url"] = "#%s" % component.htmlCode
    self.options.url = "#%s" % component.htmlCode
    return self

  def no_decoration(self, color: Optional[str] = None):
    """
    Description:
    -----------
    Property to remove the list default style.

    Attributes:
    ----------
    :param Optional[str] color: Optional. The color code.
    """
    self.style.css.text_decoration = None
    self.style.list_style_type = None
    if color is None:
      color = self.page.theme.greys[-1]
    self.style.css.color = color
    return self

  def build(self, data: Optional[Union[str, primitives.JsDataModel]] = None, options: Optional[dict] = None,
            profile: Optional[Union[bool, dict]] = False, component_id: Optional[str] = None):
    """
    Description:
    -----------
    Return the JavaScript fragment to refresh the component content.

    Attributes:
    ----------
    :param Optional[Union[str, primitives.JsDataModel]] data: The component expected content.
    :param Optional[dict] options: Optional. Specific Python options available for this component.
    :param Optional[Union[bool, dict]] profile: Optional. A flag to set the component performance storage.
    :param Optional[str] component_id: Optional. The component reference (the htmlCode).
    """
    if not hasattr(data, 'toStr'):
      if not isinstance(data, dict):
        data = {"text": data}
      if "url" not in data:
        data["url"] = self.val["url"]
    return super(ExternalLink, self).build(data, options, profile, component_id)

  def __str__(self):
    return '<a %s>%s</a>%s' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.val['text'], self.helper)


class DataLink(Html.Html):
  name = 'Data link'
  filename = "Download"

  def __init__(self, report: primitives.PageModel, text: str, value: Any, width: tuple, height: tuple, fmt: str,
               options: Optional[str], profile: Optional[Union[bool, dict]]):
    super(DataLink, self).__init__(report, {"text": text, 'value': value}, profile=profile, options=options,
                                   css_attrs={"width": width, 'height': height})
    self.format = fmt

  @property
  def no_decoration(self):
    """
    Description:
    -----------
    Property to remove the list default style.
    """
    self.style.css.text_decoration = None
    self.style.css.list_style_type = None
    return self

  _js__builder__ = '''var b = new Blob([data.value]); htmlObj.href = URL.createObjectURL(b); 
    htmlObj.innerHTML = data.text'''

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    return '<a %(attr)s href="#" download="%(filename)s.%(format)s" type="text/%(format)s">%(val)s</a>' % {
      "filename": self.filename, 'attr': self.get_attrs(pyClassNames=self.style.get_classes()), 'val': self.val['text'],
      'format': self.format}
