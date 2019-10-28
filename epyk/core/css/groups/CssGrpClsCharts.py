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


class CssClassChartsC3(CssGrpCls.CssGrpClass):
  CssDivChart = CssStylesChart.CssDivChart
  CssC3Title = CssStylesChart.CssC3Title
  CssC3Legend = CssStylesChart.CssC3Legend
  CssC3Axis = CssStylesChart.CssC3Axis
  CssC3XAxis = CssStylesChart.CssC3XAxis
  CssC3YAxis = CssStylesChart.CssC3YAxis
  __map, __alt_map = ['CssDivChart', 'CssC3Title', 'CssC3Legend', 'CssC3Axis', 'CssC3XAxis', 'CssC3YAxis'], []


class CssClassCharts(CssGrpCls.CssGrpClass):
  CssDivChart = CssStylesChart.CssDivChart
  __map, __alt_map = ["CssDivChart"], []


class CssClassChartsSparkline(CssGrpCls.CssGrpClass):
  CssSparklines = CssStylesChart.CssSparklines
  __map, __alt_map = ["CssSparklines"], []

