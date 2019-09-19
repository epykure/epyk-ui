"""
Module dedicated to perform the data transformation for the ChartJs charts

https://www.chartjs.org/
"""

class JsChartJs(object):
  """
  """
  alias = "ChartJs"
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
    result = {datasets: [], labels: labels};
    seriesNames.forEach(function(series){
      dataSet = {label: series, data: []};
      labels.forEach(function(x){
        if (temp[series][x] == undefined) {dataSet.data.push(null)} else {dataSet.data.push(temp[series][x])}
      }); result.datasets.push(dataSet)})
    '''


class JsChartJsPie(object):
  """
  """
  alias = "ChartJs"
  chartTypes = ['pie', 'polar']
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
    result = {datasets: [], labels: labels};
    seriesNames.forEach(function(series){
      dataSet = {label: series, data: []};
      labels.forEach(function(x){
        if (temp[series][x] == undefined) {dataSet.data.push(null)} else {dataSet.data.push(temp[series][x])}
      }); result.datasets.push(dataSet)});
    '''


class JsChartJsBubble(object):
  """
  """
  alias = "ChartJs"
  chartTypes = ['bubble']
  params = ("seriesNames", "xAxis", "rDim")
  value = '''
    var temp = {}; var labels = []; var uniqLabels = {};
    seriesNames.forEach(function(series){temp[series] = {}}) ;
    data.forEach(function(rec) { 
      seriesNames.forEach(function(name){
        if(rec[name] !== undefined) {
          if (!(rec[xAxis] in uniqLabels)){labels.push(rec[xAxis]); uniqLabels[rec[xAxis]] = true};
          var r = 5; if ((rDim != undefined) && (rec[rDim] != undefined)){r = rec[rDim]};
          temp[name][rec[xAxis]] = {y: rec[name], r: r} }})
    });
    result = {datasets: [], labels: labels};
    seriesNames.forEach(function(series){
      dataSet = {label: series, data: []};
      labels.forEach(function(x, i){
        if (temp[series][x] == undefined) {dataSet.data.push(null)} 
        else {dataSet.data.push({y: temp[series][x].y, x: x, r: temp[series][x].r})}
      }); result.datasets.push(dataSet)})
    '''


class JsChartJsScatter(object):
  """
  """
  alias = "ChartJs"
  chartTypes = ['scatter']
  params = ("seriesNames", "xAxis", "rDim")
  value = '''
    var temp = {}; var labels = [];
    seriesNames.forEach(function(series){temp[series] = []}) ;
    data.forEach(function(rec) { 
      seriesNames.forEach(function(name){
        if(rec[name] !== undefined) {
          labels.push(rec[xAxis]);
          var r = 2; if ((rDim != undefined) && (rec[rDim] != undefined)){r = rec[rDim]};
          temp[name].push({y: rec[name], x: rec[xAxis], r: r}) }})
    });
    result = {datasets: [], labels: labels};
    seriesNames.forEach(function(series){
      dataSet = {label: series, data: []};
      labels.forEach(function(x, i){
        dataSet.data = temp[series]
      }); result.datasets.push(dataSet)})
    '''
