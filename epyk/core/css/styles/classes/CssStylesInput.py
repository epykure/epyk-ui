
from epyk.core.html import Defaults as Defaults_html
from epyk.core.css import Defaults as Defaults_css

from epyk.core.css.styles.classes import CssStyle


class CssInput(CssStyle.Style):
  """
  CSS Base style for the input components
  """
  _attrs = {'border': 'none', 'text-align': 'center', 'cursor': 'text', 'margin': 0, 'border-radius': '5px'}
  _focus = {'outline': 0}

  def customize(self):
    self.attrs.css({"color": self.page.theme.greys[-1],
                    'font-family': Defaults_css.Font.family,
                    'line-height': '%spx' % Defaults_html.LINE_HEIGHT,
                    'border': '1px solid %s' % self.page.theme.colors[0],
                    'font-size': '%s%s' % (Defaults_css.Font.size, Defaults_css.Font.unit)})
    self.hover.css({'color': self.page.theme.colors[6]})


class CssInputRange(CssStyle.Style):
  """
  CSS Style for the input range component
  """
  _attrs = {'-webkit-appearance': 'none', 'appearance': 'none', 'outline': 'none', 'opacity': 0.7,
            '-webkit-transition': '.2s', 'transition': 'opacity .2s', 'cursor': 'pointer'}
  _hover = {'opacity': 1}
  _selectors = {'child': 'input'}

  def customize(self):
    self.attrs.css({"background": self.page.theme.colors[0]})


class CssInputRangeThumb(CssStyle.Style):
  """
  CSS Style for the thumb of the input range component
  """
  _attrs = {'-webkit-appearance': 'none', 'appearance': 'none', 'cursor': 'pointer'}
  _webkit_slider_thumb = {'-webkit-appearance': 'none', 'appearance': 'none', 'cursor': 'pointer'}
  _selectors = {'child': 'input'}

  def customize(self):
    self.webkit_slider_thumb.css({
      "background": self.page.theme.success[1],
      'width': '%spx' % Defaults_html.INPUTS_RANGE_THUMB,
      'height': '%spx' % Defaults_html.INPUTS_RANGE_THUMB})


class CssInputLabel(CssStyle.Style):
  """
  CSS Style for the label attached to an input component
  """
  _attrs = {'line-height': '1.5', 'margin-left': '10px'}
  _selectors = {'child': 'label'}

  def customize(self):
    self.attrs.css({'font-family': Defaults_css.Font.family,
                    'font-size': '%s%s' % (Defaults_css.Font.size, Defaults_css.Font.unit)})


class CssInputInteger(CssStyle.Style):
  """

  """
  cssId = {'reference': 'input[type=number]::-webkit-inner-spin-button, input[type=number]::-webkit-outer-spin-button'}
  _attrs = {"-webkit-appearance": 'none', "margin": 0}


class CssInputText(CssStyle.Style):
  """
  CSS Style for the input text component (within a field object)
  """
  _attrs = {'margin-left': '10px'}
  _selectors = {'child': 'input'}


class CssInputTextArea(CssStyle.Style):
  """
  CSS Style for the textarea component.
  """
  _attrs = {'resize': 'none', 'margin-bottom': '5px', 'padding': '5px'}
  _focus = {'outline': 0}

  def customize(self):
    self.css({"background-color": self.page.theme.colors[0], "color": self.page.theme.greys[-1],
              'border': '1px solid %s' % self.page.theme.colors[1]})
    self.hover.css({'color': self.page.theme.greys[-1]})


class CssInputValid(CssStyle.Style):
  _valid = {'color': 'red'}
  _invalid = {
    'color': 'yellow', "background": "url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/3/check.svg)",
    "background-size": "10px", "background-repeat": 'no-repeat', "background-position": "0"}


class CssUIActive(CssStyle.Style):
  classname = "ui-state-active"

  def customize(self):
    self.css({"border": "1px solid %s" % self.page.theme.success[1],
              'background-color': self.page.theme.success[1]}, important=True)
    self.hover.css({"border": "1px solid %s" % self.page.theme.success[1],
                    'background-color': self.page.theme.success[1]})


class CssUIMenuActive(CssStyle.Style):
  classname = "ui-state-active"

  def customize(self):
    self.css({"border": "1px solid %s" % self.page.theme.success[1],
              'background-color': self.page.theme.success[1]}, important=True)
    self.hover.css({"border": "1px solid %s" % self.page.theme.success[1],
                    'background-color': self.page.theme.success[1]})


class CssAutocomplete(CssStyle.Style):
  classname = "ui-autocomplete"

  def customize(self):
    self.css({'background-color': self.page.theme.colors[0], 'color': self.page.theme.greys[5]}, important=True)


class CssAutocompleteMenu(CssStyle.Style):
  classname = "ui-menu"

  def customize(self):
    self.css({'border': self.page.theme.greys[0]}, important=True)


class CssAutocompleteItemActive(CssStyle.Style):
  classname = "ui-menu .ui-state-active"

  def customize(self):
    self.css({
      'border': "1px solid %s" % self.page.theme.greys[4],
      'background': self.page.theme.colors[7],
      "color":  self.page.theme.greys[0]}, important=True)
