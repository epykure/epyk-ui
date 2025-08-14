#!/usr/bin/python
# -*- coding: utf-8 -*-


from epyk.core.html.options import Options


class OptionsImage(Options):
    component_properties = ('color',)

    @property
    def background(self):
        """
    """
        return self._config_get(None)

    @background.setter
    def background(self, color):
        self._config(color)

    @property
    def color(self):
        """
    """
        return self._config_get(self.page.theme.colors[-1])

    @color.setter
    def color(self, color: str):
        self._config(color)


class OptionsIcon(Options):

    @property
    def kind(self) -> str:
        """Set CSS class for the icon"""
        return self._config_get(None)

    @kind.setter
    def kind(self, value: str):
        self._config(value)
        self.component.classList.add("html-icon-%s" % value)
        if self.plain:
            self.component.classList.add("html-icon-plain-%s" % value)
        if self.outline:
            self.component.classList.add("html-icon-outline-%s" % value)

    @property
    def plain(self) -> bool:
        """Set plain CSS class for the icon"""
        return self._config_get(False)

    @plain.setter
    def plain(self, flag: bool):
        self._config(flag)

    @property
    def outline(self) -> bool:
        """Set outline CSS class for the icon"""
        return self._config_get(False)

    @outline.setter
    def outline(self, flag: bool):
        self._config(flag)

    @property
    def icon_family(self) -> str:
        """Set the family for the report and update the requirements"""
        return self._config_get(self.page.icons.family)

    @icon_family.setter
    def icon_family(self, value: str):
        self._config(value)
        if value == 'office-ui-fabric-core':
            self.component.classList.add("ms-Icon")
        elif value == 'material-design-icons':
            self.component.classList.add("material-icons")
        elif value == 'bootstrap-icons':
            self.component.classList.add("bi")
            from epyk.fwk.bs import PkgImports
            if self.page.ext_packages is None:
                self.page.ext_packages = {}
            self.page.ext_packages.update(PkgImports.BOOTSTRAP)
            self.page.cssImport.add("bootstrap-icons")
