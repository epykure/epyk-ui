"""

"""

from epyk.core.js import Js
from epyk.core.js import JsUtils
from epyk.tests import test_statics

from epyk.core.js.packages import JsChartJs
from epyk.core.Page import Report


# Create a blank Javascript Python object
rptObj = Report()

f = JsUtils.JsFile("DataExamplesChartJs", path=test_statics.OUTPUT_PATHS)

data = test_statics.get_data("flights.txt", n=10)
record = rptObj.js.data.records(data)
data_fnc = record.fnc.count(["origin", "destination"], ["distance", "delay"])

chart = JsChartJs.ChartJs("test", rptObj, setVar=False)


f.writeJs([
  #jsObj.console.log(data_fnc),
  rptObj.js.console.log(record.to.chartJs.line(["distance"], "origin")),
  rptObj.js.console.log(chart)
])

# Close the file and print the location of the launcher
print(f.close(rptObj))
