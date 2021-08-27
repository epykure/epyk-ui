
from epyk.core.html import Defaults
from epyk.core.css.styles import GrpCls
from epyk.core.css.styles.classes import CssStyle


class CssToastTimePicker(CssStyle.Style):
  """
  Style override for the CSS class tui-timepicker
  """
  classname = "tui-timepicker"

  def customize(self):
    self.css({
      'padding': 0, "border": 0}, important=True)


class CssToastTimePickerSelect(CssStyle.Style):
  """
  Style override for the CSS class tui-timepicker-select
  """
  classname = "tui-timepicker-select"

  def customize(self):
    self.css({
      'height': "%spx" % Defaults.LINE_HEIGHT, "padding": "0 0 0px 9px"}, important=True)


class ClassTimePicker(GrpCls.ClassHtml):

  def __init__(self, component):
    super(ClassTimePicker, self).__init__(component)
    self.classList['main'].add(CssToastTimePicker(self.component.page))
    self.classList['main'].add(CssToastTimePickerSelect(self.component.page))
