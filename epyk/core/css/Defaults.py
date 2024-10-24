#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Optional, Union
from epyk.core.py import primitives
from epyk.core.html import Defaults as defaultHtml
from epyk.conf.global_settings import ICONS_FAMILY


REG_EXP_SECTOR = r"([A-Za-z0-9~_\:\\+.,\(\)\>\<\@\#\+\*\-\ \=\"'\[\]]*){([#A-Za-z0-9\%\ \,\-\\\"'\:\*\;\+\!\(\)\-\.]*) }"
""" Regular expression to parse the CSS files and extract the definition """


class Font:
    _size, header_size, unit = 12, 14, "px"
    _family = "Arial"

    def __init__(self, page: primitives.PageModel):
        self.page = page

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, value: int):
        self.page.body.style.css.font_family = value
        self._family = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value: int):
        self.page.body.style.css.font_size = value
        self.header_size = value + 2
        self._size = value

    def normal(self, step: int = 0, unit: str = None) -> str:
        """Font text format.

        :param step: Optional. The value to be added to the default font size
        :param unit: Optional. The unit code. default px
        """
        return "%s%s" % (self._size + step, unit or self.unit)

    def header(self, step: int = 0, unit: str = None) -> str:
        """Font header format.

        :param step: Optional. The value to be added to the default font size
        :param unit: Optional. The unit code. default px
        """
        return "%s%s" % (self.header_size + step, unit or self.unit)

    def vars(self) -> dict:
        return {"font-family": self.family, "font-size": self.normal(), "header-size": self.header()}


class Icon:
    small, normal, big, unit = 10, 15, 25, 'px'

    @property
    def family(self):
        return ICONS_FAMILY

    def small_size(self, step: int = 0, unit: str = None) -> str:
        """Icon small format.

        :param step: Optional. The value to be added to the default font size
        :param unit: Optional. The unit code. default px
        """
        return "%s%s" % (self.small + step, unit or self.unit)

    def normal_size(self, step: int = 0, unit: str = None) -> str:
        """Icon normal format.

        :param step: Optional. The value to be added to the default font size
        :param unit: Optional. The unit code. default px
        """
        return "%s%s" % (self.normal + step, unit or self.unit)

    def big_size(self, step: int = 0, unit: str = None) -> str:
        """Icon big format.

        :param step: Optional. The value to be added to the default font size
        :param unit: Optional. The unit code. default px
        """
        return "%s%s" % (self.big + step, unit or self.unit)

    def vars(self) -> dict:
        return {"icon-family": self.family, "icon-small": self.small_size(), "icon-size": self.normal_size(),
                "icon-large": self.big_size()}


def header(step: int = 0) -> str:
    """

    :param step: Optional. The value to be added to the default font size.
    """
    return "%s%s" % (Font.header_size + step, Font.unit)


def inline(css_attrs: dict, important: bool = False) -> str:
    """Convert a CSS attributes dictionary to a online CSS Style to be added to the dom object.
    `w3schools <https://www.w3schools.com/css/css_howto.asp>`_

    Usage::
      inline({"color": "red"})

    :param css_attrs: The CSS Attributes
    :param important: Optional. Set the attributes to important. Default False
    """
    if important:
        return ";".join(["%s: %s !IMPORTANT" % (k, v) for k, v in css_attrs.items()])

    return ";".join(["%s: %s" % (k, v) for k, v in css_attrs.items()])


def px_to_em(value: float, with_unit: bool = True) -> Union[str, float]:
    """Convert the pixel value to em.
    `w3schools <https://www.w3schools.com/cssref/css_pxtoemconversion.asp>`_

    :param value: A pixel value
    :param with_unit: Optional. To define the return format
    """
    em_value = value / 16
    if with_unit:
        return "%sem" % em_value

    return em_value


def em_to_px(value: float, with_unit: bool = True) -> Union[str, float]:
    """Convert an em value in pixel.
    `w3schools <https://www.w3schools.com/cssref/css_pxtoemconversion.asp>`_

    :param value: The em value
    :param with_unit: Optional. To define the return format
    """
    px_value = value * 16
    if with_unit:
        return "%spx" % px_value

    return px_value


# Global configuration for the entire framework
# Changing those variables will impact all reports generated
# Theme global settings
THEME = "default"
DARK_MODE = False

