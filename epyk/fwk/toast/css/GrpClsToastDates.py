
from epyk.core.py import primitives
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
  _focus = {'outline': 0}

  def customize(self):
    self.focus.css({"border-color": self.page.theme.notch()})
    self.css({
      'height': "%spx" % Defaults.LINE_HEIGHT, "padding": "0 0 0px 9px"}, important=True)


class ClassTimePicker(GrpCls.ClassHtml):

  def __init__(self, component: primitives.HtmlModel = None, page: primitives.PageModel = None):
    super(ClassTimePicker, self).__init__(component=component, page=page)
    self.classList['main'].add(CssToastTimePicker(self.page))
    self.classList['main'].add(CssToastTimePickerSelect(self.page))


class CssToastDatePickerInput(CssStyle.Style):
  """
  Style override for the CSS class tui-Datepicker-select
  """
  classname = "tui-datetime-input>input"
  _focus = {'outline': 0}

  def customize(self):
    self.css({"border": "1px solid %s" % self.page.theme.greys[0]}, important=True)
    self.focus.css({"border": "1px solid %s" % self.page.theme.notch()}, important=True)


class CssToastDatePickerFocus(CssStyle.Style):
  """
  Style override for the CSS class tui-Datepicker-select
  """
  classname = "tui-datepicker-input"

  def customize(self):
    self.focus.css({"border": None}, important=True)


class ClassDatePicker(GrpCls.ClassHtml):

  def __init__(self, component: primitives.HtmlModel = None, page: primitives.PageModel = None):
    super(ClassDatePicker, self).__init__(component=component, page=page)
    self.classList['main'].add(CssToastDatePickerInput(self.page))
    self.classList['main'].add(CssToastDatePickerFocus(self.page))
