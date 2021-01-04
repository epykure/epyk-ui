
from epyk.core.html import geo


class ChartJs(object):
  def __init__(self, context):
    self.parent = context
    self.chartFamily = "ChartJs"

  @property
  def choropleths(self):
    return Choropleth(self.parent)

  @property
  def bubbleMap(self):
    return BubbleMaps(self.parent)


class BubbleMaps(object):
  def __init__(self, context):
    self.parent = context
    self.chartFamily = "ChartJs"

  def world(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------

    Underlying HTML Objects:

      - :class:`epyk.core.geo.GeoChartJs.Choropleth`

    Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param htmlCode:
    """
    geo_chart = geo.GeoChartJs.Choropleth(self.parent.context.rptObj, width, height, htmlCode, options or {}, profile)
    geo_chart._attrs['type'] = "bubbleMap"
    geo_chart.options.scale.projection = "mercator"
    geo_chart.options.geo.radiusScale.display = True
    geo_chart.options.geo.radiusScale.size = [1, 20]
    geo_chart.options.showOutline = True
    geo_chart.options.legend.display = False
    geo_chart.options.showGraticule = True
    return geo_chart

  def us(self, record=None, y_columns=None, x_axis=None,  profile=None, options=None, width=(100, "%"),
           height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------

    Underlying HTML Objects:

      - :class:`epyk.core.geo.GeoChartJs.Choropleth`

    Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param htmlCode:
    """
    geo_chart = geo.GeoChartJs.ChoroplethUs(self.parent.context.rptObj, width, height, htmlCode, options or {}, profile)
    geo_chart._attrs['type'] = "bubbleMap"
    geo_chart.options.scale.projection = "albersUsa"
    geo_chart.options.geo.radiusScale.display = True
    geo_chart.options.geo.radiusScale.size = [1, 20]
    geo_chart.options.showOutline = True
    geo_chart.options.legend.display = False
    geo_chart.options.showGraticule = True
    return geo_chart


class Choropleth(object):
  def __init__(self, context):
    self.parent = context
    self.chartFamily = "ChartJs"

  def us(self, record=None, y_columns=None, x_axis=None,  profile=None, options=None, width=(100, "%"),
           height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------

    Underlying HTML Objects:

      - :class:`epyk.core.geo.GeoChartJs.Choropleth`

    Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param htmlCode:
    """
    geo_chart = geo.GeoChartJs.ChoroplethUs(self.parent.context.rptObj, width, height, htmlCode, options or {}, profile)
    geo_chart.options.scale.projection = "albersUsa"
    geo_chart.options.geo.colorScale.display = True
    geo_chart.options.geo.colorScale.quantize = 5
    geo_chart.options.geo.colorScale.position = "bottom"
    geo_chart.options.geo.colorScale.legend.position = "bottom-right"
    geo_chart.options.showOutline = True
    geo_chart.options.legend.display = False
    geo_chart.options.showGraticule = True
    return geo_chart

  def world(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------

    Underlying HTML Objects:

      - :class:`epyk.core.geo.GeoChartJs.Choropleth`

    Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param htmlCode:
    """
    geo_chart = geo.GeoChartJs.Choropleth(self.parent.context.rptObj, width, height, htmlCode, options or {}, profile)
    geo_chart.options.scale.projection = "equalEarth"
    geo_chart.options.scale.projection = "equirectangular"
    geo_chart.options.geo.colorScale.display = True
    geo_chart.options.showOutline = True
    geo_chart.options.legend.display = False
    geo_chart.options.showGraticule = True
    return geo_chart

  def country(self, record=None, y_columns=None, x_axis=None, profile=None, options=None, width=(100, "%"),
           height=(330, "px"), htmlCode=None):
    """
    Description:
    ------------

    Underlying HTML Objects:

      - :class:`epyk.core.geo.GeoChartJs.Choropleth`

    Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param htmlCode:
    """
    geo_chart = geo.GeoChartJs.ChoroplethCountry(self.parent.context.rptObj, width, height, htmlCode, options or {}, profile)
    geo_chart.options.scale.projection = "equalEarth"
    geo_chart.options.geo.colorScale.display = True
    geo_chart.options.showOutline = True
    geo_chart.options.legend.display = False
    geo_chart.options.showGraticule = True
    return geo_chart
