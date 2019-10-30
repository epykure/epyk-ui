"""

"""
from epyk.core.Page import Report
from epyk.tests import test_statics


# Create a basic report object
rpt = Report()

rpt.ui.lists.badges([{'label': 'Python', 'value': 12}, {'label': 'R', 'value': 3}])

rpt.ui.lists.accordeon([{'value': 'super', 'url': "google", 'category': 'Test', 'icon': 'fas fa-heart'},
                        {'value': 'super2', 'url': "google", 'category': 'Youpi', 'icon': 'fab fa-google'},
                        {'value': 'super3', 'url': "google", 'category': 'Youpi'}])


rpt.ui.lists.points([{'label': 'Python', 'url': 'https://www.python.org/'}, {'label': 'R'}])

rpt.outs.browser.codepen(path=test_statics.OUTPUT_PATHS)