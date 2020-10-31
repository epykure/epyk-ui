
import sys

from epyk.core.css import Properties
from epyk.core.css import Defaults_css


class Attrs(Properties.CssMixin):
  def __init__(self, htmlObj):
    self.htmlObj, self.attrs = self, {}
    self.orign_htmlObj = htmlObj
    self._report = htmlObj._report

  def css(self, attrs):
    """
    Description:
    ------------
    Set multiple CSS attributes to the HTML component

    Attributes:
    ----------
    :param attrs: Dictionary. optional. The attributes to be added
    """
    if not isinstance(attrs, dict):
      return self.attrs.get(attrs)

    for k, v in attrs.items():
      self.attrs[k] = v

  def remove(self, attr=None, set_none=False):
    """
    Description:
    ------------
    Remove a CSS attribute to the HTML component.

    This function will either remove it if it is part of the existing CSS attribute or set it to auto in case it is
    coming from a CSS class.

    Attributes:
    ----------
    :param attr: String. Optional. The attribute to be removed
    :param set_none:Boolean. Optinal. Set the CSS attribute value to None on the CSS
    """
    key = attr or sys._getframe().f_back.f_code.co_name.replace("_", "-")
    if set_none:
      self.attrs[key] = "none"
      self.orign_htmlObj.attr['css'][key] = "none"
    else:
      if key in self.attrs:
        del self.attrs[key]
        if key in self.orign_htmlObj.attr['css']:
          del self.orign_htmlObj.attr['css'][key]
      else:
        self.attrs[key] = "unset"
        self.orign_htmlObj.attr['css'][key] = "auto"

  def __str__(self):
    """

    """
    css_tag = []
    for k, v in self.attrs.items():
      css_tag.append("%s:%s" % (k, v))
    return ";".join(css_tag)


class Commons(Attrs):

  def __init__(self, htmlObj):
    super(Commons, self).__init__(htmlObj)
    self.font_size = 'inherit'
    self.font_family = 'inherit'
    self.box_sizing = 'border-box'


class Empty(Attrs):

  def __init__(self, htmlObj):
    super(Empty, self).__init__(htmlObj)


class Body(Attrs):

  def __init__(self, htmlObj):
    super(Body, self).__init__(htmlObj)
    self.font_size = Defaults_css.font()
    self.font_family = Defaults_css.Font.family
    self.margin = 0


