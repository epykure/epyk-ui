"""

"""


class JsAggColSum(object):
  """
  Get the result only on the selected column. This function will return a dictionary with the column name and the sum
  """
  alias = "sum(Column)"
  params = ("column", )
  value = '''
    var value = 0;
    data.forEach(function(rec){if(rec[column] !== undefined){value += rec[column]}})
    result = {label: column, value: value}
    '''


class JsAggColStats(object):
  """
  Get the result only on the selected column. This function will return a dictionary with the column name and the sum
  """
  alias = "stats(Column)"
  params = ("column", )
  value = '''
    var value = 0; var countVals = 0;
    data.forEach(function(rec) {if(rec[column] !== undefined){value += rec[column]; countVals ++}})
    result = {label: column, value: value, count: countVals, average: value/countVals}
    '''


