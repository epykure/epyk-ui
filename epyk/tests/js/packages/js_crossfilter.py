from epyk.core.js import Js
from epyk.core.js import JsUtils
from epyk.tests import test_statics


jsObj = Js.JsBase()
crossFilter = jsObj.data.crossfilter(data=[], var_name="test")
print(crossFilter.toStr())
print(crossFilter.dimension("column").filterAll().filterRange(100, 40).top(10).toStr())

f = JsUtils.JsFile("CrossFilter", path=test_statics.OUTPUT_PATHS)
f.writeJs([

])
f.close()