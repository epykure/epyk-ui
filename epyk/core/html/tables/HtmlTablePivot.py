"""
Module in charge of the PivotTable library

https://pivottable.js.org/examples/
"""

import json

from epyk.core.html import Html
from epyk.core.js.objects import JsPivotFncs

# The list of CSS classes
from epyk.core.css.groups import CssGrpClsTable

extensions = {
  'sub-total': {'jsImports': ['pivot-sub-total']},
  'c3': {'jsImports': ['pivot-c3']},
}


class PivotTable(Html.Html):
  __reqJs, __reqCss = ["pivot"], ["pivot"]
  name, category, callFnc = 'Pivot Table', 'Tables', 'pivot'
  _grpCls = CssGrpClsTable.CssStylesPivot

  def __init__(self, report, recordSet, rows, cols, valCol, title, tableOptions, width, height, aggOptions, rendererName,
               htmlCode, dataSrc, helper, profile):
    super(PivotTable, self).__init__(report, [], width=width[0], widthUnit=width[1], height=height[0], heightUnit=height[1],
                                     code=htmlCode, dataSrc=dataSrc, profile=profile)
    # Add the extra HTML components
    self.add_title(title)
    self.add_helper(helper)
    # to add all the columns in the table if nothing defined
    self.aggOptions, self.dsc, self.tableOptions, self.addinOptions = aggOptions, '', dict(tableOptions), []
    self.__pivot = {'cols': [] if cols is None else cols, 'rows': [] if rows is None else rows, 'vals': [] if valCol is None else valCol,
                    'aggregatorName': aggOptions['name'], 'rendererName': rendererName}
    self.__aggFncs = dict(JsPivotFncs.getAggFnc())
    self.data = recordSet
    self.data.attach(self)
    self.css({"overflow": 'auto', 'margin': '0 auto'})
    self.addGlobalFnc("numberWithCommas(x)", 'return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")')
    if not self.tableOptions.get("editable", True):
      self.addinOptions.append("window['options_%s'].showUI = false" % self.htmlId)
      del self.tableOptions["editable"]

    if self.tableOptions.get('sub-total'):
      self._report.jsImports.add('pivot-sub-total')
      self.addinOptions.append("window['options_%s'].dataClass = $.pivotUtilities.SubtotalPivotData" % self.htmlId)
      self.addinOptions.append("window['options_%s'].renderers = $.pivotUtilities.subtotal_renderers" % self.htmlId)
      self.addinOptions.append("window['options_%s'].rendererName = 'Table With Subtotal'" % self.htmlId)
      del tableOptions['sub-total']

    # https://pivottable.js.org/examples/onrefresh.html
    for k, v in self.tableOptions.items():
      if k == 'sorters':
        row = []
        for i, j in v.items():
          if isinstance(j, list):
            row.append("'%s': $.pivotUtilities.sortAs(%s)" % (i, j))
          else:
            row.append("'%s': %s" % (i, j))
        self.addinOptions.append("window['options_%(htmlId)s'].%(opt)s = {%(val)s}" % {'htmlId': self.htmlId, 'opt': k, 'val': ",".join(row)})
      else:
        self.addinOptions.append("window['options_%(htmlId)s'].%(opt)s = %(val)s" % {'htmlId': self.htmlId, 'opt': k, 'val': json.dumps(v)})

  @property
  def jqId(self):
    return "$('#%s div')" % self.htmlId

  def addAggregator(self, aggCls):
    """
    Add on the fly new aggregation logic to the pivot table. This will allow the creation of bespoke aggregation functions.
    Those functions will be structure in the way they can be added to the core framework easily.
    Aggregators should follow some rules and they should defined some mandatory parameters (name, keyAgg, push, value, format).

    Example
      class JsPivotSumAgg(object):
        name = "New Sum Agg"
        keyAgg, key2Agg = 0, None
        push = 'this.keyAgg += parseFloat(record[attributeArray[0]]) * 2'
        value = 'return this.keyAgg'
        format = 'return numberWithCommas(x.toFixed(%(digits)s))'

    Documentation
    https://github.com/nicolaskruchten/pivottable/wiki/Aggregators
    """
    if not ':dsc:' in aggCls.__doc__:
      raise Exception("The new Aggregator class %s must have a doc string with a :dsc: field !" % aggCls.name)

    if aggCls.name in self.__aggFncs:
      raise Exception("Duplicated Name - Aggregator %s cannot be replaced !!!" % aggCls.name)

    self.__aggFncs[aggCls.name] = type(aggCls.__name__, (aggCls, JsPivotFncs.JsPivotAggFnc), {})()
    return self

  def jsGenerate(self, jsData='data', jsDataKey=None, isPyData=False, jsId=None):
    return """%(jqId)s.pivotUI(%(jsData)s, window['options_%(htmlId)s'])""" % {'jqId': self.jqId, 'jsData': self.data.setId(jsData).getJs(), 'htmlId': self.htmlId}

  def onDocumentReady(self):
    jsAggFncs = "{%s}" % ", ".join(["'%s': function(attributeArray) {return function(data, rowKey, colKey) {return %s}}" % (name, aggFncs.toJs(self.aggOptions)) for name, aggFncs in self.__aggFncs.items()])
    profile = self.profile if self.profile is not None else getattr(self._report, 'PROFILE', False)
    preFnc, endFnc = "", ""
    if profile:
      preFnc, endFnc = "var t0 = performance.now()", "console.log('|%s|%s|'+ (performance.now()-t0))" % (self.__class__.__name__, self.htmlId)
    self._report.jsOnLoadFnc.add(""" %(preFnc)s;
      var tpl = $.pivotUtilities.aggregatorTemplates; window['options_%(htmlId)s'] = %(options)s; %(addinOptions)s;
      window['options_%(htmlId)s'].aggregators = %(agg)s;
      window['options_%(htmlId)s'].onRefresh = function (config) {
          %(jqId)s.find('.pvtVal').each(function( index, items ) {
            if (parseFloat(items.innerText.replace(',', '.')) < 0){ $(items).css('color', 'red')}});
          %(jqId)s.find('.pvtTotal').each(function( index, items ) {
            if (parseFloat(items.innerText.replace(',', '.')) < 0){ $(items).css('color', 'red')}});
          %(jqId)s.find('.pvtGrandTotal').each(function( index, items ) {
            if (parseFloat(items.innerText.replace(',', '.')) < 0){ $(items).css('color', 'red')}});
      } """ % {'jqId': self.jqId, 'options': json.dumps(self.__pivot), 'agg': jsAggFncs, 'htmlId': self.htmlId,
               'addinOptions': ";".join(self.addinOptions), "preFnc": preFnc})
    self._report.jsOnLoadFnc.add("%s;%s" % (self.jsGenerate(None), endFnc))

  def onDocumentLoadFnc(self): return True

  def setTableCss(self, cssClss):
    """
    Add a style to the datatable. This can be used to change some specific part of the table (for example the header)

    Example
      class CssTableHeader(object):
        __style = [{'attr': 'background', 'value': 'grey'}]
        childrenTag = 'th'

      tb.setTableCss(CssTableHeader)

    :return: The Python Datatable object
    """
    import inspect

    if not isinstance(cssClss, list):
      cssClss = [cssClss]
    for cssCls in cssClss:
      if inspect.isclass(cssCls):
        self._report.cssObj.addPy(cssCls)
        cssCls = cssCls.__name__
      clssMod = self._report.style.add(cssCls)
      if clssMod is not None:
        self._report.style.cssCls(cssCls)
    return self

  def __str__(self):
    return '<div %(strAttr)s><div></div></div>%(helper)s' % {'strAttr': self.strAttr(pyClassNames=self.defined), "helper": self.helper}


  # -----------------------------------------------------------------------------------------
  #                                    MARKDOWN SECTION
  # -----------------------------------------------------------------------------------------
  @classmethod
  def matchMarkDownBlock(cls, data):
    return True if data[0].strip().startswith("---Pivot") else None

  @staticmethod
  def matchEndBlock(data):
    return data.endswith("---")

  @classmethod
  def convertMarkDownBlock(cls, data, report=None):
    return []

  def jsMarkDown(self): return ""

