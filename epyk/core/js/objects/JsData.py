#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Optional, Union, List, Any
from epyk.core.py import primitives

from epyk.core.js.primitives import JsArray
from epyk.core.js.primitives import JsObject
from epyk.core.js.primitives import JsBoolean
from epyk.core.js.primitives import JsNumber
from epyk.core.js.primitives import JsString

from epyk.core.js.objects import JsNodeDom

from epyk.core.js.packages.JsVis import VisDataSet, VisDataView

from epyk.core.js.fncs import JsFncs
from epyk.core.js import JsUtils


class DataLoop:
  """
  Description:
  -----------
  Data Class used for all the loop and map in the Javascript side.
  This will get the below attributes

  val   : The current value in the loop
  index : The index item
  arr   : The full array (only available in case of arrays, map, filter, every  )
  """
  val, index, arr = JsObject.JsObject("value"), JsNumber.JsNumber("index", isPyData=False), JsArray.JsArray("arr")


class DataReduce:
  """
  Description:
  -----------

  rVal  :
  val   :
  index :
  """
  rVal, val = JsObject.JsObject("r"), JsNumber.JsNumber("o", isPyData=False)
  index = JsNumber.JsNumber("i", isPyData=False)


class DataSort:
  """

  """


class DataEach:
  """
  Description:
  -----------
  Data Class for the Jquery each loop

  index : index
  data  : element
  """
  index, data = JsNumber.JsNumber("index", isPyData=False), JsObject.JsObject("data", isPyData=False)


class DataAll:
  """
  Description:
  -----------
  Data Class for the Jquery each loop

  index : index
  data  : elt
  """
  index, element = JsNumber.JsNumber("index", isPyData=False), JsNodeDom.JsDoms.get(varName="elt")


class ContainerData:

  def __init__(self, report: primitives.PageModel, schema):
    self.page, self._schema = report, schema

  @property
  def fnc(self):
    """
    Description:
    -----------
    All the predefined transformation functions.
    """
    return JsFncs.FncOnRecords(self.page._props, self._schema)

  @property
  def to(self):
    """
    Description:
    -----------
    All the possible object transformation to deal with external packages
    """
    return JsFncs.FncToObject(self.page._props, self._schema)

  @property
  def filter(self):
    """
    Description:
    -----------

    """
    return JsFncs.FncFiltere(self, self.page._props, self._schema)


