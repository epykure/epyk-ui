
from epyk.core.data import DataClass


class OptionConfig(DataClass):

  @property
  def responsive(self):
    """
    https://plot.ly/javascript/configuration-options/
    """
    return self._attrs["responsive"]

  @responsive.setter
  def responsive(self, val):
    self._attrs["responsive"] = val

  @property
  def editable(self):
    """
    https://plot.ly/javascript/configuration-options/
    """
    return self._attrs["editable"]

  @editable.setter
  def editable(self, val):
    self._attrs["editable"] = val

  @property
  def staticPlot(self):
    """
    https://plot.ly/javascript/configuration-options/
    """
    return self._attrs["staticPlot"]

  @staticPlot.setter
  def staticPlot(self, val):
    self._attrs["staticPlot"] = val

  @property
  def scrollZoom(self):
    """
    https://plot.ly/javascript/configuration-options/
    """
    return self._attrs["scrollZoom"]

  @scrollZoom.setter
  def scrollZoom(self, val):
    self._attrs["scrollZoom"] = val
