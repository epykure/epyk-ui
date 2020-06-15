"""
Module dedicated to wrap the Javascript Object

"""

import json

from epyk.core.js import JsUtils

_JSVARS = 0


class JsKeyword(object):
  def __init__(self, keyword):
    self.__keyword = keyword

  def toStr(self):
    return self.__keyword

  def __str__(self):
    return self.__keyword


class JsObject(object):
  _jsClass = "Object"

  def __init__(self, data, varName=None, setVar=False, isPyData=False, report=None):
    """

    Related Pages:

			https//www.w3schools.com/js/js_type_conversion.asp

    Attributes:
    ----------
    :param varName:
    :param data:
    :param setVar:
    :param isPyData:
    :param report: The internal report object

    """
    global _JSVARS

    self.varName, self.varData, self._js, self._report = varName, str(data), [], report
    self._frozen, self._sealed = False, False
    if varName is None and setVar:
      _JSVARS += 1
      self.varName = "%s_%s" % (self.__class__.__name__, _JSVARS)
    if setVar:
      self.setVar(self.varName)

  @classmethod
  def new(cls, data=None, varName=None, isPyData=True, report=None):
    """
    Create a Python Javascript Object

    Example
    JsDate.new("2019-05-03", varName="MyDate")

    Related Pages:

			https://www.w3schools.com/jsref/jsref_obj_date.asp

    :param data: Optional, The object data
    :param varName: Optional, The object variable name
    :param isPyData: Optional, Boolean to specify if it is a Python reference and if it should be converted to Json
    :param report: The internal report object

    :return: The Python Javascript Date primitive
    """
    if isPyData:
      return cls(data=JsUtils.jsConvertData(data, None), varName=varName, setVar=True, isPyData=isPyData, report=report)

    return cls(data=data, varName=varName, setVar=True, isPyData=isPyData, report=report)

  @classmethod
  def this(cls, report=None):
    """
    Get the object this

    Example
    jsObj.object.this

    Related Pages:

			https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this

    :param report: The internal report object

    :return: The python Javascript object
    """
    return cls.get("this", report=report)

  @classmethod
  def get(cls, varName, report=None):
    """
    Get the Javascript Object by its reference

    Example
    JsDate.new("2019-05-03", varName="MyDate")
    JsDate.get("MyDate")

    Related Pages:

			https://www.w3schools.com/jsref/jsref_obj_date.asp

    :param varName: The Javascript object reference
    :param report: The internal report object

    :return: The python Javascript object
    """
    return cls(data=None, varName=varName, setVar=False, report=report)

  @property
  def varId(self):
    """
    The Javascript and Python reference ID

    :return: The Javascript String of the object variable name
    """
    return self.varData if self.varName is None else self.varName

  def setVar(self, varName, varType="var"):
    """
    The setVar() method will defined the variable name and use this reference in the future

    Example

    Documentation

    :param varName: Required, The variable name
    :param varType: The type of variable to be set on the Javascript side

    :return: The Python Javascript Object
    """
    if varName is None:
      return self

    if varName != self.varName:
      if len(self._js) == 1:
        if self._js[0].startswith("var "):
          # Remove the entry used to define by default the javascript object
          self._js = ["%s %s = %s" % (varType, varName, self.varData)]
        else:
          self._js.append("%s %s = %s" % (varType, varName, self.varName))
      else:
        self._js.append("%s %s = %s" % (varType, varName, self.varName or self.varData))
    else:
      self._js.append("%s %s = %s" % (varType, varName, self.varData))
    return self

  def prototype(self, name, value):
    """
    The prototype property allows you to add new properties and methods to existing object types.

    Documentation:
      - https://www.w3schools.com/jsref/jsref_prototype_string.asp

    :param name: The objects property name
    :param value: The objects property values

    :return: A reference to the String.prototype object
    """
    return "%s.prototype.%s = %s" % (self.varName, name, value)

  def add(self, n):
    """
    Add value to a Javascript Number.
    The value will be added and it will return a new number object on the Javascript side

    Example
    jsNumber.add(34.5)

    Documentation

    :param n: The number value

    :return: A new Python Javascript Number
    """
    jsData = JsUtils.jsConvertData(n, None)
    return JsObject("%s + %s" % (self.varId, jsData), isPyData=False)

  def __add__(self, value):
    return JsObject("%s += %s" % (self.varId, value), isPyData=False)

  def __sub__(self, value):
    return JsObject("%s -= %s" % (self.varId, value), isPyData=False)

  def __mul__(self, value):
    return JsObject("%s *= %s" % (self.varId, value), isPyData=False)

  def __truediv__(self, value):
    return JsObject("%s /= %s" % (self.varId, value), isPyData=False)

  def __mod__(self, value):
    return JsObject("%s %%= %s" % (self.varId, value), isPyData=False)

  def __pow__(self, value):
    from epyk.core.js import JsMaths

    return JsObject("%s = %s" % (self.varId, JsMaths.JsMaths.pow(self, value)))

  def __eq__(self, a):
    """

    :param a:

    :return:
    """
    if hasattr(a, 'toStr'):
      return "%s == %s" % (self.varId, a.toStr())

    if hasattr(a, 'varName'):
      return "%s == %s" % (self.varId, a.varName)

    return "%s == %s" % (self.varId, json.dumps(a))

  def __lt__(self, a):
    """

    :param a:
    :return:
    """
    if hasattr(a, 'toStr'):
      return "%s < %s" % (self.varId, a.toStr())

    if hasattr(a, 'varName'):
      return "%s < %s" % (self.varId, a.varName)

    return "%s < %s" % (self.varId, json.dumps(a))

  def __le__(self, a):
    """

    :param a:

    :return:
    """
    if hasattr(a, 'toStr'):
      return "%s <= %s" % (self.varId, a.toStr())

    if hasattr(a, 'varName'):
      return "%s <= %s" % (self.varId, a.varName)

    return "%s <= %s" % (self.varId, json.dumps(a))

  def __ne__(self, a):
    """

    :param a:

    :return:
    """
    if hasattr(a, 'toStr'):
      return "%s != %s" % (self.varId, a.toStr())

    if hasattr(a, 'varName'):
      return "%s != %s" % (self.varId, a.varName)

    return "%s != %s" % (self.varId, json.dumps(a))

  def __gt__(self, a):
    """

    :param a:

    :return:
    """
    if hasattr(a, 'toStr'):
      return "%s > %s" % (self.varId, a.toStr())

    if hasattr(a, 'varName'):
      return "%s > %s" % (self.varId, a.varName)

    return "%s > %s" % (self.varId, json.dumps(a))

  def __ge__(self, a):
    """

    :param a:

    :return:
    """
    if hasattr(a, 'toStr'):
      return "%s >= %s" % (self.varId, a.toStr())

    if hasattr(a, 'varName'):
      return "%s >= %s" % (self.varId, a.varName)

    return "%s >= %s" % (self.varId, json.dumps(a))

  def isFrozen(self):
    """
    The Object.isFrozen() determines if an object is frozen.

    Example
    jsObj.objects.get("MyObject").isFrozen()

    Related Pages:

			https://medium.com/@wlodarczyk_j/object-freeze-vs-object-seal-ba6d7553a436
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/isFrozen

    :return: A Python Javascript Boolean
    """
    if self.varName is None:
      raise Exception("Cannot freeze an object without variable name")

    from epyk.core.js.primitives import JsBoolean
    return JsBoolean.JsBoolean("Object.isFrozen(%s)" % self.varName, isPyData=False)

  def freeze(self):
    """
    The Object.freeze() method freezes an object. A frozen object can no longer be changed; freezing an object prevents new properties from being added to it, existing properties from being removed, prevents changing the enumerability, configurability, or writability of existing properties, and prevents the values of existing properties from being changed.

    Example
    jsObj.objects.get("MyObject").freeze()

    Related Pages:

			https://medium.com/@wlodarczyk_j/object-freeze-vs-object-seal-ba6d7553a436
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze

    :return: The object that was passed to the function
    """
    if self.varName is None:
      raise Exception("Cannot freeze an object without variable name")

    self._frozen = True
    return JsObject("Object.freeze(%s)" % self.varName, isPyData=False)

  def isSealed(self):
    """
    The Object.seal() method seals an object, preventing new properties from being added to it and marking all existing properties as non-configurable.
    Values of present properties can still be changed as long as they are writable

    Example
    jsObj.objects.get("MyObject").isSealed()

    Related Pages:

			https://medium.com/@wlodarczyk_j/object-freeze-vs-object-seal-ba6d7553a436
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/seal

    :return: A Javascript Boolean
    """
    from epyk.core.js.primitives import JsBoolean

    self._sealed = True
    return JsBoolean.JsBoolean("Object.isSealed(%s)" % self.varId, isPyData=False)

  def defineProperty(self, obj, prop, descriptor):
    """
    The static method Object.defineProperty() defines a new property directly on an object, or modifies an existing property on an object, and returns the object.

    Related Pages:

			https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty

    :param obj: The object on which to define the property.
    :param prop: The name or Symbol of the property to be defined or modified.
    :param descriptor: The descriptor for the property being defined or modified.

    :return: The object that was passed to the function.
    """
    return JsObject("Object.defineProperty(%s, %s, %s)" % (obj.varId, JsUtils.jsConvertData(prop, None), JsUtils.jsConvertData(descriptor, None)))

  def getOwnPropertyNames(self, obj):
    """
    The Object.getOwnPropertyNames() method returns an array of all properties (including non-enumerable properties except for those which use Symbol) found directly in a given object.

    Related Pages:

			https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getOwnPropertyNames

    :param obj: The object whose enumerable and non-enumerable properties are to be returned.

    :return: An JsArray of strings that corresponds to the properties found directly in the given object.
    """
    from epyk.core.js.primitives import JsArray

    return JsArray.JsArray("Object.getOwnPropertyNames(%s)" % obj.varId)

  def seal(self):
    """
    The Object.seal() method seals an object, preventing new properties from being added to it and marking all existing properties as non-configurable.
    Values of present properties can still be changed as long as they are writable.

    Related Pages:

			https://medium.com/@wlodarczyk_j/object-freeze-vs-object-seal-ba6d7553a436
    https://www.w3schools.com/Js/js_object_es5.asp
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/seal

    :return: The Python Javascript object being sealed.
    """
    if self.varName is None:
      raise Exception("Variable name must be defined")

    return JsObject("Object.seal(%s)" % self.varName)

  def assign(self, target, sources, jsObj=None):
    """
    The Object.assign() method is used to copy the values of all enumerable own properties from one or more source objects to a target object.
    It will return the target object.
    This function might not work with older browser, so to guarantee a good compatibility the jsObj must be defined.

    Related Pages:

			https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign

    :param target: The target object.
    :param sources: The source object(s).
    :param jsObj: Optional, The base Python Javascript object to add the polyfill

    :return:
    """
    if jsObj is not None:
      # Add a polyfill to ensure the browser compatibility
      jsObj._addImport("babel-polyfill")

    if not isinstance(sources, list):
      sources = [sources]
    srcObj = ",".join([JsUtils.jsConvertData(s, None) for s in sources])
    return JsObject("Object.assign(%s, %s)" % (JsUtils.jsConvertData(target, None), srcObj), isPyData=False)

  def create(self, proto=None, propertiesObject=None):
    """
    The Object.create() method creates a new object, using an existing object as the prototype of the newly created object.

    Related Pages:

			https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/create

    :param proto: The object which should be the prototype of the newly-created object.
    :param propertiesObject: Optional. If specified and not undefined, an object whose enumerable own properties (that is, those properties defined upon itself and not enumerable properties along its prototype chain) specify property descriptors to be added to the newly-created object, with the corresponding property names.
                                       These properties correspond to the second argument of Object.defineProperties()

    :return: A Python Javascript object
    """
    if object is None:
      return JsObject("Object.create()")

    return JsObject("Object.create(%s)" % object)

  def entries(self):
    """
    The entries() method returns an Array Iterator object with key/value pairs.

    Related Pages:

			https://www.w3schools.com/jsref/jsref_entries.asp
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/entries

    :return: A new Array, containing the selected elements
    """
    from epyk.core.js.primitives import JsArray

    return JsArray.JsArray("Object.entries(%s)" % self.varId)

  def setattr(self, key, value):
    """

    Example
    jsObj.objects.get("MyObject").setattr("tesr", jsObj.objects.number.get("MyNumber"))

    Related Pages:

			https://www.w3schools.com/js/js_objects.asp
    https://www.w3schools.com/js/js_object_es5.asp

    :param key: The key to add to the object
    :param value: The value corresponding to the key. Can be a Python object or a Javascript reference

    :return: The Python Javascript object
    """
    if self.varName is None:
      raise Exception("Not name defined for this object")

    if getattr(self, '_frozen', False):
      print("Warning, try to change a frozen variable")

    return JsObject("%s[%s] = %s" % (self.varName, JsUtils.jsConvertData(key, None), JsUtils.jsConvertData(value, None)), setVar=False)

  def addItem(self, key, value):
    """
    Wrapper to the setattr method
    """
    return self.setattr(key, value)

  def __getitem__(self, key):
    """
    Return the value for a given key defined in the object

    Example
    jsObj.objects.get("MyObject")["test"]

    Related Pages:

			https://www.w3schools.com/js/js_object_es5.asp

    :param key: The String used as key

    :return: The corresponding Javascript object
    """
    return JsObject("%s[%s]" % (self.varId, JsUtils.jsConvertData(key, None)))

  def keys(self):
    """
    Returns an array of enumerable properties

    Example
    jsObj.objects.get("MyObject").keys()

    Related Pages:

			https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys
    https://www.w3schools.com/js/js_object_es5.asp

    :return: A new Array, containing the selected elements
    """
    from epyk.core.js.primitives import JsArray

    return JsArray.JsArray("Object.keys(%s)" % self.varId, isPyData=False)

  def update(self, dico, jsObj=None):
    """
    This might not be supported by all the browser

    Documentation

    :param dico:
    :param jsObj: Optional, The base Python Javascript object to add the polyfill

    :return:
    """
    if jsObj is not None:
      # Add a polyfill to ensure the browser compatibility
      jsObj._addImport("babel-polyfill")
    return "try{Object.assign({}, %s, %s)} catch(err){console.warn('Assign not supported by the browser')}" % (self.varId, dico)

  def toString(self, explicit=True):
    """
    Converts a Object to a string, and returns the result

    Example
    jsObj.objects.get("MyObject").toString()

    Related Pages:

			https://www.w3schools.com/JS/js_number_methods.asp

    :param explicit: Optional, default True. Parameter to force the String conversion on the Js side

    :return: A Javascript String
    """
    from epyk.core.js.primitives import JsString

    if not explicit:
      return JsString.JsString("%s" % self.varId, isPyData=False)

    return JsString.JsString("%s.toString()" % self.varId, isPyData=False)

  def isArray(self):
    """
    The isArray() method determines whether an object is an array.

    Example
    jsObj.objects.get("MyObject").isArray()

    Related Pages:

			https://www.w3schools.com/jsref/jsref_isarray.asp

    :return: A Javascript Boolean
    """
    from epyk.core.js.primitives import JsBoolean

    return JsBoolean.JsBoolean("Array.isArray(%s)" % self.varId, isPyData=False, setVar=False)

  def toArray(self):
    """
    THis is not a standard Javascript method for an object.
    It is only defined for some objects like the Datatable data()

    :return:
    """
    from epyk.core.js.primitives import JsArray

    return JsArray.JsArray("%s.toArray()" % self.varId, isPyData=False, setVar=False)

  def toStr(self):
    """
    Internal function which return the object reference.
    This will either return the variable name if available and defined or the data itself

    :return: The Javascript String reference
    """
    result = list(self._js)
    self._js = []
    if len(result) > 0:
      return ";".join(JsUtils.jsConvertFncs(result))

    return self.varData if self.varName is None else self.varName

  def toRecord(self, header, varName):
    """

    Example
    d = rptObj.ui.div()
    d.drop([rptObj.js.objects.data.toRecord([1, 2, 3, 4], "result")])

    Attributes:
    ----------
    :param header:
    :param varName:
    """
    from epyk.core.js.primitives import JsArray
    from epyk.core.js.objects import JsData
    from epyk.core.js.fncs.JsFncs import JsFunctions

    fncs = JsFunctions([
      self.toString().split("\\n").setVar("rows"), JsArray.JsArray.set(varName),
      JsArray.JsArray.get("rows").forEach([
        JsArray.JsArray.get(JsData.JsData(self._report).loop().val.toString().split("\t")).toDict(header).setVar("row").r,
        JsArray.JsArray.get(varName).push(JsObject.get("row"))])])
    record = JsObject.get(varName)
    record._js = [fncs.toStr()] + record._js
    return record

  @property
  def r(self):
    """
    Description:
    -----------

    Return the String representation of the Js object.
    This will produce the chain, empty the internal buffer and produce the string
    """
    return self.toStr()

  def clone(self, report=None):
    """
    Description:
    -----------
    Create a shallow-copied clone of the provided plain object.
    Any nested objects or arrays will be copied by reference, not duplicated.

    Related Pages:

			https://underscorejs.org/#clone

    Attributes:
    ----------
    :param report: Optional. The report object
    """
    report = report or self._report
    report.jsImports.add('underscore')
    if self.varName is None:
      return JsObject("_.clone(%s)" % self.varName, isPyData=False)

    return JsObject("(function(){ %s; return _.clone(%s) }()" % (self.toStr(), self.varName), isPyData=False)

  def defaults(self, attrs, report=None):
    """
    Description:
    -----------
    Returns object after filling in its undefined properties with the first value present in the following list of defaults objects.

    Related Pages:

      https://underscorejs.org/#defaults

    Attributes:
    ----------
    :param report: Optional. The report object
    """
    report = report or self._report
    report.jsImports.add('underscore')
    attrs = JsUtils.jsConvertData(attrs, None)
    if self.varName is None:
      return JsObject("_.defaults(%s, %s)" % (self.toStr(), attrs), isPyData=False)

    return JsObject("(function(){ %s; return _.defaults(%s, %s) }()" % (self.toStr(), self.varName, attrs), isPyData=False)

  def pick(self, keys, report=None):
    """
    Description:
    -----------
    Return a copy of the object, filtered to only have values for the whitelisted keys (or array of valid keys).
    Alternatively accepts a predicate indicating which keys to pick.

    Related Pages:

			https://underscorejs.org/#pick

    Attributes:
    ----------
    :param keys:
    """
    report = report or self._report
    report.jsImports.add('underscore')
    keys = JsUtils.jsConvertData(keys, None)
    if self.varName is None:
      return JsObject("_.pick(%s, ..%s)" % (self.varName, keys), isPyData=False)

    return JsObject("(function(){ %s; return _.pick(%s, ..%s) }()" % (self.toStr(), self.varName, keys), isPyData=False)

  def __str__(self):
    """
    The str() method return the variable Javascript reference of the variable.

    According to the variable definition it can be either its name or its value

    :return: A Javascript reference
    """
    return self.varData if self.varName is None else self.varName
