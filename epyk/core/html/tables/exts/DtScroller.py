
from epyk.core.html.options import Options


class Scroller(Options):

  def activate(self):
    """   Enable and configure the Scroller extension for DataTables

    Related Pages:

      https://datatables.net/reference/option/scroller
    """
    self.loadingIndicator = True
    return self

  @property
  def boundaryScale(self):
    """   Set the point at which new data will be loaded and drawn.

    Related Pages:

      https://datatables.net/reference/option/scroller.boundaryScale
    """
    return self._config_get()

  @boundaryScale.setter
  def boundaryScale(self, val):
    self._config(val)

  @property
  def displayBuffer(self):
    """   The amount of data that Scroller should pre-buffer to ensure smooth scrolling.

    Related Pages:

      https://datatables.net/reference/option/scroller.displayBuffer
    """
    return self._config_get()

  @displayBuffer.setter
  def displayBuffer(self, val):
    self._config(val)

  @property
  def loadingIndicator(self):
    """   Display a loading message while Scroller is loading additional data.

    Related Pages:

      https://datatables.net/reference/option/scroller.loadingIndicator
    """
    return self._config_get()

  @loadingIndicator.setter
  def loadingIndicator(self, val):
    self._config(val)

  @property
  def rowHeight(self):
    """   Set the row height, or how the row height is calculated.

    Related Pages:

      https://datatables.net/reference/option/scroller.rowHeight
    """
    return self._config_get()

  @rowHeight.setter
  def rowHeight(self, val):
    self._config(val)

  @property
  def serverWait(self):
    """   Time delay before new data is requested when server-side processing is enabled.

    Related Pages:

      https://datatables.net/reference/option/scroller.serverWait
    """
    return self._config_get()

  @serverWait.setter
  def serverWait(self, val):
    self._config(val)
