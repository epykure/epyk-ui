from epyk.core.Ares import Report
from epyk.tests import test_statics


rptObj = Report()

rptObj.ui.texts.text("Test text").css({"color": 'red'})
rptObj.ui.texts.number(188448228, label="test")
rptObj.ui.texts.title("title").css({"color": 'green'})
rptObj.ui.texts.highlights("This is a news", title="Important news")

rptObj.outs.browser.codepen(path=test_statics.OUTPUT_PATHS)