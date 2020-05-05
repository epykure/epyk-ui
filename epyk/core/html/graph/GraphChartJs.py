
from epyk.core.html import Html
from epyk.core.html.options import OptChartJs

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObject

from epyk.core.js.packages import JsChartJs
from epyk.core.js.packages import JsD3


class Chart(Html.Html):
  name, category, callFnc = 'ChartJs', 'Charts', 'chartJs'

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
      self._js = JsChartJs.ChartJs(selector=self.chartId, src=self)
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

    :rtype: OptionsPolar
    """
    if self._options is None:
      self._options = OptChartJs.OptionsLine(self._report, attrs=self._options_init)
    return self._options

  def add_dataset(self, data, colors=None, opacity=None):
    """

    """
    data = JsChartJs.DataSetScatterLine(self._report, attrs={"data": data})
    data.fill = False
    data.label = self._data_attrs['labels'][len(self._datasets)]
    if colors is None:
      data.borderColor = self._report.theme.charts[len(self._datasets)]
      data.backgroundColor = self._report.theme.charts[len(self._datasets)]
    data.borderWidth = 1
    data.pointRadius = 1
    if opacity is not None:
      data.fillOpacity = opacity
    self._datasets.append(data)
    return data


class ChartBubble(Chart):
  __reqJs = ['Chart.js']

  def __init__(self, report, width, height, htmlCode, options, profile):
    super(ChartBubble, self).__init__(report, width, height, htmlCode, options, profile)
    self._attrs['type'] = 'bubble'

  def add_dataset(self, data, colors=None, opacity=0.8):
    """

    """
    data = JsChartJs.DataSetBubble(self._report, attrs={"data": data})
    data.fill = False
    data.label = self._data_attrs['labels'][len(self._datasets)]
    if colors is None:
      data.borderColor = self._report.theme.charts[len(self._datasets)]
      data.backgroundColor = self._report.theme.charts[len(self._datasets)]
      data.fillOpacity = opacity
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

  def add_dataset(self, data, type=None, colors=None, opacity=0.8):
    """

    :return:
    """
    if type is not None:
      data = JsChartJs.DataSetBar(self._report, attrs={"data": data, 'type': type})
    else:
      data = JsChartJs.DataSetBar(self._report, attrs={"data": data})
    self._datasets.append(data)
    data.label = self._data_attrs['labels'][len(self._datasets)]
    if colors is None:
      data.backgroundColor = self._report.theme.charts[len(self._datasets)]
      data.fillOpacity = opacity
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

  def add_dataset(self, data, type=None, colors=None, opacity=0.4):
    """

    :return:
    """
    if type is not None:
      data = JsChartJs.DataSetPolar(self._report, attrs={"data": data, 'type': type})
    else:
      data = JsChartJs.DataSetPolar(self._report, attrs={"data": data})
    self._datasets.append(data)
    data.label = self._data_attrs['labels'][len(self._datasets)]
    #if colors is None:
    data.backgroundColor = self._report.theme.charts
    data.fillOpacity = opacity
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

  def add_dataset(self, data, colors=None, opacity=0.8):
    """

    :return:
    """
    data = JsChartJs.DataSetPie(self._report, attrs={"data": data})
    self._datasets.append(data)
    if colors is None:
      data.backgroundColor = self._report.theme.charts
      data.fillOpacity = opacity
    return data


class ChartRadar(Chart):
  __reqJs = ['Chart.js']

  def __init__(self, report, width, height, htmlCode, options, profile):
    super(ChartRadar, self).__init__(report, width, height, htmlCode, options, profile)
    self._attrs['type'] = 'radar'

  def add_dataset(self, data, colors=None, opacity=0.4):
    """

    """
    data = JsChartJs.DataSetRadar(self._report, attrs={"data": data})
    self._datasets.append(data)
    if colors is None:
      data.backgroundColor = self._report.theme.charts[len(self._datasets)]
      data.borderColor = self._report.theme.charts[len(self._datasets)]
      data.borderWidth = 0.2
      data.fillOpacity = opacity
    return data


class ChartScatter(Chart):
  __reqJs = ['Chart.js']

  def __init__(self, report, width, height, htmlCode, options, profile):
    super(ChartScatter, self).__init__(report, width, height, htmlCode, options, profile)
    self._attrs['type'] = 'scatter'

  def add_dataset(self, data, colors=None):
    """

    :return:
    """
    data = JsChartJs.DataSetScatterLine(self._report, attrs={"data": data})
    data.fill = False
    data.label = self._data_attrs['labels'][len(self._datasets)]
    if colors is None:
      data.backgroundColor = self._report.theme.charts[len(self._datasets)]
      data.borderColor = self._report.theme.charts[len(self._datasets)]
    self._datasets.append(data)
    return data
