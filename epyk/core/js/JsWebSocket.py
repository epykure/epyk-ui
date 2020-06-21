
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects
from epyk.core.data import primitives
from epyk.core.data import datamap


class SocketState(object):
  CONNECTING = 0
  OPEN = 1
  CLOSING = 2
  CLOSED = 2


class HttpCode(object):
  NORMAL_CLOSURE = 1000
  SHUTDOWN_SERVER = 1001
  LOST_CONNECTION = 1006

  MESSAGE_TYPE_NOT_CONSISTENT = 1007
  MESSAGE_VIOLATE_POLICY = 1008
  MESSAGE_TOO_BIG = 1009

  UNEXPECTED_ERROR = 1011


class WebSocket(object):

  def __init__(self, htmlCode=None, src=None, secured=False):
    """
    Description:
    ------------
    """
    self._src, self.secured, self.__connect = src, secured, None
    self._selector = htmlCode or "websocket_%s" % id(self)

  @property
  def readyState(self):
    """

    """
    return JsObjects.JsObject.JsObject.get("%s.readyState" % self._selector)

  @property
  def states(self):
    """
    To get connection state, additionally there’s socket.readyState property with values:

    Related Pages:

			https://javascript.info/websocket
    """
    return SocketState

  @property
  def http_codes(self):
    """
    To get connection state, additionally there’s socket.readyState property with values:

    Related Pages:

			https://tools.ietf.org/html/rfc6455#section-7.4.1
    """
    return HttpCode

  @property
  def message(self):
    """

    """
    return JsObjects.JsObject.JsObject.get("event.data")

  def reconnect(self):
    return JsObjects.JsVoid("if(%(varName)s.readyState > 1){ %(varName)s = %(connect)s}" % {"varName": self._selector, "connect": self.__connect})

  def connect(self, url=None, port=None, protocol=None, from_config=None):
    """
    Description:
    ------------
    n order to communicate using the WebSocket protocol, you need to create a WebSocket object; this will automatically attempt to open the connection to the server.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications

    Attributes:
    ----------
    :param url: String. The URL to which to connect; this should be the URL to which the WebSocket server will respond.
        This should use the URL scheme wss://, although some software may allow you to use the insecure ws:// for local connections.
    :param protocol: String or List. Either a single protocol string or an array of protocol strings.
    :param from_config:
    """
    if from_config is not None:
      self._src._props['js']['builders'].add("var %s = new WebSocket(%s)" % (self._selector, from_config.address))
      self.__connect = "new WebSocket(%s)" % from_config.address
      return JsObjects.JsVoid("var %s = new WebSocket(%s)" % (self._selector, from_config.address))

    prefix = "wss" if self.secured else 'ws'
    if protocol is None:
      self._src._props['js']['builders'].add(
        "var %s = new WebSocket('%s://%s:%s')" % (self._selector, prefix, url, port))
      self.__connect = "new WebSocket('%s://%s:%s')" % (prefix, url, port)
      return JsObjects.JsVoid("var %s = new WebSocket('%s://%s:%s')" % (self._selector, prefix, url, port))

    protocol = JsUtils.jsConvertData(protocol, None)
    self._src._props['js']['builders'].add(
      "var %s = new WebSocket('%s://%s:%s', %s)" % (self._selector, prefix, url, port, protocol))
    self.__connect = "new WebSocket('%s://%s:%s', %s)" % (prefix, url, port, protocol)
    return JsObjects.JsVoid("var %s = new WebSocket('%s://%s:%s', %s)" % (self._selector, prefix, url, port, protocol))

  def onopen(self, jsFncs):
    """
    Description:
    ------------

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications

    Attributes:
    ----------
    :param jsFncs:
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self._src.js.onReady("%s.onopen = function (event) { %s }" % (self._selector, JsUtils.jsConvertFncs(jsFncs, toStr=True)))
    return self

  def onmessage(self, jsFncs):
    """
    Description:
    ------------

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications

    Attributes:
    ----------
    :param jsFncs:
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self._src.js.onReady("%s.onmessage = function (event) { %s }" % (self._selector, JsUtils.jsConvertFncs(jsFncs, toStr=True)))
    return self

  def onerror(self, jsFncs):
    """
    Description:
    ------------

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications

    Attributes:
    ----------
    :param jsFncs:
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self._src.js.onReady("%s.onerror = function (event) { %s }" % (self._selector, JsUtils.jsConvertFncs(jsFncs, toStr=True)))
    return self

  def onclose(self, jsFncs):
    """
    Description:
    ------------

    Related Pages:

			https://javascript.info/websocket

    Attributes:
    ----------
    :param jsFncs:
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self._src.js.onReady("%s.onclose = function (event) { %s }" % (self._selector, JsUtils.jsConvertFncs(jsFncs, toStr=True)))
    return self

  def receive(self, jsFncs):
    """
    Description:
    ------------

    :param jsFncs:
    """
    return JsObjects.JsVoid("%(varName)s.onmessage = function (event) { %(data)s }" % {"varName": self._selector, "data": JsUtils.jsConvertFncs(jsFncs, toStr=True)})

  def send(self, data):
    """
    Description:
    ------------
    Basic way to send a text message to the server

    Related Pages:

			https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications

    Attributes:
    ----------
    :param data: String. The message to be sent
    """
    data = JsUtils.jsConvertData(data, None)
    return JsObjects.JsVoid("%(varName)s.send(%(data)s)" % {"varName": self._selector, "connect": self.__connect, "data": data})

  def sendText(self, components, attrs=None):
    """
    Description:
    ------------
    Send a complex message from components.

    Related Pages:

			https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications

    Attributes:
    ----------
    :param components: List. The list of HTML components (it will get the dom.content automatically)
    :param attrs: Dictionary. Attach some static attributes to the request
    """
    dftl_attrs = {"type": 'message', 'date': primitives.date()}
    if attrs is not None:
      dftl_attrs.update(attrs)
    data = JsUtils.jsConvertData(datamap(components, attrs=dftl_attrs), None)
    return JsObjects.JsVoid("%(varName)s.send(JSON.stringify(%(data)s))" % {"varName": self._selector, "connect": self.__connect, "data": data})

  def close(self, code=1000, reason=None):
    """
    Description:
    ------------
    When you've finished using the WebSocket connection, call the WebSocket method close()

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications

    Attributes:
    ----------
    :param code: Integer. The HTTP code to be sent to the server for the closure
    :param reason: String. The message to be sent to the server for the closure
    """
    if reason is None:
      return JsObjects.JsVoid("%s.close(%s)" % (self._selector, code))

    return JsObjects.JsVoid("%s.close(%s, '%s')" % (self._selector, code, reason))


