"""

"""

from epyk.core.js import Js
from epyk.core.js import JsUtils
from epyk.tests import test_statics


# Create a blank Javascript Python object
jsObj = Js.JsBase()

# Write the results to a Javascript file with a Launcher
f = JsUtils.JsFile("DataExamplesNvd3", path=test_statics.OUTPUT_PATHS)

# Load the data from the static sample file
data = test_statics.get_data("flights.txt", n=10)

# Create the data object
record = jsObj.data.records(data)

#record.f.count("B").o.nvd3_bar("count", "column") #.top("count_distinct", n=2, order="asc")
#record.f.count("B").o.nvd3.pie("count", "column") #.top("count_distinct", n=2, order="asc")
#record.f.count("B").o.billboard.line("count", "column") #.top("count_distinct", n=2, order="asc")

text = jsObj.string("1234455").toFormattedNumber()
data_fnc = record.fnc.count_with_kpi(["origin", "destination"], ["distance", "delay"])

# Write the Javascript fragments to the file
f.writeJs([
  jsObj.console.log(data_fnc), #.a.eq("B", "RR5")),
  #jsObj.console.log(data_fnc.filter.in_("origin", ["MCI", "STL"])), #.a.eq("B", "RR5")),
  #jsObj.console.log(data_fnc.filter.in_("column", "origin")), #.a.eq("B", "RR5")),
  jsObj.console.log(record.to.nvd3.pie(["distance"], "origin")),
])

import json

#data = test_statics.get_data("stocks.json")

# Close the file and print the location of the launcher
print(f.close(jsObj))
