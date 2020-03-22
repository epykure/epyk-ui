
from epyk.core.data import DataClass


class KeyTable(DataClass):

  def activate(self):
    self.columns = ":not(:first-child)"
    return self

  @property
  def blurable(self):
    """
    Allow KeyTable's focus to be blurred (removed) from a table.

    https://datatables.net/reference/option/keys.blurable
    """
    return self._attrs["blurable"]

  @blurable.setter
  def blurable(self, val):
    self._attrs["blurable"] = val

  @property
  def className(self):
    """
    Set the class name used for the focused cell.

    https://datatables.net/reference/option/keys.className
    """
    return self._attrs["className"]

  @className.setter
  def className(self, val):
    self._attrs["className"] = val

  @property
  def clipboard(self):
    """
    Enable / disable clipboard interaction with KeyTable.

    https://datatables.net/reference/option/keys.clipboard
    """
    return self._attrs["clipboard"]

  @clipboard.setter
  def clipboard(self, val):
    self._attrs["clipboard"] = val

  @property
  def clipboardOrthogonal(self):
    """
    Set the orthogonal data to copy to clipboard.

    https://datatables.net/reference/option/keys.clipboardOrthogonal
    """
    return self._attrs["clipboardOrthogonal"]

  @clipboardOrthogonal.setter
  def clipboardOrthogonal(self, val):
    self._attrs["clipboardOrthogonal"] = val

  @property
  def columns(self):
    """
    Select the columns that can gain focus.

    https://datatables.net/reference/option/keys.columns
    """
    return self._attrs["columns"]

  @columns.setter
  def columns(self, val):
    self._attrs["columns"] = val

  @property
  def focus(self):
    """
    Cell to receive initial focus in the table.

    https://datatables.net/reference/option/keys.focus
    """
    return self._attrs["focus"]

  @focus.setter
  def focus(self, val):
    self._attrs["focus"] = val

  @property
  def keys(self):
    """
    Limit the keys that KeyTable will listen for and take action on

    https://datatables.net/reference/option/keys.keys
    """
    return self._attrs["keys"]

  @keys.setter
  def keys(self, val):
    self._attrs["keys"] = val

  @property
  def tabIndex(self):
    """
    Set the table's tab index for when it will receive focus.

    https://datatables.net/reference/option/keys.tabIndex
    """
    return self._attrs["tabIndex"]

  @tabIndex.setter
  def tabIndex(self, val):
    self._attrs["tabIndex"] = val
