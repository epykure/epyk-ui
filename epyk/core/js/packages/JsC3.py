#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.py import primitives

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects
from epyk.core.js.packages import JsPackage


class C3Legend:

  def __init__(self, js_code: str):
    self.varName = js_code

  def show(self, target_ids=None):
    """   Show legend for each target.

    Related Pages:

      https://c3js.org/reference.html#api-legend-show

    :param target_ids:
    """
    if target_ids is None:
      return "%s.show()" % self.varName

    target_ids = JsUtils.jsConvertData(target_ids, None)
    return "%s.show(%s)" % (self.varName, target_ids)

  def hide(self, target_ids=None):
    """   Show legend for each target.

    Related Pages:

      https://c3js.org/reference.html#api-legend-show

    :param target_ids:
    """
    if target_ids is None:
      return "%s.hide()" % self.varName

    target_ids = JsUtils.jsConvertData(target_ids, None)
    return "%s.hide(%s)" % (self.varName, target_ids)


class C3Data:
  def __init__(self, js_code: str):
    self.varName = js_code

  def axes(self, target_ids=None):
    """   Get and set axes of the data loaded in the chart.

    Related Pages:

      https://c3js.org/reference.html#api-data-axes

    :param target_ids:
    """
    if target_ids is None:
      return "%s.axes()" % self.varName

    target_ids = JsUtils.jsConvertData(target_ids, None)
    return "%s.axes(%s)" % (self.varName, target_ids)

  def values(self, target_ids=None):
    """   Get values of the data loaded in the chart.

    Related Pages:

      https://c3js.org/reference.html#api-data-values

    :param target_ids:
    """
    if target_ids is None:
      return "%s.values()" % self.varName

    target_ids = JsUtils.jsConvertData(target_ids, None)
    return "%s.values(%s)" % (self.varName, target_ids)

  def colors(self, target_ids=None):
    """   Get and set colors of the data loaded in the chart.

    Related Pages:

      https://c3js.org/reference.html#api-data-colors

    :param target_ids:
    """
    if target_ids is None:
      return "%s.colors()" % self.varName

    target_ids = JsUtils.jsConvertData(target_ids, None)
    return "%s.colors(%s)" % (self.varName, target_ids)

  def names(self, target_ids=None):
    """   Get and set names of the data loaded in the chart.

    Related Pages:

      https://c3js.org/reference.html#api-data-names

    :param target_ids:
    """
    if target_ids is None:
      return "%s.names()" % self.varName

    target_ids = JsUtils.jsConvertData(target_ids, None)
    return "%s.names(%s)" % (self.varName, target_ids)

  def show(self, target_ids=None):
    """   Show legend for each target.

    Related Pages:

      https://c3js.org/reference.html#api-legend-show

    :param target_ids:
    """
    if target_ids is None:
      return "%s.show()" % self.varName

    target_ids = JsUtils.jsConvertData(target_ids, None)
    return "%s.show(%s)" % (self.varName, target_ids)

  def hide(self, target_ids=None):
    """   Show legend for each target.

    Related Pages:

      https://c3js.org/reference.html#api-legend-show

    :param target_ids:
    """
    if target_ids is None:
      return "%s.hide()" % self.varName

    target_ids = JsUtils.jsConvertData(target_ids, None)
    return "%s.hide(%s)" % (self.varName, target_ids)


