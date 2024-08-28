#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union, Optional
from epyk.core.py import primitives, types

from epyk.core.js.packages import JsPackage
from epyk.core.js.primitives import JsObjects
from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtml
from epyk.core.js.objects import JsNodeDom


class Radio(JsPackage):

    def __init__(self, component: primitives.HtmlModel, js_code: str = None, set_var: bool = True,
                 is_py_data: bool = True, page: primitives.PageModel = None):
        self.varName, self.varData, self.__var_def = js_code, "", None
        self.component, self.page = component, page
        self._js, self._jquery = [], None

    def check(self):
        """Set the status of the Check / Radio component to checked"""
        return JsUtils.jsWrap("%s.checked = true" % self.component.input.dom.varName)

    def uncheck(self):
        """Set the status of the Check / Radio component to unchecked"""
        return JsUtils.jsWrap("%s.checked = false" % self.component.input.dom.varName)

    def is_checked(self, js_funcs: Union[list, str], else_funcs: Union[list, str] = None,
                   profile: Optional[Union[bool, dict]] = None):
        """Condition on the status of the checkbox / Radio.

        This will trigger the underlying JavaScript functions only if the box is checked.

        :param js_funcs: The Javascript functions
        :param else_funcs: The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
        if else_funcs is not None:
            else_funcs = JsUtils.jsConvertFncs(else_funcs, toStr=True, profile=profile)
            return JsUtils.jsWrap("if(%s.checked){%s} else {%s}" % (self.component.input.dom.varName, js_funcs, else_funcs))

        return JsUtils.jsWrap("if(%s.checked){%s}" % (self.component.input.dom.varName, js_funcs))

    def is_not_checked(self, js_funcs: Union[list, str], else_funcs: Union[list, str] = None,
                       profile: Optional[Union[bool, dict]] = None):
        """Condition on the status of the checkbox / Radio.

        This will trigger the underlying JavaScript functions only if the box is not checked.

        :param js_funcs: The Javascript functions
        :param else_funcs: Optional. The Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
        if else_funcs is not None:
            else_funcs = JsUtils.jsConvertFncs(else_funcs, toStr=True, profile=profile)
            return JsUtils.jsWrap("if(!%s.checked){%s} else {%s}" % (self.component.input.dom.varName, js_funcs, else_funcs))

        return JsUtils.jsWrap("if(!%s.checked){%s}" % (self.component.input.dom.varName, js_funcs))

    def uncheck_all(self, name: Union[str, primitives.JsDataModel] = None):
        """Set the status of the Check / Radio component to unchecked"""
        name = JsUtils.jsConvertData(name or self.component.input.attr["name"], None)
        return JsUtils.jsWrap("document.body.querySelectorAll('input[name=%s]').forEach((s) => {s.checked = false})" % name)

    def set_value(self, value: Union[str, primitives.JsDataModel] = None, name: Union[str, primitives.JsDataModel] = None):
        """ """
        name = JsUtils.jsConvertData(name or self.component.input.attr["name"], None)
        if not value:
            return self.uncheck_all(name).extend(self.check())

        value = JsUtils.jsConvertData(value, None)
        return self.uncheck_all(name).extend(JsUtils.jsWrap(
            "let eltVal = %s; if(eltVal){let elt = document.body.querySelector('input[name=%s][data-content='+ eltVal +']'); if(elt !== null){elt.checked = true}}" % (value, name)))


