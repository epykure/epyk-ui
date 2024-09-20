from epyk.core.html.options import Options


class OptionsQuillHistory(Options):

    @property
    def delay(self) -> bool:
        """Changes occurring within the delay number of milliseconds are merged into a single change. """
        return self._config_get(1000)

    @delay.setter
    def delay(self, num: int):
        self._config(num)

    @property
    def maxStack(self) -> bool:
        """CMaximum size of the history's undo/redo stack. Merged changes with the delay option counts as a singular
        change."""
        return self._config_get(100)

    @maxStack.setter
    def maxStack(self, num: int):
        self._config(num)

    @property
    def userOnly(self) -> bool:
        """By default all changes, whether originating from user input or programmatically through the API, are
        treated the same and change be undone or redone by the history module. If userOnly is set to true, only
        user changes will be undone or redone."""
        return self._config_get(False)

    @userOnly.setter
    def userOnly(self, flag: bool):
        self._config(flag)


class OptionsQuillModules(Options):

    @property
    def syntax(self) -> bool:
        """Whether to instantiate the editor to read-only mode.
        """
        return self._config_get(True)

    @syntax.setter
    def syntax(self, flag: bool):
        self._config(flag)

    @property
    def history(self) -> OptionsQuillHistory:
        """The History module is responsible for handling undo and redo for Quill. It can be configured with the
        following options:
        `quilljs <https://quilljs.com/docs/modules/history>`_
        """
        return self._config_sub_data("modules", OptionsQuillHistory)

    @property
    def toolbar(self) -> bool:
        """Whether to instantiate the editor to read-only mode.
        """
        return self._config_get()

    @toolbar.setter
    def toolbar(self, html_code: str):
        self._config(html_code)


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
        return self._config_sub_data("modules", OptionsQuillModules)

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
