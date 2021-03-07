from epyk.core.data.DataClass import DataClass, DataEnum

from epyk.core.js import JsUtils
from epyk.core.js.packages import packageImport
from epyk.core.js.primitives import JsObjects


class EnumRender(DataEnum):
  js_conversion = True

  def label(self):
    """
    Description:
    -----------

    """
    return self.set()

  def value(self):
    """
    Description:
    -----------

    """
    return self.set()

  def percentage(self):
    """
    Description:
    -----------

    """
    return self.set()

  def image(self):
    """
    Description:
    -----------

    """
    return self.set()

  def custom(self, jsFncs):
    """
    Description:
    -----------

    """
    return self.set()

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
    return self.set(JsObjects.JsVoid("function (args) { return args.dataset.label + ': ' + accounting.formatNumber(args.value, %s, '%s') }" % (digit, thousand_sep)))

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
    return self.set(JsObjects.JsVoid("function (args) {return accounting.formatNumber(args.value, %s, '%s') }" % (digit, thousand_sep)))

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
    return self.set(JsObjects.JsVoid(
      "function(args) { return accounting.formatMoney(args.value, %s, %s, %s, %s) }" % (
      symbol, digit, thousand_sep, decimal_sep)))


class LabelsImages(DataClass):

  @property
  def src(self):
    """
    Description:
    -----------
    Define the image path.

    Related Pages:

      https://github.com/emn178/chartjs-plugin-labels
    """
    return self.get(None)

  @src.setter
  def src(self, image):
    self.set(image)

  @property
  def width(self):
    """
    Description:
    -----------
    Set the image height in pixel.

    Related Pages:

      https://github.com/emn178/chartjs-plugin-labels
    """
    return self.get(16)

  @width.setter
  def width(self, num):
    self.set(num)

  @property
  def height(self):
    """
    Description:
    -----------
    Set the image height in pixel.

    Related Pages:

      https://github.com/emn178/chartjs-plugin-labels
    """
    return self.get(16)

  @height.setter
  def height(self, num):
    self.set(num)


class Labels(DataClass):

  @property
  def render(self):
    """
    Description:
    -----------
    render 'label', 'value', 'percentage', 'image' or custom function, default is 'percentage'

    Related Pages:

      https://github.com/emn178/chartjs-plugin-labels
    """
    return self.sub_data("render", EnumRender)

  @property
  def precision(self):
    """
    Description:
    -----------
    precision for percentage, default is 0

    Related Pages:

      https://github.com/emn178/chartjs-plugin-labels
    """
    return self.get(0)

  @precision.setter
  def precision(self, num):
    self.set(num)

  @property
  def showZero(self):
    """
    Description:
    -----------
    Identifies whether or not labels of value 0 are displayed, default is false

    Related Pages:

      https://github.com/emn178/chartjs-plugin-labels
    """
    return self.get(True)

  @showZero.setter
  def showZero(self, flag):
    self.set(flag)

  @property
  def fontSize(self):
    """
    Description:
    -----------
    Font size, default is defaultFontSize

    Related Pages:

      https://github.com/emn178/chartjs-plugin-labels
    """
    return self.get(12)

  @fontSize.setter
  def fontSize(self, num):
    self.set(num)

  @property
  def fontColor(self):
    """
    Description:
    -----------
    Font color, can be color array for each data or function for dynamic color, default is defaultFontColor

    Related Pages:

      https://github.com/emn178/chartjs-plugin-labels
    """
    return self.get("#fff")

  @fontColor.setter
  def fontColor(self, value):
    self.set(value)

  @property
  def fontStyle(self):
    """
    Description:
    -----------
    Font style, default is defaultFontStyle

    Related Pages:

      https://github.com/emn178/chartjs-plugin-labels
    """
    return self.get('normal')

  @fontStyle.setter
  def fontStyle(self, value):
    self.set(value)

  @property
  def fontFamily(self):
    """
    Description:
    -----------
    Font family, default is defaultFontFamily.

    Related Pages:

      https://github.com/emn178/chartjs-plugin-labels
    """
    return self.get("'Helvetica Neue', 'Helvetica', 'Arial', sans-serif")

  @fontFamily.setter
  def fontFamily(self, value):
    self.set(value)

  @property
  def textShadow(self):
    """
    Description:
    -----------
    Draw text shadows under labels, default is false

    Related Pages:

      https://github.com/emn178/chartjs-plugin-labels
    """
    return self.get(True)

  @textShadow.setter
  def textShadow(self, flag):
    self.set(flag)

  @property
  def shadowBlur(self):
    """
    Description:
    -----------
    Text shadow intensity, default is 6

    Related Pages:

      https://github.com/emn178/chartjs-plugin-labels
    """
    return self.get(10)

  @shadowBlur.setter
  def shadowBlur(self, num):
    self.set(num)

  @property
  def shadowOffsetX(self):
    """
    Description:
    -----------
    Text shadow X offset, default is 3

    Related Pages:

      https://github.com/emn178/chartjs-plugin-labels
    """
    return self.get(-5)

  @shadowOffsetX.setter
  def shadowOffsetX(self, num):
    self.set(num)

  @property
  def shadowOffsetY(self):
    """
    Description:
    -----------
    Text shadow Y offset, default is 3

    Related Pages:

      https://github.com/emn178/chartjs-plugin-labels
    """
    return self.get(5)

  @shadowOffsetY.setter
  def shadowOffsetY(self, num):
    self.set(num)

  @property
  def shadowColor(self):
    """
    Description:
    -----------
    Text shadow color, default is 'rgba(0,0,0,0.3)'

    Related Pages:

      https://github.com/emn178/chartjs-plugin-labels
    """
    return self.get('rgba(255,0,0,0.75)')

  @shadowColor.setter
  def shadowColor(self, value):
    self.set(value)

  @property
  def arc(self):
    """
    Description:
    -----------
    Draw label in arc, default is false, bar chart ignores this

    Related Pages:

      https://github.com/emn178/chartjs-plugin-labels
    """
    return self.get(True)

  @arc.setter
  def arc(self, flag):
    self.set(flag)

  @property
  def position(self):
    """
    Description:
    -----------
    Position to draw label, available value is 'default', 'border' and 'outside'
    default is 'default'

    Related Pages:

      https://github.com/emn178/chartjs-plugin-labels
    """
    return self.get("default")

  @position.setter
  def position(self, value):
    self.set(value)

  @property
  def overlap(self):
    """
    Description:
    -----------
    Draw label even it's overlap, default is true

    Related Pages:

      https://github.com/emn178/chartjs-plugin-labels
    """
    return self.get(True)

  @overlap.setter
  def overlap(self, flag):
    self.set(flag)

  @property
  def outsidePadding(self):
    """
    Description:
    -----------
    add padding when position is `outside`

    Related Pages:

      https://github.com/emn178/chartjs-plugin-labels
    """
    return self.get(4)

  @outsidePadding.setter
  def outsidePadding(self, num):
    self.set(num)

  @property
  def images(self):
    """
    Description:
    -----------
    set images when `render` is 'image'
    """
    self.render.image()
    return self.sub_data("images", LabelsImages)

  @property
  def textMargin(self):
    """
    Description:
    -----------
    Add margin of text when position is `outside` or `border`

    Related Pages:

      https://github.com/emn178/chartjs-plugin-labels
    """
    return self.get(4)

  @textMargin.setter
  def textMargin(self, num):
    self.set(num)
