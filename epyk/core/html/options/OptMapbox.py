#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union
from epyk.core.py import types
from epyk.core.html.options import Options
from epyk.core.html.options import Enums


class EnumStyles(Enums):

  def street(self):
    self._set_value(value="mapbox://styles/mapbox/streets-v11")

  def outdoors(self):
    self._set_value(value="mapbox://styles/mapbox/outdoors-v11")

  def light(self):
    self._set_value(value="mapbox://styles/mapbox/light-v10")

  def dark(self):
    self._set_value(value="mapbox://styles/mapbox/dark-v10")

  def satellite(self):
    self._set_value(value="mapbox://styles/mapbox/satellite-v9")

  def satellite_street(self):
    self._set_value(value="mapbox://styles/mapbox/satellite-streets-v11")

  def navigation_dark(self):
    self._set_value(value="mapbox://styles/mapbox/navigation-day-v1")

  def navigation_night(self):
    self._set_value(value="mapbox://styles/mapbox/navigation-night-v1")


class EnumProjections(Enums):

  def globe(self):
    """
    Description:
    ------------
    3d Globe as globe

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/example/globe/
    """
    self._set_value()

  def naturalEarth(self):
    """
    Description:
    ------------
    This example uses the Map's projection parameter to display the map using the Natural Earth ('naturalEarth')
    projection instead of the default Mercator projection.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/example/map-projection/
    """
    self._set_value()

  def albers(self):
    """
    Description:
    ------------
    Albers equal-area conic projection as albers

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/example/globe/
    """
    self._set_value()

  def equalEarth(self):
    """
    Description:
    ------------
    Equal Earth equal-area pseudocylindrical projection as equalEarth

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/example/globe/
    """
    self._set_value()

  def equirectangular(self):
    """
    Description:
    ------------
    Equirectangular (Plate Carrée/WGS84) as equirectangular.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/example/globe/
    """
    self._set_value()

  def lambertConformalConic(self):
    """
    Description:
    ------------
    Lambert Conformal Conic as lambertConformalConic.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/example/globe/
    """
    self._set_value()

  def mercator(self):
    """
    Description:
    ------------
    Mercator cylindrical map projection as mercator.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/example/globe/
    """
    self._set_value()

  def winkelTripel(self):
    """
    Description:
    ------------
    Winkel Tripel azimuthal map projection as winkelTripel.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/example/globe/
    """
    self._set_value()


