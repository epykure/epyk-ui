from epyk.core.Ares import Report
from epyk.tests import test_statics

rptObj = Report()

l = rptObj.ui.links.link('data', 'www.google.fr', icon="fas fa-align-center", options={"target": "_blank"})

rptObj.ui.layouts.new_line()

b = rptObj.ui.images.badge("new")
l.append_child(b)

rptObj.ui.layouts.new_line()

rptObj.ui.links.data("test#data", value="this is a test")

rptObj.outs.browser.codepen(path=test_statics.OUTPUT_PATHS)