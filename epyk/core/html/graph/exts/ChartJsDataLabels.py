
from typing import Optional, Union
from epyk.core.html.options import Options, Enums


class EnumDisplays(Enums):

  def withoutZeros(self):
    """
    Do not display the label for series with zero values.

    Usage::

    """
    return self._set_value("function(context){return context.dataset.data[context.dataIndex] !== 0}", js_type=True)

  def aboveThreshold(self, value, included=True, absolute=False):
    """
    Display only the labels above a specific threshold.

    Usage::

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
    Display only the labels below a specific threshold.

    Usage::

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
    """   Display the label and its corresponding value.

    Usage::

    :param digit: Integer. Optional. The number of digits.
    :param thousand_sep: String. Optional. The separator for the thousand.
    """
    return self._set_value(
      "function(value, context){return context.dataset.label + '\\n' + accounting.formatNumber(value, %s, '%s') ;}" % (
        digit, thousand_sep), js_type=True)

  def label(self):
    """   

    Usage::

    """
    return self._set_value("function(value, context) {return context.dataset.label}", js_type=True)


class Padding(Options):

  @property
  def top(self):
    """

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/options.html#indexable-options
    """
    return self._config_get(None)

  @top.setter
  def top(self, value: float):
    self._config(value)

  @property
  def right(self):
    """

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/options.html#indexable-options
    """
    return self._config_get(None)

  @right.setter
  def right(self, value: float):
    self._config(value)

  @property
  def bottom(self):
    """

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/options.html#indexable-options
    """
    return self._config_get(None)

  @bottom.setter
  def bottom(self, value: float):
    self._config(value)

  @property
  def left(self):
    """

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/options.html#indexable-options
    """
    return self._config_get(None)

  @left.setter
  def left(self, value: float):
    self._config(value)


class Font(Options):

  @property
  def family(self):
    """

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/positioning.html#alignment-and-offset
    """
    return self._config_get(None)

  @family.setter
  def family(self, value: str):
    self._config(value)

  @property
  def size(self):
    """

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/positioning.html#alignment-and-offset
    """
    return self._config_get(None)

  @size.setter
  def size(self, value: str):
    self._config(value)

  @property
  def style(self):
    """

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/positioning.html#alignment-and-offset
    """
    return self._config_get(None)

  @style.setter
  def style(self, value: str):
    self._config(value)

  @property
  def weight(self):
    """

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/positioning.html#alignment-and-offset
    """
    return self._config_get(None)

  @weight.setter
  def weight(self, value: str):
    self._config(value)

  @property
  def lineHeight(self):
    """

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/formatting.html#multiline-labels
    """
    return self._config_get(None)

  @lineHeight.setter
  def lineHeight(self, value: Union[str, float]):
    self._config(value)


class Datalabels(Options):
  component_properties = ("color", )

  @property
  def align(self):
    """ The align option defines the position of the label relative to the anchor point position and orientation.

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/positioning.html#alignment-and-offset
    """
    return self._config_get("center")

  @align.setter
  def align(self, value: str):
    self._config(value)

  @property
  def anchor(self):
    """ An anchor point is defined by an orientation vector and a position on the data element.

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/positioning.html#anchoring
    """
    return self._config_get("center")

  @anchor.setter
  def anchor(self, value: str):
    self._config(value)

  @property
  def backgroundColor(self):
    """ The text color for the label.

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/options.html#scriptable-options
    """
    return self._config_get(None)

  @backgroundColor.setter
  def backgroundColor(self, color: Optional[str]):
    self._config(color)

  @property
  def borderColor(self):
    """   The text color for the label.

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/options.html#scriptable-options
    """
    return self._config_get(None)

  @borderColor.setter
  def borderColor(self, color: Optional[str]):
    self._config(color)

  @property
  def borderRadius(self):
    """ The text color for the label.

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/options.html#scriptable-options
    """
    return self._config_get(None)

  @borderRadius.setter
  def borderRadius(self, num: float):
    self._config(num)

  @property
  def borderWidth(self):
    """ The text color for the label.

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/options.html#scriptable-options
    """
    return self._config_get(None)

  @borderWidth.setter
  def borderWidth(self, num: float):
    self._config(num)

  @property
  def clamp(self):
    """ The clamp option, when true, enforces the anchor position to be calculated based on the visible geometry of the
    associated element.

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/positioning.html#clamping
    """
    return self._config_get(False)

  @clamp.setter
  def clamp(self, flag: bool):
    self._config(flag)

  @property
  def clip(self):
    """ When the clip option is true, the part of the label which is outside the chart area will be masked.

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/positioning.html#overlap
    """
    return self._config_get(False)

  @clip.setter
  def clip(self, flag: bool):
    self._config(flag)

  @property
  def color(self):
    """ The text color for the label.

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/options.html#scriptable-options
    """
    return self._config_get('#F66')

  @color.setter
  def color(self, c: str):
    self._config(c)

  @property
  def display(self):
    """   

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/positioning.html#rotation
    """
    return self._config_get(True)

  @display.setter
  def display(self, value: Union[str, bool]):
    self._config(value)

  @property
  def displays(self) -> EnumDisplays:
    """

    """
    return EnumDisplays(self, "display")

  @property
  def font(self):
    """

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/options.html#indexable-options
    """
    return self._config_get(None)

  @font.setter
  def font(self, values: dict):
    self._config(values)

  def fonts(self) -> Font:
    """

    Related Pages:


    """
    return self._config_sub_data("font", Font)

  @property
  def formatters(self) -> EnumFormatters:
    """ Pre-defined formatters to show label on the chart.

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/formatting.html#data-transformation
    """
    return EnumFormatters(self, "formatter")

  @property
  def formatter(self):
    """ Format the labels displayed on the chart.

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/formatting.html#data-transformation
    """
    return self.get(None)

  @formatter.setter
  def formatter(self, value):
    self.set(value)

  @property
  def padding(self):
    """

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/options.html#indexable-options
    """
    return self._config_get(None)

  @padding.setter
  def padding(self, values: dict):
    self._config(values)

  def paddings(self) -> Padding:
    """

    Related Pages:


    """
    return self._config_sub_data("padding", Padding)

  @property
  def rotation(self):
    """ This option controls the clockwise rotation angle (in degrees) of the label, the rotation center point being the
    label center.

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/positioning.html#alignment-and-offset
    """
    return self.get(0)

  @rotation.setter
  def rotation(self, num: float):
    self.set(num)

  @property
  def textAlign(self):
    """ The textAlign option only applies to multiline labels and specifies the text alignment being used when drawing
    the label text.

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/formatting.html#text-alignment
    """
    return self.get("start")

  @textAlign.setter
  def textAlign(self, value: str):
    self.set(value)

  @property
  def textStrokeColor(self):
    """

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/formatting.html#text-alignment
    """
    return self.get(None)

  @textStrokeColor.setter
  def textStrokeColor(self, value: str):
    self.set(value)

  @property
  def textStrokeWidth(self):
    """

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/formatting.html#text-alignment
    """
    return self.get(0)

  @textStrokeWidth.setter
  def textStrokeWidth(self, num: float):
    self.set(num)

  @property
  def textShadowBlur(self):
    """

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/formatting.html#text-alignment
    """
    return self.get(0)

  @textShadowBlur.setter
  def textShadowBlur(self, num: float):
    self.set(num)

  @property
  def textShadowColor(self):
    """

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/formatting.html#text-alignment
    """
    return self.get(None)

  @textShadowColor.setter
  def textShadowColor(self, color: str):
    self.set(color)
