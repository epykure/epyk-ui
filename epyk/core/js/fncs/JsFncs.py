from epyk.core.js.fncs import JsFncsRecords
from epyk.core.js.fncs import JsFncsUtils


FNCS_MAPS = {
  "row-buckets": JsFncsRecords.JsRowBuckets,
  'toMarkUp': JsFncsUtils.JsMarkUp,
  'formatNumber': JsFncsUtils.JsFormatNumber,
}


def cleanFncs(fnc):
  """
  Try to remove as much as possible all the characters in order to speed up the javascript
  Indeed most of the browsers are using minify Javascript to make the page less heavy

  Thus pre stored function code can be written to be easier to read.

  :param fnc: The Javascript String

  :return: Return a cleaned an minify Javascript String
  """
  return "".join([r.strip() for r in fnc.strip().split('\n')])


class FncOnRecords(object):
  def __init__(self, js_src, data_schema=None):
    self._js_src, self._data_schema = js_src, data_schema

  def __register_records_fnc(self, fnc_name, fnc_def, fnc_pmts=None):
    """
    This function will attach to the report object only the javascript functions used during the report

    :param fnc_name:
    :param fnc_def:

    :return:
    """
    fnc_pmts = ["data"] + (fnc_pmts or [])
    if not fnc_name in self._js_src.get('js', {}).get('functions', {}):
      self._js_src.setdefault('js', {}).setdefault('functions', {})[fnc_name] = {'content': "var result = []; %s;return result" % cleanFncs(fnc_def), 'pmt': fnc_pmts}

  def url(self):
    """

    :return:
    """
    fnc_name = JsFncsRecords.JsToUrl.__name__
    fnc_pmts = ["data"]
    for p in getattr(JsFncsRecords.JsToUrl, 'params', []):
      fnc_pmts.append(p)
    if not fnc_name in self._js_src.get('functions', {}):
      content = cleanFncs(JsFncsRecords.JsToUrl.value)
      self._js_src.setdefault('functions', {})[fnc_name] = {'content': "%s; return result" % content, 'pmt': fnc_pmts}
    return fnc_name

  def count(self, keys, values=None):
    """

    The Javascript function are using the main data as a first parameter

    :param keys:
    :param values:

    :return: "This" to allow function chains
    """
    if not isinstance(keys, list):
      keys = [keys]

    if values is None:
      fnc_name = JsFncsRecords.JsCountAll.__name__
      self.__register_records_fnc(fnc_name, JsFncsRecords.JsCountAll.value, fnc_pmts=list(JsFncsRecords.JsCountAll.params))
      self._data_schema['fncs'].append("%s(%%s, %s)" % (fnc_name, keys))
    else:
      fnc_name = JsFncsRecords.JsCount.__name__
      self.__register_records_fnc(fnc_name, JsFncsRecords.JsCount.value, fnc_pmts=list(JsFncsRecords.JsCount.params))
      self._data_schema['fncs'].append("%s(%%s, %s, %s)" % (fnc_name, keys, values))
    return self

  def count_distinct(self, keys):
    """

    :param keys:

    :return: "This" to allow function chains
    """
    if not isinstance(keys, list):
      keys = [keys]
    fnc_name = JsFncsRecords.JsCountDistinct.__name__
    self.__register_records_fnc(fnc_name, JsFncsRecords.JsCountDistinct.value, fnc_pmts=list(JsFncsRecords.JsCountDistinct.params))
    self._data_schema['fncs'].append("%s(%%s, %s)" % (fnc_name, keys))
    return self

  def top(self, column, n=1, order='desc'):
    """
    The Javascript function are using the main data as a first parameter

    Example

    :param column:
    :param n:
    :param order:

    :return: "This" to allow function chains
    """
    fnc_name = JsFncsRecords.JsTop.__name__
    self.__register_records_fnc(fnc_name, JsFncsRecords.JsTop.value, fnc_pmts=list(JsFncsRecords.JsTop.params))
    self._data_schema['fncs'].append("%s(%%s, %s, '%s', '%s')" % (fnc_name, n, column, order))
    return self


class JsRegisteredFunctions(object):
  class __internal(object):
    _props = {}

  def __init__(self, src=None):
    src = src or self.__internal()
    if not 'js' in src._props:
      src._props['js'] = {}
    self._js_src = src._props['js']

  @property
  def markUp(self):
    """
    Javascript function to convert a string to the equivelent Markdown HTML tags

    Documentation
    https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

    :return: The function name to be used in a Javascript String
    """
    fnc_name = JsFncsUtils.JsMarkUp.__name__
    fnc_pmts = JsFncsUtils.JsMarkUp.params
    if not fnc_name in self._js_src.get('functions', {}):
      self._js_src.setdefault('functions', {})[fnc_name] = {'content': "%s; return result" % JsFncsUtils.JsMarkUp.value, 'pmt': fnc_pmts}
    return fnc_name

  @property
  def cssStyle(self):
    """

    :return:
    """
    self._js_src.setdefault('functions', {})["cssStyle"] = {
      'content': '''
        cssParams = [] ;
        for(var i in params){cssParams.push( i +":"+ params[i])}
        return cssParams.join(";")''',
      'pmt': ["params"]}
    return "cssStyle"

  def anonymous(self, jsFnc, pmts=None):
    """
    Create a anonymous / lambda function.
    Those functions are directly called when they are defined.

    Documentation
    https://www.w3schools.com/js/js_function_definition.asp

    :param jsFnc:
    :param pmts:

    :return:
    """
    if pmts is None:
      return JsFunction("(function(){%s})()" % jsFnc)

    return JsFunction("(function(%s) {%s})()" % (",".join(pmts), jsFnc))

  def inline(self, fnc_name, jsFnc, pmts=None):
    """
    Create a name function which can be then called later

    Documentation
    https://www.w3schools.com/js/js_function_definition.asp

    :param fnc_name:
    :param jsFnc:
    :param pmts:

    :return: The function name which can be used in the Javascript
    """
    self._js_src.setdefault('functions', {})[fnc_name] = {'content': jsFnc, 'pmt': pmts}
    return fnc_name

  @property
  def records(self):
    """
    Javascript pre defined function dedicated to transform a records.
    Namely a list of dictionaries
    """
    return FncOnRecords(self._js_src)


class JsFunction(object):
  """

  """
  fncName = "lambda"

  def __init__(self, strFnc):
    self.__strFnc = strFnc

  def __str__(self):
    return self.__strFnc

  def toStr(self):
    return self.__strFnc


_JSFNCS = 0


class JsLambda(object):
  """

  """

  def __init__(self):
    """
    """
    global _JSFNCS

    _JSFNCS += 1
    self.fncName = "function_%s" % _JSFNCS


class JsTypeOf(object):
  """

  """
  fncName = "typeof"

  def __init__(self, jsData):
    if self.fncName is None:
      raise Exception("Private fncName variable should be defined for pre defined functions ")

    self.__jsArgs = [jsData]

  def __str__(self):
    """

    :return:
    """
    return "%s(%s)" % (self.fncName, ", ".join([str(a) for a in self.__jsArgs]))
