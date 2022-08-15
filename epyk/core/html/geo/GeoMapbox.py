#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html
from epyk.core.py import types
from epyk.core.html.options import OptMapbox
from epyk.core.js.packages import JsMapbox
from epyk.core.js import JsUtils


class GeoMapbox(Html.Html):
  name = 'MapBox Map'
  requirements = ('mapbox-gl', )
  _option_cls = OptMapbox.OptionsMapbox

  def __init__(self,  page, width, height, html_code, options, profile):
    self.height = height[0]
    super(GeoMapbox, self).__init__(page, [], html_code=html_code, profile=profile, options=options,
                                    css_attrs={"width": width, "height": height})
    self.chartId = "window['%s_obj']" % self.htmlCode
    self.options.container = self.htmlCode
    self.style.css.display = "inline-block"

  _js__builder__ = """window[""+ htmlObj.id + "_obj"] = new mapboxgl.Map(options) """

  @property
  def js(self) -> JsMapbox.MapBoxMap:
    """
    Description:
    -----------
    The Javascript functions defined for this component.
    Those can be specific ones for the module or generic ones from the language.

    Usage::

      l = page.ui.geo.mapbox.globe() # page.ui.geo.leaflet.europe()
      l.load([l.js.addControl([l.js._.FullscreenControl()])])

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/

    :return: A Javascript Dom object functions.
    """
    if self._js is None:
      self._js = JsMapbox.MapBoxMap(selector=self.chartId, component=self, page=self.page)
    return self._js

  @property
  def options(self) -> OptMapbox.OptionsMapbox:
    """
    Description:
    -----------
    Property to the component options.
    Options can either impact the Python side or the Javascript builder.

    Python can pass some options to the JavaScript layer.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/api/
    """
    return super().options

  def load(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
    """
    Description:
    -----------
    Fired immediately after all necessary resources have been downloaded and the first visually complete rendering
    of the map has occurred.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/example/simple-map/

    Attributes:
    ----------
    :param js_funcs: The Javascript function definition
    :param profile: Optional. A flag to set the component performance storage
    """
    self.page.body.onReady("%s.on('load', () => {%s})" % (
      self.chartId, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)), profile=profile)

  def loading(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
    """
    Description:
    -----------
    Fired when any map data loads or changes. See MapDataEvent for more information.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/example/simple-map/

    Attributes:
    ----------
    :param js_funcs: The Javascript function definition
    :param profile: Optional. A flag to set the component performance storage
    """
    self.page.body.onReady("%s.on('data', () => {%s})" % (
      self.chartId, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)), profile=profile)

  def resize(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
    """
    Description:
    -----------
    Fired immediately after the map has been resized.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/example/simple-map/

    Attributes:
    ----------
    :param js_funcs: The Javascript function definition
    :param profile: Optional. A flag to set the component performance storage
    """
    self.page.body.onReady("%s.on('resize', () => {%s})" % (
      self.chartId, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)), profile=profile)

  def remove(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
    """
    Description:
    -----------
    Fired immediately after the map has been removed with Map.event:remove.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/example/simple-map/

    Attributes:
    ----------
    :param js_funcs: The Javascript function definition
    :param profile: Optional. A flag to set the component performance storage
    """
    self.page.body.onReady("%s.on('remove', () => {%s})" % (
      self.chartId, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)), profile=profile)

  def mousedown(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
    """
    Description:
    -----------
    Fired when a pointing device (usually a mouse) is pressed within the map.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/example/simple-map/

    Attributes:
    ----------
    :param js_funcs: The Javascript function definition
    :param profile: Optional. A flag to set the component performance storage
    """
    self.page.body.onReady("%s.on('mousedown', function(e) {%s})" % (
      self.chartId, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)), profile=profile)

  def mouseup(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
    """
    Description:
    -----------
    Fired when a pointing device (usually a mouse) is released within the map.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/example/simple-map/

    Attributes:
    ----------
    :param js_funcs: The Javascript function definition
    :param profile: Optional. A flag to set the component performance storage
    """
    self.page.body.onReady("%s.on('mouseup', function(e) {%s})" % (
      self.chartId, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)), profile=profile)

  def dblclick(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
    """
    Description:
    -----------
    Fired when a pointing device (usually a mouse) is pressed and released twice at the same point
    on the map in rapid succession.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/example/simple-map/

    Attributes:
    ----------
    :param js_funcs: The Javascript function definition
    :param profile: Optional. A flag to set the component performance storage
    """
    self.page.body.onReady("%s.on('dblclick', function(e) {%s})" % (
      self.chartId, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)), profile=profile)

  def click(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
    """
    Description:
    -----------
    Fired when a pointing device (usually a mouse) is pressed and released at the same point on the map.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/example/simple-map/

    Attributes:
    ----------
    :param js_funcs: The Javascript function definition
    :param profile: Optional. A flag to set the component performance storage
    """
    self.page.body.onReady("%s.on('click', function(e) {%s})" % (
      self.chartId, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)), profile=profile)

  def on(self, event_type: str, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
    """
    Description:
    -----------
    Fired when a pointing device (usually a mouse) is pressed and released at the same point on the map.

    Related Pages:

      https://docs.mapbox.com/mapbox-gl-js/example/simple-map/

    Attributes:
    ----------
    :param event_type: The JavaScript event type
    :param js_funcs: The Javascript function definition
    :param profile: Optional. A flag to set the component performance storage
    """
    event_type = JsUtils.jsConvertData(event_type, None)
    self.page.body.onReady("%s.on(%s, function(e) {%s})" % (event_type,
      self.chartId, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)), profile=profile)

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    return '<div %s></div>' % self.get_attrs(css_class_names=self.style.get_classes())
