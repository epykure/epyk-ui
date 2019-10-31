"""
Base class for all the HTML components

HTML components are complex structured mixin Javascript and HTML in order to create valid objects to be added
to the final page. Page.py will create report objects in charge of collecting all those components
"""


import re
import json
import importlib
import collections
import functools
import logging

from epyk.core.css import CssInternal
from epyk.core.css.groups import CssGrpCls

from epyk.core.js import Js
from epyk.core.js import JsEncoder
from epyk.core.js import JsHtml

try:  # For python 3
  import urllib.request as urllib2
  import urllib.parse as parse
except:  # For Python 2
  import urllib2
  import urllib as parse


regex = re.compile('[^a-zA-Z0-9_]')


def cleanData(value):
  """ Function to clean the javascript data to allow the use of variables """
  return regex.sub('', value.strip())


# ---------------------------------------------------------------------------------------------------------
#                                          FRAMEWORK DECORATORS
#
# ---------------------------------------------------------------------------------------------------------
def deprecated(func):
  """
  This is a decorator which can be used to mark functions
  as deprecated. It will result in a warning being emmitted
  when the function is used.
  """

  @functools.wraps(func)
  def new_func(*args, **kwargs):
    logging.warn('#########################################')
    logging.warn("Call to deprecated function {}.".format(func.__name__))
    logging.warn('#########################################')
    return func(*args, **kwargs)
  return new_func


def inprogress(func):
  @functools.wraps(func)
  def new_func(*args, **kwargs):
    # warnings.simplefilter('always', DeprecationWarning)  # turn off filter
    # warnings.warn('############################################################################')
    # warnings.warn("Call to a test function {}.".format(func.__name__), category=DeprecationWarning, stacklevel=2)
    # warnings.warn('############################################################################')
    # warnings.simplefilter('default', DeprecationWarning)  # reset filter
    return func(*args, **kwargs)

  return new_func


