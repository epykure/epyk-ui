
import os
import re
import json
import functools

from epyk.core.js import Imports
from epyk.core.js.primitives import JsObject


# --------------------------------------------------------------------------------------------------------------
#                                                       DECORATORS
#
def incompatibleBrowser(browsers):
  """
  Description:
  ------------

  :param browsers: List. Incompatible browsers
  """
  def decorator(func):
    @functools.wraps(func)
    def decorated(*args, **kwargs):
      print("Warning: This function - %s - is not compatible with %s" % (func.__name__, ", ".join(browsers)))
      return func(*args, **kwargs)

    return decorated

  return decorator


def fromVersion(data):
  """
  Description:
  ------------
  This system decorate will decorate a component function to specify during the Python execution
  if a method is not yet available in the current state of the Javascript modules.

  Example
  .fromVersion({'jqueryui': '1.12.0'})

  :param data: Set the minimum version of a package for a specific function

  :return: The decorated function
  """
  def decorator(func):
    @functools.wraps(func)
    def decorated(*args, **kwargs):
      for k, v in data.items():
        if k in Imports.JS_IMPORTS:
          for mod in Imports.JS_IMPORTS[k]['modules']:
            if mod['version'] < v:
              raise Exception("Function %s can only be used from %s version %s (current %s)" % (func.__name__, k, v, mod['version']))

      return func(*args, **kwargs)

    return decorated

  return decorator


def untilVersion(data, newFeature):
  """
  Description:
  ------------
  This system decorate will decorate a component function to specify during the Python execution
  if a method is not available since the current state of the Javascript modules.
  Indeed as it is possible to override JS version on the fly it is also important to get notify with functions
  are not compatible anymore.
  This decorator will also propose an alternative with the new feature to.

  Usage::

      .untilVersion({'jqueryui': '1.12.0'}, "new function")

  :param data: String. The maximum version number of a package to use this function
  :param newFeature: String. The new function name

  :return: The decorated function
  """
  def decorator(func):
    @functools.wraps(func)
    def decorated(*args, **kwargs):
      for k, v in data.items():
        if k in Imports.JS_IMPORTS:
          for mod in Imports.JS_IMPORTS[k]['modules']:
            if mod['version'] > v:
              raise Exception("Function %s can only be used since %s version %s (current %s). It has been replaced by %s" % (func.__name__, k, v, mod['version'], newFeature))

      return func(*args, **kwargs)
    return decorated
  return decorator


# --------------------------------------------------------------------------------------------------------------
#                                                       FUNCTIONS
#
def jsConvertData(jsData, jsFnc):
  """
  Description:
  ------------
  Generic conversion function for any data in the internal framework.
  This will convert to String any data coming from the Javascript Python interface.

  Any pure Python object will be converted using the json function to be then written as a string
  to the resulting page

  :param jsData: The Python Javascript data
  :param jsFnc: Optional. The conversion function

  :return:
  """
  if not hasattr(jsData, 'varData') and not hasattr(jsData, 'fncName'):
    if hasattr(jsData, 'toStr'):
      return jsData.toStr()
    else:
      try:
        return JsObject.JsObject(json.dumps(jsData))

      except TypeError as err:
        return str(jsData)

      except Exception as err:
        if isinstance(jsData, range):
          return JsObject.JsObject(json.dumps(list(jsData)))

        raise

  return jsData


def jsConvert(jsData, jsDataKey, isPyData, jsFnc):
  """
  Description:
  ------------

  :param jsData:
  :param jsDataKey:
  :param isPyData:
  :param jsFnc:
  """
  if isPyData:
    if hasattr(jsData, 'toStr'):
      return jsData.toStr()
    else:
      try:
        return json.dumps(jsData)

      except Exception as err:
        if isinstance(jsData, range):
          return json.dumps(list(jsData))

        raise

  if jsDataKey is not None:
    jsData = "%s['%s']" % (jsData, jsDataKey)
  if jsFnc is not None:
    jsData = "%s(%s)" % (jsFnc, jsData)
  return jsData


