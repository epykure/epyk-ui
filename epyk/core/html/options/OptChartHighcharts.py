from epyk.core.html.options import OptionsWithTemplates
from epyk.core.html.options.highcharts import oannotations
from epyk.core.html.options.highcharts import onoData
from epyk.core.html.options.highcharts import otime
from epyk.core.html.options.highcharts import oloading
from epyk.core.html.options.highcharts import oyAxis
from epyk.core.html.options.highcharts import oresponsive
from epyk.core.html.options.highcharts import oexporting
from epyk.core.html.options.highcharts import oaccessibility
from epyk.core.html.options.highcharts import otitle
from epyk.core.html.options.highcharts import oseries
from epyk.core.html.options.highcharts import oxAxis
from epyk.core.html.options.highcharts import ozAxis
from epyk.core.html.options.highcharts import odata
from epyk.core.html.options.highcharts import onavigation
from epyk.core.html.options.highcharts import opane
from epyk.core.html.options.highcharts import oglobal
from epyk.core.html.options.highcharts import olang
from epyk.core.html.options.highcharts import ochart
from epyk.core.html.options.highcharts import otooltip
from epyk.core.html.options.highcharts import odefs
from epyk.core.html.options.highcharts import oplotOptions
from epyk.core.html.options.highcharts import ocredits
from epyk.core.html.options.highcharts import osubtitle
from epyk.core.html.options.highcharts import ocolorAxis
from epyk.core.html.options.highcharts import odrilldown
from epyk.core.html.options.highcharts import ocaption
from epyk.core.html.options.highcharts import oboost
from epyk.core.html.options.highcharts import olegend
from epyk.core.html.options.highcharts import osonification


class OptionsHighcharts(OptionsWithTemplates):

    @property
    def defs(self) -> odefs.OptionDefs:
        """ """
        return self._config_sub_data("defs", odefs.OptionDefs)


    @property
    def navigation(self) -> onavigation.OptionNavigation:
        """ """
        return self._config_sub_data("navigation", onavigation.OptionNavigation)


    @property
    def responsive(self) -> oresponsive.OptionResponsive:
        """ """
        return self._config_sub_data("responsive", oresponsive.OptionResponsive)


    @property
    def drilldown(self) -> odrilldown.OptionDrilldown:
        """ """
        return self._config_sub_data("drilldown", odrilldown.OptionDrilldown)


    @property
    def series_(self) -> oseries.OptionSeries:
        """ """
        return self._config_sub_data_enum("series", oseries.OptionSeries)


    @property
    def subtitle(self) -> osubtitle.OptionSubtitle:
        """ """
        return self._config_sub_data("subtitle", osubtitle.OptionSubtitle)


    @property
    def annotations(self) -> oannotations.OptionAnnotations:
        """ """
        return self._config_sub_data("annotations", oannotations.OptionAnnotations)


    @property
    def yAxis(self) -> oyAxis.OptionYaxis:
        """ """
        return self._config_sub_data("yAxis", oyAxis.OptionYaxis)


    @property
    def accessibility(self) -> oaccessibility.OptionAccessibility:
        """ """
        return self._config_sub_data("accessibility", oaccessibility.OptionAccessibility)


    @property
    def credits(self) -> ocredits.OptionCredits:
        """ """
        return self._config_sub_data("credits", ocredits.OptionCredits)


    @property
    def data(self) -> odata.OptionData:
        """ """
        return self._config_sub_data("data", odata.OptionData)


    @property
    def exporting(self) -> oexporting.OptionExporting:
        """ """
        return self._config_sub_data("exporting", oexporting.OptionExporting)


    @property
    def caption(self) -> ocaption.OptionCaption:
        """ """
        return self._config_sub_data("caption", ocaption.OptionCaption)


    @property
    def colorAxis(self) -> ocolorAxis.OptionColoraxis:
        """ """
        return self._config_sub_data("colorAxis", ocolorAxis.OptionColoraxis)


    @property
    def title(self) -> otitle.OptionTitle:
        """ """
        return self._config_sub_data("title", otitle.OptionTitle)


    @property
    def pane(self) -> opane.OptionPane:
        """ """
        return self._config_sub_data("pane", opane.OptionPane)


    @property
    def time(self) -> otime.OptionTime:
        """ """
        return self._config_sub_data("time", otime.OptionTime)


    @property
    def chart(self) -> ochart.OptionChart:
        """ """
        return self._config_sub_data("chart", ochart.OptionChart)


    @property
    def zAxis(self) -> ozAxis.OptionZaxis:
        """ """
        return self._config_sub_data("zAxis", ozAxis.OptionZaxis)


    @property
    def global_(self) -> oglobal.OptionGlobal:
        """ """
        return self._config_sub_data("global", oglobal.OptionGlobal)


    @property
    def noData(self) -> onoData.OptionNodata:
        """ """
        return self._config_sub_data("noData", onoData.OptionNodata)


    @property
    def sonification(self) -> osonification.OptionSonification:
        """ """
        return self._config_sub_data("sonification", osonification.OptionSonification)


    @property
    def legend(self) -> olegend.OptionLegend:
        """ """
        return self._config_sub_data("legend", olegend.OptionLegend)


    @property
    def loading(self) -> oloading.OptionLoading:
        """ """
        return self._config_sub_data("loading", oloading.OptionLoading)


    @property
    def boost(self) -> oboost.OptionBoost:
        """ """
        return self._config_sub_data("boost", oboost.OptionBoost)


    @property
    def tooltip(self) -> otooltip.OptionTooltip:
        """ """
        return self._config_sub_data("tooltip", otooltip.OptionTooltip)


    @property
    def xAxis(self) -> oxAxis.OptionXaxis:
        """ """
        return self._config_sub_data("xAxis", oxAxis.OptionXaxis)


    @property
    def plotOptions(self) -> oplotOptions.OptionPlotoptions:
        """ """
        return self._config_sub_data("plotOptions", oplotOptions.OptionPlotoptions)


    @property
    def lang(self) -> olang.OptionLang:
        """ """
        return self._config_sub_data("lang", olang.OptionLang)
