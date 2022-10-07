#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union, List
from epyk.core.py import primitives

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsString
from epyk.core.js.primitives import JsObject
from epyk.core.js.primitives import JsObjects
from epyk.core.js.primitives import JsBoolean


class JsGeolocation:

  def __init__(self, page: primitives.PageModel):
    self.page, self.options = page, {}

  def set_timeout(self, value: float):
    """
    Amount of time before the error callback is invoked, if 0 it will never invoke.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/getCurrentPosition
 
    :param float value: Time in milliseconds.
    """
    self.options["timeout"] = value
    return self

  def set_maximum_age(self, value: float):
    """
    Maximum cached position age.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/getCurrentPosition
 
    :param float value: Time in milliseconds.
    """
    self.options["maximumAge"] = value
    return self

  def set_enable_high_accuracy(self, flag: bool = False):
    """
    Indicates the application would like to receive the best possible results

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/getCurrentPosition
 
    :param bool flag: If true and if the device is able to provide a more accurate position.
    """
    self.options["enableHighAccuracy"] = flag
    return self

  def getCurrentPosition(self, callback_func: Union[List[Union[str, primitives.JsDataModel]], str] = None,
                         error_func=None, options=None, profile=None):
    """
    The getCurrentPosition() method is used to return the user's position.

    You can use the underlying data object pk.events.geolocationPosition to get geo location information.

    Usage::

      page.ui.button("Test").click([
        page.js.navigator.geolocation.getCurrentPosition([
          page.js.console.log(pk.events.geolocationPosition.accuracy),
          page.js.console.log(pk.events.geolocationPosition.latitude),
        ]),
      ])

    Related Pages:

      https://developer.mozilla.org/fr/docs/Web/API/Geolocation/getCurrentPosition
      https://www.w3schools.com/html/html5_geolocation.asp
      https://developer.kaiostech.com/api/geolocation/getposition
 
    :param callback_func: String. A callback function that takes a Position object as its sole input parameter.
    :param error_func: String. Optional. An callback func that takes a PositionError object as its sole input parameter.
    :param options: Dictionary. Optional. An optional PositionOptions object.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    options = options or self.options
    callback_func = JsUtils.jsConvertFncs(callback_func, toStr=True, profile=profile)
    return JsObject.JsObject.get(
      "navigator.geolocation.getCurrentPosition(function(navPos){let data = navPos; %s}, function(err){%s}, %s)" % (
        callback_func, JsUtils.jsConvertFncs(
          error_func, toStr=True, profile=profile), JsUtils.jsConvertData(options, None)))

  def watchPosition(self, callback_func: Union[List[Union[str, primitives.JsDataModel]], str],
                    watch_id, error_func=None, options=None, profile=None, global_scope=True):
    """
    Returns the current position of the user and continues to return updated position as the user moves.

    Usage::

      c.click([
        page.js.navigator.geolocation.watchPosition([
          page.js.console.log(pk.events.geolocationPosition.accuracy),
          page.js.console.log(pk.events.geolocationPosition.latitude),
        ], "geoId", [page.js.alert("error")]),
        #page.js.alert("Test")
      ])

    Related Pages:

      https://www.w3schools.com/html/html5_geolocation.asp
 
    :param callback_func: String. A callback function that takes a Position object as an input parameter.
    :param watch_id: The ID number returned by the Geolocation.watchPosition() method when installing the handler you
      wish to remove.
    :param error_func: Optional An optional callback function that takes a PositionError object as an input parameter.
    :param options: Optional An optional PositionOptions object that provides configuration options for the location
      watch.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param global_scope: Boolean. Optional. Flag to properly set the scope for global variables.
    """
    options = options or self.options
    callback_func = JsUtils.jsConvertFncs(callback_func, toStr=True, profile=profile)
    if global_scope:
      watch_id = "window['%s']" % watch_id
    return JsObject.JsObject.new(
      "navigator.geolocation.watchPosition(function(navPos){let data = navPos; %s}, function(err){%s}, %s)" % (
        callback_func, JsUtils.jsConvertFncs(
          error_func, toStr=True, profile=profile), JsUtils.jsConvertData(options, None))
      , is_py_data=False).setVar(watch_id)

  def clearWatch(self, watch_id, global_scope: bool = True):
    """
    Stops the watchPosition() method.

    Usage::

      page.ui.button("Stop").click([
        page.js.navigator.geolocation.clearWatch("geoId")
      ])

    Related Pages:

      https://www.w3schools.com/html/html5_geolocation.asp
 
    :param watch_id: The ID number returned by the Geolocation.watchPosition() method when installing the handler
    you wish to remove.
    :param bool global_scope: Optional. Flag to properly set the scope for global variables.
    """
    if global_scope:
      watch_id = "window['%s']" % watch_id
    return JsObject.JsObject("navigator.geolocation.clearWatch(%s)" % watch_id, is_py_data=False)


class JsClipboard:

  def __init__(self, page: primitives.PageModel):
    self.page, self.options = page, {}

  def readText(self):
    return JsObjects.JsPromise("window.navigator.clipboard.readText()")


class JsNavigator:

  def __init__(self, page: primitives.PageModel):
    self.page = page

  @property
  def geolocation(self):
    """
    The HTML Geolocation API is used to locate a user's position.

    Related Pages:

      https://w3c.github.io/geolocation-api/#navi-geo
      https://www.w3schools.com/html/html5_geolocation.asp
    """
    return JsGeolocation(self.page)

  @property
  def language(self):
    """
    The language property returns the language version of the browser.

    Related Pages:

      https://www.w3schools.com/jsref/prop_nav_language.asp
    """
    return JsString.JsString("navigator.language", is_py_data=False)

  @property
  def browserLanguage(self):
    """
    The language property returns the language version of the browser.
    For IE10 and earlier versions, you can use the browserLanguage property.

    Related Pages:

      https://www.w3schools.com/jsref/prop_nav_language.asp
    """
    return JsString.JsString("navigator.browserLanguage", is_py_data=False)

  @property
  def appCodeName(self):
    """
    The appCodeName property returns the application code name of the browser.

    Related Pages:

      https://www.w3schools.com/js/js_window_navigator.asp
    """
    return JsString.JsString("navigator.appCodeName", is_py_data=False)

  @property
  def appName(self):
    """
    The appName property returns the application name of the browser.

    Related Pages:

      https://www.w3schools.com/js/js_window_navigator.asp
    """
    return JsString.JsString("navigator.appName", is_py_data=False)

  @property
  def product(self):
    """
    The product property returns the product name of the browser engine.

    Related Pages:

      https://www.w3schools.com/js/js_window_navigator.asp
    """
    return JsString.JsString("navigator.product", is_py_data=False)

  @property
  def appVersion(self):
    """
    The appVersion property returns version information about the browser.

    Related Pages:

      https://www.w3schools.com/js/js_window_navigator.asp
    """
    return JsString.JsString("navigator.appVersion", is_py_data=False)

  @property
  def cookieEnabled(self):
    """
    """
    return JsString.JsString("navigator.cookieEnabled", is_py_data=False)

  @property
  def onLine(self):
    """
    The onLine property returns true if the browser is online.

    Related Pages:

      https://www.w3schools.com/js/js_window_navigator.asp
    """
    return JsBoolean.JsBoolean("navigator.onLine", is_py_data=False)

  @property
  def platform(self):
    """
    The platform property returns the browser platform (operating system).

    Related Pages:

      https://www.w3schools.com/js/js_window_navigator.asp
    """
    return JsString.JsString("navigator.platform", is_py_data=False)

  @property
  def userAgent(self):
    """
    The userAgent property returns the user-agent header sent by the browser to the server.

    Related Pages:

      https://www.w3schools.com/js/js_window_navigator.asp

    """
    return JsString.JsString("navigator.userAgent", is_py_data=False)

  def javaEnabled(self):
    """
    The javaEnabled() method returns a Boolean value that specifies whether the browser has Java enabled.

    Related Pages:

      https://www.w3schools.com/jsref/met_nav_javaenabled.asp
    """
    return JsBoolean.JsBoolean("navigator.javaEnabled()", is_py_data=False)

  @property
  def clipboard(self) -> JsClipboard:
    """

    """
    return JsClipboard(self.page)
