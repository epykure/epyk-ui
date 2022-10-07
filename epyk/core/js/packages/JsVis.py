
from typing import Union, Any
from epyk.core.py import primitives

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects
from epyk.core.js.packages import JsPackage, DataAttrs


class VisDataSet(JsPackage):
  lib_alias = {'css': 'vis', 'js': 'vis'}

  def __init__(self, page: primitives.PageModel, js_code: str, data, set_var: bool = True):
    super(VisDataSet, self).__init__(js_code=js_code, selector="new vis.DataSet(%s)" % data, set_var=set_var, page=page)

  @property
  def length(self):
    """   The number of items in the DataSet.
    """
    return JsObjects.JsNumber.JsNumber("%s.length" % self.getStr())

  def add(self, data: Union[str, list, primitives.JsDataModel]):
    """   Add one or multiple items to the DataSet. data can be a single item or an array with items.

    Related Pages:

      https://visjs.github.io/vis-data/data/dataset.html

    :param Union[str, list, primitives.JsDataModel] data: data can be a single item or an array with items.

    :return: The function returns an array with the ids of the added items. See section Data Manipulation.
    """
    data = JsUtils.jsConvertData(data, None)
    return JsObjects.JsArray.JsArray("%s.add(%s)" % (self.varId, data))

  def clear(self, sender_id: Union[str, primitives.JsDataModel] = None):
    """   Clear all data from the DataSet.

    Related Pages:

      https://visjs.github.io/vis-data/data/dataset.html

    :param Union[str, primitives.JsDataModel] sender_id: The record ID to be removed.

    :return: The function returns an array with the ids of the removed items.
    """
    if sender_id is None:
      return JsObjects.JsArray.JsArray("%s.clear()" % self.varId)

    sender_id = JsUtils.jsConvertData(sender_id, None)
    return JsObjects.JsArray.JsArray("%s.clear(%s)" % (self.varId, sender_id))

  def distinct(self, field: Union[list, primitives.JsDataModel]):
    """   Find all distinct values of a specified field

    Related Pages:

      https://visjs.github.io/vis-data/data/dataset.html

    :param Union[list, primitives.JsDataModel] field:

    :return: Returns an unordered array containing all distinct values. If data items do not contain the
    specified field are ignored.
    """
    return JsObjects.JsArray.JsArray("%s.distinct(%s)" % (self.varId, JsUtils.jsConvertData(field, None)))

  def flush(self):
    """   Flush queued changes. Only available when the DataSet is configured with the option queue, see section Construction.

    Related Pages:

      https://visjs.github.io/vis-data/data/dataset.html
    """
    return JsObjects.JsObject.JsObject("%s.flush()" % self.varId)

  def forEach(self, callback, options=None):
    """   Execute a callback function for every item in the dataset.

    :param callback:
    :param options:
    """
    return JsObjects.JsObject.JsObject("%s.forEach()" % self.varId)

  def map(self, callback):
    raise NotImplementedError()

  def max(self, field: Union[str, primitives.JsDataModel]):
    """   Find the item with maximum value of specified field

    Related Pages:

      https://visjs.github.io/vis-data/data/dataset.html

    :param Union[str, primitives.JsDataModel] field:

    :return: Returns null if no item is found.
    """
    return JsObjects.JsObject.JsObject("%s.max(%s)" % (self.varId, JsUtils.jsConvertData(field, None)))

  def min(self, field: Union[str, primitives.JsDataModel]):
    """   Find the item with minimum value of specified field

    Related Pages:

      https://visjs.github.io/vis-data/data/dataset.html

    :param Union[str, primitives.JsDataModel] field:

    :return: Returns null if no item is found.
    """
    return JsObjects.JsObject.JsObject("%s.min(%s)" % (self.varId, JsUtils.jsConvertData(field, None)))

  def update(self):
    raise NotImplementedError()

  def on(self, event, callback):
    raise NotImplementedError()

  def off(self, event, callback):
    raise NotImplementedError()

  def remove(self, ids: Union[list, primitives.JsDataModel], sender_id=None):
    """   Remove a data item or an array with items.

    Related Pages:

      https://visjs.github.io/vis-data/data/dataset.html

    :param ids:
    :param sender_id:
    """
    ids = JsUtils.jsConvertData(ids, None)
    return JsObjects.JsArray.JsArray("%s.remove(%s)" % (self.varId, ids))

  def setOptions(self, options: Union[dict, primitives.JsDataModel]):
    """   Set options for the DataSet.

    Related Pages:

      https://visjs.github.io/vis-data/data/dataset.html

    :param Union[dict, primitives.JsDataModel] options:
    """
    return self.fnc_closure("setOptions(%s)" % options)

  def get(self, i: int):
    return JsObjects.JsObject.JsObject("%s.get(%s)" % (self.varId, i))

  def getIds(self, options: Union[dict, primitives.JsDataModel] = None):
    """   Get ids of all items or of a filtered set of items.

    Available options are described in section Data Selection, except that options fields and type are not applicable
    in case of getIds.

    Related Pages:

      https://visjs.github.io/vis-data/data/dataset.html

    :param Union[dict, primitives.JsDataModel] options:
    """
    if options is not None:
      options = JsUtils.jsConvertData(options, None)
      return JsObjects.JsArray.JsArray("%s.getIds(%s)" % (self.getStr(), options))

    return JsObjects.JsArray.JsArray("%s.getIds()" % self.varId)

  def options(self):
    """   Create a new option object on the Python side for DataViz
    """
    return VisDataOptions(self.page)


