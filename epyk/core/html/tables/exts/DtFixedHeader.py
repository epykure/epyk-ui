
from epyk.core.data.DataClass import DataClass


class FixedHeater(DataClass):

  def activate(self):
    """

    :return:
    """
    self.header = True
    return self

  @property
  def header(self):
    return self._attrs["header"]

  @header.setter
  def header(self, val):
    self._attrs["header"] = val

  @property
  def headerOffset(self):
    return self._attrs["header"]

  @headerOffset.setter
  def headerOffset(self, val):
    self._attrs["headerOffset"] = val

  @property
  def footer(self):
    return self._attrs["footer"]

  @footer.setter
  def footer(self, val):
    self._attrs["footer"] = val

  @property
  def footerOffset(self):
    return self._attrs["footerOffset"]

  @footerOffset.setter
  def footerOffset(self, val):
    self._attrs["footerOffset"] = val
