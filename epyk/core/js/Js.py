#!/usr/bin/python
#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import os
import base64
import logging
from typing import Union, Optional, Any, List, Callable, Tuple
from epyk.core.py import primitives
from epyk.core.py import types

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
from epyk.core.js import JsMediaRecorder
from epyk.core.js import JsSpeechRecognition
from epyk.core.js import JsCacheStorage
from epyk.core.js import treemap

# All the predefined variable types
from epyk.core.js.fncs import JsFncs
from epyk.core.js.fncs import JsFncsSamples
from epyk.core.js.objects import JsData
from epyk.core.js.objects import JsNodeAttributes
from epyk.core.js.objects import JsNodeDom
from epyk.core.js.objects import JsIntersectionObserver
from epyk.core.js.primitives import JsNumber
from epyk.core.js.primitives import JsObject
from epyk.core.js.primitives import JsObjects
from epyk.core.js.primitives import JsString

# All the predefined Javascript Statements
from epyk.core.js.statements import JsIf
from epyk.core.js.statements import JsWhile
from epyk.core.js.statements import JsSwitch
from epyk.core.js.statements import JsFor

_CONSOLE_LOG_EXPR = "console.log({})"


class JsBreadCrumb:

    def __init__(self, src: primitives.PageModel = None):
        self.page = src
        self._selector = "breadcrumb"
        self._anchor = None
        self.page.properties.js.add_builders("%s = {pmts: %s}" % (self._selector, json.dumps(self.page.inputs)))

    def add(self, key: str, data: Union[str, primitives.JsDataModel], js_conv_func: Optional[Union[str, list]] = None):
        """
        Add an entry to the Javascript breadcrumb dictionary.

        :param key: The key in the Breadcrumb dictionary
        :param data: A String corresponding to a JavaScript object
        :param js_conv_func: Optional. A specific JavaScript data conversion function
        """
        return JsFncs.JsFunction('%s["pmts"]["%s"] = %s' % (
            self._selector, key, JsUtils.jsConvertData(data, js_conv_func)))

    def get(self, key: Optional[str] = None):
        """
        Returns the object stored in the breadcrumb dictionary.

        :param key: Optional. The key in the Breadcrumb dictionary

        :return: A Python object.
        """
        if key is None:
            return JsObject.JsObject("%s" % self._selector)

        return JsObject.JsObject('%s["pmts"]["%s"]' % (self._selector, key))

    def hash(self, data: Union[str, primitives.JsDataModel], js_conv_func: Optional[Union[str, list]] = None):
        """
        Add an anchor to the URL after the hashtag.

        `Related Pages <https://www.w3schools.com/jsref/prop_loc_hash.>`_

        :param data: A String corresponding to a JavaScript object
        :param js_conv_func: Optional. A specific JavaScript data conversion function
        """
        return JsObject.JsObject('{}["anchor"] = {}'.format(self._selector, JsUtils.jsConvertData(data, js_conv_func)))

    @property
    def url(self):
        """ Get the full URL. """
        js_location = JsLocation.JsLocation(self.page)
        origin = js_location.origin
        pathname = js_location.pathname
        return JsString.JsString(origin + pathname + "?" + JsObject.JsObject(self.toStr(), page=self.page),
                                 js_code="window")

    def toStr(self):
        return '%s(%s)' % (JsFncs.FncOnRecords(None, self.page.properties.js).url(), self._selector)


class JsStorage:

    def __init__(self, js_base):
        self.page = js_base.page
        self.__js , self._caches = js_base, {}

    def name(self, js_code: str, data: Optional[dict] = None,
             components: Optional[Union[Tuple[primitives.HtmlModel, str], List[primitives.HtmlModel]]] = None):
        if (not data and not components) or self.page is None:
            return JsUtils.jsWrap(JsUtils.jsConvertData(js_code, None, force=True))

        if not data:
            dyn_data = []
            for c in components:
                if hasattr(c, "dom"):
                    dyn_data.append(c.dom.content.toStr())
                else:
                    dyn_data.append(self.page.components[c].dom.content.toStr())
            if dyn_data:
                return JsUtils.jsWrap(JsUtils.jsConvertData(js_code, None, force=True) + " + '_' +" +  " + '_' + ".join(dyn_data))

            return JsUtils.jsWrap(JsUtils.jsConvertData(js_code, None, force=True))

        if not components:
            dyn_data = [JsUtils.jsConvertData(v, None, force=True) for v in data.values()]
            if dyn_data:
                return JsUtils.jsWrap(JsUtils.jsConvertData(js_code, None, force=True) + " + '_' +" +  " + '_' + ".join(dyn_data))

            return JsUtils.jsWrap(JsUtils.jsConvertData(js_code, None, force=True))

        dyn_data = []
        for c in components:
            if hasattr(c, "dom"):
                dyn_data.append(c.dom.content.toStr())
            else:
                dyn_data.append(self.page.components[c].dom.content.toStr())
        dyn_data.extend([JsUtils.jsConvertData(v, None, force=True) for v in data.values()])
        if dyn_data:
            return JsUtils.jsWrap(JsUtils.jsConvertData(js_code, None, force=True) + " + '_' +" +  " + '_' + ".join(dyn_data))

        return JsUtils.jsWrap(JsUtils.jsConvertData(js_code, None, force=True))

    def cache(self, js_code: str, value, set_once: bool = False):
        """

        """
        if value is None:
            return self.__js.caches.open("page").match(js_code)

        self.__js.caches.open("page").put(js_code, value)
        return value

    def local(self, js_code: str, value = None, set_once: bool = False, data: Optional[dict] = None,
              components: Optional[Union[Tuple[primitives.HtmlModel, str], List[primitives.HtmlModel]]] = None,
              profile: Optional[Union[dict, bool]] = None) -> JsObjects.JsObject.JsObject:
        """Cache data to the browser local storage (shared between tabs).

        Usage::

            page.js.storage.local("test", {"test": "This is a test"}, set_once=
            {
                "missing": [msg.build("Data set!")],
                "exists": [msg.build("Data already cached!")]
             })

        :param js_code: Variable name and cache key
        :param value: Optional. Cache value
        :param set_once: Optional. Flag or object to set variable only once
        :param data:
        :param components:
        :param profile: Optional. A flag to set the component performance storage
        """
        if value is None:
            code = self.name(js_code, data, components)
            return self.__js.localStorage.getItem(code)

        self._caches[js_code] = "local"
        if set_once:
            if isinstance(set_once, dict):
                if "value" in set_once:
                    return self.undefined(
                        JsUtils.jsConvertData(set_once["value"], None),
                        [self.local(js_code, value, False, data=data, components=components)] + set_once.get("missing", []),
                        set_once.get("exists", []), profile=profile
                    )

                return self.undefined(
                    self.local(js_code, data=data, components=components),
                    [self.local(js_code, value, False)] + set_once.get("missing", []),
                    set_once.get("exists", []), profile=profile
                )

            return self.undefined(
                self.local(js_code, data=data, components=components),
                [self.local(js_code, value, False)], profile=profile)

        code = self.name(js_code, data, components)
        return self.__js.localStorage.setItem(code, value)

    def session(self, js_code: str, value = None, set_once: Union[bool, dict] = False, data: Optional[dict] = None,
                components: Optional[Union[Tuple[primitives.HtmlModel, str], List[primitives.HtmlModel]]] = None,
                profile: Optional[Union[dict, bool]] = None) -> JsObjects.JsObject.JsObject:
        """Cache data to the browser session storage.

        Usage::

            page.js.storage.local("test", inp.dom.content, set_once=
            {
                "value": check.dom.content,
                "missing": [msg.build("Data updated!")],
                "exists": [msg.build("Data already cached (Flag false)!")]
             })

        :param js_code: Variable name and cache key
        :param value: Optional. Cache value
        :param set_once: Optional. Flag or object to set variable only once
        :param profile: Optional. A flag to set the component performance storage
        """
        if value is None:
            return self.__js.sessionStorage.getItem(js_code)

        self._caches[js_code] = "session"
        if set_once:
            if isinstance(set_once, dict):
                if "value" in set_once:
                    return self.undefined(
                        JsUtils.jsConvertData(set_once["value"], None),
                        [self.session(js_code, value, False)] + set_once.get("missing", []),
                        set_once.get("exists", []),
                        profile=profile
                    )

                return self.undefined(
                    self.session(js_code),
                    [self.session(js_code, value, False)] + set_once.get("missing", []),
                    set_once.get("exists", []),
                    profile=profile
                )

            return self.undefined(
                self.local(js_code), [self.local(js_code, value, False)], profile=profile)

        return self.__js.sessionStorage.setItem(js_code, value)

    def global_(self, js_code: str, value = None, set_once: Union[bool, dict] = False, data: Optional[dict] = None,
                components: Optional[Union[Tuple[primitives.HtmlModel, str], List[primitives.HtmlModel]]] = None,
                profile: Optional[Union[dict, bool]] = None):
        """Cache data using a global variable.

        This variable will have a global scope and will be attached to the window properties.

        Usage::

            page.onDOMContentLoaded([
                page.js.storage.global_("test", {"test": "ok"}, set_once=
                {
                    "missing": [msg.build("Data set!")],
                    "exists": [msg.build("Data already cached!")]
                 })
            ])

        :param js_code: Variable name and cache key
        :param value: Optional. Cache value
        :param set_once: Optional. Flag or object to set variable only once
        :param profile: Optional. A flag to set the component performance storage
        """
        if value is None:
            code = JsUtils.jsConvertData(self.name(js_code, data, components), None)
            return JsObjects.JsObject.JsObject.get("window[%s]" % code)

        self._caches[js_code] = "global"
        if set_once:
            if isinstance(set_once, dict):
                if "value" in set_once:
                    return self.undefined(
                        JsUtils.jsConvertData(set_once["value"], None),
                        [self.global_(js_code, value, False)] + set_once.get("missing", []),
                        set_once.get("exists", []),
                        profile=profile
                    )

                return self.undefined(
                    self.global_(js_code),
                    [self.global_(js_code, value, False)] + set_once.get("missing", []),
                    set_once.get("exists", []),
                    profile=profile
                )

            return self.undefined(
                self.global_(js_code), [self.global_(js_code, value, False)], profile=profile)

        value = JsUtils.jsConvertData(value, None)
        code = JsUtils.jsConvertData(self.name(js_code, data, components), None)
        return JsObjects.JsObject.JsObject(value, "window[%s]" % code, set_var=True)

    def undefined(self, var, js_funcs: Union[list, str], js_funcs_exist: Union[list, str] = None,
                  profile: Optional[Union[dict, bool]] = False):
        """Condition on the cached variable.

        This will be used by the various cached options to do a pivot if the set_once option is activated.

        :param var: The variable used as pivot for the if statement
        :param js_funcs: Function if variable not set
        :param js_funcs_exist: Optional. Function if variable already exist
        :param profile: Optional. A flag to set the component performance storage
        """
        if not isinstance(js_funcs_exist, list):
            js_funcs_exist = [js_funcs_exist]
        return self.__js.if_(var, js_funcs_exist + [var], profile=profile).else_(js_funcs, profile=profile)

    def from_config(self, options: dict) -> JsObjects.JsObject.JsObject:
        """Interface to get the right caching setup.

        Possible options:
            code: The variable name
            type: Optional. Caching type. local, session or global
            value: Optional. The value to set (or function to use)
            setOnce: Optional. Enable mechanism to store value. Default False
            profile: Optional. Set the profile to None

        :param js_code: Variable name and cache key
        :param value: Optional. Cache value
        :param set_once: Optional. Flag or object {missing, exists} to set variable only once
        :param profile: Optional. A flag to set the component performance storage
        """
        if options.get("type") == "session":
            return self.session(
                js_code=options["code"], value=options.get("value"), data=options.get("data"),
                components=options.get("components"), set_once=options.get("setOnce", False),
                profile=options.get("profile"))

        if options.get("type") == "local":
            return self.local(
                js_code=options["code"], value=options.get("value"), data=options.get("data"),
                components=options.get("components"), set_once=options.get("setOnce", False),
                profile=options.get("profile"))

        return self.global_(
                js_code=options["code"], value=options.get("value"), data=options.get("data"),
                components=options.get("components"), set_once=options.get("setOnce", False), profile=options.get("profile"))

    def clear(self, js_code: str, type: str = None, data: Optional[dict] = None,
              components: Optional[Union[Tuple[primitives.HtmlModel, str], List[primitives.HtmlModel]]] = None
              ):
        type = type or self._caches.get(js_code)
        code = self.name(js_code, data, components)
        if type == "local":
            return self.__js.localStorage.removeItem(code)

        if type == "session":
            return self.__js.sessionStorage.removeItem(code)

        return JsUtils.jsWrap("delete window[%s]" % JsUtils.jsConvertData(code, None))

    def clear_all(self, js_code: str, type: str = None):
        if type == "local":
            return self.__js.localStorage.clear_all(js_code)

        if type == "session":
            return self.__js.sessionStorage.clear_all(js_code)

        return JsUtils.jsWrap('''Object.keys(window).forEach(function(key){
if (key == %(match)s || key.startsWith(%(match)s + '_')) {console.log(key)}})
''' % {"match": JsUtils.jsConvertData(js_code, None)})


