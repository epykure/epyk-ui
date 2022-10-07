
from epyk.core.js.packages import JsPackage
from epyk.core.js.primitives import JsNumber
from epyk.core.js import JsUtils


class CompNumber(JsPackage):

  def set(self, num: float):
    """
    Set the number value.

    Usage::

      num = page.ui.number(5977, label="test")
      num.click([num.js.set(18)])

    :param num: The value.
    """
    return self.component.build(
      JsNumber.JsNumber(data=JsUtils.jsConvertData(num, None)))

  def add(self, num: float = 1):
    """
    Add a value.

    Usage::

      inp = page.ui.input()
      num = page.ui.number(10, label="test")
      num.click([num.js.add(inp.dom.content)])

    :param num: The value
    """
    num = JsUtils.jsConvertData(num, None)
    return self.component.build(
      JsNumber.JsNumber(
        data="parseFloat(accounting.unformat(%s.querySelector('font').innerHTML)) + parseFloat(%s)" % (
          self.varId, num)))

  def sub(self, num: float = 1):
    """
    Substract a value.

    Usage::

      inp = page.ui.input()
      num = page.ui.number(10, label="test")
      num.click([num.js.sub()])

    :param num: The value
    """
    num = JsUtils.jsConvertData(num, None)
    return self.component.build(
      JsNumber.JsNumber(
        data="parseFloat(accounting.unformat(%s.querySelector('font').innerHTML)) - parseFloat(%s)" % (
          self.varId, num)))
