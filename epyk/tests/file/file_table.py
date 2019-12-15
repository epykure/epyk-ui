"""
Module in charge of the testing of the trees
"""


from epyk.core.Page import Report
from epyk.tests import test_statics

# Create a basic report object
rptObj = Report()

records = [
  {"label": 'python', 'value': 12},
  {"label": 'Java', 'value': 5},
  {"label": 'Javascript', 'value': 80}]
rptObj.ui.charts.skillbars(records, y_column=['value'], x_axis=['label']).css({"width": '100px'})

records = [["title 1", "title 2"], [True, 2], [3, 4]]
table = rptObj.ui.layouts.table(records)
table.style.clear()
for cell in table.col(i=1):
  cell.css({"color": 'red'})

table.row(i=1)[1].css({"background": 'green'})
table.row(i=1)[0].set_html_content(rptObj.ui.rich.light(table.row(i=1)[0].val, label="ok", tooltip="test"))
table.add([2, 87])

print(rptObj.outs.html_file(path=test_statics.OUTPUT_PATHS, name="report_table"))
