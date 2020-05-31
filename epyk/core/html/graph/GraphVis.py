
from epyk.core.html import Html
from epyk.core.html.options import OptVis

from epyk.core.js import JsUtils
from epyk.core.js.packages import JsVis


class Chart(Html.Html):
  name = 'Vis'
  requirements = ('vis', )

  def __init__(self, report, width, height, htmlCode, options, profile):
    self.height = height[0]
    super(Chart, self).__init__(report, [], htmlCode=htmlCode, css_attrs={"width": width, "height": height}, profile=profile)
    self._d3, self._datasets, self._options, self._data_attrs, self._attrs = None, [], None, {}, {}
    self._options_init = options
    self.style.css.margin_top = 10
    self.style.css.display = "inline-block"

  @property
  def chartId(self):
    """
    Return the Javascript variable of the chart
    """
    return "%s_obj" % self.htmlId

  @property
  def options(self):
    """

    :rtype: OptVis.Options2D
    """
    if self._options is None:
      self._options = OptVis.Options2D(self._report, attrs=self._options_init)
    return self._options

  @property
  def js(self):
    """
    Description:
    -----------
    Javascript base function

    Return all the Javascript functions defined in the framework.
    THis is an entry point to the full Javascript ecosystem.

    :return: A Javascript object

    :rtype: JsVis.VisGraph2D
    """
    if self._js is None:
      self._js = JsVis.VisGraph2D(selector="window['%s']" % self.chartId, src=self)
    return self._js

  def build(self, data=None, options=None, profile=False):
    if data:
      return JsUtils.jsConvertFncs([self.js.setItems(data[0]), self.js.redraw()], toStr=True)

    return '''%s; var %s = %s''' % (self.groups.toStr(), self.chartId, self.getCtx())

  def getCtx(self):
    raise Exception("Cannot create an object from the Vis base class directly")

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
    Description:
    -----------
    Javascript base function

    Return all the Javascript functions defined in the framework.
    THis is an entry point to the full Javascript ecosystem.

    :return: A Javascript object

    :rtype: JsVis.VisGraph2D
    """
    if self._js is None:
      self._js = JsVis.VisGraph2D(selector="window['%s']" % self.chartId, src=self)
    return self._js

  @property
  def groups(self):
    """

    :rtype: JsVis.VisGroups
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
    return "new vis.Graph2d(%s, %s, %s, %s)" % (self.dom.varId, self.items, self.groups.varId, self.options)


class ChartBar(ChartLine):
  __reqJs, __reqCss = ['vis'], ['vis']

  def __init__(self, report, width, height, htmlCode, options, profile):
    super(ChartBar, self).__init__(report, width, height, htmlCode, options, profile)
    self.options.style = "bar"


class ChartScatter(ChartLine):
  __reqJs, __reqCss = ['vis'], ['vis']

  def __init__(self, report, width, height, htmlCode, options, profile):
    super(ChartScatter, self).__init__(report, width, height, htmlCode, options, profile)
    self.options.style = "points"
    self.options.drawPoints.style.circle()


