"""

"""

from epyk.core.css.catalogs import Catalog

from epyk.core.css.styles.classes import CssStylesChart


class CatalogChart(Catalog.CatalogGroup):

  def div(self) -> CssStylesChart.CssDivChart:
    """  """
    return self._set_class(CssStylesChart.CssDivChart)

  def billboard_title(self) -> CssStylesChart.CssBillboardTitle:
    """  """
    return self._set_class(CssStylesChart.CssBillboardTitle)

  def billboard_legend(self) -> CssStylesChart.CssBillboardLegend:
    """  """
    return self._set_class(CssStylesChart.CssBillboardLegend)

  def billboard_axis(self) -> CssStylesChart.CssBillboardAxis:
    """  """
    return self._set_class(CssStylesChart.CssBillboardAxis)

  def billboard_axis_x(self) -> CssStylesChart.CssBillboardXAxis:
    """  """
    return self._set_class(CssStylesChart.CssBillboardXAxis)

  def billboard_axis_y(self) -> CssStylesChart.CssBillboardYAxis:
    """  """
    return self._set_class(CssStylesChart.CssBillboardYAxis)

  def c3_title(self) -> CssStylesChart.CssC3Title:
    """  """
    return self._set_class(CssStylesChart.CssC3Title)

  def c3_legend(self) -> CssStylesChart.CssC3Legend:
    """  """
    return self._set_class(CssStylesChart.CssC3Legend)

  def c3_axis(self) -> CssStylesChart.CssC3Axis:
    """  """
    return self._set_class(CssStylesChart.CssC3Axis)

  def c3_axis_x(self) -> CssStylesChart.CssC3XAxis:
    """  """
    return self._set_class(CssStylesChart.CssC3XAxis)

  def c3_axis_y(self) -> CssStylesChart.CssC3YAxis:
    """  """
    return self._set_class(CssStylesChart.CssC3YAxis)

  def nvd3_axis(self) -> CssStylesChart.CssNVD3Axis:
    """  """
    return self._set_class(CssStylesChart.CssNVD3Axis)

  def nvd3_axis_label(self) -> CssStylesChart.CssNVD3AxisLabel:
    """  """
    return self._set_class(CssStylesChart.CssNVD3AxisLabel)

  def nvd3_axis_legend(self) -> CssStylesChart.CssNVD3AxisLegend:
    """  """
    return self._set_class(CssStylesChart.CssNVD3AxisLegend)

  def nvd3_grid_hide(self) -> CssStylesChart.CssNVD3HideGrid:
    """  """
    return self._set_class(CssStylesChart.CssNVD3HideGrid)

  def sparklines(self) -> CssStylesChart.CssSparklines:
    """  """
    return self._set_class(CssStylesChart.CssSparklines)

  def vis_items(self) -> CssStylesChart.CssVisItems:
    """  """
    return self._set_class(CssStylesChart.CssVisItems)

  def vis_items_overflow(self) -> CssStylesChart.CssVisItemsOverlow:
    """  """
    return self._set_class(CssStylesChart.CssVisItemsOverlow)
