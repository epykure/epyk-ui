#!/usr/bin/python
# -*- coding: utf-8 -*-


class DataConfig(object):

  def __getitem__(self, key):
    from epyk.core.js.primitives import JsObjects

    return JsObjects.JsObjects.get("window['page_config']['%s']" % key)

  def fromConfig(self, k, default=None, page=None, end_point="/static/configs"):
    """
    Description:
    ------------
    Get the configuration for loading the report from json files.
    This will allow the creation of templates on the Python side and configuration in a static manner in json.

    By using this way of working it is easier to split the page and the configuration and non developers can
    change the content or create new ones based on the templates.

    Usage:
    -----


    Attributes:
    ----------
    :param k: String. THe alias of the cache, variable.
    :param default: Object. Optional. The default value of the cache.
    :param page: Report. Optional. The page object.
    :param end_point: String. Optional. THe static end point for the configurations.
    """
    if page.json_config_file is None:
      raise Exception("json_config_file must be attached to the page to load the corresponding configuration")

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


class TabulatorEvents(object):

  @property
  def row(self):
    """
    Description:
    ------------
    Get a Tabulator Row object.

    Usage:
    -----

    """
    from epyk.core.js.packages import JsTabulator

    return JsTabulator.RowComponent(setVar=False, varName=None)

  @property
  def cell(self):
    """
    Description:
    ------------
    Get a Tabulator cell object.

    Usage:
    -----

    """
    from epyk.core.js.packages import JsTabulator

    return JsTabulator.CellComponent(setVar=False, varName=None)

  @property
  def column(self):
    """
    Description:
    ------------
    Get a Tabulator column object.

    Usage:
    -----

    """
    from epyk.core.js.packages import JsTabulator

    return JsTabulator.ColumnComponent(setVar=False, varName=None)


class DataEvents(object):

  @property
  def tabulator(self):
    """
    Description:
    ------------

    Usage:
    -----

    """
    return TabulatorEvents()

  @property
  def files(self):
    """
    Description:
    ------------

    Usage:
    -----

    """
    from epyk.core.js.primitives import JsObjects
    return JsObjects.JsArray.JsArray.get("Array.from(event.dataTransfer.files)")

  @property
  def file(self):
    """
    Description:
    ------------

    Usage:
    -----

    """
    return DataFile("value")

  @property
  def data(self):
    """
    Description:
    ------------
    Interface to a standard data object available in any Event.
    This is the default variable name in all the JavaScript embedded methods.

    Usage:
    -----
    """
    from epyk.core.js.primitives import JsObjects
    return JsObjects.JsObjects.get("data")

  @property
  def value(self):
    """
    Description:
    ------------
    Interface to a standard value object available in any Event.
    This is the default variable name in all the JavaScript embedded methods.

    Usage:
    -----

    """
    from epyk.core.js.primitives import JsObjects
    return JsObjects.JsObjects.get("value")

  @property
  def event(self):
    """
    Description:
    ------------
    Interface to the standard event.

    Usage:
    -----

    """
    from epyk.core.js.objects import JsEvents

    return JsEvents.Event()

  @property
  def mouse(self):
    """
    Description:
    ------------
    Interface to the standard mouse event.

    Usage:
    -----

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
    This object is available in any event specific to touch screens
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


class DataFile(object):

  def __init__(self, varName="value"):
    self.varName = varName

  @property
  def name(self):
    """
    Description:
    ------------

    """
    from epyk.core.js.primitives import JsObjects
    return JsObjects.JsString.JsString.get("%s.name" % self.varName)

  @property
  def size(self):
    """
    Description:
    ------------

    """
    from epyk.core.js.primitives import JsObjects
    return JsObjects.JsString.JsString.get("%s.size" % self.varName)

  @property
  def lastModifiedDate(self):
    """
    Description:
    ------------

    """
    from epyk.core.js.primitives import JsObjects
    return JsObjects.JsDate.JsDate("%s.lastModifiedDate" % self.varName)

  @property
  def lastModified(self):
    """
    Description:
    ------------

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
    return JsObjects.JsString.JsString.get("(function(){var dt = new Date(%s.lastModified); return dt.toISOString() }())" % self.varName)

  @property
  def description(self):
    """
    Description:
    ------------

    """
    from epyk.core.js.primitives import JsObjects
    return JsObjects.JsString.JsString.get("%(varName)s.name +', '+ (%(varName)s.size / 1024) +'Ko, '+ %(dt)s" % {'varName': self.varName, 'dt': self.toISOString})


class DataLoops(object):

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
    The index value return in loop statement
    """
    from epyk.core.js.primitives import JsObjects
    return JsObjects.JsNumber.JsNumber.get("index")

  @property
  def file(self):
    return DataFile()


class DataPrimitives(object):

  def list(self, data=None, name=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param data: List. The Python object used to feed the list
    :param name: String. The variable name used on the JavaScript
    """
    from epyk.core.js.primitives import JsObjects

    if data is not None:
      setVar = True if name is not None else False
      return JsObjects.JsArray.JsArray(data, varName=name, setVar=setVar)

    return JsObjects.JsArray.JsArray.get(name)

  def dict(self, data=None, name=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param data:
    :param name: String. The variable name used on the JavaScript
    """
    from epyk.core.js.primitives import JsObjects

    if data is not None:
      setVar = True if name is not None else False
      return JsObjects.JsObject.JsObject(data, varName=name, setVar=setVar)

    return JsObjects.JsObject.JsObject.get(name)

  def str(self, data=None, name=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param data:
    :param name: String. The variable name used on the JavaScript
    """
    from epyk.core.js.primitives import JsObjects

    if data is not None:
      setVar = True if name is not None else False
      return JsObjects.JsString.JsString(data, varName=name, setVar=setVar)

    return JsObjects.JsString.JsString.get(name)

  def float(self, data=None, name=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param data:
    :param name: String. The variable name used on the JavaScript
    """
    from epyk.core.js.primitives import JsObjects

    if data is not None:
      setVar = True if name is not None else False
      return JsObjects.JsNumber.JsNumber(data, varName=name, setVar=setVar)

    return JsObjects.JsNumber.JsNumber.get(name)

  def int(self, data=None, name=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param data:
    :param name: String. The variable name used on the JavaScript
    """
    from epyk.core.js.primitives import JsObjects

    if data is not None:
      setVar = True if name is not None else False
      return JsObjects.JsNumber.JsNumber(data, varName=name, setVar=setVar)

    return JsObjects.JsNumber.JsNumber.get(name)

  def date(self, data=None, name=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param data:
    :param name:
    """
    from epyk.core.js.primitives import JsObjects

    if data is not None:
      setVar = True if name is not None else False
      return JsObjects.JsDate.JsDate(data, varName=name, setVar=setVar)

    if data is None and name is None:
      return JsObjects.JsDate.JsDate(data, varName=name, setVar=False)

    return JsObjects.JsDate.JsDate.get(name)
