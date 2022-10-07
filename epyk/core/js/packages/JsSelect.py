#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

from epyk.core.js import JsUtils
from epyk.core.js.objects import JsNodeDom
from epyk.core.js.packages import JsPackage
from epyk.core.js.primitives import JsObjects
from epyk.core.js.packages import JsQuery
from epyk.core.js.statements import JsIf


class JsSelectItem:

  def __init__(self, selector):
    self._selector = selector

  def css(self, attrs):
    """
    Set CSS properties to the option item.

    Related Pages:

      https://www.w3schools.com/tags/tag_option.asp

    :param attrs: Dictionary. The CSS attributes.
    """
    return JsObjects.JsObjects.get("%s.css(%s)" % (self._selector, attrs))

  def prop(self, name, data):
    """
    Set a specific property / option to the selection Picker object.

    :param name: String. optional. The option name of the new DOM component. Default the value.
    :param data: String or Js Object. The value of the item to be removed from the list.
    """
    data = JsUtils.jsConvertData(data, None)
    return JsObjects.JsObjects.get('%s.prop("%s", %s)' % (self._selector, name, data))


class JSelect(JsPackage):
  lib_alias = {"js": 'jqueryui', 'css': 'jqueryui'}
  lib_selector = 'jQuery("body")'
  lib_set_var = False

  def __init__(self, component, js_code=None, set_var=True, is_py_data=True, page=None):
    self.htmlCode = js_code if js_code is not None else component.htmlCode
    self.varName, self.varData, self.__var_def = "document.getElementById('%s')" % self.htmlCode, "", None
    self.component, self.page = component, page
    self._js, self._jquery = [], None

  def val(self, data=None):
    """
    You can set the selected value by calling the val method on the element.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/methods/

    :param data: String | Js Object. The value of the item to be removed from the list.
    """
    if data is None:
      return JsObjects.JsObjects.get("%s.val()" % self.component.dom.jquery.varId)

    data = JsUtils.jsConvertData(data, None)
    return JsObjects.JsObjects.get("%s.val(%s).selectpicker('refresh')" % (self.component.dom.jquery.varId, data))

  def prop(self, name, data):
    """
    Set a specific property / option to the selection Picker object.

    :param name: String. optional. The option name of the new DOM component. Default the value.
    :param data: String | Js Object. The value of the item to be removed from the list.
    """
    data = JsUtils.jsConvertData(data, None)
    return JsObjects.JsObjects.get('%s.prop("%s", %s)' % (self.component.dom.jquery.varId, name, data))

  def empty(self):
    """
    Empty the selection component.
    Using this method will force the refresh of the component to update it on the page.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/methods/
    """
    if 'multiple' in self.component.attr:
      return JsObjects.JsObjects.get("%s.val([]).selectpicker('refresh')" % self.component.dom.jquery.varId)

    return JsObjects.JsObjects.get("%s.val('').selectpicker('refresh')" % self.component.dom.jquery.varId)

  def remove(self, data, refresh=True):
    """
    Remove an item from the list based on its value (and not necessarly its visible name).

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/methods/

    :param data: String or Js Object. The value of the item to be removed from the list.
    :param refresh: Boolean. Optional. Refresh the list after the item removal. (default true).
    """
    data = JsUtils.jsConvertData(data, None)
    if refresh:
      return JsObjects.JsObjects.get('%s.find("option[value="+ %s +"]").remove(); %s' % (
        self.component.dom.jquery.varId, data, self.refresh()))

    return JsObjects.JsObjects.get('%s.find("option[value="+ %s +"]").remove()' % (
      self.component.dom.jquery.varId, data))

  def mobile(self):
    """
    Enable mobile scrolling by calling $('.selectpicker').selectpicker('mobile').
    This enables the device's native menu for select menus.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/methods/
    """
    return JsObjects.JsObjects.get("%s.selectpicker('mobile')" % self.component.dom.jquery.varId)

  def add(self, value, name=None, refresh=True, selected=False):
    """
    Add an item to the list.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/methods/

    TODO: Manage correctly the spaces in the value.

    :param value: String. The option value of the new DOM component.
    :param name: String. optional. The option name of the new DOM component. Default the value.
    :param refresh: Boolean. Optional. Refresh the list after the item removal. (default true).
    :param selected: Boolean. Optional. Specify if the option needs to be selected.
    """
    name = name or value
    name = JsUtils.jsConvertData(name, None)
    value = JsUtils.jsConvertData(value, None)
    selection = self.val(value) if selected else ""
    if refresh:
      return JsObjects.JsObjects.get("%s.append('<option value='+ %s +'>'+ %s +'</option>'); %s; %s" % (
        self.component.dom.jquery.varId, value, name, self.refresh(), selection))

    return JsObjects.JsObjects.get("%s.append('<option value='+ %s +'>'+ %s +'</option>'); %s" % (
      self.component.dom.jquery.varId, value, name, selection))

  def item(self, value):
    """
    Search an item from the select box.

    :param value: String. The value of the options.
    """
    value = JsUtils.jsConvertData(value, None)
    return JsSelectItem("%s.find('option[value='+ %s +']')" % (self.component.dom.jquery.varId, value))

  def deselectAll(self):
    """
    This will deselect all items in a multi-select.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/methods/
    """
    return JsObjects.JsObjects.get("%s.selectpicker('deselectAll')" % self.component.dom.jquery.varId)

  def selectAll(self):
    """
    This will select all items in a multi-select.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/methods/
    """
    return JsObjects.JsObjects.get("%s.selectpicker('selectAll')" % self.component.dom.jquery.varId)

  def selectIndex(self, i: int):
    """
    This will select the option at the specified index.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/methods/
    """
    return JsObjects.JsObjects.get("%(jqid)s.find('option')[%(index)s].setAttribute('selected', 'selected')" % {
      'jqid': self.component.dom.jquery.varId, 'index': i})

  def render(self):
    """
    You can force a re-render of the bootstrap-select ui with the render method.
    This is useful if you programmatically change any underlying values that affect the layout of the element.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/methods/
    """
    return JsObjects.JsObjects.get("%s.selectpicker('render')" % self.component.dom.jquery.varId)

  def refresh(self):
    """
    Force the refresh of the select Picker object.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/methods/
    """
    return JsObjects.JsObjects.get("%s.selectpicker('refresh')" % self.component.dom.jquery.varId)

  def toggle(self):
    """
    Programmatically toggles the bootstrap-select menu open/closed.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/methods/
    """
    return JsObjects.JsObjects.get("%s.selectpicker('toggle')" % self.component.dom.jquery.varId)

  def hide(self):
    """
    To programmatically hide the bootstrap-select use the hide method (this only affects the visibility of
    the bootstrap-select itself).

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/methods/
    """
    return JsObjects.JsObjects.get("%s.selectpicker('hide')" % self.component.dom.jquery.varId)

  def show(self):
    """
    To programmatically show the bootstrap-select use the show method (this only affects the visibility of
    the bootstrap-select itself).

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/methods/
    """
    return JsObjects.JsObjects.get("%s.selectpicker('show')" % self.component.dom.jquery.varId)

  def setStyle(self, class_name, event=None):
    """
    To programmatically show the bootstrap-select use the show method (this only affects the visibility
    of the bootstrap-select itself).

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/methods/

    :param class_name: String.
    :param event: List. Set of Javascript function to trigger on this event
    """
    if event is None:
      return JsObjects.JsObjects.get("%s.selectpicker('setStyle', '%s')" % (
        self.component.dom.jquery.varId, class_name))

    return JsObjects.JsObjects.get("%s.selectpicker('setStyle', '%s', '%s')" % (
      self.component.dom.jquery.varId, class_name, event))

  def disable(self, flag):
    """
    Disable the selection component.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/methods/

    :param flag: Boolean. A flag to specify the status of the component.
    """
    flag = JsUtils.jsConvertData(flag, None)
    return JsObjects.JsObjects.get("%s.prop('disabled', %s)" % (self.component.dom.jquery.varId, flag))

  @property
  def search(self):
    """
    Get the selected content from the Select component

    Usage::

      b.click([rptObj.js.console.log(s.dom.content)])
    """
    return JsObjects.JsObjects.get("this.plugin.query")

  @property
  def events(self):
    """

    """
    return JsNodeDom.JsDomEvents(component=self.component)

  @property
  def jquery(self):
    """
    jQuery UI is a curated set of user interface interactions, effects, widgets, and themes
    built on top of the jQuery JavaScript Library.
    Whether you're building highly interactive web applications or you just need to add a date picker to a form control,
    jQuery UI is the perfect choice.

    Related Pages:

      https://jqueryui.com/

    :rtype: JsQuery.JQuery
    """
    if self._jquery is None:
      self._jquery = JsQuery.JQuery(
        component=self.component, selector=JsQuery.decorate_var("#%s" % self.component.htmlCode))
    return self._jquery

  def ajaxSelectPicker(self, options):
    """
    Process the raw data returned from a request. The following arguments are passed to this callback:

    Related Pages:

      https://github.com/truckingsim/Ajax-Bootstrap-Select

    Usage::

      s.dom.ajaxSelectPicker({"values": "a, b, c", "ajax": {
    "url": 'https://jsonplaceholder.typicode.com/posts', "type": "POST", "dataType": "json",
    "data": {"q": "{{{q}}}"}}, 'preserveSelected': False, 'log': 2, 'preprocessData':
        'function(data) {return [{text: "C", value: "C"}, {text: "D", value: "D"}]}', "locale": {
    "emptyTitle": "Select and Begin Typing"}})])

    :param options:
    """
    self.component.cssImport.add('ajax-bootstrap-select')
    self.component.jsImports.add('ajax-bootstrap-select')
    opts = []
    for k, v in options.items():
      if not isinstance(v, (dict, int)) and v.startswith("function"):
        opts.append("%s: %s" % (k, v))
      elif isinstance(v, dict):
        tmp_dict = []
        for sk, sv in v.items():
          if not isinstance(sv, (dict, int)) and (sv.startswith("function") or sv.startswith("(function") or sv.startswith('"')):
            tmp_dict.append("%s: %s" % (sk, sv))
          else:
            tmp_dict.append("%s: %s" % (sk, json.dumps(sv)))
        opts.append("%s: {%s}" % (k, ", ".join(tmp_dict)))
      else:
        opts.append("%s: %s" % (k, json.dumps(v)))
    return "%s.selectpicker().ajaxSelectPicker({%s})" % (self.jquery.varId, ", ".join(opts))

  def if_(self, rule, js_funcs):
    """
    Generic if statement for an select component.

    :param rule: String.
    :param js_funcs: List | String. Javascript functions.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    return JsIf.JsIf(rule, js_funcs)

  def __str__(self):
    """
    The str() method return the variable Javascript reference of the variable.

    According to the variable definition it can be either its name or its value.

    :return: A Javascript reference
    """
    return self.htmlCode
