#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List, Optional

from epyk.core.py import types as etypes
from epyk.core.py import primitives
from epyk.core.html import Html
from epyk.core.html.mixins import MixHtmlState
from epyk.core.css.styles.attributes import CssInline
from epyk.core.html.options import OptChartCss


class ChartCss(MixHtmlState.HtmlOverlayStates, Html.Html):
    requirements = ('charts.css',)
    name = 'ChartCss'
    _chart__type = "line"
    _option_cls = OptChartCss.ChartCssOptions

    def __init__(self, page: primitives.PageModel, width, height, html_code, options, profile):
        super(ChartCss, self).__init__(
            page, [], html_code=html_code, profile=profile, options=options,
            css_attrs={"width": width, "height": height})
        self.attr["class"].clear()
        self.attr["class"].add("charts-css %s" % self._chart__type)
        self._datasets, self._labels, self.row_style = [], [], CssInline(page=page)

    @property
    def options(self) -> OptChartCss.ChartCssOptions:
        """
        Set the ChartCss options.

        Related Pages:

          https://chartscss.org/charts/area/
        """
        return super().options

    def labels(self, values: List[str]):
        """
        Set the chart labels.

        :param values: The different values for the x-axis
        """
        self._labels = values

    def dataset(self, i: int = None) -> Optional[list]:
        """
        The data property of a ChartJs chart.

        Related Pages:

          https://www.chartjs.org/docs/master/general/data-structures

        :param i: Optional. The series index according to the y_columns
        """
        if i is None:
            return self._datasets[-1]

    def add_dataset(
            self,
            data: etypes.JS_DATA_TYPES,
            label: str,
            colors: List[str] = None,
            opacity: float = None,
            kind: str = None
    ):
        """
        Add a new Dataset to the chart list of Datasets.

        Usage::

        Related Pages:

          https://www.chartjs.org/docs/latest/developers/updates.html

        :param data: The list of points (float)
        :param label: The list of points (float)
        :param colors: Optional. The color for this series. Default the global definition
        :param opacity: Optional. The opacity level for the content
        """
        self._datasets.append([label] + data)

    def define(self, options: etypes.JS_DATA_TYPES = None, dataflows: List[dict] = None) -> str:
        """ Not yet defined for this chart """
        return ""

    def __str__(self):
        html_frg = [['<th scope="row" style="%s"> %s </th>' % (
            self.row_style, self._labels[i])] for i in range(len(self._datasets[0][1:]))]
        html_frg_head, sections = [], len(self._labels)
        for series in self._datasets:
            for i, y in enumerate(series[1:]):
                html_frg[i].append('<td style="--start: %s; --size: %s"><span class="data"> %s </span></td>' % (
                    i / sections, y / 100, y))
        html_frg_trs = ["".join(frg) for frg in html_frg]
        return '''<table %s><caption>%s</caption><thead>%s</thead><tbody><tr>%s</tr></tbody></table>
      ''' % (self.get_attrs(css_class_names=self.style.get_classes()), self.options.title,
             "".join(html_frg_head), "</tr><tr>".join(html_frg_trs))


class ChartCssBar(ChartCss):
    requirements = ('charts.css',)
    name = 'ChartCss Bar'
    _chart__type = "column"


class ChartCssBarArea(ChartCss):
    requirements = ('charts.css',)
    name = 'ChartCss Area'
    _chart__type = "area"


class ChartCssBarStacked(ChartCssBar):
    requirements = ('charts.css',)
    name = 'ChartCss Stacked Bar'
    _chart__type = "bar"

    def __init__(self, page: primitives.PageModel, width, height, html_code, options, profile):
        super(ChartCssBar, self).__init__(page, width, height, html_code, options, profile)
        self.options.multiple()
        self.attr["class"].add("stacked")
