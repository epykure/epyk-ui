
from epyk.core.css import Defaults_css
from epyk.core.css.styles.attributes import Attrs


class NavBar(Attrs):

  def __init__(self, component):
    super(NavBar, self).__init__(component)
    self.font_size = Defaults_css.font(8)
    self.display = 'block'
    self.margin = 0
    self.vertical_align = 'top'
    self.left = 0
    self.box_sizing = "border-box"
    self.padding = "0 5px 0 2px"
    self.position = "fixed"
    self.background_color = component.page.theme.greys[0]
    self.border_bottom = "1px solid %s" % component.page.theme.greys[4]
    self.top = 0
    self.z_index = 510


class Footer(Attrs):

  def __init__(self, component):
    super(Footer, self).__init__(component)
    self.display = 'block'
    self.margin = 0
    self.vertical_align = 'bottom'
    self.left = 0
    self.padding = "0 2px 0 2px"
    self.position = "fixed"
    self.bottom = 0
    self.z_index = 10
