#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union, List
from epyk.core.html.options import Options
from epyk.core.html.options import OptionsWithTemplates
from epyk.core.html.options import OptChart


class OptionTitle(Options):

    @property
    def left(self) -> str:
        return self._config_get()

    @left.setter
    def left(self, val: str):
        self._config(val)

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
    def bottom(self) -> int:
        return self._config_get()

    @bottom.setter
    def bottom(self, val: int):
        self._config(val)

    @property
    def data(self) -> list:
        return self._config_get()

    @data.setter
    def data(self, values: list):
        self._config(values)

    @property
    def left(self) -> str:
        return self._config_get()

    @left.setter
    def left(self, val: str):
        self._config(val)

    @property
    def orient(self) -> str:
        return self._config_get()

    @orient.setter
    def orient(self, val: str):
        self._config(val)

    @property
    def right(self) -> int:
        return self._config_get()

    @right.setter
    def right(self, val: int):
        self._config(val)

    @property
    def type(self) -> str:
        return self._config_get()

    @type.setter
    def type(self, val: str):
        self._config(val)

    @property
    def top(self) -> str:
        return self._config_get()

    @top.setter
    def top(self, val: str):
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


class OptionLineStyle(Options):

    @property
    def type(self) -> str:
        return self._config_get()

    @type.setter
    def type(self, val: str):
        self._config(val)

    @property
    def width(self):
        return self._config_get()

    @width.setter
    def width(self, val: int):
        self._config(val)


class OptionSplitLine(Options):

    @property
    def show(self) -> bool:
        return self._config_get()

    @show.setter
    def show(self, val: bool):
        self._config(val)

    @property
    def lineStyle(self) -> OptionLineStyle:
        return self._config_sub_data("lineStyle", OptionLineStyle)


class OptionAxisLine(Options):

    @property
    def show(self) -> bool:
        return self._config_get()

    @show.setter
    def show(self, val: bool):
        self._config(val)


class OptionAxisTick(Options):

    @property
    def alignWithLabel(self) -> bool:
        return self._config_get()

    @alignWithLabel.setter
    def alignWithLabel(self, val: bool):
        self._config(val)

    @property
    def show(self) -> bool:
        return self._config_get()

    @show.setter
    def show(self, val: bool):
        self._config(val)


class OptionAxisLabel(Options):

    @property
    def interval(self) -> int:
        return self._config_get()

    @interval.setter
    def interval(self, val: int):
        self._config(val)

    @property
    def overflow(self) -> str:
        return self._config_get()

    @overflow.setter
    def overflow(self, val: str):
        self._config(val)

    @property
    def rotate(self) -> int:
        return self._config_get()

    @rotate.setter
    def rotate(self, val: int):
        self._config(val)

    @property
    def show(self) -> bool:
        return self._config_get()

    @show.setter
    def show(self, val: bool):
        self._config(val)

    @property
    def width(self) -> int:
        return self._config_get()

    @width.setter
    def width(self, val: int):
        self._config(val)


class OptionSplitArea(Options):

    @property
    def show(self) -> bool:
        return self._config_get()

    @show.setter
    def show(self, val: bool):
        self._config(val)


