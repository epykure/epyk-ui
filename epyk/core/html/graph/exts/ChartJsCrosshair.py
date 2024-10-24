from epyk.core.html.options import Options
from epyk.core.js import JsUtils
from epyk.core.py import types as etypes


class Line(Options):

    @property
    def color(self):
        """
        crosshair line color.

        Related Pages:

          https://www.npmjs.com/package/chartjs-plugin-crosshair
        """
        return self._config_get('#F66')

    @color.setter
    def color(self, c: str):
        self._config(c)

    @property
    def width(self):
        """
        crosshair line width.

        Related Pages:

          https://www.npmjs.com/package/chartjs-plugin-crosshair
        """
        return self._config_get(1)

    @width.setter
    def width(self, num: int):
        self._config(num)


class Sync(Options):

    @property
    def enabled(self):
        """
        Enable or disable syncing of crosshairs between charts of the same group.

        Related Pages:

          https://chartjs-plugin-crosshair.netlify.app/options.html
        """
        return self._config_get(True)

    @enabled.setter
    def enabled(self, flag: bool):
        self._config(flag)

    @property
    def group(self):
        """
        Limit crosshair syncing to charts belonging to the same 'group'.

        Related Pages:

          https://www.npmjs.com/package/chartjs-plugin-crosshair
        """
        return self._config_get(1)

    @group.setter
    def group(self, num: int):
        self._config(num)

    @property
    def suppressTooltips(self):
        """
        Allows for suppressing tooltips when showing a synced crosshair.

        Related Pages:

          https://www.npmjs.com/package/chartjs-plugin-crosshair
        """
        return self._config_get(True)

    @suppressTooltips.setter
    def suppressTooltips(self, flag: bool):
        self._config(flag)


class Zoom(Options):

    @property
    def enabled(self):
        """
        Enable or disable zooming by drag and drop.

        Related Pages:

          https://www.npmjs.com/package/chartjs-plugin-crosshair
        """
        return self._config_get(True)

    @enabled.setter
    def enabled(self, flag: bool):
        self._config(flag)

    @property
    def zoomboxBackgroundColor(self):
        """
        Background color of the zoombox.

        Related Pages:

          https://www.npmjs.com/package/chartjs-plugin-crosshair
        """
        return self._config_get('rgba(66,133,244,0.2)')

    @zoomboxBackgroundColor.setter
    def zoomboxBackgroundColor(self, color: str):
        self._config(color)

    @property
    def zoomboxBorderColor(self):
        """
        Border color of the zoombox.

        Related Pages:

          https://www.npmjs.com/package/chartjs-plugin-crosshair
        """
        return self._config_get('#48F')

    @zoomboxBorderColor.setter
    def zoomboxBorderColor(self, color: str):
        self._config(color)

    @property
    def zoomButtonText(self):
        """
        Text of the button to reset the chart to original axis ranges.

        Related Pages:

          https://www.npmjs.com/package/chartjs-plugin-crosshair
        """
        return self._config_get('Reset Zoom')

    @zoomButtonText.setter
    def zoomButtonText(self, text):
        self._config(text)

    @property
    def zoomButtonClass(self):
        """
        Class of the button to reset the chart to original axis ranges.

        Related Pages:

          https://www.npmjs.com/package/chartjs-plugin-crosshair
        """
        return self._config_get('reset-zoom')

    @zoomButtonClass.setter
    def zoomButtonClass(self, text: str):
        self._config(text)


class Callbacks(Options):

    def beforeZoom(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: bool = None):
        """
        Called before zooming, return false to prevent the zoom.

        Related Pages:

          https://chartjs-plugin-crosshair.netlify.app/options.html

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self._config(
            "function(start, end){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile), js_type=True)

    def afterZoom(self, js_funcs: etypes.JS_FUNCS_TYPES, profile: bool = None):
        """
        Called after zooming, can for example be used for reloading data at a higher resolution

        Related Pages:

          https://chartjs-plugin-crosshair.netlify.app/options.html

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self._config(
            "function(start, end){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile), js_type=True)


class Crosshair(Options):

    @property
    def line(self) -> Line:
        """
        crosshair line.

        Related Pages:

          https://chartjs-plugin-crosshair.netlify.app/options.html
        """
        return self._config_sub_data("line", Line)

    @property
    def sync(self) -> Sync:
        """
        The plugin allows for syncing crosshairs over multiple charts.

        Related Pages:

          https://chartjs-plugin-crosshair.netlify.app/options.html
        """
        return self._config_sub_data("sync", Sync)

    @property
    def zoom(self) -> Zoom:
        """
        The plugin allows for horizontal zooming by clicking and dragging over the chart.

        Related Pages:

          https://chartjs-plugin-crosshair.netlify.app/options.html
        """
        return self._config_sub_data("zoom", Zoom)

    @property
    def snapToDataPoint(self):
        """
        The plugin allows snapping to datapoints when used with line charts.

        Related Pages:

          https://canvasjs.com/docs/charts/chart-options/axisx/crosshair/snap-to-datapoint/
        """
        return self._config_get(True)

    @snapToDataPoint.setter
    def snapToDataPoint(self, flag: bool):
        self._config(flag)

    @property
    def callbacks(self) -> Callbacks:
        """
        crosshair callbacks.

        Related Pages:

          https://chartjs-plugin-crosshair.netlify.app/options.html
        """
        return self._config_sub_data("callbacks", Callbacks)
