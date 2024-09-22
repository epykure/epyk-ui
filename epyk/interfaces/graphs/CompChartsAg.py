#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.py import types
from epyk.core.html import graph
from epyk.interfaces import Arguments
from epyk.core.html import Defaults_html
from epyk.core.js import JsUtils


class AgCharts:

    def __init__(self, ui):
        self.page = ui.page
        self.chartFamily = "AgCharts"

    def plot(self, record=None, y: list = None, x: str = None, kind: str = "line", profile: types.PROFILE_TYPE = None,
             width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
             options: dict = None, html_code: str = None, **kwargs):
        """

        :tags:
        :categories:

        :param record: Optional. The list of dictionaries with the input data
        :param y: Optional. The columns corresponding to keys in the dictionaries in the record
        :param x: Optional. The column corresponding to a key in the dictionaries in the record
        :param kind: Optional. The chart type
        :param profile: Optional. A flag to set the component performance storage
        :param width: Optional. The width of the component in the page, default (100, '%')
        :param height: Optional. The height of the component in the page, default (330, "px")
        :param options: Optional. Specific Python options available for this component
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        """
        if y is not None and not isinstance(y, list) and not JsUtils.isJsData(y):
            y = [y]
        options = options or {}
        options["series"] = [{"type": kind, "xKey": x, "yKey": s} for s in y]
        return graph.GraphAgCharts.Chart(self.page, record, width, height, html_code, options, profile)
