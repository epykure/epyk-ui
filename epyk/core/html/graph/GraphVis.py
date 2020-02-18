"""

"""

import json

from epyk.core.html.graph import GraphFabric
from epyk.core.html import Html

# The list of CSS classes
# from epyk.core.css.styles import CssGrpClsCharts


# Define a set of common standard properties cross charting libraries.
# The below mapping will ensure the correct definition is applied
CHART_ATTRS = {
  # Legend
  'legend': {'key': 'showLegend'},
  'legendLabel': {'key': 'legendLabel'},

  # Axes
  'grid': {'key': 'showGrid'},

  'xLabel': {'key': 'xLabel'},
  'xFontColor': {'key': 'axisColor'},
  'xDisplay': {'key': 'showXAxis'},

  'yLabel': {'key': 'yLabel'},
  'yFontColor': {'key': 'axisColor'},
  'yDisplay': {'key': 'showYAxis'},

  'zLabel': {'key': 'zLabel'},
  'zFontColor': {'key': 'axisColor'},
  'zDisplay': {'key': 'showZAxis'}
}


class Chart(Html.Html):
  name, category, callFnc = 'Vis', 'Charts', 'vis'
  __reqJs, __reqCss = ['vis'], ['vis']
  # _grpCls = CssGrpClsCharts.CssClassCharts

  def __init__(self,  report, chartType, data, width, height, title, options, htmlCode, filters, profile):
    self.seriesProperties, self.height, self._groups, self.__edges = {'static': {}, 'dynamic': {}}, height[0], None, None
    if GraphFabric.CHARTS_FACTORY is None:
      GraphFabric.CHARTS_FACTORY = GraphFabric.loadFactory()  # atomic function to store all the different table mapping
    super(Chart, self).__init__(report, data, width=width[0], widthUnit=width[1], height=height[0], heightUnit=height[1], code=htmlCode, profile=profile)
    self.__chart = GraphFabric.CHARTS_FACTORY[self.name][chartType](report, data, self.seriesProperties)
    # self.addAttr({'grid': False, 'top': 0, 'precision': 0, 'bottom': 0, 'xFontColor': self.getColor("greys", -1),
    #               'yFontColor': self.getColor("greys", -1), 'legendFontColor': self.getColor("greys", -1),
    #               'legendPosition': chartOptions.get('legend', {'position': 'right'}).get('position', 'right')})
    if self.__chart.jsType is not None:
      # Simple remapping to be able to reuse existing transformation functions for new chart configurations
      # This will allow the creation of dynamic configurations based on existing charts
      self.__chart.jsCls = GraphFabric.CHARTS_FACTORY[self.name][self.__chart.jsType].jsCls
      self.__chart.data._schema['out']['config'] = self.__chart.data._schema['out']['name']
      self.__chart.data._schema['out']['name'] = "%s_%s" % (self.__chart.data._schema['out']['family'], self.__chart.jsType.replace("-", ""))
    self.__chart.data.attach(self)
    self.title, self.chartType = title, chartType
    self.__chart["height"] = "'%spx'" % (self.height - 50 if title else self.height - 30)

  @property
  def jsQueryData(self): return self.__chart.jsQueryData
  @property
  def eventId(self): return "window['%s_chart']" % self.htmlId

  def onDocumentLoadVar(self): pass
  def onDocumentLoadFnc(self): return True

  def onDocumentReady(self):
    self.ctx = []  # Just to ensure that the Structure of the chart component will not be changed in the python layer
    GraphFabric.Chart.resolveDict(dict([(key, val) for key, val in self.__chart.items() if val]), self.ctx)
    self._report.jsOnLoadFnc.add('''
      window['%(htmlId)s_options'] = {%(options)s}; %(jsChart)s;
      ''' % {'jsChart': self.jsGenerate(jsData=None), 'htmlId': self.htmlId, 'options': ", ".join(self.ctx)})

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
      window['%(htmlId)s_data'] = new vis.DataSet(%(chartData)s);
      if(window['%(htmlId)s_chart'] === undefined){
        window['%(htmlId)s_edges'] = %(edges)s;
        if (window['%(htmlId)s_edges'] == undefined){
          window['%(htmlId)s_chart'] = new vis.%(chartObj)s($("#%(htmlId)s").get(0), window['%(htmlId)s_data'], window['%(htmlId)s_options'])}
        else{
          window['%(htmlId)s_chart'] = new vis.%(chartObj)s($("#%(htmlId)s").get(0), {nodes: window['%(htmlId)s_data'], edges: window['%(htmlId)s_edges']}, window['%(htmlId)s_options'])
        };
        %(groups)s}
      else {window['%(htmlId)s_chart'].%(updateFnc)s(window['%(htmlId)s_data'])}
      ''' % {'htmlId': self.htmlId, 'updateFnc': {"timeline": 'setItems'}.get(self.chartType, "setData"),
             'styles': "window['%s_chart'].setGroups(%s)" % (self.htmlId, json.dumps(self._groups)) if self._groups is not None else '',
             'chartData': self.__chart.data.setId(jsData).getJs([('extend', self.seriesProperties)], filterSensitive=True),
             'chartObj': self.__chart.jsCls, 'edges': json.dumps(self.__edges)}

  def getJs(self):
    """
    Return the full Javascript structure of the object used to defined the chart
    """
    self.ctx = []  # Just to ensure that the Structure of the chart component will not be changed in the python layer
    GraphFabric.Chart.resolveDict(dict([(key, val) for key, val in self.__chart.items() if val]), self.ctx)
    return '''
