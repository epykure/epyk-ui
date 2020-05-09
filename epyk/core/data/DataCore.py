
import json

from epyk.core.js import JsUtils
from epyk.core.py import OrderedSet

from epyk.core.js.primitives import JsObjects


class DataAggregators(object):

  def __init__(self,  varName, report=None):
    self.varName = varName
    self._report = report

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
        ''' % (json.dumps(attrs), self.varName, json.dumps(columns)), isPyData=False)

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
        ''' % (json.dumps(attrs), self.varName, json.dumps(columns)), isPyData=False)

  def sumBy(self, columns, keys):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param columns:
    :param keys:
    """
    constructors = self._report._props.setdefault("js", {}).setdefault("constructors", {})
    name = "AggSumBy"
    constructors[name] = '''
      function %s(rs, cs, ks){ var result = {}; 
        fs.forEach(function(r){
          
        })
      } return result; ''' % name
    return JsObjects.JsArray.JsArray('%s(%s, %s, %s)' % (name, self.varName, json.dumps(columns), json.dumps(keys)))


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
       function %s(r, v){if(v.length == 0){return r}; var n=[];r.forEach(function(e){var isValid = true;
           for(const a in v){if(!v[a].includes(e[a])){isValid = false; break}}; if(isValid){n.push(e)}}); return n}''' % name
    self.__filters.add("%s(%%s, %s)" % (name, data))
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

  def toStr(self):
    """
    Description:
    -----------

    """
    result = "%s"
    for rec in self.__filters[::-1]:
      result %= rec
    return result % self.varName


class DataGlobal(object):

  def __init__(self, varName, data, report=None):
    if data is not None:
      report._props["js"]["datasets"][varName] = json.dumps(data)
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
