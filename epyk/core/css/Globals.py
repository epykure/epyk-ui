"""

"""

from epyk.core.css.styles import CssStyle


class Overflow(object):
  def __init__(self, cssObj):
    self._cssObj = cssObj
    self._cssObj.cssStyles["::-webkit-scrollbar"] = "{ height: 10px; }"
    self._cssObj.cssStyles["::-webkit-scrollbar-track"] = "{ border-radius: 10px; -webkit-box-shadow: inset 0 0 2px rgba(0,0,0,0.5); }"

  def thumb(self, style=None, css_hover=None, css_active=None):
    """

    :param style:
    :param css_hover:
    :param css_active:

    :return:
    """
    if style is not None:
      self._cssObj.cssStyles["::-webkit-scrollbar-thumb"] = CssStyle.CssCls.toCss(style)
    if css_hover is not None:
      self._cssObj.cssStyles["::-webkit-scrollbar-thumb:hover"] = CssStyle.CssCls.toCss(css_hover)
    if css_active is not None:
      self._cssObj.cssStyles["::-webkit-scrollbar-thumb:active"] = CssStyle.CssCls.toCss(css_active)

  def horizontal(self):
    """

    :return:
    """

  def vertical(self):
    """

    :return:
    """


class CssGlobal(object):

  def __init__(self, cssObj):
    self._cssObj = cssObj

  @property
  def overflow(self):
    return Overflow(self._cssObj)
