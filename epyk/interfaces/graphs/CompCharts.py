#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.py import types
from epyk.core import html
from epyk.interfaces import Arguments
from epyk.core.html import Defaults_html
from epyk.core.css import Defaults_css

from epyk.interfaces.graphs import CompChartsApex
from epyk.interfaces.graphs import CompChartist
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
from epyk.interfaces.graphs import CompChartsHighcharts


class Graphs:

  def __init__(self, ui):
    self.page = ui.page
    # Add shortcut to the default charting library
    dflt_chart_fam = getattr(self, html.Defaults.CHART_FAMILY)
    self.pie = dflt_chart_fam.pie
    self.bar = dflt_chart_fam.bar
    self.line = dflt_chart_fam.line

  def plot(self, pkg: str = "apex", record=None, y: list = None, x: str = None, kind: str = "line",
           profile: types.PROFILE_TYPE = None, width: types.SIZE_TYPE = (100, "%"),
           height: types.SIZE_TYPE = (Defaults_html.CHARTS_HEIGHT_PX, "px"), options: dict = None,
           html_code: str = None):
    """
    Generic shortcut to plot a chart in the framework.
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
    return getattr(chart_pkg, kind)(record=record, y_columns=y, x_axis=x, profile=profile, width=width, height=height,
                                    options=options, html_code=html_code)

  def skillbars(self, records=None, y_column: str = None, x_axis: str = None, title: str = None,
                width: types.SIZE_TYPE = (100, '%'), height: types.SIZE_TYPE = (None, 'px'), html_code: str = None,
                options: dict = None, profile: types.PROFILE_TYPE = False) -> html.HtmlEvent.SkillBar:
    """
    Python interface for the HTML Skill bars, simple bars chart done in pure Javascript and CSS.

    :Category: Web Application, Analytics

    Usage::

      records = [
        {"label": 'python', 'value': 12}, {"label": 'Java', 'value': 5}, {"label": 'Javascript', 'value': 80}]
      page.ui.charts.skillbars(records, y_column='value', x_axis='label').css({"width": '100px'})

      s3 = page.ui.charts.skillbars(records, y_column='value', x_axis='label')
      s3.options.height = "10px"

    `Related Pages <https://www.w3schools.com/howto/howto_css_skill_bar.asp>`_
 
    :param records: Optional. The Python list of dictionaries
    :param y_column: Optional. The columns corresponding to keys in the dictionaries in the record
    :param x_axis: Optional. The column corresponding to a key in the dictionaries in the record
    :param title: Optional. The chart title
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    if y_column is None or x_axis is None:
      raise ValueError("seriesName and axis must be defined")

    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    html_skillbar = html.HtmlEvent.SkillBar(
      self.page, records or [], y_column, x_axis, title, width, height, html_code, options, profile)
    html.Html.set_component_skin(html_skillbar)
    return html_skillbar

  def sparkline(self, chart_type: str, data, title: str = None, options: dict = None,
                width: types.SIZE_TYPE = (None, "%"), height: types.SIZE_TYPE = (None, "px"),
                profile: types.PROFILE_TYPE = False) -> html.graph.GraphSparklines.Sparklines:
    """
    Display a sparkline component.

    :Category: Web Application, Analytics

    Usage::

      page.ui.charts.sparkline("box", [1, 2, 3, 4, 5, 4, 3, 2, 1])
      page.ui.charts.sparkline("bar", [1, 2, 3, 4, 5, 4, 3, 2, 10])
      chart = page.ui.charts.sparkline("line", [1, 2, 3, 4, 5, 4, 3, 2, 10])
      chart.click([
        page.js.console.log(chart.dom.val),
        page.js.console.log(chart.dom.content),
        page.js.console.log(chart.dom.offset)
      ])

    `Related Pages <https://omnipotent.net/jquery.sparkline/#s-about>`_

    :param chart_type: The type of chart (bullet, line, bar, tristate, discrete, pie, box)
    :param data: A String corresponding to a JavaScript object
    :param options: Optional. Specific Python options available for this component
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param title: Optional. A panel title. This will be attached to the title property
    :param profile: Optional. A flag to set the component performance storage

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
  def highcharts(self) -> CompChartsHighcharts.Highcharts:
    """
    Highcharts JS is a JavaScript charting library based on SVG and some canvas/WebGL.

    Usage::

      chart = page.ui.charts.highcharts.line()

    `Related Pages <https://github.com/highcharts/highcharts>`_
    """
    return CompChartsHighcharts.Highcharts(self)

  @property
  def chartist(self) -> CompChartist.Chartist:
    """
    You may think that this is just yet an other charting library.
    But Chartist.js is the product of a community that was disappointed about the abilities provided by other
    charting libraries.
    Of course there are hundreds of other great charting libraries but after using them there were always tweaks you
    would have wished for that were not included.

    Usage::

      chart = page.ui.charts.chartist.line()

    `Related Pages <https://gionkunz.github.io/chartist-js/?utm_source=cdnjs&utm_medium=cdnjs_link&utm_campaign=cdnjs_library>`_
    """
    return CompChartist.Chartist(self)

  @property
  def sparklines(self) -> CompChartsSparkline.Sparkline:
    """
    Display a sparkline component.

    :Category: Web Application, Analytics

    Usage::

      page.ui.charts.sparklinea.box([1, 2, 3, 4, 5, 4, 3, 2, 1])
      page.ui.charts.sparklines.bar([1, 2, 3, 4, 5, 4, 3, 2, 10])

    `Related Pages <https://plotly.com/javascript/>`_
    """
    return CompChartsSparkline.Sparkline(self)

  @property
  def plotly(self) -> CompChartsPlotly.Plotly:
    """
    Built on top of d3.js and stack.gl, Plotly.js is a high-level, declarative charting library.
    plotly.js ships with over 40 chart types, including 3D charts, statistical graphs, and SVG maps.

    :Category: Analytics, Dataviz

    `Related Pages <https://plotly.com/javascript/>`_

    :return: A Python Plotly object
    """
    return CompChartsPlotly.Plotly(self)

  @property
  def chartJs(self) -> CompChartsChartJs.ChartJs:
    """
    Simple yet flexible JavaScript charting for designers & developers.

    :Category: Web Application

    `Related Pages <https://www.chartjs.org/>`_

    :return: A Python ChartJs object
    """
    return CompChartsChartJs.ChartJs(self)

  @property
  def apex(self) -> CompChartsApex.ApexChart:
    """
    Interface for the ApexChart library.

    :Category: Web application

    `Related Pages <https://apexcharts.com/>`_
    """
    return CompChartsApex.ApexChart(self)

  @property
  def c3(self) -> CompChartsC3.C3:
    """
    Interface to the JavaScript C3 module.

    :Category: Analytics, Dataviz

    Usage::

      data = page.py.requests.csv(data_urls.DEMO_COUNTRY)
      c3 = page.ui.charts.c3.line(results, y_columns=['Value'], x_axis="Year")

    `Related Pages <https://c3js.org/>`_
    """
    return CompChartsC3.C3(self)

  @property
  def bb(self) -> CompChartsBillboard.Billboard:
    """
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

    `Related Pages <https://naver.github.io/billboard.js/>`_
    """
    return CompChartsBillboard.Billboard(self)

  @property
  def billboard(self) -> CompChartsBillboard.Billboard:
    """
    Interface to the Javascript Billboard module.

    This will propose various charts for data analysis and visualisation based on D£.
    This project has been forked from C3.js.

    :Category: Analytics, Dataviz

    Usage::

      data = page.py.requests.csv(data_urls.DEMO_COUNTRY)
      c3 = page.ui.charts.billboard.bar(results, y_columns=['Value'], x_axis="Year")

    `Related Pages <https://naver.github.io/billboard.js/>`_
    """
    return CompChartsBillboard.Billboard(self)

  @property
  def vis(self) -> CompChartsVis.Vis:
    """
    A dynamic, browser based visualization library.

    :Category: Analytics, Dataviz

    `Related Pages <https://visjs.org/>`_
    """
    return CompChartsVis.Vis(self)

  @property
  def nvd3(self) -> CompChartsNvd3.Nvd3:
    """
    Interface to the Javascript NVD3 library.

    :Category: Analytics, Web application

    `Related Pages <http://nvd3.org/>`_
    """
    return CompChartsNvd3.Nvd3(self)

  @property
  def dc(self) -> CompChartsDc.DC:
    """
    dc.js is a javascript charting library with native crossfilter support,
    allowing highly efficient exploration on large multi-dimensional datasets (inspired by crossfilter's demo).

    :Category: Analytics, Dataviz

    `Related Pages <https://dc-js.github.io/dc.js/>`_
    """
    return CompChartsDc.DC(self)

  @property
  def d3(self) -> CompChartsD3.D3:
    """
    D3.js is a JavaScript library for manipulating documents based on data.

    :Category: Analytics, Dataviz

    `Related Pages <https://d3js.org/>`_
    """
    return CompChartsD3.D3(self)

  @property
  def google(self) -> CompChartsGoogle.ChartGoogle:
    """
    Google chart tools are powerful, simple to use, and free.
    Try out our rich gallery of interactive charts and data tools.

    :Category: Analytics, Dataviz

    `Related Pages <https://developers.google.com/chart>`_
    """
    if not getattr(self.page, '_with_google_imports', False):
      raise ValueError("Google produce must be added using for example page.imports.google_products(['charts'])")

    return CompChartsGoogle.ChartGoogle(self)

  @property
  def svg(self) -> CompChartsSvg.SVG:
    """
    SVG defines vector-based graphics in XML format.

    `Related Pages <https://www.w3schools.com/graphics/svg_intro.asp>`_
    """
    return CompChartsSvg.SVG(self)

  @property
  def canvas(self) -> CompChartsCanvas.Canvas:
    """
    The HTML <canvas> element is used to draw graphics on a web page.

    The graphic to the left is created with <canvas>.
    It shows four elements: a red rectangle, a gradient rectangle, a multicolor rectangle, and a multicolor text.

    `Related Pages <https://www.w3schools.com/html/html5_canvas.asp>`_
    """
    return CompChartsCanvas.Canvas(self)

  @property
  def roughviz(self) -> CompChartsRoughViz.CompRoughViz:
    """
    Reusable JavaScript library for creating sketchy/hand-drawn styled charts in the browser.

    :Category: Web application

    `Related Pages <https://github.com/jwilber/roughViz>`_
    """
    return CompChartsRoughViz.CompRoughViz(self)

  @property
  def frappe(self) -> CompChartsFrappe.CompChartFrappe:
    """
    GitHub-inspired simple and modern SVG charts for the web with zero dependencies.

    :Category: Web application

    `Related Pages <https://frappe.io/charts>`_
    """
    return CompChartsFrappe.CompChartFrappe(self)

  @property
  def chartCss(self) -> CompChartsChartCss.CompChartCss:
    """
    Charts.css is a modern CSS framework. It uses CSS utility classes to style HTML elements as charts.

    :Category: Web application

    `Related Pages <https://chartscss.org/>`_
    """
    return CompChartsChartCss.CompChartCss(self)

  @property
  def vega(self) -> CompChartsVega.VegaEmbedded:
    """
    Vega – A Visualization Grammar.

    :Category: Analytics, Vega

    `Related Pages <https://vega.github.io/vega/>`_

    :return: A Python Vega object
    """
    return CompChartsVega.VegaEmbedded(self)

  def menu(self, chart: html.Html.Html, height: types.SIZE_TYPE = (18, 'px'), options: dict = None,
           post: types.JS_FUNCS_TYPES = None, profile: types.PROFILE_TYPE = None) -> html.HtmlContainer.Col:
    """
    Add a standard menu on the table to trigger standard operation (add, empty, copy, download).

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
          icon, align="center", tooltip=typ, height=height, width=(size, 'px'), options=options, profile=profile)
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


