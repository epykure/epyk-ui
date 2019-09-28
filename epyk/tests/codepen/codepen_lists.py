from epyk.core.Page import Report
from epyk.tests import test_statics


rpt = Report()

rpt.ui.lists.list([{'label': 'Python', 'url': 'https://www.python.org/'}, {'label': 'R'}])

rpt.outs.browser.codepen(path=test_statics.OUTPUT_PATHS)