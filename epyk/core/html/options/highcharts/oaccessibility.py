from epyk.core.html.options import Options
from typing import Any

        
class OptionAccessibilitySeries(Options):

    @property
    def describeSingleSeries(self):
        """Whether or not to add series descriptions to charts with a single series.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(False)

    @describeSingleSeries.setter
    def describeSingleSeries(self, flag: bool): self._config(flag, js_type=False)

    @property
    def descriptionFormat(self):
        """Format to use for describing the data series group to assistive technology - including screen readers.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get("{seriesDescription}{authorDescription}{axisDescription}")

    @descriptionFormat.setter
    def descriptionFormat(self, text: str): self._config(text, js_type=False)

    @property
    def descriptionFormatter(self):
        """Formatter function to use instead of the default for series descriptions.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(None)

    @descriptionFormatter.setter
    def descriptionFormatter(self, value: Any): self._config(value, js_type=False)

    @property
    def pointDescriptionEnabledThreshold(self):
        """When a series contains more points than this, we no longer expose information about individual points to screen readers.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(200)

    @pointDescriptionEnabledThreshold.setter
    def pointDescriptionEnabledThreshold(self, flag: bool): self._config(flag, js_type=False)

        
class OptionAccessibilityScreenreadersection(Options):

    @property
    def afterChartFormat(self):
        """Format for the screen reader information region after the chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get("{endOfChartMarker}")

    @afterChartFormat.setter
    def afterChartFormat(self, text: str): self._config(text, js_type=False)

    @property
    def afterChartFormatter(self):
        """A formatter function to create the HTML contents of the hidden screen reader information region after the chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(None)

    @afterChartFormatter.setter
    def afterChartFormatter(self, value: Any): self._config(value, js_type=False)

    @property
    def axisRangeDateFormat(self):
        """Date format to use to describe range of datetime axes.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get("%Y-%m-%d %H:%M:%S")

    @axisRangeDateFormat.setter
    def axisRangeDateFormat(self, text: str): self._config(text, js_type=False)

    @property
    def beforeChartFormat(self):
        """Format for the screen reader information region before the chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get("<{headingTagName}>{chartTitle}</{headingTagName}><div>{typeDescription}</div><div>{chartSubtitle}</div><div>{chartLongdesc}</div><div>{playAsSoundButton}</div><div>{viewTableButton}</div><div>{xAxisDescription}</div><div>{yAxisDescription}</div><div>{annotationsTitle}{annotationsList}</div>")

    @beforeChartFormat.setter
    def beforeChartFormat(self, text: str): self._config(text, js_type=False)

    @property
    def beforeChartFormatter(self):
        """A formatter function to create the HTML contents of the hidden screen reader information region before the chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(None)

    @beforeChartFormatter.setter
    def beforeChartFormatter(self, value: Any): self._config(value, js_type=False)

    @property
    def onPlayAsSoundClick(self):
        """Function to run upon clicking the &quot;Play as sound&quot; button in the screen reader region.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(None)

    @onPlayAsSoundClick.setter
    def onPlayAsSoundClick(self, value: Any): self._config(value, js_type=False)

    @property
    def onViewDataTableClick(self):
        """Function to run upon clicking the &quot;View as Data Table&quot; link in the screen reader region.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(None)

    @onViewDataTableClick.setter
    def onViewDataTableClick(self, value: Any): self._config(value, js_type=False)

        
class OptionAccessibilityPoint(Options):

    @property
    def dateFormat(self):
        """Date format to use for points on datetime axes when describing them to screen reader users.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(None)

    @dateFormat.setter
    def dateFormat(self, text: str): self._config(text, js_type=False)

    @property
    def dateFormatter(self):
        """Formatter function to determine the date/time format used with points on datetime axes when describing them to screen reader users.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(None)

    @dateFormatter.setter
    def dateFormatter(self, value: Any): self._config(value, js_type=False)

    @property
    def describeNull(self):
        """Whether or not to describe points with the value <code>null</code> to assistive technology, such as screen readers.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(True)

    @describeNull.setter
    def describeNull(self, flag: bool): self._config(flag, js_type=False)

    @property
    def descriptionFormat(self):
        """A <a href="https://www.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(None)

    @descriptionFormat.setter
    def descriptionFormat(self, text: str): self._config(text, js_type=False)

    @property
    def descriptionFormatter(self):
        """Formatter function to use instead of the default for point descriptions.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(None)

    @descriptionFormatter.setter
    def descriptionFormatter(self, value: Any): self._config(value, js_type=False)

    @property
    def valueDecimals(self):
        """Decimals to use for the values in the point descriptions.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(None)

    @valueDecimals.setter
    def valueDecimals(self, num: float): self._config(num, js_type=False)

    @property
    def valueDescriptionFormat(self):
        """Format to use for describing the values of data points to assistive technology - including screen readers.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get("{xDescription}{separator}{value}.")

    @valueDescriptionFormat.setter
    def valueDescriptionFormat(self, text: str): self._config(text, js_type=False)

    @property
    def valuePrefix(self):
        """Prefix to add to the values in the point descriptions.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(None)

    @valuePrefix.setter
    def valuePrefix(self, text: str): self._config(text, js_type=False)

    @property
    def valueSuffix(self):
        """Suffix to add to the values in the point descriptions.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(None)

    @valueSuffix.setter
    def valueSuffix(self, text: str): self._config(text, js_type=False)

        
