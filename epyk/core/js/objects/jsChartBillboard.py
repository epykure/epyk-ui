"""
Module dedicated to perform the data transformation for the Billboard / C3 charts

https://naver.github.io/billboard.js/
https://c3js.org/
"""


class JsBillboard(object):
  """
  Function to convert a recordSet to a valid object for Billboard.
  """
  alias = "Billboard"
  params = ("seriesNames", "xAxis")
  value = '''
    var temp = {}; var labels = []; var uniqLabels = {};
    seriesNames.forEach(function(series){temp[series] = {}});
    data.forEach(function(rec) { 
      seriesNames.forEach(function(name){
        if(rec[name] !== undefined) {
          if (!(rec[xAxis] in uniqLabels)){labels.push(rec[xAxis]); uniqLabels[rec[xAxis]] = true};
          temp[name][rec[xAxis]] = rec[name]}})
    });
    result = [];
    result.push(['x'].concat(labels));
    seriesNames.forEach(function(series){
      dataSet = [series];
      labels.forEach(function(x){
        if (temp[series][x] == undefined) {dataSet.push(null)} else {dataSet.push(temp[series][x])}
      }); result.push(dataSet)}); '''


class JsScatter(object):
  """
  Function to convert a recordSet to a valid object for Billboard scatter charts.

  Example

  """
  alias = "Billboard"
  chartTypes = ['scatter']
  params = ("seriesNames", "xAxis")
  value = '''
      var tempVal = {}; var tempX = {}; var labels = []; 
      seriesNames.forEach(function(series){tempVal[series] = []; tempX[series +"_x"] = []}) ;
      data.forEach(function(rec) { 
        seriesNames.forEach(function(name){
          if(rec[name] !== undefined) {
            if (!(rec[xAxis] in tempVal[name])){ tempVal[name] = [name, rec[name]]; tempX[name +"_x"] = [name +"_x", rec[xAxis]] }
            else {tempVal[name].push(rec[name]); tempX[name +"_x"].push(rec[xAxis]) } }})
      });
      result = {'columns': [], 'xs': {}};
      seriesNames.forEach(function(series){
        result.columns.push(tempVal[series]);
        result.columns.push(tempX[series +"_x"]);
        result.xs[series] = series +"_x"
      })'''


class JsC3Pie(object):
  """
  Function to convert a recordSet to a valid object for Billboard pie charts.

  """
  alias = "Billboard"
  chartTypes = ['pie', 'donut']
  params = ("seriesNames", "xAxis")
  value = '''
    var temp = {} ; var labels = {};
    data.forEach(function(rec) { 
      if (!(rec[xAxis] in temp)) {temp[rec[xAxis]] = {}};
      seriesNames.forEach(function(name){
        labels[name] = true; if(rec[name] !== undefined) {if (!(name in temp[rec[xAxis]])) {temp[rec[xAxis]][name] = rec[name]} else {temp[rec[xAxis]][name] += rec[name]}}  }) ;
    });
    result = [];
    result.push(['x'].concat(labels));
    var labels = Object.keys(labels);
    for(var series in temp){
      var values = [series];
      labels.forEach(function(label) {
        if(temp[series][label] !== undefined ) { values.push(temp[series][label]) } else { values.push(null) }});
      result.push(values);};
    '''


class JsC3(object):
  """
  Function to convert a recordSet to a valid object for C3.
  """
  alias = "C3"
  params = ("seriesNames", "xAxis")
  value = '''
    var temp = {}; var labels = []; var uniqLabels = {};
    seriesNames.forEach(function(series){temp[series] = {}}) ;
    data.forEach(function(rec) { 
      seriesNames.forEach(function(name){
        if(rec[name] !== undefined) {
          if (!(rec[xAxis] in uniqLabels)){labels.push(rec[xAxis]); uniqLabels[rec[xAxis]] = true};
          temp[name][rec[xAxis]] = rec[name]}})
    });
    result = [];
    result.push(['x'].concat(labels));
    seriesNames.forEach(function(series){
      dataSet = [series];
      labels.forEach(function(x){
        if (temp[series][x] == undefined) {dataSet.push(null)} else {dataSet.push(temp[series][x])}
      }); result.push(dataSet)}); '''
