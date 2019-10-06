"""
Wrapper to the Viz package

https://visjs.org/
"""

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
    pass

  def add(self):
    pass

  def clear(self):
    pass

  def distinct(self):
    pass

  def flush(self):
    pass

  def forEach(self):
    pass

  def map(self):
    pass

  def max(self, field):
    pass

  def min(self, field):
    pass

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

  def getIds(self):
    pass


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
