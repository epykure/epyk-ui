
from epyk.core.css.styles.attributes import Attrs


class AttrDiv(Attrs):
  """
  CSS pre defined properties for the Div container.

  CSS Properties:

    vertical-align: middle
    box-sizing: border-box
  """

  def __init__(self, component):
    super(AttrDiv, self).__init__(component)
    self.vertical_align = "middle"
    self.box_sizing = 'border-box'


class AttrModal(Attrs):
  """
  CSS pre defined properties for the Div Modal.

  CSS Properties:

    background-color: rgb(0,0,0,0.4)
    display: none
  """

  def __init__(self, component):
    super(AttrModal, self).__init__(component)
    self.background_color = 'rgb(0,0,0,0.4)'
    self.display = 'none'
