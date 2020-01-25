"""
Wrapper to the Javascript Window module

Allows to save key/value pairs in a web browser. Stores the data with no expiration date
The localStorage and sessionStorage properties allow to save key/value pairs in a web browser.

https://www.w3schools.com/Jsref/prop_win_localstorage.asp
"""

from epyk.core.js import JsUtils
from epyk.core.js.objects import JsNodeDom

# All the predefined variable types
from epyk.core.js.fncs import JsFncs
from epyk.core.js.primitives import JsNumber
from epyk.core.js.primitives import JsObject


class JsLocalStorage(object):
  def key(self, i):
    """
    The key() method returns name of the key with the specified index.

    The localStorage object stores data with no expiration date.
    The data will not be deleted when the browser is closed, and will be available the next day, week, or year.

    Example
    jsObj.localStorage.key(0)

    Documentation
    https://www.w3schools.com/jsref/met_storage_key.asp

    :param i: Required. A Number representing the index of the key you want to get the name of

    :return: A String, representing the name of the specified key
    """
    i = JsUtils.jsConvertData(i, None)
    return JsObject.JsObject("localStorage.key(%s)" % i)

  def __setitem__(self, key, data):
    """

    :param key:
    :param data:

    :return:
    """
    self.setItem(key, data)

  def __getitem__(self, item):
    """
    Python wrapper to getItem

    Example
    jsObj.console.log(jsObj.sessionStorage["lastname"])

    :param item:

    :return:
    """
    return self.getItem(item)

  def setItem(self, key, data):
    """
    Syntax for SAVING data to localStorage

    The localStorage object stores data with no expiration date.
    The data will not be deleted when the browser is closed, and will be available the next day, week, or year.

    Example
    jsObj.localStorage.getItem("lastname", "test")

    Documentation
    https://www.w3schools.com/jsref/met_storage_setitem.asp

    :param key: Required. A String specifying the name of the key you want to set the value of
    :param data: Required. A String specifying the value of the key you want to set the value of

    :return: A String, representing the inserted value
    """
    key = JsUtils.jsConvertData(key, None)
    data = JsUtils.jsConvertData(data, None)
    return JsObject.JsObject("localStorage.setItem(%s, %s)" % (key, data))

  def getItem(self, key):
    """
    Syntax for READING data from localStorage:

    The localStorage object stores data with no expiration date.
    The data will not be deleted when the browser is closed, and will be available the next day, week, or year.

    Example
    jsObj.localStorage.getItem("lastname")

    Documentation
    https://www.w3schools.com/jsref/met_storage_getitem.asp

    :param key: Required. A String specifying the name of the key you want to get the value of

    :return: A String, representing the value of the specified key
    """
    key = JsUtils.jsConvertData(key, None)
    return JsObject.JsObject("localStorage.getItem(%s)" % key)

  def removeItem(self, key):
    """
    The removeItem() method removes the specified Storage Object item.

    The localStorage object stores data with no expiration date.
    The data will not be deleted when the browser is closed, and will be available the next day, week, or year.

    Example
    jsObj.localStorage.removeItem("lastname")

    Documentation
    https://www.w3schools.com/jsref/met_storage_removeitem.asp

    :param key: Required. A String specifying the name of the item you want to remove

    :return: Void
    """
    key = JsUtils.jsConvertData(key, None)
    return JsFncs.JsFunction("localStorage.removeItem(%s)" % key)

  def clear(self):
    """
    The clear() method removes all the Storage Object item for this domain.

    The localStorage object stores data with no expiration date.
    The data will not be deleted when the browser is closed, and will be available the next day, week, or year.

    Example
    jsObj.localStorage.clear()

    Documentation
    https://www.w3schools.com/jsref/met_storage_clear.asp

    :return: Void
    """
    return JsFncs.JsFunction("localStorage.clear()")


