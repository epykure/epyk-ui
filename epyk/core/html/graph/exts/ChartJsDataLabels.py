
from epyk.core.data.DataClass import DataClass, DataEnum

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects


class EnumLayout(DataEnum):
  js_conversion = True

  def fitDataStretch(self):
    """
    Description:
    -----------
    The fitDataStretch layout mode functions in the same way as the fitDataFill mode, but instead of stretching the empty row to fill the table it stretches the last visible column.

    Related Pages:
http://tabulator.info/docs/4.5/layout
    """
    return self.set()


class Datalabels(DataClass):

  @property
  def color(self):
    """
    Description:
    -----------

    Related Pages:

      https://www.npmjs.com/package/chartjs-plugin-crosshair
    """
    return self.get('#F66')

  @color.setter
  def color(self, color):
    self.set(color)

  @property
  def formatter(self):
    """
    Description:
    -----------

    Related Pages:

      https://www.npmjs.com/package/chartjs-plugin-crosshair
    """
    return self.get(None)

  @formatter.setter
  def formatter(self, value):
    self.set(value)