class RawData(primitives.JsDataModel):

  def __init__(self, report: primitives.PageModel, records=None, profile: bool = False):
    self.page, self._data_id = report, id(records)
    if "data" not in self.page._props:
      self.page._props["data"] = {"sources": {}, "schema": {}}
    self.page._props["data"]["sources"][self._data_id] = records
    self.page._props["data"]["schema"][self._data_id] = {'fncs': [], "profile": profile}
    self._data = self.page._props["data"]["sources"][self._data_id]
    self._schema = self.page._props["data"]["schema"][self._data_id]

  @classmethod
  def get(cls, report: primitives.PageModel, varName: str):
    """
    Description:
    -----------
    Return the internal RawData object.

    Attributes:
    ----------
    :param primitives.PageModel report: The main page object.
    :param str varName: The JavaScript variable name.

    :return: A internal data object
    """
    return RawData(report, None)

  def setId(self, jq_id: str = None):
    """
    Description:
    -----------
    Change the Id variable name for the javascript data source.

    Attributes:
    ----------
    :param str jq_id: The JQuery Identifier.

    :return: The Python object
    """
    self.jqId = jq_id if jq_id is not None else self._jqId
    return self

  def attach(self, html_obj: primitives.HtmlModel, profile: Optional[Union[bool, dict]] = False):
    """
    Description:
    -----------
    Attach the data object to a HTML Object.

    This function is automatically used in the different components in order
    to guarantee the link of the data. This will also ensure that the same data set will be store only once in the page

    Attributes:
    ----------
    :param primitives.HtmlModel html_obj:
    :param Optional[Union[bool, dict]] profile: Optional.
    """
    self._data["schema"][self._data_id].setdefault('containers', {})[html_obj.htmlCode] = {
      'fncs': [], 'outs': None, "profile": profile}
    return ContainerData(self.page, self._data["schema"][self._data_id]['containers'][html_obj.htmlCode])

  def toTsv(self, col_names: list = None, profile: Optional[Union[bool, dict]] = False):
    """
    Description:
    -----------

    :return: A String with the Javascript function to be used
    """
    col_names = col_names or list(self._schema['keys'] | self._schema['values'])
    js_funcs = self.page._props.setdefault('js', {}).setdefault('functions', {})
    if "ToTsv" in js_funcs:
      js_funcs["ToTsv"] = {'content': '''var result = []; var tmp = []; var row = [];
                colNames.forEach(function(col){row.push(col)}); tmp.push(row.join('\t'));
                data.forEach(function(rec){
                  row = []; colNames.forEach(function(col){row.push(rec[col])});
                  tmp.push(row.join('\t'))}); result = tmp.join('\\n'); return result''', 'pmt': col_names}
    return "ToTsv(%s, %s)" % (self.jqId, col_names)

  @property
  def fnc(self):
    """
    Description:
    -----------

    """
    return JsFncs.FncOnRecords(self, self.page._props, self._schema)

  @property
  def filter(self):
    """
    Description:
    -----------

    """
    return JsFncs.FncFiltere(self, self.page._props, self._schema)

  @property
  def to(self):
    """
    Description:
    -----------

    """
    return JsFncs.FncToObject(self, self.page._props, self._schema)

  def toStr(self):
    data = "data_%s" % self._data_id
    # Add the different javascript transformation functions
    for fnc in self._schema.get('fncs', []):
      data = fnc % data
    # Add the global filtering rules
    if len(self._schema.get("filters", [])) > 0:
      data = "%s(%s, [%s])" % ("JsFilter", data, ",".join(self._schema['filters']))
    # Add the final output object transformation
    if self._schema.get('out', None) is not None:
      data = self._schema['out'] % data
    return data


class Datamap(primitives.JsDataModel):

  def __init__(self, components: List[primitives.HtmlModel] = None, attrs: dict = None):
    self._data = []
    if components is not None:
      for c in components:
        if isinstance(c, tuple):
          self.attr(c[1], c[0].dom.content)
        else:
          self.add(c)
    if attrs is not None:
      for k, v in attrs.items():
        self.attr(k, v)

  def add(self, component: primitives.HtmlModel, htmlCode: str = None):
    """
    Description:
    -----------
    Add an HTML component to the object.
    The key will be the html_code.

    Attributes:
    ----------
    :param primitives.HtmlModel component: The HTML component.
    :param str htmlCode: Optional. The Html code.
    """
    self._data.append((htmlCode or component.htmlCode, JsUtils.jsConvertData(component.dom.content, None)))
    return self

  def attr(self, k: Union[str, primitives.JsDataModel], v: Any):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param k:
    :param v:
    """
    self._data.append((JsUtils.jsConvertData(k, None), JsUtils.jsConvertData(v, None)))
    return self

  def attrs(self, data: dict):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param data:
    """
    for k, v in data.items():
      self.attr(k, v)
    return self

  def toStr(self):
    return "{%s}" % ",".join(["%s: %s" % (k, v) for k, v in self._data])

  def get(self, value: Union[str, primitives.JsDataModel], dfl=None):
    return JsObject.JsObject.get(
      "{%s}[%s]" % (",".join(["%s: %s" % (k, v) for k, v in self._data]), JsUtils.jsConvertData(value, None)))

  def update(self, attrs: dict):
    self.attrs(attrs)
    return self

  def __str__(self):
    return self.toStr()


