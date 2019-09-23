
from epyk.core.js import JsUtils
from epyk.core.js import Js




f = JsUtils.JsFile(path=r"../outs")
js_obj = Js.JsBase()
breadcrumb = js_obj.breadcrumb
js_obj.addOnLoad(breadcrumb.add("test1", "value1"))
js_obj.addOnLoad(breadcrumb.add("test2", "value2"))
js_obj.addOnLoad(breadcrumb.hash("test3"))
js_obj.addOnLoad(js_obj.clipboard(breadcrumb.url))
f.codepen(js_obj)

