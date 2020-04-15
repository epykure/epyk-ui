"""
CSS Style module for the Dates components
"""

from epyk.core.css.styles.classes import CssStyle
from epyk.core.css import Defaults_css


class CssDatePickerUI(CssStyle.Style):
  classname = "ui-datepicker"

  def customize(self):
    self.css({"background": self.rptObj.theme.colors[0], "font-size": Defaults_css.font()})


class CssDatePicker(CssStyle.Style):
  _attrs = {'font-family': 'inherit', 'border': 'none', 'cursor': 'pointer', 'margin': 0,
            'padding': '2px', 'display': 'inline-block', 'border-radius': '5px', 'text-align': 'center'}
  _focus = {'outline': 0}

  def customize(self):
    self.css({"background": self.rptObj.theme.colors[0], "color": self.rptObj.theme.greys[-1],
              'border': '1px solid %s' % self.rptObj.theme.colors[0]})
    self.hover.css({'color': self.rptObj.theme.colors[-1]})


class CssDatesDatePickerHeader(CssStyle.Style):
  classname = "ui-widget-header"

  def customize(self):
    self.css({"background": self.rptObj.theme.success[1]})


class CssDatesTimePicker(CssStyle.Style):
  _attrs = {'margin': 0}
  classname = "ui-timepicker-standard"

  def customize(self):
    self.css({'color': self.rptObj.theme.greys[-1], "background": self.rptObj.theme.colors[0],
              "font-size": Defaults_css.font()})


class CssDatesTimePickerState(CssStyle.Style):
  classname = "ui-timepicker-standard .ui-state-hover"

  def customize(self):
    self.css({"background": self.rptObj.theme.colors[0]})

