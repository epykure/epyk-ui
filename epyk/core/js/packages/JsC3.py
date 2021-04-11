#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

Related Pages:

		https://naver.github.io/billboard.js/release/latest/doc/Chart.html#data%25E2%2580%25A4colors
"""

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects
from epyk.core.js.packages import JsPackage


class C3Legend:

  def __init__(self, varName):
    self.varName = varName

  def show(self, targetIds=None):
    """
    Description:
    -----------
    Show legend for each target.

    Related Pages:

      https://c3js.org/reference.html#api-legend-show

    :param targetIds:
    """
    if targetIds is None:
      return "%s.show()" % self.varName

    targetIds = JsUtils.jsConvertData(targetIds, None)
    return "%s.show(%s)" % (self.varName, targetIds)

  def hide(self, targetIds=None):
    """
    Description:
    -----------
    Show legend for each target.

    Related Pages:

      https://c3js.org/reference.html#api-legend-show

    :param targetIds:
    """
    if targetIds is None:
      return "%s.hide()" % self.varName

    targetIds = JsUtils.jsConvertData(targetIds, None)
    return "%s.hide(%s)" % (self.varName, targetIds)


class C3Data:
  def __init__(self, varName):
    self.varName = varName

  def axes(self, targetIds=None):
    """
    Description:
    -----------
    Get and set axes of the data loaded in the chart.

    Related Pages:

      https://c3js.org/reference.html#api-data-axes

    Attributes:
    ----------
    :param targetIds:
    """
    if targetIds is None:
      return "%s.axes()" % self.varName

    targetIds = JsUtils.jsConvertData(targetIds, None)
    return "%s.axes(%s)" % (self.varName, targetIds)

  def values(self, targetIds=None):
    """
    Description:
    -----------
    Get values of the data loaded in the chart.

    Related Pages:

      https://c3js.org/reference.html#api-data-values

    Attributes:
    ----------
    :param targetIds:
    """
    if targetIds is None:
      return "%s.values()" % self.varName

    targetIds = JsUtils.jsConvertData(targetIds, None)
    return "%s.values(%s)" % (self.varName, targetIds)

  def colors(self, targetIds=None):
    """
    Description:
    -----------
    Get and set colors of the data loaded in the chart.

    Related Pages:

      https://c3js.org/reference.html#api-data-colors

    Attributes:
    ----------
    :param targetIds:
    """
    if targetIds is None:
      return "%s.colors()" % self.varName

    targetIds = JsUtils.jsConvertData(targetIds, None)
    return "%s.colors(%s)" % (self.varName, targetIds)

  def names(self, targetIds=None):
    """
    Description:
    -----------
    Get and set names of the data loaded in the chart.

    Related Pages:

      https://c3js.org/reference.html#api-data-names

    Attributes:
    ----------
    :param targetIds:
    """
    if targetIds is None:
      return "%s.names()" % self.varName

    targetIds = JsUtils.jsConvertData(targetIds, None)
    return "%s.names(%s)" % (self.varName, targetIds)

  def show(self, targetIds=None):
    """
    Description:
    -----------
    Show legend for each target.

    Related Pages:

      https://c3js.org/reference.html#api-legend-show

    Attributes:
    ----------
    :param targetIds:
    """
    if targetIds is None:
      return "%s.show()" % self.varName

    targetIds = JsUtils.jsConvertData(targetIds, None)
    return "%s.show(%s)" % (self.varName, targetIds)

  def hide(self, targetIds=None):
    """
    Description:
    -----------
    Show legend for each target.

    Related Pages:

      https://c3js.org/reference.html#api-legend-show

    Attributes:
    ----------
    :param targetIds:
    """
    if targetIds is None:
      return "%s.hide()" % self.varName

    targetIds = JsUtils.jsConvertData(targetIds, None)
    return "%s.hide(%s)" % (self.varName, targetIds)


class C3(JsPackage):
  lib_alias = {'js': "c3", 'css': 'c3'}

  def __init__(self, src, varName, setVar=False, report=None):
    super(C3, self).__init__(src=src, varName=varName, selector=varName, setVar=setVar)
    self._report = report

  @property
  def legend(self):
    return C3Legend("%s.legend" % self.src.htmlCode)

  @property
  def value(self):
    return JsObjects.JsObjects.get(
      "{'%s': arguments[0], timestamp: Date.now(), offset: new Date().getTimezoneOffset()}" % self.src.htmlCode)

  @property
  def content(self):
    return JsObjects.JsNumber.JsNumber("arguments[0].value")

  @property
  def label(self):
    return JsObjects.JsString.JsString("arguments[0].name", isPyData=False)

  def load(self):
    """

    :return:
    """

  def show(self, targetIds=None, options=None):
    """
    Description:
    -----------
    This API shows specified targets.

    You can specify multiple targets by giving an array that includes id as String.
    If no argument is given, all of targets will be shown.

    Related Pages:

      https://c3js.org/reference.html#api-show

    Attributes:
    ----------
    :param targetIds:
    :param options:
    """
    if targetIds is None and options is None:
      return JsObjects.JsVoid("%s.show()" % self._selector)

    targetIds = JsUtils.jsConvertData(targetIds, None)
    options = JsUtils.jsConvertData(options, None)
    return JsObjects.JsVoid("%s.show(%s, %s)" % (self._selector, targetIds, options))

  def toggle(self, targetIds=None, options=None):
    """
    Description:
    -----------
    This API shows specified targets.

    You can specify multiple targets by giving an array that includes id as String.
    If no argument is given, all of targets will be shown.

    Related Pages:

      https://c3js.org/reference.html#api-show

    Attributes:
    ----------
    :param targetIds:
    :param options:
    """
    if targetIds is None and options is None:
      return JsObjects.JsVoid("%s.toggle()" % self._selector)

    targetIds = JsUtils.jsConvertData(targetIds, None)
    options = JsUtils.jsConvertData(options, None)
    return JsObjects.JsVoid("%s.toggle(%s, %s)" % (self._selector, targetIds, options))

  @property
  def data(self):
    """
    Description:
    -----------
    Get data loaded in the chart.

    Related Pages:

      https://c3js.org/reference.html#api-data
    """
    return

  def hide(self, targetIds=None, options=None):
    """
    Description:
    -----------
    This API hides specified targets.

    You can specify multiple targets by giving an array that includes id as String.
    If no argument is given, all of targets will be hidden.

    Related Pages:

      https://c3js.org/reference.html#api-hide

    Attributes:
    ----------
    :param targetIds:
    :param options:
    """
    if targetIds is None and options is None:
      return JsObjects.JsVoid("%s.show()" % self._selector)

    targetIds = JsUtils.jsConvertData(targetIds, None)
    options = JsUtils.jsConvertData(options, None)
    return JsObjects.JsVoid("%s.show(%s, %s)" % (self._selector, targetIds, options))

  def flow(self, args):
    """
    Description:
    -----------
    Flow data to the chart.

    By this API, you can append new data points to the chart.

    Related Pages:

      https://c3js.org/reference.html#api-flow

    Attributes:
    ----------
    :param args:
    """
    args = JsUtils.jsConvertData(args, None)
    return JsObjects.JsVoid("%s.flow(%s)" % (self._selector, args))

  def transform(self, type, targetIds=None):
    """
    Description:
    -----------
    Change the type of the chart.

    Related Pages:

      https://c3js.org/reference.html#api-transform

    :param args:
    """
    if targetIds is None:
      type = JsUtils.jsConvertData(type, None)
      return JsObjects.JsVoid("%s.transform(%s)" % (self._selector, type))

    targetIds = JsUtils.jsConvertData(targetIds, None)
    return JsObjects.JsVoid("%s.transform(%s, %s)" % (self._selector, type, targetIds))

  def load(self, args):
    """
    Description:
    -----------
    Load data to the chart.

    You can specify multiple targets by giving an array that includes id as String.
    If no argument is given, all of targets will be toggles.

    Related Pages:

      https://c3js.org/reference.html#api-load

    Attributes:
    ----------
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
    """
    Description:
    -----------
    Unload data to the chart.

    You can specify multiple targets by giving an array that includes id as String.
    If no argument is given, all of targets will be toggles.

    Related Pages:

      https://c3js.org/reference.html#api-unload

    Attributes:
    ----------
    :param args:
    """
    if isinstance(args, list):
      args = {"ids": args}
    args = JsUtils.jsConvertData(args, None)
    return JsObjects.JsVoid("%s.unload(%s)" % (self._selector, args))

  def resise(self, size):
    """
    Description:
    -----------
    Resize the chart.

    Related Pages:

      https://c3js.org/reference.html#api-resize
    """
    size = JsUtils.jsConvertData(size, None)
    return JsObjects.JsVoid("%s.resise(%s)" % (self._selector, size))

  def flush(self):
    """
    Description:
    -----------
    Force to redraw.

    Related Pages:

      https://c3js.org/reference.html#api-flush
    """
    return JsObjects.JsVoid("%s.flush()" % self._selector)

  def destroy(self):
    """
    Description:
    -----------
    Reset the chart object and remove element and events completely.

    Related Pages:

      https://c3js.org/reference.html#api-flush
    """
    return JsObjects.JsVoid("%s.destroy()" % self._selector)

  def xgrids(self, grids):
    """
    Description:
    -----------
    Update x grid lines.
    """
    grids = JsUtils.jsConvertData(grids, None)
    return JsObjects.JsVoid("%s.xgrids(%s)" % (self._selector, grids))

  def select(self, ids, indices, resetOthers):
    """
    Description:
    -----------
    Change data point state to selected.

    By this API, you can select data points. To use this API, data.selection.enabled needs to be set true.

    Related Pages:

      https://c3js.org/reference.html#api-select
    """
    ids = JsUtils.jsConvertData(ids, None)
    indices = JsUtils.jsConvertData(indices, None)
    resetOthers = JsUtils.jsConvertData(resetOthers, None)
    return JsObjects.JsVoid("%s.select(%s, %s, %s)" % (self._selector, ids, indices, resetOthers))

  def unselected(self, ids, indices):
    """
    Description:
    -----------
    Change data point state to unselected.

    By this API, you can unselect data points. To use this API, data.selection.enabled needs to be set true.

    Related Pages:

      https://c3js.org/reference.html#api-select
    """
    ids = JsUtils.jsConvertData(ids, None)
    indices = JsUtils.jsConvertData(indices, None)
    return JsObjects.JsVoid("%s.select(%s, %s)" % (self._selector, ids, indices))

  def selected(self, ids):
    """
    Description:
    -----------
    Get selected data points.

    By this API, you can get selected data points information.
    To use this API, data.selection.enabled needs to be set true.

    Related Pages:

      https://c3js.org/reference.html#api-selected
    """
    ids = JsUtils.jsConvertData(ids, None)
    return JsObjects.JsVoid("%s.selected(%s)" % (self._selector, ids))

  def zoom(self, domain):
    """
    Description:
    -----------
    Zoom by giving x domain.

    Related Pages:

      https://c3js.org/reference.html#api-zoom
    """
    domain = JsUtils.jsConvertData(domain, None)
    return JsObjects.JsVoid("%s.zoom(%s)" % (self._selector, domain))

  def unzoom(self):
    """
    Description:
    -----------
    Unzoom to the original domain.

    Related Pages:

      https://c3js.org/reference.html#api-unzoom
    """
    return JsObjects.JsVoid("%s.unzoom()" % self._selector)