class OptionAxis(Options):
    @property
    def animationDuration(self) -> int:
        return self._config_get()

    @animationDuration.setter
    def animationDuration(self, val: int):
        self._config(val)

    @property
    def animationDurationUpdate(self) -> int:
        return self._config_get()

    @animationDurationUpdate.setter
    def animationDurationUpdate(self, val: int):
        self._config(val)

    @property
    def axisLabel(self) -> OptionAxisLabel:
        return self._config_sub_data("axisLabel", OptionAxisLabel)

    @property
    def axisLine(self) -> OptionAxisLine:
        return self._config_sub_data("axisLine", OptionAxisLine)

    @property
    def axisTick(self) -> OptionAxisTick:
        return self._config_sub_data("axisTick", OptionAxisTick)

    @property
    def boundaryGap(self):
        return self._config_get()

    @boundaryGap.setter
    def boundaryGap(self, flag: bool):
        self._config(flag)

    @property
    def data(self):
        return self._config_get()

    @data.setter
    def data(self, val):
        self._config(val)

    @property
    def inverse(self) -> bool:
        return self._config_get()

    @inverse.setter
    def inverse(self, flag: bool):
        self._config(flag)

    @property
    def max(self) -> int:
        return self._config_get()

    @max.setter
    def max(self, num: int):
        self._config(num)

    @property
    def min(self) -> int:
        return self._config_get()

    @min.setter
    def min(self, num: int):
        self._config(num)

    @property
    def minInterval(self) -> int:
        return self._config_get()

    @minInterval.setter
    def minInterval(self, num: int):
        self._config(num)

    @property
    def name(self) -> str:
        return self._config_get()

    @name.setter
    def name(self, val: str):
        self._config(val)

    @property
    def nameGap(self) -> int:
        """The gap between axisName and axisLine."""
        return self._config_get()

    @nameGap.setter
    def nameGap(self, val: int):
        self._config(val)

    @property
    def nameLocation(self) -> str:
        return self._config_get()

    @nameLocation.setter
    def nameLocation(self, val: str):
        self._config(val)

    @property
    def nameRotate(self) -> int:
        """By degree. By default auto rotate by nameLocation."""
        return self._config_get()

    @nameRotate.setter
    def nameRotate(self, val: int):
        self._config(val)

    @property
    def nameTruncate(self) -> dict:
        """By degree. By default auto rotate by nameLocation."""
        return self._config_get()

    @nameTruncate.setter
    def nameTruncate(self, valS: dict):
        self._config(valS)

    @property
    def position(self) -> str:
        return self._config_get()

    @position.setter
    def position(self, val: str):
        self._config(val)

    @property
    def scale(self) -> bool:
        return self._config_get()

    @scale.setter
    def scale(self, flag: bool):
        self._config(flag)

    @property
    def show(self) -> bool:
        return self._config_get()

    @show.setter
    def show(self, flag: bool):
        self._config(flag)

    @property
    def splitArea(self) -> OptionSplitArea:
        return self._config_sub_data("splitArea", OptionSplitArea)

    @property
    def splitLine(self) -> OptionSplitLine:
        return self._config_sub_data("splitLine", OptionSplitLine)

    @property
    def splitNumber(self) -> int:
        return self._config_get()

    @splitNumber.setter
    def splitNumber(self, num: int):
        self._config(num)

    @property
    def type(self):
        return self._config_get()

    @type.setter
    def type(self, val):
        self._config(val)

    @property
    def z(self) -> int:
        """z level: 0,"""
        return self._config_get(0)

    @z.setter
    def z(self, val: int):
        self._config(val)


class OptionYAxis(OptionAxis):
    ...


class OptionXAxis(OptionAxis):
    ...


class OptionAxisPointer(Options):

    @property
    def type(self) -> str:
        return self._config_get()

    @type.setter
    def type(self, val: str):
        self._config(val)


class OptionTooltip(Options):

    @property
    def axisPointer(self) -> OptionAxisPointer:
        return self._config_sub_data("axisPointer", OptionAxisPointer)

    @property
    def trigger(self):
        return self._config_get()

    @trigger.setter
    def trigger(self, val):
        self._config(val)


class OptionStyleNormal(Options):

    @property
    def areaColor(self):
        return self._config_get()

    @areaColor.setter
    def areaColor(self, val: str):
        self._config(val)

    @property
    def borderColor(self) -> str:
        return self._config_get()

    @borderColor.setter
    def borderColor(self, val: str):
        self._config(val)

    @property
    def borderWidth(self) -> int:
        return self._config_get()

    @borderWidth.setter
    def borderWidth(self, val: int):
        self._config(val)

    @property
    def color(self) -> str:
        return self._config_get()

    @color.setter
    def color(self, val: str):
        self._config(val)

    @property
    def fontSize(self) -> str:
        return self._config_get()

    @fontSize.setter
    def fontSize(self, val: str):
        self._config(val)

    @property
    def shadowOffsetX(self) -> int:
        return self._config_get()

    @shadowOffsetX.setter
    def shadowOffsetX(self, val: int):
        self._config(val)

    @property
    def shadowOffsetY(self) -> int:
        return self._config_get()

    @shadowOffsetY.setter
    def shadowOffsetY(self, val: int):
        self._config(val)

    @property
    def show(self) -> bool:
        return self._config_get()

    @show.setter
    def show(self, val: bool):
        self._config(val)


