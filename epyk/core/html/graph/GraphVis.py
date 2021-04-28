#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html
from epyk.core.html.options import OptVis

from epyk.core.js import JsUtils
from epyk.core.css.styles import GrpClsCharts
from epyk.core.js.packages import JsVis


class Chart(Html.Html):
  name = 'Vis'
  requirements = ('vis', )
  _option_cls = OptVis.Options2D

  def __init__(self, report, width, height, html_code, options, profile):
    self.height = height[0]
    super(Chart, self).__init__(report, [], html_code=html_code, profile=profile, options=options,
                                css_attrs={"width": width, "height": height})
    self._d3, self._datasets, self._options, self._data_attrs, self._attrs = None, [], None, {}, {}
    self.style.css.margin_top = 10
    self.style.css.display = "inline-block"

  @property
  def chartId(self):
    """
    Description:
    -----------
    Return the Javascript variable of the chart.

    Usage::

    """
    return "%s_obj" % self.htmlCode

  @property
  def options(self):
    """
    Description:
    -----------

    Usage::

    :rtype: OptVis.Options2D
    """
    return super().options

  @property
  def js(self):
    """
    Description:
    -----------
    Return all the Javascript functions defined in the framework.
    THis is an entry point to the full Javascript ecosystem.

    Usage::

    :return: A Javascript object

    :rtype: JsVis.VisGraph2D
    """
    if self._js is None:
      self._js = JsVis.VisGraph2D(selector="window['%s']" % self.chartId, src=self)
    return self._js

  def build(self, data=None, options=None, profile=False, component_id=None):
    """
    Description:
    -----------

    Usage::

    Attributes:
    ----------
    :param data: String. A String corresponding to a JavaScript object.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param component_id: String. Optional.
    """
    profile = self.with_profile(profile, event="Builder", element_id=self.chartId)
    if data:
      return JsUtils.jsConvertFncs([self.js.setItems(data[0]), self.js.redraw()], toStr=True, profile=profile)

    return JsUtils.jsConvertFncs(
      [self.groups.toStr(), "var %s = %s" % (self.chartId, self.getCtx())], toStr=True, profile=profile)

  def getCtx(self):
    """


    """
    raise Exception("Cannot create an object from the Vis base class directly")

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    return '<div %s></div>' % self.get_attrs(pyClassNames=self.style.get_classes())


class ChartLine(Chart):

  def __init__(self, report, width, height, html_code, options, profile):
    super(ChartLine, self).__init__(report, width, height, html_code, options, profile)
    self.items, self.__grps = [], None
    self.options.style = "line"

  @property
  def js(self):
    """
    Description:
    -----------
    Return all the Javascript functions defined in the framework.
    THis is an entry point to the full Javascript ecosystem.

    Usage::

    :return: A Javascript object

    :rtype: JsVis.VisGraph2D
    """
    if self._js is None:
      self._js = JsVis.VisGraph2D(selector="window['%s']" % self.chartId, src=self)
    return self._js

  @property
  def groups(self):
    """
    Description:
    -----------

    Usage::

    :rtype: JsVis.VisGroups
    """
    if self.__grps is None:
      self.__grps = JsVis.VisGroups(self._report, setVar=True, varName="%s_group" % self.chartId)
    return self.__grps

  def add_item(self, x, y, group, label=None, end=None):
    """
    Description:
    -----------

    Usage::

    Attributes:
    ----------
    :param x:
    :param y:
    :param group:
    :param label:
    :param end:
    """
    self.items.append({"x": x, "y": y, "group": group})
    return self

  def add_items(self, records):
    """
    Description:
    -----------

    Usage::

    Attributes:
    ----------
    :param records:
    """
    for rec in records:
      self.add_item(rec['x'], rec['y'], rec.get('group', 0))
    return self

  def getCtx(self):
    """
    Description:
    ------------

    Usage::

    """
    return "new vis.Graph2d(%s, %s, %s, %s)" % (self.dom.varId, self.items, self.groups.varId, self.options)


