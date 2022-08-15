
from typing import Union
from epyk.core.html import geo
from epyk.interfaces import Arguments
from epyk.core.html import Defaults_html


class MapboxMaps:

  def __init__(self, ui):
    self.page = ui.page
    self.chartFamily = "Mapbox"

  def globe(self, record=None, y_column: list = None, x_axis: str = None, profile: Union[dict, bool] = None,
          options: dict = None, width: Union[int, tuple] = (100, "%"),
          height: Union[int, tuple] = (Defaults_html.CHARTS_HEIGHT_PX, "px"),
          html_code: str = None) -> geo.GeoMapbox.GeoMapbox:
    """
    Description:
    -----------

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/example/globe/

    Attributes:
    ----------
    :param record:
    :param y_column:
    :param x_axis:
    :param profile:
    :param options:
    :param width:
    :param height:
    :param html_code:
    """
    mapbox = geo.GeoMapbox.GeoMapbox(self.page, width, height, html_code, options or {}, profile)
    return mapbox
