
from epyk.core.html.options import Enums
from epyk.core.html.options import Options
from epyk.core.js import JsUtils
from epyk.core.js.packages import packageImport


class EnumRender(Enums):

  def label(self):
    """
    Description:
    -----------

    """
    return self._set_value()

  def value(self):
    """
    Description:
    -----------

    """
    return self._set_value()

  def percentage(self):
    """
    Description:
    -----------

    """
    return self._set_value()

  def image(self):
    """
    Description:
    -----------

    """
    return self._set_value()

  def custom(self, jsFncs):
    """
    Description:
    -----------

    """
    return self._set_value()

  @packageImport("accounting")
  def details(self, digit=0, thousand_sep="."):
    """
    Description:
    ------------
    Display both the label and its value.

    Attributes:
    ----------
    :param digit: String. Optional. Decimal point separator
    :param thousand_sep: String. Optional. thousands separator
    """
    return self._set_value(
      "function (args) {return args.dataset.label + ': ' + accounting.formatNumber(args.value, %s, '%s') }" % (
        digit, thousand_sep), js_type=True)

  @packageImport("accounting")
  def labelNumber(self, digit=0, thousand_sep="."):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param digit: String. Optional. Decimal point separator
    :param thousand_sep: String. Optional. thousands separator
    """
    return self._set_value(
      "function (args) {return accounting.formatNumber(args.value, %s, '%s') }" % (digit, thousand_sep), js_type=True)

  @packageImport("accounting")
  def labelCurrency(self, symbol="", digit=0, thousand_sep=".", decimal_sep=","):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param symbol: String. Optional. Default currency symbol is ''
    :param digit: String. Optional. Decimal point separator
    :param thousand_sep: String. Optional. thousands separator
    :param decimal_sep: String. Optional. Decimal point separator
    """
    symbol = JsUtils.jsConvertData(symbol, None)
    thousand_sep = JsUtils.jsConvertData(thousand_sep, None)
    decimal_sep = JsUtils.jsConvertData(decimal_sep, None)
    return self._set_value(
      "function(args) { return accounting.formatMoney(args.value, %s, %s, %s, %s) }" % (
      symbol, digit, thousand_sep, decimal_sep), js_type=True)


class LabelsImages(Options):

  @property
  def src(self):
    """
    Description:
    -----------
    Define the image path.

    Related Pages:

      https://github.com/emn178/chartjs-plugin-labels
    """
    return self._config_get(None)

  @src.setter
  def src(self, image):
    self._config(image)

  @property
  def width(self):
    """
    Description:
    -----------
    Set the image height in pixel.

    Related Pages:

      https://github.com/emn178/chartjs-plugin-labels
    """
    return self._config_get(16)

  @width.setter
  def width(self, num):
    self._config(num)

  @property
  def height(self):
    """
    Description:
    -----------
    Set the image height in pixel.

    Related Pages:

      https://github.com/emn178/chartjs-plugin-labels
    """
    return self._config_get(16)

  @height.setter
  def height(self, num):
    self._config(num)