class Html(object):
  """
  Parent class for all the HTML components. All the function defined here are available in the children classes.
  Child class can from time to time re implement the logic but the function will always get the same meaning (namely the same signature and return)
  """
  alias, jsEvent, cssCls, __css = None, None, None, None
  incIndent, helper, jsVal, jsUpdateDataFnc = 0, '', '', ''
  # Those variables should not be used anymore and should be replaced by the __ ones
  # This is done in order to avoid having users to change them. Thanks to the name
  # mangling technique Python will make the change more difficult and easier to see
  reqJs, reqCss = ['jquery'], [] # Jquery is already needed
  references, htmlCode, dataSrc, _code = None, None, None, None
  hidden, inReport, isLoadFnc = False, True, True
  dashboards = [] # Static definition of useful dashboards to get more example of an component

  _grpCls = CssGrpCls.CssGrpClass

  class _CssStyle(object):
    def __init__(self, htmlObj):
      self.htmlObj = htmlObj
      self._def_styles = None
      self.__common, self.__div, self.__chart = None, None, None

    @property
    def list(self):
      """
      Return a copy of the CSS class defined for a given component.
      This will list all the classes which will be attached to the HTML container

      The internal class name is defined using the dynamic prefix py_ in front of the classname

      :return: A list of CSS class Name
      """
      return list(self.htmlObj.attr['class'])

    def cssClear(self):
      """
      CSS Function

      Clear all the CSS classes definition for this component.

      :return: The Python htmlObj
      """
      self.htmlObj.defined.clsMap = set([])
      return self.htmlObj

    def cssDelCls(self, cssNname):
      """
      CSS Function

      Function to remove a predefined class attached to an HTML component.
      This will not remove the CSS class from the factory. It will only remove the use in this object.

      TODO: migrate everything to only use self.htmlObj.attr['class']

      :param cssNname: The CSS classname (or class reference)
      :return: The Python htmlObj
      """
      pyCssName = self.htmlObj._report.style.cssName(cssNname)
      if pyCssName in self.htmlObj.attr['class']:
        self.htmlObj.attr['class'].remove(pyCssName)
      if cssNname in self.htmlObj.defined:
        self.htmlObj.defined.remove(cssNname)
      return self.htmlObj

    def addCls(self, cssName):
      """
      Add a class based on its name.

      Example
      cls_name = rptObj.style.anonymous_cls({"color": "red"})
      rptObj.ui.text("test").style.addCls(cls_name)

      :param cssName: The CSS Class name as a string

      :return:
      """
      pyCssName = self.htmlObj._report.style.get(cssName)
      self.htmlObj._report.style.cssStyles[cssName] = pyCssName
      self.htmlObj.attr['class'].add(cssName)
      return self

    def cssCls(self, cssNname, attrs=None, eventAttrs=None, formatClsName=True):
      """
      CSS Function

      Dedicated to replace the existing definition by a bespoke one only for an object of this class.
      The way it work, the process will take a copy of the CSS object and then create a new one by adding the htmlId
      in the class name.

      Thus CSS properties can be overridden without impacting the all report

      :param cssNname: The CSS classname (or class reference)
      :param attrs: A dictionary with the main CSS attributes for the class
      :param eventAttrs: A dictionary with the CSS Style for the events
      :param formatClsName: Flag to change the classname to the internal convention for CSS classes in the framework
      :return: The Python htmlObj
      """
      if attrs is None and eventAttrs is None:
        if self.htmlObj._report.style.get(cssNname) is not None:
          self.htmlObj._report.style.add(cssNname)
        if formatClsName:
          cssNname = self.htmlObj._report.style.cssName(cssNname)
        self.htmlObj.attr['class'].add(cssNname)
      else:
        if cssNname in self.htmlObj.pyStyle:
          self.htmlObj.defined.remove(cssNname)
        dervfCls = self.htmlObj._report.style.cssDerivCls(self.htmlObj.htmlId, cssNname, attrs, eventAttrs=eventAttrs, forceReload=True)
        self.htmlObj._report.style.add(dervfCls.classname)
        self.htmlObj.defined.add(dervfCls.classname)
      return self.htmlObj

    def css(self, key, value=None):
      """
      CSS Function

      Set the CSS Attributes to a HTML component.
      This function is similar to the Jquery css function and it will accept any CSS Style defined by W3C.

      https://www.w3schools.com/css/

      Example:
        - cssObj.css('color', 'red')
        - cssObj.css({'color': 'red'})

      :param key: The CSS Key definition or a dictionary with all the CSS definition
      :param value: The CSS Value defined for a given attribute key (optional if key is a dictionary)
      :rtype: Css
      :return: The Python CSS Object
      """
      pixelCats = set(['font-size', 'width', 'height'])
      cssVals = key if value is None and isinstance(key, dict) else {key: value}
      for k, v in cssVals.items():
        if isinstance(v, str):
          self.htmlObj.attr.setdefault('css', {})[k] = v
        elif v is not None:
          if k in pixelCats and isinstance(v, int):
            v = "%spx" % v
          self.htmlObj.attr.setdefault('css', {})[k] = v
      return self

    @property
    def commons(self):
      """
      All the defined commons styles
      """
      if self.__common is None:
        self.__common = CssInternal.DefinedCommonStyles(self.htmlObj)
      return self.__common

    @property
    def div(self):
      """
      All the defined Div styles
      """
      if self.__div is None:
        self.__div = CssInternal.DefinedDivStyles(self.htmlObj)
      return self.__div

    @property
    def chart(self):
      """
      All the defined Chart styles
      """
      if self.__chart is None:
        self.__chart = CssInternal.DefinedChartStyles(self.htmlObj)
      return self.__chart

  def __init__(self, report, vals, htmlCode=None, code=None, width=None, widthUnit=None, height=None,
               heightUnit=None, globalFilter=None, dataSrc=None, options=None, profile=None):
    """ Create an python HTML object """
    self._triggerEvents, self.profile = set(), profile
    self._report, self._styleObj = report, None # The html object ID
    self._dom, self._container, self._sub_htmls, self._js, self.helper = None, None, [], None, ""
    self.jsImports = report.jsImports
    self.cssImport = report.cssImport
    self.attr = {'class': set([])} if self.cssCls is None else {'class': set(self.cssCls)} # default HTML attributes
    self.jsFncFrag, self._code, self._jsStyles = {}, code, None
    if code is not None:
      # Control to ensure the Javascript problem due to multiple references is highlighted during the report generation
      if code in self._report.htmlRefs:
        raise Exception("Duplicated Html Code %s in the script !" % code)

      self._report.htmlRefs[code] = True
      self._report.htmlCodes[code] = self
      if code[0].isdigit() or cleanData(code) != code:
        raise Exception("htmlCode %s cannot start with a number or contain, suggestion %s " % (code, cleanData(code)))

    if htmlCode is not None:
      self._report.htmlRefs[htmlCode] = True
      if htmlCode[0].isdigit() or cleanData(htmlCode) != htmlCode:
        raise Exception("htmlCode %s cannot start with a number or contain, suggestion %s " % (htmlCode, cleanData(htmlCode)))

      self._report.htmlCodes[htmlCode] = self
      try:
        int(htmlCode[0])
        raise Exception("htmlCode cannot start with a number - %s" % htmlCode)

      except: pass

      self.htmlCode = htmlCode
      self._report.jsGlobal.reportHtmlCode.add(htmlCode)
      if htmlCode in self._report.http:
        self.vals = self._report.http[htmlCode]

    css = getattr(self, '_%s__css' % self.__class__.__name__, None)
    self.pyStyle = None #list(getattr(self, '_%s__pyStyle' % self.__class__.__name__, []))
    if hasattr(self, '_%s__reqJs' % self.__class__.__name__):
      self.reqJs = list(getattr(self, '_%s__reqJs' % self.__class__.__name__, []))
    if hasattr(self, '_%s__reqCss' % self.__class__.__name__):
      self.reqCss = list(getattr(self, '_%s__reqCss' % self.__class__.__name__, []))
    #if hasattr(self, '_%s__table_name' % self.__class__.__name__):
    #  self.createObjectTables()
    self.pyCssCls = set()
    if css is not None:
      # we need to do a copy of the CSS style at this stage
      self.attr['css'] = dict(css)
    self.jsOnLoad, self.jsEvent, self.jsEventFnc = set(), {}, collections.defaultdict(set)
    self.vals = vals
    self.jsVal = "%s_data" % self.htmlId
    if self._report is not None:
       # Some components are not using _report because they are directly used for the display
       if self.reqJs is not None:
         for js in self.reqJs:
           self._report.jsImports.add(js)

       if self.reqCss is not None:
         for css in self.reqCss:
           self._report.cssImport.add(css)
    # Add the CSS dimension
    if width is not None:
      self.css({'width': "%s%s" % (width, widthUnit)})
    if height is not None:
      self.css('height', "%s%s" % (height, heightUnit))
    if htmlCode is not None and globalFilter is not None:
      self.filter(**globalFilter)
    if dataSrc is not None:
      self.dataSrc = dataSrc

  @property
  def htmlId(self):
    if self._code is not None:
      # This is a special code used to update components but not to store the results to the breadcrumb
      # Indeed for example for components like paragraph this does not really make sense to use the htmlCode
      return self._code

    if self.htmlCode is not None:
      return self.htmlCode

    return "%s_%s" % (self.__class__.__name__.lower(), id(self))

  @property
  def js(self):
    """
    Javascript base function

    Return all the Javascript functions defined in the framework.
    THis is an entry point to the full Javascript ecosystem.

    :return: A Javascript object
    :rtype: Js.JsBase
    """
    if self._js is None:
      self._js = Js.JsBase(self._report)
    return self._js

  @property
  def dom(self):
    """
    Javascript Functions

    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    :return: A Javascript Dom object
    :rtype: JsHtml.JsHtml
    """
    if self._dom is None:
      self._dom = JsHtml.JsHtml(self, report=self._report)
    return self._dom

  @property
  def container(self):
    """

    :rtype: JsHtml.JsHtml
    :return:
    """
    if self._container is None:
      if hasattr(self, "id_container"):
        self._container = JsHtml.JsHtml(self, self.id_container)
      else:
        self._container = JsHtml.JsHtml(self, self.htmlId)
    return self._container

  def prepend_child(self, htmlObj):
    """
    Wrapper to the Javascript method insertChild to add an HTML component

    Example
    for i in range(10):
      encore = rptObj.ui.texts.label("Add Label %s" % i).css({"width": "100%", "display": 'block'})
      select.prepend_child(encore)

    Documentation
    https://www.w3schools.com/jsref/met_node_insertbefore.asp

    :param htmlObj: The html component
    :return: The htmlObj
    """
    self._sub_htmls.append(htmlObj)
    self._report.js.addOnLoad([self.container.insertBefore(htmlObj.dom)])
    return self

  def append_child(self, htmlObj):
    """
    Wrapper to the Javascript method appendChild to append an HTML component

    Example
    for i in range(10):
      encore = rptObj.ui.texts.label("Add Label %s" % i).css({"width": "100%", "display": 'block'})
      select.append_child(encore)

    Documentation:
    https://www.w3schools.com/jsref/met_node_appendchild.asp

    :param htmlObj: The html component
    :return: The htmlObj
    """
    self._sub_htmls.append(htmlObj)
    self._report.js.addOnLoad([self.container.appendChild(htmlObj.dom)])
    return self

  def add_icon(self, text, css=None, position="before"):
    """
    Add an icon to the HTML object

    Example
    checks.title.add_icon("fas fa-align-center")

    Documentation

    :param text: The icon reference from font awsome website
    :param css: Optional. A dictionary with the CSS style to be added to the component
    :param position:
    :return: The Html object
    """
    self.icon = ""
    if text is not None:
      self.icon = self._report.ui.images.icon(text).css({"margin-right": '5px'})
      if position == "before":
        self.prepend_child(self.icon)
      else:
        self.append_child(self.icon)
      #elf.icon.inReport = False
      if css is not None:
        self.icon.css(css)
    return self

  def add_label(self, text, css=None, position="before", for_=None):
    """
    Add an elementary label component

    Example

    Documentation
    https://www.w3schools.com/tags/tag_label.asp

    :param text: The label content
    :param css: Optional. A dictionary with the CSS style to be added to the component
    :param position:
    :param for_: Specifies which form element a label is bound to
    """
    self.label = ""
    if text is not None:
      self.label = self._report.ui.texts.label(text)
      if for_ is not None:
        # Attach the label to another HTML component based on the ID
        self.label.attr['for'] = for_
      if position == "before":
        self.prepend_child(self.label)
      else:
        self.append_child(self.label)
      if css is not None:
        self.label.css(css)
    return self

  def add_link(self, script_name, report_name=None, name=None, icon=None, css=None, position="before"):
    """
    Add an elementary label component

    Example
    div = rptObj.ui.div()
    div.add_link("test.py", name="Click to go to the test report")

    :param script_name:
    :param report_name:
    :param name:
    :param icon:
    :param css: Optional. A dictionary with the CSS style to be added to the component
    :param position:
    """
    self.link = ""
    if script_name is not None:
      options = {"name": name} if name is not None else {}
      self.link = self._report.ui.links.script(script_name, report_name, icon=icon, options=options)
      if position == "before":
        self.prepend_child(self.link)
      else:
        self.append_child(self.link)
      if css is not None:
        self.link.css(css)
    return self

  def add_title(self, text, css=None, position="before"):
    """
    Add an elementary title component

    Example

    :param text: The title content
    :param css: Optional. A dictionary with the CSS style to be added to the component
    :param position:
    """
    self.title = ""
    if text is not None:
      self.title = self._report.ui.texts.title(text)
      if position == "before":
        self.prepend_child(self.title)
      else:
        self.append_child(self.title)
      #self.title.inReport = False
      if css is not None:
        self.title.css(css)
    return self

  def add_input(self, text, css=None, attrs=None, position="before"):
    """
    Add an elementary input component

    Example

    :param text: The title content
    :param css: Optional. A dictionary with the CSS style to be added to the component
    :param attrs: Optional
    :param position:
    """
    self.input = ""
    if text is not None:
      self.input = self._report.ui.inputs.input(text)
      if position == "before":
        self.prepend_child(self.input)
      else:
        self.append_child(self.input)
      if css is not None:
        self.input.css(css)
      if attrs is not None:
        self.input.add_attrs(attrs)
    return self

  def add_helper(self, text, css=None):
    """
    Add an elementary helper icon

    Example

    :param text: The helper content
    :param css: Optional. A dictionary with the CSS style to be added to the component

    :rtype: self._report.ui.rich.info

    :return:
    """
    if text is not None:
      self.helper = self._report.ui.rich.info(text)
      self.helper.inReport = False
      if css is not None:
        self.helper.css(css)
    return self

  @property
  def jqId(self):
    """
    Python property to get a unique Jquery ID function for a given Object

    :return: Javascript String of the variable used to defined the Jquery object in Javascript
    """
    return "$('#%s')" % self.htmlId

  @property
  def jqDiv(self):
    """
    Python property to get a unique Jquery ID function for a given Object (the div as the jqId might refer to the content)

    :return: Javascript String of the variable used to defined the Jquery object in Javascript
    """
    return "$('#%s')" % self.htmlId

  @property
  def eventId(self):
    return self.jqId

  @property
  def val(self):
    """
    Property to get the jquery value of the HTML object in a python HTML object.
    This method can be used in any jsFunction to get the value of a component in the browser.
    This method will only be used on the javascript side, so please do not consider it in your algorithm in Python

    :returns: Javascript string with the function to get the current value of the component
    """
    return '%s.val()' % self.jqId

  @property
  def style(self):
    """
    CSS Functions

    Derived CSS features for the HTML object. Those functions will only be applied on the style
    of this HTML object. All the other styles loaded in the factory will not be impacted.

    Example:
    textObj.style.cssCls("CssText", {"background-color": 'yellow'})

    :return: The Internal CSS Style Object
    """
    if self._styleObj is None:
      self._styleObj = self._CssStyle(self)
    return self._styleObj

  @property
  def defined(self):
    """
    Return the static CSS style definition of this component
    """
    if self.pyStyle is None:
      self.pyStyle = self._grpCls(self)
    return self.pyStyle

  @property
  def contextVal(self):
    """
    Set the javascript data defined when the context menu is created

    :return: Javascript String with the value attached to the context menu
    """
    return "{val: $(event.target).html()}"

  @property
  def jsQueryData(self):
    """
    Python function to define the Javascript object to be passed in case of Ajax call internally or via external REST service with other languages

    Documentation
    http://api.jquery.com/jquery.ajax/
    """
    if self.htmlCode is not None:
      return "{event_val: %s, event_code: '%s', %s: %s}" % (self.jsVal, self.htmlId, self.htmlCode, self.jsVal)

    return "{event_val: %s, event_code: '%s'}" % (self.jsVal, self.htmlId)

  @classmethod
  def jsMarkDown(cls, vals): return None

  @property
  def disableFnc(self): return ''

  def source(self, dataSrc):
    if dataSrc.get('type') == 'script':
      if dataSrc.get('frequency') is not None:
        self.dataSrc['intervalId'] = self._report.jsInterval(self.refresh(), dataSrc['frequency'] * 1000)
      else:
        if dataSrc.get('on_init', True):
          self._report.jsOnLoadFnc.add(self.refresh())
    elif dataSrc.get('type') == 'socket':
      self._report.jsImports.add('socket.io')
      self._report.jsOnLoadFnc.add("var socket = io.connect('%s')" % self._report.run.url_root)
      if dataSrc.get("append", False) and hasattr(self, 'jsAppend'):
        self._report.jsOnLoadFnc.add("socket.on('message_%s_%s_%s', function(data) {%s})" % (self._report.run.report_name, self._report.run.script_name, self.htmlId, self.jsAppend()))
      else:
        self._report.jsOnLoadFnc.add("socket.on('message_%s_%s_%s', function(data) {%s})" % (self._report.run.report_name, self._report.run.script_name, self.htmlId, self.jsGenerate()))

  def refresh(self):
    if self.dataSrc is None:
      raise Exception("Cannot use refresh() without dataSrc defined")

    if not self.dataSrc['script'].endswith(".py"):
      self.dataSrc['script'] = "%s.py" % self.dataSrc['script']
    fncs = [self.jsGenerate(jsDataKey=self.dataSrc.get('jsDataKey'))]
    if 'jsFnc' in self.dataSrc:
      if not isinstance(self.dataSrc['jsFnc'], list):
        self.dataSrc['jsFnc'] = [self.dataSrc['jsFnc']]
      fncs.extend(self.dataSrc['jsFnc'])
    return self._report.jsPost(self.dataSrc['script'], jsData=self.dataSrc.get('jsData'), jsFnc=fncs,
                               context=self.dataSrc.get('context'), httpCodes=self.dataSrc.get('httpCodes'), profile=self.profile)

  def attach_menu(self, context_menu):
    """
    Attach a context menu to an existing component. A context menu must have a component attached to otherwise
    the report will not be triggered

    """
    context_menu.source = self
    self._report._contextMenu[self.jqDiv] = context_menu
    return self

  def _jsData(self, jsData, jsDataKey, jsParse, isPyData, jsFnc=None):
    if isPyData:
      return json.dumps(jsData)

    if jsDataKey is not None:
      jsData = "%s['%s']" % (jsData, jsDataKey)
    if jsParse:
      print("jsParse deprecated - Should be using jsFnc instead")
      jsData = "JSON.parse(%s)" % jsData
    if jsFnc is not None:
      jsData = "%s(%s)" % (jsFnc, jsData)
    return jsData

  def addClass(self, cssCls):
    """
    Add class to the Html object. This function is used to add an existing CSS class to a component.
    Existing CSS class means that the definition is defined in one of the CSS external module used in the framework

    Example
    myObj.addClass('btn-default')

    Documentation
    https://www.w3schools.com/bootstrap/bootstrap_ref_all_classes.asp

    :return: The Python object itself
    """
    if not isinstance(cssCls, list):
      cssCls = [cssCls]
    for css in cssCls:
      if hasattr(css, 'classname'):
        css = css.classname
      self.attr['class'].add(css)
    return self

  def getClass(self):
    """
    Returns a string with the CSS classes to be added to the HTML attribute. This will return all the HTML classes added to the component
    it can be Python Class generated from the CSS or internal CSS class coming from external modules

    :category: CSS function
    :rubric: CSS
    :type: Configuration
    :example: myObj.getClass()
    :link HTML Classes: https://www.w3schools.com/html/html_classes.asp
    """
    return " ".join(self.attr['class'])

  def delClass(self, cssCls):
    """
    Remove a class from the list of CSS classes

    :category: CSS function
    :rubric: CSS
    :type: Configuration
    :example: myObj.delClass( 'btn-default' )
    """
    self.attr['class'].pop(cssCls)
    return self

  def css(self, key, value=None):
    """
    Change the CSS Style of a main component. This is trying to mimic the signature of the Jquery css function

    :category: Javascript function
    :rubric: JS
    :param key: The key style in the CSS attributes (Can also be a dictionary)
    :param value: The value corresponding to the key style
    :return: The python object itself

    :link CSS Function: http://api.jquery.com/css/
    """
    if value is None and isinstance(key, dict):
      # Do not add None value to the CSS otherwise it will break the page on the front end side
      cssVals = key if isinstance(key, dict) else {}
    else:
      cssVals = {key: value}
    for key, value in cssVals.items():
      if not 'css' in self.attr:
        # Convert the variable to something to be dump to javascript / CSS
        if isinstance(value, str):
          self.attr['css'] = {key: value}
        else:
          self.attr['css'] = {key: json.dumps(value)}
      else:
        self.attr['css'][key] = value
    return self

  def tooltip(self, value, location='top'):
    """
    Add the Tooltip feature when the mouse is over the component.
    This tooltip version is coming from Bootstrap

    :category: Javascript function
    :rubric: JS
    :type: Property
    :example: htmlObj.tooltip("My tooltip", location="bottom")
    :link Bootstrap: https://getbootstrap.com/docs/4.1/components/tooltips/
    :return: The Python object self
    """
    self.attr.update({'title': value, 'data-toggle': 'tooltip', 'data-placement': location})
    self._report.jsFnc.add("%s.tooltip()" % self.jqId)
    return self

  # ok
  def uitooltip(self, value, attrs=None, jsFncs=None, url=None, jsData=None, httpCodes=None, context=None, isHtml=False):
    """
    Add the Tooltip feature when the mouse is over the component.
    This tooltip version is coming for Jquery UI.
    $.widget.bridge('uitooltip', $.ui.tooltip);

    :category: Javascript function
    :rubric: JS
    :type: Property
    :example: htmlObj.uitooltip(value)
    :example: t.uitooltip("Youpi", attrs={"position": { "my": "left+15 top", "at": "right center" }, "tooltipClass":'preview-tip'}, jsFncs=["alert() "])
    :example: t.uitooltip("Youpi", attrs={"position": { "my": "left+15 top", "at": "right center" }, "tooltipClass":'preview-tip'}, url="service.py")
    :example: t.uitooltip("Youpi", attrs={"track": True} )
    :example: t.uitooltip('', attrs={"content": "function(){return 'bgjg<br />hihh'}"})
    :link Jquery: https://jqueryui.com/tooltip/#custom-content
    :link Ajax Jquery: https://stackoverflow.com/questions/13175268/ajax-content-in-a-jquery-ui-tooltip-widget
    :link Tooltip conflicts: https://stackoverflow.com/questions/13731400/jqueryui-tooltips-are-competing-with-twitter-bootstrap
    :return: The Python object self
    """
    self._report.jsImports.add('jqueryui')
    self._report.cssImport.add('jqueryui')
    self._report.jsGlobal.addJs("$.widget.bridge('uitooltip', $.ui.tooltip);")
    if attrs is None:
      attrs = {}
    if isHtml:
      if not "return" in value:
        raise Exception("Value should return an HTML string and can use the variable htmlObj")

      attrs['content'] = "function(){var htmlObj = $(this); var value = htmlObj.text(); %s}" % value
      value = ''
    self.attr.update({'title': value})
    if jsFncs is not None:
      rec = ["k: %s" % json.dumps(v) for k, v in attrs.items()]
      rec.append("content: function(callback) {%s}" % ";".join(jsFncs))
      jsAttr = '{%s}' % ", ".join(rec)
    elif url is not None:
      jsFncs = self._report.jsPost(url, jsData, jsFnc="callback(data)", httpCodes=httpCodes, context=context)
      rec = ["k: %s" % json.dumps(v) for k, v in attrs.items()]
      rec.append("content: function(callback) {%s}" % jsFncs)
      jsAttr = '{%s}' % ", ".join(rec)
    else:
      # TODO: add recursivity
      lAttrs = []
      for k, v in attrs.items():
        if isinstance(v, dict):
          sAttrs = []
          for sk, sv in v.items():
            if sv.startswith("function"):
              sAttrs.append("%s: %s" % (sk, sv))
            else:
              sAttrs.append("%s: %s" % (sk, json.dumps(sv)))
          lAttrs.append("%s: {%s}" % (k, ",".join(sAttrs)))
        elif v.startswith("function"):
          lAttrs.append("%s: %s" % (k, v))
        else:
          lAttrs.append("%s: %s" % (k, json.dumps(v)))
      jsAttr = "{%s}" % ",".join(lAttrs)
    self._report.jsFnc.add("%s.uitooltip(%s);" % (self.jqId, jsAttr ))
    return self

  def add_attrs(self, attrs):
    """

    :param attrs:
    :return:
    """
    if attrs is not None:
      for k, v in attrs.items():
        self.addAttr(k, v)
    return self

  def attr_data(self, name, value):
    """
    Add data attributes to the HTML containers

    Example
    html_obj.attr_data("count", 0)

    :param name: The attribute name
    :param value: The attribute value
    """
    self.attr["data-%s" % name] = value
    return self

  # ok
  def addAttr(self, name, value, isPyData=False):
    """
    Function to update the internal dictionary of object attributes. Those attributes will be used when the HTML component will be defined.
    Basically all sort of attributes can be defined here: CSS attributes, but also data, name...

    Documentation
    https://www.w3schools.com/tags/ref_attributes.asp

    Example
    htmlObj.addAttr("css', {'background-color': 'red'})
    htmlObj.addAttr("title", tooltip)

    :return: The python object itself
    """
    if isPyData:
      value = json.dumps(value)
    if name == 'css':
      # Section for the Style attributes
      if not 'css' in self.attr:
        self.attr['css'] = dict(value)
      else:
        self.attr['css'].update(value)
    else:
      # Section for all the other attributes
      self.attr[name] = value
    return self

  # ok
  def strAttr(self, withId=True, pyClassNames=None):
    """
    Return the string line with all the attributes

    All the attributes in the div should use double quote and not simple quote to be consistent everywhere in the framework
    and also in the javascript. If there is an inconsistency, the aggregation of the string fragments will not work
    """
    cssStyle, cssClass = '', ''
    if 'css' in self.attr:
      cssStyle = 'style="%s"' % ";".join(["%s:%s" % (key, val) for key, val in self.attr["css"].items()])
    classData = self.getClass()
    if 'class' in self.attr and len(self.attr['class']) > 0 and classData:
      if pyClassNames is not None:
        # Need to merge in the class attribute some static classes coming from external CSS Styles sheets
        # and the static python classes defined on demand in the header of your report
        # self._report.cssObj.getClsTag(pyClassNames)[:-1] to remove the ' generated in the module automatically
        cssClass = self._report.style.getClsTag(pyClassNames.clsMap).replace('class="', 'class="%s ')
        cssClass %= classData
      else:
        cssClass = 'class="%s"' % classData
    elif pyClassNames is not None:
      cssClass = self._report.style.getClsTag(pyClassNames.clsMap)
    if withId:
      return 'id="%s" %s %s %s' % (self.htmlId, " ".join(['%s="%s"' % (key, val) for key, val in self.attr.items() if key not in ('css', 'class')]), cssStyle, cssClass)

    return '%s %s %s' % (" ".join(['%s="%s"' % (key, val) for key, val in self.attr.items() if key not in ('css', 'class')]), cssStyle, cssClass)

  def addGlobalVar(self, varName, jsDefinition=None, varDependencies=None, isPyData=None):
    data = self._report._props.setdefault("js", {}).setdefault("datasets", {})
    data[varName] = "var %s = %s" % (varName, jsDefinition)

  def addGlobalFnc(self, fncName, fncDef, fncDsc=''):
    constructors = self._report._props.setdefault("js", {}).setdefault("constructors", {})
    constructors[fncName.split('(')[0]] = "function %s{%s}" % (fncName, fncDef)

  def onDocumentReady(self):
    """ Return the javascript calls to be returned to update the component """
    if self._jsStyles is not None:
      self.jsUpdateDataFnc = '''%(pyCls)s(%(jqId)s, %(htmlId)s_data, %(jsStyles)s)
            ''' % {'pyCls': self.__class__.__name__, 'jqId': self.jqId, 'htmlId': self.htmlId, 'htmlCode': json.dumps(self.htmlCode),
                   'jsVal': self.val, 'jsStyles': json.dumps(self._jsStyles)}
    else:
      self.jsUpdateDataFnc = '''%(pyCls)s(%(jqId)s, %(htmlId)s_data) 
        ''' % {'pyCls': self.__class__.__name__, 'jqId': self.jqId, 'htmlId': self.htmlId, 'htmlCode': json.dumps(self.htmlCode),
               'jsVal': self.val}

    profile = self.profile if self.profile is not None else getattr(self._report, 'PROFILE', False)
    if profile:
      fncContentTemplate = ["var t0 = performance.now()", self.jsUpdateDataFnc,
                            "console.log('|%s|%s|'+ (performance.now()-t0))" % (self.__class__.__name__, self.htmlId)]
    else:
      fncContentTemplate = [self.jsUpdateDataFnc]
    if self.dataSrc is None or self.dataSrc.get('type') != 'url':
      builder, optBuilder = fncContentTemplate[0].strip(), []
      for l in builder.split("\n"):
        optBuilder.append(l.strip())
      self._report._props.setdefault('js', {}).setdefault("builders", []).append("".join(optBuilder))
      self._report.jsOnLoadFnc.add(";".join(fncContentTemplate))

  def onDocumentLoadVar(self):
    """ Return the variable to store in the global section of the javacript part """
    self.addGlobalVar(self.jsVal, json.dumps(self.vals, cls=JsEncoder.Encoder))
    if self.dataSrc is not None and self.dataSrc.get('type') == 'url':
      if 'time_out' in self.dataSrc:
        if self.dataSrc['time_out'] < 60:
          self._report.notification('WARNING', 'Server Load',  'Process configured to run every %s seconds' % self.dataSrc['time_out'])

        self._report.jsOnLoadFnc.add('''
          setInterval(function(){ 
            var params = {} ; for(var key in %(htmlCodes)s) { params[key] = %(breadCrumVar)s['params'][key] ;  }
            $.getJSON( "%(url)s", params, function( data ) { %(jsVal)s = data ; %(pyCls)s(%(jqId)s, %(htmlId)s_data) ; });
          }, %(time_out)s);
          ''' % {'pyCls': self.__class__.__name__, 'jqId': self.jqId, 'htmlId': self.htmlId, 'jsVal': self.jsVal,
                 'jsUpdateDataFnc': self.jsUpdateDataFnc, 'url': self.dataSrc['url'],
                 'breadCrumVar': self._report.jsGlobal.breadCrumVar, 'time_out': self.dataSrc['time_out'] * 1000,
                 'htmlCodes': json.dumps(self.dataSrc.get('htmlCodes', []))})
      else:
        self._report.jsOnLoadFnc.add('''
          var params = {} ; for(var key in %(htmlCodes)s) { params[key] = %(breadCrumVar)s['params'][key] ;  }
          $.post( "%(url)s", params, function( data ) { %(jsVal)s = JSON.parse(data) ; %(pyCls)s(%(jqId)s, %(jsVal)s, %(jsStyles)s ) ; });
          ''' % {'pyCls': self.__class__.__name__, 'jqId': self.jqId, 'htmlId': self.htmlId, 'jsVal': self.jsVal,
                 'jsUpdateDataFnc': self.jsUpdateDataFnc, 'url': self.dataSrc['url'], 'jsStyles': json.dumps(self._jsStyles),
                 'breadCrumVar': self._report.jsGlobal.breadCrumVar, 'htmlCodes': json.dumps(self.dataSrc.get('htmlCodes', [])) } )

  def onDocumentLoadFnc(self):
    """ Flag set to True by default to check if this function is overriden """
    self.isLoadFnc = False

  def onDocumentLoadContextmenu(self):
    """ Generic Javascript function to define a Contenxt Menu """
    self._report.jsGlobal.fnc("ContextMenu(htmlObj, data, markdownFnc)",
        '''
        $('#popup').empty(); $('#popup').append('<ul style="width:100%%;height:100%%;margin:0;padding:0"></ul>');
        var listMenu = $('#popup').find('ul');
        data.forEach(function(rec){
          if ('title' in rec) {
            listMenu.append('<li class="list-group-item" style="cursor:cursor;width:100%%;display:inline-block;padding:5px 5px 2px 10px;font-weight:bold;color:white;background:%(color)s">' + rec.title + '</li> ');
          } else {
            if (rec.url != undefined) { var content = '<a href="' + rec.url + '" style="color:black">' + rec.label + '</a>' ;} else {var content = rec.label;};
            listMenu.append('<li class="list-group-item" style="cursor:pointer;width:100%%;display:inline-block;padding:2px 5px 2px 10px">' + content + '</li> '); }
        });
        if (markdownFnc != false) {
          listMenu.append('<li class="list-group-item" style="cursor:cursor;width:100%%;display:inline-block;padding:5px 5px 2px 10px;font-weight:bold;color:white;background:%(color)s">MarkDown</li> ');
          listMenu.append('<li onclick="CopyMarkDown(\\''+ markdownFnc +'\\');" class="list-group-item" style="cursor:pointer;width:100%%;display:inline-block;padding:2px 5px 2px 10px"><i class="fas fa-thumbtack"></i>&nbsp;&nbsp;Copy MarkDown</li> ');};
        $('#popup').css({'padding': '0', 'width': '200px'});
        $('#popup').show()''' % {'color': self.getColor('colors', 9)})

  def notSelectable(self):
    """ Change the html Object to not be selectable """
    self._report.jsOnLoadFnc.add("%s.disableSelection()" % self.jqId)

  def onInit(self, htmlCode, dataSrc):
    if dataSrc['type'] == 'script':
      mod = importlib.import_module('%s.sources.%s' % (self._report.run.report_name, dataSrc['script'].replace('.py', '')))
      httpParams = dict([(param, self._report.http.get(param, '')) for param in dataSrc.get('htmlCodes', [])])
      recordSet = mod.getData(self._report, httpParams)
      if 'jsDataKey' in dataSrc:
        recordSet = recordSet[dataSrc['jsDataKey']]
      return recordSet

    elif dataSrc['type'] == 'flask':
      if 'fncName' in dataSrc:
        mod = importlib.import_module('epyk.%s' % dataSrc['module'])
        return json.loads(getattr(mod, dataSrc['fncName'])(*dataSrc.get('pmts', [])))
      else:
        return json.loads(dataSrc['fnc'](*dataSrc.get('pmts', [])))

    elif dataSrc['type'] == 'url':
      # To think about the security here
      data = {'user_name': self._report.user, 'report_name': self._report.run.report_name, 'script_name': self._report.run.script_name, 'host_name': self._report.run.host_name}
      data.update( self._report._run )
      response = urllib2.urlopen("%s%s" % (self._report.run.url_root, dataSrc['url']), parse.urlencode(data).encode("utf-8"))
      if dataSrc.get('jsDataKey') is not None:
        return json.loads(response.read().decode('utf_8'))['jsDataKey']
      try:
        return json.loads(response.read().decode('utf_8'))
      except Exception as err:
        self._report.log("[%s] urlopen:%s%s" % (str(err), self._report.run.url_root, dataSrc['url']), type='WARNING')
        return ""

  # ---------------------------------------------------------------------------------------------------------
  #                                          JAVASCRIPT STANDARD EVENTS
  #
  def draggable(self, attrs=None):
    if attrs is None:
      attrs = {}
    self._report.jsImports.add('jqueryui')
    self._report.cssImport.add('jqueryui')
    self._report.jsOnLoadFnc.add("%(jqDiv)s.addClass('ui-widget-content');%(jqDiv)s.css({'z-index': 10, 'background': 'inherit', color: 'inherit'});%(jqDiv)s.draggable(%(attrs)s)" % {'jqDiv': self.jqDiv, 'attrs': json.dumps(attrs)})
    return self

  def jsEvents(self):
    if hasattr(self, 'jsFncFrag'):
      for eventKey, fnc in self.jsFncFrag.items():
        self._report._props.get('js', {}).get('builders', []).extend(fnc)
        if self.htmlCode is not None:
          fnc.insert(0, self.jsAddUrlParam(self.htmlCode, self.val, isPyData=False))
        if getattr(self._report, 'PROFILE', False):
          self._report.jsOnLoadEvtsFnc.add('''
                    %(jqId)s.on('%(eventKey)s', function(event) {var t0_event = performance.now(); 
                      %(disableFnc)s; var useAsync = false; var data = %(data)s; var returnVal = undefined; %(jsInfo)s; %(jsFnc)s; 
                      data.event_time = Today(); data.event_time_offset = new Date().getTimezoneOffset();
                      if (!useAsync) {var body_loading_count = parseInt($('#body_loading span').text());
                        $('#body_loading span').html(body_loading_count - 1);
                        if($('#body_loading span').html() == '0') {$('#body_loading').remove()}};
                      console.log('|%(pyClass)s|%(eventKey)s(%(htmlId)s)|'+ (performance.now()-t0_event));
                      if (returnVal != undefined) {return returnVal}})
            ''' % {'jqId': self.eventId, 'eventKey': eventKey, 'data': self.jsQueryData, 'disableFnc': self.disableFnc, 'htmlId': self.htmlId,
                   'pyClass': self.__class__.__name__, 'jsFnc': ";".join([f for f in fnc if f is not None]),
                   'jsInfo': self._report.jsInfo('process(es) running', 'body_loading')})
        else:
          self._report.jsOnLoadEvtsFnc.add('''
            %(jqId)s.on('%(eventKey)s', function(event) {
              %(disableFnc)s; var useAsync = false; var data = %(data)s; var returnVal = undefined; %(jsFnc)s; 
              data.event_time = Today(); data.event_time_offset = new Date().getTimezoneOffset();
              if (!useAsync) {var body_loading_count = parseInt($('#body_loading span').text());
                $('#body_loading span').html(body_loading_count - 1); if($('#body_loading span').html() == '0') {$('#body_loading').remove()}}
              if (returnVal != undefined) {return returnVal}})''' % {'jqId': self.eventId, 'eventKey': eventKey, 'data': self.jsQueryData, 'disableFnc': self.disableFnc,
                     'jsFnc': ";".join([f for f in fnc if f is not None])})

  def click(self, jsFncs): return self.jsFrg('click', ";".join(jsFncs) if isinstance(jsFncs, list) else jsFncs)
  def change(self, jsFncs): return self.jsFrg('change', ";".join(jsFncs) if isinstance(jsFncs, list) else jsFncs)
  def drop(self, jsFncs): return self.jsFrg('drop', ";".join(jsFncs) if isinstance(jsFncs, list) else jsFncs)
  def dragover(self, jsFncs): return self.jsFrg('dragover', ";".join(jsFncs) if isinstance(jsFncs, list) else jsFncs)
  def dragleave(self, jsFncs): return self.jsFrg('dragleave', ";".join(jsFncs) if isinstance(jsFncs, list) else jsFncs)
  def dragenter(self, jsFncs): return self.jsFrg('dragenter', ";".join(jsFncs) if isinstance(jsFncs, list) else jsFncs)
  def dblclick(self, jsFncs): return self.jsFrg('dblclick', ";".join(jsFncs) if isinstance(jsFncs, list) else jsFncs)
  def mouseup(self, jsFncs): return self.jsFrg('mouseup', ";".join(jsFncs) if isinstance(jsFncs, list) else jsFncs)
  def blur(self, jsFncs): return self.jsFrg('blur', ";".join(jsFncs) if isinstance(jsFncs, list) else jsFncs)
  def focusout(self, jsFncs): return self.jsFrg('focusout', ";".join(jsFncs) if isinstance(jsFncs, list) else jsFncs)
  def keydown(self, jsFncs): return self.jsFrg('keydown', ";".join(jsFncs) if isinstance(jsFncs, list) else jsFncs)
  def keypress(self, jsFncs): return self.jsFrg('keypress', ";".join(jsFncs) if isinstance(jsFncs, list) else jsFncs)
  def keyup(self, jsFncs): return self.jsFrg('keyup', ";".join(jsFncs) if isinstance(jsFncs, list) else jsFncs)
  def hover(self, jsFncs): return self.jsFrg('hover', ";".join(jsFncs) if isinstance(jsFncs, list) else jsFncs)
  def mouseover(self, jsFncs): return self.jsFrg('mouseover', ";".join(jsFncs) if isinstance(jsFncs, list) else jsFncs)
  def mouseout(self, jsFncs): return self.jsFrg('mouseout', ";".join(jsFncs) if isinstance(jsFncs, list) else jsFncs)

  def callPy(self, script_name, jsData=None, success="", cacheObj=None, isPyData=True, isDynUrl=False, httpCodes=None,
             datatype='json', context=None, profile=False, loadings=None, report_name=None, before=None, jsFnc=''):
    if not script_name.endswith(".py"):
      script_name = "%s.py" % script_name
    if success != "":
      jsFnc = success
    if before is not None:
      if not isinstance(before, list):
        before = [before]
    else:
      before = []
    return self.click(before + [self._report.jsPost(script_name, jsData, jsFnc, cacheObj, isPyData, isDynUrl, httpCodes,
                                          datatype, context, profile, loadings, report_name)])

  def paste(self, jsFnc):
    """ Generic click function """
    self._report.jsOnLoadFnc.add('''%(jqId)s.on('paste', function(event) { 
       var data;
       if (window.clipboardData && window.clipboardData.getData) { // IE
            data = window.clipboardData.getData('Text'); }
        else if (event.originalEvent.clipboardData && event.originalEvent.clipboardData.getData) { // other browsers
            data = event.originalEvent.clipboardData.getData('text/plain')} 
        %(jsFnc)s 
      })''' % {'jqId': self.jqId, 'jsFnc': jsFnc})

  def input(self, jsFnc): self._report.jsOnLoadFnc.add("%(jqId)s.on('input', function(event) { %(jsFnc)s }) ; " % {'jqId': self.jqId, 'jsFnc': jsFnc})

  def filter(self, jsId, colName, allSelected=True, filterGrp=None, operation="=", itemType="string"):
    """
    :category: Data Transformation
    :rubric: JS
    :type: Filter
    :dsc:
      Link the data to the filtering function. The record will be filtered based on the composant value
    :return: The Python Html Object
    """
    filterObj = {"operation": operation, 'itemType': itemType, 'allIfEmpty': allSelected, 'colName': colName, 'val': self.val, 'typeVal': 'js'}
    self._report.jsSources.setdefault(jsId, {}).setdefault('_filters', {})[self.htmlCode] = filterObj
    return self

  # ---------------------------------------------------------------------------------------------------------
  #                                          JAVASCRIPT FRAGMENTS
  #
  def jsGenerate(self, jsData='data', jsDataKey=None, isPyData=False, jsParse=False, jsStyles=None, jsFnc=None):
    """
    Python function used to build a HTML component based on a common javascript definition

    :param jsData: The javascript data dictionary (or Python)
    :param jsDataKey: The key in the javascript data dictionary (or Python)
    :param isPyData: A flag to apply a javascript conversion if this is not called from a jsXXX() method
    :param jsParse: A flag to parse the javascript function is it is coming from a json string for some reason

    :example: htmlObj.jsGenerate( {"test": True}, jsDataKey="test", isPyData=True)

    :return: Javascript String with the different pieces and functions calls used to build the component
    """
    if jsStyles is None:
      jsStyles = json.dumps(self._jsStyles)
    return '''%(fncName)s(%(jsId)s, %(jsData)s, %(jsStyles)s)
          ''' % {'jsDataKey': json.dumps(jsDataKey), 'fncName': self.__class__.__name__, 'jsId': self.jqId,
                 'jsData': self._jsData(jsData, jsDataKey, jsParse, isPyData, jsFnc), 'jsStyles': jsStyles}

  def jsUpdate(self, data, isPyData=True):
    """
    Javascript function to update a component with a new val

    """
    self.onDocumentReady()
    self.onDocumentLoadVar()
    if isPyData:
      data = json.dumps(data)
    return "var %s = %s; %s; " % (self.jsVal, data, self.jsUpdateDataFnc)

  def jsHtml(self, jqId, jsData, isPydata=False):
    """
    Function to set on the Javascript side (during an event) the content of a component.
    With this function HTML content is possible and it will be correctly displayed

    :category: Javascript function
    :rubric: JS
    :example: >>> myObj.html("<b>My Test</b>")
    :link W3C Documentation: https://www.w3schools.com/jquery/html_html.asp
    :return: String with the html function to set the HTML content of an element
    """
    if isPydata:
      jsData = json.dumps(jsData)
    return '''%s.html(%s)''' % (jqId, jsData)

  # pas besoin
  def jsFrg(self, typeEvent, jsFnc):
    if typeEvent not in self.jsFncFrag:
      self.jsFncFrag[typeEvent] = []
    if isinstance(jsFnc, list):
      self.jsFncFrag[typeEvent].extend(jsFnc)
    else:
      self.jsFncFrag[typeEvent].append(jsFnc)
    return self

  # ---------------------------------------------------------------------------------------------------------
  #                                             CSS SECTION
  #

  # ok
  def loadStyle(self):
    """
    Internal function in charge of loading the different CSS Python Styles attached to a component

    :category: CSS function
    :rubric: CSS
    """
    for cssStyle in self.defined.clsMap:
      # Remove the . or # corresponding to the type of CSS reference
      self.pyCssCls.add(self._report.style.add(cssStyle).classname)

  def getColor(self, typeChart, i):
    """
    CSS Color function

    Python function to get the different pre defined color codes in the Framework

    :return: the hexadecimal code of the CSS color used in the CSS framework
    :link hexadecimal color: https://www.w3schools.com/colors/colors_picker.asp
    """
    return self._report.style.colors.get(typeChart, i)

  def _addToContainerMap(self, htmlObj):
    if hasattr(self, 'htmlMaps'):
      if hasattr(htmlObj, 'htmlMaps'):
        # It is a container and we need to get the mapping of the different components inside
        self.htmlMaps.update(htmlObj.htmlMaps)
      else:
        if getattr(htmlObj, 'htmlCode', None) is not None:
          if htmlObj.category == 'Table':
            self.htmlMaps[htmlObj.htmlCode] = (htmlObj.__class__.__name__, '%s_table' % htmlObj.htmlCode)
          elif htmlObj.category == 'Charts':
            self.htmlMaps[htmlObj.htmlCode] = ('PyChartJs', '$("#%s")' % htmlObj.htmlCode)
          else:
            self.htmlMaps[htmlObj.htmlCode] = (htmlObj.__class__.__name__, htmlObj.jqId)
        elif getattr(htmlObj, '_code', None) is not None:
          if htmlObj.category == 'Table':
            self.htmlMaps[htmlObj._code] = (htmlObj.__class__.__name__, '%s_table' % htmlObj._code)
          elif htmlObj.category == 'Charts':
            self.htmlMaps[htmlObj._code] = ('PyChartJs', '$("#%s")' % htmlObj._code)
          else:
            self.htmlMaps[htmlObj._code] = (htmlObj.__class__.__name__, htmlObj.jqId)

  # -------------------------------------------------------------------------------------------------------------------
  #                    OUTPUT METHODS
  # -------------------------------------------------------------------------------------------------------------------
  def __str__(self):
    """
    Apply the corresponding function to build the HTML result.
    This function is very specific and it has to be defined in each class.

    :category: Output function
    :rubric: PY
    """
    raise NotImplementedError('subclasses must override __str__()!')

  def to_word(self, document):
    """
    Apply the corresponding function to produce the same result in a word document.
    This function is very specific and it has to be defined in each class.

    :category: Output function
    :rubric: PY
    :link Python Module Documentation: http://python-docx.readthedocs.io/en/latest/
    """
    raise NotImplementedError('''
      subclasses must override to_word(), %s !
      Go to http://python-docx.readthedocs.io/en/latest/user/quickstart.html for more details  
    ''' % self.__class__.__name__)

  def to_xls(self, workbook, worksheet, cursor):
    """
    Apply the corresponding function to produce the same result in a word document.
    This function is very specific and it has to be defined in each class.

    :category: Output function
    :rubric: PY
    :link Python Module Documentation: https://xlsxwriter.readthedocs.io/
    """
    raise NotImplementedError('''
      subclasses must override to_xls(), %s !
      Go to https://xlsxwriter.readthedocs.io/working_with_tables.html for more details  
    ''' % self.__class__.__name__)

  def html(self):
    """
    Return the onload, the HTML object and the javascript events

    """
    for htmlObj in self._sub_htmls:
      htmlObj.html()
    if self.helper != "":
      self.helper.html()
    self.loadStyle()
    self.jsEvents()
    # Update the HTML element with the values defined in the function call in the report
    self.onDocumentLoadFnc()
    if self.isLoadFnc:
      self.onDocumentLoadVar()
      self.onDocumentReady()
    if self.dataSrc is not None:
      self.source(self.dataSrc)
    contextlinks = []
    if self.references is not None:
      contextlinks.append({'title': 'Useful Links'})
      for label, url in self.references.items():
        contextlinks.append({"label": label, "url": url})

    # This is not needed in the pages by default
    markDown = None # self.jsMarkDown()
    if markDown is not None:
      self.addGlobalVar("%s_markDownFnc" % self.htmlId, json.dumps(markDown))

      self._report.jsGlobal.fnc("CopyMarkDown(jsMarkDown)",
          ''' 
          var textArea = $('<textarea />') ;
          $('body').append(textArea) ;
          textArea.text(jsMarkDown.split('&&').join('\\n')) ;
          $('body').append(textArea) ;
          textArea.select();
          document.execCommand('copy');
          textArea.remove(); 
          ''')
    else:
      self.addGlobalVar("%s_markDownFnc" % self.htmlId, json.dumps(False))

    #self.contextMenu(contextlinks)
    if self._triggerEvents:
      self._report.jsOnLoadEvtsFnc.add(";".join(self._triggerEvents))
    if self.hidden == True:
      self.addAttr('css', {'display': 'none'})
    return str(self)
