"""
Create a HTML page only from JavaScript functions
"""

from epyk.core.js import Js
from epyk.core.js import JsUtils
from epyk.core.js.packages import JsTabulator
from epyk.tests import test_statics

# Create a blank Javascript Python object
jsObj = Js.JsBase()

# Write the results to a Javascript file with a Launcher
f = JsUtils.JsFile("TestTabulator", path=test_statics.OUTPUT_PATHS)

tab = JsTabulator.Tabulator(selector="table", setVar=False)


col = JsTabulator.ColumnComponent()
col.delete()

f.writeJs([
  tab.getColumns.forEach(jsObj.console.log("column")).table.addRow({"test": "ok"}),
  col
])

# Close the file and print the location of the launcher
print(f.close(jsObj))