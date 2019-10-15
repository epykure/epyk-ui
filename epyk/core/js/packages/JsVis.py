"""
Wrapper to the Viz package

https://visjs.org/
"""

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects
from epyk.core.js.packages import JsPackage, DataAttrs


class VisDataSet(JsPackage):
  lib_alias = {'css': 'vis', 'js': 'vis'}

  @property
  def length(self):
    """
    The number of items in the DataSet.

    :return:
    """
    return JsObjects.JsNumber.JsNumber("%s.length" % self.toStr())

  def add(self, jsData):
    """
    Add one or multiple items to the DataSet. data can be a single item or an array with items.

    Documentation
    https://visjs.github.io/vis-data/data/dataset.html

    :param jsData: data can be a single item or an array with items.

    :return: The function returns an array with the ids of the added items. See section Data Manipulation.
    """
    jsData = JsUtils.jsConvertData(jsData, None)
    return JsObjects.JsArray.JsArray("%s.add(%s)" % (self.toStr(), jsData))

  def clear(self, senderId=None):
    """
    Clear all data from the DataSet

    Documentation
    https://visjs.github.io/vis-data/data/dataset.html

    :return: The function returns an array with the ids of the removed items.
    """
    return JsObjects.JsArray.JsArray("%s.clear()" % (self.toStr()))

  def distinct(self, field):
    """
    Find all distinct values of a specified field

    Documentation
    https://visjs.github.io/vis-data/data/dataset.html

    :param field:

    :return: Returns an unordered array containing all distinct values. If data items do not contain the specified field are ignored.
    """
    field = JsUtils.jsConvertData(field, None)
    return JsObjects.JsArray.JsArray("%s.distinct(%s)" % (self.toStr(), field))

  def flush(self):
    """
    Flush queued changes. Only available when the DataSet is configured with the option queue, see section Construction.

    Documentation
    https://visjs.github.io/vis-data/data/dataset.html

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.flush()" % self.toStr())

  def forEach(self, callback, options=None):
    """
    Execute a callback function for every item in the dataset.

    :param callback:
    :param options:

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.forEach()" % self.toStr())

  def map(self):
    pass

  def max(self, field):
    """
    Find the item with maximum value of specified field

    Documentation
    https://visjs.github.io/vis-data/data/dataset.html

    :param field:

    :return: Returns null if no item is found.
    """
    field = JsUtils.jsConvertData(field, None)
    return JsObjects.JsObject.JsObject("%s.max(%s)" % (self.toStr(), field))

  def min(self, field):
    """
    Find the item with minimum value of specified field

    Documentation
    https://visjs.github.io/vis-data/data/dataset.html

    :param field:

    :return: Returns null if no item is found.
    """
    field = JsUtils.jsConvertData(field, None)
    return JsObjects.JsObject.JsObject("%s.min(%s)" % (self.toStr(), field))

  def update(self):
    pass

  def on(self, event, callback):
    pass

  def off(self, event, callback):
    pass

  def remove(self):
    pass

  def setOptions(self):
    pass

  def get(self):
    pass

  def getIds(self, options=None):
    """
    Get ids of all items or of a filtered set of items

    Available options are described in section Data Selection, except that options fields and type are not applicable in case of getIds

    Documentation
    https://visjs.github.io/vis-data/data/dataset.html

    :param options:

    :return:
    """
    if options is not None:
      options = JsUtils.jsConvertData(options, None)
      return JsObjects.JsArray.JsArray("%s.getIds(%s)" % (self.toStr(), options))

    return JsObjects.JsArray.JsArray("%s.getIds()" % self.toStr())


