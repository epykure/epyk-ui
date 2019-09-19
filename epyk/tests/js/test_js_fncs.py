
from epyk.core.js import Js
from epyk.core.js.fncs import JsFncsRecords

jsObj = Js.JsBase()
jsObj.registerFunction("row-buckets")
print(jsObj._src._props)