class OptionItemStyle(Options):

    @property
    def borderColor(self) -> str:
        return self._config_get()

    @borderColor.setter
    def borderColor(self, val: str):
        self._config(val)

    @property
    def borderRadius(self) -> int:
        return self._config_get()

    @borderRadius.setter
    def borderRadius(self, val: int):
        self._config(val)

    @property
    def borderWidth(self) -> int:
        return self._config_get()

    @borderWidth.setter
    def borderWidth(self, val: int):
        self._config(val)

    @property
    def emphasis(self) -> OptionStyleNormal:
        return self._config_sub_data("emphasis", OptionEmphasis)

    @property
    def normal(self) -> OptionStyleNormal:
        return self._config_sub_data("normal", OptionStyleNormal)

    @property
    def shadowBlur(self) -> int:
        return self._config_get()

    @shadowBlur.setter
    def shadowBlur(self, val: int):
        self._config(val)

    @property
    def shadowColor(self) -> str:
        return self._config_get()

    @shadowColor.setter
    def shadowColor(self, val: str):
        self._config(val)

    @property
    def shadowOffsetX(self) -> int:
        return self._config_get()

    @shadowOffsetX.setter
    def shadowOffsetX(self, val: int):
        self._config(val)


class OptionTime(Options):

    @property
    def color(self) -> str:
        return self._config_get()

    @color.setter
    def color(self, val: str):
        self._config(val)

    @property
    def fontSize(self) -> str:
        return self._config_get()

    @fontSize.setter
    def fontSize(self, val: str):
        self._config(val)


class OptionRich(Options):

    @property
    def time(self) -> OptionTime:
        return self._config_sub_data("time", OptionTime)


class OptionLabel(Options):

    @property
    def alignTo(self) -> str:
        return self._config_get()

    @alignTo.setter
    def alignTo(self, val: str):
        self._config(val)

    @property
    def edgeDistance(self) -> int:
        return self._config_get()

    @edgeDistance.setter
    def edgeDistance(self, val: int):
        self._config(val)

    @property
    def fontSize(self) -> int:
        return self._config_get()

    @fontSize.setter
    def fontSize(self, val: int):
        self._config(val)

    @property
    def formatter(self) -> str:
        return self._config_get()

    @formatter.setter
    def formatter(self, val: str):
        self._config(val)

    @property
    def fontWeight(self) -> str:
        return self._config_get()

    @fontWeight.setter
    def fontWeight(self, val: str):
        self._config(val)

    @property
    def lineHeight(self) -> int:
        return self._config_get()

    @lineHeight.setter
    def lineHeight(self, val: int):
        self._config(val)

    @property
    def minMargin(self) -> int:
        return self._config_get()

    @minMargin.setter
    def minMargin(self, val: int):
        self._config(val)

    @property
    def position(self) -> str:
        return self._config_get()

    @position.setter
    def position(self, val: str):
        self._config(val)

    @property
    def rich(self) -> OptionRich:
        return self._config_sub_data("rich", OptionRich)

    @property
    def show(self) -> bool:
        return self._config_get()

    @show.setter
    def show(self, flag: bool):
        self._config(flag)


class OptionLLabelLine(Options):

    @property
    def show(self) -> bool:
        return self._config_get()

    @show.setter
    def show(self, flag: bool):
        self._config(flag)


class OptionEmphasis(OptionStyleNormal):

    @property
    def focus(self):
        return self._config_get()

    @focus.setter
    def focus(self, val: str):
        self._config(val)

    @property
    def itemStyle(self) -> OptionItemStyle:
        return self._config_sub_data("itemStyle", OptionItemStyle)

    @property
    def label(self) -> OptionLabel:
        return self._config_sub_data("label", OptionLabel)


