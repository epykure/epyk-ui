"""
This module get all the functions related to the transformation of the recordset on the Javascript part.
Each of those functions are in charge of transforming a recordSet in the front end (which means that this cannot be
seen on the Python side in the scripting interface). The best way to test those changes is to use a report and set
the DEBUG flag.
"""

from abc import ABC, abstractmethod


class JsRecFunc(ABC):
  """
  This class cannot be used directly to format a record as the mandatory parameters are not defined and are set to None.

  Anyway as an interface this will give you the different information which have to be defined to create a new
  js function.

  The objective in this logic is to centralise all the js functions used in the front end in this folder in order
  to limit the use and standardise the implementation.

  ## The main parameters ##

  - alias, The alias name used in the Python layer to point to this function
  - params, The parameters name available in the Javascript function (data is always passed)
  - value, The content of the function.

  ## Javascript function ##

  A javascript function, represented as a class in the framework, is always trying to transform a data variable
  which is defined as a recordSet to a result variable which should be also a recordSet. The purpose of having this
  will ensure that functions can:

    1. Transform the recordSet in a specific manner
    2. Be shared in the different components
    3. Be put together sum(count(...))

  """
  alias = None
  params = None
  value = None

  @staticmethod
  def extendArgs(category, originParams, newCols):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param category:
    :param originParams:
    :param newCols:
    """
    return originParams

  @staticmethod
  @abstractmethod
  def extendColumns(jsSchema, params):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param jsSchema:
    :param params:
    """
    pass


class JsRowBuckets(JsRecFunc):

  @staticmethod
  def extendArgs(category, originParams, newCols):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param category:
    :param originParams:
    :param newCols:
    """
    originParams[1] += newCols
    return originParams

  @staticmethod
  def extendColumns(jsSchema, params):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param jsSchema:
    :param params:
    """

  alias = "row-buckets"
  params = ("allGroups", "seriesNames")
  value = '''
    var groupRowsIds = {}; var groupRows = {};
    data.forEach(function(rec, i){
      var inBuckets = {}; for(var g in allGroups){inBuckets[g] = null};
      for(var g in allGroups){
        for(var col in allGroups[g]){if(allGroups[g][col].indexOf(rec[col]) >= 0){
          inBuckets[g] = true} else {inBuckets[g] = false; break}}}
      for(var g in inBuckets){
        if (inBuckets[g]) { 
            if (g in groupRowsIds) {groupRowsIds[g].push(i);groupRows[g].push(rec)} 
            else {groupRowsIds[g] = [i]; groupRows[g] = [rec]}}
      }; result.push(rec)});
      
    for(var g in groupRows){
      var row = {'_system': true}; var text = g;
      for(var col in allGroups[g]){row[col] = text; text=''}; seriesNames.forEach(function(v){row[v] = 0}); 
      groupRows[g].forEach(function(rec){ seriesNames.forEach(function(v){row[v] += rec[v]})});
      result.push(row)}'''


class JsRowTotal(JsRecFunc):

  @staticmethod
  def extendArgs(category, originParams, newCols):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param category:
    :param originParams:
    :param newCols:
    """
    originParams[0] += newCols
    return originParams

  @staticmethod
  def extendColumns(jsSchema, params):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param jsSchema:
    :param params:
    """

  alias = "row-total"
  params = ("seriesNames", "rowDefinition")
  value = '''
    seriesNames.forEach(function(v){rowDefinition[v] = 0});
    data.forEach(function(rec){
      if(!rec['_system']){seriesNames.forEach(function(v){rowDefinition[v] += rec[v]})};
      result.push(rec);
    }); result.push(rowDefinition);
    '''


class JsAll(JsRecFunc):
  @staticmethod
  def extendColumns(jsSchema, params):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param jsSchema:
    :param params:
    """
    if params[0] is not None and params[1] is not None:
      jsSchema['keys'] |= set(params[0])
      jsSchema['values'] |= set(params[1])

  alias = "all"
  params = ("keys", "values")
  value = 'result = data'


class JsSum(JsRecFunc):

  @staticmethod
  def extendColumns(jsSchema, params):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param jsSchema:
    :param params:
    """
    if params[0] is not None and params[1] is not None:
      jsSchema['keys'] |= set(params[0])
      jsSchema['values'] |= set(params[1])

  alias = "sum"
  params = ("keys", "values", "xOrder")
  value = '''
    if ((keys == null) || (values == null)){result = data}
    else{
      var temp = {}; var order = []; 
      if (Array.isArray(data)){
        data.forEach( function(rec){ 
          var aggKey = []; keys.forEach(function(k){ aggKey.push(rec[k])}); 
          var newKey = aggKey.join("#"); if (!(newKey in temp)) {order.push(newKey)};
          if (!(newKey in temp)) {temp[newKey] = {}};
          values.forEach(function(v) {if (!(v in temp[newKey])) {temp[newKey][v] = rec[v]} else {temp[newKey][v] += rec[v]}})})}; 
      if(Array.isArray(xOrder)){order = xOrder};
      order.forEach(function(label) {
        var rec = {}; var splitKey = label.split("#");
        keys.forEach(function(k, i) {rec[k] = splitKey[i];});
        for(var v in temp[label]) {rec[v] = temp[label][v]};
        result.push(rec)})}'''


