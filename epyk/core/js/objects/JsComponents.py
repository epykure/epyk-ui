#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union, Optional
from epyk.core.py import primitives

from epyk.core.js.packages import JsPackage
from epyk.core.js.primitives import JsObjects
from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtml


class Radio(JsPackage):

  def __init__(self, component: primitives.HtmlModel, js_code: str = None, set_var: bool = True,
               is_py_data: bool = True, page: primitives.PageModel = None):
    self.varName, self.varData, self.__var_def = js_code, "", None
    self.component, self.page = component, page
    self._js, self._jquery = [], None

  def check(self):
    """
    Description:
    -----------
    Set the status of the Check / Radio component to checked.
    """
    return JsUtils.jsWrap("%s.checked = true" % self.component.dom.varName)

  def uncheck(self):
    """
    Description:
    -----------
    Set the status of the Check / Radio component to unchecked.
    """
    return JsUtils.jsWrap("%s.checked = false" % self.component.dom.varName)

  def is_checked(self, js_funcs: Union[list, str], else_funcs: Union[list, str] = None,
                 profile: Optional[Union[bool, dict]] = None):
    """
    Description:
    -----------
    Condition on the status of the checkbox / Radio.
    This will trigger the underlying JavaScript functions only if the box is checked.

    Attributes:
    ----------
    :param js_funcs: The Javascript functions.
    :param else_funcs: The Javascript functions.
    :param profile: Optional. A flag to set the component performance storage.
    """
    js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if else_funcs is not None:
      else_funcs = JsUtils.jsConvertFncs(else_funcs, toStr=True, profile=profile)
      return JsUtils.jsWrap("if(%s.checked){%s} else {%s}" % (self.component.dom.varName, js_funcs, else_funcs))

    return JsUtils.jsWrap("if(%s.checked){%s}" % (self.component.dom.varName, js_funcs))

  def is_not_checked(self, js_funcs: Union[list, str], else_funcs: Union[list, str] = None,
                     profile: Optional[Union[bool, dict]] = None):
    """
    Description:
    -----------
    Condition on the status of the checkbox / Radio.
    This will trigger the underlying JavaScript functions only if the box is not checked.

    Attributes:
    ----------
    :param js_funcs: The Javascript functions.
    :param else_funcs: Optional. The Javascript functions.
    :param profile: Optional. A flag to set the component performance storage.
    """
    js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if else_funcs is not None:
      else_funcs = JsUtils.jsConvertFncs(else_funcs, toStr=True, profile=profile)
      return JsUtils.jsWrap("if(!%s.checked){%s} else {%s}" % (self.component.dom.varName, js_funcs, else_funcs))

    return JsUtils.jsWrap("if(!%s.checked){%s}" % (self.component.dom.varName, js_funcs))


class CheckButton(JsPackage):

  def __init__(self, component: primitives.HtmlModel, js_code: str = None, setVar=True,
               is_py_data: bool = True, page: primitives.PageModel = None):
    self.varName, self.varData, self.__var_def = js_code, "", None
    self.component, self.page = component, page
    self._js, self._jquery = [], None

  def checked(self, color: Union[str, primitives.JsDataModel] = None):
    """
    Description:
    -----------
    Set the status of the button component to checked.

    Attributes:
    ----------
    :param color: Optional. The font color in the component. Default inherit.
    """
    times = self.component.options.icon_not_check
    check = self.component.options.icon_check
    return JsObjects.JsObjects.get("%s.querySelector('i').classList.replace('%s', '%s'); %s.querySelector('i').style.color = %s" % (
      self.component.dom.varName, times, check, self.component.dom.varName,
      JsUtils.jsConvertData(color, None) or self.page.theme.success.base))

  def unchecked(self, color: Union[str, primitives.JsDataModel] = None):
    """
    Description:
    -----------
    Set the status of the button component to unchecked.

    Attributes:
    ----------
    :param color: Optional. The font color in the component. Default inherit.
    """
    times = self.component.options.icon_not_check
    check = self.component.options.icon_check
    return JsObjects.JsObjects.get("%s.querySelector('i').classList.replace('%s', '%s'); %s.querySelector('i').style.color = %s" % (
      self.component.dom.varName, check, times, self.component.dom.varName,
      JsUtils.jsConvertData(color, None) or self.page.theme.danger.base))


class Menu(JsPackage):

  def __init__(self, component, js_code: str = None, set_var: bool = True, is_py_data: bool = True,
               page: primitives.PageModel = None):
    self.varName, self.varData, self.__var_def = js_code, "", None
    self.component, self.page = component, page
    self._js, self._jquery = [], None

  @property
  def content(self):
    """
    Description:
    -----------
    Return the content of the component.
    """
    return JsHtml.ContentFormatters(self.page, "%s.innerHTML" % self.varName)

  def set_text(self, value: Union[str, primitives.JsDataModel]):
    """
    Description:
    -----------
    Set the text of the component.

    Attributes:
    ----------
    :param value: The text to be set.
    """
    value = JsUtils.jsConvertData(value, None)
    return JsObjects.JsObjects.get("%s.innerHTML = %s" % (self.varName, value))

  def set_url(self, value: str, target: str = '_blank'):
    """
    Description:
    -----------
    Set the URL information of the item component.

    Usage::

      item.js.set_url("https://stackoverflow.com")

    Related Pages:

      https://www.w3schools.com/tags/att_a_href.asp

    Attributes:
    ----------
    :param value: The url link.
    :param target: Optional. The target mode of the link component.
    """
    value = JsUtils.jsConvertData(value, None)
    target = JsUtils.jsConvertData(target, None)
    return JsObjects.JsObjects.get("%s.href = %s; %s.setAttribute('target', %s)" % (
      self.varName, value, self.varName, target))


