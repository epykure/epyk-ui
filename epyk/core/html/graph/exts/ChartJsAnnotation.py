
from epyk.core.html.options import Options
from epyk.core.js import JsUtils


class Annotations(Options):

  @property
  def drawTime(self):
    """
    Description:
    -----------
    Overrides annotation.drawTime if set.

    Related Pages:

      https://github.com/chartjs/chartjs-plugin-annotation
    """
    return self._config_get('afterDraw')

  @drawTime.setter
  def drawTime(self, value):
    self._config(value)

  @property
  def type(self):
    """
    Description:
    -----------

    Related Pages:

      https://github.com/chartjs/chartjs-plugin-annotation
    """
    return self._config_get('line')

  @type.setter
  def type(self, value):
    self._config(value)

  @property
  def mode(self):
    """
    Description:
    -----------

    Related Pages:

      https://github.com/chartjs/chartjs-plugin-annotation
    """
    return self._config_get('horizontal')

  @mode.setter
  def mode(self, value):
    self._config(value)

  @property
  def scaleID(self):
    """
    Description:
    -----------

    Related Pages:

      https://github.com/chartjs/chartjs-plugin-annotation
    """
    return self._config_get('y-axis-0')

  @scaleID.setter
  def scaleID(self, value):
    self._config(value)

  @property
  def value(self):
    """
    Description:
    -----------

    Related Pages:

      https://github.com/chartjs/chartjs-plugin-annotation
    """
    return self._config_get('25')

  @value.setter
  def value(self, v):
    self._config(v)

  @property
  def borderColor(self):
    """
    Description:
    -----------

    Related Pages:

      https://github.com/chartjs/chartjs-plugin-annotation
    """
    return self._config_get('red')

  @borderColor.setter
  def borderColor(self, color):
    self._config(color)

  @property
  def borderWidth(self):
    """
    Description:
    -----------

    Related Pages:

      https://github.com/chartjs/chartjs-plugin-annotation
    """
    return self._config_get(2)

  @borderWidth.setter
  def borderWidth(self, num):
    self._config(num)

  def onClick(self, js_funcs, profile=None):
    """
    Description:
    -----------
    Fires when the user clicks this annotation on the chart (be sure to enable the event in the events array below).
    
    Related Pages:

      https://github.com/chartjs/chartjs-plugin-annotation

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._config("function(event){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile), js_type=True)


class Annotation(Options):

  @property
  def drawTime(self):
    """
    Description:
    -----------

    Related Pages:

      https://github.com/chartjs/chartjs-plugin-annotation
    """
    return self._config_get('afterDatasetsDraw')

  @drawTime.setter
  def drawTime(self, value):
    self._config(value)

  @property
  def events(self):
    """
    Description:
    -----------

    Related Pages:

      https://github.com/chartjs/chartjs-plugin-annotation
    """
    return self._config_get(['click'])

  @events.setter
  def events(self, value):
    self._config(value)

  @property
  def dblClickSpeed(self):
    """
    Description:
    -----------

    Related Pages:

      https://github.com/chartjs/chartjs-plugin-annotation
    """
    return self._config_get(350)

  @dblClickSpeed.setter
  def dblClickSpeed(self, value):
    self._config(value)

  @property
  def annotations(self):
    """
    Description:
    -----------
    The plugin allows for horizontal zooming by clicking and dragging over the chart.

    Related Pages:

      https://chartjs-plugin-crosshair.netlify.app/options.html

    :rtype: Annotations
    """
    return self._config_sub_data("annotations", Annotations)
