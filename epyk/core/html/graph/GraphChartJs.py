
from epyk.core.html import Html
from epyk.core.html.options import OptChartJs

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObject

from epyk.core.js.packages import JsChartJs
from epyk.core.js.packages import JsD3


class Chart(Html.Html):
  name, category, callFnc = 'ChartJs', 'Charts', 'chartJs'
  data_out, data_format = 'chartjs', 'y'

  def __init__(self,  report, width, height, htmlCode, options, profile):
    self.height = height[0]
    super(Chart, self).__init__(report, [], code=htmlCode, css_attrs={"width": width, "height": height}, profile=profile)
    self._d3, self._chart, self._datasets, self._options, self._data_attrs, self._attrs = None, None, [], None, {}, {}
    self._options_init = options
    self.style.css.margin_top = 10

  @property
  def chartId(self):
    """
    Description:
    -----------
    Return the Javascript variable of the chart
    """
    return "%s_obj" % self.htmlId

  @property
  def d3(self):
    if self._d3 is None:
      self._d3 = JsD3.D3Select(self._report, selector="d3.select('#%s')" % self.htmlId, setVar=False)
    return self._d3

  @property
  def js(self):
    """
    Description:
    -----------
    Javascript base function

    Return all the Javascript functions defined in the framework.
    THis is an entry point to the full Javascript ecosystem.

    :return: A Javascript object

    :rtype: JsChartJs.JsChart
    """
    if self._js is None:
      self._js = JsChartJs.ChartJs(selector="window['%s']" % self.chartId, src=self)
    return self._js

  @property
  def options(self):
    """
    Description:
    -----------

    :rtype: OptChartJs.Options
    """
    if self._options is None:
      self._options = OptChartJs.Options(self._report, attrs=self._options_init)
    return self._options

  def labels(self, labels):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param labels:
    """
    self._data_attrs['labels'] = labels
    return self

  def label(self, i, name):
    """
    Description:
    -----------
    Change the series name

    Attributes:
    ----------
    :param i: Integer. The series index according to the y_columns
    :param name: String. The new name to be set
    """
    self.dataset(i).label = name
    return self

  def dataset(self, i=None):
    """
    Description:
    -----------

    :rtype: JsChartJs.DataSetPie
    """
    if i is None:
      return self._datasets[-1]

    return self._datasets[i]

  def click(self, jsFncs, profile=False):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFncs:
    :param profile:
    """
    if self._attrs['type'] in ['pie']:
      tmpJsFncs = ["console.log(%s)" % self.chartId, "var activePoints = %s.getSegmentsAtEvent(event)" % self.chartId]
      tmpJsFncs.append("if(activePoints.length > 0){ %s }" % JsUtils.jsConvertFncs(jsFncs, toStr=True))
    else:
      tmpJsFncs = ["var activePoints = %s.getElementsAtEvent(event)" % self.chartId]
      tmpJsFncs.append("if(activePoints.length > 0){ %s }" % JsUtils.jsConvertFncs(jsFncs, toStr=True))
    return super(Chart, self).click(tmpJsFncs, profile)

  def hover(self, jsFncs, profile=False):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFncs:
    :param profile:
    """
    tmpJsFncs = ["var activePoints = %s.getElementsAtEvent(event)" % self.chartId]
    tmpJsFncs.append("if(activePoints.length > 0){ %s }" % JsUtils.jsConvertFncs(jsFncs, toStr=True))
    return self.on("mouseover", tmpJsFncs, profile)

  @property
  def datasets(self):
    return self._datasets

  def getCtx(self):
    obj_datasets = "[%s]" % ", ".join([d.toStr() for d in self._datasets])
    self._data_attrs['datasets'] = JsObject.JsObject.get(obj_datasets)
    obj_data = "{%s}" % ", ".join(["%s: %s" % (k, JsUtils.jsConvertData(v, None)) for k, v in self._data_attrs.items()])
    self._attrs["data"] = JsObject.JsObject.get(obj_data)
    self._attrs["options"] = JsObject.JsObject.get(str(self.options))
    str_ctx = "{%s}" % ", ".join(["%s: %s" % (k, JsUtils.jsConvertData(v, None)) for k, v in self._attrs.items()])
    return str_ctx

  def build(self, data=None, options=None, profile=False):
    if data:
      dft_options = dict(self._options_init)
      dft_options.update(options or {})
      if self.data_format == 'xyz':
        js_data = getattr(getattr(self._report.data.js(data), self.data_out), self.data_format)(dft_options['y_columns'], dft_options['x_column'], dft_options['z_columns'])
      else:
        js_data = getattr(getattr(self._report.data.js(data), self.data_out), self.data_format)(dft_options['y_columns'], dft_options['x_column'])
      recordsset = []
      for i, d in enumerate(js_data['datasets']):
        recordsset.append(self.new_dataset(i, d, self._options_init['y_columns'][i]).toStr())
      return "window['%(chartId)s'].data.labels = %(labels)s; window['%(chartId)s'].data.datasets = [%(recordsset)s]; window['%(chartId)s'].update()" % {'labels': js_data['labels'], 'recordsset': ",".join(recordsset),  'chartId': self.chartId}

    return '%s = new Chart(%s.getContext("2d"), %s)' % (self.chartId, self.dom.varId, self.getCtx())

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '<canvas %s></canvas>' % self.get_attrs(pyClassNames=self.style.get_classes())


class Datasets(object):

  def __init__(self, report):
    self._report, self.__data = report, []

  def add(self, data):
    self.__data.append(data)
    return self


class ChartLine(Chart):
  __reqJs = ['Chart.js']

  def __init__(self, report, width, height, htmlCode, options, profile):
    super(ChartLine, self).__init__(report, width, height, htmlCode, options, profile)
    self._attrs['type'] = 'line'

  @property
  def options(self):
    """
    Description:
    ------------

    :rtype: OptionsPolar
    """
    if self._options is None:
      self._options = OptChartJs.OptionsLine(self._report, attrs=self._options_init)
    return self._options

  def new_dataset(self, id, data, label, colors=None, opacity=0.8, type=None):
    data = JsChartJs.DataSetScatterLine(self._report, attrs={"data": data})
    data.fill = False
    data.label = label
    if colors is None:
      data.borderColor = self._report.theme.charts[id]
      data.backgroundColor = self._report.theme.charts[id]
    data.borderWidth = 1
    data.pointRadius = 5
    if opacity is not None:
      data.fillOpacity = opacity
    return data

  def add_dataset(self, data, label="", colors=None, opacity=None):
    """
    Description:
    ------------

    :param data:
    :param label:
    :param colors:
    :param opacity:
    """
    data = self.new_dataset(len(self._datasets), data, label, colors=colors, opacity=opacity, type=None)
    self._datasets.append(data)
    return data


class ChartBubble(Chart):
  __reqJs = ['Chart.js']
  data_format = 'xyz'

  def __init__(self, report, width, height, htmlCode, options, profile):
    super(ChartBubble, self).__init__(report, width, height, htmlCode, options, profile)
    self._attrs['type'] = 'bubble'

  def new_dataset(self, id, data, label, colors=None, opacity=0.8, type=None):
    data = JsChartJs.DataSetBubble(self._report, attrs={"data": data})
    data.fill = False
    data.label = label
    if colors is None:
      data.borderColor = self._report.theme.charts[id]
      data.backgroundColor = self._report.theme.charts[id]
      data.fillOpacity = opacity
    return data

  def add_dataset(self, data, label, colors=None, opacity=0.8):
    """

    """
    data = self.new_dataset(len(self._datasets), data, label, colors, opacity=opacity)
    self._datasets.append(data)
    return data


class ChartBar(Chart):
  __reqJs = ['Chart.js']

  def __init__(self, report, width, height, htmlCode, options, profile):
    super(ChartBar, self).__init__(report, width, height, htmlCode, options, profile)
    self._attrs['type'] = 'bar'

  @property
  def options(self):
    """

    :rtype: OptionsPolar
    """
    if self._options is None:
      self._options = OptChartJs.OptionsBar(self._report, attrs=self._options_init)
    return self._options

  def new_dataset(self, id, data, label, colors=None, opacity=0.8, type=None):
    if type is not None:
      data = JsChartJs.DataSetBar(self._report, attrs={"data": data, 'type': self._attrs['type']})
    else:
      data = JsChartJs.DataSetBar(self._report, attrs={"data": data})
    data.label = label
    if colors is None:
      data.backgroundColor = self._report.theme.charts[id]
      data.fillOpacity = opacity
    return data

  def add_dataset(self, data, type=None, colors=None, opacity=0.8):
    """

    """
    data = self.new_dataset(len(self._datasets), data, self._data_attrs['labels'][len(self._datasets)-1], colors, opacity=opacity, type=type)
    self._datasets.append(data)
    return data


class ChartPolar(Chart):
  __reqJs = ['Chart.js']

  def __init__(self, report, width, height, htmlCode, options, profile):
    super(ChartPolar, self).__init__(report, width, height, htmlCode, options, profile)
    self._attrs['type'] = 'polarArea'

  @property
  def options(self):
    """

    :rtype: OptionsPolar
    """
    if self._options is None:
      self._options = OptChartJs.OptionsPolar(self._report, attrs=self._options_init)
    return self._options

  def new_dataset(self, id, data, label, colors=None, type=None):
    if type is not None:
      data = JsChartJs.DataSetPolar(self._report, attrs={"data": data, 'type': type})
    else:
      data = JsChartJs.DataSetPolar(self._report, attrs={"data": data})
    data.label = label
    data.backgroundColor = self._report.theme.charts
    return data

  def add_dataset(self, data, label, colors=None, opacity=0.4, type=None):
    """

    :return:
    """
    data = self.new_dataset(len(self._datasets), data, label, colors)
    self._datasets.append(data)
    return data


class ChartHBar(ChartBar):
  __reqJs = ['Chart.js']

  def __init__(self, report, width, height, htmlCode, options, profile):
    super(ChartBar, self).__init__(report, width, height, htmlCode, options, profile)
    self._attrs['type'] = 'horizontalBar'


class ChartPie(Chart):
  __reqJs = ['Chart.js']

  def __init__(self, report, width, height, htmlCode, options, profile):
    super(ChartPie, self).__init__(report, width, height, htmlCode, options, profile)
    self._attrs['type'] = 'pie'

  @property
  def options(self):
    """

    :rtype: OptionsPie
    """
    if self._options is None:
      self._options = OptChartJs.OptionsPie(self._report, attrs=self._options_init)
    return self._options

  def new_dataset(self, id, data, label="", colors=None, opacity=0.8, type=None):
    data = JsChartJs.DataSetPie(self._report, attrs={"data": data})
    if colors is None:
      data.backgroundColor = self._report.theme.charts
      data.fillOpacity = opacity
    return data

  def add_dataset(self, data, label="", colors=None, opacity=0.8):
    """

    :return:
    """
    data = self.new_dataset(len(self._datasets), data, label, colors=colors, opacity=opacity)
    self._datasets.append(data)
    return data


class ChartRadar(Chart):
  __reqJs = ['Chart.js']

  def __init__(self, report, width, height, htmlCode, options, profile):
    super(ChartRadar, self).__init__(report, width, height, htmlCode, options, profile)
    self._attrs['type'] = 'radar'

  def new_dataset(self, id, data, label, colors=None, opacity=0.8, type=None):
    data = JsChartJs.DataSetRadar(self._report, attrs={"data": data})
    data.label = label
    if colors is None:
      data.backgroundColor = self._report.theme.charts[id]
      data.borderColor = self._report.theme.charts[id]
      data.borderWidth = 0.2
      data.fillOpacity = opacity
    return data

  def add_dataset(self, data, label, colors=None, opacity=0.4):
    """

    """
    data = self.new_dataset(len(self._datasets), data, label, colors, opacity)
    self._datasets.append(data)
    return data


class ChartScatter(Chart):
  __reqJs = ['Chart.js']
  data_format = 'xy'

  def __init__(self, report, width, height, htmlCode, options, profile):
    super(ChartScatter, self).__init__(report, width, height, htmlCode, options, profile)
    self._attrs['type'] = 'scatter'

  def new_dataset(self, id, data, label, colors=None, type=None):
    data = JsChartJs.DataSetScatterLine(self._report, attrs={"data": data})
    data.fill = False
    data.label = label
    if colors is None:
      data.backgroundColor = self._report.theme.charts[id]
      data.borderColor = self._report.theme.charts[id]
    return data

  def add_dataset(self, data, label, colors=None):
    """

    :return:
    """
    data = self.new_dataset(len(self._datasets), data, label, colors)
    self._datasets.append(data)
    return data
