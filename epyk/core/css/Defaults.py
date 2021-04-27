#!/usr/bin/python
# -*- coding: utf-8 -*-


class Font:
  _size, header_size, unit = 14, 16, "px"
  family = "Calibri"

  def __init__(self, page):
    self.page = page

  @property
  def size(self):
    return self._size

  @size.setter
  def size(self, value):
    self.page.body.style.css.font_size = value
    self.header_size = value + 2
    self._size = value

  def normal(self, step=0, unit=None):
    """
    Description:
    ------------
    Font text format.

    Attributes:
    ----------
    :param step: Integer. Optional. The value to be added to the default font size.
    :param unit: String. Optional. The unit code. default px.
    """
    return "%s%s" % (self._size + step, unit or self.unit)

  def header(self, step=0, unit=None):
    """
    Description:
    ------------
    Font header format.

    Attributes:
    ----------
    :param step: Integer. Optional. The value to be added to the default font size.
    :param unit: String. Optional. The unit code. default px.
    """
    return "%s%s" % (self.header_size + step, unit or self.unit)


class Icon:
  small, normal, big, unit = 10, 15, 25, 'px'

  def small_size(self, step=0, unit=None):
    """
    Description:
    ------------
    Icon small format.

    Attributes:
    ----------
    :param step: Integer. Optional. The value to be added to the default font size.
    :param unit: String. Optional. The unit code. default px.
    """
    return "%s%s" % (self.small+step, unit or self.unit)

  def normal_size(self, step=0, unit=None):
    """
    Description:
    ------------
    Icon normal format.

    Attributes:
    ----------
    :param step: Integer. Optional. The value to be added to the default font size.
    :param unit: String. Optional. The unit code. default px.
    """
    return "%s%s" % (self.normal+step, unit or self.unit)

  def big_size(self, step=0, unit=None):
    """
    Description:
    ------------
    Icon big format.

    Attributes:
    ----------
    :param step: Integer. Optional. The value to be added to the default font size.
    :param unit: String. Optional. The unit code. default px.
    """
    return "%s%s" % (self.big+step, unit or self.unit)


def header(step=0):
  """
  Description:
  ------------

  Usage::

  Attributes:
  ----------
  :param step: Integer. Optional. The value to be added to the default font size.
  """
  return "%s%s" % (Font.header_size+step, Font.unit)


def inline(css_attrs):
  """
  Description:
  ------------
  Convert a CSS attributes dictionary to a online CSS Style to be added to the dom object.

  Usage::

    inline({"color": "red"})

  Related Pages:
  --------------
  https://www.w3schools.com/css/css_howto.asp

  Attributes:
  ----------
  :param css_attrs: Dictionary. The CSS Attributes.
  """
  return ";".join(["%s: %s" % (k, v) for k, v in css_attrs.items()])


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
BODY_CONTAINER = None   # The body CSS dictionary
BODY_STYLE = None
BACKGROUND = ('greys', 0)
MEDIA = 600


# Default CSS
CSS_EXCEPTIONS = True
CSS_EXCEPTIONS_FORMAT = "CSS - %s - invalid %s"


class GlobalStyle:

  def __init__(self, page):
    self.page = page
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
      self._font = Font(self.page)
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
        header_background = self.page.theme.colors[-1]
        header_color = "white"
        header_border = '1px solid white'
        cell_border_bottom = "1px solid %s" % self.page.theme.colors[4]
        cell_border_right = None
        sorter_arrow_selected = self.page.theme.colors[-3]
        sorter_arrow = "white"
      self._table = GlobalTable()
    return self._table