class JsPercentage(JsRecFunc):

  @staticmethod
  def extendColumns(jsSchema, params):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param jsSchema:
    :param params:
    """
    if params[0] is not None and params[1] is not None:
      jsSchema['keys'] |= set(params[0])
      jsSchema['values'] |= set(params[1])

  alias = "percentage"
  params = ("keys", "values")
  value = ''' 
    if ((keys == null) || (values == null)){result = data}
    else{
      var temp = {}; var order = []; var sumPerSeries = {};
      data.forEach( function(rec) { 
        var aggKey = []; keys.forEach(function(k){ aggKey.push(rec[k])}); 
        var newKey = aggKey.join("#"); if (!(newKey in temp)) {order.push(newKey)};
        if (!(newKey in temp)) {temp[newKey] = {}};
        values.forEach(function(v) {
          if (!(v in sumPerSeries)) {sumPerSeries[v] = rec[v]} else {sumPerSeries[v] += rec[v]};
          if (!(v in temp[newKey])) {temp[newKey][v] = rec[v]} 
          else {temp[newKey][v] += rec[v]}})});
      order.forEach(function(label) {
        var rec = {}; var splitKey = label.split("#");
        keys.forEach(function(k, i) {rec[k] = splitKey[i]});
        for(var v in temp[label]) {rec[v] = 100 * (temp[label][v] / sumPerSeries[v])};
        result.push(rec)})}'''


class JsOperations(JsRecFunc):
  """
  This function will aggregate the different values for each series according to a shcema defined in a Python
  dictionary in the last position of the tuple.

  Usage::

    aggFnc=('aggregation', ['direction'], values, {'dn': 'sum', 'Date': 'count'}),
  """

  @staticmethod
  def extendArgs(category, originParams, newCols):
    """
    Description:
    ------------
    This function will update the function argument according to the mode defined by the user. Indeed some properties
    can be received to validate the accuracy of the data.
    Those data should be added to the different transformation functions and the columns should be passed to the final
    object.
    This function will ensure that by activating the mode the columns will be automatically added to the aggregated data.

    :return: The update set of columns to be considered in the Javascript function
    """
    if category == 'age':
      originParams[1] = originParams[1] + newCols
      for c in newCols:
        originParams[2][c] = 'sum'
    return originParams

  @staticmethod
  def extendColumns(jsSchema, params):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param jsSchema:
    :param params:
    """
    if params[0] is not None and params[1] is not None:
      jsSchema['keys'] |= set(params[0])
      jsSchema['values'] |= set(params[1])

  alias = "aggregation"
  params = ("keys", "values", "operations")
  value = '''
    var temp = {};
    var order = [];
    data.forEach( function(rec) { 
      var aggKey = []; keys.forEach(function(k){ aggKey.push( rec[k])}); var newKey = aggKey.join("#"); order.push(newKey);
      if (!(newKey in temp)) {temp[newKey] = {}};
      values.forEach(function(v) {
        if (operations[v] === undefined){ if (!(v in temp[newKey])) {temp[newKey][v] = 1} else {temp[newKey][v] += 1} }
        else if (operations[v] == 'sum') {if (!(v in temp[newKey])) {temp[newKey][v] = rec[v]} else {temp[newKey][v] += rec[v]}}
        else if (operations[v] == 'count') {if (!(v in temp[newKey])) {temp[newKey][v] = 1} else {temp[newKey][v] += 1}}
      })}); 
    order.forEach(function(label) {
      var rec = {}; var splitKey = label.split("#");
      keys.forEach(function(k, i) {rec[k] = splitKey[i];});
      for(var v in temp[label]) {rec[v] = temp[label][v]};
      result.push(rec)})'''


