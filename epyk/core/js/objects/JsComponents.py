#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.js.packages import JsPackage
from epyk.core.js.primitives import JsObjects
from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtml


class Radio(JsPackage):

  def __init__(self, htmlObj, varName=None, setVar=True, isPyData=True, report=None):
    self.varName, self.varData, self.__var_def = varName, "", None
    self._src, self._report = htmlObj, report
    self._js, self._jquery = [], None

  def check(self):
    """
    Description:
    -----------

    """
    return JsObjects.JsObjects.get("%s.checked = true" % self._src.input.dom.varName)

  def uncheck(self):
    """
    Description:
    -----------

    """
    return JsObjects.JsObjects.get("%s.checked = false" % self._src.input.dom.varName)


class CheckButton(JsPackage):

  def __init__(self, htmlObj, varName=None, setVar=True, isPyData=True, report=None):
    self.varName, self.varData, self.__var_def = varName, "", None
    self._src, self._report = htmlObj, report
    self._js, self._jquery = [], None

  def checked(self, color=None):
    """
    Description:
    -----------

    """
    times = self._src.options.icon_not_check
    check = self._src.options.icon_check
    return JsObjects.JsObjects.get("%s.querySelector('i').classList.replace('%s', '%s'); %s.querySelector('i').style.color = '%s'" % (self._src.dom.varName, times, check, self._src.dom.varName, color or self._report.theme.success[1]))

  def unchecked(self, color=None):
    """
    Description:
    -----------

    """
    times = self._src.options.icon_not_check
    check = self._src.options.icon_check
    return JsObjects.JsObjects.get("%s.querySelector('i').classList.replace('%s', '%s'); %s.querySelector('i').style.color = '%s'" % (self._src.dom.varName, check, times, self._src.dom.varName, color or self._report.theme.danger[1]))


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

    Usage::

      item.js.set_url("https://stackoverflow.com")

    Related Pages:

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
    self.htmlCode = varName if varName is not None else htmlObj.htmlCode
    self.varName, self.varData, self.__var_def = "document.getElementById('%s')" % self.htmlCode, "", None
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
    return JsObjects.JsObjects.get("%s.querySelector('input').checked = false; %s.querySelector('p').innerHTML = %s_data.off" % (self.varName, self.varName, self.htmlCode))

  def true(self):
    """
    Description:
    -----------
    Set the switch component to True
    """
    return JsObjects.JsObjects.get("%s.querySelector('input').checked = true; %s.querySelector('p').innerHTML = %s_data.on" % (self.varName, self.varName, self.htmlCode))


class Alerts(JsPackage):

  def __init__(self, htmlObj, varName=None, setVar=True, isPyData=True, report=None):
    self.htmlCode = varName if varName is not None else htmlObj.htmlCode
    self.varName, self.varData, self.__var_def = "document.getElementById('%s')" % self.htmlCode, "", None
    self._src, self._report = htmlObj, report
    self._js, self._jquery = [], None

  def replay(self, time=None):
    """
    Description:
    -----------

    """
    time = time or self._src.options.time
    return JsObjects.JsVoid('''
    var s = %(varName)s.style; s.opacity = 1; %(varName)s.style.display = 'block';
    (function fade(){(s.opacity-=.1)<0?s.display="none":setTimeout(fade, %(time)s)})();
    ''' % {'varName': self.varName, 'time': time})


class News(JsPackage):

  def __init__(self, htmlObj, varName=None, setVar=True, isPyData=True, report=None):
    self.htmlCode = varName if varName is not None else htmlObj.htmlCode
    self.varName, self.varData, self.__var_def = "document.getElementById('%s')" % self.htmlCode, "", None
    self._src, self._report = htmlObj, report
    self._js, self._jquery = [], None

  def reset(self):
    """
    Description:
    -----------

    """
    return JsObjects.JsVoid('''
      %(varName)s.innerHTML = '';  
      ''' % {'varName': self.varName})


class Chat(JsPackage):

  def __init__(self, htmlObj, varName=None, setVar=True, isPyData=True, report=None):
    self.htmlCode = varName if varName is not None else htmlObj.htmlCode
    self.varName, self.varData, self.__var_def = "document.getElementById('%s')" % self.htmlCode, "", None
    self._src, self._report = htmlObj, report
    self._js, self._jquery = [], None

  def add(self, message):
    return JsObjects.JsVoid('''
      %(builder)s; %(counter)s
      ''' % {"builder": self._src.build(message), 'counter': self._src.dom.querySelector(' [name=count]').innerText(1, append=True, valType=int).r})


class Room(JsPackage):

  def __init__(self, htmlObj, varName=None, setVar=True, isPyData=True, report=None):
    self.htmlCode = varName if varName is not None else htmlObj.htmlCode
    self.varName, self.varData, self.__var_def = "document.getElementById('%s')" % self.htmlCode, "", None
    self._src, self._report = htmlObj, report
    self._js, self._jquery = [], None

  def typing(self):
    """
    Description:
    -----------

    """
    return self._src.dom.querySelector("div[name=dots]").show(duration=3000)


