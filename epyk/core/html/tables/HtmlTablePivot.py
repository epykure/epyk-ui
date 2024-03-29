#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union

from epyk.core.py import primitives
from epyk.core.html import Html
from epyk.core.html.mixins import MixHtmlState
from epyk.core.html.tables.evts import EvtTablePivot
from epyk.core.js import JsUtils
from epyk.core.html.options import OptTable
from epyk.core.js.packages import JsQuery

# The list of CSS classes
from epyk.core.css.styles import GrpClsTable


class PivotAggregator:

    def __init__(self, page: primitives.PageModel, options: Union[OptTable.OptionsPivot, dict]):
        self.page, self.options = page, options

    def sumOverSum(self, cols: list):
        """
        :param cols: The columns to be added up.
        """
        cols = JsUtils.jsConvertData(cols, None)
        self.options.aggregator = '$.pivotUtilities.aggregators["Sum over Sum"](%s)' % cols
        self.options.aggregatorName = "Sum over Sum"

    def count(self):
        self.options.aggregator = '$.pivotUtilities.aggregators["Count"]()'
        self.options.aggregatorName = "Count"

    def sum(self, col1: str):
        """
        :param col1: The column name.
        """
        col1 = JsUtils.jsConvertData(col1, None)
        self.options.aggregator = '$.pivotUtilities.aggregators["Sum"]([%s])' % col1
        self.options.aggregatorName = "Sum"

    def max(self, col1: str):
        """
        :param col1: The column name.
        """
        self.singleFactorFormulas(col1, "= Math.max(this.tmpVal, col1)", "Max")

    def min(self, col1: str):
        """
        :param col1: The column name.
        """
        self.singleFactorFormulas(col1, "= Math.min(this.tmpVal, col1)", "Min")

    def absSum(self, col1: str):
        """
        :param col1:
        """
        self.singleFactorFormulas(col1, "+= Math.abs(col1)", "sum (abs)")

    def quick(self, col1: str, name: str, formula: str):
        """Add a fix formula without input options.

        Usage::

          tb = page.ui.tables.pivot(languages, ['name'], ['type'])
          tb.aggregators.quick("change", "Abs Change", "+= Math.abs(col1)")

        :param col1: The column name.
        :param name: The function name.
        :param formula: The formula to be applied.
        """
        col1 = JsUtils.jsConvertData(col1, None)
        fnc = '''function(attributeArray) { 
return function(){
  var attribute = attributeArray[0];
  return function(data, rowKey, colKey) {
    return {
      tmpVal: 0, numInputs: 0,
      push: function(record){
        const col1 = record[attribute]; this.tmpVal %s; return this.tmpVal},
      value: function() { return this.tmpVal; },
      format: function(x) { return x; },
  }}}}''' % formula
        self.page.properties.js.add_builders("$.pivotUtilities.aggregators['%(name)s'] = %(fnc)s([%(col)s])" % {
            "name": name, "fnc": fnc, "col": col1})
        self.options.aggregatorName = name  # "diff Abs Agg"
        self.options.aggregator = "$.pivotUtilities.aggregators['%(name)s']()" % {"name": name}

    def singleFactorFormulas(self, col1: str, formula: str, name: str):
        """
        TODO: Find way to set the column name on init

        Usage::

          tb = page.ui.tables.pivot(languages, ['name'], ['type'])
          tb.aggregators.absSum('rating')

        :param col1: The column name.
        :param formula: The formula to be applied.
        :param name: The function name.
        """
        col1 = JsUtils.jsConvertData(col1, None)
        fnc = '''function(attributeArray) { 
var attribute = attributeArray[0];
return function(data, rowKey, colKey) {
  return {
    tmpVal: 0, numInputs: 1,
    push: function(record){
      const col1 = record[attribute]; this.tmpVal %s; return this.tmpVal},
    value: function() { return this.tmpVal; },
    format: function(x) { return x; },
  }}}''' % formula
        self.options.aggregatorName = name  # "diff Abs Agg"
        self.options.aggregator = "$.extend($.pivotUtilities.aggregators, {'%(name)s': function(){return %(fnc)s}() })['%(name)s']([%(col)s])" % {
            "name": name, "fnc": fnc, "col": col1}

    def twoFactorFormulas(self, col1: str, col2: str, name: str, formula: str):
        """Create a two factor function.

        TODO: Find way to set the column name on init

        Usage::

          tb = page.ui.tables.pivot(languages, ['name'], ['type'])
          tb.aggregators.diffAbsolute('change', 'rating')

        :param col1: The column name.
        :param col2: The column name.
        :param name: The function name.
        :param formula: The formula to be applied.
        """
        col1 = JsUtils.jsConvertData(col1, None)
        col2 = JsUtils.jsConvertData(col2, None)
        fnc = '''function(attributeArray) { 
var keyAgg = attributeArray[0]; var key2Agg = attributeArray[1];
return function(data, rowKey, colKey) {
  return {
    tmpVal: 0, numInputs: 2,
    push: function(record){
      const col1 = record[keyAgg]; const col2 = record[key2Agg]; this.tmpVal %s; return this.tmpVal},
    value: function() { return this.tmpVal; },
    format: function(x) { return x; },
  };
}}''' % formula
        self.options.aggregator = "$.extend($.pivotUtilities.aggregators, {'%(name)s': function(){return %(fnc)s}() })['%(name)s']([%(col1)s, %(col2)s])" % {
            "name": name, "fnc": fnc, "col1": col1, "col2": col2}
        self.options.aggregatorName = "diff Abs Agg"

    def diffAbsolute(self, col1: str, col2: str, formula: str = "+= col1 - col2"):
        """
        :param col1: The column name.
        :param col2: The column name.
        :param formula: The formula to be applied.
        """
        self.twoFactorFormulas(col1, col2, "diff Abs Agg", formula)

    def custom(self, name: str, js_def: str):
        """Add a custom aggregator function.

        'Package Doc <'https://github.com/nicolaskruchten/pivottable/wiki/Aggregators>`_

        :param name: The function name.
        :param js_def: The function definition
        """
        self.page.properties.js.add_builders("$.pivotUtilities.aggregators['%(name)s'] = %(fnc)s" % {
            "name": name, "fnc": js_def.strip()})
        self.options.aggregator = "$.pivotUtilities.aggregators['%(name)s']()" % {"name": name}
        self.options.aggregatorName = name


