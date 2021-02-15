
from epyk.core.data.DataClass import DataClass, DataEnum

from epyk.core.js.primitives import JsObjects


class EnumFormatters(DataEnum):

  js_conversion = True

  def details(self, digit=0, thousand_sep="."):
    """
    Description:
    -----------

    """
    return self.set(JsObjects.JsVoid("function(value, context) {return context.dataset.label + '\\n\\n' + accounting.formatNumber(value, %s, '%s') ;}" % (digit, thousand_sep)))

  def label(self, digit=0, thousand_sep="."):
    """
    Description:
    -----------

    """
    return self.set(JsObjects.JsVoid("function(value, context) {return context.dataset.label}"))


class Datalabels(DataClass):
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
    return self.get("center")

  @align.setter
  def align(self, value):
    self.set(value)

  @property
  def backgroundColor(self):
    """
    Description:
    -----------
    The text color for the label.

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/options.html#scriptable-options
    """
    return self.get(None)

  @backgroundColor.setter
  def backgroundColor(self, color):
    self.set(color)

  @property
  def borderColor(self):
    """
    Description:
    -----------
    The text color for the label.

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/options.html#scriptable-options
    """
    return self.get(None)

  @borderColor.setter
  def borderColor(self, color):
    self.set(color)

  @property
  def borderRadius(self):
    """
    Description:
    -----------
    The text color for the label.

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/options.html#scriptable-options
    """
    return self.get(None)

  @borderRadius.setter
  def borderRadius(self, num):
    self.set(num)

  @property
  def borderWidth(self):
    """
    Description:
    -----------
    The text color for the label.

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/options.html#scriptable-options
    """
    return self.get(None)

  @borderWidth.setter
  def borderWidth(self, num):
    self.set(num)

  @property
  def clamp(self):
    """
    Description:
    -----------
    The clamp option, when true, enforces the anchor position to be calculated based on the visible geometry of the associated element.

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/positioning.html#clamping
    """
    return self.get(False)

  @clamp.setter
  def clamp(self, flag):
    self.set(flag)

  @property
  def clip(self):
    """
    Description:
    -----------
    When the clip option is true, the part of the label which is outside the chart area will be masked.

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/positioning.html#overlap
    """
    return self.get(False)

  @clip.setter
  def clip(self, flag):
    self.set(flag)

  @property
  def display(self):
    """
    Description:
    -----------

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/positioning.html#rotation
    """
    return self.get(True)

  @display.setter
  def display(self, bool):
    self.set(bool)

  @property
  def anchor(self):
    """
    Description:
    -----------
    An anchor point is defined by an orientation vector and a position on the data element.

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/positioning.html#anchoring
    """
    return self.get("center")

  @anchor.setter
  def anchor(self, value):
    self.set(value)

  @property
  def color(self):
    """
    Description:
    -----------
    The text color for the label.

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/options.html#scriptable-options
    """
    return self.get('#F66')

  @color.setter
  def color(self, color):
    self.set(color)

  @property
  def formatters(self):
    """
    Description:
    -----------
    Pre defined formatters to show label on the chart.

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/formatting.html#data-transformation
    """
    return self.sub_data("formatter", EnumFormatters)

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
    This option controls the clockwise rotation angle (in degrees) of the label, the rotation center point being the label center.

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
    The textAlign option only applies to multiline labels and specifies the text alignment being used when drawing the label text.

    Related Pages:

      https://chartjs-plugin-datalabels.netlify.app/guide/formatting.html#text-alignment
    """
    return self.get("start")

  @textAlign.setter
  def textAlign(self, value):
    self.set(value)
