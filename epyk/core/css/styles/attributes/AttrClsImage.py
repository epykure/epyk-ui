
from epyk.core.css.styles.attributes import Attrs
from epyk.core.py import primitives


class AttrIcon(Attrs):
  """  CSS pre defined properties for the Icon.

  CSS Properties:

    font-size: Normal (the value defined by the framework)
    vertical-align: middle
    display: inline-block
    margin: auto 0
    padding: auto 0
  """

  def __init__(self, component: primitives.HtmlModel, page: primitives.PageModel = None):
    super(AttrIcon, self).__init__(component, page=page)
    self.font_size = component.page.body.style.globals.font.normal()
    self.vertical_align = "middle"
    self.display = "inline-block"
    self.margin = "auto 0"
    self.padding = "auto 0"
