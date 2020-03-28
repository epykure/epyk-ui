
import json

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
      "{%s: {value: %s, name: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
      self.htmlId, self.content, self.name))

  @property
  def content(self):
    """
    Get the selected content from the Select component

    Example
    b.click([rptObj.js.console.log(s.dom.content)])
    """
    return JsObjects.JsObjects.get("%s.value" % self.varName)

  @property
  def search(self):
    """
    Get the selected content from the Select component

    Example
    b.click([rptObj.js.console.log(s.dom.content)])
    """
    return JsObjects.JsObjects.get("this.plugin.query")

  @property
  def name(self):
    """
    Get the selected name / label from the Select component

    Example
    b.click([rptObj.js.console.log(s.dom.name)])
    """
    return JsObjects.JsObjects.get("%s[%s].innerHTML" % (self.varName, self.index))

  @property
  def index(self):
    """
    Get the selected index from the Select component

    Example
    b.click([rptObj.js.console.log(s.dom.index)])
    """
    return JsObjects.JsNumber.JsNumber.get("%s.selectedIndex" % self.varName)

  @property
  def events(self):
    """

    """
    return JsNodeDom.JsDomEvents(self._src)

  @property
  def jquery(self):
    """

    :rtype: JsQuery.JQuery
    """
    if self._jquery is None:
      self._jquery = JsQuery.JQuery(src=self._src, selector=JsQuery.decorate_var("#%s" % self._src.htmlId))
    return self._jquery

  @property
  def jquery_ui(self):
    """

    :rtype: JsQueryUi.JQueryUI
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

  def __str__(self):
    """
    The str() method return the variable Javascript reference of the variable.

    According to the variable definition it can be either its name or its value

    :return: A Javascript reference
    """
    return self.htmlId
