"""

"""


class OptionsPanelPoints(object):
  def __init__(self, src, options):
    self.src = src
    self.__background_color = options.get("background-color", src.theme.success[1])
    self.__div_css = options.get("div_css", {})

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
