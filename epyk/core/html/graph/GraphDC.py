"""

"""

from epyk.core.html import Html

from epyk.core.html.graph import GraphFabric
from epyk.core.js.objects import JsChartDC


class Chart(Html.Html):
  name, category, callFnc = 'DC', 'Charts', 'dc'
  __reqCss, __reqJs = ['dc'], ['dc', 'crossfilter']
  __pyStyle = ['CssDivChart']

  def __init__(self,  report, chart_obj, width, height, title, options, htmlCode, filters, profile):
    self.seriesProperties, self.__chartJsEvents, self.height = {'static': {}, 'dynamic': {}}, {}, height[0]
    super(Chart, self).__init__(report, [], code=htmlCode, width=width[0], widthUnit=width[1], height=height[0],
                                heightUnit=height[1], profile=profile)
    self.chart = chart_obj # GraphFabric.CHARTS_FACTORY[self.name][chartType](report, data, self.seriesProperties)
    resolvedOptions = {}
    self.chart.rAttr(options, resolvedOptions)
    self.chart.update(resolvedOptions)
    #self.chart.data.attach(self)

  @property
  def js(self):
    """
    :rtype: JsChartDC.JsBase
    """
    if self._js is None:
      self._js = self.chart
    return self._js

  # -----------------------------------------------------------------------------------------
  #                                STANDARD HTML METHODS
  # -----------------------------------------------------------------------------------------
  def onDocumentLoadVar(self): pass  # Data should be registered externally
  def onDocumentLoadFnc(self): return True

  def onDocumentReady(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.jsGenerate(jsData=None))

  def jsDataSrc(self, jsData='data', jsDataKey=None, isPyData=False, jsParse=None, jsFnc=None):
    jsData = self._jsData(jsData, jsDataKey, jsParse, isPyData, jsFnc)
    return '%(dataId)s = %(jsData)s' % {"dataId": self.chart.data._jqId, 'jsData': jsData}

  def jsGenerate(self, jsData='data', jsDataKey=None, isPyData=False, jsId=None):
    return '''
      var data = crossfilter(%(data)s);
      var runDimension = data.dimension(function(d) {return d.name});
      var speedSumGroup = runDimension.group().reduceSum(function(d) {return d.count});
      
      window['%(htmlId)s_chart'] = dc.%(jsCls)s('#%(htmlId)s')
        .x(d3.scaleBand()).xUnits(dc.units.ordinal)
        .keyAccessor(function (p) { return p.key;
        })
        .valueAccessor(function (p) { return p.value;
        })
        .radiusValueAccessor(function (p) { return 1 })
        .dimension(runDimension).group(speedSumGroup);
      window['%(htmlId)s_chart'].render();
      ''' % {'htmlId': self.htmlId, 'jsCls': self.chart.jsCls, 'data': self.chart.data}

  def __str__(self):
    strChart = '<div id="%s" style="height:%spx;width:100%%"></div>' % (self.htmlId, self.height-30)
    return GraphFabric.Chart.html(self, self.strAttr(withId=False, pyClassNames=self.pyStyle), strChart)
