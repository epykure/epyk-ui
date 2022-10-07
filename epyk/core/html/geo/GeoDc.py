#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html.graph import GraphDC
from epyk.core.js.packages import JsDc


class ChartGeoChoropleth(GraphDC.Chart):
  name = 'DC Choropleth'
  requirements = ('dc', 'crossfilter')

  @property
  def dom(self) -> JsDc.GeoChoropleth:
    """   Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    :rtype: JsDc.GeoChoropleth
    """
    if self._dom is None:
      self._dom = JsDc.GeoChoropleth(self.page, js_code=self.chartId, component=self)
    return self._dom