class Chart2d:

  def __init__(self, ui):
    self.page = ui.page

  @property
  def plotly(self) -> CompChartsPlotly.Plotly2D:
    """
    Built on top of d3.js and stack.gl, Plotly.js is a high-level, declarative charting library.
    plotly.js ships with over 40 chart types, including 3D charts, statistical graphs, and SVG maps.

    :Category: Analytics, Plotly

    `Related Pages <https://plotly.com/javascript/>`_

    :return: A Python Plotly object
    """
    return CompChartsPlotly.Plotly2D(self)

  @property
  def nvd3(self) -> CompChartsNvd3.Nvd3:
    """
    This project is an attempt to build re-usable charts and chart components for d3.js
    without taking away the power that d3.js gives you.

    :Category: Analytics, Web application

    `Related Pages <http://nvd3.org/>`_

    :return: A Python NVD3 object
    """
    return CompChartsNvd3.Nvd3(self)

  @property
  def dc(self) -> CompChartsDc.DC:
    """
    dc.js is a javascript charting library with native crossfilter support, allowing highly
    efficient exploration on large multi-dimensional datasets (inspired by crossfilter's demo).

    :Category: Analytics, Dataviz

    `Related Pages <https://dc-js.github.io/dc.js/>`_
    """
    return CompChartsDc.DC(self)

  @property
  def d3(self) -> CompChartsD3.D3:
    """
    D3.js is a JavaScript library for manipulating documents based on data.

    :Category: Analytics, Dataviz

    `Related Pages <https://d3js.org/>`_
    """
    return CompChartsD3.D3(self)

  @property
  def svg(self) -> CompChartsSvg.SVG:
    """
    SVG stands for Scalable Vector Graphics.

    SVG defines vector-based graphics in XML format.

    `Related Pages <https://www.w3schools.com/graphics/svg_intro.asp>`_
    """
    return CompChartsSvg.SVG(self)

  @property
  def canvas(self) -> CompChartsCanvas.Canvas:
    """
    The HTML <canvas> element is used to draw graphics on a web page.

    The graphic to the left is created with <canvas>.
    It shows four elements: a red rectangle, a gradient rectangle, a multicolor rectangle, and a multicolor text.

    `Related Pages <https://www.w3schools.com/html/html5_canvas.asp>`_
    """
    return CompChartsCanvas.Canvas(self)

  @property
  def chartJs(self) -> CompChartsChartJs.ChartJs:
    """
    Interface for the ChartJs library.

    :Category: Web application

    `Related Pages <https://www.chartjs.org>`_

    :return: A Python ChartJs object
    """
    return CompChartsChartJs.ChartJs(self)

  @property
  def apex(self) -> CompChartsApex.ApexChart:
    """
    Interface for the ApexChart library.

    :Category: Web application

    `Related Pages <https://apexcharts.com>`_

    :return: A Python ChartJs object
    """
    return CompChartsApex.ApexChart(self)

  @property
  def c3(self) -> CompChartsC3.C3:
    """
    Interface to the JavaScript C3 module.

    :Category: Analytics, Dataviz

    `Related Pages <ttps://c3js.org>`_

    :return: A Python C3 object
    """
    return CompChartsC3.C3(self)

  @property
  def billboard(self) -> CompChartsBillboard.Billboard:
    """
    Interface to the Javascript Billboard module.

    This will propose various charts for data analysis and visualisation based on D£.
    This project has been forked from Billboard.js.

    :Category: Analytics, Bilboard

    `Related Pages <https://naver.github.io/billboard.js>`_

    :return: A Python Billboard Object
    """
    return CompChartsBillboard.Billboard(self)

  @property
  def vis(self) -> CompChartsVis.Vis2D:
    """
    Interface for the Vis library.

    :Category: Analytics, Vis

    `Related Pages <https://visjs.org>`_

    :return: A Python Vis object
    """
    return CompChartsVis.Vis2D(self)


class Chart3d:

  def __init__(self, ui):
    self.page = ui.page

  @property
  def plotly(self) -> CompChartsPlotly.Plotly3D:
    """
    Built on top of d3.js and stack.gl, Plotly.js is a high-level, declarative charting library.
    plotly.js ships with over 40 chart types, including 3D charts, statistical graphs, and SVG maps.

    :Category: Analytics, Plotly

    `Related Pages <https://plotly.com/javascript>`_

    :return: A Python Plolty object
    """
    return CompChartsPlotly.Plotly3D(self)

  @property
  def vis(self) -> CompChartsVis.Vis3D:
    """
    Interface for the Vis library.

    :Category: Analytics, Dataviz

    `Related Pages <https://visjs.org/>`_

    :return: A Python Vis object
    """
    return CompChartsVis.Vis3D(self)
