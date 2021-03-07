"""
Wrapper to the Javascript Window module

Allows to save key/value pairs in a web browser. Stores the data with no expiration date
The localStorage and sessionStorage properties allow to save key/value pairs in a web browser.

Related Pages:

		https://www.w3schools.com/Jsref/prop_win_localstorage.asp
"""

from epyk.core.js import JsUtils
from epyk.core.js.objects import JsNodeDom

# All the predefined variable types
from epyk.core.js.fncs import JsFncs
from epyk.core.js.primitives import JsBoolean
from epyk.core.js.primitives import JsNumber
from epyk.core.js.primitives import JsObject


class JsLocalStorage:

  def key(self, i):
    """
    Description:
    ------------
    The key() method returns name of the key with the specified index.

    The localStorage object stores data with no expiration date.
    The data will not be deleted when the browser is closed, and will be available the next day, week, or year.

    Usage:
    -----

      jsObj.localStorage.key(0)

    Related Pages:

      https://www.w3schools.com/jsref/met_storage_key.asp

    Attributes:
    ----------
    :param i: Integer. Required. A Number representing the index of the key you want to get the name of.

    :return: A String, representing the name of the specified key
    """
    i = JsUtils.jsConvertData(i, None)
    return JsObject.JsObject("localStorage.key(%s)" % i)

  def __setitem__(self, key, data):
    """
    Description:
    ------------

    Usage:
    -----


    Attributes:
    ----------
    :param key:
    :param data:
    """
    self.setItem(key, data)

  def __getitem__(self, item):
    """
    Description:
    ------------
    Python wrapper to getItem.

    Usage:
    -----

      jsObj.console.log(jsObj.sessionStorage["lastname"])

    Attributes:
    ----------
    :param item: String. The item name
    """
    return self.getItem(item)

  def setItem(self, key, data):
    """
    Description:
    ------------
    Syntax for SAVING data to localStorage.

    The localStorage object stores data with no expiration date.
    The data will not be deleted when the browser is closed, and will be available the next day, week, or year.

    Usage:
    -----

      jsObj.localStorage.getItem("lastname", "test")

    Related Pages:

      https://www.w3schools.com/jsref/met_storage_setitem.asp

    Attributes:
    ----------
    :param key: String. Required. A String specifying the name of the key you want to set the value of.
    :param data: String. Required. A String specifying the value of the key you want to set the value of.

    :return: A String, representing the inserted value.
    """
    key = JsUtils.jsConvertData(key, None)
    data = JsUtils.jsConvertData(data, None)
    return JsObject.JsObject("localStorage.setItem(%s, %s)" % (key, data))

  def getItem(self, key):
    """
    Description:
    ------------
    Syntax for READING data from localStorage:

    The localStorage object stores data with no expiration date.
    The data will not be deleted when the browser is closed, and will be available the next day, week, or year.

    Usage:
    -----

      jsObj.localStorage.getItem("lastname")

    Related Pages:

      https://www.w3schools.com/jsref/met_storage_getitem.asp

    Attributes:
    ----------
    :param key: String. Required. A String specifying the name of the key you want to get the value of.

    :return: A String, representing the value of the specified key
    """
    key = JsUtils.jsConvertData(key, None)
    return JsObject.JsObject("localStorage.getItem(%s)" % key)

  def removeItem(self, key):
    """
    Description:
    ------------
    The removeItem() method removes the specified Storage Object item.

    The localStorage object stores data with no expiration date.
    The data will not be deleted when the browser is closed, and will be available the next day, week, or year.

    Usage:
    -----

      jsObj.localStorage.removeItem("lastname")

    Related Pages:

      https://www.w3schools.com/jsref/met_storage_removeitem.asp

    Attributes:
    ----------
    :param key: String. Required. A String specifying the name of the item you want to remove.

    :return: Void
    """
    key = JsUtils.jsConvertData(key, None)
    return JsFncs.JsFunction("localStorage.removeItem(%s)" % key)

  def clear(self):
    """
    Description:
    ------------
    The clear() method removes all the Storage Object item for this domain.

    The localStorage object stores data with no expiration date.
    The data will not be deleted when the browser is closed, and will be available the next day, week, or year.

    Usage:
    -----

      jsObj.localStorage.clear()

    Related Pages:

      https://www.w3schools.com/jsref/met_storage_clear.asp

    :return: Void
    """
    return JsFncs.JsFunction("localStorage.clear()")


