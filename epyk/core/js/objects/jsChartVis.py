"""
Module dedicated to perform the data transformation for the Vis charts

https://visjs.org/
"""


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
  alias = "Vis"
  params = ("seriesNames", "xAxis", "group")
  value = '''
    var temp = {} ; var labels = {}; var groups = {};
    data.forEach(function(rec) { 
      if (!(rec[xAxis] in temp)) {temp[rec[xAxis]] = {}; groups[rec[xAxis]] = {}};
      seriesNames.forEach(function(name){
        labels[name] = true; if(rec[name] !== undefined) {
          if (!(name in temp[rec[xAxis]])) {temp[rec[xAxis]][name] = rec[name]; if (group !== undefined){groups[rec[xAxis]][name] = rec[group]}} 
          else {temp[rec[xAxis]][name] += rec[name]}}})});
          
    var labels = Object.keys(labels);
    for(var series in temp) {
      labels.forEach(function(label, i) {if(temp[series][label] !== undefined) { 
        var row = {x: series, y: temp[series][label], label: {content: temp[series][label].formatMoney(1, ',', '.') } };
        if (group !== undefined){row['group'] = groups[series][label]} else {row['group'] = i} ;
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
  alias = "Vis"
  chartTypes = ['3D', 'surface', 'bar3d', 'scatter3d', 'line3d', 'bubble']
  params = ("yAxis", "xAxis", "zAxis")
  value = '''
    data.forEach(function(rec, i) { 
      yAxis.forEach(function(s, j){
        result.push({x: parseFloat(rec[xAxis]), y: rec[s], z: rec[zAxis], name: s, style: rec[zAxis]})})
    });
    '''


class JsVisRecords(object):
  """
  :category: Vis Transformer
  :rubric: JS
  :type: Configuration
  :dsc:

  :example: For the Network charts
    c = aresObj.chart('network', df1, chartFamily='Vis', debug=True)
    c.edges([
      {'from': 1, 'to': 3},
      {'from': 1, 'to': 2},
      {'from': 2, 'to': 2},
      {'from': 2, 'to': 3, 'value': 10},
     ])

    This will define a group for the nodes and change the icons
    c.addAttr('user', {'shape': 'icon', 'icon': {'face': 'FontAwesome', 'code': '\uf007', 'size': 50, 'color': '#aa00ff'}}, category='groups')
  """
  alias = "Vis"
  chartTypes = ['timeline', 'network']
  params = ("yAxis", "xAxis")
  value = 'result = data'