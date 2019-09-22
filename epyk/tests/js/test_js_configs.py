
from epyk.core.js.configs import JsConfig
from epyk.core import Page


report = Page.Report()

chart_type = 'hbar'
configs = JsConfig.get(chart_type, chartFam='Billboard', preferred=False)
config_chart = configs['Billboard'][chart_type](report, [], {})
config_chart.addAttr("test", 'function(){alert}', isPyData=False)

print(config_chart.toJs())

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