
from epyk.interfaces.geo import CompGeoPlotly
from epyk.interfaces.geo import CompGeoDc
from epyk.interfaces.geo import CompGeoJqV
from epyk.interfaces.geo import CompGeoChartJs
from epyk.interfaces.geo import CompGeoGoogle
from epyk.interfaces.geo import CompGeoLeaflet
from epyk.interfaces.geo import CompGeoD3
from epyk.interfaces.geo import CompGeoMapboxGl


class Geo:

  def __init__(self, ui):
    self.page = ui.page

  @property
  def plotly_map(self) -> CompGeoPlotly.Plotly:
    """
    Description:
    ------------
    Interface for the Plotly library.

    Usage::

    Related Pages:
    --------------

      https://plotly.com/javascript/choropleth-maps/
    """
    return CompGeoPlotly.Plotly(self)

  @property
  def dc_choropleth(self) -> CompGeoDc.Dc:
    """
    Description:
    ------------

    Related Pages:
    --------------
    """
    return CompGeoDc.Dc(self)

  @property
  def chartJs(self) -> CompGeoChartJs.ChartJs:
    """
    Description:
    ------------
    Property to the ChartJs Geo API.

    Usage::

    Related Pages:
    --------------

      https://github.com/sgratzl/chartjs-chart-geo
    """
    return CompGeoChartJs.ChartJs(self)

  @property
  def plotly(self) -> CompGeoPlotly.Plotly:
    """
    Description:
    ------------

    Usage::

    Related Pages:
    --------------

      https://plotly.com/javascript/choropleth-maps/
    """
    return CompGeoPlotly.Plotly(self)

  @property
  def google(self) -> CompGeoGoogle.GeoGoogle:
    """
    Description:
    ------------
    Property to the google charts API.

    Usage::

    Related Pages:
    --------------

      https://developers.google.com/chart
    """
    if not getattr(self.page, '_with_google_imports', False):
      raise ValueError("Google produce must be added using for example page.imports.google_products(['charts'])")

    return CompGeoGoogle.GeoGoogle(self)

  @property
  def jqv(self) -> CompGeoJqV.JqueryVertorMap:
    """
    Description:
    ------------
    Property to the Jquery vector Map API.

    Usage::

    Related Pages:
    --------------

      https://www.10bestdesign.com/jqvmap/
    """
    return CompGeoJqV.JqueryVertorMap(self)

  @property
  def leaflet(self) -> CompGeoLeaflet.GeoLeaflet:
    """
    Description:
    ------------
    Property to the Jquery vector Map API.

    Usage::

    Related Pages:
    --------------

      https://www.10bestdesign.com/jqvmap/
    """
    return CompGeoLeaflet.GeoLeaflet(self)

  @property
  def d3(self) -> CompGeoD3.D3:
    """
    Description:
    ------------
    Interactive maps for data visualizations. Bundled into a single Javascript file.

    Related Pages:
    --------------

      https://github.com/markmarkoh/datamaps

    """
    return CompGeoD3.D3(self)

  @property
  def mapbox(self) -> CompGeoMapboxGl.MapboxMaps:
    """
    Description:
    ------------
    A JavaScript library that uses WebGL to render interactive maps from vector tiles and Mapbox styles.

    Related Pages:
    --------------

      https://docs.mapbox.com/
    """
    return CompGeoMapboxGl.MapboxMaps(self)
