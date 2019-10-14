"""
Module dedicated to perform the data transformation for the ChartJs charts

https://www.chartjs.org/
"""

from epyk.core.js import JsUtils


class JsChartLinks(object):

  def __init__(self, data, js_src, data_schema=None, profile=False):
    self._js_src, self._data_schema, self.profile, self._data = js_src, data_schema, profile, data

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

  def line(self, y_columns, x_axis, colors=None, attrs=None, profile=False):
    """
    Data Conversion to a ChartJs Line chart object.

    This entry point will register the Javascript function and then use it on the javascript side using the parameters
    passed in this function. Some basic controls are done on the Python side during the transpilation

    Example

    :param y_columns: A python list with the columns in the records
    :param x_axis: A string with a column name from the records
    :param profile: A boolean flag to activate the framework profiling

    :return:
    """
    colors = ["red", "blue"]
    attrs = attrs or {}
    if not isinstance(y_columns, list):
      y_columns = [y_columns]
    fnc_name = JsChartJsPie.__name__
    x_axis = JsUtils.jsConvertData(x_axis, None)
    colors = JsUtils.jsConvertData(colors, None)
    attrs = JsUtils.jsConvertData(attrs, None)
    self.__register_records_fnc(fnc_name, JsChartJs.content, list(JsChartJs.pmts), profile | self.profile)
    self._data_schema['out'] = "%s(%%s, %s, %s, %s, %s)" % (fnc_name, y_columns, x_axis, colors, attrs)
    return self._data

  def pie(self, y_columns, x_axis, profile=False):
    """
    Data Conversion to a Chart Pie chart object.

    This entry point will register the Javascript function and then use it on the javascript side using the parameters
    passed in this function. Some basic controls are done on the Python side during the transpilation

    Example

    :param y_columns: A python list with the columns in the records
    :param x_axis: A string with a column name from the records
    :param profile: A boolean flag to activate the framework profiling

    :return:
    """
    if not isinstance(y_columns, list):
      y_columns = [y_columns]
    fnc_name = JsChartJsPie.__name__
    x_axis = JsUtils.jsConvertData(x_axis, None)
    self.__register_records_fnc(fnc_name, JsChartJsPie.content, list(JsChartJsPie.pmts), profile | self.profile)
    self._data_schema['out'] = "%s(%%s, %s, %s)" % (fnc_name, y_columns, x_axis)
    return self._data

  def polar(self, y_columns, x_axis, profile=False):
    """
    ata Conversion to a ChartJs Polar chart object.

    This entry point will register the Javascript function and then use it on the javascript side using the parameters
    passed in this function. Some basic controls are done on the Python side during the transpilation

    Example

    :param y_columns: A python list with the columns in the records
    :param x_axis: A string with a column name from the records
    :param profile: A boolean flag to activate the framework profiling

    :return:
    """
    return self.pie(y_columns, x_axis, profile)

  def bubble(self, y_columns, x_axis, r_column, profile=False):
    """
    Data Conversion to a ChartJs Bubble chart object.

    This entry point will register the Javascript function and then use it on the javascript side using the parameters
    passed in this function. Some basic controls are done on the Python side during the transpilation

    Example

    :param y_columns: A python list with the columns in the records
    :param x_axis: A string with a column name from the records
    :param profile: A boolean flag to activate the framework profiling

    :return:
    """
    if not isinstance(y_columns, list):
      y_columns = [y_columns]
    fnc_name = JsChartJsPie.__name__
    x_axis = JsUtils.jsConvertData(x_axis, None)
    self.__register_records_fnc(fnc_name, JsChartJsBubble.content, list(JsChartJsBubble.pmts), profile | self.profile)
    self._data_schema['out'] = "%s(%%s, %s, %s, %s)" % (fnc_name, y_columns, x_axis, r_column)
    return self._data

  def scatter(self, y_columns, x_axis, r_column, profile=False):
    """
    Data Conversion to a ChartJs Scatter chart object.

    This entry point will register the Javascript function and then use it on the javascript side using the parameters
    passed in this function. Some basic controls are done on the Python side during the transpilation

    Example

    :param y_columns: A python list with the columns in the records
    :param x_axis: A string with a column name from the records
    :param profile: A boolean flag to activate the framework profiling

    :return:
    """
    if not isinstance(y_columns, list):
      y_columns = [y_columns]
    fnc_name = JsChartJsPie.__name__
    x_axis = JsUtils.jsConvertData(x_axis, None)
    self.__register_records_fnc(fnc_name, JsChartJsScatter.content, list(JsChartJsScatter.pmts), profile | self.profile)
    self._data_schema['out'] = "%s(%%s, %s, %s, %s)" % (fnc_name, y_columns, x_axis, r_column)
    return self._data


