"""
Module in charge of the CSS color conversion
The preferred color format in the framework is the hexadecimal format.

Some examples can be found here: https://htmlcolorcodes.com/color-picker/

There are also some features in order to convert from the RGB code color.

This module will also manage the different predefined themes

All the tests in this module are using doctest
https://docs.python.org/2/library/doctest.html
"""

import random
import math
import os
import importlib
import inspect


from epyk.core.css import Colors
from epyk.core.css import themes


class Theme(object):
  """
  Classe dedicated to store the current theme used.
  This singleton will store some important variable about the theme:
    - themes: THe list of the different available themes
    - selected: The definition of the selected theme (all the colors stored in a python dict)
    - name: the name of the current theme
  """
  themes, selected, name = None, None, None

  @classmethod
  def toHtml(cls, theme_name=None, path=None):
    """
    Export the theme to a HTML flat file

    :param theme_name: The theme reference (alias) in the framework
    :param path: Optional. The path for the HTML file
    """
    if theme_name is None:
      theme_name = cls.name
    if theme_name is None:
      raise Exception("theme_name should be defined")

    color_path = os.path.join(path, "colors")
    if not os.path.exists(color_path):
      os.mkdir(color_path)

    theme_obj = None
    for th in os.listdir(os.path.dirname(themes.__file__)):
      if th.startswith("Theme") and th.endswith(".py") and th != 'Theme.py':
        mod = importlib.import_module("epyk.core.css.themes.%s" % th.replace(".py", ""))
        for _, obj in inspect.getmembers(mod):
          if inspect.isclass(obj) and obj.name == theme_name:
            theme_obj = obj

    if theme_obj is None:
      raise Exception("%s does not exist in the internal themes" % theme_name)

    with open(os.path.join(color_path, "%s.html" % theme_name), "w") as f:
      css_style = "text-align:center;vertical-align:middle;width:80px;height:30px"
      for c in theme_obj.charts:
        f.write("<div style='background:%(color)s;%(css)s'>%(color)s</div>\n" % {'color': c, "css": css_style})


