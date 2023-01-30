#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html
from epyk.core.js.packages import JsD3
from epyk.core.html.options import OptChartRoughViz


class RoughViz(Html.Html):
  requirements = ('rough-viz', )
  name = 'rough_viz'
  _chart__type = 'Line'
  _option_cls = OptChartRoughViz.RoughVizLine

  def __init__(self,  page, width, height, html_code, options, profile):
    super(RoughViz, self).__init__(
      page, [], html_code=html_code, profile=profile, options=options, css_attrs={"width": width, "height": height})
    self._d3, self._chart, self._datasets, self._data_attrs, self._attrs = None, None, [], {}, {}
    self.chartId = "%s_obj" % self.htmlCode
    self.options.element = "#%s" % self.htmlCode

  @property
  def shared(self) -> OptChartRoughViz.OptionsChartSharedRoughViz:
    """   All the common properties shared between all the charts.
    This will ensure a compatibility with the plot method.

    Usage::

      b = page.ui.charts.roughviz.plot(languages, y=["rating", 'change'], x='name', width=300)
      b.shared.x_label("Test X")
      b.shared.y_label("Test Y")
    """
    return OptChartRoughViz.OptionsChartSharedRoughViz(self)

  @property
  def options(self) -> OptChartRoughViz.RoughVizLine:
    """   Chart specific options.
    """
    return super().options

  @property
  def datasets(self):
    """   

    """
    return self._datasets

  @property
  def d3(self) -> JsD3.D3Select:
    """   Property to the D3 library.
    """
    if self._d3 is None:
      self._d3 = JsD3.D3Select(page=self.page, component=self, selector="d3.select('#%s')" % self.htmlCode, setVar=False)
    return self._d3

  def add_dataset(self, data, label="", colors=None, opacity=None, kind=None):
    """
    Add a new Dataset to the chart list of Datasets.

    Usage::

    Related Pages:

      https://www.chartjs.org/docs/latest/developers/updates.html
 
    :param data: List. The list of points (float).
    :param label: List. Optional. The list of points (float).
    :param colors: List. Optional. The color for this series. Default the global definition.
    :param opacity: Float. Optional. The opacity level for the content.
    """
    dataset = self.options.data.add(label, data)
    return dataset

  def build(self, data=None, options=None, profile=None, component_id=None):
    """
    Update the chart with context and / or data changes.
 
    :param data: List. Optional. The full datasets object expected by ChartJs.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param component_id: String. Not used.
    """
    if data is not None:
      options = options or {}
      options["data"] = data
      return '''
        %(chartId)s.data = {"values": [80, 10], "labels": ["www", "test"]}
        ''' % {"chartId": self.chartId}
      #return '''
      #      %(chartId)s = new roughViz.%(chartType)s(%(config)s);
      #    ''' % {"chartId": self.chartId, "chartType": self._chart__type, "hmlCode": component_id or self.htmlCode,
      #           'config': self.options.config_js(options)}

    return '''%(chartId)s = new roughViz.%(chartType)s(%(config)s)''' % {"chartId": self.chartId, "chartType": self._chart__type, "hmlCode": component_id or self.htmlCode,
           'config': self.options.config_js(options)}

  def __str__(self):
    self.page.properties.js.add_builders(self.build())
    return '<div %s></div>' % self.get_attrs(css_class_names=self.style.get_classes())


class RoughVizBar(RoughViz):
  _chart__type = 'Bar'
  _option_cls = OptChartRoughViz.RoughVizBar


class RoughVizPie(RoughViz):
  _chart__type = 'Pie'
  _option_cls = OptChartRoughViz.RoughVizPie


class RoughVizDonut(RoughViz):
  _chart__type = 'Donut'
  _option_cls = OptChartRoughViz.RoughVizPie


class RoughVizBarH(RoughViz):
  _chart__type = 'BarH'
  _option_cls = OptChartRoughViz.RoughVizBar


class RoughVizScatter(RoughViz):
  _chart__type = 'Scatter'
  _option_cls = OptChartRoughViz.RoughVizScatter