# --------------------------------------------------------------------------------------------------------------------
#                               DATA TRANSFORMATION JAVASCRIPT DEFINITION
# --------------------------------------------------------------------------------------------------------------------
class JsChartJs(object):
  pmts = ("seriesNames", "xAxis", "colors", "attrs")
  content = '''
    var temp = {}; var labels = []; var uniqLabels = {};
    seriesNames.forEach(function(series){temp[series] = {}});
    data.forEach(function(rec){ 
      seriesNames.forEach(function(name){
        if(rec[name] !== undefined){
          if (!(rec[xAxis] in uniqLabels)){labels.push(rec[xAxis]); uniqLabels[rec[xAxis]] = true};
          temp[name][rec[xAxis]] = rec[name]}})});
    result = {datasets: [], labels: labels};
    seriesNames.forEach(function(series, i){
      dataSet = {label: series, data: [], backgroundColor: colors[i], borderColor: colors[i]};
      for(var attr in attrs){dataSet[attr] = attrs[attr]};
      labels.forEach(function(x){
        if (temp[series][x] == undefined) {dataSet.data.push(null)} else{dataSet.data.push(temp[series][x])}
      }); result.datasets.push(dataSet)})
    '''


class JsChartJsPie(object):
  pmts = ("seriesNames", "xAxis")
  content = '''
    var temp = {}; var labels = []; var uniqLabels = {};
    seriesNames.forEach(function(series){temp[series] = {}});
    data.forEach(function(rec){ 
      seriesNames.forEach(function(name){
        if(rec[name] !== undefined){
          if (!(rec[xAxis] in uniqLabels)){labels.push(rec[xAxis]); uniqLabels[rec[xAxis]] = true};
          temp[name][rec[xAxis]] = rec[name]}})});
    result = {datasets: [], labels: labels};
    seriesNames.forEach(function(series){
      dataSet = {label: series, data: []};
      labels.forEach(function(x){
        if(temp[series][x] == undefined) {dataSet.data.push(null)} else{dataSet.data.push(temp[series][x])}
      }); result.datasets.push(dataSet)})
    '''


class JsChartJsBubble(object):
  pmts = ("seriesNames", "xAxis", "rDim")
  content = '''
    var temp = {}; var labels = []; var uniqLabels = {};
    seriesNames.forEach(function(series){temp[series] = {}});
    data.forEach(function(rec){ 
      seriesNames.forEach(function(name){
        if(rec[name] !== undefined){
          if (!(rec[xAxis] in uniqLabels)){labels.push(rec[xAxis]); uniqLabels[rec[xAxis]] = true};
          var r = 5; if((rDim != undefined) && (rec[rDim] != undefined)){r = rec[rDim]};
          temp[name][rec[xAxis]] = {y: rec[name], r: r}}})});
    result = {datasets: [], labels: labels};
    seriesNames.forEach(function(series){
      dataSet = {label: series, data: []};
      labels.forEach(function(x, i){
        if(temp[series][x] == undefined) {dataSet.data.push(null)} 
        else{dataSet.data.push({y: temp[series][x].y, x: x, r: temp[series][x].r})}
      }); result.datasets.push(dataSet)})
    '''


class JsChartJsScatter(object):
  pmts = ("seriesNames", "xAxis", "rDim")
  content = '''
    var temp = {}; var labels = [];
    seriesNames.forEach(function(series){temp[series] = []});
    data.forEach(function(rec){ 
      seriesNames.forEach(function(name){
        if(rec[name] !== undefined){
          labels.push(rec[xAxis]); var r = 2; if((rDim != undefined) && (rec[rDim] != undefined)){r = rec[rDim]};
          temp[name].push({y: rec[name], x: rec[xAxis], r: r})}})});
    result = {datasets: [], labels: labels};
    seriesNames.forEach(function(series){
      dataSet = {label: series, data: []};
      labels.forEach(function(x, i){dataSet.data = temp[series]}); 
    result.datasets.push(dataSet)})
    '''