class FormData(primitives.JsDataModel):
  alias = None

  def new(self, varName: str, varType: str = "let"):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param varName:
    :param varType:
    """
    self.alias = varName
    return "%s %s = new FormData()" % (varType, varName)

  def get(self, varName: str):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param varName:
    """
    self.alias = varName
    return self

  def append(self, name: str, value: Any):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param name:
    :param value:
    """
    return "%s.append(%s, %s)" % (self.alias, JsUtils.jsConvertData(name, None), value)

  def add(self, component: primitives.HtmlModel, htmlCode: str = None):
    """
    Description:
    ------------
    Add an HTML component to the object.
    The key will be the html_code.

    Attributes:
    ----------
    :param primitives.HtmlModel component: The HTML component.
    :param str htmlCode: Optional. The Html code.
    """
    return "%s.append(%s, %s)" % (
      self.alias, JsUtils.jsConvertData(htmlCode or component.htmlCode, None),
      JsUtils.jsConvertData(component.dom.content, None))

  def update(self, attrs: Union[Datamap, dict]):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param Union[Datamap, dict] attrs:
    """
    appends = []
    if isinstance(attrs, Datamap):
      for k, v in attrs._data:
        appends.append(self.append(k, v))
    else:
      for k, v in attrs.items():
        appends.append(self.append(k, JsUtils.jsConvertData(v, None)))
    return appends

  def toStr(self):
    return self.alias


