
from typing import Union, Optional
from epyk.core.html.options import Options


class OptionsPivot(Options):

  @property
  def sortable(self):
    """
    """
    return self._config_get(True)

  @sortable.setter
  def sortable(self, flag: bool):
    self._config(flag)

  @property
  def readonly_rows(self):
    """
    """
    return self._config_get(False)

  @readonly_rows.setter
  def readonly_rows(self, flag: bool):
    self._config(flag)

  @property
  def delete_rows(self):
    """
    """
    return self._config_get(True)

  @delete_rows.setter
  def delete_rows(self, flag: bool):
    self._config(flag)

  @property
  def readonly_columns(self):
    """
    """
    return self._config_get(False)

  @readonly_columns.setter
  def readonly_columns(self, flag: bool):
    self._config(flag)

  @property
  def delete_columns(self):
    """
    """
    return self._config_get(True)

  @delete_columns.setter
  def delete_columns(self, flag: bool):
    self._config(flag)

  @property
  def title_values(self):
    """
    """
    return self._config_get(
      "Values <i style='font-size:%s'>(multiple fields)</i>" % self.page.body.style.globals.font.normal(-3))

  @title_values.setter
  def title_values(self, text: str):
    self._config(text)

  @property
  def title_rows(self):
    """
    """
    return self._config_get(
      "Rows <i style='font-size:%s'>(unique field)</i>" % self.page.body.style.globals.font.normal(-3))

  @title_rows.setter
  def title_rows(self, text: str):
    self._config(text)
