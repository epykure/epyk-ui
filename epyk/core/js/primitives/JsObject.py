#!/usr/bin/python
# -*- coding: utf-8 -*-


from typing import Union, Optional, Any, List
from epyk.core.py import primitives

import json

from epyk.core.js import JsUtils

_JSVARS = 0


class JsKeyword:
  def __init__(self, keyword: str):
    self.__keyword = keyword

  def toStr(self):
    return self.__keyword

  def __str__(self):
    return self.__keyword


class JsObject(primitives.JsDataModel):
  _jsClass = "Object"

  def __init__(self, data, js_code: Optional[str] = None, set_var: bool = False, is_py_data: bool = False,
               page: primitives.PageModel = None, component: primitives.HtmlModel = None):
    """
    Description:
    ------------

    Related Pages:

      https//www.w3schools.com/js/js_type_conversion.asp

    Attributes:
    ----------
    :param Optional[str] js_code:
    :param data:
    :param bool set_var:
    :param bool is_py_data:
    :param page: The internal report object.
    :param component:
    """
    global _JSVARS

    self.varName, self.varData, self._js, self.component = js_code, str(data), [], component
    self.page = page
    if page is None and component is not None:
      self.page = component.page
    self._frozen, self._sealed = False, False
    if js_code is None and set_var:
      _JSVARS += 1
      self.varName = "%s_%s" % (self.__class__.__name__, _JSVARS)
    if set_var:
      self.setVar(self.varName)

  @classmethod
  def new(cls, data: Optional[Any] = None, js_code: Optional[str] = None, is_py_data: bool = True,
          page: primitives.PageModel = None):
    """
    Description:
    ------------
    Create a Python Javascript Object.

    Usage::

      JsDate.new("2019-05-03", varName="MyDate")

    Related Pages:

      https://www.w3schools.com/jsref/jsref_obj_date.asp

    Attributes:
    ----------
    :param data: Optional, The object data.
    :param Optional[str] js_code: Optional, The object variable name.
    :param bool is_py_data: Optional, To specify if it is a Python reference and if it should be converted to Json.
    :param primitives.PageModel page: The internal report object.

    :return: The Python Javascript Date primitive
    """
    if is_py_data:
      return cls(
        data=JsUtils.jsConvertData(data, None), js_code=js_code, set_var=True, is_py_data=is_py_data, page=page)

    return cls(data=data, js_code=js_code, set_var=True, is_py_data=is_py_data, page=page)

  @classmethod
  def this(cls, page: primitives.PageModel = None):
    """
    Description:
    ------------
    Get the object this.

    Usage::

      jsObj.object.this

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this

    Attributes:
    ----------
    :param Optional[primitives.PageModel] page: The internal report object.

    :return: The python Javascript object
    """
    return cls.get("this", page=page)

  @classmethod
  def get(cls, js_code: str, page: Optional[primitives.PageModel] = None, component: primitives.HtmlModel = None):
    """
    Description:
    ------------
    Get the Javascript Object by its reference.

    Usage::

      JsDate.new("2019-05-03", varName="MyDate")
      JsDate.get("MyDate")

    Related Pages:

      https://www.w3schools.com/jsref/jsref_obj_date.asp

    Attributes:
    ----------
    :param str js_code: The Javascript object reference.
    :param Optional[primitives.PageModel] page: The internal report object.

    :return: The python Javascript object
    """
    return cls(data=None, js_code=js_code, set_var=False, page=page, component=component)

  @property
  def varId(self):
    """
    Description:
    ------------
    The Javascript and Python reference ID.

    :return: The Javascript String of the object variable name
    """
    return self.varData if self.varName is None else self.varName

  def setVar(self, js_code: str, var_type: str = "var"):
    """
    Description:
    ------------
    The setVar() method will define the variable name and use this reference in the future.

    Usage::

    Attributes:
    ----------
    :param str js_code: The variable name.
    :param str var_type: The type of variable to be set on the Javascript side.

    :return: The Python Javascript Object
    """
    if js_code is None:
      return self

    if (self.varName is not None and (self.varName.startswith("window.") or self.varName.startswith("window["))) or (js_code is not None and (js_code.startswith("window.") or js_code.startswith("window["))):
      var_type = ""
    if js_code != self.varName:
      if len(self._js) == 1:
        if self._js[0].startswith("var "):
          # Remove the entry used to define by default the javascript object
          self._js = ["%s %s = %s" % (var_type, js_code, self.varData)]
        else:
          self._js.append("%s %s = %s" % (var_type, js_code, self.varName))
      else:
        self._js.append("%s %s = %s" % (var_type, js_code, self.varName or self.varData))
    else:
      self._js.append("%s %s = %s" % (var_type, js_code, self.varData))
    return self

  def prototype(self, name: str, value: Any):
    """
    Description:
    ------------
    The prototype property allows you to add new properties and methods to existing object types.

    Related Pages:

      https://www.w3schools.com/jsref/jsref_prototype_string.asp

    Attributes:
    ----------
    :param str name: The object property name.
    :param value: The object property values.

    :return: A reference to the String.prototype object
    """
    return "%s.prototype.%s = %s" % (self.varName, name, value)

  def add(self, n: Union[primitives.JsDataModel, float, str]):
    """
    Description:
    ------------
    Add value to a Javascript Number.
    The value will be added. It will return a new number object on the Javascript side.

    Usage::

      jsNumber.add(34.5)

    Attributes:
    ----------
    :param Union[primitives.JsDataModel, float] float n: The number value.

    :return: A new Python Javascript Number
    """
    data = JsUtils.jsConvertData(n, None)
    return JsObject("%s + %s" % (self.varId, data), is_py_data=False)

  def __add__(self, value: primitives.JsDataModel):
    return JsObject("%s += %s" % (self.varId, value), is_py_data=False)

  def __sub__(self, value: primitives.JsDataModel):
    return JsObject("%s -= %s" % (self.varId, value), is_py_data=False)

  def __mul__(self, value: primitives.JsDataModel):
    return JsObject("%s *= %s" % (self.varId, value), is_py_data=False)

  def __truediv__(self, value: primitives.JsDataModel):
    return JsObject("%s /= %s" % (self.varId, value), is_py_data=False)

  def __mod__(self, value: primitives.JsDataModel):
    return JsObject("%s %%= %s" % (self.varId, value), is_py_data=False)

  def __pow__(self, value: Union[primitives.JsDataModel, int]):
    from epyk.core.js import JsMaths

    return JsObject("%s = %s" % (self.varId, JsMaths.JsMaths.pow(self, value)))

  def __eq__(self, a: Any):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param a:
    """
    if hasattr(a, 'toStr'):
      return "%s == %s" % (self.varId, a.toStr())

    if hasattr(a, 'varName'):
      return "%s == %s" % (self.varId, a.varName)

    return "%s == %s" % (self.varId, json.dumps(a))

  def __lt__(self, a: Any):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param a:
    """
    if hasattr(a, 'toStr'):
      return "%s < %s" % (self.varId, a.toStr())

    if hasattr(a, 'varName'):
      return "%s < %s" % (self.varId, a.varName)

    return "%s < %s" % (self.varId, json.dumps(a))

  def __le__(self, a: Any):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param a:
    """
    if hasattr(a, 'toStr'):
      return "%s <= %s" % (self.varId, a.toStr())

    if hasattr(a, 'varName'):
      return "%s <= %s" % (self.varId, a.varName)

    return "%s <= %s" % (self.varId, json.dumps(a))

  def __ne__(self, a: Union[primitives.JsDataModel, str]):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param a:
    """
    if hasattr(a, 'toStr'):
      return "%s != %s" % (self.varId, a.toStr())

    if hasattr(a, 'varName'):
      return "%s != %s" % (self.varId, a.varName)

    return "%s != %s" % (self.varId, json.dumps(a))

  def __gt__(self, a: Union[primitives.JsDataModel, str]):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param a:
    """
    if hasattr(a, 'toStr'):
      return "%s > %s" % (self.varId, a.toStr())

    if hasattr(a, 'varName'):
      return "%s > %s" % (self.varId, a.varName)

    return "%s > %s" % (self.varId, json.dumps(a))

  def __ge__(self, a: Union[primitives.JsDataModel, str]):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param a:
    """
    if hasattr(a, 'toStr'):
      return "%s >= %s" % (self.varId, a.toStr())

    if hasattr(a, 'varName'):
      return "%s >= %s" % (self.varId, a.varName)

    return "%s >= %s" % (self.varId, json.dumps(a))

  def isFrozen(self):
    """
    Description:
    ------------
    The Object.isFrozen() determines if an object is frozen.

    Usage::

      jsObj.objects.get("MyObject").isFrozen()

    Related Pages:

      https://medium.com/@wlodarczyk_j/object-freeze-vs-object-seal-ba6d7553a436
      https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/isFrozen

    :return: A Python Javascript Boolean
    """
    if self.varName is None:
      raise ValueError("Cannot freeze an object without variable name")

    from epyk.core.js.primitives import JsBoolean
    return JsBoolean.JsBoolean("Object.isFrozen(%s)" % self.varName, is_py_data=False)

  def freeze(self):
    """
    Description:
    ------------
    The Object.freeze() method freezes an object.
    A frozen object can no longer be changed; freezing an object prevents new properties from being added to it,
    existing properties from being removed, prevents changing the enumerability, configurability,
    or writability of existing properties, and prevents the values of existing properties from being changed.

    Usage::

      jsObj.objects.get("MyObject").freeze()

    Related Pages:

      https://medium.com/@wlodarczyk_j/object-freeze-vs-object-seal-ba6d7553a436
      https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze

    :return: The object that was passed to the function
    """
    if self.varName is None:
      raise ValueError("Cannot freeze an object without variable name")

    self._frozen = True
    return JsObject("Object.freeze(%s)" % self.varName, is_py_data=False)

  def isSealed(self):
    """
    Description:
    ------------
    The Object.seal() method seals an object, preventing new properties from being added to it and marking all
    existing properties as non-configurable.
    Values of present properties can still be changed as long as they are writable

    Usage::

      jsObj.objects.get("MyObject").isSealed()

    Related Pages:

      https://medium.com/@wlodarczyk_j/object-freeze-vs-object-seal-ba6d7553a436
      https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/seal

    :return: A Javascript Boolean
    """
    from epyk.core.js.primitives import JsBoolean

    self._sealed = True
    return JsBoolean.JsBoolean("Object.isSealed(%s)" % self.varId, is_py_data=False)

  def defineProperty(self, obj, prop: str, descriptor: str):
    """
    Description:
    ------------
    The static method Object.defineProperty() defines a new property directly on an object, or modifies an existing
    property on an object, and returns the object.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty

    Attributes:
    ----------
    :param obj: The object on which to define the property.
    :param str prop: The name or Symbol of the property to be defined or modified.
    :param str descriptor: The descriptor for the property being defined or modified.

    :return: The object that was passed to the function.
    """
    return JsObject(
      "Object.defineProperty(%s, %s, %s)" % (
        obj.varId, JsUtils.jsConvertData(prop, None), JsUtils.jsConvertData(descriptor, None)))

  def getOwnPropertyNames(self, obj):
    """
    Description:
    ------------
    The Object.getOwnPropertyNames() method returns an array of all properties (including non-enumerable properties
    except for those which use Symbol) found directly in a given object.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getOwnPropertyNames

    Attributes:
    ----------
    :param obj: The object whose enumerable and non-enumerable properties are to be returned.

    :return: An JsArray of strings that corresponds to the properties found directly in the given object.
    """
    from epyk.core.js.primitives import JsArray

    return JsArray.JsArray("Object.getOwnPropertyNames(%s)" % obj.varId)

  def seal(self):
    """
    Description:
    ------------
    The Object.seal() method seals an object, preventing new properties from being added to it and marking all existing
    properties as non-configurable.
    Values of present properties can still be changed as long as they are writable.

    Related Pages:

      https://medium.com/@wlodarczyk_j/object-freeze-vs-object-seal-ba6d7553a436
      https://www.w3schools.com/Js/js_object_es5.asp
      https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/seal

    :return: The Python Javascript object being sealed.
    """
    if self.varName is None:
      raise ValueError("Variable name must be defined")

    return JsObject("Object.seal(%s)" % self.varName)

  def assign(self, target: Union[primitives.JsDataModel, str], sources: List[Union[primitives.JsDataModel, str]],
             js_obj=None):
    """
    Description:
    ------------
    The Object.assign() method is used to copy the values of all enumerable own properties from one or more source
    objects to a target object.
    It will return the target object.
    This function might not work with older browser, so to guarantee a good compatibility the jsObj must be defined.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign

    Attributes:
    ----------
    :param Union[primitives.JsDataModel, str] target: The target object.
    :param List[Union[primitives.JsDataModel, str]] sources: The source object(s).
    :param js_obj: Optional, The base Python Javascript object to add the polyfill
    """
    if js_obj is not None:
      # Add a polyfill to ensure the browser compatibility
      js_obj._addImport("babel-polyfill")

    if not isinstance(sources, list):
      sources = [sources]
    js_obj = ",".join([JsUtils.jsConvertData(s, None) for s in sources])
    return JsObject("Object.assign(%s, %s)" % (JsUtils.jsConvertData(target, None), js_obj), is_py_data=False)

  def create(self, proto=None, propertiesObject=None):
    """
    Description:
    ------------
    The Object.create() method creates a new object, using an existing object as the prototype of the newly
    created object.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/create

    Attributes:
    ----------
    :param proto: The object which should be the prototype of the newly-created object.
    :param propertiesObject: Optional. If specified and not undefined, an object whose enumerable own properties
    (that is, those properties defined upon itself and not enumerable properties along its prototype chain) specify
    property descriptors to be added to the newly-created object, with the corresponding property names.
    These properties correspond to the second argument of Object.defineProperties()

    :return: A Python Javascript object
    """
    if object is None:
      return JsObject("Object.create()")

    return JsObject("Object.create(%s)" % object)

  def entries(self):
    """
    Description:
    ------------
    The entries() method returns an Array Iterator object with key/value pairs.

    Related Pages:

      https://www.w3schools.com/jsref/jsref_entries.asp
      https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/entries

    :return: A new Array, containing the selected elements
    """
    from epyk.core.js.primitives import JsArray

    return JsArray.JsArray("Object.entries(%s)" % self.varId)

  def setattr(self, key: Union[primitives.JsDataModel, str], value: Union[primitives.JsDataModel, str]):
    """
    Description:
    ------------

    Usage::

      jsObj.objects.get("MyObject").setattr("tesr", jsObj.objects.number.get("MyNumber"))

    Related Pages:

      https://www.w3schools.com/js/js_objects.asp
      https://www.w3schools.com/js/js_object_es5.asp

    Attributes:
    ----------
    :param Union[primitives.JsDataModel, str] key: The key to add to the object.
    :param Union[primitives.JsDataModel, str] value: The value corresponding to the key. Can be a Python object or a
    Javascript reference

    :return: The Python Javascript object
    """
    if self.varName is None:
      raise ValueError("Not name defined for this object")

    if getattr(self, '_frozen', False):
      print("Warning, try to change a frozen variable")

    return JsObject("%s[%s] = %s" % (
      self.varName, JsUtils.jsConvertData(key, None), JsUtils.jsConvertData(value, None)), set_var=False)

  def addItem(self, key: Union[primitives.JsDataModel, str], value: Union[primitives.JsDataModel, str]):
    """
    Description:
    ------------
    Wrapper to the setattr method.
    """
    return self.setattr(key, value)

  def addComponent(self, component: primitives.HtmlModel):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param primitives.HtmlModel component:
    """
    return self.setattr(component.htmlCode, component.dom.content)

  def __getitem__(self, key: Union[primitives.JsDataModel, str]):
    """
    Description:
    ------------
    Return the value for a given key defined in the object.

    Usage::

      jsObj.objects.get("MyObject")["test"]

    Related Pages:

      https://www.w3schools.com/js/js_object_es5.asp

    Attributes:
    ----------
    :param Union[primitives.JsDataModel, str] key: The String used as key.

    :return: The corresponding Javascript object
    """
    return JsObject("%s[%s]" % (self.varId, JsUtils.jsConvertData(key, None)))

  def keys(self):
    """
    Description:
    ------------
    Returns an array of enumerable properties.

    Usage::

      jsObj.objects.get("MyObject").keys()

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys
      https://www.w3schools.com/js/js_object_es5.asp

    :return: A new Array, containing the selected elements
    """
    from epyk.core.js.primitives import JsArray

    return JsArray.JsArray("Object.keys(%s)" % self.varId, is_py_data=False)

  def update(self, dico, js_obj=None):
    """
    Description:
    ------------
    This might not be supported by all the browser.

    Usage::

    Attributes:
    ----------
    :param dico:
    :param js_obj: Optional, The base Python Javascript object to add the polyfill
    """
    if js_obj is not None:
      # Add a polyfill to ensure the browser compatibility
      js_obj._addImport("babel-polyfill")
    return "try{Object.assign({}, %s, %s)} catch(err){console.warn('Assign not supported by the browser')}" % (
      self.varId, dico)

  def toString(self, explicit: bool = True):
    """
    Description:
    ------------
    Converts an Object to a string, and returns the result

    Usage::

      jsObj.objects.get("MyObject").toString()

    Related Pages:

      https://www.w3schools.com/JS/js_number_methods.asp

    Attributes:
    ----------
    :param bool explicit: Optional, default True. Parameter to force the String conversion on the Js side

    :return: A Javascript String
    """
    from epyk.core.js.primitives import JsString

    if not explicit:
      return JsString.JsString("%s" % self.varId, is_py_data=False)

    return JsString.JsString("%s.toString()" % self.varId, is_py_data=False)

  def toNumber(self):
    """
    Description:
    ------------
    """
    from epyk.core.js.primitives import JsNumber

    return JsNumber.JsNumber("parseFloat(%s)" % self.varId, is_py_data=False, set_var=False)

  def isArray(self):
    """
    Description:
    ------------
    The isArray() method determines whether an object is an array.

    Usage::

      jsObj.objects.get("MyObject").isArray()

    Related Pages:

      https://www.w3schools.com/jsref/jsref_isarray.asp

    :return: A Javascript Boolean
    """
    from epyk.core.js.primitives import JsBoolean

    return JsBoolean.JsBoolean("Array.isArray(%s)" % self.varId, is_py_data=False, set_var=False)

  def toArray(self):
    """
    Description:
    ------------
    THis is not a standard Javascript method for an object.
    It is only defined for some objects like the Datatable data()
    """
    from epyk.core.js.primitives import JsArray

    return JsArray.JsArray("%s.toArray()" % self.varId, is_py_data=False, set_var=False)

  def toStr(self):
    """
    Description:
    ------------
    Internal function which return the object reference.
    This will either return the variable name if available and defined or the data itself

    :return: The Javascript String reference
    """
    result = list(self._js)
    self._js = []
    if len(result) > 0:
      return JsUtils.jsConvertFncs(result, toStr=True)

    return self.varData if self.varName is None else self.varName

  def fromArrayToRecord(self, header: list = None):
    """
    Description:
    ------------

    row["Date"] = row["Date"].toISOString().slice(0, 10);

    Attributes:
    ----------
    :param header:
    """
    from epyk.core.js.primitives import JsArray

    if header is None:
      return JsArray.JsArray.get('''(function(data){var results = []; var header = data[0]; 
        data.slice(1).forEach(function(rec){var row = []; rec.forEach(function(r, i){row[header[i]] = r}); 
        results.push(row)}); return results})(%s)''' % self.varName)

  def toRecord(self, header: list, js_code: str):
    """
    Description:
    ------------

    Usage::

      d = rptObj.ui.div()
      d.drop([rptObj.js.objects.data.toRecord([1, 2, 3, 4], "result")])

    Attributes:
    ----------
    :param list header:
    :param str js_code:
    """
    from epyk.core.js.primitives import JsArray
    from epyk.core.js.objects import JsData
    from epyk.core.js.fncs.JsFncs import JsFunctions

    funcs = JsFunctions([
      self.toString().split("\\n").setVar("rows"), JsArray.JsArray.set(js_code),
      JsArray.JsArray.get("rows").forEach([
        JsArray.JsArray.get(
          JsData.JsData(self.page).loop().val.toString().split("\t")).toDict(header).setVar("row").r,
        JsArray.JsArray.get(js_code).push(JsObject.get("row"))])])
    record = JsObject.get(js_code)
    record._js = [funcs.toStr()] + record._js
    return record

  @property
  def r(self):
    """
    Description:
    -----------
    Return the String representation of the Js object.
    This will produce the chain, empty the internal buffer and produce the string.
    """
    return self.toStr()

  def clone(self, page: Optional[primitives.PageModel] = None):
    """
    Description:
    -----------
    Create a shallow-copied clone of the provided plain object.
    Any nested objects or arrays will be copied by reference, not duplicated.

    Related Pages:

      https://underscorejs.org/#clone

    Attributes:
    ----------
    :param Optional[primitives.PageModel] page: Optional. The report object
    """
    page = page or self.page
    page.jsImports.add('underscore')
    if self.varName is None:
      return JsObject("_.clone(%s)" % self.varName, is_py_data=False)

    return JsObject("(function(){ %s; return _.clone(%s) })()" % (self.toStr(), self.varName), is_py_data=False)

  def defaults(self, attrs: Union[primitives.JsDataModel, dict], page: Optional[primitives.PageModel] = None):
    """
    Description:
    -----------
    Returns object after filling in its undefined properties with the first value present in the following list
    of defaults objects.

    Related Pages:

      https://underscorejs.org/#defaults

    Attributes:
    ----------
    :param Union[primitives.JsDataModel, dict] attrs:
    :param Optional[primitives.PageModel] page: Optional. The report object.
    """
    page = page or self.page
    page.jsImports.add('underscore')
    attrs = JsUtils.jsConvertData(attrs, None)
    if self.varName is None:
      return JsObject("_.defaults(%s, %s)" % (self.toStr(), attrs), is_py_data=False)

    return JsObject(
      "(function(){ %s; return _.defaults(%s, %s) }()" % (self.toStr(), self.varName, attrs), is_py_data=False)

  def pick(self, keys: Union[primitives.JsDataModel, list], page: Optional[primitives.PageModel] = None):
    """
    Description:
    -----------
    Return a copy of the object, filtered to only have values for the whitelisted keys (or array of valid keys).
    Alternatively accepts a predicate indicating which keys to pick.

    Related Pages:

      https://underscorejs.org/#pick

    Attributes:
    ----------
    :param Union[primitives.JsDataModel, list] keys:
    :param Optional[primitives.PageModel] page: Optional. The report object.
    """
    page = page or self.page
    page.jsImports.add('underscore')
    keys = JsUtils.jsConvertData(keys, None)
    if self.varName is None:
      return JsObject("_.pick(%s, ..%s)" % (self.varName, keys), is_py_data=False)

    return JsObject(
      "(function(){ %s; return _.pick(%s, ..%s) }()" % (self.toStr(), self.varName, keys), is_py_data=False)

  def jsonParse(self):
    """
    Description:
    -----------
    A common use of JSON is to exchange data to/from a web server.

    When receiving data from a web server, the data is always a string.

    Parse the data with JSON.parse(), and the data becomes a JavaScript object.

    Related Pages:

      https://www.w3schools.com/js/js_json_parse.asp
    """
    return JsObject("JSON.parse(%s)" % self.varName)

  def stringify(self):
    """
    Description:
    -----------
    The JSON.stringify() method converts a JavaScript object or value to a JSON string, optionally replacing values
    if a replacer function is specified or optionally including only the specified properties if a replacer array
    is specified.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify
    """
    return JsObject("JSON.stringify(%s)" % self.varName)

  def fileParse(self, delimiter: Union[primitives.JsDataModel, str]):
    """
    Description:
    -----------
    Parse a file based on the delimiter and return an Array of Arrays on the Javascript side.

    Attributes:
    ----------
    :param Union[primitives.JsDataModel, str] delimiter: The line delimiter in the file.
    """
    delimiter = JsUtils.jsConvertData(delimiter, None)
    return JsObject('''(function(){var results = []; 
      %s.split('\\n').forEach(function(rec){ results.push(String(rec).replace(/^\s+|\s+$/g, '').split(%s)); }); 
      return results})()''' % (self.varName, delimiter))

  def fileToDict(self, delimiter: Union[primitives.JsDataModel, str],
                 columns: Optional[Union[primitives.JsDataModel, list]] = None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param Union[primitives.JsDataModel, str] delimiter: The line delimiter in the file.
    :param Optional[Union[primitives.JsDataModel, list]] columns: The list of columns.
    """
    delimiter = JsUtils.jsConvertData(delimiter, None)
    columns = JsUtils.jsConvertData(columns, None)
    return JsObject('''(function(){var results = []; 
          var delimiter = %(delimiter)s; if (delimiter == 'TAB'){delimiter = '\\t'};
          var rows = %(varName)s.split('\\n'); var results = []; 
          var header = String(rows[0]).replace(/^\s+|\s+$/g, '').split(delimiter);
          for(var i = 1; i < rows.length; i++){
            var row = {}; var line = String(rows[i]).replace(/^\s+|\s+$/g, '');
            if(line != ""){
              line.split(delimiter).forEach(function(rec, j){row[header[j]] = rec}); results.push(row)}
          }; return results})()''' % {"varName": self.varName, "delimiter": delimiter})

  def format(self, *args, **kwargs):
    """ Format the underlying string object """
    if self.varData == 'None':
      self.varName = self.varName.format(*(JsUtils.jsConvertData(a, None) for a in args),
                                         **{k: JsUtils.jsConvertData(v, None) for k, v in kwargs.items()})
    else:
      self.varData = self.varData.format(*(JsUtils.jsConvertData(a, None) for a in args),
                                         **{k: JsUtils.jsConvertData(v, None) for k, v in kwargs.items()})
    return self

  def __str__(self):
    """
    Description:
    -----------
    The str() method return the variable Javascript reference of the variable.

    According to the variable definition it can be either its name or its value

    :return: A Javascript reference
    """
    return self.varData if self.varName is None else self.varName
