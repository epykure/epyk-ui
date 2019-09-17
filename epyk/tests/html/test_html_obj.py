
from epyk.core.Ares import Report
from epyk.tests import test_statics


# -------------------------------------------------------------------------------------------------------------------
# test button components
rptObj = Report()
check = rptObj.ui.button("test")
file_path = rptObj.outs.w3cTryIt(path=test_statics.OUTPUT_PATHS)



# -------------------------------------------------------------------------------------------------------------------
# test button components
rptObj = Report()

#test_statics.open_url(test_statics.URL_w3c)