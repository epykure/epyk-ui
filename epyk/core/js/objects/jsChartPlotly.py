"""
Module dedicated to perform the data transformation for the Plotly charts
"""

import json

from epyk.core.js import JsUtils

# List of defined names for the country charts
CTY = ['Belarus', 'Moldova', 'Lithuania', 'Russia', 'Romania', 'Ukraine', 'Andorra', 'Hungary', 'Czech Republic',
       'Slovakia', 'Portugal', 'Serbia', 'Grenada', 'Poland', 'Latvia', 'Finland', 'South Korea', 'France', 'Australia',
       'Croatia', 'Ireland', 'Luxembourg', 'Germany', 'Slovenia', 'United Kingdom', 'Denmark', 'Bulgaria', 'Spain',
       'Belgium', 'South Africa', 'New Zealand', 'Gabon', 'Namibia', 'Switzerland', 'Saint Lucia', 'Austria', 'Estonia',
       'Greece', 'Kazakhstan', 'Canada', 'Nigeria', 'Netherlands', 'Uganda', 'Rwanda', 'Chile', 'Argentina', 'Burundi',
       'United States', 'Cyprus', 'Sweden', 'Venezuela', 'Paraguay', 'Brazil', 'Sierra Leone', 'Montenegro', 'Belize',
       'Cameroon', 'Botswana', 'Saint Kitts and Nevis', 'Guyana', 'Peru', 'Panama', 'Niue', 'Palau', 'Norway', 'Tanzania',
       'Georgia', 'Uruguay', 'Angola', 'Laos', 'Japan', 'Mexico', 'Ecuador', 'Dominica', 'Iceland', 'Thailand',
       'Bosnia and Herzegovina', 'Sao Tome and Principe', 'Malta', 'Albania', 'Bahamas', 'Dominican Republic',
       'Mongolia', 'Cape Verde', 'Barbados', 'Burkina Faso', 'Italy', 'Trinidad and Tobago', 'China', 'Macedonia',
       'Saint Vincent and the Grenadines', 'Equatorial Guinea', 'Suriname', 'Vietnam', 'Lesotho', 'Haiti', 'Cook Islands',
       'Colombia', 'Ivory Coast', 'Bolivia', 'Swaziland', 'Zimbabwe', 'Seychelles', 'Cambodia', 'Puerto Rico',
       'Netherlands Antilles', 'Philippines', 'Costa Rica', 'Armenia', 'Cuba', 'Nicaragua', 'Jamaica', 'Ghana', 'Liberia',
       'Uzbekistan', 'Chad', 'United Arab Emirates', 'Kyrgyzstan', 'India', 'Turkmenistan', 'Kenya', 'Ethiopia', 'Honduras',
       'Guinea-Bissau', 'Zambia', 'Republic of the Congo', 'Guatemala', 'Central African Republic', 'North Korea',
       'Sri Lanka', 'Mauritius', 'Samoa', 'Democratic Republic of the Congo', 'Nauru', 'Gambia',
       'Federated States of Micronesia', 'El Salvador', 'Fiji', 'Papua New Guinea', 'Kiribati', 'Tajikistan',
       'Israel', 'Sudan', 'Malawi', 'Lebanon', 'Azerbaijan', 'Mozambique', 'Togo', 'Nepal', 'Brunei', 'Benin',
       'Singapore', 'Turkey', 'Madagascar', 'Solomon Islands', 'Tonga', 'Tunisia', 'Tuvalu', 'Qatar', 'Vanuatu',
       'Djibouti', 'Malaysia', 'Syria', 'Maldives', 'Mali', 'Eritrea', 'Algeria', 'Iran', 'Oman', 'Brunei', 'Morocco',
       'Jordan', 'Bhutan', 'Guinea', 'Burma', 'Afghanistan', 'Senegal', 'Indonesia', 'Timor-Leste', 'Iraq', 'Somalia',
       'Egypt', 'Niger', 'Yemen', 'Comoros', 'Saudi Arabia', 'Bangladesh', 'Kuwait', 'Libya', 'Mauritania', 'Pakistan']


