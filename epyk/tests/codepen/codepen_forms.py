from epyk.core.Page import Report
from epyk.tests import test_statics


rpt = Report()


form = rpt.ui.forms.input("youpi", title="Title", label="data")
form.row(1).input.set_attrs(name="placeholder", value="youpi")

#form.add_input("test", "RRR")
form.add_input("test", "ok")
form.add_input("test 2", "Super")
form.add_title("New Title")
form.add_date("New Title")
form.add_text("RRRR", "text")

rpt.ui.options_bar([
  {"icon": 'fab fa-airbnb', 'jsFnc': ''},
  {"icon": 'fas fa-thumbs-up', 'jsFnc': ''}
]).draggable({"scroll": True})
print(form.rows)
rpt.outs.browser.codepen(path=test_statics.OUTPUT_PATHS)