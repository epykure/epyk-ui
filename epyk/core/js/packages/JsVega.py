
from epyk.core.js import JsUtils
from epyk.core.js.packages import JsPackage


class Vega(JsPackage):
  lib_alias = {'js': "vega", 'css': 'vega'}

  def __init__(self, src, varName, setVar=False, report=None):
    super(Vega, self).__init__(src=src, varName=varName, selector=varName, setVar=setVar)
    self._report = report

  def parse(self, jsData):
    return JsUtils.jsWrap("vega.parse(%s)" % JsUtils.jsConvertData(jsData, None))

  def toSVG(self, scaleFactor):
    pass

  def toImageURL(self, kind, scaleFactor):
    pass

  def toCanvas(self, scaleFactor, options=None):
    pass

  def events(self, source, type, filter):
    pass
