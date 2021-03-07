
from epyk.core.js.packages import JsPackage
from epyk.core.js.primitives import JsObjects


class Mathjax(JsPackage):
  lib_alias = {"js": 'mathjax'}
  lib_set_var = False

  def typesetClear(self):
    return JsObjects.JsVoid("MathJax.typesetClear([%s])" % self.varId)

  def typeset(self):
    return JsObjects.JsVoid("MathJax.typeset([%s])" % self.varId)