class OptionAccessibilityKeyboardnavigationSeriesnavigation(Options):

    @property
    def mode(self):
        """Set the keyboard navigation mode for the chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get("normal")

    @mode.setter
    def mode(self, text: str): self._config(text, js_type=False)

    @property
    def pointNavigationEnabledThreshold(self):
        """When a series contains more points than this, we no longer allow keyboard navigation for it.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(False)

    @pointNavigationEnabledThreshold.setter
    def pointNavigationEnabledThreshold(self, flag: bool): self._config(flag, js_type=False)

    @property
    def rememberPointFocus(self):
        """Remember which point was focused even after navigating away from the series, so that when navigating back to the series you start at the last focused point.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(False)

    @rememberPointFocus.setter
    def rememberPointFocus(self, flag: bool): self._config(flag, js_type=False)

    @property
    def skipNullPoints(self):
        """Skip null points when navigating through points with the keyboard.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(True)

    @skipNullPoints.setter
    def skipNullPoints(self, flag: bool): self._config(flag, js_type=False)

        
class OptionAccessibilityKeyboardnavigation(Options):

    @property
    def enabled(self):
        """Enable keyboard navigation for the chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(True)

    @enabled.setter
    def enabled(self, flag: bool): self._config(flag, js_type=False)

    @property
    def focusBorder(self) -> 'OptionAccessibilityKeyboardnavigationFocusborder':
        """Options for the focus border drawn around elements while navigating through them. """
        return self._config_sub_data("focusBorder", OptionAccessibilityKeyboardnavigationFocusborder)

    @property
    def order(self):
        """Order of tab navigation in the chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(None)

    @order.setter
    def order(self, value: Any): self._config(value, js_type=False)

    @property
    def seriesNavigation(self) -> 'OptionAccessibilityKeyboardnavigationSeriesnavigation':
        """Options for the keyboard navigation of data points and series. """
        return self._config_sub_data("seriesNavigation", OptionAccessibilityKeyboardnavigationSeriesnavigation)

    @property
    def wrapAround(self):
        """Whether or not to wrap around when reaching the end of arrow-key navigation for an element in the chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(True)

    @wrapAround.setter
    def wrapAround(self, flag: bool): self._config(flag, js_type=False)

        
class OptionAccessibilityKeyboardnavigationFocusborderStyle(Options):

    @property
    def borderRadius(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(3)

    @borderRadius.setter
    def borderRadius(self, num: float): self._config(num, js_type=False)

    @property
    def color(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get("#334eff")

    @color.setter
    def color(self, text: str): self._config(text, js_type=False)

    @property
    def lineWidth(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(2)

    @lineWidth.setter
    def lineWidth(self, num: float): self._config(num, js_type=False)

        
class OptionAccessibilityKeyboardnavigationFocusborder(Options):

    @property
    def enabled(self):
        """Enable/disable focus border for chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(True)

    @enabled.setter
    def enabled(self, flag: bool): self._config(flag, js_type=False)

    @property
    def hideBrowserFocusOutline(self):
        """Hide the browser&#39;s default focus indicator.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(True)

    @hideBrowserFocusOutline.setter
    def hideBrowserFocusOutline(self, flag: bool): self._config(flag, js_type=False)

    @property
    def margin(self):
        """Focus border margin around the elements.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(2)

    @margin.setter
    def margin(self, num: float): self._config(num, js_type=False)

    @property
    def style(self) -> 'OptionAccessibilityKeyboardnavigationFocusborderStyle':
        """Style options for the focus border drawn around elements while navigating through them. """
        return self._config_sub_data("style", OptionAccessibilityKeyboardnavigationFocusborderStyle)

        
