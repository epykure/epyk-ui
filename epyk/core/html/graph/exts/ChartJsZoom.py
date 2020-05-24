
from epyk.core.data import DataClass

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects


class ZoomRange(DataClass):

  @property
  def x(self):
    """
    https://github.com/chartjs/chartjs-plugin-zoom
    """
    return self._attrs["x"]

  @x.setter
  def x(self, num):
    self._attrs["x"] = num

  @property
  def y(self):
    """
    https://github.com/chartjs/chartjs-plugin-zoom
    """
    return self._attrs["y"]

  @y.setter
  def y(self, num):
    self._attrs["y"] = num


class ZoomAttrs(DataClass):

  @property
  def enabled(self):
    """
    https://github.com/chartjs/chartjs-plugin-zoom
    """
    return self._attrs["enabled"]

  @enabled.setter
  def enabled(self, bool):
    self._attrs["enabled"] = bool

  @property
  def mode(self):
    """
    https://github.com/chartjs/chartjs-plugin-zoom
    """
    return self._attrs["mode"]

  @mode.setter
  def mode(self, value):
    self._attrs["mode"] = value

  @property
  def rangeMin(self):
    return self.sub_data("rangeMin", ZoomRange)

  @property
  def rangeMax(self):
    return self.sub_data("rangeMax", ZoomRange)

  @property
  def speed(self):
    """
    https://github.com/chartjs/chartjs-plugin-zoom
    """
    return self._attrs["speed"]

  @speed.setter
  def speed(self, num):
    self._attrs["speed"] = num

  @property
  def threshold(self):
    """
    https://github.com/chartjs/chartjs-plugin-zoom
    """
    return self._attrs["threshold"]

  @threshold.setter
  def threshold(self, num):
    self._attrs["threshold"] = num


class ZoomPan(ZoomAttrs):

  def onPan(self, jsFncs):
    """
    Function called while the user is zooming

    :param jsFnc:
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self._attrs["onPan"] = JsObjects.JsVoid("function(data) { %s }" % JsUtils.jsConvertFncs(jsFncs, toStr=True))

  def onPanComplete(self, jsFncs):
    """
    Function called while the user is zooming

    :param jsFnc:
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self._attrs["onPanComplete"] = JsObjects.JsVoid("function(data) { %s }" % JsUtils.jsConvertFncs(jsFncs, toStr=True))


class ZoomZoom(ZoomAttrs):

  @property
  def drag(self):
    """
    Enable drag-to-zoom behavior
    """
    return self._attrs["drag"]

  @drag.setter
  def drag(self, bool):
    self._attrs["drag"] = bool

  @property
  def sensitivity(self):
    """
    https://github.com/chartjs/chartjs-plugin-zoom
    """
    return self._attrs["sensitivity"]

  @sensitivity.setter
  def sensitivity(self, num):
    self._attrs["sensitivity"] = num

  def onZoom(self, jsFncs):
    """
    Function called while the user is zooming

    :param jsFnc:
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self._attrs["onZoom"] = JsObjects.JsVoid("function(data) { %s }" % JsUtils.jsConvertFncs(jsFncs, toStr=True))

  def onZoomComplete(self, jsFncs):
    """
    Function called once zooming is completed

    :param jsFnc:
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self._attrs["onZoomComplete"] = JsObjects.JsVoid("function(data) { %s }" % JsUtils.jsConvertFncs(jsFncs, toStr=True))


class Zoom(DataClass):

  @property
  def pan(self):
    return self.sub_data("pan", ZoomPan)

  @property
  def zoom(self):
    return self.sub_data("zoom", ZoomZoom)