class PivotRendererC3:
    def __init__(self, page: primitives.PageModel, options: dict):
        self.page, self.options = page, options

    def bar(self):
        """Horizontal bar chart from C3.

        `Package Doc <https://pivottable.js.org/examples/c3.html>`_
        """
        self.page.jsImports.add('pivot-c3')
        self.options.renderers = "$.extend($.pivotUtilities.renderers, $.pivotUtilities.c3_renderers)"
        self.options.rendererName = "Bar Chart"

    def scatter(self):
        """Scatter chart from C3.

        `Package Doc <https://pivottable.js.org/examples/c3.html>`_
        """
        self.page.jsImports.add('pivot-c3')
        self.options.renderers = "$.extend($.pivotUtilities.renderers, $.pivotUtilities.c3_renderers)"
        self.options.rendererName = "Area Chart"

    def area(self):
        """Area chart from C3.

        `Package Doc <https://pivottable.js.org/examples/c3.html>`_
        """
        self.page.jsImports.add('pivot-c3')
        self.options.renderers = "$.extend($.pivotUtilities.renderers, $.pivotUtilities.c3_renderers)"
        self.options.rendererName = "Area Chart"

    def line(self):
        """Line chart from C3.

        `Package Doc <https://pivottable.js.org/examples/c3.html>`_
        """
        self.page.jsImports.add('pivot-c3')
        self.options.renderers = "$.extend($.pivotUtilities.renderers, $.pivotUtilities.c3_renderers)"
        self.options.rendererName = "Line Chart"

    def hbar(self):
        """Stacked bar chart from C3.

        `Package Doc <https://pivottable.js.org/examples/c3.html>`_
        """
        self.page.jsImports.add('pivot-c3')
        self.options.renderers = "$.extend($.pivotUtilities.renderers, $.pivotUtilities.c3_renderers)"
        self.options.rendererName = "Horizontal Stacked Bar Chart"

    def stacked(self):
        """Stacked bar chart from C3.

        `Package Doc <https://pivottable.js.org/examples/c3.html>`_
        """
        self.page.jsImports.add('pivot-c3')
        self.options.renderers = "$.extend($.pivotUtilities.renderers, $.pivotUtilities.c3_renderers)"
        self.options.rendererName = "Stacked Bar Chart"


