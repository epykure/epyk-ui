from typing import Union
from epyk.core.py import primitives
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects


class Engine:

    def __init__(self, js_code: str = None, page: primitives.PageModel = None):
        """

        :param js_code:
        :param page:
        """
        self.page = page
        self._selector = js_code

    @property
    def clientsCount(self) -> JsObjects.JsNumber.JsNumber:
        """The number of currently connected clients.

        `Engine <https://socket.io/docs/v4/server-api/#engineclientscount>`_
        """
        return JsObjects.JsNumber.JsNumber.get("%s.clientsCount" % self._selector)

    def on(self, event_type, js_funcs, profile=False):
        """Fired upon a connection from client.

        :param event_type:
        :param js_funcs:
        :param profile:

        :return: self to allow the chaining
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        event_type = JsUtils.jsConvertData(event_type, None)
        return JsUtils.jsWrap("%s.on(%s, function(headers, request) {%s})" % (
            self._selector, event_type, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))

    def headers(self, js_funcs, profile=False):
        """This event will be emitted just before writing the response headers of each HTTP request of the session
        (including the WebSocket upgrade), allowing you to customize them.

        `Engine <https://socket.io/docs/v4/server-api/#event-headers>`_
        """
        return self.on("headers", js_funcs, profile=False)

    def initial_headers(self, js_funcs, profile=False):
        """This event will be emitted just before writing the response headers of the first HTTP request of the session
        (the handshake), allowing you to customize them.

        `Engine <https://socket.io/docs/v4/server-api/#event-initial_headers>`_
        """
        return self.on("initial_headers", js_funcs, profile=False)


class NameSpace:

    @property
    def adapter(self):
        ...

    @property
    def name(self):
        ...

    @property
    def sockets(self):
        ...


class Socket:
    ...


class SocketIO:

    def __init__(self, js_code: str = None, page: primitives.PageModel = None):
        """

        :param js_code:
        :param page:
        """
        if page is not None:
            page.jsImports.add('socket.io')
        self.page = page
        self._selector = js_code or "socket_%s" % id(self)

    @property
    def engine(self):
        """The Engine.IO server, which manages the WebSocket / HTTP long-polling connections.

        `Socket <https://socket.io/docs/v4/server-api/#engine>`_
        """
        return Engine("%s.engine", page=self.page)

    @property
    def message(self):
        """

        """
        return JsObjects.JsObject.JsObject.get("data")

    @property
    def broadcast(self):
        """Sets a modifier for a subsequent event emission that the event data will only be broadcast to every sockets
        but the sender.

        `socket <https://socket.io/docs/v4/server-api/#flag-broadcast>`_
        """
        return SocketIO("%s.broadcast" % self._selector, page=self.page)

    @property
    def local(self):
        """Sets a modifier for a subsequent event emission that the event data will only be broadcast to the current node
        (when scaling to multiple nodes).

        `socket <https://socket.io/docs/v4/server-api/#flag-local>`_
        """
        return SocketIO("%s.local" % self._selector, page=self.page)

    @property
    def volatile(self):
        """Sets a modifier for a subsequent event emission that the event data may be lost if the clients are not
        ready to receive messages

        `socket <https://socket.io/docs/v4/server-api/#flag-volatile>`_
        """
        return SocketIO("%s.volatile" % self._selector, page=self.page)

    def compress(self, value: bool = True):
        """Sets a modifier for a subsequent event emission that the event data will only be compressed if the value is true.
        Defaults to true when you don't call the method.

        `SocketIO <https://socket.io/docs/v4/server-api/#socketcompressvalue>`_
        """
        value = JsUtils.jsConvertData(value, None)
        return JsUtils.jsWrap("%s.compress(%s)" % (self._selector, value))

    def disconnect(self, close: bool = None):
        """Disconnects this socket. If value of close is true, closes the underlying connection. Otherwise,
        it just disconnects the namespace.

        `SocketIO <https://socket.io/docs/v4/server-api/#socketdisconnectclose>`_

        :param close: close <boolean> whether to close the underlying connection
        """
        if close is None:
            return JsUtils.jsWrap("%s.disconnect()" % self._selector)

        close = JsUtils.jsConvertData(close, None)
        return JsUtils.jsWrap("%s.disconnect(%s)" % (self._selector, close))

    def eventNames(self):
        """Inherited from EventEmitter (along with other methods not mentioned here). See the Node.js documentation for
        the events module.

        `SocketIO <https://socket.io/docs/v4/server-api/#socketeventnames>`_
        """
        return JsUtils.jsWrap("%s.eventNames()" % self._selector)

    def fetchSockets(self):
        """Returns the matching Socket instances:

        `SocketIO <https://socket.io/docs/v4/server-api/#namespacefetchsockets>`_
        """
        return JsUtils.jsWrap("%s.fetchSockets()" % self._selector)

    def join(self, room_id):
        """Adds the socket to the given room or to the list of rooms.

        `tutorialspoint <https://www.tutorialspoint.com/socket.io/socket.io_rooms.htm>`_
        `Socket <https://socket.io/docs/v4/server-api/#socketeventnames>`_

        :param room_id:
        """
        room_id = JsUtils.jsConvertData(room_id, None)
        return JsObjects.JsVoid("%s.join(%s)" % (self._selector, room_id))

    def leave(self, room_id):
        """Removes the socket from the given room.

        `tutorialspoint <https://www.tutorialspoint.com/socket.io/socket.io_rooms.htm>`_
        `Socket <https://socket.io/docs/v4/server-api/#socketleaveroom>`_

        :param room_id: String. The room identifier
        """
        room_id = JsUtils.jsConvertData(room_id, None)
        return JsObjects.JsVoid("%s.leave(%s)" % (self._selector, room_id))

    def listenersAny(self):
        """Returns the list of registered catch-all listeners.

        `Socket <https://socket.io/docs/v4/server-api/#socketlistenersany>`_
        """
        return JsObjects.JsVoid("%s.listenersAny()" % self._selector)

    def disconnectSockets(self, close: bool = None):
        """Makes the matching Socket instances disconnect.

        `SocketIO <https://socket.io/docs/v4/server-api/#namespacedisconnectsocketsclose>`_

        :param close: close <boolean> whether to close the underlying connection
        """
        if close is None:
            return JsUtils.jsWrap("%s.disconnectSockets()" % self._selector)

        close = JsUtils.jsConvertData(close, None)
        return JsUtils.jsWrap("%s.disconnectSockets(%s)" % (self._selector, close))

    def send(self, msg: Union[str, primitives.JsDataModel]):
        """This will send an event called message(built in) to our client, four seconds after the client connects.
        The send function on socket object associates the 'message' event.

        `tutorialspoint <https://www.tutorialspoint.com/socket.io/socket.io_event_handling.htm>`_

        :param msg:
        """
        msg = JsUtils.jsConvertData(msg, None)
        return JsObjects.JsVoid("%s.send(%s)" % (self._selector, msg))

    def inRoom(self, room_id, event_type, data=None):
        """

        `tutorialspoint <https://www.tutorialspoint.com/socket.io/socket.io_rooms.htm>`_

        :param room_id: String. The room identifier.
        :param event_type:
        :param data:
        """
        data = JsUtils.jsConvertData(data or {}, None)
        event_type = JsUtils.jsConvertData(event_type, None)
        room_id = JsUtils.jsConvertData(room_id, None)
        return JsObjects.JsVoid("%s.in(%s).emit(%s, %s)" % (self._selector, room_id, event_type, data))

    def connect(self, url=None, port=None, namespace=None, from_config=None):
        """This function will automatically add the socket to the page object.
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

        self.page._props['js']['builders'].add(
            "var %s = io.connect('%s:%s/%s')" % (self._selector, url, port, namespace))
        return JsObjects.JsVoid("var %s = io.connect('%s:%s/%s')" % (self._selector, url, port, namespace))

    def on(self, event_type, js_funcs, profile=False, data_ref: str = "data"):
        """Fired upon a connection from client.

        `tutorialspoint <https://www.tutorialspoint.com/socket.io/socket.io_event_handling.htm>`_
        `SocketIO <https://socket.io/docs/v4/server-api/#event-connection>`_

        :param event_type:
        :param js_funcs:
        :param profile:
        :param data_ref:

        :return: self to allow the chaining
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        event_type = JsUtils.jsConvertData(event_type, None)
        self.page.js.onReady("%s.on(%s, function(%s) {%s})" % (
            self._selector, event_type, data_ref, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))
        return self

    def connection(self, js_funcs, profile=False):
        """

        `Socket <https://socket.io/docs/v4/server-api/#event-disconnecting>`_
        """
        return self.on("connection", js_funcs, profile, data_ref="socket")

    def emit(self, event_type, data=None):
        """Emits an event to all connected clients in the main namespace.

        `SocketIO <https://socket.io/docs/v4/server-api/#serveremiteventname-args>`_

        :param event_type:
        :param data:
        """
        data = JsUtils.jsConvertData(data or {}, None)
        event_type = JsUtils.jsConvertData(event_type, None)
        return JsObjects.JsVoid("%s.emit(%s, %s)" % (self._selector, event_type, data))

    def in_(self, room_id: str):
        """Synonym of namespace.to(room), but might feel clearer in some cases:

        `SocketIO <https://socket.io/docs/v4/server-api/#namespaceinroom>`_
        """
        room_id = JsUtils.jsConvertData(room_id or {}, None)
        return SocketIO("%s.in(%s)" % (self._selector, room_id))

    def of(self, namespace: str):
        """Sets a modifier for a subsequent event emission that the event will only be broadcast to clients that have
        joined the given room.

        `SocketIO <https://socket.io/docs/v4/server-api/#servertoroom>`_
        """
        namespace = JsUtils.jsConvertData(namespace or {}, None)
        return SocketIO("%s.of(%s)" % (self._selector, namespace))

    def to(self, room_id: str):
        """Sets a modifier for a subsequent event emission that the event will only be broadcast to clients that have
        joined the given room.

        `SocketIO <https://socket.io/docs/v4/server-api/#servertoroom>`_
        """
        room_id = JsUtils.jsConvertData(room_id or {}, None)
        return SocketIO("%s.to(%s)" % (self._selector, room_id))

    def except_(self, room_id: str):
        """Sets a modifier for a subsequent event emission that the event will only be broadcast to clients that have
        not joined the given rooms.

        `SocketIO <https://socket.io/docs/v4/server-api/#serverexceptrooms>`_
        """
        room_id = JsUtils.jsConvertData(room_id or {}, None)
        return SocketIO("%s.except(%s)" % (self._selector, room_id))

    def serverSideEmit(self, *args):
        """Sends a message to the other Socket.IO servers of the cluster.

        `SocketIO <hhttps://socket.io/docs/v4/server-api/#namespaceserversideemiteventname-args>`_
        """
        conv_args = [JsUtils.jsConvertData(a, None, force=True) for a in args]
        return JsUtils.jsWrap("%s.serverSideEmit(%s)" % (self._selector, ", ".join(conv_args)))

    def socketsJoin(self):
        ...

    def socketsLeave(self):
        ...

    def timeout(self, num):
        """Sets a modifier for a subsequent event emission that the callback will be called with an error when the
        given number of milliseconds have elapsed without an acknowledgement from the client:

        `Socket <https://socket.io/docs/v4/server-api/#sockettimeoutvalue>`_

        :param num: Time out value in milliseconds
        """
        return JsUtils.jsWrap("%s.timeout(%s)" % (self._selector, num))
