
import json

from epyk.core.js import JsUtils
from epyk.core.js import Js


jsObj = Js.JsBase()
#data = jsObj.location.postTo("https://codepen.io/pen/define/", {"data": json.dumps({"title": "New Pen!", "html": "<div>Hello, World!</div>"})})

import webbrowser
#webbrowser.open(r"K:\test2.html")
#print(data)

f = JsUtils.JsFile(path=r"../outs")
js_obj = Js.JsBase()
breadcrumb = js_obj.breadcrumb
js_obj.addOnLoad(breadcrumb.add("ok", "test"))
js_obj.addOnLoad(breadcrumb.toClipboard)
f.codepen(js_obj)

