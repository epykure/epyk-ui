from epyk.core.js import Js
from epyk.core.js import JsUtils


# ------------------------------------------------------------------------------------------------------------------
#
f = JsUtils.JsFile("jsWindows", path=r"../outs")
jsObj = Js.JsBase()
f.writeJs([
  jsObj.window.btoa("Test").setVar("bin"),
  jsObj.createElement("div", "MyDiv").text(jsObj.objects.get("bin")).css({"color": 'red'}),
  jsObj.body.appendChild(jsObj.objects.get("MyDiv")),
  jsObj.console.log(jsObj.objects.get("bin")),
  jsObj.console.log(jsObj.window.atob(jsObj.objects.get("bin"))),
  jsObj.window.setInterval([jsObj.console.log(jsObj.math.random())], 500).setVar("interva1"),
  jsObj.window.clearInterval(jsObj.objects.get("interva1")),
  jsObj.sessionStorage.setItem("lastname", jsObj.objects.get("bin")),
  jsObj.sessionStorage.removeItem("lastname"),
  jsObj.console.log(jsObj.sessionStorage["lastname"])
])
f.close()


# ------------------------------------------------------------------------------------------------------------------
#
jsObj = Js.JsBase()
f = JsUtils.JsFile("Maths", path=r"../outs")
f.writeJs([
  jsObj.objects.number.new(23.6, varName="MyNumber"),
  jsObj.console.log(jsObj.math.log(2)),
  jsObj.console.log(jsObj.math.E),
  jsObj.console.log(jsObj.math.LN2),
  jsObj.console.log(jsObj.math.LN10),
  jsObj.console.log(jsObj.math.SQRT1_2),
  jsObj.console.log(jsObj.math.random()),
  jsObj.console.log(jsObj.math.random(10, 100)),
  jsObj.console.log(jsObj.math.min(10, 45, 100, -3, 56)),
  jsObj.console.log(jsObj.math.max(10, 45, 100, -3, 56)),
  jsObj.console.log(jsObj.math.floor(jsObj.objects.number.get("MyNumber"))),
  jsObj.console.log(jsObj.math.trunc(jsObj.objects.number.get("MyNumber"))),
  jsObj.console.log(jsObj.math.round(jsObj.objects.number.get("MyNumber"))),
  jsObj.console.log(jsObj.math.sqrt(jsObj.objects.number.get("MyNumber"))),
  jsObj.console.log(jsObj.math.ceil(jsObj.objects.number.get("MyNumber"))),
  jsObj.console.log(jsObj.math.pow(jsObj.objects.number.get("MyNumber"), 2)),
])
f.close()


# ------------------------------------------------------------------------------------------------------------------
#
f = JsUtils.JsFile("Peformance", path=r"../outs")
jsObj = Js.JsBase()
f.writeJs([
  jsObj.performance.mark("youpi"),
  jsObj.performance.measure("youpi"),
  jsObj.console.log(jsObj.performance.now),
  jsObj.console.log(jsObj.performance.getEntriesByName("youpi")),
  jsObj.console.log(jsObj.performance.toJSON()),
  jsObj.console.log(jsObj.performance.now),
])

f.close()


# ------------------------------------------------------------------------------------------------------------------
#
f = JsUtils.JsFile('Location', path=r"../outs")
jsObj = Js.JsBase()
f.writeJs([
  jsObj.console.log(jsObj.location.hostname),
  jsObj.console.log(jsObj.location.pathname),
  jsObj.console.log(jsObj.location.hash),
])
f.close()


# ------------------------------------------------------------------------------------------------------------------
#
jsObj = Js.JsBase()
f = JsUtils.JsFile('Numbers', path=r"../outs")
f.writeJs([
  jsObj.objects.NaN,
  jsObj.console.log(jsObj.objects.NaN),
  jsObj.console.log(jsObj.objects.number.POSITIVE_INFINITY()),
  jsObj.console.log(jsObj.objects.number.MAX_VALUE()),

])
f.close()