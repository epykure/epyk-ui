
from epyk.core.js.primitives import JsArray
from epyk.core.js.primitives import JsObject
from epyk.core.js.primitives import JsBoolean
from epyk.core.js.primitives import JsNumber
from epyk.core.js.primitives import JsString

from epyk.core.js.objects import JsNodeDom

from epyk.core.js.packages.JsVis import VisDataSet, VisDataView

from epyk.core.js.fncs import JsFncs
from epyk.core.js import JsUtils


class DataLoop(object):
  """
  Data Class used for all the loop and map in the Javascript side.
  This will get the below attributes

  val   : The current value in the loop
  index : The index item
  arr   : The full array (only available in case of arrays, map, filter, every  )
  """
  val, index, arr = JsObject.JsObject("value"), JsNumber.JsNumber("index", isPyData=False), JsArray.JsArray("arr")


class DataReduce(object):
  """

  rVal  :
  val   :
  index :
  """
  rVal, val, index = JsObject.JsObject("r"), JsNumber.JsNumber("o", isPyData=False), JsNumber.JsNumber("i", isPyData=False)


class DataSort(object):
  """

  """


class DataEach(object):
  """
  Data Class for the Jquery each loop

  index : index
  data  : element
  """
  index, data = JsNumber.JsNumber("index", isPyData=False), JsObject.JsObject("data", isPyData=False)


class DataAll(object):
  """
  Data Class for the Jquery each loop

  index : index
  data  : elt
  """
  index, element = JsNumber.JsNumber("index", isPyData=False), JsNodeDom.JsDoms.get(varName="elt")


class ContainerData(object):
  def __init__(self, report, schema):
    self._report, self._schema = report, schema

  @property
  def fnc(self):
    """
    All the predefined transformation functions.
    """
    return JsFncs.FncOnRecords(self._report._props, self._schema)

  @property
  def to(self):
    """
    All the possible object transformation to deal with external packages
    """
    return JsFncs.FncToObject(self._report._props, self._schema)

  @property
  def filter(self):
    """

    """
    return JsFncs.FncFiltere(self, self._report._props, self._schema)


class RawData(object):
  def __init__(self, report, records=None, profile=False):
    self._report, self._data_id = report, id(records)
    if "data" not in self._report._props:
      self._report._props["data"] = {"sources": {}, "schema": {}}
    self._report._props["data"]["sources"][self._data_id] = records
    self._report._props["data"]["schema"][self._data_id] = {'fncs': [], "profile": profile}
    self._data = self._report._props["data"]["sources"][self._data_id]
    self._schema = self._report._props["data"]["schema"][self._data_id]

  @classmethod
  def get(cls, report, varName):
    """
    Return the internal RawData object

    :return: A internal data object
    """
    return RawData(report, None)

  def setId(self, jqId):
    """
    Change the Id variable name for the javascript data source.

    Example

    :param jqId:

    :return: The Python object
    """
    self.jqId = jqId if jqId is not None else self._jqId
    return self

  def attach(self, html_obj, profile=False):
    """
    Attach the data object to a HTML Object.

    This function is automatically used in the different components in order
    to guarantee the link of the data. This will also ensure that the same data set will be store only once in the page

    Example

    :param html_obj:
    :param profile:

    """
    self._data["schema"][self._data_id].setdefault('containers', {})[html_obj.htmlCode] = {'fncs': [], 'outs': None, "profile": profile}
    return ContainerData(self._report, self._data["schema"][self._data_id]['containers'][html_obj.htmlCode])

  def toTsv(self, colNames=None, profile=False):
    """

    :return: A String with the Javascript function to be used
    """
    colNames = colNames or list(self._schema['keys'] | self._schema['values'])
    jsFncs = self._report._props.setdefault('js', {}).setdefault('functions', {})
    if "ToTsv" in jsFncs:
      jsFncs["ToTsv"] = {'content': '''var result = []; var tmp = []; var row = [];
                colNames.forEach(function(col){row.push(col)}); tmp.push(row.join('\t'));
                data.forEach(function(rec){
                  row = []; colNames.forEach(function(col){row.push(rec[col])});
                  tmp.push(row.join('\t'))}); result = tmp.join('\\n'); return result''', 'pmt': colNames}
    return "ToTsv(%s, %s)" % (self.jqId, colNames)

  @property
  def fnc(self):
    """

    :return:
    """
    return JsFncs.FncOnRecords(self, self._report._props, self._schema)

  @property
  def filter(self):
    """

    """
    return JsFncs.FncFiltere(self, self._report._props, self._schema)

  @property
  def to(self):
    """

    """
    return JsFncs.FncToObject(self, self._report._props, self._schema)

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


class Datamap(object):

  def __init__(self, components=None, attrs=None):
    self.__data = []
    if components is not None:
      for c in components:
        self.add(c)
    if attrs is not None:
      for k, v in attrs.items():
        self.attr(k, v)

  def add(self, component, htmlCode=None):
    """
    Description:
    -----------

    :param component:
    :param htmlCode:
    """
    self.__data.append((htmlCode or component.htmlCode, JsUtils.jsConvertData(component.dom.content, None)))
    return self

  def attr(self, k, v):
    """
    Description:
    -----------

    :param k:
    :param v:
    """
    self.__data.append((JsUtils.jsConvertData(k, None), JsUtils.jsConvertData(v, None)))
    return self

  def attrs(self, data):
    """
    Description:
    -----------

    :param data:
    """
    for k, v in data.items():
      self.attr(k, v)
    return self

  def toStr(self):
    return "{%s}" % ",".join(["%s: %s" % (k, v) for k, v in self.__data])

  def update(self, attrs):
    self.attrs(attrs)
    return self

  def __str__(self):
    return self.toStr()


