#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html
from epyk.core.js.html import JsHtml
from epyk.core.html.options import OptText


class ExternalLink(Html.Html):
  name = 'External link'

  def __init__(self, report, text, url, icon, helper, height, decoration, htmlCode, options, profile):
    super(ExternalLink, self).__init__(report, {"text": text, "url": url}, htmlCode=htmlCode, css_attrs={'height': height}, profile=profile)
    # Add the internal components icon and helper
    self.add_icon(icon, htmlCode=self.htmlCode, family=options.get("icon_family"))
    self.add_helper(helper)
    self.decoration, self.__url = decoration, {}
    self.__options = OptText.OptionsLink(self, options)
    if 'url' not in self.val:
      self.options.url = self.val['text']
    else:
      self.options.url = self.val['url']

  @property
  def dom(self):
    """
    Description:
    ------------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    Usage:
    -----

    :return: A Javascript Dom object

    :rtype: JsHtml.JsHtmlLink
    """
    if self._dom is None:
      self._dom = JsHtml.JsHtmlLink(self, report=self._report)
    return self._dom

  @property
  def options(self):
    """
    Description:
    ------------
    Property to set all the possible object for a button.

    Usage:
    -----

    :rtype: OptText.OptionsLink
    """
    return self.__options

  _js__builder__ = '''
      if(typeof data === 'undefined'){data = {text: ''}}
      var text = "";
      if((typeof data.text !== 'undefined') && (data.text)){text = data.text} else if (data.text) {text = data}
      if (options.type_number == 'money'){ text = accounting.formatMoney(text, options.symbol, options.digits, options.thousand_sep, options.decimal_sep, options.format) }
      else if (options.type_number == 'number'){text = accounting.formatNumber(text, options.digits, options.thousand_sep, options.decimal_sep)}
      if(typeof data.icon !== 'undefined'){htmlObj.innerHTML = '<i class="'+ data.icon +'" style="margin-right:5px"></i>'+ text;}
      else {htmlObj.innerHTML = text}; if(typeof data.url !== 'undefined'){htmlObj.href = data.url}'''

  def anchor(self, component):
    """
    Description:
    ------------
    Create a link to an HTML component defined in the page.
    This will create a shortcut to directly scroll to this component.

    Usage:
    -----

    Attributes:
    ----------
    :param component: HTML. A link to this HTML component.
    """
    self.val["url"] = "#%s" % component.htmlCode
    self.options.url = "#%s" % component.htmlCode
    return self

  def no_decoration(self, color=None):
    """
    Description:
    -----------
    Property to remove the list default style.

    Usage:
    -----

    Attributes:
    ----------
    :param color: String. Optional. The color code.
    """
    self.style.css.text_decoration = None
    self.style.list_style_type = None
    if color is None:
      color = self._report.theme.greys[-1]
    self.style.css.color = color
    return self

  def build(self, data=None, options=None, profile=False):
    """
    Description:
    -----------
    Return the JavaScript fragment to refresh the component content.

    Usage:
    -----

    Attributes:
    ----------
    :param data: String | object. The component expected content.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not hasattr(data, 'toStr'):
      if not isinstance(data, dict):
        data = {"text": data}
      if "url" not in data:
        data["url"] = self.val["url"]
    return super(ExternalLink, self).build(data, options, profile)

  def __str__(self):
    return '<a %s>%s</a>%s' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.val['text'], self.helper)


class DataLink(Html.Html):
  name = 'Data link'

  def __init__(self, report, text, value, width, height, format, profile):
    super(DataLink, self).__init__(report, {"text": text, 'value': value}, profile=profile,
                                   css_attrs={"width": width, 'height': height})
    self.format = format

  @property
  def no_decoration(self):
    """
    Description:
    -----------
    Property to remove the list default style.

    Usage:
    -----

    """
    self.style.css.text_decoration = None
    self.style.css.list_style_type = None
    return self

  _js__builder__ = '''var b = new Blob([data.value]); htmlObj.href = URL.createObjectURL(b); 
    htmlObj.innerHTML = data.text'''

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '<a %(attr)s href="#" download="Download.%(format)s" type="text/%(format)s">%(val)s</a>' % {'attr': self.get_attrs(pyClassNames=self.style.get_classes()), 'val': self.val['text'], 'format': self.format}
