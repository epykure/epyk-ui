import pytest

from epyk.core.js import Js
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsNumber


jsObj = Js.JsBase()

print(jsObj.objects.number.new(349.673, "MyNumber").toStr())



jsObj = Js.JsBase()
f = JsUtils.JsFile(os.path.basename(__file__).split(".")[0], path=r"C:\Users\olivier\Documents\youpi\jsFiles")
f.writeJs([
jsObj.objects.array.new([2, 5, 12, -3], "MyArray"),
jsObj.objects.array.new([3, -9, 2, -6], "MyArray2"),
jsObj.objects.array.new([], "MyArray3"),
jsObj.console.log(jsObj.objects.array.get("MyArray3").concat(jsObj.objects.array.get("MyArray"), jsObj.objects.array.get("MyArray2"))),
jsObj.console.log(jsObj.objects.array.get("MyArray").findIndex([
  jsObj.if_(jsObj.data.loop.val <= 0, [
    jsObj.return_(jsObj.objects.true)]).else_(jsObj.return_(jsObj.objects.false)),
])),

jsObj.console.log(jsObj.objects.array.get("MyArray").map([
  jsObj.data.loop.val * jsObj.math.max(jsObj.data.loop.arr.toArgs()),
  jsObj.return_(jsObj.data.loop.val)
])),
jsObj.console.log("########"),
# jsObj.console.log(jsObj.objects.array.get("MyArray")),
# jsObj.console.log(jsObj.objects.array.get("MyArray").reverse()),
# jsObj.console.log(jsObj.objects.array.get("MyArray").push(55, -17)),
# jsObj.console.log(jsObj.objects.array.get("MyArray")),
# jsObj.console.log(jsObj.objects.array.get("MyArray").pop()),
# jsObj.console.log(jsObj.objects.array.get("MyArray").join("_")),
# jsObj.console.log(jsObj.objects.array.get("MyArray").slice(3, 5)),
# jsObj.console.log(jsObj.objects.array.get("MyArray").sort()),
jsObj.console.log(jsObj.objects.array.new([2, 5, 12, -3], "MyArray").shift()),
jsObj.console.log(jsObj.objects.array.get("MyArray").delete(2)),
jsObj.console.log(jsObj.objects.array.get("MyArray").unshift(22)),
#jsObj.console.log(jsObj.objects.array.get("MyArray").fill("Olivier", 0, 5)),
jsObj.console.log(jsObj.objects.array.get("MyArray")),
jsObj.objects.array.get("MyArray").copyWithin().setVar("youpi"),
#jsObj.console.log(jsObj.objects.array.get("youpi").append(jsObj, 34).append(jsObj, -47)),
#jsObj.while_()
# jsObj.console.log(jsObj.objects.array.get("MyArray").reduce([
#     jsObj.data.reduce.val + jsObj.data.reduce.rVal,
#     jsObj.return_(jsObj.data.reduce.val)
#   ]).add(2)
#)
])
f.close()


# Boolean
jsObj = Js.JsBase()
f = JsUtils.JsFile(os.path.basename(__file__).split(".")[0], path=r"C:\Users\olivier\Documents\youpi\jsFiles")
f.writeJs([
  jsObj.objects.boolean.new(False, "testBool"),
  jsObj.console.log(jsObj.objects.boolean.get("testBool")),
  jsObj.console.log(jsObj.objects.boolean.get("testBool").valueOf()),
  jsObj.console.log(jsObj.objects.boolean.get("testBool").not_),
])
f.close()


# Dates

from epyk.core.js import Js

f = JsUtils.JsFile("jsDate", path=r"C:\Users\olivier\Documents\youpi\jsFiles")

dt = JsDate.new("2019-05-03")
f.writeJs([dt,
  Js.JsConsole().log(dt.getDay()),
  Js.JsConsole().log(dt.getFullYear())])

