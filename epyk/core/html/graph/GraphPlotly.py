
import json

from epyk.core.html import Html
# from epyk.core.html.graph import AxisDisplay
from epyk.core.html.graph import GraphFabric

# The list of CSS classes
# from epyk.core.css.styles import CssGrpClsCharts


CHART_ATTRS = {
  # Chart layout
  'bottom': {"key": "b", "category": "margin", 'type': 'layout'},
  'top': {"key": "t", "category": "margin", 'type': 'layout'},
  'left': {"key": "l", "category": "margin", 'type': 'layout'},
  'right': {"key": "r", "category": "margin", 'type': 'layout'},

  # Legend
  'legend': {'key': 'showlegend', 'type': 'layout'},
  'legendFontColor': {"key": "color", "tree": ['font'], "category": "legend", 'type': 'layout'},
  'legendPosition': {"key": "orientation", "category": "legend", 'type': 'layout'},

  # Title
  'title': {"key": "text", 'type': 'layout', 'category': 'title'},
  'titleFontColor': {"key": "color", "tree": ['font'], 'type': 'layout', 'category': 'title'},

  # Axes
  'grid': [
    {"key": "showgrid", 'type': 'layout', "category": "yaxis"},
    {"key": "showgrid", 'type': 'layout', "category": "xaxis"}
  ],
  'xDisplay': [
    {"key": "showline", 'type': 'layout', "category": "xaxis"},
    {"key": "zeroline", 'type': 'layout', "category": "xaxis"},
  ],
  'xGrid': {"key": "showgrid", 'type': 'layout', "category": "xaxis"},
  'xLabel': {"key": "title", "category": "xaxis", 'type': 'layout'},
  'xType': {"key": "type", "category": "xaxis", 'type': 'layout'},
  'xFontColor': [
    {"key": "color", "category": "xaxis", 'type': 'layout'},
    {"key": "color", "tree": ["titlefont"], "category": "xaxis", 'type': 'layout'},
    {"key": "color", "tree": ["tickfont"], "category": "xaxis", 'type': 'layout'},
  ],
  'yDisplay': [
    {"key": "showline", 'type': 'layout', "category": "yaxis"},
    {"key": "zeroline", 'type': 'layout', "category": "yaxis"},
  ],
  'yGrid': {"key": "showgrid", 'type': 'layout', "category": "yaxis"},
  'yLabel': {"key": "title", "category": "yaxis", 'type': 'layout'},
  'yFontColor': [
    {"key": "color", "category": "yaxis", 'type': 'layout'},
    {"key": "color", "tree": ["titlefont"], "category": "yaxis", 'type': 'layout'},
    {"key": "color", "tree": ["tickfont"], "category": "yaxis", 'type': 'layout'},
  ],
  'zlabel': {"key": "title", "category": "zaxis", 'type': 'layout'},
  'zFontColor': [
    {"key": "color", "tree": ["titlefont"], "category": "zaxis", 'type': 'layout'},
    {"key": "color", "tree": ["tickfont"], "category": "zaxis", 'type': 'layout'},
  ],
}


CHART_ATTRS_3D = {
  'grid': [
    {"key": "showgrid", 'type': 'layout', "tree": ["xaxis"], "category": "scene"},
    {"key": "showgrid", 'type': 'layout', "tree": ["yaxis"], "category": "scene"},
    {"key": "showgrid", 'type': 'layout', "tree": ["zaxis"], "category": "scene"},
  ],
  'xFontColor': [
    {"key": "color", "tree": ["xaxis", "titlefont"], "category": "scene", 'type': 'layout'},
    {"key": "color", "tree": ["xaxis", "tickfont"], "category": "scene", 'type': 'layout'},
  ],

  'yLabel': {"key": "title", "tree": ["yaxis"], "category": "scene", 'type': 'layout'},
  'yFontColor': [
    {"key": "color", "tree": ["yaxis", "titlefont"], "category": "scene", 'type': 'layout'},
    {"key": "color", "tree": ["yaxis", "tickfont"], "category": "scene", 'type': 'layout'},
  ],

  'zLabel': {"key": "title", "tree": ["zaxis"], "category": "scene", 'type': 'layout'},
  'zFontColor': [
    {"key": "color", "tree": ["zaxis", "titlefont"], "category": "scene", 'type': 'layout'},
    {"key": "color", "tree": ["zaxis", "tickfont"], "category": "scene", 'type': 'layout'},
  ],
}


