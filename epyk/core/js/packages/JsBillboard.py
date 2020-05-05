

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects
from epyk.core.js.packages import JsC3


class Billboard(JsC3.C3):

  def export(self):
    """
    Export chart as an image.

    https://naver.github.io/billboard.js/release/latest/doc/Chart.html#export
    """
    return JsObjects.JsVoid("%s.export()" % self._selector)

  def revert(self, target=None):
    """
    Export chart as an image.

    https://naver.github.io/billboard.js/release/latest/doc/Chart.html#export

    :param target: String | Array. ids to be reverted
    """
    target = JsUtils.jsConvertData(target, None)
    return JsObjects.JsVoid("%s.revert(%s)" % (self._selector, target))
