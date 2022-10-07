
from epyk.core.css.styles.attributes import Attrs
from epyk.core.py import primitives


class AttrHelp(Attrs):
  """  CSS pre defined properties for the Helper.

  CSS Properties:

    font-size: Normal (the value defined by the framework)
    cursor: pointer
    float: right
    margin: 1px 4px
  """

  def __init__(self, component: primitives.HtmlModel, page: primitives.PageModel = None):
    super(AttrHelp, self).__init__(component, page=page)
    self.font_size = component.page.body.style.globals.font.normal()
    self.cursor = "pointer"
    self.float = "right"
    self.margin = "1px 4px"
