"""

"""

from epyk.core.css.catalogs import Catalog

from epyk.core.css.styles.classes import CssStylesChart


class CatalogChart(Catalog.CatalogGroup):

  def div(self):
    """  """
    return self._set_class(CssStylesChart.CssDivChart)

  def billboard_title(self):
    """  """
    return self._set_class(CssStylesChart.CssBillboardTitle)

  def billboard_legend(self):
    """  """
    return self._set_class(CssStylesChart.CssBillboardLegend)

  def billboard_axis(self):
    """  """
    return self._set_class(CssStylesChart.CssBillboardAxis)

  def billboard_axis_x(self):
    """  """
    return self._set_class(CssStylesChart.CssBillboardXAxis)

  def billboard_axis_y(self):
    """  """
    return self._set_class(CssStylesChart.CssBillboardYAxis)

  def c3_title(self):
    """  """
    return self._set_class(CssStylesChart.CssC3Title)

  def c3_legend(self):
    """  """
    return self._set_class(CssStylesChart.CssC3Legend)

  def c3_axis(self):
    """  """
    return self._set_class(CssStylesChart.CssC3Axis)

  def c3_axis_x(self):
    """  """
    return self._set_class(CssStylesChart.CssC3XAxis)

  def c3_axis_y(self):
    """  """
    return self._set_class(CssStylesChart.CssC3YAxis)

  def nvd3_axis(self):
    """  """
    return self._set_class(CssStylesChart.CssNVD3Axis)

  def nvd3_axis_label(self):
    """  """
    return self._set_class(CssStylesChart.CssNVD3AxisLabel)

  def nvd3_axis_legend(self):
    """  """
    return self._set_class(CssStylesChart.CssNVD3AxisLegend)

  def nvd3_grid_hide(self):
    """  """
    return self._set_class(CssStylesChart.CssNVD3HideGrid)

  def sparklines(self):
    """  """
    return self._set_class(CssStylesChart.CssSparklines)
