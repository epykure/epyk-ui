

from epyk.core.js.packages import JsPackage
from epyk.core.js.primitives import JsObjects


class Json(JsPackage):
  lib_alias = {"js": "json-formatter", 'css': "json-formatter"}

  def openAtDepth(self, n):
    """
    Default: 1 This number indicates up to how many levels the rendered tree should open.
    It allows use cases such as collapse all levels (with value 0) or expand all levels (with value Infinity).

    Attributes:
    ----------
    :param n: Integer. the depth of the tree at start
    """
    return JsObjects.JsObjects.get('%s.openAtDepth(%s)' % (self.varName, n))
