
from epyk.core.css.styles.attributes import Attrs


class AttrIcon(Attrs):

  def __init__(self, component):
    super(AttrIcon, self).__init__(component)
    self.font_size = component.page.body.style.globals.font.normal()
    self.vertical_align = "middle"
    self.display = "inline-block"
    self.margin = "auto 0"
    self.padding = "auto 0"
