#!/usr/bin/python
# -*- coding: utf-8 -*-


from epyk.core.html import Html
from epyk.core.js import JsUtils
from epyk.core.html.options import OptChartGoogle


class Chart(Html.Html):
  name = 'Google Chart'
  requirements = ('google-charts', )
  _option_cls = OptChartGoogle.OptionGoogle

  def __init__(self,  report, data, width, height, html_code, options, profile):
    self.height = height[0]
    super(Chart, self).__init__(report, data, html_code=html_code, profile=profile, options=options,
                                css_attrs={"width": width, "height": height})
    self._d3, self._chart, self._datasets, self._options, self._data_attrs, self._attrs = None, None, [], None, {}, {}
    self.style.css.margin_top = 10

  @property
  def shared(self):
    """
    Description:
    -----------
    All the common properties shared between all the charts.
    This will ensure a compatibility with the plot method.

    Usage:
    -----

      line = page.ui.charts.bb.bar()
      line.shared.x_label("x axis")
    """
    return OptChartGoogle.OptionsChartSharedGoogle(self)

  @property
  def options(self):
    """
    Description:
    -----------
    Property to the series options.

    Usage:
    -----

    :rtype: OptChartGoogle.OptionGoogle
    """
    return super().options

  @property
  def chartId(self):
    """
    Description:
    -----------
    Return the Javascript variable of the chart.

    Usage:
    -----
    """
    return "%s_obj" % self.htmlCode

  def build(self, data=None, options=None, profile=None, component_id=None):
    """
    Description:
    -----------

    Usage:
    -----

    Attributes:
    ----------
    :param data:
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param component_id: String. Optional. A DOM component reference in the page.
    """
    return '''
      %(chartId)s = google.charts.setOnLoadCallback( (function(){
        var data = new google.visualization.DataTable();
        var chartOptions = %(options)s; 
        delete chartOptions.type;
        
        var chartData = %(data)s;
        data.addColumn('string', chartData.x);
        chartData.series.forEach(function(col){data.addColumn('number', col)})
        data.addRows(chartData.datasets);
        var chart = new google.visualization.%(type)s(%(varId)s);
        chart.draw(data, chartOptions);
        return chart
      }));
      ''' % {'chartId': self.chartId, 'varId': component_id or self.dom.varId,
             'options': self.options.config_js(options),
             'data': JsUtils.jsConvertData(data, None), 'type': self.options.type}

  def colors(self, colors):
    pass

  def labels(self, values):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param values:
    """
    self._vals = {"x": [], "datasets": [], "series": []}
    for v in values:
      self._vals["datasets"].append([str(v)])

  def add_dataset(self, data, label, colors=None, opacity=None, kind=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param data:
    :param label:
    :param colors:
    :param opacity:
    :param kind:
    """
    self._vals["x"].append(label)
    self._vals["series"].append(label)
    for i, val in enumerate(data):
      self._vals["datasets"][i].append(val)

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    return '<div %s></div>' % self.get_attrs(pyClassNames=self.style.get_classes())


class ChartLine(Chart):
  pass