class C3(JsPackage):
  lib_alias = {'js': "c3", 'css': 'c3'}

  def __init__(self, component: primitives.HtmlModel, js_code: str, set_var: bool = False,
               page: primitives.PageModel = None):
    super(C3, self).__init__(component=component, js_code=js_code, selector=js_code, set_var=set_var, page=page)

  @property
  def legend(self):
    return C3Legend("%s.legend" % self.component.htmlCode)

  @property
  def value(self):
    return JsObjects.JsObjects.get(
      "{'%s': arguments[0], timestamp: Date.now(), offset: new Date().getTimezoneOffset()}" % self.component.htmlCode)

  @property
  def content(self):
    return JsObjects.JsNumber.JsNumber("arguments[0].value")

  @property
  def label(self):
    return JsObjects.JsString.JsString("arguments[0].name", is_py_data=False)

  def load(self):
    """

    :return:
    """

  def show(self, target_ids=None, options=None):
    """   This API shows specified targets.

    You can specify multiple targets by giving an array that includes id as String.
    If no argument is given, all of targets will be shown.

    Related Pages:

      https://c3js.org/reference.html#api-show

    :param target_ids:
    :param options:
    """
    if target_ids is None and options is None:
      return JsObjects.JsVoid("%s.show()" % self._selector)

    target_ids = JsUtils.jsConvertData(target_ids, None)
    options = JsUtils.jsConvertData(options, None)
    return JsObjects.JsVoid("%s.show(%s, %s)" % (self._selector, target_ids, options))

  def toggle(self, target_ids=None, options=None):
    """   This API shows specified targets.

    You can specify multiple targets by giving an array that includes id as String.
    If no argument is given, all of targets will be shown.

    Related Pages:

      https://c3js.org/reference.html#api-show

    :param target_ids:
    :param options:
    """
    if target_ids is None and options is None:
      return JsObjects.JsVoid("%s.toggle()" % self._selector)

    target_ids = JsUtils.jsConvertData(target_ids, None)
    options = JsUtils.jsConvertData(options, None)
    return JsObjects.JsVoid("%s.toggle(%s, %s)" % (self._selector, target_ids, options))

  @property
  def data(self):
    """   Get data loaded in the chart.

    Related Pages:

      https://c3js.org/reference.html#api-data
    """
    raise NotImplementedError()

  def hide(self, target_ids=None, options=None):
    """   This API hides specified targets.

    You can specify multiple targets by giving an array that includes id as String.
    If no argument is given, all of targets will be hidden.

    Related Pages:

      https://c3js.org/reference.html#api-hide

    :param target_ids:
    :param options:
    """
    if target_ids is None and options is None:
      return JsObjects.JsVoid("%s.show()" % self._selector)

    target_ids = JsUtils.jsConvertData(target_ids, None)
    options = JsUtils.jsConvertData(options, None)
    return JsObjects.JsVoid("%s.show(%s, %s)" % (self._selector, target_ids, options))

  def flow(self, args):
    """   Flow data to the chart.

    By this API, you can append new data points to the chart.

    Related Pages:

      https://c3js.org/reference.html#api-flow

    :param args:
    """
    args = JsUtils.jsConvertData(args, None)
    return JsObjects.JsVoid("%s.flow(%s)" % (self._selector, args))

  def transform(self, chart_type, target_ids=None):
    """   Change the type of the chart.

    Related Pages:

      https://c3js.org/reference.html#api-transform

    :param chart_type:
    :param target_ids:
    """
    if target_ids is None:
      chart_type = JsUtils.jsConvertData(chart_type, None)
      return JsObjects.JsVoid("%s.transform(%s)" % (self._selector, chart_type))

    target_ids = JsUtils.jsConvertData(target_ids, None)
    return JsObjects.JsVoid("%s.transform(%s, %s)" % (self._selector, chart_type, target_ids))

  def load(self, args):
    """   Load data to the chart.

    You can specify multiple targets by giving an array that includes id as String.
    If no argument is given, all of targets will be toggles.

    Related Pages:

      https://c3js.org/reference.html#api-load

    :param args:
    """
    if isinstance(args, list):
      if not isinstance(args[0], list):
        args = {"columns": [args]}
      else:
        args = {"columns": args}
    args = JsUtils.jsConvertData(args, None)
    return JsObjects.JsVoid("%s.load(%s)" % (self._selector, args))

  def unload(self, args):
    """   Unload data to the chart.

    You can specify multiple targets by giving an array that includes id as String.
    If no argument is given, all of targets will be toggles.

    Related Pages:

      https://c3js.org/reference.html#api-unload

    :param args:
    """
    if isinstance(args, list):
      args = {"ids": args}
    args = JsUtils.jsConvertData(args, None)
    return JsObjects.JsVoid("%s.unload(%s)" % (self._selector, args))

  def resise(self, size):
    """   Resize the chart.

    Related Pages:

      https://c3js.org/reference.html#api-resize

    :param size:
    """
    size = JsUtils.jsConvertData(size, None)
    return JsObjects.JsVoid("%s.resise(%s)" % (self._selector, size))

  def flush(self):
    """   Force to redraw.

    Related Pages:

      https://c3js.org/reference.html#api-flush
    """
    return JsObjects.JsVoid("%s.flush()" % self._selector)

  def destroy(self):
    """   Reset the chart object and remove element and events completely.

    Related Pages:

      https://c3js.org/reference.html#api-flush
    """
    return JsObjects.JsVoid("%s.destroy()" % self._selector)

  def xgrids(self, grids):
    """   Update x grid lines.

    :param grids:
    """
    grids = JsUtils.jsConvertData(grids, None)
    return JsObjects.JsVoid("%s.xgrids(%s)" % (self._selector, grids))

  def select(self, ids, indices, reset_others):
    """   Change data point state to selected.

    By this API, you can select data points. To use this API, data.selection.enabled needs to be set true.

    Related Pages:

      https://c3js.org/reference.html#api-select

    :param ids:
    :param indices:
    :param reset_others:
    """
    ids = JsUtils.jsConvertData(ids, None)
    indices = JsUtils.jsConvertData(indices, None)
    reset_others = JsUtils.jsConvertData(reset_others, None)
    return JsObjects.JsVoid("%s.select(%s, %s, %s)" % (self._selector, ids, indices, reset_others))

  def unselected(self, ids, indices):
    """   Change data point state to unselected.

    By this API, you can unselect data points. To use this API, data.selection.enabled needs to be set true.

    Related Pages:

      https://c3js.org/reference.html#api-select

    :param ids:
    :param indices:
    """
    ids = JsUtils.jsConvertData(ids, None)
    indices = JsUtils.jsConvertData(indices, None)
    return JsObjects.JsVoid("%s.select(%s, %s)" % (self._selector, ids, indices))

  def selected(self, ids):
    """   Get selected data points.

    By this API, you can get selected data points information.
    To use this API, data.selection.enabled needs to be set true.

    Related Pages:

      https://c3js.org/reference.html#api-selected

    :param ids:
    """
    ids = JsUtils.jsConvertData(ids, None)
    return JsObjects.JsVoid("%s.selected(%s)" % (self._selector, ids))

  def zoom(self, domain):
    """   Zoom by giving x domain.

    Related Pages:

      https://c3js.org/reference.html#api-zoom

    :param domain:
    """
    domain = JsUtils.jsConvertData(domain, None)
    return JsObjects.JsVoid("%s.zoom(%s)" % (self._selector, domain))

  def unzoom(self):
    """   Unzoom to the original domain.

    Related Pages:

      https://c3js.org/reference.html#api-unzoom
    """
    return JsObjects.JsVoid("%s.unzoom()" % self._selector)
