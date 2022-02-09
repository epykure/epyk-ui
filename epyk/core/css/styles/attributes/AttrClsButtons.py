
from epyk.core.css.styles.attributes import Attrs
from epyk.core.py import primitives


class AttrButton(Attrs):
  """
  Description:
  ------------
  CSS pre defined properties for the Button.

  CSS Properties:

    font-size: Normal (the value defined by the framework)
  """

  def __init__(self, component: primitives.HtmlModel, page: primitives.PageModel = None):
    super(AttrButton, self).__init__(component, page=page)


class AttrBadge(Attrs):
  """
  Description:
  ------------
  CSS pre defined properties for the Badge.

  CSS Properties:

    padding: 1px 3px
    margin: 1px 1px 1px 2px
    vertical-align: bottom
    font-size: Normal (the value defined by the framework)
  """

  def __init__(self, component: primitives.HtmlModel, page: primitives.PageModel = None):
    super(AttrBadge, self).__init__(component, page=page)
    self.padding = "1px 3px"
    self.margin = "1px 1px 1px 2px"
    self.vertical_align = "bottom"
    self.font_size = component.page.body.style.globals.font.normal(-3)