class ChartBar(ChartLine):

  def __init__(self, report, width, height, html_code, options, profile):
    super(ChartBar, self).__init__(report, width, height, html_code, options, profile)
    self.options.style = "bar"


class ChartScatter(ChartLine):

  def __init__(self, report, width, height, html_code, options, profile):
    super(ChartScatter, self).__init__(report, width, height, html_code, options, profile)
    self.options.style = "points"
    self.options.drawPoints.style.circle()


class Chart3D(Chart):
  _option_cls = OptVis.Options3D

  def __init__(self, report, width, height, html_code, options, profile):
    super(Chart3D, self).__init__(report, width, height, html_code, options, profile)
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
    Return all the Javascript functions defined in the framework.
    THis is an entry point to the full Javascript ecosystem.

    Usage::

    :rtype: JsVis.VisGraph3D
    """
    if self._js is None:
      self._js = JsVis.VisGraph3D(self._report, varName=self.chartId)
    return self._js

  @property
  def options(self):
    """
    Description:
    -----------
    Property to the component options.
    Options can either impact the Python side or the Javascript builder.

    Python can pass some options to the JavaScript layer.

    Usage::

    :rtype: OptVis.Options3D
    """
    return super().options

  @property
  def groups(self):
    """
    Description:
    -----------

    Usage::

    :rtype: JsVis.VisGroups
    """
    if self.__grps is None:
      self.__grps = JsVis.VisGroups(self._report, setVar=True, varName="%s_group" % self.chartId)
    return self.__grps

  def add_items(self, records):
    """
    Description:
    -----------

    Usage::

    Attributes:
    ----------
    :param records:
    """
    for rec in records:
      self.add_item(rec['x'], rec['y'], rec['z'], rec.get('group', 0))
    return self

  def add_item(self, x, y, z, group=0, style=None):
    """
    Description:
    -----------

    Usage::

    Attributes:
    ----------
    :param x:
    :param y:
    :param z:
    :param group:
    :param style:
    """
    self.items.append({"x": x, "y": y, "z": z, 'group': group})
    return self

  def build(self, data=None, options=None, profile=False, component_id=None):
    """
    Description:
    -----------

    Usage::

    Attributes:
    ----------
    :param data:
    :param options:
    :param profile:
    :param component_id: String. Optional.
    """
    if data:
      return "%(chartId)s.setData(%(data)s); %(chartId)s.redraw()" % {'chartId': self.chartId, 'data': data[0]}

    return '''%s; var %s = %s''' % (self.groups.toStr(), self.chartId, self.getCtx())

  def getCtx(self):
    """
    Description:
    ------------

    Usage::

    """
    return "new vis.Graph3d(%s, %s, %s)" % (self.dom.varId, self.items, self.options)


class Chart3DScatter(Chart3D):

  def __init__(self, report, width, height, html_code, options, profile):
    super(Chart3DScatter, self).__init__(report, width, height, html_code, options, profile)
    self.items, self.__grps = [], None
    self.options.style.dot()


class Chart3DLine(Chart3D):

  def __init__(self, report, width, height, html_code, options, profile):
    super(Chart3DLine, self).__init__(report, width, height, html_code, options, profile)
    self.items, self.__grps = [], None
    self.options.style.line()


class Chart3DBar(Chart3D):

  def __init__(self, report, width, height, html_code, options, profile):
    super(Chart3DBar, self).__init__(report, width, height, html_code, options, profile)
    self.items, self.__grps = [], None
    self.options.style.bar()


class ChartNetwork(Chart):
  _option_cls = OptVis.OptionsNetwork

  def __init__(self, report, width, height, html_code, options, profile):
    super(ChartNetwork, self).__init__(report, width, height, html_code, options, profile)
    self._nodes, self._edges, self.__grps = [], [], None

  @property
  def options(self):
    """
    Description:
    ------------

    Usage::

    :rtype: OptVis.OptionsNetwork
    """
    return super().options

  @property
  def js(self):
    """
    Description:
    ------------
    Return all the Javascript functions defined in the framework.
    This is an entry point to the full Javascript ecosystem.

    Usage::

    :return: A Javascript object.

    :rtype: JsVis.VisNetwork
    """
    if self._js is None:
      self._js = JsVis.VisNetwork(self._report, selector=self.chartId, setVar=False)
    return self._js

  @property
  def groups(self):
    """
    Description:
    ------------

    Usage::

    :rtype: JsVis.VisGroups
    """
    if self.__grps is None:
      self.__grps = JsVis.VisGroups(self._report, setVar=True, varName="%s_group" % self.chartId)
    return self.__grps

  def add_node(self, label, node_id=None, group=0):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param label:
    :param node_id:
    :param group:
    """
    self._nodes.append({'label': label, 'group': group, 'id': node_id or len(self._nodes)})
    return self

  def add_edge(self, from_Id, to_Id, title=None, relation=None):
    """
    Description:
    -----------

    Usage::

    Attributes:
    ----------
    :param from_Id:
    :param to_Id:
    :param title:
    :param relation:
    """
    self._edges.append({'from': from_Id, 'to': to_Id})
    return self

  def getCtx(self):
    """
    Description:
    -----------

    Usage::
    """
    return "new vis.Network(%s, %s, %s, %s)" % (
      self.dom.varId, {"nodes": self._nodes, 'edges': self._edges}, self.groups.varId, self.options)