class Chart(Html.Html):
  name, category, callFnc = 'Plotly', 'Charts', 'plotly'
  __reqJs = ['plotly.js']
  # _grpCls = CssGrpClsCharts.CssClassCharts

  def __init__(self, report, chartType, data, width, height, title, options, htmlCode, globalFilter, profile):
    super(Chart, self).__init__(report, [], width=width[0], widthUnit=width[1], height=height[0], heightUnit=height[1], code=htmlCode, profile=profile)
    self._layout, self.options, self.seriesProperties = {}, {"displaylogo": False, 'responsive': True, 'autosize': True, 'legend': options.get("legend", True)}, {'static': {}, 'dynamic': {}}
    self.height, self._dataTraces = height[0], []
    if GraphFabric.CHARTS_FACTORY is None:
      GraphFabric.CHARTS_FACTORY = GraphFabric.loadFactory()  # atomic function to store all the different table mapping
    self.__chart = GraphFabric.CHARTS_FACTORY[self.name][chartType](report, data, self.seriesProperties)
    if self.__chart.jsType is not None:
      # Simple remapping to be able to reuse existing transformation functions for new chart configurations
      # This will allow the creation of dynamic configurations based on existing charts
      data._schema['out']['config'] = data._schema['out']['name']
      data._schema['out']['name'] = "%s_%s" % (data._schema['out']['family'], self.__chart.jsType.replace("-", ""))
    self.__chart.data.attach(self)
    if not 'type' in self.seriesProperties['static']:
      self.seriesProperties['static']['type'] = self.__chart._attrs.get('type', getattr(self.__chart, 'chartObj', None))
    self.setSeriesColor(report._report.theme.charts)
    self.addAttr({'legend': options.get("legend", True), "grid": False, 'xDisplay': True, 'yDisplay': True,
                  'top': 35, 'bottom': 35, 'left': 50, 'right': 50, "height": height[0] - 25, 'xFontColor': self._report.theme.greys[-1],
                  'yFontColor': self._report.theme.greys[-1], "legendFontColor": self._report.theme.greys[-1]})
    if self.__chart.c3d:
      self.addAttr('zFontColor', self._report.thtme.greys[-1])
      self.addAttr("color", self._report.theme.greys[-1], tree=['tickfont'], category="colorbar")
    if title is not None:
      self.addAttr({"title": title, "titleFontColor": self._report.theme.greys[-1]})
    if self.__chart._layout is not None:
      self.addLayout(self.__chart._layout)
    self.addLayout({"colorway": report._report.theme.charts})
    #if chartOptions is not None and 'legend' in chartOptions:
    #  if chartOptions['legend'].get('position') == 'bottom': 'rgba(0,0,0,0)'
    #    self.addLayout({"legend": {"orientation": "h"}})
    self.addLayout({"xaxis": {"fixedrange": options.get("zoom", False)}, "yaxis": {"fixedrange": options.get("zoom", False)}})
    self.addLayout({"modebar": {"orientation": 'v', 'color': self._report.theme.greys[-1], 'bgcolor': self._report.theme.greys[2]},
                                "paper_bgcolor": "rgba(0,0,0,0)", "plot_bgcolor": "rgba(0,0,0,0)"})
    if htmlCode is not None and globalFilter is not None:
      if globalFilter is True:
        self.filter(data._jqId, list(self.__chart.data._schema['keys'])[0])
      else:
        self.filter(**globalFilter)
      self.click('''
        if(%(breadCrumVar)s['params']['%(htmlCode)s'] == data.name){%(breadCrumVar)s['params']['%(htmlCode)s'] = ''}
        else{%(breadCrumVar)s['params']['%(htmlCode)s'] = data.name}
        ''' % {'htmlCode': self._code, 'breadCrumVar': self._report.jsGlobal.breadCrumVar})

  def onDocumentLoadFnc(self): return True
  def onDocumentReady(self):
    # if modebar visible so the margin right should be higher to avoid overlaps
    if self.options.get('displayModeBar', True):
      if self.options.get('legend', True):
        self.addAttr({"right": 150})

    profile = self.profile if self.profile is not None else getattr(self._report, 'PROFILE', False)
    if profile:
      self._report.jsOnLoadFnc.add('''
         var t0 = performance.now(); %(jsChart)s;
         console.log('|Plotly|%(htmlId)s|'+ (performance.now()-t0 +'|records:%(rowsCount)s'))
         ''' % {'htmlId': self.htmlId, 'jsChart': self.jsGenerate(jsData=None), "rowsCount": self.__chart.data._data.count})
    else:
      self._report.jsOnLoadFnc.add("%(jsChart)s;" % {'jsChart': self.jsGenerate(jsData=None), 'htmlId': self.htmlId})

  @property
  def chartId(self):
    """
    Return the Javascript variable of the chart
    """
    return "chart_%s" % self.htmlId

  @property
  def eventId(self): return "document.getElementById('%s')" % self.htmlId

  @property
  def jsQueryData(self): return '''
    function(){
      if(event.points.length == 0){ return {}}
      else{ return {event_val: event.points[0].y, x: event.points[0].x, name: event.points[0].data.name, event_data: event.points, event_code: '%s'}}
    }()''' % self.htmlId

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


  # ---------------------------------------------------------------------------------------------------------
  #                                          JAVASCRIPT EVENTS
  # ---------------------------------------------------------------------------------------------------------
  def jsUpdateChart(self, jsData='data', jsDataKey=None, isPyData=False):
    """
    Update the chart following an event

    Documentation
    https://plot.ly/javascript/plotlyjs-function-reference/#plotlyupdate

    :return:
    """
    if isPyData:
      jsData = json.dumps(jsData)
    if jsDataKey is not None:
      jsData = "%s.%s" % (jsData, jsDataKey)
    return "Plotly.update('%(htmlId)s', %(jsData)s, {});" % {'htmlId': self.htmlId,
                                                             'jsData': self.__chart.data.setId(jsData).getJs([('extend', self.seriesProperties)], filterSensitive=True)}

  def jsDestroy(self): return "Plotly.purge('%s')" % self.htmlId

  def jsRefreshSeries(self, jsData='data', jsDataSeriesNames=None, jsDataKey=None, isPyData=False):
    a = self.jsDelSeries(jsData=jsData, jsDataKey=jsDataSeriesNames, isPyData=isPyData)
    b = self.jsAddSeries(jsData=jsData, jsDataKey=jsDataKey, isPyData=isPyData)
    return ";".join([a, b])

  def setType(self, htmlObj):
    """
    Put a type based on the value of ARes component

    :return: The Python Chart object
    """
    self.addAttr("type", htmlObj.val, isPyData=False)
    return self

  def jsDelSeries(self, jsData='data', jsDataKey=None, isPyData=False):
    """
    Remove the new series to the chart.

    :return: The Javascript string to remove the selected series (based on the ID)
    """
    if isPyData:
      jsData = json.dumps(jsData)
    if jsDataKey is not None:
      jsData = "%s.%s" % (jsData, jsDataKey)
    return '''
      var seriesIds = [];
      %(seriesNames)s.forEach(function(series, i){if(%(jsData)s.indexOf(series) > -1 ){seriesIds.push(i)}});
      Plotly.deleteTraces('%(htmlId)s', seriesIds)''' % {'htmlId': self.htmlId, "jsData": jsData,
                                                         'seriesNames': json.dumps(self.__chart.data._schema['out']['params'][0])}

  def jsSetX(self, jsData='data', jsDataKey=None, isPyData=False, jsParse=None, jsFnc=None):
    # This function is useless for this chart as it will automatically update the x axis from the series it receives
    return ""

  def jsAddSeries(self, jsData='data', jsDataKey=None, isPyData=False):
    """
    Add the new series to the chart.

    Example
    chartObj.jsAddSeries( {y: [5000, null], x: ['Serie1', 'Serie2'], type: 'bar'} )

    :return: The Javascript string to add the new series
    """
    if isPyData:
      jsData = json.dumps(jsData)
    if jsDataKey is not None:
      jsData = "%s.%s" % (jsData, jsDataKey)
    return '''
      var newSeries = %(jsData)s;
      if(Array.isArray(newSeries)){}
      else{
        if (newSeries.refresh){document.getElementById('%(htmlId)s').data = []};
        if (typeof newSeries.labels !== 'undefined'){
          var pSeries = [];
          newSeries.labels.forEach(function(s, i){
            var trace; var chart3Dim = false;
            if (typeof document.getElementById('%(htmlId)s').layout.scene === 'undefined'){trace = {name: s, x: [], y: []}}
            else {chart3Dim = true; trace = {z: [], x: [], y: []}};
            if(typeof newSeries.types !== 'undefined'){trace.type = newSeries.types[i]}
            if (!newSeries.datasets[i]){
              var seriesId = -1;
              document.getElementById('%(htmlId)s').data.forEach(function(se, j){if (se.name == s){seriesId = j}});
              if(seriesId >= 0) {Plotly.deleteTraces('%(htmlId)s', seriesId)}
            } else {
              if (chart3Dim){
                var zAxis = []; var xAxis = []; var yAxis = [];
                newSeries.datasets[i].forEach(function(d, j){trace.z.push(d.z); trace.x.push(d.x); trace.y.push(d.y)});
                /*trace.z.push(zAxis); trace.x.push(xAxis); trace.y.push(yAxis);*/
              } else{
                newSeries.datasets[i].forEach(function(d, j){
                  if(typeof d === "object"){trace.x.push(d.x); trace.y.push(d.y)}
                  else{trace.x.push(j); trace.y.push(d)}
              })}
              
              if(typeof newSeries.statics !== 'undefined'){
                for(var l in newSeries.statics){
                  trace[l] = newSeries.statics[l]}
              };
              pSeries.push(trace)}
          });
          Plotly.addTraces('%(htmlId)s', pSeries)
        } else {
          newSeries.name = newSeries.label; Plotly.addTraces('%(htmlId)s', [newSeries])}}
      ''' % {'htmlId': self.htmlId, "jsData": jsData}

  def jsFlow(self, jsData='data', jsDataKey=None, isPyData=False):
    """

    Example
    chartObj.jsFlow({"columns": [['x', 'Test'], ['value', 2000], ['value2', 4000]], 'length': 0}

    :return: The Javascript event as a String
    """
    if isPyData:
      jsData = json.dumps(jsData)
    if jsDataKey is not None:
      jsData = "%s.%s" % (jsData, jsDataKey)
    return "Plotly.extendTraces('%(htmlId)s', %(jsData)s, [0]);" % {'htmlId': self.htmlId, "jsData": jsData}

  def jsDataSrc(self, jsData='data', jsDataKey=None, isPyData=False, jsParse=None, jsFnc=None):
    jsData = self._jsData(jsData, jsDataKey, jsParse, isPyData, jsFnc)
    return '%(dataId)s = %(jsData)s' % {"dataId": self.__chart.data._jqId, 'jsData': jsData}

  def jsGenerate(self, jsData='data', jsDataKey=None, isPyData=False, jsId=None):
    """
    Generate (or re build) the chart.

    :return: The Javascript event as a String
    """
    if isPyData:
      jsData = json.dumps(jsData)
    if jsDataKey is not None:
      jsData = "%s.%s" % (jsData, jsDataKey)
    return ''' 
      if(window['%(htmlId)s_chart'] === undefined){
        var chartData = %(jsData)s; 
        %(subPlots)s.forEach(function(s){chartData.push(s)});
        window['%(htmlId)s_chart'] = Plotly.newPlot('%(htmlId)s', chartData, %(jsLayout)s, %(options)s)}
      else { window['%(htmlId)s_chart'] = Plotly.react('%(htmlId)s', %(jsData)s, %(jsLayout)s, %(options)s) }; %(time)s
      ''' % {'htmlId': self.htmlId, 'jsData': self.__chart.data.setId(jsData).getJs([('extend', self.seriesProperties)], True),
             'jsLayout': json.dumps(self._layout), 'options': json.dumps(self.options),
             'subPlots': json.dumps(self._dataTraces),
             'time': GraphFabric.Chart.jsLastUpdate(self.htmlId)}

  def getJs(self):
    """
    Return the full Javascript structure of the object used to defined the chart

    """
    return '''
Plotly.newPlot('%(htmlId)s', %(jsData)s, %(jsLayout)s, %(options)s)}
    ''' % {'htmlId': self.htmlId, 'jsData': self.__chart.data.getJs([('extend', self.seriesProperties)], filterSensitive=True),
           'jsLayout': json.dumps(self._layout), 'options': json.dumps(self.options)}

  # ---------------------------------------------------------------------------------------------------------
  #                                          PYTHON CONFIGURATION
  # ---------------------------------------------------------------------------------------------------------
  def axis(self, typeAxis, title=None, type=None):
    """
    Change the usual axis parameters of the chart.

    Documentation
    https://plot.ly/javascript/reference/#layout-xaxis-type

    :return: The Python Chart Object
    """
    if title is not None:
      self.addLayout({"%saxis" % typeAxis: {"title": title}})
    if type is not None:
      self.addLayout({"%saxis" % typeAxis: {"type": type}})
    return self

  def yFormat(self, formatFnc, label=None, options=None, isPyData=False):
    """
    No need to use this function plotly will format automatically the axis
    """
    if formatFnc in AxisDisplay.DISPLAYS:
      if 'labelString' in AxisDisplay.DISPLAYS[formatFnc]:
        label = AxisDisplay.DISPLAYS[formatFnc]['labelString']
    if label is not None:
      self.addAttr({"ylabel": label})
    return self

  def xFormat(self, formatFnc, label=None, options=None, isPyData=False):
    """
    No need to use this function plotly will format automatically the axis
    """
    if formatFnc in AxisDisplay.DISPLAYS:
      if 'labelString' in AxisDisplay.DISPLAYS[formatFnc]:
        label = AxisDisplay.DISPLAYS[formatFnc]['labelString']
    if label is not None:
      self.addAttr({"xlabel": label})
    return self

  def addSeries(self, type, label, data, options=None, color=None):
    """
    Plotly.addTraces(graphDiv, {y: [1, 5, 7]}, 0);

    :return: The Python Chart Object
    """
    if options is None:
      options = {}
    seriesIndex = len(self.__chart.data._schema['values'])
    self.__chart.data._data[label] = data
    self.__chart.data._schema['values'].add(label)
    self.__chart.data._schema['fncs'][0]['args'][1].append(label)
    self.seriesProperties['dynamic'][seriesIndex] = options
    return self

  def setSeriesLabel(self, data, seriesId=None):
    if seriesId is None:
      if not isinstance(data, list):
        raise Exception("data should be a list with a name for each series")

      for i, v in enumerate(data):
        self.seriesProperties['dynamic'].setdefault(i, {}).update({'name': v})
    else:
      self.seriesProperties['dynamic'].setdefault(seriesId, {}).update({'name': data})
    return self

  def annotation(self, x, y, text, xref="x", yref="y", attrs=None):
    """

    https://plot.ly/javascript/text-and-annotations/
    """
    if not "annotations" in self._layout:
      self._layout["annotations"] = []
    self._layout["annotations"].append({"x": x, "y": y, "text": text, "xref": xref, "yref": yref,
                                        "arrowcolor": self._report.theme.greys[-1], 'font': {"color": self._report.greys[-1]}})
    if self.options.get("editable", False):
      self._layout["annotations"][-1]['captureevents'] = True
    return self

  def addAttr(self, key, val=None, tree=None, category=None, isPyData=True):
    """
    :return: The Python Chart Object
    """
    optionsAttrs = ["editable", 'displayModeBar', 'showLink', 'responsive']
    if isinstance(key, dict):
      for k, v in key.items():
        if k in optionsAttrs:
          self.options[k] = v
          continue

        if k in CHART_ATTRS:
          if self.__chart.c3d and k in CHART_ATTRS_3D:
            attrs = CHART_ATTRS_3D[k]
          else:
            attrs = CHART_ATTRS[k]
          if not attrs:
            print("INFO: %s not available for the %s family" % (k, self.name))
            continue # Option not available

          if not isinstance(attrs, list):
            attrs = [attrs]
          for attr in attrs:
            category = attr.get("category")
            if category is not None:
              tree = attr.get("tree")
              k = attr.get("key", k)
              if tree is not None:
                if not category in self._layout:
                  self._layout[category] = {}
                chartLevel = self._layout[category]
                for t in tree:
                  if t not in chartLevel:
                    chartLevel[t] = {}
                  chartLevel = chartLevel[t]
                chartLevel[k] = v
              else:
                k = attr.get("key", k)
                self._layout.setdefault(category, {})[k] = v
            else:
              k = attr.get("key", k)
              self._layout[k] = v
        else:
          self._layout[k] = v
    else:
      if key in optionsAttrs:
        self.options[key] = val
      else:
        if key in CHART_ATTRS:
          if self.__chart.c3d and key in CHART_ATTRS_3D:
            attrs = CHART_ATTRS_3D[key]
          else:
            attrs = CHART_ATTRS[key]
          if not attrs:
            print("INFO: %s not available for the %s family" % (key, self.name))
            return self

          if not isinstance(attrs, list):
            attrs = [attrs]
          for attr in attrs:
            category = attr.get("category")
            if category is not None:
              tree = attr.get("tree")
              key = attr.get("key", key)
              if tree is not None:
                if not category in self._layout:
                  self._layout[category] = {}
                chartLevel = self._layout[category]
                for t in tree:
                  if t not in chartLevel:
                    chartLevel[t] = {}
                  chartLevel = chartLevel[t]
                chartLevel[key] = val
              else:
                key = attr.get("key", key)
                self._layout.setdefault(category, {})[key] = val
            else:
              key = attr.get("key", key)
              self._layout[key] = val
        else:
          if category is not None:
            if tree is not None:
              if not category in self._layout:
                self._layout[category] = {}
              chartLevel = self._layout[category]
              for t in tree:
                if t not in chartLevel:
                  chartLevel[t] = {}
                chartLevel = chartLevel[t]
              chartLevel[key] = val
            else:
              self._layout.setdefault(category, {})[key] = val
          self._layout[key] = val
    return self

  def addSeriesAttr(self, seriesId, data, dataType=None):
    """
    Add attributes to the selected series in the dataset. The series is defined by its index (number) starting from
    zeros in the dataset.

    Example
    chartOjb.addSeriesAttr(0, {'hoverinfo': 'none', 'type': 'scatter'})

    Documentation
    https://plot.ly/javascript/bar-charts/

    :return: The Python Chart Object
    """
    if seriesId is None:
      # None will apply this to all the series
      typeAttrs = 'static' if dataType is None else dataType
      self.seriesProperties[typeAttrs].update(data)
    else:
      typeAttrs = 'dynamic' if dataType is None else dataType
      self.seriesProperties.setdefault(typeAttrs, {}).setdefault(seriesId, {}).update(data)
    return self

  def setSeriesColor(self, colors, seriesIds=None, borderColors=None):
    """
    Documentation

    Example
    report.cssObj.colorObj.getColors('#FFFFFF', '#008000', 10)

    :return: The Python Chart Object
    """
    self.__chart._colors(colors, seriesIds, borderColors)
    return self

  def addLayout(self, data):
    """
    Example
    chartOjb.addLayout( {'barmode': 'stack'} )
    """
    for k, v in data.items():
      if isinstance(v, dict):
        for sk, sv in v.items():
          self._layout.setdefault(k, {})[sk] = sv
      else:
        self._layout[k] = v
    return self


  # ---------------------------------------------------------------------------------------------------------
  #                                          JAVASCRIPT EVENTS
  # ---------------------------------------------------------------------------------------------------------
  def click(self, jsFncs):
    """
    Documentation
    https://plot.ly/javascript/plotlyjs-events/
    """
    self.jsFrg('plotly_click', jsFncs)
    return self

  def hover(self, jsFncs):
    """
    Documentation
    https://plot.ly/javascript/plotlyjs-events/
    """
    self.jsFrg('plotly_hover', jsFncs)
    return self

  def select(self, jsFncs):
    """
    Documentation
    https://plot.ly/javascript/lasso-selection/
    """
    self.jsFrg('plotly_selected', jsFncs)
    return self

  def clickAnnotation(self, jsFncs):
    """
    Documentation
    https://plot.ly/javascript/lasso-selection/
    """
    self.jsFrg('plotly_clickannotation', jsFncs)
    return self


  # ---------------------------------------------------------------------------------------------------------
  #                                          CHART SUBPLOTS
  # ---------------------------------------------------------------------------------------------------------
  def grid(self, rows, columns):
    if len(self._dataTraces) == 0:
      raise Exception("Cannot add subPlot from an empty trace")

    self.addLayout({"grid": {"rows": rows, "columns": columns}})
    return self

  def tracesDomain(self, domains, attrs=None, traceId=None):
    if isinstance(domains, dict):
      self.addLayout({"grid": domains})
    else:
      if traceId is not None:
        self.addLayout({"yaxis%s" % traceId: {"domain": domains[1], "anchor": "y%s" % traceId},
                        "xaxis%s" % traceId: {"domain": domains[0], "anchor": "x%s" % traceId}})
      else:
        for i, d in enumerate(domains):
          seriesId = i+1
          self.addLayout({"yaxis%s" % seriesId: {"domain": d[1], "anchor": "y%s" % seriesId},
                          "xaxis%s" % seriesId: {"domain": d[0], "anchor": "x%s" % seriesId}})
    #if attrs is not None and i < len(attrs):
    #  self.addLayout[-1].update(attrs[i])
    return self

  def addSubPlot(self, chart, domain, attrs=None):

    self.tracesDomain(domain, attrs)
    return self

  def addTrace(self, seriesName, xAxis, domains, zAxis=None, type="scatter", name=None, data=None):
    if data is None:
      data = self.__chart.data._data
    trace = {'type': type, 'x': list(data[xAxis]), 'y': list(data[seriesName])}
    if zAxis is not None:
      trace['z'] = data[zAxis]
    if name is not None:
      trace['name'] = name
    traceId = len(self._dataTraces) + 1 if len(self._dataTraces) > 0 else 2
    if traceId > 0:
      trace.update({'xaxis': "x%s" % traceId, "yaxis": "y%s" % traceId})
    self._dataTraces.append(trace)
    self.tracesDomain(domains, traceId=traceId)
    return self


  # -----------------------------------------------------------------------------------------
  #                                    CHART EXPORT FUNCTIONS
  # -----------------------------------------------------------------------------------------
  def toImg(self, width=400): return "Plotly.toImage(window['%s'], {format:'jpeg', height: %s, width: %s})" % (self.htmlId, self.height, width)

  def __str__(self):
    """
    Return the component HTML display. No use of the features in the function htmlContainer() for this Chart as Plotly is providing
    already most of the features. So for those charts the display of the events might slightly different from the other charts.

    :return: The HTML string to be added to the template.
    """
    strChart = '<div id="%(htmlId)s"></div>' % {'htmlId': self.htmlId}
    return GraphFabric.Chart.html(self, self.get_attrs(withId=False, pyClassNames=self.defined), strChart)


  # ---------------------------------------------------------------------------------------------------------
  #                                          MARKDOWN SECTION
  # ---------------------------------------------------------------------------------------------------------
  @classmethod
  def matchMarkDownBlock(cls, data):
    return True if data[0].strip().startswith("---Plotly") else None

  @staticmethod
  def matchEndBlock(data):
    return data.endswith("---")

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
      for i, val in enumerate(splitLine):
        if i == 0:
          rec[headers[i]] = val
        else:
          rec[headers[i]] = float(val)
      records.append(rec)

    if report is not None:
      p = report.chart(data[0].split(":")[1].strip(), records, seriesNames=headers[1:], xAxis=headers[0], chartFamily='Plottly')
      p.addAttr(attr, isPyData=False)
    return []
