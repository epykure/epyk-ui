from epyk.core.html.options import Options
from typing import Any

        
class OptionBoostDebug(Options):

    @property
    def showSkipSummary(self):
        """Show the number of points skipped through culling.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Boost/Boost.ts
        """
        return self._config_get(False)

    @showSkipSummary.setter
    def showSkipSummary(self, flag: bool): self._config(flag, js_type=False)

    @property
    def timeBufferCopy(self):
        """Time the WebGL to SVG buffer copy After rendering, the result is copied to an image which is injected into the SVG.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Boost/Boost.ts
        """
        return self._config_get(False)

    @timeBufferCopy.setter
    def timeBufferCopy(self, flag: bool): self._config(flag, js_type=False)

    @property
    def timeKDTree(self):
        """Time the building of the k-d tree.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Boost/Boost.ts
        """
        return self._config_get(False)

    @timeKDTree.setter
    def timeKDTree(self, flag: bool): self._config(flag, js_type=False)

    @property
    def timeRendering(self):
        """Time the series rendering.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Boost/Boost.ts
        """
        return self._config_get(False)

    @timeRendering.setter
    def timeRendering(self, flag: bool): self._config(flag, js_type=False)

    @property
    def timeSeriesProcessing(self):
        """Time the series processing.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Boost/Boost.ts
        """
        return self._config_get(False)

    @timeSeriesProcessing.setter
    def timeSeriesProcessing(self, flag: bool): self._config(flag, js_type=False)

    @property
    def timeSetup(self):
        """Time the the WebGL setup.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Boost/Boost.ts
        """
        return self._config_get(False)

    @timeSetup.setter
    def timeSetup(self, flag: bool): self._config(flag, js_type=False)

        
class OptionBoost(Options):

    @property
    def allowForce(self):
        """The chart will be boosted, if one of the series crosses its threshold and all the series in the chart can be boosted.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Boost/Boost.ts
        """
        return self._config_get(True)

    @allowForce.setter
    def allowForce(self, flag: bool): self._config(flag, js_type=False)

    @property
    def debug(self) -> 'OptionBoostDebug':
        """Debugging options for boost. """
        return self._config_sub_data("debug", OptionBoostDebug)

    @property
    def enabled(self):
        """Enable or disable boost on a chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Boost/Boost.ts
        """
        return self._config_get(True)

    @enabled.setter
    def enabled(self, flag: bool): self._config(flag, js_type=False)

    @property
    def pixelRatio(self):
        """The pixel ratio for the WebGL content.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Boost/Boost.ts
        """
        return self._config_get(1)

    @pixelRatio.setter
    def pixelRatio(self, num: float): self._config(num, js_type=False)

    @property
    def seriesThreshold(self):
        """Set the series threshold for when the boost should kick in globally.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Boost/Boost.ts
        """
        return self._config_get(50)

    @seriesThreshold.setter
    def seriesThreshold(self, num: float): self._config(num, js_type=False)

    @property
    def useGPUTranslations(self):
        """Enable or disable GPU translations.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Boost/Boost.ts
        """
        return self._config_get(False)

    @useGPUTranslations.setter
    def useGPUTranslations(self, flag: bool): self._config(flag, js_type=False)

    @property
    def usePreallocated(self):
        """Enable or disable pre-allocation of vertex buffers.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Boost/Boost.ts
        """
        return self._config_get(False)

    @usePreallocated.setter
    def usePreallocated(self, flag: bool): self._config(flag, js_type=False)