class Labels(Options):

  @property
  def render(self):
    """
    Description:
    -----------
    render 'label', 'value', 'percentage', 'image' or custom function, default is 'percentage'.

    Related Pages:

      https://github.com/emn178/chartjs-plugin-labels

    :rtype: EnumRender
    """
    return EnumRender(self, "render")

  @property
  def precision(self):
    """
    Description:
    -----------
    precision for percentage, default is 0

    Related Pages:

      https://github.com/emn178/chartjs-plugin-labels
    """
    return self._config_get(0)

  @precision.setter
  def precision(self, num):
    self._config(num)

  @property
  def showZero(self):
    """
    Description:
    -----------
    Identifies whether or not labels of value 0 are displayed, default is false

    Related Pages:

      https://github.com/emn178/chartjs-plugin-labels
    """
    return self._config_get(True)

  @showZero.setter
  def showZero(self, flag):
    self._config(flag)

  @property
  def fontSize(self):
    """
    Description:
    -----------
    Font size, default is defaultFontSize

    Related Pages:

      https://github.com/emn178/chartjs-plugin-labels
    """
    return self._config_get(12)

  @fontSize.setter
  def fontSize(self, num):
    self._config(num)

  @property
  def fontColor(self):
    """
    Description:
    -----------
    Font color, can be color array for each data or function for dynamic color, default is defaultFontColor.

    Related Pages:

      https://github.com/emn178/chartjs-plugin-labels
    """
    return self._config_get("#fff")

  @fontColor.setter
  def fontColor(self, value):
    self._config(value)

  @property
  def fontStyle(self):
    """
    Description:
    -----------
    Font style, default is defaultFontStyle.

    Related Pages:

      https://github.com/emn178/chartjs-plugin-labels
    """
    return self._config_get('normal')

  @fontStyle.setter
  def fontStyle(self, value):
    self._config(value)

  @property
  def fontFamily(self):
    """
    Description:
    -----------
    Font family, default is defaultFontFamily.

    Related Pages:

      https://github.com/emn178/chartjs-plugin-labels
    """
    return self._config_get("'Helvetica Neue', 'Helvetica', 'Arial', sans-serif")

  @fontFamily.setter
  def fontFamily(self, value):
    self._config(value)

  @property
  def textShadow(self):
    """
    Description:
    -----------
    Draw text shadows under labels, default is false.

    Related Pages:

      https://github.com/emn178/chartjs-plugin-labels
    """
    return self._config_get(True)

  @textShadow.setter
  def textShadow(self, flag):
    self._config(flag)

  @property
  def shadowBlur(self):
    """
    Description:
    -----------
    Text shadow intensity, default is 6.

    Related Pages:

      https://github.com/emn178/chartjs-plugin-labels
    """
    return self._config_get(10)

  @shadowBlur.setter
  def shadowBlur(self, num):
    self._config(num)

  @property
  def shadowOffsetX(self):
    """
    Description:
    -----------
    Text shadow X offset, default is 3.

    Related Pages:

      https://github.com/emn178/chartjs-plugin-labels
    """
    return self._config_get(-5)

  @shadowOffsetX.setter
  def shadowOffsetX(self, num):
    self._config(num)

  @property
  def shadowOffsetY(self):
    """
    Description:
    -----------
    Text shadow Y offset, default is 3.

    Related Pages:

      https://github.com/emn178/chartjs-plugin-labels
    """
    return self._config_get(5)

  @shadowOffsetY.setter
  def shadowOffsetY(self, num):
    self._config(num)

  @property
  def shadowColor(self):
    """
    Description:
    -----------
    Text shadow color, default is 'rgba(0,0,0,0.3)'.

    Related Pages:

      https://github.com/emn178/chartjs-plugin-labels
    """
    return self._config_get('rgba(255,0,0,0.75)')

  @shadowColor.setter
  def shadowColor(self, value):
    self._config(value)

  @property
  def arc(self):
    """
    Description:
    -----------
    Draw label in arc, default is false, bar chart ignores this.

    Related Pages:

      https://github.com/emn178/chartjs-plugin-labels
    """
    return self._config_get(True)

  @arc.setter
  def arc(self, flag):
    self._config(flag)

  @property
  def position(self):
    """
    Description:
    -----------
    Position to draw label, available value is 'default', 'border' and 'outside'
    default is 'default'.

    Related Pages:

      https://github.com/emn178/chartjs-plugin-labels
    """
    return self._config_get("default")

  @position.setter
  def position(self, value):
    self._config(value)

  @property
  def overlap(self):
    """
    Description:
    -----------
    Draw label even it's overlap, default is true.

    Related Pages:

      https://github.com/emn178/chartjs-plugin-labels
    """
    return self._config_get(True)

  @overlap.setter
  def overlap(self, flag):
    self._config(flag)

  @property
  def outsidePadding(self):
    """
    Description:
    -----------
    add padding when position is `outside`.

    Related Pages:

      https://github.com/emn178/chartjs-plugin-labels
    """
    return self._config_get(4)

  @outsidePadding.setter
  def outsidePadding(self, num):
    self._config(num)

  @property
  def images(self):
    """
    Description:
    -----------
    set images when `render` is 'image'.

    :rtype: LabelsImages
    """
    self.render.image()
    return self._config_sub_data("images", LabelsImages)

  @property
  def textMargin(self):
    """
    Description:
    -----------
    Add margin of text when position is `outside` or `border`.

    Related Pages:

      https://github.com/emn178/chartjs-plugin-labels
    """
    return self._config_get(4)

  @textMargin.setter
  def textMargin(self, num):
    self._config(num)
