"""
Create a HTML page only from JavaScript functions
"""

from epyk.core.js import Js
from epyk.core.js import JsUtils
from epyk.core.js.packages import JsDatatable
from epyk.tests import test_statics

# Create a blank Javascript Python object
jsObj = Js.JsBase()

# Write the results to a Javascript file with a Launcher
f = JsUtils.JsFile("TestDatatable", path=test_statics.OUTPUT_PATHS)

tab = JsDatatable.DatatableAPI(selector="table", setVar=False)
cell = JsDatatable.CellAPI()

f.writeJs([
  tab.order().draw().destroy(),
  tab.data().length,
  cell.select().deselect(),
  tab.jquery_node().text("")
])

# Close the file and print the location of the launcher
print(f.close(jsObj))