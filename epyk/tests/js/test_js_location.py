
import json

from epyk.core.js import Js


jsObj = Js.JsBase()
#data = jsObj.location.postTo("https://codepen.io/pen/define/", {"data": json.dumps({"title": "New Pen!", "html": "<div>Hello, World!</div>"})})

import webbrowser
#webbrowser.open(r"K:\test2.html")
#print(data)

js_obj = Js.JsBase()
breadcrumb = js_obj.breadcrumb

js_obj.addOnLoad(breadcrumb.add("ok", "test"))
js_obj.addOnLoad(breadcrumb.toClipboard)
print(breadcrumb._src._props['js'])
