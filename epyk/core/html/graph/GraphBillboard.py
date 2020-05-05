'''
Module used as a wrapper to the Javascript C3 libraries

Related Pages:

		https://c3js.org/gettingstarted.html
  http://c3js.org/
This module is defined by a main class ** Chart **.

The constructor ::__init__
::onDocumentLoadVar
::onDocumentReady


Python / Javascript Events
::click
::mouseover
::mouseout


Pure Javascript Wrapper
Those function will be only used in **Javascript called** and they will return a piece of string which will be added in the
report to get the data later on in the Javascript layer. Python is just used here to put all the pieces together

The method to destroy the C3 chart ::jsDestroy
The method to group the different charts ::jsGroups

'''


from epyk.core.data import DataClass

from epyk.core.html import Html

from epyk.core.js.primitives import JsObjects
from epyk.core.js import JsUtils

from epyk.core.js.packages import JsD3


class Chart(Html.Html):
  name, category, callFnc = 'Billboard', 'Charts', 'Billboard'

  def __init__(self, report, width, height, htmlCode, options, profile):
    self.height = height[0]
    super(Chart, self).__init__(report, [], code=htmlCode, css_attrs={"width": width, "height": height},
                                profile=profile)
    self._d3, self._datasets, self._options, self._data_attrs, self._attrs = None, [], None, {}, {}
    self._options_init = options
    self.style.css.margin_top = 10

  @property
  def chartId(self):
    """
    Return the Javascript variable of the chart
    """
    return "%s_obj" % self.htmlId

  def click(self, jsFncs, profile=False):
    self.data.onclick(jsFncs, profile)
    return self

  @property
  def d3(self):
    if self._d3 is None:
      self._d3 = JsD3.D3Select(self._report, selector="d3.select('#%s')" % self.htmlId, setVar=False)
    return self._d3

  def build(self, data=None, options=None, profile=False):
    return '%s = bb.generate(%s)' % (self.chartId, self.getCtx())

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '<div %s></div>' % self.get_attrs(pyClassNames=self.style.get_classes())


class JsTick(DataClass):

  @property
  def format(self):
    return self._attrs["format"]

  @format.setter
  def format(self, val):
    self._attrs["format"] = val


class BBAxis(DataClass):

  @property
  def type(self):
    return self._attrs["type"]

  @type.setter
  def type(self, val):
    self._attrs["type"] = val

  @property
  def show(self):
    return self._attrs["show"]

  @show.setter
  def show(self, val):
    self._attrs["show"] = val

  @property
  def tick(self):
    return self.sub_data("x", JsTick)


class BBSelection(DataClass):
  @property
  def enabled(self):
    """
    Set data selection enabled.

    If this option is set true, we can select the data points and get/set its state of selection by API (e.g. select, unselect, selected).

    https://c3js.org/reference.html#data-selection-enabled
    """
    return self._attrs["enabled"]

  @enabled.setter
  def enabled(self, val):
    self._attrs["enabled"] = val

  @property
  def grouped(self):
    """
    """
    return self._attrs["grouped"]

  @grouped.setter
  def grouped(self, val):
    self._attrs["grouped"] = val

  @property
  def multiple(self):
    """
    """
    return self._attrs["multiple"]

  @multiple.setter
  def multiple(self, val):
    self._attrs["multiple"] = val

  @property
  def draggable(self):
    """
    """
    return self._attrs["draggable"]

  @draggable.setter
  def draggable(self, val):
    self._attrs["draggable"] = val

  @property
  def isselectable(self):
    """
    """
    return self._attrs["isselectable"]

  @isselectable.setter
  def isselectable(self, jsFnc):
    self._attrs["isselectable"] = jsFnc


