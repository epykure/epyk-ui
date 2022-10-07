

from epyk.core.html import Html
from epyk.core.css import Colors
from epyk.core.js import JsUtils
from epyk.core.js.packages import JsVega
from epyk.core.html.options import OptChartVega


class VegaEmdedCharts(Html.Html):
  name = 'Vega-Lite charts'
  requirements = ('vega-embed', )
  _option_cls = OptChartVega.OptionsChart
  _chart__type = "VegaChart"

  def __init__(self, report, data, width, height, html_code, options, profile):
    super(VegaEmdedCharts, self).__init__(report, data, html_code=html_code, profile=profile, options=options,
                                     css_attrs={"width": width, "height": height})
    self.style.css.padding = "5px 50px"
    self.options.schema = "https://vega.github.io/schema/vega-lite/v5.json"

  @property
  def chartId(self):
    """   Return the Javascript variable of the chart.
    """
    return "window['%s_obj']" % self.htmlCode

  @property
  def vega(self):
    """   JavaScript Vega Chart reference API.

    Related Pages:

      https://c3js.org/reference.html#api-show

    :return: A Javascript object

    :rtype: JsVega.VegaChart
    """
    if self._js is None:
      self._js = JsVega.Vega(self, varName=self.chartId, report=self._report)
    return self._js

  @property
  def js(self):
    """   JavaScript Vega Chart reference API.

    Related Pages:

      https://c3js.org/reference.html#api-show

    :return: A Javascript object

    :rtype: JsVega.VegaChart
    """
    if self._js is None:
      self._js = JsVega.VegaChart(self, varName=self.chartId, report=self._report)
    return self._js

  _js__builder__ = '''
    return data
  '''

  def build(self, data=None, options=None, profile=None, component_id=None):
    """
    Update the chart with context and / or data changes.

    :param data: List. Optional. The full datasets object expected by ChartJs.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param component_id: String. Not used.
    """
    if data is not None:
      js_convertor = self._chart__type
      self.page.properties.js.add_constructor(
        js_convertor, "function %s(data, options){%s}" % (js_convertor, self._js__builder__))
      profile = self.with_profile(profile, event="Builder", element_id=self.chartId)
      if profile:
        js_func_builder = JsUtils.jsConvertFncs([
          "var result = %s(data, options)" % js_convertor], toStr=True, profile=profile)
        js_convertor = "(function(data, options){%s; return result})" % js_func_builder
      return """var changeSet = vega.changeset().remove(vega.truthy).insert(%(chartFnc)s(%(data)s, %(options)s));
        %(chartId)s.then(function (res) { res.view.change('table', changeSet).run()})""" % {
        'chartId': self.chartId, 'chartFnc': js_convertor, "data": JsUtils.jsConvertData(data, None),
        "options": self.options.config_js(options)}

    return '%(chartId)s = vegaEmbed("#%(htmlCode)s", %(options)s)' % {
      "chartId": self.chartId, "htmlCode": self.htmlCode, "options": self.options.config_js(options)}

  def __str__(self):
    self.page.properties.js.add_builders(self.build())
    return '<div %s></div>' % self.get_attrs(pyClassNames=self.style.get_classes())
