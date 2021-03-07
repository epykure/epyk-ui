
from epyk.core.data.DataClass import DataClass

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects


class Line(DataClass):

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
  def width(self):
    """
    Description:
    -----------

    Related Pages:

      https://www.npmjs.com/package/chartjs-plugin-crosshair
    """
    return self.get(1)

  @width.setter
  def width(self, num):
    self.set(num)


class Sync(DataClass):

  @property
  def enabled(self):
    """
    Description:
    -----------
    Enable or disable syncing of crosshairs between charts of the same group

    Related Pages:

      https://chartjs-plugin-crosshair.netlify.app/options.html
    """
    return self.get(True)

  @enabled.setter
  def enabled(self, flag):
    self.set(flag)

  @property
  def group(self):
    """
    Description:
    -----------
    Limit crosshair syncing to charts belonging to the same 'group'

    Related Pages:

      https://www.npmjs.com/package/chartjs-plugin-crosshair
    """
    return self.get(1)

  @group.setter
  def group(self, num):
    self.set(num)

  @property
  def suppressTooltips(self):
    """
    Description:
    -----------
    Allows for suppressing tooltips when showing a synced crosshair

    Related Pages:

      https://www.npmjs.com/package/chartjs-plugin-crosshair
    """
    return self.get(True)

  @suppressTooltips.setter
  def suppressTooltips(self, flag):
    self.set(flag)


class Zoom(DataClass):

  @property
  def enabled(self):
    """
    Description:
    -----------
    Enable or disable zooming by drag and drop

    Related Pages:

      https://www.npmjs.com/package/chartjs-plugin-crosshair
    """
    return self.get(True)

  @enabled.setter
  def enabled(self, flag):
    self.set(flag)

  @property
  def zoomboxBackgroundColor(self):
    """
    Description:
    -----------
    Background color of the zoombox

    Related Pages:

      https://www.npmjs.com/package/chartjs-plugin-crosshair
    """
    return self.get('rgba(66,133,244,0.2)')

  @zoomboxBackgroundColor.setter
  def zoomboxBackgroundColor(self, color):
    self.set(color)

  @property
  def zoomboxBorderColor(self):
    """
    Description:
    -----------
    Border color of the zoombox

    Related Pages:

      https://www.npmjs.com/package/chartjs-plugin-crosshair
    """
    return self.get('#48F')

  @zoomboxBorderColor.setter
  def zoomboxBorderColor(self, color):
    self.set(color)

  @property
  def zoomButtonText(self):
    """
    Description:
    -----------
    Text of the button to reset the chart to original axis ranges.

    Related Pages:

      https://www.npmjs.com/package/chartjs-plugin-crosshair
    """
    return self.get('Reset Zoom')

  @zoomButtonText.setter
  def zoomButtonText(self, text):
    self.set(text)

  @property
  def zoomButtonClass(self):
    """
    Description:
    -----------
    Class of the button to reset the chart to original axis ranges.

    Related Pages:

      https://www.npmjs.com/package/chartjs-plugin-crosshair
    """
    return self.get('reset-zoom')

  @zoomButtonClass.setter
  def zoomButtonClass(self, text):
    self.set(text)


class Crosshair(DataClass):

  @property
  def line(self):
    """
    Description:
    -----------

    Related Pages:

      https://chartjs-plugin-crosshair.netlify.app/options.html
    """
    return self.sub_data("line", Line)

  @property
  def sync(self):
    """
    Description:
    -----------
    The plugin allows for syncing crosshairs over multiple charts

    Related Pages:

      https://chartjs-plugin-crosshair.netlify.app/options.html
    """
    return self.sub_data("sync", Sync)

  @property
  def zoom(self):
    """
    Description:
    -----------
    The plugin allows for horizontal zooming by clicking and dragging over the chart.

    Related Pages:

      https://chartjs-plugin-crosshair.netlify.app/options.html
    """
    return self.sub_data("zoom", Zoom)

  @property
  def snapToDataPoint(self):
    """
    Description:
    -----------
    The plugin allows snapping to datapoints when used with line charts

    Related Pages:

      https://canvasjs.com/docs/charts/chart-options/axisx/crosshair/snap-to-datapoint/
    """
    return self.get(True)

  @snapToDataPoint.setter
  def snapToDataPoint(self, flag):
    self.set(flag)

  def beforeZoom(self, js_funcs, profile=None):
    """
    Description:
    -----------
    Called before zooming, return false to prevent the zoom

    Related Pages:

      https://chartjs-plugin-crosshair.netlify.app/options.html

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._attrs["beforeZoom"] = JsObjects.JsVoid("function(start, end) {%s}" % JsUtils.jsConvertFncs(
      js_funcs, toStr=True, profile=profile))

  def afterZoom(self, js_funcs, profile=None):
    """
    Description:
    -----------
    Called after zooming, can for example be used for reloading data at a higher resolution

    Related Pages:

      https://chartjs-plugin-crosshair.netlify.app/options.html

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._attrs["afterZoom"] = JsObjects.JsVoid("function(start, end) { %s }" % JsUtils.jsConvertFncs(
      js_funcs, toStr=True, profile=profile))

