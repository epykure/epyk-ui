"""
Main entry point for all the Javascript Framework.

This will load all the modules and function directly copied from the Javascript documentation.
The main websites used in the implementation of those modules are:



"""

import json

from epyk.core.js import JsUtils
from epyk.core.js import JsWindow
from epyk.core.js import JsLocation
from epyk.core.js import JsMaths
from epyk.core.js import JsPerformance

# All the predefined Javascript Statements
from epyk.core.js.statements import JsIf
from epyk.core.js.statements import JsFor
from epyk.core.js.statements import JsWhile
from epyk.core.js.statements import JsSwitch

# All the predefined variable types
from epyk.core.js.fncs import JsFncs
from epyk.core.js.primitives import JsArray
from epyk.core.js.primitives import JsObjects
from epyk.core.js.primitives import JsObject
from epyk.core.js.primitives import JsNumber
from epyk.core.js.primitives import JsString

from epyk.core.js.objects import JsNodeAttributes
from epyk.core.js.objects import JsNodeDom
from epyk.core.js.objects import JsData


class JsConsole(object):
  """
  This is a wrapper to the Console

  Documentation
  https://medium.freecodecamp.org/how-to-get-the-most-out-of-the-javascript-console-b57ca9db3e6d
  """

  @property
  def debugger(self):
    """
    Trigger a Javascript debugger from this point.
    The Javascript will be stopped and it will be possible to check the process step by step in the browser using F12

    Example
    rptObj.js.console.debugger

    Documentation:
    https://www.w3schools.com/jsref/jsref_debugger.asp

    :return: The Javascript Keyword to trigger the browser debugger
    """
    return JsObject.JsKeyword("debugger")

  @property
  def clear(self):
    """
    The console.clear() method clears the console.

    Example
    rptObj.js.console.clear

    Documentation
    https://www.w3schools.com/jsref/met_console_clear.asp

    :return: The Javascript String used to clear the console (F12 in standard browsers)
    """
    return JsFncs.JsFunction("console.clear()")

  def log(self, jsData, jsFnc=None, skip_data_convert=False):
    """
    The console.log() method writes a message to the console.

    Example
    rptObj.js.console.log("Test")

    Documentation:
    https://www.w3schools.com/jsref/met_console_log.asp

    :param jsData: The Javascript fragment
    :param jsFnc:
    :param skip_data_convert:
    :return: The Javascript String used to clear the console (F12 in standard browsers)
    """
    if skip_data_convert:
      return JsFncs.JsFunction("console.log(%s)" % jsData)

    return JsFncs.JsFunction("console.log(%s)" % JsUtils.jsConvertData(jsData, jsFnc))

  def info(self, jsData, jsFnc=None):
    """
    The console.info() method writes a message to the console.

    Documentation:
    https://www.w3schools.com/jsref/met_console_info.asp

    :param data: The Javascript fragment
    :param jsFnc:
    :return: The Javascript String used to clear the console (F12 in standard browsers)
    """
    return JsFncs.JsFunction("console.info(%s)" % JsUtils.jsConvertData(jsData, jsFnc))

  def warn(self, jsData, jsFnc=None):
    """
    The console.warn() method writes a warning to the console.

    Documentation:
    https://www.w3schools.com/jsref/met_console_warn.asp

    :param data: The Javascript fragment
    :param jsFnc:
    :return: The Javascript String used to clear the console (F12 in standard browsers)
    """
    return JsFncs.JsFunction("console.warn(%s)" % JsUtils.jsConvertData(jsData, jsFnc))

  def error(self, jsData, jsFnc=None):
    """
    The console.error() method writes an error message to the console.

    Documentation:
    https://www.w3schools.com/jsref/met_console_error.asp

    :param data: The Javascript fragment
    :param isPyData:
    :return: The Javascript String used to clear the console (F12 in standard browsers)
    """
    return JsFncs.JsFunction("console.error(%s)" % JsUtils.jsConvertData(jsData, jsFnc))

  def table(self, jsData, jsHeader=None):
    """
    The console.table() method writes a table in the console view.

    Documentation:
    https://www.w3schools.com/jsref/met_console_table.asp

    :param jsData: Required. The data to fill the table with
    :param jsHeader: Optional. An array containing the names of the columns to be included in the table
    :return: The Javascript String used to clear the console (F12 in standard browsers)
    """
    if jsHeader is not None:
      return JsFncs.JsFunction("console.table(%s, %s)" % (jsData, jsHeader))

    return JsFncs.JsFunction("console.table(%s)" % jsData)

  def time(self, htmlId):
    """
    The console.time() method starts a timer in the console view

    Documentation:
    https://www.w3schools.com/jsref/met_console_time.asp

    :param htmlId: Use the label parameter to give the timer a name
    :return: A Python Javascript Number
    """
    return JsNumber.JsNumber("console.time('%s')" % htmlId, isPyData=False)

  def timeEnd(self, htmlId):
    """
    The console.timeEnd() method ends a timer, and writes the result in the console view.

    Documentation:
    https://www.w3schools.com/jsref/met_console_timeend.asp

    :param htmlId: The name of the timer to end
    :return: The Javascript String used to clear the console (F12 in standard browsers)
    """
    return JsFncs.JsFunction("console.timeEnd('%s')" % htmlId)

  def _assert(self, jsData, strInfo, jsFnc=None):
    """
    The console.assert() method writes a message to the console, but only if an expression evaluates to false.

    Documentation:
    https://www.w3schools.com/jsref/met_console_assert.asp

    :param jsData:
    :param strInfo:
    :param isPyData:
    :return:
    """
    return JsFncs.JsFunction("console.assert('%s', '%s')" % (JsUtils.jsConvertData(jsData, jsFnc), strInfo))

  def tryCatch(self, jsFncs, jsFncsErrs="console.warn(err.message)"):
    """
    Javascript Try Catch Exceptions

    Documentation:
    https://www.w3schools.com/jsref/jsref_obj_error.asp

    :param jsFncs:
    :param jsFncsErrs:
    :return: The Javascript String used to clear the console (F12 in standard browsers)
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    return JsFncs.JsFunction("try{%s} catch(err){%s}" % (";".join(jsFncs), jsFncsErrs))


class JsJson(object):
  """
  Wrapper around the Javascript Json module
  This wrapper will only wrapper the different functions available in the underlying library.
  The documentation can be found in each function or are available on the Javascript Official documentation

  Documentation:
  https://www.w3schools.com/js/js_json_intro.asp

  """

  def parse(self, jsData, jsResultFnc=None, jsFnc=None):
    """
    Parses a JSON string and returns a JavaScript object

    Documentation:
    https://www.w3schools.com/js/js_json_parse.asp
    https://www.w3schools.com/jsref/jsref_parse_json.asp

    :param jsData: Required. A string written in JSON format
    :param jsResultFnc: Optional. A function used to transform the result. The function is called for each item. Any nested objects are transformed before the parent.
    :return: The Javascript string method
    """
    jsData = JsUtils.jsConvertData(jsData, jsFnc)
    if jsResultFnc is not None:
      return JsFncs.JsFunction("JSON.parse(%s, %s)" % (jsData, jsResultFnc))

    return JsFncs.JsFunction("JSON.parse(%s)" % jsData)

  def stringify(self, jsData, replacer=None, space=0, jsFnc=None):
    """
    The JSON.stringify() method converts JavaScript objects into strings.

    Documentation:
    https://www.w3schools.com/js/js_json_stringify.asp

    :param jsData: Required. The value to convert to a string
    :param replacer: Optional. Either a function or an array used to transform the result. The replacer is called for each item.
    :param space: Optional. Either a String or a Number. A string to be used as white space (max 10 characters),
      or a Number, from 0 to 10, to indicate how many space characters to use as white space.
    :return: The Javascript string method
    """
    return JsString.JsString("JSON.stringify(%s, %s, %s)" % (JsUtils.jsConvertData(jsData, jsFnc), json.dumps(replacer), space), isPyData=False)


class JsBreadCrumb(object):
  class __internal(object):
    _props, http = {}, {}

  def __init__(self, src=None):
    self._src = src if src else self.__internal() # The underlying source object is not supposed to be touched in the underlying classes
    self._selector = "breadcrumb"
    self._anchor = None
    self._src._props.setdefault('js', {}).setdefault('builders', []).append("%s = {pmts: %s}" % (self._selector, json.dumps(self._src.http)))

  def add(self, key, jsData):
    """
    Add an entry to the Javascript breadcrumb dictionary

    :param key: The key in the Breadcrumb dictionary
    :param jsData:

    :return: Nothing
    """
    jsData = JsUtils.jsConvertData(jsData, None)
    return JsFncs.JsFunction('%s["pmts"]["%s"] = %s' % (self._selector, key, jsData))

  def get(self, key=None):
    """
    returns the object stored in the breadcrumb dictionary

    :param key: Optinal. The key in the Breadcrumb dictionary

    :return: A Python object
    """
    if key is None:
      return JsObject.JsObject("%s" % self._selector)

    return JsObject.JsObject('%s["pmts"]["%s"]' % (self._selector, key))

  def hash(self, jsData):
    """
    Add an anchor to the URL after the hash tag

    Documentation
    https://www.w3schools.com/jsref/prop_loc_hash.asp

    :return:
    """
    return JsObject.JsObject('%s["anchor"] = %s' % (self._selector, JsUtils.jsConvertData(jsData, None)))



  @property
  def url(self):
    """
    Get the full URL

    :return:
    """
    js_location = JsLocation.JsLocation()
    origin = js_location.origin
    pathname = js_location.pathname
    return JsString.JsString(origin + pathname + "?" + JsObject.JsObject(self.toStr()))

  def toStr(self):
    fncToUrl = JsFncs.FncOnRecords(self._src._props['js']).url()
    return '%s(%s)' % (fncToUrl, self._selector)


class JsBase(object):
  class __internal(object):
    _props, _context, jsOnLoadEvtsFnc, http = {}, {}, [], []
    jsImports, cssImport = set([]), set([])

  def __init__(self, src=None):
    self._src = src if src else self.__internal() # The underlying source object is not supposed to be touched in the underlying classes
    self.console = JsConsole()
    self.localStorage = JsWindow.JsLocalStorage()
    self.window = JsWindow.JsWindow(self)
    self.performance = JsPerformance.JsPerformance()
    self.sessionStorage = JsWindow.JsSessionStorage()
    self.location = JsLocation.JsLocation()
    self.json = JsJson()
    self.math = JsMaths.JsMaths()
    #self.jquery = JsQuery.JQuery(src)

    # shortcut functions
    self.alert = self.window.alert
    self.log = self.console.log
    self._breadcrumb, self.__data = None, None

  @property
  def objects(self):
    """
    Interface to the main Javascript Classes and Primitives

    Documentation

    :return:
    """
    return JsObjects.JsObjects(self)

  def not_(self, data):
    """
    Add the Symbol (!) for the boolean negation.
    This feature is also available directly to any JsBoolean objects

    Example
    jsObj.not_(jsObj.objects.boolean.get("weekend"))

    Documentation
    https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Op%C3%A9rateurs/Op%C3%A9rateurs_logiques

    :param data: The Javascript Object considered as a boolean
    :return: The Javascript fragment string
    """
    jsData = JsUtils.jsConvertData(data, None)
    return JsFncs.JsFunction("!%s" % jsData)

  def if_(self, jsCond, jsFnc):
    """
    Conditional statements are used to perform different actions based on different conditions.

    Documentation:
    https://www.w3schools.com/js/js_if_else.asp

    :param jsCond:
    :param jsFnc:

    :return:
    """
    if isinstance(jsCond, list):
      jsCond = "(%s)" % ")||(".join(JsUtils.jsConvertFncs(jsCond))
    self.__if = JsIf.JsIf(jsCond, jsFnc, self._src)
    return self.__if

  def return_(self, jsData):
    """
    Javascript return keyword

    :param jsData: The Javascript expression
    :return:
    """
    return JsFncs.JsFunction("return %s" % jsData)

  def switch(self, jsObj):
    """

    Documentation:
      - https://www.w3schools.com/js/js_switch.asp

    :param jsFnc:
    :return:
    """
    if not hasattr(jsObj, 'varName'):
      if isinstance(jsObj, list):
        jsObj = JsArray.JsArray(jsObj, setVar=True)
      else:
        jsObj = JsObject.JsObject(jsObj, setVar=True)
    self.__switch = JsSwitch.JsSwitch(jsObj, self._context)
    return self.__switch

  def while_(self, pivot, jsFnc=None, iterVar='i', start=0, step=1):
    """

    :param jsCond:
    :return:
    """
    jsPivot = JsUtils.jsConvertData(pivot, jsFnc)
    if isPyData and isinstance(pivot, (list, range)):
      self.__while = JsWhile.JsWhile(jsPivot, ruleType='array', iterVar=iterVar, start=start, step=step, context=self._context)
    elif isPyData and isinstance(pivot, dict):
      self.__while = JsWhile.JsWhile(jsPivot, ruleType='dict', iterVar=iterVar, start=start, step=step, context=self._context)
    else:
      self.__while = JsWhile.JsWhile(jsPivot, self._context)
    return self.__while

  def for_(self, iterable, jsDataKey=None, isPyData=False, jsFnc=None, iterVar='i', start=0, step=1):
    """

    :param iterable:
    :return:
    """
    jsIterable = JsUtils.jsConvert(iterable, jsDataKey, isPyData, jsFnc)
    self.__for = JsFor.JsFor(jsIterable, iterVar, start, step, self._context)
    return self.__for

  def custom(self, jsData, jsDataKey=None, isPyData=False, jsFnc=None):
    """
    Allow the definition of bespoke javascript strings

    Example:
      -

    """
    jsData = JsUtils.jsConvert(jsData, jsDataKey, isPyData, jsFnc)
    self._src._props.setdefault('js', {}).setdefault('bespoke', []).append(jsData)

  def _addImport(self, importAlias):
    """

    :param importAlias:
    :return:
    """
    self._src._props.setdefault('js', {}).setdefault('imports', set([])).add(importAlias)
    return self

  def extendProto(self, pyClass, fncName, jsFncs, pmts=None):
    """
    Javascript Framework extension

    Hook in the base class to allow the definition of specific function to add extra primitive features.
    Usual this function should be used in a wrapper function with the same name in order to have a coherent bridge between
    Python and Javascript.

    Documentation
    https://www.w3schools.com/js/js_object_prototypes.asp

    :param pyClass: The PyJs Classname
    :param fncName: The Javascript function name
    :param jsFncs: The Javascript function definition
    :param pmts: The Javascript function parameters

    :return: The JsObject
    """
    jsData = JsUtils.jsConvertFncs(jsFncs)
    self._src._props.setdefault('js', {}).setdefault('prototypes', {})["%s.prototype.%s" % (pyClass._jsClass, fncName)] = {"content": ";".join(jsData), 'pmts': pmts}
    return self

  @property
  def fncs(self):
    """
    Property to the predefined Javascript functions

    :rtype: JsFncs.JsRegisteredFunctions
    :return: The predefined functions
    """
    return JsFncs.JsRegisteredFunctions(self._src)

  @property
  def breadcrumb(self):
    """
    Create a internal Breadcrumb to keep track of the user journey within your page.

    Documentation
    https://www.w3schools.com/howto/howto_css_breadcrumbs.asp

    :return: A Python breadcumb object
    """
    if self._breadcrumb is None:
      self._breadcrumb = JsBreadCrumb(self._src)
    return self._breadcrumb

  def registerFunction(self, fncName, jsFncs, pmts=None):
    """
    Javascript Framework extension

    Register a predefined Javascript function
    This is only dedicated to specific Javascript transformation functions

    Example


    :param fncName: The function name
    :param jsFncs: Optional. The Javascript function definition
    :param pmts: Optional

    :return: The JsObject
    """
    jsData = JsUtils.jsConvertFncs(jsFncs)
    self._src._props.setdefault('js', {}).setdefault('functions', {})[fncName] = {'content': ";".join(jsData), 'pmt': pmts}
    return self

  def clipboard(self, jsData):
    """
    Copy the full URL to rhe clipboard

    Documentation
    https://isabelcastillo.com/hidden-input-javascript

    :return:
    """
    return JsFncs.JsFunction('''
        var elInput = document.createElement('input'); 
        elInput.setAttribute('type', 'text');
        elInput.setAttribute('value', %s); document.body.appendChild(elInput);
        document.execCommand('copy', false, elInput.select()); elInput.remove()''' % JsUtils.jsConvertData(jsData, None))

  def addOnLoad(self, jsFncs):
    """
    Add javascript fragment dedicated to build the HTML page during the onLoad event.

    Documentation

    :param jsFncs: The Javascript functions to be added to this section

    :return:
    """
    self._src._props.setdefault('js', {}).setdefault('builders', []).append(";".join(JsUtils.jsConvertFncs(jsFncs)))
    return self

  def addKeyEvent(self, jsFncs, keyCode=None, keyCondition=None):
    """
    Add keyboard event to the document

    Either the keyCode or the keyCondition can be None

    Documentation
    http://gcctech.org/csc/javascript/javascript_keycodes.htm

    :param jsFncs: The Javascript function
    :param keyCode: Optional. The keycode as an integer
    :param keyCondition: Optional. A special condition based on the code

    :return:
    """
    if keyCode is None and keyCondition is None:
      raise Exception("keyCode or keyCondition must be defined")

    if keyCode is not None and keyCondition is not None:
      raise Exception("keyCode or keyCondition cannot be both defined")

    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]

    if keyCode is not None:
      keyCondition = "code == %s" % keyCode
    self._src._props.setdefault('js', {}).setdefault('keyboard', {})[keyCondition] = ";".join(JsUtils.jsConvertFncs(jsFncs))
    return self

  def preload(self, ajaxParams):
    """
    Preload feature to be able to produce pre cached files.
    Those files will be produced in a asynchrone way and they will facilitate the fluidity in the web dashboard.
    The success file is only used as an indicator to check if the preload function has to be started. If the file is already present it will not be triggered.
    The status will be based on the return of the service in the query return (true / false

    Tip: Put a variable result to your service return in order to change the icon according to the status of your asynchronous call

    Example
    report.preload([{'url': "Test.py", 'success': 'test.csv'}])

    :param ajaxParams:

    :return: The Python object itself
    """
    pass

  def addOnReady(self, jsFncs):
    """
    The ready event occurs when the body DOM (document object model) has been loaded.

    Documentation
    https://www.w3schools.com/jquery/event_ready.asp

    :param jsFncs: The Javascript functions to be added to this section
    """
    self._src._props.setdefault('js', {}).setdefault('onReady', []).append(";".join(JsUtils.jsConvertFncs(jsFncs)))
    return self

  def profile(self, type, htmlId, mark, recordsCount=""):
    """

    :param type:
    :param htmlId:
    :param mark:
    :param recordsCount:

    :return:
    """
    return "profileObj.push({type: '%s', htmlId: '%s', mark: '%s', records: %s})" % (type, htmlId, mark, recordsCount)


  # -----------------------------------------------------------------
  #                         DOCUMENTATION FUNCTIONS
  #
  # https://www.w3schools.com/jsref/dom_obj_document.a
  def getElementById(self, idName):
    """
    The getElementById() method returns the element that has the ID attribute with the specified value.

    Documentation:
    https://www.w3schools.com/jsref/met_document_getelementbyid.asp

    :param idName: Required. The ID attribute's value of the element you want to get

    :return: An Element Object, representing an element with the specified ID. Returns null if no elements with the specified ID exists
    """
    return JsNodeDom.JsDoms("document.getElementById('%s')" % idName)

  def getElementsByName(self, name):
    """
    The getElementsByName() method returns a collection of all elements in the document with the specified name (the value of the name attribute), as a NodeList object.

    The NodeList object represents a collection of nodes. The nodes can be accessed by index numbers. The index starts at 0.

    Documentation:
    https://www.w3schools.com/jsref/met_doc_getelementsbyname.asp

    :param name: Required. The name attribute value of the element you want to access/manipulate

    :return: A NodeList object, representing a collection of elements with the specified name.
             The elements in the returned collection are sorted as they appear in the source code.
    """
    return "document.getElementsByName(%s)" % name

  def getElementsByTagName(self, tagName, i=0):
    """
    The getElementsByTagName() method returns a collection of an elements's child elements with the specified tag name, as a NodeList object.

    The NodeList object represents a collection of nodes. The nodes can be accessed by index numbers. The index starts at 0.

    Documentation:
    https://www.w3schools.com/jsref/met_element_getelementsbytagname.asp

    :param tagName: Required. The tagname of the child elements you want to get
    :param i:

    :return:
    """
    return JsNodeDom.JsDoms("document.getElementsByTagName('%s')[%s]" % (tagName, i), varName="%s_%s" % (tagName, i), setVar=True)

  def createElement(self, tagName, varName=None, setVar=True, dom_id=None):
    """
    The createElement() method creates an Element Node with the specified name.

    Documentation
    https://www.w3schools.com/jsref/met_document_createelement.asp

    :param tagName: Required. The name of the element you want to create
    :param varName: Optional. The variable name to be set. Default random name
    :param setVar: Optional. Create a variable for the new object. Default True
    :param dom_id:

    :return:
    """
    dom_obj = JsNodeDom.JsDoms.new(tagName, varName=varName, setVar=setVar, report=self._src)
    if dom_id is not None:
      dom_obj.attr("id", dom_id)
    return dom_obj

  def createTextNode(self, jsString=None):
    """
    The createTextNode() method creates a Text Node with the specified text.

    Documentation:
    https://www.w3schools.com/jsref/met_document_createtextnode.asp

    :param jsString: Required. The text of the Text node

    :return: A Text Node object with the created Text Node
    """
    return JsObject.JsObject("document.createTextNode(%s)" % JsUtils.jsConvertData(jsString, None), isPyData=False)

  def encodeURIComponent(self, uri):
    """
    The encodeURIComponent() function encodes a URI component

    Documentation
    https://www.w3schools.com/jsref/jsref_encodeuricomponent.asp

    :param uri: Required. The URI to be encoded

    :return: A String, representing the encoded URI
    """
    return JsObject.JsObject("encodeURIComponent(%s)" % JsUtils.jsConvertData(uri, None))

  def decodeURIComponent(self, url_enc):
    """
    The decodeURIComponent() function decodes a URI component.

    Documentation
    https://www.w3schools.com/jsref/jsref_decodeuricomponent.asp

    :param url_enc: Required. The URI to be decoded

    :return: A String, representing the decoded URI
    """
    return JsObject.JsObject("decodeURIComponent(%s)" % JsUtils.jsConvertData(url_enc, None))

  @property
  def body(self):
    return JsNodeDom.JsDoms("document.body", setVar=False, isPyData=False)

  @property
  def data(self):
    if self.__data is None:
      self.__data = JsData.JsData(self._src)
    return self.__data

  def string(self, data, varName=None, setVar=False, isPyData=True):
    """
    Shortcut to the Javascript String primitives

    :param data:
    :param varName:
    :param setVar:
    :param isPyData:
    """
    return JsString.JsString(data, varName, setVar, isPyData, report=self._src)

  def number(self, data, varName=None, setVar=False, isPyData=True):
    """
    Shortcut to the Javascript Number primitives

    :param data:
    :param varName:
    :param setVar:
    :param isPyData:
    """
    return JsNumber.JsNumber(data, varName, setVar, isPyData, report=self._src)

  def object(self, data, varName=None, setVar=False, isPyData=True):
    """
    Shortcut to the Javascript Object primitives

    :param data:
    :param varName:
    :param setVar:
    :param isPyData:
    """
    return JsObject.JsObject(data, varName, setVar, isPyData, report=self._src)

  def activeElement(self):
    """
    The activeElement property returns the currently focused element in the document.

    Documentation:
    https://www.w3schools.com/jsref/prop_document_activeelement.asp

    :return: A reference to the element object in the document that has focus
    """
    return JsNodeDom.JsDoms("document.activeElement")

  def title(self, text=None):
    """
    The title property sets or returns the title of the current document (the text inside the HTML title element).

    Documentation:
    https://www.w3schools.com/jsref/prop_doc_title.asp

    :param text: A String, representing the title of the document

    :return:
    """
    if text is None:
      return JsString.JsString(text)

    return "document.title = %s" % JsUtils.jsConvertData(text, None)

  def getElementsByClassName(self, clsName):
    """
    The getElementsByClassName() method returns a collection of all elements in the document with the specified class name, as a NodeList object.

    Documentation:
    https://www.w3schools.com/jsref/met_document_getelementsbyclassname.asp

    :param clsName: Required. The class name of the elements you want to get.

    :return: A NodeList object, representing a collection of elements with the specified class name.
             The elements in the returned collection are sorted as they appear in the source code.
    """
    return "document.getElementsByClassName(%s)" % clsName

  def hasFocus(self):
    """
    The hasFocus() method returns a Boolean value indicating whether the document (or any element inside the document) has focus.

    Documentation:
    https://www.w3schools.com/jsref/met_document_hasfocus.asp

    :return: A Boolean value, incidating whether the document or any element in the document has focus:
    """
    return "document.hasFocus()"

  def execCommand(self, command, showUI, value):
    """
    The execCommand() method executes the specified command for the selected part of an editable section.

    Documentation:
    https://www.w3schools.com/jsref/met_document_execcommand.asp

    :param command:	 Specifies the name of the command to execute on the selected section
    :param showUI: A Boolean, specifies if the UI should be shown or not
    :param value: Some commands need a value to be completed

    :return: A Boolean, false if the command is not supported, otherwise true
    """
    return "document.execCommand('%s')" % command

  def createEvent(self, type):
    """
    The createEvent() method creates an event object.

    The event can be of any legal event type, and must be initialized before use.

    Documentation:
    https://www.w3schools.com/jsref/event_createevent.asp

    :param type: Required. A String that specifies the type of the event.

    :return: An Event object
    """
    if type not in ['AnimationEvent', 'ClipboardEvent', 'DragEvent', 'FocusEvent', 'HashChangeEvent', 'InputEvent',
                    'MouseEvent', 'PageTransitionEvent', 'PopStateEvent', 'ProgressEvent', 'StorageEvent', 'TouchEvent',
                    'TransitionEvent', 'UiEvent', 'WheelEvent', 'KeyboardEvent']:
      raise Exception("Not recognized type %s" % type)

  def createAttribute(self, attributename):
    """
    The createAttribute() method creates an attribute with the specified name, and returns the attribute as an Attr object.

    Documentation:
    https://www.w3schools.com/jsref/met_document_createattribute.asp

    :param attributename: Required. The name of the attribute you want to create

    :return: A Node object, representing the created attribute
    """
    return JsNodeAttributes.JsAttributes(attributename)

  def writeln(self, jsString):
    """
    The writeln() method is identical to the document.write() method, with the addition of writing a newline character after each statement.

    Documentation:
    https://www.w3schools.com/jsref/met_doc_writeln.asp

    :param jsString: Optional. What to write to the output stream.
                     Multiple arguments can be listed and they will be appended to the document in order of occurrence

    :return: No return value
    """
    return "document.writeln(%s)" % jsString

  # -----------------------------------------------------------------
  #                         DATA TYPES
  #
  # def date(self, data=None, varName=None, setVariable=False):
  #   """
  #   Create or get a Javascript Date object.
  #
  #   Example
  #   rptObj.js.date(setVariable=False).getMonth()
  #
  #   Documentation
  #   https://www.w3schools.com/jsref/jsref_obj_date.asp
  #
  #   :param data: The object data
  #   :param varName: The array javascript reference
  #   :param setVariable: A flag to force the variable to be defined on the Javascript side
  #   :return: A Python JsDate object
  #   """
  #   if data is not None and varName is not None:
  #     setVariable = True
  #   return JsDate.JsDate(data, varName, setVariable)
  #
  # def array(self, data=None, varName=None, setVariable=False):
  #   """
  #   Create or get a Javascript Array object.
  #
  #   Example
  #   rptObj.js.array([], varName="myList")
  #
  #   Documentation
  #   https://www.w3schools.com/jsref/jsref_obj_array.asp
  #
  #   :param data: The object data
  #   :param varName: The array javascript reference
  #   :param setVariable: A flag to force the variable to be defined on the Javascript side
  #   :return: A Python JsArray object
  #   """
  #   if data is not None and varName is not None:
  #     setVariable = True
  #   return JsArray.JsArray(data, varName, setVariable)
  #
  # def object(self, data=None, varName=None, setVariable=False):
  #   """
  #
  #   :param varName:
  #   :param varType:
  #   :return:
  #   """
  #   if data is not None and varName is not None:
  #     setVariable = True
  #   return JsObject.JsObject(data, varName, setVariable)
  #
  # def number(self, data=None, varName=None, setVariable=False):
  #   """
  #   Create or get a Javascript Number object.
  #
  #   Example
  #   rptObj.js.number(0, varName="myNumber")
  #   rptObj.js.number(varName="myNumber") + 76
  #
  #   Documentation
  #   https://www.w3schools.com/jsref/jsref_obj_number.asp
  #
  #   :param data: The object data
  #   :param varName: The array javascript reference
  #   :param setVariable: A flag to force the variable to be defined on the Javascript side
  #   :return: A Python JsNumber object
  #   """
  #   if data is not None and varName is not None:
  #     setVariable = True
  #   return JsNumber.JsNumber(data, varName, setVariable)
  #
  # def string(self, data=None, varName=None, setVariable=False):
  #   """
  #
  #   :param data:
  #   :param varName:
  #   :param setVariable:
  #   :return: A Python JsString object
  #   """
  #   if data is not None and varName is not None:
  #     setVariable = True
  #   return JsString.JsString(JsUtils.jsConvertData(data, None), varName=varName, setVar=setVariable)

  def parseFloat(self, jsString):
    """
    The parseFloat() function parses a string and returns a floating point number.

    Documentation:
      - https://www.w3schools.com/jsref/jsref_parseint.asp

    :param jsString: Required. The string to be parsed
    :return: A Number. If the first character cannot be converted to a number, NaN is returned
    """
    return JsNumber.JsNumber("parseFloat(%s)" % jsString, isPyData=False)

  def parseInt(self, jsString):
    """
    The parseInt() function parses a string and returns an integer.

    Documentation:
      - https://www.w3schools.com/jsref/jsref_parseint.asp

    :param jsString: Required. The string to be parsed
    :return: A Number. If the first character cannot be converted to a number, NaN is returned
    """
    return JsNumber.JsNumber("parseInt(%s)" % jsString, isPyData=False)

  def parseDate(self, jsString):
    """
    The parse() method parses a date string and returns the number of milliseconds between the date string and midnight of January 1, 1970.

    Documentation:
    https://www.w3schools.com/jsref/jsref_parse.asp

    :param jsString: Required. A string representing a date
    :return: A Number, representing the number of milliseconds between the specified date-time and midnight January 1, 1970

    """
    return JsNumber.JsNumber("Date.parse(%s)" % jsString, isPyData=False)

  def getVar(self, varName, varType="var"):
    """
    Get the Javascript Variable name

    :param varName: The Variable name
    :param varType: The scope of the variable

    :return: Return the piece of script to be added to the Javascript
    """
    if varType == 'var':
      return "window['%s']" % varName

    return varName

  def addToDataDict(self, key, jsVal, jsDataKey=None, isPyData=True, jsFnc=None, jsData="data"):
    """

    :param key:
    :param jsVal:
    :param varType:
    :param jsDataKey:
    :param isPyData:
    :param jsFnc:
    :param jsData:

    :return:
    """
    jsVal = JsUtils.jsConvert(jsVal, jsDataKey, isPyData, jsFnc)
    return "%s['%s'] = %s" % (jsData, key, jsVal)

  def getItem(self, htmlCode):
    """

    :param htmlCode:

    :return:
    """
    if not htmlCode in self._context.get('htmlCodes', []):
      raise Exception("HTML Code - %s - not defined in the current report" % htmlCode)

    return "$('#%s')" % htmlCode

  def typeof(self, jsData):
    """

    :param jsData:

    :return:
    """
    return JsFncs.JsTypeOf(JsUtils.jsConvertData(jsData, None))

  def info(self, jsData, cssStyle=None, icon="fas fa-spinner fa-spin", seconds=10000):
    """
    Display a message

    Documentation
    https://fontawesome.com/how-to-use/on-the-web/styling/animating-icons

    :param jsData:
    :param cssStyle:
    :param icon:
    :param seconds:

    :return:
    """

    if cssStyle is None:
      cssStyle = {"position": "fixed", "bottom": "5px", "right": "10px", "padding": '2px 7px', "border": "1px solid black"}
    if icon is not None:
      self._src.jsImports.add('font-awesome')
      self._src.cssImport.add('font-awesome')
      return [
        self.createElement("i", varName="popup_icon").setAttribute("aria-hidden", True).css({"display": "inline-block",
                           "width": "auto", "height": "auto", "margin-right": '5px'}).className(icon),
        self.createElement("div", varName="popup_info").appendChild(self.objects.dom("popup_icon")).css(cssStyle).text(jsData),
        self.body.appendChild(self.objects.dom("popup_info")),
        self.window.setTimeout(self.objects.dom("popup_info").remove(), milliseconds=seconds)]

    return [
      self.createElement("div", varName="popup_info").css(cssStyle).text(jsData),
      self.body.appendChild(self.objects.dom("popup_info")),
      self.window.setTimeout(self.objects.dom("popup_info").remove(), milliseconds=seconds)]
