
import json

from epyk.core.js import JsUtils
from epyk.core.py import OrderedSet


class DataFilters(object):

  def __init__(self,  varName, report=None):
    self.varName, self.__filters = varName, []
    self._report = report

  def equal(self, key, value):
    name = "filterEqual"
    key = JsUtils.jsConvertData(key, None)
    value = JsUtils.jsConvertData(value, None)
    constructors = self._report._props.setdefault("js", {}).setdefault("constructors", {})
    constructors[name] = "function %s(r, k, v){if (v == ''){return r}; var n=[];r.forEach(function(e){if(e[k]==v){n.push(e)}});return n}" % name
    self.__filters.append("%s(%%s, %s, %s)" % (name, key, value))
    return self

  def startswith(self, key, value):
    name = "filterStartsWith"
    key = JsUtils.jsConvertData(key, None)
    value = JsUtils.jsConvertData(value, None)
    constructors = self._report._props.setdefault("js", {}).setdefault("constructors", {})
    constructors[name] = "function %s(r, k, v){var n=[];r.forEach(function(e){if(e[k].startsWith(v)){n.push(e)}});return n}" % name
    self.__filters.append("%s(%%s, %s, %s)" % (name, key, value))
    return self

  def sup(self, key, value, strict=True):
    constructors = self._report._props.setdefault("js", {}).setdefault("constructors", {})
    if strict:
      name = "filterSup"
      key = JsUtils.jsConvertData(key, None)
      value = JsUtils.jsConvertData(value, None)
      constructors[name] = "function %s(r, k, v){var n=[];r.forEach(function(e){if(e[k] > v){n.push(e)}});return n}" % name
      self.__filters.append("%s(%%s, %s, %s)" % (name, key, value))
    else:
      name = "filterSupEq"
      key = JsUtils.jsConvertData(key, None)
      value = JsUtils.jsConvertData(value, None)
      constructors[name] = "function %s(r, k, v){var n=[];r.forEach(function(e){if(e[k] >= v){n.push(e)}});return n}" % name
      self.__filters.append("%s(%%s, %s, %s)" % (name, key, value))
    return self

  def inf(self, key, value, strict=True):
    constructors = self._report._props.setdefault("js", {}).setdefault("constructors", {})
    if strict:
      name = "filterInf"
      key = JsUtils.jsConvertData(key, None)
      value = JsUtils.jsConvertData(value, None)
      constructors[name] = "function %s(r, k, v){var n=[];r.forEach(function(e){if(e[k] < v){n.push(e)}});return n}" % name
      self.__filters.append("%s(%%s, %s, %s)" % (name, key, value))
    else:
      name = "filterInfEq"
      key = JsUtils.jsConvertData(key, None)
      value = JsUtils.jsConvertData(value, None)
      constructors[name] = "function %s(r, k, v){var n=[];r.forEach(function(e){if(e[k] <= v){n.push(e)}});return n}" % name
      self.__filters.append("%s(%%s, %s, %s)" % (name, key, value))

    return self

  def toStr(self):
    result = "%s"
    for rec in self.__filters[::-1]:
      result %= rec
    return result % self.varName


class DataGlobal(object):

  def __init__(self, data, varName, report=None):
    report._props["js"]["datasets"][varName] = json.dumps(data)
    self._data, self.__filters_groups, self._report, self.varName = data, {}, report, varName

  def filterGroup(self, groupBame):
    """

    :param groupBame:
    """
    if not groupBame in self.__filters_groups:
      self.__filters_groups[groupBame] = DataFilters(self.varName, self._report)
    return self.__filters_groups[groupBame]

  def cleafFilterGroup(self, groupBame):
    """

    :param groupBame:
    """
    if not groupBame in self.__filters_groups:
      del self.__filters_groups[groupBame]

    return self

  def clearFilters(self):
    self.__filters_groups = {}
    return self
