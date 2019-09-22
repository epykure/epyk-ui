"""
Module dedicated to perform the data transformation for the D3 charts
"""


class JsD3(object):
  """

  """
  alias = "D3"
  value = ''


class JsD3Bubble(object):
  """
  """
  alias = "D3"
  chartTypes = ['gravity']
  params = ("seriesNames", "xAxis")
  value = '''
    nbSeries = seriesNames.length;
    var temp = {};
    var result = [];
    data.forEach(function(rec) {
      for (var key in rec){
        if (key != xAxis && rec[key] != 0 && seriesNames.includes(key))
        { 
          result.push({'Name': rec[xAxis], 'Count': rec[key], 'Category': key, 'nbSeries': nbSeries, 'xAxis': xAxis, 'seriesNames': seriesNames});
        } 
      }
    });
    '''
