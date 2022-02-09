
from epyk.core.html.options import Options


class KeyTable(Options):

  def activate(self):
    self.component.options.columns = ":not(:first-child)"
    return self

  @property
  def blurable(self):
    """
    Description:
    -----------
    Allow KeyTable's focus to be blurred (removed) from a table.

    Related Pages:

      https://datatables.net/reference/option/keys.blurable
    """
    return self._config_get()

  @blurable.setter
  def blurable(self, val):
    self._config(val)

  @property
  def className(self):
    """
    Description:
    -----------
    Set the class name used for the focused cell.

    Related Pages:

      https://datatables.net/reference/option/keys.className
    """
    return self._config_get()

  @className.setter
  def className(self, val):
    self._config(val)

  @property
  def clipboard(self):
    """
    Description:
    -----------
    Enable / disable clipboard interaction with KeyTable.

    Related Pages:

      https://datatables.net/reference/option/keys.clipboard
    """
    return self._config_get()

  @clipboard.setter
  def clipboard(self, val):
    self._config(val)

  @property
  def clipboardOrthogonal(self):
    """
    Description:
    -----------
    Set the orthogonal data to copy to clipboard.

    Related Pages:

      https://datatables.net/reference/option/keys.clipboardOrthogonal
    """
    return self._config_get()

  @clipboardOrthogonal.setter
  def clipboardOrthogonal(self, val):
    self._config(val)

  @property
  def columns(self):
    """
    Description:
    -----------
    Select the columns that can gain focus.

    Related Pages:

      https://datatables.net/reference/option/keys.columns
    """
    return self._config_get()

  @columns.setter
  def columns(self, val):
    self._config(val)

  @property
  def focus(self):
    """
    Description:
    -----------
    Cell to receive initial focus in the table.

    Related Pages:

      https://datatables.net/reference/option/keys.focus
    """
    return self._config_get()

  @focus.setter
  def focus(self, val):
    self._config(val)

  @property
  def keys(self):
    """
    Description:
    -----------
    Limit the keys that KeyTable will listen for and take action on

    Related Pages:

      https://datatables.net/reference/option/keys.keys
    """
    return self._config_get()

  @keys.setter
  def keys(self, val):
    self._config(val)

  @property
  def tabIndex(self):
    """
    Description:
    -----------
    Set the table's tab index for when it will receive focus.

    Related Pages:

      https://datatables.net/reference/option/keys.tabIndex
    """
    return self._config_get()

  @tabIndex.setter
  def tabIndex(self, val):
    self._config(val)
