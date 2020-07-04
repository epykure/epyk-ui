#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html.graph import GraphDC

from epyk.core.js.packages import JsDc


class ChartGeoChoropleth(GraphDC.Chart):
  name = 'DC Choropleth'
  requirements = ('dc', 'crossfilter' )

  @property
  def dom(self):
    """
    Description:
    -----------

    :rtype: JsDc.GeoChoropleth
    """
    if self._dom is None:
      self._dom = JsDc.GeoChoropleth(self._report, varName=self.chartId, parent=self)
    return self._dom
