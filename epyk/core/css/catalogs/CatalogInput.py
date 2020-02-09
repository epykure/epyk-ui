"""

"""

from epyk.core.css.catalogs import Catalog

from epyk.core.css.styles.classes import CssStylesLabel, CssStylesDates, CssStylesInput


class CatalogInput(Catalog.CatalogGroup):
  def basic(self):
    """ Basic style for an input component """
    return self._set_class(CssStylesInput.CssInput)

  def range(self):
    """ CSS Style for the input range component """
    return self._set_class(CssStylesInput.CssInputRange)

  def range_thumb(self):
    """ CSS Style for the thumb of the input range component """
    return self._set_class(CssStylesInput.CssInputRangeThumb)

  def label(self):
    """ CSS Style for the label attached to an input component """
    return self._set_class(CssStylesInput.CssInputLabel)

  def label_hover(self):
    """ CSS Style to change the label background color on mouse hover """
    return self._set_class(CssStylesLabel.CssLabelCheckMarkHover)

  def label_disable(self):
    """ CSS Style to set the label to be disabled """
    return self._set_class(CssStylesLabel.CssLabelContainerDisabled)

  def integer(self):
    """ Basic style for an input integer component """
    return self._set_class(CssStylesInput.CssInputInteger)

  def text(self):
    """ Basic style for an input text component """
    return self._set_class(CssStylesInput.CssInputText)

  def textarea(self):
    """ Basic style for an input textarea component """
    return self._set_class(CssStylesInput.CssInputTextArea)

  def is_valid(self):
    """ Basic style for an input component with a valid condition """
    return self._set_class(CssStylesInput.CssInputValid)


class CatalogDate(Catalog.CatalogGroup):
  def datepicker_ui(self):
    """  """
    return self._set_class(CssStylesDates.CssDatePickerUI)

  def datepicker(self):
    """  """
    return self._set_class(CssStylesDates.CssDatePicker)

  def time_picker(self):
    """  """
    return self._set_class(CssStylesDates.CssDatesTimePicker)

