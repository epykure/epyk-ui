
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

  def build(self, data=None, options=None, profile=False):
    return '''%s; var %s = %s''' % (self.groups.toStr(), self.chartId, self.getCtx())

  def getCtx(self):
    raise Exception("")

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '<div %s></div>' % self.get_attrs(pyClassNames=self.style.get_classes())


class ChartLine(Chart):
  __reqJs, __reqCss = ['vis'], ['vis']

  def __init__(self, report, width, height, htmlCode, options, profile):
    super(ChartLine, self).__init__(report, width, height, htmlCode, options, profile)
    self.items, self.__grps = [], None
    self.options.style = "line"

  @property
  def js(self):
    """
    Javascript base function

    Return all the Javascript functions defined in the framework.
    THis is an entry point to the full Javascript ecosystem.

    :return: A Javascript object
    :rtype: Js.JsBase
    """
    if self._js is None:
      self._js = JsVis.VisTimeline(self._report, varName=self.chartId)
    return self._js

  @property
  def groups(self):
    """

    :return:
    """
    if self.__grps is None:
      self.__grps = JsVis.VisGroups(self._report, setVar=True, varName="%s_group" % self.chartId)
    return self.__grps

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

  def add_items(self, records):
    for rec in records:
      self.add_item(rec['x'], rec['y'], rec.get('group', 0))
    return self

  def getCtx(self):
    print(self.options)
    return "new vis.Graph2d(%s, %s, %s, %s)" % (self.dom.varId, self.items, self.groups.varId, self.options)


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


class ChartNetwork(Chart):
  __reqJs, __reqCss = ['vis'], ['vis']

  def __init__(self, report, width, height, htmlCode, options, profile):
    super(ChartNetwork, self).__init__(report, width, height, htmlCode, options, profile)
    self.items, self.__grps = [], None

  @property
  def options(self):
    """

    :rtype: Options2D
    """
    if self._options is None:
      self._options = OptVis.OptionsNetwork(self._report, attrs=self._options_init)
    return self._options

  @property
  def js(self):
    """
    Javascript base function

    Return all the Javascript functions defined in the framework.
    THis is an entry point to the full Javascript ecosystem.

    :return: A Javascript object
    :rtype: Js.JsBase
    """
    if self._js is None:
      self._js = JsVis.VisNetwork(self._report, varName=self.chartId)
    return self._js

  def add_node(self, label, id=None):
    pass

  def add_edge(self, fromId, toId, title=None, relation=None):
    pass

  def getCtx(self):
    return "new vis.Network(%s, %s, %s, %s)" % (self.dom.varId, self.items, self.groups.varId, self.options)


class ChartTimeline(Chart):
  __reqJs, __reqCss = ['vis'], ['vis']

  def __init__(self, report, width, height, htmlCode, options, profile):
    super(ChartTimeline, self).__init__(report, width, height, htmlCode, options, profile)
    self.items, self.__grps = [], None

  @property
  def options(self):
    """

    :rtype: Options2D
    """
    if self._options is None:
      self._options = OptVis.OptionsTimeline(self._report, attrs=self._options_init)
    return self._options

  @property
  def js(self):
    """
    Javascript base function

    Return all the Javascript functions defined in the framework.
    THis is an entry point to the full Javascript ecosystem.

    :return: A Javascript object
    :rtype: Js.JsBase
    """
    if self._js is None:
      self._js = JsVis.VisTimeline(self._report, varName=self.chartId)
    return self._js

  @property
  def groups(self):
    """

    :return:
    """
    if self.__grps is None:
      self.__grps = JsVis.VisGroups(self._report, setVar=True, varName="%s_group" % self.chartId)
    return self.__grps

  def add_item(self, start, content, style=None, end=None):
    """

    :param start:
    :param content:
    :param group:
    :param label:
    :param end:
    """
    self.items.append({"start": start, "content": "ok", "group": 0})
    return self

  def add_items(self, records):
    for rec in records:
      self.add_item(rec['x'], rec['y'], rec.get('group', 0))
    return self

  def getCtx(self):
    return "new vis.Timeline(%s, %s, %s, %s)" % (self.dom.varId, self.items, self.groups.varId, self.options)
