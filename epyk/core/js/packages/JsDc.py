"""
DC.js API

http://dc-js.github.io/dc.js/docs/html/
"""

from epyk.core.py import primitives
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObject
from epyk.core.js.packages import JsPackage


class DC(JsPackage):
  lib_alias = {'css': 'dc', 'js': 'dc'}

  def __init__(self, page=None, js_code=None, set_var=True, component=None):
    self.page, self._sub_chart, self.component = page, None, component
    if component is not None:
      # for series chart the selector is specific
      self._selector = "new dc.%s('#%s')" % (self.chartFnc, component.htmlCode)
    self.varName, self.setVar = js_code, set_var
    self.page.jsImports.add(self.lib_alias['js'])
    self.page.cssImport.add(self.lib_alias['css'])
    self._js, self._xaxis, self._yaxis, self._u = [[]], None, None, {}

  def x(self):
    return self.fnc("x(d3.scaleLinear().domain([0,20]))")

  def chartGroup(self, group_name, profile=False):
    return self.fnc("chartGroup(%s)" % JsUtils.jsConvertFncs(group_name, toStr=True, profile=profile))

  def redrawGroup(self):
    """   Redraws all charts in the same group as this chart, typically in reaction to a filter change. If the chart has
    a commitHandler, it will be executed and waited for.

    Related Pages:

      http://dc-js.github.io/dc.js/docs/html/BaseMixin.html#redrawGroup__anchor
    """
    return JsObject.JsObject.get("%s.redrawGroup()" % self.varId)

  def width(self, n):
    """   

    :param n:

    :return: Return 'self' to allow the chaining on the Python side
    """
    return self.fnc("width(%s)" % JsUtils.jsConvertData(n, None))

  def height(self, n):
    """   

    :param n:
    """
    return self.fnc("height(%s)" % JsUtils.jsConvertData(n, None))

  def yAxisLabel(self, text):
    """   

    :param text:
    """
    return self.fnc("yAxisLabel(%s)" % JsUtils.jsConvertData(text, None))

  def xAxisLabel(self, text):
    """   

    :param text:
    """
    return self.fnc("xAxisLabel(%s)" % JsUtils.jsConvertData(text, None))

  def render(self):
    """   

    """
    self._js.append(["render()"])
    return self

  def dimension(self, values):
    """   

    :param values:
    """
    return self.fnc("dimension(%s)" % values)
    #return self.fnc("dimension(%s)" % JsUtils.jsConvertData(values, None))

  def group(self, groups):
    """   

    :param groups:
    """
    return self.fnc("group(%s)" % groups)
    #return self.fnc("group(%s)" % JsUtils.jsConvertData(groups, None))

  def toStr(self):
    """
    Javascript representation

    :return: Return the Javascript String
    """
    str_chart = ""
    if self._sub_chart is not None:
      if self._sub_chart._js != [[]]:
        str_chart = ".chart(function(c) { return %s; })" % self._sub_chart.toStr()
      else:
        str_chart = ".chart(function(c) { return %s; })" % self._sub_chart._selector

    if self._selector is None:
      raise ValueError("Selector not defined, use this() or new() first")

    obj_content = []
    for i, js in enumerate(self._js):
      if len(js) == 0:
        continue

      str_fnc = ".".join([d.toStr() if hasattr(d, "toStr") else d for d in js])
      if self.setVar:
        if str_fnc:
          str_fnc = "var %s = %s; %s%s.%s" % (self.varId, self._selector, self.varId, str_chart, str_fnc)
        else:
          str_fnc = "var %s = %s" % (self.varId, self._selector)
        self.setVar = False
      else:
        if str_fnc:
          if i in self._u:
            # to avoid raising an error when the variable is not defined
            str_fnc = "if(%s !== undefined){%s.%s}" % (self.varId, self.varId, str_fnc)
          else:
            js_code = self._mapVarId(str_fnc, self.varId)
            str_fnc = "%s.%s" % (js_code, str_fnc)
        else:
          str_fnc = self.varId
      obj_content.append(str_fnc)
    self._js = [[]] # empty the stack
    return "; ".join(obj_content)


