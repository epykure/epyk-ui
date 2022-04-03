#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.css.themes import palettes


class ColorRange:

  def __init__(self, colors: list, index: int = None):
    self.__colors = colors
    self.index = index or round(len(colors)/2)

  def reverse(self):
    self.__colors = self.__colors[::-1]

  @property
  def light(self):
    return self.__colors[0]

  @property
  def dark(self):
    return self.__colors[-1]

  @property
  def base(self):
    return self.__colors[self.index]


class Theme:
  dark = False
  _greys = ['#FFFFFF', '#f5f5f5', '#eeeeee', '#e0e0e0', '#bdbdbd', '#9e9e9e', '#757575', '#616161', '#424242',
            '#212121', '#000000']
  _info = ["#e3f2fd", "#2196f3", "#0d47a1"]

  def __init__(self, ovr_attrs: dict = None, index: int = 5, step: int = 1):
    self.__colors = {
      "charts": list(self._charts),
      "colors": list(self._colors),
      "greys": list(self._greys),
      "warning": ColorRange(self._warning),
      "danger": ColorRange(self._danger),
      "success": ColorRange(self._success),
      "info": ColorRange(self._info),
    }
    self.index = index
    self.step = step
    if ovr_attrs is not None:
      self.__colors.update(ovr_attrs)

  def notch(self, value: int = None, step: int = None):
    """
    Description:
    ------------
    Get the base color from the theme.
    The base color can change and it is defined by the variable self.index.

    Usage::

      base_color = page.theme.notch()

    Attributes:
    ----------
    :param value: Optional. The number of notch from the centered index.
    :param step: Optional The value of a move (default 1).
    """
    step = step or self.step
    if value is not None:
      return self.colors[max(0, min(self.index + value * step, len(self.colors)-1))]

    return self.colors[self.index]

  @property
  def white(self):
    """
    Description:
    ------------
    Get the white color from the theme.

    Usage::

      color = page.theme.white
    """
    return self.__colors["greys"][0]

  def dark_or_white(self, light=True) -> str:
    """
    Description:
    ------------
    Get the appropriate light or dark color according to the theme.
    Setting the Light flag to true will point to white in light mode otherwise it will point to black.
    """
    if light:
      return self.black if self.dark else self.white

    return self.white if self.dark else self.black

  @property
  def black(self):
    """
    Description:
    ------------
    Get the black color from the theme.

    Usage::

      color = page.theme.black
    """
    return self.__colors["greys"][-1]

  @property
  def charts(self):
    """
    Description:
    ------------
    Get the chart colors from the theme.

    Usage::

      colors = page.theme.charts
    """
    return self.__colors["charts"]

  @charts.setter
  def charts(self, colors: list):
    self.__colors["charts"] = colors

  @property
  def colors(self):
    """
    Description:
    ------------
    Get the theme colors scale.

    Usage::

      colors = page.theme.colors
    """
    if self.dark:
      return self.__colors["colors"][::-1]

    return self.__colors["colors"]

  @colors.setter
  def colors(self, colors: list):
    self.__colors["colors"] = colors

  @property
  def greys(self):
    """
    Description:
    ------------
    Get the theme grey colors scale.

    Usage::

      colors = page.theme.greys
    """
    if self.dark:
      return self.__colors["greys"][::-1]

    return self.__colors["greys"]

  @greys.setter
  def greys(self, colors: list):
    self.__colors["greys"] = colors

  @property
  def warning(self) -> ColorRange:
    """
    Description:
    ------------
    Get the warning colors. It is a tuple (light, dark).

    Usage::

      light, dark = page.theme.warning
    """
    return self.__colors["warning"]

  @warning.setter
  def warning(self, colors: list):
    self.__colors["warning"] = ColorRange(colors)

  @property
  def danger(self) -> ColorRange:
    """
    Description:
    ------------
    Get the danger colors. It is a tuple (light, dark).

    Usage::

      light, dark = page.theme.danger
    """
    return self.__colors["danger"]

  @danger.setter
  def danger(self, colors: list):
    self.__colors["danger"] = ColorRange(colors)

  @property
  def info(self) -> ColorRange:
    """
    Description:
    ------------
    Get the info colors. It is a tuple (light, dark).

    Usage::

      light, dark = page.theme.danger
    """
    return self.__colors["info"]

  @info.setter
  def info(self, colors: list):
    self.__colors["info"] = ColorRange(colors)

  @property
  def success(self) -> ColorRange:
    """
    Description:
    ------------
    Get the success colors. It is a tuple (light, dark).

    Usage::

      light, dark = page.theme.success
    """
    return self.__colors["success"]

  @success.setter
  def success(self, colors: list):
    self.__colors["success"] = ColorRange(colors)

  def color_palette(self, palette: str = None, n_colors: int = None, desat: float = None):
    """
    Description:
    ------------
    Change the chart color codes using standard palettes used in JavaScript and Python libraries.

    Related Pages:

      https://nagix.github.io/chartjs-plugin-colorschemes/colorchart.html

    Attributes:
    ----------
    :param palette: Optional. Name of palette or None to set for charts colors.
    :param n_colors: Optional. Number of colors in the palette.
    :param desat: Optional. Proportion to desaturate each color by.
    """
    if palette is not None and palette.startswith("brewer."):
      self.__colors["charts"] = getattr(palettes.brewer, palette.split(".")[1])
    elif palette is not None and palette.startswith("office."):
      self.__colors["charts"] = getattr(palettes.office, palette.split(".")[1])
    elif palette is not None and palette.startswith("tableau."):
      self.__colors["charts"] = getattr(palettes.tableau, palette.split(".")[1])


class ThemeCustom(Theme):
  _charts, _colors, _greys = [], [], []
  _warning, _danger, _success = set(), set(), set()


class ThemeDefault(Theme):

  _charts = [
    '#009999', '#336699', '#ffdcb9',
    '#cc99ff', '#b3d9ff', '#ffff99',
    '#000066', '#b2dfdb', '#80cbc4',
    '#e0f2f1', '#b2dfdb', '#80cbc4',  # teal
    '#ffebee', '#ffcdd2', '#ef9a9a',  # red
    '#f3e5f5', '#e1bee7', '#ce93d8',  # purple
    '#ede7f6', '#d1c4e9', '#b39ddb',  # deep purple
    '#e8eaf6', '#c5cae9', '#9fa8da',  # indigo
    '#fffde7', '#fff9c4', '#fff59d',  # yellow
    '#fff3e0', '#ffe0b2', '#ffcc80',  # orange
    '#efebe9', '#d7ccc8', '#bcaaa4',  # brown
  ]
  _colors = ['#f4f9fc', '#cfd8dc', '#b0bec5', '#90a4ae', '#78909c', '#607d8b', '#546e7a', '#455a64',
             '#37474f', '#263238']
  _warning, _danger, _success = ['#FFF3CD', '#e2ac00'], ["#F8D7DA", "#C00000"], ['#e8f2ef', '#5DDEAD']
