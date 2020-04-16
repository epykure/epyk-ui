"""
Wrapper to the Javascript Socket module

Related Pages:

	ttps://www.tutorialspoint.com/html5/html5_websocket.htm
  https://blog.miguelgrinberg.com/post/easy-websockets-with-flask-and-gevent
"""


from epyk.core.js import JsUtils


class JsWebSocket(object):
  def __init__(self, htmlCode, url, protocol, service, context=None):
    """

    :param src:
    :param htmlCode:
    :param url:
    :param protocol:
    :param service:
    """
    wsId = JsUtils.jsConvert(htmlCode)
    self._context = context if context is not None else {}
    self._context.setdefault("modules", set()).add('socket.io')
    self._context.setdefault('onReady', []).append("%s = io.connect('%s:%s/%s')" % (wsId, url, protocol, service))
    self._js, self.wsId = [], wsId

  def send(self, message):
    """

    :return:
    """

  def close(self):
    """

    :return:
    """

  def open(self, jsFncs):
    """

    :param jsFncs:
    :return:
    """

  def message(self, jsFncs):
    """

    :param jsFncs:
    :return:
    """