chartData = new vis.DataSet(%(chartData)s); 
chartOptions = {%(options)s};
new vis.%(chartObj)s($("#%(htmlId)s").get(0), chartData, chartOptions)} 
    ''' % {'htmlId': self.htmlId, 'chartData': self.__chart.data.getJs([('extend', self.seriesProperties)], filterSensitive=True),
           'chartObj': self.__chart.jsCls, 'options': ", ".join(self.ctx)}

  def addAttr(self, key, val=None, tree=None, category=None, isPyData=True):
    """
    Add attributes to the javascript chart. Simple python interface to add attributes but also properties to
    all the difference object in the structure. Values can be python object but also Javascript objects like functions.

    Documentation
    http://www.chartjs.org/docs/latest/configuration/legend.html

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

  # def addAttr(self, key, val=None, tree=None, category=None, isPyData=True):
  #   """
  #   :category:
  #   :rubric: JS
  #   :type: Configuration
  #   :example: chartObj.addAttr('style', 'circle', category='drawPoints')
  #   :example: chartObj.addAttr('visible', False, category='dataAxis')
  #   :dsc:
  #     Update the Chart Options.
  #     All the details of the possible parameters are defined in the docs in the Vis.js official website.
  #     Please have a look to check the properties.
  #     For example for a 2D charts the below options are defined [here](http://visjs.org/docs/graph2d/)
  #   :return: The Python Chart Object
  #   """
  #   if category is not None:
  #     val = self._jsData(val, None, None, isPyData)
  #     if not category in self.__chart._attrs:
  #       self.__chart[category] = {}
  #     if isinstance(key, dict):
  #       self.__chart[category].update(key)
  #     else:
  #       self.__chart[category][key] = val
  #   else:
  #     if isinstance(key, dict):
  #       attrs = {}
  #       for k, v in key.items():
  #         if k in CHART_ATTRS:
  #           k = CHART_ATTRS[k].get("key", k)
  #         attrs[k] = self._jsData(v, None, None, isPyData)
  #       self.__chart.update(attrs)
  #     else:
  #       self.__chart[key] = val
  #   return self

  def jsAddPoints(self, jsData='data', jsDataKey=None, isPyData=False):
    if isPyData:
      jsData = json.dumps(jsData)
    if jsDataKey is not None:
      jsData = "%s.%s" % (jsData, jsDataKey)
    return "window['%(htmlId)s_data'].add(%(jsData)s)" % {'htmlId': self.htmlId,
        'jsData': self.__chart.data.setId(jsData).getJs([('extend', self.seriesProperties)], filterSensitive=True)}

  def jsAddSeries(self, jsData='data', jsDataKey=None, isPyData=False):
    """
    :category: Chart Series Update
    :rubric: JS
    :type: Configuration
    :example: click( ["data = [{x:'2014-06-14', y: 34, group: 3}, {x:'2014-06-11', y: 34, group: 3}]", c.jsAddSeries()])
    :dsc:
      Add a brand new series to the chart.
      The data structure of this new series should directly fit the Vis chart requirement to be correctly added
    :return: The String of the Javascript event
    """
    if isPyData:
      jsData = json.dumps(jsData)
    if jsDataKey is not None:
      jsData = "%s.%s" % (jsData, jsDataKey)
    return "window['%(htmlId)s_data'].add(%(jsData)s)" % {'htmlId': self.htmlId, 'jsData': jsData}

  def setType(self, htmlObj):
    """
    :category: Chart Type
    :rubric: JS
    :type: Configuration
    :dsc:
      Put a type based on the value of ARes component
    :return: The Python Chart object
    """
    self.addAttr("style", htmlObj.val, isPyData=False)
    return self

  def groups(self, groupInfo):
    """
    :category: Chart Groups Definition
    :rubric: JS
    :type: Configuration
    :dsc:
      For some charts this function will allow the creation of styles.
      This does not work with all type of charts, please have a look at the Vis online documentation for more details
      about this option
    :return: The Python Chart object
    """
    self._groups = groupInfo
    return self

  def edges(self, edgesInfo):
    """
    :category: Chart Groups Definition
    :rubric: JS
    :type: Configuration
    :dsc:
      only available for network charts.
    :return: The Python Chart object
    """
    if self.__chart.jsCls != 'Network':
      raise Exception("This property is only available for Network Charts to set the edges between nodes")

    self.__edges = edgesInfo
    return self

  # ---------------------------------------------------------------------------------------------------------
  #                                          PYTHON CONFIGURATION
  # ---------------------------------------------------------------------------------------------------------
  def axis(self, typeAxis, title=None, type=None): pass
  def yFormat(self, formatFnc, label=None, options=None, isPyData=False): pass
  def xormat(self, formatFnc, label=None, options=None, isPyData=False): pass

  def axisLabel(self, label, axis, attrs=None):
    self.__chart["%sLabel" % axis] = json.dumps(label)
    if attrs is not None:
      for attr, v in attrs.items():
        self.__chart["%s%s" % (axis, attr.title())] = v
    return self

  def addSeriesAttr(self, seriesId, data, dataType="dynamic"):
    if dataType == 'static':
      self.__chart.seriesProperties[dataType].update(data)
    else:
      self.__chart.seriesProperties[dataType].setdefault(seriesId, {}).update(data)
    return self

  def click(self, jsFncs):
    """
    :category:
    :rubric: JS
    :type: Events
    :dsc:

    :link Plotly Documentation: https://plot.ly/javascript/plotlyjs-events/
    """
    self.jsFrg('click', jsFncs)
    return self

  def __str__(self):
    if self.title:
      strChart = '<div style="width:100%%;text-align:center;font-size:16px">%s</div><div id="%s" style="height:%spx;margin:auto;width:%s"></div>' % (self.title, self.htmlId, self.height - 50, "400px")
    else:
      strChart = '<div id="%s" style="height:%spx"></div>' % (self.htmlId, self.height - 30)
    return GraphFabric.Chart.html(self, self.get_attrs(withId=False, pyClassNames=self.defined), strChart)


  # ---------------------------------------------------------------------------------------------------------
  #                                          MARKDOWN SECTION
  # ---------------------------------------------------------------------------------------------------------
  @classmethod
  def matchMarkDownBlock(cls, data):
    return True if data[0].strip().startswith("---Vis") else None

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
      p = report.chart(data[0].split(":")[1].strip(), records, seriesNames=headers[1:], xAxis=headers[0], chartFamily='Vis')
      p.addAttr(attr, isPyData=False)
    return []

