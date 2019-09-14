"""


"""

# https://github.com/nicolaskruchten/pivottable/wiki/Parameters

from epyk.core.js import JsUtils


class PivotUI(object):
  class __internal(object):
    jqId, htmlId, jsImports, cssImport = '', '', set([]), set([])

  def __init__(self, src=None):
    self.src = src if src is not None else self.__internal()
    self.src.jsImports.add('pivot')
    self.src.cssImport.add('pivot')
    #self.selector = self.src.jqId if hasattr(self.src, 'jqId') else None
    self._js = []