
from epyk.core.css.styles.attributes import Attrs


class AttrSkarkline(Attrs):

  def __init__(self, component):
    super(AttrSkarkline, self).__init__(component)
    self.display = "inline-block"
    self.font_size = component.page.body.style.globals.font.normal()
    self.margin = "1px 4px"