class OptionEncode(Options):

    @property
    def itemName(self):
        return self._config_get()

    @itemName.setter
    def itemName(self, val: str):
        self._config(val)

    @property
    def label(self):
        return self._config_get()

    @label.setter
    def label(self, val: List[str]):
        self._config(val)

    @property
    def tooltip(self):
        return self._config_get()

    @tooltip.setter
    def tooltip(self, val: List[str]):
        self._config(val)

    @property
    def x(self):
        return self._config_get()

    @x.setter
    def x(self, val: str):
        self._config(val)

    @property
    def y(self):
        return self._config_get()

    @y.setter
    def y(self, val: str):
        self._config(val)


class OptionSeries(Options):

    @property
    def areaStyle(self):
        return self._config_get()

    @areaStyle.setter
    def areaStyle(self, val: str):
        self._config(val)

    @property
    def bottom(self) -> int:
        return self._config_get()

    @bottom.setter
    def bottom(self, val: int):
        self._config(val)

    @property
    def center(self) -> str:
        return self._config_get()

    @center.setter
    def center(self, val: Union[int, str, list]):
        if isinstance(val, (int, float)):
            self._config("%s%%" % val)
        else:
            self._config(val)

    @property
    def color(self):
        return self._config_get()

    @color.setter
    def color(self, val):
        self._config(val)

    @property
    def data(self) -> list:
        return self._config_get()

    @data.setter
    def data(self, vals: list):
        self._config(vals)

    @property
    def datasetIndex(self) -> int:
        return self._config_get()

    @datasetIndex.setter
    def datasetIndex(self, num: int):
        self._config(num)

    @property
    def emphasis(self) -> OptionEmphasis:
        return self._config_sub_data("emphasis", OptionEmphasis)

    @property
    def encode(self) -> OptionEncode:
        """ """
        return self._config_sub_data("encode", OptionEncode)

    @property
    def endAngle(self) -> float:
        return self._config_get()

    @endAngle.setter
    def endAngle(self, vals: float):
        self._config(vals)

    @property
    def itemStyle(self) -> OptionItemStyle:
        return self._config_sub_data("itemStyle", OptionItemStyle)

    @property
    def label(self) -> OptionLabel:
        return self._config_sub_data("label", OptionLabel)

    @property
    def labelLine(self):
        return self._config_sub_data("labelLine", OptionLLabelLine)

    @property
    def left(self) -> str:
        return self._config_get()

    @left.setter
    def left(self, val: str):
        self._config(val)

    @property
    def levels(self) -> list:
        return self._config_get()

    @levels.setter
    def levels(self, values: list):
        self._config(values)

    @property
    def lineStyle(self) -> OptionLineStyle:
        return self._config_sub_data("lineStyle", OptionLineStyle)

    @property
    def name(self):
        return self._config_get()

    @name.setter
    def name(self, val):
        self._config(val)

    @property
    def markLine(self):
        return self._config_get()

    @markLine.setter
    def markLine(self, values):
        self._config(values)

    @property
    def radius(self) -> list:
        return self._config_get()

    @radius.setter
    def radius(self, values: list):
        self._config(values)

    @property
    def right(self) -> str:
        return self._config_get()

    @right.setter
    def right(self, val: str):
        self._config(val)

    @property
    def roseType(self) -> str:
        return self._config_get()

    @roseType.setter
    def roseType(self, val: str):
        self._config(val)

    @property
    def selectedMode(self) -> str:
        return self._config_get()

    @selectedMode.setter
    def selectedMode(self, vals: str):
        self._config(vals)

    @property
    def stack(self) -> str:
        return self._config_get()

    @stack.setter
    def stack(self, vals: str):
        self._config(vals)

    @property
    def startAngle(self) -> float:
        return self._config_get()

    @startAngle.setter
    def startAngle(self, vals: float):
        self._config(vals)

    @property
    def top(self) -> str:
        return self._config_get()

    @top.setter
    def top(self, val: str):
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

    @property
    def radius(self) -> str:
        return self._config_get()

    @radius.setter
    def radius(self, val: Union[int, str, list]):
        if isinstance(val, (int, float)):
            self._config("%s%%" % val)
        else:
            self._config(val)

    @property
    def width(self) -> int:
        return self._config_get()

    @width.setter
    def width(self, num: int):
        self._config(num)


