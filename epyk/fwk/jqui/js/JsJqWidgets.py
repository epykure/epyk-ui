#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.js.packages import JsPackage
from epyk.core.js.primitives import JsObjects
from epyk.core.js import JsUtils


class Accordion(JsPackage):

  def __init__(self, component, js_code=None, set_var=True, is_py_data=True, page=None):
    self.varName, self.varData, self.__var_def = js_code, "", None
    self.component, self.page = component, page
    self._js, self._jquery = [], None

  def destroy(self):
    """   Removes the accordion functionality completely. This will return the element back to its pre-init state.

    Related Pages:

      https://api.jqueryui.com/accordion/
    """
    return JsUtils.jsWrap("%s.accordion('destroy')" % self.component.var)

  def disable(self):
    """   Disables the accordion.

    Related Pages:

      https://api.jqueryui.com/accordion/
    """
    return JsUtils.jsWrap("%s.accordion('disable')" % self.component.var)

  def enable(self):
    """   Enables the accordion.

    Related Pages:

      https://api.jqueryui.com/accordion/
    """
    return JsUtils.jsWrap("%s.accordion('enable')" % self.component.var)

  def options(self, option_name=None):
    """   Gets / Set the value currently associated with the specified optionName.
    Or gets an object containing key/value pairs representing the current tabs options hash.

    Related Pages:

      https://api.jqueryui.com/accordion/
 
    :param option_name: String. Optional. The name of the option to set.
    """
    if option_name is None:
      return JsObjects.JsObjects.get("%s.accordion('option')" % self.component.var)

    option_name = JsUtils.jsConvertData(option_name, None)
    return JsObjects.JsObjects.get("%s.accordion('option', %s)" % (self.component.var, option_name))

  def set_options(self, option_name, value):
    """   Sets the value of the accordion option associated with the specified.

    Related Pages:

      https://api.jqueryui.com/accordion/
 
    :param option_name: String. The name of the option to set.
    :param value: Object. A value to set for the option.
    """
    option_name = JsUtils.jsConvertData(option_name, None)
    value = JsUtils.jsConvertData(value, None)
    return JsObjects.JsObjects.get("%s.accordion('option', %s, %s)" % (self.component.var, option_name, value))

  def refresh(self):
    """   Process any tabs that were added or removed directly in the DOM and recompute the height of the tab panels.
    Related Pages:

      https://api.jqueryui.com/accordion/
    """
    return JsUtils.jsWrap("%s.accordion('refresh')" % self.component.var)

  def on(self, event, js_funcs, profile=None):
    """   

    Related Pages:

      https://api.jqueryui.com/accordion/
 
    :param event: String. The JavaScript DOM source for the event (can be a sug item).
    :param js_funcs: String | List. The Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    event = JsUtils.jsConvertData(event, None)
    return JsUtils.jsWrap("%s.on(%s, function(event, ui){%s})" % (
      self.component.input.dom.varName, event, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))

  def onCreate(self, js_funcs, profile=None):
    """  
    Triggered directly before a panel is activated. Can be canceled to prevent the panel from activating.

    Related Pages:

      https://api.jqueryui.com/accordion/
 
    :param js_funcs: String | List. The Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    return self.on("accordioncreate", js_funcs, profile)

  def onActivate(self, js_funcs, profile=None):
    """  
    Triggered after a panel has been activated (after animation completes). If the accordion was previously collapsed,

    Related Pages:

      https://api.jqueryui.com/accordion/
 
    :param js_funcs: String | List. The Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    return self.on("accordionactivate", js_funcs, profile)

  def onBeforeActivate(self, js_funcs, profile=None):
    """  
    Triggered directly before a panel is activated. Can be canceled to prevent the panel from activating.

    Related Pages:

      https://api.jqueryui.com/accordion/
 
    :param js_funcs: String | List. The Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    return self.on("accordionbeforeactivate", js_funcs, profile)


