
from epyk.core.css import Defaults_css
from epyk.core.css.styles.attributes import Attrs


class AttrButton(Attrs):

  def __init__(self, component):
    super(AttrButton, self).__init__(component)
    self.font_size = Defaults_css.font()


class AttrBadge(Attrs):

  def __init__(self, component):
    super(AttrBadge, self).__init__(component)
    self.padding = "1px 3px"
    self.margin = "1px 1px 1px 2px"
    self.vertical_align = "bottom"
    self.font_size = Defaults_css.font(-3)
