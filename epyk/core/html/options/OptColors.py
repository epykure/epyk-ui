
from typing import Union, Optional, List
from epyk.core.py import types as etypes
from epyk.core.html.options import Options
from epyk.core.js import JsUtils


class OptionsColoris(Options):

    @property
    def alpha(self):
        """Enable or disable alpha support."""
        return self._config_get(True)

    @alpha.setter
    def alpha(self, value: bool):
        self._config(value)

    @property
    def clearButton(self):
        """Show an optional clear button"""
        return self._config_get(False)

    @clearButton.setter
    def clearButton(self, value: bool):
        self._config(value)

    @property
    def closeLabel(self):
        """Set the label of the close button"""
        return self._config_get('Close')

    @closeLabel.setter
    def closeLabel(self, value: str):
        self._config(value)

    @property
    def defaultColor(self):
        """In inline mode, this is the default color that is set when the picker is initialized."""
        return self._config_get('#000000')

    @defaultColor.setter
    def defaultColor(self, value: int):
        self._config(value)

    @property
    def forceAlpha(self):
        """Set to true to always include the alpha value in the color value even if the opacity is 100%."""
        return self._config_get(False)

    @forceAlpha.setter
    def forceAlpha(self, value: bool):
        self._config(value)

    @property
    def parent(self):
        """
        """
        return self._config_get()

    @parent.setter
    def parent(self, el):
        self._config(el)

    @property
    def el(self):
        """A custom selector to bind the color picker to. This must point to HTML input fields."""
        return self._config_get()

    @el.setter
    def el(self, el):
        self._config(el)

    @property
    def inline(self):
        """Set to true to use the color picker as an inline widget. """
        return self._config_get(False)

    @inline.setter
    def inline(self, value: bool):
        self._config(value)

    @property
    def focusInput(self):
        """Focus the color value input when the color picker dialog is opened."""
        return self._config_get(True)

    @focusInput.setter
    def focusInput(self, value: bool):
        self._config(value)

    @property
    def format(self):
        """Set the preferred color string format"""
        return self._config_get('hex')

    @format.setter
    def format(self, value: str):
        self._config(value)

    @property
    def formatToggle(self):
        """Set to true to enable format toggle buttons in the color picker dialog."""
        return self._config_get(False)

    @formatToggle.setter
    def formatToggle(self, value: bool):
        self._config(value)

    @property
    def margin(self):
        """The margin in pixels between the input fields and the color picker's dialog."""
        return self._config_get(2)

    @margin.setter
    def margin(self, value: int):
        self._config(value)

    def onChange(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: etypes.PROFILE_TYPE = None, func_ref: bool = False):
        """A function that is called whenever a new color is picked. This defaults to an empty function,

        `Doc <https://coloris.js.org/>`_
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile).strip()
        if not str_func.startswith("function(color)") and not func_ref:
            if "return " not in str_func:
                str_func = "return %s" % str_func
            str_func = "function(color){%s}" % str_func
        self._config(str_func, js_type=True)

    @property
    def selectInput(self):
        """Select and focus the color value input when the color picker dialog is opened."""
        return self._config_get(False)

    @selectInput.setter
    def selectInput(self, value: bool):
        self._config(value)

    @property
    def swatchesOnly(self):
        """Set to true to hide all the color picker widgets (spectrum, hue, ...) except the swatches."""
        return self._config_get(False)

    @swatchesOnly.setter
    def swatchesOnly(self, value: bool):
        self._config(value)

    @property
    def swatches(self):
        """An array of the desired color swatches to display. If omitted or the array is empty,"""
        return self._config_get()

    @swatches.setter
    def swatches(self, values: List[str]):
        self._config(values)

    @property
    def theme(self):
        """Available themes: default, large, polaroid, pill (horizontal)."""
        return self._config_get('default')

    @theme.setter
    def theme(self, value: str):
        self._config(value)

    @property
    def themeMode(self):
        """Set the theme to light or dark mode:"""
        return self._config_get('light')

    @themeMode.setter
    def themeMode(self, value: str):
        self._config(value)

    @property
    def wrap(self):
        """"""
        return self._config_get(True)

    @wrap.setter
    def wrap(self, flag: bool):
        self._config(flag)

    @property
    def rtl(self):
        """Set to true to activate basic right-to-left support."""
        return self._config_get(False )

    @rtl.setter
    def rtl(self, flag: bool):
        self._config(flag)
