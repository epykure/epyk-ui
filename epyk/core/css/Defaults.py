
class Font:
  size, header_size, unit = 14, 16, "px"
  family = "Calibri"


class Icon:
  small, normal, big, unit = 10, 15, 20, 'px'


def font(step=0):
  """
  Description:
  ------------
  Relative change of the CSS font size based on the default one in the Font class.
  Changing the value Font.size will impact this function accordingly.

  Usage:
  -----

    font(2)

  Attributes:
  ----------
  :param step: integer. Optional. The value to be added to the default font size.
  """
  return "%s%s" % (Font.size+step, Font.unit)


def header(step=0):
  """
  Description:
  ------------

  Usage:
  -----

  Attributes:
  ----------
  :param step:
  """
  return "%s%s" % (Font.header_size+step, Font.unit)


def inline(cssAttrs):
  """
  Description:
  ------------
  Convert a CSS attributes dictionary to a online CSS Style to be added to the dom object.

  Usage:
  -----

    inline({"color": "red"})

  Related Pages:
  --------------
  https://www.w3schools.com/css/css_howto.asp

  Attributes:
  ----------
  :param cssAttrs: Dictionary. The CSS Attributes.
  """
  return ";".join(["%s: %s" % (k, v) for k, v in cssAttrs.items()])


def px_to_em(value, with_unit=True):
  """
  Description:
  ------------
  Convert the pixel value to em.

  Related Pages:
  --------------

    https://www.w3schools.com/cssref/css_pxtoemconversion.asp

  Attributes:
  ----------
  :param value: Float. A pixel value.
  :param with_unit: Boolean. Optional. To define the return format.
  """
  em_value = value / 16
  if with_unit:
    return "%sem" % em_value

  return em_value


def em_to_px(value, with_unit=True):
  """
  Description:
  ------------
  Convert a em value in pixel.

  Related Pages:
  --------------

    https://www.w3schools.com/cssref/css_pxtoemconversion.asp

  Attributes:
  ----------
  :param value: Float. The em value.
  :param with_unit: Boolean. Optional. To define the return format.
  """
  px_value = value * 16
  if with_unit:
    return "%spx" % px_value

  return px_value


#
DEFAULT_STYLE = "no_border"


# Default CSS Styles
BODY_CONTAINER = None # The body CSS dictionary
BODY_STYLE = None
BACKGROUND = ('greys', 0)
MEDIA = 600


# Default CSS
CSS_EXCEPTIONS = True
CSS_EXCEPTIONS_FORMAT = "CSS - %s - invalid %s"


class GlobalStyle:

  def __init__(self, page):
    self._report = page
    self._font = None
    self._icon = None
    self._table = None

  @property
  def font(self):
    """
    Description:
    ------------

    """
    if self._font is None:
      self._font = Font()
    return self._font

  @property
  def icon(self):
    """
    Description:
    ------------

    Usage:
    -----
    """
    if self._icon is None:
      self._icon = Icon()
    return self._icon

  @property
  def table(self):
    """
    Description:
    ------------

    Usage:
    -----
    """
    if self._table is None:
      class GlobalTable:
        header_background = self._report.theme.colors[-1]
        header_color = "white"
        header_border = '1px solid white'
      self._table = GlobalTable()
    return self._table

