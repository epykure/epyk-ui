from epyk.core.Ares import Report
from epyk.tests import test_statics

rptObj = Report()
button = rptObj.ui.button("Test", icon="fab fa-codepen")
button.click([rptObj.js.window.alert("test")])

button2 = rptObj.ui.buttons.validate("phone")
button2.click([rptObj.js.window.alert("phone")])
button2.css({"margin-left": '5px'})
rptObj.outs.browser.codepen(path=test_statics.OUTPUT_PATHS)
