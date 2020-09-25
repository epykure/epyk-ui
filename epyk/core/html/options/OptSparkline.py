

from epyk.core.html.options import Options


class OptionsSparkLine(Options):
  component_properies = ("width", )

  @property
  def animate(self):
    """

    """
    return self._config_get(False)

  @animate.setter
  def animate(self, value):
    self._config(value)

  @property
  def width(self):
    """

    """
    return self._config_get("100%")

  @width.setter
  def width(self, value):
    self._config(value)
