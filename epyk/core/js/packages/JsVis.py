
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects
from epyk.core.js.packages import JsPackage, DataAttrs


class VisDataSet(JsPackage):
  lib_alias = {'css': 'vis', 'js': 'vis'}

  def __init__(self, src, varName, data, setVar=True):
    super(VisDataSet, self).__init__(src=src, varName=varName, selector="new vis.DataSet(%s)" % data, setVar=setVar)

  @property
  def length(self):
    """
    Description:
    -----------
    The number of items in the DataSet.
    """
    return JsObjects.JsNumber.JsNumber("%s.length" % self.getStr())

  def add(self, jsData):
    """
    Description:
    -----------
    Add one or multiple items to the DataSet. data can be a single item or an array with items.

    Related Pages:
    --------------
    https://visjs.github.io/vis-data/data/dataset.html

    Attributes:
    ----------
    :param jsData: data can be a single item or an array with items.

    :return: The function returns an array with the ids of the added items. See section Data Manipulation.
    """
    jsData = JsUtils.jsConvertData(jsData, None)
    return JsObjects.JsArray.JsArray("%s.add(%s)" % (self.varId, jsData))

  def clear(self, senderId=None):
    """
    Description:
    -----------
    Clear all data from the DataSet

    Related Pages:
    --------------
    https://visjs.github.io/vis-data/data/dataset.html

    Attributes:
    ----------
    :param senderId: The record ID to be removed

    :return: The function returns an array with the ids of the removed items.
    """
    if senderId is None:
      return JsObjects.JsArray.JsArray("%s.clear()" % (self.varId))

    senderId = JsUtils.jsConvertData(senderId, None)
    return JsObjects.JsArray.JsArray("%s.clear(%s)" % (self.varId, senderId))

  def distinct(self, field):
    """
    Description:
    -----------
    Find all distinct values of a specified field

    Related Pages:
    --------------
    https://visjs.github.io/vis-data/data/dataset.html

    Attributes:
    ----------
    :param field:

    :return: Returns an unordered array containing all distinct values. If data items do not contain the specified field are ignored.
    """
    return JsObjects.JsArray.JsArray("%s.distinct(%s)" % (self.varId, JsUtils.jsConvertData(field, None)))

  def flush(self):
    """
    Description:
    -----------
    Flush queued changes. Only available when the DataSet is configured with the option queue, see section Construction.

    Related Pages:
    --------------
    https://visjs.github.io/vis-data/data/dataset.html
    """
    return JsObjects.JsObject.JsObject("%s.flush()" % self.varId)

  def forEach(self, callback, options=None):
    """
    Description:
    -----------
    Execute a callback function for every item in the dataset.

    Attributes:
    ----------
    :param callback:
    :param options:

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.forEach()" % self.varId)

  def map(self, callback):
    pass

  def max(self, field):
    """
    Description:
    -----------
    Find the item with maximum value of specified field

    Related Pages:
    --------------
    https://visjs.github.io/vis-data/data/dataset.html

    Attributes:
    ----------
    :param field:

    :return: Returns null if no item is found.
    """
    return JsObjects.JsObject.JsObject("%s.max(%s)" % (self.varId, JsUtils.jsConvertData(field, None)))

  def min(self, field):
    """
    Description:
    -----------
    Find the item with minimum value of specified field

    Related Pages:
    --------------
    https://visjs.github.io/vis-data/data/dataset.html

    Attributes:
    ----------
    :param field:

    :return: Returns null if no item is found.
    """
    return JsObjects.JsObject.JsObject("%s.min(%s)" % (self.varId, JsUtils.jsConvertData(field, None)))

  def update(self):
    pass

  def on(self, event, callback):
    pass

  def off(self, event, callback):
    pass

  def remove(self, ids, senderId=None):
    """
    Description:
    -----------
    Remove a data item or an array with items

    Related Pages:
    --------------
    https://visjs.github.io/vis-data/data/dataset.html

    Attributes:
    ----------
    :param ids:
    :param senderId:

    :return:
    """
    ids = JsUtils.jsConvertData(ids, None)
    return JsObjects.JsArray.JsArray("%s.remove(%s)" % (self.varId, ids))

  def setOptions(self, options):
    """
    Description:
    -----------
    Set options for the DataSet.

    Related Pages:
    --------------
    https://visjs.github.io/vis-data/data/dataset.html

    Attributes:
    ----------
    :param options:
    """
    return self.fnc_closure("setOptions(%s)" % options)

  def get(self, i):
    return JsObjects.JsObject.JsObject("%s.get(%s)" % (self.varId, i))

  def getIds(self, options=None):
    """
    Description:
    -----------
    Get ids of all items or of a filtered set of items

    Available options are described in section Data Selection, except that options fields and type are not applicable in case of getIds

    Related Pages:
    --------------
    https://visjs.github.io/vis-data/data/dataset.html

    Attributes:
    ----------
    :param options:
    """
    if options is not None:
      options = JsUtils.jsConvertData(options, None)
      return JsObjects.JsArray.JsArray("%s.getIds(%s)" % (self.getStr(), options))

    return JsObjects.JsArray.JsArray("%s.getIds()" % self.varId)

  def options(self):
    """
    Description:
    -----------
    Create a new option object on the Python side for DataViz
    """
    return VisDataOptions(self.src)


class VisDataOptions(DataAttrs):

  def align(self, position):
    """
    Description:
    -----------

    Related Pages:
    --------------
    :param position:
    """
    return self.attr("align", JsUtils.jsConvertData(position, None))

  def queue_delay(self, n=None):
    """
    Description:
    -----------
    The queue will be flushed automatically after an inactivity of this delay in milliseconds. Default value is null

    Related Pages:
    --------------
    :param n:
    """
    if n is None:
      n = self._report.js.data.null
    return self.attr("delay", JsUtils.jsConvertData(n, None))

  def queue_max(self, n=None):
    """
    Description:
    -----------
    When the queue exceeds the given maximum number of entries, the queue is flushed automatically. Default value is

    Related Pages:
    --------------
    :param n:
    """
    if n is None:
      n = self._report.js.number.POSITIVE_INFINITY
    return self.attr("max", JsUtils.jsConvertData(n, None))

  def autoResize(self, flag):
    """
    Description:
    -----------

    Related Pages:
    --------------
    :param flag:
    """
    return self.attr("autoResize", JsUtils.jsConvertData(flag, None))

  def clickToUse(self, flag):
    """
    Description:
    -----------

    Related Pages:
    --------------
    https://visjs.github.io/vis-timeline/examples/timeline/interaction/clickToUse.html

    Related Pages:
    --------------
    :param flag:
    """
    return self.attr("clickToUse", JsUtils.jsConvertData(flag, None))

  def configure(self, flag):
    """
    Description:
    -----------

    Related Pages:
    --------------
    :param flag:
    """
    return self.attr("configure", JsUtils.jsConvertData(flag, None))

  def dataAttributes(self, strings):
    """
    Description:
    -----------

    Related Pages:
    --------------
    :param strings:
    """
    return self.attr("dataAttributes", JsUtils.jsConvertData(strings, None))

  @property
  def editable(self):
    pass

  def end(self, object):
    """
    Description:
    -----------

    Related Pages:
    --------------
    :param object:
    """
    return self.attr("end", JsUtils.jsConvertData(object, None))

  def format(self, object):
    """
    Description:
    -----------

    Related Pages:
    --------------
    :param object:
    """
    return self.attr("format", JsUtils.jsConvertData(object, None))

  @property
  def groupEditable(self):
    pass

  def groupHeightMode(self, text):
    """
    Description:
    -----------

    Related Pages:
    --------------
    :param text:
    """
    return self.attr("groupHeightMode", JsUtils.jsConvertData(text, None))

  def groupOrder(self, text):
    """
    Description:
    -----------

    Related Pages:
    --------------
    :param text:
    """
    return self.attr("groupOrder", JsUtils.jsConvertData(text, None))

  def groupOrderSwap(self, fnc):
    """
    Description:
    -----------

    Related Pages:
    --------------
    :param fnc:
    """

  def groupTemplate(self, fnc):
    """
    Description:
    -----------

    Related Pages:
    --------------
    :param fnc:
    """

  def height(self, n):
    """
    Description:
    -----------

    Related Pages:
    --------------
    :param n:
    """
    return self.attr("height", JsUtils.jsConvertData(n, None))

  def hiddenDates(self, object):
    """
    Description:
    -----------

    Related Pages:
    --------------
    :param object:
    """

  def horizontalScroll(self, flag):
    """
    Description:
    -----------

    Related Pages:
    --------------
    :param flag:
    """
    return self.attr("horizontalScroll", JsUtils.jsConvertData(flag, None))


class VisDataView(JsPackage):
  lib_alias = {'css': 'vis', 'js': 'vis'}

  def __init__(self, src, varName, data, setVar=True):
    super(VisDataView, self).__init__(src=src, varName=varName, selector="new vis.DataView(%s)" % data, setVar=setVar)

  @property
  def length(self):
    """
    Description:
    -----------
    The number of items in the DataSet.
    """
    return JsObjects.JsNumber.JsNumber("%s.length" % self.varId)

  def get(self, options=None, data=None):
    """
    Description:
    -----------
    Get a single item, multiple items, or all items from the DataView.

    Related Pages:
    --------------
    https://visjs.github.io/vis-data/data/dataview.html
    """
    if data is None:
      if options is None:
        return JsObjects.JsObject.JsObject("%s.get()" % (self.getStr()))

      options = JsUtils.jsConvertData(options, None)
      return JsObjects.JsObject.JsObject("%s.get(%s)" % (self.getStr(), options))

    options = JsUtils.jsConvertData(options, None)
    data = JsUtils.jsConvertData(data, None)
    return JsObjects.JsObject.JsObject("%s.get(%s, %s)" % (self.varId, options, data))

  def getByIds(self, ids, options=None, data=None):
    """
    Description:
    -----------
    Get a single item, multiple items, or all items from the DataView.

    Related Pages:
    --------------
    https://visjs.github.io/vis-data/data/dataview.html

    Attributes:
    ----------
    :param ids:
    :param options:
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

  def getDataSet(self, vanName):
    """
    Description:
    -----------
    Get the DataSet to which the DataView is connected.

    Related Pages:
    --------------
    https://visjs.github.io/vis-data/data/dataview.html
    """
    return VisDataSet(src=self.src, data="%s.getDataSet()" % self.varId, varName=vanName)

  def getIds(self, options=None):
    """
    Description:
    -----------
    Get ids of all items or of a filtered set of items.
    Available options are described in section Data Selection, except that options fields and type are not applicable in case of getIds.

    Related Pages:
    --------------
    https://visjs.github.io/vis-data/data/dataview.html

    Attributes:
    ----------
    :param options:
    """
    if options is not None:
      options = JsUtils.jsConvertData(options, None)
      return JsObjects.JsArray.JsArray("%s.getIds(%s)" % (self.varId, options))

    return JsObjects.JsArray.JsArray("%s.getIds()" % self.varId)

  def off(self, event, callback):
    """
    Description:
    -----------
    Unsubscribe from an event, remove an event listener.

    Related Pages:
    --------------
    https://visjs.github.io/vis-data/data/dataview.html
    https://visjs.github.io/vis-data/data/dataview.html#Subscriptions

    Attributes:
    ----------
    :param event:
    :param callback:
    """

  def on(self, event, callback):
    """
    Description:
    -----------
    Subscribe to an event, add an event listener.

    Related Pages:
    --------------
    https://visjs.github.io/vis-data/data/dataview.html
    https://visjs.github.io/vis-data/data/dataview.html#Subscriptions

    Attributes:
    ----------
    :param event:
    :param callback:
    """

  def refresh(self):
    """
    Description:
    -----------
    Refresh the filter results of a DataView.

    Related Pages:
    --------------
    https://visjs.github.io/vis-data/data/dataview.html
    """
    return self.fnc_closure("refresh()")

  def setData(self, data):
    """
    Description:
    -----------
    Replace the DataSet of the DataView. Parameter data can be a DataSet or a DataView.

    Attributes:
    ----------
    :param data:
    """
    return self.fnc("setData(%s)" % JsUtils.jsConvertData(data, None))

  def options(self):
    """
    Description:
    -----------
    Create a new option object on the Python side for DataViz
    """
    return VisDataOptions(self.src)


