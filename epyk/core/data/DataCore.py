
import json

from epyk.core.js import JsUtils
from epyk.core.py import OrderedSet


class DataAggregators(object):
  """

  """

  def sum(self):
    pass

  def count(self):
    pass


class DataFilters(object):

  def __init__(self,  varName, report=None):
    self.varName, self.__filters = varName, OrderedSet()
    self._report = report

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

  def includes(self, key, values, case_sensitive=True):
    """
    Description:
    -----------
    Filtering rule based on a key, list of values

    Attributes:
    ----------
    :param key: String, The key in the various records
    :param values: List . The list of values to keep
    :param case_sensitive: Boolean. To make sure algorithm case sensitive
    """
    constructors = self._report._props.setdefault("js", {}).setdefault("constructors", {})
    key = JsUtils.jsConvertData(key, None)
    value = JsUtils.jsConvertData(values, None)
    if not case_sensitive:
      name = "filterContainUpper"
      constructors[name] = '''function %s(r, k, v){if (v.length == 0){return r}; 
          var vUp = []; v.forEach(function(t){vUp.push(t.toUpperCase())}); 
          var n=[];r.forEach(function(e){if(vUp.includes(e[k].toUpperCase())){n.push(e)}});return n}''' % name
    else:
      name = "filterContain"
      constructors[name] = "function %s(r, k, v){if (v.length == 0){return r}; var n=[];r.forEach(function(e){if(v.includes(e[k])){n.push(e)}});return n}" % name
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

  def filterGroup(self, groupBame):
    """
    Description:
    -----------

    :param groupBame:
    """
    if not groupBame in self.__filters_groups:
      self.__filters_groups[groupBame] = DataFilters(self.varName, self._report)
    return self.__filters_groups[groupBame]

  def cleafFilterGroup(self, groupBame):
    """
    Description:
    -----------

    :param groupBame:
    """
    if not groupBame in self.__filters_groups:
      del self.__filters_groups[groupBame]

    return self

  def clearFilters(self):
    self.__filters_groups = {}
    return self