class VisDataOptions(DataAttrs):
  def align(self, position):
    """

    :param position:
    :return:
    """
    return self.attr("align", JsUtils.jsConvertData(position, None))

  def autoResize(self, flag):
    """

    :param flag:

    :return:
    """

  def clickToUse(self, flag):
    """

    :param flag:

    :return:
    """

  def configure(self, flag):
    """

    :param flag:

    :return:
    """

  def dataAttributes(self, strings):
    """

    :param strings:

    :return:
    """

  @property
  def editable(self):
    pass

  def end(self, object):
    """

    :param object:
    :return:
    """

  def format(self, object):
    """

    :param object:
    :return:
    """

  @property
  def groupEditable(self):
    pass

  def groupHeightMode(self, text):
    """

    :param text:
    :return:
    """

  def groupOrder(self, text):
    """

    :param text:
    :return:
    """

  def groupOrderSwap(self, fnc):
    """

    :param fnc:
    :return:
    """

  def groupTemplate(self, fnc):
    """

    :param fnc:
    :return:
    """

  def height(self, n):
    """

    :param n:
    :return:
    """

  def hiddenDates(self, object):
    """

    :param object:
    :return:
    """

  def horizontalScroll(self, flag):
    """

    :param flag:
    :return:
    """


class VisDataView(JsPackage):
  lib_alias = {'css': 'vis', 'js': 'vis'}

  @property
  def length(self):
    return

  def get(self, options=None, data=None):
    """
    Get a single item, multiple items, or all items from the DataView.

    Documentation
    https://visjs.github.io/vis-data/data/dataview.html

    :return:
    """

  def getByIds(self, ids, options=None, data=None):
    """
    Get a single item, multiple items, or all items from the DataView.

    Documentation
    https://visjs.github.io/vis-data/data/dataview.html

    :param ids:
    :param options:
    :param data:
    :return:
    """

  def getDataSet(self):
    """
    Get the DataSet to which the DataView is connected.

    Documentation
    https://visjs.github.io/vis-data/data/dataview.html

    :return:
    """

  def getIds(self, options):
    """
    Get ids of all items or of a filtered set of items.
    Available options are described in section Data Selection, except that options fields and type are not applicable in case of getIds.

    Documentation
    https://visjs.github.io/vis-data/data/dataview.html

    :param options:
    :return:
    """

  def off(self, event, callback):
    """
    Unsubscribe from an event, remove an event listener.

    Documentation
    https://visjs.github.io/vis-data/data/dataview.html
    https://visjs.github.io/vis-data/data/dataview.html#Subscriptions

    :param event:
    :param callback:
    :return:
    """

  def on(self, event, callback):
    """
    Subscribe to an event, add an event listener.

    Documentation
    https://visjs.github.io/vis-data/data/dataview.html
    https://visjs.github.io/vis-data/data/dataview.html#Subscriptions

    :param event:
    :param callback:
    :return:
    """

  def refresh(self):
    """
    Refresh the filter results of a DataView.

    Documentation
    https://visjs.github.io/vis-data/data/dataview.html

    :return:
    """

  def setData(self, data):
    """
    Replace the DataSet of the DataView. Parameter data can be a DataSet or a DataView.

    :param data:
    :return:
    """


class VisDataGroups(DataAttrs):
  def className(self, value):
    """
    This field is optional. A className can be used to give groups an individual css style. For example, when a group has className 'red', one can define a css style .red { color: red; } .

    Documentation
    https://visjs.github.io/vis-timeline/docs/timeline/

    :param value:

    :return:
    """
    return self.attr("className", JsUtils.jsConvertData(value, None))

  def content(self, item):
    """
    The contents of the group. This can be plain text, html code or an html element.

    :param item:

    :return:
    """
    return self.attr("content", item)


class VisNetworkNode(JsPackage):
  pass


