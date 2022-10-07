
from epyk.core.html.options import Options


class RowGroup(Options):

  def activate(self):
    self.dataSrc = 'group'
    return self

  @property
  def className(self):
    """   Set the class name to be used for the grouping rows.

    Related Pages:

      https://datatables.net/reference/option/rowGroup.className
    """
    return self._config_get()

  @className.setter
  def className(self, val):
    self._config(val)

  @property
  def dataSrc(self):
    """   Set the data point to use as the grouping data source

    Related Pages:

      https://datatables.net/reference/option/rowGroup.className
    """
    return self._config_get()

  @dataSrc.setter
  def dataSrc(self, val):
    self._config(val)

  @property
  def emptyDataGroup(self):
    """   Text to show for rows which have null, undefined or empty string group data.

    Related Pages:

      https://datatables.net/reference/option/rowGroup.emptyDataGroup
    """
    return self._config_get()

  @emptyDataGroup.setter
  def emptyDataGroup(self, val):
    self._config(val)

  @property
  def enable(self):
    """   Provides the ability to disable row grouping at initialisation.

    Related Pages:

      https://datatables.net/reference/option/rowGroup.enable
    """
    return self._config_get()

  @enable.setter
  def enable(self, val):
    self._config(val)

  @property
  def endClassName(self):
    """   Set the class name to be used for the grouping end rows.

    Related Pages:

      https://datatables.net/reference/option/rowGroup.endClassName
    """
    return self._config_get()

  @endClassName.setter
  def endClassName(self, val):
    self._config(val)

  @property
  def startClassName(self):
    """   Set the class name to be used for the grouping start rows.

    Related Pages:

      https://datatables.net/reference/option/rowGroup.startClassName
    """
    return self._config_get()

  @startClassName.setter
  def startClassName(self, val):
    self._config(val)
