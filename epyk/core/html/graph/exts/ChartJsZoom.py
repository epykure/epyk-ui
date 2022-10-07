
from epyk.core.html.options import Options
from epyk.core.js import JsUtils


class ZoomRange(Options):

  @property
  def x(self):
    """   

    Related Pages:

      https://github.com/chartjs/chartjs-plugin-zoom
    """
    return self._config_get(None)

  @x.setter
  def x(self, num):
    self._config(num)

  @property
  def y(self):
    """   

    Related Pages:

      https://github.com/chartjs/chartjs-plugin-zoom
    """
    return self._config_get(None)

  @y.setter
  def y(self, num):
    self._config(num)


class ZoomAttrs(Options):

  @property
  def enabled(self):
    """   

    Related Pages:

      https://github.com/chartjs/chartjs-plugin-zoom
    """
    return self._config_get()

  @enabled.setter
  def enabled(self, flag):
    self._config(flag)

  @property
  def mode(self):
    """   

    Related Pages:

      https://github.com/chartjs/chartjs-plugin-zoom
    """
    return self._config_get()

  @mode.setter
  def mode(self, value):
    self._config(value)

  @property
  def rangeMin(self):
    """   

    :rtype: ZoomRange
    """
    return self._config_sub_data("rangeMin", ZoomRange)

  @property
  def rangeMax(self):
    """   

    :rtype: ZoomRange
    """
    return self._config_sub_data("rangeMax", ZoomRange)

  @property
  def speed(self):
    """   

    Related Pages:

      https://github.com/chartjs/chartjs-plugin-zoom
    """
    return self._config_get()

  @speed.setter
  def speed(self, num):
    self._config(num)

  @property
  def threshold(self):
    """   

    Related Pages:

      https://github.com/chartjs/chartjs-plugin-zoom
    """
    return self._config_get()

  @threshold.setter
  def threshold(self, num):
    self._config(num)


class ZoomPan(ZoomAttrs):

  def onPan(self, js_funcs, profile=None):
    """   Function called while the user is zooming.

    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._config("function(data){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile), js_type=True)

  def onPanComplete(self, js_funcs, profile=None):
    """   Function called while the user is zooming.

    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._config("function(data){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile), js_type=True)


class ZoomZoom(ZoomAttrs):

  @property
  def drag(self):
    """   Enable drag-to-zoom behavior.
    """
    return self._config_get()

  @drag.setter
  def drag(self, flag):
    self._config(flag)

  @property
  def sensitivity(self):
    """   

    Related Pages:

      https://github.com/chartjs/chartjs-plugin-zoom
    """
    return self._config_get()

  @sensitivity.setter
  def sensitivity(self, num):
    self._config(num)

  def onZoom(self, js_funcs, profile=None):
    """   Function called while the user is zooming.

    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._config("function(data){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile), js_type=True)

  def onZoomComplete(self, js_funcs, profile=None):
    """   Function called once zooming is completed.

    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._config("function(data){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile), js_type=True)


class Zoom(Options):

  def set_default(self, mode="xy"):
    """
    Set zoom default attributes.

    Related Pages:

      https://github.com/chartjs/chartjs-plugin-zoom

    :param mode: String. Optional. Zooming directions.
    """
    self.pan.mode = mode
    self.pan.enabled = True
    self.zoom.enabled = True
    self.zoom.mode = mode

  @property
  def pan(self):
    """   

    :rtype: ZoomPan
    """
    return self._config_sub_data("pan", ZoomPan)

  @property
  def zoom(self):
    """   

    :rtype: ZoomZoom
    """
    return self._config_sub_data("zoom", ZoomZoom)