class Tabs(JsPackage):

  def __init__(self, component, js_code=None, set_var=True, is_py_data=True, page=None):
    self.varName, self.varData, self.__var_def = js_code, "", None
    self.component, self.page = component, page
    self._js, self._jquery = [], None

  def destroy(self):
    """   Removes the tabs functionality completely. This will return the element back to its pre-init state.

    Related Pages:

      https://api.jqueryui.com/tabs/
    """
    return JsUtils.jsWrap("%s.tabs('destroy')" % self.component.var)

  def disable(self, i=None):
    """   Disables all tabs. This signature does not accept any arguments.

    Related Pages:

      https://api.jqueryui.com/tabs/
 
    :param i: Array<Integer>. Optional. The zero-based index of the tab to disable.
    """
    if i is None:
      return JsUtils.jsWrap("%s.tabs('disable')" % self.component.var)

    return JsUtils.jsWrap("%s.tabs('disable', %s)" % (self.component.var, i))

  def enable(self, i=None):
    """   Enables a tab.

    Related Pages:

      https://api.jqueryui.com/tabs/
 
    :param i: Array<Integer>. Optional. The zero-based index of the tab to disable.
    """
    if i is None:
      return JsUtils.jsWrap("%s.tabs('enable')" % self.component.var)

    return JsUtils.jsWrap("%s.tabs('enable', %s)" % (self.component.var, i))

  def load(self, value):
    """   Loads the panel content of a remote tab.

    Related Pages:

      https://api.jqueryui.com/tabs/
 
    :param value: Number | String. The href of the tab to load.
    """
    value = JsUtils.jsConvertData(value, None)
    return JsUtils.jsWrap("%s.tabs('load', %s)" % (self.component.var, value))

  def options(self, option_name=None):
    """   Gets / Set the value currently associated with the specified optionName.
    Or gets an object containing key/value pairs representing the current tabs options hash.

    Related Pages:

      https://api.jqueryui.com/tabs/
 
    :param option_name: String. Optional. The name of the option to set.
    """
    if option_name is None:
      return JsObjects.JsObjects.get("%s.tabs('option')" % self.component.var)

    option_name = JsUtils.jsConvertData(option_name, None)
    return JsObjects.JsObjects.get("%s.tabs('option', %s)" % (self.component.var, option_name))

  def set_options(self, option_name, value):
    """   Sets the value of the tabs option associated with the specified.

    Related Pages:

      https://api.jqueryui.com/tabs/
 
    :param option_name: String. The name of the option to set.
    :param value: Object. A value to set for the option.
    """
    option_name = JsUtils.jsConvertData(option_name, None)
    value = JsUtils.jsConvertData(value, None)
    return JsObjects.JsObjects.get("%s.tabs('option', %s, %s)" % (self.component.var, option_name, value))

  def refresh(self):
    """   Process any tabs that were added or removed directly in the DOM and recompute the height of the tab panels.
    Related Pages:

      https://api.jqueryui.com/tabs/
    """
    return JsUtils.jsWrap("%s.tabs('refresh')" % self.component.var)

  def on(self, event, js_funcs, profile=None):
    """   

    Related Pages:

      https://api.jqueryui.com/tabs/
 
    :param event: String. The JavaScript DOM source for the event (can be a sug item).
    :param js_funcs: String | List. The Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    event = JsUtils.jsConvertData(event, None)
    return JsUtils.jsWrap("%s.on(%s, function(event, ui){%s})" % (
      self.component.input.dom.varName, event, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))

  def onCreate(self, js_funcs, profile=None):
    """  
    Triggered when the tabs are created.

    Related Pages:

      https://api.jqueryui.com/tabs/
 
    :param js_funcs: String | List. The Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    return self.on("tabscreate", js_funcs, profile)

  def onActivate(self, js_funcs, profile=None):
    """  
    Triggered after a tab has been activated (after animation completes).
    If the tabs were previously collapsed, ui.oldTab and ui.oldPanel will be empty jQuery objects.

    Related Pages:

      https://api.jqueryui.com/tabs/
 
    :param js_funcs: String | List. The Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    return self.on("tabsactivate", js_funcs, profile)

  def onBeforeActivate(self, js_funcs, profile=None):
    """  
    Triggered when a remote tab is about to be loaded, after the beforeActivate event.

    Related Pages:

      https://api.jqueryui.com/tabs/
 
    :param js_funcs: String | List. The Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    return self.on("tabsbeforeload", js_funcs, profile)

  def onBeforeLoad(self, js_funcs, profile=None):
    """  
    Triggered when a remote tab is about to be loaded, after the beforeActivate event.

    Related Pages:

      https://api.jqueryui.com/tabs/
 
    :param js_funcs: String | List. The Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    return self.on("tabsbeforeload", js_funcs, profile)

  def onLoad(self, js_funcs, profile=None):
    """  
    Triggered after a remote tab has been loaded.

    Related Pages:

      https://api.jqueryui.com/tabs/
 
    :param js_funcs: String | List. The Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    return self.on("tabsload", js_funcs, profile)
