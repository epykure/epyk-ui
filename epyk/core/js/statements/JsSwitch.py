import json

from epyk.core.js import JsUtils


class JsSwitch(object):
  """

  Documentation:
    - https://www.w3schools.com/js/js_switch.asp

  """

  def __init__(self, jsObj, context=None):
    """

    :param jsCondition:
    :param jsFncs:
    :param context:
    """
    self._context = context
    self.__jsObj = jsObj
    self.__js, self.__default = [], None

  def case(self, value, jsFncs):
    """

    :param jsFncs:
    :param isPyData:
    :param jsFncVal:
    :return:
    """
    self.__js.append((value, jsFncs))
    return self

  def default_(self, jsFncs):
    """

    :param jsFncs:
    :return:
    """
    self.__default = jsFncs
    return self

  def toStr(self):
    """

    :return:
    """
    strData = []
    for val, jsFncs in self.__js:
      strData.append("case %s: {%s; break}" % (json.dumps(val), ";".join(map(lambda x: str(x),  jsFncs))))
    if self.__default is not None:
      strData.append("default: {%s}" % ";".join(self.__default))
    self.__jsFncs, self.__default = [], None # empty the stack
    return "switch (%s){%s}" % (self.__jsObj.varName, "".join(strData))
