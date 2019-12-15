"""
Module in charge of the testing of the trees
"""


from epyk.core.Page import Report
from epyk.tests import test_statics

# Create a basic report object
rptObj = Report()

rptObj.ui.rich.textbubble({"value": 23, "title": "Title"}, helper="This is a helper")
rptObj.ui.rich.delta({'number': 100, 'prevNumber': 60, 'thresold1': 100, 'thresold2': 50}, helper="test")
rptObj.ui.rich.stars(3, label="test", helper="This is a helper")
rptObj.ui.rich.textborder({"title": "New Python Framework", 'value': "A new Python Web Framework", 'color': 'green',
                             'icon': 'fab fa-python', 'colorTitle': 'darkgreen'})
rptObj.ui.rich.light("red", label="label", tooltip="Tooltip", helper="Helper")
rptObj.ui.info("Test")
rptObj.ui.rich.number(500, "Test")
rptObj.ui.rich.update("Last update: ")
rptObj.ui.rich.prism("print('test')")


# rptObj.ui.rich.countdown("2050-09-24")
#rptObj.ui.rich.blocktext({"text": 'This is a brand new python framework', "title": 'New Python Web Framework',
#                          "button": {"text": 'Get Started', 'url': "/getStarted"}, 'color': 'green'})

print(rptObj.outs.html_file(path=test_statics.OUTPUT_PATHS, name="report_rich_text"))
