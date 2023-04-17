from epyk.core.html.options import Options
from epyk.core.js import JsUtils
from epyk.core.py import types as etypes


class ZoomRange(Options):

    @property
    def x(self):
        """

        Related Pages:

          https://github.com/chartjs/chartjs-plugin-zoom
        """
        return self._config_get(None)

    @x.setter
    def x(self, num: float):
        self._config(num)

    @property
    def y(self):
        """

        Related Pages:

          https://github.com/chartjs/chartjs-plugin-zoom
        """
        return self._config_get(None)

    @y.setter
    def y(self, num: float):
        self._config(num)


class ZoomAttrs(Options):

    @property
    def enabled(self):
        """

        Related Pages:

          https://github.com/chartjs/chartjs-plugin-zoom
        """
        return self._config_get()

    @enabled.setter
    def enabled(self, flag: bool):
        self._config(flag)

    @property
    def mode(self):
        """

        Related Pages:

          https://github.com/chartjs/chartjs-plugin-zoom
        """
        return self._config_get()

    @mode.setter
    def mode(self, value):
        self._config(value)

    @property
    def rangeMin(self) -> ZoomRange:
        """ """
        return self._config_sub_data("rangeMin", ZoomRange)

    @property
    def rangeMax(self) -> ZoomRange:
        """ """
        return self._config_sub_data("rangeMax", ZoomRange)

    @property
    def speed(self):
        """

        Related Pages:

          https://github.com/chartjs/chartjs-plugin-zoom
        """
        return self._config_get()

    @speed.setter
    def speed(self, num: float):
        self._config(num)

    @property
    def threshold(self):
        """
        Minimal pan distance required before actually applying pan

        Related Pages:

          https://github.com/chartjs/chartjs-plugin-zoom
        """
        return self._config_get()

    @threshold.setter
    def threshold(self, num: float):
        self._config(num)


