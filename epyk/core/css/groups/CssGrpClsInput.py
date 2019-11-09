"""
Group CSS class for all the Text components (this will include rich text components)
"""

from epyk.core.css.groups import CssGrpCls

# The list of CSS classes
from epyk.core.css.styles import CssStylesDiv
from epyk.core.css.styles import CssStylesPopup
from epyk.core.css.styles import CssStylesInput
from epyk.core.css.styles import CssStylesSearch
from epyk.core.css.styles import CssStylesDates


class CssClassDatePicker(CssGrpCls.CssGrpClass):
  """

  """
  css_div_no_border = CssStylesDiv.CssDivNoBorder
  Css_input = CssStylesInput.CssInput
  Css_date_picker = CssStylesDates.CssDatePicker
  Css_date_picker_ui = CssStylesDates.CssDatePickerUI
  __map, __alt_map = ['CssDivNoBorder', 'CssInput', 'CssDatePicker', 'CssDatePickerUI'], []


class CssClassTimePicker(CssGrpCls.CssGrpClass):
  """

  """
  css_div_no_border = CssStylesDiv.CssDivNoBorder
  Css_input = CssStylesInput.CssInput
  Css_dates_time_picker = CssStylesDates.CssDatesTimePicker
  __map, __alt_map = ['CssDivNoBorder', 'CssInput', 'CssDatesTimePicker'], []


class CssClassInput(CssGrpCls.CssGrpClass):
  """
  CSS Basic group for all the Input components
  """
  css_div_no_border = CssStylesDiv.CssDivNoBorder
  css_date_picker = CssStylesDates.CssDatePicker
  __map, __alt_map = ['CssDivNoBorder', 'CssInput'], []


class CssClassTextArea(CssGrpCls.CssGrpClass):
  """

  """
  css_input_text_area = CssStylesInput.CssInputTextArea
  __map, __alt_map = ['CssInputTextArea'], []


class CssClassInputSearch(CssGrpCls.CssGrpClass):
  """

  """
  css_search_button = CssStylesSearch.CssSearchButton
  __map, __alt_map = ['CssSearchButton'], []


class CssClassInputInteger(CssGrpCls.CssGrpClass):
  """

  """
  css_div_no_border = CssStylesDiv.CssDivNoBorder
  css_input = CssStylesInput.CssInput
  css_input_integer = CssStylesInput.CssInputInteger
  __map, __alt_map = ['CssSearchButton'], []


class CssClassInputRange(CssGrpCls.CssGrpClass):
  """

  """
  css_div_no_border = CssStylesDiv.CssDivNoBorder
  css_input = CssStylesInput.CssInput
  css_input_integer = CssStylesInput.CssInputInteger
  css_input_range = CssStylesInput.CssInputRange
  css_input_range_thumb = CssStylesInput.CssInputRangeThumb
  __map, __alt_map = ['CssDivNoBorder', 'CssInput', 'CssInputInteger', 'CssInputRange', 'CssInputRangeThumb'], []


class CssClassPopup(CssGrpCls.CssGrpClass):
  """

  """
  css_popup_table = CssStylesPopup.CssPopupTable
  __map, __alt_map = ['CssPopupTable'], []
