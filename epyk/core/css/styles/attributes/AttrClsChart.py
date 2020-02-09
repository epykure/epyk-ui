"""

"""

from epyk.core.css import Defaults_css
from epyk.core.css.styles.attributes import Attrs


class AttrSkarkline(Attrs):
  def __init__(self, rptObj):
    super(AttrSkarkline, self).__init__(rptObj)
    self.display = "inline-block"
    self.font_size = Defaults_css.font()
    self.margin = "1px 4px"
