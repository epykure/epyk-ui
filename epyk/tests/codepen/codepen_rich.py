from epyk.core.Ares import Report
from epyk.tests import test_statics

rptObj = Report()

rptObj.ui.rich.stars(3, label="feedbacks")
rptObj.ui.rich.stars(3, label="feedbacks", best=10)
rptObj.ui.rich.textbubble({"value": 23, "title": "Title"}, helper="This is a helper")
rptObj.ui.rich.delta({'number': 100, 'prevNumber': 60, 'thresold1': 100, 'thresold2': 50}, helper="test")
rptObj.ui.rich.vignet({'title': 'Python', 'number': 100, 'text': 'Content', 'color': 'green', 'url':
                       'https://www.python.org/', 'icon': 'fab fa-python', 'tooltip': 'Python Fondation',
                       'urlTitle': 'WebSite'})
rptObj.ui.rich.light("red", label="label", tooltip="Tooltip", helper="Helper")
rptObj.outs.browser.codepen(path=test_statics.OUTPUT_PATHS)