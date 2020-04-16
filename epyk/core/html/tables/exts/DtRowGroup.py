
from epyk.core.data import DataClass


class RowGroup(DataClass):

  def activate(self):
    self.dataSrc = 'group'
    return self

  @property
  def className(self):
    """
    Description:
    -----------
    Set the class name to be used for the grouping rows.

    Related Pages:

			https://datatables.net/reference/option/rowGroup.className
    """
    return self._attrs["className"]

  @className.setter
  def className(self, val):
    self._attrs["className"] = val

  @property
  def dataSrc(self):
    """
    Description:
    -----------
    Set the data point to use as the grouping data source

    Related Pages:

			https://datatables.net/reference/option/rowGroup.className
    """
    return self._attrs["dataSrc"]

  @dataSrc.setter
  def dataSrc(self, val):
    self._attrs["dataSrc"] = val

  @property
  def emptyDataGroup(self):
    """
    Description:
    -----------
    Text to show for rows which have null, undefined or empty string group data.

    Related Pages:

			https://datatables.net/reference/option/rowGroup.emptyDataGroup
    """
    return self._attrs["emptyDataGroup"]

  @emptyDataGroup.setter
  def emptyDataGroup(self, val):
    self._attrs["emptyDataGroup"] = val

  @property
  def enable(self):
    """
    Description:
    -----------
    Provides the ability to disable row grouping at initialisation.

    Related Pages:

			https://datatables.net/reference/option/rowGroup.enable
    """
    return self._attrs["enable"]

  @enable.setter
  def enable(self, val):
    self._attrs["enable"] = val

  @property
  def endClassName(self):
    """
    Description:
    -----------
    Set the class name to be used for the grouping end rows.

    Related Pages:

			https://datatables.net/reference/option/rowGroup.endClassName
    """
    return self._attrs["endClassName"]

  @endClassName.setter
  def endClassName(self, val):
    self._attrs["endClassName"] = val

  @property
  def startClassName(self):
    """
    Description:
    -----------
    Set the class name to be used for the grouping start rows.

    Related Pages:

			https://datatables.net/reference/option/rowGroup.startClassName
    """
    return self._attrs["startClassName"]

  @startClassName.setter
  def startClassName(self, val):
    self._attrs["startClassName"] = val