class JsSessionStorage:
  """
  Description:
  ------------
  The localStorage and sessionStorage properties allow to save key/value pairs in a web browser.

  The sessionStorage object stores data for only one session (the data is deleted when the browser tab is closed).

  Related Pages:
  --------------

    https://www.w3schools.com/Jsref/prop_win_sessionstorage.asp
  """

  def key(self, i):
    """
    Description:
    ------------
    The sessionStorage object stores data for only one session (the data is deleted when the browser tab is closed).

    Usage:
    -----

    Attributes:
    ----------
    :param i: Integer. The key number.
    """
    i = JsUtils.jsConvertData(i, None)
    return JsObject.JsObject("sessionStorage.key(%s)" % i)

  def __setitem__(self, key, data):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param key:
    :param data:
    """
    self.setItem(key, data)

  def __getitem__(self, item):
    """
    Description:
    ------------
    Python wrapper to getItem.

    Usage:
    -----

      jsObj.console.log(jsObj.sessionStorage["lastname"])

    Attributes:
    ----------
    :param item:
    """
    return self.getItem(item)

  def setItem(self, key, data):
    """
    Description:
    ------------
    Syntax for SAVING data to sessionStorage.

    The sessionStorage object stores data for only one session (the data is deleted when the browser tab is closed).

    Usage:
    -----

      jsObj.sessionStorage.setItem("lastname", "Smith")
      jsObj.sessionStorage.setItem("lastname", jsObj.objects.get("bin")),

    Related Pages:

      https://www.w3schools.com/Jsref/prop_win_sessionstorage.asp

    Attributes:
    ----------
    :param key: The key used to store the data in the session cache.
    :param data:
    """
    key = JsUtils.jsConvertData(key, None)
    data = JsUtils.jsConvertData(data, None)
    return JsObject.JsObject("sessionStorage.setItem(%s, %s)" % (key, data))

  def getItem(self, key):
    """
    Description:
    ------------
    Syntax for READING data from sessionStorage

    The sessionStorage object stores data for only one session (the data is deleted when the browser tab is closed).

    Usage:
    -----

      jsObj.sessionStorage.getItem("lastname")
      jsObj.console.log(jsObj.sessionStorage.getItem("lastname"))

    Attributes:
    ----------
    :param key:
    """
    key = JsUtils.jsConvertData(key, None)
    return JsObject.JsObject("sessionStorage.getItem(%s)" % key)

  def removeItem(self, jsData, jsDataKey=None, isPyData=False, jsFnc=None):
    """
    Description:
    ------------
    Syntax for REMOVING ALL saved data from sessionStorage.

    The sessionStorage object stores data for only one session (the data is deleted when the browser tab is closed).

    Usage:
    -----

      jsObj.sessionStorage.removeItem("lastname")

    Related Pages:

      https://www.w3schools.com/jsref/met_storage_removeitem.asp

    Attributes:
    ----------
    :param jsData:
    :param jsDataKey:
    :param isPyData:
    :param jsFnc:
    """
    jsData = JsUtils.jsConvert(jsData, jsDataKey, isPyData, jsFnc)
    return JsFncs.JsFunction("sessionStorage.removeItem(%s)" % jsData)

  def clear(self):
    """
    Description:
    ------------
    Syntax for REMOVING ALL saved data from sessionStorage

    The sessionStorage object stores data for only one session (the data is deleted when the browser tab is closed).

    Related Pages:

      https://www.w3schools.com/jsref/prop_win_sessionstorage.asp
    """
    return JsFncs.JsFunction("sessionStorage.clear()")


class JsHistory:
  """
  Description:
  ------------
  Interface to the Javascript history module.

  Related Pages:
  --------------

    https://www.w3schools.com/js/js_window_history.asp
  """

  def __init__(self, context):
    self.__jsObj = context

  @property
  def length(self):
    """
    Description:
    ------------
    The length property returns the number of URLs in the history list of the current browser window.

    Usage:
    -----

      rptObj.js.window.history.length

    Related Pages:

      https://www.w3schools.com/jsref/prop_his_length.asp

    :return: A Number, representing the number of entries in the session history
    """
    return JsNumber.JsNumber("history.length", isPyData=False)

  def back(self):
    """
    Description:
    ------------
    The back() method loads the previous URL in the history list.

    Usage:
    -----

      rptObj.js.window.history.back()

    Related Pages:

      https://www.w3schools.com/jsref/met_his_back.asp

    :return: The Javascript String to be added to the page
    """
    return JsFncs.JsFunction("window.history.back()")

  def forward(self):
    """
    Description:
    ------------
    The forward() method loads the next URL in the history list.

    Related Pages:

      https://www.w3schools.com/jsref/met_his_forward.asp

    :return: The Javascript String to be added to the page.
    """
    return JsFncs.JsFunction("window.history.forward()")

  def go(self, number):
    """
    Description:
    ------------
    The go() method loads a specific URL from the history list.

    Related Pages:

      https://www.w3schools.com/jsref/met_his_go.asp

    Attributes:
    ----------
    :param number: Required. The parameter can either be a number which goes to the URL within the specific position (-1 goes back one page, 1 goes forward one page), or a string.

    :return: The Javascript String to be added to the page
    """
    return JsFncs.JsFunction("window.history.go(%s)" % number)

  def pushState(self, stateObj, title, url):
    """
    Description:
    ------------
    Pushes the given data onto the session history stack with the specified title and, if provided, URL.

    Note that pushState() never causes a hashchange event to be fired, even if the new URL differs from the old URL
    only in its hash

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/History_API

    Attributes:
    ----------
    :param stateObj: The state object is a JavaScript object which is associated with the new history entry created by pushState()
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
    Description:
    ------------
    history.replaceState() operates exactly like history.pushState() except that replaceState() modifies the current
    history entry instead of creating a new one.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/History_API

    Attributes:
    ----------
    :param stateObj: he state object is a JavaScript object which is associated with the new history entry created by pushState()
    :param title: Firefox currently ignores this parameter, although it may use it in the future
                  Passing the empty string here should be safe against future changes to the method.
                  Alternatively, you could pass a short title for the state to which you're moving.
    :param url: The new history entry's URL is given by this parameter.
                Note that the browser won't attempt to load this URL after a call to pushState(),
    """
    return JsFncs.JsFunction("window.history.replaceState('%s', '%s', %s)" % (stateObj, title, url))

  def updateState(self, key, val):
    """
    Description:
    ------------
    Wrapper function

    This function is a simple wrapping function on top of the pushState history method.
    The purpose of this method is to make easier the update of the url whenever a component in the framework is updated.

    Usage:
    -----

      htmlObj.js.js.window.history.updateState(self.htmlCode, self.val)

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/History_API

    Attributes:
    ----------
    :param key: String. The key to be added or updated in the current URL.
    :param val: String. The value to be changed to the current URL.

    :return: The Javascript String for the method.
    """
    self.__jsObj.registerFunction("updateUrl", [
      self.__jsObj.objects.new([], varName="newPmts"),
      self.__jsObj.location.search.substr(1).split("&").forEach([
        self.__jsObj.if_(self.__jsObj.data.loop().val.toString(explicit=False).includes("=", jsObj=self.__jsObj), [
          self.__jsObj.objects.array.new(self.__jsObj.data.loop().val.toString().split("="), varName="urlPmts"),
          self.__jsObj.objects.array.get("urlPmts")[0].toString(),
          self.__jsObj.objects.get("newPmts").addItem(
            self.__jsObj.objects.array.get("urlPmts")[0], self.__jsObj.objects.array.get("urlPmts")[1])
        ])
      ]),

      self.__jsObj.objects.get("newPmts").addItem(self.__jsObj.objects.get("urlKey"), self.__jsObj.objects.get("urlValue")),
      # Then we concatenate the URL
      self.__jsObj.objects.array.new([], varName="pmts"),
      self.__jsObj.objects.get("newPmts").entries().forEach([
        self.__jsObj.objects.array.get("pmts").push(
          self.__jsObj.data.loop().val[0].toString(explicit=False).add("=").add(self.__jsObj.data.loop().val[1]))
      ]),
      self.__jsObj.return_(
        self.__jsObj.location.origin + self.__jsObj.location.pathname + "?" + self.__jsObj.objects.array.get("pmts").join("&"))
      ], ["urlKey", "urlValue"])
    return self.pushState("data", "", JsFncs.JsFunction("updateUrl(%s, %s)" % (
      JsUtils.jsConvertData(key, None), JsUtils.jsConvertData(val, None))))


class JsWindowEvent:

  def addEventListener(self, eventType, jsFncs, windowId="window", subEvents=None, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param eventType:
    :param jsFncs:
    :param windowId:
    :param subEvents: List of names you want your underlying function to have as arguments.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    subEvents = '' if not subEvents else ','.join(subEvents)
    eventType = JsUtils.jsConvertData(eventType, None)
    jsFncs = JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile)
    return JsFncs.JsFunction("%s.addEventListener(%s, function(%s){%s})" % (windowId, eventType, subEvents, jsFncs))

  def addScrollListener(self, jsFncs, windowId="window"):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param jsFncs:
    :param windowId:
    """
    return self.addEventListener("scroll", jsFncs, windowId)

  def addContentLoaded(self, jsFncs, windowId="window"):
    """
    Description:
    ------------
    The DOMContentLoaded event fires when the initial HTML document has been completely loaded and parsed,
    without waiting for stylesheets, images, and subframes to finish loading.

    Usage::

      rptObj.js.addOnLoad(
      rptObj.js.window.events.addContentLoaded(rptObj.js.alert("DOM fully loaded and parsed"))
      )

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/Window/DOMContentLoaded_event

    Attributes:
    ----------
    :param jsFncs:
    :param windowId:
    """
    return self.addEventListener("DOMContentLoaded", jsFncs, windowId)

  def addClickListener(self, jsFncs, windowId="window", subEvents=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param jsFncs:
    :param windowId:
    """
    return self.addEventListener("click", jsFncs, windowId, subEvents)


class JsWindow:
  """
  Description:
  ------------
  The window object represents an open window in a browser.

  If a document contain frames (<iframe> tags), the browser creates one window object for the HTML document,
  and one additional window object for each frame.

  Related Pages:
  --------------
  https://www.w3schools.com/Jsref/obj_window.asp
  """
  @property
  def scrollY(self, windowId="window"):
    """
    Description:
    ------------
    The read-only scrollY property of the Window interface returns the number of pixels that the document is
    currently scrolled vertically.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/Window/scrollY

    Attributes:
    ----------
    :param windowId: String. Optional. The window reference.
    """
    return JsNumber.JsNumber("%s.scrollY" % windowId)

  @property
  def innerHeight(self, windowId="window"):
    """
    Description:
    ------------
    The innerHeight property returns the height of a window's content area.

    Related Pages:

      https://www.w3schools.com/jsref/prop_win_innerheight.asp

    Attributes:
    ----------
    :param windowId: String. Optional. The window reference.
    """
    return JsNumber.JsNumber("%s.innerHeight" % windowId)

  @property
  def scrollEndPage(self, windowId="window"):
    """
    Description:
    ------------
    The scrollEndPage property indicates if the page is scrolled to the end.

    Attributes:
    ----------
    :param windowId: String. Optional. The window reference.
    """
    return JsBoolean.JsBoolean("(%s.scrollY + %s.innerHeight > document.body.clientHeight)? true: false" % (
      windowId, windowId), isPyData=False)

  @property
  def scrollPercentage(self, windowId="window"):
    """
    Description:
    ------------
    The scrollPercentage property return the percentage of the page scrolled.

    Attributes:
    ----------
    :param windowId: String. Optional. The window reference.
    """
    return JsNumber.JsNumber(
      "Math.min((%s.scrollY + %s.innerHeight)/ document.body.clientHeight * 100, 100)" % (
        windowId, windowId), isPyData=False)

  @property
  def scrollMaxY(self, windowId="window"):
    """
    Description:
    ------------
    The Window.scrollMaxY read-only property returns the maximum number of pixels that the document can be
    scrolled vertically.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/Window/scrollMaxY

    Attributes:
    ----------
    :param windowId: String. Optional. The window reference.
    """
    return JsNumber.JsNumber(
      "(%s.scrollMaxY || (document.documentElement.scrollHeight - document.documentElement.clientHeight))" % windowId)

  def __init__(self, src=None):
    """
    Description:
    ------------

    :type src: epyk.Lib.js.Js.JsBase

    Attributes:
    ----------
    :param src:
    """
    self.__src = src
    self._context = src._context if hasattr(src, '_context') else {}

  @property
  def document(self):
    """
    Description:
    ------------
    Interface to the DOM object on the current window.

    :return: A Python JsDoms object wrapping the DOM Js interface.
    """
    return JsNodeDom.JsDoms(self.__src)

  @property
  def history(self):
    """
    Description:
    ------------
    Interface to the History object.

    :return: A Python Js History object.
    """
    return JsHistory(self.__src)

  def close(self, windowId="window"):
    """
    Description:
    ------------
    Closes the current window.

    Related Pages:

      https://www.w3schools.com/jsref/met_win_close.asp

    Attributes:
    ----------
    :param windowId: String. Optional. The JavaScript window object reference variable.

    :return: The String representing the Javascript function.
    """
    return JsFncs.JsFunction("%s.close()" % windowId)

  @property
  def events(self):
    """
    Description:
    ------------
    Property to all the events.
    """
    return JsWindowEvent()

  def addEventListener(self, eventType, jsFncs, windowId="window", profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param eventType:
    :param jsFncs:
    :param windowId: String. Optional. The JavaScript window object reference variable.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    eventType = JsUtils.jsConvertData(eventType, None)
    jsFncs = JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile)
    return JsFncs.JsFunction("%s.addEventListener(%s, function(){%s})" % (windowId, eventType, jsFncs))

  def open(self, url, name="_self", specs=None, replace=None, windowId="window"):
    """
    Description:
    ------------
    Opens a new browser window

    Related Pages:

      https://www.w3schools.com/Jsref/met_win_open.asp

    Attributes:
    ----------
    :param url: Optional. Specifies the URL of the page to open. If no URL is specified, a new window/tab with about:blank is opened
    :param name: Optional. Specifies the target attribute or the name of the window.
    :param specs: Optional. A comma-separated list of items, no whitespaces.
    :param replace: Optional. Specifies whether the URL creates a new entry or replaces the current entry in the history list
    :param windowId: String. Optional. The JavaScript window object reference variable.
    """
    url = JsUtils.jsConvertData(url, None)
    name = JsUtils.jsConvertData(name, None)
    specs = JsUtils.jsConvertData(specs, None)
    replace = JsUtils.jsConvertData(replace, None)
    return JsFncs.JsFunction("%s.open(%s, %s, %s, %s)" % (windowId, url, name, specs, replace))

  def postData(self, jsData):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param jsData:
    """

    if not isinstance(jsData, list):
      jsData = [jsData]

  def download(self, data, fileName, profile=False):
    """
    Description:
    ------------
    Download the data from a flat file.

    Usage:
    -----

      rptObj.js.window.download(rptObj.js.window.btoa(rptObj.js.objects.get("test")), fileName="test.txt")

    Attributes:
    ----------
    :param data:
    :param fileName:
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.

    :return: Void,
    """
    data = JsUtils.jsConvertData(data, None)
    return JsFncs.JsFunction(JsUtils.jsConvertFncs([
      self.__src.createElement("a", varName="a_temp").setAttribute("download", fileName).setAttribute(
        "href", JsFncs.JsFunction("'data:text/csv;base64,'+ %s" % data)),
      self.__src.body.appendChild(self.__src.objects.get("a_temp")),
      self.__src.objects.dom.get("a_temp").click(),
      #self.__src.objects.dom.get("a_temp").remove()
    ], toStr=True, profile=profile))
    #return JsFncs.JsFunction("%s.open('data:text/csv;base64,'+ %s, '_self')" % (windowId, data))

  def moveBy(self, x, y, windowId="window"):
    """
    Description:
    ------------
    The moveBy() method moves a window a specified number of pixels relative to its current coordinates.

    Related Pages:

      https://www.w3schools.com/Jsref/met_win_moveby.asp

    Attributes:
    ----------
    :param x: Integer. The horizontal move in pixel.
    :param y: Integer. The vertical move in pixel.
    :param windowId: String. Optional. The JavaScript window object reference variable.
    """
    x = JsUtils.jsConvertData(x, None)
    y = JsUtils.jsConvertData(y, None)
    return JsFncs.JsFunction("%s.moveBy(%s, %s)" % (windowId, x, y))

  def focus(self, windowId="window"):
    """
    Description:
    ------------
    The focus() method sets focus to the current window

    Related Pages:

      https://www.w3schools.com/Jsref/met_win_focus.asp

    Attributes:
    ----------
    :param windowId: String. Optional. The JavaScript window object reference variable.

    :return: Void, The Javascript String
    """
    return JsFncs.JsFunction("%s.focus()" % windowId)

  def scroll(self, x, y, windowId="window"):
    """
    Description:
    ------------
    The Window.scroll() method scrolls the window to a particular place in the document.

    Related Pages:

      https://developer.mozilla.org/uk/docs/Web/API/Window/scroll

    Attributes:
    ----------
    :param x: Integer. The pixel along the horizontal axis of the document that you want displayed in the upper left.
    :param y: Integer. The pixel along the vertical axis of the document that you want displayed in the upper left.
    :param windowId: String. Optional. The JavaScript window object reference variable.
    """
    return JsFncs.JsFunction("%s.scroll(%s, %s)" % (windowId, x, y))

  def scrollTo(self, x=None, y=None, windowId="window"):
    """
    Description:
    ------------
    The window.scrollTo() go to a particular point.

    Attributes:
    ----------
    :param x: Integer. Optional.
    :param y: Integer. Optional.
    :param windowId: String. Optional. The JavaScript window object reference variable.
    """
    y = y or "document.body.scrollHeight"
    x = x or "document.body.scrollWidth"
    return JsFncs.JsFunction("%s.scrollTo(%s, %s)" % (windowId, x, y))

  def scrollUp(self, windowId="window"):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param windowId: String. Optional. The JavaScript window object reference variable.
    """
    return JsFncs.JsFunction("%s.scrollTo(0, 0)" % windowId)

  def print_(self, windowId="window"):
    """
    Description:
    ------------
    Prints the content of the current window.

    Related Pages:

      https://www.w3schools.com/Jsref/met_win_print.asp

    Attributes:
    ----------
    :param windowId: String. Optional. The JavaScript window object reference variable.

    :return: Void, The Javascript String
    """
    return JsFncs.JsFunction("%s.print()" % windowId)

  def alert(self, jsData, jsFnc=None, windowId="window", skip_data_convert=False):
    """
    Description:
    ------------
    The alert() method displays an alert box with a specified message and an OK button.

    Usage:
    -----

      page.js.window.alert("Test")
      page.js.alert("Test 2")

    Related Pages:

      https://www.w3schools.com/jsref/met_win_alert.asp

    Attributes:
    ----------
    :param jsData: Optional. Specifies the text to display in the alert box, or an object converted into a string and displayed
    :param jsFnc: A JsFnc or a list of JsFncs.
    :param windowId: String. Optional. The JavaScript window object reference variable.
    """
    if skip_data_convert:
      return JsFncs.JsFunction("%s.alert(%s)" % (windowId, jsData))

    if hasattr(jsData, 'dom'):
      jsData = jsData.dom.content
    return JsFncs.JsFunction("%s.alert(%s)" % (windowId, JsUtils.jsConvertData(jsData, jsFnc)))

  def atob(self, jsData, jsFnc=None, windowId="window"):
    """
    Description:
    ------------
    Decodes a base-64 encoded string.

    Usage:
    -----

      jsObj.window.btoa("Test").setVar("bin")
      jsObj.window.atob(jsObj.objects.get("bin"))

    Related Pages:

      https://www.w3schools.com/jsref/met_win_atob.asp

    Attributes:
    ----------
    :param jsData: Required. The string which has been encoded by the btoa() method
    :param jsFnc: A JsFnc or a list of JsFncs
    :param windowId: String. Optional. The JavaScript window object reference variable.
    """
    return JsFncs.JsFunction("%s.atob(%s)" % (windowId, JsUtils.jsConvertData(jsData, jsFnc)))

  def btoa(self, jsData, jsFnc=None, windowId="window"):
    """
    Description:
    ------------
    Encodes a string in base-64.

    Usage:
    -----

      jsObj.window.btoa("Test").setVar("bin")

    Related Pages:

      https://www.w3schools.com/jsref/met_win_btoa.asp

    Attributes:
    ----------
    :param jsData: Required. The string to be encoded
    :param jsFnc: A JsFnc or a list of JsFncs
    :param windowId: String. Optional. The JavaScript window object reference variable.
    """
    return JsObject.JsObject("%s.btoa(%s)" % (windowId, JsUtils.jsConvertData(jsData, jsFnc)), isPyData=False)

  def setInterval(self, jsFncs, varId, milliseconds, windowId="window", setVar=True, profile=False):
    """
    Description:
    ------------
    The setInterval() method calls a function or evaluates an expression at specified intervals (in milliseconds).

    The setInterval() method will continue calling the function until clearInterval() is called, or the window
    is closed.

    Usage:
    -----

      jsObj.window.setInterval([jsObj.console.log(jsObj.math.random())], 5000)

    Related Pages:

      https://www.w3schools.com/jsref/met_win_setinterval.asp

    #TODO: Add a control on setInterval to only have one created

    Attributes:
    ----------
    :param jsFncs: Required. The function that will be executed
    :param varId:
    :param milliseconds: Required. The intervals (in milliseconds) on how often to execute the code. If the value is less than 10, the value 10 is used
    :param windowId: The JavaScript window object
    :param setVar: Boolean.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    jsFncs = JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile)
    if setVar:
      if windowId == 'window':
        # To make the variable scope as global
        varId = "window['%s']" % varId
      else:
        varId = "var %s" % varId

      return JsFncs.JsFunction(
        "%s = %s.setInterval(function(){%s}, %s)" % (varId, windowId, jsFncs, milliseconds))

    return JsFncs.JsFunction("%s.setInterval(function(){%s}, %s)" % (windowId, jsFncs, milliseconds))

  def clearInterval(self, varId, windowId="window"):
    """
    Description:
    ------------
    The clearInterval() method clears a timer set with the setInterval() method.

    The ID value returned by setInterval() is used as the parameter for the clearInterval() method.

    Usage:
    -----

      jsObj.window.setInterval([jsObj.console.log(jsObj.math.random())], 500).setVar("interva1"),
      jsObj.window.clearInterval(jsObj.objects.get("interva1"))

    Related Pages:

      https://www.w3schools.com/jsref/met_win_clearinterval.asp

    #TODO: Check if interval is unique

    Attributes:
    ----------
    :param varId: A PythonJs object (JsArray, JsObject...)
    :param windowId: The JavaScript window object

    :return: Void, The Javascript String
    """
    js_data = varId if not hasattr(varId, "toStr") else JsUtils.jsConvertData(varId, None)
    return JsFncs.JsFunction("%s.clearInterval(%s); %s = undefined" % (windowId, js_data, js_data))

  def toggleInterval(self, jsFncs, varId, milliseconds, windowId="window"):
    """
    Description:
    ------------

    Usage:
    -----

      page.ui.button("Interval Toggle").click([
        page.js.window.toggleInterval(rptObj.js.console.log('Print called'), 'test', 400),
      ])

    Attributes:
    ----------
    :param jsFncs:
    :param varId:
    :param milliseconds:
    :param windowId:
    """
    interval = self.setInterval(jsFncs, varId, milliseconds, windowId, setVar=False)
    clear = self.clearInterval(varId, windowId)
    return JsFncs.JsFunction("if(%s){%s = %s} else{%s}" % (JsUtils.isNotDefined(varId), varId, interval, clear))

  def setTimeout(self, jsFncs, milliseconds=0, windowId="window", profile=False):
    """
    Description:
    ------------
    The setTimeout() method calls a function or evaluates an expression after a specified number of milliseconds.

    Related Pages:

      https://www.w3schools.com/jsref/met_win_settimeout.asp

    Attributes:
    ----------
    :param jsFncs: List. Required. The function that will be executed
    :param milliseconds: Integer. Optional. The number of milliseconds to wait before executing the code.
    :param windowId: String. Optional. The JavaScript window object.
    :param profile: Boolean. Optional. Set to true to get the profile for the function on the Javascript console.
    """
    return JsObject.JsObject(
      "%s.setTimeout(function(){%s}, %s)" % (
        windowId, JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile), milliseconds),
      setVar=True, isPyData=False)

  def clearTimeout(self, jsData, jsFnc=None, windowId="window"):
    """
    Description:
    ------------
    The clearTimeout() method clears a timer set with the setTimeout() method.
    The ID value returned by setTimeout() is used as the parameter for the clearTimeout() method.

    Related Pages:

      https://www.w3schools.com/jsref/met_win_cleartimeout.asp

    Attributes:
    ----------
    :param jsData:
    :param jsFnc:
    :param windowId: The JavaScript window object.
    """
    return JsFncs.JsFunction("%s.clearTimeout(%s)" % (windowId, JsUtils.jsConvertData(jsData, jsFnc)))

  def getComputedStyle(self, jsElement, jsPseudoElement=None, windowId="window"):
    """
    Description:
    ------------
    The getComputedStyle() method gets all the actual (computed) CSS property and values of the specified element.

    Related Pages:

      https://www.w3schools.com/jsref/jsref_getcomputedstyle.asp

    Attributes:
    ----------
    :param jsElement: Required. The element to get the computed style for
    :param windowId: The JavaScript window object

    :return: A CSSStyleDeclaration object containing CSS declaration block of the element
    """
    if jsPseudoElement is None:
      return JsFncs.JsFunction("%s.getComputedStyle(%s)" % (windowId, jsElement))

    return JsFncs.JsFunction("%s.getComputedStyle(%s, %s)" % (windowId, jsElement, jsPseudoElement))

  def getSelection(self, windowId="window"):
    """
    Description:
    ------------
    Returns a Selection object representing the range of text selected by the user.

    Attributes:
    ----------
    :param windowId: The JavaScript window object
    """
    return JsFncs.JsFunction("%s.getSelection()" % windowId)

  def getVar(self, varName, windowId="window"):
    """
    Description:
    ------------
    Get the Javascript Variable name.

    Attributes:
    ----------
    :param varName: The Variable name.
    :param windowId: The JavaScript window object.

    :return: Return the piece of script to be added to the Javascript.
    """
    return "%s['%s']" % (windowId, varName)

  def onPageShow(self, jsFncs):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param jsFncs:
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self._context.setdefault('pageshow', []).extend(jsFncs)

  def onBeforeUnload(self, jsFncs):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param jsFncs: A JsFnc or a list of JsFncs
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self._context.setdefault('beforeunload', []).extend(jsFncs)

  def location(self, url, windowId="window"):
    """
    Description:
    ------------
    Change the window and open the page specify by the url.

    Attributes:
    ----------
    :param url: String. The new page url.
    :param windowId: String. Optional. The JavaScript window object.
    """
    url = JsUtils.jsConvertData(url, None)
    return JsFncs.JsFunction("%s.location = %s" % (windowId, url))
