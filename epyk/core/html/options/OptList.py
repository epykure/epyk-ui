
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


class OptionsItems(Options):

  @property
  def style(self):
    """
    Description:
    ------------
    Item CSS Style
    """
    return self._config_get({})

  @style.setter
  def style(self, attrs):
    self._config(attrs)

  @property
  def badge(self):
    """
    Description:
    ------------
    Get the badge style
    """
    return self._config_get({})

  @badge.setter
  def badge(self, attrs):
    self._config(attrs)

  @property
  def delete(self):
    """
    Description:
    ------------
    Add a delete icon
    """
    return self._config_get(False)

  @delete.setter
  def delete(self, attrs):
    self._config(attrs)

  @property
  def checked(self):
    """
    Description:
    ------------
    Check default value for radio and check lists
    """
    return self._config_get(False)

  @checked.setter
  def checked(self, attrs):
    self._config(attrs)

  @property
  def icon(self):
    """
    Description:
    ------------
    Check default value for radio and check lists
    """
    return self._config_get("")

  @icon.setter
  def icon(self, attrs):
    self._config(attrs)


class OptionsTagItems(Options):

  @property
  def visible(self):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param css: Dictionary. All the CSS attributes to add the any items
    """
    return self._config_get(False)

  @visible.setter
  def visible(self, attrs):
    self._config(attrs)

  @property
  def category_css(self):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param css: Dictionary. All the CSS attributes to add the any items
    """
    return self._config_get({})

  @category_css.setter
  def category_css(self, attrs):
    self._config(attrs)

  @property
  def value_css(self):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param css: Dictionary. All the CSS attributes to add the any items
    """
    return self._config_get({})

  @value_css.setter
  def value_css(self, attrs):
    self._config(attrs)

  @property
  def item_css(self):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param css: Dictionary. All the CSS attributes to add the any items
    """
    return self._config_get({})

  @item_css.setter
  def item_css(self, attrs):
    self._config(attrs)

  @property
  def category(self):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param css: Dictionary. All the CSS attributes to add the any items
    """
    return self._config_get({})

  @category.setter
  def category(self, attrs):
    self._config(attrs)

  @property
  def icon_css(self):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param css: Dictionary. All the CSS attributes to add the any items
    """
    return self._config_get({})

  @icon_css.setter
  def icon_css(self, attrs):
    self._config(attrs)
