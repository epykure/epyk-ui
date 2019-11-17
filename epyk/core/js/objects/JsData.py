"""

"""

import json

from epyk.core.js.primitives import JsArray
from epyk.core.js.primitives import JsObject
from epyk.core.js.primitives import JsNumber

from epyk.core.js.objects import JsNodeDom

from epyk.core.js.packages.JsCrossFilter import CrossFilter
from epyk.core.js.packages.JsVis import VisDataSet, VisDataView

from epyk.core.js.fncs import JsFncs


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
  def agg(self):
    """
    Property to the data aggregator functions
    The aggregator will create a new record with different column names
    """
    return JsFncs.FncRoAggRec(self._report._props, self._schema)

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
    self._data["schema"][self._data_id].setdefault('containers', {})[html_obj.htmlId] = {'fncs': [], 'outs': None, "profile": profile}
    return ContainerData(self._report, self._data["schema"][self._data_id]['containers'][html_obj.htmlId])

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

  @property
  def agg(self):
    """
    Property to the data aggregator functions
    The aggregator will create a new record with different column names
    """
    return JsFncs.FncRoAggRec(self, self._report._props, self._schema)

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

  def crossfilter(self, data, var_name):
    """

    :param data:

    :return:
    """
    return CrossFilter(self._src, varName=var_name, data=data)

  def dataset(self, data, var_name=None):
    """
    One of the starting points of the visualizations of vis.js is that they can deal with dynamic data, and allow manipulation of the data.
    To enable this, vis.js includes a flexible key/value based DataSet and DataView to handle unstructured JSON data.

    Documentation
    https://visjs.github.io/vis-data/data/index.html

    :param data:

    :return:
    """
    return VisDataSet(self._src, data=data, varName=var_name)

  def dataview(self, data, var_name=None):
    """
    A DataView offers a filtered and/or formatted view on a DataSet.
    One can subscribe to changes in a DataView, and easily get filtered or formatted data without having to specify filters and field types all the time.

    Viz.Js module

    DOcumentation
    https://visjs.github.io/vis-data/data/dataview.html

    :param data:
    :param var_name:

    """
    return VisDataView(self._src, data=data, varName=var_name)

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