class JsCount(JsRecFunc):
  params = ("keys", "values")
  value = '''
    var temp = {}; var order = [];
    data.forEach(function(rec){ 
      var aggKey = []; keys.forEach(function(k){aggKey.push(rec[k])}); var newKey = aggKey.join("#"); 
      if(!(newKey in temp)){order.push(newKey); temp[newKey] = {}};
      values.forEach(function(v){if (!(v in temp[newKey])){
        temp[newKey][v] = rec[v]; temp[newKey][v +"_count"] = 1} else{temp[newKey][v +"_count"] += 1}})}); 
    order.forEach(function(label){
      var rec = {}; var splitKey = label.split("#");
      keys.forEach(function(k, i){rec[k] = splitKey[i]});
      for(var v in temp[label]){rec[v] = temp[label][v]};
      result.push(rec)})'''


class JsCountSum(JsRecFunc):
  params = ("keys", "values")
  value = '''
    var temp = {}; var order = [];
    data.forEach(function(rec){ 
      var aggKey = []; keys.forEach(function(k){aggKey.push(rec[k])}); var newKey = aggKey.join("#"); 
      if(!(newKey in temp)){order.push(newKey); temp[newKey] = {}};
      values.forEach(function(v){
        if (!(v in temp[newKey])){
          temp[newKey][v] = rec[v]; temp[newKey][v +"_count"] = 1; temp[newKey][v +"_min"] = rec[v]; 
          temp[newKey][v +"_max"] = rec[v]} 
        else{
          if(rec[v] > temp[newKey][v +"_max"]){temp[newKey][v +"_max"] = rec[v]};
          if(rec[v] < temp[newKey][v +"_min"]){temp[newKey][v +"_min"] = rec[v]};
          temp[newKey][v] += rec[v];temp[newKey][v +"_count"] += 1}})}); 
    order.forEach(function(label){
      var rec = {}; var splitKey = label.split("#");
      keys.forEach(function(k, i){rec[k] = splitKey[i]});
      for(var v in temp[label]){rec[v] = temp[label][v]};
      result.push(rec)})'''


class JsTop:

  @staticmethod
  def extendColumns(jsSchema, params): pass

  alias = "top"
  params = ("countItems", "value", "sortType")
  value = '''
    var tmpRec = {};
    data.forEach(function(rec){
      if(tmpRec[rec[value]] === undefined){ tmpRec[rec[value]] = [rec] } else {tmpRec[rec[value]].push(rec)}});
    
    var result = []; 
    Object.keys(tmpRec).sort().forEach(function(key){
      tmpRec[key].forEach(function(rec){result.push(rec)})});
    
    if (sortType == 'desc'){ result = result.slice(-countItems)}
    else {result = result.slice(0, countItems)}
    '''


class JsCountDistinct:
  """
  Return the distinct counts of element in a list of columns. This function will return a list of dictionaries
  with the following structure {'column': '', 'count_distinct': 0}

  :return: A new recordSet with the properties of the requested keys
  """
  params = ("keys", )
  value = '''
    var temp = {}; keys.forEach(function(k){temp[k] = {}});
    data.forEach(function(rec){keys.forEach(function(k){temp[k][rec[k]] = 1})}); 
    for(var col in temp){
      var dCount = Object.keys(temp[col]).length; 
      result.push({'column': col, 'count': dCount, 'distinct': true, 'values': Object.keys(temp[col])})}'''


class JsCountAll:
  """
  Function to produce KPI on an original recordSet. This function will create a new recordSet based on the selected
  columns of the original data source.

  :return: A new recordSet with the properties of the requested keys
  """
  params = ("keys", )
  value = '''
    var temp = {}; var order= [];
    data.forEach(function(rec){ 
      keys.forEach(function(k){
        var aggKey = k +"#"+ rec[k]; if(!(aggKey in temp)){order.push(aggKey); temp[aggKey] = 1} else{temp[aggKey] += 1}})}); 
    order.forEach(function(label){
      var keys = label.split("#"); var rec = {'column': keys[0], 'value': keys[1], 'count': temp[label], 'distinct': false};
      result.push(rec)})'''


class JsRename:
  """
  Function to remap some columns in the recordSet. The renaming is done based on the input parameter.
  The parameter passed in this function is a dictionary with as keys the existing column names and value the new column.

  :return: The Js recordSet with the new columns in each record. The original keys will be removed
  """
  alias = "rename"
  params = ("colsWithName", )
  value = '''
    data.forEach(function(rec){ 
      for(var col in colsWithName){rec[colsWithName[col]] = rec[col]; delete rec[col]; result.push(rec)}})'''


