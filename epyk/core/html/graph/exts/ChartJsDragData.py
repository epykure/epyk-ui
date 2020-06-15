
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
  def showTooltip(self, bool):
    self.set(bool)


class DragData(DataClass):

  @property
  def dragX(self):
    """
    Description:
    -----------
    """
    return self.get(False)

  @dragX.setter
  def dragX(self, bool):
    self.set(bool)

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

  def onDragStart(self, jsFncs):
    """
    Description:
    -----------
    Called before zooming, return false to prevent the zoom

    Related Pages:

      https://github.com/chrispahm/chartjs-plugin-dragdata

    Attributes:
    ----------
    :param jsFncs:
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self._attrs["onDragStart"] = JsObjects.JsVoid("function(event, element) { %s }" % JsUtils.jsConvertFncs(jsFncs, toStr=True))

  def onDrag(self, jsFncs):
    """
    Description:
    -----------
    Change cursor style to grabbing during drag action

    Related Pages:

      https://github.com/chrispahm/chartjs-plugin-dragdata

    Attributes:
    ----------
    :param jsFncs:
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self._attrs["onDrag"] = JsObjects.JsVoid("function(event, datasetIndex, index, value) { %s }" % JsUtils.jsConvertFncs(jsFncs, toStr=True))

  def onDragEnd(self, jsFncs):
    """
    Description:
    -----------
    Restore default cursor style upon drag release

    Related Pages:

      https://github.com/chrispahm/chartjs-plugin-dragdata

    Attributes:
    ----------
    :param jsFncs:
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self._attrs["onDragEnd"] = JsObjects.JsVoid("function(event, datasetIndex, index, value) { %s }" % JsUtils.jsConvertFncs(jsFncs, toStr=True))
