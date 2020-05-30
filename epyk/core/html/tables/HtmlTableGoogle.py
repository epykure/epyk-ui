

from epyk.core.html import Html
from epyk.core.js import JsUtils


class Table(Html.Html):
  name = 'Google Table'
  requirements = ('google-tables', )

  def __init__(self, report, records, width, height, htmlCode, options, profile):
    data, columns, self.__config = [], [], None
    super(Table, self).__init__(report, records, code=htmlCode, css_attrs={"width": width, "height": height}, profile=profile)
    self.__options = options

  @property
  def tableId(self):
    """
    Return the Javascript variable of the chart
    """
    return "%s_obj" % self.htmlId

  def add_column(self, c):
    pass

  def build(self, data=None, options=None, profile=False):
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
      ''' % {'chartId': self.tableId, 'varId': self.dom.varId, 'data': JsUtils.jsConvertData(data, None),
             'type': self.__options["type"]}

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '<div %s></div>' % self.get_attrs(pyClassNames=self.style.get_classes())
