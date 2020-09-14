#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.css.catalogs import Catalog

from epyk.core.css.styles.classes import CssStylesLabel, CssStylesDates, CssStylesInput


class CatalogInput(Catalog.CatalogGroup):
  def active(self):
    """

    """
    return self._set_class(CssStylesInput.CssUIActive)

  def basic(self):
    """
    Description:
    -----------
    Basic style for an input component
    """
    return self._set_class(CssStylesInput.CssInput)

  def range(self):
    """
    Description:
    -----------
    CSS Style for the input range component
    """
    return self._set_class(CssStylesInput.CssInputRange)

  def range_thumb(self):
    """
    Description:
    -----------
    CSS Style for the thumb of the input range component
    """
    return self._set_class(CssStylesInput.CssInputRangeThumb)

  def label(self):
    """
    Description:
    -----------
    CSS Style for the label attached to an input component
    """
    return self._set_class(CssStylesInput.CssInputLabel)

  def label_hover(self):
    """
    Description:
    -----------
    CSS Style to change the label background color on mouse hover
    """
    return self._set_class(CssStylesLabel.CssLabelCheckMarkHover)

  def label_disable(self):
    """
    Description:
    -----------
    CSS Style to set the label to be disabled
    """
    return self._set_class(CssStylesLabel.CssLabelContainerDisabled)

  def integer(self):
    """
    Description:
    -----------
    Basic style for an input integer component
    """
    return self._set_class(CssStylesInput.CssInputInteger)

  def text(self):
    """
    Description:
    -----------
    Basic style for an input text component
    """
    return self._set_class(CssStylesInput.CssInputText)

  def textarea(self):
    """
    Description:
    -----------
    Basic style for an input textarea component
    """
    return self._set_class(CssStylesInput.CssInputTextArea)

  def is_valid(self):
    """
    Description:
    -----------
    Basic style for an input component with a valid condition
    """
    return self._set_class(CssStylesInput.CssInputValid)

  def menu(self):
    """
    Description:
    -----------

    """
    return self._set_class(CssStylesInput.CssUIMenuActive)


class CatalogDate(Catalog.CatalogGroup):
  def datepicker_ui(self):
    """
    Description:
    ------------

    """
    return self._set_class(CssStylesDates.CssDatePickerUI)

  def datepicker(self):
    """
    Description:
    ------------
    """
    return self._set_class(CssStylesDates.CssDatePicker)

  def datepicker_header(self):
    """
    Description:
    ------------
    """
    return self._set_class(CssStylesDates.CssDatesDatePickerHeader)

  def time_picker(self):
    """
    Description:
    ------------
    CSS class in charge of changing the container of the different possible items to be selected
    """
    return self._set_class(CssStylesDates.CssDatesTimePicker)

  def time_picker_items(self):
    """
    Description:
    ------------
    CSS class in charge of changing the color of the items on mouse hover.
    This will by default change the background of the item
    """
    return self._set_class(CssStylesDates.CssDatesTimePickerState)
