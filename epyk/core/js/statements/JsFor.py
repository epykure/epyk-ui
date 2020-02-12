"""

"""


from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObject


class JsFor(object):

  def __init__(self, jsIterable, iterVar="i", start=0, step=1, context=None):
    """
    The for statement creates a loop that is executed as long as a condition is true.

    The loop will continue to run as long as the condition is true. It will only stop when the condition becomes false.

    Documentation:
    https://www.w3schools.com/jsref/jsref_for.asp
    https://www.w3schools.com/js/js_performance.asp

    :param jsIterable:
    :param iterVar:
    :param start:
    :param step:
    :param context:
    """
    self._context = context
    if not hasattr(jsIterable, 'toStr'):
      self.__jsObj = JsObject.JsObject(jsIterable, setVar=True)
    else:
      self.__jsObj = jsIterable
    self._js = [
      "var %s = %s" % (self.__jsObj.varName, jsIterable),
      "var l = %s.length" % self.__jsObj.varName,
      "for(var %(iterVar)s = %(start)s; %(iterVar)s < l; i+=%(step)s)" % {"step": step, 'start': start, 'iterVar': iterVar}]
    self.__iterVar = iterVar
    self.__jsFncs = []

  def js(self, jsFncs, isPyData=False, jsFncVal=None):
    """

    :param jsFncs:
    :param isPyData:
    :param jsFncVal:
    :return:
    """
    if jsFncVal is None:
      jsFncVal = "%s[%s]" % (self.__jsObj.varName, self.__iterVar)
    jsIterable = JsUtils.jsConvertFncs(jsFncs, isPyData, jsFncVal)
    self.__jsFncs.extend(jsIterable)
    return self

  def toStr(self):
    """

    :return:
    """
    #if self.__forid is None:
    #  raise Exception("Javascript For loop not correctly defined")

    strData = ";".join(self._js) + "{%s}"
    strData %= ";".join(self.__jsFncs)
    self.__jsFncs, self.__jsObj = [], None  # empty the stack
    return "".join(strData)

