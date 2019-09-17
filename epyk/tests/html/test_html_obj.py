
from epyk.core.Ares import Report
from epyk.tests import test_statics


rptObj = Report()

check = rptObj.ui.button("test")


file_path = rptObj.outs.w3cTryIt(path=test_statics.OUTPUT_PATHS)
print(file_path)

test_statics.open_url(test_statics.URL_w3c)