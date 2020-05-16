
from epyk.interfaces.geo import CompGeoPlotly
from epyk.interfaces.geo import CompGeoDc
from epyk.interfaces.geo import CompGeoChartJs


class Geo(object):
  def __init__(self, context):
    self.context = context

  @property
  def plotly_map(self):
    """
    Interface for the Plotly library

    :return: CompGeoPlotly.Plotly
    """
    return CompGeoPlotly.Plotly(self)

  @property
  def dc_choropleth(self):
    """

    :return: CompGeoDc.Dc
    """
    return CompGeoDc.Dc(self)

  @property
  def chartJs(self):
    """

    :return: CompGeoChartJs.ChartJs
    """
    return CompGeoChartJs.ChartJs(self)

  @property
  def plotly(self):
    """

    :return: CompGeoPlotly.PlotlyChoropleth
    """
    return CompGeoPlotly.Plotly(self)
