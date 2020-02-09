"""

"""

from epyk.core.css import Defaults_css
from epyk.core.css.styles.attributes import Attrs


class AttrDiv(Attrs):
  def __init__(self, rptObj):
    super(AttrDiv, self).__init__(rptObj)
    self.font_size = Defaults_css.font()
    self.vertical_align = "middle"