class JsSessionStorage(object):
  """
  The localStorage and sessionStorage properties allow to save key/value pairs in a web browser.

  The sessionStorage object stores data for only one session (the data is deleted when the browser tab is closed).

  Documentation:
  https://www.w3schools.com/Jsref/prop_win_sessionstorage.asp
  """

  def key(self, i):
    """
    The sessionStorage object stores data for only one session (the data is deleted when the browser tab is closed).

    Documentation

    :param i: The key number
    :return:
    """
    i = JsUtils.jsConvertData(i, None)
    return JsObject.JsObject("sessionStorage.key(%s)" % i)

  def __setitem__(self, key, data):
    """

    :param key:
    :param data:

    :return:
    """
    self.setItem(key, data)

  def __getitem__(self, item):
    """
    Python wrapper to getItem

    Example
    jsObj.console.log(jsObj.sessionStorage["lastname"])

    :param item:

    :return:
    """
    return self.getItem(item)

  def setItem(self, key, data):
    """
    Syntax for SAVING data to sessionStorage

    The sessionStorage object stores data for only one session (the data is deleted when the browser tab is closed).

    Example:
    sessionStorage.setItem("lastname", "Smith")
    jsObj.sessionStorage.setItem("lastname", jsObj.objects.get("bin")),

    Documentation:
    https://www.w3schools.com/Jsref/prop_win_sessionstorage.asp

    :param key: The key used to store the data in the session cache
    :param data:

    :return:
    """
    key = JsUtils.jsConvertData(key, None)
    data = JsUtils.jsConvertData(data, None)
    return JsObject.JsObject("sessionStorage.setItem(%s, %s)" % (key, data))

  def getItem(self, key):
    """
    Syntax for READING data from sessionStorage

    The sessionStorage object stores data for only one session (the data is deleted when the browser tab is closed).

    Examples:
    sessionStorage.getItem("lastname")
    jsObj.console.log(jsObj.sessionStorage.getItem("lastname"))

    :param key:

    :return:
    """
    key = JsUtils.jsConvertData(key, None)
    return JsObject.JsObject("sessionStorage.getItem(%s)" % key)

  def removeItem(self, jsData, jsDataKey=None, isPyData=False, jsFnc=None):
    """
    Syntax for REMOVING ALL saved data from sessionStorage

    The sessionStorage object stores data for only one session (the data is deleted when the browser tab is closed).

    Examples
    jsObj.sessionStorage.removeItem("lastname")

    Documentation
    https://www.w3schools.com/jsref/met_storage_removeitem.asp

    :param jsData:
    :param jsDataKey:
    :param isPyData:
    :param jsFnc:

    :return:
    """
    jsData = JsUtils.jsConvert(jsData, jsDataKey, isPyData, jsFnc)
    return JsFncs.JsFunction("sessionStorage.removeItem(%s)" % jsData)

  def clear(self):
    """
    Syntax for REMOVING ALL saved data from sessionStorage

    The sessionStorage object stores data for only one session (the data is deleted when the browser tab is closed).

    Documentation:
    https://www.w3schools.com/jsref/prop_win_sessionstorage.asp

    :return:
    """
    return JsFncs.JsFunction("sessionStorage.clear()")


