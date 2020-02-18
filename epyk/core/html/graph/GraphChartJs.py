"""

"""

import time
import json
import os
import re

from epyk.core.js.Imports import requires
from epyk.core.html import Html
# from epyk.core.html.graph import AxisDisplay
from epyk.core.html.graph import GraphFabric
from epyk.core.js.packages import JsChartJs

# The list of CSS classes
# from epyk.core.css.styles import CssGrpClsCharts


# Define a set of common standard properties cross charting libraries.
# The below mapping will ensure the correct definition is applied
CHART_ATTRS = {
  # Chart layout
  'bottom': {"key": "bottom", "tree": ['layout', 'padding'], "category": "options"},
  'top': {"key": "top", "tree": ['layout', 'padding'], "category": "options"},

  # Legend
  'legendPosition': {"key": "position", "tree": ['legend'], "category": "options"},
  'legendFontColor': {"key": "fontColor", "tree": ['legend', 'labels'], "category": "options"},

  # Title
  'title': {"key": "text", "tree": ['title'], "category": "options"},
  'titleDisplay': {"key": "display", "tree": ['title'], "category": "options"},
  'titleFontColor': {"key": "fontColor", "tree": ['title'], "category": "options"},

  # Axes
  'grid': [
    {"key": "drawOnChartArea", "tree": ['scales', 'xAxes', 'gridLines'], "category": "options"},
    {"key": "drawOnChartArea", "tree": ['scales', 'yAxes', 'gridLines'], "category": "options"},
  ],
  'xLabel': {"key": "labelString", "tree": ['scales', "xAxes", 'scaleLabel'], "category": "options"},
  'xDisplay': {"key": "display", "tree": ['scales', "xAxes", 'scaleLabel'], "category": "options"},
  'xFontColor': [
    {"key": "fontColor", "tree": ['scales', 'xAxes', 'ticks'], "category": "options"},
    {"key": "color", "tree": ['scales', 'xAxes', 'gridLines'], "category": "options"}
  ],
  'xGrid': {"key": "display", "tree": ['scales', 'xAxes', 'gridLines'], "category": "options"},
  'yLabel': {"key": "labelString", "tree": ['scales', "yAxes", 'scaleLabel'], "category": "options"},
  'yDisplay': {"key": "display", "tree": ['scales', "yAxes", 'scaleLabel'], "category": "options"},
  'precision': {"key": "precision", "tree": ['scales', 'yAxes', 'ticks'], "category": "options"},
  'yFontColor': [
    {"key": "fontColor", "tree": ['scales', 'yAxes', 'ticks'], "category": "options"},
    {"key": "color", "tree": ['scales', 'yAxes', 'gridLines'], "category": "options"}],
  'yGrid': {"key": "display", "tree": ['scales', 'yAxes', 'gridLines'], "category": "options"},

}


