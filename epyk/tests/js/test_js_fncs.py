
from epyk.core.js import Js
from epyk.core.js import JsUtils
from epyk.core.js.fncs import JsFncsRecords

jsObj = Js.JsBase()
jsObj.registerFunction("row-buckets")


f = JsUtils.JsFile("RowBucket", path=r"../outs")
f.writeReport(jsObj)
f.close()


