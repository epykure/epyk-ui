"""

"""


from epyk.core.Page import Report
from epyk.tests import test_statics


# Create a basic report object
rptObj = Report()

bs = rptObj.ui.menus.buttons(["Button", "Button 2", "Button 3"])
bs[2].click([
  rptObj.js.alert(bs[2].dom.content)
])

print(rptObj.outs.html_file(path=test_statics.OUTPUT_PATHS, name="report_menu"))
