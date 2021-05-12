#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html


class MuzeJs(Html.Html):
  requirements = ('@chartshq/muze', )
  name = 'Frappe Mixed'
  _chart__type = 'axis-mixed'

  def __init__(self,  report, width, height, html_code, options, profile):
    super(MuzeJs, self).__init__(
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
  async function test(){
    const muze = window.muze;
    const DataModel = muze.DataModel;
    const env = await muze();
    const dm = new DataModel([["A", 33435]], [
        {
            name: 'Year',
            type: 'dimension',
        },
        {
            name: 'Displacement',
            type: 'measure'
        }
    ]);
    env.canvas()
      .data([{'Displacement': 223, 'Year': 2021}])
      .layers([
          { mark: 'point' },
          { mark: 'line' }
        ])
      .rows(['Displacement'])
      .columns(['Year'])
      .mount('#%(chartId)s');
  }; test()''' % {"chartId": self.chartId, "chartType": self._chart__type, "hmlCode": component_id or self.htmlCode}

  def __str__(self):
    self.page.properties.js.add_builders(self.build())
    return '<div %s></div>' % self.get_attrs(pyClassNames=self.style.get_classes())


class MuzeJsLine(MuzeJs):
  name = 'Frappe Line'
  _chart__type = 'line'


class MuzeJsBar(MuzeJs):
  name = 'Frappe Bar'
  _chart__type = 'bar'


class MuzeJsScatter(MuzeJs):
  name = 'Frappe Scatter'
  _chart__type = 'scatter'


class MuzeJsPie(MuzeJs):
  name = 'Frappe Pie'
  _chart__type = 'pie'


class MuzeJsDonut(MuzeJs):
  name = 'Frappe Donut'
  _chart__type = 'donut'


class FMuzeJsHeatmap(MuzeJs):
  name = 'Frappe Heatmap'
  _chart__type = 'heatmap'