class JsExtend:
  """
  Function to add some predefined entries to each records in the RecordSet
  The parameter passed in the function call should be a dictionary with as keys the columns to be added to the original record
  and the value {'static': {}, 'dynamic': {}}
  In case of key clashes the values will be replaced.

  :return: A new Js recordSet with the extra columns
  """
  alias = "extend"
  params = ('values', 'recKey')
  value = '''
    if (Array.isArray(data)){
      if(recKey == undefined){
        data.forEach(function(rec, i){ 
          var newRec = Object.assign(rec, values.static);
          if (i in values.dynamic) {newRec = Object.assign(newRec, values.dynamic[i])};
          result.push(newRec)})}
      else{
        data.forEach(function(rec, i){ 
          var newRec = Object.assign(rec, values.static);
          if (i in values.dynamic) {newRec = Object.assign(newRec, values.dynamic[i])};
          result.push(newRec);
          var subValues = rec[recKey]; result[recKey] = [];
          subValues.forEach(function(row, j){ 
            var newRec = Object.assign(row, values.static);
            if (i in values.dynamic) {newRec = Object.assign(newRec, values.dynamic[i])};
            result[recKey].push(newRec)})  
        })
      }} 
    else {result = data}
  '''


class JsExtendDataSet:
  """
  :return: A new Js recordSet with the extra columns in the datasets section
  """
  alias = "extend-dataset"
  params = ("values", 'recKey')
  value = '''
    var records; var recResults; 
    if(recKey == undefined){records = data; recResults = result} 
    else {records = data[recKey];result[recKey] = [];recResults = result[recKey];
      for(var k in data) {if (k != recKey) {result[k] = data[k]}}};
    records.forEach(function(rec, i) { 
      var newRec = Object.assign(rec, values.static);
      if (i in values.dynamic) {newRec = Object.assign(newRec, values.dynamic[i])};
      recResults.push(newRec)})'''


class JsFilter:
  """
  Filter the different records in a recordSet from the definition given as a parameter.
  The filters definition is based on a dictionary as keys the column names. Each records should have the given columns.
  All records which do not match the rules will not be considered

  :return: A new JS dictionary with only the selected lines
  """
  pmts = ("filterCols", )
  content = ''' 
    filters = {};
    filterCols.forEach(function(rec){  
      if (filters[rec['colName']] === undefined){
        filters[rec['colName']] = {val: [], op: rec['op'], allIfEmpty: rec['allIfEmpty']}};
      if(Array.isArray(rec['val'])){ filters[rec['colName']].val = filters[rec['colName']].val.concat(rec['val'])}
      else if (filters[rec['colName']].val.indexOf(rec['val']) < 0) { filters[rec['colName']].val.push(rec['val'])}});
    data.forEach( function(rec) {  
      var isValid = true; 
      for (var col in filters) {
        var opType = filters[col]['op']; 
        if (opType == '='){if(filters[col].val.indexOf(rec[col]) < 0){if ( (filters[col].val != '') && filters[col].allIfEmpty ) {isValid = false; break}}}
        else if (opType == 'in'){ 
          if(filters[col].val.indexOf(rec[col]) < 0){isValid = false; break}
          else if ((filters[col].val.length == 0) && !filters[col].allIfEmpty) {isValid = false; break}}
        else if (opType == 'above'){if(filters[col].val[0] > rec[col]){isValid = false; break}}
        else if (opType == 'below'){if(filters[col].val[0] < rec[col]){isValid = false; break}}
        else if (opType == 'between'){if((filters[col].val[0] > rec[col]) || (filters[col].val[1] < rec[col])){isValid = false; break}}
    }; if (isValid) {result.push(rec)}})'''


class JsIntensity:
  """

  """
  alias = "intensity"
  params = ("cols",)
  value = '''
    stats = {};
    cols.forEach(function(col){stats[col] = {min: null, max: null}});
    data.forEach(function(rec){
      cols.forEach(function(col){
        if((stats[col].max == null) || (rec[col] > stats[col].max) ) { stats[col].max = rec[col]};
        if((stats[col].min == null) || (rec[col] < stats[col].min) ) { stats[col].min = rec[col]}})});
    data.forEach(function(rec){
      cols.forEach(function(col){rec[col + ".intensity.min"] = stats[col].min; rec[col + ".intensity.max"] = stats[col].max});
      result.push(rec)});
    '''

  @staticmethod
  def extendColumns(jsSchema, params):
    """
    Description:
    ------------

    :param jsSchema:
    :param params:
    """


class JsToUrl:
  alias = "dictToUrl"
  value = '''
    var tmpResults = [];
    for(var k in data["pmts"]){tmpResults.push(k +"="+ data["pmts"][k])}; 
    result = tmpResults.join("&");
    if (typeof data["anchor"] !== 'undefined'){result = result +"#"+ data["anchor"]}
    '''
