
from epyk.core.js.packages import JsPackage
from epyk.core.js.primitives import JsObjects


class Switch(JsPackage):

  def __init__(self, htmlObj, varName=None, setVar=True, isPyData=True, report=None):
    self.htmlId = varName if varName is not None else htmlObj.htmlId
    self.varName, self.varData, self.__var_def = "document.getElementById('%s')" % self.htmlId, "", None
    self._src, self._report = htmlObj, report
    self._js, self._jquery = [], None

  def toggle(self):
    """
    Description:
    -----------
    Simulate a click event on the component
    """
    return JsObjects.JsObjects.get(self._src.switch.click())

  def false(self):
    """
    Description:
    -----------
    Set the switch component to False
    """
    return JsObjects.JsObjects.get("%s.querySelector('input').checked = false; %s.querySelector('p').innerHTML = %s_data.off" % (self.varName, self.varName, self.htmlId))

  def true(self):
    """
    Description:
    -----------
    Set the switch component to True
    """
    return JsObjects.JsObjects.get("%s.querySelector('input').checked = true; %s.querySelector('p').innerHTML = %s_data.on" % (self.varName, self.varName, self.htmlId))
