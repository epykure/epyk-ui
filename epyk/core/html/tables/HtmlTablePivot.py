#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.py import primitives
from epyk.core.html import Html
from epyk.core.js import JsUtils
from epyk.core.html.options import OptTable
from epyk.core.js.packages import JsQuery

# The list of CSS classes
from epyk.core.css.styles import GrpClsTable


class PivotAggregator:

  def __init__(self, page: primitives.PageModel, options: dict):
    self.page, self.options = page, options

  def sumOverSum(self, cols: list):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param cols: List. The columns to be added up.
    """
    cols = JsUtils.jsConvertData(cols, None)
    self.options.aggregator = '$.pivotUtilities.aggregators["Sum over Sum"](%s)' % cols
    self.options.aggregatorName = "Sum over Sum"

  def count(self):
    """
    Description:
    ------------

    Usage::
    """
    self.options.aggregator = '$.pivotUtilities.aggregators["Count"]()'
    self.options.aggregatorName = "Count"

  def sum(self, col1):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param col1: String. The column name.
    """
    col1 = JsUtils.jsConvertData(col1, None)
    self.options.aggregator = '$.pivotUtilities.aggregators["Sum"]([%s])' % col1
    self.options.aggregatorName = "Sum"

  def max(self, col1):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param col1: String. The column name.
    """
    self.singleFactorFormulas(col1, "= Math.max(this.tmpVal, col1)", "Max")

  def min(self, col1):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param col1: String. The column name.
    """
    self.singleFactorFormulas(col1, "= Math.min(this.tmpVal, col1)", "Min")

  def absSum(self, col1):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param col1:
    """
    self.singleFactorFormulas(col1, "+= Math.abs(col1)", "sum (abs)")

  def quick(self, col1, name, formula):
    """
    Description:
    ------------
    Add a fix formula without input options.

    Usage::

      tb = page.ui.tables.pivot(languages, ['name'], ['type'])
      tb.aggregators.quick("change", "Abs Change", "+= Math.abs(col1)")

    Attributes:
    ----------
    :param col1: String. The column name.
    :param name: String. The function name.
    :param formula: String. The formula to be applied.
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

  def singleFactorFormulas(self, col1, formula, name):
    """
    Description:
    ------------

    TODO: Find way to set the column name on init

    Usage::

      tb = page.ui.tables.pivot(languages, ['name'], ['type'])
      tb.aggregators.absSum('rating')

    Attributes:
    ----------
    :param col1: String. The column name.
    :param formula: String. The formula to be applied.
    :param name: String. The function name.
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
    self.options.aggregatorName = name # "diff Abs Agg"
    self.options.aggregator = "$.extend($.pivotUtilities.aggregators, {'%(name)s': function(){return %(fnc)s}() })['%(name)s']([%(col)s])" % {"name": name, "fnc": fnc, "col": col1}

  def twoFactorFormulas(self, col1, col2, name, formula):
    """
    Description:
    ------------
    Create a two factor function.

    TODO: Find way to set the column name on init

    Usage::

      tb = page.ui.tables.pivot(languages, ['name'], ['type'])
      tb.aggregators.diffAbsolute('change', 'rating')

    Attributes:
    ----------
    :param col1: String. The column name.
    :param col2: String. The column name.
    :param name: String. The function name.
    :param formula: String. The formula to be applied.
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
    self.options.aggregator = "$.extend($.pivotUtilities.aggregators, {'%(name)s': function(){return %(fnc)s}() })['%(name)s']([%(col1)s, %(col2)s])" % {"name": name, "fnc": fnc, "col1": col1, "col2": col2}
    self.options.aggregatorName = "diff Abs Agg"

  def diffAbsolute(self, col1, col2, formula="+= col1 - col2"):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param col1: String. The column name.
    :param col2: String. The column name.
    :param formula: String. The formula to be applied.
    """
    self.twoFactorFormulas(col1, col2, "diff Abs Agg", formula)

  def custom(self, name, js_def):
    """
    Description:
    ------------
    Add a custom aggregator function.

    Usage::

    Related Pages:

      https://github.com/nicolaskruchten/pivottable/wiki/Aggregators

    Attributes:
    ----------
    :param name: String. The function name.
    :param js_def: String. The function definition
    """
    self.page.properties.js.add_builders("$.pivotUtilities.aggregators['%(name)s'] = %(fnc)s" % {
      "name": name, "fnc": js_def.strip()})
    self.options.aggregator = "$.pivotUtilities.aggregators['%(name)s']()" % {"name": name}
    self.options.aggregatorName = name


class PivotRendererC3:
  def __init__(self, page: primitives.PageModel, options: dict):
    self.page, self.options = page, options

  def bar(self):
    """
    Description:
    ------------
    Horizontal bar chart from C3.

    Usage::

    Related Pages:

      https://pivottable.js.org/examples/c3.html

    """
    self.page.jsImports.add('pivot-c3')
    self.options.renderers = "$.extend($.pivotUtilities.renderers, $.pivotUtilities.c3_renderers)"
    self.options.rendererName = "Bar Chart"

  def scatter(self):
    """
    Description:
    ------------
    Scatter chart from C3.

    Usage::

    Related Pages:

      https://pivottable.js.org/examples/c3.html
    """
    self.page.jsImports.add('pivot-c3')
    self.options.renderers = "$.extend($.pivotUtilities.renderers, $.pivotUtilities.c3_renderers)"
    self.options.rendererName = "Area Chart"

  def area(self):
    """
    Description:
    ------------
    Area chart from C3.

    Usage::

    Related Pages:

      https://pivottable.js.org/examples/c3.html
    """
    self.page.jsImports.add('pivot-c3')
    self.options.renderers = "$.extend($.pivotUtilities.renderers, $.pivotUtilities.c3_renderers)"
    self.options.rendererName = "Area Chart"

  def line(self):
    """
    Description:
    ------------
    Line chart from C3.

    Usage::

    Related Pages:

      https://pivottable.js.org/examples/c3.html
    """
    self.page.jsImports.add('pivot-c3')
    self.options.renderers = "$.extend($.pivotUtilities.renderers, $.pivotUtilities.c3_renderers)"
    self.options.rendererName = "Line Chart"

  def hbar(self):
    """
    Description:
    ------------
    Stacked bar chart from C3.

    Usage::

    Related Pages:

      https://pivottable.js.org/examples/c3.html
    """
    self.page.jsImports.add('pivot-c3')
    self.options.renderers = "$.extend($.pivotUtilities.renderers, $.pivotUtilities.c3_renderers)"
    self.options.rendererName = "Horizontal Stacked Bar Chart"

  def stacked(self):
    """
    Description:
    ------------
    Stacked bar chart from C3.

    Usage::

    Related Pages:

      https://pivottable.js.org/examples/c3.html
    """
    self.page.jsImports.add('pivot-c3')
    self.options.renderers = "$.extend($.pivotUtilities.renderers, $.pivotUtilities.c3_renderers)"
    self.options.rendererName = "Stacked Bar Chart"


class PivotRendererPlotly:

  def __init__(self, page: primitives.PageModel, options: dict):
    self.page, self.options = page, options

  def pies(self):
    """
    Description:
    ------------
    Multiple Pies charts from Plotly.

    Usage::

    Related Pages:

      https://pivottable.js.org/examples/plotly.html
    """
    self.page.jsImports.add('pivot-plotly')
    self.options.renderers = "$.extend($.pivotUtilities.renderers, $.pivotUtilities.plotly_renderers)"
    self.options.rendererName = "Multiple Pie Chart"

  def area(self):
    """
    Description:
    ------------
    Area chart from Plotly.

    Usage::

    Related Pages:

      https://pivottable.js.org/examples/c3.html
    """
    self.page.jsImports.add('pivot-plotly')
    self.options.renderers = "$.extend($.pivotUtilities.renderers, $.pivotUtilities.plotly_renderers)"
    self.options.rendererName = "Area Chart"

  def scatter(self):
    """
    Description:
    ------------
    Scatter chart from Plotly.

    Usage::

    Related Pages:

      https://pivottable.js.org/examples/c3.html
    """
    self.page.jsImports.add('pivot-plotly')
    self.options.renderers = "$.extend($.pivotUtilities.renderers, $.pivotUtilities.plotly_renderers)"
    self.options.rendererName = "Scatter Chart"

  def line(self):
    """
    Description:
    ------------
    Line chart from Plotly.

    Usage::

    Related Pages:

      https://pivottable.js.org/examples/c3.html
    """
    self.page.jsImports.add('pivot-plotly')
    self.options.renderers = "$.extend($.pivotUtilities.renderers, $.pivotUtilities.plotly_renderers)"
    self.options.rendererName = "Line Chart"

  def bar(self):
    """
    Description:
    ------------
    Bar chart from Plotly.

    Usage::

    Related Pages:

      https://pivottable.js.org/examples/c3.html
    """
    self.page.jsImports.add('pivot-plotly')
    self.options.renderers = "$.extend($.pivotUtilities.renderers, $.pivotUtilities.plotly_renderers)"
    self.options.rendererName = "Bar Chart"

  def hbar(self):
    """
    Description:
    ------------
    Horizontal Bar chart from Plotly.

    Usage::

    Related Pages:

      https://pivottable.js.org/examples/c3.html
    """
    self.page.jsImports.add('pivot-plotly')
    self.options.renderers = "$.extend($.pivotUtilities.renderers, $.pivotUtilities.plotly_renderers)"
    self.options.rendererName = "Horizontal Bar Chart"


class PivotRenderer:

  def __init__(self, page: primitives.PageModel, options: dict):
    self.page, self.options = page, options

  def table(self):
    """
    Description:
    ------------

    """
    self.options.renderer = '$.pivotUtilities.renderers["table"]'

  @property
  def plotly(self) -> PivotRendererPlotly:
    """
    Description:
    ------------
    Property to use the Plotly special renderers.

    Usage::

    """
    return PivotRendererPlotly(self.page, self.options)

  @property
  def c3(self) -> PivotRendererC3:
    """
    Description:
    ------------
    Property to use the C3 special renderers.

    Usage::
    """
    return PivotRendererC3(self.page, self.options)

  def treemap(self):
    """
    Description:
    ------------

    Usage::

    https://pivottable.js.org/examples/plotly.html

    """
    self.page.jsImports.add('pivot-d3')
    self.options.renderers = "$.pivotUtilities.d3_renderers"
    self.options.rendererName = "Treemap"

  def heatmap(self):
    """
    Description:
    ------------

    Usage::
    """
    self.options.renderer = '$.pivotUtilities.renderers["Heatmap"]'

  def bars(self):
    """
    Description:
    ------------

    Usage::

    """
    self.options.renderer = '$.pivotUtilities.renderers["Table Barchart"]'

  def custom(self, name, js_def):
    """
    Description:
    ------------

    Usage::

    https://github.com/nicolaskruchten/pivottable/wiki/Renderers

    Attributes:
    ----------
    :param name:
    :param js_def:
    """
    pass


class PivotTable(Html.Html):

  requirements = ('pivottable', )
  name = 'Pivot Table'
  _option_cls = OptTable.OptionsPivot

  def __init__(self, page: primitives.PageModel, records, rows, cols, width, height, html_code, helper,
               options, profile):
    super(PivotTable, self).__init__(page, records, html_code=html_code, profile=profile,
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
  def style(self) -> GrpClsTable.Pivot:
    """
    Description:
    ------------
    Property to the CSS Style of the component.

    Usage::

    :rtype: GrpClsTable.Pivot
    """
    if self._styleObj is None:
      self._styleObj = GrpClsTable.Pivot(self)
    return self._styleObj

  @property
  def options(self) -> OptTable.OptionsPivot:
    """
    Description:
    ------------
    Pivot Table options.

    Usage::

    :rtype: OptTable.OptionsPivot
    """
    return super().options

  @property
  def aggregators(self) -> PivotAggregator:
    """
    Description:
    ------------

    """
    return PivotAggregator(self.page, self.options)

  @property
  def renderers(self) -> PivotRenderer:
    """
    Description:
    ------------

    """
    return PivotRenderer(self.page, self.options)

  _js__builder__ = '''
      if (options.showUI){%(jqId)s.pivotUI(data, options)}
      else {%(jqId)s.pivot(data, options)}
      ''' % {"jqId": JsQuery.decorate_var("htmlObj", convert_var=False)}

  def sub_total(self):
    """
    Description:
    -----------

    Usage::
    """
    self.page.jsImports.add('subtotal')
    self.options.dataClass = "$.pivotUtilities.SubtotalPivotData"
    self.options.renderers = "$.pivotUtilities.subtotal_renderers"
    self.options.rendererName = 'Table With Subtotal'

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    return '<div %(strAttr)s></div>%(helper)s' % {
      'strAttr': self.get_attrs(css_class_names=self.style.get_classes()), "helper": self.helper}


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
  def options(self) -> OptTable.OptionsPivotUI:
    """
    Description:
    ------------
    Pivot Table options.

    Usage::

    :rtype: OptTable.OptionsPivotUI
    """
    return super().options

  _js__builder__ = '''
      %(jqId)s.pivotUI(data, options)
      ''' % {"jqId": JsQuery.decorate_var("htmlObj", convert_var=False)}
