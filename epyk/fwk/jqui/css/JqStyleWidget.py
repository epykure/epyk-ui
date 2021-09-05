
from epyk.core.css.styles import GrpCls
from epyk.core.css.styles.classes import CssStyle


class CssJqActiveState(CssStyle.Style):
  """
  Description:
  -----------
  Change the default color style for the component to math the selected theme.
  """
  classname = "ui-state-active"

  def customize(self):
    self.css({'background': self.page.theme.notch(3), "border": self.page.theme.notch(-4)}, important=True)


class Accordion(GrpCls.ClassHtml):

  def __init__(self, component):
    super(Accordion, self).__init__(component)
    self.classList['other'].add(CssJqActiveState(self.component.page))
