"""
Module dedicated to perform the data transformation for the Billboard / C3 charts

Related Pages:

		https://naver.github.io/billboard.js/
Related Pages:

		https://c3js.org/
"""

from epyk.core.js import JsUtils


class JsChartBillboardLinks(object):
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

  def line(self, y_columns, x_axis, profile=False):
    """
    Data Conversion to a Line chart object.

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
    fnc_name = JsBillDefault.__name__
    x_axis = JsUtils.jsConvertData(x_axis, None)
    self.__register_records_fnc(fnc_name, JsBillDefault.content, list(JsBillDefault.pmts), profile | self.profile)
    self._data_schema['out'] = "%s(%%s, %s, %s)" % (fnc_name, y_columns, x_axis)

  def pie(self, y_columns, x_axis, profile=False):
    """
    Data Conversion to a Pie chart object.

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
    fnc_name = JsBillPie.__name__
    x_axis = JsUtils.jsConvertData(x_axis, None)
    self.__register_records_fnc(fnc_name, JsBillPie.content, list(JsBillPie.pmts), profile | self.profile)
    self._data_schema['out'] = "%s(%%s, %s, %s)" % (fnc_name, y_columns, x_axis)

  def scatter(self, y_columns, x_axis, profile=False):
    """
    Data Conversion to a Scatter chart object.

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
    fnc_name = JsBillScatter.__name__
    x_axis = JsUtils.jsConvertData(x_axis, None)
    self.__register_records_fnc(fnc_name, JsBillScatter.content, list(JsBillScatter.pmts), profile | self.profile)
    self._data_schema['out'] = "%s(%%s, %s, %s)" % (fnc_name, y_columns, x_axis)


# --------------------------------------------------------------------------------------------------------------------
#                               DATA TRANSFORMATION JAVASCRIPT DEFINITION
# --------------------------------------------------------------------------------------------------------------------
class JsBillDefault(object):
  pmts = ("seriesNames", "xAxis")
  content = '''
    var temp = {}; var labels = []; var uniqLabels = {};
    seriesNames.forEach(function(series){temp[series] = {}});
    data.forEach(function(rec){ 
      seriesNames.forEach(function(name){
        if(rec[name] !== undefined){
          if (!(rec[xAxis] in uniqLabels)){labels.push(rec[xAxis]); uniqLabels[rec[xAxis]] = true};
          temp[name][rec[xAxis]] = rec[name]}})});
    result = []; result.push(['x'].concat(labels));
    seriesNames.forEach(function(series){
      dataSet = [series];
      labels.forEach(function(x){
        if(temp[series][x] == undefined){dataSet.push(null)} else {dataSet.push(temp[series][x])}
      }); result.push(dataSet)})
    '''


class JsBillScatter(object):
  pmts = ("seriesNames", "xAxis")
  content = '''
    var tempVal = {}; var tempX = {}; var labels = []; 
    seriesNames.forEach(function(series){tempVal[series] = []; tempX[series +"_x"] = []});
    data.forEach(function(rec){ 
      seriesNames.forEach(function(name){
        if(rec[name] !== undefined){
          if(!(rec[xAxis] in tempVal[name])){tempVal[name] = [name, rec[name]]; tempX[name +"_x"] = [name +"_x", rec[xAxis]]}
          else {tempVal[name].push(rec[name]); tempX[name +"_x"].push(rec[xAxis])}}})});
    result = {'columns': [], 'xs': {}};
    seriesNames.forEach(function(series){
      result.columns.push(tempVal[series]); result.columns.push(tempX[series +"_x"]); result.xs[series] = series +"_x"})
    '''


class JsBillPie(object):
  pmts = ("seriesNames", "xAxis")
  content = '''
    var temp = {}; var labels = {};
    data.forEach(function(rec){ 
      if(!(rec[xAxis] in temp)){temp[rec[xAxis]] = {}};
      seriesNames.forEach(function(name){
        labels[name] = true; 
        if(rec[name] !== undefined){
          if(!(name in temp[rec[xAxis]])){temp[rec[xAxis]][name] = rec[name]} else{temp[rec[xAxis]][name] += rec[name]}}})});
    result = []; result.push(['x'].concat(labels)); var labels = Object.keys(labels);
    for(var series in temp){
      var values = [series];
      labels.forEach(function(label){
        if(temp[series][label] !== undefined){values.push(temp[series][label])} else{values.push(null)}});
      result.push(values)}
    '''
