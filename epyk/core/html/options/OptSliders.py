
from epyk.core.data import DataClass


class OptionsSlider(DataClass):

  @property
  def animate(self):
    """
    Description:
    ------------
    Whether to slide the handle smoothly when the user clicks on the slider track. Also accepts any valid animation

    Related Pages:
    --------------
    https://api.jqueryui.com/slider/#option-animate
    """
    return self._report._jsStyles('animate', False)

  @animate.setter
  def animate(self, value):
    self._report._jsStyles["animate"] = value
    return self

  @property
  def classes(self):
    """
    Description:
    ------------
    Specify additional classes to add to the widget's elements.
    Any of classes specified in the Theming section can be used as keys to override their value.
    To learn more about this option, check out the learn article about the classes option.

    Related Pages:
    --------------
    https://api.jqueryui.com/slider/#option-classes
    """
    return self._report._jsStyles('classes')

  @classes.setter
  def classes(self, value):
    self._report._jsStyles["classes"] = value
    return self

  @property
  def disabled(self):
    """
    Description:
    ------------
    Disables the slider if set to true.

    Related Pages:
    --------------
    https://api.jqueryui.com/slider/#option-disabled
    """
    return self._report._jsStyles('disabled', False)

  @disabled.setter
  def disabled(self, value):
    self._report._jsStyles["disabled"] = value
    return self

  @property
  def max(self):
    """
    Description:
    ------------
    The maximum value of the slider.

    Related Pages:
    --------------
    https://api.jqueryui.com/slider/#option-max
    """
    return self._report._jsStyles('max', 100)

  @max.setter
  def max(self, value):
    self._report._jsStyles["max"] = value
    return self

  @property
  def min(self):
    """
    Description:
    ------------
    The minimum value of the slider.

    Related Pages:
    --------------
    https://api.jqueryui.com/slider/#option-min
    """
    return self._report._jsStyles('min', 0)

  @min.setter
  def min(self, value):
    self._report._jsStyles["min"] = value
    return self

  @property
  def orientation(self):
    """
    Description:
    ------------
    Determines whether the slider handles move horizontally (min on left, max on right) or vertically (min on bottom, max on top).
    Possible values: "horizontal", "vertical".

    Related Pages:
    --------------
    https://api.jqueryui.com/slider/#option-orientation
    """
    return self._report._jsStyles('orientation', "horizontal")

  @orientation.setter
  def orientation(self, value):
    self._report._jsStyles["orientation"] = value
    return self

  @property
  def range(self):
    """
    Description:
    ------------
    Whether the slider represents a range.

    Related Pages:
    --------------
    https://api.jqueryui.com/slider/#option-range
    """
    return self._report._jsStyles('range', False)

  @range.setter
  def range(self, value):
    self._report._jsStyles["range"] = value
    return self

  @property
  def step(self):
    """
    Description:
    ------------
    Determines the size or amount of each interval or step the slider takes between the min and max.
    The full specified value range of the slider (max - min) should be evenly divisible by the step.

    Related Pages:
    --------------
    https://api.jqueryui.com/slider/#option-step
    """
    return self._report._jsStyles('step', 1)

  @step.setter
  def step(self, value):
    self._report._jsStyles["step"] = value
    return self

  @property
  def value(self):
    """
    Description:
    ------------
    Determines the value of the slider, if there's only one handle.
    If there is more than one handle, determines the value of the first handle.

    Related Pages:
    --------------
    https://api.jqueryui.com/slider/#option-value
    """
    return self._report._jsStyles('value', 0)

  @value.setter
  def value(self, value):
    self._report._jsStyles["value"] = value
    return self

  @property
  def values(self):
    """
    Description:
    ------------
    This option can be used to specify multiple handles.
    If the range option is set to true, the length of values should be 2.

    Related Pages:
    --------------
    https://api.jqueryui.com/slider/#option-values
    """
    return self._report._jsStyles('values', 0)

  @values.setter
  def values(self, value):
    self._report._jsStyles["values"] = value
    return self


class OptionsProgBar(DataClass):

  @property
  def classes(self):
    """
    Description:
    ------------
    Initialize the progressbar with the classes option specified, changing the theming for the ui-progressbar

    Related Pages:
    --------------
    https://api.jqueryui.com/progressbar/#option-classes
    """
    return self._report._jsStyles('classes')

  @classes.setter
  def classes(self, value):
    self._report._jsStyles["classes"] = value
    return self

  @property
  def disabled (self):
    """
    Description:
    ------------
    Disables the progressbar if set to true.

    Related Pages:
    --------------
    https://api.jqueryui.com/progressbar/#option-disabled
    """
    return self._report._jsStyles('disabled ', False)

  @disabled .setter
  def disabled (self, bool):
    self._report._jsStyles["disabled "] = bool
    return self

  @property
  def max(self):
    """
    Description:
    ------------
    The maximum value of the progressbar.

    Related Pages:
    --------------
    https://api.jqueryui.com/progressbar/#option-max
    """
    return self._report._jsStyles('max', False)

  @max.setter
  def max(self, bool):
    self._report._jsStyles["max"] = bool
    return self

  @property
  def value(self):
    """
    Description:
    ------------
    The value of the progressbar.

    Related Pages:
    --------------
    https://api.jqueryui.com/progressbar/#option-value
    """
    return self._report._jsStyles('value', False)

  @value.setter
  def value(self, bool):
    self._report._jsStyles["value"] = bool
    return self
