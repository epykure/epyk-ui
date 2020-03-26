from epyk.core.js.primitives import JsString
from epyk.core.js.primitives import JsObjects
from epyk.core.js import JsUtils

def packageImport(jsPackage=None, cssPackage=None):
  def wrap(func):
    def inner(rptObj, *args, **kwargs):
      report = getattr(rptObj, '_report') if getattr(rptObj, '_report', None) else rptObj
      if jsPackage:
        report.jsImports.add(jsPackage)
      if cssPackage:
        report.cssImport.add(cssPackage)
      return func(rptObj, *args, **kwargs)

    return inner

  return wrap




class JsPackage(object):
  lib_alias, lib_selector, lib_set_var = None, None, True

  class __internal(object):
    # By default it will attach eveything to the body
    jqId, jsImports, cssImport = '', set([]), set([])

  def __init__(self, src=None, varName=None, selector=None, data=None, setVar=None, parent=None):
    self.src = src if src is not None else self.__internal()
    self._selector = selector if selector is not None else self.lib_selector
    self.varName, self.setVar, self._parent = varName, self.lib_set_var if setVar is None else setVar, parent
    self._data = data
    self._js, self._u, self._js_enums = [[]], {}, {} # a list of list of object definition
    self.__js_uniq_fncs = {}
    if self.lib_alias is not None:
      if 'css' in self.lib_alias:
        self.src.cssImport.add(self.lib_alias['css'])
      if 'js' in self.lib_alias:
        self.src.jsImports.add(self.lib_alias['js'])

  @property
  def varId(self):
    """
    Description:
    ------------
    The Javascript and Python reference ID
    """
    return self._selector if self.varName is None else self.varName

  def version(self, ver):
    """
    Description:
    ------------
    Change the package version number

    Usage:
    ------
    bar.chart.version("1.11.0")

    Attributes:
    ----------
    :param ver: String. The package versions example 1.11.0
    """
    self.src._props.setdefault("packages", {})[self.lib_alias] = ver
    return self

  def fnc(self, data, unique=False):
    """
    Description:
    ------------
    Base function to allow the object chain.
    THis will add the elements to the current section in the object structure
    All the items at the same level wil be chained

    Attributes:
    ----------
    :param data: String. THe Javascript fragment to be added
    :param unique: Boolean. Ensure the function is available one time in the chain. If not the last call we will present

    :return: "Self" to allow the chains
    """
    if unique:
      fnc_name = data.split("(")[0]
      if fnc_name in self.__js_uniq_fncs:
        i, j = self.__js_uniq_fncs[fnc_name]
        self._js[i].pop(j)
      self.__js_uniq_fncs[fnc_name] = (len(self._js)-1, self._js[-1])
    self._js[-1].append(data)
    return self

  def fnc_enum(self, name, data_class):
    """
    Description:
    ------------
    Base function to allow the creation of function with parameters which are list of dataclasses.
    Basically this will be then transpiled to a list of dictionary

    :param name: String. The function Name
    :param data_class: Class. The Python Data class
    """
    index = len(self._js) - 1
    if not index in self._js_enums:
      self._js_enums[index] = {name: []}
      self._js[-1].append(name)
    elif not name in self._js_enums[index]:
      self._js_enums[index][name] = []
      self._js[-1].append(name)
    self._js_enums[index][name].append(data_class(self.src))
    return self._js_enums[index][name][-1]

  def fnc_closure(self, data, checkUndefined=False, unique=False):
    """
    Description:
    ------------
    Add the function string to the existing object definition but create a new entry point for the next ones.
    This structure will allow the chain on the Javascript side but also on the Python side.

    Thanks to this Python can always keep the same structure and produce the correct Javascript definition
    There will be no chain in the Javascript side

    Attributes:
    ----------
    :param data: String. The Javascript fragment to be added
    :param checkUndefined: Boolean. Add a check on the variable definition
    :param unique: Boolean. Ensure the function is available one time in the chain. If not the last call we will present

    :return: The "self" to allow the chains
    """
    if unique:
      fnc_name = data.split("(")[0]
      if fnc_name in self.__js_uniq_fncs:
        i, j = self.__js_uniq_fncs[fnc_name]
        self._js[i].pop(j)
      self.__js_uniq_fncs[fnc_name] = (len(self._js)-1, self._js[-1])

    self._js[-1].append(data)
    if checkUndefined:
      self._u[len(self._js) - 1] = checkUndefined
    self._js.append([])
    return self

  def fnc_closure_in_promise(self, data, checkUndefined=False):
    """
    Description:
    ------------
    Base function to allow the creation of a promise.

    A Js promise is an event attached toa function which will be only executed after the function.
    In case of success the then will be triggered otherwise the exception will be caught.

    Attributes:
    ----------
    :param data: String. The Javascript fragment to be added
    :param checkUndefined: Boolean. Add a check on the variable definition

    :return: The promise
    """
    self._js[-1].append(JsObjects.JsPromise(data))
    if checkUndefined:
      self._u[len(self._js) - 1] = checkUndefined
    self._js.append([])
    return data

  @property
  def var(self):
    """
    Description:
    ------------
    Property to return the variable name as a valid pyJs object
    """
    return JsString.JsString(self.varId, isPyData=False)

  def set_var(self, flag):
    """
    Description:
    ------------
    Change the flag to define if the variable should be defined on the Javascript side.
    Default this is set to True

    Attributes:
    ----------
    :param flag: A python boolean

    :return: This in order to allow js chains
    """
    self.setVar = flag
    return self

  def getStr(self, emptyStack=True):
    """
    Description:
    ------------
    Get the current string representation for the object and remove the stack
    """
    js_stack = None
    if not emptyStack:
      js_stack = list(self._js)
    content = self.toStr()
    if not emptyStack:
      self._js = js_stack
    if not content:
      return self.varId

    return content

  def _mapVarId(self, strFnc, varId):
    """
    Description:
    ------------
    Special function used for some external packages used to fix the problem of function override.
    Indeed in Datatable row.add is used as a class method compare to the other functions used at object level

    Attributes:
    ----------
    :param strFnc: The function string
    :param varId: The object reference

    :return: The converted object reference
    """
    return varId

  def toStr(self):
    """
    Description:
    ------------
    Javascript representation

    :return: Return the Javascript String
    """
    if self._selector is None:
      raise Exception("Selector not defined, use this() or new() first")

    obj_content = []
    # TODO find better way to check emtpy js structure
    if self._js != [[]]:
      for i, js in enumerate(self._js):
        if len(js) == 0:
          continue

        fnc_frg = []
        for d in js:
          if hasattr(d, "toStr"):
            fnc_frg.append(d.toStr())
          else:
            if i in self._js_enums and d in self._js_enums[i]:
              fnc_frg.append("%s([%s])" % (d, ",".join([str(s) for s in self._js_enums[i][d]])))
            else:
              fnc_frg.append(d)
        str_fnc = ".".join(fnc_frg)
        if self.setVar:
          if str_fnc:
            str_fnc = "var %s = %s.%s" % (self.varId, self._selector, str_fnc)
          else:
            str_fnc = "var %s = %s" % (self.varId, self._selector)
          self.setVar = False
        else:
          if str_fnc:
            if i in self._u:
              # to avoid raising an error when the variable is not defined
              str_fnc = "if(%s !== undefined){%s.%s}" % (self.varId, self.varId, str_fnc)
            else:
              varId = self._mapVarId(str_fnc, self.varId)
              str_fnc = "%s.%s" % (varId, str_fnc)
          else:
            str_fnc = self.varId
        obj_content.append(str_fnc)
    else:
      if self.setVar:
        obj_content = ["var %s = %s" % (self.varId, self._selector)]
    self._js = [[]] # empty the stack
    return "; ".join(obj_content)