class ChartTimeline(Chart):
  requirements = ('vis-timeline', )
  _option_cls = OptVis.OptionsTimeline

  def __init__(self, report, width, height, html_code, options, profile):
    super(ChartTimeline, self).__init__(report, width, height, html_code, options, profile)
    self.items, self.__grps, self.__cats = [], None, None

  def addClassName(self, name, css, css_hover=None):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param name:
    :param css:
    :param css_hover:
    """
    from epyk.core.css.styles.classes import CssStyle

    class CssHoverColor(CssStyle.Style):
      _attrs = css
      _hover = css_hover or []
      classname = 'vis-item.%s .vis-item-overflow' % name

    self.style.add_classes.custom(CssHoverColor)
    return self

  @property
  def style(self):
    """
    Description:
    ------------
    Property to the CSS Style of the component.

    Usage::

    :rtype: GrpClsCharts.ClassVisTimeline
    """
    if self._styleObj is None:
      self._styleObj = GrpClsCharts.ClassVisTimeline(self)
    return self._styleObj

  @property
  def options(self):
    """
    Description:
    ------------
    Property to the component options.
    Options can either impact the Python side or the Javascript builder.

    Python can pass some options to the JavaScript layer.

    Usage::

    :rtype: OptVis.OptionsTimeline
    """
    return super().options

  @property
  def js(self):
    """
    Description:
    ------------
    Return all the Javascript functions defined in the framework.
    This is an entry point to the full Javascript ecosystem.

    Usage::

    :return: A Javascript object

    :rtype: JsVis.VisTimeline
    """
    if self._js is None:
      self._js = JsVis.VisTimeline(selector=self.chartId, src=self)
    return self._js

  @property
  def groups(self):
    """
    Description:
    ------------

    Usage::

    :rtype: JsVis.VisGroups
    """
    if self.__grps is None:
      self.__grps = JsVis.VisGroups(self._report, setVar=True, varName="%s_group" % self.chartId)
    return self.__grps

  def setGroups(self, groups):
    """
    Description:
    ------------
    Add group labels to the timeline.

    Usage::

    Attributes:
    ----------
    :param groups:
    """
    self.__cats = "%s.setGroups(%s)" % (self.chartId, JsUtils.jsConvertData(groups, None))
    return self

  def add_items(self, records):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param records:
    """
    self.items.extend(records)
    return self

  def getCtx(self):
    """
    Description:
    ------------

    Usage::
    """
    # Remove the managed parameter to avoid issue with the library
    if self.__cats is not None:
      return "new vis.Timeline(%s, %s, (function(){let opt = %s; delete opt.managed; return opt})() ); %s" % (
        self.dom.varId, self.items, self.options, self.__cats)

    return "new vis.Timeline(%s, %s, (function(){let opt = %s; delete opt.managed; return opt})() ))" % (
      self.dom.varId, self.items, self.options)
