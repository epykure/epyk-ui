"""
Test section to write Markdown files
"""

from epyk.core.Page import Report
from epyk.tests import test_statics


# Create an empty report in the webpage
rptObj = Report()
rptObj.ui.sliders.progressbar(300)


# Transpile to Javascriot and create a report in codepen (python will automatically open the default browser)
rptObj.outs.markdown_file(path=test_statics.OUTPUT_PATHS)