class JsData:

  def __init__(self, src):
    self._src = src

  def loop(self):
    return DataLoop()

  def reduce(self):
    return DataReduce()

  def sort(self):
    return DataSort()

  def each(self):
    return DataEach()

  @property
  def all(self):
    return DataAll()

  def crossfilter(self, data=None, var_name: str = None, crossDimension=None):
    """
    Description:
    -----------
    A crossfilter represents a multi-dimensional dataset.

    Constructs a new crossfilter. If records is specified, simultaneously adds the specified records.
    Records can be any array of JavaScript objects or primitives.

    Related Pages:

      https://github.com/crossfilter/crossfilter/wiki/API-Reference

    Attributes:
    ----------
    :param data:
    """
    from epyk.core.js.packages.JsCrossFilter import CrossFilter

    if data is None:
      data = "%s.top(Infinity)" % crossDimension.toStr()

    if var_name is None:
      return CrossFilter(self._src, varName=var_name, data=data, setVar=False)

    return CrossFilter(self._src, varName=JsUtils.getJsValid(var_name), data=data)

  @property
  def formdata(self):
    """
    Description:
    -----------

    """
    return FormData()

  def datamap(self, components: List[primitives.HtmlModel] = None, attrs: dict = None):
    """
    Description:
    -----------

    """
    return Datamap(components, attrs)

  def dataset(self, data: Any, var_name: str = None, options: Union[dict, primitives.JsDataModel] = None):
    """
    Description:
    -----------
    One of the starting points of the visualizations of vis.js is that they can deal with dynamic data,
    and allow manipulation of the data.
    To enable this, vis.js includes a flexible key/value based DataSet and DataView to handle unstructured JSON data.

    Related Pages:

      https://visjs.github.io/vis-data/data/index.html

    Attributes:
    ----------
    :param data:
    :param var_name:
    :param options:
    """
    vis_obj = VisDataSet(self._src, data=data, varName=JsUtils.getJsValid(var_name))
    if options is not None:
      vis_obj.setOptions(options)
    return vis_obj

  def dataview(self, dataset, var_name: str = None, options: Union[dict, primitives.JsDataModel] = None):
    """
    Description:
    -----------
    A DataView offers a filtered and/or formatted view on a DataSet.
    One can subscribe to change in a DataView, and easily get filtered or formatted data without having to specify
    filters and field types all the time.

    Viz.Js module

    Related Pages:

      https://visjs.github.io/vis-data/data/dataview.html

    Attributes:
    ----------
    :param dataset:
    :param options:
    :param var_name:
    """
    vis_obj = VisDataView(self._src, data=dataset.varId, varName=JsUtils.getJsValid(var_name))
    if options is not None:
      vis_obj.setOptions(options)
    return vis_obj

  def records(self, data: Any):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param data:
    """
    return RawData(self._src, data)

  @property
  def null(self):
    """
    Description:
    -----------
    Javascript null reference
    """
    return JsObject.JsObject("null", isPyData=False)


class JsDataTransfer:

  def __init__(self, varName: str):
    self.varId = varName

  @property
  def text(self):
    """
    Description:
    -----------

    """
    return JsString.JsString("%s.getData('text')" % self.varId, isPyData=False)

  @property
  def files(self):
    """
    Description:
    -----------
    The DataTransfer.files property is a list of the files in the drag operation. If the operation includes no files,
    the list is empty.

    This feature can be used to drag files from a user's desktop to the browser.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/DataTransfer/files
    """
    return JsArray.JsArray.get("%s.files" % self.varId)

  @property
  def dropEffect(self, flag: Union[bool, primitives.JsDataModel] = False):
    """
    Description:
    -----------

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/DataTransfer/dropEffect
    """
    if flag == False:
      return JsBoolean.JsBoolean("%s.dropEffect" % self.varId)

    if flag not in [None, 'move', 'link', 'copy']:
      raise ValueError("")

    flag = JsUtils.jsConvertData(flag, None)
    return JsFncs.JsFunction("%s.dropEffect = %s" % (self.varId, flag))

  @property
  def effectAllowed(self, flag: Union[bool, primitives.JsDataModel] = False):
    """
    Description:
    -----------

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/DataTransfer/effectAllowed
    """
    if flag == False:
      return JsBoolean.JsBoolean("%s.effectAllowed" % self.varId)

    if flag not in [None, 'move', 'link', 'copy']:
      raise ValueError("")

    flag = JsUtils.jsConvertData(flag, None)
    return JsFncs.JsFunction("%s.effectAllowed = %s" % (self.varId, flag))

  def clearData(self, format: Union[str, primitives.JsDataModel] = None):
    """
    Description:
    -----------
    Remove the data associated with a given type. The type argument is optional.
    If the type is empty or not specified, the data associated with all types is removed.
    If data for the specified type does not exist, or the data transfer contains no data, this method will have no
    effect.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/DataTransfer/clearData
    """
    if format is None:
      return JsFncs.JsFunction("%s.clearData()" % self.varId)

    format = JsUtils.jsConvertData(format, None)
    return JsFncs.JsFunction("%s.clearData(%s)" % (self.varId, format))

  def setDragImage(self):
    """
    Description:
    -----------

    """

  def setData(self, data: Any, format: Union[str, primitives.JsDataModel] = 'text'):
    """
    Description:
    -----------

    :param data:
    :param format:
    """
    format = JsUtils.jsConvertData(format, None)
    data = JsUtils.jsConvertData(data, None)
    return JsFncs.JsFunction("%s.setData(%s, %s)" % (self.varId, format, data))

  def getData(self, format: str = "text"):
    """
    Description:
    -----------

    :param format:
    """
    return JsString.JsString("%s.getData(%s)" % (self.varId, format), isPyData=False)


class JsClipboardData:

  def __init__(self, varName: str):
    self.varId = varName

  def src(self, name: str):
    """
    Description:
    ------------
    Set the event source.
    By default the event is event but this can be changed according to the trigger event.
    
    Attributes:
    ----------
    :param name: String. Change the event source
    """
    self.varId = "%s.clipboardData" % name
    return self

  @property
  def text(self):
    """
    Description:
    ------------
    The DataTransfer.getData() method retrieves drag data (as a DOMString) for the specified type.
    If the drag operation does not include data, this method returns an empty string

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/DataTransfer/getData
    """
    return JsString.JsString("%s.getData('text')" % self.varId, isPyData=False)

  @property
  def plain(self):
    """
    Description:
    ------------
    The DataTransfer.getData() method retrieves drag data (as a DOMString) for the specified type.
    If the drag operation does not include data, this method returns an empty string

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/DataTransfer/getData
    """
    return JsString.JsString("%s.getData('text/plain')" % self.varId, isPyData=False)

  @property
  def uri(self):
    """
    Description:
    ------------
    The DataTransfer.getData() method retrieves drag data (as a DOMString) for the specified type.
    If the drag operation does not include data, this method returns an empty string

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/DataTransfer/getData
    """
    return JsString.JsString("%s.getData('text/uri-list')" % self.varId, isPyData=False)

  def getData(self, format: str):
    """
    Description:
    ------------
    The DataTransfer.getData() method retrieves drag data (as a DOMString) for the specified type.
    If the drag operation does not include data, this method returns an empty string

    Example data types are text/plain and text/uri-list.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/API/DataTransfer/getData

    Attributes:
    ----------
    :param format: The data format
    """
    return JsString.JsString("%s.getData('%s')" % (self.varId, format), isPyData=False)
