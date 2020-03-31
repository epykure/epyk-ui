
from epyk.core.js import JsUtils
from epyk.core.js.packages import JsPackage
from epyk.core.js.primitives import JsObjects


class Timepicker(JsPackage):

  def __init__(self, htmlObj, varName=None, setVar=True, isPyData=True, report=None):
    self.htmlId = varName if varName is not None else htmlObj.htmlId
    self.varName, self.varData, self.__var_def = "document.getElementById('%s')" % self.htmlId, "", None
    self._src, self._report = htmlObj, report
    self._js, self._jquery = [], None

  def change(self, jsFncs):
    """
    Description:
    ------------
    Event triggerd when the value of the input field changes. A Date object containing the selected time is passed as the first argument of the callback.

    Related Pages:
    --------------
    https://timepicker.co/options/
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    jsFncs = JsUtils.jsConvertFncs(jsFncs, toStr=True)
    return JsObjects.JsObjects.get('%s.timepicker({change: function(time) { %s } })' % (self._src.dom.jquery.varId, jsFncs))

  def value(self, jsValue=None):
    """
    Description:
    ------------
    Set the timepicker object value

    Related Pages:
    --------------
    https://stackoverflow.com/questions/32378842/setting-the-hour-and-minute-of-timepicker-dynamically

    Attributes:
    ----------
    :param jsValue: String or Js Object
    """
    jsValue = JsUtils.jsConvertData(jsValue, None)
    return JsObjects.JsObjects.get('%s.timepicker("setTime", %s)' % (self._src.dom.jquery.varId, jsValue))