class Chart(Html.Html):
  name, category, callFnc = 'ChartJs', 'Charts', 'chartJs'
  references = {
    'Website': 'http://www.chartjs.org/',
    'Documentation': 'http://www.chartjs.org/docs/latest/',
    'examples': 'http://tobiasahlin.com/blog/chartjs-charts-to-get-you-started/#10-bubble-chart',
    'Repository': 'https://github.com/chartjs/Chart.js'}
  __reqJs = ['Chart.js']
  # _grpCls = CssGrpClsCharts.CssClassCharts

  def __init__(self, report, width, height, title, options, htmlCode, filters, profile):
    digits = 0
    if 'digits' in options:
      digits = options['digits']
      del options['digits']
    #if GraphFabric.CHARTS_FACTORY is None:
    #  GraphFabric.CHARTS_FACTORY = GraphFabric.loadFactory() # atomic function to store all the different table mapping
    self.title, self.seriesProperties, self.height, self._chart = title, {'static': {}, 'dynamic': {}}, height[0], None
    super(Chart, self).__init__(report, [], code=htmlCode, width=width[0], widthUnit=width[1], height=height[0], heightUnit=height[1], profile=profile)
    # self.setSeriesColor(report.getColor('charts'))
    self.css({'position': 'relative'})
    if not options.get('legend', True):
      options['legend'] = {'position': 'none'}
    # to solve https://github.com/chartjs/Chart.js/issues/4748
    #self.addAttr({'grid': False, 'top': 0, 'precision': 0, 'bottom': 0, 'xFontColor': self.getColor("greys", -1),
    #              'yFontColor': self.getColor("greys", -1), 'legendFontColor': self.getColor("greys", -1),
    #              'legendPosition': options.get('legend', {'position': 'right'}).get('position', 'right')})
    #self.colName = list(self.__chart.data._schema['keys'])[0]
    #self.yFormat("FLOAT", options={"digits": digits})

  @property
  def chartId(self):
    """
    Return the Javascript variable of the chart
    """
    return "window['%s_obj']" % self.htmlId

  @property
  def chart(self):
    raise Exception("Chart object should be defined in the configuration")

  def filter(self, jsId, colName, allSelected=True, filterGrp=None, operation="=", itemType="string"):
    """
    Link the data to the filtering function. The record will be filtered based on the composant value

    :return: The Python Html Object
    """
    self._report.jsOnLoadFnc.add("%(breadCrumVar)s['params']['%(htmlCode)s'] = ''" % {'htmlCode': self._code, 'breadCrumVar': self._report.jsGlobal.breadCrumVar})
    val = "%(breadCrumVar)s['params']['%(htmlCode)s']" % {'htmlCode': self._code, 'breadCrumVar': self._report.jsGlobal.breadCrumVar}
    filterObj = {"operation": operation, 'itemType': itemType, 'allIfEmpty': allSelected, 'colName': colName, 'val': val, 'typeVal': 'js'}
    self._report.jsSources.setdefault(jsId, {}).setdefault('_filters', {})[self._code] = filterObj
    return self

  @property
  def jsQueryData(self): return "{}" % {"htmlId": self.htmlId}

  def onDocumentLoadVar(self): pass

  def onDocumentReady(self):
    self.ctx = []  # Just to ensure that the Structure of the chart component will not be changed in the python layer
    #GraphFabric.Chart.resolveDict(dict([(key, val) for key, val in self.chart.items() if val]), self.ctx)
    profile = self.profile if self.profile is not None else getattr(self._report, 'PROFILE', False)
    #if profile:
    #  self._report.jsOnLoadFnc.add('''
    #     var t0 = performance.now(); window['%(htmlId)s_def'] = {%(chartDef)s}; %(jsChart)s;
    #     console.log('|ChartJs|%(htmlId)s|'+ (performance.now()-t0 +'|records:%(rowsCount)s'))
    #     ''' % {'htmlId': self.htmlId, 'chartDef': ", ".join(self.ctx), 'jsChart': self.jsGenerate(None), "rowsCount": self.__chart.data._data.count})
    #else:
    self._report.jsOnLoadFnc.add('''window['%(htmlId)s_def'] = {%(chartDef)s}; %(jsChart)s
      ''' % {'htmlId': self.htmlId, 'chartDef': ", ".join(self.ctx), 'jsChart': self.jsGenerate(None)})

  def onDocumentLoadFnc(self): return True


  # --------------------------------------------------------------------------------------------------------------
  #                                             USER FUNCTIONS SECTION
  #
  def addSeries(self, type, label, data, options=None, color=None):
    """
    :category: Javascript - ChartJs
    :rubric: JS
    :example: myChart.addSerie("line", 'test', [1, 2, 3], {"borderColor": "red" })
    :dsc:
      Add a bespoke series to a chartJs chart.
      Be aware that the type might depend of the type expected by your chart at the beginning. Basically if you create a bar chart
      you will not be able to add line series. The best in this case is to create a multi chart.
    :link ChartJs Example: http://www.chartjs.org/samples/latest/scales/logarithmic/line.html
    """
    if options is None:
      options = {}
    seriesIndex = len(self.chart.data.jsArgs[0]['values'])
    colors = color if color is not None else self._report.theme.charts[seriesIndex]
    self.chart.data._data[label] = data
    self.chart.data.jsArgs[0]['values'].append(label)
    options.update({'backgroundColor': colors, 'type': type})
    if type == 'line':
      options['borderColor'] = colors
    self.chart.data._schema['post'][0]['args'][0]['dynamic'][seriesIndex] = options
    return self

  def setType(self, htmlObj):
    self.addAttr("type", htmlObj.val, isPyData=False)
    return self

  def addLine(self, label, data, options=None):
    """
    :category: Javascript - ChartJs
    :rubric: JS
    :example: myChart.addLine('test', [1, 2, 3], {"borderColor": "red" })
    :dsc:
      Add a line series to a chartJs chart.
      Be aware that the type might depend of the type expected by your chart at the beginning. Basically if you create a bar chart
      you will not be able to add line series. The best in this case is to create a multi chart.
    :link ChartJs Example: http://www.chartjs.org/samples/latest/scales/logarithmic/line.html
    """
    extraOption = {'fill': False}
    if options is not None:
      extraOption.update(options)
    self.addSeries('line', label, data, extraOption)

  def addPoints(self, label, data, options=None):
    """
    :category: Javascript - ChartJs
    :rubric: JS
    :example: myChart.addPoints('test', [1, 2, 3], {"borderColor": "red" })
    :dsc:
      Add a Point series to a chartJs chart.
      Be aware that the type might depend of the type expected by your chart at the beginning. Basically if you create a bar chart
      you will not be able to add line series. The best in this case is to create a multi chart.
    :link ChartJs Example: http://www.chartjs.org/samples/latest/scales/logarithmic/scatter.html
    """
    extraOption = {'fill': False, 'showLine': False}
    if options is not None:
      extraOption.update(options)
    self.addSeries('line', label, data, extraOption)

  def addTriangles(self, label, data, options=None):
    """
    :category: Javascript - ChartJs
    :rubric: JS
    :example: myChart.addTriangles('test', [1, 2, 3], {"borderColor": "red" })
    :dsc:
      Add a Point series to a chartJs chart.
      Be aware that the type might depend of the type expected by your chart at the beginning. Basically if you create a bar chart
      you will not be able to add line series. The best in this case is to create a multi chart.
    :link ChartJs Example: http://www.chartjs.org/samples/latest/scales/logarithmic/scatter.html
    """
    extraOption = {'fill': False, 'pointStyle': 'triangle', 'showLine': False}
    if options is not None:
      extraOption.update(options)
    self.addSeries('scatter', label, data, extraOption)


  # --------------------------------------------------------------------------------------------------------------
  #                                             CHART PROPERTIES FUNCTIONS
  #
  def _formatAxis(self, axisName, formatFnc, label=None, options=None, isPyData=False):
    formatFnc = AxisDisplay.DISPLAYS.get(formatFnc, {'tickFormat': formatFnc})
    if 'labelString' in formatFnc:
      label = formatFnc['labelString']
    if label is not None:
      self.addAttr('display', True, ['scales', axisName, 'scaleLabel'], category='options')
      self.addAttr('labelString', label, ['scales', axisName, 'scaleLabel'], category='options')
      self.addAttr('fontColor', self._report.theme.greys[-1], ['scales', axisName, 'scaleLabel'], category='options')
    if options is None:
      options = {'digits': 0}
    if 'digits' not in options:
      options['digits'] = 0
    self.toolTip(digit=options['digits'], format='''
        function(){ 
          if(typeof %(value)s == "number"){return %(value)s.formatMoney(%(digit)s, ",", ".")} 
          else { var tooltipData = %(value)s;
            if(tooltipData.x != undefined){ return "("+ tooltipData.x +", "+ tooltipData.y.formatMoney(%(digit)s, ",", ".") +")" }
            else{return %(value)s}} 
        }()''')
    self.addAttr('callback', formatFnc['tickFormat'] % options, ['scales', axisName, 'ticks'], category='options', isPyData=isPyData)

  def addYAxis(self, axeId, position, type='linear', seriesIds=None, options=None):
    """
    :category: Javascript - ChartJs
    :rubric: JS
    :example: myChart.addYAxis( "", 'right')
    :dsc:
      To attached a series to a new axis; use the option 'yAxisID': 'axeId'
    :link ChartJs Documentation: https://www.chartjs.org/docs/latest/axes/
    :link ChartJs Documentation 2: https://www.chartjs.org/docs/latest/developers/axes.html
    """
    axisName = 'xAxes' if self.__chart.alias in ['hbar'] else 'yAxes'
    axis = {'id': json.dumps(axeId), 'type': json.dumps(type), 'ticks': {'beginAtZero': 'true'}, 'position': json.dumps(position)}
    if options is not None:
      for key, val in options.items():
        if isinstance(val, dict):
          subVal = []
          for sKey, sVal in val.items():
            if "function" in sVal:
              subVal.append("%s: %s" % (sKey, sVal))
            else:
              subVal.append("%s: %s" % (sKey, json.dumps(sVal)))
          axis[key] = "{%s}" % ";".join(subVal)
        else:
          if "function" in val:
            axis[key] = val
          else:
            axis[key] = json.dumps(val)
    if seriesIds is not None:
      for i in seriesIds:
        self.seriesProperties['dynamic'].setdefault(i, {}).update({'yAxisID': axeId})
    self.__chart['options'].setdefault('scales', {}).setdefault(axisName, []).append(axis)

  def yFormat(self, formatFnc, label=None, options=None, isPyData=False):
    """
    :category: Javascript - ChartJs
    :rubric: JS
    :example: myChart.yFormat('K')
    :example: myChart.yFormat( "function(d) { return d3.format(',.2f')(d) }" )
    :dsc:
      Function to format the y-axis. Some formats are already pre defined.
      You can also put a full Javascript function if you want to test a bespoke formatting
    :wrap AxisDisplay: DISPLAYS
    """
    axisName = 'xAxes' if self.__chart.alias in ['hbar'] else 'yAxes'
    self._formatAxis(axisName, formatFnc, label, options, isPyData)
    return self

  def xFormat(self, formatFnc, label=None, options=None, isPyData=False):
    """
    :category: Javascript - ChartJs
    :rubric: JS
    :example: myChart.xFormat('K')
    :dsc:
      Function to format the x-axis. Some formats are already pre defined
    :wrap AxisDisplay: DISPLAYS
    :link ChartJs Documentation: https://www.chartjs.org/docs/latest/axes/cartesian/time.html
    """
    axisName = 'yAxes' if self.__chart.alias in ['hbar'] else 'xAxes'
    self._formatAxis(axisName, formatFnc, label, options, isPyData)

  def addSeriesAttr(self, seriesId, data, dataType=None):
    """
    :category: Chartjs Series Attributes
    :rubric: JS
    :example: >>> chartObj.addSeriesAttr(0, {'label': 'label', 'pointStyle': 'triangle', 'pointRadius': 10})
    :dsc:
      Add attributes to the selected series in the dataset. The series is defined by its index (number) starting from
      zeros in the dataset.
    :link ChartJs Documentation: http://www.chartjs.org/docs/latest/charts/bar.html
    :return: The Python object itself
    """
    if seriesId is None:
      # None will apply this to all the series
      typeAttrs = 'static' if dataType is None else dataType
      self.seriesProperties[typeAttrs].update(data)
    else:
      typeAttrs = 'dynamic' if dataType is None else dataType
      self.seriesProperties[typeAttrs].setdefault(seriesId, {}).update(data)
    return self

  def setSeriesLabel(self, data, seriesId=None):
    if seriesId is None:
      if not isinstance(data, list):
        raise Exception("data should be a list with a name for each series")

      for i, v in enumerate(data):
        self.seriesProperties['dynamic'].setdefault(i, {}).update({'label': v})
    else:
      self.seriesProperties['dynamic'].setdefault(seriesId, {}).update({'label': data})
    return self

  def setSeriesColor(self, colors, seriesId=None, borderColors=None):
    self.__chart._colors(colors, seriesId, borderColors)
    return self

  def addAttr(self, key, val=None, tree=None, category=None, isPyData=True):
    """
    Add attributes to the javascript chart. Simple python interface to add attributes but also properties to
    all the difference object in the structure. Values can be python object but also Javascript objects like functions.

    Documentation
    http://www.chartjs.org/docs/latest/configuration/legend.html

    :return: The python chart object
    """
    if isinstance(key, dict):
      for k, v in key.items():
        if k in CHART_ATTRS:
          attrs = CHART_ATTRS[k]
          if not attrs:
            print("INFO: %s not available for the %s family" % (k, self.name))
            continue # Option not available

          if not isinstance(attrs, list):
            attrs = [attrs]
          for attr in attrs:
            tree = attr.get("tree")
            category = attr.get("category")
            k = attr.get('key', k)
            self.__chart.addAttr(k, v, tree, category, isPyData)
        else:
          self.__chart.addAttr(k, v, tree, category, isPyData)
    else:
      if key in CHART_ATTRS:
        tree = CHART_ATTRS[key].get("tree")
        category = CHART_ATTRS[key].get("category")
        key = CHART_ATTRS[key].get(key, key)
      self.__chart.addAttr(key, val, tree, category, isPyData)
    return self

  def delAttr(self, keys, tree=None, category=None): self.__chart.delAttr(keys, tree, category)

  def showLabels(self, flag):
    """
    :category: Javascript - ChartJs
    :rubric: JS
    :example: myChart.showLabels( False )
    :dsc:
      Show or hide the legend definition
    """
    self.__chart.addAttr('display', flag, ['legend'], category='options')

  def showGrid(self, xGridFlag, yGridFlag):
    """
    :category: Javascript - ChartJs
    :rubric: JS
    :example: myChart.showGrid( True, True )
    :dsc:
      Display or not the x and y grids in the charts
    :link ChartJs Documentation: https://www.chartjs.org/docs/latest/axes/styling.html
    """
    self.__chart.addAttr('display', yGridFlag, ['scales', 'yAxes', 'gridLines'], category='options')
    self.__chart.addAttr('display', xGridFlag, ['scales', 'xAxes', 'gridLines'], category='options')

  def dataSetType(self, chartType, seriesId=None):
    """
    :category: Python - ChartJs
    :rubric: PY
    :example: myChart.dataSetType( "bullet", 0)
    :dsc:
      Change the type of a series in the chart.
      Make sure you are using a chart compatible with the Series you are requesting.
      For example the type multi chart will accept any type of series.
    :return:
    """
    self.__chart.dataSetType(chartType, seriesId)

  def jsRemove(self):
    """
    :category: Javascript function
    :rubric: JS
    :example: myChart.jsRemove()
    :dsc:
      Javascript function to remove the content of a chart container. By triggering this function the chart will be
      totally removed from the page and only a F5 might restore it
    :return: The javascript string used to perform this event
    """
    return '$("#%s_container").remove()' % self.htmlId

  def jsDataSrc(self, jsData='data', jsDataKey=None, isPyData=False, jsParse=None, jsFnc=None):
    jsData = self._jsData(jsData, jsDataKey, jsParse, isPyData, jsFnc)
    return '%(dataId)s = %(jsData)s' % {"dataId": self.__chart.data._jqId, 'jsData': jsData}

  def jsGenerate(self, jsData='data', jsDataKey=None, isPyData=False, jsParse=None, jsFnc=None):
    return '''
      if(%(chartId)s !== undefined){%(chartId)s.destroy()};
      %(chartObj)s''' % {'chartId': self.chartId, 'chartObj': self.chart.build(self.htmlId, self.chartId)}

  def jsTitle(self, jsData='data', jsDataKey=None, isPyData=False, jsParse=None, jsFnc=None):
    jsData = self._jsData(jsData, jsDataKey, jsParse, isPyData, jsFnc)
    return "window['%(htmlId)s_def'].options.title.text = %(jsData)s; window['%(htmlId)s_chart'].update()" % {'htmlId': self.htmlId, 'jsData': jsData}

  def getJs(self):
    """
    Return the full Javascript structure of the object used to defined the chart
    """
    self.ctx = []  # Just to ensure that the Structure of the chart component will not be changed in the python layer
    GraphFabric.Chart.resolveDict(dict([(key, val) for key, val in self.__chart.items() if val]), self.ctx)
    return '''
      chartDef = {%(chartDef)s, data: %(dc)s}; 
      new %(jsCls)s($("#%(htmlId)s").get(0).getContext('2d'), chartDef);
    ''' % {'htmlId': self.htmlId, 'dc': self.__chart.data.getJs(filterSensitive=True), 'jsCls': self.__chart.jsCls,
           'chartDef': ", ".join(self.ctx)}

  def jsSetX(self, jsData='data', jsDataKey=None, isPyData=False, jsParse=None, jsFnc=None):
    jsData = self._jsData(jsData, jsDataKey, jsParse, isPyData, jsFnc)
    return '%(htmlId)s_chart.data.labels = %(jsData)s' % {'htmlId': self.htmlId, 'jsData': jsData}

  def jsAddSeries(self, jsData='data', jsDataKey=None, isPyData=False, jsParse=None, jsFnc=None):
    """
    :category: Javascript - ChartJs
    :rubric: JS
    :example: myChart.jsAddSeries( {"datasets": [[1, 2, 3]], "labels": ["series 1"]} )
    :dsc:
      Function to add on the Javascript side a Series to a chart on demand. This will usually be triggered thanks to a javascript event.
      If the series already exists, it will be replaced by the new one.
    :link ChartJs Documentation: https://stackoverflow.com/questions/8073673/how-can-i-add-new-array-elements-at-the-beginning-of-an-array-in-javascript
    """
    jsData = self._jsData(jsData, jsDataKey, jsParse, isPyData, jsFnc)
    return '''
      if ($.trim(%(jsData)s.labels) !== undefined) {
        if (%(jsData)s.refresh){%(htmlId)s_chart.data.datasets = []}
        var records = %(jsData)s; var chartColors = %(chartColors)s;
        if (%(jsData)s.x !== undefined){%(htmlId)s_chart.data.labels = %(jsData)s.x};
        records.labels.forEach(function(label, i){var seriesIndex = -1;
          %(htmlId)s_chart.data.datasets.forEach(function(rec, index) {
          if (rec.label == label) {seriesIndex = index; %(htmlId)s_chart.data.datasets.splice(index, 1)}});   
          if (records.datasets[i] !== undefined){
            if (seriesIndex != -1){%(htmlId)s_chart.data.datasets.push({fill: false, borderColor: %(chartColors)s[seriesIndex], label: label, backgroundColor: %(chartColors)s[seriesIndex], data: records.datasets[i]})}
            else {%(htmlId)s_chart.data.datasets.push({fill: false, label: label, borderColor: %(chartColors)s[%(htmlId)s_chart.data.datasets.length], backgroundColor: %(chartColors)s[%(htmlId)s_chart.data.datasets.length], data: records.datasets[i]})}}
        }); %(htmlId)s_chart.update()} ''' % {'htmlId': self.htmlId, 'jsData': jsData, 'chartColors': json.dumps(self._report.theme.charts)}

  def jsSetSeries(self, htmlObj, event, url=None, jsData=None, jsFnc='', cacheObj=None, isPyData=True, isDynUrl=False, httpCodes=None,
             htmlCodes=None, datatype='json', context=None, profile=False):
    """
    :category: Chart Event
    :rubric: JS
    :type: Chart Definition
    :example: chartObj.jsSetSeries(s, 'change')
    :dsc:
      Change the series to be displayed by the chart dynamically
    """
    self.addGlobalFnc('UpdateSeries(chartArgs, series)', '''
      var newChartAgrs = {};
      for (var key in chartArgs) {
        if ( (key.indexOf("value") >= 0) || (key.indexOf("chart_0") >= 0)) {newChartAgrs[key] = series} 
        else {newChartAgrs[key] = chartArgs[key]}}; return newChartAgrs''')
    if url is not None:
      if jsData is None:
        jsData = []
      jsData.append(htmlObj)
      getattr(htmlObj, event)(["window['args_%(jsDataId)s'] = UpdateSeries(window['args_%(jsDataId)s'], %(jsFnc)s)" % {
          'jsDataId': self.__chart.data._jsId, 'jsFnc': self._report.jsPost(url, jsData, jsFnc, cacheObj, isPyData,
                      isDynUrl, httpCodes, htmlCodes, datatype, context, profile)}, self.jsGenerate(None)])
    elif jsFnc != '':
      getattr(htmlObj, event)(["window['args_%(jsDataId)s'] = UpdateSeries(window['args_%(jsDataId)s'], %(jsFnc)s(%(val)s))" % {
        'jsDataId': self.__chart.data._jsId, 'val': htmlObj.val, 'jsFnc': jsFnc}, self.jsGenerate(None)])
    else:
      getattr(htmlObj, event)(["window['args_%(jsDataId)s'] = UpdateSeries(window['args_%(jsDataId)s'], [%(val)s])" % {'jsDataId': self.__chart.data._jsId, 'val': htmlObj.val}, self.jsGenerate(None)])
    return self

  def jsSetXAxis(self, htmlObj, event, url=None, jsData=None, jsFnc='', cacheObj=None, isPyData=True, isDynUrl=False, httpCodes=None,
             htmlCodes=None, datatype='json', context=None, profile=False):
    """
    :category: Chart Event
    :rubric: JS
    :type: Chart Definition
    :example: chartObj.jsSetXAxis(s, 'change')
    :dsc:
      Change the xAxis to be displayed by the chart dynamically
    """
    self.addGlobalFnc('UpdateAxis(chartArgs, series)', '''
      var newChartAgrs = {};
      for (var key in chartArgs) {
        if ( (key.indexOf("keys") >= 0) || (key.indexOf("chart_1") >= 0)) {newChartAgrs[key] = series} 
        else {newChartAgrs[key] = chartArgs[key]}}; return newChartAgrs''')
    if url is not None:
      if jsData is None:
        jsData = []
      jsData.append(htmlObj)
      getattr(htmlObj, event)(["window['args_%(jsDataId)s'] = UpdateAxis(window['args_%(jsDataId)s'], %(jsFnc)s)" % {
          'jsDataId': self.__chart.data._jsId, 'jsFnc': self._report.jsPost(url, jsData, jsFnc, cacheObj, isPyData,
                      isDynUrl, httpCodes, htmlCodes, datatype, context, profile)}, self.jsGenerate(None)])
    elif jsFnc != '':
      getattr(htmlObj, event)(["window['args_%(jsDataId)s'] = UpdateAxis(window['args_%(jsDataId)s'], %(jsFnc)s(%(val)s))" % {
        'jsDataId': self.__chart.data._jsId, 'val': htmlObj.val, 'jsFnc': jsFnc}, self.jsGenerate(None)])
    else:
      getattr(htmlObj, event)(["window['args_%(jsDataId)s'] = UpdateAxis(window['args_%(jsDataId)s'], %(val)s)" % {'jsDataId': self.__chart.data._jsId, 'val': htmlObj.val}, self.jsGenerate(None)])
    return self

  def click(self, jsFncs):
    """
    :category: Javascript - ChartJs
    :rubric: JS
    :example: myChart.click( report.jsConsole() )
    :dsc:
      Add a click event on the different items in a Chart. This will act like a button and might trigger some other function on the browser side.
      It might be also used to trigger some Ajax JsPost services
    :link ChartJs Documentation: https://www.chartjs.org/docs/latest/general/interactions/events.html
    """
    if isinstance(jsFncs, list):
      jsFncs = ";".join(jsFncs)
    self.jsFrg('click', '''
      var activePoints = window['%(htmlId)s_chart'].getElementsAtEvent(event); var activeDataSet = window['%(htmlId)s_chart'].getDatasetAtEvent(event); 
      if(activePoints.length > 0) {
        var clickedElementindex = activePoints[0]["_index"];
        data['event_index'] = clickedElementindex; data['value'] = window['%(htmlId)s_chart'].data.datasets[activeDataSet[0]["_datasetIndex"]].data[clickedElementindex] ;
        data['xaxis'] = window['%(htmlId)s_chart'].data.labels[clickedElementindex]; 
        data['label'] = window['%(htmlId)s_chart'].data.datasets[activeDataSet[0]["_datasetIndex"]].label;
        if(%(breadCrumVar)s['params']['%(htmlCode)s'] == data.xaxis) {
          data.isFilter = false; %(breadCrumVar)s['params']['%(htmlCode)s'] = ''; $('#%(dataCode)s_%(htmlId)s').remove()}
        else {data.isFilter = true; %(breadCrumVar)s['params']['%(htmlCode)s'] = data.xaxis};
        %(jsFncs)s;
      } ''' % {"htmlId": self.htmlId, 'jsFncs': jsFncs, "htmlCode": self._code, 'dataCode': self.__chart.data._data.filterCode,
               "breadCrumVar": self._report.jsGlobal.breadCrumVar})

  def toolTip(self, category='label', digit=0, format='%(label)s +": "+ %(value)s.formatMoney(%(digit)s, ",", ".")'):
    """
    :category: Python - ChartJs
    :rubric: PY
    :example: myChart.toolTip()
    :dsc:
      Change the tooltip feature of the chartJs.
      This will translate a python String to a Javascript valid fragment.
    :link ChartJs Documentation: https://www.chartjs.org/docs/latest/configuration/tooltip.html
    """
    formatStr = re.compile("%\(([0-9a-zA-Z_]*)\)s")
    #matches = formatStr.findall(format)
    mapCodes = {"digit": digit, "label": "data.labels[tooltipItems.index]", "value": "data.datasets[tooltipItems.datasetIndex].data[tooltipItems.index]", "y": "tooltipItems.yLabel", "x": "tooltipItems.xLabel"}
    format = format.strip() % mapCodes
    #if matches:
    #  for res in formatStr.finditer(format):
    #    format = format.replace(res.group(0), mapCodes[res.group(1)])
    self.__chart.addAttr(category, 'function(tooltipItems, data) { return %(format)s; }' % {'format':  format}, ['tooltips', 'callbacks'], category='options', isPyData=False)
    return self

  def addLayout(self, data):
    """
    """
    if 'barmode' in data:
      self.__chart.addAttr('stacked', data['barmode'] == 'stack', ['scales', 'xAxes'], category='options')
      self.__chart.addAttr('stacked', data['barmode'] == 'stack', ['scales', 'yAxes'], category='options')
    return self

  # -----------------------------------------------------------------------------------------
  #                                    CHART EXPORT FUNCTIONS
  # -----------------------------------------------------------------------------------------
  def toImg(self): return "window['%s_chart'].toBase64Image()" % self.htmlId

  #def toTsv(self): return "'data:text/csv;charset=utf-8,' + encodeURIComponent(%s)" % self.chart.data.toTsv()

  # -----------------------------------------------------------------------------------------
  #                                    CHART EXPORT OPTIONS
  # -----------------------------------------------------------------------------------------
  def jsLoad(self, flag):
    if flag:
      return '''
      if (!$('#%(htmlId)s').data('loading') || $('#%(htmlId)s').data('loading') == false){
        $('#%(htmlId)s').data('loading', true); $('#%(htmlId)s').hide(); 
        var loadingDiv = $("<div name='loading'><i class='fas fa-spinner fa-spin' style='margin-right:5px'></i> Loading</div>");
        loadingDiv.css({'width': '100%%', 'height': '%(height)spx', 'line-height': '%(height)spx', 'font-style': 'italic', 'display': 'inline-block', 'vertical-align': 'middle', 'text-align': 'center'});
        $('#%(htmlId)s').parent().append(loadingDiv)}''' % {"htmlId": self.htmlId, "height": self.height-40}

    return "$('#%(htmlId)s').parent().find('div[name=loading]').remove(); $('#%(htmlId)s').data('loading', false); $('#%(htmlId)s').show()" % {"htmlId": self.htmlId}

  def __str__(self):
    strChart = '<div style="height:%spx;margin-top:10px"><canvas id="%s"></canvas></div>' % (self.height-40, self.htmlId)
    return GraphFabric.Chart.html(self, self.get_attrs(withId=False, pyClassNames=self.defined), strChart)

  def to_word(self, document):
    # Will automatically add the external library to be able to use this module
    mod_plt = requires("matplotlib.pyplot", reason='Missing Package', install='matplotlib', autoImport=True, sourceScript=__file__)

    if self.__chart['type'] == '"pie"':
      timestamp = time.strftime("%Y%m%d_%H%M%S", time.gmtime())
      aggDf = self.data.data.groupby([self.data.xAxis])[self.data.seriesNames[0]].sum().reset_index()
      fig1, ax1 = mod_plt.subplots()
      ax1.pie(aggDf[self.data.seriesNames[0]], labels=aggDf[self.data.xAxis], autopct='%1.1f%%', shadow=True, startangle=90)
      ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
      chartPath = os.path.join(self._report.run.local_path, "saved", 'pictures', '%s_%s.png' % (self._report._export['id'], timestamp) )
      fig1.savefig(chartPath, format='png')
      document.add_picture(chartPath)

  def to_xls(self, workbook, worksheet, cursor):
    """

    :param workbook:
    :param worksheet:
    :param cursor:
    :return:
    :link xlsxwriter Documentation: http://xlsxwriter.readthedocs.io/working_with_charts.html
    """
    labels = list(self.data.data[self.data.xAxis])
    sizes = list(self.data.data[self.data.seriesNames[0]])
    worksheet.write(cursor['row'], cursor['col'], self.data.xAxis)
    worksheet.write(cursor['row'], cursor['col'] + 1, self.data.seriesNames[0])
    cursor['row'] += 1
    startRow = cursor['row']
    for i, label in enumerate(labels):
      worksheet.write(cursor['row'], cursor['col'], label)
      worksheet.write(cursor['row'], cursor['col'] + 1, sizes[i])
      cursor['row'] += 1
    cursor['row'] += 1

    # Map only on the charts defined in the Python library
    chartType = self.__chart['type'].replace('"', '')
    chart = workbook.add_chart({'type': {"line": "line", "bar": "bar", "pie": "pie"}.get(chartType, 'line')})
    chart.add_series({
      'name': self.title,
      'styles': '=%s!$A$%s:$A$%s' % (worksheet.get_name(), startRow + 1, startRow + len(sizes)) ,
      'values': '=%s!$B$%s:$B$%s' % (worksheet.get_name(), startRow + 1, startRow + len(sizes)),
    })

    # Insert the chart into the worksheet.
    worksheet.insert_chart(startRow, cursor['col']+3, chart)


  # -----------------------------------------------------------------------------------------
  #                                    MARKDOWN SECTION
  # -----------------------------------------------------------------------------------------
  @classmethod
  def matchMarkDownBlock(cls, data): return True if data[0].strip().startswith( "---ChartJs" ) else None

  @staticmethod
  def matchEndBlock(data): return data.endswith("---")

  @classmethod
  def convertMarkDownBlock(cls, data, report=None):
    """
    :category: Markdown
    :rubric: PY
    :example: Data structure recognised
      ---ChartJs:pie
      test|val
      a|12
      b|4
      c|2
      ---
    :dsc:
      onvert the markdown text to a valid report item.
      In order to include it to a report it is necessary to pass the report
    """
    headers = data[1].strip().split("|")
    records = []
    for line in data[2:-1]:
      rec, attr = {}, {}
      if line.startswith("@"):
        dataAttr = line[1:].strip().split(";")
        for d in dataAttr:
          a, b = d.split(":")
          attr[a] = b
        continue

      splitLine = line.replace(",", '.').strip().split("|")
      for i, val in enumerate( splitLine ):
        if i == 0:
          rec[headers[i]] = val
        else:
          rec[headers[i]] = float(val)
      records.append(rec)

    if report is not None:
      p = report.chart(data[0].split(":")[1].strip(), records, seriesNames=headers[1:], xAxis=headers[0])
      p.addAttr(attr, isPyData=False)
    return []

  def jsMarkDown(self): return ""


class ChartLine(Chart):
  @property
  def chart(self):
    """
    :rtype: JsChartJs.ChartJsTypeBar
    """
    if self._chart is None:
      self._chart = JsChartJs.ChartJsTypeBar(self._report, [])
    return self._chart