class VisDataOptions(DataAttrs):

  def align(self, position: Union[str, primitives.JsDataModel]):
    """   

    Related Pages:

    :param Union[str, primitives.JsDataModel] position:
    """
    return self.attr("align", JsUtils.jsConvertData(position, None))

  def queue_delay(self, n: Union[int, primitives.JsDataModel] = None):
    """   The queue will be flushed automatically after an inactivity of this delay in milliseconds. Default value is null

    Related Pages:

    :param Union[int, primitives.JsDataModel] n:
    """
    if n is None:
      n = self.page.js.data.null
    return self.attr("delay", JsUtils.jsConvertData(n, None))

  def queue_max(self, n: Union[int, primitives.JsDataModel] = None):
    """   When the queue exceeds the given maximum number of entries, the queue is flushed automatically. Default value is.

    Related Pages:

    :param Union[int, primitives.JsDataModel] n:
    """
    if n is None:
      n = self.page.js.number.POSITIVE_INFINITY
    return self.attr("max", JsUtils.jsConvertData(n, None))

  def autoResize(self, flag: Union[bool, primitives.JsDataModel]):
    """   

    Related Pages:

    :param Union[bool, primitives.JsDataModel] flag:
    """
    return self.attr("autoResize", JsUtils.jsConvertData(flag, None))

  def clickToUse(self, flag: Union[bool, primitives.JsDataModel]):
    """   

    Related Pages:

      https://visjs.github.io/vis-timeline/examples/timeline/interaction/clickToUse.html

    :param Union[bool, primitives.JsDataModel] flag:
    """
    return self.attr("clickToUse", JsUtils.jsConvertData(flag, None))

  def configure(self, flag: Union[bool, primitives.JsDataModel]):
    """   

    :param Union[bool, primitives.JsDataModel] flag:
    """
    return self.attr("configure", JsUtils.jsConvertData(flag, None))

  def dataAttributes(self, strings: Union[str, primitives.JsDataModel]):
    """   

    :param strings:
    """
    return self.attr("dataAttributes", JsUtils.jsConvertData(strings, None))

  @property
  def editable(self):
    raise NotImplementedError()

  def end(self, value: Union[Any, primitives.JsDataModel]):
    """   

    :param Union[Any, primitives.JsDataModel] value:
    """
    return self.attr("end", JsUtils.jsConvertData(value, None))

  def format(self, value: Union[Any, primitives.JsDataModel]):
    """   

    :param Union[Any, primitives.JsDataModel] value:
    """
    return self.attr("format", JsUtils.jsConvertData(value, None))

  @property
  def groupEditable(self):
    raise NotImplementedError()

  def groupHeightMode(self, text: Union[str, primitives.JsDataModel]):
    """   

    :param Union[str, primitives.JsDataModel] text:
    """
    return self.attr("groupHeightMode", JsUtils.jsConvertData(text, None))

  def groupOrder(self, text: Union[str, primitives.JsDataModel]):
    """   

    :param text:
    """
    return self.attr("groupOrder", JsUtils.jsConvertData(text, None))

  def groupOrderSwap(self, fnc):
    """   

    :param fnc:
    """
    raise NotImplementedError()

  def groupTemplate(self, fnc):
    """   

    :param fnc:
    """
    raise NotImplementedError()

  def height(self, n: Union[int, primitives.JsDataModel]):
    """   

    :param Union[int, primitives.JsDataModel] n:
    """
    return self.attr("height", JsUtils.jsConvertData(n, None))

  def hiddenDates(self, value: Union[Any, primitives.JsDataModel]):
    """   

    :param Union[Any, primitives.JsDataModel] value:
    """
    raise NotImplementedError()

  def horizontalScroll(self, flag: Union[bool, primitives.JsDataModel]):
    """   

    :param Union[bool, primitives.JsDataModel] flag:
    """
    return self.attr("horizontalScroll", JsUtils.jsConvertData(flag, None))


