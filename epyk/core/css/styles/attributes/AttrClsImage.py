
from epyk.core.css.styles.attributes import Attrs


class AttrIcon(Attrs):
  """
  CSS pre defined properties for the Icon.

  CSS Properties:

    font-size: Normal (the value defined by the framework)
    vertical-align: middle
    display: inline-block
    margin: auto 0
    padding: auto 0
  """

  def __init__(self, component):
    super(AttrIcon, self).__init__(component)
    self.font_size = component.page.body.style.globals.font.normal()
    self.vertical_align = "middle"
    self.display = "inline-block"
    self.margin = "auto 0"
    self.padding = "auto 0"
