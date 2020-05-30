

from epyk.core.html.options import Options


class OptionsSparkLine(Options):

  @property
  def animate(self):
    """

    """
    return self._config_get(False)

  @animate.setter
  def animate(self, value):
    self._config(value)
