from epyk.core.js import JsUtils


class JsIf(object):

  def __init__(self, jsCondition, jsFncs, context=None):
    """
    Description:
    ------------
    Create a JavaScript If statement

    Usage:
    ------
    JsIf.JsIf(self.input.dom.hasClass("fa-check"), jsFncsTrue)

    Attributes:
    ----------
    :param jsCondition: The Javascript condition. Can be a JsBoolean object
    :param jsFncs: The Javascript functions
    :param context: Optional. Dictionary. Meta data concerning the context
    """
    self._context = context
    jsFncs = JsUtils.jsConvertFncs(jsFncs, False)
    self._js = [(jsCondition, jsFncs)]
    self.__jsElse = None

  def elif_(self, jsCondition, jsFncs):
    """
    Description:
    ------------
    Add a Javascript elif statement to the loop

    Usage:
    ------

    Attributes:
    ----------
    :param jsCondition: The Javascript condition. Can be a JsBoolean object
    :param jsFncs: The Javascript functions
    :return: The If object to allow the chaining
    """
    jsFncs = JsUtils.jsConvertFncs(jsFncs, False)
    self._js.append((jsCondition, jsFncs))
    return self

  def else_(self, jsFncs):
    """
    Description:
    ------------
    Add the Javascript else statement to the loop

    Usage:
    ------
    JsIf.JsIf(self.input.dom.hasClass("fa-check"), jsFncsTrue).else_(jsFncFalse)

    Attributes:
    ----------
    :param jsFncs: The Javascript functions
    :return: The If object to allow the chaining
    """
    jsFncs = JsUtils.jsConvertFncs(jsFncs, False)
    self.__jsElse = jsFncs
    return self

  def toStr(self):
    strData = ["if(%s){%s}" % (self._js[0][0], ";".join(map(lambda x: str(x),  self._js[0][1])))]
    for condition, fncs in self._js[1:]:
      strData.append("else if(%s){%s}" % (condition, ";".join(fncs)))
    if self.__jsElse is not None:
      strData.append("else{%s}" % ";".join(map(lambda x: str(x),  self.__jsElse)))
    self._js, self.__jsElse = [], None # empty the stack
    return "".join(strData)