class PivotRendererPlotly:

    def __init__(self, page: primitives.PageModel, options: dict):
        self.page, self.options = page, options

    def pies(self):
        """Multiple Pies charts from Plotly.

        `Package Doc <https://pivottable.js.org/examples/plotly.html>`_
        """
        self.page.jsImports.add('pivot-plotly')
        self.options.renderers = "$.extend($.pivotUtilities.renderers, $.pivotUtilities.plotly_renderers)"
        self.options.rendererName = "Multiple Pie Chart"

    def area(self):
        """Area chart from Plotly.

        `Package Doc <https://pivottable.js.org/examples/c3.html>`_
        """
        self.page.jsImports.add('pivot-plotly')
        self.options.renderers = "$.extend($.pivotUtilities.renderers, $.pivotUtilities.plotly_renderers)"
        self.options.rendererName = "Area Chart"

    def scatter(self):
        """Scatter chart from Plotly.

        `Package Doc <https://pivottable.js.org/examples/c3.html>`_
        """
        self.page.jsImports.add('pivot-plotly')
        self.options.renderers = "$.extend($.pivotUtilities.renderers, $.pivotUtilities.plotly_renderers)"
        self.options.rendererName = "Scatter Chart"

    def line(self):
        """Line chart from Plotly.

        `Package Doc <https://pivottable.js.org/examples/c3.html>`_
        """
        self.page.jsImports.add('pivot-plotly')
        self.options.renderers = "$.extend($.pivotUtilities.renderers, $.pivotUtilities.plotly_renderers)"
        self.options.rendererName = "Line Chart"

    def bar(self):
        """Bar chart from Plotly.

        `Package Doc <https://pivottable.js.org/examples/c3.html>`_
        """
        self.page.jsImports.add('pivot-plotly')
        self.options.renderers = "$.extend($.pivotUtilities.renderers, $.pivotUtilities.plotly_renderers)"
        self.options.rendererName = "Bar Chart"

    def hbar(self):
        """Horizontal Bar chart from Plotly.

        `Package Doc <https://pivottable.js.org/examples/c3.html>`_
        """
        self.page.jsImports.add('pivot-plotly')
        self.options.renderers = "$.extend($.pivotUtilities.renderers, $.pivotUtilities.plotly_renderers)"
        self.options.rendererName = "Horizontal Bar Chart"