class JsHistory(object):
  """
  Interface to the Javascript history module

  Documentation
  https://www.w3schools.com/js/js_window_history.asp
  """

  def __init__(self, context):
    self.__jsObj = context

  @property
  def length(self):
    """
    The length property returns the number of URLs in the history list of the current browser window.

    Example
    rptObj.js.window.history.length

    Documentation
    https://www.w3schools.com/jsref/prop_his_length.asp

    :return: A Number, representing the number of entries in the session history
    """
    return JsNumber.JsNumber("history.length", isPyData=False)

  def back(self):
    """
    The back() method loads the previous URL in the history list.

    Example
    rptObj.js.window.history.back()

    Documentation
    https://www.w3schools.com/jsref/met_his_back.asp

    :return: The Javascript String to be added to the page
    """
    return JsFncs.JsFunction("window.history.back()")

  def forward(self):
    """
    The forward() method loads the next URL in the history list.

    Documentation
    https://www.w3schools.com/jsref/met_his_forward.asp

    :return: The Javascript String to be added to the page
    """
    return JsFncs.JsFunction("window.history.forward()")

  def go(self, number):
    """
    The go() method loads a specific URL from the history list.

    Documentation
    https://www.w3schools.com/jsref/met_his_go.asp

    :param number: Required. The parameter can either be a number which goes to the URL within the specific position (-1 goes back one page, 1 goes forward one page), or a string.

    :return: The Javascript String to be added to the page
    """
    return JsFncs.JsFunction("window.history.go(%s)" % number)

  def pushState(self, stateObj, title, url):
    """
    Pushes the given data onto the session history stack with the specified title and, if provided, URL

    Note that pushState() never causes a hashchange event to be fired, even if the new URL differs from the old URL only in its hash

    Documentation
    https://developer.mozilla.org/en-US/docs/Web/API/History_API

    :param stateObj: he state object is a JavaScript object which is associated with the new history entry created by pushState()
    :param title: Firefox currently ignores this parameter, although it may use it in the future
                  Passing the empty string here should be safe against future changes to the method.
                  Alternatively, you could pass a short title for the state to which you're moving.
    :param url: The new history entry's URL is given by this parameter.
                Note that the browser won't attempt to load this URL after a call to pushState(),

    :return:
    """
    return JsFncs.JsFunction("window.history.pushState('%s', '%s', %s)" % (stateObj, title, url))

  def replaceState(self, stateObj, title, url):
    """
    history.replaceState() operates exactly like history.pushState() except that replaceState() modifies the current history entry instead of creating a new one.

    Example

    Documentation
    https://developer.mozilla.org/en-US/docs/Web/API/History_API

    :param stateObj: he state object is a JavaScript object which is associated with the new history entry created by pushState()
    :param title: Firefox currently ignores this parameter, although it may use it in the future
                  Passing the empty string here should be safe against future changes to the method.
                  Alternatively, you could pass a short title for the state to which you're moving.
    :param url: The new history entry's URL is given by this parameter.
                Note that the browser won't attempt to load this URL after a call to pushState(),

    :return:
    """
    return JsFncs.JsFunction("window.history.replaceState('%s', '%s', %s)" % (stateObj, title, url))

  def updateState(self, key, val):
    """
    Wrapper function

    This function is a simple wrapping function on top of the pushState history method.
    The purpose of this method is to make easier the update of the url whenever a component in the framework is updated.

    Example
    htmlObj.js.js.window.history.updateState(self.htmlId, self.val)

    Documentation
    https://developer.mozilla.org/en-US/docs/Web/API/History_API

    :param key: The key to be added or updated in the current URL
    :param val: The value to be changed to the current URL

    :return: The Javascript String for the method
    """
    self.__jsObj.registerFunction("updateUrl", [
      self.__jsObj.objects.new([], varName="newPmts"),
      self.__jsObj.location.search.substr(1).split("&").forEach([
        self.__jsObj.if_(self.__jsObj.data.loop.val.toString(explicit=False).includes("=", jsObj=self.__jsObj), [
          self.__jsObj.objects.array.new(self.__jsObj.data.loop.val.toString().split("="), varName="urlPmts"),
          self.__jsObj.objects.array.get("urlPmts")[0].toString(),
          self.__jsObj.objects.get("newPmts").addItem(self.__jsObj.objects.array.get("urlPmts")[0], self.__jsObj.objects.array.get("urlPmts")[1])
        ])
      ]),

      self.__jsObj.objects.get("newPmts").addItem(self.__jsObj.objects.get("urlKey"), self.__jsObj.objects.get("urlValue")),
      # Then we concatenate the URL
      self.__jsObj.objects.array.new([], varName="pmts"),
      self.__jsObj.objects.get("newPmts").entries().forEach([
        self.__jsObj.objects.array.get("pmts").push(self.__jsObj.data.loop.val[0].toString(explicit=False).add("=").add(self.__jsObj.data.loop.val[1]))
      ]),
      self.__jsObj.return_(self.__jsObj.location.origin + self.__jsObj.location.pathname + "?" + self.__jsObj.objects.array.get("pmts").join("&"))
      ], ["urlKey", "urlValue"])
    return self.pushState("data", "", JsFncs.JsFunction("updateUrl(%s, %s)" % (JsUtils.jsConvertData(key, None), JsUtils.jsConvertData(val, None))))


