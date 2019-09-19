"""
Module dedicated to perform the data transformation for the NVD3 charts
"""


class JsNVD3Pie(object):
  """
  """
  alias = "NVD3"
  chartTypes = ['pie']
  params = ("seriesNames", "xAxis")
  value = '''
    var temp = {}; var labels = {};
    data.forEach(function(rec) { 
      if (!(rec[xAxis] in temp)) {temp[rec[xAxis]] = {}};
      seriesNames.forEach(function(name){
        labels[name] = true; if(rec[name] !== undefined) {if (!(name in temp[rec[xAxis]])) {temp[rec[xAxis]][name] = rec[name]} else {temp[rec[xAxis]][name] += rec[name]}}  }) ;
    });
    var labels = Object.keys(labels); result = [];
    for(var series in temp) {
      var values = {y: 0, x: series};
      labels.forEach(function(label) {
        if(temp[series][label] !== undefined ) { values.y = temp[series][label] }});
      result.push(values)}
    '''


class JsNVD3Bar(object):
  """
  """
  alias = "NVD3"
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
    seriesNames.forEach(function(series){
      dataSet = {key: series, values: [], labels: labels};
      labels.forEach(function(x, i){
        var value = temp[series][x]; 
        if (isNaN(value)) { value = null};
        if (value !== undefined) {dataSet.values.push({y: value, x: i, label: x})}
      }); result.push(dataSet)})
    '''


class JsNVD3Sunburst(object):
  """
  """
  alias = "NVD3"
  chartTypes = ['sunburst']
  params = ("seriesNames", "xAxis")
  value = '''
    var result = [{name: xAxis, children: []}]; var sizeTree = seriesNames.length-1;
    data.forEach(function(rec){
      var path = []; var tmpResultLevel = result[0].children; var branchVal = 0;
      seriesNames.forEach(function(s, i){
        var treeLevel = -1; 
        tmpResultLevel.forEach(function(l, j){if (l.name == rec[s]){treeLevel = j}});
        if (i == sizeTree) {
          if (treeLevel >= 0 ){
            tmpResultLevel[treeLevel].size += rec[xAxis];
          } else{tmpResultLevel.push({name: rec[s], size: rec[xAxis]})}
        }else{
          if (treeLevel < 0 ){
            tmpResultLevel.push({name: rec[s], children: []});
            treeLevel = tmpResultLevel.length - 1};
          tmpResultLevel = tmpResultLevel[treeLevel].children}
      })})'''
