
import json

from epyk.core.js import Js


jsObj = Js.JsBase()
data = jsObj.location.postTo("https://codepen.io/pen/define/", {"data": json.dumps({"title": "New Pen!", "html": "<div>Hello, World!</div>"})})

print(data)