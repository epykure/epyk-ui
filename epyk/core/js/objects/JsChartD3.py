"""
Module dedicated to perform the data transformation for the D3 charts
"""

from epyk.core.js import JsUtils


class JsChartD3Links:
  def __init__(self, data, js_src, data_schema=None, profile=False):
    self._js_src, self._data_schema, self.profile, self._data = js_src, data_schema, profile, data

  def __register_records_fnc(self, fnc_name, fnc_def, fnc_pmts=None, profile=False):
    """
    Description:
    ------------
    This function will attach to the report object only the javascript functions used during the report,

    Attributes:
    ----------
    :param fnc_name: A String with the Javascript function name to be defined
    :param fnc_def: A String with the Javascript function content
    :param fnc_pmts: A list of parameters
    :param profile: A boolean flag to activate the framework profiling
    """
    fnc_pmts = ["data"] + (fnc_pmts or [])
    if not fnc_name in self._js_src.get('js', {}).get('functions', {}):
      if profile:
        content = "var result = []; %s;return result" % JsUtils.cleanFncs(fnc_def)
      else:
        content = "var result = []; %s;return result" % JsUtils.cleanFncs(fnc_def)
      self._js_src.setdefault('js', {}).setdefault('functions', {})[fnc_name] = {'content': content, 'pmt': fnc_pmts}

  def line(self):
    pass


class JsD3:
  """

  """
  alias = "D3"
  value = ''


class JsD3Bubble:
  alias = "D3"
  chartTypes = ['gravity']
  params = ("seriesNames", "xAxis")
  value = '''
    nbSeries = seriesNames.length;
    var temp = {}; var result = [];
    data.forEach(function(rec){
      for (var key in rec){
        if(key != xAxis && rec[key] != 0 && seriesNames.includes(key))
        { 
          result.push({'Name': rec[xAxis], 'Count': rec[key], 'Category': key, 'nbSeries': nbSeries, 'xAxis': xAxis, 'seriesNames': seriesNames});
        } 
      }
    });
    '''