class VisDataGroups(DataAttrs):

  def className(self, value):
    """
    Description:
    -----------
    This field is optional. A className can be used to give groups an individual css style. For example, when a group has className 'red', one can define a css style .red { color: red; } .

    Related Pages:
    --------------
    https://visjs.github.io/vis-timeline/docs/timeline/

    Attributes:
    ----------
    :param value:
    """
    return self.attr("className", JsUtils.jsConvertData(value, None))

  @property
  def content(self):
    """
    Description:
    -----------
    The contents of the group. This can be plain text, html code or an html element.

    Attributes:
    ----------
    :param item:
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
    return VisDataGroups(self.src)

  def add(self, groups):
    for name in groups:
      grp = self.add_group()
      grp.content = name
      self.fnc_closure("add(%s)" % grp.toStr())
    return self


class VisNetworkNode(JsPackage):
  pass


class VisNetworkEdge(JsPackage):
  def getPositions(self, nodeIds):
    """
    Description:
    -----------
    Returns the x y positions in canvas space of the nodes with the supplied nodeIds as an object

    Related Pages:
    --------------
    https://visjs.github.io/vis-network/docs/network/

    Attributes:
    ----------
    :param nodeIds:
    """

  def storePositions(self):
    """
    Description:
    -----------
    When using the vis.DataSet to load your nodes into the network, this method will put the X and Y positions of all nodes into that dataset.

    Related Pages:
    --------------
    https://visjs.github.io/vis-network/docs/network/
    """

  def moveNode(self, nodeId, x, y):
    """
    Description:
    -----------
    You can use this to programatically move a node. The supplied x and y positions have to be in canvas space!

    Attributes:
    ----------
    :param nodeId:
    :param x:
    :param y:
    """

  def getBoundingBox(self, nodeId):
    """
    Description:
    -----------
    Returns a bounding box for the node including label in the format:
    {top: Number, left: Number, right: Number, bottom: Number}

    Attributes:
    ----------
    :param nodeId:
    """

  def getConnectedNodes(self, nodeId, direction=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param nodeId:
    :param direction:
    """

  def getConnectedEdges(self, nodeId):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param nodeId:
    """


class VisNetwork(JsPackage):
  lib_alias = {'css': 'vis', 'js': 'vis'}

  def destroy(self):
    """
    Description:
    -----------
    Remove the network from the DOM and remove all Hammer bindings and references.

    Related Pages:
    --------------
    https://visjs.github.io/vis-network/docs/network/
    """
    return self.fnc_closure("destroy()")

  def setData(self, data):
    """
    Description:
    -----------
    Override all the data in the network.
    If stabilization is enabled in the physics module, the network will stabilize again.
    This method is also performed when first initializing the network.

    Related Pages:
    --------------
    https://visjs.github.io/vis-network/docs/network/

    Attributes:
    ----------
    :param data:
    """
    return self.fnc_closure("setData(%s)" % JsUtils.jsConvertData(data, None))

  def setOptions(self, options):
    """
    Description:
    -----------
    Set the options. All available options can be found in the modules above.
    Each module requires it's own container with the module name to contain its options.

    Related Pages:
    --------------
    https://visjs.github.io/vis-network/docs/network/

    Attributes:
    ----------
    :param options:
    """
    return self.fnc_closure("setOptions(%s)" % JsUtils.jsConvertData(options, None))

  def redraw(self):
    """
    Description:
    -----------
    Redraw the network.

    Related Pages:
    --------------
    https://visjs.github.io/vis-network/docs/network/
    """
    return self.fnc_closure("redraw()")

  def setSize(self, width, height):
    """
    Description:
    -----------
    Set the size of the canvas. This is automatically done on a window resize.

    Related Pages:
    --------------
    https://visjs.github.io/vis-network/docs/network/

    Attributes:
    ----------
    :param width:
    :param height:
    """
    if isinstance(width, int):
      width = "%spx" % width

    if isinstance(height, int):
      height = "%spx" % height
    return self.fnc_closure("setSize(%s, %s)" % (JsUtils.jsConvertData(width, None), JsUtils.jsConvertData(height, None)))


class VisTimeline(JsPackage):
  lib_alias = {'css': 'vis', 'js': 'vis'}


class VisGraph3D(JsPackage):
  lib_alias = {'css': 'vis', 'js': 'vis'}

  def animationStart(self):
    """
    Description:
    -----------
    Start playing the animation.
    Only applicable when animation data is available.

    Related Pages:
    --------------
    https://visjs.github.io/vis-graph3d/docs/graph3d/
    """
    return self.fnc_closure("animationStart()")

  def animationStop(self):
    """
    Description:
    -----------
    Stop playing the animation.
    Only applicable when animation data is available.

    Related Pages:
    --------------
    https://visjs.github.io/vis-graph3d/docs/graph3d/
    """
    return self.fnc_closure("animationStop()")

  def getCameraPosition(self):
    """
    Description:
    -----------
    Returns an object with parameters horizontal, vertical and distance, which each one of them is a number, representing the rotation and position of the camera.

    Related Pages:
    --------------
    https://visjs.github.io/vis-graph3d/docs/graph3d/
    """
    return "getCameraPosition()"

  def redraw(self):
    """
    Description:
    -----------
    Redraw the graph. Useful after the camera position is changed externally, when data is changed, or when the layout of the webpage changed.

    Related Pages:
    --------------
    https://visjs.github.io/vis-graph3d/docs/graph3d/
    """
    return self.fnc_closure("redraw()")

  def setData(self, data):
    """
    Description:
    -----------
    Replace the data in the Graph3d.

    Related Pages:
    --------------
    https://visjs.github.io/vis-graph3d/docs/graph3d/

    Attributes:
    ----------
    :param data:
    """
    return self.fnc_closure("setData(%s)" % JsUtils.jsConvertData(data, None))

  def setOptions(self, options):
    """
    Description:
    -----------
    Update options of Graph3d. The provided options will be merged with current options.

    Related Pages:
    --------------
    https://visjs.github.io/vis-graph3d/docs/graph3d/

    Attributes:
    ----------
    :param options:
    """
    return self.fnc_closure("setOptions(%s)" % JsUtils.jsConvertData(options, None))

  def setSize(self, width, height):
    """
    Description:
    -----------
    Parameters width and height are strings, containing a new size for the graph. Size can be provided in pixels or in percentages.

    Related Pages:
    --------------
    https://visjs.github.io/vis-graph3d/docs/graph3d/

    Attributes:
    ----------
    :param width:
    :param height:
    """
    width = JsUtils.jsConvertData(width, None)
    height = JsUtils.jsConvertData(height, None)
    return self.fnc_closure("setSize(%s, %s)" % (width, height))

  def setCameraPosition(self, pos):
    """
    Description:
    -----------
    Set the rotation and position of the camera.
    Parameter pos is an object which contains three parameters: horizontal, vertical, and distance.

    Related Pages:
    --------------
    https://visjs.github.io/vis-graph3d/docs/graph3d/

    Attributes:
    ----------
    :param pos:
    """
    pos = JsUtils.jsConvertData(pos)
    return self.fnc_closure("setCameraPosition(%s)" % pos)

  def onCameraPositionChange(self, jsFnc):
    """
    Description:
    -----------
    The camera position changed. Fired after the user modified the camera position by moving (dragging) the graph, or by zooming (scrolling), but not after a call to setCameraPosition method.

    Related Pages:
    --------------
    https://visjs.github.io/vis-graph3d/docs/graph3d/

    Attributes:
    ----------
    :param jsFnc:
    """
    return self.fnc_closure("on('cameraPositionChange', %s)" % jsFnc)