class DataAttrs(object):
  def __init__(self, report, attrs=None, oprions=None):
    self._report, self.oprions, self._attrs = report, oprions, attrs or {}

  def custom(self, name, value):
    """
    Description:
    ------------
    Custom function to add a bespoke attribute to a class.

    This entry point will not be able to display any documentation but it is a shortcut to test new features.
    If the value is a Javascript object, the PyJs object must be used

    Attributes:
    ----------
    :param name: String. The key to be added to the attributes
    :param value: String or JString. The value of the defined attributes

    :return: The DataAttrs to allow the chains
    """
    self._attrs[name] = JsUtils.jsConvertData(value, None)
    return self

  def attr(self, name, value):
    """
    Description:
    ------------
    Add an attribute to the Javascript underlying dictionary

    Attributes:
    ----------
    :param name: String. The attribute name
    :param value: Object. The attribute value

    :return: "Self" to allow the chains on the Python side
    """
    self._attrs[name] = value
    return self

  def attrs(self, values):
    """
    Description:
    ------------
    Set multiple attributes to the underlying data directly from a dictionary

    Attributes:
    ----------
    :param values: Dictionary. The data to set

    :return: "Self" to allow the chains on the Python side
    """
    self._attrs.update(values)
    return self

  def __str__(self):
    """
    Description:
    ------------
    Produce the resulting string to be added to the Javascript section of the web page
    """
    return "{%s}" % ", ".join(["%s: %s" % (k, v) for k, v in self._attrs.items()])

  def toStr(self):
    """

    :return:
    """
    return "{%s}" % ", ".join(["%s: %s" % (k, JsUtils.jsConvertData(v, None)) for k, v in self._attrs.items()])
