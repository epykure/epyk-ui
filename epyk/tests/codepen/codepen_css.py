from epyk.core.Page import Report
from epyk.tests import test_statics

rptObj = Report()

data = [{"A": 1, "B": 2}]
rptObj.ui.tables.tabulators.table(data, cols=["A"], rows=["B"])

rptObj.style.globals.overflow.thumb(
  {"-webkit-box-shadow": "inset 0 0 2px rgba(0,0,0,0.5)", "border-radius": "10px"},
  {"background": "green"},
  {"background": "red"},
)

rptObj.outs.browser.codepen(path=test_statics.OUTPUT_PATHS, target="_self")