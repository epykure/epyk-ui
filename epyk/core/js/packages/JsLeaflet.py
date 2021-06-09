from epyk.core.js import JsUtils
from epyk.core.js.packages import JsPackage


class LTooltip:

  def __init__(self, latlng=None, options=None, selector=None):
    self._selector = selector
    self._js, self.__is_attached = [], False
    self.varId = "L.marker(%s)" % latlng

  def openTooltip(self):
    """
    Description:
    -----------

    """
    self._js.append("openTooltip()")
    return self

  def toStr(self):
    js_fnc = ".".join(self._js)
    self._js = []
    return "%s.%s" % (self.varId, js_fnc)


class LMarker:

  def __init__(self, latlng, options=None, leaflet_map=None):
    self.leaflet_map, self.latlng = leaflet_map, latlng
    self._js, self.__is_attached, self.options = [], False, options or {}
    self.varId = "L.marker"

  def addTo(self, selector=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param selector:
    """
    self._js.append("addTo(%s)" % selector)
    self.__is_attached = True
    return self

  def bindPopup(self, content):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param content:
    """
    self._js.append("bindPopup(%s)" % JsUtils.jsConvertData(content, None))
    popup = LPopup()
    popup.varId = self.toStr()
    return popup

  def bindTooltip(self, content):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param content:
    """
    self._js.append("bindTooltip(%s)" % JsUtils.jsConvertData(content, None))
    tooltip = LTooltip()
    tooltip.varId = self.toStr()
    return tooltip

  def toStr(self):
    if not self.__is_attached and self.leaflet_map is not None:
      self.addTo(self.leaflet_map.varName)
    js_fnc = ".".join(self._js)
    self._js = []
    return "%s(%s, %s).%s" % (self.varId, self.latlng, JsUtils.jsConvertData(self.options, None), js_fnc)


class LCircle(LMarker):

  def __init__(self, latlng, options=None, shape="circle", leaflet_map=None):
    super(LCircle, self).__init__(latlng, options, leaflet_map)
    self.varId = "L.%s" % shape

  def radius(self, num):
    self.options["radius"] = num
    return self

  def color(self, hexcode):
    self.options["color"] = hexcode
    return self

  def fillOpacity(self, num):
    self.options["fillOpacity"] = num
    return self

  def fillColor(self, hexcode):
    self.options["fillColor"] = hexcode
    return self

  def weight(self, num):
    self.options["weight"] = num
    return self


class LPopup:

  def __init__(self, latlng=None, options=None, selector=None):
    self._selector = selector
    self._js, self.__is_attached = [], False
    self.varId = "L.marker(%s)" % latlng

  def openPopup(self):
    """
    Description:
    -----------

    """
    self._js.append("openPopup()")
    return self

  def setLatLng(self, latlng):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param latlng:
    """
    self._js.append("setLatLng(%s)" % latlng)
    return self

  def setContent(self, content):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param content: String. The popup content.
    """
    self._js.append("setContent(%s)" % JsUtils.jsConvertData(content, None))
    return self

  def openOn(self):
    pass

  def toStr(self):
    if not self._js:
      return self.varId

    js_fnc = ".".join(self._js)
    self._js = []
    return "%s.%s" % (self.varId, js_fnc)


class LtileLayer:

  def __init__(self, component, token, url, options, leaflet_map=None):
    self.component, self.leaflet_map = component, leaflet_map
    self.srv_url = "%s?access_token=%s" % (url, token)
    self.options, self.__is_attached, self._js = options or {}, False, []

  def attribution(self, text):
    self.options["attribution"] = text
    return self

  def maxZoom(self, num):
    self.options["maxZoom"] = num
    return self

  def minZoom(self, num):
    self.options["minZoom"] = num
    return self

  def id(self, value):
    self.options["id"] = value
    return self

  def tileSize(self, num):
    self.options["tileSize"] = num
    return self

  def zoomOffset(self, num):
    self.options["zoomOffset"] = num
    return self

  def accessToken(self, token):
    self.srv_url = "%s?access_token=%s" % (self.srv_url.split("?")[0], token)
    return self

  def addTo(self, map):
    self.__is_attached = True
    self._js.append("addTo(%s)" % map)
    return self

  def toStr(self):
    if not self.__is_attached and self.leaflet_map is not None:
      self.addTo(self.leaflet_map.varName)
    js_fnc = ".".join(self._js)
    self._js = []
    return "L.tileLayer(%s, %s).%s" % (
      JsUtils.jsConvertData(self.srv_url, None), JsUtils.jsConvertData(self.options, None), js_fnc)


class LMapAttributionControl:

  def __init__(self, varId=None):
    self._js = []
    self.varId = varId

  def addAttribution(self, text):
    return "%s.addAttribution(%s)" % (self.varId, JsUtils.jsConvertData(text, None))


class LMap:

  def __init__(self, component=None, set_var=None):
    self.component = component
    self._js, self.set_var = [], set_var
    self.varId = "L.map(%s)" % JsUtils.jsConvertData(component.htmlCode, None)

  @property
  def varName(self):
    return self.varId or self.set_var or "window['%s']" % self.component.chartId

  def setView(self, LatLng, zoom=None):
    """
    Description:
    -----------
    Sets the view of the map (geographical center and zoom) with the given animation options.

    Related Pages:

      https://leafletjs.com/reference-1.7.1.html#map-example

    Attributes:
    ----------
    :param LatLng: List.
    :param zoom: Integer. Optional.
    """
    if zoom is not None:
      self._js.append("setView(%s, %s)" % (LatLng, zoom))
    else:
      self._js.append("setView(%s)" % LatLng)
    return self

  def on(self, typeEvent, jsFuncs, profile=None):
    return JsUtils.jsWrap("%s; %s.on('%s', function(){%s})" % (
      self.toStr(), self.varName, typeEvent, JsUtils.jsConvertFncs(jsFuncs, toStr=True, profile=profile)))

  def locationfound(self, jsFuncs, profile=None):
    """

    https://leafletjs.com/examples/mobile/

    :param jsFuncs:
    :param profile:
    :return:
    """
    return self.on("locationfound", jsFuncs, profile)

  def locationerror(self, jsFuncs, profile=None):
    """

    https://leafletjs.com/examples/mobile/

    :param jsFuncs:
    :param profile:
    :return:
    """
    return self.on("locationerror", jsFuncs, profile)

  def createPane(self, text):
    return JsUtils.jsWrap("%s; %s.createPane(%s)" % (self.toStr(), self.varName, JsUtils.jsConvertData(text, None)))

  def fitBounds(self):
    pass

  @property
  def attributionControl(self):
    return LMapAttributionControl("%s.attributionControl" % self.toStr())

  def fitWorld(self):
    self._js.append("fitWorld()")
    return self

  def locate(self, options=None):
    options = options or {"setView": True, "maxZoom": 16}
    self._js.append("locate(%s)" % JsUtils.jsConvertData(options, None))
    return self

  def toStr(self):
    if not self._js:
      return self.varName

    js_fnc = ".".join(self._js)
    self._js = []
    if self.set_var is not None:
      expr = "%s = %s.%s" % (self.set_var, self.varId, js_fnc)
      self.set_var = None
      self.varId = self.set_var
      return expr

    return "%s.%s" % (self.varId, js_fnc)


class LGeoJSON(LMarker):

  def __init__(self, shapes, options=None, leaflet_map=None):
    super(LGeoJSON, self).__init__(JsUtils.jsConvertData(shapes, None), options, leaflet_map)
    self.varId = "L.geoJSON"


class LControl:

  def __init__(self, component=None, options=None, set_var=None):
    self.component = component
    self._js, self.set_var = [], set_var
    self.varId, self.varName = "L.control()" if options is None else "L.control(%s)" % JsUtils.jsConvertData(options, None), None

  def onAdd(self, jsFuncs, profile=None):
    pass

  def update(self, jsFuncs, profile=None):
    pass

  def addTo(self):
    pass

  def toStr(self):
    if not self._js:
      return self.varId

    js_fnc = ".".join(self._js)
    self._js = []
    if self.set_var is not None:
      expr = "var %s = %s.%s" % (self.set_var, self.varId, js_fnc)
      self.set_var = None
      self.varId = self.set_var
      return expr

    return "%s.%s" % (self.varId, js_fnc)


class LeafLet(JsPackage):
  lib_alias = {'js': "leaflet", 'css': 'leaflet'}

  def __init__(self, htmlCode=None, config=None, src=None, varName=None, selector=None, setVar=False):
    self.src = src if src is not None else self.__internal()
    self._selector = selector
    self.varName, self.setVar = varName or self._selector, setVar
    self.src.jsImports.add(self.lib_alias['js'])
    self.src.cssImport.add(self.lib_alias['css'])
    self._js, self._map, self._control = [], None, {}

  @property
  def map(self):
    if self._map is None:
      self._map = LMap(self.src, set_var=self._selector)
    return self._map

  def control(self, alias, options=None):
    if alias not in self._control:
      self._control[alias] = LControl(self.src, options=options, set_var=self._selector)
    return self._control[alias]



  def setZoom(self, zoom):
    """
    Description:
    -----------
    Sets the zoom of the map.

    hRelated Pages:

      ttps://leafletjs.com/reference-1.7.1.html#map-example

    Attributes:
    ----------
    :param zoom:
    """
    return JsUtils.jsWrap("%s.setZoom(%s)" % (self._selector, zoom))

  def setView(self, LatLng, zoom=None):
    """
    Description:
    -----------
    Sets the view of the map (geographical center and zoom) with the given animation options.

    Related Pages:

      https://leafletjs.com/reference-1.7.1.html#map-example

    Attributes:
    ----------
    :param LatLng:
    :param zoom:
    """
    if zoom is not None:
      return JsUtils.jsWrap("%s.setView(%s, %s)" % (self._selector, LatLng, zoom))

    return JsUtils.jsWrap("%s.setView(%s)" % (self._selector, LatLng))

  def zoomIn(self, delta):
    """
    Description:
    -----------
    Increases the zoom of the map by delta (zoomDelta by default).

    Attributes:
    ----------
    :param delta:
    """
    return JsUtils.jsWrap("%s.zoomIn(%s)" % (self._selector, delta))

  def marker(self, latlng, options=None):
    """
    Description:
    -----------

    Related Pages:

      https://leafletjs.com/reference-1.7.1.html#marker

    Attributes:
    ----------
    :param latlng:
    :param options:
    """
    return LMarker(latlng, options, leaflet_map=self.map)

  def circle(self, latlng, options=None):
    return LCircle(latlng, options, leaflet_map=self.map)

  def tileLayer(self, token, options=None, url="https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}"):
    return LtileLayer(self.src, token, url, options, leaflet_map=self.map)

  def popup(self, options=None, source=None):
    """
    Description:
    -----------

    Related Pages:

      https://leafletjs.com/reference-1.7.1.html#popup-l-popup

    Attributes:
    ----------
    :param options:
    :param source:
    """
    pass

  def tooltip(self, options=None, source=None):
    """
    Description:
    -----------

    Related Pages:

      https://leafletjs.com/reference-1.7.1.html#tooltip-l-tooltip

    Attributes:
    ----------
    :param options:
    :param source:
    """
    return LTooltip(options, self._selector)

  def imageOverlay(self):
    """
    Description:
    -----------

    Related Pages:

      https://leafletjs.com/reference-1.7.1.html#imageoverlay-l-imageoverlay

    """
    pass

  def videoOverlay (self):
    pass

  def svgOverlay(self):
    pass

  def polyline(self, latlng1, latlng2, options=None):
    return LCircle([latlng1, latlng2], options, shape="polyline", leaflet_map=self.map)

  def polygon(self, latlng1, latlng2, options=None):
    return LCircle([latlng1, latlng2], options, shape="polygon", leaflet_map=self.map)

  def rectangle(self, latlng1, latlng2, options=None):
    return LCircle([latlng1, latlng2], options, shape="rectangle", leaflet_map=self.map)

  def circleMarker(self):
    pass

  def layerGroup(self):
    pass

  def featureGroup(self):
    pass

  def geoJSON(self, shapes, options=None):
    """

    https://leafletjs.com/examples/geojson/

    """
    return LGeoJSON(shapes, options, leaflet_map=self.map)

  def latLng(self):
    pass