class Worker(object):

  def __init__(self, htmlCode=None, src=None, server=False):
    """
    Description:
    ------------

    """
    self._src, self.__server = src, server
    self._selector = htmlCode or "worker_%s" % id(self)
    self._src._props['js']['builders'].add("var %s" % self._selector)

  @property
  def message(self):
    """
    Description:
    ------------

    """
    return JsObjects.JsObject.JsObject.get("event.data")

  def connect(self, script=None, content=None):
    """
    Description:
    ------------

    Related Pages:

      https://www.w3schools.com/html/html5_webworkers.asp
      https://www.html5rocks.com/en/tutorials/workers/basics/

    Attributes:
    ----------
    :param script: String.
    :param content: String.
    """
    if not self.__server or content is not None:
      # load the file and put this to Js Blobs
      if script is not None:
        with open(script) as f:
          self._src._props['js']['workers']['js_%s' % self._selector] = f.read()
      else:
        self._src._props['js']['workers']['js_%s' % self._selector] = content
      self._src._props['js']['builders'].add('''
        var blob_%(selector)s = new Blob([document.querySelector('#js_%(selector)s').textContent ], {type: "text/javascript"})
        %(selector)s = new Worker(window.URL.createObjectURL(blob_%(selector)s))''' % {'selector': self._selector})
    else:
      self._src._props['js']['builders'].add("%s = new Worker('%s')" % (self._selector, script))
    return JsObjects.JsVoid("%s = new Worker('%s')" % (self._selector, script))

  def postMessage(self, data):
    """
    Description:
    ------------

    Related Pages:

      https://www.html5rocks.com/en/tutorials/workers/basics/

    Attributes:
    ----------
    :param data:
    """
    data = JsUtils.jsConvertData(data, None)
    return JsObjects.JsVoid("%s.postMessage(%s)" % (self._selector, data))

  def on(self, eventType, jsFncs):
    self._src.js.onReady(self.addEventListener(eventType, jsFncs))

  def addEventListener(self, eventType, jsFncs):
    """
    Description:
    ------------

    :param eventType:
    :param jsFncs:
    """
    return JsObjects.JsVoid("%(varName)s.addEventListener('%(eventType)s', function (event) {%(data)s})" % {"varName": self._selector, 'eventType': eventType, "data": JsUtils.jsConvertFncs(jsFncs, toStr=True)})

  def receive(self, jsFncs):
    """
    Description:
    ------------

    :param jsFncs:
    """
    return JsObjects.JsVoid("%(varName)s.onmessage = function (event) {%(data)s}" % {"varName": self._selector, "data": JsUtils.jsConvertFncs(jsFncs, toStr=True)})

  def terminate(self):
    """
    Description:
    ------------
    When a web worker object is created, it will continue to listen for messages (even after the external script is finished) until it is terminated.

    Related Pages:

      https://www.w3schools.com/html/html5_webworkers.asp
    """
    return JsObjects.JsVoid("%s.terminate(); %s = undefined" % (self._selector, self._selector))
