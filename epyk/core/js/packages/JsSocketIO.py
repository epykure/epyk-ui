
from typing import Union
from epyk.core.py import primitives
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects


class SocketIO:

  def __init__(self, htmlCode: str = None, page: primitives.PageModel = None):
    """  

    :param htmlCode:
    :param page:
    """
    if page is not None:
      page.jsImports.add('socket.io')
    self.page = page
    self._selector = htmlCode or "socket_%s" % id(self)

  @property
  def message(self):
    """  

    """
    return JsObjects.JsObject.JsObject.get("data")

  def send(self, msg: Union[str, primitives.JsDataModel]):
    """  
    This will send an event called message(built in) to our client, four seconds after the client connects.
    The send function on socket object associates the 'message' event.

    Usage::

      https://www.tutorialspoint.com/socket.io/socket.io_event_handling.htm

    :param msg:
    """
    msg = JsUtils.jsConvertData(msg, None)
    return JsObjects.JsVoid("%s.send(%s)" % (self._selector, msg))

  def join(self, room_id):
    """  

    Usage::

      https://www.tutorialspoint.com/socket.io/socket.io_rooms.htm

    :param room_id:
    """
    room_id = JsUtils.jsConvertData(room_id, None)
    return JsObjects.JsVoid("%s.join(%s)" % (self._selector, room_id))

  def inRoom(self, room_id, event_type, data=None):
    """  

    Usage::

      https://www.tutorialspoint.com/socket.io/socket.io_rooms.htm

    :param room_id: String. The room identifier.
    :param event_type:
    :param data:
    """
    data = JsUtils.jsConvertData(data or {}, None)
    event_type = JsUtils.jsConvertData(event_type, None)
    room_id = JsUtils.jsConvertData(room_id, None)
    return JsObjects.JsVoid("%s.in(%s).emit(%s, %s)" % (self._selector, room_id, event_type, data))

  def leave(self, room_id):
    """  

    Related Pages:

      https://www.tutorialspoint.com/socket.io/socket.io_rooms.htm

    :param room_id: String. The room identifier
    """
    room_id = JsUtils.jsConvertData(room_id, None)
    return JsObjects.JsVoid("%s.leave(%s)" % (self._selector, room_id))

  def connect(self, url=None, port=None, namespace=None, from_config=None):
    """  
    This function will automatically add the socket to the page object.
    This must be defined first in order to be used in the various components

    :param url: String. The server url
    :param port: Integer. The server port
    :param namespace: String. Optional. The server namespace (or room)
    :param from_config: Python Object. An internal Server configuration object (page.js.server())
    """
    if from_config is not None:
      self.page._props['js']['builders'].add("var %s = io.connect(%s)" % (self._selector, from_config.address))
      return JsObjects.JsVoid("var %s = io.connect(%s)" % (self._selector, from_config.address))

    elif url is None:
      self.page._props['js']['builders'].add("var %s = io.connect()" % self._selector)
      return JsObjects.JsVoid("var %s = io.connect()" % self._selector)

    if namespace is None:
      self.page._props['js']['builders'].add("var %s = io.connect('%s:%s')" % (self._selector, url, port))
      return JsObjects.JsVoid("var %s = io.connect('%s:%s')" % (self._selector, url, port))

    self.page._props['js']['builders'].add("var %s = io.connect('%s:%s/%s')" % (self._selector, url, port, namespace))
    return JsObjects.JsVoid("var %s = io.connect('%s:%s/%s')" % (self._selector, url, port, namespace))

  def on(self, event_type, js_funcs, profile=False):
    """  

    Usage::

      https://www.tutorialspoint.com/socket.io/socket.io_event_handling.htm

    :param event_type:
    :param js_funcs:
    :param profile:

    :return: self to allow the chaining
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    event_type = JsUtils.jsConvertData(event_type, None)
    self.page.js.onReady("%s.on(%s, function(data) {%s})" % (
      self._selector, event_type, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))
    return self

  def emit(self, event_type, data=None):
    """  

    :param event_type:
    :param data:
    """
    data = JsUtils.jsConvertData(data or {}, None)
    event_type = JsUtils.jsConvertData(event_type, None)
    return JsObjects.JsVoid("%s.emit(%s, %s)" % (self._selector, event_type, data))
