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
  CssDivNoBorder = CssStylesDiv.CssDivNoBorder
  CssInput = CssStylesInput.CssInput
  CssDatePicker = CssStylesDates.CssDatePicker
  CssDatePickerUI = CssStylesDates.CssDatePickerUI
  __map, __alt_map = ['CssDivNoBorder', 'CssInput', 'CssDatePicker', 'CssDatePickerUI'], []


class CssClassTimePicker(CssGrpCls.CssGrpClass):
  CssDivNoBorder = CssStylesDiv.CssDivNoBorder
  CssInput = CssStylesInput.CssInput
  CssDatesTimePicker = CssStylesDates.CssDatesTimePicker
  __map, __alt_map = ['CssDivNoBorder', 'CssInput', 'CssDatesTimePicker'], []


class CssClassInput(CssGrpCls.CssGrpClass):
  CssDivNoBorder = CssStylesDiv.CssDivNoBorder
  CssDatePicker = CssStylesDates.CssDatePicker
  __map, __alt_map = ['CssDivNoBorder', 'CssInput'], []


class CssClassTextArea(CssGrpCls.CssGrpClass):
  CssInputTextArea = CssStylesInput.CssInputTextArea
  __map, __alt_map = ['CssInputTextArea'], []


class CssClassInputSearch(CssGrpCls.CssGrpClass):
  CssSearchButton = CssStylesSearch.CssSearchButton
  __map, __alt_map = ['CssSearchButton'], []


class CssClassInputInteger(CssGrpCls.CssGrpClass):
  CssDivNoBorder = CssStylesDiv.CssDivNoBorder
  CssInput = CssStylesInput.CssInput
  CssInputInteger = CssStylesInput.CssInputInteger
  __map, __alt_map = ['CssSearchButton'], []


class CssClassInputRange(CssGrpCls.CssGrpClass):
  CssDivNoBorder = CssStylesDiv.CssDivNoBorder
  CssInput = CssStylesInput.CssInput
  CssInputInteger = CssStylesInput.CssInputInteger
  CssInputRange = CssStylesInput.CssInputRange
  CssInputRangeThumb = CssStylesInput.CssInputRangeThumb
  __map, __alt_map = ['CssDivNoBorder', 'CssInput', 'CssInputInteger', 'CssInputRange', 'CssInputRangeThumb'], []


class CssClassPopup(CssGrpCls.CssGrpClass):
  CssPopupTable = CssStylesPopup.CssPopupTable
  __map, __alt_map = ['CssPopupTable'], []
