"""

"""

import json

from epyk.core.js import JsUtils


class JQueryTime(object):
  class __internal(object):
    jqId, htmlCode, jsImports, cssImport = '', '', set([]), set([])

  def __init__(self, src=None):
    self.src = src if src is not None else self.__internal()
    self.src.jsImports.add('timepicker')
    self.src.cssImport.add('timepicker')
    #self.selector = self.src.jqId if hasattr(self.src, 'jqId') else None
    self._js = []
