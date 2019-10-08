"""

"""

import json

from epyk.core.js.primitives import JsArray
from epyk.core.js.primitives import JsObject
from epyk.core.js.primitives import JsNumber

from epyk.core.js.objects import jsText

from epyk.core.js.packages.JsCrossFilter import CrossFilter
from epyk.core.js.packages.JsVis import VisDataSet


class DataLoop(object):
  """
  Data Class used for all the loop and map in the Javascript side.
  This will get the below attributes

  val   : The current value in the loop
  index : The index item
  arr   : The full array (only available in case of arrays, map, filter, every  )
  """
  val, index, arr = JsObject.JsObject("value"), JsNumber.JsNumber("index", isPyData=False), JsArray.JsArray("arr")


class DataReduce(object):
  """

  rVal  :
  val   :
  index :
  """
  rVal, val, index = JsObject.JsObject("r"), JsNumber.JsNumber("o", isPyData=False), JsNumber.JsNumber("i", isPyData=False)


class DataSort(object):
  """

  """


class DataEach(object):
  """
  Data Class for the Jquery each loop

  index : index
  data  : element
  """
  index, data = JsNumber.JsNumber("index", isPyData=False), JsObject.JsObject("data", isPyData=False)


class RawData(object):
  def __init__(self, report, records, keys=None, values=None, profile=False):
    self._schema = {'fncs': [], 'out': None, 'post': [], 'keys': set() if keys is None else set(keys),
                    'values': set() if values is None else set(values), 'profile': getattr(report, 'PROFILE', profile)}
    self._dataId = id(records) # Store the memory ID of the original object (the one known by all the components
    self._jqId = "data_%s" % self._dataId # Original recordSet, this will never change
    self._report, self.jqId, self._data = report, self._jqId, records
    self._jsId, self.jsArgs = id(self), []

  def setId(self, jqId):
    """
    Change the Id variable name for the javascript data source.

    Example

    :param jqId:

    :return: The Python object
    """
    self.jqId = jqId if jqId is not None else self._jqId
    return self

  def attach(self, html_obj):
    """
    Attach the data object to a HTML Object.

    This function is automatically used in the different components in order
    to guarantee the link of the data. This will also ensure that the same data set will be store only once in the page

    Example

    :param html_obj:

    """
    if not self._jqId in self._report.jsSources or not 'containers' in self._report.jsSources[self._jqId]:
      self._report.jsSources[self._jqId] = {'dataId': self._dataId, 'containers': [], 'data': self._data}
    self._report.jsSources[self._jqId]['containers'].append(html_obj)
    self._report.jsSources[self._jqId]['data'] = self._data # In case of replacements
    return self

  def output(self, out_family, out_type, args):
    """
    Format the recordSet to a defined container.

    Example

    Documentation

    :param out_family:
    :param out_type:
    :param args:

    """
    self._schema['out'] = {"family": out_family, 'type': out_type, 'params': args}
    self._schema['out']['name'] = "%s_%s" % (out_family, str(out_type).replace("-", "")) if "%s_%s" % (out_family, str(out_type).replace("-", "")) in factory['objs'] else out_family
    return self

  def fncs(self, fnc_names, system_info=None):
    """
    Post process functions on the recordSet. It will potentially enhance the columns to be processed if the systemInfo parameters are defined.
    This will allow to pass extra parameters to the different functions in the framework according to the system.
    Information can be computed in the bespoke reports or coming directly from the source system.
    In order to use this the category should be defined in the Javascript function defined in the module jsFncsRecords.

    Documentation

    :param fnc_names:
    :param system_info:

    """
    if not fnc_names:
      return self

    if not isinstance(fnc_names, list):
      fnc_names = [fnc_names]
    for fnc_name in fnc_names:
      args = None
      if isinstance(fnc_name, tuple):
        # This mean that some parameters are expected in the configuration
        if fnc_name[0] == 'order':
          count_per_axis, order_series = {}, []
          self._data['order'] = 0
          if fnc_name[1] is not None:
            for rec in self._data[fnc_name[1]]:
              count_per_axis[rec] = count_per_axis.get(rec, -1) + 1
              order_series.append(count_per_axis[rec])
            self._data['order'] = order_series
          continue

        args = list(fnc_name)[1:]
        fnc_name = fnc_name[0].replace("-", "")
        factory['fncs'][fnc_name]['class'].extendColumns(self._schema, args)
      if system_info is not None:
        for category, sysCols in system_info.items():
          args = factory['fncs'][fnc_name]['class'].extendArgs(category, args, sysCols)
      self.jsArgs.append(dict([(factory['fncs'][fnc_name]['class'].params[i], arg) for i, arg in enumerate(args)]))
      argsId = len(self._schema['fncs'])
      self._schema['fncs'].append({'name': fnc_name, 'args': ["%s_%s" % (factory['fncs'][fnc_name]['class'].params[i], argsId) for i, _ in enumerate(args)] })
    return self

  def post_process(self, fnc_names):
    """

    Example

    :param fnc_names:

    """
    if not isinstance(fnc_names, list):
      fnc_names = [fnc_names]
    for fnc_name in fnc_names:
      args = None
      if isinstance(fnc_name, tuple):
        # This mean that some parameters are expected in the configuration
        args = list(fnc_name)[1:]
        fnc_name = fnc_name[0].replace("-", "")
      self._schema['post'].append({'name': fnc_name, 'args': args})
    return self

  def getJs(self, fncs=None, filter_sensitive=True):
    """

    :param fncs:
    :param filter_sensitive:

    """
    val = self.jqId
    if fncs is not None:
      self.post_process(fncs)
    fnc_content_template = ["var result = []", "if (data !== null){%s} else {data = []}", "return result"]
    if self._schema['profile']:
      html_codes = [h.htmlId for h in self._report.jsSources[self._jqId]['containers']]
      if isinstance(self._schema['profile'], dict) and self._schema['profile'].get('full', False):
        fnc_content_template = ["var t0 = performance.now()", "var result = []", "if (data !== null){%s} else {data = []}",
            "console.log('-----------')",
            "console.log('htmlCodes [%s]')" % ",".join(html_codes),
            "console.log('Function: '+ arguments.callee.name +', count records: '+ data.length +', time: '+ (performance.now()-t0) +' ms.')",
            "console.log('Arguments -')",
            "for(var i = 1; i < arguments.length; i++){console.log('   ' + i +': '+ JSON.stringify(arguments[i]))}",
            "console.log()",
            "console.log('Input Data -')", "console.log(arguments[0])", "console.log()",
            "console.log('Output Data -')", "console.log(result)", "console.log()", "return result"]
      else:
        fnc_content_template = ["var t0 = performance.now()", "var result = []", "if (data !== null){%s} else {data = []}",
                                "console.log('||%s('+arguments.callee.name+')|'+ (performance.now()-t0)+ '|records:'+ data.length)" % ";".join(html_codes),
                                "return result"]
    fnc_content_template = "; ".join(fnc_content_template)
    # Add the different filtering rules
    filters, js_fncs, js_filters = [],  self._schema['fncs'], []
    dyn_filters = self._report.jsSources.get(self.jqId, {}).get('_filters', {})
    for rec_id, f in dyn_filters.items():
      filter_val = f['val'] if f['typeVal'] == 'js' else json.dumps(f['val'])
      js_filters.append("{allIfEmpty: %s, colName: '%s', val: %s, op: '%s', data: '%s'}" % (json.dumps(f['allIfEmpty']), f['colName'], filter_val, f['operation'], rec_id))
    if len(js_filters) > 0 and filter_sensitive:
      jsFncs = [{'args_js': ["[%s]" % ",".join(js_filters)], 'name': 'filter'}] + js_fncs
    # Set all the Javascript functions
    for fnc in js_fncs:
      if fnc['name'] in factory['fncs']:
        if hasattr(self._report, "jsGlobal"):
          self._report.jsGlobal.fnc("%s(%s)" % (fnc['name'], factory['fncs'][fnc['name']]['params']), fnc_content_template % factory['fncs'][fnc['name']]['text'])
        else:
          print("function %s(%s) {var result = []; %s;return result};" % (fnc['name'], factory['fncs'][fnc['name']]['params'], factory['fncs'][fnc['name']]['text']))
      if fnc.get('args') is not None:
        val = "%s(%s, %s)" % (fnc['name'], val, ", ".join(["window['args_%s']['%s']" % (self._jsId, a) for a in fnc['args']]))
      elif fnc.get('args_js') is not None:
        # TODO: Remove this hack done for the filter function
        val = "%s(%s, %s)" % (fnc['name'], val, ", ".join([a for a in fnc['args_js']]))
      else:
        val = "%s(%s)" % (fnc['name'], val)
    # Container formatting
    if self._schema['out'] is not None:
      if self._schema['out']['name'] in factory['objs']:
        print("function %s(%s){%s};" % (self._schema['out']['name'], fnc_content_template % factory['objs'][self._schema['out']]['params'], factory['objs'][self._schema['out']['name']]['text']))
      args_len = len(self.jsArgs)
      self.jsArgs.append(dict([("chart_%s" % i, p) for i, p in enumerate(self._schema['out']['params'])]))
      if len(self._schema['out']['params']) > 3:
        js_parameters = ["window['args_%s']['chart_%s_%s']" % (self._jsId, i, args_len) for i, _ in enumerate(self._schema['out']['params'])]
        val = "%s(%s, %s, [%s])" % (self._schema['out']['name'], val, ",".join(js_parameters[:2]), ",".join(js_parameters[2:]))
      else:
        val = "%s(%s, %s)" % (self._schema['out']['name'], val, ",".join(["window['args_%s']['chart_%s_%s']" % (self._jsId, i, args_len) for i, _ in enumerate(self._schema['out']['params'])]))
    # Post process function
    for fnc in self._schema['post']:
      fnc_name = fnc['name']
      if fnc_name in factory['fncs']:
        if hasattr(self._report, "jsGlobal"):
          self._report.jsGlobal.fnc("%s(%s)" % (fnc_name, factory['fncs'][fnc_name]['params']), fnc_content_template % factory['fncs'][fnc_name]['text'])
        else:
          print("function %s(%s) {%s" % (fnc_name, factory['fncs'][fnc_name]['params'], fnc_content_template % factory['fncs'][fnc_name]['text']))
      if fnc['args']:
        val = "%s(%s, %s)" % (fnc_name, val, ", ".join([json.dumps(a) for a in fnc['args']]))
      else:
        val = "%s(%s)" % (fnc_name, val)
    js_args_definition = {}
    for i, vals in enumerate(self.jsArgs):
      for k, v in vals.items():
        js_args_definition["%s_%s" % (k, i)] = v
    self._report.jsGlobal.add("args_%s = %s" % (self._jsId, json.dumps(js_args_definition)))
    return val

  def toTsv(self, process='input'):
    """

    :return: A String with the Javascript function to be used
    """
    self._report.jsGlobal.fnc("ToTsv(data, colNames)", "%s; return result" % jsText.JsTextTsv().value)
    return "ToTsv(%s, %s)" % (self.jqId, json.dumps(list(self._schema['keys'] | self._schema['values'])))


class JsData(object):

  def __init__(self, src):
    self._src = src

  def loop(self):
    return DataLoop()

  def reduce(self):
    return DataReduce()

  def sort(self):
    return DataSort()

  def each(self):
    return DataEach()

  def crossfilter(self, data, var_name):
    """

    :param data:

    :return:
    """
    return CrossFilter(self._src, varName=var_name, data=data)

  def dataset(self, data):
    """

    :param data:

    :return:
    """
    return VisDataSet(self._src, data)

  def records(self, data):
    return RawData(self._src, data)
