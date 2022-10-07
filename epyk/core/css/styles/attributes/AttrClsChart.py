
from epyk.core.css.styles.attributes import Attrs
from epyk.core.py import primitives


class AttrSkarkline(Attrs):
  """  CSS pre defined properties for the SparkLine.

  CSS Properties:

    display: inline-block
    font-size: Normal (the value defined by the framework)
    margin: 1px 4px
  """

  def __init__(self, component: primitives.HtmlModel, page: primitives.PageModel = None):
    super(AttrSkarkline, self).__init__(component, page=page)
    self.display = "inline-block"
    self.font_size = component.page.body.style.globals.font.normal()
    self.margin = "1px 4px"
