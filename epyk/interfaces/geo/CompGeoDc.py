
from typing import Union
from epyk.core.html import geo
from epyk.core.html import Defaults_html


class Dc:

  def __init__(self, ui):
    self.page = ui.page
    self.chartFamily = "DC"

  def usa(self, record=None, y_columns: list = None, x_axis: str = None, title: str = None,
          profile: Union[dict, bool] = None, options: dict = None, width: Union[int, tuple] = (100, "%"),
          height: Union[int, tuple] = (Defaults_html.CHARTS_HEIGHT_PX, "px"), html_code: str = None):
    """

    Underlying HTML Objects:

      - :class:`epyk.core.geo.GeoDc.ChartGeoChoroplethk`

    Related Pages:

      https://jsfiddle.net/djmartin_umich/9VJHe/
      http://bl.ocks.org/KatiRG/cccd23dd7a830da0de5c

    :param record:
    :param y_columns:
    :param x_axis:
    :param title:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param html_code:
    """
    geo_chart = geo.GeoDc.ChartGeoChoropleth(self.page, width, height, title, options or {}, html_code, profile)
    line_id = geo_chart.html_code
    self.page._props.setdefault('js', {}).setdefault('datasets', {})['data_cf_%s' % line_id] = "var %(cId)s_cf = crossfilter(%(data)s); var %(cId)s_dim = %(cId)s_cf.dimension(function(d) {return +d['%(x)s'];})" % {'cId': line_id, 'data': record, 'x': x_axis}
    geo_chart.dom.height(height[0]).dimension("%s_dim" % line_id).group("%(cId)s_dim.group().reduceSum(function(d) {return d['%(y)s'] ;})" % {'cId': line_id, 'y': y_columns})
    return geo_chart
