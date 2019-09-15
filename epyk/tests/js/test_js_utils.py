from epyk.core.js import JsUtils


print(JsUtils.getJsValid("Test", fail=False))
print(JsUtils.getJsValid("1Test", fail=False))
print(JsUtils.getJsValid("tes-t", fail=False))