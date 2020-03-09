
from epyk.core.html import Html
from epyk.core.html.options import OptVis

from epyk.core.js import JsUtils
from epyk.core.js.packages import JsVis


class Chart(Html.Html):
  name, category, callFnc = 'Vis', 'Charts', 'vis'

  def __init__(self, report, width, height, htmlCode, options, profile):
    self.height = height[0]
    super(Chart, self).__init__(report, [], code=htmlCode, css_attrs={"width": width, "height": height}, profile=profile)
    self._d3, self._datasets, self._options, self._data_attrs, self._attrs = None, [], None, {}, {}
    self._options_init = options
    self.style.css.margin_top = 10

  @property
  def chartId(self):
    """
    Return the Javascript variable of the chart
    """
    return "%s_obj" % self.htmlId

  @property
  def options(self):
    """

    :rtype: Options2D
    """
    if self._options is None:
      self._options = OptVis.Options2D(self._report, attrs=self._options_init)
    return self._options

  @property
  def _js__builder__(self):
    return '''%s = %s''' % (self.chartId, self.getCtx())

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '<div %s></div>' % self.get_attrs(pyClassNames=self.style.get_classes())


class VisGroups(object):

  def add(self, id, content):
    content = JsUtils.jsConvertData(content, None)
    self._js.append("groups.add({id: %s, content: %s})" % (id, content))


class VsDataSet(object):
  pass


class ChartLine(Chart):
  __reqJs, __reqCss = ['vis'], ['vis']

  def __init__(self, report, width, height, htmlCode, options, profile):
    super(ChartLine, self).__init__(report, width, height, htmlCode, options, profile)
    self.items = []
    self.options.style = "line"

  @property
  def dom(self):
    """

    :rtype: JsCanvas.Canvas
    """
    if self._dom is None:
      self._dom = JsVis.VisTimeline(self, report=self._report)
    return self._dom

  @property
  def groups(self):
    """

    :return:
    """
    return VisGroups(self._report)

  def add_item(self, x, y, group, label=None, end=None):
    """

    :param x:
    :param y:
    :param group:
    :param label:
    :param end:
    """
    self.items.append({"x": x, "y": y, "group": group})
    return self

  def getCtx(self):
    return "new vis.Graph2d(%s, items, groups, options)" % self.dom.varId


class Chart3D(Chart):
  __reqJs, __reqCss = ['vis'], ['vis']

  def __init__(self, report, width, height, htmlCode, options, profile):
    super(Chart3D, self).__init__(report, width, height, htmlCode, options, profile)
    self.items = []
    self.options.style = "line"

  @property
  def options(self):
    """

    :rtype: Options3D
    """
    if self._options is None:
      self._options = OptVis.Options3D(self._report, attrs=self._options_init)
    return self._options

  @property
  def dom(self):
    """

    :rtype: JsCanvas.Canvas
    """
    if self._dom is None:
      self._dom = JsVis.VisGraph3D(self, report=self._report)
    return self._dom

  def add_item(self, x, y, z, style=None):
    """

    :param x:
    :param y:
    :param z:
    :param style:
    """
    self.items.append({"x": x, "y": y, "z": z})
    return self

  def getCtx(self):
    return "new vis.Graph3d(%s, data, options)" % self.dom.varId