class JsWindowEvent(object):
  def addEventListener(self, eventType, jsFncs, windowId="window"):
    """

    :param eventType:
    :param jsFncs:
    :param windowId:
    :return:
    """
    eventType = JsUtils.jsConvertData(eventType, None)
    jsFncs = JsUtils.jsConvertFncs(jsFncs, toStr=True)
    return JsFncs.JsFunction("%s.addEventListener(%s, function(){%s})" % (windowId, eventType, jsFncs))

  def addScrollListener(self, jsFncs, windowId="window"):
    """

    :param jsFncs:
    :param windowId:
    :return:
    """
    return self.addEventListener("scroll", jsFncs, windowId)

  def addContentLoaded(self, jsFncs, windowId="window"):
    """
    The DOMContentLoaded event fires when the initial HTML document has been completely loaded and parsed, without waiting for stylesheets, images, and subframes to finish loading.

    Example
    rptObj.js.addOnLoad(
      rptObj.js.window.events.addContentLoaded(rptObj.js.alert("DOM fully loaded and parsed"))
    )

    Documentation
    https://developer.mozilla.org/en-US/docs/Web/API/Window/DOMContentLoaded_event

    :param jsFncs:
    :param windowId:
    :return:
    """
    return self.addEventListener("DOMContentLoaded", jsFncs, windowId)

  def addClickListener(self, jsFncs, windowId="window"):
    """

    :param jsFncs:
    :param windowId:
    :return:
    """
    return self.addEventListener("click", jsFncs, windowId)