class Line(DC):
  chartFnc = "LineChart"

  def curve(self, fnc):
    return self.fnc("curve(%s)" % fnc)

  def curveStepBefore(self):
    return self.fnc("curve(d3.curveStepBefore)")

  def renderArea(self, flag):
    """   

    :param flag:
    """
    return self.fnc("renderArea(%s)" % JsUtils.jsConvertData(flag, None))

  def renderDataPoints(self, flag):
    """   

    :param flag:
    """
    return self.fnc("renderDataPoints(%s)" % JsUtils.jsConvertData(flag, None))

  def clipPadding(self, value):
    """   

    :param value:
    """
    return self.fnc("clipPadding(%s)" % JsUtils.jsConvertData(value, None))


class Bar(DC):
  chartFnc = "BarChart"

  def controlsUseVisibility(self, flag):
    """   

    Related Pages:

      https://dc-js.github.io/dc.js/examples/bar-single-select.html

    :param flag:
    """
    return self.fnc("controlsUseVisibility(%s)" % JsUtils.jsConvertData(flag, None))

  def singleSelection(self):
    self.xUnitsOridinal()
    self.scaleBand()
    return self.fnc("addFilterHandler(function(filters, filter) {return [filter]; })")

  def xUnitsOridinal(self):
    return self.fnc("xUnits(dc.units.ordinal)")

  def scaleBand(self):
    return self.fnc("x(d3.scaleBand())")


class Row(DC):
  chartFnc = "RowChart"

  def elasticY(self, flag):
    """   

    Related Pages:

      https://github.com/dc-js/dc.js/blob/master/web-src/examples/row-targets.html

    :param flag:
    """
    return self.fnc("elasticY(%s)" % JsUtils.jsConvertData(flag, None))

  def elasticX(self, flag):
    """   

    Related Pages:

      https://github.com/dc-js/dc.js/blob/master/web-src/examples/row-targets.html

    :param flag:
    """
    return self.fnc("elasticX(%s)" % JsUtils.jsConvertData(flag, None))

  def yAxisLabel(self, text):
    raise NotImplementedError()


class Pie(DC):
  chartFnc = "PieChart"

  def slicesCap(self, value):
    """   

    Related Pages:

      https://github.com/dc-js/dc.js/blob/master/web-src/examples/pie.html

    :param value:
    """
    return self.fnc("slicesCap(%s)" % JsUtils.jsConvertData(value, None))

  def innerRadius(self, value):
    """   

    Related Pages:

      https://github.com/dc-js/dc.js/blob/master/web-src/examples/pie.html

    :param value:
    """
    return self.fnc("innerRadius(%s)" % JsUtils.jsConvertData(value, None))

  def legend(self):
    pass

  def drawPaths(self, flag):
    """   

    Related Pages:

      https://github.com/dc-js/dc.js/blob/master/web-src/examples/pie-external-labels.html

    :param flag:
    """
    return self.fnc("drawPaths(%s)" % JsUtils.jsConvertData(flag, None))

  def externalLabels(self, size):
    """   

    Related Pages:

      https://github.com/dc-js/dc.js/blob/master/web-src/examples/pie-external-labels.html

    :param size:
    """
    return self.fnc("externalLabels(%s)" % JsUtils.jsConvertData(size, None))

  def externalRadiusPadding(self, size):
    """   

    Related Pages:

      https://github.com/dc-js/dc.js/blob/master/web-src/examples/pie-external-labels.html

    :param size:
    """
    return self.fnc("externalRadiusPadding(%s)" % JsUtils.jsConvertData(size, None))


