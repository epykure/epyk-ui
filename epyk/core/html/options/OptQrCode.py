
from epyk.core.html.options import Options


class OptionsQrCode(Options):
  component_properties = ("colorDark", "colorLight")

  @property
  def width(self):
    """
    Description:
    ------------

    Related Pages:

      https://davidshimjs.github.io/qrcodejs/

    Attributes:
    ----------
    :prop num:
    """
    return self._config_get(128)

  @width.setter
  def width(self, num: int):
    self._config(num)

  @property
  def height(self):
    """
    Description:
    ------------

    Related Pages:

      https://davidshimjs.github.io/qrcodejs/

    Attributes:
    ----------
    :prop num:
    """
    return self._config_get(128)

  @height.setter
  def height(self, num: int):
    self._config(num)

  @property
  def size(self):
    """
    Description:
    ------------

    Related Pages:

      https://davidshimjs.github.io/qrcodejs/

    Attributes:
    ----------
    :prop num:
    """
    return self.width

  @size.setter
  def size(self, num: int):
    self.height = num
    self.width = num

  @property
  def colorDark(self):
    """
    Description:
    ------------

    Related Pages:

      https://davidshimjs.github.io/qrcodejs/

    Attributes:
    ----------
    :prop color: String. The color value.
    """
    return self._config_get("#000000")

  @colorDark.setter
  def colorDark(self, color: str):
    self._config(color)

  @property
  def colorLight(self):
    """
    Description:
    ------------

    Related Pages:

      https://davidshimjs.github.io/qrcodejs/

    Attributes:
    ----------
    :prop color: String. The color value.
    """
    return self._config_get("#ffffff")

  @colorLight.setter
  def colorLight(self, color: str):
    self._config(color)
