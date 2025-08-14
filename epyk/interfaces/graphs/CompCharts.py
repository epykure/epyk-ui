#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.py import types
from epyk.core import html
from epyk.core.html import Defaults_html
from epyk.core.css import Defaults_css



class Graphs:

    def __init__(self, ui):
        self.page = ui.page
        # Add shortcut to the default charting library


    def plot(self, pkg: str = "apex", record=None, y: list = None, x: str = None, kind: str = "line",
             profile: types.PROFILE_TYPE = None, width: types.SIZE_TYPE = (100, "%"),
             height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"), options: dict = None,
             html_code: str = None):
        """Generic shortcut to plot a chart in the framework.
        Family and kind of chart are passed in parameter.

        :param pkg: Optional. The external chart package reference. Default ApexCharts
        :param record: Optional. The list of dictionaries with the input data
        :param y: Optional. The columns corresponding to keys in the dictionaries in the record
        :param x: Optional. The column corresponding to a key in the dictionaries in the record
        :param kind: Optional. The chart type
        :param profile:  Optional. A flag to set the component performance storage
        :param width: Optional. The width of the component in the page, default (100, '%')
        :param height: Optional. The height of the component in the page, default (330, "px")
        :param options: Optional. Specific Python options available for this component
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        """
        if y is not None and not isinstance(y, list):
            y = [y]
        chart_pkg = getattr(self, pkg)
        return getattr(chart_pkg, kind)(record=record, y_columns=y, x_axis=x, profile=profile, width=width,
                                        height=height,
                                        options=options, html_code=html_code)
    # 
    #
    # @property
    # def google(self) -> CompChartsGoogle.ChartGoogle:
    #     """Google chart tools are powerful, simple to use, and free.
    #     Try out our rich gallery of interactive charts and data tools.
    #
    #     :Category: Analytics, Dataviz
    #
    #     `Related Pages <https://developers.google.com/chart>`_
    #     """
    #     if not getattr(self.page, '_with_google_imports', False):
    #         raise ValueError("Google produce must be added using for example page.imports.google_products(['charts'])")
    #
    #     return CompChartsGoogle.ChartGoogle(self)

    def menu(self, chart: html.Html.Html, height: types.SIZE_TYPE = (18, 'px'), options: dict = None,
             post: types.JS_FUNCS_TYPES = None, profile: types.PROFILE_TYPE = None) -> html.HtmlContainer.Col:
        """Add a standard menu on the table to trigger standard operation (add, empty, copy, download).

        :param chart: The chart component
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param options: Optional. Specific Python options available for this component
        :param post: Optional.
        :param profile: Optional. A flag to set the component performance storage
        """
        # ("Csv", "fas fa-file-csv")
        commands = [("Clear", "fas fa-trash-alt", 15)]
        menu_items = []
        options = options or {}
        for typ, icon, size in commands:
            if icon:
                if isinstance(icon, tuple):
                    icon = icon[0]
                r = self.page.ui.icons.awesome(
                    icon, align="center", tooltip=typ, height=height, width=(size, 'px'), options=options,
                    profile=profile)
                r.icon.style.css.font_factor(options.get("icon_size", Defaults_css.MENU_ICON_SIZE))
                r.style.css.font_factor(options.get("icon_size", Defaults_css.MENU_ICON_SIZE))
                if typ == "Csv":
                    r.click([chart.js.download(filename="data.csv", format="csv")])
                    r.icon.style.add_classes.div.color_hover()
                elif typ == "Clear":
                    r.click([chart.js.clearData()])
                    r.icon.style.add_classes.div.danger_hover()
                else:
                    r.icon.style.add_classes.div.color_hover()
                menu_items.append(r)
        container = self.page.ui.menu(chart, menu_items=menu_items, copy=False, post=post, editable=False)
        html.Html.set_component_skin(container)
        return container