class VisDataView(JsPackage):
  lib_alias = {'css': 'vis', 'js': 'vis'}

  def __init__(self, page: primitives.PageModel, js_code: str, data: Any, set_var: bool = True):
    super(VisDataView, self).__init__(
      component=None, js_code=js_code, selector="new vis.DataView(%s)" % data, set_var=set_var,
      page=page)

  @property
  def length(self):
    """   The number of items in the DataSet.
    """
    return JsObjects.JsNumber.JsNumber("%s.length" % self.varId)

  def get(self, options: Union[dict, primitives.JsDataModel] = None, data: Any = None):
    """   Get a single item, multiple items, or all items from the DataView.

    Related Pages:

      https://visjs.github.io/vis-data/data/dataview.html

    :param Union[dict, primitives.JsDataModel] options:
    :param data:
    """
    if data is None:
      if options is None:
        return JsObjects.JsObject.JsObject("%s.get()" % (self.getStr()))

      options = JsUtils.jsConvertData(options, None)
      return JsObjects.JsObject.JsObject("%s.get(%s)" % (self.getStr(), options))

    options = JsUtils.jsConvertData(options, None)
    data = JsUtils.jsConvertData(data, None)
    return JsObjects.JsObject.JsObject("%s.get(%s, %s)" % (self.varId, options, data))

  def getByIds(self, ids: Union[list, primitives.JsDataModel],
               options: Union[dict, primitives.JsDataModel] = None,
               data: Any = None):
    """   Get a single item, multiple items, or all items from the DataView.

    Related Pages:

      https://visjs.github.io/vis-data/data/dataview.html

    :param Union[list, primitives.JsDataModel] ids:
    :param Union[dict, primitives.JsDataModel] options:
    :param data:
    """
    ids = JsUtils.jsConvertData(ids, None)
    if data is None:
      if options is None:
        return JsObjects.JsObject.JsObject.get("%s.get(%s)" % (self.varId, ids))

      options = JsUtils.jsConvertData(options, None)
      return JsObjects.JsObject.JsObject.get("%s.get(%s, %s)" % (self.varId, ids, options))

    options = JsUtils.jsConvertData(options, None)
    data = JsUtils.jsConvertData(data, None)
    return JsObjects.JsObject.JsObject.get("%s.get(%s, %s, %s)" % (self.varId, ids, options, data))

  def getDataSet(self, js_code: str):
    """   Get the DataSet to which the DataView is connected.

    Related Pages:

      https://visjs.github.io/vis-data/data/dataview.html

    :param str js_code: The JavaScript variable name for this dataset object.
    """
    return VisDataSet(page=self.page, data="%s.getDataSet()" % self.varId, js_code=js_code)

  def getIds(self, options: Union[dict, primitives.JsDataModel] = None):
    """   Get ids of all items or of a filtered set of items.
    Available options are described in section Data Selection, except that options fields and type are not applicable
    in case of getIds.

    Related Pages:

      https://visjs.github.io/vis-data/data/dataview.html

    :param Union[dict, primitives.JsDataModel] options:
    """
    if options is not None:
      options = JsUtils.jsConvertData(options, None)
      return JsObjects.JsArray.JsArray("%s.getIds(%s)" % (self.varId, options))

    return JsObjects.JsArray.JsArray("%s.getIds()" % self.varId)

  def off(self, event, callback):
    """   Unsubscribe from an event, remove an event listener.

    Related Pages:

      https://visjs.github.io/vis-data/data/dataview.html
      https://visjs.github.io/vis-data/data/dataview.html#Subscriptions

    :param event:
    :param callback:
    """
    raise NotImplementedError()

  def on(self, event, callback):
    """   Subscribe to an event, add an event listener.

    Related Pages:

      https://visjs.github.io/vis-data/data/dataview.html
      https://visjs.github.io/vis-data/data/dataview.html#Subscriptions

    :param event:
    :param callback:
    """
    raise NotImplementedError()

  def refresh(self):
    """   Refresh the filter results of a DataView.

    Related Pages:

      https://visjs.github.io/vis-data/data/dataview.html
    """
    return self.fnc_closure("refresh()")

  def setOptions(self, options: Union[dict, primitives.JsDataModel]):
    """   Set options for the DataSet.

    Related Pages:

      https://visjs.github.io/vis-data/data/dataset.html

    :param Union[dict, primitives.JsDataModel] options:
    """
    return self.fnc_closure("setOptions(%s)" % options)

  def setData(self, data: Any):
    """   Replace the DataSet of the DataView. Parameter data can be a DataSet or a DataView.

    :param Any data:
    """
    return self.fnc("setData(%s)" % JsUtils.jsConvertData(data, None))

  def options(self):
    """   Create a new option object on the Python side for DataViz
    """
    return VisDataOptions(self.page)


