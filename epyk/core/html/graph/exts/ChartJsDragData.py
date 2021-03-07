
from epyk.core.data.DataClass import DataClass

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects


class DragOptions(DataClass):

  @property
  def showTooltip(self):
    """
    Description:
    -----------

    Related Pages:

      https://github.com/chrispahm/chartjs-plugin-dragdata
    """
    return self.get(True)

  @showTooltip.setter
  def showTooltip(self, flag):
    self.set(flag)


class DragData(DataClass):

  @property
  def dragX(self):
    """
    Description:
    -----------
    """
    return self.get(False)

  @dragX.setter
  def dragX(self, flag):
    self.set(flag)

  @property
  def dragDataRound(self):
    """
    Description:
    -----------
    """
    return self.get(0)

  @dragDataRound.setter
  def dragDataRound(self, num):
    self.set(num)

  @property
  def dragOptions(self):
    """
    Description:
    -----------
    """
    return self.sub_data("dragOptions", DragOptions)

  def onDragStart(self, js_funcs, profile=None):
    """
    Description:
    -----------
    Called before zooming, return false to prevent the zoom

    Related Pages:

      https://github.com/chrispahm/chartjs-plugin-dragdata

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._attrs["onDragStart"] = JsObjects.JsVoid("function(event, element) { %s }" % JsUtils.jsConvertFncs(
      js_funcs, toStr=True, profile=profile))

  def onDrag(self, js_funcs, profile=None):
    """
    Description:
    -----------
    Change cursor style to grabbing during drag action

    Related Pages:

      https://github.com/chrispahm/chartjs-plugin-dragdata

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._attrs["onDrag"] = JsObjects.JsVoid("function(event, datasetIndex, index, value) {%s}" % JsUtils.jsConvertFncs(
      js_funcs, toStr=True, profile=profile))

  def onDragEnd(self, js_funcs, profile=None):
    """
    Description:
    -----------
    Restore default cursor style upon drag release

    Related Pages:

      https://github.com/chrispahm/chartjs-plugin-dragdata

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._attrs["onDragEnd"] = JsObjects.JsVoid(
      "function(event, datasetIndex, index, value) {%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile))
