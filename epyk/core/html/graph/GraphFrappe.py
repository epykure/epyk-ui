#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html
from epyk.core.css import Colors
from epyk.core.html.options import OptChartFrappe
from epyk.core.js.packages import JsFrappe


class Frappe(Html.Html):
  requirements = ('frappe-charts', )
  name = 'Frappe Mixed'
  _chart__type = 'axis-mixed'
  _option_cls = OptChartFrappe.FrappeLine

  def __init__(self,  report, width, height, html_code, options, profile):
    super(Frappe, self).__init__(
      report, [], html_code=html_code, profile=profile, options=options, css_attrs={"width": width, "height": height})
    self.chartId = "%s_obj" % self.htmlCode
    self.options.type = self._chart__type

  @property
  def shared(self):
    """
    Description:
    -----------
    All the common properties shared between all the charts.
    This will ensure a compatibility with the plot method.

    Usage::

      line = page.ui.charts.chartJs.bar()
      line.shared.x_label("x axis")
    """
    return OptChartFrappe.OptionsChartSharedFrappe(self)

  @property
  def js(self):
    """
    Description:
    -----------
    The Javascript functions defined for this component.
    Those can be specific ones for the module or generic ones from the language.

    Usage::

      btn = page.ui.button("Click").click([
        line.js.addDataPoint("test", [15, 67])
      ])

    :return: A Javascript Dom object functions.

    :rtype: JsFrappe.FrappeCharts
    """
    if self._js is None:
      self._js = JsFrappe.FrappeCharts(selector="window['%s']" % self.chartId, src=self)
    return self._js

  @property
  def options(self):
    """
    Description:
    -----------
    Chart specific options.

    :rtype: OptChartFrappe.FrappeLine
    """
    return super().options

  def colors(self, hex_values):
    """
    Description:
    -----------
    Set the colors of the chart.

    hex_values can be a list of string with the colors or a list of tuple to also set the bg colors.
    If the background colors are not specified they will be deduced from the colors list changing the opacity.

    Usage::

    Attributes:
    ----------
    :param hex_values: List. An array of hexadecimal color codes.
    """
    line_colors, bg_colors = [], []
    for h in hex_values:
      if h.upper() in Colors.defined:
        h = Colors.defined[h.upper()]['hex']
      if not isinstance(h, tuple):
        line_colors.append(h)
        bg_colors.append("rgba(%s, %s, %s, %s" % (
          Colors.getHexToRgb(h)[0], Colors.getHexToRgb(h)[1],
          Colors.getHexToRgb(h)[2], 0.8))
      else:
        line_colors.append(h[0])
        bg_colors.append(h[0])
    self.options.colors = line_colors

  def labels(self, values):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param values: List. The different values for the x axis.
    """
    self.options.data.labels = values

  def add_dataset(self, data, label, colors=None, opacity=None, kind=None):
    return self.options.data.add_data(data, label, kind or "line")

  def build(self, data=None, options=None, profile=None, component_id=None):
    """
    Description:
    ------------
    Update the chart with context and / or data changes.

    Attributes:
    ----------
    :param data: List. Optional. The full datasets object expected by ChartJs.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param component_id: String. Not used.
    """
    if data is not None:
      return self.js.update(data)

    return '''%(chartId)s = new frappe.Chart("#%(hmlCode)s", %(config)s)
    ''' % {"chartId": self.chartId, "chartType": self._chart__type, "hmlCode": component_id or self.htmlCode,
           "config": self.options.config_js(options).toStr()}

  def __str__(self):
    self.page.properties.js.add_builders(self.build())
    return '<div %s></div>' % self.get_attrs(pyClassNames=self.style.get_classes())


class FrappeLine(Frappe):
  name = 'Frappe Line'
  _chart__type = 'line'


class FrappeBar(Frappe):
  name = 'Frappe Bar'
  _chart__type = 'bar'


class FrappePie(Frappe):
  name = 'Frappe Pie'
  _chart__type = 'pie'


class FrappeDonut(Frappe):
  name = 'Frappe Donut'
  _chart__type = 'donut'


class FrappePercentage(Frappe):
  name = 'Frappe Percentage'
  _chart__type = 'percentage'


class FrappeHeatmap(Frappe):
  name = 'Frappe Heatmap'
  _chart__type = 'heatmap'