class OptionToolBoxDataZoom(Options):

    @property
    def yAxisIndex(self) -> str:
        return self._config_get()

    @yAxisIndex.setter
    def yAxisIndex(self, val: str):
        self._config(val)


class OptionDataView(Options):

    @property
    def show(self) -> bool:
        return self._config_get()

    @show.setter
    def show(self, val: bool):
        self._config(val)

    @property
    def readOnly(self) -> bool:
        return self._config_get()

    @readOnly.setter
    def readOnly(self, val: bool):
        self._config(val)


class OptionFeature(Options):

    @property
    def restore(self):
        return self._config_get()

    @restore.setter
    def restore(self, val: str):
        self._config(val)

    @property
    def saveAsImage(self) -> str:
        return self._config_get()

    @saveAsImage.setter
    def saveAsImage(self, val: str):
        self._config(val)

    @property
    def dataView(self) -> OptionDataView:
        """ """
        return self._config_sub_data("dataView", OptionDataView)

    @property
    def dataZoom(self) -> OptionToolBoxDataZoom:
        """ """
        return self._config_sub_data("dataZoom", OptionToolBoxDataZoom)


class OptionToolbox(Options):

    @property
    def feature(self) -> OptionFeature:
        """ """
        return self._config_sub_data("feature", OptionFeature)

    @property
    def order(self) -> str:
        return self._config_get()

    @order.setter
    def order(self, val: str):
        self._config(val)

    @property
    def show(self) -> bool:
        return self._config_get()

    @show.setter
    def show(self, val: bool):
        self._config(val)

    @property
    def trigger(self) -> str:
        return self._config_get()

    @trigger.setter
    def trigger(self, val: str):
        self._config(val)

    @property
    def triggerOn(self) -> str:
        return self._config_get()

    @triggerOn.setter
    def triggerOn(self, val: str):
        self._config(val)


class OptionTimeline(Options):

    @property
    def autoPlay(self) -> bool:
        return self._config_get()

    @autoPlay.setter
    def autoPlay(self, flag: bool):
        self._config(flag)

    @property
    def axisType(self) -> str:
        return self._config_get()

    @axisType.setter
    def axisType(self, val: str):
        self._config(val)

    @property
    def bottom(self) -> int:
        return self._config_get()

    @bottom.setter
    def bottom(self, val: int):
        self._config(val)

    @property
    def data(self) -> list:
        return self._config_get()

    @data.setter
    def data(self, values: list):
        self._config(values)

    @property
    def height(self) -> int:
        return self._config_get()

    @height.setter
    def height(self, val: int):
        self._config(val)

    @property
    def inverse(self) -> bool:
        return self._config_get()

    @inverse.setter
    def inverse(self, flag: bool):
        self._config(flag)

    @property
    def left(self) -> int:
        return self._config_get()

    @left.setter
    def left(self, val: int):
        self._config(val)

    @property
    def orient(self) -> str:
        return self._config_get()

    @orient.setter
    def orient(self, val: str):
        self._config(val)

    @property
    def playInterval(self) -> int:
        return self._config_get()

    @playInterval.setter
    def playInterval(self, val: int):
        self._config(val)

    @property
    def right(self) -> int:
        return self._config_get()

    @right.setter
    def right(self, val: int):
        self._config(val)

    @property
    def symbol(self) -> str:
        return self._config_get()

    @symbol.setter
    def symbol(self, val: str):
        self._config(val)

    @property
    def top(self) -> int:
        return self._config_get()

    @top.setter
    def top(self, val: int):
        self._config(val)

    @property
    def width(self) -> int:
        return self._config_get()

    @width.setter
    def width(self, val: int):
        self._config(val)