class FormData(object):
  alias = None

  def new(self, varName, varType="let"):
    """
    Description:
    ------------

    :param varName:
    :param varType:
    """
    self.alias = varName
    return "%s %s = new FormData()" % (varType, varName)

  def get(self, varName):
    """
    Description:
    ------------

    :param varName:
    """
    self.alias = varName
    return self

  def append(self, name, value):
    """
    Description:
    ------------

    :param name:
    :param value:
    """
    return "%s.append(%s, %s)" % (self.alias, JsUtils.jsConvertData(name, None), value)

  def update(self, attrs):
    pass

  def toStr(self):
    return self.alias


class JsData(object):

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

  def crossfilter(self, data=None, var_name=None, crossDimension=None):
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

  def formdata(self):
    """
    Description:
    -----------

    """
    return FormData()

  def datamap(self, components=None, attrs=None):
    """
    Description:
    -----------

    """
    return Datamap(components, attrs)

  def dataset(self, data, var_name=None, options=None):
    """
    Description:
    -----------
    One of the starting points of the visualizations of vis.js is that they can deal with dynamic data, and allow manipulation of the data.
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

  def dataview(self, dataset, var_name=None, options=None):
    """
    Description:
    -----------
    A DataView offers a filtered and/or formatted view on a DataSet.
    One can subscribe to changes in a DataView, and easily get filtered or formatted data without having to specify filters and field types all the time.

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

  def records(self, data):
    """

    :param data:

    :return:
    """
    return RawData(self._src, data)

  @property
  def null(self):
    """
    Javascript null reference
    """
    return JsObject.JsObject("null", isPyData=False)


class JsDataTransfer(object):

  def __init__(self, varName):
    self.varId = varName

  @property
  def text(self):
    """
    Example

    Documentation

    :return:
    """
    return JsString.JsString("%s.getData('text')" % self.varId, isPyData=False)

  @property
  def files(self):
    """
    The DataTransfer.files property is a list of the files in the drag operation. If the operation includes no files, the list is empty.

    This feature can be used to drag files from a user's desktop to the browser.

    Related Pages:

			https://developer.mozilla.org/en-US/docs/Web/API/DataTransfer/files

    :return:
    """
    return JsArray.JsArray.get("%s.files" % self.varId)

  @property
  def dropEffect(self, flag=False):
    """

    Related Pages:

			https://developer.mozilla.org/en-US/docs/Web/API/DataTransfer/dropEffect

    :return:
    """
    if flag == False:
      return JsBoolean.JsBoolean("%s.dropEffect" % self.varId)

    if flag not in [None, 'move', 'link', 'copy']:
      raise Exception("")

    flag = JsUtils.jsConvertData(flag, None)
    return JsFncs.JsFunction("%s.dropEffect = %s" % (self.varId, flag))

  @property
  def effectAllowed(self, flag=False):
    """

    Related Pages:

			https://developer.mozilla.org/en-US/docs/Web/API/DataTransfer/effectAllowed

    :return:
    """
    if flag == False:
      return JsBoolean.JsBoolean("%s.effectAllowed" % self.varId)

    if flag not in [None, 'move', 'link', 'copy']:
      raise Exception("")

    flag = JsUtils.jsConvertData(flag, None)
    return JsFncs.JsFunction("%s.effectAllowed = %s" % (self.varId, flag))

  def clearData(self, format=None):
    """
    Remove the data associated with a given type. The type argument is optional.
    If the type is empty or not specified, the data associated with all types is removed.
    If data for the specified type does not exist, or the data transfer contains no data, this method will have no effect.

    Related Pages:

			https://developer.mozilla.org/en-US/docs/Web/API/DataTransfer/clearData

    :return:
    """
    if format is None:
      return JsFncs.JsFunction("%s.clearData()" % self.varId)

    format = JsUtils.jsConvertData(format, None)
    return JsFncs.JsFunction("%s.clearData(%s)" % (self.varId, format))

  def setDragImage(self):
    """

    :return:
    """

  def setData(self, data, format='text'):
    """

    :param data:
    :param format:
    :return:
    """
    format = JsUtils.jsConvertData(format, None)
    data = JsUtils.jsConvertData(data, None)
    return JsFncs.JsFunction("%s.setData(%s, %s)" % (self.varId, format, data))

  def getData(self, format="text"):
    """

    Example

    Documentation

    :param format:
    :return:
    """
    return JsString.JsString("%s.getData(%s)" % (self.varId, format), isPyData=False)


class JsClipboardData(object):

  def __init__(self, varName):
    self.varId = varName

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

  def getData(self, format):
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
    :param format: String. The data format
    """
    return JsString.JsString("%s.getData('%s')" % (self.varId, format), isPyData=False)
