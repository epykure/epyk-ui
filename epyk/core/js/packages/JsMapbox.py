#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Any
from epyk.core.py import types, primitives
from epyk.core.js import JsUtils
from epyk.core.js.packages import JsPackage
from epyk.core.js.packages import JsLeaflet
from epyk.core.js.primitives import JsObjects


class MabBoxSource:
  def updateImage(self):
    # https://docs.mapbox.com/mapbox-gl-js/example/animate-images/
    pass


class MapBoxMap(JsPackage):
  lib_alias = {'js': "mapbox-gl", 'css': 'mapbox-gl'}

  def __init__(self, component: primitives.HtmlModel = None, page: primitives.PageModel = None, js_code: str = None,
               selector: str = None, data: Any = None, set_var: bool = None):
    super(MapBoxMap, self).__init__(component, page, js_code, selector, data, set_var)
    self.varName = self.component.chartId

  def marker(self, lng: float, lat: float, options: dict = None) -> JsLeaflet.LMarker:
    """   Add a market to a map.

    Usage::

      l = page.ui.geo.mapbox.globe() # page.ui.geo.leaflet.europe()
      l.options.style = 'mapbox://styles/mapbox/streets-v11'
      marker = l.js.marker(-0.11, 51.508)

    Related Pages:

      https://leafletjs.com/reference-1.7.1.html#marker

    :param lng: The longitude value
    :param lat: The latitude value
    :param options: Market options
    """
    l_marker = JsLeaflet.LMarker(options=options, leaflet_map=self)
    l_marker.setLngLat([lng, lat])
    l_marker.varId = "new mapboxgl.Marker"
    return l_marker

  def set_accessToken(self, value: str):
    """   Set the library access token.
    This can be done at chart level or directly at the library level.

    :param value: Token value
    """
    self.component.options.accessToken = value

  def addControl(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
    """   Adds an IControl to the map, calling control.onAdd(this).

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/map/#map#addcontrol
      https://docs.mapbox.com/mapbox-gl-js/example/fullscreen/

    :param js_funcs: Javascript functions
    :param profile: Optional. A flag to set the component performance storage.
    """
    return JsUtils.jsWrap("%s.addControl(%s)" % (
      self.component.chartId, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))

  def addLayer(self, data: types.JS_DATA_TYPES):
    """   

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/example/canvas-source/

    :param data:
    """
    data = JsUtils.jsConvertData(data, None)
    return JsUtils.jsWrap("%s.addLayer(%s)" % (self.component.chartId, data))

  def addSource(self, name: types.JS_DATA_TYPES, data: types.JS_DATA_TYPES):
    """   

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/example/canvas-source/

    :param name:
    :param data:
    """
    name = JsUtils.jsConvertData(name, None)
    data = JsUtils.jsConvertData(data, None)
    return JsUtils.jsWrap("%s.addSource(%s, %s)" % (self.component.chartId, name, data))

  def addImage(self, name: types.JS_DATA_TYPES, data: types.JS_DATA_TYPES):
    """   

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/example/add-image-generated/

    :param name:
    :param data:
    """
    name = JsUtils.jsConvertData(name, None)
    data = JsUtils.jsConvertData(data, None)
    return JsUtils.jsWrap("%s.addImage(%s, %s)" % (self.component.chartId, name, data))

  def getBearing(self):
    """   Returns the map's current bearing. The bearing is the compass direction that is "up"; for example, a bearing of 90°
    orients the map so that east is up.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/map/#map#getbearing
      https://docs.mapbox.com/mapbox-gl-js/example/add-fog/
    """
    return JsObjects.JsNumber.JsNumber("%s.getBearing()" % self.component.chartId)

  def getZoom(self):
    """   Returns the map's current zoom level.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/map/#map#getzoom
    """
    return JsObjects.JsNumber.JsNumber("%s.getZoom()" % self.component.chartId)

  def getContainer(self):
    """   Returns the map's containing HTML element.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/map/#map#getcontainer
    """
    return JsObjects.JsObject.JsObject("%s.getContainer()" % self.component.chartId)

  def getCanvasContainer(self):
    """   Returns the HTML element containing the map's <canvas> element.

    If you want to add non-GL overlays to the map, you should append them to this element.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/map/#map#getcontainer
    """
    return JsObjects.JsObject.JsObject("%s.getCanvasContainer()" % self.component.chartId)

  def getCanvas(self):
    """   Returns the map's <canvas> element.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/map/#map#getcontainer
    """
    return JsObjects.JsObject.JsObject("%s.getCanvas()" % self.component.chartId)

  def resize(self, data: types.JS_DATA_TYPES = None):
    """
    Resizes the map according to the dimensions of its container element.

    Checks if the map container size changed and updates the map if it has changed.
    This method must be called after the map's container is resized programmatically or when the map is shown after being initially hidden with CSS.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/map/#map#getcontainer
    """
    if data is None:
      return JsObjects.JsObject.JsObject("%s.resize()" % self.component.chartId)

    data = JsUtils.jsConvertData(data, None)
    return JsObjects.JsObject.JsObject("%s.resize(%s)" % (self.component.chartId, data))

  def getSource(self, js_code: str):
    """   Returns the source with the specified ID in the map's style.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/map/#map#getcontainer
      https://docs.mapbox.com/mapbox-gl-js/example/animate-images/

    :param js_code:
    """
    _id = JsUtils.jsConvertData(js_code, None)
    return JsObjects.JsObject.JsObject("%s.getSource(%s)" % (self.component.chartId, _id))

  def getBounds(self):
    """   Returns the map's geographical bounds.
    When the bearing or pitch is non-zero, the visible region is not an axis-aligned rectangle,
    and the result is the smallest bounds that encompasses the visible region.
    If a padding is set on the map, the bounds returned are for the inset.
    This function isn't supported with globe projection.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/map/#map#getcontainer
    """
    return JsObjects.JsObject.JsObject("%s.getBounds()" % self.component.chartId)

  def getMaxBounds(self):
    """   Returns the maximum geographical bounds the map is constrained to, or null if none set.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/map/#map#getcontainer
    """
    return JsObjects.JsObject.JsObject("%s.getMaxBounds()" % self.component.chartId)

  def setMaxBounds(self, data: types.JS_DATA_TYPES):
    """   Sets or clears the map's geographical bound.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/map/#map#getcontainer

    :param data: The maximum bounds to set.
      If null or undefined is provided, the function removes the map's maximum bounds.
    """
    data = JsUtils.jsConvertData(data, None)
    return JsObjects.JsObject.JsObject("%s.setMaxBounds(%s)" % (self.component.chartId, data))

  def setMinZoom(self, data: types.JS_DATA_TYPES):
    """   Sets or clears the map's minimum zoom level. If the map's current zoom level is lower than the new minimum,
    the map will zoom to the new minimum.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/map/#map#getcontainer

    :param data: The maximum bounds to set.
      If null or undefined is provided, the function removes the map's maximum bounds.
    """
    data = JsUtils.jsConvertData(data, None)
    return JsObjects.JsObject.JsObject("%s.setMinZoom(%s)" % (self.component.chartId, data))

  def setMaxZoom(self, data: types.JS_DATA_TYPES):
    """   Sets or clears the map's maximum zoom level. If the map's current zoom level is higher than the new maximum,
    the map will zoom to the new maximum.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/map/#map#getcontainer

    :param data: The maximum bounds to set.
      If null or undefined is provided, the function removes the map's maximum bounds.
    """
    data = JsUtils.jsConvertData(data, None)
    return JsObjects.JsObject.JsObject("%s.setMaxZoom(%s)" % (self.component.chartId, data))

  def getMinZoom(self):
    """   Returns the map's minimum allowable zoom level.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/map/#map#getcontainer
    """
    return JsObjects.JsNumber.JsNumber("%s.getMinZoom()" % self.component.chartId)

  def getMaxZoom(self):
    """   Returns the map's maximum allowable zoom level.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/map/#map#getcontainer
    """
    return JsObjects.JsNumber.JsNumber("%s.getMaxZoom()" % self.component.chartId)

  def getStyle(self):
    """   Returns the map's Mapbox style object, a JSON object which can be used to recreate the map's style.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/map
      https://docs.mapbox.com/mapbox-gl-js/example/geojson-layer-in-stack/
    """
    return JsObjects.JsObject.JsObject("%s.getMaxZoom()" % self.component.chartId)

  def setBearing(self, bearing: int, event_data):
    """   Sets the map's bearing (rotation).
    The bearing is the compass direction that is "up"; for example, a bearing of 90° orients the map so that east is up.


    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/map
      https://docs.mapbox.com/mapbox-gl-js/example/dancing-buildings/

    :param bearing:
    :param event_data:
    """
    return JsUtils.jsWrap("%s.setBearing(%s)" % (self.component.chartId, bearing))

  def setFog(self, options: types.OPTION_TYPE = None):
    """   Set the default atmosphere style.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/example/simple-map/

    :param options: Optional. The fog properties
    """
    options = options or {}
    return JsUtils.jsWrap("%s.setFog(%s)" % (self.component.chartId, options))

  def setLight(self, light: str = None, options: dict = None):
    """   Sets the any combination of light values.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/example/simple-map/
      https://docs.mapbox.com/mapbox-gl-js/example/dancing-buildings/

    :param light:
    :param options:
    """
    if light is not None:
      light = JsUtils.jsConvertData(light, None)
      if options is None:
        return JsUtils.jsWrap("%s.setLight(%s)" % (self.component.chartId, light))

      else:
        options = JsUtils.jsConvertData(options, None)
        return JsUtils.jsWrap("%s.setLight(%s, %s)" % (self.component.chartId, light, options))

    else:
      options = JsUtils.jsConvertData(options, None)
      return JsUtils.jsWrap("%s.setLight(%s)" % (self.component.chartId, options))

  def setPaintProperty(self, layer_id: str, name: str, value: str, options: dict = None):
    """   Sets the value of a paint property in the specified style layer.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/example/simple-map/
      https://docs.mapbox.com/mapbox-gl-js/example/change-building-color-based-on-zoom-level/
    """
    layer_id = JsUtils.jsConvertData(layer_id, None)
    name = JsUtils.jsConvertData(name, None)
    value = JsUtils.jsConvertData(value, None)
    if options is None:
      return JsUtils.jsWrap("%s.setPaintProperty(%s, %s, %s)" % (self.component.chartId, layer_id, name, value))

    options = JsUtils.jsConvertData(options, None)
    return JsUtils.jsWrap("%s.setPaintProperty(%s, %s, %s, %s)" % (
      self.component.chartId, layer_id, name, value, options))

  def setLayoutProperty(self, layer_id: str, name: str, value: str, options: dict = None):
    """   Sets the value of a layout property in the specified style layer.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/example/simple-map/
      https://docs.mapbox.com/mapbox-gl-js/example/language-switch/
    """
    layer_id = JsUtils.jsConvertData(layer_id, None)
    name = JsUtils.jsConvertData(name, None)
    value = JsUtils.jsConvertData(value, None)
    if options is None:
      return JsUtils.jsWrap("%s.setLayoutProperty(%s, %s, %s)" % (self.component.chartId, layer_id, name, value))

    options = JsUtils.jsConvertData(options, None)
    return JsUtils.jsWrap("%s.setLayoutProperty(%s, %s, %s, %s)" % (
      self.component.chartId, layer_id, name, value, options))

  def setStyle(self, style: str, options: dict = None):
    """   Updates the map's Mapbox style object with a new value.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/example/simple-map/

    :param style: A JSON object conforming to the schema described in the Mapbox Style Specification ,
      or a URL to such JSON.
    :param options: Options object.
    """
    style = JsUtils.jsConvertData(style, None)
    if options is None:
      return JsUtils.jsWrap("%s.setStyle(%s)" % (self.component.chartId, style))

    options = JsUtils.jsConvertData(options, None)
    return JsUtils.jsWrap("%s.setStyle(%s, %s)" % (self.component.chartId, style, options))

  def setTerrain(self, terrain: types.JS_DATA_TYPES):
    """   Sets the terrain property of the style.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/example/simple-map/
      https://docs.mapbox.com/mapbox-gl-js/example/free-camera-path/

    :param terrain: Terrain properties to set. Must conform to the Terrain Style Specification .
    """
    terrain = JsUtils.jsConvertData(terrain, None)
    return JsUtils.jsWrap("%s.setTerrain(%s)" % (self.component.chartId, terrain))

  @property
  def _(self):
    """
    Tabulator standard components.

    Usage::

      table.js._.cell.getRow()
    """
    return _Export()

  def once(self):
    # https://docs.mapbox.com/mapbox-gl-js/example/add-fog/
    pass


class _Export:

  def FullscreenControl(self):
    """

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/example/fullscreen/
    """
    return JsUtils.jsWrap("new mapboxgl.FullscreenControl()")

  def GeolocateControl(self, options: dict = None):
    """

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/markers/

    :param options:
    """
    if options is not None:
      options = JsUtils.jsConvertData(options, None)
      return JsUtils.jsWrap("new mapboxgl.GeolocateControl(%s)" % options)

    return JsUtils.jsWrap("new mapboxgl.GeolocateControl()")

  def AttributionControl(self, options: dict = None):
    """

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/markers/

    :param options:
    """
    if options is not None:
      options = JsUtils.jsConvertData(options, None)
      return JsUtils.jsWrap("new mapboxgl.AttributionControl(%s)" % options)

    return JsUtils.jsWrap("new mapboxgl.AttributionControl()")

  def NavigationControl(self, options: dict = None):
    """

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/markers/

    :param options:
    """
    if options is not None:
      options = JsUtils.jsConvertData(options, None)
      return JsUtils.jsWrap("new mapboxgl.NavigationControl(%s)" % options)

    return JsUtils.jsWrap("new mapboxgl.NavigationControl()")

  def ScaleControl(self, options: dict = None):
    """

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/markers/

    :param options:
    """
    if options is not None:
      options = JsUtils.jsConvertData(options, None)
      return JsUtils.jsWrap("new mapboxgl.ScaleControl(%s)" % options)

    return JsUtils.jsWrap("new mapboxgl.ScaleControl()")

  def MapboxGeocoder(self, options: dict = None):
    """
    https://docs.mapbox.com/mapbox-gl-js/example/mapbox-gl-geocoder/

    :param options:
    :return:
    """
    return JsUtils.jsWrap("new mapboxgl.MapboxGeocoder()")
