
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObject


class JsWhile(object):

  def __init__(self, jsCondition, ruleType='boolean', iterVar="i", start=0, step=1, context=None):
    """
    Marks a block of statements to be executed while a condition is true

    Documentation:
      - https://www.w3schools.com/jsref/jsref_while.asp

    :param jsCondition:
    :param ruleType:
    :param iterVar:
    :param start:
    :param step:
    :param context:
    """
    self._context, self.__whileId, self.__iterVar, self.__next = context, None, None, None
    self.__whileDataId = None
    if ruleType == 'array':
      self.step = step
      self.__jsObj = JsObject.JsObject(jsCondition, setVar=True)
      self.__iterVar = iterVar
      self.__val = JsObject.JsObject("{key: %(keys)s, value: %(dico)s[%(keys)s]}" % {"dico": self.__jsObj, "keys": iterVar}, isPyData=False, setVar=True)
      self.next("%s+=%s" % (self.__iterVar, self.step))
      # Should add undefined in order not to stop in the zero values in the iterator
      self.__while = ["var %s = %s" % (self.__jsObj, jsCondition), "var %s = %s" % (self.__iterVar, start),
                      "while(%s[i] !== undefined)" % self.__jsObj.varName]
    elif ruleType == 'dict':
      self.__jsObj = JsObject.JsObject(jsCondition, setVar=True)
      self.__iterVar = "%s_keys" % self.__jsObj.varName
      self.__val = JsObject.JsObject("{key: %(keys)s[k], value: %(dico)s[%(keys)s[k]]}" % {"dico": self.__jsObj, "keys": self.__iterVar}, isPyData=False, setVar=True)
      self.next("k += 1")
      # Should add undefined in order not to stop in the zero values in the iterator
      self.__while = ["var %s = %s" % (self.__jsObj, jsCondition), "var %s = %s" % (self.__iterVar, self.__jsObj.keys()),
                      "var k = 0", "while(%s[k] !== undefined)" %  self.__iterVar]
    else:
      self.__while = ["while(%s)" % jsCondition]
    self.__jsFncs = []

  def next(self, rule):
    """

    :return:
    """
    self.__next = rule
    return self

  def js(self, jsFncs, isPyData=False, jsFncVal=None):
    """

    :param jsFncs:
    :param isPyData:
    :param jsFncVal:
    :return:
    """
    if jsFncVal is None:
      jsFncVal = self.__val.varName
    jsIterable = JsUtils.jsConvertFncs(jsFncs, isPyData, jsFncVal)
    self.__jsFncs.extend(jsIterable)
    return self

  def toStr(self):
    if self.__next is None:
      raise Exception("next() function must be used to avoid infinite loops !!")

    self.__jsFncs.append(self.__next)
    strData = "%s{%s}" % (";".join(self.__while), ";".join(self.__jsFncs))

    self.__jsFncs = []
    return strData

