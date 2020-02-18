'''
Module used as a wrapper to the Javascript C3 libraries
reference website: http://c3js.org/
https://c3js.org/gettingstarted.html

This module is defined by a main class ** Chart **.

The constructor ::__init__
::onDocumentLoadVar
::onDocumentReady


Python / Javascript Events
::click
::mouseover
::mouseout


Pure Javascript Wrapper
Those function will be only used in **Javascript called** and they will return a piece of string which will be added in the
report to get the data later on in the Javascript layer. Python is just used here to put all the pieces together

The method to destroy the C3 chart ::jsDestroy
The method to group the different charts ::jsGroups

'''


import json

from epyk.core.html import Html
#from epyk.core.html.graph import AxisDisplay
from epyk.core.html.graph import GraphFabric

# The list of CSS classes
# from epyk.core.css.styles import CssGrpClsCharts


CHART_ATTRS = {
  # Legend
  'legend': {'key': 'show', 'category': 'legend'},
  'legendPosition': {"key": "position", "category": "legend"},
  'legendFontColor': False,  # devrived from the CSS Style

  # Title
  'title': {"key": "text", "category": "title"},
  'titleDisplay': False,
  'titleFontColor': False,  # devrived from the CSS Style

  # Points
  'pointDisplay': {"key": "show", 'tree': ['point'], "category": "line"},

  # Axes
  'grid': [
    {"key": 'show', 'tree': ['x'], 'category': 'grid'},
    {"key": 'show', 'tree': ['y'], 'category': 'grid'},
  ],

  # x Axis
  'xLabel': {"key": "label", "tree": ['x'], "category": "axis"},
  'xGrid': {"key": 'show', 'tree': ['x'], 'category': 'grid'},
  'xFontColor': False,  # devrived from the CSS Style

  # y Axis
  'yLabel': {"key": "label", "tree": ['y'], "category": "axis"},
  'yGrid': {"key": 'show', 'tree': ['y'], 'category': 'grid'},
  'yFontColor': False,  # devrived from the CSS Style
}