class VisDataGroups(DataAttrs):

  def className(self, value: Union[str, primitives.JsDataModel]):
    """   This field is optional. A className can be used to give groups an individual css style. For example, when a group
    has className 'red', one can define a css style .red { color: red; } .

    Related Pages:

      https://visjs.github.io/vis-timeline/docs/timeline/

    :param Union[str, primitives.JsDataModel] value:
    """
    return self.attr("className", JsUtils.jsConvertData(value, None))

  @property
  def content(self):
    """   The contents of the group. This can be plain text, html code or an html element.

    :prop item:
    """
    return self._attrs["content"]

  @content.setter
  def content(self, item):
    return self.attr("content", item)

  def options(self):
    pass


class VisGroups(JsPackage):
  lib_selector = "new vis.DataSet()"

  def add_group(self):
    return VisDataGroups(self.page)

  def add(self, groups):
    for name in groups:
      grp = self.add_group()
      grp.content = name
      self.fnc_closure("add(%s)" % grp.toStr())
    return self


class VisNetworkNode(JsPackage):
  pass


class VisNetworkEdge(JsPackage):

  def getPositions(self, node_ids):
    """   Returns the x y positions in canvas space of the nodes with the supplied nodeIds as an object

    Related Pages:

      https://visjs.github.io/vis-network/docs/network/

    :param node_ids:
    """
    raise NotImplementedError()

  def storePositions(self):
    """   When using the vis.DataSet to load your nodes into the network, this method will put the X and Y positions of
    all nodes into that dataset.

    Related Pages:

      https://visjs.github.io/vis-network/docs/network/
    """
    raise NotImplementedError()

  def moveNode(self, node_id, x, y):
    """   You can use this to programmatically move a node. The supplied x and y positions have to be in canvas space!

    :param node_id:
    :param x:
    :param y:
    """
    raise NotImplementedError()

  def getBoundingBox(self, node_id: str):
    """   Returns a bounding box for the node including label in the format:
    {top: Number, left: Number, right: Number, bottom: Number}

    :param str node_id:
    """
    raise NotImplementedError()

  def getConnectedNodes(self, node_id: str, direction=None):
    """   

    :param str node_id:
    :param direction:
    """
    raise NotImplementedError()

  def getConnectedEdges(self, node_id: str):
    """   

    :param str node_id:
    """
    raise NotImplementedError()


