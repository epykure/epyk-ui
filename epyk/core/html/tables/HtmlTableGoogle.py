#!/usr/bin/python
# -*- coding: utf-8 -*-


from epyk.core.html import Html
from epyk.core.js import JsUtils


class Table(Html.Html):
  name = 'Google Table'
  requirements = ('google-tables', )

  def __init__(self, report, records, width, height, html_code, options, profile):
    data, columns, self.__config = [], [], None
    super(Table, self).__init__(report, records, html_code=html_code, profile=profile,
                                css_attrs={"width": width, "height": height})
    self.__options = options

  @property
  def tableId(self):
    """
    Description:
    -----------
    Return the Javascript variable of the chart.

    Usage:
    -----
    """
    return "%s_obj" % self.htmlCode

  def add_column(self, c):
    pass

  def build(self, data=None, options=None, profile=None, component_id=None):
    return '''
      %(chartId)s = google.charts.setOnLoadCallback( (function(){
        var data = new google.visualization.DataTable();
        var tableData = %(data)s;
        tableData.rows.forEach(function(c){
          data.addColumn('string', c)});
        tableData.cols.forEach(function(c){
          data.addColumn('number', c)});
        data.addRows(tableData.datasets);

        var chart = new google.visualization.%(type)s(%(varId)s);
        chart.draw(data, {});
        return chart
      }));
      ''' % {'chartId': self.tableId, 'varId': component_id or self.dom.varId,
             'data': JsUtils.jsConvertData(data, None), 'type': self.__options["type"]}

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    return '<div %s></div>' % self.get_attrs(pyClassNames=self.style.get_classes())
