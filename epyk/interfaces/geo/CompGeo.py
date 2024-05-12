from epyk.interfaces.geo import CompGeoPlotly
from epyk.interfaces.geo import CompGeoDc
from epyk.interfaces.geo import CompGeoJqV
from epyk.interfaces.geo import CompGeoChartJs
from epyk.interfaces.geo import CompGeoGoogle
from epyk.interfaces.geo import CompGeoLeaflet
from epyk.interfaces.geo import CompGeoD3
from epyk.interfaces.geo import CompGeoMapboxGl
from epyk.interfaces.geo import CompGeoECharts


class Geo:

    def __init__(self, ui):
        self.page = ui.page

    @property
    def plotly_map(self) -> CompGeoPlotly.Plotly:
        """Interface for the Plotly library.

        `Plotly <https://plotly.com/javascript/choropleth-maps/>`_
        """
        return CompGeoPlotly.Plotly(self)

    @property
    def dc_choropleth(self) -> CompGeoDc.Dc:
        """ """
        return CompGeoDc.Dc(self)

    @property
    def chartJs(self) -> CompGeoChartJs.ChartJs:
        """Property to the ChartJs Geo API.

        `Chartjs <https://github.com/sgratzl/chartjs-chart-geo>`_
        """
        return CompGeoChartJs.ChartJs(self)

    @property
    def echarts(self) -> CompGeoECharts.ECharts:
        """Property to the EChartJs Geo API.

        `echarts <https://echarts.apache.org/en/index.html>`_
        """
        return CompGeoECharts.ECharts(self)

    @property
    def plotly(self) -> CompGeoPlotly.Plotly:
        """

        `plotly <https://plotly.com/javascript/choropleth-maps/>`_
        """
        return CompGeoPlotly.Plotly(self)

    @property
    def google(self) -> CompGeoGoogle.GeoGoogle:
        """Property to the Google charts API.

        `google <https://developers.google.com/chart>`_
        """
        if not getattr(self.page, '_with_google_imports', False):
            raise ValueError("Google produce must be added using for example page.imports.google_products(['charts'])")

        return CompGeoGoogle.GeoGoogle(self)

    @property
    def jqv(self) -> CompGeoJqV.JqueryVertorMap:
        """Property to the Jquery vector Map API.

        `jqvmap <https://www.10bestdesign.com/jqvmap/>`_
        """
        return CompGeoJqV.JqueryVertorMap(self)

    @property
    def leaflet(self) -> CompGeoLeaflet.GeoLeaflet:
        """Property to the Jquery vector Map API.

        `leaflet <https://leafletjs.com/>`_
        """
        return CompGeoLeaflet.GeoLeaflet(self)

    @property
    def d3(self) -> CompGeoD3.D3:
        """Interactive maps for data visualizations. Bundled into a single Javascript file.

        `datamaps <https://github.com/markmarkoh/datamaps>`_
        """
        return CompGeoD3.D3(self)

    @property
    def mapbox(self) -> CompGeoMapboxGl.MapboxMaps:
        """A JavaScript library that uses WebGL to render interactive maps from vector tiles and Mapbox styles.

        Usage::

          page.imports.pkgs.mapbox.set_access_token(
            "XXXXXX",
            "mapboxgl.accessToken"
          )

          l = page.ui.geo.mapbox.globe() # page.ui.geo.leaflet.europe()
          l.load([
            l.js.addControl([l.js._.FullscreenControl()]),
            l.js.addControl([l.js._.GeolocateControl()]),
            l.js.addControl([l.js._.NavigationControl()]),
            l.js.addControl([l.js._.ScaleControl()]),
            l.js.addSource('portland', {'type': 'raster', 'url': 'mapbox://examples.32xkp0wd'}),
            l.js.addLayer({'id': 'portland', 'source': 'portland', 'type': 'raster'}),
            l.js.addSource('route', {'type': 'geojson', 'data': {'type': 'Feature', 'properties': {}, 'geometry': {
              'type': 'LineString', 'coordinates': [
                [-122.483696, 37.833818], [-122.483482, 37.833174], [-122.483396, 37.8327], [-122.483568, 37.832056]
                [-122.48404, 37.831141], [-122.48404, 37.830497], [-122.483482, 37.82992], [-122.483568, 37.829548],
                [-122.48507, 37.829446], [-122.4861, 37.828802], [-122.486958, 37.82931], [-122.487001, 37.830802],
                [-122.487516, 37.831683], [-122.488031, 37.832158], [-122.488889, 37.832971], [-122.489876, 37.832632],
                [-122.490434, 37.832937], [-122.49125, 37.832429], [-122.491636, 37.832564], [-122.492237, 37.833378],
                [-122.493782, 37.833683]]}}}),
            l.js.addLayer({'id': 'route', 'type': 'line', 'source': 'route', 'layout': {
              'line-join': 'round', 'line-cap': 'round'}, 'paint': {'line-color': '#888', 'line-width': 8}})
          ])
          l.options.style = 'mapbox://styles/mapbox/streets-v11'

        `mapbox <https://docs.mapbox.com/>`_
        """
        return CompGeoMapboxGl.MapboxMaps(self)