class OptionsBaseOption(Options):

    @property
    def animationDuration(self) -> int:
        return self._config_get()

    @animationDuration.setter
    def animationDuration(self, num: int):
        self._config(num)

    @property
    def animationDurationUpdate(self) -> int:
        return self._config_get()

    @animationDurationUpdate.setter
    def animationDurationUpdate(self, num: int):
        self._config(num)

    @property
    def animationEasing(self) -> str:
        return self._config_get()

    @animationEasing.setter
    def animationEasing(self, val: str):
        self._config(val)

    @property
    def animationEasingUpdate(self) -> str:
        return self._config_get()

    @animationEasingUpdate.setter
    def animationEasingUpdate(self, val: str):
        self._config(val)

    @property
    def grid(self) -> bool:
        """Shortcut to set list of titles"""
        return self._config_get()

    @grid.setter
    def grid(self, values: list):
        self._config(values)

    @property
    def options(self) -> bool:
        """"""
        return self._config_get()

    @options.setter
    def options(self, values: list):
        self._config(values)

    @property
    def timeline(self) -> OptionTimeline:
        """ """
        return self._config_sub_data("timeline", OptionTimeline)

    @property
    def title(self) -> bool:
        return self._config_get()

    @title.setter
    def title(self, values: Union[dict, list]):
        self._config(values)

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
    def visualMap(self) -> List[dict]:
        return self._config_get()

    @visualMap.setter
    def visualMap(self, val: List[dict]):
        self._config(val)


class EChartOptions(OptionsWithTemplates):

    @property
    def animationDuration(self) -> int:
        return self._config_get()

    @animationDuration.setter
    def animationDuration(self, num: int):
        self._config(num)

    @property
    def animationDurationUpdate(self) -> int:
        return self._config_get()

    @animationDurationUpdate.setter
    def animationDurationUpdate(self, num: int):
        self._config(num)

    @property
    def animationEasing(self) -> str:
        return self._config_get()

    @animationEasing.setter
    def animationEasing(self, val: str):
        self._config(val)

    @property
    def animationEasingUpdate(self) -> str:
        return self._config_get()

    @animationEasingUpdate.setter
    def animationEasingUpdate(self, val: str):
        self._config(val)

    @property
    def baseOption(self) -> OptionsBaseOption:
        """Core attributes for all charting libraries"""
        return self._config_sub_data("baseOption", OptionsBaseOption)

    @property
    def dataset(self) -> List[dict]:
        return self._config_get()

    @dataset.setter
    def dataset(self, val: List[dict]):
        self._config(val)

    @property
    def dataZoom(self) -> List[dict]:
        return self._config_get()

    @dataZoom.setter
    def dataZoom(self, val: List[dict]):
        self._config(val)

    @property
    def ek(self) -> OptChart.OptionsCoreChart:
        """Core attributes for all charting libraries"""
        return self._config_sub_data("_ek", OptChart.OptionsCoreChart)

    @property
    def graphic(self) -> bool:
        return self._config_get()

    @graphic.setter
    def graphic(self, values: Union[dict, list]):
        self._config(values)

    @property
    def grid(self) -> bool:
        """Shortcut to set list of titles"""
        return self._config_get()

    @grid.setter
    def grid(self, values: list):
        self._config(values)

    @property
    def timeline(self) -> OptionTimeline:
        """ """
        return self._config_sub_data("timeline", OptionTimeline)

    @property
    def title(self) -> bool:
        return self._config_get()

    @title.setter
    def title(self, values: Union[dict, list]):
        self._config(values)

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
        if self.ek.chart.type in ("pie", "radar"):
            s.color = self.ek.colors
        else:
            i = len(self.js_tree["series"]) - 1 % len(self.ek.colors)
            s.color = self.ek.colors[i]
        return s

    def setXAxis(self, values):
        """Set the X Axis definition

        :param values: the X axis values
        """
        self._config(values, name="xAxis")

    def setYAxis(self, values):
        """Set the Y Axis definition

        :param values: the Y axis values
        """
        self._config(values, name="yAxis")

    @property
    def visualMap(self) -> List[dict]:
        return self._config_get()

    @visualMap.setter
    def visualMap(self, val: List[dict]):
        self._config(val)