# Icon global settings
DEFAULT_STYLE = "no_border"
""" """
DEFINED_FAMILIES = ('office-ui-fabric-core', 'material-design-icons', 'font-awesome', 'bootstrap-icons')
""" """
ICON_MAPPINGS = {
    "font-awesome": {
        "danger": "fas fa-stop-circle",
        "error": 'fas fa-times-circle',
        "success": 'fas fa-check-circle',
        "warning": "fas fa-exclamation-triangle",
        "search": "fas fa-search",
        "times": "fas fa-times",
        "close": "fas fa-times-circle",
        "upload": "fas fa-upload",
        "word": "fa-file-word",
        "csv": "fas fa-file-csv",
        "code": "far fa-file-code",
        "download": "fas fa-file-download",
        "info": "fas fa-question-circle",
        "edit": 'far fa-edit',
        "clock": "fas fa-clock",
        "lock_open": "fas fa-lock-open",
        "compress": "fas fa-compress",
        "calendar": "far fa-calendar-alt",
        "calendar-week": "fas fa-calendar-week",
        "spin": "fas fa-spinner",
        "next": "fas fa-caret-right",
        "previous": "fas fa-caret-left",
        "play": "fas fa-play",
        "stop": "fas fa-stop",
        "zoom_out": "fas fa-search-minus",
        "zoom_in": "fas fa-search-plus",
        "save": "fas fa-save",
        "refresh": "fas fa-sync-alt",
        "pdf": "far fa-file-pdf",
        "square_plus": "fas fa-plus-square",
        "square_minus": "far fa-minus-square",
        "plus": "fas fa-plus",
        "minus": "fas fa-minus",
        "excel": 'far fa-file-excel',
        "delete": "far fa-trash-alt",
        "zoom": "fas fa-search-plus",
        "capture": "far fa-clipboard",
        "remove": "fas fa-times-circle",
        "clear": "fas fa-eraser",
        "table": "fas fa-table",
        "check": "fas fa-check",
        "wrench": "fas fa-wrench",
        "rss": "fas fa-rss-square",
        "facebook": "fab fa-facebook-f",
        "messenger": "fab fa-facebook-messenger",
        "twitter": "fab fa-twitter",
        "twitch": "fab fa-twitch",
        "instagram": "fab fa-instagram-square",
        "linkedIn": "fab fa-linkedin-in",
        "youtube": 'fab fa-youtube',
        "github": 'fab fa-github',
        "python": 'fab fa-python',
        "stackoverflow": 'fab fa-stack-overflow',
        "envelope": 'far fa-envelope',
        "question": 'fas fa-question-circle',
        "google_plus": 'fab fa-google-plus',
        "circle": 'fas fa-circle',
        'user': 'fas fa-user-tie',
        'chevron_up': 'fas fa-chevron-up',
        'chevron_down': 'fas fa-chevron-down',
        'folder_open': "fas fa-folder-open",
        'folder_close': "fas fa-folder",
        'show': "fas fa-eye",
        'hide': "far fa-eye-slash",
        'star': "fa fa-star",
        'arrow_right': "fas fa-arrow-alt-circle-right",
        'arrow_left': "fas fa-arrow-alt-circle-left",
        'face_grin_hearts': "far fa-grin-hearts",
        'face_smile': "far fa-smile",
        'face_meh': "far fa-meh",
        'face_frown_open': "far fa-frown-open",
        'face_frown': "far fa-frown",
        'loader': "fas fa-spinner fa-spin",
    }
}

WEB_LIBS = "std"


def get_icon(alias: Optional[str], family: str = None) -> dict:
    """Return the icon from an alias from any family.
    This will allow the integration of multiple icon libraries.

    :param alias: The icon reference in the components
    :param family: Optional. The defined family (if different from the page icon family)
    """
    icon = ICON_MAPPINGS[family or ICONS_FAMILY].get(alias, alias)
    if icon is None:
        return {"icon": ICON_MAPPINGS['font-awesome'].get(alias, alias), "icon_family": 'font-awesome'}

    return {"icon": icon, "icon_family": ICONS_FAMILY}


ICON_FAMILY = ICONS_FAMILY
""" Deprecated family definition - to use ICONS_FAMILY from global_settings instead """
# Default CSS Styles
BODY_CONTAINER = None  # The body CSS dictionary
BODY_STYLE = None
BACKGROUND = ('greys', 0)
MEDIA = 600
MENU_ICON_SIZE = -1

# Default CSS
CSS_EXCEPTIONS = True
CSS_EXCEPTIONS_FORMAT = "CSS - %s - invalid %s"


class GlobalStyle:

    def __init__(self, page: primitives.PageModel):
        self.page = page
        self._font = None
        self._icon = None
        self._table = None
        self._line_height = max(defaultHtml.LINE_HEIGHT, self.font.size)

    @property
    def line_height(self) -> int:
        return self._line_height

    @line_height.setter
    def line_height(self, value: int):
        self._line_height = value

    @property
    def font(self) -> Font:
        """Set the page font"""
        if self._font is None:
            self._font = Font(self.page)
        return self._font

    @property
    def icon(self) -> Icon:
        """ """
        if self._icon is None:
            self._icon = Icon()
        return self._icon

    @property
    def table(self):
        """ """
        if self._table is None:
            class GlobalTable:
                header_background = self.page.theme.colors[0] if self.page.theme.dark else self.page.theme.colors[-1]
                header_color = self.page.theme.white  # if self.page.theme.dark else self.page.theme.white
                header_border = '1px solid %s' % self.page.theme.black if self.page.theme.dark else self.page.theme.white
                cell_border_bottom = "1px solid %s" % self.page.theme.colors[4]
                cell_border_right = None
                sorter_arrow_selected = self.page.theme.colors[-3]
                sorter_arrow = self.page.theme.black if self.page.theme.dark else self.page.theme.white

            self._table = GlobalTable()
        return self._table

    def vars(self) -> dict:
        results = {"line-height": "%spx" % self._line_height}
        results.update(self.font.vars())
        results.update(self.icon.vars())
        return results
