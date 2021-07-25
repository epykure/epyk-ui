
from epyk.core.css.styles.attributes import Attrs


class NavBar(Attrs):

  def __init__(self, component):
    super(NavBar, self).__init__(component)
    self.font_size = component.page.body.style.globals.font.normal(4)
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
  """
  CSS pre defined properties for the Footer.

  CSS Properties:

    display: block
    margin: 0
    vertical-align: bottom
    left: 0
    padding: 0 2px 0 2px
    bottom: 0
    z-index: 10
  """

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
