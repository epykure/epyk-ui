from typing import List, Optional
import inspect

from .. import Defaults
from . import Theme
from . import ThemeDark as darks
from . import ThemeRed as reds
from . import ThemeGreen as greens
from . import ThemeBlue as blues

DIV_STYLE = '<div style="display:block;background-color:%s;width:20px;height:18px;margin-top:3px !IMPORTANT;border:1px solid black;margin:auto;vertical-align:middle" title="%s">&nbsp;</div>'

REGISTERED_THEMES = [
    {"value": 'Theme.ThemeDefault', 'name': '', 'content': DIV_STYLE % ('#607d8b', "Default"), "color": '#607d8b',
     "class": Theme.ThemeDefault},
    {"value": 'ThemeBlue.Blue', 'name': '', 'content': DIV_STYLE % ('#0d47a1', "Blue"), "color": '#0d47a1',
     "class": blues.Blue},
    {"value": 'ThemeBlue.BlueGrey', 'name': '', 'content': DIV_STYLE % ('#607d8b', "Grey blue"), "color": '#607d8b',
     "class": blues.BlueGrey},
    {"value": 'ThemeBlue.LightBlue', 'name': '', 'content': DIV_STYLE % ('#01579B', "Light blue"), "color": '#01579B',
     "class": blues.LightBlue},
    {"value": 'ThemeDark.Dark', 'name': '', 'content': DIV_STYLE % ('#eceff1', "Dark"), "color": '#eceff1',
     "class": darks.Dark},
    {"value": 'ThemeDark.Grey', 'name': '', 'content': DIV_STYLE % ('#eceff1', "Grey"), "color": '#eceff1',
     "class": darks.Grey},
    {"value": 'ThemeGreen.Green', 'name': '', 'content': DIV_STYLE % ('#1b5e20', "Green"), "color": '#1b5e20',
     "class": greens.Green},
    {"value": 'ThemeGreen.Teal', 'name': '', 'content': DIV_STYLE % ('#004D40', "Teal"), "color": '#004D40',
     "class": greens.Teal},
    {"value": 'ThemeGreen.LightGreen', 'name': '', 'content': DIV_STYLE % ('#33691E', "Light green"),
     "color": '#33691E', "class": greens.LightGreen},
    {"value": 'ThemeRed.Red', 'name': '', 'content': DIV_STYLE % ('#B71C1C', "Red"), "color": '#B71C1C',
     "class": reds.Red},
    {"value": 'ThemeRed.Pink', 'name': '', 'content': DIV_STYLE % ('#d598a3', "Pink"), "color": '#d598a3',
     "class": reds.Pink},
]


