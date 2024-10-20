#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Optional, Any, Type, Callable, List, Union, Tuple
from epyk.core.py import primitives
from epyk.core.py import types

from epyk.core.js.primitives import JsArray
from epyk.core.js.primitives import JsDate
from epyk.core.js.primitives import JsObject
from epyk.core.js.primitives import JsNumber
from epyk.core.js.primitives import JsString
from epyk.core.js.primitives import JsBoolean

from epyk.core.js.objects import JsIntersectionObserver
from epyk.core.js.objects import JsNodeDom
from epyk.core.js.objects import JsData
from epyk.core.js.objects import JsEvents

from epyk.core.js import JsUtils


class JsVoid(primitives.JsDataModel):
    def __init__(self, data: Any):
        self._data = data

    def __add__(self, other):
        """Add two JavaScript expressions.

        :param other: A second expression
        :return: A new JavaScript expression
        """
        if hasattr(other, "toStr"):
            other = other.toStr()
        return JsVoid("%s;%s" % (self._data, other))

    def toStr(self):
        return self._data


class JsPromiseRecords(primitives.JsDataModel):

    def __init__(self, promise):
        self.promise = promise
        self.page = promise.page

    def get(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
        """

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self.promise.then("function(data){%s}" % JsUtils.jsConvertFncs(js_funcs or [], toStr=True, profile=profile))
        return self

    def cast(self, columns: list, to: str = "float", profile: types.PROFILE_TYPE = None):
        """

        :param columns:
        :param to: Optional.
        :param profile: Optional. A flag to set the component performance storage.
        """
        cast_cols = {}
        str_frg = []
        if not isinstance(to, dict):
            for c in columns:
                cast_cols[c] = to
        else:
            cast_cols = to
        for col, kind in cast_cols.items():
            if kind == "float":
                str_frg.append("row['%(col)s'] = parseFloat(row['%(col)s'])" % {"col": col})
            elif kind == "int":
                str_frg.append("row['%(col)s'] = parseInt(row['%(col)s'])" % {"col": col})
        return self.row(str_frg, profile=profile)

    def row(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = False):
        """

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        if not isinstance(js_funcs, list):
            js_funcs = []
        self.promise.then(
            "function(data){let result = []; data.forEach(function(row){%s; result.push(row)}); return result}" % JsUtils.jsConvertFncs(
                js_funcs or [], toStr=True, profile=profile))
        return self

    def filterCol(self, column: types.JS_DATA_TYPES,
                  value: types.JS_DATA_TYPES,
                  operator: str = "==", keep: bool = True):
        """

        :param column:
        :param value:
        :param operator: Optional.
        :param keep: Optional.
        """
        column = JsUtils.jsConvertData(column, None)
        value = JsUtils.jsConvertData(value, None)
        if not keep:
            self.promise.then(
                "function(data){let result = []; data.forEach(function(row){if(!(row[%s] %s %s)){result.push(row)}}); return result}" % (
                column, operator, value))
        else:
            self.promise.then(
                "function(data){let result = []; data.forEach(function(row){if(row[%s] %s %s){result.push(row)}}); return result}" % (
                column, operator, value))
        return self

    def toStr(self):
        return self.promise.toStr()

    def __str__(self):
        return self.toStr()


class JsPromise:

    def __init__(self, data: types.JS_DATA_TYPES, profile: types.PROFILE_TYPE = False,
                 async_await: bool = False, page = None):
        self.data, self.profile, self.async_await, self.page = data, profile, async_await, page
        self.__thens, self.__catch = [], []

    @staticmethod
    def new(data: types.JS_DATA_TYPES, profile: types.PROFILE_TYPE = False, async_await: bool = False, page = None):
        """

        :param data:
        :param profile: Optional. A flag to set the component performance storage
        :param async_await: Optional.
        :param page: Optional. Page context
        """
        return JsPromise("new Promise(%s)" % data, profile=profile, async_await=async_await, page=page)

    def set(self, js_code: str, async_await: bool = None):
        """

        :param js_code:
        :param async_await:
        """
        if async_await is None:
            async_await = self.async_await
        if async_await:
            self.data = "let %s = await %s" % (js_code, self.data)
        else:
            self.data = "let %s = %s" % (js_code, self.data)
        return self

    def then(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, js_code: str = "data"):
        """Add a new post-processing step to a then statement.

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param js_code: Optional. The variable name created in the Javascript (default response)
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        str_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
        if "=>" in str_funcs:
            self.__thens.append(str_funcs)
        elif str_funcs.strip().startswith("function("):
            self.__thens.append(str_funcs)
        else:
            self.__thens.append("(%s) => {%s}" % (js_code, str_funcs))
        return self

    def csvRows(
            self, js_funcs: types.JS_FUNCS_TYPES = None, profile: types.PROFILE_TYPE = None, js_code: str = "response"):
        """

        :param js_funcs: Optional. The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param js_code: Optional. The variable name created in the Javascript (default response)
        """
        js_funcs = js_funcs or []
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self.then(["function(%s){return %s.text()}" % (js_code, js_code)], profile)
        return self.then([
                             "function(data){let result = []; data.split('\\n').forEach(function(line){let row = line.split(','); %s; result.push(row)}); return result}" % JsUtils.jsConvertFncs(
                                 js_funcs, toStr=True, profile=profile)], profile)

    def csvtoRecords(
            self, js_funcs: types.JS_FUNCS_TYPES = None, profile: types.PROFILE_TYPE = None, js_code: str = "response"):
        """

        :param js_funcs: Optional. The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param js_code: Optional. The variable name created in the Javascript (default response)
        """
        js_funcs = js_funcs or []
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self.then(["function(%s){ return %s.text()}" % (js_code, js_code)], profile)
        return JsPromiseRecords(self.then(['''function(%s){
let fileContent = %s.split(/\\r?\\n/); let data = []; let fileHeader = fileContent[0].split(',');
for (var i=1; i < fileContent.length; i++){
  let splitLine = fileContent[i].split(','); let row = {}; fileHeader.forEach(function(h, j){row[h] = splitLine[j]}) 
  %s; data.push(row)}; return data}''' % (
            js_code, js_code, JsUtils.jsConvertFncs(js_funcs or [], toStr=True, profile=profile))], profile))

    def catch(self, js_funcs: types.JS_FUNCS_TYPES):
        """

        :param js_funcs: The Javascript functions
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self.__catch.extend(js_funcs)
        return self

    def headers(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
        """Allow actions on the response headers.

        Usage::

            page.body.onReady([
                page.js.console.log("Start Call"),
                page.js.fetch(urls.AGGRID_OLYMPIC_WINNERS).headers([
                    page.js.console.log(pk.events.header)
                ]).json().process(...).then([page.js.console.log("Completed")])])

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        return self.then("function(response){let headers = response.headers; %s; return response}" % JsUtils.jsConvertFncs(js_funcs or [], toStr=True, profile=profile))

    def json(self):
        """Get the json response once received"""
        return self.then("(response) => response.json()")

    def process(self, callback: Callable):
        """

        :param callback:
        """
        return self.then(JsUtils.jsConvertData(callback(JsObject.JsObject.get("data")), None))

    def onSuccess(self, js_funcs: types.JS_FUNCS_TYPES = None, profile: types.PROFILE_TYPE = None):
        """Shortcut to replicated post and get requests
v
        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        return self.json().then(
            "function(data){%s}" % JsUtils.jsConvertFncs(js_funcs or [], toStr=True, profile=profile))

    @property
    def r(self):
        return self.toStr()

    def toStr(self):
        result = [str(self.data)]
        if self.__thens:
            for then_step in self.__thens:
                result.append("then(%s)" % then_step)
        if self.__catch:
            result.append(
                "catch(function(error){%s})" % JsUtils.jsConvertFncs(self.__catch, toStr=True, profile=self.profile))
        return ".".join(result)

    def cache(self, name: str, type: str = "local"):
        """Cache data from the promise.

        :param name: Cache name
        :param type: Optional. Type of cache to used (default local)
        """
        return self.then([self.page.js.storage.from_config(
            {"code": name, "value": JsUtils.jsWrap("data"), "type": type}), "return data"])

    def emit(self, name: str, targets: list = None, bubbles: bool = True,
             cancelable: bool = False, defaultPrevented: bool = False):
        """Emit a signal during the promise process to trigger some sub processes for defined target components.

        :param name: Signal's name
        :param targets: Optional. List of HTML components to get the signal
        :param bubbles: Optional. A boolean value, which is true if the event bubbles up through the DOM tree
        :param cancelable: Optional. make the event cancelable
        :param defaultPrevented: Optional. A boolean value indicating whether or not the call to Event.preventDefault() canceled the event
        """
        options = []
        for k, v in {
            "bubbles": bubbles, "detail": JsUtils.jsWrap("data", None),
            "cancelable": cancelable, "defaultPrevented": defaultPrevented}.items():
            options.append("%s: %s" % (k, JsUtils.jsConvertData(v, None)))
        name = JsUtils.jsConvertData(name, None)
        if targets:
            s_targets = ["%s.dispatchEvent(evt)" % t.dom.varId for t in targets]
            return self.then("let evt = new CustomEvent(%s, {%s}); %s; return data" % (name, ",".join(options), ";".join(s_targets)))

        return self.then("let evt = new CustomEvent(%s, {%s}); document.dispatchEvent(evt); return data" % (name, ",".join(options)))

    def __str__(self):
        return self.toStr()


class XMLHttpRequestErrors:

    def __init__(self, onerrors: list, page: primitives.PageModel, http_request):
        self.__onerrors = onerrors
        self.page = page
        self._http = http_request
        self.profile = None

    def e404(self, js_funcs: types.JS_FUNCS_TYPES = None, default: bool = True,
             profile: types.PROFILE_TYPE = None):
        """404 Not Found.

        The HTTP 404 Not Found response status code indicates that the server cannot find the requested resource.
        Links that lead to a 404 page are often called broken or dead links and can be subject to link rot.

        :param js_funcs: Javascript functions
        :param default: Optional. Use the default messages
        :param profile: Optional. A flag to set the component performance storage
        """
        js_funcs = list(js_funcs or [])
        if default:
            js_funcs.append(self.page.js.msg.text(
                "Service [%s] not found" % self._http.url,
                cssAttrs={"background": self.page.theme.danger.base, 'color': 'white'}))
        self.__onerrors.append("if(%s == 404){%s}" % (
            self._http.status, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))
        return self._http

    def e405(self, js_funcs: types.JS_FUNCS_TYPES = None, default: bool = True,
             profile: types.PROFILE_TYPE = None):
        """405 Method Not Allowed.

        The HyperText Transfer Protocol (HTTP) 405 Method Not Allowed response status code indicates that the server knows
        the request method, but the target resource doesn't support this method.

        :param js_funcs: Javascript functions
        :param default: Optional. Use the default messages
        :param profile: Optional. A flag to set the component performance storage
        """
        js_funcs = list(js_funcs or [])
        if default:
            js_funcs.append(
                self.page.js.msg.text("Service [%s] failed to return response" % self._http.url,
                                      cssAttrs={"background": self.page.theme.danger.base, 'color': 'white'}))
        self.__onerrors.append("if(%s == 405){%s}" % (
            self._http.status, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))
        return self._http

    def e200(self, js_funcs: types.JS_FUNCS_TYPES = None, default: bool = True,
             profile: types.PROFILE_TYPE = None):
        """

        :param js_funcs: Javascript functions
        :param default: Optional. Use the default messages
        :param profile: Optional. A flag to set the component performance storage
        """
        js_funcs = list(js_funcs or [])
        if default:
            js_funcs.append(
                self.page.js.msg.text("Service [%s] completed successfully" % self._http.url,
                                      cssAttrs={"background": self.page.theme.success.base, 'color': 'white'}))
        self.__onerrors.append(
            "if(%s == 200){%s}" % (self._http.status, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))
        return self._http

    def commons(self, js_funcs: types.JS_FUNCS_TYPES = None, default: bool = True,
                profile: types.PROFILE_TYPE = None):
        """

        :param js_funcs: Javascript functions
        :param default: Optional. Use the default messages
        :param profile: Optional. A flag to set the component performance storage
        """
        self.e405(js_funcs, default, profile)
        self.e404(js_funcs, default, profile)
        self.e200(js_funcs, default, profile)
        return self._http


class XMLHttpRequest:

    def __init__(self, page: Optional[primitives.PageModel], js_code: str, method_type: Optional[str],
                 url: Optional[str], data: JsData.Datamap = None, asynchronous: bool = False):
        self.data = JsData.Datamap() if data is None else data
        self.page, self.__headers, self.url = page, {}, url
        self.__mod_name, self.__mod_path, self.method, self.__data_ref = None, None, method_type, "data"
        self.__req_success, self.__req_fail, self.__req_send, self.__req_end = None, None, None, None
        self.__on, self.__url, self.__cache, self.__headers_ref = {}, url, {}, "headers"
        self.__stringify = True
        self.__url_prefix, self.__responseType = "", 'json'
        self.varId, self.profile, self.timeout, self.asynchronous = js_code, False, None, asynchronous
        if url is not None:
            self.open(method_type, url)

    @property
    def URL(self):
        """Get the url requested"""
        return self.__url

    @URL.setter
    def URL(self, value: Any):
        self.__url = value

    @property
    def response(self) -> str:
        """Response response variable reference on the JavaScript side - default data"""
        return self.__data_ref

    @response.setter
    def response(self, value: str):
        self.__data_ref = value

    @property
    def headers(self) -> str:
        """Response headers variable reference on the JavaScript side - default headers"""
        return self.__headers_ref

    @headers.setter
    def headers(self, value: str):
        self.__headers_ref = value

    def set_cache(self, name: str = None, type: str = None, data: Optional[dict] = None,
                  components: Optional[Union[Tuple[primitives.HtmlModel, str], List[primitives.HtmlModel]]] = None,
                  missing: List[str] = None, exists: List[str] = None):
        """Add a custom caching dimension to the XMLHttpRequest.
        It is still possible to tru to

        :param name: The cache name
        :param keys: The keys for the cache - The url will be used otherwise
        :param type: The cache type
        """
        setOnce = {}
        if missing:
            setOnce["missing"] = missing
        if exists:
            setOnce["exists"] = exists
        self.__cache = {"name": name, "data": data, "components": components, "type": type, "setOnce": setOnce}
        return self

    def get_response(self, data_ref: str = None, keys: List[str] = None) -> str:
        """Get a value from the response.

        :param data_ref:
        :param keys:
        """
        ref = data_ref or self.__data_ref
        if keys is not None:
            if len(keys) == 1:
                return "%s['%s']" % (ref, keys[0])

            return "%s?.%s" % (ref, "?.".join(["['%s']" % k for k in keys]))

        return ref

    @classmethod
    def get(cls, js_code: str):
        """Interface to the Javascript Object primitive.

        :param js_code: The variable name on tje JavaScript side

        :return: The requested Python JsObject primitive.
        """
        return XMLHttpRequest(None, js_code, None, None)

    @property
    def readyState(self) -> JsNumber.JsNumber:
        """The XMLHttpRequest.readyState property returns the state an XMLHttpRequest client is in.

        `Ready State <https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/readyState>`_
        """
        return JsNumber.JsNumber("%s.readyState" % self.varId)

    @property
    def status(self) -> JsNumber.JsNumber:
        """The read-only XMLHttpRequest.status property returns the numerical HTTP status code of the XMLHttpRequest's
        response.

        `Status <https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/status>`_
        """
        return JsNumber.JsNumber("%s.status" % self.varId)

    def responseType(self, value: Optional[str] = None) -> JsString.JsString:
        """The XMLHttpRequest property responseType is an enumerated string value specifying the type of data contained in
        the response.

        `Response Type <https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/responseType>`_

        :param value: Optional. The response type
        """
        if value is not None:
            self.__responseType = value
            return self

        return JsString.JsString("%s.responseType" % self.varId, is_py_data=False)

    @property
    def responseText(self) -> JsString.JsString:
        """The read-only XMLHttpRequest property responseText returns the text received from a server following a request
        being sent.

        `Response Text <https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/responseText>`_
        """
        return JsString.JsString("%s.responseText" % self.varId, is_py_data=False)

    def abort(self):
        """The abort event is fired when a request has been aborted, for example because the program called
        XMLHttpRequest.abort().

        `Abort Event <https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/abort_event>`_
        """

    def addEventListener(self, event: str, js_funcs: types.JS_FUNCS_TYPES, options: types.OPTION_TYPE = None):
        """The EventTarget method addEventListener() sets up a function that will be called whenever the specified event
        is delivered to the target.

        Common targets are Element, Document, and Window, but the target may be any object that supports
        events (such as XMLHttpRequest).

        `Error Event <https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/error_event>`_
        `addEventListener <https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener>`_

        :param event: A case-sensitive string representing the event type to listen for
        :param js_funcs: Optional. The Javascript functions
        :param options: Optional. Specific Python options available for this component
        """

    def open(self, method_type: str, url: str, _async: bool = True, user: Optional[str] = None,
             password: Optional[str] = None):
        """The XMLHttpRequest method open() initializes a newly-created request, or re-initializes an existing one.

        `Open <https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/open>`_

        :param method_type: The HTTP request method to use, such as "GET", "POST", "PUT", "DELETE", etc. Ignored for non-HTTP(S) URLs
        :param url: A DOMString representing the URL to send the request to
        :param _async: Optional. Defaulting to true. Indicating whether or not to perform the operation asynchronously
        :param user: Optional. The optional user name to use for authentication purposes; by default, this is the null value
        :param password: Optional. The optional password to use for authentication purposes; by default, this is the null value
        """
        self.url, self.method = url, method_type
        return self

    def setHeaders(self, headers: dict):
        """The XMLHttpRequest method setRequestHeader() sets the value of an HTTP request header.

        `Set Request Header <https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/setRequestHeader>`_

        :param headers: The different attributes to be added to the header
        """
        self.__headers.update(headers)
        return self

    def setRequestHeader(self, name: str, value: str):
        """The XMLHttpRequest method setRequestHeader() sets the value of an HTTP request header.

        `Set Request Header <https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/setRequestHeader>`_

        :param name: The header name
        :param value: The header value
        """
        self.__headers[name] = value
        return self

    def onSuccess(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, data_ref: str = None):
        """The XMLHttpRequestEventTarget.onload is the function called when an XMLHttpRequest transaction completes
        successfully.

        callback is the function to be executed when the request completes successfully.
        It receives a ProgressEvent object as its first argument.
        The value of this (i.e. the context) is the same XMLHttpRequest this callback is related to.

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param data_ref: Optional. JavaScript variable name for the main data in the function (default data)
        """
        if profile is not None:
            self.profile = profile
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self.response = self.get_response(data_ref)
        if self.profile is not None and self.profile:
            js_funcs.insert(
                0, "console.log('Start[SUCCESS]: '+ (performance.now() - t_post%s)+ ' ms')" % JsUtils.PROFILE_COUNT)
            js_funcs.append(
                "console.log('End[SUCCESS]: '+ (performance.now() - t_post%s)+ ' ms')" % JsUtils.PROFILE_COUNT)
        if self.__req_success is None:
            self.__req_success = js_funcs
        else:
            self.__req_success.extend(js_funcs)
        return self

    def onSuccessIf(self, rules: list, else_: types.JS_FUNCS_TYPES = None, profile: types.PROFILE_TYPE = None,
                    data_ref: str = None):
        """If statement on the XMLHttpRequest result.

        :param rules:
        :param else_:
        :param profile: Optional. A flag to set the component performance storage
        :param data_ref: Optional. JavaScript variable name for the main data in the function (default data)
        """
        js_expr = []
        if profile is not None:
            self.profile = profile
        for i, rule in enumerate(rules):
            condition, js_funcs = rule
            if i == 0:
                js_expr.append("if(%s){%s}" % (
                    JsUtils.jsConvertData(condition, None),
                    JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile or self.profile)))
            else:
                js_expr.append("elif(%s){%s}" % (
                    JsUtils.jsConvertData(condition, None),
                    JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile or self.profile)))
        if else_ is not None:
            if not isinstance(else_, list):
                else_ = [else_]
            js_expr.append("else{%s}" % JsUtils.jsConvertFncs(else_, toStr=True, profile=profile or self.profile))
        self.response = self.get_response(data_ref)
        if self.profile is not None and self.profile:
            js_expr.insert(
                0, "console.log('Start[SUCCESS]: '+ (performance.now() - t_post%s)+ ' ms')" % JsUtils.PROFILE_COUNT)
            js_expr.append(
                "console.log('End[SUCCESS]: '+ (performance.now() - t_post%s)+ ' ms')" % JsUtils.PROFILE_COUNT)
        if self.__req_success is None:
            self.__req_success = js_expr
        else:
            self.__req_success.extend(js_expr)
        return self

    def onSuccessHas(self, keys: List[str], js_funcs: types.JS_FUNCS_TYPES, comparator: Union[dict, str] = None,
                    profile: types.PROFILE_TYPE = None, data_ref: str = None):
        """Condition for a response object value of the XMLHttpRequest.

        :param keys: The keys / depth defined in the response
        :param js_funcs: The Javascript functions
        :param comparator: Optional. The comparator rule. By default it will just check if key exist
        :param profile: Optional. A flag to set the component performance storage
        :param data_ref: Optional. JavaScript variable name for the main data in the function (default data)
        """
        if profile is not None:
            self.profile = profile
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        if comparator is not None:
            if isinstance(comparator, dict):
                value = JsUtils.jsConvertData(comparator.get("value", ""), None)
                operator = comparator.get("operator", "==")
            else:
                value = JsUtils.jsConvertData(comparator, None)
                operator = "=="
            js_expr = [
                "if((typeof(%s) !== 'undefined') && (%s %s %s)){%s}" % (
                    self.get_response(data_ref, keys), self.get_response(data_ref, keys), operator, value,
                    JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile or self.profile))]
        else:
            js_expr = [
                "if(typeof(%s) !== 'undefined'){%s}" % (
                    self.get_response(data_ref, keys),
                    JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile or self.profile))]
        if self.profile is not None and self.profile:
            js_expr.insert(
                0, "console.log('Start[SUCCESS]: '+ (performance.now() - t_post%s)+ ' ms')" % JsUtils.PROFILE_COUNT)
            js_expr.append(
                "console.log('End[SUCCESS]: '+ (performance.now() - t_post%s)+ ' ms')" % JsUtils.PROFILE_COUNT)
        if self.__req_success is None:
            self.__req_success = js_expr
        else:
            self.__req_success.extend(js_expr)
        return self

    def onerror(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
        """The XMLHttpRequestEventTarget.onerror is the function called when an XMLHttpRequest transaction fails due to
        an error.

        `Error Event <https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/error_event>`_

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        if profile is not None:
            self.profile = profile
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        if self.__on.get("onerror", None) is None:
            self.__on["onerror"] = js_funcs
        else:
            self.__on["onerror"] = js_funcs
        return self

    def onFail(self, js_funcs: types.JS_FUNCS_TYPES, status_code: int = 404, profile: types.PROFILE_TYPE = None):
        """The loaded event is fired when a request has completed, whether successfully (after load) or unsuccessfully
        (after abort or error).

        `Loadend Event <https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/loadend_event>`_

        :param js_funcs: The Javascript functions
        :param status_code: Optional. The status code for the failure condition
        :param profile: Optional. A flag to set the component performance storage
        """
        if "onloadend" not in self.__on:
            self.__on["onloadend"] = []
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self.__on["onloadend"].append("if(%s.status == %s){%s}" % (
            self.varId, status_code, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile or self.profile)))
        return self

    @property
    def errors(self) -> XMLHttpRequestErrors:
        """ """
        if self.__on.get("onloadend") is None:
            self.__on["onloadend"] = []
        return XMLHttpRequestErrors(self.__on["onloadend"], self.page, self)

    def ontimeout(self, js_funcs: types.JS_FUNCS_TYPES, timeout: int = 2000, profile: types.PROFILE_TYPE = None):
        """The timeout event is fired when progression is terminated due to preset time expiring.

        `Timeout <https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/timeout>`_

        :param js_funcs: The Javascript functions
        :param timeout: Optional. Time in milliseconds
        :param profile: Optional. A flag to set the component performance storage
        """
        if profile is not None:
            self.profile = profile
        self.timeout = timeout
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self.__on["ontimeout"] = js_funcs
        return self

    def onloadend(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
        """Fired when a request has completed, whether successfully (after load) or unsuccessfully.

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        if profile is not None:
            self.profile = profile
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self.__on["onloadend"] = js_funcs
        return self

    def onloadstart(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
        """The XMLHttpRequestEventTarget.onloadstart is the function called when an XMLHttpRequest transaction starts
        transferring data.

        :param js_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        if profile is not None:
            self.profile = profile
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self.__on["onloadstart"] = js_funcs
        return self

    def withCredentials(self, flag: bool):
        """The XMLHttpRequest.withCredentials property is a Boolean that indicates whether or not cross-site Access-Control
        requests should be made using credentials such as cookies, authorization headers or TLS client certificates.

        Setting withCredentials has no effect on same-site requests.

        `With Credentials <https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/withCredentials>`_

        :param flag: Flag to specify the use of credentials
        """

    def send(self, json_data: types.JS_DATA_TYPES = None, encode_uri_data: dict = None,
             stringify: bool = None, is_json: bool = True, dataflows: List[dict] = None):
        """The XMLHttpRequest method send() sends the request to the server.
        If the request is asynchronous (which is the default), this method returns as soon as the request is sent and the
        result is delivered using events.
        If the request is synchronous, this method doesn't return until the response has arrived.

        `Send <https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/send>`_

        :param json_data: Optional. JavaScript input data
        :param encode_uri_data: Optional. Encode data for url
        :param stringify: Optional. Force the JavaScript data to be changed to String. Default True
        :param is_json: Optional. Specify the type of data. Default True
        :param dataflows: Optional. Chain of data transformations
        """
        if stringify is not None:
            self.__stringify = stringify
        # Initialize jsonData with potential initial data passed in the constructor
        if json_data:
            if isinstance(json_data, list):
                for obj in json_data:
                    if hasattr(obj, 'options'):
                        self.data.add(obj, is_json=is_json)
                    elif isinstance(obj, tuple):
                        self.data.add(obj[0], obj[1], is_json=is_json)
                    else:
                        self.data.attrs(obj)

            elif isinstance(json_data, dict):
                if is_json:
                    self.data.update(json_data)

                else:
                    for k, v in json_data.items():
                        self.data.attr(k, v)
            else:  # formdata
                self.data = json_data
        if json_data:
            if self.__stringify:
                self.__req_send = "%s.send(JSON.stringify(%s))" % (
                self.varId, JsUtils.dataFlows(self.data, dataflows, self.page))
            else:
                # For data form when dealing with files
                self.__req_send = "%s.send(%s)" % (self.varId, self.data.toStrFormData())
        elif encode_uri_data is not None:
            self.__url_prefix = "?%s" % "&".join(["%s=%s" % (k, v) for k, v in encode_uri_data.items()])
            self.__req_send = "%s.send()" % self.varId
        else:
            self.__req_send = "%s.send()" % self.varId
        return self

    def getResponseHeader(self, headerName: str) -> JsString.JsString:
        """The XMLHttpRequest method getResponseHeader() returns the string containing the text of a particular
        header's value.

        `Mozilla <https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/getResponseHeader>`_

        Usage::

            s_query = web.js.get("/url", data={"value": 45, "ok": "test"})
            b.click([js_query.onSuccess([web.js.console.log(s_query.getResponseHeader("content-type"))])])

        :param headerName: A string indicating the name of the header you want to return the text value of.
        """
        headerName = JsUtils.jsConvertData(headerName, None)
        return JsString.JsString.get("%s.getResponseHeader(%s)" % (self.varId, headerName))

    def getAllResponseHeaders(self) -> JsString.JsString:
        """The XMLHttpRequest method getAllResponseHeaders() returns all the response headers, separated by CRLF, as a
        string, or returns null if no response has been received.

        `Mozilla <https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/getAllResponseHeaders>`_

        Usage::

            s_query = web.js.get("/url", data={"value": 45, "ok": "test"})
            b.click([js_query.onSuccess([web.js.console.log(s_query.getAllResponseHeaders())])])
        """
        return JsString.JsString.get("%s.getAllResponseHeaders()" % self.varId)

    def getResponseHeaders(self) -> JsString.JsString:
        """The XMLHttpRequest method getAllResponseHeaders() returns all the response headers, separated by CRLF, as a
        string, or returns null if no response has been received.

        `Mozilla <https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/getAllResponseHeaders>`_

        Usage::

            s_query = web.js.get("/url", data={"value": 45, "ok": "test"})
            b.click([js_query.onSuccess([web.js.console.log(s_query.getResponseHeaders())])])
        """
        return JsString.JsString.get(r"(function(r){return r.split('\r\n').reduce(function (acc, current, i){var parts = current.split(': ');acc[parts[0]] = parts[1];return acc;}, {})})(%s.getAllResponseHeaders())" % self.varId)

    def toStr(self):
        request = [
            "var %s = new XMLHttpRequest()" % self.varId,
            "%s.responseType = '%s'" % (self.varId, self.__responseType)]
        if self.profile is not None and self.profile:
            request.insert(0, "let t_post%s = performance.now()" % JsUtils.PROFILE_COUNT)
        if self.timeout is not None:
            request.append("%s.timeout = %s" % (self.varId, self.timeout))
        if self.__url_prefix:
            request.append("%s.open(%s, %s+'%s')" % (self.varId, self.method, self.url, self.__url_prefix))
        else:
            request.append("%s.open(%s, %s)" % (self.varId, self.method, self.url))
        for k, v in self.__headers.items():
            request.append("%s.setRequestHeader(%s, %s)" % (
                self.varId, JsUtils.jsConvertData(k, None), JsUtils.jsConvertData(v, None)))
        if self.__req_success is not None:
            if self.__cache and self.page:
                self.__req_success.insert(0, self.page.js.storage.from_config(
                    {"code": self.__cache["name"], "data": self.__cache["data"], "value": JsUtils.jsWrap(self.response),
                     "components": self.__cache["components"], "type": self.__cache["type"]}))
            if self.__req_fail is not None:
                request.append("%s.onload = function(){}" % self.varId)
            else:
                request.append("%(varId)s.onload = function(){let %(dataRef)s = %(varId)s.response; let %(hdrRef)s = %(reshdrs)s; %(jsFncs)s}" % {
                    'varId': self.varId, 'dataRef': self.response, "reshdrs": self.getResponseHeaders().toStr(),
                    'hdrRef': self.headers, 'jsFncs': JsUtils.jsConvertFncs(self.__req_success, toStr=True, profile=self.profile)})
        if self.__req_end is not None:
            request.append("%(varId)s.onloadend = function(){%(jsFncs)s}" % {
                'varId': self.varId, 'jsFncs': JsUtils.jsConvertFncs(self.__req_end, toStr=True, profile=self.profile)})
        for k, fncs in self.__on.items():
            request.append("%(varId)s.%(name)s = function(){%(jsFncs)s}" % {
                'name': k, 'varId': self.varId,
                'jsFncs': JsUtils.jsConvertFncs(fncs, toStr=True, profile=self.profile)})
        if self.__req_send is None:
            raise ValueError("The send method must be called")

        request.append(self.__req_send)
        if self.profile is not None and self.profile:
            JsUtils.PROFILE_COUNT += 1

        if self.__cache and self.page:
            var_cache = self.page.js.storage.from_config({
                "code": self.__cache["name"], "data": self.__cache["data"],
                "components": self.__cache["components"], "type": self.__cache["type"]})
            return self.page.js.if_(
                var_cache, ["let %s = %s" % (self.response, var_cache)] + self.__req_success[1:],
                profile=self.profile).else_(request, profile=self.profile).toStr()

        return ";".join(request)

    def to_promise(self, js_code: str = "pRes") -> JsPromise:
        """Return a promise object from a XMLHttpRequest request

        :param js_code: Optional. The JavaScript variable name defined for this promise
        """
        if self.__req_success is None:
            self.__req_success = []
        self.__req_success.append("if(%(id)s.status == 200){resolve(%(r)s)} else {reject(%(id)s.status)}" % {
            "id": self.varId, "r": self.response})
        if js_code is None:
            return JsPromise.new("function(resolve, reject){%s}" % self.toStr(), page=self.page)

        return JsPromise.new("function(resolve, reject){%s}" % self.toStr(), page=self.page).set(js_code)


class JsObjects:
    def __init__(self, page: primitives.PageModel = None, component: primitives.HtmlModel = None):
        self.page, self.component = page, component

    def __getitem__(self, alias: str):
        """Get a bespoke object.

        :param alias: The variable name on the JavaScript side
        """
        return JsObject.JsObject.get("data")[alias]

    @property
    def this(self) -> JsNodeDom.JsDoms:
        """Interface to the Javascript Object primitive.

        :return: The Javascript "this" object (which is a dom object very often).
        """
        return JsNodeDom.JsDoms.get("this")

    @property
    def result(self) -> JsObject.JsObject:
        """Interface to the Javascript Object primitive.

        :return: The Javascript result object from a post or any other AJAX calls.
        """
        return JsObject.JsObject.get("result")

    @property
    def request(self) -> XMLHttpRequest:
        """Interface to the Javascript Object primitive.

        :return: The Javascript result object from a post or any other AJAX calls.
        """
        return XMLHttpRequest.get("result")

    @property
    def data(self) -> JsObject.JsObject:
        """Interface to the Javascript Object primitive.

        :return: The Javascript data object from a post or any other AJAX calls.
        """
        return JsObject.JsObject.get("data")

    @property
    def value(self) -> JsObject.JsObject:
        """Interface to the Javascript Object primitive.

        :return: The Javascript value in an event
        """
        return JsObject.JsObject.get("value")

    @property
    def mouseEvent(self) -> JsEvents.MouseEvent:
        """Interface to the JavaScript MouseEvents.

        `Mouse Event <https://www.w3schools.com/jsref/obj_mouseevent.asp>`_
        """
        return JsEvents.MouseEvent()

    @property
    def event(self) -> JsEvents.Event:
        """Interface to the JavaScript Events.

        `Event <https://www.w3schools.com/jsref/obj_event.asp>`_
        """
        return JsEvents.Event()

    @property
    def jqThis(self):
        """Interface to the Javascript Object primitive.

        :return: The Javascript "this" object
        """
        from epyk.core.js.packages import JsQuery
        return JsQuery.JQuery(component=self.component, page=self.page, selector="jQuery(this)", set_var=False)

    @classmethod
    def get(cls, js_code: str) -> JsObject.JsObject:
        """Interface to the Javascript Object primitive.

        :param js_code: The variable name

        :return: The requested Python JsObject primitive
        """
        return JsObject.JsObject.get(js_code)

    @classmethod
    def new(cls, data=None, js_code: Optional[str] = None, is_py_data: bool = False,
            page: primitives.PageModel = None) -> JsObject.JsObject:
        """Interface to the Javascript Object primitive.

        :param data: Optional. The value
        :param js_code: Optional. The variable name
        :param is_py_data: Optional. The data type
        :param page: Optional. The underlying page object (the context)

        :return: A Python generic JsObject primitive.
        """
        return JsObject.JsObject.new(data, js_code, is_py_data, page=page)

    def time(self, js_code: str, page: primitives.PageModel = None) -> JsObject.JsObject:
        """Return a time object from the Javascript function performance.now().

        :param js_code: The variable name
        :param page: Optional. The report object
        """
        return JsObject.JsObject.new("performance.now()", js_code, False, page=page)

    @property
    def number(self) -> Type[JsNumber.JsNumber]:
        """Interface to the Javascript Number primitive.

        `Number <https://www.w3schools.com/jsref/jsref_number.asp>`_

        :return: A Python JsNumber primitive.
        """
        return JsNumber.JsNumber

    @property
    def string(self) -> Type[JsString.JsString]:
        """Interface to the Javascript String primitive.

        `String <https://www.w3schools.com/jsref/jsref_obj_string.asp>`_

        :return: A Python JsString primitive.
        """
        return JsString.JsString

    @property
    def list(self) -> Type[JsArray.JsArray]:
        """Interface to the Javascript Array primitive.

        `Array <https://www.w3schools.com/jsref/jsref_obj_array.asp>`_

        :return: A Python JsArray primitive.
        """
        return JsArray.JsArray

    @property
    def array(self) -> Type[JsArray.JsArray]:
        """Interface to the Javascript Array primitive.

        `Array <https://www.w3schools.com/jsref/jsref_obj_array.asp>`_

        :return: A Python JsArray primitive.
        """
        return JsArray.JsArray

    @property
    def date(self) -> Type[JsDate.JsDate]:
        """Interface to the Javascript Date primitive.

        `Date <https://www.w3schools.com/jsref/jsref_obj_date.asp>`_

        :return: A Python JsDate object.
        """
        return JsDate.JsDate

    @property
    def boolean(self) -> Type[JsBoolean.JsBoolean]:
        """Interface to the Javascript Boolean primitive.

        `Boolean <https://www.w3schools.com/jsref/jsref_obj_boolean.asp>`_

        :return: A Python JsBoolean primitive.
        """
        return JsBoolean.JsBoolean

    @property
    def dom(self) -> Type[JsNodeDom.JsDoms]:
        """Interface to the Javascript Dom class.

        :return: A Python Document.
        """
        return JsNodeDom.JsDoms

    @property
    def null(self) -> JsObject.JsObject:
        """Similar as None in Python.

        `datatypes <https://www.w3schools.com/js/js_datatypes.asp>`_

        :return: A Python Js Null object.
        """
        return JsObject.JsObject("null")

    @property
    def undefined(self) -> JsObject.JsObject:
        """Similar as the None in Python.

        `Undefined <https://www.w3schools.com/jsref/jsref_undefined.asp>`_

        :return: A Python Js undefined object.
        """
        return JsObject.JsObject("undefined", is_py_data=False)

    @property
    def NaN(self) -> JsNumber.JsNumber:
        """The NaN property represents "Not-a-Number" value. This property indicates that a value is not a legal number.

        The NaN property is the same as the Number.Nan property.

        `NaN <https://www.w3schools.com/jsref/jsref_number_nan.asp>`_
        `Is NaN <https://www.w3schools.com/jsref/jsref_isnan.asp>`_
        """
        return JsNumber.JsNumber("Number.NaN")

    @property
    def true(self) -> JsBoolean.JsBoolean:
        """Similar as True in Python.

        `Boolean <https://www.w3schools.com/js/js_booleans.asp>`_

        :return: A Python Js True object.
        """
        return JsBoolean.JsBoolean.get('true')

    @property
    def false(self) -> JsBoolean.JsBoolean:
        """Similar as False in Python.

        `Boolean <https://www.w3schools.com/js/js_booleans.asp>`_

        :return: A Python Js False object.
        """
        return JsBoolean.JsBoolean.get('false')

    def record(self, js_code: str) -> JsData.RawData:
        """Get a record object.

        :param js_code: A string with of the existing variable name
        """
        return JsData.RawData.get(page=self.page, js_code=js_code)

    def incr(self, incr: str) -> JsObject.JsObject:
        """Increment a counter.

        :param incr: the variable name used to store the counter
        """
        return JsObject.JsObject("%s++" % incr)

    def function(self, args, returns: str, eval: bool = False) -> JsObject.JsObject:
        """

        :param args:
        :param returns:
        :param eval:
        """
        params, values = [], []
        for i, v in enumerate(args):
            if i > 0:
                params.append("x%s" % i)
            else:
                params.append("x")
            values.append(str(v))
        if eval:
            return JsObject.JsObject("(function(%s){ return eval(%s) })(%s)" % (
                ", ".join(params), returns, ", ".join(values)))

    def entry(self, i: int = 0, entry_code: str = "entry") -> JsIntersectionObserver.IntersectionObserverEntry:
        """Get a specific entry when using a JsIntersectionObserver in a loop.

        :param i: The index entry
        :param entry_code: Optional. The entry reference in the loop. Default entry
        """
        return JsIntersectionObserver.IntersectionObserverEntry("%s[%s]" % (entry_code, i))
