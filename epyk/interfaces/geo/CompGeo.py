
from epyk.interfaces.geo import CompGeoPlotly
from epyk.interfaces.geo import CompGeoDc
from epyk.interfaces.geo import CompGeoChartJs


class Geo(object):
  def __init__(self, context):
    self.context = context

  @property
  def plotly_map(self):
    """
    Description:
    ------------
    Interface for the Plotly library
    """
    return CompGeoPlotly.Plotly(self)

  @property
  def dc_choropleth(self):
    """
    Description:
    ------------
    """
    return CompGeoDc.Dc(self)

  @property
  def chartJs(self):
    """
    Description:
    ------------

    """
    return CompGeoChartJs.ChartJs(self)

  @property
  def plotly(self):
    """
    Description:
    ------------

    """
    return CompGeoPlotly.Plotly(self)