class OptionsMapbox(Options):

  @property
  def accessToken(self):
    """
    Description:
    ------------
    If specified, map will use this token instead of the one defined in mapboxgl.accessToken.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(None)

  @accessToken.setter
  def accessToken(self, value: str):
    self._config(value)

  @property
  def antialias(self):
    """
    Description:
    ------------
    If true , the gl context will be created with MSAA antialiasing ,
    which can be useful for antialiasing custom layers. This is false by default as a performance optimization.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(False)

  @antialias.setter
  def antialias(self, flag: bool):
    self._config(flag)

  @property
  def attributionControl(self):
    """
    Description:
    ------------
    If true , an AttributionControl will be added to the map.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(True)

  @attributionControl.setter
  def attributionControl(self, flag: bool):
    self._config(flag)

  @property
  def bearing(self):
    """
    Description:
    ------------
    The initial bearing (rotation) of the map, measured in degrees counter-clockwise from north.
    If bearing is not specified in the constructor options, Mapbox GL JS will look for it in the map's style object.
    If it is not specified in the style, either, it will default to 0 .

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(0)

  @bearing.setter
  def bearing(self, value: float):
    self._config(value)

  @property
  def bearingSnap(self):
    """
    Description:
    ------------
    The threshold, measured in degrees, that determines when the map's bearing will snap to north.
    For example, with a bearingSnap of 7, if the user rotates the map within 7 degrees of north,
    the map will automatically snap to exact north.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(7)

  @bearingSnap.setter
  def bearingSnap(self, value: float):
    self._config(value)

  @property
  def bounds(self):
    """
    Description:
    ------------
    The initial bounds of the map.
    If bounds is specified, it overrides center and zoom constructor options.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(None)

  @bounds.setter
  def bounds(self, value: str):
    self._config(value)

  @property
  def boxZoom(self):
    """
    Description:
    ------------
    If true , the "box zoom" interaction is enabled (see BoxZoomHandler ).

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(True)

  @boxZoom.setter
  def boxZoom(self, flag: bool):
    self._config(flag)

  @property
  def container(self):
    """
    Description:
    ------------
    The HTML element in which Mapbox GL JS will render the map, or the element's string id .
    The specified element must have no children.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(None)

  @container.setter
  def container(self, value: str):
    self._config(value)

  @property
  def interactive(self):
    """
    Description:
    ------------
    If false , no mouse, touch, or keyboard listeners will be attached to the map, so it will not respond
    to interaction.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(True)

  @interactive.setter
  def interactive(self, flag: bool):
    self._config(flag)

  @property
  def keyboard(self):
    """
    Description:
    ------------
    If true , keyboard shortcuts are enabled (see KeyboardHandler ).

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(True)

  @keyboard.setter
  def keyboard(self, flag: bool):
    self._config(flag)

  @property
  def cooperativeGestures(self):
    """
    Description:
    ------------
    If true , scroll zoom will require pressing the ctrl or ⌘ key while scrolling to zoom map,
    and touch pan will require using two fingers while panning to move the map. Touch pitch will require three fingers
    to activate if enabled.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(None)

  @cooperativeGestures.setter
  def cooperativeGestures(self, num: int):
    self._config(num)

  @property
  def crossSourceCollisions(self):
    """
    Description:
    ------------
    If true , symbols from multiple sources can collide with each other during collision detection.
    If false , collision detection is run separately for the symbols in each source.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(True)

  @crossSourceCollisions.setter
  def crossSourceCollisions(self, flag: bool):
    self._config(flag)

  @property
  def customAttribution(self):
    """
    Description:
    ------------
    String or strings to show in an AttributionControl .
    Only applicable if options.attributionControl is true .

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(None)

  @customAttribution.setter
  def customAttribution(self, num: int):
    self._config(num)

  @property
  def doubleClickZoom(self):
    """
    Description:
    ------------
    If true , the "double click to zoom" interaction is enabled (see DoubleClickZoomHandler ).

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(True)

  @doubleClickZoom.setter
  def doubleClickZoom(self, flag: bool):
    self._config(flag)

  @property
  def dragPan(self):
    """
    Description:
    ------------
    If true , the "drag to pan" interaction is enabled. An Object value is passed as options to DragPanHandler#enable .

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(True)

  @dragPan.setter
  def dragPan(self, flag: bool):
    self._config(flag)

  @property
  def dragRotate(self):
    """
    Description:
    ------------
    If true , the "drag to rotate" interaction is enabled (see DragRotateHandler ).

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(True)

  @dragRotate.setter
  def dragRotate(self, flag: bool):
    self._config(flag)

  @property
  def fadeDuration(self):
    """
    Description:
    ------------
    Controls the duration of the fade-in/fade-out animation for label collisions, in milliseconds.
    This setting affects all symbol layers. This setting does not affect the duration of runtime styling transitions
    or raster tile cross-fading.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(300)

  @fadeDuration.setter
  def fadeDuration(self, num: int):
    self._config(num)

  @property
  def failIfMajorPerformanceCaveat(self):
    """
    Description:
    ------------
    If true , map creation will fail if the performance of Mapbox GL JS would be dramatically worse than expected
    (a software renderer would be used).

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(False)

  @failIfMajorPerformanceCaveat.setter
  def failIfMajorPerformanceCaveat(self, num: int):
    self._config(num)

  @property
  def fitBoundsOptions(self):
    """
    Description:
    ------------
    A Map#fitBounds options object to use only when fitting the initial bounds provided above.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(None)

  @fitBoundsOptions.setter
  def fitBoundsOptions(self, num: int):
    self._config(num)

  @property
  def hash(self):
    """
    Description:
    ------------
    If true , the map's position (zoom, center latitude, center longitude, bearing, and pitch) will be synced with the
    hash fragment of the page's URL.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(None)

  @hash.setter
  def hash(self, flag: bool):
    self._config(flag)

  @property
  def language(self):
    """
    Description:
    ------------
    A string representing the language used for the map's data and UI components.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(None)

  @language.setter
  def language(self, value: str):
    self._config(value)

  @property
  def locale(self):
    """
    Description:
    ------------
    A patch to apply to the default localization table for UI strings such as control tooltips.
    The locale object maps namespaced UI string IDs to translated strings in the target language;

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(None)

  @locale.setter
  def locale(self, value: str):
    self._config(value)

  @property
  def localFontFamily(self):
    """
    Description:
    ------------
    Defines a CSS font-family for locally overriding generation of all glyphs.
    Font settings from the map's style will be ignored, except for font-weight keywords (light/regular/medium/bold).
    If set, this option overrides the setting in localIdeographFontFamily.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(False)

  @localFontFamily.setter
  def localFontFamily(self, flag: bool):
    self._config(flag)

  @property
  def localIdeographFontFamily(self):
    """
    Description:
    ------------
    Defines a CSS font-family for locally overriding generation of glyphs in the 'CJK Unified Ideographs', 'Hiragana',
    'Katakana', 'Hangul Syllables' and 'CJK Symbols and Punctuation' ranges. In these ranges,
    font settings from the map's style will be ignored, except for font-weight keywords

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get("sans-serif")

  @localIdeographFontFamily.setter
  def localIdeographFontFamily(self, value: str):
    self._config(value)

  @property
  def logoPosition(self):
    """
    Description:
    ------------
    A string representing the position of the Mapbox wordmark on the map.
    Valid options are top-left , top-right , bottom-left , bottom-right .

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get("bottom-left")

  @logoPosition.setter
  def logoPosition(self, value: str):
    self._config(value)

  @property
  def maxBounds(self):
    """
    Description:
    ------------
    If set, the map will be constrained to the given bounds.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(None)

  @maxBounds.setter
  def maxBounds(self, value: str):
    self._config(value)

  @property
  def maxPitch(self):
    """
    Description:
    ------------
    The maximum pitch of the map (0-85).

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(85)

  @maxPitch.setter
  def maxPitch(self, num: int):
    self._config(num)

  @property
  def maxTileCacheSize(self):
    """
    Description:
    ------------
    The maximum number of tiles stored in the tile cache for a given source. If omitted,
    the cache will be dynamically sized based on the current viewport.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(None)

  @maxTileCacheSize.setter
  def maxTileCacheSize(self, num: float):
    self._config(num)

  @property
  def pitch(self):
    """
    Description:
    ------------
    The initial pitch (tilt) of the map, measured in degrees away from the plane of the screen (0-85).
    If pitch is not specified in the constructor options, Mapbox GL JS will look for it in the map's style object.
    If it is not specified in the style, either, it will default to 0 .

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(0)

  @pitch.setter
  def pitch(self, num: int):
    self._config(num)

  @property
  def pitchWithRotate(self):
    """
    Description:
    ------------
    If false , the map's pitch (tilt) control with "drag to rotate" interaction will be disabled.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(True)

  @pitchWithRotate.setter
  def pitchWithRotate(self, flag: bool):
    self._config(flag)

  @property
  def preserveDrawingBuffer(self):
    """
    Description:
    ------------
    If true , the map's canvas can be exported to a PNG using map.getCanvas().toDataURL() .
    This is false by default as a performance optimization.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(False)

  @preserveDrawingBuffer.setter
  def preserveDrawingBuffer(self, flag: bool):
    self._config(flag)

  @property
  def styles(self):
    """
    Description:
    ------------
    The map's Mapbox style enumeration.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/map/
    """
    return EnumStyles(self, "style")

  @property
  def style(self):
    """
    Description:
    ------------
    The map's Mapbox style.
    This must be an a JSON object conforming to the schema described in the Mapbox Style Specification ,
    or a URL to such JSON. Can accept a null value to allow adding a style manually.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(None)

  @style.setter
  def style(self, value: str):
    self._config(value)

  @property
  def center(self):
    """
    Description:
    -----------
    The initial geographical centerpoint of the map.
    If center is not specified in the constructor options, Mapbox GL JS will look for it in the map's style object.
    If it is not specified in the style, either, it will default to [0, 0] Note: Mapbox GL uses longitude,
    latitude coordinate order (as opposed to latitude, longitude) to match GeoJSON.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/example/simple-map/
    """
    return self._config_get([0, 0])

  @center.setter
  def center(self, values: list):
    self._config(values)

  def set_center(self, lon: float, lat: float):
    """
    Description:
    -----------
    Starting position [lng, lat]

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/example/simple-map/
      https://docs.mapbox.com/mapbox-gl-js/api/

    Attributes:
    ----------
    :param lon: The longitude
    :param lat: The latitude
    """
    self.center = [lon, lat]

  @property
  def clickTolerance(self):
    """
    Description:
    ------------
    The max number of pixels a user can shift the mouse pointer during a click for it to be considered a valid
    click (as opposed to a mouse drag).

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(3)

  @clickTolerance.setter
  def clickTolerance(self, num: float):
    self._config(num)

  @property
  def collectResourceTiming(self):
    """
    Description:
    ------------
    If true , Resource Timing API information will be collected for requests made by GeoJSON and Vector
    Tile web workers (this information is normally inaccessible from the main Javascript thread).
    Information will be returned in a resourceTiming property of relevant data events.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(False)

  @collectResourceTiming.setter
  def collectResourceTiming(self, num: float):
    self._config(num)

  @property
  def maxZoom(self):
    """
    Description:
    ------------
    The maximum zoom level of the map (0-24).

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(22)

  @maxZoom.setter
  def maxZoom(self, num: float):
    self._config(num)

  @property
  def minPitch(self):
    """
    Description:
    ------------
    The minimum pitch of the map (0-85).

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(0)

  @minPitch.setter
  def minPitch(self, num: float):
    self._config(num)

  @property
  def minTileCacheSize(self):
    """
    Description:
    ------------
    The minimum number of tiles stored in the tile cache for a given source.
    Larger viewports use more tiles and need larger caches.
    Larger viewports are more likely to be found on devices with more memory and on pages where the map
    is more important. If omitted, the cache will be dynamically sized based on the current viewport.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(None)

  @minTileCacheSize.setter
  def minTileCacheSize(self, num: float):
    self._config(num)

  @property
  def minZoom(self):
    """
    Description:
    ------------
    The minimum zoom level of the map (0-24).

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(0)

  @minZoom.setter
  def minZoom(self, num: float):
    self._config(num)

  @property
  def optimizeForTerrain(self):
    """
    Description:
    ------------
    With terrain on, if true , the map will render for performance priority, which may lead to layer reordering
    allowing to maximize performance (layers that are draped over terrain will be drawn first, including fill,
    line, background, hillshade and raster). Otherwise, if set to false , the map will always be drawn for
    layer order priority.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(0)

  @optimizeForTerrain.setter
  def optimizeForTerrain(self, flag: bool):
    self._config(flag)

  @property
  def projections(self):
    """
    Description:
    ------------
    Projection enumerations.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/example/map-projection/
      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return EnumProjections(self, "projection")

  @property
  def projection(self):
    """
    Description:
    ------------
    The projection the map should be rendered in.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get("mercator")

  @projection.setter
  def projection(self, value: str):
    self._config(value)

  @property
  def refreshExpiredTiles(self):
    """
    Description:
    ------------
    If false , the map won't attempt to re-request tiles once they expire per their HTTP cacheControl / expires headers.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(True)

  @refreshExpiredTiles.setter
  def refreshExpiredTiles(self, flag: bool):
    self._config(flag)

  @property
  def renderWorldCopies(self):
    """
    Description:
    ------------
    If true , multiple copies of the world will be rendered side by side beyond -180 and 180 degrees longitude.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(True)

  @renderWorldCopies.setter
  def renderWorldCopies(self, flag: bool):
    self._config(flag)

  @property
  def scrollZoom(self):
    """
    Description:
    ------------
    If true , the "scroll to zoom" interaction is enabled.
    An Object value is passed as options to ScrollZoomHandler#enable .

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(True)

  @scrollZoom.setter
  def scrollZoom(self, flag: bool):
    self._config(flag)

  @property
  def testMode(self):
    """
    Description:
    ------------
    Silences errors and warnings generated due to an invalid accessToken,
    useful when using the library to write unit tests.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(False)

  @testMode.setter
  def testMode(self, flag: bool):
    self._config(flag)

  @property
  def touchPitch(self):
    """
    Description:
    ------------
    If true , the "drag to pitch" interaction is enabled. An Object value is passed as options to TouchPitchHandler .

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(True)

  @touchPitch.setter
  def touchPitch(self, flag: bool):
    self._config(flag)

  @property
  def touchZoomRotate(self):
    """
    Description:
    ------------
    If true , the "pinch to rotate and zoom" interaction is enabled.
    An Object value is passed as options to TouchZoomRotateHandler#enable .

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(True)

  @touchZoomRotate.setter
  def touchZoomRotate(self, value: Union[str, bool]):
    self._config(value)

  @property
  def trackResize(self):
    """
    Description:
    ------------
    If true , the map will automatically resize when the browser window resizes.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(True)

  @trackResize.setter
  def trackResize(self, flag: bool):
    self._config(flag)

  @property
  def worldview(self):
    """
    Description:
    ------------
    Sets the map's worldview. A worldview determines the way that certain disputed boundaries are rendered.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(None)

  @worldview.setter
  def worldview(self, value: str):
    self._config(value)

  def transformRequest(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
    raise NotImplementedError("Not available yet")

  @property
  def zoom(self):
    """
    Description:
    ------------
    The initial zoom level of the map.
    If zoom is not specified in the constructor options, Mapbox GL JS will look for it in the map's style object.
    If it is not specified in the style, either, it will default to 0 .

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return self._config_get(0)

  @zoom.setter
  def zoom(self, num: float):
    self._config(num)