class JsBase:

    def __init__(self, page: Optional[primitives.PageModel] = None, component: Optional[primitives.HtmlModel] = None):
        # The underlying source object is not supposed to be touched in the underlying classes
        self.page = page
        self.component = component
        self.console = JsConsole(self.page)
        self.localStorage = JsWindow.JsLocalStorage()
        self.window = JsWindow.JsWindow(self.page)
        self.performance = JsPerformance.JsPerformance(self.page)
        self.sessionStorage = JsWindow.JsSessionStorage()
        self.json = JsJson()
        self.math = JsMaths.JsMaths()
        self._jquery_ref = None

        # shortcut functions
        self.alert = self.window.alert
        self.log = self.console.log
        self._breadcrumb, self.__data, self.__location = None, None, None
        self.__media_recorder, self.__accounting, self.__storage = None, None, None

    @property
    def storage(self):
        """Data Storage interface"""
        if not self.__storage:
            self.__storage = JsStorage(self)
        return self.__storage

    @property
    def accounting(self):
        """Shortcut to accounting properties.

        `Related Pages <http://openexchangerates.github.io/accounting.js>`_

        Usages::

          page.js.accounting.add_to_imports()

        """
        from epyk.core.js.packages import JsAccounting

        if self.__accounting is None:
            self.__accounting = JsAccounting.Accounting(page=self.page)
        return self.__accounting

    @property
    def viewHeight(self):
        """Return the current View port height visible in the browser. """
        return JsNumber.JsNumber("Math.max(%s, %s)" % (self.documentElement.clientHeight, self.window.innerHeight))

    @property
    def documentElement(self):
        """Document.documentElement returns the Element that is the root element of the document (for example,
        the <html> element for HTML documents).

        `Related Pages <https://developer.mozilla.org/en-US/docs/Web/API/Document/documentElement>`_
        """
        return JsNodeDom.JsDoms.get("document.documentElement")

    @property
    def screen(self):
        """The screen object contains information about the visitor's screen.

        `Related Pages <https://www.w3schools.com/jsref/obj_screen.asp>`_
        """
        return JsScreen()

    @property
    def navigator(self) -> JsNavigator.JsNavigator:
        """The information from the navigator object can often be misleading, and should not be used to detect
        browser versions because:

          - Different browsers can use the same name.
          - The navigator data can be changed by the browser owner.
          - Some browsers misidentify themselves to bypass site tests.
          - Browsers cannot report new operating systems, released later than the browser.
        """
        return JsNavigator.JsNavigator(self.page)

    @property
    def location(self) -> JsLocation.JsLocation:
        """Property to the Javascript Location functions.

        Usage::

          page.ui.text("Test").click([
            page.js.location.open_new_tab(page.js.location.getUrlFromArrays([
              ["AAA", "BBB"], ["111", "222"]], end_line="\r\n"))])

        `Related Pages <https://www.w3schools.com/jsref/obj_location.asp>`_
        """
        if self.__location is None:
            self.__location = JsLocation.JsLocation(self.page)
        return self.__location

    @property
    def mediaRecorder(self) -> JsMediaRecorder.MediaRecorder:
        """The MediaRecorder interface of the MediaStream Recording API provides functionality to easily record media.
        It is created using the MediaRecorder() constructor.

        `Related Pages <https://developer.mozilla.org/en-US/docs/Web/API/MediaRecorder>`_
        """
        if self.__media_recorder is None:
            self.__media_recorder = JsMediaRecorder.MediaRecorder(self.page)
        return self.__media_recorder

    def speechRecognition(self, js_code: str) -> JsSpeechRecognition.SpeechRecognition:
        """The SpeechRecognition interface of the Web Speech API is the controller interface for the recognition service;
        this also handles the SpeechRecognitionEvent sent from the recognition service.

        `Related Pages <https://developer.mozilla.org/en-US/docs/Web/API/SpeechRecognition>`_

        Usage::

          page = pk.Page()
          rec = page.js.speechRecognition("reco")

          test = page.ui.button("Start recording")
          test.click([rec.start()])

          page.ui.input(html_code="test")

          rec.speechend([rec.stop()])
          rec.onresult([pk.js_callback("UpdateComponent(transcript, confidence)"), page.js.console.log("Done")])
          page.body.onReady([page.js.import_js("test_fnc.js", [], self_contained=True), rec])

          # in the module test_fnc.js
          function ProcessData(transcript, confidence){
              console.log(transcript); return (transcript == 'hello')}

          function UpdateComponent(transcript, confidence){
              var expr = transcript.split(" ");
              if (expr[0] === "put"){document.getElementById(expr[3]).value = expr[1]}}

        :param js_code: The variable name for the speech recognition object
        """
        return JsSpeechRecognition.SpeechRecognition(js_code, self.page)

    @property
    def objects(self) -> JsObjects.JsObjects:
        """Interface to the main Javascript Classes and Primitives. """
        return JsObjects.JsObjects(self.page)

    @property
    def jquery(self):
        """jQuery is a fast, small, and feature-rich JavaScript library.

        It makes things like HTML document traversal and manipulation, event handling, animation, and Ajax much simpler
        with an easy-to-use API that works across a multitude of browsers.
        With a combination of versatility and extensibility, jQuery has changed the way that millions of
        people write JavaScript.

        `Related Pages <https://jquery.com/>`_

        Usage::

          btn = page.ui.button("Click")
          btn.js.jquery.on("click", [
            page.js.alert("It works"),
            btn.js.jquery.after('<div style="background-color:yellow"> New div </div>'),
          ])
        """
        from epyk.core.js.packages import JsQuery

        if self.component is not None:
            return JsQuery.JQuery(self.component, js_code=JsQuery.decorate_var("#%s" % self.component.htmlCode),
                                  set_var=False)

        return JsQuery.JQuery(self._jquery_ref)

    @property
    def rxjs(self):
        """Reactive Extensions Library for JavaScript.

        `Related Pages <https://rxjs.dev>`_
        """
        self.page.jsImports.add("rxjs")
        from epyk.core.js.packages import JsRxJs
        return JsRxJs

    @property
    def moment(self):
        """Parse, validate, manipulate, and display dates and times in JavaScript.

        Usage::

          page.js.moment.new("2021-08-05", varName="momentTime"),
          page.js.console.log(page.js.moment.var("momentTime").weekYear(1998)),
          page.js.console.log(page.js.moment.var("momentTime").weekYear()),
          page.js.console.log(page.js.moment.new("2021-08-05")),

        `Website <https://momentjs.com/>`_
        `Related Pages <https://github.com/you-dont-need/You-Dont-Need-Momentjs>`_
        """
        from epyk.core.js.packages import JsMoment

        return JsMoment.Moment(page=self.page)

    def add(self, name: str, sub_folder: str = None, full_path: str = None, required_funcs: List[str] = None):
        is_loaded = JsUtils.addJsResources(
            self.page._props["js"]['constructors'], name, sub_folder=sub_folder, full_path=full_path,
            required_funcs=required_funcs)
        return is_loaded

    def eval(self, data: Union[primitives.JsDataModel, str], js_conv_func: Optional[Union[str, list]] = None):
        """The eval() function evaluates JavaScript code represented as a string.

        Warning: Executing JavaScript from a string is an enormous security risk.
        It is far too easy for a bad actor to run arbitrary code when you use eval(). See Never use eval()!, below.

        `Related Pages <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval>`_

        :param data: Data to be evaluated
        :param js_conv_func: Optional. A specific JavaScript data conversion function
        """
        return JsObject.JsObject("eval(%s)" % JsUtils.jsConvertData(data, js_conv_func))

    def socketio(self, html_code: Optional[str] = None):
        """This object must be created on the Python side.

        The various function will be the one generating the Javascript string.
        This is just a Python wrapper on top of the library.

        `Related Pages <https://www.tutorialspoint.com/socket.io/socket.io_event_handling.htm>`_

        :param html_code: Optional. The WebSocket id (variable name) on the JavaScript side
        """
        from epyk.core.js.packages import JsSocketIO

        return JsSocketIO.SocketIO(html_code, self.page)

    def websocket(self, html_code: Optional[str] = None, secured: bool = False):
        """WebSocket client applications use the WebSocket API to communicate with WebSocket servers
        using the WebSocket protocol.

        `Related Pages <https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications>`_
        `WebSocket <https://javascript.info/websocket>`_

        :param html_code: Optional. The WebSocket id (variable name) on the JavaScript side
        :param secured: Optional. To define the right protocol for the WebSocket connection we or wss
        """
        return JsWebSocket.WebSocket(html_code, self.page, secured)

    def worker(self, html_code: Optional[str] = None, server: bool = False):
        """A web worker is a JavaScript running in the background, without affecting the performance of the page.

        `Related Pages <https://www.w3schools.com/html/html5_webworkers.asp>`_

        :param html_code: Optional. The WebSocket id (variable name) on the JavaScript side
        :param server: Optional. Specify if the page is running on a server
        """
        return JsWebSocket.Worker(html_code, self.page, server)

    def serverSentEvent(self, html_code: Optional[str] = None) -> JsWebSocket.ServerSentEvent:
        """SSE is a native HTML5 feature that allows the server to keep the HTTP connection open and push data
        changes to the client.
        Server-sent Streaming is really ideal for server-push notifications, device monitoring and all other tasks
        that do not require real-time push back from the client.

        `Related Pages <https://medium.com/code-zen/python-generator-and-html-server-sent-events-3cdf14140e56>`_
        `Related Pages <https://www.w3schools.com/html/html5_serversentevents.asp>`_
        `Related Pages <https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events>`_

        :param html_code: The EventSource id (variable name) on the JavaScript side
        """
        return JsWebSocket.ServerSentEvent(html_code, self.page)

    @property
    def d3(self):
        """D3.js is a JavaScript library for manipulating documents based on data.
        D3 helps you bring data to life using HTML, SVG, and CSS.

        D3’s emphasis on web standards gives you the full capabilities of modern browsers without tying yourself to a
        proprietary framework, combining powerful visualization components and a data-driven approach to DOM manipulation.

        `Related Pages <https://d3js.org/>`_
        """
        from epyk.core.js.packages import JsD3
        return JsD3.JsD3(page=self.page, component=self.component)

    def not_(self, data, js_conv_func: Optional[Union[str, list]] = None) -> JsFncs.JsFunction:
        """Add the Symbol (!) for the boolean negation.
        This feature is also available directly to any JsBoolean objects.

        Usage::

          jsObj.not_(jsObj.objects.boolean.get("weekend"))

        `Related Pages <https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Op%C3%A9rateurs/Op%C3%A9rateurs_logiques>`_

        :param data: A String corresponding to a JavaScript object
        :param js_conv_func: Optional. A specific JavaScript data conversion function

        :return: The Javascript fragment string.
        """
        return JsFncs.JsFunction("!%s" % JsUtils.jsConvertData(data, js_conv_func))

    def online(self, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = False):
        return self.if_(self.navigator.onLine, js_funcs, profile)

    def if_(self, condition: Union[str, list, bool], js_funcs: Union[list, str],
            profile: Optional[Union[dict, bool]] = False):
        """Conditional statements are used to perform different actions based on different conditions.

        Usage::

          page.js.if_(icon.icon.dom.content == "fas fa-lock-open cssicon", [
            page.js.console.log(icon.icon.dom.content)])

        `Related Pages <https://www.w3schools.com/js/js_if_else.asp>`_

        :param condition: The Javascript condition. Can be a JsBoolean object
        :param js_funcs: Optional. The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        if isinstance(condition, list):
            condition = "(%s)" % ")||(".join(JsUtils.jsConvertFncs(condition))
        self.__if = JsIf.JsIf(condition, js_funcs, self.page, profile)
        return self.__if

    def while_(self, condition: Union[str, list], js_funcs: Union[list, str], options: Optional[dict] = None,
               profile: Optional[Union[dict, bool]] = False) -> JsWhile.JsWhile:
        """The while loop loops through a block of code as long as a specified condition is true.

        `Related Pages <https://www.w3schools.com/js/js_loop_while.asp>`_

        :param condition: The JavaScript condition
        :param js_funcs: Javascript functions
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        if isinstance(condition, list):
            condition = "(%s)" % ")||(".join(JsUtils.jsConvertFncs(condition))
        self.__while = JsWhile.JsWhile(condition, options, self.page).fncs(js_funcs, profile=profile)
        return self.__while

    def for_(self, js_funcs: Union[list, str] = None, step: int = 1, start: int = 0, end: int = 10,
             options: Optional[dict] = None, profile: Optional[Union[dict, bool]] = False) -> JsFor.JsFor:
        """Shortcut to a for loop.

        Usage::

          js_for = page.js.for_(end=30)
          js_for.fncs([page.js.console.log(js_for.i)])

        `Related Pages <https://www.w3schools.com/js/js_loop_for.asp>`_

        :param js_funcs: Javascript functions
        :param step: Optional. The value to increment. Default 1
        :param start: Optional. The first index in the for loop
        :param end: Optional. The last index in the for loop
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        for_statment = JsFor.JsFor(end, options)
        for_statment.start = start
        for_statment.end = end
        for_statment.step = step
        if js_funcs is None:
            return for_statment

        return for_statment.fncs(js_funcs, profile=profile)

    def return_(self, data: str) -> JsFncs.JsFunction:
        """Javascript return keyword.

        :param data: The Javascript expression
        """
        return JsFncs.JsFunction("return %s" % data)

    def and_(self, *args) -> JsUtils.jsWrap:
        """Create a Javascript and statement. """
        vals = []
        for a in args:
            if hasattr(a, "html_code"):
                vals.append(a.dom.content.toStr())
            else:
                vals.append(JsUtils.jsConvertData(a, None, force=True))
        return JsUtils.jsWrap(" && " .join(vals))

    def or_(self, *args) -> JsUtils.jsWrap:
        """Create a Javascript Or statement. """
        vals = []
        for a in args:
            if hasattr(a, "html_code"):
                vals.append(a.dom.content.toStr())
            else:
                vals.append(JsUtils.jsConvertData(a, None, force=True))
        return JsUtils.jsWrap(" || " .join(vals))

    def switch(self, variable: Union[str, primitives.JsDataModel, primitives.HtmlModel],
               js_conv_func: Optional[Union[str, list]] = None) -> JsSwitch.JsSwitch:
        """switch statement is used to perform different actions based on different conditions.

        `Related Pages <https://www.w3schools.com/js/js_switch.asp>`_

        :param variable: Variable on which we will apply the switch
        :param js_conv_func: Optional. A specific JavaScript data conversion function
        """
        if hasattr(variable, 'dom'):
            variable = variable.dom.content
        variable = JsUtils.jsConvertData(variable, js_conv_func)
        self.__switch = JsSwitch.JsSwitch(variable)
        return self.__switch

    def clipboard(self, data: Union[str, primitives.JsDataModel], js_conv_func: Optional[Union[str, list]] = None):
        """Copy the full URL to rhe clipboard.

        `Related Pages <https://isabelcastillo.com/hidden-input-javascript>`_

        :param data: The Javascript expression
        :param js_conv_func: Optional. A specific JavaScript data conversion function
        """
        return JsFncs.JsFunction('''
var elInput = document.createElement('input'); elInput.setAttribute('type', 'text');
elInput.setAttribute('value', %s); document.body.appendChild(elInput);
document.execCommand('copy', false, elInput.select()); elInput.remove()
''' % JsUtils.jsConvertData(data, js_conv_func))

    def _addImport(self, import_alias: str):
        """Internal function to include an external JavaScript module
        This can only use pre-defined modules. This will fail during the resolution if it does not exist

        :param import_alias: Alias reference of a JavaScript module
        """
        self.page._props.setdefault('js', {}).setdefault('imports', set([])).add(import_alias)
        return self

    @staticmethod
    def typeof(data: str, var_type: Optional[str] = None):
        """The typeof function.

        `Related Pages <https://www.w3schools.com/js/js_datatypes.asp>`_

        :param data: A String corresponding to a JavaScript object
        :param var_type: Optional. The type of object
        """
        if var_type is None:
            return JsObjects.JsBoolean.JsBoolean("typeof %s" % data)

        return JsObjects.JsVoid("typeof %s === '%s'" % (data, var_type))

    def custom(self, data: Union[str, primitives.JsDataModel], key: Optional[str] = None,
               is_py_data: bool = False, js_func: Optional[Union[list, str]] = None):
        """Allow the definition of bespoke javascript strings.

        :param data: A String corresponding to a JavaScript object
        :param key: Optional. A key reference in the JavaScript object
        :param is_py_data: Optional. Specify if the data is in Python and should be jsonify first
        :param js_func: Optional. Javascript functions
        """
        data = JsUtils.jsConvert(data, key, is_py_data, js_func)
        self.page._props.setdefault('js', {}).setdefault('bespoke', []).append(data)

    def customText(self, text: str):
        """Javascript fragment added at the beginning of the page.
        This will be called before any function in the framework.

        :param text: The Javascript fragment

        :return: self to allow the chaining.
        """
        self.page.properties.js.add_text(text)
        return self

    def customFile(self, filename: str, path: Optional[str] = None, module_type: str = "text/javascript",
                   absolute_path: bool = False, requirements: Optional[list] = None,
                   randomize: bool = False, authorize: bool = False):
        """This will load your local javascript file when the report will be built.
        Then you will be able to use the new features in the different Javascript wrappers.

        Usage::

          page.js.customFile("test.js", r"C:\folder")

        :param filename: The filename
        :param path: Optional. The file path
        :param module_type: Optional. The module type
        :param absolute_path: Optional. If path is None this flag will map to the current main path
        :param requirements: Optional. The list of required packages
        :param randomize: Optional. Add random suffix to the module to avoid browser caching
        :param authorize: Optional. Add to the restricted list of packages

        :return: The Js Object to allow the chaining.
        """
        if path is None:
            if absolute_path:
                path = os.getcwd()
            else:
                path = "%s/js" % Imports.STATIC_PATH.replace("\\", "/")
        file_alias = 'local_%s' % filename[:-3].lower()
        self.page.imports.addPackage(file_alias, {
            'version': "", 'req': requirements or [],
            'register': {'alias': 'local_%s' % filename[:-3], 'module': filename[:-3],
                         'npm_path': 'dist/maps/continents/'},
            'modules': [{'script': filename, "path": '', 'type': module_type, 'cdnjs': path, "config": "version=1"}]})
        if file_alias not in self.page.jsImports:
            self.page.jsImports.add(file_alias)
        if authorize:
            import inspect

            mod_path = inspect.getmodule(inspect.stack()[1][0]).__file__
            Imports.PACKAGE_STATUS[file_alias] = {"allowed": True, "info": "from {}".format(mod_path)}
            randomize = False  # No point to change the url in this case.

        if randomize:
            import random

            self.page.imports.moduleConfigs['local_%s' % filename[:-3]] = "version=%s" % random.random()
        return self

    def extendProto(self, py_class: Any, func_name: str, js_funcs: Union[str, list], pmts: Optional[dict] = None,
                    profile: Optional[Union[dict, bool]] = False):
        """Javascript Framework extension.

        Hook in the base class to allow the definition of specific function to add extra primitive features.
        Usual this function should be used in a wrapper function with the same name in order to have a coherent
        bridge between Python and Javascript.

        `Related Pages <https://www.w3schools.com/js/js_object_prototypes.asp>`_

        :param py_class: PyJs class name
        :param func_name: The Javascript function name
        :param js_funcs: Javascript functions
        :param pmts: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage

        :return: The Js Object to allow the chaining.
        """
        js_data = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
        self.page._props.setdefault('js', {}).setdefault('prototypes', {})["%s.prototype.%s" % (
            py_class._jsClass, func_name)] = {"content": js_data, 'pmts': pmts}
        return self

    def request_http(self, method_type: str, url: str, js_code: str = "response", is_json: bool = True,
                     components: Optional[List[primitives.HtmlModel]] = None) -> JsObjects.XMLHttpRequest:
        """All modern browsers have a built-in XMLHttpRequest object to request data from a server.

        `Related Pages <https://www.w3schools.com/xml/xml_http.asp>`_

        Usage::

          page.js.request_http("ajax", "POST", "https://api.cdnjs.com/libraries").setHeaders(header).onSuccess([
          page.js.alert(rptObj.js.objects.request.get("ajax").responseText)]).send(encodeURIData={"search": 'ractive'})

        :param method_type: The method of the HTTP Request
        :param url: The url path of the HTTP request
        :param js_code: Optional. The variable name created in the Javascript
        :param is_json: Optional. Specify the type of object passed
        :param components: Optional. A list of HTML objects values to be passed in the request
        """
        method_type = JsUtils.jsConvertData(method_type, None)
        url = JsUtils.jsConvertData(url, None)
        return JsObjects.XMLHttpRequest(self.page, js_code, method_type, url)

    def flows(self, data, dataflows, js_code: str = None) -> JsObjects.JsObject.JsObject:
        """Allow isolated data process.
        Those data processes are running in JavaScript.

        :param data: Input data
        :param js_code: Optional. The variable to use (to allow the chaining).
        """
        if js_code is not None:
            return JsObjects.JsObject.JsObject.get("%s = %s" % (js_code, JsUtils.dataFlows(data, dataflows, self.page)))

        return JsObjects.JsObject.JsObject.get(data, dataflows, self.page)

    def get(self, url: Union[str, primitives.JsDataModel], data: Optional[dict] = None,
            js_code: str = "response", is_json: bool = True,
            components: Optional[Union[Tuple[primitives.HtmlModel, str], List[primitives.HtmlModel]]] = None,
            headers: Optional[dict] = None,
            asynchronous: bool = False, stringify: bool = True,
            dataflows: List[dict] = None, options: dict = None) -> JsObjects.XMLHttpRequest:
        """Create a GET HTTP request.

        Usage::

          inputs = page.ui.input("")
          btn = page.ui.button("Click").click([
            page.js.get("/test", {"fegeg": "efefe", "ok": inputs.dom.content}, components=[("input", inputs)])])

        :param url: The url path of the HTTP request
        :param data: Optional. A String corresponding to a JavaScript object
        :param js_code: Optional. The variable name created in the Javascript (default response)
        :param is_json: Optional. Specify the type of object passed
        :param components: Optional. This will add the component value to the request object
        :param headers: Optional. The request headers
        :param asynchronous: Async flag: true (asynchronous) or false (synchronous)
        :param dataflows: Chain of data transformations
        """
        method_type = JsUtils.jsConvertData('GET', None)
        url = JsUtils.jsConvertData(url, None)
        url_params = []
        if components is not None:
            for component in components:
                if isinstance(component, tuple):
                    if hasattr(component[1], "dom"):
                        url_params.append('"%s=" + %s' % (component[0], component[1].dom.content.toStr()))
                    else:
                        url_params.append('"%s=" + %s' % (component[1], component[0].dom.content.toStr()))
                else:
                    url_params.append('"%s=" + %s' % (component.ref, component.dom.content.toStr()))
        if data is not None:
            for k, v in data.items():
                url_params.append('"%s=" + %s' % (k, JsUtils.jsConvertData(v, None)))
        if url_params:
            url = '%s + "?" + %s' % (url, ' +"&"+ '.join(url_params))
        request = JsObjects.XMLHttpRequest(self.page, js_code, method_type, url, asynchronous=asynchronous)
        request.URL = JsUtils.jsWrap(url) if not hasattr(url, "toStr") else url
        request.send({}, stringify=is_json, dataflows=dataflows)
        if is_json:
            request.setRequestHeader("Content-Type", "application/json;charset=UTF-8")
        if headers is not None:
            for k, v in headers.items():
                request.setRequestHeader(k, v)
        if options and "cache" in options:
            request.set_cache(
                options["cache"]["name"], options["cache"].get("type", "local"), data=data, components=components)
        return request

    def rest(self, method: str, url: Union[str, primitives.JsDataModel], data: Optional[dict] = None,
             js_code: str = "response", is_json: bool = True,
             components: Optional[List[Union[Tuple[primitives.HtmlModel, str], primitives.HtmlModel]]] = None,
             profile: Optional[Union[dict, bool]] = None, headers: Optional[dict] = None,
             asynchronous: bool = False, stringify: bool = True,
             dataflows: List[dict] = None, options: dict = None) -> JsObjects.XMLHttpRequest:
        """Create a POST HTTP request.

        :param method: The REST method used
        :param url: The url path of the HTTP request
        :param data: Optional. Corresponding to a JavaScript object
        :param js_code: Optional. The variable name created in the Javascript (default response)
        :param is_json: Optional. Specify the type of object passed
        :param components: Optional. This will add the component value to the request object
        :param profile: Optional. A flag to set the component performance storage
        :param headers: Optional. The request headers
        :param asynchronous: Optional. Async flag: true (asynchronous) or false (synchronous)
        :param stringify: Optional. Stringify the request data for json exchange
        :param dataflows: Chain of data transformations
        :param options: 
        """
        if method.upper() == "GET":
            # Redirect to the specific get method
            return self.get(
                url=url, data=data, js_code=js_code, is_json=is_json, components=components, headers=headers,
                asynchronous=asynchronous, options=options)

        method_type = JsUtils.jsConvertData(method, None)
        url = JsUtils.jsConvertData(url, None)
        request = JsObjects.XMLHttpRequest(self.page, js_code, method_type, url, asynchronous=asynchronous)
        request.profile = profile
        if components is not None:
            for c in components:
                if c.__class__.__name__ == 'InputFile':
                    stringify = False
            if not data:
                data = components
            else:
                for c in components:
                    if isinstance(c, tuple):
                        request.data.add(c[0], c[1], is_json=is_json)
                    else:
                        request.data.add(c, is_json=is_json)
        request.send(data, stringify=stringify, is_json=is_json, dataflows=dataflows)
        if stringify:
            request.setRequestHeader("Content-Type", "application/json;charset=UTF-8")
        if headers is not None:
            for k, v in headers.items():
                request.setRequestHeader(k, v)
        if options and "cache" in options:
            request.set_cache(
                options["cache"]["name"], options["cache"].get("type", "local"), data=data, components=components)
        return request

    def post(self, url: Union[str, primitives.JsDataModel], data: Optional[dict] = None, js_code: str = "response",
             is_json: bool = True,
             components: Optional[List[Union[Tuple[primitives.HtmlModel, str], primitives.HtmlModel]]] = None,
             profile: Optional[Union[dict, bool]] = None, headers: Optional[dict] = None,
             asynchronous: bool = False, stringify: bool = True,
             dataflows: List[dict] = None, options: dict = None) -> JsObjects.XMLHttpRequest:
        """Create a POST HTTP request.

        `Related Pages <https://pythonise.com/series/learning-flask/flask-http-methods>`_

        :param url: The url path of the HTTP request
        :param data: Optional. Corresponding to a JavaScript object
        :param js_code: Optional. The variable name created in the Javascript (default response)
        :param is_json: Optional. Specify the type of object passed
        :param components: Optional. This will add the component value to the request object
        :param profile: Optional. A flag to set the component performance storage
        :param headers: Optional. The request headers
        :param asynchronous: Async flag: true (asynchronous) or false (synchronous)
        :param stringify: Optional. Stringify the request data for json exchange
        :param dataflows: Chain of data transformations
        """
        return self.rest("POST", url=url, data=data, js_code=js_code, is_json=is_json, components=components,
                         profile=profile, headers=headers, asynchronous=asynchronous, stringify=stringify,
                         dataflows=dataflows, options=options)

    def put(self, url: Union[str, primitives.JsDataModel], data: Optional[dict] = None, js_code: str = "response",
            is_json: bool = True,
            components: Optional[List[Union[Tuple[primitives.HtmlModel, str], primitives.HtmlModel]]] = None,
            profile: Optional[Union[dict, bool]] = None, headers: Optional[dict] = None,
            asynchronous: bool = False, stringify: bool = True,
            dataflows: List[dict] = None, options: dict = None) -> JsObjects.XMLHttpRequest:
        """Create a PUT HTTP request.

        `Related Pages <https://pythonise.com/series/learning-flask/flask-http-methods>`_

        :param url: The url path of the HTTP request
        :param data: Optional. Corresponding to a JavaScript object
        :param js_code: Optional. The variable name created in the Javascript (default response)
        :param is_json: Optional. Specify the type of object passed
        :param components: Optional. This will add the component value to the request object
        :param profile: Optional. A flag to set the component performance storage
        :param headers: Optional. The request headers
        :param asynchronous: Async flag: true (asynchronous) or false (synchronous)
        :param stringify: Optional. Stringify the request data for json exchange
        :param dataflows: Chain of data transformations
        """
        return self.rest("PUT", url=url, data=data, js_code=js_code, is_json=is_json, components=components,
                         profile=profile, headers=headers, asynchronous=asynchronous, stringify=stringify,
                         dataflows=dataflows, options=options)

    def patch(self, url: Union[str, primitives.JsDataModel], data: Optional[dict] = None, js_code: str = "response",
              is_json: bool = True,
              components: Optional[List[Union[Tuple[primitives.HtmlModel, str], primitives.HtmlModel]]] = None,
              profile: Optional[Union[dict, bool]] = None, headers: Optional[dict] = None,
              asynchronous: bool = False, stringify: bool = True,
              dataflows: List[dict] = None, options: dict = None) -> JsObjects.XMLHttpRequest:
        """Create a PATH HTTP request.

        `Related Pages <https://pythonise.com/series/learning-flask/flask-http-methods>`_

        :param url: The url path of the HTTP request
        :param data: Optional. Corresponding to a JavaScript object
        :param js_code: Optional. The variable name created in the Javascript (default response)
        :param is_json: Optional. Specify the type of object passed
        :param components: Optional. This will add the component value to the request object
        :param profile: Optional. A flag to set the component performance storage
        :param headers: Optional. The request headers
        :param asynchronous: Async flag: true (asynchronous) or false (synchronous)
        :param stringify: Optional. Stringify the request data for json exchange
        :param dataflows: Chain of data transformations
        """
        return self.rest("PATH", url=url, data=data, js_code=js_code, is_json=is_json, components=components,
                         profile=profile, headers=headers, asynchronous=asynchronous, stringify=stringify,
                         dataflows=dataflows, options=options)

    def delete(self, url: Union[str, primitives.JsDataModel], data: Optional[dict] = None, js_code: str = "response",
               is_json: bool = True,
               components: Optional[List[Union[Tuple[primitives.HtmlModel, str], primitives.HtmlModel]]] = None,
               profile: Optional[Union[dict, bool]] = None, headers: Optional[dict] = None,
               asynchronous: bool = False, stringify: bool = True,
               dataflows: List[dict] = None, options: dict = None) -> JsObjects.XMLHttpRequest:
        """Create a DELETE HTTP request.

        `Related Pages <https://pythonise.com/series/learning-flask/flask-http-methods>`_

        :param url: The url path of the HTTP request
        :param data: Optional. Corresponding to a JavaScript object
        :param js_code: Optional. The variable name created in the Javascript (default response)
        :param is_json: Optional. Specify the type of object passed
        :param components: Optional. This will add the component value to the request object
        :param profile: Optional. A flag to set the component performance storage
        :param headers: Optional. The request headers
        :param asynchronous: Async flag: true (asynchronous) or false (synchronous)
        :param stringify: Optional. Stringify the request data for json exchange
        :param dataflows: Chain of data transformations
        :param options:
        """
        return self.rest("DELETE", url=url, data=data, js_code=js_code, is_json=is_json, components=components,
                         profile=profile, headers=headers, asynchronous=asynchronous, stringify=stringify,
                         dataflows=dataflows, options=options)

    def queueMicrotask(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
        """The queueMicrotask() method, which is exposed on the Window or Worker interface, queues a microtask to be
        executed at a safe time prior to control returning to the browser's event loop.

        Usage::

          page.body.onReady([page.js.queueMicrotask([page.js.alert("ok")])])

        `Related Pages <https://developer.mozilla.org/fr/docs/Web/API/queueMicrotask>`_

        :param js_funcs: The Javascript function definition
        :param profile: Optional. A flag to set the component performance storage
        """
        js_data = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
        return JsObjects.JsVoid("queueMicrotask(() => {%s})" % js_data)

    def request_rpc(self, js_code: str, method_type: Union[str, primitives.JsDataModel],
                    fnc: Callable, url: str,
                    extra_params: Optional[Union[dict, primitives.JsDataModel]] = None) -> JsObjects.XMLHttpRequest:
        """Internal RPC to trigger services.

        :param js_code: The variable name created in the Javascript
        :param method_type: The method type
        :param fnc: Python function
        :param url: The service url
        :param extra_params: Optional
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
        return JsObjects.XMLHttpRequest(self.page, js_code, method_type, url, JsData.Datamap(attrs=rpc_params))

    def fetch(self, url: str, options: Optional[dict] = None, profile: Optional[Union[dict, bool]] = False,
              async_await: bool = False) -> JsObjects.JsPromise:
        """The Fetch API provides a JavaScript interface for accessing and manipulating parts of the HTTP pipeline,
        such as requests and responses.

        Usage::

          page.ui.button("Click").click([
            page.js.fetch("test", {"method": "POST"}).then([
              page.js.console.log(pk.events.response)])])

        `Related Pages <https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch>`_

        :param url: The target url
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        :param async_await: Optional.
        """
        fetch_name = "await fetch" if async_await else "fetch"
        if options is None:
            return JsObjects.JsPromise(
                "%s(%s)" % (fetch_name, JsUtils.jsConvertData(url, None)), profile, async_await, page=self.page)

        return JsObjects.JsPromise(
            "%s(%s, %s)" % (fetch_name, JsUtils.jsConvertData(url, None), JsUtils.jsConvertData(options, None)),
            profile, async_await, page=self.page)

    def await_promises(self, promises: list, js_funcs: list, before_js_funcs: list = None, data_ref = "responses") -> JsUtils.jsWrap:
        """Add sync to async promises.

        :param promises: List of promises to wait for
        :param before_js_funcs: Events to be executed before the promises setup
        :param js_funcs: Events when all promises are completed
        :param data_ref: JavaScript variable name for the different promises responses.
        """
        js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True)
        apis = "[%s]" % ",".join([JsUtils.jsConvertData(p, None) for p in promises])
        if before_js_funcs:
            before_js_funcs = JsUtils.jsConvertFncs(before_js_funcs, toStr=True)
            return JsUtils.jsWrap("(async function (){%s; let %s = await Promise.all(%s); %s})()" % (
                before_js_funcs, data_ref, apis, js_funcs))

        return JsUtils.jsWrap("(async function (){let %s = await Promise.all(%s); %s})()" % (data_ref, apis, js_funcs))

    @property
    def fncs(self) -> JsFncs.JsRegisteredFunctions:
        """Property to the predefined Javascript functions.

        :return: The predefined functions.
        """
        return JsFncs.JsRegisteredFunctions(self.page)

    @property
    def samples(self) -> JsFncsSamples.Samples:
        """JavaScript feature to provide sample of data for a test/demo.

        Usage::

          page.js.samples.months(count_=7)
          page.js.samples.numbers(count_=7, min_=-100, max_=100)
        """
        return JsFncsSamples.Samples(self.page)

    @property
    def breadcrumb(self) -> JsBreadCrumb:
        """Create an internal Breadcrumb to keep track of the user journey within your page.

        `Related Pages <https://www.w3schools.com/howto/howto_css_breadcrumbs.asp>`_

        :return: A Python breadcrumb object.
        """
        if self._breadcrumb is None:
            self._breadcrumb = JsBreadCrumb(self.page)
        return self._breadcrumb

    def navigateTo(self, url: Union[str, primitives.JsDataModel], options: Optional[dict] = None) -> JsObject.JsObject:
        """Navigator to another URL like NodeJs.

        Usage::

          icon.click([self.context.page.js.navigateTo(url)])

        `Related Pages <https://redfin.github.io/react-server/annotated-src/navigateTo.html>`_

        :param url: The target url
        :param options: Optional. The property of the location object
        """
        options = options or {}
        if options.get("target", '') != "_blank":
            return self.location.href(href=url)

        return self.location.open_new_tab(url=url)

    def registerFunction(self, func_name: str, js_funcs: Union[str, list], args: Optional[dict] = None,
                         profile: Optional[Union[dict, bool]] = False):
        """Javascript Framework extension.

        Register a predefined Javascript function.
        This is only dedicated to specific Javascript transformation functions.

        :param func_name: The function name
        :param js_funcs: The Javascript function definition
        :param args: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        js_data = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
        self.page.properties.js.add_function(func_name, js_data, args)
        return self

    @property
    def keydown(self) -> KeyCodes.KeyCode:
        """The onkeydown event occurs when the user is pressing a key (on the keyboard).

        Usage::

          page.js.keydown.enter(pk.js_std.alert('Hello World'), profile=True)

        `Related Pages <https://www.w3schools.com/jsref/event_onkeydown.asp>`_
        """
        keydown = KeyCodes.KeyCode(page=self.page, source_event='document')
        self.page.properties.js.add_event('keydown', keydown)
        return keydown

    @property
    def keypress(self) -> KeyCodes.KeyCode:
        """The onkeypress event occurs when the user presses a key (on the keyboard).

        Usage::

          page.js.keypress.enter(pk.js_std.alert('Hello World'), profile=True)

        `Related Pages <https://www.w3schools.com/jsref/event_onkeypress.asp>`_
        """
        keypress = KeyCodes.KeyCode(page=self.page, source_event='document')
        self.page.properties.js.add_event('keypress', keypress)
        return keypress

    @property
    def keyup(self) -> KeyCodes.KeyCode:
        """The onkeypress event occurs when the user presses a key (on the keyboard).

        Usage::

          page.js.keyup.enter(pk.js_std.alert('Hello World'), profile=True)

        `Related Pages <https://www.w3schools.com/jsref/event_onkeypress.asp>`_
        """
        keyup = KeyCodes.KeyCode(page=self.page, source_event='document')
        self.page.properties.js.add_event('keyup', keyup)
        return keyup

    def onReady(self, js_funcs: Union[str, list], profile: Optional[Union[dict, bool]] = False):
        """The ready event occurs when the body DOM (document object model) has been loaded.

        `Related Pages <https://www.w3schools.com/jquery/event_ready.asp>`_

        :param js_funcs: The Javascript functions to be added to this section
        :param profile: Optional. A flag to set the component performance storage
        """
        self.page.properties.js.add_on_ready(JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile))
        return self

    def profile(self, type: Union[str, primitives.JsDataModel], html_code: str,
                mark: Union[str, primitives.JsDataModel],
                records_count: Optional[int] = None):
        """

        :param type: The type of profile tag.
        :param html_code: The HTML component ID.
        :param mark: The mark reference.
        :param records_count: Optional. The records count.
        """
        type = JsUtils.jsConvertData(type, None)
        mark = JsUtils.jsConvertData(mark, None)
        return "profileObj.push({type: %s, htmlCode: '%s', mark: %s, records: %s})" % (
            type, html_code, mark, records_count or "")

    @staticmethod
    def getElementById(id_name: Union[str, primitives.JsDataModel], js_conv_func: Optional[Union[str, list]] = None):
        """The getElementById() method returns the element that has the ID attribute with the specified value.

        `Related Pages <https://www.w3schools.com/jsref/met_document_getelementbyid.asp>`_

        :param id_name: The ID attribute's value of the element you want to get
        :param js_conv_func: Optional. A specific JavaScript data conversion function

        :return: An Element Object, representing an element with the specified ID. Returns null if no elements with
        the specified ID exists
        """
        return JsNodeDom.JsDoms(
            "document.getElementById(%s)" % JsUtils.jsConvertData(id_name, js_conv_func).toStr().replace("'", '"'))

    @staticmethod
    def getElementsByName(name: Union[str, primitives.JsDataModel],
                          js_conv_func: Optional[Union[str, list]] = None) -> JsNodeDom.JsDomsList:
        """The getElementsByName() method returns a collection of all elements in the document with the specified name
        (the value of the name attribute), as a NodeList object.

        The NodeList object represents a collection of nodes. The nodes can be accessed by index numbers.
        The index starts at 0.

        `Related Pages <https://www.w3schools.com/jsref/met_doc_getelementsbyname.asp>`_

        :param name: The name attribute value of the element you want to access/manipulate.
        :param js_conv_func: Optional. A specific JavaScript data conversion function.

        :return: A NodeList object, representing a collection of elements with the specified name.
                 The elements in the returned collection are sorted as they appear in the source code.
        """
        return JsNodeDom.JsDomsList.get(
            js_code="document.getElementsByName(%s)" % JsUtils.jsConvertData(name, js_conv_func))

    @staticmethod
    def getElementsByTagName(tag_name: Union[str, primitives.JsDataModel], i: int = 0,
                             js_conv_func: Optional[Union[str, list]] = None) -> JsNodeDom.JsDoms:
        """The getElementsByTagName() method returns a collection of an elements's child elements with the specified
        tag name, as a NodeList object.

        The NodeList object represents a collection of nodes. The nodes can be accessed by index numbers.
        The index starts at 0.

        `Related Pages <https://www.w3schools.com/jsref/met_element_getelementsbytagname.asp>`_

        :param tag_name: The tag name of the child elements you want to get
        :param i: Optional. The index of the element
        :param js_conv_func: Optional. A specific JavaScript data conversion function
        """
        return JsNodeDom.JsDoms("document.getElementsByTagName(%s)[%s]" % (
            JsUtils.jsConvertData(tag_name, js_conv_func), i), js_code="%s_%s" % (tag_name, i), set_var=True)

    @staticmethod
    def getElementsByClassName(cls_name: str) -> JsNodeDom.JsDoms:
        """The getElementsByClassName() method returns a collection of all elements in the document with the specified
        class name, as a NodeList object.

        `Related Pages <https://www.w3schools.com/jsref/met_document_getelementsbyclassname.asp>`_

        :param cls_name: The class name of the elements you want to get

        :return: A NodeList object, representing a collection of elements with the specified class name.
                 The elements in the returned collection are sorted as they appear in the source code.
        """
        return JsNodeDom.JsDoms("document.getElementsByClassName(%s)" % cls_name)

    def createElement(self, tag_name: str, js_code: str = None, set_var: bool = True, dom_id: str = None):
        """The createElement() method creates an Element Node with the specified name.

        `Related Pages <https://www.w3schools.com/jsref/met_document_createelement.asp>`_

        :param tag_name: The name of the element you want to create
        :param js_code: The variable name to be set. Default random name
        :param set_var: Optional. Create a variable for the new object. Default True
        :param dom_id: Optional. The Dom ID reference for the object
        """
        dom_obj = JsNodeDom.JsDoms.new(tag_name, js_code=js_code, set_var=set_var, page=self.page)
        if dom_id is not None:
            dom_obj.attr("id", dom_id)
        return dom_obj

    @staticmethod
    def createTextNode(text: Union[str, primitives.JsDataModel] = None,
                       js_conv_func: Optional[Union[str, list]] = None) -> JsObject.JsObject:
        """The createTextNode() method creates a Text Node with the specified text.

        `Related Pages <https://www.w3schools.com/jsref/met_document_createtextnode.asp>`_

        :param text: Optional. The text of the Text node
        :param js_conv_func: Optional. A specific JavaScript data conversion function

        :return: A Text Node object with the created Text Node.
        """
        return JsObject.JsObject(
            "document.createTextNode(%s)" % JsUtils.jsConvertData(text, js_conv_func), is_py_data=False)

    def createElementStyle(self, content, map_id: str = None, js_conv_func: Optional[Union[str, list]] = None,
                           override: bool = False):
        """Add a CSS element from the JavaScript.

        `Related Pages <https://gist.github.com/sagarpanda/ed583b408a38c56f33ba>`_

        :param content: CSS full content (selector + CSS content)
        :param map_id: CSS Class reference (to avoid adding multiple times the same one to the head
        :param js_conv_func: String conversion function
        :param override: Force the page to apply again the function to update a CSS class
        """
        if map_id is None:
            if hasattr(content, "classname"):
                map_id = content.classname
            else:
                map_id = "dyn_cls_%s" % hash(content)
        if map_id not in self.page.properties.css._dyn_cls or override:
            self.page.properties.css._dyn_cls.add(map_id)
            return JsObject.JsObject('''(function(content){let cssStyle = document.createElement('style'); 
    cssStyle.type = 'text/css'; cssStyle.innerHTML = content; document.getElementsByTagName('head')[0].appendChild(cssStyle); 
    return cssStyle})(%s)''' % JsUtils.jsConvertData(content, js_conv_func), is_py_data=False)

    def encodeURIComponent(self, uri: Union[str, primitives.JsDataModel],
                           js_conv_func: Union[str, list] = None) -> JsObject.JsObject:
        """The encodeURIComponent() function encodes a URI component.

        `Related Pages <https://www.w3schools.com/jsref/jsref_encodeuricomponent.asp>`_

        :param uri: The URI to be encoded
        :param js_conv_func: Optional. A specific JavaScript data conversion function

        :return: A String, representing the encoded URI.
        """
        return JsObject.JsObject("encodeURIComponent(%s)" % JsUtils.jsConvertData(uri, js_conv_func))

    def decodeURIComponent(self, url_enc: Union[str, primitives.JsDataModel],
                           js_conv_func: Union[str, list] = None) -> JsObject.JsObject:
        """The decodeURIComponent() function decodes a URI component.

        `Related Pages <https://www.w3schools.com/jsref/jsref_decodeuricomponent.asp>`_

        :param url_enc: The URI to be decoded
        :param js_conv_func: Optional. A specific JavaScript data conversion function

        :return: A String, representing the decoded URI.
        """
        return JsObject.JsObject("decodeURIComponent(%s)" % JsUtils.jsConvertData(url_enc, js_conv_func))

    @property
    def body(self) -> JsNodeDom.JsDoms:
        """Get the DOM object.

        This will return the object. It will not create any variable.
        """
        return JsNodeDom.JsDoms("document.body", set_var=False, is_py_data=False)

    @property
    def data(self) -> JsData.JsData:
        """ Get wrapped JavaScript data structures. """
        if self.__data is None:
            self.__data = JsData.JsData(self.page)
        return self.__data

    def string(self, data, js_code: str = None, set_var: bool = False, is_py_data: bool = True) -> JsString.JsString:
        """Shortcut to the Javascript String primitives.

        :param data: The String data.
        :param js_code: Optional. The specific name to be used for this JavaScript String.
        :param set_var: Optional. Set a variable. Default False.
        :param is_py_data: Optional. Specify the type of data.
        """
        return JsString.JsString(data, js_code, set_var, is_py_data, page=self.page)

    def number(self, data, js_code: str = None, set_var: bool = False, is_py_data: bool = True) -> JsNumber.JsNumber:
        """Shortcut to the Javascript Number primitives.

        :param data: The String data.
        :param js_code: Optional. The specific name to be used for this JavaScript String.
        :param set_var: Optional. Set a variable. Default False.
        :param is_py_data: Optional. Specify the type of data.
        """
        return JsNumber.JsNumber(data, js_code, set_var, is_py_data, page=self.page)

    def object(self, data, js_code: str = None, set_var: bool = False, is_py_data: bool = True) -> JsObject.JsObject:
        """Shortcut to the Javascript Object primitives.

        :param data: The String data.
        :param js_code: Optional. The specific name to be used for this JavaScript String.
        :param set_var: Optional. Set a variable. Default False.
        :param is_py_data: Optional. Specify the type of data.
        """
        return JsObject.JsObject(data, js_code, set_var, is_py_data, page=self.page)

    def intersectionObserver(self, js_code: str, callback: types.JS_FUNCS_TYPES = None, options: dict = None,
                             observe_once: bool = False, profile: types.PROFILE_TYPE = None
                             ) -> JsIntersectionObserver.IntersectionObserver:
        """

        :param js_code: The PyJs functions.
        :param callback: JavaScript functions called by the intersectionObserver.
        :param options: intersectionObserver options.
        :param observe_once: A flag to remove the observable once callbacks run.
        :param profile: Option to perform profiling logs in the browser console.
        """
        if callback is not None or options is not None:
            return JsIntersectionObserver.IntersectionObserver(self.page, js_code).new(
                callback, options, observe_once, profile)

        return JsIntersectionObserver.IntersectionObserver(self.page, js_code)

    def querySelectorAll(
            self,
            selector: Union[str, primitives.JsDataModel],
            js_conv_func: Union[str, list] = None) -> JsNodeDom.JsDomsList:
        """The querySelectorAll() method returns all elements in the document that matches a specified CSS selector(s),
        as a static NodeList object.

        `Related Pages <https://www.w3schools.com/jsref/met_document_queryselectorall.asp>`_

        :param selector: CSS selectors
        :param js_conv_func: Optional. A specific JavaScript data conversion function
        """
        return JsNodeDom.JsDomsList(
            "document.querySelectorAll(%s)" % JsUtils.jsConvertData(selector, js_conv_func), is_py_data=False)

    def querySelector(self, selector: Union[str, primitives.JsDataModel], js_conv_func: Union[str, list] = None):
        """The querySelector() method returns the first element that matches a specified CSS selector(s) in the document.

        `Related Pages <https://www.w3schools.com/jsref/met_document_queryselector.asp>`_

        :param selector: CSS selectors
        :param js_conv_func: Optional. A specific JavaScript data conversion function
        """
        return JsNodeDom.JsDoms.get("document.querySelector(%s)" % JsUtils.jsConvertData(selector, js_conv_func))

    def activeElement(self):
        """The activeElement property returns the currently focused element in the document.

        `Related Pages <https://www.w3schools.com/jsref/prop_document_activeelement.asp>`_

        :return: A reference to the element object in the document that has focus.
        """
        return JsNodeDom.JsDoms("document.activeElement")

    @staticmethod
    def title(text: Optional[Union[str, primitives.JsDataModel]] = None,
              js_conv_func: Optional[Union[str, list]] = None):
        """The title property sets or returns the title of the current document (the text inside the HTML title element).

        `Related Pages <https://www.w3schools.com/jsref/prop_doc_title.asp>`_

        :param text: Optional. Representing the title of the document
        :param js_conv_func: Optional. A specific JavaScript data conversion function
        """
        if text is None:
            return JsString.JsString("document.title")

        return JsObjects.JsVoid("document.title = %s" % JsUtils.jsConvertData(text, js_conv_func))

    def execCommand(self, command: str, show_ui: bool, value: str) -> JsObjects.JsVoid:
        """The execCommand() method executes the specified command for the selected part of an editable section.

        `Related Pages <https://www.w3schools.com/jsref/met_document_execcommand.asp>`_

        :param command:. Specifies the name of the command to execute on the selected section
        :param show_ui: specifies if the UI should be shown or not
        :param value: Some commands need a value to be completed

        :return: A Boolean, false if the command is not supported, otherwise true.
        """
        return JsObjects.JsVoid("document.execCommand('%s')" % command)

    def createEvent(self, event_type: str):
        """The createEvent() method creates an event object.
        The event can be of any legal event type, and must be initialized before use.

        `Related Pages <https://www.w3schools.com/jsref/event_createevent.asp>`_

        :param event_type: A String that specifies the type of the event.

        :return: An Event object
        """
        if event_type not in ['AnimationEvent', 'ClipboardEvent', 'DragEvent', 'FocusEvent', 'HashChangeEvent',
                              'InputEvent', 'MouseEvent', 'PageTransitionEvent', 'PopStateEvent', 'ProgressEvent',
                              'StorageEvent', 'TouchEvent', 'TransitionEvent', 'UiEvent', 'WheelEvent',
                              'KeyboardEvent']:
            raise ValueError("Not recognized type %s" % event_type)

    def createAttribute(self, attribute_name):
        """The createAttribute() method creates an attribute with the specified name, and returns the attribute as an
        Attr object.

        `Related Pages <https://www.w3schools.com/jsref/met_document_createattribute.asp>`_

        :param attribute_name: The name of the attribute you want to create

        :return: A Node object, representing the created attribute.
        """
        return JsNodeAttributes.JsAttributes(attribute_name)

    def writeln(self, value: str):
        """The writeln() method is identical to the document.write() method, with the addition of writing a newline
        character after each statement.

        `Related Pages <https://www.w3schools.com/jsref/met_doc_writeln.asp>`_

        :param value: What to write to the output stream. Multiple arguments can be listed and they will be appended
          to the document in order of occurrence

        :return: No return value
        """
        return JsObjects.JsVoid("document.writeln(%s)" % value)

    @staticmethod
    def parseFloat(value: str) -> JsNumber.JsNumber:
        """The parseFloat() function parses a string and returns a floating point number.

        `Related Pages <https://www.w3schools.com/jsref/jsref_parseint.asp>`_

        :param value: The string to be parsed

        :return: A Number. If the first character cannot be converted to a number, NaN is returned.
        """
        return JsNumber.JsNumber("parseFloat(%s)" % value, is_py_data=False)

    @staticmethod
    def parseInt(value: str):
        """The parseInt() function parses a string and returns an integer.

        `Related Pages <https://www.w3schools.com/jsref/jsref_parseint.asp>`_

        :param value: The string to be parsed

        :return: A Number. If the first character cannot be converted to a number, NaN is returned.
        """
        return JsNumber.JsNumber("parseInt(%s)" % value, is_py_data=False)

    @staticmethod
    def parseDate(value: str) -> JsNumber.JsNumber:
        """The parse() method parses a date string and returns the number of milliseconds between the date string and
        midnight of January 1, 1970.

        `Related Pages <https://www.w3schools.com/jsref/jsref_parse.asp>`_

        :param value: A string representing a date

        :return: Number. Representing the milliseconds between the specified date-time and midnight January 1, 1970.
        """
        return JsNumber.JsNumber("Date.parse(%s)" % value, is_py_data=False)

    def getVar(self, js_code: Union[str, primitives.JsDataModel], var_type: str = "var") -> JsObjects.JsObject.JsObject:
        """Get the Javascript Variable name.

        :param js_code: The Variable name
        :param var_type: Optional. The scope of the variable

        :return: Return the piece of script to be added to the Javascript.
        """
        if var_type == 'var':
            js_code = JsUtils.jsConvertData(js_code, None)
            return JsObjects.JsObject.JsObject.get("window[%s]" % js_code)

        return JsObjects.JsObject.JsObject.get(js_code)

    def setVar(self, js_code: Union[str, primitives.JsDataModel], data: Any) -> JsObjects.JsObject.JsObject:
        """Set a global / window Javascript variable.

        Usage::

            table_load_flag = "isTableLoaded"
            page.js.setVar(table_load_flag, False)

        :param js_code: The Variable name
        :param data: The Variable content
        """
        js_code = JsUtils.jsConvertData(js_code, None)
        js_data = JsUtils.jsConvertData(data, None)
        return JsObjects.JsObject.JsObject.get("window[%s] = %s" % (js_code, js_data))

    def info(self, data: Union[str, primitives.JsDataModel], css_style: Optional[dict] = None,
             icon: str = "fas fa-spinner fa-spin", seconds: int = 10000):
        """Display a message.

        `Related Pages <https://fontawesome.com/how-to-use/on-the-web/styling/animating-icons>`_

        :param data: A String corresponding to a JavaScript object
        :param css_style: Optional. The CSS attributes to be added to the HTML component
        :param icon: Optional. A string with the value of the icon to display from font-awesome
        :param seconds: Optional. The number of second the info will be visible
        """
        if css_style is None:
            css_style = {"position": "fixed", "bottom": "5px", "right": "10px", "padding": '2px 7px',
                         "border": "1px solid black"}
        if icon is not None:
            self.page.jsImports.add('font-awesome')
            self.page.cssImport.add('font-awesome')
            return [
                self.createElement("i", js_code="popup_icon").setAttribute("aria-hidden", True).css(
                    {"display": "inline-block", "width": "auto", "height": "auto", "margin-right": '5px'}).className(
                    icon),
                self.createElement("div", js_code="popup_info").appendChild(
                    self.objects.dom("popup_icon")).css(css_style).text(data),
                self.body.appendChild(self.objects.dom("popup_info")),
                self.window.setTimeout(self.objects.dom("popup_info").remove(), milliseconds=seconds)]

        return [
            self.createElement("div", js_code="popup_info").css(css_style).text(data),
            self.body.appendChild(self.objects.dom("popup_info")),
            self.window.setTimeout(self.objects.dom("popup_info").remove(), milliseconds=seconds)]

    def print(self, content: Union[str, primitives.JsDataModel], timer: int = 1000, css_attrs: Optional[dict] = None):
        """Print a temporary message.

        :param content: The content of the popup.
        :param timer: Optional. The time the popup will be displayed.
        :param css_attrs: Optional. The CSS attributes for the popup.
        """
        dfl_attrs = {"position": "absolute", "background": "white", "padding": "5px 10px", 'border-radius': "5px",
                     "top": JsObject.JsObject.get('event.clientY + "px"'),
                     'left': JsObject.JsObject.get('event.clientX + "px"')}
        if css_attrs is not None:
            dfl_attrs.update(css_attrs)
            if 'bottom' in css_attrs:
                del dfl_attrs["top"]
            if 'right' in css_attrs:
                del dfl_attrs["left"]
        return '''
      (function(event, content){
        var popup = document.createElement("div"); %s
        popup.innerHTML = content; document.body.appendChild(popup);
        setTimeout(function(){ document.body.removeChild(popup); }, %s);
      })(event, %s)''' % (JsNodeDom.JsDoms.get("popup").css(dfl_attrs).r, timer, JsUtils.jsConvertData(content, None))

    def mail(self, mails, subject=None, body=None, cc=None, bcc=None):
        """Create an email.

        `Related Pages <https://www.w3docs.com/snippets/html/how-to-create-mailto-links.html>`_

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
    def msg(self) -> JsMsgAlerts.Msg:
        """Shortcut to predefined temporary messages displayed to the UI. """
        return JsMsgAlerts.Msg(self.page)

    def import_js(self, script: str, js_funcs: Union[str, list], profile: Optional[Union[bool, dict]] = None,
                  self_contained: bool = False):
        """Add a Javascript module and then run function once it is loaded.

        Usage::

          icon = page.ui.icons.clock().css({"color": 'blue'})
          icon.click([ page.js.import_js("utils.js", ["testImport()"])])

        `Related Pages <https://cleverbeagle.com/blog/articles/tutorial-how-to-load-third-party-scripts-dynamically-in-javascript>`_
        `Related Pages <https://stackoverflow.com/questions/950087/how-do-i-include-a-javascript-file-in-another-javascript-file>`_

        :param script: A script name. A Js extension
        :param js_funcs: Callback function when module loaded. The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param self_contained: Optional. A flag to specify where the import will be done
        """
        if script.endswith(".js"):
            if os.path.exists(script) and self_contained:
                with open(script, 'rb') as fp:
                    base64_bytes = base64.b64encode(fp.read())
                    base64_message = base64_bytes.decode('ascii')
                    url_module = "data:text/javascript;base64,%s" % base64_message
            else:
                url_module = script
            js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
            return JsUtils.jsWrap('''
let scriptElementId = "pkg_%(script)s";    
let existingScript = document.getElementById(scriptElementId);
if (!existingScript && (scriptElementId !== 'pkg_undefined')) {
  const script = document.createElement('script'); script.src = "%(content)s"; script.id = scriptElementId;
  document.body.appendChild(script); script.onload = function(){%(fncs)s; };}
else {%(fncs)s}  ''' % {"script": abs(hash(script)), "content": url_module, "fncs": js_funcs})

        else:
            js_script = JsUtils.jsConvertData(script, None)
            js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
            return JsUtils.jsWrap('''
  let scriptElementId = "pkg_"+ %(script)s;    
  let existingScript = document.getElementById(scriptElementId);
  if (!existingScript && (scriptElementId !== 'pkg_undefined')) {
    const script = document.createElement('script'); script.src = %(script)s; script.id = scriptElementId;
    document.body.appendChild(script); script.onload = function(){%(fncs)s; };}
  else {%(fncs)s}  ''' % {"script": js_script, "fncs": js_funcs})

    def import_css(self, css_file: str, self_contained: bool = False, js_code: str = "css_dyn"):
        """Add a CSS file on the fly from a JavaScript event.

        `Related Pages <https://stackoverflow.com/questions/19844545/replacing-css-file-on-the-fly-and-apply-the-new-style-to-the-page>`_

        :param css_file: A script name with a CSS extension
        :param self_contained: Optional. A flag to specify where the import will be done
        :param js_code: Optional. The CSS Style element tag
        """
        if css_file.endswith(".css"):
            if os.path.exists(css_file) and self_contained:
                with open(css_file, 'rb') as fp:
                    base64_bytes = base64.b64encode(fp.read())
                    base64_message = base64_bytes.decode('ascii')
                    url_module = "data:text/css;base64,%s" % base64_message
            else:
                url_module = css_file
        else:
            base64_bytes = base64.b64encode(css_file.encode('ascii'))
            base64_message = base64_bytes.decode('ascii')
            url_module = "data:text/css;base64,%s" % base64_message
        return JsUtils.jsWrap('''
let styleElementId = "css_"+ %(js_code)s;    
let existingStyle = document.getElementById(styleElementId);
if (!existingStyle && (styleElementId !== 'css_')) {
  var fileref = document.createElement("link"); fileref.id = styleElementId;
  fileref.setAttribute("rel", "stylesheet"); fileref.setAttribute("type", "text/css");
  fileref.setAttribute("href", "%(file)s"); document.getElementsByTagName("head")[0].appendChild(fileref)
}''' % {"file": url_module, "js_code": JsUtils.jsConvertData(js_code, None)})

    def delay(self, js_funcs: Union[list, str], seconds: int = 0, window_id: str = "window",
              profile: Optional[Union[dict, bool]] = False):
        """Add a wrapper on top of the setTimeout.

        Usage::

          page.js.delay([text.build("Change the value")], 5)

        :param js_funcs: The function that will be executed
        :param seconds: Optional. The number of seconds to wait before executing the code
        :param window_id: Optional. The JavaScript window object
        :param profile: Optional. Set to true to get the profile for the function on the Javascript console
        """
        return self.window.setTimeout(js_funcs, seconds * 1000, window_id, profile)

    def callback_data(self, data, keys, js_funcs, comparator: Union[dict, str] = None, html_codes: List[str] = None,
                      profile: Optional[Union[bool, dict]] = None, ignore_empty: bool = False) -> types.JS_EXPR_TYPES:
        """JavaScript's expression to define a data callback function.

        :param data: The data object
        :param keys: The keys / depth structure within the object
        :param js_funcs: The callback methods if
        :param comparator: Optional. The comparator rule. By default, it will just check if key exist
        :param html_codes: Optional. The components required to run the expression
        :param profile: Optional. Set to true to get the profile for the function on the Javascript console
        :param ignore_empty: Optional. Flag to ignore key with empty value
        """
        if html_codes and self.page is not None:
            for html_code in html_codes:
                if html_code not in self.page.components:
                    return ""

        if comparator is not None:
            if isinstance(comparator, dict):
                value = JsUtils.jsConvertData(comparator.get("value", ""), None)
                operator = comparator.get("operator", "==")
            else:
                value = JsUtils.jsConvertData(comparator, None)
                operator = "=="
            return JsUtils.jsWrap("if((%s) && (%s %s %s)){%s}" % (
                data.has_keys(keys, ignore_empty=ignore_empty), data.get_value(keys), operator, value,
                JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))

        return JsUtils.jsWrap("if(%s){%s}" % (
            data.has_keys(keys, ignore_empty=ignore_empty),
            JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))

    @property
    def caches(self) -> JsCacheStorage.CacheStorage:
        """The CacheStorage interface represents the storage for Cache objects."""
        logging.debug(
            "Caches not available for all browsers: https://developer.mozilla.org/en-US/docs/Web/API/CacheStorage#browser_compatibility")
        return JsCacheStorage.CacheStorage(self.page)

    def warnings(self, js_funcs, attrs: dict = None, name: str = "signOffModal", module: str = "WarningsPopup",
                 required_funcs: List[str] = None, group: str = "utils",
                 profile: Optional[Union[bool, dict]] = None) -> Optional[JsUtils.jsWrap]:
        """Add a popup window before triggering the event.

        Usage::
            ic = page.ui.icon("far fa-thumbs-up", text="0")
            ic.click(page.js.warnings([ic.dom.increment(by=-1)]))

        :param js_funcs: List of JavaScript events to be triggered
        :param attrs: Popup static attributes
        :param name: JavaScript popup function - default signOffModal
        :param module: JavaScript popup module - default WarningsPopup
        :param required_funcs: Required JavaScript modules
        :param group: Sub folder with the module location - default utils
        :param profile: Optional. Set to true to get the profile for the function on the Javascript console
        """
        self.page.properties.css.add_text(".warning-model:focus{outline: None}", map_id="warning-model")
        attrs = attrs or {}
        is_loaded = JsUtils.addJsResources(
            self.page._props["js"]['constructors'], module + ".js", sub_folder=group,
            required_funcs=required_funcs or treemap._BUILDERS_MAP.get(name, []),
            verbose=False)
        if is_loaded:
            return JsUtils.jsWrap("%s(event, function(event){%s}, %s)" % (
                name, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile),
                JsUtils.jsConvertData(attrs, None)))

    def const(self, name: str, value: str = None):
        """Add a constant to the page. Variable will be in uppercase.

        Usage::
            page.body.onReady([page.js.const("file", page.js.location.part(1, from_="locals"))])

        :param name: Constant variable's name
        :param value: Optional. Constant variable's value
        """
        if value:
            value = JsUtils.jsConvertData(value, None)
            return JsUtils.jsWrap("const %s = %s" % (name.upper(), value))

        return JsObject.JsObject.get(name.upper())