class ZoomPan(ZoomAttrs):

    def onPan(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: bool = None):
        """
        Function called while the user is zooming.

        Related Pages:

          https://www.chartjs.org/chartjs-plugin-zoom/latest/guide/options.html

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self._config("function(data){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile), js_type=True)

    def onPanComplete(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: bool = None):
        """
        Function called while the user is zooming.

        Related Pages:

          https://www.chartjs.org/chartjs-plugin-zoom/latest/guide/options.html

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self._config("function(data){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile), js_type=True)

    def onPanRejected(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: bool = None):
        """
        Called when panning is rejected due to missing modifier key. event is the a hammer event that failed.

        Related Pages:

          https://www.chartjs.org/chartjs-plugin-zoom/latest/guide/options.html

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self._config("function(data){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile), js_type=True)

    def onPanStart(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: bool = None):
        """
        Called when panning is about to start.
        If this callback returns false, panning is aborted and onPanRejected is invoked.

        Related Pages:

          https://www.chartjs.org/chartjs-plugin-zoom/latest/guide/options.html

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self._config("function(data){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile), js_type=True)


class ZoomWheel(Options):

    @property
    def enabled(self):
        """
        Enable zooming via mouse wheel.

        Related Pages:

          https://www.chartjs.org/chartjs-plugin-zoom/latest/guide/options.html
        """
        return self._config_get()

    @enabled.setter
    def enabled(self, flag: bool):
        self._config(flag)

    @property
    def speed(self):
        """
        Factor of zoom speed via mouse wheel.

        Related Pages:

          https://www.chartjs.org/chartjs-plugin-zoom/latest/guide/options.html
        """
        return self._config_get()

    @speed.setter
    def speed(self, num: float):
        self._config(num)

    @property
    def modifierKey(self):
        """
        Modifier key required for zooming via mouse wheel.

        Related Pages:

          https://www.chartjs.org/chartjs-plugin-zoom/latest/guide/options.html
        """
        return self._config_get(None)

    @modifierKey.setter
    def modifierKey(self, value: str):
        self._config(value)


class ZoomDrag(Options):

    @property
    def enabled(self):
        """
        Enable drag-to-zoom.

        Related Pages:

          https://www.chartjs.org/chartjs-plugin-zoom/latest/guide/options.html
        """
        return self._config_get(True)

    @enabled.setter
    def enabled(self, flag: bool):
        self._config(flag)

    @property
    def backgroundColor(self):
        """
        Fill color.

        Related Pages:

          https://www.chartjs.org/chartjs-plugin-zoom/latest/guide/options.html
        """
        return self._config_get('rgba(225,225,225,0.3)')

    @backgroundColor.setter
    def backgroundColor(self, color: str):
        self._config(color)

    @property
    def borderColor(self):
        """
        Stroke color.

        Related Pages:

          https://www.chartjs.org/chartjs-plugin-zoom/latest/guide/options.html
        """
        return self._config_get('rgba(225,225,225)')

    @borderColor.setter
    def borderColor(self, color: str):
        self._config(color)

    @property
    def borderWidth(self):
        """
        Stroke width.

        Related Pages:

          https://www.chartjs.org/chartjs-plugin-zoom/latest/guide/options.html
        """
        return self._config_get(0)

    @borderWidth.setter
    def borderWidth(self, num: int):
        self._config(num)

    @property
    def borderColor(self):
        """
        When the dragging box is drawn on the chart.

        Related Pages:

          https://www.chartjs.org/chartjs-plugin-zoom/latest/guide/options.html
        """
        return self._config_get('beforeDatasetsDraw')

    @borderColor.setter
    def borderColor(self, value: str):
        self._config(value)

    @property
    def threshold(self):
        """
        Minimal zoom distance required before actually applying zoom.

        Related Pages:

          https://www.chartjs.org/chartjs-plugin-zoom/latest/guide/options.html
        """
        return self._config_get(0)

    @threshold.setter
    def threshold(self, num: int):
        self._config(num)

    @property
    def modifierKey(self):
        """
        Modifier key required for drag-to-zoom.

        Related Pages:

          https://www.chartjs.org/chartjs-plugin-zoom/latest/guide/options.html
        """
        return self._config_get(None)

    @modifierKey.setter
    def modifierKey(self, value: str):
        self._config(value)


class ZoomPinch(Options):

    @property
    def enabled(self):
        """
        Enable drag-to-zoom.

        Related Pages:

          https://www.chartjs.org/chartjs-plugin-zoom/latest/guide/options.html
        """
        return self._config_get(True)

    @enabled.setter
    def enabled(self, flag: bool):
        self._config(flag)


class ZoomZoom(ZoomAttrs):

    @property
    def drag(self) -> ZoomDrag:
        """
        Options of the drag-to-zoom behavior

        Related Pages:

          https://www.chartjs.org/chartjs-plugin-zoom/latest/guide/options.html
          https://www.chartjs.org/chartjs-plugin-zoom/latest/guide/options.html
        """
        return self._config_sub_data("drag", ZoomDrag)

    @property
    def mode(self):
        """
        Allowed zoom directions.

        Related Pages:

          https://www.chartjs.org/chartjs-plugin-zoom/latest/guide/options.html
        """
        return self._config_get('xy')

    @mode.setter
    def mode(self, value: str):
        self._config(value)

    @property
    def scaleMode(self):
        """
        Which of the enabled zooming directions should only be available when the mouse cursor is over a scale
         for that axis.

        Related Pages:

          https://www.chartjs.org/chartjs-plugin-zoom/latest/guide/options.html
        """
        return self._config_get(None)

    @scaleMode.setter
    def scaleMode(self, value: str):
        self._config(value)

    @property
    def sensitivity(self):
        """

        Related Pages:

          https://github.com/chartjs/chartjs-plugin-zoom
        """
        return self._config_get()

    @sensitivity.setter
    def sensitivity(self, num: float):
        self._config(num)

    def onZoom(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: bool = None):
        """
        Function called while the user is zooming.

        Related Pages:

          https://www.chartjs.org/chartjs-plugin-zoom/latest/guide/options.html

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self._config("function(data){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile), js_type=True)

    def onZoomComplete(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: bool = None):
        """
        Function called once zooming is completed.

        Related Pages:

          https://www.chartjs.org/chartjs-plugin-zoom/latest/guide/options.html

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self._config("function(data){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile), js_type=True)

    @property
    def wheel(self) -> ZoomWheel:
        """
        Options of the mouse wheel behavior

        Related Pages:

          https://www.chartjs.org/chartjs-plugin-zoom/latest/guide/options.html
        """
        return self._config_sub_data("wheel", ZoomWheel)

    @property
    def pinch(self) -> ZoomPinch:
        """
        Options of the pinch behavior

        Related Pages:

          https://www.chartjs.org/chartjs-plugin-zoom/latest/guide/options.html
        """
        return self._config_sub_data("pinch", ZoomPinch)


class ZoomLimits(Options):

    def x(self, min: float = 'original', max: float = 'original', minRange: float = None):
        """
        Limits for x-axis.

        Related Pages:

          https://www.chartjs.org/chartjs-plugin-zoom/latest/guide/options.html
          https://www.chartjs.org/chartjs-plugin-zoom/latest/guide/options.html

        :param min: Minimum allowed value for scale.min
        :param max: Maximum allowed value for scale.max
        :param minRange: Minimum allowed range (max - min). This defines the max zoom level
        """

    def y(self, min: float = 'original', max: float = 'original', minRange: float = None):
        """
        Limits for y-axis.

        Related Pages:

          https://www.chartjs.org/chartjs-plugin-zoom/latest/guide/options.html
          https://www.chartjs.org/chartjs-plugin-zoom/latest/guide/options.html

        :param min: Minimum allowed value for scale.min
        :param max: Maximum allowed value for scale.max
        :param minRange: Minimum allowed range (max - min). This defines the max zoom level
        """

    def axis(self, name: str, min: float = 'original', max: float = 'original', minRange: float = None):
        """
        Limits for x-axis.

        Related Pages:

          https://www.chartjs.org/chartjs-plugin-zoom/latest/guide/options.html
          https://www.chartjs.org/chartjs-plugin-zoom/latest/guide/options.html

        :param min: Minimum allowed value for scale.min
        :param max: Maximum allowed value for scale.max
        :param minRange: Minimum allowed range (max - min). This defines the max zoom level
        """


class Zoom(Options):

    def set_default(self, mode: str = "xy"):
        """
        Set zoom default attributes.

        Related Pages:

          https://github.com/chartjs/chartjs-plugin-zoom

        :param mode: Optional. Zooming directions
        """
        self.pan.mode = mode
        self.pan.enabled = True
        self.zoom.enabled = True
        self.zoom.mode = mode

    @property
    def pan(self) -> ZoomPan:
        """
        Enable panning.

        Related Pages:

          https://www.chartjs.org/chartjs-plugin-zoom/latest/guide/options.html

        """
        return self._config_sub_data("pan", ZoomPan)

    @property
    def zoom(self) -> ZoomZoom:
        """

        Related Pages:

          https://www.chartjs.org/chartjs-plugin-zoom/latest/guide/options.html

        """
        return self._config_sub_data("zoom", ZoomZoom)

    @property
    def limits(self) -> ZoomLimits:
        """
        Limits options define the limits per axis for pan and zoom.

        Related Pages:

          https://www.chartjs.org/chartjs-plugin-zoom/latest/guide/options.html

        """
        return self._config_sub_data("limits", ZoomLimits)
