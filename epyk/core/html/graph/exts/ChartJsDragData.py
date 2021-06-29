
from epyk.core.html.options import Options
from epyk.core.js import JsUtils


class DragOptions(Options):

  @property
  def showTooltip(self):
    """
    Description:
    -----------

    Related Pages:

      https://github.com/chrispahm/chartjs-plugin-dragdata
    """
    return self._config_get(True)

  @showTooltip.setter
  def showTooltip(self, flag):
    self._config(flag)


class DragData(Options):

  @property
  def dragX(self):
    """
    Description:
    -----------
    """
    return self._config_get(False)

  @dragX.setter
  def dragX(self, flag):
    self._config(flag)

  @property
  def dragDataRound(self):
    """
    Description:
    -----------
    """
    return self._config_get(0)

  @dragDataRound.setter
  def dragDataRound(self, num):
    self._config(num)

  @property
  def dragOptions(self):
    """
    Description:
    -----------

    :rtype: DragOptions
    """
    return self._config_sub_data("dragOptions", DragOptions)

  def onDragStart(self, js_funcs, profile=None):
    """
    Description:
    -----------
    Called before zooming, return false to prevent the zoom.

    Related Pages:

      https://github.com/chrispahm/chartjs-plugin-dragdata

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._config(
      "function(event, element){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile), js_type=True)

  def onDrag(self, js_funcs, profile=None):
    """
    Description:
    -----------
    Change cursor style to grabbing during drag action.

    Related Pages:

      https://github.com/chrispahm/chartjs-plugin-dragdata

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._config(
      "function(event, datasetIndex, index, value){%s}" % JsUtils.jsConvertFncs(
        js_funcs, toStr=True, profile=profile), js_type=True)

  def onDragEnd(self, js_funcs, profile=None):
    """
    Description:
    -----------
    Restore default cursor style upon drag release.

    Related Pages:

      https://github.com/chrispahm/chartjs-plugin-dragdata

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._config(
      "function(event, datasetIndex, index, value){%s}" % JsUtils.jsConvertFncs(
        js_funcs, toStr=True, profile=profile), js_type=True)
