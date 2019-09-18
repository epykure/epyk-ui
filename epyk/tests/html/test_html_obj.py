
from epyk.core.Ares import Report
from epyk.tests import test_statics


# -------------------------------------------------------------------------------------------------------------------
# test button components
#
rptObj = Report()
#rptObj.ui.button("button")
#rptObj.ui.buttons.validate("validate")
#rptObj.ui.buttons.remove("remove")
rptObj.ui.buttons.checkbox("remove")
#rptObj.ui.buttons.zipfile("click me", "test.dat").add()
#rptObj.ui.buttons.radio(["A", "B", "C"])
rptObj.ui.buttons.switch({"off": 'Python', 'on': 'Javascript'})

file_path = rptObj.outs.w3cTryIt(path=test_statics.OUTPUT_PATHS, name="button")
file_path = rptObj.outs.codepen(path=test_statics.OUTPUT_PATHS, name="button")

rptObj.outs.browser.codepen(path=test_statics.OUTPUT_PATHS)

# -------------------------------------------------------------------------------------------------------------------
# test media components
#
rptObj = Report()
#rptObj.ui.media.audio("")
#rptObj.ui.media.video("")
rptObj.ui.media.youtube("https://www.youtube.com/embed/dfiHMtih5Ac ")
file_path = rptObj.outs.w3cTryIt(path=test_statics.OUTPUT_PATHS, name="media")


# -------------------------------------------------------------------------------------------------------------------
# test check components
#
rptObj = Report()
check = rptObj.ui.check(False, label="test")
file_path = rptObj.outs.w3cTryIt(path=test_statics.OUTPUT_PATHS, name="check")




#test_statics.open_url(test_statics.URL_w3c)
