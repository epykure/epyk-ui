#!/usr/bin/python
# -*- coding: utf-8 -*-

import json


class DataConfig:

  def __init__(self):
    self.keys = {}
    self.docs = {}

  def __getitem__(self, key):
    from epyk.core.js.primitives import JsObjects

    self.keys[key] = ""
    return JsObjects.JsObjects.get("window['page_config']['%s']" % key)

  def get(self, key, dfl="", doc=""):
    """
    Description:
    ------------
    Get the key from the configuration on the JavaScript side and add the documentation.

    Attributes:
    ----------
    :param key: String. The key to look up from the JavaScript configuration.
    :param dfl: Object. Optional. The default value in the configuration.
    :param doc: String. Optional. The doc for this key in the Json.
    """
    from epyk.core.js.primitives import JsObjects

    self.keys[key] = dfl
    self.docs[key] = doc
    return JsObjects.JsObjects.get("window['page_config']['%s']" % key)

  def fromConfig(self, k, default=None, page=None, end_point="/static/configs"):
    """
    Description:
    ------------
    Get the configuration for loading the report from json files.
    This will allow the creation of templates on the Python side and configuration in a static manner in json.

    By using this way of working it is easier to split the page and the configuration and non developers can
    change the content or create new ones based on the templates.

    Attributes:
    ----------
    :param k: String. The alias of the cache, variable.
    :param default: String. Object. Optional. The default value of the cache.
    :param page: Report. Optional. The page object.
    :param end_point: String. Optional. THe static end point for the configurations.
    """
    if page.json_config_file is None:
      raise Exception("json_config_file must be attached to the page to load the corresponding configuration")

    self.keys[k] = default
    return '''
      (function(){
        if (typeof window['page_config'] === 'undefined'){
          var rawFile = new XMLHttpRequest();
          const queryString = window.location.search;
          const urlParams = new URLSearchParams(queryString);
          var lang = urlParams.get('lang') || 'eng';
          rawFile.overrideMimeType("application/json");
          rawFile.open("GET", "%(static)s/"+ lang +"/%(script)s.json", false);
          rawFile.onreadystatechange = function() {
              if (rawFile.readyState === 4 && rawFile.status == "200") {
                 var data = JSON.parse(rawFile.responseText); window['page_config'] = data}}
          rawFile.send(null);
          var results = window['page_config']['%(key)s'];
          if(typeof window['page_config']['%(key)s'] === 'undefined'){return %(dflt)s}
          else {return results}
        } else {return window['page_config']['%(key)s']}
      })(%(key)s)
      ''' % {"static": end_point, "script": page.json_config_file, "key": k, "dflt": default}

  def to_json(self, sort_keys=True, indent=4):
    """
    Description:
    ------------
    Return the json configuration inputs for the page.

    Attributes:
    ----------
    :param sort_keys: Boolean. Optional. Set the order for the keys.
    :param indent: Integer. Optional. Add number of indent to the Json.
    """
    vals = {}
    if sort_keys:
      for k in sorted(self.keys):
        vals[k] = self.keys[k]
    else:
      vals = self.keys
    if self.docs:
      vals["_comment"] = self.docs
    return json.dumps(vals, indent=indent)


class TabulatorEvents:

  @property
  def row(self):
    """
    Description:
    ------------
    Get a Tabulator Row object.
    """
    from epyk.core.js.packages import JsTabulator

    return JsTabulator.RowComponent(setVar=False, varName=None)

  @property
  def cell(self):
    """
    Description:
    ------------
    Get a Tabulator cell object.
    """
    from epyk.core.js.packages import JsTabulator

    return JsTabulator.CellComponent(setVar=False, varName=None)

  @property
  def column(self):
    """
    Description:
    ------------
    Get a Tabulator column object.
    """
    from epyk.core.js.packages import JsTabulator

    return JsTabulator.ColumnComponent(setVar=False, varName=None)