class Chart3D(Chart):
  __reqJs, __reqCss = ['vis'], ['vis']

  def __init__(self, report, width, height, htmlCode, options, profile):
    super(Chart3D, self).__init__(report, width, height, htmlCode, options, profile)
    self.items, self.__grps = [], None
    self.options.style.surface()
    self.options.showPerspective = True
    self.options.showGrid = True
    self.options.keepAspectRatio = True
    self.options.verticalRatio = 0.5

  @property
  def js(self):
    """
    Description:
    -----------
    Javascript base function

    Return all the Javascript functions defined in the framework.
    THis is an entry point to the full Javascript ecosystem.

    :return: A Javascript object

    :rtype: JsVis.VisGraph2D
    """
    if self._js is None:
      self._js = JsVis.VisGraph3D(selector="window['%s']" % self.chartId, src=self)
    return self._js

  @property
  def options(self):
    """

    :rtype: OptVis.Options3D
    """
    if self._options is None:
      self._options = OptVis.Options3D(self._report, attrs=self._options_init)
    return self._options

  @property
  def groups(self):
    """

    :rtype: JsVis.VisGroups
    """
    if self.__grps is None:
      self.__grps = JsVis.VisGroups(self._report, setVar=True, varName="%s_group" % self.chartId)
    return self.__grps

  @property
  def js(self):
    """

    :rtype: JsVis.VisGraph3D
    """

    if self._js is None:
      self._js = JsVis.VisGraph3D(self._report, varName=self.chartId)
    return self._js

  def add_items(self, records):
    for rec in records:
      self.add_item(rec['x'], rec['y'], rec['z'], rec.get('group', 0))
    return self

  def add_item(self, x, y, z, group=0, style=None):
    """

    :param x:
    :param y:
    :param z:
    :param style:
    """
    self.items.append({"x": x, "y": y, "z": z, 'group': group})
    return self

  def build(self, data=None, options=None, profile=False):
    if data:
      return "%(chartId)s.setData(%(data)s); %(chartId)s.redraw()" % {'chartId': self.chartId, 'data': data[0]}

    return '''%s; var %s = %s''' % (self.groups.toStr(), self.chartId, self.getCtx())

  def getCtx(self):
    return "new vis.Graph3d(%s, %s, %s)" % (self.dom.varId, self.items, self.options)


class Chart3DScatter(Chart3D):
  __reqJs, __reqCss = ['vis'], ['vis']

  def __init__(self, report, width, height, htmlCode, options, profile):
    super(Chart3DScatter, self).__init__(report, width, height, htmlCode, options, profile)
    self.items, self.__grps = [], None
    self.options.style.dot()


class Chart3DLine(Chart3D):
  __reqJs, __reqCss = ['vis'], ['vis']

  def __init__(self, report, width, height, htmlCode, options, profile):
    super(Chart3DLine, self).__init__(report, width, height, htmlCode, options, profile)
    self.items, self.__grps = [], None
    self.options.style.line()


class Chart3DBar(Chart3D):
  __reqJs, __reqCss = ['vis'], ['vis']

  def __init__(self, report, width, height, htmlCode, options, profile):
    super(Chart3DBar, self).__init__(report, width, height, htmlCode, options, profile)
    self.items, self.__grps = [], None
    self.options.style.bar()


class ChartNetwork(Chart):
  __reqJs, __reqCss = ['vis'], ['vis']

  def __init__(self, report, width, height, htmlCode, options, profile):
    super(ChartNetwork, self).__init__(report, width, height, htmlCode, options, profile)
    self._nodes, self._edges, self.__grps = [], [], None

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
      self._js = JsVis.VisNetwork(self._report, selector=self.chartId, setVar=False)
    return self._js

  @property
  def groups(self):
    """

    :return:
    """
    if self.__grps is None:
      self.__grps = JsVis.VisGroups(self._report, setVar=True, varName="%s_group" % self.chartId)
    return self.__grps

  def add_node(self, label, id=None, group=0):
    """

    :param label:
    :param id:
    :param group:
    """
    self._nodes.append({'label': label, 'group': group, 'id': id or len(self._nodes)})
    return self

  def add_edge(self, fromId, toId, title=None, relation=None):
    self._edges.append({'from': fromId, 'to': toId})
    return self

  def getCtx(self):
    return "new vis.Network(%s, %s, %s, %s)" % (self.dom.varId, {"nodes": self._nodes, 'edges': self._edges}, self.groups.varId, self.options)


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

  def add_item(self, start, content, group=0, end=None, style=None):
    """

    :param start:
    :param content:
    :param group:
    :param end:
    """
    self.items.append({"start": start, "content": str(content), "group": group})
    return self

  def add_items(self, records):
    for rec in records:
      self.add_item(rec['x'], rec['y'], rec.get('group', rec.get("group", 0)))
    return self

  def getCtx(self):
    #return "new vis.Timeline(%s, %s, %s, %s)" % (self.dom.varId, self.items, self.groups.varId, self.options)
    return "new vis.Timeline(%s, %s, %s)" % (self.dom.varId, self.items, self.options)
