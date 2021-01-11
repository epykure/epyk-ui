#!/usr/bin/python
# -*- coding: utf-8 -*-


from epyk.core.html import Html
from epyk.core.js import JsUtils


class Chart(Html.Html):
  name = 'Google Chart'
  requirements = ('google-charts', )

  def __init__(self,  report, data, width, height, htmlCode, options, profile):
    self.height = height[0]
    super(Chart, self).__init__(report, data, htmlCode=htmlCode, css_attrs={"width": width, "height": height}, profile=profile)
    self._d3, self._chart, self._datasets, self._options, self._data_attrs, self._attrs = None, None, [], None, {}, {}
    self.__options = options
    self.style.css.margin_top = 10

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

  def build(self, data=None, options=None, profile=False):
    """
    Description:
    -----------

    Usage:
    -----

    Attributes:
    ----------
    :param data:
    :param options:
    :param profile:
    """
    return '''
      %(chartId)s = google.charts.setOnLoadCallback( (function(){
        var data = new google.visualization.DataTable();
        var chartData = %(data)s;
        data.addColumn('string', chartData.x);
        chartData.series.forEach(function(col){data.addColumn('number', col)})
        data.addRows(chartData.datasets);
        
        var chart = new google.visualization.%(type)s(%(varId)s);
        chart.draw(data, {});
        return chart
      }));
      ''' % {'chartId': self.chartId, 'varId': self.dom.varId, 'data': JsUtils.jsConvertData(data, None), 'type': self.__options["type"]}

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '<div %s></div>' % self.get_attrs(pyClassNames=self.style.get_classes())


class ChartLine(Chart):
  pass
