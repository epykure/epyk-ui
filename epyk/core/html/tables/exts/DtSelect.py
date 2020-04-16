
from epyk.core.data import DataClass
from epyk.core.data import DataEnum


class EnumStyleOptions(DataEnum):

  def api(self):
    """
    Description:
    -----------
    Selection can only be performed via the API

    Related Pages:


    https://datatables.net/reference/option/select.style
    """
    return self.set()

  def single(self):
    """
    Description:
    -----------
    Only a single item can be selected, any other selected items will be automatically deselected when a new item is selected

    Related Pages:


    https://datatables.net/reference/option/select.style
    """
    return self.set()

  def multi(self):
    """
    Description:
    -----------
    Multiple items can be selected. Selection is performed by simply clicking on the items to be selected

    Related Pages:


    https://datatables.net/reference/option/select.style
    """
    return self.set()

  def os(self):
    """
    Description:
    -----------
    Operating System (OS) style selection. This is the most comprehensive option and provides complex behaviours such as ctrl/cmd clicking to select / deselect individual items, shift clicking to select ranges and an unmodified click to select a single item.

    Related Pages:


    https://datatables.net/reference/option/select.style
    """
    return self.set()

  def multi_shift(self):
    """
    Description:
    -----------
    a hybrid between the os style and multi, allowing easy multi-row selection without immediate de-selection when clicking on a row.

    Related Pages:


    https://datatables.net/reference/option/select.style
    """
    return self.set("multi+shift")


class Select(DataClass):

  def activate(self):
    """
    Enable and configure the Scroller extension for DataTables

    https://datatables.net/reference/option/scroller
    """
    self.info = False
    self.items = 'row'
    return self

  @property
  def info(self):
    """
    Enable / disable the display for item selection information in the table summary

    https://datatables.net/reference/option/select.info
    """
    return self._attrs["info"]

  @info.setter
  def info(self, val):
    self._attrs["info"] = val

  @property
  def blurable(self):
    """
    Description:
    -----------
    Indicate if the selected items will be removed when clicking outside of the table

    Related Pages:


    https://datatables.net/reference/option/select.blurable
    """
    return self._attrs["blurable"]

  @blurable.setter
  def blurable(self, val):
    self._attrs["blurable"] = val

  @property
  def items(self):
    """
    Description:
    -----------
    Set which table items to select (rows, columns or cells).

    Related Pages:


    https://datatables.net/reference/option/select.items
    """
    return self._attrs["items"]

  @items.setter
  def items(self, val):
    self._attrs["items"] = val

  @property
  def style(self):
    """
    Description:
    -----------
    Set the selection style for end user interaction with the table.

    Related Pages:


    https://datatables.net/reference/option/select.style
    """
    return self._attrs["style"]

  @style.setter
  def style(self, val):
    self._attrs["style"] = val

  @property
  def toggleable(self):
    """
    Description:
    -----------
    Disable the deselection of selected rows when clicked.

    Related Pages:


    https://datatables.net/reference/option/select.toggleable
    """
    return self._attrs["toggleable"]

  @toggleable.setter
  def toggleable(self, val):
    self._attrs["toggleable"] = val