class DataEvents:

  @property
  def tabulator(self):
    """
    Description:
    ------------
    Interface to the Tabulator events.
    """
    return TabulatorEvents()

  @property
  def files(self):
    """
    Description:
    ------------

    """
    from epyk.core.js.primitives import JsObjects
    return JsObjects.JsArray.JsArray.get("Array.from(event.dataTransfer.files)")

  @property
  def file(self):
    """
    Description:
    ------------

    """
    return DataFile("value")

  @property
  def data(self):
    """
    Description:
    ------------
    Interface to a standard data object available in any Event.
    This is the default variable name in all the JavaScript embedded methods.
    """
    from epyk.core.js.primitives import JsObjects
    return JsObjects.JsObjects.get("data")

  @property
  def target(self):
    """
    Description:
    ------------
    Interface to a standard data object available in any Event.
    This is the default variable name in all the JavaScript embedded methods.
    """
    from epyk.core.js.objects import JsNodeDom
    return JsNodeDom.JsDoms.get("event.target")

  @property
  def value(self):
    """
    Description:
    ------------
    Interface to a standard value object available in any Event.
    This is the default variable name in all the JavaScript embedded methods.
    """
    from epyk.core.js.primitives import JsObjects
    return JsObjects.JsObjects.get("value")

  @property
  def response(self):
    """
    Description:
    ------------
    Get the response from a promise event in the then statement.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise
    """
    from epyk.core.js.primitives import JsObjects
    return JsObjects.JsObjects.get("response")

  @property
  def event(self):
    """
    Description:
    ------------
    Interface to the standard event.
    """
    from epyk.core.js.objects import JsEvents

    return JsEvents.Event()

  @property
  def mouse(self):
    """
    Description:
    ------------
    Interface to the standard mouse event.
    """
    from epyk.core.js.objects import JsEvents

    return JsEvents.MouseEvent()

  @property
  def ui(self):
    """
    Description:
    ------------
    Interface to the UI generic event.
    """
    from epyk.core.js.objects import JsEvents

    return JsEvents.UIEvent()

  @property
  def touch(self):
    """
    Description:
    ------------
    Interface to a standard touch event.
    This object is available in any event specific to touch screens.
    """
    from epyk.core.js.objects import JsEvents

    return JsEvents.TouchEvent()

  @property
  def key(self):
    """
    Description:
    ------------
    Interface to a standard keyboard event.
    This object is available in any keyup, keydown... events
    """
    from epyk.core.js.objects import JsEvents

    return JsEvents.KeyboardEvent()

  @property
  def d3(self):
    """
    Description:
    ------------
    Get a D3 component. Wrap the d3.select(this) statement.

    Related Pages:

      https://www.tutorialspoint.com/d3js/d3js_selections.htm
    """
    from epyk.core.js.packages import JsD3

    return JsD3.D3Select(selector="d3.select(this)", setVar=False)

  @property
  def leaflet(self):
    from epyk.core.js.packages import JsLeaflet

    return JsLeaflet.LEvent(selector="d3.select(this)", setVar=False)

  @property
  def geolocationPosition(self):
    return GeolocationCoordinates("navPos")


class DataFile:

  def __init__(self, varName="value"):
    self.varName = varName

  @property
  def name(self):
    """
    Description:
    ------------
    Get the filename.
    """
    from epyk.core.js.primitives import JsObjects
    return JsObjects.JsString.JsString.get("%s.name" % self.varName)

  @property
  def size(self):
    """
    Description:
    ------------
    Get the file size.
    """
    from epyk.core.js.primitives import JsObjects
    return JsObjects.JsString.JsString.get("%s.size" % self.varName)

  @property
  def lastModifiedDate(self):
    """
    Description:
    ------------
    Get the last modified date for the file.
    """
    from epyk.core.js.primitives import JsObjects
    return JsObjects.JsDate.JsDate("%s.lastModifiedDate" % self.varName)

  @property
  def lastModified(self):
    """
    Description:
    ------------
    Get the last modified date for the file.
    """
    from epyk.core.js.primitives import JsObjects
    return JsObjects.JsDate.JsDate("%s.lastModified" % self.varName)

  @property
  def toISOString(self):
    """
    Description:
    ------------

    """
    from epyk.core.js.primitives import JsObjects
    return JsObjects.JsString.JsString.get(
      "(function(){var dt = new Date(%s.lastModified); return dt.toISOString() }())" % self.varName)

  @property
  def description(self):
    """
    Description:
    ------------
    Get file description (name, size and date).
    """
    from epyk.core.js.primitives import JsObjects
    return JsObjects.JsString.JsString.get("%(varName)s.name +', '+ (%(varName)s.size / 1024) +'Ko, '+ %(dt)s" % {
      'varName': self.varName, 'dt': self.toISOString})


