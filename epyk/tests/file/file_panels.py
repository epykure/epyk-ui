"""

"""


from epyk.core.Page import Report
from epyk.tests import test_statics


# Create a basic report object
rptObj = Report()

p = rptObj.ui.panels.pills()
p.add_panel("Pill 1", rptObj.ui.col([rptObj.ui.text("test 1")]))
p.add_panel("Pill 2", rptObj.ui.col([rptObj.ui.text("test 2")]), selected=True)
p.add_panel("Pill 3", rptObj.ui.col([rptObj.ui.text("test 3")]))

tabs = rptObj.ui.panels.arrows_down()
tabs.add_panel("tab 1, this is something", rptObj.ui.col([rptObj.ui.text("test 1, this is for something")]))
tabs.add_panel("tab 2", rptObj.ui.col([rptObj.ui.text("test 2")]))
tabs.add_panel("tab 3", rptObj.ui.col([rptObj.ui.text("test 3")]))


tabs = rptObj.ui.panels.arrows_up()
tabs.add_panel("tab 1, this is something", rptObj.ui.col([rptObj.ui.text("test 1, this is for something")]))
tabs.add_panel("tab 2", rptObj.ui.col([rptObj.ui.text("test 2")]))
tabs.add_panel("tab 3", rptObj.ui.col([rptObj.ui.text("test 3")]))

print(rptObj.outs.html_file(path=test_statics.OUTPUT_PATHS, name="report_panel"))
