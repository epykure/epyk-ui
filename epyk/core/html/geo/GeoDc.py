
from epyk.core.html.graph import GraphDC

from epyk.core.js.packages import JsDc


class ChartGeoChoropleth(GraphDC.Chart):
  name = 'DC Choropleth'
  requirements = ('dc', 'crossfilter' )

  @property
  def dom(self):
    """
    :rtype: JsChartDC.JsLine
    """
    if self._dom is None:
      self._dom = JsDc.GeoChoropleth(self._report, varName=self.chartId, parent=self)
    return self._dom
