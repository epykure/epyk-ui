"""

"""

from epyk.core.css import Properties
from epyk.core.css import Defaults_css


class Attrs(Properties.CssMixin):
  def __init__(self, htmlObj):
    self.htmlObj, self.attrs = self, {}
    self.orign_htmlObj = htmlObj

  def css(self, attrs):
    for k, v in attrs.items():
      self.attrs[k] = v

  def __str__(self):
    """

    """
    css_tag = []
    for k, v in self.attrs.items():
      css_tag.append("%s:%s" % (k, v))
    return ";".join(css_tag)


class Commons(Attrs):
  def __init__(self, htmlObj):
    super(Commons, self).__init__(htmlObj)
    self.font_size = Defaults_css.font()

