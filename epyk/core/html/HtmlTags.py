"""
Module for the bespoke HTML tags
"""


from epyk.core.html import Html


class HtmlGeneric(Html.Html):
  category, name = 'Tags', 'tag'

  def __init__(self, report, tag, text, width, height, htmlCode, tooltip, profile):
    self.tag = tag
    super(HtmlGeneric, self).__init__(report, text, htmlCode=htmlCode, css_attrs={"width": width, "height": height}, profile=profile)
    if tooltip:
      self.tooltip(tooltip)

  def __str__(self):
    return '<%s %s>%s</%s>%s' % (self.tag, self.get_attrs(pyClassNames=self.style.get_classes()), self.val, self.tag, self.helper)


class HtmlComment(Html.Html):
  category, name = 'Tags', 'comment'

  def __str__(self):
    return '<!--%s-->' % self.val
