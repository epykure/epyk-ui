from epyk.core.Page import Report
from epyk.tests import test_statics


rpt = Report()


rpt.ui.forms.input("youpi", title="Title", label="data")


rpt.outs.browser.codepen(path=test_statics.OUTPUT_PATHS)