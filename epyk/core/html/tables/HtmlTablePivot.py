#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Module in charge of the PivotTable library

Related Pages:

		https://pivottable.js.org/examples/
"""

from epyk.core.html import Html
from epyk.core.js import JsUtils
from epyk.core.html.options import OptTable
from epyk.core.js.packages import JsQuery

# The list of CSS classes
from epyk.core.css.styles import GrpClsTable


class PivotTable(Html.Html):

  requirements = ('pivottable', )
  name = 'Pivot Table'
  _option_cls = OptTable.OptionsPivot

  def __init__(self, report, records, rows, cols, width, height, html_code, helper, options, profile):
    super(PivotTable, self).__init__(report, records, html_code=html_code, profile=profile,
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
  def style(self):
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
  def options(self):
    """
    Description:
    ------------
    Pivot Table options.

    Usage::

    :rtype: OptTable.OptionsPivot
    """
    return super().options

  @property
  def aggregators(self):
    """
    Description:
    ------------

    """
    return PivotAggregator(self._report, self.options)

  @property
  def renderers(self):
    """
    Description:
    ------------

    """
    return PivotRenderer(self._report, self.options)

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
    self._report.jsImports.add('subtotal')
    self.options.dataClass = "$.pivotUtilities.SubtotalPivotData"
    self.options.renderers = "$.pivotUtilities.subtotal_renderers"
    self.options.rendererName = 'Table With Subtotal'

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    return '<div %(strAttr)s></div>%(helper)s' % {
      'strAttr': self.get_attrs(pyClassNames=self.style.get_classes()), "helper": self.helper}


class PivotUITable(PivotTable):
  _option_cls = OptTable.OptionsPivotUI

  def __init__(self, report, records, rows, cols, width, height, html_code, helper, options, profile):
    super(PivotUITable, self).__init__(report, records or [], rows, cols, width, height, html_code, helper, options,
                                       profile)
    # to add all the columns in the table if nothing defined
    self.options.cols = cols or []
    self.options.rows = rows or []

  @property
  def options(self):
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


class PivotAggregator:

  def __init__(self, report, options):
    self.report, self.options = report, options

  def sumOverSum(self, cola):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param cola:
    """
    cola = JsUtils.jsConvertData(cola, None)
    self.options.aggregator = '$.pivotUtilities.aggregators["Sum over Sum"](%s)' % cola
    self.options.aggregatorName = "sumOverSum"

  def count(self):
    """
    Description:
    ------------

    Usage::
    """
    self.options.aggregator = '$.pivotUtilities.aggregators["Count"]()'
    self.options.aggregatorName = "count"

  def sum(self, col1):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    """
    col1 = JsUtils.jsConvertData(col1, None)
    self.options.aggregator = '$.pivotUtilities.aggregators["Sum"]([%s])' % col1
    self.options.aggregatorName = "sum"

  def max(self, col1):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    """
    self.singleFactorFormulas(col1, "= Math.max(this.tmpVal, col1)")
    self.options.aggregatorName = "Max"

  def min(self, col1):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param col1:
    """
    self.singleFactorFormulas(col1, "= Math.min(this.tmpVal, col1)")
    self.options.aggregatorName = "Min"

  def absSum(self, col1):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param col1:
    """
    self.singleFactorFormulas(col1, "+= Math.abs(col1)")
    self.options.aggregatorName = "sum (abs)"

  def singleFactorFormulas(self, col1, formula):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param col1:
    :param formula:
    """
    col1 = JsUtils.jsConvertData(col1, None)
    self.options.aggregator = '''
      function(keyAgg) { 
        return function(data, rowKey, colKey) {
          return {
            tmpVal: 0, numInputs: 1,
            push: function(record){
              const col1 = record[keyAgg]; this.tmpVal %s; return this.tmpVal},
            value: function() { return this.tmpVal; },
            format: function(x) { return x; },
          }}}(%s)''' % (formula, col1)
    self.options.aggregatorName = "diff Abs Agg"

  def twoFactorFormulas(self, col1, col2, formula):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param col1:
    :param col2:
    :param formula:
    """
    col1 = JsUtils.jsConvertData(col1, None)
    col2 = JsUtils.jsConvertData(col2, None)
    self.options.aggregator = '''
      function(keyAgg, key2Agg) { 
        return function(data, rowKey, colKey) {
          return {
            tmpVal: 0, numInputs: 2,
            push: function(record){
              const col1 = record[keyAgg]; const col2 = record[key2Agg]; this.tmpVal %s; return this.tmpVal},
            value: function() { return this.tmpVal; },
            format: function(x) { return x; },
          };
        };
      }(%s, %s)''' % (formula, col1, col2)
    self.options.aggregatorName = "diff Abs Agg"

  def diffAbsolute(self, col1, col2, formula="+= col1 - col2"):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param col1:
    :param col2:
    :param formula:
    """
    self.twoFactorFormulas(col1, col2, formula)
    self.options.aggregatorName = "diff Abs Agg"

  def custom(self, name, js_def):
    """
    Description:
    ------------

    Usage::

    https://github.com/nicolaskruchten/pivottable/wiki/Aggregators

    Attributes:
    ----------
    :param name:
    :param js_def:
    """
    self.options.aggregator = js_def
    self.options.aggregatorName = name


class PivotRendererC3:
  def __init__(self, report, options):
    self._report, self.options = report, options

  def bar(self):
    """
    Description:
    ------------
    Horizontal bar chart from C3.

    Usage::

    Related Pages:

      https://pivottable.js.org/examples/c3.html

    """
    self._report.jsImports.add('pivot-c3')
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
    self._report.jsImports.add('pivot-c3')
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
    self._report.jsImports.add('pivot-c3')
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
    self._report.jsImports.add('pivot-c3')
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
    self._report.jsImports.add('pivot-c3')
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
    self._report.jsImports.add('pivot-c3')
    self.options.renderers = "$.extend($.pivotUtilities.renderers, $.pivotUtilities.c3_renderers)"
    self.options.rendererName = "Stacked Bar Chart"


class PivotRendererPlotly:

  def __init__(self, report, options):
    self._report, self.options = report, options

  def pies(self):
    """
    Description:
    ------------
    Multiple Pies charts from Plotly.

    Usage::

    Related Pages:

      https://pivottable.js.org/examples/plotly.html
    """
    self._report.jsImports.add('pivot-plotly')
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
    self._report.jsImports.add('pivot-plotly')
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
    self._report.jsImports.add('pivot-plotly')
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
    self._report.jsImports.add('pivot-plotly')
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
    self._report.jsImports.add('pivot-plotly')
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
    self._report.jsImports.add('pivot-plotly')
    self.options.renderers = "$.extend($.pivotUtilities.renderers, $.pivotUtilities.plotly_renderers)"
    self.options.rendererName = "Horizontal Bar Chart"


class PivotRenderer:

  def __init__(self, report, options):
    self._report, self.options = report, options

  def table(self):
    """
    Description:
    ------------

    """
    self.options.renderer = '$.pivotUtilities.renderers["table"]'

  @property
  def plotly(self):
    """
    Description:
    ------------
    Property to use the Plotly special renderers.

    Usage::

    """
    return PivotRendererPlotly(self._report, self.options)

  @property
  def c3(self):
    """
    Description:
    ------------
    Property to use the C3 special renderers.

    Usage::
    """
    return PivotRendererC3(self._report, self.options)

  def treemap(self):
    """
    Description:
    ------------

    Usage::

    https://pivottable.js.org/examples/plotly.html

    """
    self._report.jsImports.add('pivot-d3')
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
