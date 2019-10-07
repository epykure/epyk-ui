from epyk.core.js import Js
from epyk.core.js import JsUtils
from epyk.tests import test_statics


jsObj = Js.JsBase()

f = JsUtils.JsFile("CrossFilter", path=test_statics.OUTPUT_PATHS)
f.writeJs([

])
f.close()