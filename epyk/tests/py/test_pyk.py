from epyk.core.py import Pyk
from epyk.core.Page import Report
pyk_rpt = Pyk.requires(r'C:\Users\nelso\PycharmProjects\epyk-ui\epyk\tests\pyk_report.py')


rpt_obj = Report()

rpt_obj.ui.text("Here we have a text followed by a normal button")

Pyk.register(rpt_obj, pyk_rpt.button)

rpt_obj.ui.text("Then we have an import button")

Pyk.register(rpt_obj, pyk_rpt.imp)

print(rpt_obj.outs.html_file())
