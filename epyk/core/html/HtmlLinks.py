#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html

# The list of CSS classes
# from epyk.core.css.styles import GrpCls
# from epyk.core.css.styles import CssGrpClsText


class ExternalLink(Html.Html):
  name = 'External link'

  def __init__(self, report, text, url, icon, helper, height, decoration, options, profile):
    super(ExternalLink, self).__init__(report, {"text": text, "url": url}, css_attrs={'height': height}, profile=profile)
    # Add the internal components icon and helper
    self.add_icon(icon, family=options.get("icon_family"))
    self.add_helper(helper)
    if not 'url' in self.val:
      self.val['url'] = self.val['text']
    if 'target' in options:
      self.set_attrs(name="target", value=options['target'])
    self.decoration, self.__url = decoration, {}

  @property
  def _js__builder__(self):
    return 'htmlObj.innerHTML = data.text; htmlObj.href = data.url'

  def no_decoration(self, color=None):
    """
    Description:
    -----------
    Property to remove the list default style
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

    :param data:
    :param options:
    :param profile:
    """
    if not isinstance(data, dict):
      data = {"text": data}
    if "url" not in data:
      data["url"] = self.val["url"]
    return super(ExternalLink, self).build(data, options, profile)

  def __str__(self):
    self.set_attrs(name="href", value=self.val['url'])
    return '<a %s>%s</a>%s' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.val['text'], self.helper)


class DataLink(Html.Html):
  name = 'Data link'
  # _grpCls = CssGrpClsText.CssClassHref

  def __init__(self, report, text, value, width, height, format, profile):
    super(DataLink, self).__init__(report, {"text": text, 'value': value}, profile=profile,
                                   css_attrs={"width": width, 'height': height})
    self.format = format

  @property
  def no_decoration(self):
    """
    Description:
    -----------
    Property to remove the list default style
    """
    self.style.css.text_decoration = None
    self.style.css.list_style_type = None
    return self

  @property
  def _js__builder__(self):
    return ''' var b = new Blob([data.value]); htmlObj.href = URL.createObjectURL(b); htmlObj.innerHTML = data.text'''

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '<a %(attr)s href="#" download="Download.%(format)s" type="text/%(format)s">%(val)s</a>' % {'attr': self.get_attrs(pyClassNames=self.style.get_classes()), 'val': self.val['text'], 'format': self.format}
