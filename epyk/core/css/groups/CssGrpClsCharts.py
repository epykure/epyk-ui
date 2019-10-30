"""
Group CSS class for all the Charts components
"""

from epyk.core.css.groups import CssGrpCls

# The list of CSS classes
from epyk.core.css.styles import CssStylesChart


class CssClassChartsNvd3(CssGrpCls.CssGrpClass):
  """

  """
  css_div_chart = CssStylesChart.CssDivChart
  css_NVD3_hide_grid = CssStylesChart.CssNVD3HideGrid
  css_NVD3_axis = CssStylesChart.CssNVD3Axis
  css_NVD3_axis_label = CssStylesChart.CssNVD3AxisLabel
  css_NVD3_axis_legend = CssStylesChart.CssNVD3AxisLegend
  __map, __alt_map = ["CssDivChart", "CssNVD3HideGrid", 'CssNVD3Axis', 'CssNVD3AxisLabel', 'CssNVD3AxisLegend'], []


class CssClassChartsC3(CssGrpCls.CssGrpClass):
  """

  """
  css_div_chart = CssStylesChart.CssDivChart
  css_C3_title = CssStylesChart.CssC3Title
  css_C3_legend = CssStylesChart.CssC3Legend
  css_C3_axis = CssStylesChart.CssC3Axis
  css_C3X_axis = CssStylesChart.CssC3XAxis
  css_C3Y_axis = CssStylesChart.CssC3YAxis
  __map, __alt_map = ['CssDivChart', 'CssC3Title', 'CssC3Legend', 'CssC3Axis', 'CssC3XAxis', 'CssC3YAxis'], []


class CssClassCharts(CssGrpCls.CssGrpClass):
  """

  """
  css_div_chart = CssStylesChart.CssDivChart
  __map, __alt_map = ["CssDivChart"], []


class CssClassChartsSparkline(CssGrpCls.CssGrpClass):
  """

  """
  css_sparklines = CssStylesChart.CssSparklines
  __map, __alt_map = ["CssSparklines"], []