def getJsValid(value, fail=True):
  """
  Return an error if the variable name is not valid following the Javascript naming conventions.
  Even if the function will fail it will propose a valid name to replace the one passed in input

  Example
  >>> getJsValid("test-js", False)
  'testjs'

  >>> getJsValid("234@test-js", False)
  'js234testjs'

  >>> getJsValid("234@test-js", True)
  Traceback (most recent call last):
      ...
  Exception: Javascript Variable name 234@test-js, for example you could use js234testjs instead

  Related Pages:

      https://www.w3schools.com/js/js_conventions.asp

  :param value: The Javascript variable name
  :param fail: Boolean to raise an exception if the name is not valid on the Javascript side

  :return: The input variable name or a suggested one
  """
  regex = re.compile('[^a-zA-Z0-9_]')
  cleanName = regex.sub('', value.strip())
  isValid = not value[0].isdigit() and cleanName == value
  if fail and not isValid:
    raise Exception("Javascript Variable name %s, for example you could use js%s instead" % (value, cleanName))

  if cleanName[0].isdigit():
    cleanName = "js%s" % cleanName
  return cleanName


def jsConvertFncs(jsFncs, isPyData=False, jsFncVal=None, toStr=False):
  """
  Description:
  ------------
  Generic conversion function for all the PyJs functions

  :param jsFncs: Array. The PyJs functions
  :param isPyData: Boolean. A flag to force the Python conversion using json
  :param jsFncVal:
  :param toStr: Boolean. A flag to specify if the result should be aggregated

  :return:
  """
  if not isinstance(jsFncs, list):
    jsFncs = [jsFncs]

  cnvFncs = []
  for f in jsFncs:
    if f is None:
      continue

    if hasattr(f, 'toStr'):
      strFnc = f.toStr()
      if jsFncVal is not None:
        strFnc = strFnc.replace("trans_val", jsFncVal)
      cnvFncs.append(strFnc)
    else:
      if isPyData:
        strVal = json.dumps(f)
        if jsFncVal is not None:
          strVal = strVal.replace("trans_val", jsFncVal)
        cnvFncs.append(strVal)
      else:
        if jsFncVal is not None:
          f = str(f).replace("trans_val", jsFncVal)
        cnvFncs.append(f)
  if toStr:
    return ";".join(cnvFncs)

  return cnvFncs


def cleanFncs(fnc):
  """
  Description:
  ------------
  Try to remove as much as possible all the characters in order to speed up the javascript
  Indeed most of the browsers are using minify Javascript to make the page less heavy

  Thus pre stored function code can be written to be easier to read.

  :param fnc: The Javascript String

  :return: Return a cleaned an minify Javascript String
  """
  return "".join([r.strip() for r in fnc.strip().split('\n')])


def isNotDefined(varName):
  """
  Description:
  ------------
  Check if a variable is defined

  Example
  JsUtils.isNotDefined(varId)

  :param varName: String. The varName
  :return: A string in Python and a Boolean in Javascript
  """
  return "typeof %s === 'undefined'" % varName


