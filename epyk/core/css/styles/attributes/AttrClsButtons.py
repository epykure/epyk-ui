"""

"""

from epyk.core.css import Defaults_css
from epyk.core.css.styles.attributes import Attrs


class AttrButton(Attrs):
  def __init__(self, rptObj):
    super(AttrButton, self).__init__(rptObj)
    self.cursor = "pointer"
    self.font_size = Defaults_css.font()


class AttrBadge(Attrs):
  def __init__(self, rptObj):
    super(AttrBadge, self).__init__(rptObj)
    self.padding = "1px 3px"
    self.margin = "1px 1px 1px 2px"
    self.vertical_align = "bottom"
    self.font_size = Defaults_css.font(-3)

