"""
Javascript Aggregators

Those functions will return only 1 record within the recordset.
They are all returning list of records in order to allow function chains
"""


class JsAggColSum(object):
  pmts = ("column", )
  content = '''
    var value = 0;
    data.forEach(function(rec){if(rec[column] !== undefined){value += rec[column]}});
    result = {label: column, value: value}
    '''


class JsAggColMax(object):
  pmts = ("column", )
  content = '''
    var max_val = undefined;
    data.forEach(function(rec){if(rec[column] !== undefined){
      if((max_val == undefined) || (rec[column] > max_val[column])){max_val = rec}}});
    result = [max_val]
    '''


class JsAggColEq(object):
  pmts = ("column", "value")
  content = '''data.forEach(function(rec){if(rec[column] == value){result = [rec]}})'''


class JsAggColMin(object):
  pmts = ("column", )
  content = '''
    var min_val = undefined;
    data.forEach(function(rec){if(rec[column] !== undefined){
      if((min_val == undefined) || (rec[column] < min_val[column])){min_val = rec} }});
    result = [min_val]
    '''


class JsAggColStats(object):
  pmts = ("column", )
  content = '''
    var value = 0; var countVals = 0; var min_val = null; var max_val = null;
    data.forEach(function(rec){
      if(rec[column] !== undefined){value += rec[column]; countVals ++;
      if((min_val == null) || (rec[column] < min_val)){min_val = rec[column]};
      if((max_val == null) || (rec[column] > max_val)){max_val = rec[column]}}});
    result = [{label: column, value: value, count: countVals, average: value/countVals, max: max_val, min: min_val}]
    '''


