
from epyk.core.css import Defaults_css
from epyk.core.css.styles.attributes import Attrs


class AttrInput(Attrs):

  def __init__(self, component):
    super(AttrInput, self).__init__(component)
    self.font_size = Defaults_css.font()
    self.font_family = Defaults_css.Font.family
    self.box_sizing = 'border-box'