class JsChartPlotlyLinks(object):
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

  def line(self, y_columns, x_axis, profile=False):
    """
    Data Conversion to a Plotly Line chart object.

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
    fnc_name = JsPlotly.__name__
    x_axis = JsUtils.jsConvertData(x_axis, None)
    self.__register_records_fnc(fnc_name, JsPlotly.content, list(JsPlotly.pmts), profile | self.profile)
    self._data_schema['out'] = "%s(%%s, %s, %s)" % (fnc_name, y_columns, x_axis)

  def pie(self, y_columns, x_axis, profile=False):
    """
    Data Conversion to a Plotly Pie chart object.

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
    fnc_name = JsPlotlyPie.__name__
    x_axis = JsUtils.jsConvertData(x_axis, None)
    self.__register_records_fnc(fnc_name, JsPlotlyPie.content, list(JsPlotlyPie.pmts), profile | self.profile)
    self._data_schema['out'] = "%s(%%s, %s, %s)" % (fnc_name, y_columns, x_axis)

  def heatmap(self, y_columns, x_axis, profile=False):
    """
    Data Conversion to a Plotly Heatmap chart object.

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
    fnc_name = JsPlotlyHeatmap.__name__
    x_axis = JsUtils.jsConvertData(x_axis, None)
    self.__register_records_fnc(fnc_name, JsPlotlyHeatmap.content, list(JsPlotlyHeatmap.pmts), profile | self.profile)
    self._data_schema['out'] = "%s(%%s, %s, %s)" % (fnc_name, y_columns, x_axis)

  def map(self, y_columns, x_axis, profile=False):
    """
    Data Conversion to a Plotly Map chart object.

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
    fnc_name = JsPlotlyMaps.__name__
    x_axis = JsUtils.jsConvertData(x_axis, None)
    self.__register_records_fnc(fnc_name, JsPlotlyMaps.content, list(JsPlotlyMaps.pmts), profile | self.profile)
    self._data_schema['out'] = "%s(%%s, %s, %s)" % (fnc_name, y_columns, x_axis)

  def scatter(self, y_columns, x_axis, profile=False):
    """
    Data Conversion to a Plotly Scatter chart object.

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
    fnc_name = JsPlotlyScatter.__name__
    x_axis = JsUtils.jsConvertData(x_axis, None)
    self.__register_records_fnc(fnc_name, JsPlotlyScatter.content, list(JsPlotlyScatter.pmts), profile | self.profile)
    self._data_schema['out'] = "%s(%%s, %s, %s)" % (fnc_name, y_columns, x_axis)

  def box(self, y_columns, profile=False):
    """
    Data Conversion to a Plotly Box chart object.

    This entry point will register the Javascript function and then use it on the javascript side using the parameters
    passed in this function. Some basic controls are done on the Python side during the transpilation

    Example

    :param y_columns: A python list with the columns in the records
    :param profile: A boolean flag to activate the framework profiling

    :return:
    """
    if not isinstance(y_columns, list):
      y_columns = [y_columns]
    fnc_name = JsPlotlyBox.__name__
    self.__register_records_fnc(fnc_name, JsPlotlyBox.content, list(JsPlotlyBox.pmts), profile | self.profile)
    self._data_schema['out'] = "%s(%%s, %s)" % (fnc_name, y_columns)

  def h_box(self, y_columns, profile=False):
    """
    Data Conversion to a Plotly Horizontal Box chart object.

    This entry point will register the Javascript function and then use it on the javascript side using the parameters
    passed in this function. Some basic controls are done on the Python side during the transpilation

    Example

    :param y_columns: A python list with the columns in the records
    :param profile: A boolean flag to activate the framework profiling

    :return:
    """
    if not isinstance(y_columns, list):
      y_columns = [y_columns]
    fnc_name = JsPlotlyHBox.__name__
    self.__register_records_fnc(fnc_name, JsPlotlyHBox.content, list(JsPlotlyHBox.pmts), profile | self.profile)
    self._data_schema['out'] = "%s(%%s, %s)" % (fnc_name, y_columns)

  def h_bar(self, y_columns, profile=False):
    """
    Data Conversion to a Plotly Horizontal Bar chart object.

    This entry point will register the Javascript function and then use it on the javascript side using the parameters
    passed in this function. Some basic controls are done on the Python side during the transpilation

    Example

    :param y_columns: A python list with the columns in the records
    :param profile: A boolean flag to activate the framework profiling

    :return:
    """
    if not isinstance(y_columns, list):
      y_columns = [y_columns]
    fnc_name = JsPlotlyHBar.__name__
    self.__register_records_fnc(fnc_name, JsPlotlyHBar.content, list(JsPlotlyHBar.pmts), profile | self.profile)
    self._data_schema['out'] = "%s(%%s, %s)" % (fnc_name, y_columns)

  def surface(self, y_columns, x_axis, z_axis, profile=False):
    """
    Data Conversion to a Plotly Surface chart object.

    This entry point will register the Javascript function and then use it on the javascript side using the parameters
    passed in this function. Some basic controls are done on the Python side during the transpilation

    Example

    :param y_columns: A python list with the columns in the records
    :param x_axis: A string with a column name from the records
    :param z_axis: A string with a column name from the records
    :param profile: A boolean flag to activate the framework profiling

    :return:
    """
    if not isinstance(y_columns, list):
      y_columns = [y_columns]
    fnc_name = JsPlotlySurface.__name__
    x_axis = JsUtils.jsConvertData(x_axis, None)
    self.__register_records_fnc(fnc_name, JsPlotlySurface.content, list(JsPlotlySurface.pmts), profile | self.profile)
    self._data_schema['out'] = "%s(%%s, %s, %s, %s)" % (fnc_name, y_columns, x_axis, JsUtils.jsConvertData(z_axis, None))

  def parcoords(self, y_columns, x_axis, profile=False):
    """
    Data Conversion to a Plotly ParCoordinate chart object.

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
    fnc_name = JsPlotlyParCoordinates.__name__
    x_axis = JsUtils.jsConvertData(x_axis, None)
    self.__register_records_fnc(fnc_name, JsPlotlyParCoordinates.content, list(JsPlotlyParCoordinates.pmts), profile | self.profile)
    self._data_schema['out'] = "%s(%%s, %s, %s)" % (fnc_name, y_columns, x_axis)