class VisNetworkEdge(JsPackage):
  def getPositions(self, nodeIds):
    """
    Returns the x y positions in canvas space of the nodes with the supplied nodeIds as an object

    Documentation
    https://visjs.github.io/vis-network/docs/network/

    :param nodeIds:
    :return:
    """

  def storePositions(self):
    """
    When using the vis.DataSet to load your nodes into the network, this method will put the X and Y positions of all nodes into that dataset.

    Documentation
    https://visjs.github.io/vis-network/docs/network/

    :return:
    """

  def moveNode(self, nodeId, x, y):
    """
    You can use this to programatically move a node. The supplied x and y positions have to be in canvas space!

    :param nodeId:
    :param x:
    :param y:
    """

  def getBoundingBox(self, nodeId):
    """
    Returns a bounding box for the node including label in the format:
    {top: Number, left: Number, right: Number, bottom: Number}

    :param nodeId:
    """

  def getConnectedNodes(self, nodeId, direction=None):
    """

    :param nodeId:
    :param direction:
    :return:
    """

  def getConnectedEdges(self, nodeId):
    """

    :param nodeId:
    :return:
    """


class VisNetwork(JsPackage):
  lib_alias = {'css': 'vis', 'js': 'vis'}


class VisTImeline(JsPackage):
  lib_alias = {'css': 'vis', 'js': 'vis'}


class VisGraph3D(JsPackage):
  lib_alias = {'css': 'vis', 'js': 'vis'}

  def animationStart(self):
    """
    Start playing the animation.
    Only applicable when animation data is available.

    Documentation
    https://visjs.github.io/vis-graph3d/docs/graph3d/

    :return:
    """
    return self.fnc_closure("animationStart()")

  def animationStop(self):
    """
    Stop playing the animation.
    Only applicable when animation data is available.

    Documentation
    https://visjs.github.io/vis-graph3d/docs/graph3d/

    :return:
    """
    return self.fnc_closure("animationStop()")

  def getCameraPosition(self):
    """
    Returns an object with parameters horizontal, vertical and distance, which each one of them is a number, representing the rotation and position of the camera.

    Documentation
    https://visjs.github.io/vis-graph3d/docs/graph3d/

    :return:
    """
    return "getCameraPosition()"

  def redraw(self):
    """
    Redraw the graph. Useful after the camera position is changed externally, when data is changed, or when the layout of the webpage changed.

    Documentation
    https://visjs.github.io/vis-graph3d/docs/graph3d/

    :return:
    """
    return self.fnc_closure("redraw()")

  def setData(self, data):
    """
    Replace the data in the Graph3d.

    Documentation
    https://visjs.github.io/vis-graph3d/docs/graph3d/

    :param data:

    :return:
    """
    return self.fnc_closure("setData(%s)" % JsUtils.jsConvertData(data, None))

  def setOptions(self, options):
    """
    Update options of Graph3d. The provided options will be merged with current options.

    Documentation
    https://visjs.github.io/vis-graph3d/docs/graph3d/

    :param options:

    :return:
    """
    return self.fnc_closure("setOptions(%s)" % JsUtils.jsConvertData(options, None))

  def setSize(self, width, height):
    """
    Parameters width and height are strings, containing a new size for the graph. Size can be provided in pixels or in percentages.

    Documentation
    https://visjs.github.io/vis-graph3d/docs/graph3d/

    :param width:
    :param height:

    :return:
    """
    width = JsUtils.jsConvertData(width, None)
    height = JsUtils.jsConvertData(height, None)
    return self.fnc_closure("setSize(%s, %s)" % (width, height))

  def setCameraPosition(self, pos):
    """
    Set the rotation and position of the camera.
    Parameter pos is an object which contains three parameters: horizontal, vertical, and distance.

    Documentation
    https://visjs.github.io/vis-graph3d/docs/graph3d/

    :param pos:

    :return:
    """
    pos = JsUtils.jsConvertData(pos)
    return self.fnc_closure("setCameraPosition(%s)" % pos)

  def onCameraPositionChange(self, jsFnc):
    """
    The camera position changed. Fired after the user modified the camera position by moving (dragging) the graph, or by zooming (scrolling), but not after a call to setCameraPosition method.

    Documentation
    https://visjs.github.io/vis-graph3d/docs/graph3d/

    :param jsFnc:

    :return:
    """
    return self.fnc_closure("on('cameraPositionChange', %s)" % jsFnc)


if __name__ == "__main__":
  VisDataSet(None)
