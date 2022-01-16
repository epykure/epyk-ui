#!/usr/bin/python
# -*- coding: utf-8 -*-


from typing import Union, Optional

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

  def __init__(self, htmlCode: Optional[str] = None, src=None, secured: bool = False):
    """
    Description:
    ------------
    """
    self._src, self.secured, self.__connect = src, secured, None
    self._selector = htmlCode or "websocket_%s" % id(self)

  @property
  def readyState(self):
    """
    Description:
    ------------

    """
    return JsObjects.JsObject.JsObject.get("%s.readyState" % self._selector)

  @property
  def states(self):
    """
    Description:
    ------------
    To get connection state, additionally there’s socket.readyState property with values:

    Related Pages:

      https://javascript.info/websocket
    """
    return SocketState

  @property
  def http_codes(self):
    """
    Description:
    ------------
    To get connection state, additionally there’s socket.readyState property with values:

    Related Pages:

      https://tools.ietf.org/html/rfc6455#section-7.4.1
    """
    return HttpCode

  @property
  def message(self):
    """
    Description:
    ------------

    """
    return JsObjects.JsObject.JsObject.get("event.data")

  def reconnect(self):
    """
    Description:
    ------------

    """
    return JsObjects.JsVoid("if(%(varName)s.readyState > 1){ %(varName)s = %(connect)s}" % {
      "varName": self._selector, "connect": self.__connect})

  def connect(self, url: str = None, port: Optional[int] = None, protocol: Union[list, str] = None,
              from_config=None):
    """
    Description:
    ------------
    In order to communicate using the WebSocket protocol, you need to create a WebSocket object; this will automatically
    attempt to open the connection to the server.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications

    Attributes:
    ----------
    :param str url: The URL to which to connect; this should be the URL to which the WebSocket server will respond.
        This should use the URL scheme wss://, although some software may allow you to use the insecure ws:// for local connections.
    :param Optional[int] port: The application port number.
    :param Union[list, str] protocol: Either a single protocol string or an array of protocol strings.
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

  def onopen(self, js_funcs: Optional[Union[list, str]], profile: Optional[Union[dict, bool]] = None):
    """
    Description:
    ------------

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications

    Attributes:
    ----------
    :param Optional[Union[list, str]] js_funcs: Javascript functions.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._src.js.onReady(
      "%s.onopen = function (event) {%s}" % (
        self._selector, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))
    return self

  def onmessage(self, js_funcs: Optional[Union[list, str]], profile: Optional[Union[dict, bool]] = None):
    """
    Description:
    ------------

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications

    Attributes:
    ----------
    :param Optional[Union[list, str]] js_funcs: Javascript functions.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._src.js.onReady("%s.onmessage = function (event) {%s}" % (
      self._selector, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))
    return self

  def onerror(self, js_funcs: Optional[Union[list, str]], profile: Optional[Union[dict, bool]] = None):
    """
    Description:
    ------------

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications

    Attributes:
    ----------
    :param Optional[Union[list, str]] js_funcs: Javascript functions.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._src.js.onReady("%s.onerror = function (event) {%s}" % (
      self._selector, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))
    return self

  def onclose(self, js_funcs: Optional[Union[list, str]], profile: Optional[Union[dict, bool]] = None):
    """
    Description:
    ------------

    Related Pages:

      https://javascript.info/websocket

    Attributes:
    ----------
    :param Optional[Union[list, str]] js_funcs: Javascript functions.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._src.js.onReady("%s.onclose = function (event) {%s}" % (
      self._selector, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))
    return self

  def receive(self, js_funcs: Optional[Union[list, str]], profile: Optional[Union[dict, bool]] = None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param Optional[Union[list, str]] js_funcs: Javascript functions.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    return JsObjects.JsVoid("%(varName)s.onmessage = function (event) { %(data)s }" % {
      "varName": self._selector, "data": JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)})

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
    return JsObjects.JsVoid("%(varName)s.send(%(data)s)" % {
      "varName": self._selector, "connect": self.__connect, "data": data})

  def sendText(self, components, attrs: dict = None):
    """
    Description:
    ------------
    Send a complex message from components.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications

    Attributes:
    ----------
    :param components: List. The list of HTML components (it will get the dom.content automatically)
    :param dict attrs: Optional. Attach some static attributes to the request
    """
    from epyk.core.data import primitives
    from epyk.core.data import datamap

    dftl_attrs = {"type": 'message', 'date': primitives.date()}
    if attrs is not None:
      dftl_attrs.update(attrs)
    data = JsUtils.jsConvertData(datamap(components, attrs=dftl_attrs), None)
    return JsObjects.JsVoid("%(varName)s.send(JSON.stringify(%(data)s))" % {
      "varName": self._selector, "connect": self.__connect, "data": data})

  def close(self, code: int = 1000, reason: Optional[str] = None):
    """
    Description:
    ------------
    When you've finished using the WebSocket connection, call the WebSocket method close()

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications

    Attributes:
    ----------
    :param int code: Optional. The HTTP code to be sent to the server for the closure
    :param Optional[str] reason: Optional. The message to be sent to the server for the closure
    """
    if reason is None:
      return JsObjects.JsVoid("%s.close(%s)" % (self._selector, code))

    return JsObjects.JsVoid("%s.close(%s, '%s')" % (self._selector, code, reason))


class Worker:

  def __init__(self, htmlCode: Optional[str] = None, src: Optional[str] = None, server: bool = False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param Optional[str] htmlCode: Optional. The Id of the script.
    :param Optional[str] src: Optional.
    :param bool server: Optional. Specify if the page is running on a server.
    """
    self._src, self.__server = src, server
    self._selector = htmlCode or "worker_%s" % id(self)
    self._src._props['js']['builders'].add("var %s" % self._selector)

  @property
  def message(self):
    """
    Description:
    ------------
    Get the event data from the web worker
    """
    return JsObjects.JsObject.JsObject.get("event.data")

  def connect(self, script: Optional[str] = None, content: Optional[str] = None, url: Optional[str] = None):
    """
    Description:
    ------------
    Create the worker content.

    Only one of the three parameter is needed.

    .. note::

      The JavaScript content used in a web worker need to be written in a way that he can be put in one line.
      In order to be compatible with Jupyter this content need to be loaded from Js and this can only be done by loading a plain
      text in one line.

    Related Pages:

      https://www.w3schools.com/html/html5_webworkers.asp
      https://www.html5rocks.com/en/tutorials/workers/basics/

    Attributes:
    ----------
    :param Optional[str] script: Optional. The full path of the file with the javaScript content.
    :param Optional[str] content: Optional. The JavaScript content.
    :param Optional[str] url: Optional. The link of the worker module to be included to the page.
    """
    if not self.__server or content is not None:
      script_content = [
        'if(document.getElementById("js_%(id)s") != null){document.getElementById("js_%(id)s").remove()}' % {"id": self._selector},
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
      self._src._props['js']['builders'].add('''
        %(content)s; var blob_%(selector)s = new Blob([document.querySelector('#js_%(selector)s').textContent ], {type: "text/javascript"})
        %(selector)s = new Worker(window.URL.createObjectURL(blob_%(selector)s))''' % {
          "content": ";".join(script_content), 'selector': self._selector})
    else:
      self._src._props['js']['builders'].add("%s = new Worker('%s')" % (self._selector, script))
    return JsObjects.JsVoid("%s = new Worker('%s')" % (self._selector, script))

  def postMessage(self, data, components=None):
    """
    Description:
    ------------
    Post a message to the webworker.

    Usage::

      page.ui.button("Add").click([w2.postMessage({'cmd': 'add', 'value1': 2}, components=[(slider, "value2")])])

    Related Pages:

      https://www.html5rocks.com/en/tutorials/workers/basics/

    Attributes:
    ----------
    :param data:
    :param components: HTML components. A list of html component or tuples with the alias
    """
    if components is not None:
      data = JsData.Datamap(components=components, attrs=data)
    else:
      data = JsUtils.jsConvertData(data, None)
    return JsObjects.JsVoid("%s.postMessage(%s)" % (self._selector, data))

  def on(self, eventType: str, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param str eventType: The event type.
    :param Union[list, str] js_funcs: Javascript functions.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    self._src.js.onReady(self.addEventListener(eventType, js_funcs, profile))

  def addEventListener(self, eventType: str, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param str eventType: The event type.
    :param Union[list, str] js_funcs: Javascript functions.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    return JsObjects.JsVoid("%(varName)s.addEventListener('%(eventType)s', function (event) {%(data)s})" % {
      "varName": self._selector, 'eventType': eventType, "data":
        JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)})

  def receive(self, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param Union[list, str] js_funcs: Javascript functions.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    return JsObjects.JsVoid("%(varName)s.onmessage = function (event) {%(data)s}" % {
      "varName": self._selector, "data": JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)})

  def terminate(self):
    """
    Description:
    ------------
    When a web worker object is created, it will continue to listen for messages (even after the external script is
    finished) until it is terminated.

    Related Pages:

      https://www.w3schools.com/html/html5_webworkers.asp
    """
    return JsObjects.JsVoid("%s.terminate(); %s = undefined" % (self._selector, self._selector))

  def close(self):
    """
    Description:
    ------------
    Proxy to the terminate method.
    """
    return self.terminate()


class ServerSentEvent:

  def __init__(self, htmlCode: Optional[str] = None, src=None, server: Optional[str] = False):
    """
    Description:
    ------------

    Attributes:
    ----------
    """
    self._src, self.__server = src, server
    self._selector = htmlCode or "sse_%s" % id(self)
    self._src._props['js']['builders'].add("var %s" % self._selector)

  @property
  def message(self):
    """
    Description:
    ------------

    """
    return JsObjects.JsObject.JsObject.get("event.data")

  def connect(self, url: Optional[str] = None, port: Optional[int] = None, from_config=None,
              options: Optional[dict] = None):
    """
    Description:
    ------------
    n order to communicate using the WebSocket protocol, you need to create a WebSocket object; this will
    automatically attempt to open the connection to the server.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications

    Attributes:
    ----------
    :param Optional[str] url: The URL to which to connect; this should be the URL to which the WebSocket server will respond.
        This should use the URL scheme wss://, although some software may allow you to use the insecure ws:// for local connections.
    :param Optional[int] port:
    :param from_config:
    :param Optional[dict] options:
    """
    if from_config is not None:
      self._src._props['js']['builders'].add("%s = new EventSource(%s)" % (self._selector, from_config.address))
      self.__connect = "new EventSource(%s)" % from_config.address
      return JsObjects.JsVoid("%s = new EventSource(%s)" % (self._selector, from_config.address))

    self._src._props['js']['builders'].add("%s = new EventSource('%s:%s')" % (self._selector, url, port))
    self.__connect = "new EventSource('%s:%s')" % (url, port)
    return JsObjects.JsVoid("%s = new EventSource('%s:%s')" % (self._selector, url, port))

  def onmessage(self, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = None):
    """
    Description:
    ------------
    The EventSource object is used to receive server-sent event notifications:

    Related Pages:

      https://www.w3schools.com/html/html5_serversentevents.asp

    Attributes:
    ----------
    :param Union[list, str] js_funcs: Javascript functions.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._src.js.onReady("%s.onmessage = function (event) { %s }" % (
      self._selector, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))
    return self

  def onerror(self, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = None):
    """
    Description:
    ------------
    When an error occurs.

    Related Pages:

      https://www.w3schools.com/html/html5_serversentevents.asp

    Attributes:
    ----------
    :param Union[list, str] js_funcs: Javascript functions.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._src.js.onReady("%s.onerror = function (event) {%s}" % (
      self._selector, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))
    return self

  def onopen(self, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = None):
    """
    Description:
    ------------
    When a connection to the server is opened.

    Related Pages:

      https://www.w3schools.com/html/html5_serversentevents.asp

    Attributes:
    ----------
    :param Union[list, str] js_funcs: Javascript functions.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._src.js.onReady("%s.onopen = function (event) { %s }" % (
      self._selector, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))
    return self

  def addEventListener(self, event_type: str, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param str event_type: The event type.
    :param Union[list, str] js_funcs: Javascript functions.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    return JsObjects.JsVoid("%(varName)s.addEventListener('%(eventType)s', function (event) {%(data)s})" % {
      "varName": self._selector, 'eventType': event_type,
      "data": JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)})

  def on(self, event_type: str, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param str event_type: The event type.
    :param Union[list, str] js_funcs: Javascript functions.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    self._src.js.onReady(self.addEventListener(event_type, js_funcs, profile))

  def receive(self, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = None):
    """
    Description:
    ------------
    The EventSource object is used to receive server-sent event notifications:

    Related Pages:

      https://www.w3schools.com/html/html5_serversentevents.asp

    Attributes:
    ----------
    :param Union[list, str] js_funcs: Javascript functions.
    :param Optional[Union[dict, bool]] profile: Optional. A flag to set the component performance storage.
    """
    return JsObjects.JsVoid("%(varName)s.onmessage = function (event) { %(data)s }" % {
      "varName": self._selector, "data": JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)})

  def close(self):
    """
    Description:
    ------------
    By default, if the connection between the client and server closes, the connection is restarted.
    The connection is terminated with the .close() method.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events
    """
    return JsObjects.JsVoid("%s.close(); %s = undefined" % (self._selector, self._selector))
