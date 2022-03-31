
from typing import Union, Optional
from epyk.core.html.options import Options


class OptionsPivot(Options):

  @property
  def sortable(self):
    """
    Description:
    ------------
    """
    return self._config_get(True)

  @sortable.setter
  def sortable(self, flag: bool):
    self._config(flag)

  @property
  def readonly_rows(self):
    """
    Description:
    ------------
    """
    return self._config_get(False)

  @readonly_rows.setter
  def readonly_rows(self, flag: bool):
    self._config(flag)

  @property
  def delete_rows(self):
    """
    Description:
    ------------
    """
    return self._config_get(True)

  @delete_rows.setter
  def delete_rows(self, flag: bool):
    self._config(flag)

  @property
  def readonly_columns(self):
    """
    Description:
    ------------
    """
    return self._config_get(False)

  @readonly_columns.setter
  def readonly_columns(self, flag: bool):
    self._config(flag)

  @property
  def delete_columns(self):
    """
    Description:
    ------------
    """
    return self._config_get(True)

  @delete_columns.setter
  def delete_columns(self, flag: bool):
    self._config(flag)