jsObj = Js.JsBase()
domObj = jsObj.createElement("a").text("Toupi 4").attr({"href": 'google', "title": 'google2'}).css({"color": "red"})
f.writeJs(domObj)
f.writeJs(jsObj.title(""))
f.writeJs(jsObj.objects.date.new("2019-01-01", varName="dateTest"))
#f.writeJs(jsObj.objects.date.get("dateTest").setMonth(7))
f.writeJs(jsObj.console.log(jsObj.objects.date.get("dateTest").addDays(jsObj, 7)))
f.writeJs(jsObj.console.log(jsObj.objects.date.get("dateTest").isWeedend))
f.writeJs(jsObj.console.log("#################"))
f.writeJs(jsObj.console.log(jsObj.objects.date.get("dateTest").getDate().add(jsObj.objects.date.get("2019-01-05"))))
f.writeJs(jsObj.console.log(jsObj.objects.date.get("dateTest").add(jsObj.objects.number.get("5"))))
f.writeJs(jsObj.console.log(jsObj.objects.date.get("dateTest").add(5)))
#f.writeJs(jsObj.console.log(jsObj.objects.date.get("dateTest").getMonth()))
f.writeJs(jsObj.console.log(jsObj.objects.date.get("dateTest").getStrTimeStamp()))
f.writeJs(jsObj.console.log(jsObj.body))
f.writeJs(jsObj.body.appendChild(domObj))

f.close(jsObj)


# Number

import os

from epyk.core.js import Js
from epyk.core.js import JsUtils

jsObj = Js.JsBase()
f = JsUtils.JsFile(os.path.basename(__file__).split(".")[0], path=r"C:\Users\olivier\Documents\youpi\jsFiles")
f.writeJs([
  jsObj.objects.number.new(349.673, "MyNumber"),
  jsObj.console.log(jsObj.objects.number.get("MyNumber").toPrecision(2)),
  jsObj.console.log(jsObj.objects.number.get("MyNumber").isFinite()),
  jsObj.console.log(jsObj.objects.number.get("MyNumber").toFixed()),
  jsObj.console.log(jsObj.objects.number.get("MyNumber").NEGATIVE_INFINITY),
  jsObj.console.log(jsObj.objects.number.get("MyNumber").toExponential()),
])
f.close()


# Object

import os
from epyk.core.js import Js

jsObj = Js.JsBase()
f = JsUtils.JsFile(os.path.basename(__file__).split(".")[0], path=r"C:\Users\olivier\Documents\youpi\jsFiles")
f.writeJs([
  jsObj.objects.new({}, varName="MyObject"),
  jsObj.objects.number.new(13, varName="MyNumber"),
  jsObj.console.log(jsObj.objects.get("MyObject").isSealed()),
  jsObj.objects.get("MyObject").setattr("youpi", jsObj.objects.number.get("MyNumber")),
  jsObj.console.log(jsObj.objects.get("MyObject").isArray()),
  #jsObj.objects.get("MyObject").seal(),
  jsObj.objects.get("MyObject").setattr("test", 45),
  jsObj.console.log(jsObj.objects.get("MyObject").isSealed()),
  jsObj.console.log(jsObj.objects.get("MyObject")),
  jsObj.console.log(jsObj.objects.get("MyObject")["youpi"]),
  jsObj.objects.get("MyObject").keys().forEach([
    jsObj.console.log(jsObj.data.loop.val)]),
])
f.close()



# String

import os
from epyk.core.js import Js

jsObj = Js.JsBase()
f = JsUtils.JsFile(os.path.basename(__file__).split(".")[0], path=r"C:\Users\olivier\Documents\youpi\jsFiles")

string = JsString.new("te st", "testStr")
f.writeJs([
#print(string.length.toStr())
  string,
  string.split(" "),
  string.parseFloat().isNaN(),
  string.endsWith("st"),
  string.charCodeAt(2),
  string.freeze(),
  JsString.new("2019-08-03", "testDate").toDate().setVar("MyDate"),
  jsObj.console.log(jsObj.objects.date.get("MyDate").addDays(jsObj, 6).getStrDate())
])
f.close(jsObj)