# --------------------------------------------------------------------------------------------------------------------
#                               DATA TRANSFORMATION JAVASCRIPT DEFINITION
# --------------------------------------------------------------------------------------------------------------------
class JsPlotlyPie(object):
  pmts = ("seriesNames", "xAxis")
  content = '''
    var temp = {}; var labels = {};
    data.forEach(function(rec){ 
      if (!(rec[xAxis] in temp)){temp[rec[xAxis]] = {}};
      seriesNames.forEach(function(name){
        labels[name] = true; if(rec[name] !== undefined){
          if(!(name in temp[rec[xAxis]])){temp[rec[xAxis]][name] = rec[name]} else {temp[rec[xAxis]][name] += rec[name]}}})
    });
    result = [{labels: [], values: []}]; var labels = Object.keys(labels);
    for(var series in temp){
      labels.forEach(function(label){if(temp[series][label] !== undefined){
        result[0].labels.push(series); result[0].values.push(temp[series][label])}})}
    '''


class JsPlotly(object):
  pmts = ("seriesNames", "xAxis")
  content = '''
    var temp = {}; var labels = []; var uniqLabels = {};
    seriesNames.forEach(function(series){temp[series] = {}});
    data.forEach(function(rec){ 
      seriesNames.forEach(function(name){
        if(rec[name] !== undefined){
          if(!(rec[xAxis] in uniqLabels)){labels.push(rec[xAxis]); uniqLabels[rec[xAxis]] = true};
          temp[name][rec[xAxis]] = rec[name]}})});
    seriesNames.forEach(function(series){
      dataSet = {x: [], y: [], name: series};
      labels.forEach(function(x, i){
        dataSet.x.push(x);
        if(temp[series][x] == undefined){dataSet.y.push(null)} else{dataSet.y.push(temp[series][x])}
      }); result.push(dataSet)})
    '''


class JsPlotlyScatter(object):
  pmts = ("seriesNames", "xAxis")
  content = '''
    var temp = {}; var labels = [];
    seriesNames.forEach(function(series){temp[series] = {x: [], y: [], name: series}});
    data.forEach(function(rec){ 
      seriesNames.forEach(function(name){
        if(rec[name] !== undefined){temp[name].x.push(rec[xAxis]); temp[name].y.push(rec[name])}})});
    seriesNames.forEach(function(series){result.push(temp[series])})
    '''


class JsPlotlyBox(object):
  pmts = ("seriesNames", )
  content = '''
    var temp = {}; seriesNames.forEach(function(name){temp[name] = []});
    data.forEach(function(rec){ 
      seriesNames.forEach(function(name){if (rec[name] !== undefined){temp[name].push(rec[name])}})}); 
    for(var name in temp){result.push({type: 'box', name: name, y: temp[name]})}
    '''


class JsPlotlyHBox(object):
  pmts = ("seriesNames", )
  content = '''
    var temp = {}; seriesNames.forEach(function(name){temp[name] = []});
    data.forEach(function(rec){ 
      seriesNames.forEach(function(name){if(rec[name] !== undefined){temp[name].push(rec[name])}})}); 
    for(var name in temp){result.push({type: 'box', name: name, x: temp[name]})}
    '''


