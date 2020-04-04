
from epyk.core.js.packages import JsPackage
from epyk.core.js.primitives import JsObjects
from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtml


class CheckButton(JsPackage):

  def __init__(self, htmlObj, varName=None, setVar=True, isPyData=True, report=None):
    self.varName, self.varData, self.__var_def = varName, "", None
    self._src, self._report = htmlObj, report
    self._js, self._jquery = [], None

  def checked(self):
    """
    Description:
    -----------

    """
    return JsObjects.JsObjects.get("%s.querySelector('i').classList.replace('fa-times', 'fa-check'); %s.querySelector('i').style.color = '%s'" % (self._src.dom.varName, self._src.dom.varName, self._report.theme.success[1]))

  def unchecked(self):
    """
    Description:
    -----------

    """
    return JsObjects.JsObjects.get("%s.querySelector('i').classList.replace('fa-check', 'fa-times'); %s.querySelector('i').style.color = '%s'" % (self._src.dom.varName, self._src.dom.varName, self._report.theme.danger[1]))


class Menu(JsPackage):

  def __init__(self, htmlObj, varName=None, setVar=True, isPyData=True, report=None):
    self.varName, self.varData, self.__var_def = varName, "", None
    self._src, self._report = htmlObj, report
    self._js, self._jquery = [], None

  @property
  def content(self):
    """
    Description:
    -----------
    Return the content of the component
    """
    return JsHtml.ContentFormatters(self._report, "%s.innerHTML" % self.varName)

  def set_text(self, value):
    """
    Description:
    -----------
    Set the text of the component

    Attributes:
    ----------
    :param value: String. The text to be set
    """
    value = JsUtils.jsConvertData(value, None)
    return JsObjects.JsObjects.get("%s.innerHTML = %s" % (self.varName, value))

  def set_url(self, value, target='_blank'):
    """
    Description:
    -----------
    Set the URL information of the item component

    Usage:
    ------
    item.js.set_url("https://stackoverflow.com")

    Related Pages:
    --------------
    https://www.w3schools.com/tags/att_a_href.asp

    Attributes:
    ----------
    :param value: String. The url link
    :param target: String.  Teh target mode of the link component
    """
    value = JsUtils.jsConvertData(value, None)
    target = JsUtils.jsConvertData(target, None)
    return JsObjects.JsObjects.get("%s.href = %s; %s.setAttribute('target', %s)" % (self.varName, value, self.varName, target))


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
