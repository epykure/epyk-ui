"""
Chart Fabric to manage the priorities between the different Javascript libraries
"""

import os
import inspect
import logging
import importlib

from epyk.core.html import Html
from epyk.core.js.configs import JsConfig


JS_CHARTS = [
  {"chart": 'ChartJs', 'dsc': {'eng': 'The ChartJS Javacript Framework'}},
  {"chart": 'Plotly', 'dsc': {'eng': 'The Plotly.js Javacript Framework'}},
  {"chart": 'Billboard', 'dsc': {'eng': 'The Billboard.js Javascript Framework'}},
  {"chart": 'C3', 'dsc': {'eng': 'The C3.js Javascript Framework'}},
  {"chart": 'D3', 'dsc': {'eng': 'The base library for most of the charting ones'}},
  {"chart": 'Vis', 'dsc': {'eng': 'The Vis.js Javascript Framework'}},
  {"chart": 'NVD3', 'dsc': {'eng': 'The NVD3 Javascript Framework'}},
  {"chart": 'DC', 'dsc': {'eng': 'The DC Javascript Framework'}}
]

# The main charting factory. This will reuse by the different interface dedicated to the different javascript frameworks
CHARTS_FACTORY = None
__CHART_CONFIGS_PATH = 'epyk.core.js.configs.JsConfig'

def loadFactory():
  """
  This function will load in memory the different charts configurations available in each javascript charting libraries.
  This function will retrieve the different configurations from the different location and allow the mapping between an
  alias and its object.
  """
  tmp, chart_libs = {}, []
  for jsChart in JS_CHARTS:
    chart_libs.append(jsChart["chart"])
    if jsChart["chart"] in ['Vis', 'Billboard', 'DC']:
      continue

    try:
      chart_mod = importlib.import_module(__CHART_CONFIGS_PATH % jsChart)
      for script in os.listdir(os.path.dirname(chart_mod.__file__)):
        if script.startswith(jsChart['chart']) and script.endswith('py'):
          for name, obj in inspect.getmembers(importlib.import_module(__CHART_CONFIGS_PATH % (jsChart['chart'], script.replace(".py", ""))), inspect.isclass):
            if getattr(obj, 'chartCall', None) is not None:
              tmp.setdefault(jsChart['chart'], {})[getattr(obj, 'chartCall')] = obj
    except Exception as err:
      logging.warning("%s, error %s" % (jsChart['chart'], err))
  # Add the configurations attached to the new configuration framework
  for chart_fam, chart_def in JsConfig.getConfigs(chart_libs).items():
    for chartAlias, chartCls in chart_def.items():
      tmp.setdefault(chart_fam, {})[chartAlias] = chartCls
  return tmp


class Chart(Html.Html):
  """
  This class will be used in order to return the preferred Chart Python interface to the user.
  Indeed each Javascript Chart framework has its own specificities and this method will only renderer the preferred one.
  It will be then possible to use all the available method of the specific object received from this Factory.
  Methods between the different frameworks will tend to be aligned.

  To get more details it is possible to use the help method on the object (or the help method on the report object to get something in Html)
  """
  name, category, callFnc = 'Chart', 'Charts', 'plot'

  @staticmethod
  def create():
    """
    Call the internal module function to load the charting factory and return the content. This wrapper will also
    store the results in order to avoid having to reload it multiple times. This will guarantee a unique parsing
    of the different modules for efficiency purposes.
    """
    global CHARTS_FACTORY

    if CHARTS_FACTORY is None:
      CHARTS_FACTORY = loadFactory()  # atomic function to store all the different table mapping
    return CHARTS_FACTORY

  @staticmethod
  def addConfig(config_cls, chart_family):
    """
    Entry point in the framework in order to create bespoke charts configurations on the fly.
    Existing charts definition cannot be overriden. This is only designed to allow the creation of new classes in
    the reports without expecting a release of the whole framework

    :param config_cls:
    :param chart_family:

    :return: The internal chart class from the internal factory
    """
    new_chart = None
    factory = Chart.create()
    if factory is not None and not config_cls.alias in factory:
      new_chart = JsConfig.getConfig(config_cls, chart_family)
      if new_chart is not None:
        factory[chart_family][new_chart.alias] = new_chart
    return new_chart

  @staticmethod
  def get(report, chart_type, chart_family):
    """
    Return the chart object according to the chartType selected by the user.
    This will go thought the different javascript frameworks and try to find the preferred one.
    The priority will be set using the order of the frameworks in the global variable JS_CHARTS

    :param report: The internal report object
    :param chart_type: The chart type (the configuration aliases e.g: line, bar, scatter...)
    :param chart_family: The chart family alias (e.g plotly, chartJs, NVd3...)

    """
    # In this case we are dealing with a bespoke D3 chart
    if chart_type is None:
      return "D3Bespoke"

    factory = Chart.create()
    if chart_family is not None:
      return chart_family

    for chart_family in JS_CHARTS:
      if chart_type in factory[chart_family['chart']]:
        return chart_family['chart']

  def chart(self, chart_type, chart_family):
    return ""

  @staticmethod
  def html(chart_obj, attrs, chart_container):
    """

    Example
    <i style="margin:0 5px;cursor:pointer" class="far fa-comment-alt"></i>
    <i style="margin:0 5px;cursor:pointer" class="fas fa-table"></i>
    <a href="" style="margin:0 5px;cursor:pointer" class="fas fa-download" onclick="this.href = window['%(htmlId)s_chart'].toBase64Image()" download></a>
    <i style="margin:0 5px;cursor:pointer" class="fas fa-redo-alt"></i>

    :param chart_obj: The Python chart object
    :param attrs:
    :param chart_container: The Chart HTML container

    :return: The HTML fragment
    """
    options = []
    for pyFnc, icon, aType in [('toTsv', 'fa fa-file-excel', 'download="data.tsv"'),
                               ('toImg', 'fas fa-download', 'download'), ('toImg', 'fas fa-search-plus', '')]:
      if hasattr(chart_obj, pyFnc):
        options.append('<a href="" style="margin:0 5px;cursor:pointer;color:inherit" class="%(icon)s" onclick="this.href = %(fnc)s" %(aType)s></a>' % {'icon': icon, 'fnc': getattr(chart_obj, pyFnc)().replace('"', "'"), 'aType': aType})
    if chart_obj.helper != "":
      options.append(chart_obj.helper)
    iconAnimated, iconEvent = "", ""
    if chart_obj.dataSrc is not None:
      if chart_obj.dataSrc.get("type") == "script" and "frequency" in chart_obj.dataSrc:
        iconAnimated = " fa-pulse"
        iconEvent = ' title="click to stop refresh" onclick="$(this).removeClass(\'fa-pulse\'); clearInterval(window[\'interval_%s\'])"' % chart_obj.dataSrc['intervalId']
    return '''
          <div %(strAttr)s id="%(htmlId)s_container">  
            %(strChart)s
            <span style="bottom:0;margin:0 0 5px 0;width:100%%;color:%(grey)s;display:inline-block;text-align:left">
              <i style="margin:0 5px 0 0" class="fas fa-clock%(animated)s"%(iconEvent)s></i>Last update: <div id="%(htmlId)s_time" style="display:inline-block"></div>
              <div style="display:inline-block;float:right;margin-right:0px">
                %(options)s
              </div>
            </span>
          </div>
          ''' % {'htmlId': chart_obj.htmlId, 'strAttr': attrs, 'strChart': chart_container,
                 'grey': chart_obj._report.theme.greys[3],
                 'options': "".join(options), 'animated': iconAnimated, 'iconEvent': iconEvent}
