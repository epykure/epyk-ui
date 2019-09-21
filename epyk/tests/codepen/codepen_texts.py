from epyk.core.Ares import Report
from epyk.tests import test_statics


rptObj = Report()

text = rptObj.ui.texts.text("Test text").css({"color": 'red'})
rptObj.ui.texts.number(188448228, label="test")
rptObj.ui.texts.title("title").css({"color": 'green'})
rptObj.ui.texts.highlights("This is a news", title="Important news")


button = rptObj.ui.button("click me")
button.click([rptObj.js.window.alert("ok"), text.jsGenerate("Youpi", isPyData=True)])

rptObj.outs.browser.codepen(path=test_statics.OUTPUT_PATHS)