class ColorMaker(object):
  """
  The Color interface in charge of the color production.
  This class will manage the colors used in the framework.
  """
  class __internal(object):
    """
    Internal context for all the object created not in the framework context.
    This will ensure the process will still work.
    """
    _props = {}

  def __init__(self, rptObj=None, theme="blue-grey"):
    self.rptObj = rptObj if rptObj is not None else self.__internal()
    if isinstance(self.rptObj._props, dict):
      self.rptObj._props.setdefault('style', {})['theme'] = Theme()
      self._themeObj = self.rptObj._props.setdefault('style', {})['theme']
    else:
      self.rptObj._props.themes = None
      self._themeObj = self.rptObj._props
    self._loadThemes()
    self.setTheme(theme)

  @property
  def defined(self):
    """
    Returns the defined colors based on the name

    Documentation
    https://www.rapidtables.com/web/color/RGB_Color.html
    """
    return Colors.DefinedColors()

  def _loadThemes(self, reset=False):
    """
    Load all the predefined Color Themes in the module. This can be extend by some user functions in the epyk interface

    :param reset: Boolean flag to force the reset of the theme factory
    :return: A dictionary with all the defined themes
    """
    if self._themeObj.themes is None or reset:
      allThemes = {}
      for th in os.listdir(os.path.dirname(themes.__file__)):
        if th.startswith("Theme") and th.endswith(".py") and th != 'Theme.py':
          mod = importlib.import_module("epyk.core.css.themes.%s" % th.replace(".py", ""))
          for _, obj in inspect.getmembers(mod):
            if inspect.isclass(obj):
              allThemes[obj.name] = {}
              for n, cs in [("colors", list(obj.colors)), ('greys', list(obj.greys)),
                            ('charts', list(obj.charts)), ('warning', list(obj.warning)),
                            ('danger', list(obj.danger)), ('success', list(obj.success))]:
                allThemes[obj.name][n] = cs
      self._themeObj.themes = allThemes
    return self._themeObj.themes

  def setTheme(self, name, bespokeTheme=None):
    """
    Add a bespoke theme to the framework on the fly

    :param name: A theme class
    :param bespokeTheme: A theme class
    :return: The theme loaded from the factory
    """
    if bespokeTheme is not None and not name in self._themeObj.themes:
      self._themeObj.themes[name] = bespokeTheme
    self._themeObj.selected = self.getTheme(name)
    self._themeObj.name = name
    return self._themeObj.selected

  def getTheme(self, name, colorAttrs=None):
    """
    Get a defined theme using its reference. This function allows also the overrides of any parameters.
    The override will impact the theme definition in the factory. All the different use will be impacted.

    Examples
    >>> ColorMaker().getTheme('grey', {"colors": ["yellow"]})['colors'][:3]
    ['yellow', '#37474f', '#455a64']

    :param name: The theme name
    :param colorAttrs: The theme attributes with the list of colors
    :return: The overridden theme
    """
    t = self._themeObj.themes.get(name)
    if t is not None:
      if colorAttrs is not None:
        for k, colors in colorAttrs.items():
          for i, c in enumerate(colors):
            t[k][i] = c
    return t

  def set(self, colorCategory, hexColor, index=None):
    """
    Colors definition in Themes

    Set the colors defined in the current theme
    Category can be one of the following: charts, colors, greys, warning, danger, success

    :param category: The color category defined in the theme
    :param hexColor: The hexadecimal color code, examples: https://www.color-hex.com/
    :param index: Optional, the Color index in the theme
    :return: The Python ColorMaker Object
    """
    if index is not None:
      self._themeObj.selected[colorCategory][index] = hexColor
    else:
      self._themeObj.selected[colorCategory] = hexColor
    return self

  def get(self, category, index=None, hexColor=None):
    """
    Colors definition in Themes

    Get or override the colors defined in the current theme

    Example
    >>> ColorMaker().get('colors', 1)
    '#cfd8dc'

    >>> ColorMaker().get('colors', 2, 'yellow')
    'yellow'

    :param category: The color category defined in the theme
    :param index: The index in the range of color for the category
    :param hexColor: The color code to be set for this category, examples: https://www.color-hex.com/
    :return: The hexadecimal color code
    """
    if hexColor is not None:
      if index is None:
        self._themeObj.selected[category] = hexColor
      else:
        self._themeObj.selected[category][index] = hexColor
    if index is None:
      return self._themeObj.selected[category]

    return self._themeObj.selected[category][index]

  # --------------------------------------------------------------------------------------------------------------
  #
  #                                   COMMON COLOR TRANSFORMATIONS
  # --------------------------------------------------------------------------------------------------------------
  @classmethod
  def getHexToRgb(cls, hexColor):
    """
    Convert a hexadecimal color to a rgb code

    Examples
    >>> ColorMaker().getHexToRgb('#213B68')
    [33, 59, 104]

    :param hexColor: A String with a hexadecimal code color
    :return: The list with the rgb code color
    """
    if not hexColor.startswith("#"):
      raise Exception("Hexadecimal color should start with #")

    if not len(hexColor) == 7:
      raise Exception("Color should have a length of 7")

    return [int(hexColor[1:3], 16), int(hexColor[3:5], 16), int(hexColor[5:7], 16)]

  @classmethod
  def getRgbToHex(cls, rgbColor):
    """
    Convert a RGB color to a hexadecimal code

    Examples
    >>> ColorMaker().getRgbToHex([255, 0, 0])
    '#ff0000'

    :param rgbColor: A list corresponding to the RGB color code
    :return: String object defining the hexadecimal color code
    """
    color = []
    for val in rgbColor:
      val = hex(int(val)).lstrip('0x')
      if len(val) != 2:
        leadingZeros = ["0"] * (2 - len(val))
        val = "%s%s" % ("".join(leadingZeros), val)
      color.append(val)
    return "#%s" % "".join(color)

  @staticmethod
  def randColor(seedNo=None):
    """
    Generate a random hexadecimal color code

    Example
    >>> ColorMaker.randColor(10)
    '#9693DD'

    :param seedNo: Optional, The seed number used to generate random numbers
    :return: String with Hexadecimal color code
    """
    letters = '0123456789ABCDEF'
    color = ['#']
    if seedNo is not None:
      random.seed(seedNo)
    for i in range(6):
      color.append(letters[math.floor(random.random() * 16)])
    if seedNo is not None:
      random.seed(None) # Resent the seed to None
    return "".join(color)

  @classmethod
  def colors(cls, start, end, steps):
    """
    Generate a list of colors between two color codes.

    Example
    >>> ColorMaker().colors("#ffffff", "#FF0000", 10)
    ['#ffffff', '#ffe2e2', '#ffc6c6', '#ffaaaa', '#ff8d8d', '#ff7171', '#ff5555', '#ff3838', '#ff1c1c', '#FF0000']

    :param start: The start hexadecimal color code
    :param end: The end hexadecimal color code
    :param steps: The number of colors in the array
    :return: A list of hexadecimal color codes
    """
    colors = [start]
    for i in range(steps-2):
      colors.append(cls.gradient(start, end, 1.0/ (steps-1) * (i + 1)))
    colors.append(end)
    return colors

  @classmethod
  def gradient(cls, start, end, factor):
    """
    Deduce the color from a factor in a range of colors

    Examples
    >>> ColorMaker().gradient("#ffffff", "#FF0000", 0.2)
    '#ffcccc'

    :param start: The start hexadecimal color code
    :param end: The end hexadecimal color code
    :param factor: A factor in the range [0, 1]
    :return: The hexadecimal color code
    """
    if factor > 1:
      raise Exception("Gradient factor must be <= 1")

    rgbEnd = cls.getHexToRgb(end)
    rgbDiff = [(rgbEnd[i] - val) * factor + val for i, val in enumerate(cls.getHexToRgb(start))]
    return cls.getRgbToHex(rgbDiff)
