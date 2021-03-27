from . import Theme
from . import ThemeDark as darks
from . import ThemeRed as reds
from . import ThemeGreen as greens
from . import ThemeBlue as blues


DIV_STYLE = '<div style="display:block;background-color:%s;width:20px;height:18px;margin-top:3px !IMPORTANT;border:1px solid black;margin:auto;vertical-align:middle" title="%s">&nbsp;</div>'

REGISTERED_THEMES = [
  {"value": 'Theme.ThemeDefault', 'name': '', 'content': DIV_STYLE % ('#1b5e20', "Default")},
  {"value": 'ThemeBlue.Blue', 'name': '', 'content': DIV_STYLE % ('#0d47a1', "Blue")},
  {"value": 'ThemeBlue.BlueGrey', 'name': '', 'content': DIV_STYLE % ('#263238', "Grey blue")},
  {"value": 'ThemeBlue.LightBlue', 'name': '', 'content': DIV_STYLE % ('#01579B', "Light blue")},
  {"value": 'ThemeDark.Dark', 'name': '', 'content': DIV_STYLE % ('#eceff1', "Dark")},
  {"value": 'ThemeDark.Grey', 'name': '', 'content': DIV_STYLE % ('#eceff1', "Grey")},
  {"value": 'ThemeGreen.Green', 'name': '', 'content': DIV_STYLE % ('#1b5e20', "Green")},
  {"value": 'ThemeGreen.Teal', 'name': '', 'content': DIV_STYLE % ('#004D40', "Teal")},
  {"value": 'ThemeGreen.LightGreen', 'name': '', 'content': DIV_STYLE % ('#33691E', "Light green")},
  {"value": 'ThemeRed.Red', 'name': '', 'content': DIV_STYLE % ('#B71C1C', "Red")},
  {"value": 'ThemeRed.Pink', 'name': '', 'content': DIV_STYLE % ('#d598a3', "Pink")},
]


class RegisteredThemes:

  def __init__(self, page):
    self.page = page

  def default(self, index=5, step=1, ovr_attrs=None):
    """
    Description:
    ------------
    The default CSS Color theme.

    Attributes:
    ----------
    :param index: Integer. Optional. The base color index.
    :param step: Integer. Optional. The move step number.
    :param ovr_attrs: Dictionary. Optional. The nested dictionary with color codes.
    """
    self.page.theme = Theme.ThemeDefault(ovr_attrs=ovr_attrs, index=index, step=step)

  def blue(self, index=5, step=1, ovr_attrs=None):
    """
    Description:
    ------------
    The Blue CSS Color theme.

    Attributes:
    ----------
    :param index: Integer. Optional. The base color index.
    :param step: Integer. Optional. The move step number.
    :param ovr_attrs: Dictionary. Optional. The nested dictionary with color codes.
    """
    self.page.theme = blues.Blue(ovr_attrs=ovr_attrs, index=index, step=step)

  def blue_grey(self, index=5, step=1, ovr_attrs=None):
    """
    Description:
    ------------
    The Blue Grey CSS Color theme.

    Attributes:
    ----------
    :param index: Integer. Optional. The base color index.
    :param step: Integer. Optional. The move step number.
    :param ovr_attrs: Dictionary. Optional. The nested dictionary with color codes.
    """
    self.page.theme = blues.BlueGrey(ovr_attrs=ovr_attrs, index=index, step=step)

  def blue_light(self, index=5, step=1, ovr_attrs=None):
    """
    Description:
    ------------
    The Light Blue CSS Color theme.

    Attributes:
    ----------
    :param index: Integer. Optional. The base color index.
    :param step: Integer. Optional. The move step number.
    :param ovr_attrs: Dictionary. Optional. The nested dictionary with color codes.
    """
    self.page.theme = blues.LightBlue(ovr_attrs=ovr_attrs, index=index, step=step)

  def green(self, index=5, step=1, ovr_attrs=None):
    """
    Description:
    ------------
    The Green CSS Color theme.

    Attributes:
    ----------
    :param index: Integer. Optional. The base color index.
    :param step: Integer. Optional. The move step number.
    :param ovr_attrs: Dictionary. Optional. The nested dictionary with color codes.
    """
    self.page.theme = greens.Green(ovr_attrs=ovr_attrs, index=index, step=step)

  def green_light(self, index=5, step=1, ovr_attrs=None):
    """
    Description:
    ------------
    The light Green CSS Color theme.

    Attributes:
    ----------
    :param index: Integer. Optional. The base color index.
    :param step: Integer. Optional. The move step number.
    :param ovr_attrs: Dictionary. Optional. The nested dictionary with color codes.
    """
    self.page.theme = greens.LightGreen(ovr_attrs=ovr_attrs, index=index, step=step)

  def teal(self, index=5, step=1, ovr_attrs=None):
    """
    Description:
    ------------
    The Teal CSS Color theme.

    Attributes:
    ----------
    :param index: Integer. Optional. The base color index.
    :param step: Integer. Optional. The move step number.
    :param ovr_attrs: Dictionary. Optional. The nested dictionary with color codes.
    """
    self.page.theme = greens.Teal(ovr_attrs=ovr_attrs, index=index, step=step)

  def grey(self, index=5, step=1, ovr_attrs=None):
    """
    Description:
    ------------
    The Grey CSS Color theme.

    Attributes:
    ----------
    :param index: Integer. Optional. The base color index.
    :param step: Integer. Optional. The move step number.
    :param ovr_attrs: Dictionary. Optional. The nested dictionary with color codes.
    """
    self.page.theme = darks.Grey(ovr_attrs=ovr_attrs, index=index, step=step)

  def dark(self, index=5, step=1, ovr_attrs=None):
    """
    Description:
    ------------
    The Dark CSS Color theme.

    Attributes:
    ----------
    :param index: Integer. Optional. The base color index.
    :param step: Integer. Optional. The move step number.
    :param ovr_attrs: Dictionary. Optional. The nested dictionary with color codes.
    """
    self.page.theme = darks.Dark(ovr_attrs=ovr_attrs, index=index, step=step)

  def pink(self, index=5, step=1, ovr_attrs=None):
    """
    Description:
    ------------
    The Pink CSS Color theme.

    Attributes:
    ----------
    :param index: Integer. Optional. The base color index.
    :param step: Integer. Optional. The move step number.
    :param ovr_attrs: Dictionary. Optional. The nested dictionary with color codes.
    """
    self.page.theme = reds.Pink(ovr_attrs=ovr_attrs, index=index, step=step)

  def red(self, index=5, step=1, ovr_attrs=None):
    """
    Description:
    ------------
    The Red CSS Color theme.

    Attributes:
    ----------
    :param index: Integer. Optional. The base color index.
    :param step: Integer. Optional. The move step number.
    :param ovr_attrs: Dictionary. Optional. The nested dictionary with color codes.
    """
    self.page.theme = reds.Red(ovr_attrs=ovr_attrs, index=index, step=step)
