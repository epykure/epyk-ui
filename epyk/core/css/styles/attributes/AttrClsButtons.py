
from epyk.core.css.styles.attributes import Attrs


class AttrButton(Attrs):
  """
  CSS pre defined properties for the Button.

  CSS Properties:

    font-size: Normal (the value defined by the framework)
  """

  def __init__(self, component):
    super(AttrButton, self).__init__(component)


class AttrBadge(Attrs):
  """
  CSS pre defined properties for the Badge.

  CSS Properties:

    padding: 1px 3px
    margin: 1px 1px 1px 2px
    vertical-align: bottom
    font-size: Normal (the value defined by the framework)
  """

  def __init__(self, component):
    super(AttrBadge, self).__init__(component)
    self.padding = "1px 3px"
    self.margin = "1px 1px 1px 2px"
    self.vertical_align = "bottom"
    self.font_size = component.page.body.style.globals.font.normal(-3)
