
from epyk.core.js.html import JsHtml


class JsHtmlD3(JsHtml.JsHtml):

  def __init__(self, htmlObj, varName=None, setVar=True, isPyData=True, report=None):
    super(JsHtmlD3, self).__init__(htmlObj, varName, setVar, isPyData, report)
    self.varName = "d3.select('#%s')" % self.htmlId
