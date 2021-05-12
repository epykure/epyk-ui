#!/usr/bin/python
# -*- coding: utf-8 -*-


from epyk.core.html import Html
from epyk.core.css.styles.attributes import CssInline
from epyk.core.html.options import OptChartCss


class ChartCss(Html.Html):
  requirements = ('charts.css', )
  name = 'ChartCss'
  _chart__type = "line"
  _option_cls = OptChartCss.ChartCssOptions

  def __init__(self,  report, width, height, html_code, options, profile):
    super(ChartCss, self).__init__(
      report, [], html_code=html_code, profile=profile, options=options, css_attrs={"width": width, "height": height})
    self.attr["class"].clear()
    self.attr["class"].add("charts-css %s" % self._chart__type)
    self._datasets, self._labels, self.row_style = [], [], CssInline()

  @property
  def options(self):
    """
    Description:
    ------------
    Set the ChartCss options.

      https://chartscss.org/charts/area/

    :rtype: OptChartCss.ChartCssOptions
    """
    return super().options

  def labels(self, values):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param values: List. The different values for the x axis.
    """
    self._labels = values

  def dataset(self, i=None):
    """
    Description:
    -----------
    The data property of a ChartJs chart.

    Related Pages:

      https://www.chartjs.org/docs/master/general/data-structures

    Attributes:
    ----------
    :param i: Integer. Optional. The series index according to the y_columns.

    :rtype: JsChartJs.DataSetPie
    """
    if i is None:
      return self._datasets[-1]

  def add_dataset(self, data, label, colors=None, opacity=None, kind=None):
    """
    Description:
    ------------
    Add a new Dataset to the chart list of Datasets.

    Usage::

    Related Pages:

      https://www.chartjs.org/docs/latest/developers/updates.html

    Attributes:
    ----------
    :param data: List. The list of points (float).
    :param label: List. Optional. The list of points (float).
    :param colors: List. Optional. The color for this series. Default the global definition.
    :param opacity: Float. Optional. The opacity level for the content.
    """
    self._datasets.append([label] + data)

  def __str__(self):
    html_frg = [['<th scope="row" style="%s"> %s </th>' % (
      self.row_style, self._labels[i])] for i in range(len(self._datasets[0][1:]))]
    html_frg_head, sections = [], len(self._labels)
    for series in self._datasets:
      #html_frg_head.append('<th scope="col"> %s </th>' % series[0])
      for i, y in enumerate(series[1:]):
        html_frg[i].append('<td style="--start: %s; --size: %s"><span class="data"> %s </span></td>' % (i/sections, y/100, y))
    html_frg_trs = ["".join(frg) for frg in html_frg]
    return '''<table %s><caption>%s</caption><thead>%s</thead><tbody><tr>%s</tr></tbody></table>
      ''' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.options.title,
             "".join(html_frg_head), "</tr><tr>".join(html_frg_trs))


class ChartCssBar(ChartCss):
  requirements = ('charts.css', )
  name = 'ChartCss Bar'
  _chart__type = "column"


class ChartCssBarArea(ChartCss):
  requirements = ('charts.css', )
  name = 'ChartCss Area'
  _chart__type = "area"


class ChartCssBarStacked(ChartCssBar):
  requirements = ('charts.css', )
  name = 'ChartCss Stacked Bar'
  _chart__type = "bar"

  def __init__(self, report, width, height, html_code, options, profile):
    super(ChartCssBar, self).__init__(report, width, height, html_code, options, profile)
    self.options.multiple()
    self.attr["class"].add("stacked")
