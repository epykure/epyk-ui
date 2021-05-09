#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html
from epyk.core.js import JsUtils


class Frappe(Html.Html):
  requirements = ('frappe-charts', )
  name = 'Frappe Mixed'
  _chart__type = 'axis-mixed'

  def __init__(self,  report, width, height, html_code, options, profile):
    super(Frappe, self).__init__(
      report, [], html_code=html_code, profile=profile, options=options, css_attrs={"width": width, "height": height})
    self._d3, self._chart, self._datasets, self._data_attrs, self._attrs = None, None, [], {}, {}
    self.chartId = "%s_obj" % self.htmlCode

  def build(self, data=None, options=None, profile=None, component_id=None):
    """
    Description:
    ------------
    Update the chart with context and / or data changes.

    Usage::

    Attributes:
    ----------
    :param data: List. Optional. The full datasets object expected by ChartJs.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param component_id: String. Not used.
    """
    if data is not None:
      pass

    return '''
const data = {
    labels: ["12am-3am", "3am-6pm", "6am-9am", "9am-12am",
        "12pm-3pm", "3pm-6pm", "6pm-9pm", "9am-12am"
    ],
    datasets: [
        {
            name: "Some Data", type: "bar",
            values: [25, 40, 30, 35, 8, 52, 17, -4]
        },
        {
            name: "Another Set", type: "line",
            values: [25, 50, -10, 15, 18, 32, 27, 14]
        }
    ]
}; console.log(frappe);
%(chartId)s = new frappe.Chart("#%(hmlCode)s", {  // or a DOM element,
                                            // new Chart() in case of ES6 module with above usage
    title: "My Awesome Chart",
    data: data,
    type: 'donut', // or 'bar', 'line', 'scatter', 'pie', 'percentage'
    height: 250,
    colors: ['#7cd6fd', '#743ee2']
})
    ''' % {"chartId": self.chartId, "chartType": self._chart__type, "hmlCode": component_id or self.htmlCode}

  def __str__(self):
    self.page.properties.js.add_builders(self.build())
    return '<div %s></div>' % self.get_attrs(pyClassNames=self.style.get_classes())


class FrappeLine(Frappe):
  name = 'Frappe Line'
  _chart__type = 'line'


class FrappeBar(Frappe):
  name = 'Frappe Bar'
  _chart__type = 'bar'


class FrappeScatter(Frappe):
  name = 'Frappe Scatter'
  _chart__type = 'scatter'


class FrappePie(Frappe):
  name = 'Frappe Pie'
  _chart__type = 'pie'


class FrappeDonut(Frappe):
  name = 'Frappe Donut'
  _chart__type = 'donut'


class FrappePercentage(Frappe):
  name = 'Frappe Percentage'
  _chart__type = 'percentage'


class FrappeHeatmap(Frappe):
  name = 'Frappe Heatmap'
  _chart__type = 'heatmap'
