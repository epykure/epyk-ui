"""
Group CSS class for all the Charts components
"""

from epyk.core.css.groups import CssGrpCls

# The list of CSS classes
from epyk.core.css.styles import CssStylesChart


class CssClassChartsNvd3(CssGrpCls.CssGrpClass):
  CssDivChart = CssStylesChart.CssDivChart
  CssNVD3HideGrid = CssStylesChart.CssNVD3HideGrid
  CssNVD3Axis = CssStylesChart.CssNVD3Axis
  CssNVD3AxisLabel = CssStylesChart.CssNVD3AxisLabel
  CssNVD3AxisLegend = CssStylesChart.CssNVD3AxisLegend
  __map, __alt_map = ["CssDivChart", "CssNVD3HideGrid", 'CssNVD3Axis', 'CssNVD3AxisLabel', 'CssNVD3AxisLegend'], []


class CssClassCharts(CssGrpCls.CssGrpClass):
  CssDivChart = CssStylesChart.CssDivChart
  __map, __alt_map = ["CssDivChart"], []

