
from epyk.core.html.options import Options


class OptionsNumCircle(Options):
  @property
  def value(self):
    """
    """
    return self._config_get(None)

  @value.setter
  def value(self, val: str):
    self._config(val)