class OptionAccessibilityAnnouncenewdata(Options):

    @property
    def announcementFormatter(self):
        """Optional formatter callback for the announcement.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(None)

    @announcementFormatter.setter
    def announcementFormatter(self, value: Any): self._config(value, js_type=False)

    @property
    def enabled(self):
        """Enable announcing new data to screen reader users.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(False)

    @enabled.setter
    def enabled(self, flag: bool): self._config(flag, js_type=False)

    @property
    def interruptUser(self):
        """Choose whether or not the announcements should interrupt the screen reader.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(False)

    @interruptUser.setter
    def interruptUser(self, flag: bool): self._config(flag, js_type=False)

    @property
    def minAnnounceInterval(self):
        """Minimum interval between announcements in milliseconds.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(5000)

    @minAnnounceInterval.setter
    def minAnnounceInterval(self, num: float): self._config(num, js_type=False)

        
class OptionAccessibility(Options):

    @property
    def announceNewData(self) -> 'OptionAccessibilityAnnouncenewdata':
        """Options for announcing new data to screen reader users. """
        return self._config_sub_data("announceNewData", OptionAccessibilityAnnouncenewdata)

    @property
    def customComponents(self):
        """A hook for adding custom components to the accessibility module.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(None)

    @customComponents.setter
    def customComponents(self, value: Any): self._config(value, js_type=False)

    @property
    def description(self):
        """A text description of the chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(None)

    @description.setter
    def description(self, text: str): self._config(text, js_type=False)

    @property
    def enabled(self):
        """Enable accessibility functionality for the chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(True)

    @enabled.setter
    def enabled(self, flag: bool): self._config(flag, js_type=False)

    @property
    def highContrastTheme(self):
        """Theme to apply to the chart when Windows High Contrast Mode is detected.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(None)

    @highContrastTheme.setter
    def highContrastTheme(self, value: Any): self._config(value, js_type=False)

    @property
    def keyboardNavigation(self) -> 'OptionAccessibilityKeyboardnavigation':
        """Options for keyboard navigation. """
        return self._config_sub_data("keyboardNavigation", OptionAccessibilityKeyboardnavigation)

    @property
    def landmarkVerbosity(self):
        """Amount of landmarks/regions to create for screen reader users.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get("all")

    @landmarkVerbosity.setter
    def landmarkVerbosity(self, text: str): self._config(text, js_type=False)

    @property
    def linkedDescription(self):
        """Link the chart to an HTML element describing the contents of the chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get('*[data-highcharts-chart="{index}"] + .highcharts-description')

    @linkedDescription.setter
    def linkedDescription(self, text: str): self._config(text, js_type=True)

    @property
    def point(self) -> 'OptionAccessibilityPoint':
        """Options for descriptions of individual data points. """
        return self._config_sub_data("point", OptionAccessibilityPoint)

    @property
    def screenReaderSection(self) -> 'OptionAccessibilityScreenreadersection':
        """Accessibility options for the screen reader information sections added before and after the chart. """
        return self._config_sub_data("screenReaderSection", OptionAccessibilityScreenreadersection)

    @property
    def series(self) -> 'OptionAccessibilitySeries':
        """Accessibility options global to all data series. """
        return self._config_sub_data("series", OptionAccessibilitySeries)

    @property
    def typeDescription(self):
        """A text description of the chart type.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(None)

    @typeDescription.setter
    def typeDescription(self, text: str): self._config(text, js_type=False)
