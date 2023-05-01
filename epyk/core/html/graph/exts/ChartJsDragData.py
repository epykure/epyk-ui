from epyk.core.html.options import Options
from epyk.core.js import JsUtils
from epyk.core.py import types as etypes


class DragOptions(Options):

    @property
    def showTooltip(self):
        """

        Related Pages:

          https://github.com/chrispahm/chartjs-plugin-dragdata
        """
        return self._config_get(True)

    @showTooltip.setter
    def showTooltip(self, flag: bool):
        self._config(flag)


class DragData(Options):

    @property
    def dragX(self):
        """   """
        return self._config_get(False)

    @dragX.setter
    def dragX(self, flag: bool):
        self._config(flag)

    @property
    def dragDataRound(self):
        """   """
        return self._config_get(0)

    @dragDataRound.setter
    def dragDataRound(self, num: int):
        self._config(num)

    @property
    def dragOptions(self) -> DragOptions:
        """  """
        return self._config_sub_data("dragOptions", DragOptions)

    def onDragStart(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: bool = None):
        """
        Called before zooming, return false to prevent the zoom.

        Related Pages:

          https://github.com/chrispahm/chartjs-plugin-dragdata

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self._config(
            "function(event, element){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile), js_type=True)
        return self

    def onDrag(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: bool = None):
        """
        Change cursor style to grabbing during drag action.

        Related Pages:

          https://github.com/chrispahm/chartjs-plugin-dragdata

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self._config(
            "function(event, datasetIndex, index, value){%s}" % JsUtils.jsConvertFncs(
                js_funcs, toStr=True, profile=profile), js_type=True)
        return self

    def onDragEnd(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: bool = None):
        """
        Restore default cursor style upon drag release.

        Related Pages:

          https://github.com/chrispahm/chartjs-plugin-dragdata

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self._config(
            "function(event, datasetIndex, index, value){%s}" % JsUtils.jsConvertFncs(
                js_funcs, toStr=True, profile=profile), js_type=True)
        return self

    @property
    def round(self):
        """   """
        return self._config_get(None)

    @round.setter
    def round(self, num: float):
        self._config(num)

    @property
    def showTooltip(self):
        """   """
        return self._config_get(None)

    @showTooltip.setter
    def showTooltip(self, flag: bool):
        self._config(flag)
