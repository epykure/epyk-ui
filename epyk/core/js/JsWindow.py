"""
Wrapper to the Javascript Window module

Allows to save key/value pairs in a web browser. Stores the data with no expiration date
The localStorage and sessionStorage properties allow to save key/value pairs in a web browser.

Related Pages: https://www.w3schools.com/Jsref/prop_win_localstorage.asp
"""

from typing import Union, Optional, Any, List
from epyk.core.py import primitives

from epyk.core.js import JsUtils
from epyk.core.js.objects import JsNodeDom

# All the predefined variable types
from epyk.core.js.fncs import JsFncs
from epyk.core.js.primitives import JsBoolean
from epyk.core.js.primitives import JsNumber
from epyk.core.js.primitives import JsObject


class JsUrl:

    def createObjectURL(self, data: Union[primitives.JsDataModel, str]):
        """
        `Related Pages <https://developer.mozilla.org/en-US/docs/Web/API/Blob>`_

        :param data:
        """
        data = JsUtils.jsConvertData(data, None)
        return JsObject.JsObject.get("window.URL.createObjectURL(%s)" % data)


class JsLocalStorage:

    def key(self, i: Union[primitives.JsDataModel, int]):
        """The key() method returns name of the key with the specified index.

        The localStorage object stores data with no expiration date.
        The data will not be deleted when the browser is closed, and will be available the next day, week, or year.

        Usage::

          jsObj.localStorage.key(0)

        `Related Pages <https://www.w3schools.com/jsref/met_storage_key.asp>`_

        :param i: A Number representing the index of the key you want to get the name of

        :return: A String, representing the name of the specified key
        """
        i = JsUtils.jsConvertData(i, None)
        return JsObject.JsObject("localStorage.key(%s)" % i)

    def __setitem__(self, key: str, data):
        """

        :param key: The key attribute
        :param: Object. The value to store
        """
        self.setItem(key, data)

    def __getitem__(self, item: str):
        """Python wrapper to getItem.

        Usage::

          jsObj.console.log(jsObj.sessionStorage["lastname"])

        :param item: The item name
        """
        return self.getItem(item)

    def setItem(self, key: Union[primitives.JsDataModel, str], data: Any, force_json: bool = True):
        """Syntax for SAVING data to localStorage.

        The localStorage object stores data with no expiration date.
        The data will not be deleted when the browser is closed, and will be available the next day, week, or year.

        Usage::

          jsObj.localStorage.getItem("lastname", "test")

        `Related Pages <https://www.w3schools.com/jsref/met_storage_setitem.asp>`_

        :param key: A String specifying the name of the key you want to set the value of
        :param data: A String specifying the value of the key you want to set the value of
        :param force_json: Change the value object to a JSon string

        :return: A String, representing the inserted value.
        """
        key = JsUtils.jsConvertData(key, None)
        data = JsUtils.jsConvertData(data, None)
        if force_json:
            return JsObject.JsObject("localStorage.setItem(%s, JSON.stringify(%s))" % (key, data))

        return JsObject.JsObject("localStorage.setItem(%s, %s)" % (key, data))

    def getItem(self, key: Union[primitives.JsDataModel, str], force_json: bool = True):
        """Syntax for READING data from localStorage:

        The localStorage object stores data with no expiration date.
        The data will not be deleted when the browser is closed, and will be available the next day, week, or year.

        Usage::

          jsObj.localStorage.getItem("lastname")

        `Related Pages <https://www.w3schools.com/jsref/met_storage_getitem.asp>`_

        :param key: A String specifying the name of the key you want to get the value of
        :param force_json: Change the value json string to a javascript object

        :return: A String, representing the value of the specified key
        """
        key = JsUtils.jsConvertData(key, None)
        if force_json:
            return JsObject.JsObject("JSON.parse(localStorage.getItem(%s))" % key)

        return JsObject.JsObject("localStorage.getItem(%s)" % key)

    def removeItem(self, key: Union[primitives.JsDataModel, str]):
        """The removeItem() method removes the specified Storage Object item.

        The localStorage object stores data with no expiration date.
        The data will not be deleted when the browser is closed, and will be available the next day, week, or year.

        Usage::

          jsObj.localStorage.removeItem("lastname")

        `Related Pages <https://www.w3schools.com/jsref/met_storage_removeitem.asp>`_

        :param key: A String specifying the name of the item you want to remove.

        :return: Void
        """
        key = JsUtils.jsConvertData(key, None)
        return JsFncs.JsFunction("localStorage.removeItem(%s)" % key)

    def clear(self):
        """
        The clear() method removes all the Storage Object item for this domain.

        The localStorage object stores data with no expiration date.
        The data will not be deleted when the browser is closed, and will be available the next day, week, or year.

        Usage::

          jsObj.localStorage.clear()

        `Related Pages <https://www.w3schools.com/jsref/met_storage_clear.asp>`_

        :return: Void
        """
        return JsFncs.JsFunction("localStorage.clear()")


