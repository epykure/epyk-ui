#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List

from epyk.core.py import primitives
from epyk.core.html import Html
from epyk.core.js import JsUtils


class Table(Html.Html):
    name = 'Google Table'
    tag = "div"
    requirements = ('google-tables',)

    def __init__(self, page: primitives.PageModel, records, width, height, html_code, options, profile):
        data, columns, self.__config = [], [], None
        super(Table, self).__init__(page, records, html_code=html_code, profile=profile,
                                    css_attrs={"width": width, "height": height})
        self.__options = options

    def add_column(self, c):
        raise NotImplementedError("Not yet available")

    def _set_js_code(self, html_code: str, js_code: str):
        """Set a different code for the component.
        This method will ensure both HTML and Js references will be properly changed for this component.
        This method is used by the js_code property and should not be used directly.

        :param html_code: The new HTML code
        :param js_code: The new JavaScript code
        """
        self.dom.varName = "document.getElementById('%s')" % html_code

    def define(self, options: dict, dataflows: List[dict] = None):
        raise NotImplementedError("Not yet available")

    def build(self, data=None, options=None, profile=None, component_id=None, dataflows: List[dict] = None):
        self.js_code = component_id
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
}))''' % {
            'chartId': self.js_code, 'varId': component_id or self.dom.varId,
            'data': JsUtils.dataFlows(data, dataflows, self.page), 'type': self.__options["type"]}

    def __str__(self):
        self.page.properties.js.add_builders(self.refresh())
        return '<%s %s></%s>' % (self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.tag)
