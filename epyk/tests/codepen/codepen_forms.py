from epyk.core.Page import Report
from epyk.tests import test_statics


rpt = Report()


form = rpt.ui.forms.input("youpi", title="Title", label="data")
#form.add_input("test", "RRR")
form.add_input("test", "ok")
form.add_row([])

print(form.rows[0].toStr())
rpt.outs.browser.codepen(path=test_statics.OUTPUT_PATHS)