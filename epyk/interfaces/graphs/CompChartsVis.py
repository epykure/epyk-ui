
from epyk.core.html import graph


class Vis2D(object):
  def __init__(self, context):
    self.parent = context
    self.chartFamily = "Vis"

  def line(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"), options=None,
           htmlCode=None):
    """
    Description:
    -----------
    Graph2d is an interactive visualization chart to draw data in a 2D graph. You can freely move and zoom in the graph by dragging and scrolling in the window.

    Graph2d uses HTML DOM and SVG for rendering. This allows for flexible customization using css styling.

    Usage:
    -----

    Related Pages:
    --------------
    http://www.chartjs.org/
    https://visjs.github.io/vis-timeline/examples/graph2d/16_bothAxisTitles.html

    Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    data = self.parent.context.rptObj.data.vis.xy(record, y_columns, x_axis)
    line_chart = graph.GraphVis.ChartLine(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    #line_chart.groups.add(sorted(list(labels)))
    for d in data:
      line_chart.add_items(d)
    return line_chart

  def scatter(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
              options=None, htmlCode=None):
    """
    Description:
    -----------

    Usage:
    -----

    Related Pages:
    --------------

      http://www.chartjs.org/

    Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    data = self.parent.context.rptObj.data.vis.xy(record, y_columns, x_axis)
    line_chart = graph.GraphVis.ChartScatter(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.options.height = height[0]
    #line_chart.groups.add(sorted(list(labels)))
    for d in data:
      line_chart.add_items(d)
    return line_chart

  def bar(self, record, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
          options=None, htmlCode=None):
    """
    Description:
    -----------

    Usage:
    -----

    Related Pages:
    --------------

      http://www.chartjs.org/

    Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    data = self.parent.context.rptObj.data.vis.xy(record, y_columns, x_axis)
    line_chart = graph.GraphVis.ChartBar(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.options.height = height[0]
    for d in data:
      line_chart.add_items(d)
    return line_chart

  def timeline(self, record=None, start=None, content=None, end=None, type=None, group=None, profile=None,
               width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """
    Description:
    -----------

    Usage:
    -----

    Related Pages:
    --------------

      http://www.chartjs.org/

    Attributes:
    ----------
    :param record:
    :param start:
    :param content:
    :param end:
    :param type:
    :param group:
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    data = self.parent.context.rptObj.data.vis.timeline(record, start, content, end, type, group, options)
    line_chart = graph.GraphVis.ChartTimeline(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.options.height = height[0]
    line_chart.options.editable = True
    line_chart.options.showCurrentTime = True
    if data['datasets']:
      line_chart.add_items(data['datasets'])
    return line_chart

  def network(self, profile=None, width=(100, "%"), height=(330, "px"), options=None, htmlCode=None):
    """
    Description:
    -----------

    Usage:
    -----

    Attributes:
    ----------
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    line_chart = graph.GraphVis.ChartNetwork(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    line_chart.options.height = height[0]
    return line_chart


class Vis3D(object):

  def __init__(self, context):
    self.parent = context
    self.chartFamily = "Vis"

  def line(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, width=(100, "%"), height=(400, "px"), options=None, htmlCode=None):
    """
    Description:
    -----------

    Usage:
    -----

    Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param z_axis:
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    data = self.parent.context.rptObj.data.vis.xyz(record, y_columns, x_axis, z_axis)
    line_chart = graph.GraphVis.Chart3DLine(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    for d in data:
      line_chart.add_items(d)
    return line_chart

  def bar(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, width=(100, "%"), height=(400, "px"), options=None, htmlCode=None):
    """
    Description:
    -----------

    Usage:
    -----

    Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param z_axis:
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    data = self.parent.context.rptObj.data.vis.xyz(record, y_columns, x_axis, z_axis)
    line_chart = graph.GraphVis.Chart3DBar(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    for d in data:
      line_chart.add_items(d)
    return line_chart

  def surface(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, width=(100, "%"), height=(400, "px"), options=None, htmlCode=None):
    """
    Description:
    -----------

    Usage:
    -----

    Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param z_axis:
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    data = self.parent.context.rptObj.data.vis.xyz(record, y_columns, x_axis, z_axis)
    line_chart = graph.GraphVis.Chart3D(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    for d in data:
      line_chart.add_items(d)
    return line_chart

  def scatter(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, width=(100, "%"), height=(400, "px"), options=None, htmlCode=None):
    """
    Description:
    -----------

    Usage:
    -----

    Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param z_axis:
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    data = self.parent.context.rptObj.data.vis.xyz(record, y_columns, x_axis, z_axis)
    line_chart = graph.GraphVis.Chart3DScatter(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    for d in data:
      line_chart.add_items(d)
    return line_chart


class Vis(Vis2D):

  def __init__(self, context):
    super(Vis, self).__init__(context)
    self._3d = Vis3D(context)

  def surface(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, width=(100, "%"), height=(400, "px"), options=None, htmlCode=None):
    """
    Description:
    -----------

    Usage:
    -----

    Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param z_axis:
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    return self._3d.surface(record, y_columns, x_axis, z_axis, profile, width, height, options, htmlCode)

  def bar3d(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, width=(100, "%"), height=(400, "px"), options=None, htmlCode=None):
    """
    Description:
    -----------

    Usage:
    -----

    Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param z_axis:
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    return self._3d.bar(record, y_columns, x_axis, z_axis, profile, width, height, options, htmlCode)

  def scatter3d(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, width=(100, "%"), height=(400, "px"), options=None, htmlCode=None):
    """
    Description:
    -----------

    Usage:
    -----

    Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param z_axis:
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    return self._3d.scatter(record, y_columns, x_axis, z_axis, profile, width, height, options, htmlCode)

  def line3d(self, record, y_columns=None, x_axis=None, z_axis=None, profile=None, width=(100, "%"), height=(400, "px"), options=None, htmlCode=None):
    """
    Description:
    -----------

    Usage:
    -----

    Attributes:
    ----------
    :param record:
    :param y_columns:
    :param x_axis:
    :param z_axis:
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    return self._3d.line(record, y_columns, x_axis, z_axis, profile, width, height, options, htmlCode)