class PivotRenderer:

    def __init__(self, page: primitives.PageModel, options: Union[OptTable.OptionsPivot, dict]):
        self.page, self.options = page, options

    def table(self):
        self.options.renderer = '$.pivotUtilities.renderers["table"]'

    @property
    def plotly(self) -> PivotRendererPlotly:
        """Property to use the Plotly special renderers"""
        return PivotRendererPlotly(self.page, self.options)

    @property
    def c3(self) -> PivotRendererC3:
        """Property to use the C3 special renderers"""
        return PivotRendererC3(self.page, self.options)

    def treemap(self):
        """
        `Package Doc <https://pivottable.js.org/examples/plotly.html>`_
        """
        self.page.jsImports.add('pivot-d3')
        self.options.renderers = "$.pivotUtilities.d3_renderers"
        self.options.rendererName = "Treemap"

    def heatmap(self):
        self.options.renderer = '$.pivotUtilities.renderers["Heatmap"]'

    def bars(self):
        self.options.renderer = '$.pivotUtilities.renderers["Table Barchart"]'

    def custom(self, name, js_def):
        """
        `Package Doc <https://github.com/nicolaskruchten/pivottable/wiki/Renderers>`_

        :param name:
        :param js_def:
        """
        pass


class PivotTable(MixHtmlState.HtmlOverlayStates, Html.Html):
    requirements = ('pivottable',)
    name = 'Pivot Table'
    tag = "div"
    _option_cls = OptTable.OptionsPivot

    def __init__(self, page: primitives.PageModel, records, rows, cols, width, height, html_code, helper,
                 options, profile):
        super(PivotTable, self).__init__(page, records, html_code=html_code, profile=profile, options=options,
                                         css_attrs={"width": width, "height": height})
        # Add the extra HTML components
        self.add_helper(helper)
        # to add all the columns in the table if nothing defined
        self.options.cols = cols or []
        self.options.rows = rows or []
        self.style.css.display = 'inline-block'
        self.style.css.position = 'relative'
        self.style.css.overflow = 'auto'
        self.style.css.background_color = "white"

    @property
    def events(self) -> EvtTablePivot.EvtPivot:
        """Common events for tables"""
        return EvtTablePivot.EvtPivot(page=self.page, component=self)

    @property
    def style(self) -> GrpClsTable.Pivot:
        """Property to the CSS Style of the component"""
        if self._styleObj is None:
            self._styleObj = GrpClsTable.Pivot(self)
        return self._styleObj

    @property
    def options(self) -> OptTable.OptionsPivot:
        """Pivot Table options"""
        return super().options

    @property
    def aggregators(self) -> PivotAggregator:
        return PivotAggregator(self.page, self.options)

    @property
    def renderers(self) -> PivotRenderer:
        return PivotRenderer(self.page, self.options)

    _js__builder__ = '''if (options.showUI){%(jqId)s.pivotUI(data, options)} else {%(jqId)s.pivot(data, options)}''' % {
        "jqId": JsQuery.decorate_var("htmlObj", convert_var=False)}

    def sub_total(self):
        self.page.jsImports.add('subtotal')
        self.options.dataClass = "$.pivotUtilities.SubtotalPivotData"
        self.options.renderers = "$.pivotUtilities.subtotal_renderers"
        self.options.rendererName = 'Table With Subtotal'

    def __str__(self):
        self.page.properties.js.add_builders(self.refresh())
        return '<%(tag)s %(strAttr)s></%(tag)s>%(helper)s' % {
            "tag": self.tag, 'strAttr': self.get_attrs(css_class_names=self.style.get_classes()), "helper": self.helper}


class PivotUITable(PivotTable):
    _option_cls = OptTable.OptionsPivotUI

    def __init__(self, page: primitives.PageModel, records, rows, cols, width, height, html_code,
                 helper, options, profile):
        super(PivotUITable, self).__init__(
            page, records or [], rows, cols, width, height, html_code, helper, options, profile)
        # to add all the columns in the table if nothing defined
        self.options.cols = cols or []
        self.options.rows = rows or []

    @property
    def events(self) -> EvtTablePivot.EvtPivot:
        """Common events for tables"""
        return EvtTablePivot.EvtPivot(page=self.page, component=self)

    @property
    def options(self) -> OptTable.OptionsPivotUI:
        """Pivot Table options"""
        return super().options

    _js__builder__ = '''%(jqId)s.pivotUI(data, options)''' % {
        "jqId": JsQuery.decorate_var("htmlObj", convert_var=False)}