class JsWindow(object):
  """
  The window object represents an open window in a browser.

  If a document contain frames (<iframe> tags), the browser creates one window object for the HTML document,
  and one additional window object for each frame.

  Documentation:
  https://www.w3schools.com/Jsref/obj_window.asp
  """
  @property
  def scrollY(self, windowId="window"):
    return JsNumber.JsNumber("%s.scrollY" % windowId)

  def __init__(self, src=None):
    """

    :type src: epyk.Lib.js.Js.JsBase
    :param src:
    """
    self.__src = src
    self._context = src._context if hasattr(src, '_context') else {}

  @property
  def document(self):
    """
    Interface to the DOM object on the current window

    :return: A Python JsDoms object wrapping the DOM Js interface
    """
    return JsNodeDom.JsDoms(self.__src)

  @property
  def history(self):
    """
    Interface to the History object

    Documentation

    :return: A Python Js History object
    """
    return JsHistory(self.__src)

  def close(self, windowId="window"):
    """
    Closes the current window

    Documentation
    https://www.w3schools.com/jsref/met_win_close.asp

    :param windowId: The JavaScript window object

    :return: The String representing the Javascript function
    """
    return JsFncs.JsFunction("%s.close()" % windowId)

  @property
  def events(self):
    """ Property to all the events """
    return JsWindowEvent()

  def addEventListener(self, eventType, jsFncs, windowId="window"):
    """

    :param eventType:
    :param jsFncs:
    :param windowId:
    :return:
    """
    eventType = JsUtils.jsConvertData(eventType, None)
    jsFncs = JsUtils.jsConvertFncs(jsFncs, toStr=True)
    return JsFncs.JsFunction("%s.addEventListener(%s, function(){%s})" % (windowId, eventType, jsFncs))

  def open(self, url, name="_self", specs=None, replace=None, windowId="window"):
    """
    Opens a new browser window

    Documentation
    https://www.w3schools.com/Jsref/met_win_open.asp

    :param url: Optional. Specifies the URL of the page to open. If no URL is specified, a new window/tab with about:blank is opened
    :param name: Optional. Specifies the target attribute or the name of the window.
    :param specs: Optional. A comma-separated list of items, no whitespaces.
    :param replace: Optional. Specifies whether the URL creates a new entry or replaces the current entry in the history list
    :param windowId: The JavaScript window object

    :return:
    """
    url = JsUtils.jsConvertData(url, None)
    name = JsUtils.jsConvertData(name, None)
    specs = JsUtils.jsConvertData(specs, None)
    replace = JsUtils.jsConvertData(replace, None)
    return JsFncs.JsFunction("%s.open(%s, %s, %s, %s)" % (windowId, url, name, specs, replace))

  def postData(self, jsData):
    """

    :param jsData:

    :return:
    """

    if not isinstance(jsData, list):
      jsData = [jsData]

  def download(self, data, fileName):
    """
    Download the data from a flat file

    Example
    rptObj.js.window.download(rptObj.js.window.btoa(rptObj.js.objects.get("test")), fileName="test.txt")

    Documentation

    :param data:
    :param fileName:

    :return: Void,
    """
    data = JsUtils.jsConvertData(data, None)
    return JsFncs.JsFunction(";".join(JsUtils.jsConvertFncs([
      self.__src.createElement("a", varName="a_temp").setAttribute("download", fileName).setAttribute("href", JsFncs.JsFunction("'data:text/csv;base64,'+ %s" % data)),
      self.__src.body.appendChild(self.__src.objects.get("a_temp")),
      self.__src.objects.dom.get("a_temp").click(),
      #self.__src.objects.dom.get("a_temp").remove()
    ])))
    #return JsFncs.JsFunction("%s.open('data:text/csv;base64,'+ %s, '_self')" % (windowId, data))

  def moveBy(self, x, y, windowId="window"):
    """
    The moveBy() method moves a window a specified number of pixels relative to its current coordinates.

    Documentation
    https://www.w3schools.com/Jsref/met_win_moveby.asp

    :param x: The horizontal move in pixel
    :param y: The vertical move in pixel
    :param windowId: The JavaScript window object

    :return:
    """
    x = JsUtils.jsConvertData(x, None)
    y = JsUtils.jsConvertData(y, None)
    return JsFncs.JsFunction("%s.moveBy(%s, %s)" % (windowId, x, y))

  def focus(self, windowId="window"):
    """
    The focus() method sets focus to the current window

    Documentation
    https://www.w3schools.com/Jsref/met_win_focus.asp

    :param windowId: The JavaScript window object

    :return: Void, The Javascript String
    """
    return JsFncs.JsFunction("%s.focus()" % windowId)

  def scroll(self, x, y, windowId="window"):
    """
    The Window.scroll() method scrolls the window to a particular place in the document.

    Documentation
    https://developer.mozilla.org/uk/docs/Web/API/Window/scroll

    :param x: The pixel along the horizontal axis of the document that you want displayed in the upper left
    :param y: The pixel along the vertical axis of the document that you want displayed in the upper left

    :return:
    """
    return JsFncs.JsFunction("%s.scroll(%s, %s)" % (windowId, x, y))

  def scrollTo(self, x=None, y=None, windowId="window"):
    """
    The window.scrollTo() go to a particular point

    :param x:
    :param y:
    :param windowId:
    """
    y = y or "document.body.scrollHeight"
    x = x or "document.body.scrollWidth"
    return JsFncs.JsFunction("%s.scrollTo(%s, %s)" % (windowId, x, y))

  def print(self, windowId="window"):
    """
    Prints the content of the current window

    Documentation
    https://www.w3schools.com/Jsref/met_win_print.asp

    :param windowId: The JavaScript window object

    :return: Void, The Javascript String
    """
    return JsFncs.JsFunction("%s.print()" % windowId)

  def alert(self, jsData, jsFnc=None, windowId="window"):
    """
    The alert() method displays an alert box with a specified message and an OK button.

    Example
    rptObj.js.window.alert("Test")
    rptObj.js.alert("Test 2")

    Documentation
    https://www.w3schools.com/jsref/met_win_alert.asp

    :param jsData: Optional. Specifies the text to display in the alert box, or an object converted into a string and displayed
    :param jsFnc: A JsFnc or a list of JsFncs
    :param windowId: The JavaScript window object

    :return:
    """
    return JsFncs.JsFunction("%s.alert(%s)" % (windowId, JsUtils.jsConvertData(jsData, jsFnc)))

  def atob(self, jsData, jsFnc=None, windowId="window"):
    """
    Decodes a base-64 encoded string

    Example
    jsObj.window.btoa("Test").setVar("bin")
    jsObj.window.atob(jsObj.objects.get("bin"))

    Documentation
    https://www.w3schools.com/jsref/met_win_atob.asp

    :param jsData: Required. The string which has been encoded by the btoa() method
    :param jsFnc: A JsFnc or a list of JsFncs
    :param windowId: The JavaScript window object

    :return:
    """
    return JsFncs.JsFunction("%s.atob(%s)" % (windowId, JsUtils.jsConvertData(jsData, jsFnc)))

  def btoa(self, jsData, jsFnc=None, windowId="window"):
    """
    Encodes a string in base-64

    Example
    jsObj.window.btoa("Test").setVar("bin")

    Documentation
    https://www.w3schools.com/jsref/met_win_btoa.asp

    :param jsData: Required. The string to be encoded
    :param jsFnc: A JsFnc or a list of JsFncs
    :param windowId: The JavaScript window object

    :return:
    """
    return JsObject.JsObject("%s.btoa(%s)" % (windowId, JsUtils.jsConvertData(jsData, jsFnc)), isPyData=False)

  def setInterval(self, jsFncs, varId, milliseconds, windowId="window", setVar=True):
    """
    The setInterval() method calls a function or evaluates an expression at specified intervals (in milliseconds).

    The setInterval() method will continue calling the function until clearInterval() is called, or the window is closed.

    Example
    jsObj.window.setInterval([jsObj.console.log(jsObj.math.random())], 5000)

    Documentation
    https://www.w3schools.com/jsref/met_win_setinterval.asp

    #TODO: Add a control on setInterval to only have one created

    :param jsFncs: Required. The function that will be executed
    :param varId:
    :param milliseconds: Required. The intervals (in milliseconds) on how often to execute the code. If the value is less than 10, the value 10 is used
    :param windowId: The JavaScript window object
    :param setVar: Boolean.

    :return:
    """
    jsFncs = JsUtils.jsConvertFncs(jsFncs)
    if setVar:
      return JsFncs.JsFunction("var %s = %s.setInterval(function(){%s}, %s)" % (varId, windowId, ";".join(jsFncs), milliseconds))

    return JsFncs.JsFunction("%s.setInterval(function(){%s}, %s)" % (windowId, ";".join(jsFncs), milliseconds))

  def clearInterval(self, varId, windowId="window"):
    """
    The clearInterval() method clears a timer set with the setInterval() method.

    The ID value returned by setInterval() is used as the parameter for the clearInterval() method.

    Example
    jsObj.window.setInterval([jsObj.console.log(jsObj.math.random())], 500).setVar("interva1"),
    jsObj.window.clearInterval(jsObj.objects.get("interva1"))

    Documentation
    https://www.w3schools.com/jsref/met_win_clearinterval.asp

    #TODO: Check if interval is unique

    :param varId: A PythonJs object (JsArray, JsObject...)
    :param windowId: The JavaScript window object

    :return: Void, The Javascript String
    """
    js_data = varId if not hasattr(varId, "toStr") else JsUtils.jsConvertData(varId, None)
    return JsFncs.JsFunction("%s.clearInterval(%s); %s = undefined" % (windowId, js_data, js_data))

  def toggleInterval(self, jsFncs, varId, milliseconds, windowId="window"):
    """

    Example
    rptObj.ui.button("Interval Toggle").click([
      rptObj.js.window.toggleInterval(rptObj.js.console.log('Print called'), 'test', 400),
    ])

    Documentation

    :param jsFncs:
    :param varId:
    :param milliseconds:
    :param windowId:
    """
    interval = self.setInterval(jsFncs, varId, milliseconds, windowId, setVar=False)
    clear = self.clearInterval(varId, windowId)
    return JsFncs.JsFunction("if(%s){%s = %s} else{%s}" % (JsUtils.isNotDefined(varId), varId, interval, clear))

  def setTimeout(self, jsFncs, milliseconds=0, windowId="window"):
    """
    The setTimeout() method calls a function or evaluates an expression after a specified number of milliseconds.

    Documentation
    https://www.w3schools.com/jsref/met_win_settimeout.asp

    :param jsFncs: Required. The function that will be executed
    :param milliseconds: 	Optional. The number of milliseconds to wait before executing the code. If omitted, the value 0 is used
    :param windowId: The JavaScript window object

    :return:
    """
    jsFncs = JsUtils.jsConvertFncs(jsFncs)
    return JsObject.JsObject("%s.setTimeout(function(){%s}, %s)" % (windowId, ";".join(jsFncs), milliseconds), setVar=True, isPyData=False)

  def clearTimeout(self, jsData, jsFnc=None, windowId="window"):
    """
    The clearTimeout() method clears a timer set with the setTimeout() method.
    The ID value returned by setTimeout() is used as the parameter for the clearTimeout() method.

    Documentation
    https://www.w3schools.com/jsref/met_win_cleartimeout.asp

    :param windowId: The JavaScript window object

    :return:
    """
    return JsFncs.JsFunction("%s.clearTimeout(%s)" % (windowId, JsUtils.jsConvertData(jsData, jsFnc)))

  def getComputedStyle(self, jsElement, jsPseudoElement=None, windowId="window"):
    """
    The getComputedStyle() method gets all the actual (computed) CSS property and values of the specified element.

    Documentation
    https://www.w3schools.com/jsref/jsref_getcomputedstyle.asp

    :param jsElement: Required. The element to get the computed style for
    :param windowId: The JavaScript window object

    :return: A CSSStyleDeclaration object containing CSS declaration block of the element
    """
    if jsPseudoElement is None:
      return JsFncs.JsFunction("%s.getComputedStyle(%s)" % (windowId, jsElement))

    return JsFncs.JsFunction("%s.getComputedStyle(%s, %s)" % (windowId, jsElement, jsPseudoElement))

  def getSelection(self, windowId="window"):
    """
    Returns a Selection object representing the range of text selected by the user

    Documentation

    :param windowId: The JavaScript window object

    :return:
    """
    return JsFncs.JsFunction("%s.getSelection()" % windowId)

  def getVar(self, varName, windowId="window"):
    """
    Get the Javascript Variable name

    Documentation

    :param varName: The Variable name
    :param windowId: The JavaScript window object

    :return: Return the piece of script to be added to the Javascript
    """
    return "%s['%s']" % (windowId, varName)

  def onPageShow(self, jsFncs):
    """

    Documentation

    :param jsFncs:

    :return:
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self._context.setdefault('pageshow', []).extend(jsFncs)

  def onBeforeUnload(self, jsFncs):
    """

    Documentation

    :param jsFncs: A JsFnc or a list of JsFncs

    :return:
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self._context.setdefault('beforeunload', []).extend(jsFncs)

