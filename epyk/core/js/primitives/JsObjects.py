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


class JsVoid(object):
  def __init__(self, data):
    self._data = data

  def toStr(self):
    return self._data


class JsObjects(object):
  def __init__(self, jsObj=None):
    self._jsObj = jsObj

  @property
  def this(self):
    """
    Description:
    -----------
    Interface to the Javascript Object primitive

    :return: The Javascript "this" object (which is a dom object very often)
    """
    return JsNodeDom.JsDoms.get("this")

  @property
  def result(self):
    """
    Description:
    -----------
    Interface to the Javascript Object primitive

    :return: The Javascript result object from a post or any other AJAX calls
    """
    return JsObject.JsObject.get("result")

  @property
  def request(self):
    """
    Description:
    -----------
    Interface to the Javascript Object primitive

    :return: The Javascript result object from a post or any other AJAX calls

    :rtype: XMLHttpRequest
    """
    return XMLHttpRequest.get("result")

  @property
  def data(self):
    """
    Description:
    -----------
    Interface to the Javascript Object primitive

    :return: The Javascript data object from a post or any other AJAX calls
    """
    return JsObject.JsObject.get("data")

  @property
  def value(self):
    """
    Description:
    -----------
    Interface to the Javascript Object primitive

    :return: The Javascript value in a event
    """
    return JsObject.JsObject.get("value")

  @property
  def mouseEvent(self):
    """
    Description:
    -----------
    Interface to the JavaScript MouseEvents

    Related Pages:

      https://www.w3schools.com/jsref/obj_mouseevent.asp
    """
    return JsEvents.MouseEvent()

  @property
  def event(self):
    """
    Description:
    -----------
    Interface to the JavaScript Events

    Related Pages:

      https://www.w3schools.com/jsref/obj_event.asp
    """
    return JsEvents.Event()

  @property
  def jqThis(self):
    """
    Description:
    -----------
    Interface to the Javascript Object primitive

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
    :param varName:

    :return: The requested Python JsObject primitive
    """
    return JsObject.JsObject.get(varName)

  @classmethod
  def new(cls, data=None, varName=None, isPyData=False, report=None):
    """
    Description:
    -----------
    Interface to the Javascript Object primitive

    :return: A Python generic JsObject primitive
    """
    return JsObject.JsObject.new(data, varName, isPyData, report=report)

  def time(self, varName, report=None):
    """
    Description:
    -----------
    Return a time object from the Javascript function performance.now()

    Attributes:
    ----------
    :param varName: String. The variable name
    :param report: Report. The report object
    """
    return JsObject.JsObject.new("performance.now()", varName, False, report=report)

  @property
  def number(self):
    """
    Description:
    -----------
    Interface to the Javascript Number primitive

    Related Pages:

      https://www.w3schools.com/jsref/jsref_number.asp

    :return: A Python JsNumber primitive
    """
    return JsNumber.JsNumber

  @property
  def string(self):
    """
    Description:
    -----------
    Interface to the Javascript String primitive

    Related Pages:

      https://www.w3schools.com/jsref/jsref_obj_string.asp

    :return: A Python JsString primitive
    """
    return JsString.JsString

  @property
  def list(self):
    """
    Description:
    -----------
    Interface to the Javascript Array primitive

    Related Pages:

      https://www.w3schools.com/jsref/jsref_obj_array.asp

    :return: A Python JsArray primitive
    """
    return JsArray.JsArray

  @property
  def array(self):
    """
    Description:
    -----------
    Interface to the Javascript Array primitive

    Related Pages:

      https://www.w3schools.com/jsref/jsref_obj_array.asp

    :return: A Python JsArray primitive
    """
    return JsArray.JsArray

  @property
  def date(self):
    """
    Description:
    -----------
    Interface to the Javascript Date primitive

    Related Pages:

      https://www.w3schools.com/jsref/jsref_obj_date.asp

    :return: A Python JsDate object
    """
    return JsDate.JsDate

  @property
  def boolean(self):
    """
    Description:
    -----------
    Interface to the Javascript Boolean primitive

    Related Pages:

      https://www.w3schools.com/jsref/jsref_obj_boolean.asp

    :return: A Python JsBoolean primitive
    """
    return JsBoolean.JsBoolean

  @property
  def dom(self):
    """
    Description:
    -----------
    Interface to the Javascript Dom class

    :return: A Python Document
    """
    return JsNodeDom.JsDoms

  @property
  def null(self):
    """
    Description:
    -----------
    Similar as None in Python

    Related Pages:

      https://www.w3schools.com/js/js_datatypes.asp

    :return: A Python Js Null object
    """
    return JsObject.JsObject("null")

  @property
  def undefined(self):
    """
    Description:
    -----------
    Similar as the None in Python

    Related Pages:

      https://www.w3schools.com/jsref/jsref_undefined.asp

    :return: A Python Js undefined object
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
    Similar as True in Python

    Related Pages:

      https://www.w3schools.com/js/js_booleans.asp

    :return: A Python Js True object
    """
    return JsBoolean.JsBoolean.get('true')

  @property
  def false(self):
    """
    Description:
    -----------
    Similar as False in Python

    Related Pages:

      https://www.w3schools.com/js/js_booleans.asp
    
    :return: A Python Js False object
    """
    return JsBoolean.JsBoolean.get('false')

  def record(self, varName):
    """
    Description:
    -----------
    Get a record object

    :param varName: A string with of the existing variable name
    """
    return JsData.RawData.get(self._jsObj, varName)

  def incr(self, incr):
    """
    Description:
    -----------

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


class JsPromise(object):

  def __init__(self, jsObj):
    self._jsObj = jsObj
    self.__then, self.__catch = [], []

  def then(self, jsFnc):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFnc:
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
    :param jsFnc:
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
      result.append("then(function(fulfilled){%s})" % ";".join(self.__then))
    if self.__catch:
      result.append("catch(function(error){%s})" % ";".join(self.__catch))
    return ".".join(result)

  def __str__(self):
    return self.toStr()


class XMLHttpRequest(object):

  def __init__(self, report, varName, method_type, url, data=None):
    self.data = JsData.Datamap() if data is None else data
    self._src, self.__headers, self.url = report, {}, url
    self.__mod_name, self.__mod_path, self.method = None, None, method_type
    self.__req_success, self.__req_fail, self.__req_send = None, None, None
    self.__url_prefix, self.__responseType = "", 'json'
    self.varId = varName
    if url is not None:
      self.open(method_type, url)

  @classmethod
  def get(cls, varName):
    """
    Description:
    ------------
    Interface to the Javascript Object primitive

    Attributes:
    ----------
    :param varName:

    :return: The requested Python JsObject primitive
    """
    return XMLHttpRequest(None, varName, None, None)

  def readyState(self):
    """
    Description:
    ------------
    The XMLHttpRequest.readyState property returns the state an XMLHttpRequest client is in.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/readyState
    """
    return JsNumber.JsNumber("%s.readyState" % self.varId)

  def status(self):
    """
    Description:
    ------------
    The read-only XMLHttpRequest.status property returns the numerical HTTP status code of the XMLHttpRequest's response.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/status
    """
    return JsNumber.JsNumber("%s.status" % self.varId)

  def responseType(self, value=None):
    """
    Description:
    ------------
    The XMLHttpRequest property responseType is an enumerated string value specifying the type of data contained in the response.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/responseType

    Attributes:
    ----------
    :param value:
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
    The read-only XMLHttpRequest property responseText returns the text received from a server following a request being sent.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/responseText
    """
    return JsString.JsString("%s.responseText" % self.varId, isPyData=False)

  def timeout(self, milliSeconds):
    """
    Description:
    ------------
    The XMLHttpRequest.timeout property is an unsigned long representing the number of milliseconds a request can take before automatically being terminated.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/timeout

    Attributes:
    ----------
    :param milliSeconds: Number. The value of milliseconds
    """

  def abort(self):
    """
    Description:
    ------------
    The abort event is fired when a request has been aborted, for example because the program called XMLHttpRequest.abort().

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/abort_event
    """

  def addEventListener(self, event, jsFncs):
    """
    Description:
    ------------

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/error_event

    Attributes:
    ----------
    :param event:
    :param jsFncs:
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
    :param _async: Boolean. An optional Boolean parameter, defaulting to true, indicating whether or not to perform the operation asynchronously.
    :param user: The optional user name to use for authentication purposes; by default, this is the null value.
    :param password: The optional password to use for authentication purposes; by default, this is the null value.
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
    :param headers: Dictionary. The different attributes to be added to the header
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
    :param name: String. The header name
    :param value: String. The header value
    """
    self.__headers[name] = value
    return self

  def onSuccess(self, jsFncs):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param jsFncs:
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self.__req_success = jsFncs
    return self

  def ontimeout(self, jsFncs):
    """
    Description:
    ------------

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/timeout

    Attributes:
    ----------
    :param jsFncs:
    """

  def onFail(self, jsFncs):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param jsFncs:
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self.__req_fail = jsFncs
    return self

  def withCredentials(self, flag):
    """
    Description:
    ------------
    The XMLHttpRequest.withCredentials property is a Boolean that indicates whether or not cross-site Access-Control requests should be made using credentials such as cookies, authorization headers or TLS client certificates. Setting withCredentials has no effect on same-site requests.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/withCredentials

    Attributes:
    ----------
    :param flag:
    """

  def send(self, jsonData=None, encodeURIData=None, stringify=True):
    """
    Description:
    ------------
    The XMLHttpRequest method send() sends the request to the server.
    If the request is asynchronous (which is the default), this method returns as soon as the request is sent and the result is delivered using events.
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
          else:
            self.data.attrs(obj)
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
    request = ["var %s = new XMLHttpRequest()" % self.varId]
    request.append("%s.responseType = '%s'" % (self.varId, self.__responseType))
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
        request.append("%(varId)s.onload = function(){var data = %(varId)s.response; %(jsFncs)s}" % {'varId': self.varId, 'jsFncs': JsUtils.jsConvertFncs(self.__req_success, toStr=True)})
    if self.__req_send is None:
      raise Exception("The send method must be called")

    request.append(self.__req_send)
    return ";".join(request)
