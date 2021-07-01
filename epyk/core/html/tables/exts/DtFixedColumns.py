
from epyk.core.html.options import Options


class FixedColumns(Options):

  def activate(self):
    """
    Description:
    -----------

    Related Pages:

      https://datatables.net/reference/option/fixedColumns
    """
    self.leftColumns = 2
    return self

  @property
  def heightMatch(self):
    """
    Description:
    -----------
    FixedColumns operates by cloning the cells from the original table and then inserting them into the document, positioned visually above the DataTable - thus allowing them to appear fixed.

    Related Pages:

      https://datatables.net/reference/option/fixedColumns.heightMatch
    """
    return self._config_get()

  @heightMatch.setter
  def heightMatch(self, val):
    self._config(val)

  @property
  def leftColumns(self):
    return self._config_get()


  @leftColumns.setter
  def leftColumns(self, val):
    self._config(val)

  @property
  def rightColumns(self):
    return self._config_get()

  @rightColumns.setter
  def rightColumns(self, val):
    self._config(val)
