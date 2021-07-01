#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import os

from epyk.core.html import KeyCodes

from epyk.core.js import Imports
from epyk.core.js import JsLocation
from epyk.core.js import JsMaths
from epyk.core.js import JsNavigator
from epyk.core.js import JsPerformance
from epyk.core.js import JsUtils
from epyk.core.js import JsWindow
from epyk.core.js import JsWebSocket
from epyk.core.js import JsMsgAlerts

# All the predefined variable types
from epyk.core.js.fncs import JsFncs
from epyk.core.js.objects import JsData
from epyk.core.js.objects import JsNodeAttributes
from epyk.core.js.objects import JsNodeDom
from epyk.core.js.primitives import JsNumber
from epyk.core.js.primitives import JsObject
from epyk.core.js.primitives import JsObjects
from epyk.core.js.primitives import JsString

# All the predefined Javascript Statements
from epyk.core.js.statements import JsIf
from epyk.core.js.statements import JsWhile
from epyk.core.js.statements import JsSwitch
from epyk.core.js.statements import JsFor


class JsConsole:
  """
  Description:
  ------------
  This is a wrapper to the Console.

  Related Pages:

    https://medium.freecodecamp.org/how-to-get-the-most-out-of-the-javascript-console-b57ca9db3e6d
  """

  def __init__(self, page=None):
    self.page = page

  @property
  def debugger(self):
    """
    Description:
    ------------
    Trigger a Javascript debugger from this point.
    The Javascript will be stopped and it will be possible to check the process step by step in the browser using F12.

    Usage::

      page.js.console.debugger

    Related Pages:

      https://www.w3schools.com/jsref/jsref_debugger.asp

    :return: The Javascript Keyword to trigger the browser debugger.
    """
    return JsObject.JsKeyword("debugger")

  @property
  def clear(self):
    """
    Description:
    ------------
    The console.clear() method clears the console.

    Usage::

      page.js.console.clear

    Related Pages:

      https://www.w3schools.com/jsref/met_console_clear.asp

    :return: The Javascript String used to clear the console (F12 in standard browsers).
    """
    return JsFncs.JsFunction("console.clear()")

  def log(self, jsData, jsConvFnc=None, skip_data_convert=False):
    """
    Description:
    ------------
    The console.log() method writes a message to the console.

    Usage::

      page.js.console.log("Test")

    Related Pages:

      https://www.w3schools.com/jsref/met_console_log.asp

    Attributes:
    ----------
    :param jsData: String | Object. The Javascript fragment.
    :param jsConvFnc: String. Optional. A specific JavaScript data conversion function.
    :param skip_data_convert: Boolean. Optional. Flag to specify to the framework if a Json conversion is needed.

    :return: The Javascript String used to clear the console (F12 in standard browsers)
    """
    if skip_data_convert:
      return JsFncs.JsFunction("console.log(%s)" % jsData)

    if isinstance(jsData, list):
      jsData = JsUtils.jsWrap(JsUtils.jsConvertFncs(jsData, toStr=True))
    # display directly the content of the component
    if hasattr(jsData, 'dom'):
      return JsFncs.JsFunction("console.log(%s)" % JsUtils.jsConvertData(jsData.dom.content, jsConvFnc))

    return JsFncs.JsFunction("console.log(%s)" % JsUtils.jsConvertData(jsData, jsConvFnc))

  def info(self, jsData, jsConvFnc=None):
    """
    Description:
    ------------
    The console.info() method writes a message to the console.

    Related Pages:

      https://www.w3schools.com/jsref/met_console_info.asp

    Attributes:
    ----------
    :param jsData: String | Object. The Javascript fragment.
    :param jsConvFnc: String. Optional. A specific JavaScript data conversion function.

    :return: The Javascript String used to clear the console (F12 in standard browsers)
    """
    return JsFncs.JsFunction("console.info(%s)" % JsUtils.jsConvertData(jsData, jsConvFnc))

  def warn(self, jsData, jsConvFnc=None):
    """
    Description:
    ------------
    The console.warn() method writes a warning to the console.

    Related Pages:

      https://www.w3schools.com/jsref/met_console_warn.asp

    Attributes:
    ----------
    :param jsData: String | Object. The Javascript fragment.
    :param jsConvFnc: String. Optional. A specific JavaScript data conversion function.

    :return: The Javascript String used to clear the console (F12 in standard browsers)
    """
    return JsFncs.JsFunction("console.warn(%s)" % JsUtils.jsConvertData(jsData, jsConvFnc))

  def error(self, jsData, jsConvFnc=None):
    """
    Description:
    ------------
    The console.error() method writes an error message to the console.

    Related Pages:

      https://www.w3schools.com/jsref/met_console_error.asp

    Attributes:
    ----------
    :param jsData: String | Object. The Javascript fragment.
    :param jsConvFnc: String. Optional. A specific JavaScript data conversion function.

    :return: The Javascript String used to clear the console (F12 in standard browsers)
    """
    return JsFncs.JsFunction("console.error(%s)" % JsUtils.jsConvertData(jsData, jsConvFnc))

  def table(self, jsData, jsHeader=None):
    """
    Description:
    ------------
    The console.table() method writes a table in the console view.

    Related Pages:

      https://www.w3schools.com/jsref/met_console_table.asp

    Attributes:
    ----------
    :param jsData: String | Object. Required. The data to fill the table with.
    :param jsHeader: List. Optional. An array containing the names of the columns to be included in the table.

    :return: The Javascript String used to clear the console (F12 in standard browsers).
    """
    if jsHeader is not None:
      return JsFncs.JsFunction("console.table(%s, %s)" % (jsData, jsHeader))

    return JsFncs.JsFunction("console.table(%s)" % jsData)

  def time(self, htmlCode):
    """
    Description:
    ------------
    The console.time() method starts a timer in the console view.

    Related Pages:

      https://www.w3schools.com/jsref/met_console_time.asp

    Attributes:
    ----------
    :param htmlCode: String. Use the label parameter to give the timer a name.

    :return: A Python Javascript Number.
    """
    return JsNumber.JsNumber("console.time('%s')" % htmlCode, isPyData=False)

  def timeEnd(self, htmlCode):
    """
    Description:
    ------------
    The console.timeEnd() method ends a timer, and writes the result in the console view.

    Related Pages:

      https://www.w3schools.com/jsref/met_console_timeend.asp

    Attributes:
    ----------
    :param htmlCode: String. The name of the timer to end.

    :return: The Javascript String used to clear the console (F12 in standard browsers).
    """
    return JsFncs.JsFunction("console.timeEnd('%s')" % htmlCode)

  def _assert(self, jsData, strInfo, jsConvFnc=None):
    """
    Description:
    ------------
    The console.assert() method writes a message to the console, but only if an expression evaluates to false.

    Related Pages:

      https://www.w3schools.com/jsref/met_console_assert.asp

    Attributes:
    ----------
    :param jsData: String | Object. The Javascript fragment.
    :param strInfo: String. The JavaScript result.
    :param jsConvFnc: String. Optional. A specific JavaScript data conversion function.
    """
    return JsFncs.JsFunction("console.assert('%s', '%s')" % (JsUtils.jsConvertData(jsData, jsConvFnc), strInfo))

  def tryCatch(self, jsFncs, jsFncsErrs="console.warn(err.message)", profile=False):
    """
    Description:
    ------------
    Javascript Try Catch Exceptions.

    Related Pages:

      https://www.w3schools.com/jsref/jsref_obj_error.asp

    Attributes:
    ----------
    :param jsFncs: String or List. The Javascript functions.
    :param jsFncsErrs: String or List. The Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.

    :return: The Javascript String used to clear the console (F12 in standard browsers)
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    return JsFncs.JsFunction(
      "try{%s} catch(err){%s}" % (JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile), jsFncsErrs))

  def perf(self, varName, label=None):
    """
    Description:
    ------------
    Shortcut function to display performances from a variable.
    The variable must be global. Namely the name should start with window.

    Attributes:
    ----------
    :param varName: String. The variable var name use to compute the performance.
    :param label: String. Optional. The description.
    """
    if label is not None:
      return JsFncs.JsFunction("console.log('%s' + (performance.now() - %s) + 'ms')" % (label, varName))

    return JsFncs.JsFunction("console.log((performance.now() - %s) + 'ms')" % varName)

  def service(self, msg, headers=None):
    """
    Description:
    ------------
    Send logs to the backend.

    Attributes:
    ----------
    :param msg: String. The log message to be sent to the backend.
    :param headers: Dictionary the service headers.
    """
    from epyk import LOG_SERVICE

    if LOG_SERVICE is None:
      raise Exception("Log service must be defined pk.LOG_SERVICE = <service_url>")

    return self.page.post(LOG_SERVICE, {"content": msg}, headers=headers, asynchronous=True)


class JsJson:
  """
  Description:
  ------------
  Wrapper around the Javascript Json module.

  This wrapper will only wrapper the different functions available in the underlying library.
  The documentation can be found in each function or are available on the Javascript Official documentation.

  Related Pages:

    https://www.w3schools.com/js/js_json_intro.asp
  """

  def parse(self, jsData, jsResultFnc=None, jsConvFnc=None):
    """
    Description:
    ------------
    Parses a JSON string and returns a JavaScript object.

    Related Pages:

      https://www.w3schools.com/js/js_json_parse.asp
      https://www.w3schools.com/jsref/jsref_parse_json.asp

    Attributes:
    ----------
    :param jsData: String. A String corresponding to a JavaScript object.
    :param jsResultFnc: Optional. A function used to transform the result. The function is called for each item.
                                  Any nested objects are transformed before the parent.
    :param jsConvFnc: String. Optional. A specific JavaScript data conversion function.

    :return: The Javascript string method
    """
    jsData = JsUtils.jsConvertData(jsData, jsConvFnc)
    if jsResultFnc is not None:
      return JsFncs.JsFunction("JSON.parse(%s, %s)" % (jsData, jsResultFnc))

    return JsFncs.JsFunction("JSON.parse(%s)" % jsData)

  def stringify(self, jsData, replacer=None, space=0, jsConvFnc=None):
    """
    Description:
    ------------
    The JSON.stringify() method converts JavaScript objects into strings.

    Related Pages:

      https://www.w3schools.com/js/js_json_stringify.asp

    Attributes:
    ----------
    :param jsData: String. Required. The value to convert to a string.
    :param replacer: Optional. Either a function or an array used to transform the result.
                               The replacer is called for each item.
    :param space: Optional. Either a String or a Number. A string to be used as white space (max 10 characters),
      or a Number, from 0 to 10, to indicate how many space characters to use as white space.
    :param jsConvFnc: String. Optional. A specific JavaScript data conversion function.

    :return: The Javascript string method.
    """
    return JsString.JsString(
      "JSON.stringify(%s, %s, %s)" % (
        JsUtils.jsConvertData(jsData, jsConvFnc), json.dumps(replacer), space), isPyData=False)


class JsBreadCrumb:

  def __init__(self, src=None):
    self._src = src
    self._selector = "breadcrumb"
    self._anchor = None
    self._src.properties.js.add_builders("%s = {pmts: %s}" % (self._selector, json.dumps(self._src.inputs)))

  def add(self, key, jsData, jsConvFnc=None):
    """
    Description:
    ------------
    Add an entry to the Javascript breadcrumb dictionary.

    Attributes:
    ----------
    :param key: String. The key in the Breadcrumb dictionary.
    :param jsData: String. A String corresponding to a JavaScript object.
    :param jsConvFnc: String. Optional. A specific JavaScript data conversion function.
    """
    return JsFncs.JsFunction('%s["pmts"]["%s"] = %s' % (self._selector, key, JsUtils.jsConvertData(jsData, jsConvFnc)))

  def get(self, key=None):
    """
    Description:
    ------------
    returns the object stored in the breadcrumb dictionary.

    Attributes:
    ----------
    :param key: String. Optional. The key in the Breadcrumb dictionary.

    :return: A Python object.
    """
    if key is None:
      return JsObject.JsObject("%s" % self._selector)

    return JsObject.JsObject('%s["pmts"]["%s"]' % (self._selector, key))

  def hash(self, jsData, jsConvFnc=None):
    """
    Description:
    ------------
    Add an anchor to the URL after the hash tag.

    Related Pages:

      https://www.w3schools.com/jsref/prop_loc_hash.asp

    Attributes:
    ----------
    :param jsData: String. A String corresponding to a JavaScript object.
    :param jsConvFnc: String. Optional. A specific JavaScript data conversion function.
    """
    return JsObject.JsObject('%s["anchor"] = %s' % (self._selector, JsUtils.jsConvertData(jsData, jsConvFnc)))

  @property
  def url(self):
    """
    Description:
    ------------
    Get the full URL.
    """
    js_location = JsLocation.JsLocation()
    origin = js_location.origin
    pathname = js_location.pathname
    return JsString.JsString(origin + pathname + "?" + JsObject.JsObject(self.toStr()))

  def toStr(self):
    return '%s(%s)' % (JsFncs.FncOnRecords(self._src._props['js']).url(), self._selector)


class JsScreen:

  @property
  def availHeight(self):
    """
    Description:
    ------------
    The availHeight property returns the height of the user's screen, in pixels, minus interface features
    like the Windows Task bar.

    Related Pages:

      https://www.w3schools.com/jsref/prop_screen_availheight.asp
    """
    return JsNumber.JsNumber("screen.availHeight")

  @property
  def availWidth(self):
    """
    Description:
    ------------
    The availWidth property returns the width of the user's screen, in pixels, minus interface features like the
    Windows Task bar.

    Related Pages:

      https://www.w3schools.com/jsref/prop_screen_availwidth.asp
    """
    return JsNumber.JsNumber("screen.availWidth")

  @property
  def colorDepth(self):
    """
    Description:
    ------------
    The colorDepth property returns the bit depth of the color palette for displaying images (in bits per pixel).

    Related Pages:

      https://www.w3schools.com/jsref/prop_screen_colordepth.asp
    """
    return JsNumber.JsNumber("screen.colorDepth")

  @property
  def height(self):
    """
    Description:
    ------------
    The height property returns the total height of the user's screen, in pixels.

    Related Pages:

      https://www.w3schools.com/jsref/prop_screen_height.asp
    """
    return JsNumber.JsNumber("screen.height")

  @property
  def pixelDepth(self):
    """
    Description:
    ------------
    The pixelDepth property returns the color resolution (in bits per pixel) of the visitor's screen.

    Related Pages:

      https://www.w3schools.com/jsref/prop_screen_pixeldepth.asp
    """
    return JsNumber.JsNumber("screen.pixelDepth")

  @property
  def width(self):
    """
    Description:
    ------------
    The width property returns the total width of the user's screen, in pixels.

    Related Pages:

      https://www.w3schools.com/jsref/prop_screen_width.asp
    """
    return JsNumber.JsNumber("screen.width")


class JsBase:
  class __internal:
    _props, _context, http = {}, {}, []
    jsImports, cssImport = set([]), set([])

  def __init__(self, src=None, component=None):
    # The underlying source object is not supposed to be touched in the underlying classes
    self._src = src if src else self.__internal()
    self.component, self.page = component, src
    self.console = JsConsole(self)
    self.localStorage = JsWindow.JsLocalStorage()
    self.window = JsWindow.JsWindow(self)
    self.performance = JsPerformance.JsPerformance(self)
    self.sessionStorage = JsWindow.JsSessionStorage()
    self.json = JsJson()
    self.math = JsMaths.JsMaths()
    self._jquery_ref = None

    # shortcut functions
    self.alert = self.window.alert
    self.log = self.console.log
    self._breadcrumb, self.__data, self.__location = None, None, None

  @property
  def viewHeight(self):
    """
    Description:
    -----------
    Return the current View port height visible in the browser.
    """
    return JsNumber.JsNumber("Math.max(%s, %s)" % (self.documentElement.clientHeight, self.window.innerHeight))

  @property
  def documentElement(self):
    """
    Description:
    -----------
    Document.documentElement returns the Element that is the root element of the document (for example,
    the <html> element for HTML documents).

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/Document/documentElement
    """
    return JsNodeDom.JsDoms.get("document.documentElement")

  @property
  def screen(self):
    """
    Description:
    ------------
    The screen object contains information about the visitor's screen.

    Related Pages:

      https://www.w3schools.com/jsref/obj_screen.asp
    """
    return JsScreen()

  @property
  def navigator(self):
    """
    Description:
    ------------
    The information from the navigator object can often be misleading, and should not be used to detect
    browser versions because:

      - Different browsers can use the same name.
      - The navigator data can be changed by the browser owner.
      - Some browsers misidentify themselves to bypass site tests.
      - Browsers cannot report new operating systems, released later than the browser.
    """
    return JsNavigator.JsNavigator(self)

  @property
  def location(self):
    """
    Description:
    ------------
    Property to the Javascript Location functions.

    Related Pages:

      https://www.w3schools.com/jsref/obj_location.asp

    :rtype: JsLocation.JsLocation
    """
    if self.__location is None:
      self.__location = JsLocation.JsLocation()
    return self.__location

  @property
  def objects(self):
    """
    Description:
    ------------
    Interface to the main Javascript Classes and Primitives.

    :rtypw: JsObjects.JsObjects
    """
    return JsObjects.JsObjects(self)

  @property
  def jquery(self):
    """
    Description:
    ------------
    jQuery is a fast, small, and feature-rich JavaScript library.

    It makes things like HTML document traversal and manipulation, event handling, animation, and Ajax much simpler
    with an easy-to-use API that works across a multitude of browsers.
    With a combination of versatility and extensibility, jQuery has changed the way that millions of
    people write JavaScript.

    Related Pages:

      https://jquery.com/
    """
    from epyk.core.js.packages import JsQuery

    if self.component is not None:
      return JsQuery.JQuery(self.component, varName=JsQuery.decorate_var(self.component.htmlCode), setVar=False)

    return JsQuery.JQuery(self._jquery_ref)

  def eval(self, jsData, jsConvFnc=None):
    """
    Description:
    ------------
    The eval() function evaluates JavaScript code represented as a string.

    Warning: Executing JavaScript from a string is an enormous security risk.
    It is far too easy for a bad actor to run arbitrary code when you use eval(). See Never use eval()!, below.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval

    Attributes:
    ----------
    :param jsData: String. Data to be evaluated.
    :param jsConvFnc: String. Optional. A specific JavaScript data conversion function.
    """
    return JsObject.JsObject("eval(%s)" % JsUtils.jsConvertData(jsData, jsConvFnc))

  def socketio(self, htmlCode=None):
    """
    Description:
    ------------
    This object must be created on the Python side.

    The various function will be the one generating the Javascript string.
    This is just a Python wrapper on top of the library.

    Related Pages:

      https://www.tutorialspoint.com/socket.io/socket.io_event_handling.htm

    Attributes:
    ----------
    :param htmlCode: String. Optional. The WebSocket id (variable name) on the JavaScript side.
    """
    from epyk.core.js.packages import JsSocketIO

    return JsSocketIO.SocketIO(htmlCode, self._src)

  def websocket(self, htmlCode=None, secured=False):
    """
    Description:
    ------------
    WebSocket client applications use the WebSocket API to communicate with WebSocket servers
    using the WebSocket protocol.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications
      https://javascript.info/websocket

    Attributes:
    ----------
    :param htmlCode: String. Optional. The WebSocket id (variable name) on the JavaScript side.
    :param secured: Boolean. Optional. To define the right protocol for the WebSocket connection we or wss.
    """
    return JsWebSocket.WebSocket(htmlCode, self._src, secured)

  def worker(self, htmlCode=None, server=False):
    """
    Description:
    ------------
    A web worker is a JavaScript running in the background, without affecting the performance of the page.

    Related Pages:

      https://www.w3schools.com/html/html5_webworkers.asp

    Attributes:
    ----------
    :param htmlCode: String. The WebSocket id (variable name) on the JavaScript side.
    :param server: Boolean.
    """
    return JsWebSocket.Worker(htmlCode, self._src, server)

  def serverSentEvent(self, htmlCode=None):
    """
    Description:
    ------------
    SSE is a native HTML5 feature that allows the server to keep the HTTP connection open and push data
    changes to the client.
    Server-sent Streaming is really ideal for server-push notifications, device monitoring and all other tasks
    that do not require real-time push back from the client.

    Related Pages:

      https://medium.com/code-zen/python-generator-and-html-server-sent-events-3cdf14140e56
      https://www.w3schools.com/html/html5_serversentevents.asp
      https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events

    Attributes:
    ----------
    :param htmlCode: String. The EventSource id (variable name) on the JavaScript side.
    """
    return JsWebSocket.ServerSentEvent(htmlCode, self._src)

  @property
  def d3(self):
    """
    Description:
    ------------
    D3.js is a JavaScript library for manipulating documents based on data.
    D3 helps you bring data to life using HTML, SVG, and CSS.

    D3’s emphasis on web standards gives you the full capabilities of modern browsers without tying yourself to a
    proprietary framework, combining powerful visualization components and a data-driven approach to DOM manipulation.

    Related Pages:

      https://d3js.org/
    """
    from epyk.core.js.packages import JsD3

    return JsD3.JsD3(self._src, "d3")

  def not_(self, data, jsConvFnc=None):
    """
    Description:
    ------------
    Add the Symbol (!) for the boolean negation.
    This feature is also available directly to any JsBoolean objects.

    Usage::

      jsObj.not_(jsObj.objects.boolean.get("weekend"))

    Related Pages:

      https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Op%C3%A9rateurs/Op%C3%A9rateurs_logiques

    Attributes:
    ----------
    :param data: String. A String corresponding to a JavaScript object.
    :param jsConvFnc: String. Optional. A specific JavaScript data conversion function.

    :return: The Javascript fragment string.
    """
    return JsFncs.JsFunction("!%s" % JsUtils.jsConvertData(data, jsConvFnc))

  def if_(self, jsCond, jsFncs, profile=False):
    """
    Description:
    ------------
    Conditional statements are used to perform different actions based on different conditions.

    Related Pages:

      https://www.w3schools.com/js/js_if_else.asp

    Attributes:
    ----------
    :param jsCond: String. The Javascript condition. Can be a JsBoolean object.
    :param jsFncs: List | String. Optional. The Javascript functions.
    :param profile: Boolean. Optional. A flag to set the component performance storage.
    """
    if isinstance(jsCond, list):
      jsCond = "(%s)" % ")||(".join(JsUtils.jsConvertFncs(jsCond))
    self.__if = JsIf.JsIf(jsCond, jsFncs, self._src, profile)
    return self.__if

  def while_(self, jsCond, jsFnc, options=None, profile=False):
    """
    Description:
    ------------
    The while loop loops through a block of code as long as a specified condition is true.

    Related Pages:

      https://www.w3schools.com/js/js_loop_while.asp

    Attributes:
    ----------
    :param jsCond: String. The JavaScript condition.
    :param jsFnc: List | String. Javascript functions.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean. Optional. A flag to set the component performance storage.
    """
    if isinstance(jsCond, list):
      jsCond = "(%s)" % ")||(".join(JsUtils.jsConvertFncs(jsCond))
    self.__while = JsWhile.JsWhile(jsCond, options, self._src).fncs(jsFnc, profile=profile)
    return self.__while

  def for_(self, jsFnc, step=1, start=0, end=10, options=None, profile=False):
    """
    Description:
    ------------
    Shortcut to a for loop.

    Related Pages:

      https://www.w3schools.com/js/js_loop_for.asp

    Attributes:
    ----------
    :param jsFnc: List | String. Javascript functions.
    :param step: Integer. The increment index. Default 1.
    :param start: Integer. The first index in the for loop.
    :param end: Integer. The last index in the for loop.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean. Optional. A flag to set the component performance storage.
    """
    for_statment = JsFor.JsFor(end, options)
    for_statment.start = start
    for_statment.end = end
    for_statment.step = step
    return for_statment.fncs(jsFnc, profile=profile)

  def return_(self, jsData):
    """
    Description:
    ------------
    Javascript return keyword.

    Attributes:
    ----------
    :param jsData: The Javascript expression.
    """
    return JsFncs.JsFunction("return %s" % jsData)

  def switch(self, variable, jsConvFnc=None):
    """
    Description:
    ------------
    switch statement is used to perform different actions based on different conditions.

    Related Pages:

      https://www.w3schools.com/js/js_switch.asp

    Attributes:
    ----------
    :param variable: String | Js Object. Variable on which we will apply the switch.
    :param jsConvFnc: String. Optional. A specific JavaScript data conversion function.
    """
    if hasattr(variable, 'dom'):
      variable = variable.dom.content
    variable = JsUtils.jsConvertData(variable, jsConvFnc)
    self.__switch = JsSwitch.JsSwitch(variable)
    return self.__switch

  def clipboard(self, jsData, jsConvFnc=None):
    """
    Description:
    ------------
    Copy the full URL to rhe clipboard.

    Related Pages:

      https://isabelcastillo.com/hidden-input-javascript

    Attributes:
    ----------
    :param jsData: Object | String. The Javascript expression.
    :param jsConvFnc: String. Optional. A specific JavaScript data conversion function.
    """
    return JsFncs.JsFunction('''
        var elInput = document.createElement('input'); elInput.setAttribute('type', 'text');
        elInput.setAttribute('value', %s); document.body.appendChild(elInput);
        document.execCommand('copy', false, elInput.select()); elInput.remove()
        ''' % JsUtils.jsConvertData(jsData, jsConvFnc))

  def _addImport(self, importAlias):
    """
    Description:
    ------------
    Internal function to include an external JavaScript module.
    This can only use pre defined modules. This will fail during the resolution if it does not exist.

    Attributes:
    ----------
    :param importAlias: String. Alias reference of a JavaScript module.
    """
    self._src._props.setdefault('js', {}).setdefault('imports', set([])).add(importAlias)
    return self

  @staticmethod
  def typeof(jsData, type=None):
    """
    Description:
    ------------
    The typeof function.

    Related Pages:

      https://www.w3schools.com/js/js_datatypes.asp

    Attributes:
    ----------
    :param jsData: String. A String corresponding to a JavaScript object.
    :param type: String. Optional. The type of object.
    """
    if type is None:
      return JsObjects.JsBoolean.JsBoolean("typeof %s" % jsData)

    return JsObjects.JsVoid("typeof %s === '%s'" % (jsData, type))

  def custom(self, jsData, jsDataKey=None, isPyData=False, jsFnc=None):
    """
    Description:
    ------------
    Allow the definition of bespoke javascript strings.

    Attributes:
    ----------
    :param jsData: String. A String corresponding to a JavaScript object.
    :param jsDataKey: String. Optional. A key reference in the JavaScript object.
    :param isPyData: Boolean. Optional. Specify if the data is in Python and should be jsonify first.
    :param jsFnc: List | String. Optional. Javascript functions.
    """
    jsData = JsUtils.jsConvert(jsData, jsDataKey, isPyData, jsFnc)
    self._src._props.setdefault('js', {}).setdefault('bespoke', []).append(jsData)

  def customText(self, text):
    """
    Description:
    ------------
    Javascript fragment added at the beginning of the page.
    This will be called before any function in the framework.

    Attributes:
    ----------
    :param text: String. The Javascript fragment.

    :return: self to allow the chaining.
    """
    self._src.properties.js.add_text(text)
    return self

  def customFile(self, filename, path=None):
    """
    Description:
    ------------
    This will load your local javascript file when the report will be built.
    Then you will be able to use the new features in the different Javascript wrappers.

    Attributes:
    ----------
    :param filename: String. The file name.
    :param path: String. optional. The file path.

    :return: The Js Object to allow the chaining.
    """
    if path is None:
      self._src.jsLocalImports.add("%s/js/%s" % (Imports.STATIC_PATH.replace("\\", "/"), filename))
    else:
      self._src.jsLocalImports.add("%s/%s" % (path, filename))
    self.page.imports.addPackage('local_%s' % filename[:-3], {'version': "",
      'register': {'alias': 'local_%s' % filename[:-3], 'module': filename[:-3], 'npm_path': 'dist/maps/continents/'},
      'modules': [{'script': filename, "path": '', 'cdnjs': path}]})
    self.page.jsImports.add('local_%s' % filename[:-3])
    return self

  def extendProto(self, pyClass, fncName, jsFncs, pmts=None, profile=False):
    """
    Description:
    ------------
    Javascript Framework extension.

    Hook in the base class to allow the definition of specific function to add extra primitive features.
    Usual this function should be used in a wrapper function with the same name in order to have a coherent
    bridge between Python and Javascript.

    Related Pages:

      https://www.w3schools.com/js/js_object_prototypes.asp

    Attributes:
    ----------
    :param pyClass: String. The PyJs Classname.
    :param fncName: String. The Javascript function name.
    :param jsFncs: List | String. Javascript functions.
    :param pmts: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.

    :return: The Js Object to allow the chaining.
    """
    jsData = JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile)
    self._src._props.setdefault('js', {}).setdefault('prototypes', {})["%s.prototype.%s" % (
      pyClass._jsClass, fncName)] = {"content": jsData, 'pmts': pmts}
    return self

  def request_http(self, method_type, url, varName="response", is_json=True, components=None):
    """
    Description:
    ------------
    All modern browsers have a built-in XMLHttpRequest object to request data from a server.

    Related Pages:

      https://www.w3schools.com/xml/xml_http.asp

    Usage::

      page.js.request_http("ajax", "POST", "https://api.cdnjs.com/libraries").setHeaders(header).onSuccess([
      page.js.alert(rptObj.js.objects.request.get("ajax").responseText)]).send(encodeURIData={"search": 'ractive'})

    Attributes:
    ----------
    :param method_type: String. The method of the HTTP Request.
    :param url: String. The url path of the HTTP request.
    :param varName: String. Optional. The variable name created in the Javascript.
    :param is_json: Boolean. Optional. Specify the type of object passed.
    :param components: List. Optional. A list of HTML objects values to be passed in the request.

    :rtype: JsObjects.XMLHttpRequest
    """
    method_type = JsUtils.jsConvertData(method_type, None)
    return JsObjects.XMLHttpRequest(self._src, varName, method_type, url)

  def get(self, url, jsData=None, varName="response", is_json=True, components=None, headers=None, asynchronous=False):
    """
    Description:
    ------------
    Create a GET HTTP request.

    Usage::

      inputs = page.ui.input("")
      btn = page.ui.button("Click").click([
        page.js.get("/test", {"fegeg": "efefe", "ok": inputs.dom.content}, components=[("input", inputs)])
      ])

    Attributes:
    ----------
    :param url: String. The url path of the HTTP request.
    :param jsData: String. Optional. A String corresponding to a JavaScript object.
    :param varName: String. Optional. The variable name created in the Javascript (default response).
    :param is_json: Boolean. Optional. Specify the type of object passed.
    :param components: HTML component. Optional. This will add the component value to the request object.
    :param headers: Dictionary. Optional. The request headers.
    :param asynchronous: Boolean. Async flag: true (asynchronous) or false (synchronous).

    :rtype: JsObjects.XMLHttpRequest
    """
    method_type = JsUtils.jsConvertData('GET', None)
    url = JsUtils.jsConvertData(url, None)
    url_params = []
    if components is not None:
      for component in components:
        if isinstance(component, tuple):
          url_params.append('"%s=" + %s' % (component[0], component[1].dom.content.toStr()))
        else:
          url_params.append('"%s=" + %s' % (component.htmlCode, component.dom.content.toStr()))
    if jsData is not None:
      for k, v in jsData.items():
        url_params.append('"%s=" + %s' % (k, JsUtils.jsConvertData(v, None)))
    if url_params:
      url = '%s + "?" + %s' % (url, ' +"&"+ '.join(url_params))
    request = JsObjects.XMLHttpRequest(self._src, varName, method_type, url, asynchronous=asynchronous)
    request.send({}, stringify=is_json)
    if is_json:
      request.setRequestHeader("Content-Type", "application/json;charset=UTF-8")
    if headers is not None:
      for k, v in headers.items():
        request.setRequestHeader(k, v)
    return request

  def post(self, url, jsData=None, varName="response", is_json=True, components=None, profile=None, headers=None,
           asynchronous=False):
    """
    Description:
    ------------
    Create a POST HTTP request.

    Attributes:
    ----------
    :param url: String. The url path of the HTTP request.
    :param jsData: String. Optional. Corresponding to a JavaScript object.
    :param varName: String. Optional. The variable name created in the Javascript (default response).
    :param is_json: Boolean. Optional. Specify the type of object passed.
    :param components: HTML component. Optional. This will add the component value to the request object.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param headers: Dictionary. Optional. The request headers.
    :param asynchronous: Boolean. Async flag: true (asynchronous) or false (synchronous).

    :rtype: JsObjects.XMLHttpRequest
    """
    method_type = JsUtils.jsConvertData('POST', None)
    url = JsUtils.jsConvertData(url, None)
    request = JsObjects.XMLHttpRequest(self._src, varName, method_type, url, asynchronous=asynchronous)
    request.profile = profile
    if components is not None:
      if jsData is None:
        jsData = components
      else:
        for c in components:
          if isinstance(c, tuple):
            jsData[c[1]] = c[0].dom.content
          else:
            request.data.add(c)
    request.send(jsData, stringify=is_json)
    if is_json:
      request.setRequestHeader("Content-Type", "application/json;charset=UTF-8")
    if headers is not None:
      for k, v in headers.items():
        request.setRequestHeader(k, v)
    return request

  def request_rpc(self, varName, method_type, fnc, url, extra_params=None):
    """
    Description:
    ------------
    Internal RPC to trigger services.

    Attributes:
    ----------
    :param varName: String. The variable name created in the Javascript.
    :param method_type: String. The method type
    :param fnc: Fnc. A python function.
    :param url: String. The service url
    :param extra_params: Dictionary. Optional.

    :rtype: JsObjects.XMLHttpRequest
    """
    if not extra_params:
      extra_params = {}
    extra_params = JsUtils.jsConvertData(extra_params, None)
    method_type = JsUtils.jsConvertData(method_type, None)
    url = JsUtils.jsConvertData(url, None)
    mod_name = fnc.__module__
    if mod_name == "__main__":
      import __main__

      mod_path, mod_name = os.path.split(__main__.__file__[:-3])
    else:
      mod_path = os.path.abspath(os.path.dirname(fnc.__module__))
    rpc_params = {"function": fnc.__name__, 'module': mod_name, 'path': mod_path, 'extra_params': extra_params}
    return JsObjects.XMLHttpRequest(self._src, varName, method_type, url, rpc_params)

  def fetch(self, url, options=None, profile=False, async_await=False):
    """
    Description:
    ------------
    The Fetch API provides a JavaScript interface for accessing and manipulating parts of the HTTP pipeline,
    such as requests and responses.

    Usage::

      page.ui.button("Click").click([
        page.js.fetch("test", {"method": "POST"}).then([
          page.js.console.log(pk.events.response)
        ])
      ])

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch

    Attributes:
    ----------
    :param url: String. The target url.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param async_await: Boolean. Optional.
    """
    fetch_name = "await fetch" if async_await else "fetch"
    if options is None:
      return JsObjects.JsPromise("%s(%s)" % (fetch_name, JsUtils.jsConvertData(url, None)), profile, async_await)

    return JsObjects.JsPromise(
      "%s(%s, %s)" % (fetch_name, JsUtils.jsConvertData(url, None), JsUtils.jsConvertData(options, None)),
      profile, async_await)

  @property
  def fncs(self):
    """
    Description:
    ------------
    Property to the predefined Javascript functions.

    :rtype: JsFncs.JsRegisteredFunctions

    :return: The predefined functions.
    """
    return JsFncs.JsRegisteredFunctions(self._src)

  @property
  def breadcrumb(self):
    """
    Description:
    ------------
    Create a internal Breadcrumb to keep track of the user journey within your page.

    Related Pages:

      https://www.w3schools.com/howto/howto_css_breadcrumbs.asp

    :rtype: JsBreadCrumb

    :return: A Python breadcrumb object.
    """
    if self._breadcrumb is None:
      self._breadcrumb = JsBreadCrumb(self._src)
    return self._breadcrumb

  def navigateTo(self, url, options=None):
    """
    Description:
    ------------
    Navigator to another URL like NodeJs.

    Usage::

      icon.click([self.context.page.js.navigateTo(url)])

    Related Pages:

      https://redfin.github.io/react-server/annotated-src/navigateTo.html

    Attributes:
    ----------
    :param url: String. The target url.
    :param options: Dictionary. Optional. The property of the location object.
    """
    options = options or {}
    if options.get("target", '') != "_blank":
      return self.location.href(href=url)

    return self.location.open_new_tab(url=url)

  def registerFunction(self, fncName, jsFncs, pmts=None, profile=False):
    """
    Description:
    ------------
    Javascript Framework extension.

    Register a predefined Javascript function.
    This is only dedicated to specific Javascript transformation functions.

    Description:
    ------------
    :param fncName: String. The function name.
    :param jsFncs: List | String. Optional. The Javascript function definition.
    :param pmts: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.

    :return: The JsObject
    """
    jsData = JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile)
    self._src._props.setdefault('js', {}).setdefault('functions', {})[fncName] = {
      'content': jsData, 'pmt': pmts}
    return self

  @property
  def keydown(self):
    """
    Description:
    -----------
    The onkeydown event occurs when the user is pressing a key (on the keyboard).

    Related Pages:

      https://www.w3schools.com/jsref/event_onkeydown.asp

    :rtype: KeyCodes.KeyCode
    """
    keydown = KeyCodes.KeyCode(page=self._src, source_event='document')
    self._src._props['js'].setdefault('events', {})['keydown'] = keydown
    return keydown

  @property
  def keypress(self):
    """
    Description:
    -----------
    The onkeypress event occurs when the user presses a key (on the keyboard).

    Related Pages:

      https://www.w3schools.com/jsref/event_onkeypress.asp

    :rtype: KeyCodes.KeyCode
    """
    keypress = KeyCodes.KeyCode(page=self._src, source_event='document')
    self._src._props['js'].setdefault('events', {})['keypress'] = keypress
    return keypress

  @property
  def keyup(self):
    """
    Description:
    -----------
    The onkeypress event occurs when the user presses a key (on the keyboard).

    Related Pages:

      https://www.w3schools.com/jsref/event_onkeypress.asp

    :rtype: KeyCodes.KeyCode
    """
    keyup = KeyCodes.KeyCode(page=self._src, source_event='document')
    self._src._props['js'].setdefault('events', {})['keyup'] = keyup
    return keyup

  def onReady(self, jsFncs, profile=False):
    """
    Description:
    ------------
    The ready event occurs when the body DOM (document object model) has been loaded.

    Related Pages:

      https://www.w3schools.com/jquery/event_ready.asp

    Attributes:
    ----------
    :param jsFncs: List | String. The Javascript functions to be added to this section.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    self._src._props['js']['onReady'].add(JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile))
    return self

  def profile(self, type, htmlCode, mark, recordsCount=""):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param type: String. The type of profile tag.
    :param htmlCode: String. The HTML component ID.
    :param mark: String. The mark reference.
    :param recordsCount: Integer. Optional. The records count.
    """
    type = JsUtils.jsConvertData(type, None)
    mark = JsUtils.jsConvertData(mark, None)
    return "profileObj.push({type: %s, htmlCode: '%s', mark: %s, records: %s})" % (
      type, htmlCode, mark, recordsCount)

  @staticmethod
  def getElementById(idName, jsConvFnc=None):
    """
    Description:
    ------------
    The getElementById() method returns the element that has the ID attribute with the specified value.

    Related Pages:

      https://www.w3schools.com/jsref/met_document_getelementbyid.asp

    Attributes:
    ----------
    :param idName: String. Required. The ID attribute's value of the element you want to get.
    :param jsConvFnc: String. Optional. A specific JavaScript data conversion function.

    :return: An Element Object, representing an element with the specified ID. Returns null if no elements with
    the specified ID exists
    """
    return JsNodeDom.JsDoms(
      "document.getElementById(%s)" % JsUtils.jsConvertData(idName, jsConvFnc).toStr().replace("'", '"'))

  @staticmethod
  def getElementsByName(name, jsConvFnc=None):
    """
    Description:
    ------------
    The getElementsByName() method returns a collection of all elements in the document with the specified name
    (the value of the name attribute), as a NodeList object.

    The NodeList object represents a collection of nodes. The nodes can be accessed by index numbers.
    The index starts at 0.

    Related Pages:

      https://www.w3schools.com/jsref/met_doc_getelementsbyname.asp

    Attributes:
    ----------
    :param name: String. Required. The name attribute value of the element you want to access/manipulate.
    :param jsConvFnc: String. Optional. A specific JavaScript data conversion function.

    :return: A NodeList object, representing a collection of elements with the specified name.
             The elements in the returned collection are sorted as they appear in the source code.

    :rtype: JsNodeDom.JsDomsList
    """
    return JsNodeDom.JsDomsList.get(varName="document.getElementsByName(%s)" % JsUtils.jsConvertData(name, jsConvFnc))

  @staticmethod
  def getElementsByTagName(tagName, i=0, jsConvFnc=None):
    """
    Description:
    ------------
    The getElementsByTagName() method returns a collection of an elements's child elements with the specified tag name,
    as a NodeList object.

    The NodeList object represents a collection of nodes. The nodes can be accessed by index numbers.
    The index starts at 0.

    Related Pages:

      https://www.w3schools.com/jsref/met_element_getelementsbytagname.asp

    Attributes:
    ----------
    :param tagName: String. Required. The tag name of the child elements you want to get.
    :param i: Integer. Optional. The index of the element.
    :param jsConvFnc: String. Optional. A specific JavaScript data conversion function.
    """
    return JsNodeDom.JsDoms("document.getElementsByTagName(%s)[%s]" % (
      JsUtils.jsConvertData(tagName, jsConvFnc), i), varName="%s_%s" % (tagName, i), setVar=True)

  @staticmethod
  def getElementsByClassName(clsName):
    """
    Description:
    ------------
    The getElementsByClassName() method returns a collection of all elements in the document with the specified
    class name, as a NodeList object.

    Related Pages:

      https://www.w3schools.com/jsref/met_document_getelementsbyclassname.asp

    Attributes:
    ----------
    :param clsName: Required. The class name of the elements you want to get.

    :return: A NodeList object, representing a collection of elements with the specified class name.
             The elements in the returned collection are sorted as they appear in the source code.
    """
    return JsNodeDom.JsDoms("document.getElementsByClassName(%s)" % clsName)

  def createElement(self, tagName, varName=None, setVar=True, dom_id=None):
    """
    Description:
    ------------
    The createElement() method creates an Element Node with the specified name.

    Related Pages:

      https://www.w3schools.com/jsref/met_document_createelement.asp

    Attributes:
    ----------
    :param tagName: String. Required. The name of the element you want to create.
    :param varName: String. Optional. The variable name to be set. Default random name.
    :param setVar: Boolean. Optional. Create a variable for the new object. Default True.
    :param dom_id: String. Optional. The Dom ID reference for the object.
    """
    dom_obj = JsNodeDom.JsDoms.new(tagName, varName=varName, setVar=setVar, report=self._src)
    if dom_id is not None:
      dom_obj.attr("id", dom_id)
    return dom_obj

  @staticmethod
  def createTextNode(jsString=None, jsConvFnc=None):
    """
    Description:
    ------------
    The createTextNode() method creates a Text Node with the specified text.

    Related Pages:

      https://www.w3schools.com/jsref/met_document_createtextnode.asp

    Attributes:
    ----------
    :param jsString: String. Optional. The text of the Text node.
    :param jsConvFnc: String. Optional. A specific JavaScript data conversion function.

    :return: A Text Node object with the created Text Node.
    """
    return JsObject.JsObject("document.createTextNode(%s)" % JsUtils.jsConvertData(jsString, jsConvFnc), isPyData=False)

  def encodeURIComponent(self, uri, jsConvFnc=None):
    """
    Description:
    ------------
    The encodeURIComponent() function encodes a URI component.

    Related Pages:

      https://www.w3schools.com/jsref/jsref_encodeuricomponent.asp

    Attributes:
    ----------
    :param uri: String. Required. The URI to be encoded.
    :param jsConvFnc: String. Optional. A specific JavaScript data conversion function.

    :return: A String, representing the encoded URI.
    """
    return JsObject.JsObject("encodeURIComponent(%s)" % JsUtils.jsConvertData(uri, jsConvFnc))

  def decodeURIComponent(self, url_enc, jsConvFnc=None):
    """
    Description:
    ------------
    The decodeURIComponent() function decodes a URI component.

    Related Pages:

      https://www.w3schools.com/jsref/jsref_decodeuricomponent.asp

    Attributes:
    ----------
    :param url_enc: String. Required. The URI to be decoded.
    :param jsConvFnc: String. Optional. A specific JavaScript data conversion function.

    :return: A String, representing the decoded URI.
    """
    return JsObject.JsObject("decodeURIComponent(%s)" % JsUtils.jsConvertData(url_enc, jsConvFnc))

  @property
  def body(self):
    """
    Description:
    ------------
    Get the DOM object object.

    This will return the object and it will not create any variable.
    """
    return JsNodeDom.JsDoms("document.body", setVar=False, isPyData=False)

  @property
  def data(self):
    """
    Description:
    ------------

    :rtype: JsData.JsData
    """
    if self.__data is None:
      self.__data = JsData.JsData(self._src)
    return self.__data

  def string(self, data, varName=None, setVar=False, isPyData=True):
    """
    Description:
    ------------
    Shortcut to the Javascript String primitives.

    Attributes:
    ----------
    :param data: String | Object. The String data.
    :param varName: String. Optional. The specific name to be used for this JavaScript String.
    :param setVar: Boolean. Optional. Set a variable. Default False.
    :param isPyData: Boolean. Optional. Specify the type of data.
    """
    return JsString.JsString(data, varName, setVar, isPyData, report=self._src)

  def number(self, data, varName=None, setVar=False, isPyData=True):
    """
    Description:
    ------------
    Shortcut to the Javascript Number primitives.

    Attributes:
    ----------
    :param data: String | Object. The String data.
    :param varName: String. Optional. The specific name to be used for this JavaScript String.
    :param setVar: Boolean. Optional. Set a variable. Default False.
    :param isPyData: Boolean. Optional. Specify the type of data.
    """
    return JsNumber.JsNumber(data, varName, setVar, isPyData, report=self._src)

  def object(self, data, varName=None, setVar=False, isPyData=True):
    """
    Description:
    ------------
    Shortcut to the Javascript Object primitives.

    Attributes:
    ----------
    :param data: String | Object. The String data.
    :param varName: String. Optional. The specific name to be used for this JavaScript String.
    :param setVar: Boolean. Optional. Set a variable. Default False.
    :param isPyData: Boolean. Optional. Specify the type of data.
    """
    return JsObject.JsObject(data, varName, setVar, isPyData, report=self._src)

  def querySelectorAll(self, selector, jsConvFnc=None):
    """
    Description:
    ------------
    The querySelectorAll() method returns all elements in the document that matches a specified CSS selector(s),
    as a static NodeList object.

    Related Pages:

      https://www.w3schools.com/jsref/met_document_queryselectorall.asp

    Attributes:
    ----------
    :param selector: String. CSS selectors.
    :param jsConvFnc: String. Optional. A specific JavaScript data conversion function.
    """
    return JsNodeDom.JsDomsList(
      "document.querySelectorAll(%s)" % JsUtils.jsConvertData(selector, jsConvFnc), isPyData=False)

  def querySelector(self, selector, jsConvFnc=None):
    """
    Description:
    ------------
    The querySelector() method returns the first element that matches a specified CSS selector(s) in the document.

    Related Pages:

      https://www.w3schools.com/jsref/met_document_queryselector.asp

    Attributes:
    ----------
    :param selector: String. CSS selectors.
    :param jsConvFnc: String. Optional. A specific JavaScript data conversion function.
    """
    return JsNodeDom.JsDoms.get("document.querySelector(%s)" % JsUtils.jsConvertData(selector, jsConvFnc))

  def activeElement(self):
    """
    Description:
    ------------
    The activeElement property returns the currently focused element in the document.

    Related Pages:

      https://www.w3schools.com/jsref/prop_document_activeelement.asp

    :return: A reference to the element object in the document that has focus.
    """
    return JsNodeDom.JsDoms("document.activeElement")

  @staticmethod
  def title(text=None, jsConvFnc=None):
    """
    Description:
    ------------
    The title property sets or returns the title of the current document (the text inside the HTML title element).

    Related Pages:

      https://www.w3schools.com/jsref/prop_doc_title.asp

    Attributes:
    ----------
    :param text: String. Optional. Representing the title of the document.
    :param jsConvFnc: String. Optional. A specific JavaScript data conversion function.
    """
    if text is None:
      return JsString.JsString("document.title")

    return JsObjects.JsVoid("document.title = %s" % JsUtils.jsConvertData(text, jsConvFnc))

  def execCommand(self, command, showUI, value):
    """
    Description:
    ------------
    The execCommand() method executes the specified command for the selected part of an editable section.

    Related Pages:

      https://www.w3schools.com/jsref/met_document_execcommand.asp

    Attributes:
    ----------
    :param command:	 String. Specifies the name of the command to execute on the selected section.
    :param showUI: Boolean. specifies if the UI should be shown or not.
    :param value: String. Some commands need a value to be completed.

    :return: A Boolean, false if the command is not supported, otherwise true.
    """
    return JsObjects.JsVoid("document.execCommand('%s')" % command)

  def createEvent(self, type):
    """
    Description:
    ------------
    The createEvent() method creates an event object.

    The event can be of any legal event type, and must be initialized before use.

    Related Pages:

      https://www.w3schools.com/jsref/event_createevent.asp

    Attributes:
    ----------
    :param type: Required. A String that specifies the type of the event.

    :return: An Event object
    """
    if type not in ['AnimationEvent', 'ClipboardEvent', 'DragEvent', 'FocusEvent', 'HashChangeEvent', 'InputEvent',
                    'MouseEvent', 'PageTransitionEvent', 'PopStateEvent', 'ProgressEvent', 'StorageEvent', 'TouchEvent',
                    'TransitionEvent', 'UiEvent', 'WheelEvent', 'KeyboardEvent']:
      raise Exception("Not recognized type %s" % type)

  def createAttribute(self, attributename):
    """
    Description:
    ------------
    The createAttribute() method creates an attribute with the specified name, and returns the attribute as an
    Attr object.

    Related Pages:

      https://www.w3schools.com/jsref/met_document_createattribute.asp

    Attributes:
    ----------
    :param attributename: String. Required. The name of the attribute you want to create.

    :return: A Node object, representing the created attribute.
    """
    return JsNodeAttributes.JsAttributes(attributename)

  def writeln(self, jsString):
    """
    Description:
    ------------
    The writeln() method is identical to the document.write() method, with the addition of writing a newline character
    after each statement.

    Related Pages:

      https://www.w3schools.com/jsref/met_doc_writeln.asp

    :param jsString: Optional. What to write to the output stream.
                     Multiple arguments can be listed and they will be appended to the document in order of occurrence

    :return: No return value
    """
    return JsObjects.JsVoid("document.writeln(%s)" % jsString)

  @staticmethod
  def parseFloat(jsString):
    """
    Description:
    ------------
    The parseFloat() function parses a string and returns a floating point number.

    Related Pages:

      https://www.w3schools.com/jsref/jsref_parseint.asp

    Attributes:
    ----------
    :param jsString: String. Required. The string to be parsed.

    :return: A Number. If the first character cannot be converted to a number, NaN is returned.
    """
    return JsNumber.JsNumber("parseFloat(%s)" % jsString, isPyData=False)

  @staticmethod
  def parseInt(jsString):
    """
    Description:
    ------------
    The parseInt() function parses a string and returns an integer.

    Related Pages:

      https://www.w3schools.com/jsref/jsref_parseint.asp

    Attributes:
    ----------
    :param jsString: Required. The string to be parsed.

    :return: A Number. If the first character cannot be converted to a number, NaN is returned.
    """
    return JsNumber.JsNumber("parseInt(%s)" % jsString, isPyData=False)

  @staticmethod
  def parseDate(jsString):
    """
    Description:
    ------------
    The parse() method parses a date string and returns the number of milliseconds between the date string and midnight
    of January 1, 1970.

    Related Pages:

      https://www.w3schools.com/jsref/jsref_parse.asp

    Attributes:
    ----------
    :param jsString: Required. A string representing a date.

    :return: Number. Representing the milliseconds between the specified date-time and midnight January 1, 1970.
    """
    return JsNumber.JsNumber("Date.parse(%s)" % jsString, isPyData=False)

  def getVar(self, varName, varType="var"):
    """
    Description:
    ------------
    Get the Javascript Variable name.

    Attributes:
    ----------
    :param varName: String. The Variable name.
    :param varType: String. Optional. The scope of the variable.

    :return: Return the piece of script to be added to the Javascript.
    """
    if varType == 'var':
      return "window['%s']" % varName

    return varName

  def info(self, jsData, cssStyle=None, icon="fas fa-spinner fa-spin", seconds=10000):
    """
    Description:
    ------------
    Display a message.

    Related Pages:

      https://fontawesome.com/how-to-use/on-the-web/styling/animating-icons

    Attributes:
    ----------
    :param jsData: String. A String corresponding to a JavaScript object
    :param cssStyle: Dictionary. Optional. The CSS attributes to be added to the HTML component.
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome.
    :param seconds: Integer. Optional. The number of second the info will be visible.
    """
    if cssStyle is None:
      cssStyle = {"position": "fixed", "bottom": "5px", "right": "10px", "padding": '2px 7px',
                  "border": "1px solid black"}
    if icon is not None:
      self._src.jsImports.add('font-awesome')
      self._src.cssImport.add('font-awesome')
      return [
        self.createElement("i", varName="popup_icon").setAttribute("aria-hidden", True).css(
          {"display": "inline-block", "width": "auto", "height": "auto", "margin-right": '5px'}).className(icon),
        self.createElement("div", varName="popup_info").appendChild(
          self.objects.dom("popup_icon")).css(cssStyle).text(jsData),
        self.body.appendChild(self.objects.dom("popup_info")),
        self.window.setTimeout(self.objects.dom("popup_info").remove(), milliseconds=seconds)]

    return [
      self.createElement("div", varName="popup_info").css(cssStyle).text(jsData),
      self.body.appendChild(self.objects.dom("popup_info")),
      self.window.setTimeout(self.objects.dom("popup_info").remove(), milliseconds=seconds)]

  def print(self, content, timer=1000, cssAttrs=None):
    """
    Description:
    ------------
    Print a temporary message.

    Attributes:
    ----------
    :param content: String. The content of the popup.
    :param timer: Number. Optional. The time the popup will be displayed.
    :param cssAttrs: Dictionary. Optional. The CSS attributes for the popup.
    """
    dflt_attrs = {"position": "absolute", "background": "white", "padding": "5px 10px", 'border-radius': "5px",
                  "top": JsObject.JsObject.get('event.clientY + "px"'),
                  'left': JsObject.JsObject.get('event.clientX + "px"')}
    if cssAttrs is not None:
      dflt_attrs.update(cssAttrs)
      if 'bottom' in cssAttrs:
        del dflt_attrs["top"]
      if 'right' in cssAttrs:
        del dflt_attrs["left"]
    return '''
      (function(event, content){
        var popup = document.createElement("div"); %s
        popup.innerHTML = content; document.body.appendChild(popup);
        setTimeout(function(){ document.body.removeChild(popup); }, %s);
      })(event, %s)''' % (JsNodeDom.JsDoms.get("popup").css(dflt_attrs).r, timer, JsUtils.jsConvertData(content, None))

  def mail(self, mails, subject=None, body=None, cc=None, bcc=None):
    """
    Description:
    ------------
    Create an email.

    Related Pages:

      https://www.w3docs.com/snippets/html/how-to-create-mailto-links.html

    Attributes:
    ----------
    :param mails:
    :param subject:
    :param body:
    :param bcc:
    """
    mail_data = []
    for label, value in [("cc", cc), ('bcc', bcc), ("subject", subject), ("body", body)]:
      if value is None:
        continue

      if not isinstance(value, list):
        value = [value]
      content, html_content = [], False
      for v in value:
        if hasattr(v, 'options'):
          content.append(v.html())
          html_content = True
        else:
          content.append(str(v))
      if label == 'body':
        if html_content:
          # TODO: Check how to send HTML page
          mail_data.append("%s=%s" % (label, ",".join(content)))
        else:
          mail_data.append("%s=%s" % (label, ",".join(content)))
      else:
        mail_data.append("%s=%s" % (label, ",".join(content)))

    if hasattr(mails, 'toStr'):
      return JsObjects.JsVoid("(function(url){return 'mailto:'+ url +'?%s'})(%s)" % ("&".join(mail_data), mails))

    if not isinstance(mails, list):
      mails = [mails]

    return JsUtils.jsConvertData("mailto:%s?%s" % (";".join(mails), "&".join(mail_data)), None)

  @property
  def msg(self):
    """
    Description:
    ------------
    Shortcut to predefined temporary messages displayed to the UI.
    """
    return JsMsgAlerts.Msg(self._src)

  def hot_imports(self, script, jsFuncs, profile=None):
    """
    Description:
    ------------
    Add a Javascript module and then run function once it is loaded.

    Related Pages:

      https://cleverbeagle.com/blog/articles/tutorial-how-to-load-third-party-scripts-dynamically-in-javascript

    Attributes:
    ----------
    :param script: String. A script name. A Js extension.
    :param jsFuncs: String | List. The Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    js_script = JsUtils.jsConvertData(script, None)
    js_funcs = JsUtils.jsConvertFncs(jsFuncs, toStr=True, profile=profile)
    return JsObjects.JsVoid('''
let scriptElementId = "pkg_"+ %(script)s;    
let existingScript = document.getElementById(scriptElementId);
if (!existingScript && (scriptElementId !== 'pkg_undefined')) {
  const script = document.createElement('script'); script.src = %(script)s; script.id = scriptElementId;
  document.body.appendChild(script); script.onload = function(){%(fncs)s; };}
else { %(fncs)s}  ''' % {"script": js_script, "fncs": js_funcs})
