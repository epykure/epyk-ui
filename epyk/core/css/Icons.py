import re
from typing import Optional, Any
from . import Defaults as Defaults_css


class IconModel:

    def __init__(self, page):
        self.page = page
        self._family, self._category = Defaults_css.ICON_FAMILY, "CLASS"
        self.__icons = {}

    @property
    def category(self) -> str:
        """Set the category to define the icon for an object. This is used by the set method"""
        return self._category

    @category.setter
    def category(self, name: str):
        name = name.upper()
        if name not in ("CLASS", "VALUE"):
            raise ValueError("Only Class and Value are possible for the icon's definition type!")

        self._category = name

    @property
    def family(self) -> str:
        """Set the icon family to be used in the page.

        This will have to be defined first before loading any components.
        """
        return self._family

    @family.setter
    def family(self, fam: str):
        self._family = fam

    def other(self, package: str = None, icons_map: dict = None):
        """Set the default icon to another bespoke package.

        This will not rely anymore to fontawesome by default.
        By using this it is important to align _ICON_MAPPINGS variables to point to the updated icon classes

        Usage::

          page = pk.Page()
          page.icons.other("bootstrap-icons", {"edit": 'bi bi-2-circle'})
          page.ui.icons.edit("test")

        :param package: Optional. The package alias
        :param icons_map: Optional. The internal icon mapping
        """

        self._family = 'other'
        if package is not None:
            self.page.imports.add(package)
            if package in Defaults_css.ICON_MAPPINGS:
                self._family = package
        if icons_map is not None:
            Defaults_css.ICON_MAPPINGS[self._family] = icons_map

    def get(self, alias: Optional[str], family: str = None, options: dict = None) -> dict:
        """Return the icon properties based on the internal mapping

        :param alias: The full icon definition or an alias from the internal mapping
        :param family: Optional. The icon family
        :param options: Optional. The common component options
        :return: The icon properties
        """
        if options is not None:
            family = options.get("icon_family")
        family = family or self.family
        icon = Defaults_css.ICON_MAPPINGS.get(family, {}).get(alias, alias)
        if icon is None:
            return {"icon": Defaults_css.ICON_MAPPINGS[self.family].get(alias, alias), "icon_family": self.family}

        return {"icon": icon, "icon_family": family}

    def add(self, alias: str, imports: dict, set_default: bool = True):
        """Register another icons library to the framework.

        :param alias: The full icon definition or an alias from the internal mapping
        :param imports: The different external modules to add to the Import (css and Js)
        :param set_default: Optional. Change the default family
        """
        self.page.ext_packages.update(imports)
        self.page.imports.reload()
        Defaults_css.ICON_MAPPINGS[alias] = imports
        if set_default:
            self._family = alias

    def set(self, alias: Optional[str], component: Any, family: str = None, options: dict = None):
        """Decorate the component with the corresponding type.
        Some icon frameworks use CSS Classes some other will use value instead.

        By default, the framework will use font awesome and then rely on class definition.
        """
        if options is not None:
            family = options.get("icon_family")
        family = family or self.family
        if self.category == "VALUE":
            component.attr["class"].add(Defaults_css.ICON_MAPPINGS[family].get(alias, alias))
        else:
            component._vals = Defaults_css.ICON_MAPPINGS[family].get(alias, alias)

    def from_sass(self, file_path: str):
        """Load the SASS file to set the icons' definition.

        Usage::

            page = pk.Page()

        :param file_path: The full file path
        """
        regex = re.compile("\$(.*): (.*);")
        with open(file_path) as fp:
            content = fp.read()
            for m in regex.findall(content):
                tag, value = m
                self.__icons[tag.strip()] = value.strip()
        self._family = "SCSS"
        Defaults_css.ICON_MAPPINGS[self._family] = self.__icons
