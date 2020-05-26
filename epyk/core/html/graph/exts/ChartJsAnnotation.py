
from epyk.core.data import DataClass

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects


class Annotations(DataClass):

  @property
  def drawTime(self):
    """
    Description:
    -----------
    Overrides annotation.drawTime if set

    Related Pages:

      https://github.com/chartjs/chartjs-plugin-annotation
    """
    return self.get('afterDraw')

  @drawTime.setter
  def drawTime(self, value):
    self.set(value)

  @property
  def type(self):
    """
    Description:
    -----------

    Related Pages:

      https://github.com/chartjs/chartjs-plugin-annotation
    """
    return self.get('line')

  @type.setter
  def type(self, value):
    self.set(value)

  @property
  def mode(self):
    """
    Description:
    -----------

    Related Pages:

      https://github.com/chartjs/chartjs-plugin-annotation
    """
    return self.get('horizontal')

  @mode.setter
  def mode(self, value):
    self.set(value)

  @property
  def scaleID(self):
    """
    Description:
    -----------

    Related Pages:

      https://github.com/chartjs/chartjs-plugin-annotation
    """
    return self.get('y-axis-0')

  @scaleID.setter
  def scaleID(self, value):
    self.set(value)

  @property
  def value(self):
    """
    Description:
    -----------

    Related Pages:

      https://github.com/chartjs/chartjs-plugin-annotation
    """
    return self.get('25')

  @value.setter
  def value(self, value):
    self.set(value)

  @property
  def borderColor(self):
    """
    Description:
    -----------

    Related Pages:

      https://github.com/chartjs/chartjs-plugin-annotation
    """
    return self.get('red')

  @borderColor.setter
  def borderColor(self, color):
    self.set(color)

  @property
  def borderWidth(self):
    """
    Description:
    -----------

    Related Pages:

      https://github.com/chartjs/chartjs-plugin-annotation
    """
    return self.get(2)

  @borderWidth.setter
  def borderWidth(self, num):
    self.set(num)

  def onClick(self, jsFncs):
    """
    Description:
    -----------
    Fires when the user clicks this annotation on the chart
    (be sure to enable the event in the events array below).
    
    Related Pages:

      https://github.com/chartjs/chartjs-plugin-annotation

    Attributes:
    ----------
    :param jsFncs:
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self._attrs["onClick"] = JsObjects.JsVoid(
      "function(event) { %s }" % JsUtils.jsConvertFncs(jsFncs, toStr=True))


class Annotation(DataClass):

  @property
  def drawTime(self):
    """
    Description:
    -----------

    Related Pages:

      https://github.com/chartjs/chartjs-plugin-annotation
    """
    return self.get('afterDatasetsDraw')

  @drawTime.setter
  def drawTime(self, value):
    self.set(value)

  @property
  def events(self):
    """
    Description:
    -----------

    Related Pages:

      https://github.com/chartjs/chartjs-plugin-annotation
    """
    return self.get(['click'])

  @events.setter
  def events(self, value):
    self.set(value)

  @property
  def dblClickSpeed(self):
    """
    Description:
    -----------

    Related Pages:

      https://github.com/chartjs/chartjs-plugin-annotation
    """
    return self.get(350)

  @dblClickSpeed.setter
  def dblClickSpeed(self, value):
    self.set(value)

  @property
  def annotations(self):
    """
    Description:
    -----------
    The plugin allows for horizontal zooming by clicking and dragging over the chart.

    Related Pages:

      https://chartjs-plugin-crosshair.netlify.app/options.html
    """
    return self.sub_data("annotations", Annotations)
