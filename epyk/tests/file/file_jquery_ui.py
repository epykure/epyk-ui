"""
Module in charge of the testing of the trees
"""


from epyk.core.Page import Report
from epyk.tests import test_statics

# Create a basic report object
rptObj = Report()

p = rptObj.ui.sliders.progressbar(30)
rptObj.ui.date()
t = rptObj.ui.fields.today()
t.selectable(["2019-09-01", "2019-09-06"])
ti = rptObj.ui.fields.now()
s = rptObj.ui.slider(recordSet=[1, 2, 3, 4, 5, 6, 7])

b = rptObj.ui.button("Get")

b.click([
  rptObj.js.alert(t.dom.content),
  #rptObj.js.alert(p.dom.content),
  rptObj.js.alert(s.dom.content),
  #rptObj.js.alert(ti.input.dom.content),
])

print(rptObj.outs.html_file(path=test_statics.OUTPUT_PATHS, name="report_jquery_ui"))
