
from epyk.core.html.options import Options


class OptionsPanelPoints(object):

  def __init__(self, src, options):
    self.src = src
    self.__background_color = options.get("background-color", src.theme.success[1])
    self.__div_css = options.get("div_css", {})
    self.__selected = options.get("selected", 0)

  @property
  def background_color(self):
    return self.__background_color

  @background_color.setter
  def background_color(self, val):
    self.__background_color = val

  @property
  def div_css(self):
    return self.__div_css

  @div_css.setter
  def div_css(self, css):
    self.__div_css = css

  @property
  def selected(self):
    return self.__selected

  @selected.setter
  def selected(self, num):
    self.__selected = num


class OptionPanelSliding(Options):

  @property
  def expanded(self):
    """
    Description:
    ------------

    :return:
    """
    return self.get(True)

  @expanded.setter
  def expanded(self, boool):
    self.set(boool)

  @property
  def icon_expanded(self):
    """
    Description:
    ------------

    :return:
    """
    return self.get("fas fa-caret-down")

  @icon_expanded.setter
  def icon_expanded(self, icon):
    self.set(icon)

  @property
  def icon_closed(self):
    """
    Description:
    ------------

    :return:
    """
    return self.get("fas fa-caret-up")

  @icon_closed.setter
  def icon_closed(self, icon):
    self.set(icon)


class OptionPanelTabs(Options):

  @property
  def css_tab(self):
    """
    Description:
    ------------
    The default CSS style for the tabs.
    This must be changed before adding components
    """
    dflt = {'display': 'inline-block', 'text-align': 'center', 'cursor': 'pointer', 'margin': '0 2px 5px 0', "border-bottom": "1px solid white"}
    return self.get(dflt)

  @css_tab.setter
  def css_tab(self, attrs):
    self.set(attrs)

  @property
  def css_tab_clicked(self):
    """
    Description:
    ------------
    The default CSS style for the clicked tab.
    This must be changed before adding components
    """
    dflt = {"border-bottom": "1px solid %s" % self._report.theme.success[1]}
    return self.get(dflt)

  @css_tab_clicked.setter
  def css_tab_clicked(self, attrs):
    self.set(attrs)

  def tab_style(self, name, css_style=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param name:
    :param css_style:
    """
    if not 'tab_style' in self._attrs:
      self._attrs['tab_style'] = {}
    css = dict(self.css_tab)
    if css_style is not None:
      css.update(css_style)
      self._attrs['tab_style'][name] = css
    return self._attrs['tab_style'].get(name, css)

  def tab_clicked_style(self, name, css_style=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param name:
    :param css_style:
    """
    if not 'tab_style_clicked' in self._attrs:
      self._attrs['tab_style_clicked'] = {}
    css = dict(self.css_tab_clicked)
    if css_style is not None:
      css.update(css_style)
      self._attrs['tab_style_clicked'][name] = css
    return self._attrs['tab_style_clicked'].get(name, css)

  def tab_not_clicked_style(self, name=None, css_style=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param name:
    :param css_style:
    """
    tab_clicked_style = self.tab_clicked_style(name)
    tab_style = self.tab_style(name)
    tab_not_clicked = {k: tab_style[k] if k in tab_style else 'none' for k, v in tab_clicked_style.items()}
    if css_style is not None:
     tab_not_clicked.update(css_style)
    return tab_not_clicked


class OptionPanelTable(Options):

  @property
  def header(self):
    """
    Description:
    ------------
    """
    return self.get(True)

  @header.setter
  def header(self, bool):
    self.set(bool)


class OptionsDiv(Options):

  @property
  def inline(self):
    """
    Description:
    ------------
    """
    return self.get(False)

  @inline.setter
  def inline(self, bool):
    self.set(bool)
