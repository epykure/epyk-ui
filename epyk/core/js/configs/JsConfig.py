"""

"""

import json
import importlib
import inspect
import sys

from epyk.core.js import JsEncoder

factory = None

_REGISTERED_CHARTS = ['ChartJs', 'Plotly', 'Billboard', 'C3', 'Vis', 'DC', 'D3', 'NVD3']
__CHART_CONFIGS_PATH = 'epyk.core.js.configs.JsConfig'


def getConfigs(libraries):
  """
  Load the factory with all the different javascript configuration for the different HTML components.
  Some components like charts, tables, pivot and lists are bespoke and would require extra tuning according to the need.
  This module in the framework will segregate all the different official configurations. Some bespoke ones can be
  added in the reports using the available hooks for each type of components

  :param libraries:
  """
  global factory

  if factory is None:
    tmpFactory = {}
    for libConfig in libraries:
      chartMod = importlib.import_module('%s%s' % (__CHART_CONFIGS_PATH, libConfig))
      for name, chartCls in inspect.getmembers(sys.modules[chartMod.__name__]):
        chartAlias = getattr(chartCls, 'alias', None)
        if chartAlias is not None:
          if chartAlias in tmpFactory.get(libConfig, {}):
            raise Exception("Duplicated Name - Chart %s in %s cannot be replaced !!!" % (chartAlias, libConfig))

          tmpFactory.setdefault(libConfig, {})[chartAlias] = chartCls
    factory = tmpFactory
  return factory


def getConfig(pyCls, chartFam):
  """
  Entry point to allow the add of bespoke configurations. Those configurations should be linked to an alias which has
  to be unique. From this entry point it is not possible to update existing configurations.
  Those configurations should follow the defined class structure in order to be then easily added to the framework in the
  next release.

  The entry point of this function in the framework is in the function report.addChartConfig in the framework

  :param pyCls:
  :param chartFam:

  Example
  report.addChartConfig(JsTestHBar, 'ChartJs')
  """
  chartMod = importlib.import_module('%s%s' % (__CHART_CONFIGS_PATH, chartFam))

  return type(pyCls.__name__, (pyCls, chartMod.JsBase), {})


def get(alias, chartFam=None, preferred=True):
  """

  :param alias:
  :param chartFam:
  :param preferred:

  :return:
  """
  result = {}
  for libConfig in _REGISTERED_CHARTS:
    if chartFam is not None and chartFam != libConfig:
      continue

    chartMod = importlib.import_module('%s%s' % (__CHART_CONFIGS_PATH, libConfig))
    for name, chartCls in inspect.getmembers(sys.modules[chartMod.__name__]):
      chartAlias = getattr(chartCls, 'alias', None)
      if chartAlias is not None and chartAlias == alias:
        if chartAlias in result.get(libConfig, {}):
          raise Exception("Duplicated Name - Chart %s in %s cannot be replaced !!!" % (chartAlias, libConfig))

        result.setdefault(libConfig, {})[chartAlias] = chartCls
        if preferred:
          return result

  return result


