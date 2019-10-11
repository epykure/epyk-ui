"""
Module dedicated to perform the data transformation for the Vis charts

https://visjs.org/
"""

from epyk.core.js import JsUtils


class JsChartVisLinks(object):
  def __init__(self, js_src, data_schema=None, profile=False):
    self._js_src, self._data_schema, self.profile = js_src, data_schema, profile

  def __register_records_fnc(self, fnc_name, fnc_def, fnc_pmts=None, profile=False):
    """
    This function will attach to the report object only the javascript functions used during the report

    :param fnc_name: A String with the Javascript function name to be defined
    :param fnc_def: A String with the Javascript function content
    :param fnc_pmts: A list of parameters
    :param profile: A boolean flag to activate the framework profiling

    :return:
    """
    fnc_pmts = ["data"] + (fnc_pmts or [])
    if not fnc_name in self._js_src.get('js', {}).get('functions', {}):
      if profile:
        content = "var result = []; %s;return result" % JsUtils.cleanFncs(fnc_def)
      else:
        content = "var result = []; %s;return result" % JsUtils.cleanFncs(fnc_def)
      self._js_src.setdefault('js', {}).setdefault('functions', {})[fnc_name] = {'content': content, 'pmt': fnc_pmts}

  def timeline(self):
    pass

  def network(self):
    pass

  def two_dim(self, y_columns, x_axis, group=None, profile=False):
    """

    :param y_columns:
    :param x_axis:
    :param group:
    :param profile:

    :return:
    """
    if not isinstance(y_columns, list):
      y_columns = [y_columns]
    fnc_name = JsVis.__name__
    x_axis = JsUtils.jsConvertData(x_axis, None)
    self.__register_records_fnc(fnc_name, JsVis.content, list(JsVis.pmts), profile | self.profile)
    self._data_schema['out'] = "%s(%%s, %s, %s, %s)" % (fnc_name, y_columns, x_axis, JsUtils.jsConvertData(group, None))

  def three_dim(self, y_columns, x_axis, z_axis, profile=False):
    """

    :param y_columns:
    :param x_axis:
    :param z_axis:
    :param profile:

    :return:
    """
    if not isinstance(y_columns, list):
      y_columns = [y_columns]
    fnc_name = JsVis.__name__
    x_axis = JsUtils.jsConvertData(x_axis, None)
    self.__register_records_fnc(fnc_name, JsVis3D.content, list(JsVis3D.pmts), profile | self.profile)
    self._data_schema['out'] = "%s(%%s, %s, %s, %s)" % (fnc_name, y_columns, x_axis, JsUtils.jsConvertData(z_axis, None))


# --------------------------------------------------------------------------------------------------------------------
#                               DATA TRANSFORMATION JAVASCRIPT DEFINITION
# --------------------------------------------------------------------------------------------------------------------
class JsVis(object):
  """
  :category: Vis Transformer
  :rubric: JS
  :type: Configuration
  :dsc:
    Transform a recordset to a data structure usable for a Vis 2D chart.
    As Vis is used for time line, the x axis should be a date in the format YYYY-MM-DD.
    Example of DataFrame:

      index x           y
      0     2018-01-01  10
      1     2018-01-02  20
      2     2018-01-03  30

  :example: aresObj.chart('bar', df, seriesNames=['y', 'y2'], xAxis='x', chartFamily='Vis')
  :example: aresObj.chart('line', df, seriesNames=['y', 'y2'], xAxis='x', chartFamily='Vis')
  """
  pmts = ("seriesNames", "xAxis", "group")
  content = '''
    var temp = {}; var labels = {}; var groups = {};
    data.forEach(function(rec){ 
      if(!(rec[xAxis] in temp)){temp[rec[xAxis]] = {}; groups[rec[xAxis]] = {}};
      seriesNames.forEach(function(name){
        labels[name] = true; if(rec[name] !== undefined){
          if(!(name in temp[rec[xAxis]])){
            temp[rec[xAxis]][name] = rec[name]; if(group !== undefined){groups[rec[xAxis]][name] = rec[group]}} 
          else{temp[rec[xAxis]][name] += rec[name]}}})});
    var labels = Object.keys(labels);
    for(var series in temp){
      labels.forEach(function(label, i){if(temp[series][label] !== undefined){ 
        var row = {x: series, y: temp[series][label], label: {content: temp[series][label].formatMoney(1, ',', '.')}};
        if(group !== undefined){row['group'] = groups[series][label]} else{row['group'] = i};
        result.push(row)}})}
    '''


class JsVis3D(object):
  """
  :category: Vis Transformer
  :rubric: JS
  :type: Configuration
  :dsc:


    for the surface the recordset should be
      data = [
        { x: 0, y: 0, z: 50 },
        { x: 0, y: 31.4, z: 50 },
        { x: 0, y: 62.8, z: 50 },
        { x: 31.4, y: 0, z: 79.37637628569459 },
        { x: 31.4, y: 31.4, z: 20.623660971554436 },
        { x: 31.4, y: 62.8, z: 26.179684010439026 }
      ]

    style: rec[zAxis]
  """
  chartTypes = ['3D', 'surface', 'bar3d', 'scatter3d', 'line3d', 'bubble']
  pmts = ("yAxis", "xAxis", "zAxis")
  content = '''
    data.forEach(function(rec, i){ 
      yAxis.forEach(function(s, j){
        result.push({x: parseFloat(rec[xAxis]), y: rec[s], z: rec[zAxis], name: s, style: rec[zAxis]})})})
    '''
