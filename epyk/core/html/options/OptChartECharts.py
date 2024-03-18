#!/usr/bin/python
# -*- coding: utf-8 -*-


from epyk.core.html.options import Options
from epyk.core.html.options import OptionsWithTemplates


class OptionTitle(Options):

    @property
    def subtext(self):
        return self._config_get()

    @subtext.setter
    def subtext(self, val):
        self._config(val)

    @property
    def text(self):
        return self._config_get()

    @text.setter
    def text(self, val):
        self._config(val)


class OptionLegend(Options):

    @property
    def data(self):
        return self._config_get()

    @data.setter
    def data(self, val):
        self._config(val)


class OptionYAxis(Options):

    @property
    def type(self):
        return self._config_get()

    @type.setter
    def type(self, val):
        self._config(val)

    @property
    def data(self):
        return self._config_get()

    @data.setter
    def data(self, val):
        self._config(val)


class OptionGrid(Options):

    @property
    def left(self):
        return self._config_get()

    @left.setter
    def left(self, value: str):
        self._config(value)

    @property
    def right(self):
        return self._config_get()

    @right.setter
    def right(self, value: str):
        self._config(value)

    @property
    def bottom(self):
        return self._config_get()

    @bottom.setter
    def bottom(self, value: str):
        self._config(value)

    @property
    def containLabel(self):
        return self._config_get()

    @containLabel.setter
    def containLabel(self, flag: bool):
        self._config(flag)
        

class OptionXAxis(Options):

    @property
    def boundaryGap(self):
        return self._config_get()

    @boundaryGap.setter
    def boundaryGap(self, flag: bool):
        self._config(flag)

    @property
    def nameLocation(self):
        return self._config_get()

    @nameLocation.setter
    def nameLocation(self, val):
        self._config(val)

    @property
    def type(self):
        return self._config_get()

    @type.setter
    def type(self, val):
        self._config(val)

    @property
    def data(self):
        return self._config_get()

    @data.setter
    def data(self, val):
        self._config(val)


class OptionTooltip(Options):

    @property
    def trigger(self):
        return self._config_get()

    @trigger.setter
    def trigger(self, val):
        self._config(val)


class OptionEmphasis(Options):

    @property
    def focus(self):
        return self._config_get()

    @focus.setter
    def focus(self, val: str):
        self._config(val)


class OptionLabel(Options):

    @property
    def position(self):
        return self._config_get()

    @position.setter
    def position(self, val: str):
        self._config(val)

    @property
    def show(self):
        return self._config_get()

    @show.setter
    def show(self, flag: bool):
        self._config(flag)


class OptionLineStyle(Options):

    @property
    def width(self):
        return self._config_get()

    @width.setter
    def width(self, val: int):
        self._config(val)


class OptionSeries(Options):

    @property
    def areaStyle(self):
        return self._config_get()

    @areaStyle.setter
    def areaStyle(self, val: str):
        self._config(val)

    @property
    def color(self):
        return self._config_get()

    @color.setter
    def color(self, val):
        self._config(val)

    @property
    def data(self):
        return self._config_get()

    @data.setter
    def data(self, val):
        self._config(val)

    @property
    def emphasis(self):
        return self._config_sub_data("emphasis", OptionEmphasis)

    @property
    def label(self):
        return self._config_sub_data("label", OptionLabel)

    @property
    def lineStyle(self):
        return self._config_sub_data("lineStyle", OptionLineStyle)

    @property
    def name(self):
        return self._config_get()

    @name.setter
    def name(self, val):
        self._config(val)

    @property
    def type(self):
        return self._config_get()

    @type.setter
    def type(self, val):
        self._config(val)

    @property
    def showSymbol(self):
        return self._config_get()

    @showSymbol.setter
    def showSymbol(self, flag: bool):
        self._config(flag)

    @property
    def smooth(self):
        return self._config_get()

    @smooth.setter
    def smooth(self, flag: bool):
        self._config(flag)

    @property
    def stack(self):
        return self._config_get()

    @stack.setter
    def stack(self, val: str):
        self._config(val)

    @property
    def step(self):
        return self._config_get()

    @step.setter
    def step(self, val: str):
        self._config(val)

    @property
    def symbolSize(self):
        return self._config_get()

    @symbolSize.setter
    def symbolSize(self, num: int):
        self._config(num)


class OptionFeature(Options):

    @property
    def saveAsImage(self):
        return self._config_get()

    @saveAsImage.setter
    def saveAsImage(self, val: str):
        self._config(val)


class OptionToolbox(Options):

    @property
    def feature(self) -> OptionFeature:
        """ """
        return self._config_sub_data("feature", OptionFeature)


class EChartOptions(OptionsWithTemplates):


    @property
    def grid(self) -> OptionGrid:
        """ """
        return self._config_sub_data("grid", OptionGrid)

    @property
    def title(self) -> OptionTitle:
        """ """
        return self._config_sub_data("title", OptionTitle)

    @property
    def legend(self) -> OptionLegend:
        """ """
        return self._config_sub_data("legend", OptionLegend)

    @property
    def toolbox(self) -> OptionTooltip:
        """ """
        return self._config_sub_data("toolbox", OptionToolbox)

    @property
    def tooltip(self) -> OptionTooltip:
        """ """
        return self._config_sub_data("tooltip", OptionTooltip)

    @property
    def xAxis(self) -> OptionXAxis:
        """ """
        return self._config_sub_data("xAxis", OptionXAxis)

    @property
    def yAxis(self) -> OptionXAxis:
        """ """
        return self._config_sub_data("yAxis", OptionYAxis)

    @property
    def series(self) -> OptionSeries:
        """ """
        s = self._config_sub_data_enum("series", OptionSeries)
        i = len(self.js_tree["series"]) - 1 % len(self.js_tree["_ek"]['colors'])
        s.color = self.js_tree["_ek"]['colors'][i]
        return s