class JsConsole:
    """This is a wrapper to the Console.

    `Related Pages <https://medium.freecodecamp.org/how-to-get-the-most-out-of-the-javascript-console-b57ca9db3e6d>`_
    """

    def __init__(self, page: primitives.PageModel = None):
        self.page = page

    @property
    def debugger(self):
        """Trigger a Javascript debugger from this point.
        The Javascript will be stopped. It will be possible to check the process step by step in the browser using F12.

        Usage::

          page.js.console.debugger

        `Related Pages <https://www.w3schools.com/jsref/jsref_debugger.asp>`_

        :return: The Javascript Keyword to trigger the browser debugger.
        """
        return JsObject.JsKeyword("debugger")

    @property
    def clear(self):
        """The console.clear() method clears the console.

        Usage::

          page.js.console.clear

        `Related Pages <https://www.w3schools.com/jsref/met_console_clear.asp>`_

        :return: The Javascript String used to clear the console (F12 in standard browsers).
        """
        return JsFncs.JsFunction("console.clear()")

    def log(self, data: Union[str, primitives.JsDataModel], js_conv_func: Optional[Union[str, list]] = None,
            skip_data_convert: bool = False):
        """The console.log() method writes a message to the console.

        Usage::

          page.js.console.log("Test")

        `Related Pages <https://www.w3schools.com/jsref/met_console_log.asp>`_

        :param data: The Javascript fragment
        :param js_conv_func: Optional. A specific JavaScript data conversion function
        :param skip_data_convert: Optional. Flag to specify to the framework if a Json conversion is needed

        :return: The Javascript String used to clear the console (F12 in standard browsers)
        """
        if skip_data_convert:
            return JsFncs.JsFunction(_CONSOLE_LOG_EXPR.format(data))

        if isinstance(data, list):
            data = JsUtils.jsWrap(JsUtils.jsConvertFncs(data, toStr=True))
        # display directly the content of the component
        if hasattr(data, 'dom'):
            return JsFncs.JsFunction(_CONSOLE_LOG_EXPR.format(JsUtils.jsConvertData(data.dom.content, js_conv_func)))

        return JsFncs.JsFunction(_CONSOLE_LOG_EXPR.format(JsUtils.jsConvertData(data, js_conv_func)))

    def info(self, data: Union[str, primitives.JsDataModel], js_conv_func: Optional[Union[str, list]] = None):
        """The console.info() method writes a message to the console.

        `Related Pages <https://www.w3schools.com/jsref/met_console_info.asp>`_

        :param data: The Javascript fragment
        :param js_conv_func: Optional. A specific JavaScript data conversion function

        :return: The Javascript String used to clear the console (F12 in standard browsers)
        """
        return JsFncs.JsFunction("console.info(%s)" % JsUtils.jsConvertData(data, js_conv_func))

    def warn(self, data: Union[str, primitives.JsDataModel], js_conv_func: Optional[Union[str, list]] = None):
        """The console.warn() method writes a warning to the console.

        `Related Pages <https://www.w3schools.com/jsref/met_console_warn.asp>`_

        :param data: The Javascript fragment
        :param js_conv_func: Optional. A specific JavaScript data conversion function

        :return: The Javascript String used to clear the console (F12 in standard browsers)
        """
        return JsFncs.JsFunction("console.warn(%s)" % JsUtils.jsConvertData(data, js_conv_func))

    def error(self, data: Union[str, primitives.JsDataModel], js_conv_func: Optional[Union[str, list]] = None):
        """The console.error() method writes an error message to the console.

        `Related Pages <https://www.w3schools.com/jsref/met_console_error.asp>`_

        :param data: The Javascript fragment
        :param js_conv_func: Optional. A specific JavaScript data conversion function

        :return: The Javascript String used to clear the console (F12 in standard browsers)
        """
        return JsFncs.JsFunction("console.error(%s)" % JsUtils.jsConvertData(data, js_conv_func))

    def table(self, data: Union[str, primitives.JsDataModel], js_header: Optional[list] = None) -> JsFncs.JsFunction:
        """The console.table() method writes a table in the console view.

        `Related Pages <https://www.w3schools.com/jsref/met_console_table.asp>`_

        :param data: The data to fill the table with
        :param js_header: Optional. An array containing the names of the columns to be included in the table

        :return: The Javascript String used to clear the console (F12 in standard browsers).
        """
        if js_header is not None:
            return JsFncs.JsFunction("console.table(%s, %s)" % (data, js_header))

        return JsFncs.JsFunction("console.table(%s)" % data)

    def time(self, html_code: Union[str, primitives.JsDataModel]) -> JsNumber.JsNumber:
        """The console.time() method starts a timer in the console view.

        `Related Pages <https://www.w3schools.com/jsref/met_console_time.asp>`_

        :param html_code: Use the label parameter to give the timer a name

        :return: A Python Javascript Number.
        """
        return JsNumber.JsNumber("console.time('%s')" % html_code, is_py_data=False)

    def timeEnd(self, html_code: Union[str, primitives.JsDataModel]):
        """The console.timeEnd() method ends a timer, and writes the result in the console view.

        `Related Pages <https://www.w3schools.com/jsref/met_console_timeend.asp>`_

        :param html_code: The name of the timer to end

        :return: The Javascript String used to clear the console (F12 in standard browsers).
        """
        return JsFncs.JsFunction("console.timeEnd('%s')" % html_code)

    def _assert(self, data: Union[str, primitives.JsDataModel], info: str,
                js_conv_func: Optional[Union[str, list]] = None) -> JsFncs.JsFunction:
        """The console.assert() method writes a message to the console, but only if an expression evaluates to false.

        `Related Pages <https://www.w3schools.com/jsref/met_console_assert.asp>`_

        :param data: The Javascript fragment
        :param info: The JavaScript result
        :param js_conv_func: Optional. A specific JavaScript data conversion function
        """
        return JsFncs.JsFunction("console.assert(%s, '%s')" % (JsUtils.jsConvertData(data, js_conv_func), info))

    def tryCatch(self, js_funcs: Union[str, list], js_funcs_errs: Union[str, list] = "console.warn(err.message)",
                 profile: Optional[Union[dict, bool]] = False):
        """Javascript Try Catch Exceptions.

        `Related Pages <https://www.w3schools.com/jsref/jsref_obj_error.asp>`_

        :param js_funcs: The Javascript functions
        :param js_funcs_errs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage

        :return: The Javascript String used to clear the console (F12 in standard browsers)
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        return JsFncs.JsFunction(
            "try{%s} catch(err){%s}" % (JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile), js_funcs_errs))

    def perf(self, js_code: str, label: Optional[str] = None):
        """Shortcut function to display performances from a variable.
        The variable must be global. Namely the name should start with window.

        :param js_code: The variable var name use to compute the performance
        :param label: Optional. The description
        """
        if label is not None:
            return JsFncs.JsFunction("console.log('%s' + (performance.now() - %s) + 'ms')" % (label, js_code))

        return JsFncs.JsFunction("console.log((performance.now() - %s) + 'ms')" % js_code)

    def service(self, msg: str, headers: Optional[dict] = None):
        """Send logs to the backend.

        :param msg: The log message to be sent to the backend
        :param headers: the service headers
        """
        from epyk import LOG_SERVICE

        if LOG_SERVICE is None:
            raise ValueError("Log service must be defined pk.LOG_SERVICE = <service_url>")

        return self.page.js.post(LOG_SERVICE, {"content": msg}, headers=headers, asynchronous=True)


class JsJson:
    """Wrapper around the Javascript Json module.

    This wrapper will only wrapper the different functions available in the underlying library.
    The documentation can be found in each function or are available on the Javascript Official documentation.

    `Related Pages <https://www.w3schools.com/js/js_json_intro.asp>`_
    """

    def parse(self, data: Union[str, primitives.JsDataModel],
              js_result_func: Optional[str] = None, js_conv_func: Optional[Union[str, list]] = None) -> JsFncs.JsFunction:
        """Parses a JSON string and returns a JavaScript object.

        `Related Pages <https://www.w3schools.com/js/js_json_parse.asp>`_
        `Related Pages <https://www.w3schools.com/jsref/jsref_parse_json.asp>`_

        :param data: A String corresponding to a JavaScript object
        :param js_result_func: Optional. A function used to transform the result. The function is called for each item.
          Any nested objects are transformed before the parent
        :param js_conv_func: Optional. A specific JavaScript data conversion function

        :return: The Javascript string method
        """
        data = JsUtils.jsConvertData(data, js_conv_func)
        if js_result_func is not None:
            return JsFncs.JsFunction("JSON.parse(%s, %s)" % (data, js_result_func))

        return JsFncs.JsFunction("JSON.parse(%s)" % data)

    def stringify(self, data: Union[str, primitives.JsDataModel],
                  replacer=None, space: int = 0, js_conv_func: Optional[Union[str, list]] = None) -> JsString.JsString:
        """The JSON.stringify() method converts JavaScript objects into strings.
        `Related Pages <https://www.w3schools.com/js/js_json_stringify.asp>`_

        :param data: The value to convert to a string.
        :param replacer: Optional. Either a function or an array used to transform the result.
                                   The replacer is called for each item.
        :param space: Optional. Either a String or a Number. A string to be used as white space (max 10 characters),
          or a Number, from 0 to 10, to indicate how many space characters to use as white space.
        :param js_conv_func: Optional. A specific JavaScript data conversion function.

        :return: The Javascript string method.
        """
        return JsString.JsString(
            "JSON.stringify(%s, %s, %s)" % (
                JsUtils.jsConvertData(data, js_conv_func), json.dumps(replacer), space), is_py_data=False)


class JsScreen:

    @property
    def availHeight(self) -> JsNumber.JsNumber:
        """The availHeight property returns the height of the user's screen, in pixels, minus interface features
        like the Windows Task bar.

        `Related Pages <https://www.w3schools.com/jsref/prop_screen_availheight.asp>`_
        """
        return JsNumber.JsNumber("screen.availHeight")

    @property
    def availWidth(self) -> JsNumber.JsNumber:
        """The availWidth property returns the width of the user's screen, in pixels, minus interface features like the
        Windows Task bar.

        `Related Pages <https://www.w3schools.com/jsref/prop_screen_availwidth.asp>`_
        """
        return JsNumber.JsNumber("screen.availWidth")

    @property
    def colorDepth(self) -> JsNumber.JsNumber:
        """The colorDepth property returns the bit depth of the color palette for displaying images (in bits per pixel).

        `Related Pages <https://www.w3schools.com/jsref/prop_screen_colordepth.asp>`_
        """
        return JsNumber.JsNumber("screen.colorDepth")

    @property
    def height(self) -> JsNumber.JsNumber:
        """The height property returns the total height of the user's screen, in pixels.

        `Related Pages <https://www.w3schools.com/jsref/prop_screen_height.asp>`_
        """
        return JsNumber.JsNumber("screen.height")

    @property
    def pixelDepth(self) -> JsNumber.JsNumber:
        """The pixelDepth property returns the color resolution (in bits per pixel) of the visitor's screen.

        `Related Pages <https://www.w3schools.com/jsref/prop_screen_pixeldepth.asp>`_
        """
        return JsNumber.JsNumber("screen.pixelDepth")

    @property
    def width(self) -> JsNumber.JsNumber:
        """The width property returns the total width of the user's screen, in pixels.

        `Related Pages <https://www.w3schools.com/jsref/prop_screen_width.asp>`_
        """
        return JsNumber.JsNumber("screen.width")
