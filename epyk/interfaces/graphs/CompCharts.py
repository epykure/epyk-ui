"""

"""

# Check if pandas is available in the current environment
# if it is the case this module can handle DataFrame directly
try:
  import pandas as pd
  has_pandas = True

except:
  has_pandas = False

from epyk.core import html
from epyk.core import js
from epyk.core.html import graph

from epyk.interfaces.graphs import CompChartsBillboard
from epyk.interfaces.graphs import CompChartsDc
from epyk.interfaces.graphs import CompChartsC3
from epyk.interfaces.graphs import CompChartsChartJs
from epyk.interfaces.graphs import CompChartsPlotly
from epyk.interfaces.graphs import CompChartsNvd3
from epyk.interfaces.graphs import CompChartsD3
from epyk.interfaces.graphs import CompChartsVis
from epyk.interfaces.graphs import CompChartsSvg
from epyk.interfaces.graphs import CompChartsCanvas


class Graphs(object):
  def __init__(self, context):
    self.context = context

  def skillbars(self, records=None, y_column=None, x_axis=None, title=None, width=(100, '%'),
                height=(None, 'px'), htmlCode=None, colUrl=None, colTooltip=None, filters=None, profile=False):
    """
    Python interface for the HTML Skill bars, simple bars chart done in pure Javascript and CSS

    Example
    records = [
      {"label": 'python', 'value': 12},
      {"label": 'Java', 'value': 5},
      {"label": 'Javascript', 'value': 80}]
    rptObj.ui.charts.skillbars(records, y_column=['value'], x_axis=['label']).css({"width": '100px'})

    Documentation
    https://www.w3schools.com/howto/howto_css_skill_bar.asp

    :param records:
    :param y_column:
    :param x_axis:
    :param title:
    :param width:
    :param height:
    :param htmlCode:
    :param colUrl:
    :param colTooltip:
    :param filters:
    :param profile:
    """
    if y_column is None or x_axis is None:
      raise Exception("seriesName and axis must be defined")

    #data = self.context.rptObj.js.data.records(records)
    #jsDataObj = js.AresJs.Js(self.context.rptObj, records, profile=profile).fncs([('percentage', [x_axis], [y_column])])
    html_skillbar = html.HtmlEvent.SkillBar(self.context.rptObj, records, y_column, x_axis, title, width, height, htmlCode,
                                            colUrl, colTooltip, filters, profile)
    self.context.register(html_skillbar)
    return html_skillbar

  def _data(self, data, seriesNames, xAxis, otherDims, dataFncs, xAxisOrder, chartFam, chartType, profile):
    """

    :param data:
    :param seriesNames:
    :param xAxis:
    :param otherDims:
    :param dataFncs:
    :param xAxisOrder:
    :param chartFam:
    :param chartType:
    :param profile:
    :return:
    """
    if data is None:
      data = []
    if xAxis == '_index' or xAxis is None:
      xAxis = '_index'
      if seriesNames is None:
        seriesNames = list(data.columns)
      data['_index'] = data.index

    if not isinstance(seriesNames, list):
      seriesNames = [seriesNames]
    if dataFncs == False:
      dataFncs = [('all', [xAxis], seriesNames)]
    elif dataFncs is None:
      if otherDims is not None:
        dataFncs = [('sum', [xAxis], seriesNames + list(otherDims), xAxisOrder)]
      else:
        dataFncs = [('sum', [xAxis], seriesNames, xAxisOrder)]
    params = (seriesNames, xAxis) if otherDims is None else tuple([seriesNames, xAxis] + list(otherDims))
    return js.AresJs.Js(self.context.rptObj, data, profile=profile).fncs(dataFncs).output(chartFam, chartType, params)

  def chart(self, chartType=None, data=None, seriesNames=None, xAxis=None, otherDims=None, dataFncs=None, title=None,
            chartFamily=None, filters=None, profile=None, xAxisOrder=None, options=None,
            width=(100, "%"), height=(330, 'px'),  htmlCode=None):
    """
    Quick charts generation.

    This function will always return the preferred Chart library for the requested chartType.
    This can be overridden by defining the variable chartFamily

    :rtype: graph.GraphFabric.Chart
    """
    chartFam = html.graph.GraphFabric.Chart.get(self.context.rptObj, chartType, chartFamily)
    if chartFam is None:
      raise Exception("This type of chart %s does not exist in all the Js Charting families" % chartType)

    data = self._data(data, seriesNames, xAxis, otherDims, dataFncs, xAxisOrder, chartFam, chartType, profile)
    return self.context.register(getattr(graph, 'Graph%s' % chartFam).Chart(self.context.rptObj, chartType, data, width,
                                                                            height, title, options, htmlCode, filters, profile))

  def d3script(self, script, aresDf=None, seriesNames=None, xAxis=None, otherDims=None, dataFncs=None, title='',
            globalFilter=None, filterSensitive=True, profile=None, dataSrc=None, xAxisOrder=None, chartOptions=None,
            width=100, widthUnit="%", height=330, heightUnit="px", url=None, htmlCode=None, d3Version=None):
    if aresDf is None:
      aresDf = self.context.rptObj.df([])
    if not hasattr(aresDf, 'htmlCode'):
      if len(aresDf) > 0 and isinstance(aresDf[0], list):
        tmpAresDf = []
        for line in aresDf[1:]:
          tmpAresDf.append(dict(zip(aresDf[0], line)))
        aresDf = tmpAresDf
      aresDf = self.context.rptObj.df(aresDf)
    if xAxis == '_index' or xAxis is None:
      xAxis = '_index'
      if seriesNames is None:
        seriesNames = list(aresDf.columns)
      aresDf['_index'] = aresDf.index
    # if not 'sort_values' in kwargs:
    #   if xAxis is not None and not aresDf.empty:
    #     aresDf.sort_values(by=[xAxis], inplace=True)
    # else:
    #   kwargs['sort_values']["inplace"] = True
    #   aresDf.sort_values(**kwargs['sort_values'])
    #   del kwargs['sort_values']

    if not isinstance(seriesNames, list):
      seriesNames = [seriesNames]
    if dataFncs == False:
      dataFncs = [('all', [xAxis], seriesNames)]
    elif dataFncs is None:
      if otherDims is not None:
        dataFncs = [('sum', [xAxis], seriesNames + list(otherDims), xAxisOrder)]
      else:
        dataFncs = [('sum', [xAxis], seriesNames, xAxisOrder)]
    params = (seriesNames, xAxis) if otherDims is None else tuple([seriesNames, xAxis] + list(otherDims))
    data = js.AresJs.Js(self.context.rptObj, aresDf, profile=profile).fncs(dataFncs).output("D3Bespoke", None, params)
    return self.context.register(getattr(graph, 'GraphD3Bespoke').Chart(self.context.rptObj, script, data,
                                                                        width, widthUnit, height, heightUnit, title, chartOptions, htmlCode, globalFilter, filterSensitive, dataSrc, profile, url, d3Version))

  def sparkline(self, chart_type, data, title=None, options=None, column=None):
    """
    Display a sparkline component

    Example
    rptObj.ui.charts.sparkline("box", [1, 2, 3, 4, 5, 4, 3, 2, 1])
    rptObj.ui.charts.sparkline("bar", [1, 2, 3, 4, 5, 4, 3, 2, 10])

    Documentation
    https://omnipotent.net/jquery.sparkline/#s-about

    :param chart_type: The type of chart (bullet, line, bar, tristate, discrete, pie, box)
    :param data: A list of values
    :param options: The chart options
    :param column:

    :rtype: graph.GraphSparklines.Sparklines
    :return: A python Sparkline object
    """
    if column is not None:
      if isinstance(data, list):
        pass

    html_chart = html.graph.GraphSparklines.Sparklines(self.context.rptObj, data, chart_type, title, options)
    self.context.register(html_chart)
    return html_chart


  #  ------------------------------------------------------------------------------------------------------------------
  #
  #
  #  ------------------------------------------------------------------------------------------------------------------
  @property
  def plotly(self):
    """
    Interface for the Plotly library

    Documentation

    :return: A Python Plolty object
    """
    return CompChartsPlotly.Plotly(self)

  @property
  def chartJs(self):
    """
    Interface for the ChartJs library

    Documentation

    :return: A Python ChartJs object
    """
    return CompChartsChartJs.ChartJs(self)

  @property
  def c3(self):
    """
    Interface to the Javsacript C3 module

    Documentation

    :return: A Python C3 object
    """
    return CompChartsC3.C3(self)

  @property
  def billboard(self):
    """
    Interface to the Javascript Billboard module

    This will propose various charts for data analysis and visualisation based on D£.
    This project has been forked from C3.js

    Documentation
    https://naver.github.io/billboard.js/

    :return: A Python Billboard Object
    """
    return CompChartsBillboard.Billboard(self)

  @property
  def vis(self):
    """
    Interface to the Javascript Vis module

    Documentation

    :return: A Python Vis object
    """
    return CompChartsVis.Vis(self)

  @property
  def nvd3(self):
    """
    Interface to the Javascript NVD3 library

    Documentation
    http://nvd3.org/

    :return: A Python NVD3 object
    """
    return CompChartsNvd3.Nvd3(self)

  @property
  def dc(self):
    """
    """
    return CompChartsDc.DC(self)

  @property
  def d3(self):
    """
    """
    return CompChartsD3.D3(self)

  @property
  def svg(self):
    """
    SVG defines vector-based graphics in XML format

    Documentation
    https://www.w3schools.com/graphics/svg_intro.asp
    """
    return CompChartsSvg.SVG(self)

  @property
  def canvas(self):
    """ """
    return CompChartsCanvas.Canvas(self)