class VisNetwork(JsPackage):
  lib_alias = {'css': 'vis', 'js': 'vis'}

  def destroy(self):
    """   Remove the network from the DOM and remove all Hammer bindings and references.

    Related Pages:

      https://visjs.github.io/vis-network/docs/network/
    """
    return JsObjects.JsVoid("%s.destroy()" % self.varId)

  def setData(self, data: Any):
    """   Override all the data in the network.
    If stabilization is enabled in the physics module, the network will stabilize again.
    This method is also performed when first initializing the network.

    Related Pages:

      https://visjs.github.io/vis-network/docs/network/

    :param Any data:
    """
    return JsObjects.JsVoid("%s.setData(%s)" % (self.varId, JsUtils.jsConvertData(data, None)))

  def setOptions(self, options: Union[dict, primitives.JsDataModel]):
    """   Set the options. All available options can be found in the modules above.
    Each module requires it's own container with the module name to contain its options.

    Related Pages:

      https://visjs.github.io/vis-network/docs/network/

    :param Union[dict, primitives.JsDataModel] options:
    """
    return JsObjects.JsVoid("%s.setOptions(%s)" % (self.varId, JsUtils.jsConvertData(options, None)))

  def redraw(self):
    """   Redraw the network.

    Related Pages:

      https://visjs.github.io/vis-network/docs/network/
    """
    return JsObjects.JsVoid("%s.redraw()" % self.varId)

  def setSize(self, width: Union[int, primitives.JsDataModel], height: Union[int, primitives.JsDataModel]):
    """   Set the size of the canvas. This is automatically done on a window resize.

    Related Pages:

      https://visjs.github.io/vis-network/docs/network/

    :param Union[int, primitives.JsDataModel] width: The width
    :param Union[int, primitives.JsDataModel] height: The height
    """
    if isinstance(width, int):
      width = "%spx" % width

    if isinstance(height, int):
      height = "%spx" % height
    return JsObjects.JsVoid(
      "%s.setSize(%s, %s)" % (self.varId, JsUtils.jsConvertData(width, None), JsUtils.jsConvertData(height, None)))


