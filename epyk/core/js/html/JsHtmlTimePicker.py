"""

"""

from epyk.core.js.objects import JsNodeDom


class JsHtmlTimePicker(JsNodeDom.JsDoms):
  def __init__(self, htmlObj):
    super(JsHtmlTimePicker, self).__init__(htmlObj)
    self._jqueryui = None
