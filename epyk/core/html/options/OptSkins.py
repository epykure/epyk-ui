
from epyk.core.html.options import Options


class OptionsSkin(Options):
  component_properties = ("color", 'font_size')

  @property
  def color(self):
    """
    Specify if the all item should be added to the items.

    """
    return self._config_get(self.page.theme.notch())

  @color.setter
  def color(self, value: str):
    self._config(value)

  @property
  def font_size(self):
    """

    """
    return self._config_get(10)

  @font_size.setter
  def font_size(self, num: int):
    self._config(num)
