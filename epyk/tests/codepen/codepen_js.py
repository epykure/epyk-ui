
from epyk.core.js import Js
from epyk.core.css import Css
from epyk.core.js import JsUtils

jsObj = Js.JsBase()

css_obj = Css.Css(jsObj._src)
css_obj.globals.new_class("test", {"color": "red"})
css_obj.globals.new_class("test_2", {"color": "blue", "cursor": 'pointer'})

dom = jsObj.createElement("div", varName="id_test")
dom_click = jsObj.createElement("div", varName="id_click")
# dom.toggleClass("test")

print( css_obj.colors.defined.rgb.AQUA )

jsObj.addOnLoad([
  dom.text("toto").className("test"),
  dom_click.text("Click Me").className("test_2"),
  dom_click.onclick(jsObj.objects.dom.get("id_test").toggleAttrs("color", "red",
                                                                 {"color": 'red', 'background': "pink"},
                                                                 {"color": "yellow"})),
  jsObj.body.appendChild(dom_click),
  jsObj.body.appendChild(dom),
])

f = JsUtils.JsFile(path=r"../outs")
f.codepen(jsObj, cssObj=css_obj)
