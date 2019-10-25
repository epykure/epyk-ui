from epyk.core.Page import Report
from epyk.tests import test_statics

rptObj = Report()

data = [{"A": 1, "B": 2}]
rptObj.ui.tables.tabulators.table(data, cols=["A"], rows=["B"])

rptObj.outs.browser.codepen(path=test_statics.OUTPUT_PATHS,
                            open_browser=True)
