#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union
from epyk.core import html
from epyk.interfaces import Arguments
from epyk.core.html import Defaults_html

from epyk.interfaces.graphs import CompChartsApex
from epyk.interfaces.graphs import CompChartsBillboard
from epyk.interfaces.graphs import CompChartsDc
from epyk.interfaces.graphs import CompChartsRoughViz
from epyk.interfaces.graphs import CompChartsFrappe
from epyk.interfaces.graphs import CompChartsChartCss
from epyk.interfaces.graphs import CompChartsC3
from epyk.interfaces.graphs import CompChartsChartJs
from epyk.interfaces.graphs import CompChartsPlotly
from epyk.interfaces.graphs import CompChartsNvd3
from epyk.interfaces.graphs import CompChartsD3
from epyk.interfaces.graphs import CompChartsVis
from epyk.interfaces.graphs import CompChartsVega
from epyk.interfaces.graphs import CompChartsSvg
from epyk.interfaces.graphs import CompChartsCanvas
from epyk.interfaces.graphs import CompChartsGoogle
from epyk.interfaces.graphs import CompChartsSparkline


class Graphs:

  def __init__(self, ui):
    self.page = ui.page
    # Add shortcut to the default charting library
    dflt_chart_fam = getattr(self, html.Defaults.CHART_FAMILY)
    self.pie = dflt_chart_fam.pie
    self.bar = dflt_chart_fam.bar
    self.line = dflt_chart_fam.line

  def plot(self, pkg: str = "apex", record=None, y: list = None, x: str = None, kind: str = "line",
           profile: Union[dict, bool] = None, width: Union[int, tuple] = (100, "%"),
           height: Union[int, tuple] = (Defaults_html.CHARTS_HEIGHT_PX, "px"), options: dict = None,
           html_code: str = None):
    """
    Description:
    ------------
    Generic shortcut to plot a chart in the framework.
    Family and kind of chart are passed in parameter.

    Usage::

    Attributes:
    ----------
    :param pkg: String. Optional. The external chart package reference. Default ApexCharts.
    :param record: List. Optional. The list of dictionaries with the input data.
    :param y: List | String. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param kind: String. Optional. The chart type.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. The width of the component in the page, default (100, '%').
    :param height: Tuple. Optional. The height of the component in the page, default (330, "px").
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    if y is not None and not isinstance(y, list):
      y = [y]
    chart_pkg = getattr(self, pkg)
    return getattr(chart_pkg, kind)(record=record, y_columns=y, x_axis=x, profile=profile, width=width, height=height,
                                    options=options, html_code=html_code)

  def skillbars(self, records=None, y_column: list = None, x_axis: str = None, title: str = None,
                width: Union[int, tuple] = (100, '%'), height: Union[int, tuple] = (None, 'px'), html_code: str = None,
                options: dict = None, profile: Union[dict, bool] = False):
    """
    Description:
    ------------
    Python interface for the HTML Skill bars, simple bars chart done in pure Javascript and CSS.

    :Category: Web Application, Analytics

    Usage::

      records = [
        {"label": 'python', 'value': 12},
        {"label": 'Java', 'value': 5},
        {"label": 'Javascript', 'value': 80}]
      page.ui.charts.skillbars(records, y_column='value', x_axis='label').css({"width": '100px'})

    Related Pages:

      https://www.w3schools.com/howto/howto_css_skill_bar.asp

    Attributes:
    ----------
    :param records: Array<dict>. Optional. The Python list of dictionaries.
    :param y_column: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param title: String. Optional. The chart title.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if y_column is None or x_axis is None:
      raise ValueError("seriesName and axis must be defined")

    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    html_skillbar = html.HtmlEvent.SkillBar(
      self.page, records, y_column, x_axis, title, width, height, html_code, options, profile)
    html.Html.set_component_skin(html_skillbar)
    return html_skillbar

  def sparkline(self, chart_type: str, data, title: str = None, options: dict = None,
                width: Union[int, tuple] = (None, "%"), height: Union[int, tuple] = (None, "px"),
                profile: Union[dict, bool] = False):
    """
    Description:
    ------------
    Display a sparkline component.

    :Category: Web Application, Analytics

    Usage::

      page.ui.charts.sparkline("box", [1, 2, 3, 4, 5, 4, 3, 2, 1])
      page.ui.charts.sparkline("bar", [1, 2, 3, 4, 5, 4, 3, 2, 10])

    Related Pages:

      https://omnipotent.net/jquery.sparkline/#s-about

    Attributes:
    ----------
    :param chart_type: The type of chart (bullet, line, bar, tristate, discrete, pie, box)
    :param data: String. A String corresponding to a JavaScript object.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param title: String. Optional. A panel title. This will be attached to the title property.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.

    :return: A python Sparkline object
    """
    dfl_options = {"type": chart_type}
    if options is not None:
      dfl_options.update(options)
    html_chart = html.graph.GraphSparklines.Sparklines(
      self.page, data, title, width, height, dfl_options, profile)
    html_chart.color(self.page.theme.charts[0])
    html.Html.set_component_skin(html_chart)
    return html_chart

  @property
  def sparklines(self) -> CompChartsSparkline.Sparkline:
    """
    Description:
    ------------
    Display a sparkline component.

    :Category: Web Application, Analytics

    Usage::

      page.ui.charts.sparklinea.box([1, 2, 3, 4, 5, 4, 3, 2, 1])
      page.ui.charts.sparklines.bar([1, 2, 3, 4, 5, 4, 3, 2, 10])

    Related Pages:

      https://plotly.com/javascript/

    :return: A Python Plotly object
    """
    return CompChartsSparkline.Sparkline(self)

  @property
  def plotly(self) -> CompChartsPlotly.Plotly:
    """
    Description:
    ------------
    Built on top of d3.js and stack.gl, Plotly.js is a high-level, declarative charting library.
    plotly.js ships with over 40 chart types, including 3D charts, statistical graphs, and SVG maps.

    :Category: Analytics, Dataviz

    Usage::

    Related Pages:

      https://plotly.com/javascript/

    :return: A Python Plotly object
    """
    return CompChartsPlotly.Plotly(self)

  @property
  def chartJs(self) -> CompChartsChartJs.ChartJs:
    """
    Description:
    ------------
    Simple yet flexible JavaScript charting for designers & developers.

    :Category: Web Application

    Usage::

    Related Pages:

      https://www.chartjs.org/

    :return: A Python ChartJs object
    """
    return CompChartsChartJs.ChartJs(self)

  @property
  def apex(self) -> CompChartsApex.ApexChart:
    """
    Description:
    ------------
    Interface for the ApexChart library.

    :Category: Web application

    Usage::

    Related Pages:

      https://apexcharts.com/

    :return: A Python ChartJs object
    """
    return CompChartsApex.ApexChart(self)

  @property
  def c3(self) -> CompChartsC3.C3:
    """
    Description:
    ------------
    Interface to the JavaScript C3 module.

    :Category: Analytics, Dataviz

    Usage::

      data = page.py.requests.csv(data_urls.DEMO_COUNTRY)
      c3 = page.ui.charts.c3.line(results, y_columns=['Value'], x_axis="Year")

    Related Pages:

      https://c3js.org/

    :return: A Python C3 object
    """
    return CompChartsC3.C3(self)

  @property
  def bb(self) -> CompChartsBillboard.Billboard:
    """
    Description:
    ------------
    Interface to the Javascript Billboard module.

    This will propose various charts for data analysis and visualisation based on D£.
    This project has been forked from C3.js.

    :Category: Analytics, Dataviz

    Usage::

      languages = [
        {"name": 'C', 'type': 'code', 'rating': 17.07, 'change': 12.82},
        {"name": 'Java', 'type': 'code', 'rating': 16.28, 'change': 0.28},
      ]

      c = page.ui.charts.bb.line(languages, y_columns=["rating", 'change'], x_axis='name')

    Related Pages:

      https://naver.github.io/billboard.js/

    :return: A Python Billboard Object
    """
    return CompChartsBillboard.Billboard(self)

  @property
  def billboard(self) -> CompChartsBillboard.Billboard:
    """
    Description:
    ------------
    Interface to the Javascript Billboard module.

    This will propose various charts for data analysis and visualisation based on D£.
    This project has been forked from C3.js.

    :Category: Analytics, Dataviz

    Usage::

      data = page.py.requests.csv(data_urls.DEMO_COUNTRY)
      c3 = page.ui.charts.billboard.bar(results, y_columns=['Value'], x_axis="Year")

    Related Pages:

      https://naver.github.io/billboard.js/

    :return: A Python Billboard Object
    """
    return CompChartsBillboard.Billboard(self)

  @property
  def vis(self) -> CompChartsVis.Vis:
    """
    Description:
    ------------
    A dynamic, browser based visualization library.

    :Category: Analytics, Dataviz

    Usage::

    Related Pages:

      https://visjs.org/

    :return: A Python Vis object
    """
    return CompChartsVis.Vis(self)

  @property
  def nvd3(self) -> CompChartsNvd3.Nvd3:
    """
    Description:
    ------------
    Interface to the Javascript NVD3 library.

    :Category: Analytics, Web application

    Usage::

    Related Pages:

      http://nvd3.org/

    :return: A Python NVD3 object
    """
    return CompChartsNvd3.Nvd3(self)

  @property
  def dc(self) -> CompChartsDc.DC:
    """
    Description:
    ------------
    dc.js is a javascript charting library with native crossfilter support,
    allowing highly efficient exploration on large multi-dimensional datasets (inspired by crossfilter's demo).

    :Category: Analytics, Dataviz

    Usage::

    Related Pages:

      https://dc-js.github.io/dc.js/
    """
    return CompChartsDc.DC(self)

  @property
  def d3(self) -> CompChartsD3.D3:
    """
    Description:
    ------------
    D3.js is a JavaScript library for manipulating documents based on data.

    :Category: Analytics, Dataviz

    Usage::

    Related Pages:

      https://d3js.org/
    """
    return CompChartsD3.D3(self)

  @property
  def google(self) -> CompChartsGoogle.ChartGoogle:
    """
    Description:
    ------------
    Google chart tools are powerful, simple to use, and free.
    Try out our rich gallery of interactive charts and data tools.

    :Category: Analytics, Dataviz

    Usage::

    Related Pages:

      https://developers.google.com/chart
    """
    if not getattr(self.page, '_with_google_imports', False):
      raise ValueError("Google produce must be added using for example page.imports.google_products(['charts'])")

    return CompChartsGoogle.ChartGoogle(self)

  @property
  def svg(self) -> CompChartsSvg.SVG:
    """
    Description:
    ------------
    SVG defines vector-based graphics in XML format.

    Usage::

    Related Pages:

      https://www.w3schools.com/graphics/svg_intro.asp
    """
    return CompChartsSvg.SVG(self)

  @property
  def canvas(self) -> CompChartsCanvas.Canvas:
    """
    Description:
    ------------
    The HTML <canvas> element is used to draw graphics on a web page.

    The graphic to the left is created with <canvas>.
    It shows four elements: a red rectangle, a gradient rectangle, a multicolor rectangle, and a multicolor text.

    Usage::

    Related Pages:

      https://www.w3schools.com/html/html5_canvas.asp
    """
    return CompChartsCanvas.Canvas(self)

  @property
  def roughviz(self) -> CompChartsRoughViz.CompRoughViz:
    """
    Description:
    ------------
    Reusable JavaScript library for creating sketchy/hand-drawn styled charts in the browser.

    :Category: Web application

    Related Pages:

      https://github.com/jwilber/roughViz
    """
    return CompChartsRoughViz.CompRoughViz(self)

  @property
  def frappe(self) -> CompChartsFrappe.CompChartFrappe:
    """
    Description:
    ------------
    GitHub-inspired simple and modern SVG charts for the web with zero dependencies.

    :Category: Web application

    Related Pages:

      https://frappe.io/charts
    """
    return CompChartsFrappe.CompChartFrappe(self)

  @property
  def chartCss(self) -> CompChartsChartCss.CompChartCss:
    """
    Description:
    ------------
    Charts.css is a modern CSS framework. It uses CSS utility classes to style HTML elements as charts.

    :Category: Web application

    Related Pages:

      https://chartscss.org/
    """
    return CompChartsChartCss.CompChartCss(self)

  @property
  def vega(self) -> CompChartsVega.VegaEmbedded:
    """
    Description:
    ------------
    Vega – A Visualization Grammar.

    :Category: Analytics, Dataviz

    Usage::

    Related Pages:

      https://vega.github.io/vega/

    :return: A Python Vega object
    """
    return CompChartsVega.VegaEmbedded(self)

  def menu(self, chart: html.Html.Html, height: Union[int, tuple] = (18, 'px'), options: dict = None,
           post: Union[list, str] = None, profile: Union[dict, bool] = None):
    """
    Description:
    -----------
    Add a standard menu on the table to trigger standard operation (add, empty, copy, download).

    Attributes:
    ----------
    :param chart: The chart component.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param options: Optional. Specific Python options available for this component.
    :param post:
    :param profile: Optional. A flag to set the component performance storage.
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
          icon, align="center", tooltip=typ, height=height, width=(size, 'px'), options=options, profile=profile)
        r.span.style.css.line_height = r.style.css.height
        r.icon.style.css.font_factor(-4)
        r.style.css.font_factor(-3)
        r.style.css.margin_left = 5
        r.style.css.margin_right = 5
        if typ == "Csv":
          r.click([chart.js.download("csv", "data.csv")])
        elif typ == "Clear":
          r.click([chart.js.clearData()])
        menu_items.append(r)
    container = self.page.ui.menu(chart, menu_items=menu_items, copy=False, post=post, editable=False)
    html.Html.set_component_skin(container)
    return container


class Chart2d:

  def __init__(self, ui):
    self.page = ui.page

  @property
  def plotly(self) -> CompChartsPlotly.Plotly2D:
    """
    Description:
    ------------
    Built on top of d3.js and stack.gl, Plotly.js is a high-level, declarative charting library.
    plotly.js ships with over 40 chart types, including 3D charts, statistical graphs, and SVG maps.

    :Category: Analytics, Dataviz

    Usage::

    Related Pages:

      https://plotly.com/javascript/

    :return: A Python Plolty object
    """
    return CompChartsPlotly.Plotly2D(self)

  @property
  def nvd3(self) -> CompChartsNvd3.Nvd3:
    """
    Description:
    ------------
    This project is an attempt to build re-usable charts and chart components for d3.js
    without taking away the power that d3.js gives you.

    :Category: Analytics, Web application

    Usage::

    Related Pages:

      http://nvd3.org/

    :return: A Python NVD3 object
    """
    return CompChartsNvd3.Nvd3(self)

  @property
  def dc(self) -> CompChartsDc.DC:
    """
    Description:
    ------------
    dc.js is a javascript charting library with native crossfilter support, allowing highly
    efficient exploration on large multi-dimensional datasets (inspired by crossfilter's demo).

    :Category: Analytics, Dataviz

    Usage::

    Related Pages:

      https://dc-js.github.io/dc.js/
    """
    return CompChartsDc.DC(self)

  @property
  def d3(self) -> CompChartsD3.D3:
    """
    Description:
    ------------
    D3.js is a JavaScript library for manipulating documents based on data.

    :Category: Analytics, Dataviz

    Usage::

    Related Pages:

      https://d3js.org/
    """
    return CompChartsD3.D3(self)

  @property
  def svg(self) -> CompChartsSvg.SVG:
    """
    Description:
    ------------
    SVG stands for Scalable Vector Graphics.

    SVG defines vector-based graphics in XML format.

    Usage::

    Related Pages:

      https://www.w3schools.com/graphics/svg_intro.asp
    """
    return CompChartsSvg.SVG(self)

  @property
  def canvas(self) -> CompChartsCanvas.Canvas:
    """
    Description:
    ------------
    The HTML <canvas> element is used to draw graphics on a web page.

    The graphic to the left is created with <canvas>.
    It shows four elements: a red rectangle, a gradient rectangle, a multicolor rectangle, and a multicolor text.

    Usage::

    Related Pages:

      https://www.w3schools.com/html/html5_canvas.asp
    """
    return CompChartsCanvas.Canvas(self)

  @property
  def chartJs(self) -> CompChartsChartJs.ChartJs:
    """
    Description:
    ------------
    Interface for the ChartJs library

    :Category: Web application

    Usage::

    Related Pages:

      https://www.chartjs.org/

    :return: A Python ChartJs object
    """
    return CompChartsChartJs.ChartJs(self)

  @property
  def apex(self) -> CompChartsApex.ApexChart:
    """
    Description:
    ------------
    Interface for the ApexChart library.

    :Category: Web application

    Usage::

    Related Pages:

      https://apexcharts.com/

    :return: A Python ChartJs object
    """
    return CompChartsApex.ApexChart(self)

  @property
  def c3(self) -> CompChartsC3.C3:
    """
    Description:
    ------------
    Interface to the JavaScript C3 module.

    :Category: Analytics, Dataviz

    Usage::

    Related Pages:

      https://c3js.org/

    :return: A Python C3 object
    """
    return CompChartsC3.C3(self)

  @property
  def billboard(self) -> CompChartsBillboard.Billboard:
    """
    Description:
    ------------
    Interface to the Javascript Billboard module.

    This will propose various charts for data analysis and visualisation based on D£.
    This project has been forked from Billboard.js.

    :Category: Analytics, Dataviz

    Usage::

    Related Pages:

      https://naver.github.io/billboard.js/

    :return: A Python Billboard Object
    """
    return CompChartsBillboard.Billboard(self)

  @property
  def vis(self) -> CompChartsVis.Vis2D:
    """
    Description:
    ------------
    Interface for the Vis library.

    :Category: Analytics, Dataviz

    Usage::

    Related Pages:

      https://visjs.org/

    :return: A Python Vis object
    """
    return CompChartsVis.Vis2D(self)


class Chart3d:

  def __init__(self, ui):
    self.page = ui.page

  @property
  def plotly(self) -> CompChartsPlotly.Plotly3D:
    """
    Description:
    ------------
    Built on top of d3.js and stack.gl, Plotly.js is a high-level, declarative charting library.
    plotly.js ships with over 40 chart types, including 3D charts, statistical graphs, and SVG maps.

    :Category: Analytics, Dataviz

    Usage::

    Related Pages:

      https://plotly.com/javascript/

    :return: A Python Plolty object
    """
    return CompChartsPlotly.Plotly3D(self)

  @property
  def vis(self) -> CompChartsVis.Vis3D:
    """
    Description:
    ------------
    Interface for the Vis library.

    :Category: Analytics, Dataviz

    Usage::

    Related Pages:

      https://visjs.org/

    :return: A Python Vis object
    """
    return CompChartsVis.Vis3D(self)