class CheckButton(JsPackage):

    def __init__(self, component: primitives.HtmlModel, js_code: str = None, setVar=True,
                 is_py_data: bool = True, page: primitives.PageModel = None):
        self.varName, self.varData, self.__var_def = js_code, "", None
        self.component, self.page = component, page
        self._js, self._jquery = [], None

    def checked(self, color: Union[str, primitives.JsDataModel] = None):
        """Set the status of the button component to checked.

        Usage::

          c3 = page.ui.buttons.check(False, label="C3", icon="fas fa-align-center")
          page.ui.button("click").click([c3.js.checked()])

        :param color: Optional. The font color in the component. Default inherit
        """
        times = self.component.options.icon_not_check.split(" ")[-1]
        check = self.component.options.icon_check.split(" ")[-1]
        return JsObjects.JsObjects.get(
            "%s.querySelector('i').classList.replace('%s', '%s'); %s.querySelector('i').style.color = %s" % (
                self.component.dom.varName, times, check, self.component.dom.varName,
                JsUtils.jsConvertData(color, None) or self.page.theme.success.base))

    def unchecked(self, color: Union[str, primitives.JsDataModel] = None):
        """Set the status of the button component to unchecked.

        Usage::

          c3 = page.ui.buttons.check(False, label="C3", icon="fas fa-align-center")
          page.ui.button("click").click([c3.js.unchecked()])

        :param color: Optional. The font color in the component. Default inherit
        """
        times = self.component.options.icon_not_check.split(" ")[-1]
        check = self.component.options.icon_check.split(" ")[-1]
        return JsObjects.JsObjects.get(
            "%s.querySelector('i').classList.replace('%s', '%s'); %s.querySelector('i').style.color = %s" % (
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
        """Return the content of the component"""
        return JsHtml.ContentFormatters(self.page, "%s.innerHTML" % self.varName)

    def set_text(self, value: Union[str, primitives.JsDataModel]):
        """Set the text of the component.

        :param value: The text to be set
        """
        value = JsUtils.jsConvertData(value, None)
        return JsObjects.JsObjects.get("%s.innerHTML = %s" % (self.varName, value))

    def set_url(self, value: str, target: str = '_blank'):
        """Set the URL information of the item component.

        Usage::

          item.js.set_url("https://stackoverflow.com")

        `w3schools <https://www.w3schools.com/tags/att_a_href.asp>`_

        :param value: The url link
        :param target: Optional. The target mode of the link component
        """
        value = JsUtils.jsConvertData(value, None)
        target = JsUtils.jsConvertData(target, None)
        return JsObjects.JsObjects.get("%s.href = %s; %s.setAttribute('target', %s)" % (
            self.varName, value, self.varName, target))


class Switch(JsPackage):

    def __init__(self, component: primitives.HtmlModel, js_code: str = None, set_var: bool = True,
                 is_py_data: bool = True, page: primitives.PageModel = None):
        self.htmlCode = js_code if js_code is not None else component.html_code
        self.varName, self.varData, self.__var_def = "document.getElementById('%s')" % self.htmlCode, "", None
        self.component, self.page = component, page
        self._js, self._jquery = [], None

    def toggle(self):
        """Simulate a click event on the component"""
        return JsObjects.JsObjects.get(self.component.switch.click())

    def val(self, data: Union[bool, primitives.JsDataModel]):
        """Set the value for the switch.

        :param data: Flag to specify the state for the switch
        """
        data = JsUtils.jsConvertData(data, None)
        return JsObjects.JsObjects.get('''%(varName)s.querySelector('input').checked = %(flag)s; 
if(%(flag)s) {%(varName)s.querySelector('p').innerHTML = %(htmlCode)s_data.on}
else {%(varName)s.querySelector('p').innerHTML = %(htmlCode)s_data.off}''' % {
    "varName": self.varName, "flag": data, "htmlCode": self.htmlCode})

    def false(self):
        """Set the switch component to False"""
        return JsObjects.JsObjects.get(
            "%s.querySelector('input').checked = false; %s.querySelector('p').innerHTML = %s_data.off" % (
                self.varName, self.varName, self.htmlCode))

    def true(self):
        """Set the switch component to True"""
        return JsObjects.JsObjects.get(
            "%s.querySelector('input').checked = true; %s.querySelector('p').innerHTML = %s_data.on" % (
                self.varName, self.varName, self.htmlCode))


class Alerts(JsPackage):

    def __init__(self, component, js_code: str = None, set_var: bool = True,
                 is_py_data: bool = True, page: primitives.PageModel = None):
        self.htmlCode = js_code if js_code is not None else component.html_code
        self.varName, self.varData, self.__var_def = "document.getElementById('%s')" % self.htmlCode, "", None
        self.component, self.page = component, page
        self._js, self._jquery = [], None

    def replay(self, time: int = None):
        """

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
        self.htmlCode = js_code if js_code is not None else component.html_code
        self.varName, self.varData, self.__var_def = "document.getElementById('%s')" % self.htmlCode, "", None
        self.component, self.page = component, page
        self._js, self._jquery = [], None

    def reset(self):
        """  """
        return JsObjects.JsVoid('''%(varName)s.innerHTML = '' ''' % {'varName': self.varName})


class Chat(JsPackage):

    def __init__(self, component: primitives.HtmlModel, js_code: str = None, set_var: bool = True,
                 is_py_data: bool = True, page: primitives.PageModel = None):
        self.htmlCode = js_code if js_code is not None else component.html_code
        self.varName, self.varData, self.__var_def = "document.getElementById('%s')" % self.htmlCode, "", None
        self.component, self.page = component, page
        self._js, self._jquery = [], None

    def add(self, message):
        return JsObjects.JsVoid('''%(builder)s; %(counter)s''' % {
          "builder": self.component.build(message),
          'counter': self.component.dom.querySelector(' [name=count]').innerText(1, append=True, val_type=int).r})


class Room(JsPackage):

    def __init__(self, component: primitives.HtmlModel, js_code: str = None, set_var: bool = True,
                 is_py_data: bool = True, page: primitives.PageModel = None):
        self.htmlCode = js_code if js_code is not None else component.html_code
        self.varName, self.varData, self.__var_def = "document.getElementById('%s')" % self.htmlCode, "", None
        self.component, self.page = component, page
        self._js, self._jquery = [], None

    def typing(self):
        """Display dots in the status to inform user is typing. """
        return self.component.dom.querySelector("div[name=dots]").show(duration=3000)


class Buttons(JsPackage):

    def __init__(self, component: primitives.HtmlModel, js_code: str = None, setVar=True,
                 is_py_data: bool = True, page: primitives.PageModel = None):
        self.varName, self.varData, self.__var_def = js_code, "", None
        self.component, self.page = component, page
        self._js, self._jquery = [], None

    def set_value(self, value):
        """Set the component value.

        :param value: Initial value as a string (or url param component)
        """
        value = JsUtils.jsConvertData(value, None)
        delimiter = JsUtils.jsConvertData(self.component.options.delimiter, None)
        return JsObjects.JsObjects.get(
            "%s.querySelectorAll('button').forEach(function(d){if(%s.split(%s).includes(d.innerText)){d.classList.add('%s')}})" % (
                self.component.dom.varName, value, delimiter, self.component.options.selected))

    def loader(self, status: bool, dom):
        """Add loader / spin icon to the button component.

        Usage::

                js_funcs.insert(0, self.js.loader(True, JsUtils.jsWrap("event.target")))
                js_funcs.append(self.js.loader(False, JsUtils.jsWrap("event.target")))

        :param status: A flag to enable / disable the loading spinner
        :param dom: A dom / button component
        """
        loader = self.page.icons.get("loader")
        target = JsUtils.jsConvertData(dom, None)
        self.component.require.add(loader['icon_family'])
        if status:
            return JsUtils.jsWrap('''if(%(target)s.getAttribute('loading') != 'true'){
    let icon = document.createElement("i"); icon.className = '%(icon)s %(loading)s'; 
    %(target)s.setAttribute('loading', 'true'); %(target)s.prepend(icon);
}''' % {"icon": loader["icon"], "target": target, "loading": self.component.style_refs["html-button-loader"]})

        return JsUtils.jsWrap('''if(%(target)s.getAttribute('loading') == 'true'){
%(target)s.firstChild.remove() ; %(target)s.setAttribute('loading', 'false');}''' % {"target": target})

    def get(self, i: int):
        """Get a button component based on its index in the group

        :param i: Component index starting from 0
        """
        return JsNodeDom.JsDoms.get('document.querySelectorAll("div#%s button")[%s]' % (self.component.html_code, i))

    def disable(self, dom):
        """Disable the selected component to the group.

        :param dom: A dom / button component
        """
        return JsUtils.jsWrap("%s.disabled = true" % JsUtils.jsConvertData(dom, None))

    def filterByVal(self, dom_val, value, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
        """Filter process by selected only the one validating the rule.

        Usage::

            bs = page.ui.menus.buttons(["Button", "Button 2", "Button 3"])
            bs.click([bs.js.filterByVal(pk.events.innerText, "Button 3", [page.js.alert(bs.dom.content)])])

        :param dom_val: HTML component
        :param value: Value used to filter the process
        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        """
        dom_val = JsUtils.jsConvertData(dom_val, None)
        value = JsUtils.jsConvertData(value, None)
        return JsUtils.jsWrap('''if(%s == %s){%s}''' % (dom_val, value, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))