class JsPlotlySurface(object):
  pmts = ("seriesNames", "xAxis", "zAxis")
  content = '''
    seriesNames.forEach(function(series){
      records = {z: []};
      data.forEach(function(rec){var y = rec[series]; if(y == undefined){y = 0};
         records.z.push([parseFloat(rec[xAxis]), y, rec[zAxis]])})
      result.push(records)})
    '''


class JsPlotlyScatter3D(object):
  """
  Convert the recordset to a Plotly object which can be used in 3d surface charts

  Example
  report.chart('surface-contours', df1, seriesNames=['col2'], xAxis='col4', otherDims=['col3'])
  report.chart('mesh3d', df1, seriesNames=['col2', 'col3'], xAxis='col4', otherDims=['col5'], height=600)
  """
  alias = "Plotly"
  chartTypes = ['scatter3d', 'mesh3d']
  params = ("seriesNames", "xAxis", "zAxis")
  value = '''
    seriesNames.forEach(function(s){result.push({x: [], y: [], z:[], name: s})});
    data.forEach(function(rec){
      seriesNames.forEach(function(s, i){
        var y = rec[s]; if(y == undefined) {y = 0};
        result[i].x.push(rec[xAxis]); result[i].y.push(y); result[i].z.push(rec[zAxis])})})
    '''


class JsPlotlyHBar(object):
  pmts = ("seriesNames", "xAxis")
  content = '''
    var temp = {}; var labels = {};
    data.forEach(function(rec){ 
      if(!(rec[xAxis] in temp)){temp[rec[xAxis]] = {}};
      seriesNames.forEach(function(name){
        labels[name] = true; if(rec[name] !== undefined){
          if(!(name in temp[rec[xAxis]])){temp[rec[xAxis]][name] = rec[name]}else{temp[rec[xAxis]][name] += rec[name]}}})
    });
    result = []; var labels = Object.keys(labels);
    labels.forEach(function(label){
      dataSet = {x: [], y: [], name: label};
      for(var series in temp){if(temp[series][label] !== undefined){dataSet.x.push(series); dataSet.y.push(temp[series][label])}};
      result.push(dataSet)}) 
    '''


class JsPlotlyMaps(object):
  """
  Transform a recordset to a data structure usable for a Plotly map chart.
  The DataFrame should have the below structure:

    index col2  col5
    0     2     France
    1     5     Russia

  Example
  report.chart('europe', df1, seriesNames=['col2'], xAxis='col5')
  report.chart('choropleth', df1, seriesNames=['col2'], xAxis='col5')
  """
  pmts = ("seriesNames", "xAxis")
  content = '''
    var countries = %(countries)s; var dataSet = {locations:[], z: [], text: [], autocolorscale: true}; var temp = {};
    data.forEach(function(rec){ 
      seriesNames.forEach(function(name){
        if(temp[rec[xAxis]] == undefined){temp[rec[xAxis]] = rec[name]} else{temp[rec[xAxis]] += rec[name]}})});
    countries.forEach(function(country){
      dataSet.locations.push(country); dataSet.text.push(country); 
      if(country in temp){dataSet.z.push(temp[country])} else {dataSet.z.push(0)}});
    result.push(dataSet)
    ''' % {'countries': json.dumps(CTY)}


class JsPlotlyHeatmap(object):
  pmts = ("seriesNames", "xAxis")
  content = '''
    result = [{x: [], y: [], z: []}];
    seriesNames.forEach(function(s){result[0].x.push(s)});
    data.forEach(function(rec){
      result[0].y.push(rec[xAxis]); var zDim = []; seriesNames.forEach(function(s){ zDim.push(rec[s])});
      result[0].z.push(zDim)}) 
    ''' % {'countries': json.dumps(CTY)}


class JsPlotlyParCoordinates(object):
  pmts = ("seriesNames", "xAxis")
  content = '''
    dimensions = []; var counts = [];
    seriesNames.forEach(function(series){dimensions.push({label: series, values: []})});
    data.forEach(function(rec){ 
      counts.push(parseInt(rec[xAxis])); 
      seriesNames.forEach(function(series, i){
        if(rec[series] == undefined){dimensions[i].values.push(0)} else {dimensions[i].values.push(rec[series])}})});
    result = [{dimensions: dimensions, counts: counts}]
    '''
