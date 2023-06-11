import re
from typing import Optional, Any
from epyk.core.css import Defaults_css

_ICON_MAPPINGS = {
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
    }
}


class IconModel:

    def __init__(self, page):
        self.page = page
        self._family, self._category = Defaults_css.ICON_FAMILY, "CLASS"
        self.__icons = {}

    @property
    def category(self) -> str:
        """ Set the category to define the icon for an object. This is used by the set method """
        return self._category

    @category.setter
    def category(self, name: str):
        name = name.upper()
        if name not in ("CLASS", "VALUE"):
            raise ValueError("Only Class and Value are possible for the icon's definition type!")

        self._category = name

    @property
    def family(self) -> str:
        """
        Set the icon family to be used in the page.

        This will have to be defined first before loading any components.
        """
        return self._family

    @family.setter
    def family(self, fam: str):
        self._family = fam

    def other(self, package: str = None, icons_map: dict = None):
        """
        Set the default icon to another bespoke package.

        This will not rely anymore to fontawesome by default.
        By using this it is important to align _ICON_MAPPINGS variables to point to the updated
        icon classes

        Usage::

          page = pk.Page()
          page.icons.other("bootstrap-icons", {"edit": 'bi bi-2-circle'})
          page.ui.icons.edit("test")

        :param package: Optional. The package alias
        :param icons_map: Optional. The internal icon mapping
        """
        global _ICON_MAPPINGS

        self._family = 'other'
        if package is not None:
            self.page.imports.add(package)
            if package in _ICON_MAPPINGS:
                self._family = package
        if icons_map is not None:
            _ICON_MAPPINGS[self._family] = icons_map

    def get(self, alias: Optional[str], family: str = None, options: dict = None) -> dict:
        """
        Return the icon properties based on the

        :param alias: The full icon definition or an alias from the internal mapping
        :param family: The icon family
        :param options: The common component options
        :return: The icon properties
        """
        if options is not None:
            family = options.get("icon_family")
        family = family or self.family
        icon = _ICON_MAPPINGS.get(family, {}).get(alias, alias)
        if icon is None:
            return {"icon": _ICON_MAPPINGS[self.family].get(alias, alias), "icon_family": self.family}

        return {"icon": icon, "icon_family": family}

    def add(self, alias: str, imports: dict, set_default: bool = True):
        """
        Register another icons library to the framework.

        :param alias: The full icon definition or an alias from the internal mapping
        :param imports: The different external modules to add to the Import (css and Js)
        :param set_default: Change the default family
        """
        self.page.ext_packages.update(imports)
        self.page.imports.reload()
        _ICON_MAPPINGS[alias] = imports
        if set_default:
            self._family = alias

    def set(self, alias: Optional[str], component: Any, family: str = None, options: dict = None):
        """
        Decorate the component with the corresponding type.
        Some icon frameworks use CSS Classes some other will use value instead.

        By default the framework will use font awesome and then rely on class definition.
        """
        if options is not None:
            family = options.get("icon_family")
        family = family or self.family
        if self.category == "VALUE":
            component.attr["class"].add(_ICON_MAPPINGS[family].get(alias, alias))
        else:
            component._vals = _ICON_MAPPINGS[family].get(alias, alias)

    def from_sass(self, file_path: str):
        """
        Load the SASS file to set the icons' definition.

        Usage::

            page = pk.Page()

        :param file_path: The full file path
        """
        regex = re.compile("\$(.*): (.*);")
        with open(file_path) as fp:
            content = fp.read()
            for m in regex.findall(content):
                tag, value = m
                self.__icons[tag] = value
        self._family = "SCSS"
        _ICON_MAPPINGS[self._family] = self.__icons
