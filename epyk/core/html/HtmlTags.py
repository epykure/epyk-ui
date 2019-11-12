"""
Module for the bespoke HTML tags
"""


from epyk.core.html import Html


class HtmlGeneric(Html.Html):
  category, name = 'Tags', 'tag'
  builder_name = False

  def __init__(self, report, tag, text, size, width, height, htmlCode, tooltip, profile):
    self.tag = tag
    super(HtmlGeneric, self).__init__(report, text, htmlCode=htmlCode, width=width[0], widthUnit=width[1],
                                      height=height[0], heightUnit=height[1], profile=profile)
    self.css({"font-size": '%s%s' % (size[0], size[1]), "display": 'inline-block'})

  def __str__(self):
    return '<%s %s>%s</%s>%s' % (self.tag, self.get_attrs(pyClassNames=self.pyStyle), self.val, self.tag, self.helper)


class HtmlComment(Html.Html):
  category, name = 'Tags', 'comment'
  builder_name = False

  def __str__(self):
    return '<!--%s-->' % self.val