class JsData(DataClass):
  @property
  def x(self):
    return self._attrs["x"]

  @x.setter
  def x(self, val):
    self._attrs["x"] = val

  @property
  def xs(self): return self._attrs["xs"]

  @xs.setter
  def xs(self, val): self._attrs["xs"] = val

  @property
  def xFormat(self): return self._attrs["xFormat"]

  @xFormat.setter
  def xFormat(self, val): self._attrs["xFormat"] = val

  @property
  def names(self): return self._attrs["names"]

  @names.setter
  def names(self, val): self._attrs["names"] = val

  @property
  def groups(self): return self._attrs["groups"]

  @groups.setter
  def groups(self, val): self._attrs["groups"] = val

  @property
  def axes(self): return self._attrs["axes"]

  @axes.setter
  def axes(self, val): self._attrs["axes"] = val

  @property
  def type(self): return self._attrs["type"]

  @type.setter
  def type(self, val): self._attrs["type"] = val

  def add_type(self, alias, type):
    if "types" not in self._attrs:
      self.types = {}
    self.types[alias] = type
    return self

  @property
  def types(self):
    """
    This setting overwrites data.type setting:
    line, spline, step, area...

    https://c3js.org/reference.html#data-types
    """
    return self._attrs["types"]

  @types.setter
  def types(self, val): self._attrs["types"] = val

  @property
  def labels(self): return self._attrs["labels"]

  @labels.setter
  def labels(self, val): self._attrs["labels"] = val

  @property
  def order(self): return self._attrs["order"]

  @order.setter
  def order(self, val): self._attrs["order"] = val

  @property
  def colors(self):
    if "colors" not in self._attrs:
      self._attrs["colors"] = {}
    return self._attrs["colors"]

  @colors.setter
  def colors(self, val): self._attrs["colors"] = val

  @property
  def columns(self):
    if 'columns' not in self._attrs:
      self._attrs["columns"] = []
    return self._attrs["columns"]

  @columns.setter
  def columns(self, val): self._attrs["columns"] = val

  @property
  def hide(self): return self._attrs["hide"]

  @hide.setter
  def hide(self, val): self._attrs["hide"] = val

  @property
  def selection(self):
    return self.sub_data("selection", BBSelection)

  def onclick(self, jsFncs, profile=False):
    self._attrs["onclick"] = JsObjects.JsObject.JsObject("function () { %s }" % JsUtils.jsConvertFncs(jsFncs, toStr=True))


class JsScales(DataClass):

  @property
  def rotated(self):
    return self._attrs["rotated"]

  @rotated.setter
  def rotated(self, val):
    self._attrs["rotated"] = val

  @property
  def x(self):
    return self.sub_data("x", BBAxis)

  @property
  def y(self):
    return self.sub_data("y", BBAxis)

  @property
  def y2(self):
    """

    https://c3js.org/reference.html#axis-y2-show

    :rtype: C3Axis
    """
    return self.sub_data("y2", BBAxis)


class BBGridLine(DataClass):
  @property
  def value(self):
    return self._attrs["value"]

  @value.setter
  def value(self, val):
    self._attrs["value"] = val

  @property
  def text(self):
    return self._attrs["text"]

  @text.setter
  def text(self, val):
    self._attrs["text"] = val

  @property
  def css_class(self):
    return self._attrs["class"]

  @css_class.setter
  def css_class(self, val):
    self._attrs["class"] = val

  @property
  def position(self):
    return self._attrs["position"]

  @position.setter
  def position(self, val):
    self._attrs["position"] = val


class C3GridAxis(DataClass):

  @property
  def show(self):
    return self._attrs["show"]

  @show.setter
  def show(self, val):
    self._attrs["show"] = val

  @property
  def lines(self):
    return self.sub_data_enum("lines", BBGridLine)


class BBGrid(DataClass):

  @property
  def x(self):
    return self.sub_data("x", C3GridAxis)

  @property
  def y(self):
    return self.sub_data("y", C3GridAxis)


class JsLegend(DataClass):
  pass


class JsTooltip(DataClass):
  pass


class JsSubchart(DataClass):
  pass


class JsZoom(DataClass):
  @property
  def enabled(self):
    return self._attrs["enabled"]

  @enabled.setter
  def enabled(self, val):
    self._attrs["enabled"] = val

  @property
  def type(self):
    return self._attrs["type"]

  @type.setter
  def type(self, val):
    self._attrs["type"] = val

  @property
  def rescale(self):
    return self._attrs["rescale"]

  @rescale.setter
  def rescale(self, val):
    self._attrs["rescale"] = val

  @property
  def extent(self):
    return self._attrs["extent"]

  @extent.setter
  def extent(self, val):
    self._attrs["extent"] = val


