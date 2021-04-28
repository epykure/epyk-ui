#!/usr/bin/python
# -*- coding: utf-8 -*-


from epyk.core.js.fncs import JsFncsRecords
from epyk.core.js.objects import JsChartD3
from epyk.core.js.primitives import JsObject
from epyk.core.js import JsUtils


class FncToObject:

  def __init__(self, data, js_src, data_schema=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param data:
    :param js_src:
    :param data_schema:
    """
    self._js_src, self._data_schema, self._data = js_src, data_schema, data

  def __register_records_fnc(self, fnc_name, fnc_def, fnc_pmts=None):
    """
    Description:
    ------------
    This function will attach to the report object only the javascript functions used during the report.

    Attributes:
    ----------
    :param fnc_name: String.
    :param fnc_def:
    :param fnc_pmts:
    """
    fnc_pmts = ["data"] + (fnc_pmts or [])
    if fnc_name not in self._js_src.get('js', {}).get('functions', {}):
      self._js_src.setdefault('js', {}).setdefault('functions', {})[fnc_name] = {
        'content': "var result = []; %s;return result" % JsUtils.cleanFncs(fnc_def), 'pmt': fnc_pmts}

  @property
  def d3(self):
    """
    Description:
    ------------
    Data transformation to the D3 package.
    """
    return JsChartD3.JsChartD3Links(self._data, self._js_src, self._data_schema)

  @property
  def dc(self):
    """
    Description:
    ------------
    Data transformation to the DC package.
    """
    from epyk.core.js.objects import JsChartDC

    return JsChartDC.JsChartDCLinks(self._data, self._js_src, self._data_schema)


class FncRoAggRec:

  def __init__(self, data, js_src, data_schema=None):
    self._js_src, self._data_schema, self._data = js_src, data_schema, data

  def __register_records_fnc(self, fnc_name, fnc_def, fnc_pmts=None):
    """
    Description:
    ------------
    This function will attach to the report object only the javascript functions used during the report.

    Attributes:
    ----------
    :param fnc_name: String.
    :param fnc_def:
    :param fnc_pmts: Dictionary. Optional.
    """
    fnc_pmts = ["data"] + (fnc_pmts or [])
    if fnc_name not in self._js_src.get('js', {}).get('functions', {}):
      self._js_src.setdefault('js', {}).setdefault('functions', {})[fnc_name] = {
        'content': "var result = []; %s;return result" % JsUtils.cleanFncs(fnc_def), 'pmt': fnc_pmts}


class FncOnRecords:

  def __init__(self, data, js_src, data_schema=None, profile=False):
    self._js_src, self._data_schema, self._data = js_src, data_schema, data

  @property
  def o(self):
    """
    Description:
    ------------
    Property to the data final object.
    Those items help to the link to external packages.
    """
    return FncToObject(self._js_src, self._data_schema)

  def __register_records_fnc(self, fnc_name, fnc_def, fnc_pmts=None, profile=False):
    """
    Description:
    ------------
    This function will attach to the report object only the javascript functions used during the report.

    Attributes:
    ----------
    :param fnc_name: String.
    :param fnc_def:
    :param fnc_pmts: Dictionary. Optional.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    fnc_pmts = ["data"] + (fnc_pmts or [])
    if fnc_name not in self._js_src.get('js', {}).get('functions', {}):
      self._js_src.setdefault('js', {}).setdefault('functions', {})[fnc_name] = {
        'content': "var result = []; %s;return result" % JsUtils.cleanFncs(fnc_def), 'pmt': fnc_pmts}

  def custom(self, fnc_name, fnc_content, fnc_pmts=None, profile=False):
    """
    Description:
    ------------
    The function content should use data and produce an object record.

    Attributes:
    ----------
    :param fnc_name: A string for the Javascript function name.
    :param fnc_content: The javascript function content.
    :param fnc_pmts: String. Optional. The Javascript function parameters.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.

    :return: "This" in order to allow the chains
    """
    self.__register_records_fnc(fnc_name, fnc_content, fnc_pmts, profile)
    return self

  def url(self):
    """
    Description:
    ------------

    """
    fnc_name = JsFncsRecords.JsToUrl.__name__
    fnc_pmts = ["data"]
    for p in getattr(JsFncsRecords.JsToUrl, 'params', []):
      fnc_pmts.append(p)
    if fnc_name not in self._js_src.get('functions', {}):
      content = JsUtils.cleanFncs(JsFncsRecords.JsToUrl.value)
      self._js_src.setdefault('functions', {})[fnc_name] = {'content': "%s; return result" % content, 'pmt': fnc_pmts}
    return fnc_name

  def count(self, keys, values=None, profile=False):
    """
    Description:
    ------------
    The Javascript function are using the main data as a first parameter.

    If values is defined, the Javascript will aggregate the data based on the composite key and the values will be
    available in the record. Also the count will be displayed.
    The values will be one in the record and not the sum.

    Attributes:
    ----------
    :param keys: List | String. The column names.
    :param values: List. Optional. The values to keep in the result record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.

    :return: "This" to allow function chains
    """
    if not isinstance(keys, list):
      keys = [keys]

    if values is None:
      fnc_name = JsFncsRecords.JsCountAll.__name__
      self.__register_records_fnc(
        fnc_name, JsFncsRecords.JsCountAll.value, fnc_pmts=list(JsFncsRecords.JsCountAll.params))
      self._data_schema['fncs'].append("%s(%%s, %s)" % (fnc_name, keys))
    else:
      fnc_name = JsFncsRecords.JsCount.__name__
      self.__register_records_fnc(
        fnc_name, JsFncsRecords.JsCount.value, fnc_pmts=list(JsFncsRecords.JsCount.params))
      self._data_schema['fncs'].append("%s(%%s, %s, %s)" % (fnc_name, keys, values))
    return self._data

  def count_with_kpi(self, keys, values, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param keys: List | String. The column names.
    :param values: List. Optional. The values to keep in the result record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    fnc_name = JsFncsRecords.JsCountSum.__name__
    self.__register_records_fnc(
      fnc_name, JsFncsRecords.JsCountSum.value, fnc_pmts=list(JsFncsRecords.JsCountSum.params))
    self._data_schema['fncs'].append("%s(%%s, %s, %s)" % (fnc_name, keys, values))
    return self._data

  def count_distinct(self, keys, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param keys: List | String. The column names.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.

    :return: "This" to allow function chains
    """
    if not isinstance(keys, list):
      keys = [keys]
    fnc_name = JsFncsRecords.JsCountDistinct.__name__
    self.__register_records_fnc(
      fnc_name, JsFncsRecords.JsCountDistinct.value, fnc_pmts=list(JsFncsRecords.JsCountDistinct.params))
    self._data_schema['fncs'].append("%s(%%s, %s)" % (fnc_name, keys))
    return self._data

  def top(self, column, n=1, order='desc', profile=False):
    """
    Description:
    ------------
    The Javascript function are using the main data as a first parameter.

    Attributes:
    ----------
    :param column:
    :param n: Integer. Optional.
    :param order: String. Optional.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.

    :return: "This" to allow function chains
    """
    fnc_name = JsFncsRecords.JsTop.__name__
    self.__register_records_fnc(
      fnc_name, JsFncsRecords.JsTop.value, fnc_pmts=list(JsFncsRecords.JsTop.params))
    self._data_schema['fncs'].append("%s(%%s, %s, '%s', '%s')" % (fnc_name, n, column, order))
    return self


class FncFiltere:

  def __init__(self, data, js_src, data_schema=None, profile=False):
    self._js_src, self._data_schema, self._data = js_src, data_schema, data
    fnc_name = JsFncsRecords.JsFilter.__name__
    fnc_pmts = ["data"] + (list(JsFncsRecords.JsFilter.pmts) or [])
    if fnc_name not in self._js_src.get('js', {}).get('functions', {}):
      self._js_src.setdefault('js', {}).setdefault('functions', {})[fnc_name] = {
        'content': "var result = []; %s;return result" % JsUtils.cleanFncs(
          JsFncsRecords.JsFilter.content), 'pmt': fnc_pmts}
    self._data_schema['filters'] = []

  def custom(self, column, val, compare_type, all_if_empty=True):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param column:
    :param val:
    :param compare_type:
    :param all_if_empty: Boolean. Optional.
    """
    filter_data = JsUtils.jsConvertData({
      "colName": column, "val": val, "op": compare_type, "allIfEmpty": all_if_empty}, None)
    self._data_schema['filters'].append(filter_data.toStr())
    return self._data

  def not_in_(self):
    """
    Description:
    ------------

    """

  def not_range_(self, column, val, compare_type="in", all_if_empty=True):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param column:
    :param val:
    :param compare_type: String. Optional.
    :param all_if_empty: Boolean. Optional.
    """

  def in_(self, column, val):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param column:
    :param val:
    """
    return self.custom(column, val, "in", True)

  def range_(self, column, val, strict_left=False, strict_right=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param column:
    :param val:
    :param strict_left: Boolean. Optional.
    :param strict_right: Boolean. Optional.
    """
    if not strict_left:
      if not strict_right:
        return self.custom(column, val, "><=", True)

      return self.custom(column, val, "><", True)

    if not strict_right:
      if not strict_left:
        return self.custom(column, val, "=><", True)

      return self.custom(column, val, "><", True)

    return self.custom(column, val, "=><=", True)

  def eq_(self, column, val):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param column:
    :param val:
    """
    return self.custom(column, val, ">", True)

  def sup_(self, column, val, strict=False):
    """
    Description:
    ------------
    Filter only the data above the value for the given key in the record.

    Attributes:
    ----------
    :param column: String. The column name.
    :param val: Object. The value in the dictionary.
    :param strict: Boolean. Optional. A flag to specify if the value should be included.
    """
    if strict:
      return self.custom(column, val, ">", True)

    return self.custom(column, val, ">=", True)

  def inf_(self, column, val, strict=False):
    """
    Description:
    ------------
    Filter only the data below the value for the given key in the record.

    Attributes:
    ----------
    :param column: String. The column name.
    :param val: Object. The value in the dictionary.
    :param strict: Boolean. Optional. A flag to specify if the value should be included.
    """
    if strict:
      return self.custom(column, val, "<", True)

    return self.custom(column, val, "<=", True)


class JsRegisteredFunctions:

  class __internal:
    _props = {}

  def __init__(self, src=None):
    self.src = src or self.__internal()
    if 'js' not in self.src._props:
      self.src._props['js'] = {}
    self._js_src = self.src._props['js']

  def cssStyle(self, params):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param params:
    """
    self._js_src.setdefault('functions', {})["cssStyle"] = {
      'content': 'cssParams = []; for(var i in params){cssParams.push(i +":"+ params[i])}; return cssParams.join(";")',
      'pmt': ["params"]}
    return "cssStyle"

  def service(self):
    """
    Description:
    ------------
    Create and store a function to do simple services calls and return a temporary message.

    TODO: To be improved and extended.
    """
    self._js_src.setdefault('functions', {})["serviceCall"] = {
      'content': self.src.js.post(JsUtils.jsWrap("url"), {"data": JsUtils.jsWrap("data")}).onSuccess([
        self.src.js.msg.status()
      ]).toStr(),
      'pmt': ["url", "data"]}
    return "serviceCall"

  def anonymous(self, jsFnc, pmts=None):
    """
    Description:
    ------------
    Create a anonymous / lambda function.
    Those functions are directly called when they are defined.

    Related Pages:

      https://www.w3schools.com/js/js_function_definition.asp

    Attributes:
    ----------
    :param jsFnc: List | String. Javascript functions.
    :param pmts: Dictionary. Optional. The function parameters.
    """
    if pmts is None:
      return JsFunction("(function(){%s})()" % jsFnc)

    return JsFunction("(function(%s){%s})()" % (",".join(pmts), jsFnc))

  def get(self, fnc_name, *args):
    """
    Description:
    ------------
    Call a bespoke functions on the Javascript side.

    Attributes:
    ----------
    :param fnc_name: String. The function name.
    :param args: Dictionary. The different arguments in the function definition.

    :return: The Javascript sting
    """
    pmts = [str(JsUtils.jsConvertData(p, None)) for p in args]
    return "%s(%s)" % (fnc_name, ", ".join(pmts))

  def inline(self, fnc_name, jsFnc, pmts=None):
    """
    Description:
    ------------
    Create a name function which can be then called later.

    Related Pages:

      https://www.w3schools.com/js/js_function_definition.asp

    Attributes:
    ----------
    :param fnc_name: String. The function name.
    :param jsFnc: List | String. Javascript functions.
    :param pmts: Dictionary. Optional. The function parameters.

    :return: The function name which can be used in the Javascript
    """
    self._js_src.setdefault('functions', {})[fnc_name] = {
      'content': JsUtils.jsConvertFncs(jsFnc, toStr=True), 'pmt': pmts}
    return fnc_name

  @property
  def records(self):
    """
    Description:
    ------------
    Javascript pre defined function dedicated to transform a records.
    Namely a list of dictionaries.
    """
    return FncOnRecords(self._js_src)


class JsFunction:
  fncName = "lambda"

  def __init__(self, strFnc):
    self.__strFnc = strFnc

  def __str__(self):
    return self.__strFnc

  def toStr(self):
    return self.__strFnc


class JsFunctions(list):

  def __init__(self, strFnc):
    if not isinstance(strFnc, list):
      strFnc = [strFnc]
    self.__strFncs = strFnc

  def append(self, strFnc):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param strFnc:
    """
    self.__strFncs.append(strFnc)

  def extend(self, strFncs):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param strFncs:
    """
    self.__strFncs.extend(strFncs)

  def toStr(self):
    return "; ".join([s.toStr() if hasattr(s, 'toStr') else str(s) for s in self.__strFncs])


_JSFNCS = 0


class JsLambda:

  def __init__(self):
    global _JSFNCS

    _JSFNCS += 1
    self.fncName = "function_%s" % _JSFNCS


class JsTypeOf:
  fncName = "typeof"

  def __init__(self, jsData):
    if self.fncName is None:
      raise Exception("Private fncName variable should be defined for pre defined functions ")

    self.__jsArgs = [jsData]

  def __str__(self):
    return "%s(%s)" % (self.fncName, ", ".join([str(a) for a in self.__jsArgs]))


class JsAnonymous:

  def __init__(self, jsFncs):
    self.__strFnc, self.__returnFnc, self.__paramsFnc = jsFncs, "", []

  def return_(self, value):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param value:
    """
    self.__returnFnc = value
    return self

  def params(self, pmts):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param pmts: Dictionary. The function parameters.
    """
    self.__paramsFnc = pmts
    return self

  def call(self, *args, **kwargs):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param args:
    :param kwargs:
    """
    _args = []
    if self.__paramsFnc:
      for a in list(args):
        _args.append(str(a))
      if kwargs:
        for i, p in enumerate(self.__paramsFnc):
          if p in kwargs:
            _args.append(str(kwargs[p]))
    return JsObject.JsObject("%s(%s)" % (self, ", ".join(_args)))

  def __str__(self):
    return "(function (%s) {%s; return %s})" % (", ".join(self.__paramsFnc), self.__strFnc, self.__returnFnc)

  def toStr(self):
    return str(self.__strFnc)
