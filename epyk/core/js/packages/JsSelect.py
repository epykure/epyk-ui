"""
Wrapper to the Jquery UI package

https://api.jqueryui.com/
"""

import json

from epyk.core.js import JsUtils

from epyk.core.js.objects import JsNodeDom
from epyk.core.js.packages import JsPackage
from epyk.core.js.primitives import JsObjects
from epyk.core.js.packages import JsQuery
from epyk.core.js.packages import JsQueryUi


class JSelect(JsPackage):
  lib_alias = {"js": 'jqueryui', 'css': 'jqueryui'}
  lib_selector = 'jQuery("body")'
  lib_set_var = False

  def __init__(self, htmlObj, varName=None, setVar=True, isPyData=True, report=None):
    self.htmlId = varName if varName is not None else htmlObj.htmlId
    self.varName, self.varData, self.__var_def = "document.getElementById('%s')" % self.htmlId, "", None
    self._src, self._report = htmlObj, report
    self._js = []
    self._jquery, self._jquery_ui = None, None

  @property
  def val(self):
    """

    :return:
    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s.value, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
      self.htmlId, self.varName))

  @property
  def content(self):
    return JsObjects.JsObjects.get("%s.value" % self.varName)

  @property
  def events(self):
    """

    :rtype: JsNodeDom.JsDomEvents
    :return:
    """
    return JsNodeDom.JsDomEvents(self._src)

  @property
  def jquery(self):
    """

    :return:
    :rtype: JsQuery.JQuery
    """
    if self._jquery is None:
      self._jquery = JsQuery.JQuery(src=self._src, selector=JsQuery.decorate_var("#%s" % self._src.htmlId))
    return self._jquery

  @property
  def jquery_ui(self):
    """

    :return:
    :rtype: JsQuery.JQuery
    """
    if self._jquery_ui is None:
      self._jquery_ui = JsQueryUi.JQueryUI(self._src, selector=JsQuery.decorate_var("#%s" % self._src.htmlId))
    return self._jquery_ui

  def ajaxSelectPicker(self, options):
    """
    Process the raw data returned from a request. The following arguments are passed to this callback:

    Documentation
    https://github.com/truckingsim/Ajax-Bootstrap-Select

    Example
    s.dom.ajaxSelectPicker({"values": "a, b, c", "ajax": {
    "url": 'https://jsonplaceholder.typicode.com/posts', "type": "POST", "dataType": "json",
    "data": {"q": "{{{q}}}"}}, 'preserveSelected': False, 'log': 2, 'preprocessData':
        'function(data) {return [{text: "C", value: "C"}, {text: "D", value: "D"}]}', "locale": {
    "emptyTitle": "Select and Begin Typing"}})])

    :param options:
    :return:
    """
    self._src.cssImport.add('select-ajax')
    self._src.jsImports.add('select-ajax')
    opts = []
    for k, v in options.items():
      if not isinstance(v, (dict, int)) and v.startswith("function"):
        opts.append("%s: %s" % (k, v))
      else:
        opts.append("%s: %s" % (k, json.dumps(v)))
    return "%s.selectpicker().ajaxSelectPicker({%s})" % (self.jquery.varId, ", ".join(opts))

  def __str__(self):
    """
    The str() method return the variable Javascript reference of the variable.

    According to the variable definition it can be either its name or its value

    :return: A Javascript reference
    """
    return self.htmlId
