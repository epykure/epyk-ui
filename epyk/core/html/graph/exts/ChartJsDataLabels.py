
from epyk.core.html.options import Options, Enums


class EnumDisplays(Enums):

  def withoutZeros(self):
    """
    Description:
    ------------
    Do not display the label for series with zero values.

    Usage:
    -----

    """
    return self._set_value("function(context){return context.dataset.data[context.dataIndex] !== 0}", js_type=True)

  def aboveThreshold(self, value, included=True, absolute=False):
    """
    Description:
    ------------
    Display only the labels above a specific threshold.

    Usage:
    -----

    Attributes:
    ----------
    :param value: Float. The threshold value.
    :param included: Boolean. Optional. Specify if the value should be included.
    :param absolute: Boolean. Optional. Specify if the compare is using absolute values.
    """
    if absolute:
      expr = "Math.abs(context.dataset.data[context.dataIndex])"
    else:
      expr = "context.dataset.data[context.dataIndex]"
    if included:
      return self._set_value("function(context) {return %s >= %s}" % (expr, value), js_type=True)

    return self._set_value("function(context) {return %s > %s}" % (expr, value), js_type=True)

  def belowThreshold(self, value, included=True, absolute=False):
    """
    Description:
    ------------
    Display only the labels below a specific threshold.

    Usage:
    -----

    Attributes:
    ----------
    :param value: Float. The threshold value.
    :param included: Boolean. Optional. Specify if the value should be included.
    :param absolute: Boolean. Optional. Specify if the compare is using absolute values.
    """
    if absolute:
      expr = "Math.abs(context.dataset.data[context.dataIndex])"
    else:
      expr = "context.dataset.data[context.dataIndex]"
    if included:
      return self._set_value("function(context){return %s <= %s}" % (expr, value), js_type=True)

    return self._set_value("function(context){return %s < %s}" % (expr, value), js_type=True)


class EnumFormatters(Enums):

  def details(self, digit=0, thousand_sep="."):
    """
    Description:
    -----------
    Display the label and its corresponding value.

    Usage:
    -----

    Attributes:
    ----------
    :param digit: Integer. Optional. The number of digits.
    :param thousand_sep: String. Optional. The separator for the thousand.
    """
    return self._set_value(
      "function(value, context){return context.dataset.label + '\\n' + accounting.formatNumber(value, %s, '%s') ;}" % (
        digit, thousand_sep), js_type=True)

  def label(self):
    """
    Description:
    -----------

    Usage:
    -----

    """
    return self._set_value("function(value, context) {return context.dataset.label}", js_type=True)


class Datalabels(Options):
  component_properties = ("color", )

  @property
  def align(self):
    """
    Description:
    -----------
    The align option defines the position of the label relative to the anchor point position and orientation.

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/positioning.html#alignment-and-offset
    """
    return self._config_get("center")

  @align.setter
  def align(self, value):
    self._config(value)

  @property
  def backgroundColor(self):
    """
    Description:
    -----------
    The text color for the label.

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/options.html#scriptable-options
    """
    return self._config_get(None)

  @backgroundColor.setter
  def backgroundColor(self, color):
    self._config(color)

  @property
  def borderColor(self):
    """
    Description:
    -----------
    The text color for the label.

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/options.html#scriptable-options
    """
    return self._config_get(None)

  @borderColor.setter
  def borderColor(self, color):
    self._config(color)

  @property
  def borderRadius(self):
    """
    Description:
    -----------
    The text color for the label.

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/options.html#scriptable-options
    """
    return self._config_get(None)

  @borderRadius.setter
  def borderRadius(self, num):
    self._config(num)

  @property
  def borderWidth(self):
    """
    Description:
    -----------
    The text color for the label.

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/options.html#scriptable-options
    """
    return self._config_get(None)

  @borderWidth.setter
  def borderWidth(self, num):
    self._config(num)

  @property
  def clamp(self):
    """
    Description:
    -----------
    The clamp option, when true, enforces the anchor position to be calculated based on the visible geometry of the
    associated element.

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/positioning.html#clamping
    """
    return self._config_get(False)

  @clamp.setter
  def clamp(self, flag):
    self._config(flag)

  @property
  def clip(self):
    """
    Description:
    -----------
    When the clip option is true, the part of the label which is outside the chart area will be masked.

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/positioning.html#overlap
    """
    return self._config_get(False)

  @clip.setter
  def clip(self, flag):
    self._config(flag)

  @property
  def display(self):
    """
    Description:
    -----------

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/positioning.html#rotation
    """
    return self._config_get(True)

  @display.setter
  def display(self, flag):
    self._config(flag)

  @property
  def anchor(self):
    """
    Description:
    -----------
    An anchor point is defined by an orientation vector and a position on the data element.

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/positioning.html#anchoring
    """
    return self._config_get("center")

  @anchor.setter
  def anchor(self, value):
    self._config(value)

  @property
  def color(self):
    """
    Description:
    -----------
    The text color for the label.

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/options.html#scriptable-options
    """
    return self._config_get('#F66')

  @color.setter
  def color(self, c):
    self._config(c)

  @property
  def displays(self):
    """

    :rtype: EnumDisplays
    """
    return EnumDisplays(self, "display")

  @property
  def formatters(self):
    """
    Description:
    -----------
    Pre defined formatters to show label on the chart.

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/formatting.html#data-transformation

    :rtype: EnumFormatters
    """
    return EnumFormatters(self, "formatter")

  @property
  def formatter(self):
    """
    Description:
    -----------
    Format the labels displayed on the chart.

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/formatting.html#data-transformation
    """
    return self.get(None)

  @formatter.setter
  def formatter(self, value):
    self.set(value)

  @property
  def rotation(self):
    """
    Description:
    -----------
    This option controls the clockwise rotation angle (in degrees) of the label, the rotation center point being the
    label center.

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/positioning.html#alignment-and-offset
    """
    return self.get(True)

  @rotation.setter
  def rotation(self, num):
    self.set(num)

  @property
  def textAlign(self):
    """
    Description:
    -----------
    The textAlign option only applies to multiline labels and specifies the text alignment being used when drawing
    the label text.

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/formatting.html#text-alignment
    """
    return self.get("start")

  @textAlign.setter
  def textAlign(self, value):
    self.set(value)
