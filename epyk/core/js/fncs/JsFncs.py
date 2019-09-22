"""

"""


from epyk.core.js.fncs import JsFncsRecords
from epyk.core.js.fncs import JsFncsUtils


FNCS_MAPS = {
  "row-buckets": JsFncsRecords.JsRowBuckets,
  'toMarkUp': JsFncsUtils.JsMarkUp,
  'formatNumber': JsFncsUtils.JsFormatNumber,
}


class JsRegisteredFunctions(object):
  def __init__(self, src):
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
