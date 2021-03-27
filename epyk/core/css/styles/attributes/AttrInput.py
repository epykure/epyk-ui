
from epyk.core.css.styles.attributes import Attrs


class AttrInput(Attrs):

  def __init__(self, component):
    super(AttrInput, self).__init__(component)
    self.font_size = component.page.body.style.globals.font.normal()
    self.font_family = component.page.body.style.globals.font.family
    self.box_sizing = 'border-box'
