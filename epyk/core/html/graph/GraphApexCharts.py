#!/usr/bin/python
# -*- coding: utf-8 -*-


from epyk.core.data.DataClass import DataClass

from epyk.core.html import Html

from epyk.core.js.packages import JsC3
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects
from epyk.core.js.packages import JsD3


class Chart(Html.Html):
  name = 'ApexCharts'
  requirements = ('apexcharts', )

  def __init__(self,  report, width, height, htmlCode, options, profile):
    self.height = height[0]
    super(Chart, self).__init__(report, [], htmlCode=htmlCode, css_attrs={"width": width, "height": height}, profile=profile)
    self._d3, self._chart, self._datasets, self._options, self._data_attrs, self._attrs = None, None, [], None, {}, {}
    self._options_init = options
    self.style.css.margin_top = 10
    self.chartId = "%s_obj" % self.htmlCode
    if hasattr(self, '_chart__type'):
      self._attrs['type'] = self._chart__type

  def build(self, data=None, options=None, profile=False):
    """
    """
    if data:
      return "Object.assign(window['%(chartId)s'].data, %(data)s); window['%(chartId)s'].update()" % {'chartId': self.chartId, 'data': self.convert(data, options, profile)}

    return '''
      var options = {
          series: [76, 67, 61, 90],
          chart: {
          height: 390,
          type: 'radialBar',
        },
        plotOptions: {
          radialBar: {
            offsetY: 0,
            startAngle: 0,
            endAngle: 270,
            hollow: {
              margin: 5,
              size: '30%%',
              background: 'transparent',
              image: undefined,
            },
            dataLabels: {
              name: {
                show: false,
              },
              value: {
                show: false,
              }
            }
          }
        },
        colors: ['#1ab7ea', '#0084ff', '#39539E', '#0077B5'],
        labels: ['Vimeo', 'Messenger', 'Facebook', 'LinkedIn'],
        legend: {
          show: true,
          floating: true,
          fontSize: '16px',
          position: 'left',
          offsetX: 160,
          offsetY: 15,
          labels: {
            useSeriesColors: true,
          },
          markers: {
            size: 0
          },
          formatter: function(seriesName, opts) {
            return seriesName + ":  " + opts.w.globals.series[opts.seriesIndex]
          },
          itemMargin: {
            vertical: 3
          }
        },
        responsive: [{
          breakpoint: 480,
          options: {
            legend: {
                show: false
            }
          }
        }]
        };
      %(chartId)s = new ApexCharts(%(varId)s, options); %(chartId)s.render()
      ''' % {"chartId": self.chartId, "varId": self.dom.varId, "options":{}}

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return '<div %s></div>' % self.get_attrs(pyClassNames=self.style.get_classes())
