
from epyk.core.html.options import Options


class AutoFill(Options):

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
    return self._config_get()

  @alwaysAsk.setter
  def alwaysAsk(self, val):
    self._config(val)

  @property
  def columns(self):
    """
    Description:
    -----------
    Select the columns that can be auto filled.

    Related Pages:

      https://datatables.net/reference/option/autoFill.columns
    """
    return self._config_get()

  @columns.setter
  def columns(self, val):
    self._config(val)

  @property
  def enable(self):
    """
    Description:
    -----------
    Initial enablement state of AutoFill.

    Related Pages:

      https://datatables.net/reference/option/autoFill.enable
    """
    return self._config_get()

  @enable.setter
  def enable(self, val):
    self._config(val)

  @property
  def focus(self):
    """
    Description:
    -----------
    Action that will cause the auto fill drag handle to appear in a cell.

    Related Pages:

      https://datatables.net/reference/option/autoFill.focus
    """
    return self._config_get()

  @focus.setter
  def focus(self, val):
    self._config(val)

  @property
  def horizontal(self):
    """
    Description:
    -----------
    Enable / disable user ability to horizontally drag and fill.

    Related Pages:

      https://datatables.net/reference/option/autoFill.horizontal
    """
    return self._config_get()

  @horizontal.setter
  def horizontal(self, val):
    self._config(val)

  @property
  def update(self):
    """
    Description:
    -----------
    Control automatic update of data when a fill drag is completed.

    Related Pages:

      https://datatables.net/reference/option/autoFill.update
    """
    return self._config_get()

  @update.setter
  def update(self, val):
    self._config(val)

  @property
  def vertical(self):
    """
    Description:
    -----------
    Enable / disable user ability to vertically drag and fill.

    Related Pages:

      https://datatables.net/reference/option/autoFill.vertical
    """
    return self._config_get()

  @vertical.setter
  def vertical(self, val):
    self._config(val)
