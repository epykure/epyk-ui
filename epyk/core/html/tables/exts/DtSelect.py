
from epyk.core.html.options import Options
from epyk.core.html.options import Enums


class EnumStyleOptions(Enums):

  def api(self):
    """   Selection can only be performed via the API

    Related Pages:

      https://datatables.net/reference/option/select.style
    """
    return self._set_value()

  def single(self):
    """   Only a single item can be selected, any other selected items will be automatically deselected when a new item
    is selected

    Related Pages:

      https://datatables.net/reference/option/select.style
    """
    return self._set_value()

  def multi(self):
    """   Multiple items can be selected. Selection is performed by simply clicking on the items to be selected

    Related Pages:

      https://datatables.net/reference/option/select.style
    """
    return self._set_value()

  def os(self):
    """   Operating System (OS) style selection. This is the most comprehensive option and provides complex behaviours
    such as ctrl/cmd clicking to select / deselect individual items, shift clicking to select ranges and an unmodified
    click to select a single item.

    Related Pages:

      https://datatables.net/reference/option/select.style
    """
    return self._set_value()

  def multi_shift(self):
    """   a hybrid between the os style and multi, allowing easy multi-row selection without immediate de-selection when
    clicking on a row.

    Related Pages:

      https://datatables.net/reference/option/select.style
    """
    return self._set_value(value="multi+shift")


class Select(Options):

  def activate(self):
    """   Enable and configure the Scroller extension for DataTables.

    Related Pages:

      https://datatables.net/reference/option/scroller
    """
    self.info = False
    self.items = 'row'
    return self

  @property
  def info(self):
    """   Enable / disable the display for item selection information in the table summary

    Related Pages:

      https://datatables.net/reference/option/select.info
    """
    return self._config_get()

  @info.setter
  def info(self, val):
    self._config(val)

  @property
  def blurable(self):
    """   Indicate if the selected items will be removed when clicking outside of the table

    Related Pages:

      https://datatables.net/reference/option/select.blurable
    """
    return self._config_get()

  @blurable.setter
  def blurable(self, val):
    self._config(val)

  @property
  def items(self):
    """   Set which table items to select (rows, columns or cells).

    Related Pages:

      https://datatables.net/reference/option/select.items
    """
    return self._config_get()

  @items.setter
  def items(self, val):
    self._config(val)

  @property
  def style(self):
    """   Set the selection style for end user interaction with the table.

    Related Pages:

      https://datatables.net/reference/option/select.style
    """
    return self._config_get()

  @style.setter
  def style(self, val):
    self._config(val)

  @property
  def toggleable(self):
    """   Disable the deselection of selected rows when clicked.

    Related Pages:

      https://datatables.net/reference/option/select.toggleable
    """
    return self._config_get()

  @toggleable.setter
  def toggleable(self, val):
    self._config(val)
