

from epyk.core.data import DataClass


class Scroller(DataClass):

  def activate(self):
    """
    Description:
    -----------
    Enable and configure the Scroller extension for DataTables

    Related Pages:


    https://datatables.net/reference/option/scroller
    """
    self.loadingIndicator = True
    return self

  @property
  def boundaryScale(self):
    """
    Description:
    -----------
    Set the point at which new data will be loaded and drawn.

    Related Pages:


    https://datatables.net/reference/option/scroller.boundaryScale
    """
    return self._attrs["boundaryScale"]

  @boundaryScale.setter
  def boundaryScale(self, val):
    self._attrs["boundaryScale"] = val

  @property
  def displayBuffer(self):
    """
    Description:
    -----------
    The amount of data that Scroller should pre-buffer to ensure smooth scrolling.

    Related Pages:


    https://datatables.net/reference/option/scroller.displayBuffer
    """
    return self._attrs["displayBuffer"]

  @displayBuffer.setter
  def displayBuffer(self, val):
    self._attrs["displayBuffer"] = val

  @property
  def loadingIndicator(self):
    """
    Description:
    -----------
    Display a loading message while Scroller is loading additional data.

    Related Pages:


    https://datatables.net/reference/option/scroller.loadingIndicator
    """
    return self._attrs["loadingIndicator"]

  @loadingIndicator.setter
  def loadingIndicator(self, val):
    self._attrs["loadingIndicator"] = val

  @property
  def rowHeight(self):
    """
    Description:
    -----------
    Set the row height, or how the row height is calculated.

    Related Pages:


    https://datatables.net/reference/option/scroller.rowHeight
    """
    return self._attrs["rowHeight"]

  @rowHeight.setter
  def rowHeight(self, val):
    self._attrs["rowHeight"] = val

  @property
  def serverWait(self):
    """
    Description:
    -----------
    Time delay before new data is requested when server-side processing is enabled.

    Related Pages:


    https://datatables.net/reference/option/scroller.serverWait
    """
    return self._attrs["serverWait"]

  @serverWait.setter
  def serverWait(self, val):
    self._attrs["serverWait"] = val
