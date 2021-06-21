

from epyk.core.html import Html
from epyk.core.css import Colors
from epyk.core.js.packages import JsVega
from epyk.core.html.options import OptChartVega


class VegaEmdedCharts(Html.Html):
  name = 'Vega-Lite charts'
  requirements = ('vega-embed', )
  _option_cls = OptChartVega.OptionsChart

  def __init__(self, report, data, width, height, html_code, options, profile):
    super(VegaEmdedCharts, self).__init__(report, data, html_code=html_code, profile=profile, options=options,
                                     css_attrs={"width": width, "height": height})
    self.style.css.padding = "5px 50px"
    self.options.schema = "https://vega.github.io/schema/vega-lite/v5.json"

  @property
  def chartId(self):
    """
    Description:
    -----------
    Return the Javascript variable of the chart.
    """
    return "%s_obj" % self.htmlCode

  @property
  def js(self):
    """
    Description:
    -----------
    JavaScript C3 reference API.

    Related Pages:

      https://c3js.org/reference.html#api-show

    :return: A Javascript object

    :rtype: JsVega.Vega
    """
    if self._js is None:
      self._js = JsVega.Vega(self, varName=self.chartId, report=self._report)
    return self._js

  # _js__builder__ = '''
  #   console.log(options);
  #   window[htmlObj.id + '_obj'] = vegaEmbed(options, {
  #     renderer: 'canvas',
  #     container: '#' + htmlObj.id,
  #     hover: true
  #   })
  # '''

  _js__builder__ = '''
      console.log(options);
      window[htmlObj.id + '_obj'] = vegaEmbed("#"+ htmlObj.id, options)
    '''

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    return '<div %s></div>' % self.get_attrs(pyClassNames=self.style.get_classes())
