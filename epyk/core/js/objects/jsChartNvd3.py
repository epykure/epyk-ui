"""
Module dedicated to perform the data transformation for the NVD3 charts
"""

from epyk.core.js import JsUtils


class JsNVD3Links(object):
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

  def pie(self, y_columns, x_axis, profile=False):
    """
    Data Conversion to a NVD3 pie chart object.

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
    fnc_name = JsNVD3Pie.__name__
    x_axis = JsUtils.jsConvertData(x_axis, None)
    self.__register_records_fnc(fnc_name, JsNVD3Pie.content, list(JsNVD3Pie.pmts), profile | self.profile)
    self._data_schema['out'] = "%s(%%s, %s, %s)" % (fnc_name, y_columns, x_axis)

  def bar(self, y_columns, x_axis, profile=False):
    """
    Data Conversion to a NVD3 bar chart object.

    This entry point will register the Javascript function and then use it on the javascript side using the parameters
    passed in this function. Some basic controls are done on the Python side during the transpilation

    Example
    record = jsObj.data.records([{"B": 'RR3', "A": 0}, {"B": 'RR5', "A": 3}, {"B": 'RR3', "A": 2}])
    record.f.count("B").o.nvd3.pie("count", "column")

    :param y_columns: A python list with the columns in the records
    :param x_axis: A string with a column name from the records

    :return:
    """
    if not isinstance(y_columns, list):
      y_columns = [y_columns]
    fnc_name = JsNVD3Bar.__name__
    x_axis = JsUtils.jsConvertData(x_axis, None)
    self.__register_records_fnc(fnc_name, JsNVD3Bar.content, list(JsNVD3Bar.pmts), profile | self.profile)
    self._data_schema['out'] = "%s(%%s, %s, %s)" % (fnc_name, y_columns, x_axis)

  def sunburst(self, y_columns, x_axis, profile=False):
    """
    Data Conversion to a NVD3 Sunburst chart object.

    This entry point will register the Javascript function and then use it on the javascript side using the parameters
    passed in this function. Some basic controls are done on the Python side during the transpilation

    Example

    :param y_columns: A python list with the columns in the records
    :param x_axis: A string with a column name from the records

    :return:
    """
    if not isinstance(y_columns, list):
      y_columns = [y_columns]
    fnc_name = JsNVD3Bar.__name__
    x_axis = JsUtils.jsConvertData(x_axis, None)
    self.__register_records_fnc(fnc_name, JsNVD3Sunburst.content, list(JsNVD3Sunburst.pmts), profile | self.profile)
    self._data_schema['out'] = "%s(%%s, %s, %s)" % (fnc_name, y_columns, x_axis)


# --------------------------------------------------------------------------------------------------------------------
#                               DATA TRANSFORMATION JAVASCRIPT DEFINITION
# --------------------------------------------------------------------------------------------------------------------
class JsNVD3Pie(object):
  pmts = ("seriesNames", "xAxis")
  content = '''
    var temp = {}; var labels = {};
    data.forEach(function(rec){ 
      if(!(rec[xAxis] in temp)){temp[rec[xAxis]] = {}};
      seriesNames.forEach(function(name){
        labels[name] = true; if(rec[name] !== undefined) {if (!(name in temp[rec[xAxis]])){temp[rec[xAxis]][name] = rec[name]} else {temp[rec[xAxis]][name] += rec[name]}}  }) ;
    });
    var labels = Object.keys(labels); result = [];
    for(var series in temp){
      var values = {y: 0, x: series};
      labels.forEach(function(label){
        if(temp[series][label] !== undefined){values.y = temp[series][label]}});
      result.push(values)}
    '''


class JsNVD3Bar(object):
  pmts = ("seriesNames", "xAxis")
  content = '''
    var temp = {}; var labels = []; var uniqLabels = {};
    seriesNames.forEach(function(series){temp[series] = {}}) ;
    data.forEach(function(rec){ 
      seriesNames.forEach(function(name){
        if(rec[name] !== undefined){
          if (!(rec[xAxis] in uniqLabels)){labels.push(rec[xAxis]); uniqLabels[rec[xAxis]] = true};
          temp[name][rec[xAxis]] = rec[name]}})
    });
    seriesNames.forEach(function(series){
      dataSet = {key: series, values: [], labels: labels};
      labels.forEach(function(x, i){
        var value = temp[series][x]; 
        if (isNaN(value)) { value = null};
        if (value !== undefined) {dataSet.values.push({y: value, x: i, label: x})}
      }); result.push(dataSet)})
    '''


class JsNVD3Sunburst(object):
  pmts = ("seriesNames", "xAxis")
  content = '''
    var result = [{name: xAxis, children: []}]; var sizeTree = seriesNames.length-1;
    data.forEach(function(rec){
      var path = []; var tmpResultLevel = result[0].children; var branchVal = 0;
      seriesNames.forEach(function(s, i){
        var treeLevel = -1; 
        tmpResultLevel.forEach(function(l, j){if(l.name == rec[s]){treeLevel = j}});
        if(i == sizeTree){
          if(treeLevel >= 0){
            tmpResultLevel[treeLevel].size += rec[xAxis]}else{tmpResultLevel.push({name: rec[s], size: rec[xAxis]})}
        }else{
          if(treeLevel < 0 ){
            tmpResultLevel.push({name: rec[s], children: []}); treeLevel = tmpResultLevel.length - 1};
            tmpResultLevel = tmpResultLevel[treeLevel].children}
      })})'''
