from epyk.core.js import Js
from epyk.core.js import JsUtils
from epyk.tests import test_statics


jsObj = Js.JsBase()
crossFilter = jsObj.data.crossfilter(data=[{"column": 200}], var_name="test")

f = JsUtils.JsFile("CrossFilter", path=test_statics.OUTPUT_PATHS)
f.writeJs([
  crossFilter.toStr(),
  crossFilter.dimension("column").filterAll().filterRange(100, 400).top(10).toStr(),
  jsObj.console.log(crossFilter.var)
])
print(f.close(jsObj))