class JsConfig(dict):
  """
  Base class in charge of the conversion of Python configurations to Javascript ones.
  Those configurations defined on the Python side will only be used and visible on the Javascript.
  This class will build a dictionary of valid parameters for the Javascript layer.

  ## Class Parameters

  - report: The unique object, shared with all the different objects in the framework
  - seriesProperties: Dictionary with configuration to be added after the Javascript data transformation to the object
  - data: The Python data structure which will be added to the data section of the Javascript chart

  ## Special static class variables

  Those variable are properties of the class and should not be changed directly. Some methods are available
  in order to add bespoke configuration to the chart or to the series like addAttr() and addSeriesAttr().
  If something seems to be missing, please never change those variable and either create a new bespoke configuration
  or talk to your IT team.

    - _attrs, Chart properties and styles
    - _statics, parameters added to each series at the end of the data build

  The different Javascript structure are defined by the charting libraries
  """
  _attrs, _statics = None, None

  def __init__(self, report, data, seriesProperties):
    """

    :param report:
    :param data:
    :param seriesProperties:
    """
    self._report, self.seriesProperties = report, seriesProperties
    resolvedAttrs = {}
    self.rAttr(self._attrs, resolvedAttrs)
    if getattr(self, '_statics', None) is not None:
      seriesProperties.setdefault('static', {}).update(self._statics)
    self.update(resolvedAttrs)
    self.data = self.transformation(data)
    self.config()

  def config(self): pass

  def rAttr(self, srcVals, dstVals, srcKey=None):
    """

    :param srcVals:
    :param dstVals:
    :param srcKey:

    :return:
    """
    if isinstance(srcVals, dict):
      for key, val in srcVals.items():
        if isinstance(val, dict):
          dstVals[key] = {}
          self.rAttr(val, dstVals[key])
        else:
          self.rAttr(val, dstVals, key)
    elif isinstance(srcVals, list):
      dstVals[srcKey] = []
      for val in srcVals:
        dstVals[srcKey].append({})
        self.rAttr(val, dstVals[srcKey][-1])
    else:
      if srcKey is not None:
        if isinstance(srcVals, str):
          if srcVals.startswith("function") or srcVals.startswith("JSON.stringify"):
            dstVals[srcKey] = srcVals
          else:
            dstVals[srcKey] = json.dumps(srcVals)
        else:
          dstVals[srcKey] = json.dumps(srcVals)
      elif isinstance(dstVals, list):
        dstVals.append(json.dumps(srcVals))

  def toJs(self, options=None): return self

  @classmethod
  def transformation(cls, data):
    """
    Data transformation for the DataFrame. Using this function might create a new DataFrame. Thus a new Javascript
    object will be created and the logic within the global filters might not work correctly.
    If you use this, please make it obvious to ensure other users might not be surprised

    :param data:

    :return:
    """
    return data

  def addAttr(self, key, val, tree=None, category=None, isPyData=True):
    if isinstance(key, dict):
      for k, v in key.items():
        if isinstance(v, dict):
          if category is None:
            self.addAttr(v, None, tree=tree, category=k, isPyData=isPyData)
          else:
            if tree is None:
              tree = []
            tree.append(k)
            self.addAttr(v, None, tree=tree, category=category, isPyData=isPyData)
        else:
          self.addAttr(k, v, tree=tree, category=category, isPyData=isPyData)
    else:
      if isPyData:
        val = json.dumps(val, cls=JsEncoder.Encoder)
      if category is None and tree is not None:
        category, tree = tree, None
      if tree is not None:
        if not category in self:
          # Default to a dictionary if not defined in the chart structure
          self[category] = {}
        chartLocation = self[category]
        if not isinstance(tree, list):
          tree = [tree]
        for subCategory in tree:
          if isinstance(subCategory, tuple):
            subCategory, subCategoryIndex = subCategory
          else:
            subCategory, subCategoryIndex = subCategory, 0
          if subCategory in getattr(self, 'listAttributes', []):
            if not subCategory in chartLocation:
              chartLocation[subCategory] = []
              for i in range(subCategoryIndex + 1):
                chartLocation[subCategory].append({})
            if len(chartLocation[subCategory]) < subCategoryIndex + 1:
              for i in range(subCategoryIndex + 1):
                if i not in chartLocation[subCategory]:
                  chartLocation[subCategory].append({})
            chartLocation = chartLocation[subCategory][subCategoryIndex]
          else:
            if not subCategory in chartLocation:
              chartLocation[subCategory] = {}
            chartLocation = chartLocation[subCategory]
        if isinstance(chartLocation, list):
          chartLocation[0][key] = val
        else:
          chartLocation[key] = val
      elif category is not None:
        self.setdefault(category, {})[key] = val
      else:
        self[key] = val

  def delAttr(self, keys, tree=None, category=None):
    """

    :param keys:
    :param tree:
    :param category:

    :return:
    """
    chart = self
    if tree is not None:
      chartLocation = self.get(category, {})
      for subCategory in tree:
        chartLocation = chartLocation.get(subCategory, {})
      chart = chartLocation
    if category is not None:
      chart = self.get(category, {})
    for attr in keys:
      if attr in chart:
        del chart[attr]

  def _colors(self, cList, index=None, borderColors=None):
    """

    :param cList:
    :param index:
    :param borderColors:

    :return:
    """
    if index is None:
      for i in range(len(self.data._schema['values'])):
        if len(cList) > i:
          self.seriesProperties['dynamic'].setdefault(i, {})['backgroundColor'] = cList[i]
    else:
      self.seriesProperties['dynamic'].setdefault(index, {})['backgroundColor'] = cList

  @classmethod
  def resolveList(cls, attrs, curr_results, results):
    """
    Convert a list to a string before sending the data to Javascript

    :param attrs:
    :param curr_results:
    :param results:

    :return:
    """
    for item in curr_results:
      if isinstance(item, dict):
        subList = []
        cls.resolveDict(item, subList)
        results.append("{ %s }" % (", ".join(subList)))
      elif isinstance(item, list):
        subList = []
        cls.resolveList(curr_results, item, subList)
        results.append("[%s]" % (",".join(subList)))
      else:
        results.append(item)

  @classmethod
  def resolveDict(cls, attrs, results):
    """
    Convert a nested dictionary to a string before sending the data to Javascript

    :param attrs: A dictionary with some attributes (key, value)
    :param results: A list with resolved attributes

    :return:
    """
    for key, item in attrs.items():
      if isinstance(item, dict):
        subList = []
        cls.resolveDict(item, subList)
        results.append("%s: {%s}" % (key, ", ".join(subList)))
      elif isinstance(item, list):
        subList = []
        cls.resolveList(attrs, item, subList)
        if key == 'data':
          results.append("%s: [%s]" % (key, ",".join(map(lambda x: str(x), subList))))
        else:
          results.append("%s: [%s]" % (key, ",".join(subList)))
      else:
        results.append("%s: %s" % (key, item))
