
from epyk.interfaces.geo import CompGeoPlotly


class Geo(object):
  def __init__(self, context):
    self.context = context

  @property
  def plotly(self):
    """
    Interface for the Plotly library

    Documentation

    :return: A Python Plolty object
    """
    return CompGeoPlotly.Plotly(self)
