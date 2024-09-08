from epyk.core.html.options import Options


class OptionsQuillModHistory(Options):
    ...


class OptionsQuillModules(Options):

    @property
    def syntax(self) -> bool:
        """Whether to instantiate the editor to read-only mode.
        """
        return self._config_get(True)

    @syntax.setter
    def syntax(self, flag: bool):
        self._config(flag)


class OptionsQuill(Options):
    component_properties = ("theme", )

    @property
    def bounds(self) -> str:
        """DOM Element or a CSS selector for a DOM Element, within which the editor's ui elements (i.e. tooltips, etc.)
         should be confined. Currently, it only considers left and right boundaries.
        `quilljs <https://quilljs.com/docs/configuration>`_
        """
        return self._config_get("document.body")

    @bounds.setter
    def bounds(self, value: str):
        self._config(value)

    @property
    def debug(self) -> str:
        """Shortcut for debug. Note debug is a static method and will affect other instances of Quill editors on the
        page. Only warning and error messages are enabled by default.
        `quilljs <https://quilljs.com/docs/configuration>`_
        """
        return self._config_get("snow")

    @debug.setter
    def debug(self, value: str):
        self._config(value)

    @property
    def modules(self) -> OptionsQuillModules:
        """
        `quilljs <https://quilljs.com/docs/configuration>`_
        """
        return OptionsQuillModules(self, 'modules')

    @property
    def placeholder(self) -> str:
        """Placeholder text to show when editor is empty.
        `quilljs <https://quilljs.com/docs/configuration#placeholder>`_
        """
        return self._config_get(None)

    @placeholder.setter
    def placeholder(self, value: str):
        self._config(value)

    @property
    def readOnly(self) -> bool:
        """Whether to instantiate the editor to read-only mode.
        """
        return self._config_get(False)

    @readOnly.setter
    def readOnly(self, flag: bool):
        self._config(flag)

    @property
    def theme(self):
        """Name of theme to use. The builtin options are "bubble" or "snow". An invalid or falsy value will load a
        default minimal theme. Note the theme's specific stylesheet still needs to be included manually.
        `quilljs <https://quilljs.com/docs/customization/themes>`_
        """
        return self._config_get("snow")

    @theme.setter
    def theme(self, value: str):
        self._config(value)

    @property
    def toolbar(self):
        """Placeholder text to show when editor is empty.

        """
        return self._config_get(None)

    @toolbar.setter
    def toolbar(self, values):
        self._config(values)