class RegisteredThemes:

    def __init__(self, page):
        self.page = page

    def default(self, index: int = 5, step: int = 1, ovr_attrs: dict = None, dark: bool = False) -> Theme.ThemeDefault:
        """The default CSS Color theme.

        :param index: Optional. The base color index
        :param step: Optional. The move step number
        :param ovr_attrs: Optional. The nested dictionary with color codes
        :param dark: Optional. Set the dark mode
        """
        self.page.theme = Theme.ThemeDefault(ovr_attrs=ovr_attrs, index=index, step=step)
        self.page.theme.dark = dark
        return self.page.theme

    def blue(self, index: int = 5, step: int = 1, ovr_attrs: dict = None, dark: bool = False) -> blues.Blue:
        """The Blue CSS Color theme.

        :param index: Optional. The base color index
        :param step: Optional. The move step number
        :param ovr_attrs: Optional. The nested dictionary with color codes
        :param dark: Optional. Set the dark mode
        """
        self.page.theme = blues.Blue(ovr_attrs=ovr_attrs, index=index, step=step)
        self.page.theme.dark = dark
        return self.page.theme

    def blue_grey(self, index: int = 5, step: int = 1, ovr_attrs: dict = None, dark: bool = False) -> blues.BlueGrey:
        """The Blue Grey CSS Color theme.

        :param index: Optional. The base color index
        :param step: Optional. The move step number
        :param ovr_attrs: Optional. The nested dictionary with color codes
        :param dark: Optional. Set the dark mode
        """
        self.page.theme = blues.BlueGrey(ovr_attrs=ovr_attrs, index=index, step=step)
        self.page.theme.dark = dark
        return self.page.theme

    def blue_light(self, index: int = 5, step: int = 1, ovr_attrs: dict = None, dark: bool = False) -> blues.LightBlue:
        """The Light Blue CSS Color theme.

        :param index: Optional. The base color index
        :param step: Optional. The move step number
        :param ovr_attrs: Optional. The nested dictionary with color codes
        :param dark: Optional. Set the dark mode
        """
        self.page.theme = blues.LightBlue(ovr_attrs=ovr_attrs, index=index, step=step)
        self.page.theme.dark = dark
        return self.page.theme

    def green(self, index: int = 5, step: int = 1, ovr_attrs: dict = None, dark: bool = False) -> greens.Green:
        """The Green CSS Color theme.

        :param index: Optional. The base color index
        :param step: Optional. The move step number
        :param ovr_attrs: Optional. The nested dictionary with color codes
        :param dark: Optional. Set the dark mode
        """
        self.page.theme = greens.Green(ovr_attrs=ovr_attrs, index=index, step=step)
        self.page.theme.dark = dark
        return self.page.theme

    def green_light(
            self, index: int = 5, step: int = 1, ovr_attrs: dict = None, dark: bool = False) -> greens.LightGreen:
        """The light Green CSS Color theme.

        :param index: Optional. The base color index
        :param step: Optional. The move step number
        :param ovr_attrs: Optional. The nested dictionary with color codes
        :param dark: Optional. Set the dark mode
        """
        self.page.theme = greens.LightGreen(ovr_attrs=ovr_attrs, index=index, step=step)
        self.page.theme.dark = dark
        return self.page.theme

    def teal(self, index: int = 5, step: int = 1, ovr_attrs: dict = None, dark: bool = False) -> greens.Teal:
        """The Teal CSS Color theme.

        :param index: Optional. The base color index
        :param step: Optional. The move step number
        :param ovr_attrs: Optional. The nested dictionary with color codes
        :param dark: Optional. Set the dark mode
        """
        self.page.theme = greens.Teal(ovr_attrs=ovr_attrs, index=index, step=step)
        self.page.theme.dark = dark
        return self.page.theme

    def grey(self, index: int = 5, step: int = 1, ovr_attrs: dict = None, dark: bool = False) -> darks.Grey:
        """The Grey CSS Color theme.

        :param index: Optional. The base color index
        :param step: Optional. The move step number
        :param ovr_attrs: Optional. The nested dictionary with color codes
        :param dark: Optional. Set the dark mode
        """
        self.page.theme = darks.Grey(ovr_attrs=ovr_attrs, index=index, step=step)
        self.page.theme.dark = dark
        return self.page.theme

    def dark(self, index: int = 5, step: int = 1, ovr_attrs: dict = None, dark: bool = False) -> darks.Dark:
        """The Dark CSS Color theme.

        :param index: Optional. The base color index
        :param step: Optional. The move step number
        :param ovr_attrs: Optional. The nested dictionary with color codes
        :param dark: Optional. Set the dark mode
        """
        self.page.theme = darks.Dark(ovr_attrs=ovr_attrs, index=index, step=step)
        self.page.theme.dark = dark
        return self.page.theme

    def pink(self, index: int = 5, step: int = 1, ovr_attrs: dict = None, dark: bool = False) -> reds.Pink:
        """The Pink CSS Color theme.

        :param index: Optional. The base color index
        :param step: Optional. The move step number
        :param ovr_attrs: Optional. The nested dictionary with color codes
        :param dark: Optional. Set the dark mode
        """
        self.page.theme = reds.Pink(ovr_attrs=ovr_attrs, index=index, step=step)
        self.page.theme.dark = dark
        return self.page.theme

    def red(self, index: int = 5, step: int = 1, ovr_attrs: dict = None, dark: bool = False) -> reds.Red:
        """The Red CSS Color theme.

        :param index: Optional. The base color index
        :param step: Optional. The move step number
        :param ovr_attrs: Optional. The nested dictionary with color codes
        :param dark: Optional. Set the dark mode
        """
        self.page.theme = reds.Red(ovr_attrs=ovr_attrs, index=index, step=step)
        self.page.theme.dark = dark
        return self.page.theme

    @property
    def names(self) -> List[str]:
        """ """
        n = []
        for t in REGISTERED_THEMES:
            if t["class"].name is not None:
                n.append(t["class"].name)
        return n

    def get(self, name: str):
        """

        :param name:
        :return:
        """
        for t in REGISTERED_THEMES:
            if t["class"].name == name:
                return t["class"]

    def set(self, name: str, index: int = 5, step: int = 1, ovr_attrs: dict = None, dark: bool = False):
        """

        :param name:
        :param index:
        :param step:
        :param ovr_attrs:
        :param dark:
        :return:
        """
        theme_cls = self.get(name)
        if theme_cls:
            self.page.theme = theme_cls(ovr_attrs=ovr_attrs, index=index, step=step)
            self.page.theme.dark = dark
        return self.page.theme


def add_themes(themes: List[Theme.Theme]):
    """Add bespoke themes to the internal reference.

    :param themes: A list of theme
    """
    global REGISTERED_THEMES

    for t in themes:
        if t.name is None:
            raise Exception("Loaded theme -%s- must have a name" % t.__name__)

        if inspect.isclass(t):
            themeObj = t()
            name = t.__name__
        else:
            themeObj = t
            name = t.__class__.__name__
        REGISTERED_THEMES.append({"value": name, "color": themeObj.colors[-1],
                                  "content": DIV_STYLE % (themeObj.colors[-1], t.name.capitalize()), 'class': t})


def set_theme(name: str, dark: bool = False, index: int = 5, step: int = 1):
    """Set a theme to be used as default theme by the framework when building reports.
    This will change the global settings for the CSS module.

    :param name: Theme's reference
    :param dark: Set dark mode
    :param index:
    :param step:
    """
    names = []
    for t in REGISTERED_THEMES:
        names.append(t["class"].name)
        if t["class"].name == name:
            break

    else:
        raise Exception("Cannot set this theme - %s, does not exist:  %s!" % (name, names))

    t["index"] = index
    t["step"] = step
    Defaults.THEME = name
    Defaults.DARK_MODE = dark


def get_themes() -> dict:
    """Get all registered themes"""
    ts = {}
    for t in REGISTERED_THEMES:
        name = t["class"].name.capitalize()
        ts[name] = dict(t)
    return ts


def get_theme() -> Optional[Theme.Theme]:
    """Get the current theme defined for the entire framework.
    This will be the theme used by default to generate all dashboards.
    """
    for r in REGISTERED_THEMES:
        if Defaults.THEME == r["class"].name:
            if callable(r["class"]):
                return r["class"]()

            return r["class"]

