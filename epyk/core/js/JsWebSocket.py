#!/usr/bin/python
# -*- coding: utf-8 -*-


from typing import Union, Optional, List
from epyk.core.py import primitives

from epyk.core.js import JsUtils
from epyk.core.js.objects import JsData
from epyk.core.js.primitives import JsObjects


class SocketState:
  CONNECTING = 0
  OPEN = 1
  CLOSING = 2
  CLOSED = 2


class HttpCode:
  NORMAL_CLOSURE = 1000
  SHUTDOWN_SERVER = 1001
  LOST_CONNECTION = 1006

  MESSAGE_TYPE_NOT_CONSISTENT = 1007
  MESSAGE_VIOLATE_POLICY = 1008
  MESSAGE_TOO_BIG = 1009

  UNEXPECTED_ERROR = 1011


class WebSocket:

  def __init__(self, html_code: Optional[str] = None, src: Optional[Union[str, primitives.PageModel]] = None,
               secured: bool = False):
    """  
    The WebSocket object provides the API for creating and managing a WebSocket connection to a server,
    as well as for sending and receiving data on the connection.

    :param Optional[str] html_code: Optional. The Id of the script.
    :param Optional[Union[str, primitives.PageModel]] src: Optional.
    :param bool secured: Optional.
    """
    self.page, self.secured, self.__connect = src, secured, None
    self._selector = html_code or "websocket_%s" % id(self)

  @property
  def readyState(self):
    """  
    The WebSocket.readyState read-only property returns the current state of the WebSocket connection.

    Related Pages:

          https://developer.mozilla.org/en-US/docs/Web/API/WebSocket/readyState
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
    Fired when data is received through a WebSocket. Also available via the onmessage property.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/WebSocket/message_event
    """
    return JsObjects.JsObject.JsObject.get("event.data")

  def reconnect(self):
    """  

    """
    return JsObjects.JsVoid("if(%(varName)s.readyState > 1){ %(varName)s = %(connect)s}" % {
      "varName": self._selector, "connect": self.__connect})

  def connect(self, url: str = None, port: Optional[int] = None, protocol: Union[list, str] = None,
              from_config=None):
    """  
    In order to communicate using the WebSocket protocol, you need to create a WebSocket object; this will automatically
    attempt to open the connection to the server.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications

    :param str url: The URL to which to connect; this should be the URL to which the WebSocket server will respond.
        This should use the URL scheme wss://, although some software may allow you to use the insecure ws:// for
        local connections.
    :param Optional[int] port: The application port number.
    :param Union[list, str] protocol: Either a single protocol string or an array of protocol strings.
    :param from_config:
    """
    if from_config is not None:
      self.page.properties.js.add_builders("var %s = new WebSocket(%s)" % (self._selector, from_config.address))
      self.__connect = "new WebSocket(%s)" % from_config.address
      return JsObjects.JsVoid("var %s = new WebSocket(%s)" % (self._selector, from_config.address))

    prefix = "wss" if self.secured else 'ws'
    if protocol is None:
      self.page.properties.js.add_builders(
        "var %s = new WebSocket('%s://%s:%s')" % (self._selector, prefix, url, port))
      self.__connect = "new WebSocket('%s://%s:%s')" % (prefix, url, port)
      return JsObjects.JsVoid("var %s = new WebSocket('%s://%s:%s')" % (self._selector, prefix, url, port))

    protocol = JsUtils.jsConvertData(protocol, None)
    self.page.properties.js.add_builders(
      "var %s = new WebSocket('%s://%s:%s', %s)" % (self._selector, prefix, url, port, protocol))
    self.__connect = "new WebSocket('%s://%s:%s', %s)" % (prefix, url, port, protocol)
    return JsObjects.JsVoid("var %s = new WebSocket('%s://%s:%s', %s)" % (self._selector, prefix, url, port, protocol))

  def onopen(self, js_funcs: Optional[Union[list, str]], profile: Optional[Union[dict, bool]] = None):
    """  
    Fired when a connection with a WebSocket is opened. Also available via the onopen property.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications

    :param Optional[Union[list, str]] js_funcs: Javascript functions.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self.page.js.onReady(
      "%s.onopen = function (event) {%s}" % (
        self._selector, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))
    return self

  def onmessage(self, js_funcs: Optional[Union[list, str]], profile: Optional[Union[dict, bool]] = None):
    """  
    Fired when data is received through a WebSocket. Also available via the onmessage property.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications

    :param Optional[Union[list, str]] js_funcs: Javascript functions.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self.page.js.onReady("%s.onmessage = function (event) {%s}" % (
      self._selector, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))
    return self

  def onerror(self, js_funcs: Optional[Union[list, str]], profile: Optional[Union[dict, bool]] = None):
    """  
    Fired when a connection with a WebSocket has been closed because of an error,
    such as when some data couldn't be sent. Also available via the onerror property.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications

    :param Optional[Union[list, str]] js_funcs: Javascript functions.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self.page.js.onReady("%s.onerror = function (event) {%s}" % (
      self._selector, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))
    return self

  def onclose(self, js_funcs: Optional[Union[list, str]], profile: Optional[Union[dict, bool]] = None):
    """  
    Fired when a connection with a WebSocket is closed. Also available via the onclose property.

    Related Pages:

      https://javascript.info/websocket

    :param Optional[Union[list, str]] js_funcs: Javascript functions.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self.page.js.onReady("%s.onclose = function (event) {%s}" % (
      self._selector, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))
    return self

  def receive(self, js_funcs: Optional[Union[list, str]], profile: Optional[Union[dict, bool]] = None):
    """  
    Fired when data is received through a WebSocket. Also available via the onmessage property.

    :param Optional[Union[list, str]] js_funcs: Javascript functions.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    return JsObjects.JsVoid("%(varName)s.onmessage = function (event) { %(data)s }" % {
      "varName": self._selector, "data": JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)})

  def send(self, data):
    """  
    Basic way to send a text message to the server.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications

    :param data: String. The message to be sent
    """
    data = JsUtils.jsConvertData(data, None)
    return JsObjects.JsVoid("%(varName)s.send(%(data)s)" % {
      "varName": self._selector, "connect": self.__connect, "data": data})

  def sendText(self, components: List[primitives.HtmlModel], attrs: dict = None):
    """  
    Send a complex message from components.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications

    :param List[primitives.HtmlModel] components: The list of HTML components (it will get the dom.content
      automatically)
    :param dict attrs: Optional. Attach some static attributes to the request
    """
    from epyk.core.data import primitives
    from epyk.core.data import datamap

    dfl_attrs = {"type": 'message', 'date': primitives.date()}
    if attrs is not None:
      dfl_attrs.update(attrs)
    data = JsUtils.jsConvertData(datamap(components, attrs=dfl_attrs), None)
    return JsObjects.JsVoid("%(varName)s.send(JSON.stringify(%(data)s))" % {
      "varName": self._selector, "connect": self.__connect, "data": data})

  def close(self, code: int = 1000, reason: Optional[Union[str, primitives.JsDataModel]] = None):
    """  
    When you've finished using the WebSocket connection, call the WebSocket method close()

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications

    :param int code: Optional. The HTTP code to be sent to the server for the closure
    :param Optional[str] reason: Optional. The message to be sent to the server for the closure
    """
    if reason is None:
      return JsObjects.JsVoid("%s.close(%s)" % (self._selector, code))

    reason = JsUtils.jsConvertData(reason, None)
    return JsObjects.JsVoid("%s.close(%s, '%s')" % (self._selector, code, reason))


class Worker:

  def __init__(self, html_code: Optional[str] = None, src: Optional[Union[str, primitives.PageModel]] = None,
               server: bool = False):
    """  

    :param html_code: Optional. The Id of the script
    :param src: Optional.
    :param server: Optional. Specify if the page is running on a server
    """
    self.page, self.__server = src, server
    self._selector = html_code or "worker_%s" % id(self)
    self.page._props['js']['builders'].add("var %s" % self._selector)

  @property
  def message(self):
    """  
    Get the event data from the web worker
    """
    return JsObjects.JsObject.JsObject.get("event.data")

  def connect(self, script: Optional[str] = None, content: Optional[str] = None, url: Optional[str] = None):
    """  
    Create the worker content.

    Only one of the three parameter is needed.

    .. note::

      The JavaScript content used in a web worker need to be written in a way that he can be put in one line.
      In order to be compatible with Jupyter this content need to be loaded from Js and this can only be done by
      loading a plain text in one line.

    Related Pages:

      https://www.w3schools.com/html/html5_webworkers.asp
      https://www.html5rocks.com/en/tutorials/workers/basics/

    :param Optional[str] script: Optional. The full path of the file with the javaScript content.
    :param Optional[str] content: Optional. The JavaScript content.
    :param Optional[str] url: Optional. The link of the worker module to be included to the page.
    """
    if not self.__server or content is not None:
      script_content = [
        'if(document.getElementById("js_%(id)s") != null){document.getElementById("js_%(id)s").remove()}' % {
          "id": self._selector},
        'var wkScript = document.createElement("script")',
        'wkScript.setAttribute("id", "js_%s")' % self._selector]
      if script is not None:
        with open(script) as f:
          script_content.append('wkScript.textContent = "%s"' % f.read().strip().replace("\n", ""))
      elif url is not None:
        script_content.append('wkScript.setAttribute("src", %s)' % JsUtils.jsConvertData(url, None))
      else:
        script_content.append('wkScript.textContent = "%s"' % content.strip().replace("\n", ""))
      script_content.append('document.head.appendChild(wkScript)')
      self.page.properties.js.add_builders('''
%(content)s; var blob_%(selector)s = new Blob([document.querySelector('#js_%(selector)s').textContent ], {type: "text/javascript"})
%(selector)s = new Worker(window.URL.createObjectURL(blob_%(selector)s))''' % {
  "content": JsUtils.jsConvertFncs(script_content, toStr=True), 'selector': self._selector})
    else:
      self.page.properties.js.add_builders("%s = new Worker('%s')" % (self._selector, script))
    return JsObjects.JsVoid("%s = new Worker('%s')" % (self._selector, script))

  def postMessage(self, data, components: List[primitives.HtmlModel] = None):
    """  
    Post a message to the webworker.

    Usage::

      page.ui.button("Add").click([w2.postMessage({'cmd': 'add', 'value1': 2}, components=[(slider, "value2")])])

    Related Pages:

      https://www.html5rocks.com/en/tutorials/workers/basics/

    :param data:
    :param List[primitives.HtmlModel] components: A list of html component or tuples with the alias
    """
    if components is not None:
      data = JsData.Datamap(components=components, attrs=data)
    else:
      data = JsUtils.jsConvertData(data, None)
    return JsObjects.JsVoid("%s.postMessage(%s)" % (self._selector, data))

  def on(self, event_type: str, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = None):
    """  

    :param str event_type: The event type.
    :param Union[list, str] js_funcs: Javascript functions.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    self.page.js.onReady(self.addEventListener(event_type, js_funcs, profile))

  def addEventListener(self, event_type: str, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = None):
    """  

    :param str event_type: The event type.
    :param Union[list, str] js_funcs: Javascript functions.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    return JsObjects.JsVoid("%(varName)s.addEventListener('%(eventType)s', function (event) {%(data)s})" % {
      "varName": self._selector, 'eventType': event_type, "data":
        JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)})

  def receive(self, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = None):
    """  

    :param Union[list, str] js_funcs: Javascript functions.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    return JsObjects.JsVoid("%(varName)s.onmessage = function (event) {%(data)s}" % {
      "varName": self._selector, "data": JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)})

  def terminate(self):
    """  
    When a web worker object is created, it will continue to listen for messages (even after the external script is
    finished) until it is terminated.

    Related Pages:

      https://www.w3schools.com/html/html5_webworkers.asp
    """
    return JsObjects.JsVoid("%s.terminate(); %s = undefined" % (self._selector, self._selector))

  def close(self):
    """  
    Proxy to the terminate method.
    """
    return self.terminate()


