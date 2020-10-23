#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

from epyk.core.js import JsUtils
from epyk.core.py import OrderedSet

from epyk.core.js.primitives import JsObjects


class DataAggregators(object):

  def __init__(self,  varName, report=None):
    self.varName = varName
    self._report = report

  def max(self, column):
    """
    Description:
    -----------
    Returns the maximum value in list. If an iteratee function is provided, it will be used on each value to generate the criterion by which the value is ranked.
    -Infinity is returned if list is empty, so an isEmpty guard may be required. Non-numerical values in list will be ignored.

    Related Pages:

      https://underscorejs.org/#max

    Attributes:
    ----------
    :param column:
    """
    self._report.jsImports.add('underscore')
    return JsObjects.JsArray.JsArray("[_.max(%s, function(rec){return rec['%s']; })]" % (self.varName, column), report=self._report)

  def min(self, column):
    """
    Description:
    -----------
    Returns the minimum value in list. If an iteratee function is provided, it will be used on each value to generate the criterion by which the value is ranked.
    Infinity is returned if list is empty, so an isEmpty guard may be required. Non-numerical values in list will be ignored.

    Related Pages:

      https://underscorejs.org/#min

    Attributes:
    ----------
    :param column:
    """
    self._report.jsImports.add('underscore')
    return JsObjects.JsArray.JsArray("[_.min(%s, function(rec){ return rec['%s']; })]" % (self.varName, column), report=self._report)

  def sortBy(self, column):
    """
    Description:
    ------------
    Returns a (stably) sorted copy of list, ranked in ascending order by the results of running each value through iteratee.
    iteratee may also be the string name of the property to sort by (eg. length).

    Attributes:
    ----------
    :param column:
    """
    self._report.jsImports.add('underscore')
    column = JsUtils.jsConvertData(column, None)
    return JsObjects.JsArray.JsArray("_.sortBy(%s, %s)" % (self.varName, column), report=self._report)

  def sum(self, columns, attrs=None):
    """
    Description:
    -----------
    Reduce the record set by adding all the columns

    Attributes:
    ----------
    :param columns: List. The columns in the recordset to be counted
    :param attrs: Dictionary. The static values to be added to the final recordset
    """
    return JsObjects.JsArray.JsArray('''
       (function(r, cs){ var result = {}; cs.forEach(function(c){result[c] = 0});
        r.forEach(function(v){cs.forEach(function(c){ if(typeof v[c] !== 'undefined'){ result[c] += v[c]}})
        }); var attrs = %s; if(attrs){for(var attr in attrs){result[attr] = attrs[attr]}}; return [result]})(%s, %s)
        ''' % (json.dumps(attrs), self.varName, json.dumps(columns)), isPyData=False, report=self._report)

  def count(self, columns, attrs=None):
    """
    Description:
    -----------
    Reduce the record set by counting all the columns

    Attributes:
    ----------
    :param columns: List. The columns in the recordset to be counted
    :param attrs: Dictionary. The static values to be added to the final recordset
    """
    return JsObjects.JsArray.JsArray('''
       (function(r, cs){ var result = {}; cs.forEach(function(c){result[c] = 0});
        r.forEach(function(v){cs.forEach(function(c){ if(typeof v[c] !== 'undefined'){ result[c] += 1}})
        }); var attrs = %s; if(attrs){for(var attr in attrs){result[attr] = attrs[attr]}}; return [result]})(%s, %s)
        ''' % (json.dumps(attrs), self.varName, json.dumps(columns)), isPyData=False, report=self._report)

  def sumBy(self, columns, keys, dstKey=None, cast_vals=False):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param columns:
    :param keys:
    :param dstKey:
    :param cast_vals:
    """
    constructors = self._report._props.setdefault("js", {}).setdefault("constructors", {})
    keys = JsUtils.jsConvertData(keys, None)
    dstKey = JsUtils.jsConvertData(dstKey, None)
    columns = JsUtils.jsConvertData(columns, None)
    name = "AggSumBy"
    constructors[name] = '''
      function %s(rs, cs, sks, dk){var result = []; var tmpResults = {}; if(sks == ''){return rs}; var rdk = dk === null ? sks :  dk;
        if (!Array.isArray(sks)) {sks = [sks]}
        rs.forEach(function(r){
          var sk = []; sks.forEach(function(s){sk.push(r[s])}); var skKey = sk.join('#');
          if (!(skKey in tmpResults)){tmpResults[skKey] = {}; sks.forEach(function(s){tmpResults[skKey][s] = r[s]})
             cs.forEach(function(c){tmpResults[skKey][c] = 0})}
          cs.forEach(function(c){tmpResults[skKey][c] += %s})
        }); for(const v in tmpResults){result.push(tmpResults[v])}; return result}''' % (name, "parseFloat(r[c])" if cast_vals else 'r[c]')
    return JsObjects.JsArray.JsArray('%s(%s, %s, %s, %s)' % (name, self.varName, columns, keys, dstKey), report=self._report)

  def pluck(self, column):
    """
    Description:
    -----------
    A convenient version of what is perhaps the most common use-case for map: extracting a list of property values.

    Related Pages:

      https://underscorejs.org/#pluck
    """
    self._report.jsImports.add('underscore')
    column = JsUtils.jsConvertData(column, None)
    return JsObjects.JsArray.JsArray("_.pluck(%s, %s)" % (self.varName, column), report=self._report)


class DataFilters(object):

  def __init__(self,  varName, filter_map, report=None):
    self.varName, self.__filters = varName, OrderedSet()
    self._report, self.filter_map = report, filter_map

  def setFilter(self, name):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param name:
    """
    self.filter_map[name] = self.toStr()
    return JsObjects.JsVoid("const %s = %s" % (name, self.filter_map[name]))

  def match(self, data, case_sensitive=True):
    """
    Description:
    -----------
    Filtering rule based on a Dictionary of lists

    Attributes:
    ----------
    :param data: Dictionary. The keys, values to be filtered
    :param case_sensitive: Boolean. To make sure algorithm case sensitive
    """
    constructors = self._report._props.setdefault("js", {}).setdefault("constructors", {})
    data = JsUtils.jsConvertData(data, None)
    name = "filterMatch"
    constructors[name] = '''
       function %s(r, v){if(typeof r === 'undefined'){ return []}; if(v.length == 0){return r}; var n=[];r.forEach(function(e){var isValid = true;
           for(const a in v){if(!v[a].includes(e[a])){isValid = false; break}}; if(isValid){n.push(e)}}); return n}''' % name
    self.__filters.add("%s(%%s, %s)" % (name, data))
    return self

  def any(self, value, keys=None):
    """
    Description:
    -----------
    Check if any value in the record match the value.
    This is not case sensitive.

    TODO: improve the performances by filtering on a list of keys if passed

    Attributes:
    ----------
    :param value:
    :param keys:
    """
    constructors = self._report._props.setdefault("js", {}).setdefault("constructors", {})
    value = JsUtils.jsConvertData(value, None)
    keys = JsUtils.jsConvertData(keys, None)
    name = "AnyMatch"
    constructors[
      name] = "function %s(r, v, ks){if (v == ''){return r}; v = v.toUpperCase(); var n=[];r.forEach(function(e){ for(const k in e){ if(String(e[k]).toUpperCase().includes(v)){n.push(e); break;} } });return n}" % name

    self.__filters.add("%s(%%s, %s, %s)" % (name, value, keys))
    return self

  def equal(self, key, value, case_sensitive=True):
    """
    Description:
    -----------
    Filtering rule based on a key, value

    Attributes:
    ----------
    :param key: String, The key in the various records
    :param value: Object. The value to keep
    :param case_sensitive: Boolean. To make sure algorithm case sensitive
    """
    constructors = self._report._props.setdefault("js", {}).setdefault("constructors", {})
    key = JsUtils.jsConvertData(key, None)
    value = JsUtils.jsConvertData(value, None)
    if not case_sensitive:
      name = "filterEqualUpper"
      constructors[name] = "function %s(r, k, v){if (v == ''){return r}; var n=[];v = v.toUpperCase(); r.forEach(function(e){if(e[k].toUpperCase()==v){n.push(e)}});return n}" % name
    else:
      name = "filterEqual"
      constructors[name] = "function %s(r, k, v){if (v == ''){return r}; var n=[];r.forEach(function(e){if(e[k]==v){n.push(e)}});return n}" % name
    self.__filters.add("%s(%%s, %s, %s)" % (name, key, value))
    return self

  def includes(self, key, values, case_sensitive=True, empty_all=True):
    """
    Description:
    -----------
    Filtering rule based on a key, list of values

    Attributes:
    ----------
    :param key: String, The key in the various records
    :param values: List . The list of values to keep
    :param case_sensitive: Boolean. To make sure algorithm case sensitive
    :param empty_all: Boolean. To specify how to consider the empty case
    """
    constructors = self._report._props.setdefault("js", {}).setdefault("constructors", {})
    key = JsUtils.jsConvertData(key, None)
    value = JsUtils.jsConvertData(values, None)
    if not case_sensitive:
      name = "filterContainUpper"
      constructors[name] = '''function %s(r, k, v){if (v.length == 0){if(%s){return r} else {return []}}; 
          var vUp = []; v.forEach(function(t){vUp.push(t.toUpperCase())}); 
          var n=[];r.forEach(function(e){if(vUp.includes(e[k].toUpperCase())){n.push(e)}});return n}''' % (name, json.dumps(empty_all))
    else:
      name = "filterContain"
      constructors[name] = "function %s(r, k, v){if (v.length == 0){if(%s){return r} else {return []}}; var n=[];r.forEach(function(e){if(v.includes(e[k])){n.push(e)}});return n}" % (name, json.dumps(empty_all))
    self.__filters.add("%s(%%s, %s, %s)" % (name, key, value))
    return self

  def startswith(self, key, value):
    """
    Description:
    -----------
    Filtering rule based on a key, and a value starting with a specific format

    Attributes:
    ----------
    :param key: String, The key in the various records
    :param value: String . The list of values to keep
    """
    name = "filterStartsWith"
    key = JsUtils.jsConvertData(key, None)
    value = JsUtils.jsConvertData(value, None)
    constructors = self._report._props.setdefault("js", {}).setdefault("constructors", {})
    constructors[name] = "function %s(r, k, v){var n=[];r.forEach(function(e){if(e[k].startsWith(v)){n.push(e)}});return n}" % name
    self.__filters.add("%s(%%s, %s, %s)" % (name, key, value))
    return self

  def sup(self, key, value, strict=True):
    """
    Description:
    -----------
    Filter values below a certain value

    Attributes:
    ----------
    :param key: String, The key in the various records
    :param value: Number. The threshold
    :param strict: Boolean. Include threshold
    """
    key = JsUtils.jsConvertData(key, None)
    value = JsUtils.jsConvertData(value, None)
    constructors = self._report._props.setdefault("js", {}).setdefault("constructors", {})
    if strict:
      name = "filterSup"
      constructors[name] = "function %s(r, k, v){var n=[];r.forEach(function(e){if(e[k] > v){n.push(e)}});return n}" % name
    else:
      name = "filterSupEq"
      constructors[name] = "function %s(r, k, v){var n=[];r.forEach(function(e){if(e[k] >= v){n.push(e)}});return n}" % name
    self.__filters.add("%s(%%s, %s, %s)" % (name, key, value))
    return self

  def inf(self, key, value, strict=True):
    """
    Description:
    -----------
    Filter values above a certain value

    Attributes:
    ----------
    :param key: String, The key in the various records
    :param value: Number. The threshold
    :param strict: Boolean. Include threshold
    """
    key = JsUtils.jsConvertData(key, None)
    value = JsUtils.jsConvertData(value, None)
    constructors = self._report._props.setdefault("js", {}).setdefault("constructors", {})
    if strict:
      name = "filterInf"
      constructors[name] = "function %s(r, k, v){var n=[];r.forEach(function(e){if(e[k] < v){n.push(e)}});return n}" % name
    else:
      name = "filterInfEq"
      constructors[name] = "function %s(r, k, v){var n=[];r.forEach(function(e){if(e[k] <= v){n.push(e)}});return n}" % name
    self.__filters.add("%s(%%s, %s, %s)" % (name, key, value))
    return self

  def group(self):
    """
    Description:
    -----------

    """
    return DataAggregators(self.toStr(), self._report)

  def sortBy(self, column):
    """
    Returns a (stably) sorted copy of list, ranked in ascending order by the results of running each value through iteratee.
    iteratee may also be the string name of the property to sort by (eg. length).

    Related Pages:

      https://underscorejs.org/#sortBy

    Attributes:
    ----------
    :param column:
    """
    self._report.jsImports.add('underscore')
    column = JsUtils.jsConvertData(column, None)
    self.__filters.add("_.sortBy(%%s, %s)" % column)
    return self

  def toStr(self):
    result = "%s"
    for rec in self.__filters[::-1]:
      result %= rec
    return result % self.varName


