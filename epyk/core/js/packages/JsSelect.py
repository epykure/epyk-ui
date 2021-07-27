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
    Description:
    ------------
    Set CSS properties to the option item.

    Related Pages:

      https://www.w3schools.com/tags/tag_option.asp

    Attributes:
    ----------
    :param attrs: Dictionary. The CSS attributes.
    """
    return JsObjects.JsObjects.get("%s.css(%s)" % (self._selector, attrs))

  def prop(self, name, jsData):
    """
    Description:
    ------------
    Set a specific property / option to the selection Picker object.

    Attributes:
    ----------
    :param name: String. optional. The option name of the new DOM component. Default the value.
    :param jsData: String or Js Object. The value of the item to be removed from the list.
    """
    jsData = JsUtils.jsConvertData(jsData, None)
    return JsObjects.JsObjects.get('%s.prop("%s", %s)' % (self._selector, name, jsData))


class JSelect(JsPackage):
  lib_alias = {"js": 'jqueryui', 'css': 'jqueryui'}
  lib_selector = 'jQuery("body")'
  lib_set_var = False

  def __init__(self, htmlObj, varName=None, setVar=True, isPyData=True, report=None):
    self.htmlCode = varName if varName is not None else htmlObj.htmlCode
    self.varName, self.varData, self.__var_def = "document.getElementById('%s')" % self.htmlCode, "", None
    self._src, self._report = htmlObj, report
    self._js, self._jquery = [], None

  def val(self, jsData=None):
    """
    Description:
    ------------
    You can set the selected value by calling the val method on the element.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/methods/

    Attributes:
    ----------
    :param jsData: String | Js Object. The value of the item to be removed from the list.
    """
    if jsData is None:
      return JsObjects.JsObjects.get("%s.val()" % self._src.dom.jquery.varId)

    jsData = JsUtils.jsConvertData(jsData, None)
    return JsObjects.JsObjects.get("%s.val(%s).selectpicker('refresh')" % (self._src.dom.jquery.varId, jsData))

  def prop(self, name, jsData):
    """
    Description:
    ------------
    Set a specific property / option to the selection Picker object.

    Attributes:
    ----------
    :param name: String. optional. The option name of the new DOM component. Default the value.
    :param jsData: String | Js Object. The value of the item to be removed from the list.
    """
    jsData = JsUtils.jsConvertData(jsData, None)
    return JsObjects.JsObjects.get('%s.prop("%s", %s)' % (self._src.dom.jquery.varId, name, jsData))

  def empty(self):
    """
    Description:
    ------------
    Empty the selection component.
    Using this method will force the refresh of the component to update it on the page.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/methods/
    """
    if 'multiple' in self._src.attr:
      return JsObjects.JsObjects.get("%s.val([]).selectpicker('refresh')" % (self._src.dom.jquery.varId))

    return JsObjects.JsObjects.get("%s.val('').selectpicker('refresh')" % (self._src.dom.jquery.varId))

  def remove(self, jsData, refresh=True):
    """
    Description:
    ------------
    Remove an item from the list based on its value (and not necessarly its visible name).

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/methods/

    Attributes:
    ----------
    :param jsData: String or Js Object. The value of the item to be removed from the list.
    :param refresh: Boolean. Optional. Refresh the list after the item removal. (default true).
    """
    jsData = JsUtils.jsConvertData(jsData, None)
    if refresh:
      return JsObjects.JsObjects.get('%s.find("option[value="+ %s +"]").remove(); %s' % (
        self._src.dom.jquery.varId, jsData, self.refresh()))

    return JsObjects.JsObjects.get('%s.find("option[value="+ %s +"]").remove()' % (self._src.dom.jquery.varId, jsData))

  def mobile(self):
    """
    Description:
    ------------
    Enable mobile scrolling by calling $('.selectpicker').selectpicker('mobile').
    This enables the device's native menu for select menus.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/methods/
    """
    return JsObjects.JsObjects.get("%s.selectpicker('mobile')" % self._src.dom.jquery.varId)

  def add(self, value, name=None, refresh=True, selected=False):
    """
    Description:
    ------------
    Add an item to the list.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/methods/

    TODO: Manage correctly the spaces in the value.

    Attributes:
    ----------
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
        self._src.dom.jquery.varId, value, name, self.refresh(), selection))

    return JsObjects.JsObjects.get("%s.append('<option value='+ %s +'>'+ %s +'</option>'); %s" % (
      self._src.dom.jquery.varId, value, name, selection))

  def item(self, value):
    """
    Description:
    ------------
    Search an item from the select box.

    Attributes:
    ----------
    :param value: String. The value of the options.
    """
    value = JsUtils.jsConvertData(value, None)
    return JsSelectItem("%s.find('option[value='+ %s +']')" % (self._src.dom.jquery.varId, value))

  def deselectAll(self):
    """
    Description:
    ------------
    This will deselect all items in a multi-select.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/methods/
    """
    return JsObjects.JsObjects.get("%s.selectpicker('deselectAll')" % self._src.dom.jquery.varId)

  def selectAll(self):
    """
    Description:
    ------------
    This will select all items in a multi-select.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/methods/
    """
    return JsObjects.JsObjects.get("%s.selectpicker('selectAll')" % self._src.dom.jquery.varId)

  def selectIndex(self, i):
    """
    Description:
    ------------
    This will select the option at the specified index.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/methods/
    """
    return JsObjects.JsObjects.get("%(jqid)s.find('option')[%(index)s].setAttribute('selected', 'selected')" % {
      'jqid': self._src.dom.jquery.varId, 'index': i})

  def render(self):
    """
    Description:
    ------------
    You can force a re-render of the bootstrap-select ui with the render method.
    This is useful if you programmatically change any underlying values that affect the layout of the element.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/methods/
    """
    return JsObjects.JsObjects.get("%s.selectpicker('render')" % self._src.dom.jquery.varId)

  def refresh(self):
    """
    Description:
    ------------
    Force the refresh of the select Picker object.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/methods/
    """
    return JsObjects.JsObjects.get("%s.selectpicker('refresh')" % self._src.dom.jquery.varId)

  def toggle(self):
    """
    Description:
    ------------
    Programmatically toggles the bootstrap-select menu open/closed.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/methods/
    """
    return JsObjects.JsObjects.get("%s.selectpicker('toggle')" % self._src.dom.jquery.varId)

  def hide(self):
    """
    Description:
    ------------
    To programmatically hide the bootstrap-select use the hide method (this only affects the visibility of
    the bootstrap-select itself).

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/methods/
    """
    return JsObjects.JsObjects.get("%s.selectpicker('hide')" % self._src.dom.jquery.varId)

  def show(self):
    """
    Description:
    ------------
    To programmatically show the bootstrap-select use the show method (this only affects the visibility of
    the bootstrap-select itself).

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/methods/
    """
    return JsObjects.JsObjects.get("%s.selectpicker('show')" % self._src.dom.jquery.varId)

  def setStyle(self, class_name, event=None):
    """
    Description:
    ------------
    To programmatically show the bootstrap-select use the show method (this only affects the visibility
    of the bootstrap-select itself).

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/methods/

    Attributes:
    ----------
    :param class_name: String.
    :param event: List. Set of Javascript function to trigger on this event
    """
    if event is None:
      return JsObjects.JsObjects.get("%s.selectpicker('setStyle', '%s')" % (
        self._src.dom.jquery.varId, class_name))

    return JsObjects.JsObjects.get("%s.selectpicker('setStyle', '%s', '%s')" % (
      self._src.dom.jquery.varId, class_name, event))

  def disable(self, flag):
    """
    Description:
    ------------
    Disable the selection component.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/methods/

    Attributes:
    ----------
    :param flag: Boolean. A flag to specify the status of the component.
    """
    flag = JsUtils.jsConvertData(flag, None)
    return JsObjects.JsObjects.get("%s.prop('disabled', %s)" % (self._src.dom.jquery.varId, flag))

  @property
  def search(self):
    """
    Description:
    ------------
    Get the selected content from the Select component

    Usage::

      b.click([rptObj.js.console.log(s.dom.content)])
    """
    return JsObjects.JsObjects.get("this.plugin.query")

  @property
  def events(self):
    """
    Description:
    ------------

    """
    return JsNodeDom.JsDomEvents(self._src)

  @property
  def jquery(self):
    """
    Description:
    ------------
    jQuery UI is a curated set of user interface interactions, effects, widgets, and themes
    built on top of the jQuery JavaScript Library.
    Whether you're building highly interactive web applications or you just need to add a date picker to a form control,
    jQuery UI is the perfect choice.

    Related Pages:

      https://jqueryui.com/

    :rtype: JsQuery.JQuery
    """
    if self._jquery is None:
      self._jquery = JsQuery.JQuery(src=self._src, selector=JsQuery.decorate_var("#%s" % self._src.htmlCode))
    return self._jquery

  def ajaxSelectPicker(self, options):
    """
    Description:
    ------------
    Process the raw data returned from a request. The following arguments are passed to this callback:

    Related Pages:

      https://github.com/truckingsim/Ajax-Bootstrap-Select

    Usage::

      s.dom.ajaxSelectPicker({"values": "a, b, c", "ajax": {
    "url": 'https://jsonplaceholder.typicode.com/posts', "type": "POST", "dataType": "json",
    "data": {"q": "{{{q}}}"}}, 'preserveSelected': False, 'log': 2, 'preprocessData':
        'function(data) {return [{text: "C", value: "C"}, {text: "D", value: "D"}]}', "locale": {
    "emptyTitle": "Select and Begin Typing"}})])

    Attributes:
    ----------
    :param options:
    """
    self._src.cssImport.add('ajax-bootstrap-select')
    self._src.jsImports.add('ajax-bootstrap-select')
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

  def if_(self, jsRule, jsFncs):
    """
    Description:
    ------------
    Generic if statement for an select component.

    Attributes:
    ----------
    :param jsRule: String.
    :param jsFncs: List | String. Javascript functions.
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    return JsIf.JsIf(jsRule, jsFncs)

  def __str__(self):
    """
    Description:
    ------------
    The str() method return the variable Javascript reference of the variable.

    According to the variable definition it can be either its name or its value.

    :return: A Javascript reference
    """
    return self.htmlCode
