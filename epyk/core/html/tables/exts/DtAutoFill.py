
from epyk.core.data import DataClass


class AutoFill(DataClass):

  def activate(self):
    self.columns = ":not(:first-child)"
    return self

  @property
  def alwaysAsk(self):
    """
    Description:
    -----------
    Always ask the end user if an action should be taken or not.

    Related Pages:


    https://datatables.net/reference/option/autoFill.alwaysAsk
    """
    return self._attrs["alwaysAsk"]

  @alwaysAsk.setter
  def alwaysAsk(self, val):
    self._attrs["alwaysAsk"] = val

  @property
  def columns(self):
    """
    Description:
    -----------
    Select the columns that can be auto filled.

    Related Pages:


    https://datatables.net/reference/option/autoFill.columns
    """
    return self._attrs["alwaysAsk"]

  @columns.setter
  def columns(self, val):
    self._attrs["columns"] = val

  @property
  def enable(self):
    """
    Description:
    -----------
    Initial enablement state of AutoFill.

    Related Pages:


    https://datatables.net/reference/option/autoFill.enable
    """
    return self._attrs["enable"]

  @enable.setter
  def enable(self, val):
    self._attrs["enable"] = val

  @property
  def focus(self):
    """
    Description:
    -----------
    Action that will cause the auto fill drag handle to appear in a cell.

    Related Pages:


    https://datatables.net/reference/option/autoFill.focus
    """
    return self._attrs["focus"]

  @focus.setter
  def focus(self, val):
    self._attrs["focus"] = val

  @property
  def horizontal(self):
    """
    Description:
    -----------
    Enable / disable user ability to horizontally drag and fill.

    Related Pages:


    https://datatables.net/reference/option/autoFill.horizontal
    """
    return self._attrs["horizontal"]

  @horizontal.setter
  def horizontal(self, val):
    self._attrs["horizontal"] = val

  @property
  def update(self):
    """
    Description:
    -----------
    Control automatic update of data when a fill drag is completed.

    Related Pages:


    https://datatables.net/reference/option/autoFill.update
    """
    return self._attrs["update"]

  @update.setter
  def update(self, val):
    self._attrs["update"] = val

  @property
  def vertical(self):
    """
    Description:
    -----------
    Enable / disable user ability to vertically drag and fill.

    Related Pages:


    https://datatables.net/reference/option/autoFill.vertical
    """
    return self._attrs["vertical"]

  @vertical.setter
  def vertical(self, val):
    self._attrs["vertical"] = val