class DataGlobal(object):

  def __init__(self, varName, data, report=None):
    if data is not None:
      report._props["js"]["datasets"][varName] = "var %s = %s" % (varName, json.dumps(data))
    self._data, self.__filters_groups, self._report, self.varName = data, {}, report, varName
    self.__filter_saved = {}

  def getFilter(self, name, groupName=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param name:
    :param groupName:
    """
    if groupName is None:
      saved_filter = None
      for k, v in self.__filter_saved.items():
        if name in v:
          saved_filter = v
          break

    else:
      if name not in self.__filter_saved[groupName]:
        raise Exception("")

      saved_filter = self.__filter_saved[groupName]
    return DataFilters(name, saved_filter, self._report)

  def clearFilter(self, name, groupName=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param name:
    :param groupName:
    """
    if groupName is None:
      for k, v in self.__filter_saved.items():
        if name in v:
          del v[name]

    else:
      del self.__filter_saved[groupName][name]

    return self

  def filterGroup(self, groupName):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param groupName: String. The filter name
    """
    if not groupName in self.__filters_groups:
      self.__filter_saved[groupName] = {}
      self.__filters_groups[groupName] = DataFilters(self.varName, self.__filter_saved[groupName], self._report)
    return self.__filters_groups[groupName]

  def cleafFilterGroup(self, groupName):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param groupName: String. The filter name
    """
    if not groupName in self.__filters_groups:
      del self.__filters_groups[groupName]

    return self

  def clearFilters(self):
    """
    Description:
    -----------
    Remove all the filters
    """
    self.__filters_groups = {}
    return self


class ServerNameSpaceConfig(object):
  def __init__(self, config, name, alias, endPoints):
    self.__config, self.end_points, self.name, self.alias = config, {}, name, alias
    if endPoints is not None:
      self.endPoints(endPoints)

  @property
  def address(self):
    """
    Description:
    ------------

    Attributes:
    ----------

    """
    return JsObjects.JsObject.JsObject.get(self.__config.varId)[self.alias]['u']

  def endPoint(self, name):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param name:
    """
    self.end_points[name] = "http://%s:%s/%s/%s" % (self.__config.hostname, self.name, self.__config.port, name)
    return self

  def endPoints(self, names):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param names:
    """
    for name in names:
      self.endPoint(name)
    return self


class ServerConfig(object):

  def __init__(self, hostname, port, report=None):
    self.varId = "server_config_%s" % id(self)
    report._props["js"]["configs"][self.varId] = self
    self.__namespaces, self.__end_points, self.host, self.port = {}, {}, hostname, port

  def getNamespace(self, alias):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param alias:
    """
    return self.__namespaces[alias]

  def addNamespace(self, name, alias=None, endPoints=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param name:
    :param alias:
    :param endPoints:
    """
    if alias is None:
      alias = name
    self.__namespaces[alias] = ServerNameSpaceConfig(self, name, alias, endPoints)
    return self

  def endPoint(self, name):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param name:
    """
    self.__end_points[name] = "http://%s:%s/%s" % (self.host, self.port, name)
    return self

  def endPoints(self, names):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param names:
    """
    for name in names:
      self.__end_points[name] = "http://%s:%s/%s" % (self.host, self.port, name)
    return self

  def get(self, name):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param name:
    """
    if not name in self.__end_points:
      raise Exception("Missing end point in the server configuration - %s" % name)

    return JsObjects.JsObject.JsObject.get(self.varId)[name]

  def toStr(self):
    for np, np_val in self.__namespaces.items():
      self.__end_points[np] = {'e': np_val.end_points, 'n': np_val.name, 'u': "http://%s:%s/%s" % (self.host, self.port, np_val.name)}
    return "var %s = %s" % (self.varId, JsUtils.jsConvertData(self.__end_points, None))

  def __str__(self):
    return self.toStr()