class BBPoints(DataClass):

  @property
  def show(self):
    return self._attrs["show"]

  @show.setter
  def show(self, val):
    self._attrs["show"] = val

  @property
  def r(self):
    return self._attrs["r"]

  @r.setter
  def r(self, val):
    self._attrs["r"] = val

  @property
  def focus(self):
    return self._attrs["focus"]

  @focus.setter
  def focus(self, val):
    self._attrs["focus"] = {"expand": val, 'enabled': True}

  @property
  def select(self):
    return self._attrs["select"]

  @select.setter
  def select(self, val):
    self._attrs["select"] = val


class ChartLine(Chart):
  __reqJs, __reqCss = ['billboard'], ['billboard']
  _type = 'line'

  def __init__(self, report, width, height, htmlCode, options, profile):
    super(ChartLine, self).__init__(report, width, height, htmlCode, options, profile)
    self._attrs["bindto"] = "#%s" % self.htmlId

  def labels(self, labels, series_id='x'):
    self.data.x = series_id
    self.data.columns.append([series_id] + labels)

  def add_dataset(self, name, data, type=None):
    self.data.columns.append([name] + data)
    self.data.colors[name] = self._report.theme.colors[len(self.data.colors)]
    if type is None:
      self.data.add_type(name, self._type)
    return self._attrs

  @property
  def axis(self):
    """

    :rtype: JsScales
    :return:
    """
    if not'axis' in self._attrs:
      self._attrs['axis'] = JsScales(self._report)
    return self._attrs['axis']

  @property
  def point(self):
    """

    :rtype: C3Points
    """
    if not 'point' in self._attrs:
      self._attrs['point'] = BBPoints(self._report)
    return self._attrs['point']

  @property
  def zoom(self):
    """

    :rtype: JsZoom
    """
    if not 'zoom' in self._attrs:
      self._attrs['zoom'] = JsZoom(self._report)
    return self._attrs['zoom']

  @property
  def data(self):
    """

    :rtype: JsScales
    :return:
    """
    if not 'data' in self._attrs:
      self._attrs['data'] = JsData(self._report)
    return self._attrs['data']

  @property
  def grid(self):
    """

    :rtype: JsScales
    :return:
    """
    if not 'grid' in self._attrs:
      self._attrs['grid'] = BBGrid(self._report)
    return self._attrs['grid']

  def getCtx(self):
    str_ctx = "{%s}" % ", ".join(["%s: %s" % (k, JsUtils.jsConvertData(v, None)) for k, v in self._attrs.items()])
    return str_ctx


class ChartSpline(ChartLine):
  __reqJs, __reqCss = ['billboard'], ['billboard']
  _type = 'spline'


class ChartArea(ChartLine):
  __reqJs, __reqCss = ['billboard'], ['billboard']
  _type = 'area'


class ChartBar(ChartLine):
  __reqJs, __reqCss = ['billboard'], ['billboard']
  _type = 'bar'


class ChartScatter(ChartLine):
  __reqJs, __reqCss = ['billboard'], ['billboard']
  _type = 'scatter'


class ChartPie(ChartLine):
  __reqJs, __reqCss = ['billboard'], ['billboard']
  _type = 'pie'

  def add_dataset(self, name, value, type=None):
    self.data.columns.append([name, value])
    if type is None:
      self.data.add_type(name, self._type)
    return self._attrs


class ChartDonut(ChartPie):
  __reqJs, __reqCss = ['billboard'], ['billboard']
  _type = 'donut'


class ChartGauge(ChartPie):
  __reqJs, __reqCss = ['billboard'], ['billboard']
  _type = 'gauge'


class ChartBubble(ChartLine):
  __reqJs, __reqCss = ['billboard'], ['billboard']
  _type = 'bubble'

  def add_dataset(self, name, data, type=None):
    self.data.columns.append([name] + data)
    if type is None:
      self.data.type = self._type
    return self._attrs


class ChartRadar(ChartLine):
  __reqJs, __reqCss = ['billboard'], ['billboard']
  _type = 'radar'

  def add_dataset(self, name, data, type=None):
    self.data.columns.append([name] + data)
    if type is None:
      self.data.type = self._type
    return self._attrs
