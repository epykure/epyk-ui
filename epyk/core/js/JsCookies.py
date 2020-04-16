"""

"""

from epyk.core.js import Js
from epyk.core.js import JsUtils


class JsCookies(object):
  class __internal(object):
    _context = {}

  def __init__(self, src=None):
    self.src = src if src is not None else self.__internal()

  def set(self, jsKey, jsData, jsDataKey=None, isPyData=True, jsFnc=None):
    """

    Related Pages:

			https//www.w3schools.com/js/js_cookies.asp

    :return:
    """
    jsData = JsUtils.jsConvert(jsData, jsDataKey, isPyData, jsFnc)
    if self.src._context.get('cookies') is None:
      self.src._context['cookies'] = True
      return "document.cookies = {'%s': %s}" % (jsKey, jsData)

    return "document.cookies['%s'] = %s" % (jsKey, jsData)

  def get(self, jsData=None, jsDataKey=None, isPyData=True, jsFnc=None):
    """

    :return:
    """
    if jsData is None:
      return Js.JsJson().parse("decodeURIComponent(document.cookies)", isPyData=False)

    jsData = JsUtils.jsConvert(jsData, jsDataKey, isPyData, jsFnc)
    return Js.JsJson().parse("decodeURIComponent(document.cookies)['%s']" % jsData, isPyData=False)