class VisTimeline(JsPackage):
  lib_alias = {'css': 'vis-timeline', 'js': 'vis-timeline'}

  def addItem(self, data: Any):
    """   

    :param data:
    """
    return JsObjects.JsVoid("%s.itemsData.add(%s)" % (self.varId, JsUtils.jsConvertData(data, None)))
    #return JsObjects.JsVoid("console.log(%s)" % (self.varId))#, JsUtils.jsConvertData(data, None)))

  def addItems(self, data: Any):
    """   

    :param data:
    """
    return JsObjects.JsVoid("%s.forEach(function(data) {%s.itemsData.add(data)})" % (
      JsUtils.jsConvertData(data, None), self.varId))

  def setItems(self, data: Any):
    """   Replace the DataSet of the DataView. Parameter data can be a DataSet or a DataView.

    :param data:
    """
    return JsObjects.JsVoid("%s.setItems(%s)" % (self.varId, JsUtils.jsConvertData(data, None)))

  def setGroups(self, groups):
    """   Set a data set with groups for the Graph2d. groups can be an Array with Objects, a DataSet, or a DataView.
    For each of the groups, the items of the Graph2d are filtered on the property group, which must correspond
    with the id of the group.

    https://visjs.github.io/vis-timeline/docs/graph2d/

    :param groups:
    """
    return JsObjects.JsVoid("%s.setGroups(%s)" % (self.varId, JsUtils.jsConvertData(groups, None)))

  def setOptions(self, options: Union[dict, primitives.JsDataModel]):
    """   Set or update options. It is possible to change any option of the Graph2d at any time.
    You can for example switch orientation on the fly.

    https://visjs.github.io/vis-timeline/docs/graph2d/

    :param Union[dict, primitives.JsDataModel] options:
    """
    return JsObjects.JsVoid("%s.setOptions(%s)" % (self.varId, JsUtils.jsConvertData(options, None)))

  def destroy(self):
    """   Destroy the Graph2d. The Graph2d is removed from memory. all DOM elements and event listeners are cleaned up.

    Related Pages:

      https://visjs.github.io/vis-network/docs/network/
    """
    return JsObjects.JsVoid("%s.destroy()" % self.varId)

  def redraw(self):
    """   Force a redraw of the Graph2d. Can be useful to manually redraw when option autoResize=false.

    Related Pages:

      https://visjs.github.io/vis-timeline/docs/graph2d/
    """
    return JsObjects.JsVoid("%s.redraw()" % self.varId)

  def setData(self, data: Any):
    """   Set both groups and items at once. Both properties are optional.
    This is a convenience method for individually calling both setItems(items) and setGroups(groups).
    Both items and groups can be an Array with Objects, a DataSet (offering 2 way data binding), or a DataView
    (offering 1 way data binding).
    For each of the groups, the items of the timeline are filtered on the property group, which must correspond
    with the id of the group.

    Related Pages:

      https://visjs.github.io/vis-timeline/docs/timeline/

    :param data:
    """
    return JsObjects.JsVoid("%s.setData(%s)" % (self.varId, JsUtils.jsConvertData(data, None)))

  def fit(self):
    """   Adjust the visible window such that it fits all items.

    Related Pages:

      https://visjs.github.io/vis-timeline/docs/graph2d/
    """
    return JsObjects.JsVoid("%s.fit()" % self.varId)

  def addCustomTime(self, dt: Union[str, primitives.JsDataModel], code: Union[str, primitives.JsDataModel]):
    """   

    :param Union[str, primitives.JsDataModel] dt:
    :param Union[str, primitives.JsDataModel] code:
    """
    dt = JsUtils.jsConvertData(dt, None)
    code = JsUtils.jsConvertData(code, None)
    return JsObjects.JsVoid("%s.addCustomTime(new Date(%s), %s)" % (self.varId, dt, code))

  def setCustomTimeMarker(self, text: Union[str, primitives.JsDataModel], code: Union[str, primitives.JsDataModel],
                          flag: Union[bool, primitives.JsDataModel] = False):
    """   

    :param Union[str, primitives.JsDataModel] text:
    :param Union[str, primitives.JsDataModel] code:
    :param Union[bool, primitives.JsDataModel] flag:
    """
    text = JsUtils.jsConvertData(text, None)
    code = JsUtils.jsConvertData(code, None)
    flag = JsUtils.jsConvertData(flag, None)
    return JsObjects.JsVoid("%s.setCustomTimeMarker(%s, %s, %s)" % (self.varId, text, code, flag))

  def setCustomTimeTitle(self, text: Union[str, primitives.JsDataModel], code: Union[str, primitives.JsDataModel]):
    """   

    :param Union[str, primitives.JsDataModel] text:
    :param Union[str, primitives.JsDataModel] code:
    """
    text = JsUtils.jsConvertData(text, None)
    code = JsUtils.jsConvertData(code, None)
    return JsObjects.JsVoid("%s.setCustomTimeTitle(%s, %s)" % (self.varId, text, code))

  def removeCustomTime(self, code: Union[str, primitives.JsDataModel]):
    """   

    :param Union[str, primitives.JsDataModel] code:
    """
    code = JsUtils.jsConvertData(code, None)
    return JsObjects.JsVoid("%s.removeCustomTime(%s)" % (self.varId, code))