class Series(DC):
  chartFnc = "SeriesChart"

  def line(self):
    self._sub_chart = Line(page=self.page, set_var=False, component=self.component)
    self._sub_chart._selector = "new dc.LineChart(c)"
    return self

  def scatter(self):
    self._sub_chart = Scatter(page=self.page, set_var=False, component=self.component)
    self._sub_chart._selector = "new dc.ScatterPlot(c)"
    return self

  def bubble(self):
    self._sub_chart = Bubble(page=self.page, set_var=False, component=self.component)
    self._sub_chart._selector = "new dc.BubbleChart(c)"
    return self

  def bar(self):
    self._sub_chart = Bar(page=self.page, set_var=False, component=self.component)
    self._sub_chart._selector = "new dc.BarChart(c)"
    return self

  def seriesAccessor(self, js_funcs, profile=False):
    """   

    :param js_funcs:
    :param profile:
    """
    return self.fnc("seriesAccessor(function(d) {%s; })" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile))

  def seriesAccessorByKey(self, index=None, str_format=None):
    """   

    :param index:
    :param str_format:
    """
    if str_format is not None:
      key = str_format % ("d.key[%s]" % index)
      return self.fnc("seriesAccessor(function(d) {return %s; })" % key)

    if index is None:
      return self.fnc("seriesAccessor(function(d) { return d.key; })")

    return self.fnc("seriesAccessor(function(d) { return d.key[%s]; })" % JsUtils.jsConvertData(index, None))

  def keyAccessor(self, index=None):
    if index is None:
      return self.fnc("keyAccessor(function(d) {return +d.key; })")

    return self.fnc("keyAccessor(function(d) {return +d.key[%s]; })" % index)

  def valueAccessor(self):
    return self.fnc("valueAccessor(function(d) {return d.value; })")

  def elasticY(self, flag):
    """   

    :param flag:
    """
    return self.fnc("elasticY(%s)" % JsUtils.jsConvertData(flag, None))

  def mouseZoomable(self, flag):
    """   

    :param flag:
    """
    return self.fnc("mouseZoomable(%s)" % JsUtils.jsConvertData(flag, None))

  def shareTitle(self, flag):
    """   

    :param flag:
    """
    return self.fnc("shareTitle(%s)" % JsUtils.jsConvertData(flag, None))

  def controlsUseVisibility(self, flag):
    """   

    Related Pages:

      https://dc-js.github.io/dc.js/examples/bar-single-select.html

    :param flag:
    """
    return self.fnc("controlsUseVisibility(%s)" % JsUtils.jsConvertData(flag, None))

  def singleSelection(self):
    self.xUnitsOridinal()
    self.scaleBand()
    return self.fnc("addFilterHandler(function(filters, filter) {return [filter]; })")

  def xUnitsOridinal(self):
    return self.fnc("xUnits(dc.units.ordinal)")

  def scaleBand(self):
    return self.fnc("x(d3.scaleBand())")

  def renderArea(self, flag):
    """   

    :param flag:
    """
    return self.fnc("renderArea(%s)" % JsUtils.jsConvertData(flag, None))


class Scatter(DC):
  chartFnc = "ScatterPlot"

  def radiusValueAccessorByKey(self, index=None, str_format=None):
    """   

    :param index:
    :param str_format:
    """
    if str_format is not None:
      key = str_format % ("d.key[%s]" % index)
      return self.fnc("radiusValueAccessor(function(d) {return %s; })" % key)

    if index is None:
      return self.fnc("radiusValueAccessor(function(d) { return d.key; })")

    return self.fnc("radiusValueAccessor(function(d) { return d.key[%s]; })" % JsUtils.jsConvertData(index, None))

  def elasticX(self, flag):
    """   

    Related Pages:

      https://github.com/dc-js/dc.js/blob/master/web-src/examples/splom.html

    :param flag:
    """
    return self.fnc("elasticX(%s)" % JsUtils.jsConvertData(flag, None))

  def excludedOpacity(self, value):
    """   

    Related Pages:

      https://github.com/dc-js/dc.js/blob/master/web-src/examples/scatter-brushing.html

    :param value:
    """
    return self.fnc("excludedOpacity(%s)" % JsUtils.jsConvertData(value, None))

  def excludedColor(self, color):
    """   

    Related Pages:

      https://github.com/dc-js/dc.js/blob/master/web-src/examples/scatter-brushing.html

    :param color:
    """
    return self.fnc("excludedColor(%s)" % JsUtils.jsConvertData(color, None))

  def symbolSize(self, size):
    """   

    Related Pages:

      https://github.com/dc-js/dc.js/blob/master/web-src/examples/scatter-brushing.html

    :param size:
    """
    return self.fnc("symbolSize(%s)" % JsUtils.jsConvertData(size, None))

  def clipPadding(self, value):
    """   

    :param value:
    """
    return self.fnc("clipPadding(%s)" % JsUtils.jsConvertData(value, None))


