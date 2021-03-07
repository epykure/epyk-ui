
from epyk.core.css import Defaults_css
from epyk.core.css.styles.attributes import Attrs


class AttrHelp(Attrs):

  def __init__(self, component):
    super(AttrHelp, self).__init__(component)
    self.font_size = Defaults_css.font()
    self.cursor = "pointer"
    self.float = "right"
    self.margin = "1px 4px"