class VisGraph3D(JsPackage):
  lib_alias = {'css': 'vis', 'js': 'vis'}

  def animationStart(self):
    """   Start playing the animation.
    Only applicable when animation data is available.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/
    """
    return self.fnc_closure("animationStart()")

  def animationStop(self):
    """   Stop playing the animation.
    Only applicable when animation data is available.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/
    """
    return self.fnc_closure("animationStop()")

  def getCameraPosition(self):
    """   Returns an object with parameters horizontal, vertical and distance, which each one of them is a number,
    representing the rotation and position of the camera.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/
    """
    return "getCameraPosition()"

  def redraw(self):
    """   Redraw the graph. Useful after the camera position is changed externally, when data is changed, or when the
    layout of the webpage changed.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/
    """
    return JsObjects.JsVoid("%s.redraw()" % self.varName)

  def setData(self, data: Any):
    """   Replace the data in the Graph3d.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/

    :param Any data:
    """
    return self.fnc_closure("setData(%s)" % JsUtils.jsConvertData(data, None))

  def setOptions(self, options: Union[dict, primitives.JsDataModel]):
    """   Update options of Graph3d. The provided options will be merged with current options.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/

    :param Union[dict, primitives.JsDataModel] options:
    """
    return self.fnc_closure("setOptions(%s)" % JsUtils.jsConvertData(options, None))

  def setSize(self, width: Union[float, primitives.JsDataModel], height: Union[float, primitives.JsDataModel]):
    """   Parameters width and height are strings, containing a new size for the graph. Size can be provided in pixels
    or in percentages.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/

    :param Union[float, primitives.JsDataModel] width:
    :param Union[float, primitives.JsDataModel] height:
    """
    width = JsUtils.jsConvertData(width, None)
    height = JsUtils.jsConvertData(height, None)
    return self.fnc_closure("setSize(%s, %s)" % (width, height))

  def setCameraPosition(self, pos: Union[str, primitives.JsDataModel, float, dict, list]):
    """   Set the rotation and position of the camera.
    Parameter pos is an object which contains three parameters: horizontal, vertical, and distance.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/

    :param Union[str, primitives.JsDataModel, float, dict, list] pos:
    """
    pos = JsUtils.jsConvertData(pos, None)
    return self.fnc_closure("setCameraPosition(%s)" % pos)

  def onCameraPositionChange(self, js_func: Union[list, str]):
    """   The camera position changed. Fired after the user modified the camera position by moving (dragging) the graph,
    or by zooming (scrolling), but not after a call to setCameraPosition method.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/

    :param Union[list, str] js_func:
    """
    return self.fnc_closure("on('cameraPositionChange', %s)" % js_func)


class VisGraph2D(JsPackage):
  lib_alias = {'css': 'vis', 'js': 'vis'}

  def destroy(self):
    """   Destroy the Graph2d. The Graph2d is removed from memory. all DOM elements and event listeners are cleaned up.

    Related Pages:

      https://visjs.github.io/vis-timeline/docs/graph2d/
    """
    return JsObjects.JsVoid("%s.destroy()" % self.varId)

  def fit(self):
    """   Adjust the visible window such that it fits all items.

    Related Pages:

      https://visjs.github.io/vis-timeline/docs/graph2d/
    """
    return JsObjects.JsVoid("%s.fit()" % self.varId)

  def getCurrentTime(self):
    """   Get the current time. Only applicable when option showCurrentTime is true.

    Related Pages:

      https://visjs.github.io/vis-timeline/docs/graph2d/
    """
    return JsObjects.JsVoid("%s.getCurrentTime()" % self.varId)

  def getDataRange(self):
    """   Get the range of all the items as an object containing min: Date and max: Date.

    Related Pages:

      https://visjs.github.io/vis-timeline/docs/graph2d/
    """
    return JsObjects.JsVoid("%s.getCurrentTime()" % self.varId)

  def redraw(self):
    """   Redraw the graph. Useful after the camera position is changed externally, when data is changed, or when the layout
    of the webpage changed.

    Related Pages:

      https://visjs.github.io/vis-graph3d/docs/graph3d/
    """
    return JsObjects.JsVoid("%s.redraw()" % self.varId)

  def setItems(self, items: Union[dict, primitives.JsDataModel]):
    """   Set a data set with items for the Graph2d. items can be an Array with Objects, a DataSet, or a DataView.

    Related Pages:

      https://visjs.github.io/vis-timeline/docs/graph2d/

    :param Union[dict, primitives.JsDataModel] items:
    """
    items = JsUtils.jsConvertData(items, None)
    return JsObjects.JsVoid("%s.setItems(%s)" % (self.varId, items))

  def setOptions(self, options: Union[dict, primitives.JsDataModel]):
    """   Set or update options. It is possible to change any option of the Graph2d at any time.
    You can for example switch orientation on the fly.

    Related Pages:

      https://visjs.github.io/vis-timeline/docs/graph2d/

    :param Union[dict, primitives.JsDataModel] options:
    """
    options = JsUtils.jsConvertData(options, None)
    return JsObjects.JsVoid("%s.setOptions(%s)" % (self.varId, options))
