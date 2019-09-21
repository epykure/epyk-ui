
from epyk.core.js.configs import JsConfig
from epyk.core import Ares


report = Ares.Report()

chart_type = 'hbar'
configs = JsConfig.get(chart_type, chartFam='Billboard', preferred=False)


print(configs['Billboard'][chart_type](report, [], {}).toJs())

# Billboard
#
# lineChart = JsLine(None, [], {})
# lineChart.addAttr('pattern', ['yellow'], 'color')
# print(lineChart)
#
#
#
# # C3
# lineChart = JsLine(None, [], {})
# lineChart.addAttr('pattern', ['yellow'], 'color')
# print(lineChart)