
from epyk.core.Ares import Report


rptObj = Report()

check = rptObj.ui.button("test")

# path=r"../outs"
print(rptObj.outs.jupyter()._repr_html_())