class JsSessionStorage:
    """
    The localStorage and sessionStorage properties allow to save key/value pairs in a web browser.

    The sessionStorage object stores data for only one session (the data is deleted when the browser tab is closed).

    `Related Pages <https://www.w3schools.com/Jsref/prop_win_sessionstorage.asp>`_
    """

    def key(self, i: Union[primitives.JsDataModel, int]):
        """The sessionStorage object stores data for only one session (the data is deleted when the browser tab is closed).

        :param i: The key number.
        """
        i = JsUtils.jsConvertData(i, None)
        return JsObject.JsObject("sessionStorage.key(%s)" % i)

    def __setitem__(self, key: str, data):
        """

        :param key: The key attribute
        :param: Object. The value to store
        """
        self.setItem(key, data)

    def __getitem__(self, item):
        """Python wrapper to getItem.

        Usage::

          jsObj.console.log(jsObj.sessionStorage["lastname"])

        :param item:
        """
        return self.getItem(item)

    def setItem(self, key: Union[primitives.JsDataModel, str], data: Any, force_json: bool = True):
        """Syntax for SAVING data to sessionStorage.

        The sessionStorage object stores data for only one session (the data is deleted when the browser tab is closed).

        Usage::

          jsObj.sessionStorage.setItem("lastname", "Smith")
          jsObj.sessionStorage.setItem("lastname", jsObj.objects.get("bin")),

        `Related Pages <https://www.w3schools.com/Jsref/prop_win_sessionstorage.asp>`_

        :param key: The key used to store the data in the session cache.
        :param data: The cache value
        :param force_json: Change the value object to a JSon string
        """
        key = JsUtils.jsConvertData(key, None)
        data = JsUtils.jsConvertData(data, None)
        if force_json:
            return JsObject.JsObject("sessionStorage.setItem(%s, JSON.stringify(%s))" % (key, data))

        return JsObject.JsObject("sessionStorage.setItem(%s, %s)" % (key, data))

    def getItem(self, key: Union[primitives.JsDataModel, str], force_json: bool = True):
        """Syntax for READING data from sessionStorage

        The sessionStorage object stores data for only one session (the data is deleted when the browser tab is closed).

        Usage::

          jsObj.sessionStorage.getItem("lastname")
          jsObj.console.log(jsObj.sessionStorage.getItem("lastname"))

        :param key: The cache key
        :param force_json: Change the value json string to a javascript object
        """
        key = JsUtils.jsConvertData(key, None)
        if force_json:
            return JsObject.JsObject("JSON.parse(sessionStorage.getItem(%s))" % key)

        return JsObject.JsObject("sessionStorage.getItem(%s)" % key)

    def removeItem(self, data, key: Union[str, primitives.JsDataModel] = None, is_py_data: bool = False,
                   js_funcs: Union[list, str] = None):
        """Syntax for REMOVING ALL saved data from sessionStorage.

        The sessionStorage object stores data for only one session (the data is deleted when the browser tab is closed).

        Usage::

          jsObj.sessionStorage.removeItem("lastname")

        `Related Pages <https://www.w3schools.com/jsref/met_storage_removeitem.asp>`_

        :param data:
        :param key: Optional.
        :param is_py_data: Optional.
        :param js_funcs: Optional.
        """
        data = JsUtils.jsConvert(data, key, is_py_data, js_funcs)
        return JsFncs.JsFunction("sessionStorage.removeItem(%s)" % data)

    def clear(self):
        """Syntax for REMOVING ALL saved data from sessionStorage

        The sessionStorage object stores data for only one session (the data is deleted when the browser tab is closed).

        Related Pages:

          https://www.w3schools.com/jsref/prop_win_sessionstorage.asp
        """
        return JsFncs.JsFunction("sessionStorage.clear()")