class Chart(Html.Html):
  name, category, callFnc = 'C3', 'Charts', 'C3'
  references = {'Repository': 'https://github.com/c3js/c3',
                'Pie': 'http://c3js.org/samples/chart_bar.html',
                'Donut': 'http://c3js.org/samples/chart_donut.html',
                'Area': 'http://c3js.org/samples/chart_area.html',
                'Line': 'http://c3js.org/samples/point_show.html',
                'Scatter': 'http://c3js.org/samples/chart_scatter.html',
                'Gauge': 'http://c3js.org/samples/chart_gauge.html',
                'References': 'http://c3js.org/reference.html'}
  __reqCss, __reqJs = ['c3'], ['c3']
  #_grpCls = CssGrpClsCharts.CssClassChartsC3

  def __init__(self, report, chartType, data, width, height, title, options, htmlCode, filters, profile):
    self.seriesProperties, self.__chartJsEvents, self.height = {'static': {}, 'dynamic': {}}, {}, height[0]
    if GraphFabric.CHARTS_FACTORY is None:
      GraphFabric.CHARTS_FACTORY = GraphFabric.loadFactory() # atomic function to store all the different table mapping
    super(Chart, self).__init__(report, [], code=htmlCode, width=width[0], widthUnit=width[1], height=height[0], heightUnit=height[1], profile=profile)
    self.__chart = GraphFabric.CHARTS_FACTORY[self.name][chartType](report, data, self.seriesProperties)
    self.__chart.addAttr(options, None)
    self.__chart.data.attach(self)
    self.__chart['bindto'] = "'#%s_div'" % self.htmlId
    self.css({'padding': '5px', 'position': 'relative'})
    if title:
      self.addAttr('text', title, 'title')
    self.setSeriesColor(report.getColor('charts'))
    self.yFormat("function(d) { return d3.format(',')(d) }")
    self.addAttr({'grid': False, 'top': 0, 'precision': 0, 'bottom': 0, 'xFontColor': self._report.theme.greys[-1],
                  'yFontColor': self._report.theme.greys[-1], 'legendFontColor': self._report.theme.greys[-1],
                  'legendPosition': options.get('legend', {'position': 'right'}).get('position', 'right')})
    if filters is not None:
      if self._code is None:
        raise Exception("ERROR: C3 - %s -  Please add an htmlCode to name your filter" % chartType)

      if filters is True:
        self.filter(data._jqId, list(self.__chart.data._schema['keys'])[0])
      else:
        self.filter(**filters)
      self.jsFrg("onclick", '''
        if(%(breadCrumVar)s['params']['%(htmlCode)s'] === data.name){%(breadCrumVar)s['params']['%(htmlCode)s'] = ''}
        else if(%(breadCrumVar)s['params']['%(htmlCode)s'] === data.labels){%(breadCrumVar)s['params']['%(htmlCode)s'] = ''}
        else{
          if(data.x != undefined) {%(breadCrumVar)s['params']['%(htmlCode)s'] = data.x}
          else if(data.labels != undefined) {%(breadCrumVar)s['params']['%(htmlCode)s'] = data.labels}
          else{%(breadCrumVar)s['params']['%(htmlCode)s'] = data.name}}''' % {'htmlCode': self._code, 'breadCrumVar': self._report.jsGlobal.breadCrumVar})

  def filter(self, jsId, colName, allSelected=True, filterGrp=None, operation="=", itemType="string"):
    """
    Link the data to the filtering function. The record will be filtered based on the composant value

    :return: The Python Html Object
    """
    self._report.jsOnLoadFnc.add("%(breadCrumVar)s['params']['%(htmlCode)s'] = ''" % {'htmlCode': self._code, 'breadCrumVar': self._report.jsGlobal.breadCrumVar})
    val = "%(breadCrumVar)s['params']['%(htmlCode)s'] " % {'htmlCode': self._code, 'breadCrumVar': self._report.jsGlobal.breadCrumVar}
    filterObj = {"operation": operation, 'itemType': itemType, 'allIfEmpty': allSelected, 'colName': colName, 'val': val, 'typeVal': 'js'}
    self._report.jsSources.setdefault(jsId, {}).setdefault('_filters', {})[self.htmlCode] = filterObj
    return self

  def onDocumentLoadVar(self): pass
  def onDocumentLoadFnc(self): return True

  def onDocumentReady(self):
    self.ctx = []  # Just to ensure that the Structure of the chart component will not be changed in the python layer
    for event, fnc in self.__chartJsEvents.items():
      self.addAttr(event, "function (event, i) { var data = %s; %s }" % (fnc['data'], ";".join(fnc['js'])), 'data', isPyData=False)
    GraphFabric.Chart.resolveDict(dict([(key, val) for key, val in self.__chart.items() if val]), self.ctx)
    profile = self.profile if self.profile is not None else getattr(self._report, 'PROFILE', False)
    if profile:
      self._report.jsOnLoadFnc.add('''
                  var t0 = performance.now(); window['%(htmlId)s_def'] = {%(chartDef)s}; %(jsChart)s;
                  console.log('|C3|%(htmlId)s|'+ (performance.now()-t0 +'|records:%(rowsCount)s'))
                  ''' % {'htmlId': self.htmlId, 'chartDef': ", ".join(self.ctx),
                         'jsChart': self.jsGenerate(jsData=None), "rowsCount": self.__chart.data._data.count})
    else:
      self._report.jsOnLoadFnc.add('''
        window['%(htmlId)s_def'] = {%(chartDef)s}; %(jsChart)s
        ''' % {'htmlId': self.htmlId, 'chartDef': ", ".join(self.ctx), 'jsChart': self.jsGenerate(jsData=None)})

  def getJs(self):
    """
    Return the full Javascript structure of the object used to defined the chart
    """
    self.ctx = []  # Just to ensure that the Structure of the chart component will not be changed in the python layer
    for event, fnc in self.__chartJsEvents.items():
      self.addAttr(event, "function (event, i) { var data = %s; %s }" % (fnc['data'], ";".join(fnc['js'])), 'data', isPyData=False)
    GraphFabric.Chart.resolveDict(dict([(key, val) for key, val in self.__chart.items() if val]), self.ctx)
    return '''
chartDef = {%(chartDef)s};
chartDef.data.columns = %(jsData)s; 
c3.generate(chartDef)}
      ''' % {'jsData': self.__chart.data.getJs(filterSensitive=True), 'chartDef': ", ".join(self.ctx)}

  # ---------------------------------------------------------------------------------------------------------
  #                                          JAVASCRIPT EVENTS
  # ---------------------------------------------------------------------------------------------------------
  def jsDataSrc(self, jsData='data', jsDataKey=None, isPyData=False, jsParse=None, jsFnc=None):
    jsData = self._jsData(jsData, jsDataKey, jsParse, isPyData, jsFnc)
    return '%(dataId)s = %(jsData)s' % {"dataId": self.__chart.data._jqId, 'jsData': jsData}

  def jsGenerate(self, jsData='data', jsDataKey=None, isPyData=False, jsId=None):
    if isPyData:
      jsData = json.dumps(jsData)
    if jsDataKey is not None:
      jsData = "%s.%s" % (jsData, jsDataKey)
    return '''
      if(window['%(htmlId)s_chart'] === undefined){
        window['%(htmlId)s_def'].data.columns = %(jsData)s; 
        window['%(htmlId)s_chart'] = c3.generate(window['%(htmlId)s_def'])}
      else {window['%(htmlId)s_chart'].load({columns: %(jsData)s, unload: true})}; %(time)s
      ''' % {'htmlId': self.htmlId, 'jsData': self.__chart.data.setId(jsData).getJs(filterSensitive=True),
             'time': GraphFabric.Chart.jsLastUpdate(self.htmlId)}

  def jsFlow(self, jsData='data', jsDataKey=None, isPyData=False):
    """
    :category: Chart Update
    :rubric: JS
    :type: Event
    :example: chartObj.jsFlow({"columns": [['x', 'Test'], ['value', 2000], ['value2', 4000]], 'length': 0}
    :example: chartObj.jsFlow({"columns": [['x', '2017-02-18'], ['AAPL.Open', 150], ['AAPL.Low', 150]], 'length': 0}
    :dsc:
      Add new records to the charts for the defined series
    :return: The Javascript event as a String
    """
    if isPyData:
      jsData = json.dumps(jsData)
    if jsDataKey is not None:
      jsData = "%s.%s" % (jsData, jsDataKey)
    return "window['%(htmlId)s_chart'].flow(%(jsData)s)" % {'htmlId': self.htmlId, 'jsData': jsData}

  def jsOnBrush(self, jsFncs):
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self.addAttr("onbrush", "function (data) {%s}" % ";".join(jsFncs), category='subchart', isPyData=False)

  def jsDelSeries(self, jsData='data', jsDataKey=None, isPyData=False):
    """
    :category: Chart Update
    :rubric: JS
    :type: Event
    :example: chartObj.jsDelSeries(['AAPL.Open'], isPyData=True)
    :dsc:
      Delete the series in the chart. Series should be defined based on the name.
    :return: The Javascript event as a String
    """
    if isPyData:
      jsData = json.dumps(jsData)
    if jsDataKey is not None:
      jsData = "%s.%s" % (jsData, jsDataKey)
    return '''
      if(%(jsData)s != null){%(jsData)s.forEach(function(series){window['%(htmlId)s_chart'].unload({ ids: series })})} 
      else {window['%(htmlId)s_chart'].load({unload: true});}''' % {'jsData': jsData, 'htmlId': self.htmlId}

  def jsAddSeries(self, jsData='data', jsDataKey=None, isPyData=False):
    """
    :category: Chart Update
    :rubric: JS
    :type: Event
    :example: chartObj.jsAddSeries(['AAPL.Open'], isPyData=True)
    :dsc:
      Add a new series in the chart. Series should be defined based on the name.
    :link Documentation: https://c3js.org/samples/data_load.html
    :return: The Javascript event as a String
    """
    if isPyData:
      jsData = json.dumps(jsData)
    if jsDataKey is not None:
      jsData = "%s.%s" % (jsData, jsDataKey)
    return '''
      var newSeries = %(series)s;
      if(Array.isArray(newSeries)){
        records = {columns: []}; newSeries.forEach(function(s){records.push([s.label].concat(newSeries.data))
        window['%(htmlId)s_chart'].load(records)})}
      else{window['%(htmlId)s_chart'].load({columns: [['x'].concat(newSeries.x), [newSeries.label].concat(newSeries.y)] })}
      ''' % {'htmlId': self.htmlId, 'series': jsData}

  def setType(self, htmlObj):
    """
    :category: Chart Type
    :rubric: JS
    :type: Configuration
    :dsc:
      Put a type based on the value of ARes component
    :return: The Python Chart object
    """
    self.addAttr("type", htmlObj.val, category='data', isPyData=False)
    return self

  def jsDestroy(self): return "window['%s_chart'].destroy()" % self.htmlId

  def jsTranform(self, jsData='data', jsDataKey=None, isPyData=False, seriesId=None):
    """
    :category: Chart Update
    :type: JS
    :rubric: Event
    :example:
      s = report.select(['pie', 'scatter'])
      report.button("Button").click(chartObj.jsTranform(s.val))
    :dsc:
      Change the style of a chart
    :return: The Javascript event as a String
    """
    if isPyData:
      jsData = json.dumps(jsData)
    if jsDataKey is not None:
      jsData = "%s.%s" % (jsData, jsDataKey)
    if seriesId is not None:
      return "window['%(htmlId)s_chart'].transform(%(jsChartType)s, '%(id)s')" % {'htmlId': self.htmlId, 'jsChartType': jsData, 'id': seriesId}

    return "window['%(htmlId)s_chart'].transform(%(jsChartType)s)" % {'htmlId': self.htmlId, 'jsChartType': jsData}

  def jsTitle(self, jsData='data', jsDataKey=None, isPyData=False, jsParse=None, jsFnc=None):
    jsData = self._jsData(jsData, jsDataKey, jsParse, isPyData, jsFnc)
    return "$('#%(htmlId)s_div .c3-title').text(%(jsData)s)" % {'htmlId': self.htmlId, 'jsData': jsData}


  # ---------------------------------------------------------------------------------------------------------
  #                                          JAVASCRIPT EVENTS
  # ---------------------------------------------------------------------------------------------------------
  def addAttr(self, key, val=None, subCategory=None, category=None, isPyData=True):
    """
    :category: Chart Bespoke Definition
    :type: PY
    :rubric: Configuration
    :dsc:
      Add attributes to the Python chart definition. Python will construct a dictionary with all the settings
      related to this charting libraries. At the end it will create the corresponding Javascript Chart object to let
      the javascript take the control.
    :return: The Python Chart object
    """
    if isinstance(key, dict):
      for k, v in key.items():
        self.__chart.addAttr(k, v, subCategory, category, isPyData)
    else:
      if key == 'regions' and not isinstance(val, list):
        val = [val]
      self.__chart.addAttr(key, val, subCategory, category, isPyData)

  def delAttr(self, keys, subCategory=None, category=None): self.__chart.delAttr(keys, subCategory, category)

  def addSeriesAttr(self, seriesId, data, dataType=None):
    """
    :category: Chart Series properties
    :rubric: PY
    :example: chartOjb.addSeriesAttr(0, {'hoverinfo': 'none', 'type': 'scatter'})
    :dsc:
      Add attributes to the selected series in the dataset. The series is defined by its index (number) starting from
      zeros in the dataset.
    :link C3 Documentation: https://plot.ly/javascript/bar-charts/
    :return: The Python Chart Object
    """
    if seriesId is not None:
      for cat, attr in data.items():
        if isinstance(attr, dict):
          for key, val in attr.items():
            self.addAttr(key, val, json.dumps(seriesId), category=cat)
        else:
          # This will ensure C3 to be compatible with ChartJs settings
          if cat == 'backgroundColor':
            self.addAttr(list(self.__chart.data._schema['values'])[seriesId], attr, 'colors', category='data')
    return self

  def setSeriesLabel(self, data, seriesId=None):
    seriesId = {0: 'x', 1: 'y'}.get(seriesId, seriesId)
    self.addAttr('text', data, tree=[seriesId, 'label'], category="axis")
    return self

  def setSeriesColor(self, colors, seriesId=None, borderColors=None):
    """
    :category: Chart Series Settings
    :rubric: JS
    :type: Configuration
    :example: chartOjb.setSeriesColor('yellow', 'value2')
    :dsc:
      Change the default color of a series in the chart
    :link C3 Example: https://c3js.org/samples/data_color.html
    :return: The Python Chart Object
    """
    if seriesId is None:
      self.addAttr('pattern', colors, 'color')
    else:
      self.addAttr(seriesId, colors, 'colors', 'data')
    return self

  def jsGroups(self, seriesId): self.addAttr("styles", seriesId)
  def groupToolTips(self, flag): self.addAttr("grouped", flag, 'tooltip')
  def seriesNames(self, namesMap):  self.addAttr("names", namesMap, 'data')
  def seriesGroups(self, groups): self.addAttr("styles", groups, 'data')
  def seriesOrder(self, order): self.addAttr("order", order, 'data')
  def showLabels(self, flag): self.addAttr("labels", flag, 'data')

  def addGridLine(self, axis, value, text, position='end', cssClass=None):
    if cssClass is not None:
      self._report.style.cssCls(cssClass)
      cssClass = "py_%s" % cssClass.lower
    self.__chart.setdefault('grid', {}).setdefault(axis, {}).setdefault('lines', []).append(
      '{value: %s, text: "%s", position: "%s", "class": "%s"}' % (value, text, position, cssClass) )

  def addRegion(self, axis, start, end, cssClass=None):
    if cssClass is not None:
      self._report.style.cssCls(cssClass)
      cssClass = "py_%s" % cssClass.lower
    self.__chart['regions'].append('{axis: "%s", start: %s, end: %s, "class": "%s"}' % (axis, start, end, cssClass))

  def axisFormat(self, axis, formatType, formatDefinition=None):
    if axis not in self.__chart['axis']:
      self.__chart['axis'][axis] = {}
    if formatType == 'timeseries':
      self.addAttr("type", formatType, axis, 'axis')
      # for example '%Y-%m-%d %H:%M:%S' or '%Y-%m-%d'
      self.addAttr("tick", {'format': formatDefinition}, axis, 'axis')

  def yFormat(self, formatType, options=None, isPyData=False):
    if options is None:
      options = {'digits': 0}
    if 'digits' not in options:
      options['digits'] = 0
    self.addAttr("format", AxisDisplay.DISPLAYS.get(formatType, {'tickFormat': formatType})['tickFormat'] % options, ['y', 'tick'], 'axis', isPyData=isPyData)


  # -----------------------------------------------------------------------------------------
  #                                STANDARD CHART EVENTS
  # -----------------------------------------------------------------------------------------
  def jsFrg(self, typeEvent, jsFnc, jsData="{'event_index': event.index, 'labels': event.x, 'value': event.value, 'name': event.name, 'label': this.styles()[event.index]}"):
    if not typeEvent in self.__chartJsEvents:
      self.__chartJsEvents[typeEvent] = {"data": jsData, 'js': []}
    if isinstance(jsFnc, list):
      self.__chartJsEvents[typeEvent]['js'].extend(jsFnc)
    else:
      self.__chartJsEvents[typeEvent]['js'].append(jsFnc)

  def mouseover(self, jsFnc): self.jsFrg('onmouseover', jsFnc)
  def mouseout(self, jsFnc): self.jsFrg('onmouseout', jsFnc)

  def click(self, jsFncs):
    self.jsFrg("onclick", jsFncs)
    return self

  def jsLoad(self, flag):
    if flag:
      return '''
      if (!$('#%(htmlId)s_div').data('loading') || $('#%(htmlId)s_div').data('loading') == false){
        $('#%(htmlId)s_div').data('loading', true); $('#%(htmlId)s_div').hide(); 
        var loadingDiv = $("<div name='loading'><i class='fas fa-spinner fa-spin' style='margin-right:5px'></i> Loading</div>");
        loadingDiv.css({'width': '100%%', 'height': '%(height)spx', 'line-height': '%(height)spx', 'font-style': 'italic', 'display': 'inline-block', 'vertical-align': 'middle', 'text-align': 'center'});
        $('#%(htmlId)s_div').parent().prepend(loadingDiv)}''' % {"htmlId": self.htmlId, "height": self.height-30}

    return "$('#%(htmlId)s_div').parent().find('div[name=loading]').remove(); $('#%(htmlId)s_div').data('loading', false); $('#%(htmlId)s_div').show()" % {"htmlId": self.htmlId}

  def __str__(self):
    strChart = '<div id="%s_div" style="height:%spx;color:black"></div>' % (self.htmlId, self.height-30)
    return GraphFabric.Chart.html(self, self.get_attrs(withId=False, pyClassNames=self.defined), strChart)

  # -----------------------------------------------------------------------------------------
  #                                    MARKDOWN SECTION
  # -----------------------------------------------------------------------------------------
  @classmethod
  def matchMarkDownBlock(cls, data): return True if data[0].strip().startswith( "---C3" ) else None

  @staticmethod
  def matchEndBlock(data): return data.endswith("---")

  @classmethod
  def convertMarkDownBlock(cls, data, report=None):
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
      p = report.chart(data[0].split(":")[1].strip(), records, seriesNames=headers[1:], xAxis=headers[0], chartFamily='C3')
      p.addAttr(attr, isPyData=False)
    return ["rptObj.chart('C3', '%s')" % (data[2:-1])]

  def jsMarkDown(self): return ""