class Switch(JsPackage):

  def __init__(self, component: primitives.HtmlModel, js_code: str = None, set_var: bool = True,
               is_py_data: bool = True,  page: primitives.PageModel = None):
    self.htmlCode = js_code if js_code is not None else component.htmlCode
    self.varName, self.varData, self.__var_def = "document.getElementById('%s')" % self.htmlCode, "", None
    self.component, self.page = component, page
    self._js, self._jquery = [], None

  def toggle(self):
    """
    Description:
    -----------
    Simulate a click event on the component.
    """
    return JsObjects.JsObjects.get(self.component.switch.click())

  def val(self, data: Union[bool, primitives.JsDataModel]):
    """
    Description:
    -----------
    Set the value for the switch.

    Attributes:
    ----------
    :param data: Flag to specify the state for the switch.
    """
    data = JsUtils.jsConvertData(data, None)
    return JsObjects.JsObjects.get('''%(varName)s.querySelector('input').checked = %(flag)s; 
        if(%(flag)s) {%(varName)s.querySelector('p').innerHTML = %(htmlCode)s_data.on}
        else {%(varName)s.querySelector('p').innerHTML = %(htmlCode)s_data.off}''' % {
      "varName": self.varName, "flag": data, "htmlCode": self.htmlCode})

  def false(self):
    """
    Description:
    -----------
    Set the switch component to False.
    """
    return JsObjects.JsObjects.get(
      "%s.querySelector('input').checked = false; %s.querySelector('p').innerHTML = %s_data.off" % (
        self.varName, self.varName, self.htmlCode))

  def true(self):
    """
    Description:
    -----------
    Set the switch component to True.
    """
    return JsObjects.JsObjects.get(
      "%s.querySelector('input').checked = true; %s.querySelector('p').innerHTML = %s_data.on" % (
        self.varName, self.varName, self.htmlCode))


class Alerts(JsPackage):

  def __init__(self, component, js_code: str = None, set_var: bool = True,
               is_py_data: bool = True, page: primitives.PageModel = None):
    self.htmlCode = js_code if js_code is not None else component.htmlCode
    self.varName, self.varData, self.__var_def = "document.getElementById('%s')" % self.htmlCode, "", None
    self.component, self.page = component, page
    self._js, self._jquery = [], None

  def replay(self, time: int = None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param time:
    """
    time = time or self.component.options.time
    return JsObjects.JsVoid('''
    var s = %(varName)s.style; s.opacity = 1; %(varName)s.style.display = 'block';
    (function fade(){(s.opacity-=.1)<0?s.display="none":setTimeout(fade, %(time)s)})();
    ''' % {'varName': self.varName, 'time': time})


class News(JsPackage):

  def __init__(self, component: primitives.HtmlModel, js_code: str = None, set_var: bool = True,
               is_py_data: bool = True, page: primitives.PageModel = None):
    self.htmlCode = js_code if js_code is not None else component.htmlCode
    self.varName, self.varData, self.__var_def = "document.getElementById('%s')" % self.htmlCode, "", None
    self.component, self.page = component, page
    self._js, self._jquery = [], None

  def reset(self):
    """
    Description:
    -----------

    """
    return JsObjects.JsVoid('''%(varName)s.innerHTML = '' ''' % {'varName': self.varName})


class Chat(JsPackage):

  def __init__(self, component: primitives.HtmlModel, js_code: str = None, set_var: bool = True,
               is_py_data: bool = True, page: primitives.PageModel = None):
    self.htmlCode = js_code if js_code is not None else component.htmlCode
    self.varName, self.varData, self.__var_def = "document.getElementById('%s')" % self.htmlCode, "", None
    self.component, self.page = component, page
    self._js, self._jquery = [], None

  def add(self, message):
    return JsObjects.JsVoid('''
      %(builder)s; %(counter)s
      ''' % {"builder": self.component.build(message),
             'counter': self.component.dom.querySelector(' [name=count]').innerText(1, append=True, val_type=int).r})


class Room(JsPackage):

  def __init__(self, component: primitives.HtmlModel, js_code: str = None, set_var: bool = True,
               is_py_data: bool = True, page: primitives.PageModel = None):
    self.htmlCode = js_code if js_code is not None else component.htmlCode
    self.varName, self.varData, self.__var_def = "document.getElementById('%s')" % self.htmlCode, "", None
    self.component, self.page = component, page
    self._js, self._jquery = [], None

  def typing(self):
    """
    Description:
    -----------
    Display dots in the status to inform user is typing.
    """
    return self.component.dom.querySelector("div[name=dots]").show(duration=3000)


