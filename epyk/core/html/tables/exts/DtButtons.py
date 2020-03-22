
from epyk.core.data import DataClass


class Buttons(DataClass):

  @property
  def enable(self):
    """
    Description:
    -----------
    It can be useful to disable ColReorder's user input controls at certain times, depending on the state of your application. This option provides that ability when the table is initially created, while the colReorder.enable() and colReorder.disable() methods provide the option to enabling the user interaction after the table has been created.

    Related Pages:
    --------------
    https://datatables.net/reference/option/colReorder.enable
    """
    return self._attrs["enable"]

  @enable.setter
  def enable(self, val):
    self._attrs["enable"] = val
