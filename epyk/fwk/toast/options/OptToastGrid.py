
from epyk.core.html.options import Options
from epyk.core.html.options import Enums


class Column(Options):
  @property
  def header(self):
    """
    Description:
    -----------

    Related Pages:

      https://nhn.github.io/tui.grid/latest/tutorial-example01-basic
    """
    return self._config_get()

  @header.setter
  def header(self, val):
    self._config(val)

  @property
  def name(self):
    """
    Description:
    -----------

    Related Pages:

      https://nhn.github.io/tui.grid/latest/tutorial-example01-basic
    """
    return self._config_get()

  @name.setter
  def name(self, val):
    self._config(val)

  @property
  def editor(self):
    """
    Description:
    -----------

    Related Pages:

      https://nhn.github.io/tui.grid/latest/tutorial-example01-basic
    """
    return self._config_get()

  @editor.setter
  def editor(self, val):
    self._config(val)


class GridConfig(Options):

  @property
  def el(self):
    """
    Description:
    ------------

    """
    return self._config_get()

  @el.setter
  def el(self, text):
    self._config(text)

  @property
  def data(self):
    """
    Description:
    ------------
    Grid data for making rows. When using the data source, sets to object.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid
    """
    return self._config_get()

  @data.setter
  def data(self, array):
    self._config(array)

  @property
  def scrollX(self):
    """
    Description:
    ------------

    """
    return self._config_get()

  @scrollX.setter
  def scrollX(self, flag):
    self._config(flag)


  @property
  def scrollY(self):
    """
    Description:
    ------------

    """
    return self._config_get()

  @scrollY.setter
  def scrollY(self, flag):
    self._config(flag)

  def add_column(self, field, title=None):
    """
    Description:
    ------------
    Add new column to the underlying Tabulator object.

    Attributes:
    ----------
    :param field: String. Mandatory. The key in the row.
    :param title: String. Optional. The title for the column. Default to the field.

    :rtype: Column
    """
    col_def = self._config_sub_data_enum("columns", Column)
    col_def.name = field
    col_def.header = field if title is None else title
    return col_def