class DataLoops:

  @property
  def value(self):
    """
    Description:
    -----------
    The value returned by forEach statement.

    Note. For nested loop make sure you store the important information in new variable names.
    """
    from epyk.core.js.primitives import JsObjects
    return JsObjects.JsObject.JsObject.get("value")

  @property
  def dom(self):
    """
    Description:
    -----------

    """
    from epyk.core.js.objects import JsNodeDom
    return JsNodeDom.JsDoms.new(varName="value", setVar=False)

  @property
  def dom_list(self):
    """
    Description:
    -----------

    """
    from epyk.core.js.objects import JsNodeDom
    return JsNodeDom.JsDoms.new(varName="elt", setVar=False)

  @property
  def i(self):
    """
    Description:
    ------------
    The index value return in loop statement.
    """
    from epyk.core.js.primitives import JsObjects
    return JsObjects.JsNumber.JsNumber.get("index")

  @property
  def file(self):
    return DataFile()


class DataPrimitives:

  def list(self, data=None, name=None):
    """
    Description:
    -----------


    Attributes:
    ----------
    :param data: List. Optional. The Python object used to feed the list.
    :param name: String. Optional. The variable name used on the JavaScript.
    """
    from epyk.core.js.primitives import JsObjects

    if data is not None:
      return JsObjects.JsArray.JsArray(data, varName=name, setVar=True if name is not None else False)

    return JsObjects.JsArray.JsArray.get(name)

  def dict(self, data=None, name=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param data: List. Optional. The Python object used to feed the list.
    :param name: String. Optional. The variable name used on the JavaScript.
    """
    from epyk.core.js.primitives import JsObjects

    if data is not None:
      return JsObjects.JsObject.JsObject(data, varName=name, setVar=True if name is not None else False)

    return JsObjects.JsObject.JsObject.get(name)

  def str(self, data=None, name=None):
    """
    Description:
    -----------


    Attributes:
    ----------
    :param data: List. Optional. The Python object used to feed the list.
    :param name: String. Optional. The variable name used on the JavaScript.
    """
    from epyk.core.js.primitives import JsObjects

    if data is not None:
      return JsObjects.JsString.JsString(data, varName=name, setVar=True if name is not None else False)

    return JsObjects.JsString.JsString.get(name)

  def float(self, data=None, name=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param data: List. Optional. The Python object used to feed the list.
    :param name: String. Optional. The variable name used on the JavaScript.
    """
    from epyk.core.js.primitives import JsObjects

    if data is not None:
      return JsObjects.JsNumber.JsNumber(data, varName=name, setVar=True if name is not None else False)

    return JsObjects.JsNumber.JsNumber.get(name)

  def int(self, data=None, name=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param data: List. Optional. The Python object used to feed the list.
    :param name: String. Optional. The variable name used on the JavaScript.
    """
    from epyk.core.js.primitives import JsObjects

    if data is not None:
      return JsObjects.JsNumber.JsNumber(data, varName=name, setVar=True if name is not None else False)

    return JsObjects.JsNumber.JsNumber.get(name)

  def date(self, data=None, name=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param data: List. Optional. The Python object used to feed the list.
    :param name: String. Optional. The variable name used on the JavaScript.
    """
    from epyk.core.js.primitives import JsObjects

    if data is not None:
      return JsObjects.JsDate.JsDate(data, varName=name, setVar=True if name is not None else False)

    if data is None and name is None:
      return JsObjects.JsDate.JsDate(data, varName=name, setVar=False)

    return JsObjects.JsDate.JsDate.get(name)


class GeolocationCoordinates:

  def __init__(self, varName):
    self.varName = varName

  @property
  def coords(self):
    """
    Description:
    ------------
    Returns a GeolocationCoordinates object defining the current location.

    This feature is available only in secure contexts (HTTPS), in some or all supporting browsers.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/GeolocationPosition
    """
    from epyk.core.js.primitives import JsObject

    return JsObject.JsObject.get(self.varName)

  @property
  def accuracy(self):
    """
    Description:
    ------------
    Returns a double representing the accuracy of the latitude and longitude properties, expressed in meters.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/GeolocationPosition
      https://developer.mozilla.org/en-US/docs/Web/API/GeolocationCoordinates
    """
    from epyk.core.js.primitives import JsNumber

    return JsNumber.JsNumber.get("%s.coords.accuracy" % self.varName)

  @property
  def altitudeAccuracy(self):
    """
    Description:
    ------------
    Returns a double representing the accuracy of the altitude expressed in meters. This value can be null

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/GeolocationPosition
      https://developer.mozilla.org/en-US/docs/Web/API/GeolocationCoordinates
    """
    from epyk.core.js.primitives import JsNumber

    return JsNumber.JsNumber.get("%s.coords.altitudeAccuracy" % self.varName)

  @property
  def heading(self):
    """
    Description:
    ------------
    Returns a double representing the direction towards which the device is facing. This value, specified in degrees, indicates how far off from heading true north the device is.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/GeolocationPosition
      https://developer.mozilla.org/en-US/docs/Web/API/GeolocationCoordinates
    """
    from epyk.core.js.primitives import JsNumber

    return JsNumber.JsNumber.get("%s.coords.heading" % self.varName)

  @property
  def altitude(self):
    """
    Description:
    ------------
    Returns a double representing the position's altitude in meters, relative to sea level.
    This value can be null if the implementation cannot provide the data.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/GeolocationPosition/coords
      https://developer.mozilla.org/en-US/docs/Web/API/GeolocationCoordinates
    """
    from epyk.core.js.primitives import JsNumber

    return JsNumber.JsNumber.get("%s.coords.altitude" % self.varName)

  @property
  def latitude(self):
    """
    Description:
    ------------
    Returns a double representing the position's latitude in decimal degrees.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/GeolocationPosition/coords
      https://developer.mozilla.org/en-US/docs/Web/API/GeolocationCoordinates
    """
    from epyk.core.js.primitives import JsNumber

    return JsNumber.JsNumber.get("%s.coords.latitude" % self.varName)

  @property
  def longitude(self):
    """
    Description:
    ------------
    Returns a double representing the position's longitude in decimal degrees.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/GeolocationPosition/coords
      https://developer.mozilla.org/en-US/docs/Web/API/GeolocationCoordinates
    """
    from epyk.core.js.primitives import JsNumber

    return JsNumber.JsNumber.get("%s.coords.longitude" % self.varName)

  @property
  def speed(self):
    """
    Description:
    ------------
    Returns a double representing the velocity of the device in meters per second. This value can be null.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/GeolocationPosition/coords
      https://developer.mozilla.org/en-US/docs/Web/API/GeolocationCoordinates
    """
    from epyk.core.js.primitives import JsNumber

    return JsNumber.JsNumber.get("%s.coords.speed" % self.varName)

  @property
  def timestamp(self):
    """
    Description:
    ------------
    Returns a DOMTimeStamp representing the time at which the location was retrieved.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/GeolocationPosition
    """
    from epyk.core.js.primitives import JsNumber

    return JsNumber.JsNumber.get("%s.timestamp" % self.varName)

  def toStr(self):
    from epyk.core.js.primitives import JsObject

    return JsObject.JsObject.get(self.varName)