class OptionRadar(Options):

    @property
    def indicator(self) -> List[dict]:
        return self._config_get()

    @indicator.setter
    def indicator(self, val: List[dict]):
        self._config(val)


class EChartRadarOptions(EChartOptions):

    @property
    def radar(self) -> OptionRadar:
        """ """
        return self._config_sub_data("radar", OptionRadar)


class EChartTreeOptions(EChartOptions):

    @property
    def series(self) -> OptionSeries:
        return self._config_sub_data("series", OptionSeries)


class EChartSankeyOptions(EChartOptions):
    ...


class OptionGeoLabel(Options):

    @property
    def emphasis(self) -> OptionEmphasis:
        return self._config_sub_data("emphasis", OptionEmphasis)

    @property
    def normal(self) -> OptionStyleNormal:
        return self._config_sub_data("normal", OptionStyleNormal)


class OptionGeoScaleLimit(Options):

    @property
    def max(self) -> int:
        return self._config_get()

    @max.setter
    def max(self, val: int):
        self._config(val)

    @property
    def min(self) -> int:
        return self._config_get()

    @min.setter
    def min(self, val: int):
        self._config(val)


class OptionGeo(Options):

    @property
    def label(self) -> OptionGeoLabel:
        """ """
        return self._config_sub_data("label", OptionGeoLabel)

    @property
    def map(self) -> str:
        return self._config_get()

    @map.setter
    def map(self, val: str):
        self._config(val)

    @property
    def roam(self) -> bool:
        return self._config_get()

    @roam.setter
    def roam(self, flag: bool):
        self._config(flag)

    @property
    def scaleLimit(self) -> OptionGeoScaleLimit:
        """ """
        return self._config_sub_data("scaleLimit", OptionGeoScaleLimit)

    @property
    def silent(self) -> bool:
        return self._config_get()

    @silent.setter
    def silent(self, flag: bool):
        self._config(flag)

    @property
    def zoom(self) -> bool:
        return self._config_get()

    @zoom.setter
    def zoom(self, flag: bool):
        self._config(flag)


class OptionPostEffect(Options):

    @property
    def enable(self) -> bool:
        return self._config_get()

    @enable.setter
    def enable(self, val: bool):
        self._config(val)


class OptionGeoSeries(OptionSeries):

    @property
    def blendMode(self) -> str:
        return self._config_get()

    @blendMode.setter
    def blendMode(self, val: str):
        self._config(val)

    @property
    def coordinateSystem(self) -> str:
        return self._config_get()

    @coordinateSystem.setter
    def coordinateSystem(self, val: str):
        self._config(val)

    @property
    def dimensions(self) -> list:
        return self._config_get()

    @dimensions.setter
    def dimensions(self, val: list):
        self._config(val)

    @property
    def geoIndex(self) -> int:
        return self._config_get()

    @geoIndex.setter
    def geoIndex(self, val: int):
        self._config(val)

    @property
    def large(self) -> bool:
        return self._config_get()

    @large.setter
    def large(self, val: bool):
        self._config(val)

    @property
    def postEffect(self) -> OptionPostEffect:
        """ """
        return self._config_sub_data("postEffect", OptionPostEffect)

    @property
    def progressive(self) -> int:
        return self._config_get()

    @progressive.setter
    def progressive(self, val: int):
        self._config(val)

    @property
    def zoomScale(self) -> float:
        return self._config_get()

    @zoomScale.setter
    def zoomScale(self, val: float):
        self._config(val)


class EChartGeoOptions(EChartOptions):

    @property
    def geo(self) -> OptionGeo:
        """ """
        return self._config_sub_data("geo", OptionGeo)

    @property
    def series(self) -> OptionGeoSeries:
        """ """
        s = self._config_sub_data_enum("series", OptionGeoSeries)
        i = len(self.js_tree["series"]) - 1 % len(self.js_tree["_ek"]['colors'])
        if self.js_tree["_ek"]['chart']["type"] in ("pie", "radar"):
            s.color = self.js_tree["_ek"]['colors']
        else:
            s.color = self.js_tree["_ek"]['colors'][i]
        return s