class JsHistory:
    """Interface to the Javascript history module.

    `Related Pages <https://www.w3schools.com/js/js_window_history.asp>`_
    """

    def __init__(self, page: primitives.PageModel):
        self.page = page

    @property
    def length(self):
        """The length property returns the number of URLs in the history list of the current browser window.

        Usage::

          rptObj.js.window.history.length

        `Related Pages <https://www.w3schools.com/jsref/prop_his_length.asp>`_

        :return: A Number, representing the number of entries in the session history
        """
        return JsNumber.JsNumber("history.length", is_py_data=False)

    def back(self):
        """The back() method loads the previous URL in the history list.

        Usage::

          rptObj.js.window.history.back()

        `Related Pages <https://www.w3schools.com/jsref/met_his_back.asp>`_

        :return: The Javascript String to be added to the page
        """
        return JsFncs.JsFunction("window.history.back()")

    def forward(self):
        """The forward() method loads the next URL in the history list.

        `Related Pages <https://www.w3schools.com/jsref/met_his_forward.asp>`_

        :return: The Javascript String to be added to the page.
        """
        return JsFncs.JsFunction("window.history.forward()")

    def go(self, number: Union[primitives.JsDataModel, int]):
        """The go() method loads a specific URL from the history list.

        `Related Pages <https://www.w3schools.com/jsref/met_his_go.aspp>`_

        :param number: The parameter can either be a number which goes to the URL within
            the specific position (-1 goes back one page, 1 goes forward one page), or a string.

        :return: The Javascript String to be added to the page
        """
        return JsFncs.JsFunction("window.history.go(%s)" % number)

    def pushState(self, state, title, url):
        """Pushes the given data onto the session history stack with the specified title and, if provided, URL.

        Note that pushState() never causes a hashchange event to be fired, even if the new URL differs from the old URL
        only in its hash

        `Related Pages <https://developer.mozilla.org/en-US/docs/Web/API/History_API>`_

        :param state: The state object is a JavaScript object which is associated with the new history entry created by
          pushState()
        :param title: Firefox currently ignores this parameter, although it may use it in the future
                      Passing the empty string here should be safe against future changes to the method.
                      Alternatively, you could pass a short title for the state to which you're moving.
        :param url: The new history entry's URL is given by this parameter.
                    Note that the browser won't attempt to load this URL after a call to pushState(),
        """
        return JsFncs.JsFunction("window.history.pushState('%s', '%s', %s)" % (state, title, url))

    def replaceState(self, state, title, url):
        """history.replaceState() operates exactly like history.pushState() except that replaceState() modifies the
        current history entry instead of creating a new one.

        `Related Pages <https://developer.mozilla.org/en-US/docs/Web/API/History_API>`_

        :param state: The state object is a JavaScript object which is associated with the new history entry created by
          pushState()
        :param title: Firefox currently ignores this parameter, although it may use it in the future
                      Passing the empty string here should be safe against future changes to the method.
                      Alternatively, you could pass a short title for the state to which you're moving.
        :param url: The new history entry's URL is given by this parameter.
                    Note that the browser won't attempt to load this URL after a call to pushState(),
        """
        return JsFncs.JsFunction("window.history.replaceState('%s', '%s', %s)" % (state, title, url))

    def updateState(self, key: str, val: str):
        """Wrapper function

        This function is a simple wrapping function on top of the pushState history method.
        The purpose of this method is to make easier the update of the url whenever a component in the framework is updated.

        Usage::

          component.js.window.history.updateState(self.htmlCode, self.val)

        `Related Pages <https://developer.mozilla.org/en-US/docs/Web/API/History_API>`_

        :param key: The key to be added or updated in the current URL
        :param val: The value to be changed to the current URL

        :return: The Javascript String for the method.
        """
        self.page.js.registerFunction("updateUrl", [
            self.page.js.objects.new([], js_code="newPmts"),
            self.page.js.location.search.substr(1).split("&").forEach([
                self.page.js.if_(
                    self.page.js.data.loop().val.toString(explicit=False).includes("=", js_obj=self.page.js), [
                        self.page.js.objects.array.new(self.page.js.data.loop().val.toString().split("="),
                                                       js_code="urlPmts"),
                        self.page.js.objects.array.get("urlPmts")[0].toString(),
                        self.page.js.objects.get("newPmts").addItem(
                            self.page.js.objects.array.get("urlPmts")[0], self.page.js.objects.array.get("urlPmts")[1])
                    ])
            ]),

            self.page.js.objects.get("newPmts").addItem(
                self.page.js.objects.get("urlKey"), self.page.js.objects.get("urlValue")),
            # Then we concatenate the URL
            self.page.js.objects.array.new([], js_code="pmts"),
            self.page.js.objects.get("newPmts").entries().forEach([
                self.page.js.objects.array.get("pmts").push(
                    self.page.js.data.loop().val[0].toString(explicit=False).add("=").add(
                        self.page.js.data.loop().val[1]))
            ]),
            self.page.js.return_(
                self.page.js.location.origin + self.page.js.location.pathname + "?" + self.page.js.objects.array.get(
                    "pmts").join("&"))
        ], ["urlKey", "urlValue"])
        return self.pushState("data", "", JsFncs.JsFunction("updateUrl(%s, %s)" % (
            JsUtils.jsConvertData(key, None), JsUtils.jsConvertData(val, None))))

    def updateStateFromComponent(self, component: primitives.HtmlModel):
        """Add or update the url value for the specific component to keep them in case of refresh.

        Usage::

          dt = page.ui.date(html_code="date")
          input = page.ui.input(html_code="input")
          dt.select([
            page.js.window.history.updateStateFromComponent(dt),
            page.js.window.history.updateStateFromComponent(input)

        :param component: The HTML component
        """
        return self.updateState(component.htmlCode, component.dom.content)

    def cleanState(self, keys: List[str]):
        """Remove all attributes which are not useful or should not be passed.

        Usage::

          btn = page.ui.button("Clean URL")
          btn.click([page.js.window.history.cleanState(["date"])])

        :param keys: The attributes keys
        """
        self.page.js.registerFunction("restrictUrl", [
            self.page.js.objects.new([], js_code="newPmts"),
            self.page.js.location.search.substr(1).split("&").forEach([
                self.page.js.if_(
                    self.page.js.data.loop().val.toString(explicit=False).includes("=", js_obj=self.page.js), [
                        self.page.js.objects.array.new(self.page.js.data.loop().val.toString().split("="),
                                                       js_code="urlPmts"),
                        self.page.js.if_(self.page.js.objects.array.get("urlKeys").includes(
                            self.page.js.objects.array.get("urlPmts")[0].toString()), [
                                             self.page.js.objects.get("newPmts").addItem(
                                                 self.page.js.objects.array.get("urlPmts")[0],
                                                 self.page.js.objects.array.get("urlPmts")[1])
                                         ])
                    ])
            ]),

            # Then we concatenate the URL
            self.page.js.objects.array.new([], js_code="pmts"),
            self.page.js.objects.get("newPmts").entries().forEach([
                self.page.js.objects.array.get("pmts").push(
                    self.page.js.data.loop().val[0].toString(explicit=False).add("=").add(
                        self.page.js.data.loop().val[1]))
            ]),
            # Returns the new URL
            self.page.js.return_(
                self.page.js.location.origin + self.page.js.location.pathname + "?" + self.page.js.objects.array.get(
                    "pmts").join("&"))
        ], ["urlKeys"])
        return self.pushState("data", "", JsFncs.JsFunction("restrictUrl(%s)" % (
            JsUtils.jsConvertData(keys, None))))

    def deleteState(self, key: primitives.JsDataModel):
        """Remove a specific attribute from the url

        Usage::

          btn = page.ui.button("Remove from URL")
          btn.click([page.js.window.history.deleteState("date")])

        :param key: The attribute key
        """
        self.page.js.registerFunction("deleteFromUrl", [
            self.page.js.objects.new([], js_code="newPmts"),
            self.page.js.location.search.substr(1).split("&").forEach([
                self.page.js.if_(
                    self.page.js.data.loop().val.toString(explicit=False).includes("=", js_obj=self.page.js), [
                        self.page.js.objects.array.new(self.page.js.data.loop().val.toString().split("="),
                                                       js_code="urlPmts"),
                        self.page.js.if_(
                            self.page.js.objects.get("urlKey").toString() != self.page.js.objects.array.get("urlPmts")[
                                0].toString(), [
                                self.page.js.objects.get("newPmts").addItem(
                                    self.page.js.objects.array.get("urlPmts")[0],
                                    self.page.js.objects.array.get("urlPmts")[1])
                            ])
                    ])
            ]),

            # Then we concatenate the URL
            self.page.js.objects.array.new([], js_code="pmts"),
            self.page.js.objects.get("newPmts").entries().forEach([
                self.page.js.objects.array.get("pmts").push(
                    self.page.js.data.loop().val[0].toString(explicit=False).add("=").add(
                        self.page.js.data.loop().val[1]))
            ]),
            # Returns the new URL
            self.page.js.return_(
                self.page.js.location.origin + self.page.js.location.pathname + "?" + self.page.js.objects.array.get(
                    "pmts").join("&"))
        ], ["urlKey"])
        return self.pushState("data", "", JsFncs.JsFunction("deleteFromUrl(%s)" % (
            JsUtils.jsConvertData(key, None))))


