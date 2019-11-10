"""

"""

from epyk.core.js.objects import JsNodeDom
from epyk.core.js.packages import JsTabulator


class JsHtmlTabulator(JsNodeDom.JsDoms):
  def __init__(self, htmlObj):
    super(JsHtmlTabulator, self).__init__(htmlObj)
    self._tabulator = None

  @property
  def tabulator(self):
    """

    :return:
    :rtype: JsTabulator.Tabulator
    """
    if self._tabulator is None:
      self._tabulator = JsTabulator.Tabulator(self._src)
    return self._tabulator