class ServerSentEvent:

  def __init__(self, html_code: Optional[str] = None, src: Optional[Union[str, primitives.PageModel]] = None,
               server: Optional[str] = False):
    """  

    :param Optional[str] html_code: Optional. The Id of the script.
    :param Optional[Union[str, primitives.PageModel]] src: Optional.
    :param bool server: Optional. Specify if the page is running on a server.
    """
    self.page, self.__server = src, server
    self._selector = html_code or "sse_%s" % id(self)
    self.page.properties.js.add_builders("var %s" % self._selector)

  @property
  def readyState(self):
    """  
    A number representing the state of the connection. Possible values are CONNECTING (0), OPEN (1), or CLOSED (2).

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/EventSource
    """
    return JsObjects.JsObject.JsObject.get("%s.readyState" % self._selector)

  @property
  def url(self):
    """  
    A DOMString representing the URL of the source.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/EventSource
    """
    return JsObjects.JsObject.JsObject.get("%s.url" % self._selector)

  @property
  def withCredentials(self):
    """  
    A boolean value indicating whether the EventSource object was instantiated with cross-origin (CORS) credentials
    set (true), or not (false, the default).

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/EventSource
    """
    return JsObjects.JsObject.JsObject.get("%s.url" % self._selector)

  @property
  def message(self):
    """  
    Get the data object from an event on the JavaScript part.
    Point to the variable: event.data.
    """
    return JsObjects.JsObject.JsObject.get("event.data")

  def connect(self, url: Optional[str] = None, port: Optional[int] = None, from_config=None, options: dict = None):
    """  
    In order to communicate using the WebSocket protocol, you need to create a WebSocket object; this will
    automatically attempt to open the connection to the server.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications

    :param Optional[str] url: The URL to which to connect; this should be the URL to which the WebSocket server will
      respond. This should use the URL scheme wss://, although some software may allow you to use the insecure
      ws:// for local connections.
    :param Optional[int] port:
    :param from_config:
    :param dict options:
    """
    if from_config is not None:
      self.__connect = "new EventSource(%s)" % from_config.address
      self.page.properties.js.add_builders("%s = %s" % (self._selector, self.__connect))
      return JsObjects.JsVoid("%s = %s" % (self._selector, self.__connect))

    server_root = "%s:%s" % (url, port) if port is not None else url
    self.__connect = "new EventSource('%s')" % server_root if options is None else "new EventSource('%s', %s)" % (
      server_root, JsUtils.jsConvertData(options, None))
    self.page.properties.js.add_builders("%s = %s" % (self._selector, self.__connect))
    return JsObjects.JsVoid("%s = %s" % (self._selector, self.__connect))

  def onmessage(self, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = None):
    """  
    The EventSource object is used to receive server-sent event notifications:

    Related Pages:

      https://www.w3schools.com/html/html5_serversentevents.asp

    :param Union[list, str] js_funcs: Javascript functions.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self.page.js.onReady("%s.onmessage = function (event) { %s }" % (
      self._selector, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))
    return self

  def onerror(self, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = None):
    """  
    When an error occurs.

    Related Pages:

      https://www.w3schools.com/html/html5_serversentevents.asp

    :param Union[list, str] js_funcs: Javascript functions.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self.page.js.onReady("%s.onerror = function (event) {%s}" % (
      self._selector, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))
    return self

  def onopen(self, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = None):
    """  
    When a connection to the server is opened.

    Related Pages:

      https://www.w3schools.com/html/html5_serversentevents.asp

    :param Union[list, str] js_funcs: Javascript functions.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self.page.js.onReady("%s.onopen = function (event) { %s }" % (
      self._selector, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))
    return self

  def addEventListener(self, event_type: str, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = None):
    """  

    :param str event_type: The event type.
    :param Union[list, str] js_funcs: Javascript functions.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    event_type = JsUtils.jsConvertData(event_type, None)
    return JsObjects.JsVoid("%(varName)s.addEventListener(%(eventType)s, function (event) {%(data)s})" % {
      "varName": self._selector, 'eventType': event_type,
      "data": JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)})

  def on(self, event_type: str, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = None):
    """  

    :param str event_type: The event type.
    :param Union[list, str] js_funcs: Javascript functions.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    self.page.js.onReady(self.addEventListener(event_type, js_funcs, profile))

  def receive(self, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = None):
    """  
    The EventSource object is used to receive server-sent event notifications:

    Related Pages:

      https://www.w3schools.com/html/html5_serversentevents.asp

    :param Union[list, str] js_funcs: Javascript functions.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    return JsObjects.JsVoid("%(varName)s.onmessage = function (event) { %(data)s }" % {
      "varName": self._selector, "data": JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)})

  def close(self):
    """  
    By default, if the connection between the client and server closes, the connection is restarted.
    The connection is terminated with the .close() method.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events
    """
    return JsObjects.JsVoid("%s.close(); %s = undefined" % (self._selector, self._selector))
