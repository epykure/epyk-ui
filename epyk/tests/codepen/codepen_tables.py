from epyk.core.Page import Report
from epyk.tests import test_statics

rptObj = Report()

data = [{"A": 1, "B": 2}]
rptObj.ui.tables.tabulators.table(data, cols=["A"], rows=["B"])

datatable = rptObj.ui.tables.datatables.table(data, cols=["A"], rows=["B"])

datatable.dom.addOnReady([
  datatable.js.clear(update=True),
  datatable.js.rows.add(
    [
      {"A": "A", "B": 5454},
      {"A": "B", "C": 5454},
    ], toArray=True).draw()
])

rptObj.js.addOnReady(
  [
    rptObj.js.window.alert("Test")
  ]
)
rptObj.outs.browser.codepen(path=test_statics.OUTPUT_PATHS, open_browser=True)