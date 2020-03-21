
from epyk.core.html.graph import GraphChartJs


class Choropleth(GraphChartJs.Chart):
  __reqJs = ['chartjs-chart-geo']

  def __init__(self, report, width, height, htmlCode, options, profile):
    super(Choropleth, self).__init__(report, width, height, htmlCode, options, profile)
    self._attrs['type'] = 'choropleth'