class Bubble(Scatter):
  chartFnc = "BubbleChart"

  def keyAccessor(self, index=None):
    """   

    :param index:
    """
    if index is None:
      return self.fnc("keyAccessor(function(d) {return +d.key; })")

    return self.fnc("keyAccessor(function(d) {return +d.key[%s]; })" % index)

  def radiusValueAccessorByKey(self, index=None, str_format=None, statc_factor=None):
    """   

    :param index:
    :param str_format:
    """
    if str_format is not None:
      key = str_format % ("d.key[%s]" % index)
      return self.fnc("radiusValueAccessor(function(d) {return %s; })" % key)

    str_k = "d.key" if index is None else "d.key[%s]" % JsUtils.jsConvertData(index, None)
    if statc_factor is not None:
      str_k = "%s %s" % (str_k, statc_factor)

    return self.fnc("radiusValueAccessor(function(d) { return %s; })" % str_k)


class Sunburst(DC):
  chartFnc = "SunburstChart"

  def innerRadius(self, value):
    """   

    Related Pages:

      https://github.com/dc-js/dc.js/blob/master/web-src/examples/sunburst-equal-radii.html

    :param value:
    """
    return self.fnc("innerRadius(%s)" % JsUtils.jsConvertData(value, None))

  def ringSizes(self, js_func):
    """   

    Related Pages:

      https://github.com/dc-js/dc.js/blob/master/web-src/examples/sunburst-equal-radii.html

    :param js_func:
    """
    return self.fnc("ringSizes(%s)" % js_func)

  def equalRingSizes(self):
    """   

    Related Pages:

      https://github.com/dc-js/dc.js/blob/master/web-src/examples/sunburst-equal-radii.html
    """
    return self.fnc("ringSizes(%s.equalRingSizes())" % self.varId)


class Composite(DC):
  chartFnc = "CompositeChart"

  def x(self):
    pass

  def xUnits(self):
    """   

    Related Pages:

      https://github.com/dc-js/dc.js/blob/master/web-src/examples/pareto-chart.html
    """
    pass

  def elasticY(self, flag):
    """   

    :param flag:
    """
    return self.fnc("elasticY(%s)" % JsUtils.jsConvertData(flag, None))

  def renderHorizontalGridLines(self, flag):
    """   

    Related Pages:

      https://github.com/dc-js/dc.js/blob/master/web-src/examples/composite-bar-line.html

    :param flag:
    """
    return self.fnc("renderHorizontalGridLines(%s)" % JsUtils.jsConvertData(flag, None))

  def compose(self, dc_charts):
    pass


class BoxPlot(DC):
  chartFnc = "BoxPlot"

  def elasticY(self, flag):
    """   

    Related Pages:

      https://github.com/dc-js/dc.js/blob/master/web-src/examples/boxplot-basic.html

    :param flag:
    """
    return self.fnc("elasticY(%s)" % JsUtils.jsConvertData(flag, None))

  def elasticX(self, flag):
    """   

    Related Pages:

      https://github.com/dc-js/dc.js/blob/master/web-src/examples/boxplot-basic.html

    :param flag:
    """
    return self.fnc("elasticX(%s)" % JsUtils.jsConvertData(flag, None))


class GeoChoropleth(DC):
  chartFnc = "GeoChoroplethChart"
