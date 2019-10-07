"""
Wrapper to the Viz package

https://visjs.org/
"""

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects
from epyk.core.js.packages import JsPackage


class VisDataSet(JsPackage):
  """

  Documentation
  https://visjs.github.io/vis-data/data/dataset.html
  """
  lib_alias = 'vis'

  class __internal(object):
    # By default it will attach eveything to the body
    jqId, jsImports, cssImport = 'd3.select("body")', set([]), set([])

  def __init__(self, src, id=None):
    self.src = src if src is not None else self.__internal()
    self._selector = id
    self.src.jsImports.add(self.lib_alias)
    self.src.cssImport.add(self.lib_alias)
    self._js = []

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


class VisNetwork(JsPackage):
  lib_alias = 'vis'

  class __internal(object):
    # By default it will attach eveything to the body
    jqId, jsImports, cssImport = 'd3.select("body")', set([]), set([])

  def __init__(self, src, id=None):
    self.src = src if src is not None else self.__internal()
    self._selector = id
    self.src.jsImports.add(self.lib_alias)
    self.src.cssImport.add(self.lib_alias)
    self._js = []


if __name__ == "__main__":
  VisDataSet(None)
