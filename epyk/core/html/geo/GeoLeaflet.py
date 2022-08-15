#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html
from epyk.core.html.options import OptionsLeaflet
from epyk.core.js.packages import JsLeaflet
from epyk.core.js import JsUtils
from epyk.core.py import types


class GeoLeaflet(Html.Html):
  name = 'Leaflet Map'
  requirements = ('leaflet', )
  _option_cls = OptionsLeaflet.Leaflet

  def __init__(self, page, width, height, html_code, options, profile):
    self.height = height[0]
    super(GeoLeaflet, self).__init__(page, [], html_code=html_code, profile=profile, options=options,
                                     css_attrs={"width": width, "height": height})
    self.chartId = "%s_obj" % self.htmlCode
    self.style.css.display = "inline-block"
    self.__loader_funcs = []

  def click(self,  js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
            source_event: str = None, on_ready: bool = False):
    """
    Description:
    -----------
    The onclick event occurs when the user clicks on an element.
    This function will receive the region, code and element. The common data variable is mapped to the region.

    Usage:
    -----

    Related Pages:

      https://www.w3schools.com/jsref/event_onclick.asp

    Attributes:
    ----------
    :param js_funcs: A Javascript Python function
    :param profile: Optional. Set to true to get the profile for the function on the Javascript console.
    :param source_event: Optional. The source target for the event.
    :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self.js.onRegionClick(js_funcs, profile)
    return self

  @property
  def js(self) -> JsLeaflet.LeafLet:
    """
    Description:
    -----------
    The Javascript functions defined for this component.
    Those can be specific ones for the module or generic ones from the language.

    Usage::

    :return: A Javascript Dom object functions.
    """
    if self._js is None:
      self._js = JsLeaflet.LeafLet(selector="window['%s']" % self.chartId, component=self, page=self.page)
    return self._js

  @property
  def options(self) -> OptionsLeaflet.Leaflet:
    """
    Description:
    -----------
    Property to the component options.
    Options can either impact the Python side or the Javascript builder.

    Python can pass some options to the JavaScript layer.
    """
    return super().options

  # def build(self, data=None, options=None, profile=False, component_id=None):
  #
  #   """
  #   L.marker([48.804404, 2.123162]).addTo(%(chartId)s).bindPopup('A pretty CSS3 popup.<br> Easily customizable.').openPopup();
  #   L.marker([48.804404, 3.123162]).addTo(%(chartId)s).bindPopup('A pretty CSS3 popup.<br> Easily customizable.').openPopup();
  #
  #
  #   :param data:
  #   :param options:
  #   :param profile:
  #   :param component_id:
  #
  #   """
  #   return '''
  #     %(chartId)s = L.map('%(htmlId)s').setView([48.804404, 2.123162], 5);
  #     L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
  #       maxZoom: 18,
  #       attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
  #         'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
  #       id: 'mapbox/streets-v11',
  #       tileSize: 512,
  #       zoomOffset: -1
  #     }).addTo(%(chartId)s);
  #     ''' % {
  #     "chartId": self.chartId, "htmlId": self.htmlCode}

  def loader(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param js_funcs:
    :param profile:
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self.__loader_funcs.append(JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile))
    return self

  # def build(self, data=None, options=None, profile=False, component_id=None):
  #
  #   """
  #   L.marker([48.804404, 2.123162]).addTo(%(chartId)s).bindPopup('A pretty CSS3 popup.<br> Easily customizable.').openPopup();
  #   L.marker([48.804404, 3.123162]).addTo(%(chartId)s).bindPopup('A pretty CSS3 popup.<br> Easily customizable.').openPopup();
  #
  #
  #   :param data:
  #   :param options:
  #   :param profile:
  #   :param component_id:
  #
  #   """
  #   return '''
  #
  #   var map = L.map('%(htmlId)s');
  #
  #   map.setView([57, 14.5], 3);
  #
  #   map.createPane("labels");
  #
  #   L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  #       attribution: '©OpenStreetMap, ©CartoDB'
  #   }).addTo(map);
  #   var geoMap = L.geoJson([], {
  #       clickable: true,
  #       style: function (feature) {
  #           return myCustomStyle(feature.properties.adm0_a3)
  #       },
  #       onEachFeature: onEachFeature
  #   }).addTo(map);
  #
  #   geoMap.eachLayer(function (layer) {
  #       layer.bindPopup(layer.feature.properties.name);
  #   });
  #
  #   function highlightFeature(e) {
  #       var layer = e.target;
  #
  #       layer.setStyle({
  #           fillColor: '#AAA',
  #           dashArray: ''
  #       });
  #
  #       if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
  #           layer.bringToFront();
  #       }
  #   }
  #
  #   function resetHighlight(e) {
  #       geoMap.resetStyle(e.target);
  #   }
  #
  #   function zoomToFeature(e) {
  #       map.fitBounds(e.target.getBounds());
  #   }
  #
  #   function onEachFeature(feature, layer) {
  #       layer.on({
  #           mouseover: highlightFeature,
  #           mouseout: resetHighlight,
  #           click: zoomToFeature
  #       });
  #   }
  #     ''' % {
  #     "chartId": self.chartId, "htmlId": self.htmlCode}
  #

  def build(self, data=None, options: dict = None, profile: types.PROFILE_TYPE = False, component_id: str = None):
    """

    :param data:
    :param options:
    :param profile:
    :param component_id:
    """
    str_frg = JsUtils.jsConvertFncs(self.__loader_funcs, toStr=True, profile=profile)
    self.builder_name = "LeafletBuilder%s" % self.page.py.hash(str_frg)
    self._js__builder__ = str_frg

    return super().build(data, options, profile)

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    return '<div %s></div>' % self.get_attrs(css_class_names=self.style.get_classes())
