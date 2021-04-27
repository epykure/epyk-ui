#!/usr/bin/python
# -*- coding: utf-8 -*-

# TODO: improve the color palette definition for charts

from epyk.core.css.themes import palettes


class Theme:
  dark = False
  _greys = ['#FFFFFF', '#f5f5f5', '#eeeeee', '#e0e0e0', '#bdbdbd', '#9e9e9e', '#757575', '#616161', '#424242',
            '#212121', '#000000']

  def __init__(self, ovr_attrs=None, index=5, step=1):
    self.__colors = {
      "charts": list(self._charts),
      "colors": list(self._colors),
      "greys": list(self._greys),
      "warning": list(self._warning),
      "danger": list(self._danger),
      "success": list(self._success),
    }
    self.index = index
    self.step = step
    if ovr_attrs is not None:
      self.__colors.update(ovr_attrs)

  def notch(self, value=None, step=None):
    """
    Description:
    ------------
    Get the base color from the theme.
    The base color can change and it is defined by the variable self.index.

    Usage::

      base_color = page.theme.notch()

    Attributes:
    ----------
    :param value: Integer. Optional. The number of notch from the centered index.
    :param step: Integer. Optional The value of a move (default 1).
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
  def charts(self, colors):
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
  def colors(self, colors):
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
  def greys(self, colors):
    self.__colors["greys"] = colors

  @property
  def warning(self):
    """
    Description:
    ------------
    Get the warning colors. It is a tuple (light, dark).

    Usage::

      light, dark = page.theme.warning
    """
    return self.__colors["warning"]

  @warning.setter
  def warning(self, colors):
    self.__colors["warning"] = colors

  @property
  def danger(self):
    """
    Description:
    ------------
    Get the danger colors. It is a tuple (light, dark).

    Usage::

      light, dark = page.theme.danger
    """
    return self.__colors["danger"]

  @danger.setter
  def danger(self, colors):
    self.__colors["danger"] = colors

  @property
  def success(self):
    """
    Description:
    ------------
    Get the success colors. It is a tuple (light, dark).

    Usage::

      light, dark = page.theme.success
    """
    return self.__colors["success"]

  @success.setter
  def success(self, colors):
    self.__colors["success"] = colors

  def color_palette(self, palette=None, n_colors=None, desat=None):
    """
    Description:
    ------------
    Change the chart color codes using standard palettes used in JavaScript and Python libraries.

    Related Pages:

      https://nagix.github.io/chartjs-plugin-colorschemes/colorchart.html

    Attributes:
    ----------
    :param palette: String. Optional. Name of palette or None to set for charts colors.
    :param n_colors: Integer. Optional. Number of colors in the palette.
    :param desat: Float. Optional. Proportion to desaturate each color by.
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
  _warning, _danger, _success = ('#FFF3CD', '#e2ac00'), ("#F8D7DA", "#C00000"), ('#e8f2ef', '#5DDEAD')
