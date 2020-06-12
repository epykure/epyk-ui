
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects


class SocketIO(object):

  def __init__(self, htmlCode=None, src=None):
    """
    Description:
    ------------
    """
    if src is not None:
      src.jsImports.add('socket.io')
    self._src = src
    self._selector = htmlCode or "socket_%s" % id(self)

  @property
  def message(self):
    """

    """
    return JsObjects.JsObject.JsObject.get("data")

  def send(self, msg):
    """
    Description:
    ------------
    This will send an event called message(built in) to our client, four seconds after the client connects.
    The send function on socket object associates the 'message' event.

    Usage::

      https://www.tutorialspoint.com/socket.io/socket.io_event_handling.htm

    Attributes:
    ----------
    :param msg:
    """
    msg = JsUtils.jsConvertData(msg, None)
    return JsObjects.JsVoid("%s.send(%s)" % (self._selector, msg))

  def join(self, roomId):
    """
    Description:
    ------------

    Usage::

      https://www.tutorialspoint.com/socket.io/socket.io_rooms.htm

    Attributes:
    ----------
    :param roomId:
    """
    roomId = JsUtils.jsConvertData(roomId, None)
    return JsObjects.JsVoid("%s.join(%s)" % (self._selector, roomId))

  def inRoom(self, roomId, eventType, jsData=None):
    """
    Description:
    ------------

    Usage::

      https://www.tutorialspoint.com/socket.io/socket.io_rooms.htm

    Attributes:
    ----------
    :param roomId: String. The room identifier
    """
    jsData = JsUtils.jsConvertData(jsData or {}, None)
    eventType = JsUtils.jsConvertData(eventType, None)
    roomId = JsUtils.jsConvertData(roomId, None)
    return JsObjects.JsVoid("%s.in(%s).emit(%s, %s)" % (self._selector, roomId, eventType, jsData))

  def leave(self, roomId):
    """
    Description:
    ------------

    Usage::

      https://www.tutorialspoint.com/socket.io/socket.io_rooms.htm

    Attributes:
    ----------
    :param roomId: String. The room identifier
    """
    roomId = JsUtils.jsConvertData(roomId, None)
    return JsObjects.JsVoid("%s.leave(%s)" % (self._selector, roomId))

  def connect(self, url=None, port=None, namespace=None, from_config=None):
    """
    Description:
    ------------
    This function will automatically add the socket to the page object.
    This must be defined first in order to be used in the various components

    Attributes:
    ----------
    :param url: String. The server url
    :param port: Integer. The server port
    :param namespace: String. Optional. The server namespace (or room)
    :param from_config: Python Object. An internal Server configuration object (page.js.server())
    """
    if from_config is not None:
      self._src._props['js']['builders'].add("var %s = io.connect(%s)" % (self._selector, from_config.address))
      return JsObjects.JsVoid("var %s = io.connect(%s)" % (self._selector, from_config.address))

    elif url is None:
      self._src._props['js']['builders'].add("var %s = io.connect()" % self._selector)
      return JsObjects.JsVoid("var %s = io.connect()" % self._selector)

    if namespace is None:
      self._src._props['js']['builders'].add("var %s = io.connect('%s:%s')" % (self._selector, url, port))
      return JsObjects.JsVoid("var %s = io.connect('%s:%s')" % (self._selector, url, port))

    self._src._props['js']['builders'].add("var %s = io.connect('%s:%s/%s')" % (self._selector, url, port, namespace))
    return JsObjects.JsVoid("var %s = io.connect('%s:%s/%s')" % (self._selector, url, port, namespace))

  def on(self, eventType, jsFncs):
    """
    Description:
    ------------

    Usage::

      https://www.tutorialspoint.com/socket.io/socket.io_event_handling.htm

    Attributes:
    ----------
    :param eventType:
    :param jsFncs:

    :return: self to allow the chaining
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    eventType = JsUtils.jsConvertData(eventType, None)
    self._src.js.onReady("%s.on(%s, function(data) {%s})" % (self._selector, eventType, JsUtils.jsConvertFncs(jsFncs, toStr=True)))
    return self

  def emit(self, eventType, jsData=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param eventType:
    :param jsData:
    """
    jsData = JsUtils.jsConvertData(jsData or {}, None)
    eventType = JsUtils.jsConvertData(eventType, None)
    return JsObjects.JsVoid("%s.emit(%s, %s)" % (self._selector, eventType, jsData))