class JsFile(object):
  def __init__(self, scriptName=None, path=None):
    self.scriptName, self.path = scriptName, path
    self.file_path = os.path.join(path, "js") # all the files will be put in a common directory
    if not os.path.exists(self.file_path):
      os.mkdir(self.file_path)
    self.__data = []

  def writeJs(self, jsFncs):
    """
    Write the Javascript piece of code to the file

    Example
    dt = JsDate.new("2019-05-03")
    f.writeJs([dt,
      Js.JsConsole().log(dt.getDay()),
      Js.JsConsole().log(dt.getFullYear())])

    :param jsFncs: The Javascript fragments

    :return: The File object
    """
    self.__data.extend(jsConvertFncs(jsFncs))
    return self

  def writeReport(self, rptObj):
    """
    Write the Javascript content of a report to a structure .js file.
    This could help on the investigation and can be directly used in Codepen for testing

    :param rptObj: The report object

    :return:
    """
    props = rptObj._src._props if hasattr(rptObj, '_src') else rptObj._props
    for data_id, data in props.get("data", {}).get('sources', {}).items():
      self.__data.append("var data_%s = %s" % (data_id, json.dumps(data)))

    for k, v in props.get('js', {}).get('functions', {}).items():
      sPmt = "(%s)" % ", ".join(list(v["pmt"])) if "pmt" in v else "{}"
      self.__data.append("function %s%s{%s}" % (k, sPmt, v["content"].strip()))

    for c, d in props.get('js', {}).get("constructors", {}).items():
      self.__data.append(d)

    for c, d in props.get('js', {}).get("datasets", {}).items():
      self.__data.append(d)

    for b in props.get('js', {}).get("builders", []):
      self.__data.append(b)

    keyboardShortcuts = props.get('js', {}).get('keyboard', {})
    if keyboardShortcuts:
      self.__data.append("document.addEventListener('keydown', function(e){var code = e.keyCode || e.which")
      for k, v in keyboardShortcuts.items():
        self.__data.append("if(%s){%s}" % (k, v))
      self.__data.append("})")

  def codepen(self, rptObj, cssObj=None, target='_self'):
    """
    Send the piece of Javascript to Codepen for testing

    Related Pages:

      https://codepen.io/

    :param rptObj: The report object
    :param cssObj: The internal CSS object from the page
    :param target: A string flag to specify the target page in the browser
    """
    import webbrowser

    if hasattr(rptObj, '_to_html_obj'):
      results = rptObj._to_html_obj(content_only=True)
      js_external = re.findall('<script language="javascript" type="text/javascript" src="(.*?)"></script>', results['jsImports'])
      result = {"js": results["jsFrgs"], "js_external": ";".join(js_external)}
    else:
      self.writeReport(rptObj)
      import_obj = Imports.ImportManager(online=True)
      css_external = import_obj.cssURLs(import_obj.cssResolve(rptObj._src.cssImport))
      js_external = import_obj.jsURLs(import_obj.jsResolve(rptObj._src.jsImports))
      result = {"js": ";".join(self.__data), "js_external": ";".join(js_external), "css_external": ";".join(css_external)}
    if cssObj is not None:
      result["css"] = cssObj.toCss()
    data = rptObj.location.postTo("https://codepen.io/pen/define/", {"data": json.dumps(result)}, target=target)
    outFile = open(os.path.join(self.file_path, "CodePenJsLauncher.html"), "w")
    outFile.write('<html><body></body><script>%s</script></html>' % data.replace("\\\\n", ""))
    webbrowser.open(outFile.name)

  def close(self, jsObj=None):
    """
    Write the file and close the buffer

    :param jsObj: The internal JsObject
    """
    src_obj = jsObj._src if hasattr(jsObj, '_src') else jsObj
    outFile = open(os.path.join(self.file_path, "%s.js" % self.scriptName), "w")
    js_external = ""
    if jsObj is not None:
      outFile.write("//Javascript Prototype extensions \n\n")
      for fnc, details in src_obj._props.get('js', {}).get('prototypes', {}).items():
        outFile.write("%s = function(%s){%s};" % (fnc, ",".join(details.get('pmts', [])), details["content"]))
      outFile.write("\n\n//Javascript Global functions \n\n")
      for fnc, details in src_obj._props.get('js', {}).get('functions', {}).items():
        outFile.write("function %s(%s){%s}" % (fnc, ",".join(details.get('pmt', [])), details["content"]))
      import_obj = Imports.ImportManager(online=True)
      js_external = import_obj.jsResolve(src_obj.jsImports)
    outFile.write("\n\n")
    outFile.write("//Javascript Data\n\n")
    for data_id, data in src_obj._props.get("data", {}).get('sources', {}).items():
      outFile.write("var data_%s = %s" % (data_id, json.dumps(data)))
    outFile.write("\n\n")
    outFile.write("//Javascript functions\n\n")
    if len(src_obj._props.get('js', {}).get('onReady', [])) > 0:
      outFile.write("%s;" % jsConvertFncs(src_obj._props.get('js', {}).get('onReady', []), toStr=True))
    outFile.write(";".join(self.__data))
    outFile.close()
    with open(r"%s\Launche_%s.html" % (self.path, self.scriptName), "w") as f:
      f.write('<html><head></head><body></body>%s<script src="js/%s.js"></script></html>' % (js_external, self.scriptName))
    return r"%s\Launche_%s.html" % (self.path, self.scriptName)
