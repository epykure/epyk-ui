
from epyk.core.css import Defaults_css
from epyk.core.css.styles.attributes import Attrs


class AttrDiv(Attrs):
  def __init__(self, rptObj):
    super(AttrDiv, self).__init__(rptObj)
    #self.font_size = Defaults_css.font()
    self.vertical_align = "middle"
    self.box_sizing = 'border-box'


class AttrModal(Attrs):
  def __init__(self, rptObj):
    super(AttrModal, self).__init__(rptObj)
    self.background_color = 'rgb(0,0,0,0.4)'
    self.display = 'none'