class JsWindowEvent:

    def addEventListener(self, event_type: Union[primitives.JsDataModel, str], js_funcs: Union[list, str],
                         window_id: str = "window", sub_events: list = None,
                         profile: Optional[Union[dict, bool]] = False):
        """

        :param event_type:
        :param js_funcs: The PyJs functions
        :param window_id: The window object reference
        :param sub_events: List of names you want your underlying function to have as arguments
        :param profile: Optional. A flag to set the component performance storage
        """
        sub_events = '' if not sub_events else ','.join(sub_events)
        event_type = JsUtils.jsConvertData(event_type, None)
        js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
        return JsFncs.JsFunction(
            "%s.addEventListener(%s, function(%s){%s})" % (window_id, event_type, sub_events, js_funcs))

    def addScrollListener(self, js_funcs: Union[list, str], window_id: str = "window"):
        """

        :param js_funcs: The PyJs functions
        :param window_id: The window object reference
        """
        return self.addEventListener("scroll", js_funcs, window_id)

    def addContentLoaded(self, js_funcs: Union[list, str], window_id: str = "window"):
        """The DOMContentLoaded event fires when the initial HTML document has been completely loaded and parsed,
        without waiting for stylesheets, images, and subframes to finish loading.

        Usage::

          page.js.addOnLoad(
          page.js.window.events.addContentLoaded(rptObj.js.alert("DOM fully loaded and parsed")))

        `Related Pages <https://developer.mozilla.org/en-US/docs/Web/API/Window/DOMContentLoaded_event>`_

        :param js_funcs: The PyJs functions
        :param window_id: Optional. The window object reference
        """
        return self.addEventListener("DOMContentLoaded", js_funcs, window_id)

    def addClickListener(self, js_funcs: Union[list, str], window_id: str = "window", sub_events: list = None):
        """

        :param js_funcs: The PyJs functions
        :param window_id: Optional. The window object reference
        :param sub_events: Optional.
        """
        return self.addEventListener("click", js_funcs, window_id, sub_events)


