
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
    self._selector = htmlCode or "socket_%s" % id(self)

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

  def connect(self, url=None, port=None, namespace=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param url:
    :param port:
    :param namespace:
    """
    if url is None:
      return JsObjects.JsVoid("var %s = io.connect()" % self._selector)

    if namespace is None:
      return JsObjects.JsVoid("var %s = io.connect('%s:%s')" % (self._selector, url, port))

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
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    eventType = JsUtils.jsConvertData(eventType, None)
    return JsObjects.JsVoid("%s.on(%s, function(data) {%s})" % (self._selector, eventType, JsUtils.jsConvertFncs(jsFncs, toStr=True)))

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
