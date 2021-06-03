#!/usr/bin/python
# -*- coding: utf-8 -*-


from epyk.core.js.primitives import JsArray
from epyk.core.js.primitives import JsDate
from epyk.core.js.primitives import JsObject
from epyk.core.js.primitives import JsNumber
from epyk.core.js.primitives import JsString
from epyk.core.js.primitives import JsBoolean

from epyk.core.js.objects import JsNodeDom
from epyk.core.js.objects import JsData
from epyk.core.js.objects import JsEvents

from epyk.core.js import JsUtils


class JsVoid:
  def __init__(self, data):
    self._data = data

  def toStr(self):
    return self._data


class JsObjects:
  def __init__(self, jsObj=None):
    self._jsObj = jsObj

  @property
  def this(self):
    """
    Description:
    -----------
    Interface to the Javascript Object primitive.

    :return: The Javascript "this" object (which is a dom object very often).
    """
    return JsNodeDom.JsDoms.get("this")

  @property
  def result(self):
    """
    Description:
    -----------
    Interface to the Javascript Object primitive.

    :return: The Javascript result object from a post or any other AJAX calls.
    """
    return JsObject.JsObject.get("result")

  @property
  def request(self):
    """
    Description:
    -----------
    Interface to the Javascript Object primitive.

    :return: The Javascript result object from a post or any other AJAX calls.

    :rtype: XMLHttpRequest.
    """
    return XMLHttpRequest.get("result")

  @property
  def data(self):
    """
    Description:
    -----------
    Interface to the Javascript Object primitive.

    :return: The Javascript data object from a post or any other AJAX calls.
    """
    return JsObject.JsObject.get("data")

  @property
  def value(self):
    """
    Description:
    -----------
    Interface to the Javascript Object primitive.

    :return: The Javascript value in a event
    """
    return JsObject.JsObject.get("value")

  @property
  def mouseEvent(self):
    """
    Description:
    -----------
    Interface to the JavaScript MouseEvents.

    Related Pages:

      https://www.w3schools.com/jsref/obj_mouseevent.asp
    """
    return JsEvents.MouseEvent()

  @property
  def event(self):
    """
    Description:
    -----------
    Interface to the JavaScript Events.

    Related Pages:

      https://www.w3schools.com/jsref/obj_event.asp
    """
    return JsEvents.Event()

  @property
  def jqThis(self):
    """
    Description:
    -----------
    Interface to the Javascript Object primitive.

    :return: The Javascript "this" object
    """
    from epyk.core.js.packages import JsQuery
    return JsQuery.JQuery(self._jsObj._src, selector="jQuery(this)", setVar=False)

  @classmethod
  def get(cls, varName):
    """
    Description:
    -----------
    Interface to the Javascript Object primitive

    Attributes:
    ----------
    :param varName: String. Optional. The variable name.

    :return: The requested Python JsObject primitive
    """
    return JsObject.JsObject.get(varName)

  @classmethod
  def new(cls, data=None, varName=None, isPyData=False, report=None):
    """
    Description:
    -----------
    Interface to the Javascript Object primitive.

    Attributes:
    ----------
    :param data: Object. Optional. The value.
    :param varName: String. Optional. The variable name.
    :param isPyData: Boolean. Optional. The data type.
    :param report: Page. Optional. The underlying page object (the context).

    :return: A Python generic JsObject primitive.
    """
    return JsObject.JsObject.new(data, varName, isPyData, report=report)

  def time(self, varName, report=None):
    """
    Description:
    -----------
    Return a time object from the Javascript function performance.now().

    Attributes:
    ----------
    :param varName: String. The variable name.
    :param report: Report. Optional. The report object.
    """
    return JsObject.JsObject.new("performance.now()", varName, False, report=report)

  @property
  def number(self):
    """
    Description:
    -----------
    Interface to the Javascript Number primitive.

    Related Pages:

      https://www.w3schools.com/jsref/jsref_number.asp

    :return: A Python JsNumber primitive.
    """
    return JsNumber.JsNumber

  @property
  def string(self):
    """
    Description:
    -----------
    Interface to the Javascript String primitive.

    Related Pages:

      https://www.w3schools.com/jsref/jsref_obj_string.asp

    :return: A Python JsString primitive.
    """
    return JsString.JsString

  @property
  def list(self):
    """
    Description:
    -----------
    Interface to the Javascript Array primitive.

    Related Pages:

      https://www.w3schools.com/jsref/jsref_obj_array.asp

    :return: A Python JsArray primitive.
    """
    return JsArray.JsArray

  @property
  def array(self):
    """
    Description:
    -----------
    Interface to the Javascript Array primitive.

    Related Pages:

      https://www.w3schools.com/jsref/jsref_obj_array.asp

    :return: A Python JsArray primitive.
    """
    return JsArray.JsArray

  @property
  def date(self):
    """
    Description:
    -----------
    Interface to the Javascript Date primitive.

    Related Pages:

      https://www.w3schools.com/jsref/jsref_obj_date.asp

    :return: A Python JsDate object.
    """
    return JsDate.JsDate

  @property
  def boolean(self):
    """
    Description:
    -----------
    Interface to the Javascript Boolean primitive.

    Related Pages:

      https://www.w3schools.com/jsref/jsref_obj_boolean.asp

    :return: A Python JsBoolean primitive.
    """
    return JsBoolean.JsBoolean

  @property
  def dom(self):
    """
    Description:
    -----------
    Interface to the Javascript Dom class.

    :return: A Python Document.
    """
    return JsNodeDom.JsDoms

  @property
  def null(self):
    """
    Description:
    -----------
    Similar as None in Python.

    Related Pages:

      https://www.w3schools.com/js/js_datatypes.asp

    :return: A Python Js Null object.
    """
    return JsObject.JsObject("null")

  @property
  def undefined(self):
    """
    Description:
    -----------
    Similar as the None in Python.

    Related Pages:

      https://www.w3schools.com/jsref/jsref_undefined.asp

    :return: A Python Js undefined object.
    """
    return JsObject.JsObject("undefined", isPyData=False)

  @property
  def NaN(self):
    """
    Description:
    -----------
    The NaN property represents "Not-a-Number" value. This property indicates that a value is not a legal number.

    The NaN property is the same as the Number.Nan property.

    Related Pages:
      https://www.w3schools.com/jsref/jsref_number_nan.asp
      https://www.w3schools.com/jsref/jsref_isnan.asp
    """
    return JsNumber.JsNumber("Number.NaN")

  @property
  def true(self):
    """
    Description:
    -----------
    Similar as True in Python.

    Related Pages:

      https://www.w3schools.com/js/js_booleans.asp

    :return: A Python Js True object.
    """
    return JsBoolean.JsBoolean.get('true')

  @property
  def false(self):
    """
    Description:
    -----------
    Similar as False in Python.

    Related Pages:

      https://www.w3schools.com/js/js_booleans.asp
    
    :return: A Python Js False object.
    """
    return JsBoolean.JsBoolean.get('false')

  def record(self, varName):
    """
    Description:
    -----------
    Get a record object.

    Attributes:
    ----------
    :param varName: A string with of the existing variable name
    """
    return JsData.RawData.get(self._jsObj, varName)

  def incr(self, incr):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param incr:
    """
    return JsObject.JsObject("%s++" % incr)

  def function(self, args, returns, eval=False):
    params, values = [], []
    for i, v in enumerate(args):
      if i > 0:
        params.append("x%s" % i)
      else:
        params.append("x")
      values.append(str(v))
    if eval:
      return JsObject.JsObject("(function(%s){ return eval(%s) })(%s)" % (", ".join(params), returns, ", ".join(values)))


class JsPromise:

  def __init__(self, jsObj, profile=False, async_await=False):
    self._jsObj, self.profile, self.async_await = jsObj, profile, async_await
    self.__then, self.__catch = [], []

  def then(self, jsFnc):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFnc: String | List. The Javascript functions
    """
    if not isinstance(jsFnc, list):
      jsFnc = []
    self.__then.extend(jsFnc)
    return self

  def catch(self, jsFnc):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFnc: String | List. The Javascript functions
    """
    if not isinstance(jsFnc, list):
      jsFnc = []
    self.__catch.extend(jsFnc)
    return self

  @property
  def r(self):
    return self.toStr()

  def toStr(self):
    result = [str(self._jsObj)]
    if self.__then:
      result.append(
        "then(function(response){%s})" % JsUtils.jsConvertFncs(self.__then, toStr=True, profile=self.profile))
    if self.__catch:
      result.append(
        "catch(function(error){%s})" % JsUtils.jsConvertFncs(self.__catch, toStr=True, profile=self.profile))
    return ".".join(result)

  def __str__(self):
    return self.toStr()


class XMLHttpRequestErrors:

  def __init__(self, onerrors, report, http_request):
    self.__onerrors = onerrors
    self._src = report
    self._http = http_request
    self.profile = None

  def e404(self, jsFncs=None, default=True, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param default: Boolean. Optional. Use the default messages.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    jsFncs = list(jsFncs or [])
    if default:
      jsFncs.append(self._src.js.msg.text(
        "Service [%s] not found" % self._http.url,
        cssAttrs={"background": self._src.theme.danger[1], 'color': 'white'}))
    self.__onerrors.append("if(%s == 404){%s}" % (
      self._http.status, JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile)))
    return self._http

  def e405(self, jsFncs=None, default=True, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param default: Boolean. Optional. Use the default messages.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    jsFncs = list(jsFncs or [])
    if default:
      jsFncs.append(
        self._src.js.msg.text("Service [%s] failed to return response" % self._http.url,
                              cssAttrs={"background": self._src.theme.danger[1], 'color': 'white'}))
    self.__onerrors.append("if(%s == 405){%s}" % (
      self._http.status, JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile)))
    return self._http

  def e200(self, jsFncs=None, default=True, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param default: Boolean. Optional. Use the default messages.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    jsFncs = list(jsFncs or [])
    if default:
      jsFncs.append(
        self._src.js.msg.text("Service [%s] completed successfully" % self._http.url,
                              cssAttrs={"background": self._src.theme.success[1], 'color': 'white'}))
    self.__onerrors.append(
      "if(%s == 200){%s}" % (self._http.status, JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile)))
    return self._http

  def commons(self, jsFncs=None, default=True, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param default: Boolean. Optional. Use the default messages.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    self.e405(jsFncs, default, profile)
    self.e404(jsFncs, default, profile)
    self.e200(jsFncs, default, profile)
    return self._http


class XMLHttpRequest:

  def __init__(self, report, varName, method_type, url, data=None):
    self.data = JsData.Datamap() if data is None else data
    self._src, self.__headers, self.url = report, {}, url
    self.__mod_name, self.__mod_path, self.method = None, None, method_type
    self.__req_success, self.__req_fail, self.__req_send, self.__req_end = None, None, None, None
    self.__on = {}
    self.__url_prefix, self.__responseType = "", 'json'
    self.varId, self.profile, self.timeout = varName, False, None
    if url is not None:
      self.open(method_type, url)

  @classmethod
  def get(cls, varName):
    """
    Description:
    ------------
    Interface to the Javascript Object primitive.

    Attributes:
    ----------
    :param varName: String. The variable name on tje JavaScript side.

    :return: The requested Python JsObject primitive.
    """
    return XMLHttpRequest(None, varName, None, None)

  @property
  def readyState(self):
    """
    Description:
    ------------
    The XMLHttpRequest.readyState property returns the state an XMLHttpRequest client is in.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/readyState
    """
    return JsNumber.JsNumber("%s.readyState" % self.varId)

  @property
  def status(self):
    """
    Description:
    ------------
    The read-only XMLHttpRequest.status property returns the numerical HTTP status code of the XMLHttpRequest's
    response.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/status
    """
    return JsNumber.JsNumber("%s.status" % self.varId)

  @property
  def responseType(self, value=None):
    """
    Description:
    ------------
    The XMLHttpRequest property responseType is an enumerated string value specifying the type of data contained in
    the response.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/responseType

    Attributes:
    ----------
    :param value: String. Optional. The response type.
    """
    if value is not None:
      self.__responseType = value
      return self

    return JsString.JsString("%s.responseType" % self.varId, isPyData=False)

  @property
  def responseText(self):
    """
    Description:
    ------------
    The read-only XMLHttpRequest property responseText returns the text received from a server following a request
    being sent.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/responseText
    """
    return JsString.JsString("%s.responseText" % self.varId, isPyData=False)

  def abort(self):
    """
    Description:
    ------------
    The abort event is fired when a request has been aborted, for example because the program called
    XMLHttpRequest.abort().

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/abort_event
    """

  def addEventListener(self, event, jsFncs, options=None):
    """
    Description:
    ------------
    The EventTarget method addEventListener() sets up a function that will be called whenever the specified event
    is delivered to the target.
    Common targets are Element, Document, and Window, but the target may be any object that supports
    events (such as XMLHttpRequest).

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/error_event
      https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener

    Attributes:
    ----------
    :param event: String. A case-sensitive string representing the event type to listen for.
    :param jsFncs: String | List. Optional. The Javascript functions.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """

  def open(self, method_type, url, _async=True, user=None, password=None):
    """
    Description:
    ------------
    The XMLHttpRequest method open() initializes a newly-created request, or re-initializes an existing one.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/open

    Attributes:
    ----------
    :param method_type: String. The HTTP request method to use, such as "GET", "POST", "PUT", "DELETE", etc. Ignored for non-HTTP(S) URLs.
    :param url: String. A DOMString representing the URL to send the request to.
    :param _async: Boolean. Optional. Defaulting to true. Indicating whether or not to perform the operation asynchronously.
    :param user: String. Optional. The optional user name to use for authentication purposes; by default, this is the null value.
    :param password: String. Optional. The optional password to use for authentication purposes; by default, this is the null value.
    """
    self.url, self.method = url, method_type
    return self

  def setHeaders(self, headers):
    """
    Description:
    ------------
    The XMLHttpRequest method setRequestHeader() sets the value of an HTTP request header.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/setRequestHeader

    Attributes:
    ----------
    :param headers: Dictionary. The different attributes to be added to the header.
    """
    self.__headers.update(headers)
    return self

  def setRequestHeader(self, name, value):
    """
    Description:
    ------------
    The XMLHttpRequest method setRequestHeader() sets the value of an HTTP request header.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/setRequestHeader

    Attributes:
    ----------
    :param name: String. The header name.
    :param value: String. The header value.
    """
    self.__headers[name] = value
    return self

  def onSuccess(self, jsFncs):
    """
    Description:
    ------------
    The XMLHttpRequestEventTarget.onload is the function called when an XMLHttpRequest transaction completes
    successfully.

    callback is the function to be executed when the request completes successfully.
    It receives a ProgressEvent object as its first argument.
    The value of this (i.e. the context) is the same XMLHttpRequest this callback is related to.

    Attributes:
    ----------
    :param jsFncs: String | List. The Javascript functions
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self.__req_success = jsFncs
    if self.profile is not None and self.profile:
      self.__req_success.insert(0, "console.log('Start[SUCCESS]: '+ (performance.now() - t_post%s)+ ' ms')" % JsUtils.PROFILE_COUNT)
      self.__req_success.append("console.log('End[SUCCESS]: '+ (performance.now() - t_post%s)+ ' ms')" % JsUtils.PROFILE_COUNT)
    return self

  def onerror(self, jsFncs):
    """
    Description:
    ------------
    The XMLHttpRequestEventTarget.onerror is the function called when an XMLHttpRequest transaction fails due to
    an error.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/error_event

    Attributes:
    ----------
    :param jsFncs: String | List. The Javascript functions
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    if self.__on.get("onerror") is None:
      self.__on["onerror"] = jsFncs
    else:
      self.__on["onerror"] = jsFncs
    return self

  def onFail(self, jsFncs, status_code=404, profile=None):
    """
    Description:
    ------------
    The loadend event is fired when a request has completed, whether successfully (after load) or unsuccessfully
    (after abort or error).

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/loadend_event

    Attributes:
    ----------
    :param jsFncs: String | List. The Javascript functions.
    :param status_code: Integer. Optional. The status code for the failure condition.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if "onloadend" not in self.__on:
      self.__on["onloadend"] = []
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self.__on["onloadend"].append("if(%s.status == %s){%s}" % (
      self.varId, status_code, JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile or self.profile)))
    return self

  @property
  def errors(self):
    """
    Description:
    ------------

    """
    if self.__on.get("onloadend") is None:
      self.__on["onloadend"] = []
    return XMLHttpRequestErrors(self.__on["onloadend"], self._src, self)

  def ontimeout(self, jsFncs, timeout=2000):
    """
    Description:
    ------------
    The timeout event is fired when progression is terminated due to preset time expiring.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/timeout

    Attributes:
    ----------
    :param jsFncs: String | List. The Javascript functions.
    :param timeout: Integer. Optional. Time in milliseconds.
    """
    self.timeout = timeout
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self.__on["ontimeout"] = jsFncs
    return self

  def onloadend(self, jsFncs):
    """
    Description:
    ------------
    Fired when a request has completed, whether successfully (after load) or unsuccessfully

    Attributes:
    ----------
    :param jsFncs: String | List. The Javascript functions.
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self.__on["onloadend"] = jsFncs
    return self

  def onloadstart(self, jsFncs):
    """
    Description:
    ------------
    The XMLHttpRequestEventTarget.onloadstart is the function called when an XMLHttpRequest transaction starts
    transferring data.

    Attributes:
    ----------
    :param jsFncs: String | List. The Javascript functions.
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self.__on["onloadstart"] = jsFncs
    return self

  def withCredentials(self, flag):
    """
    Description:
    ------------
    The XMLHttpRequest.withCredentials property is a Boolean that indicates whether or not cross-site Access-Control
    requests should be made using credentials such as cookies, authorization headers or TLS client certificates.

    Setting withCredentials has no effect on same-site requests.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/withCredentials

    Attributes:
    ----------
    :param flag: Boolean. Flag to specify the use of credentials.
    """

  def send(self, jsonData=None, encodeURIData=None, stringify=True):
    """
    Description:
    ------------
    The XMLHttpRequest method send() sends the request to the server.
    If the request is asynchronous (which is the default), this method returns as soon as the request is sent and the
    result is delivered using events.
    If the request is synchronous, this method doesn't return until the response has arrived.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/send

    Attributes:
    ----------
    :param jsonData:
    :param encodeURIData:
    :param stringify: Boolean
    """
    #Initialize jsonData with potential initial data passed in the constructor
    if jsonData:
      if isinstance(jsonData, list):
        for obj in jsonData:
          if hasattr(obj, 'options'):
            self.data.add(obj)
          elif isinstance(obj, tuple):
            self.data.add(obj[0], obj[1])
          else:
            self.data.attrs(obj)

      if isinstance(jsonData, dict):
        self.data.update(jsonData)

    if jsonData:
      if stringify:
        self.__req_send = "%s.send(JSON.stringify(%s))" % (self.varId, JsUtils.jsConvertData(self.data, None))
      else:
        # For data form when dealing with files
        self.__req_send = "%s.send(%s)" % (self.varId, JsUtils.jsConvertData(self.data, None))
    elif encodeURIData is not None:
      self.__url_prefix = "?%s" % "&".join(["%s=%s" % (k, v) for k, v in encodeURIData.items()])
      self.__req_send = "%s.send()" % self.varId
    else:
      self.__req_send = "%s.send()" % self.varId
    return self

  def toStr(self):
    request = [
      "var %s = new XMLHttpRequest()" % self.varId,
      "%s.responseType = '%s'" % (self.varId, self.__responseType)]
    if self.profile is not None and self.profile:
      request.insert(0, "var t_post%s = performance.now()" % JsUtils.PROFILE_COUNT)
    if self.timeout is not None:
      request.append("%s.timeout = %s" % (self.varId, self.timeout))
    if self.__url_prefix:
      request.append("%s.open(%s, %s+'%s')" % (self.varId, self.method, self.url, self.__url_prefix))
    else:
      request.append("%s.open(%s, %s)" % (self.varId, self.method, self.url))
    for k, v in self.__headers.items():
      request.append("%s.setRequestHeader('%s', '%s')" % (self.varId, k, v))
    if self.__req_success is not None:
      if self.__req_fail is not None:
        request.append("%s.onload = function(){}" % self.varId)
      else:
        request.append("%(varId)s.onload = function(){var data = %(varId)s.response; %(jsFncs)s}" % {
          'varId': self.varId, 'jsFncs': JsUtils.jsConvertFncs(self.__req_success, toStr=True, profile=self.profile)})
    if self.__req_end is not None:
      request.append("%(varId)s.onloadend = function(){%(jsFncs)s}" % {
        'varId': self.varId, 'jsFncs': JsUtils.jsConvertFncs(self.__req_end, toStr=True, profile=self.profile)})
    for k, fncs in self.__on.items():
      request.append("%(varId)s.%(name)s = function(){%(jsFncs)s}" % {
        'name': k, 'varId': self.varId, 'jsFncs': JsUtils.jsConvertFncs(fncs, toStr=True, profile=self.profile)})
    if self.__req_send is None:
      raise Exception("The send method must be called")
    request.append(self.__req_send)
    if self.profile is not None and self.profile:
      JsUtils.PROFILE_COUNT += 1
    return ";".join(request)
