"""
CSS Module in charge of defining the global classes
"""

from epyk.core.css.styles.classes import CssStyle


class Overflow(object):
  def __init__(self, cssObj):
    self._cssObj = cssObj
    self._cssObj.cssStyles["::-webkit-scrollbar"] = "{ height: 10px; }"
    self._cssObj.cssStyles["::-webkit-scrollbar-track"] = "{ border-radius: 10px; -webkit-box-shadow: inset 0 0 2px rgba(0,0,0,0.5); }"

  def button(self):
    """
    Description:
    -----------
    Add the arrows to the scroll bar.

    Usage:
    -----
    """
    self._cssObj.cssStyles["::-webkit-scrollbar-button:single-button"] = "{ background-color: #bbbbbb; display: block; border-style: solid; height: 13px; width: 16px; }"
    self._cssObj.cssStyles["::-webkit-scrollbar-button:single-button:vertical:decrement"] = "{ border-width: 0 8px 8px 8px; border-color: transparent transparent #555555 transparent; }"
    self._cssObj.cssStyles["::-webkit-scrollbar-button:single-button:vertical:increment"] = "{ border-width: 8px 8px 0 8px; border-color: #555555 transparent transparent transparent; }"

  def thumb(self, style=None, css_hover=None, css_active=None):
    """
    Description:
    -----------

    Usage:
    -----

    Attributes:
    ----------
    :param style: Dictionary. Optional.
    :param css_hover: Dictionary. Optional.
    :param css_active: Dictionary. Optional.
    """
    if style is not None:
      self._cssObj.cssStyles["::-webkit-scrollbar-thumb"] = CssStyle.CssCls.toCss(style)
    if css_hover is not None:
      self._cssObj.cssStyles["::-webkit-scrollbar-thumb:hover"] = CssStyle.CssCls.toCss(css_hover)
    if css_active is not None:
      self._cssObj.cssStyles["::-webkit-scrollbar-thumb:active"] = CssStyle.CssCls.toCss(css_active)

  def horizontal(self):
    """
    Description:
    -----------

    Usage:
    -----
    """

  def vertical(self):
    """
    Description:
    -----------

    Usage:
    -----
    """


class CssGlobal(object):

  def __init__(self, cssObj):
    self._cssObj = cssObj

  @property
  def overflow(self):
    """
    Description:
    -----------

    Usage:
    -----
    """
    return Overflow(self._cssObj)

  def style(self, name, attrs):
    """
    Description:
    -----------
    Add a new CSS Class in the page header.

    Usage:
    -----

    Related Pages:

      https://www.w3schools.com/html/html_css.asp

    Attributes:
    ----------
    :param name: String. The CSS Style reference as a string.
    :param attrs: Dictionary. The CSS attributes as a dictionary.

    :return: The CSS Object
    """
    self._cssObj.cssStyles[name] = CssStyle.CssCls.toCss(attrs)
    return self

  def style_per_id(self, html_id, attrs):
    """
    Description:
    -----------
    Add a new CSS Class in the page header.

    Usage:
    -----

    Related Pages:

      https://www.w3schools.com/html/html_css.asp

    Attributes:
    ----------
    :param html_id: String. The HTML object ID.
    :param attrs: Dictionary. The CSS attributes as a dictionary.
    """
    self._cssObj.cssStyles["#%s" % html_id] = CssStyle.CssCls.toCss(attrs)
    return self

  def style_per_tag(self, html_tag, attrs):
    """
    Description:
    -----------
    Add a new CSS Class in the page header.

    Usage:
    -----

    Related Pages:

      https://www.w3schools.com/html/html_css.asp

    Attributes:
    ----------
    :param html_tag: String. The HTML object tag.
    :param attrs: Dictionary. The CSS attributes as a dictionary.
    """
    self._cssObj.cssStyles[html_tag] = CssStyle.CssCls.toCss(attrs)
    return self

  def new_class(self, clss_nam, attrs):
    """
    Description:
    -----------
    Add a new CSS Class in the page header.

    Usage:
    -----

    Related Pages:

      https://www.w3schools.com/html/html_css.asp

    Attributes:
    ----------
    :param clss_nam: String. The CSS class name as a string.
    :param attrs: Dictionary. The CSS attributes as a dictionary.
    """
    self._cssObj.cssStyles[".%s" % clss_nam] = CssStyle.CssCls.toCss(attrs)
    return self