class JsWindow:
    """The window object represents an open window in a browser.

    If a document contain frames (<iframe> tags), the browser creates one window object for the HTML document,
    and one additional window object for each frame.

    `Related Pages <https://www.w3schools.com/Jsref/obj_window.asp>`_
    """

    @property
    def scrollY(self, window_id: str = "window"):
        """The read-only scrollY property of the Window interface returns the number of pixels that the document is
        currently scrolled vertically.

        `Related Pages <https://developer.mozilla.org/en-US/docs/Web/API/Window/scrollY>`_

        :param window_id: Optional. The window reference.
        """
        return JsNumber.JsNumber("%s.scrollY" % window_id)

    @property
    def innerHeight(self, window_id: str = "window"):
        """
        The innerHeight property returns the height of a window's content area.

        `Related Pages <https://www.w3schools.com/jsref/prop_win_innerheight.asp>`_

        :param window_id: Optional. The window reference
        """
        return JsNumber.JsNumber("%s.innerHeight" % window_id)

    @property
    def scrollEndPage(self, window_id: str = "window"):
        """The scrollEndPage property indicates if the page is scrolled to the end.

        :param window_id: Optional. The window reference
        """
        return JsBoolean.JsBoolean("(%s.scrollY + %s.innerHeight > document.body.clientHeight)? true: false" % (
            window_id, window_id), is_py_data=False)

    @property
    def scrollPercentage(self, window_id: str = "window"):
        """The scrollPercentage property return the percentage of the page scrolled.

        :param window_id: Optional. The window reference
        """
        return JsNumber.JsNumber(
            "Math.min((%s.scrollY + %s.innerHeight)/ document.body.clientHeight * 100, 100)" % (
                window_id, window_id), is_py_data=False)

    @property
    def scrollMaxY(self, window_id: str = "window"):
        """The Window.scrollMaxY read-only property returns the maximum number of pixels that the document can be
        scrolled vertically.

        `Related Pages <https://developer.mozilla.org/en-US/docs/Web/API/Window/scrollMaxY>`_

        :param window_id: Optional. The window reference
        """
        return JsNumber.JsNumber(
            "(%s.scrollMaxY || (document.documentElement.scrollHeight - document.documentElement.clientHeight))" % window_id)

    def __init__(self, page: primitives.PageModel = None):
        """

        :param page: Optional.
        """
        self.page = page
        self._context = page._context if hasattr(page, '_context') else {}

    @property
    def document(self):
        """Interface to the DOM object on the current window.

        :return: A Python JsDoms object wrapping the DOM Js interface.
        """
        return JsNodeDom.JsDoms(self.page)

    @property
    def history(self) -> JsHistory:
        """Interface to the History object.

        Usage::

          dt = page.ui.date(html_code="date")
          input = page.ui.input(html_code="input")
          dt.select([
            page.js.window.history.updateStateFromComponent(dt),
            page.js.window.history.updateStateFromComponent(input)

        :return: A Python Js History object.
        """
        return JsHistory(self.page)

    def close(self, window_id: str = "window"):
        """Closes the current window.

        `Related Pages <https://www.w3schools.com/jsref/met_win_close.asp>`_

        :param window_id: Optional. The JavaScript window object reference variable

        :return: The String representing the Javascript function.
        """
        return JsFncs.JsFunction("%s.close()" % window_id)

    @property
    def events(self):
        """Property to all the events."""
        return JsWindowEvent()

    def addEventListener(self, event_type: Union[primitives.JsDataModel, str],
                         js_funcs: Union[primitives.JsDataModel, str],
                         window_id: str = "window", profile: Optional[Union[dict, bool]] = False):
        """The addEventListener() method attaches an event handler to an element.

        `w3schools <https://www.w3schools.com/jsref/met_element_addeventlistener.asp>`_

        :param event_type: The JavaScript event handler
        :param js_funcs: The Javascript functions
        :param window_id: Optional. The JavaScript window object reference variable
        :param profile: Optional. A flag to set the component performance storage
        """
        event_type = JsUtils.jsConvertData(event_type, None)
        js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
        return JsFncs.JsFunction("%s.addEventListener(%s, function(){%s})" % (window_id, event_type, js_funcs))

    def open(self, url: str, name: str = "_self", specs: list = None, replace: bool = None, window_id: str = "window"):
        """Opens a new browser window.

        `Related Pages <https://www.w3schools.com/Jsref/met_win_open.asp>`_

        :param url: Optional. Specifies the URL of the page to open. If no URL is specified, a new window/tab with
          about:blank is opened
        :param name: Optional. Specifies the target attribute or the name of the window
        :param specs: Optional. A comma-separated list of items, no whitespaces
        :param replace: Optional. Specifies whether the URL creates a new entry or replaces the current entry in
          the history list
        :param window_id: Optional. The JavaScript window object reference variable
        """
        url = JsUtils.jsConvertData(url, None)
        name = JsUtils.jsConvertData(name, None)
        specs = JsUtils.jsConvertData(specs, None)
        replace = JsUtils.jsConvertData(replace, None)
        return JsFncs.JsFunction("%s.open(%s, %s, %s, %s)" % (window_id, url, name, specs, replace))

    def postData(self, data):
        """

        :param data:
        """
        if not isinstance(data, list):
            data = [data]

    def download(self, data, file_name: str, profile: Optional[Union[dict, bool]] = False):
        """Download the data from a flat file.

        Usage::

          page.js.window.download(rptObj.js.window.btoa(rptObj.js.objects.get("test")), fileName="test.txt")

        :param data:
        :param file_name:
        :param profile: Optional. A flag to set the component performance storage

        :return: Void,
        """
        data = JsUtils.jsConvertData(data, None)
        return JsFncs.JsFunction(JsUtils.jsConvertFncs([
            self.page.js.createElement("a", js_code="a_temp").setAttribute("download", file_name).setAttribute(
                "href", JsFncs.JsFunction("'data:text/csv;base64,'+ %s" % data)),
            self.page.js.body.appendChild(self.page.js.objects.get("a_temp")),
            self.page.js.objects.dom.get("a_temp").click(),
            # self.__src.objects.dom.get("a_temp").remove()
        ], toStr=True, profile=profile))
        # return JsFncs.JsFunction("%s.open('data:text/csv;base64,'+ %s, '_self')" % (windowId, data))

    def moveBy(self, x: int, y: int, window_id: str = "window"):
        """The moveBy() method moves a window a specified number of pixels relative to its current coordinates.

        `Related Pages <https://www.w3schools.com/Jsref/met_win_moveby.asp>`_

        :param x: The horizontal move in pixel
        :param y: The vertical move in pixel
        :param window_id: Optional. The JavaScript window object reference variable
        """
        x = JsUtils.jsConvertData(x, None)
        y = JsUtils.jsConvertData(y, None)
        return JsFncs.JsFunction("%s.moveBy(%s, %s)" % (window_id, x, y))

    def focus(self, window_id: str = "window"):
        """The focus() method sets focus to the current window

        `Related Pages <https://www.w3schools.com/Jsref/met_win_focus.asp>`_

        :param window_id: Optional. The JavaScript window object reference variable

        :return: Void, The Javascript String
        """
        return JsFncs.JsFunction("%s.focus()" % window_id)

    def scroll(self, x: int, y: int, window_id: str = "window"):
        """The Window.scroll() method scrolls the window to a particular place in the document.

        `Related Pages <https://developer.mozilla.org/uk/docs/Web/API/Window/scroll>`_

        :param x: The pixel along the horizontal axis of the document that you want displayed in the upper left
        :param y: The pixel along the vertical axis of the document that you want displayed in the upper left
        :param window_id: Optional. The JavaScript window object reference variable
        """
        return JsFncs.JsFunction("%s.scroll(%s, %s)" % (window_id, x, y))

    def scrollTo(self, x: int = None, y: int = None, window_id: str = "window"):
        """The window.scrollTo() go to a particular point.

        :param x: Optional.
        :param y: Optional.
        :param window_id: Optional. The JavaScript window object reference variable
        """
        y = y or "document.body.scrollHeight"
        x = x or "document.body.scrollWidth"
        return JsFncs.JsFunction("%s.scrollTo(%s, %s)" % (window_id, x, y))

    def scrollUp(self, window_id: str = "window"):
        """

        :param window_id: Optional. The JavaScript window object reference variable
        """
        return JsFncs.JsFunction("%s.scrollTo(0, 0)" % window_id)

    def print_(self, window_id: str = "window"):
        """Prints the content of the current window.

        Related Pages:

          https://www.w3schools.com/Jsref/met_win_print.asp

        :param window_id: Optional. The JavaScript window object reference variable

        :return: Void, The Javascript String
        """
        return JsFncs.JsFunction("%s.print()" % window_id)

    def alert(self, data, js_funcs: Union[list, str] = None, window_id: str = "window",
              skip_data_convert: bool = False):
        """The alert() method displays an alert box with a specified message and an OK button.

        Usage::

          page.js.window.alert("Test")
          page.js.alert("Test 2")

        `Related Pages <https://www.w3schools.com/jsref/met_win_alert.asp>`_

        :param data: Specifies the text to display in the alert box, or an object converted into a string and displayed
        :param js_funcs: Optional. A JsFnc or a list of JsFncs
        :param window_id: Optional. The JavaScript window object reference variable
        :param skip_data_convert: Optional.
        """
        if skip_data_convert:
            return JsFncs.JsFunction("%s.alert(%s)" % (window_id, data))

        if hasattr(data, 'dom'):
            data = data.dom.content
        return JsFncs.JsFunction("%s.alert(%s)" % (window_id, JsUtils.jsConvertData(data, js_funcs)))

    def atob(self, data: Union[str, primitives.JsDataModel], js_funcs: Union[list, str] = None,
             window_id: str = "window"):
        """Decodes a base-64 encoded string.

        Usage::

          jsObj.window.btoa("Test").setVar("bin")
          jsObj.window.atob(jsObj.objects.get("bin"))

        `Related Pages <https://www.w3schools.com/jsref/met_win_atob.asp>`_

        :param data: The string which has been encoded by the btoa() method
        :param js_funcs: Optional. A JsFnc or a list of JsFncs
        :param window_id: Optional. The JavaScript window object reference variable
        """
        return JsFncs.JsFunction("%s.atob(%s)" % (window_id, JsUtils.jsConvertData(data, js_funcs)))

    def btoa(self, data: Union[str, primitives.JsDataModel], js_funcs: Union[list, str] = None,
             window_id: str = "window"):
        """Encodes a string in base-64.

        Usage::

          jsObj.window.btoa("Test").setVar("bin")

        `Related Pages h<ttps://www.w3schools.com/jsref/met_win_btoa.asp>`_

        :param data: Required. The string to be encoded
        :param js_funcs: Optional. The PyJs functions
        :param window_id: Optional. The JavaScript window object reference variable
        """
        return JsObject.JsObject("%s.btoa(%s)" % (window_id, JsUtils.jsConvertData(data, js_funcs)), is_py_data=False)

    def setInterval(self, js_funcs: Union[list, str], var_id: str, milliseconds: int, window_id: str = "window",
                    set_var: bool = True, profile=False, run_on_start: bool = False):
        """The setInterval() method calls a function or evaluates an expression at specified intervals (in milliseconds).

        The setInterval() method will continue calling the function until clearInterval() is called, or the window
        is closed.
        #TODO: Add a control on setInterval to only have one created

        Usage::

          jsObj.window.setInterval([jsObj.console.log(jsObj.math.random())], 5000)

        `Related Pages <https://www.w3schools.com/jsref/met_win_setinterval.asp>`_

        :param js_funcs: The function that will be executed
        :param var_id: The JavaScript variable name
        :param milliseconds: The intervals (in milliseconds) on how often to execute the code.
            If the value is less than 10, the value 10 is used
        :param window_id: Optional. The JavaScript window object
        :param set_var: Optional. Set the variable on the JavaScript side
        :param profile: Optional. A flag to set the component performance storage
        :param run_on_start: Optional. Flag to start the call at the start
        """
        js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
        if set_var:
            if window_id == 'window':
                # To make the variable scope as global
                var_id = "window['%s']" % var_id
            else:
                var_id = "var %s" % var_id
            if run_on_start:
                return JsFncs.JsFunction(
                    "%s; %s = %s.setInterval(function(){%s}, %s)" % (
                        JsUtils.jsConvertFncs(js_funcs, toStr=True), var_id, window_id, js_funcs, milliseconds))

            return JsFncs.JsFunction(
                "%s = %s.setInterval(function(){%s}, %s)" % (var_id, window_id, js_funcs, milliseconds))

        if run_on_start:
            return JsFncs.JsFunction("%s; %s.setInterval(function(){%s}, %s)" % (
                JsUtils.jsConvertFncs(js_funcs, toStr=True), window_id, js_funcs, milliseconds))

        return JsFncs.JsFunction("%s.setInterval(function(){%s}, %s)" % (window_id, js_funcs, milliseconds))

    def clearInterval(self, var_id: str, window_id: str = "window"):
        """The clearInterval() method clears a timer set with the setInterval() method.

        The ID value returned by setInterval() is used as the parameter for the clearInterval() method.
        #TODO: Check if interval is unique

        Usage::

          jsObj.window.setInterval([jsObj.console.log(jsObj.math.random())], 500).setVar("interva1"),
          jsObj.window.clearInterval(jsObj.objects.get("interva1"))

        `Related Pages <https://www.w3schools.com/jsref/met_win_clearinterval.asp>`_

        :param var_id: A PythonJs object (JsArray, JsObject...) or reference
        :param window_id: Optional. The JavaScript window object

        :return: Void, The Javascript String
        """
        js_data = var_id if not hasattr(var_id, "toStr") else JsUtils.jsConvertData(var_id, None)
        return JsFncs.JsFunction("%s.clearInterval(%s); %s = undefined" % (window_id, js_data, js_data))

    def toggleInterval(self, js_funcs: Union[list, str], var_id: str, milliseconds, window_id: str = "window"):
        """

        Usage::

          page.ui.button("Interval Toggle").click([
            page.js.window.toggleInterval(rptObj.js.console.log('Print called'), 'test', 400)])

        :param js_funcs: The PyJs functions
        :param var_id: A PythonJs object (JsArray, JsObject...) or reference
        :param milliseconds: The number of milliseconds to wait before executing the code
        :param window_id: Optional. The JavaScript window object
        """
        interval = self.setInterval(js_funcs, var_id, milliseconds, window_id, set_var=False)
        clear = self.clearInterval(var_id, window_id)
        return JsFncs.JsFunction("if(%s){%s = %s} else{%s}" % (JsUtils.isNotDefined(var_id), var_id, interval, clear))

    def setTimeout(self, js_funcs: Union[list, str], milliseconds: int = 0, window_id: str = "window",
                   profile: Optional[Union[dict, bool]] = False):
        """The setTimeout() method calls a function or evaluates an expression after a specified number of milliseconds.

        `Related Pages <https://www.w3schools.com/jsref/met_win_settimeout.asp>`_

        :param js_funcs: The function that will be executed
        :param milliseconds: Optional. The number of milliseconds to wait before executing the code
        :param window_id: Optional. The JavaScript window object
        :param profile: Optional. Set to true to get the profile for the function on the Javascript console
        """
        return JsObject.JsObject(
            "%s.setTimeout(function(){%s}, %s)" % (
                window_id, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile), milliseconds),
            set_var=True, is_py_data=False)

    def clearTimeout(self, data, js_funcs: Union[list, str] = None, window_id: str = "window"):
        """The clearTimeout() method clears a timer set with the setTimeout() method.
        The ID value returned by setTimeout() is used as the parameter for the clearTimeout() method.

        `Related Pages <https://www.w3schools.com/jsref/met_win_cleartimeout.asp>`_

        :param data:
        :param js_funcs: Optional. The PyJs functions
        :param window_id: Optional. The JavaScript window object
        """
        return JsFncs.JsFunction("%s.clearTimeout(%s)" % (window_id, JsUtils.jsConvertData(data, js_funcs)))

    def getComputedStyle(self, element, pseudo_element=None, window_id: str = "window"):
        """The getComputedStyle() method gets all the actual (computed) CSS property and values of the specified element.

        `Related Pages <https://www.w3schools.com/jsref/jsref_getcomputedstyle.asp>`_

        :param element: The element to get the computed style for
        :param pseudo_element: Optional.
        :param window_id: Optional. The JavaScript window object.

        :return: A CSSStyleDeclaration object containing CSS declaration block of the element
        """
        if pseudo_element is None:
            return JsFncs.JsFunction("%s.getComputedStyle(%s)" % (window_id, element))

        return JsFncs.JsFunction("%s.getComputedStyle(%s, %s)" % (window_id, element, pseudo_element))

    def getPropertyValue(self, name, element_id: str = ":root", pseudo_element=None, window_id: str = "window"):
        """Set value for a given style attribute for DOM component on the page.

        `W3School <https://www.w3schools.com/css/css3_variables_javascript.asp>`_

        :param name: CSS Style attribute
        :param element_id: Optional. Component ID on the page. Default :root
        :param window_id: Optional. The JavaScript window object.
        """
        name = JsUtils.jsConvertData(name, None)
        element_id = JsUtils.jsConvertData(element_id, None)
        return JsUtils.jsWrap("%s.getPropertyValue(%s)" % (
            self.getComputedStyle(JsNodeDom.JsDoms("document").querySelector(element_id), pseudo_element, window_id=window_id).toStr(), name))

    def setProperties(self, values, element_id: str = ":root") -> JsObject.JsObject:
        """Set style properties for a specific DOM component to the page.

        `W3School <https://www.w3schools.com/css/css3_variables_javascript.asp>`_

        :param values: Js or Python dictionary of values to set
        :param element_id: Optional. Component ID on the page. Default :root
        """
        element_id = JsUtils.jsConvertData(element_id, None)
        return JsNodeDom.JsDoms("document").querySelector(element_id).setProperties(values)

    def getSelection(self, window_id: str = "window"):
        """Returns a Selection object representing the range of text selected by the user.

        :param window_id: Optional. The JavaScript window object
        """
        return JsFncs.JsFunction("%s.getSelection()" % window_id)

    def getVar(self, var_id: str, window_id: str = "window"):
        """Get the Javascript Variable name.

        :param var_id: The Variable name
        :param window_id: Optional. The JavaScript window object

        :return: Return the piece of script to be added to the Javascript.
        """
        return "%s['%s']" % (window_id, var_id)

    def onPageShow(self, js_funcs: Union[list, str]):
        """

        :param js_funcs: The PyJs functions
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self._context.setdefault('pageshow', []).extend(js_funcs)

    def onBeforeUnload(self, js_funcs: Union[list, str]):
        """

        :param js_funcs: A JsFnc or a list of JsFncs
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self._context.setdefault('beforeunload', []).extend(js_funcs)

    def location(self, url: str, window_id: str = "window"):
        """Change the window and open the page specify by the url.

        :param url: The new page url
        :param window_id: Optional. The JavaScript window object
        """
        url = JsUtils.jsConvertData(url, None)
        return JsFncs.JsFunction("%s.location = %s" % (window_id, url))

    @property
    def URL(self):
        """ """
        return JsUrl

    def onOffline(self, js_funcs: Union[primitives.JsDataModel, str], window_id: str = "window",
                  profile: Optional[Union[dict, bool]] = False):
        """The browser starts working offline.

        `Learn more dom event <https://www.w3schools.com/jsref/dom_obj_event.asp>`_

        :param js_funcs: The Javascript functions
        :param window_id: Optional. The JavaScript window object reference variable
        :param profile: Optional. A flag to set the component performance storage
        """
        return self.addEventListener("offline", js_funcs, window_id, profile)

    def onOnline(self, js_funcs: Union[primitives.JsDataModel, str], window_id: str = "window",
                  profile: Optional[Union[dict, bool]] = False):
        """The browser starts working online.

        `Learn more dom event <https://www.w3schools.com/jsref/dom_obj_event.asp>`_

        :param js_funcs: The Javascript functions
        :param window_id: Optional. The JavaScript window object reference variable
        :param profile: Optional. A flag to set the component performance storage
        """
        return self.addEventListener("online", js_funcs, window_id, profile)

    def onBlur(self, js_funcs: Union[primitives.JsDataModel, str], window_id: str = "window",
                  profile: Optional[Union[dict, bool]] = False):
        """TAn element loses focus.

        `Learn more dom event <https://www.w3schools.com/jsref/dom_obj_event.asp>`_

        :param js_funcs: The Javascript functions
        :param window_id: Optional. The JavaScript window object reference variable
        :param profile: Optional. A flag to set the component performance storage
        """
        return self.addEventListener("blur", js_funcs, window_id, profile)

    def onFocus(self, js_funcs: Union[primitives.JsDataModel, str], window_id: str = "window",
                  profile: Optional[Union[dict, bool]] = False):
        """An element gets focus.

        `Learn more dom event <https://www.w3schools.com/jsref/dom_obj_event.asp>`_

        :param js_funcs: The Javascript functions
        :param window_id: Optional. The JavaScript window object reference variable
        :param profile: Optional. A flag to set the component performance storage
        """
        return self.addEventListener("focus", js_funcs, window_id, profile)
