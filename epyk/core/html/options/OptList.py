
from epyk.core.html.options import Options


class OptionsLi(object):
  def __init__(self, src, options):
    self.src = src
    self._li_css = options.get("li_css", {})
    self.li_class = options.get("li_class", [])

  @property
  def li_css(self):
    """
    """
    return self._li_css

  @li_css.setter
  def li_css(self, css):
    self._li_css = css

  @property
  def li_class(self):
    """
    """
    return self._li_class

  @li_class.setter
  def li_class(self, cls_names):
    self._li_class = cls_names


class OptionsTagItems(Options):

  @property
  def item_css(self):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param css: Dictionary. All the CSS attributes to add the any items
    """
    dflt_css = {"padding": '0 2px', 'border': '1px solid black', 'border-radius': '5px', 'margin': '2px'}
    return self._config_get(dflt_css)

  @item_css.setter
  def item_css(self, attrs):
    self._config(attrs)
