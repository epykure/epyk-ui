
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

    :return:
    """
    return self.get(True)

  @expanded.setter
  def expanded(self, boool):
    self.set(boool)

  @property
  def icon_expanded(self):
    """

    :return:
    """
    return self.get("fas fa-caret-down")

  @icon_expanded.setter
  def icon_expanded(self, icon):
    self.set(icon)

  @property
  def icon_closed(self):
    """

    :return:
    """
    return self.get("fas fa-caret-up")

  @icon_closed.setter
  def icon_closed(self, icon):
    self.set(icon)
