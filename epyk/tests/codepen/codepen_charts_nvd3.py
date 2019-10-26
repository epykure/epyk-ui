from epyk.core.Page import Report
from epyk.tests import test_statics


rptObj = Report()


data = test_statics.get_data("flights.txt", n=10)
for rec in data:
  rec["distance"] = float(rec["distance"])
  rec["delay"] = float(rec["delay"])

bar = rptObj.ui.charts.nvd3.area(data, y_columns=["delay"], x_axis="distance")
bar.chart.rightAlignYAxis(False).showControls(False).showLegend(False)
bar.defined.add('CssNVD3Axis')
bar.defined.remove(["CssDivChart", 'CssNVD3HideGrid'])
bar.defined.clear()

# bar.style.defined.chart.container_border().remove()
# bar.chart.width(30)
# bar.chart.xAxis.axisLabel("test").tickFormat(12)

rptObj.outs.browser.codepen(path=test_statics.OUTPUT_PATHS)