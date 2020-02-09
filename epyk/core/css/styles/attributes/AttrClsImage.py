"""

"""

from epyk.core.css import Defaults_css
from epyk.core.css.styles.attributes import Attrs


class AttrIcon(Attrs):
  def __init__(self, rptObj):
    super(AttrIcon, self).__init__(rptObj)
    self.font_size = Defaults_css.font()
    self.vertical_align = "middle"
    self.display = "inline-block"
    self.margin = "auto 0"
    self.padding = "auto 0"
