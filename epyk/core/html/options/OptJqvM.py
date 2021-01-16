
from epyk.core.html.options import Options


class OptionsJqVM(Options):
  component_properties = ('backgroundColor', 'color', 'hoverOpacity', 'selectedColor', 'enableZoom', 'showTooltip',
                          'scaleColors', 'normalizeFunction', 'hoverColor')

  @property
  def map(self):
    """
    Description:
    -----------
    The map alias.

    Usage:
    -----

    Related Pages:

      https://www.10bestdesign.com/jqvmap/documentation/

    Attributes:
    ----------
    :prop value: String. The map alias code.
    """
    return self._config_get(None)

  @map.setter
  def map(self, value):
    self._config(value)

  @property
  def borderColor(self):
    """
    Description:
    -----------
    Border Color to use to outline map objects

    Usage:
    -----

    Related Pages:

      https://www.10bestdesign.com/jqvmap/documentation/

    Attributes:
    ----------
    :prop color: String. The color code.
    """
    return self._config_get(None)

  @borderColor.setter
  def borderColor(self, color):
    self._config(color)

  @property
  def borderOpacity(self):
    """
    Description:
    -----------
    Border Opacity to use to outline map objects ( use anything from 0-1, e.g. 0.5, defaults to 0.25 )

    Usage:
    -----

    Related Pages:

      https://www.10bestdesign.com/jqvmap/documentation/

    Attributes:
    ----------
    :prop num: Float. The opacity value.
    """
    return self._config_get(0.25)

  @borderOpacity.setter
  def borderOpacity(self, num):
    self._config(num)

  @property
  def borderWidth(self):
    """
    Description:
    -----------
    Border Width to use to outline map objects ( defaults to 1 ).

    Usage:
    -----

    Related Pages:

      https://www.10bestdesign.com/jqvmap/documentation/

    Attributes:
    ----------
    :prop num: Float. The border width value in pixel.
    """
    return self._config_get(1)

  @borderWidth.setter
  def borderWidth(self, num):
    self._config(num)

  @property
  def backgroundColor(self):
    """
    Description:
    -----------
    Background color of map container in any CSS compatible format.

    Usage:
    -----

    Related Pages:

      https://www.10bestdesign.com/jqvmap/documentation/

    Attributes:
    ----------
    :prop color: String. The color code.
    """
    return self._config_get("#fff")

  @backgroundColor.setter
  def backgroundColor(self, color):
    self._config(color)

  @property
  def color(self):
    """
    Description:
    -----------
    Color of map regions.

    Usage:
    -----

    Related Pages:

      https://www.10bestdesign.com/jqvmap/documentation/

    Attributes:
    ----------
    :prop color: String. The color code.
    """
    return self._config_get("#ffffff")

  @color.setter
  def color(self, color):
    self._config(color)

  @property
  def colors(self):
    """
    Description:
    -----------
    Colors of individual map regions. Keys of the colors objects are country codes according to ISO 3166-1 alpha-2 standard.
    Keys of colors must be in lower case.

    Usage:
    -----

    Related Pages:

      https://www.10bestdesign.com/jqvmap/documentation/

    Attributes:
    ----------
    :prop colors: Dictionary. The color to be used per country.
    """
    return self._config_get(None)

  @colors.setter
  def colors(self, colors):
    self._config(colors)

  @property
  def hoverColor(self):
    """
    Description:
    -----------
    Color of the region when mouse pointer is over it.

    Usage:
    -----

    Related Pages:

      https://www.10bestdesign.com/jqvmap/documentation/

    Attributes:
    ----------
    :prop color: String. The color code.
    """
    return self._config_get(self._report._report.theme.success[1])

  @hoverColor.setter
  def hoverColor(self, color):
    self._config(color)

  @property
  def hoverColors(self):
    """
    Description:
    -----------
    Colors of individual map regions when mouse pointer is over it. Keys of the colors objects are country codes according to ISO 3166-1 alpha-2 standard.
    Keys of colors must be in lower case.

    Usage:
    -----

    Related Pages:

      https://www.10bestdesign.com/jqvmap/documentation/

    Attributes:
    ----------
    :prop colors: Dictionary. The color code.
    """
    return self._config_get(None)

  @hoverColors.setter
  def hoverColors(self, colors):
    self._config(colors)

  @property
  def hoverOpacity(self):
    """
    Description:
    -----------
    Opacity of the region when mouse pointer is over it.

    Usage:
    -----

    Related Pages:

      https://www.10bestdesign.com/jqvmap/documentation/

    Attributes:
    ----------
    :prop num: Float. The opacity value.
    """
    return self._config_get(0.7)

  @hoverOpacity.setter
  def hoverOpacity(self, num):
    self._config(num)

  @property
  def selectedColor(self):
    return self._config_get(self._report._report.theme.colors[-1])

  @selectedColor.setter
  def selectedColor(self, num):
    self._config(num)

  @property
  def selectedRegions(self):
    return self._config_get(None)

  @selectedRegions.setter
  def selectedRegions(self, value):
    self._config(value)

  @property
  def enableZoom(self):
    return self._config_get(False)

  @enableZoom.setter
  def enableZoom(self, bool):
    self._config(bool)

  @property
  def showTooltip(self):
    return self._config_get(True)

  @showTooltip.setter
  def showTooltip(self, bool):
    self._config(bool)

  @property
  def scaleColors(self):
    """
    Description:
    -----------
    This option defines colors, with which regions will be painted when you set option values.
    Array scaleColors can have more then two elements.
    Elements should be strings representing colors in RGB hex format.

    Usage:
    -----

    Related Pages:

      https://www.10bestdesign.com/jqvmap/documentation/

    Attributes:
    ----------
    :prop colors: List. The colors codes.
    """
    return self._config_get([self._report._report.theme.colors[0], self._report._report.theme.colors[-1]])

  @scaleColors.setter
  def scaleColors(self, colors):
    self._config(colors)

  @property
  def values(self):
    return self._config_get({})

  @values.setter
  def values(self, value):
    self._config(value)

  @property
  def normalizeFunction(self):
    return self._config_get('polynomial')

  @normalizeFunction.setter
  def normalizeFunction(self, value):
    self._config(value)
