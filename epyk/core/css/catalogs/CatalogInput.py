#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.css.catalogs import Catalog

from epyk.core.css.styles.classes import CssStylesLabel, CssStylesDates, CssStylesInput


class CatalogInput(Catalog.CatalogGroup):
  def active(self):
    """

    """
    return self._set_class(CssStylesInput.CssUIActive)

  def slider(self):
    """

    """
    return self._set_class(CssStylesInput.CssUISlider)

  def widget_header(self):
    return self._set_class(CssStylesInput.CssUIWidgetHeader)

  def basic(self):
    """   Basic style for an input component
    """
    return self._set_class(CssStylesInput.CssInput)

  def basic_border_bottom(self):
    """   Basic style for an input component
    """
    return self._set_class(CssStylesInput.CssInputBottom)

  def basic_noborder(self):
    """   Basic style for an input component
    """
    return self._set_class(CssStylesInput.CssInputNoBorder)

  def range(self):
    """   CSS Style for the input range component
    """
    return self._set_class(CssStylesInput.CssInputRange)

  def textfield_appearance_inner(self):
    """   CSS Style for the thumb of the input number component
    """
    return self._set_class(CssStylesInput.CssInputNumberNoInnerScroll)

  def textfield_appearance_outer(self):
    """   CSS Style for the thumb of the input number component
    """
    return self._set_class(CssStylesInput.CssInputNumberNoOuterScroll)

  def textfield_appearance(self):
    """   CSS Style for the thumb of the input number component
    """
    return self._set_class(CssStylesInput.CssInputNumberNoScroll)

  def range_thumb(self):
    """   CSS Style for the thumb of the input range component
    """
    return self._set_class(CssStylesInput.CssInputRangeThumb)

  def label(self):
    """   CSS Style for the label attached to an input component
    """
    return self._set_class(CssStylesInput.CssInputLabel)

  def label_hover(self):
    """   CSS Style to change the label background color on mouse hover
    """
    return self._set_class(CssStylesLabel.CssLabelCheckMarkHover)

  def label_disable(self):
    """   CSS Style to set the label to be disabled
    """
    return self._set_class(CssStylesLabel.CssLabelContainerDisabled)

  def integer(self):
    """   Basic style for an input integer component
    """
    return self._set_class(CssStylesInput.CssInputInteger)

  def text(self):
    """   Basic style for an input text component
    """
    return self._set_class(CssStylesInput.CssInputText)

  def textarea(self):
    """   Basic style for an input textarea component
    """
    return self._set_class(CssStylesInput.CssInputTextArea)

  def is_valid(self):
    """   Basic style for an input component with a valid condition
    """
    return self._set_class(CssStylesInput.CssInputValid)

  def menu(self):
    """   

    """
    return self._set_class(CssStylesInput.CssUIMenuActive)


class CatalogDate(Catalog.CatalogGroup):
  def datepicker_ui(self):
    """

    """
    return self._set_class(CssStylesDates.CssDatePickerUI)

  def datepicker(self):
    """
    """
    return self._set_class(CssStylesDates.CssDatePicker)

  def datepicker_header(self):
    """
    """
    return self._set_class(CssStylesDates.CssDatesDatePickerHeader)

  def time_picker(self):
    """
    CSS class in charge of changing the container of the different possible items to be selected
    """
    return self._set_class(CssStylesDates.CssDatesTimePicker)

  def time_picker_items(self):
    """
    CSS class in charge of changing the color of the items on mouse hover.
    This will by default change the background of the item
    """
    return self._set_class(CssStylesDates.CssDatesTimePickerState)

  def autocomplete(self):
    """
    CSS class to change the style of the Jquery UI autocomplete input box.
    """
    return self._set_class(CssStylesInput.CssAutocomplete)

  def autocomplete_menu(self):
    """
    CSS class to change the style of the Jquery UI autocomplete dropdown menu.
    """
    return self._set_class(CssStylesInput.CssAutocompleteMenu)

  def autocomplete_item_active(self):
    """
    CSS class to change the style of the Jquery UI autocomplete active item.
    """
    return self._set_class(CssStylesInput.CssAutocompleteItemActive)
