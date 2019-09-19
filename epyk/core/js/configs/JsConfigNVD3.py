"""

"""


from epyk.core.js.configs import JsConfig


class JsBase(JsConfig.JsConfig):
  """
  Base Class for the C3 Charts
  """
  listAttributes = []
  jsCls = 'Chart'
  priorities = ['color', 'showValues', 'x', 'y', 'interpolate']

  def toJs(self, options=None):
    chart = dict([(key, val) for key, val in self.items() if val])
    ctx = []  # Just to ensure that the Structure of the chart component will not be changed in the python layer
    for attrOrder in self.priorities:
      if attrOrder in chart:
        if isinstance(chart[attrOrder], dict):
          for subKey, subVal in chart[attrOrder].items():
            ctx.append("%s.%s(%s)" % (attrOrder, subKey, subVal))
        else:
          ctx.append("%s(%s)" % (attrOrder, chart[attrOrder]))
        del chart[attrOrder]
    for key, val in chart.items():
      if isinstance(val, dict):
        for subKey, subVal in val.items():
          ctx.append("%s.%s(%s)" % (key, subKey, subVal))
      else:
        ctx.append("%s(%s)" % (key, val))
    axis = []
    #for key, vals in self.axis.items():
    #  axis.append("%s.%s.%s" % ('%s_chart' % self.chartId, key, ".".join(["%s(%s)" % (subKey, val) for subKey, val in vals.items()])))
    return 'nv.models.%s().%s' % (self.chartObj, ".".join(ctx))


# ---------------------------------------------------------------------------------------------------------
#                                          NVD3 Configurations
# ---------------------------------------------------------------------------------------------------------
class JsBar(JsBase):
  """
  Configuration for a Bars Chart in NVD3
  """
  alias = 'nvd3barTest'
  name = 'Bars'
  eventObject = 'discretebar'
  chartObj = 'discreteBarChart'
  _attrs = {
    'staggerLabels': True,
  }


class JsMultiBar(JsBase):
  """
  Configuration for a Multi Bars Chart in NVD3
  """
  alias = 'nvd3bar'
  name = 'Bars'
  eventObject = 'discretebar'
  chartObj = 'multiBarChart'
  _attrs = {
    'reduceXTicks': True, 'showControls': True, 'groupSpacing': 0.1, 'rotateLabels': -15, 'showLegend': True
  }


class JsSunburst(JsBase):
  """
  Configuration for a Multi Bars Chart in NVD3
  """
  alias = 'sunburst'
  name = 'Sunburst'
  eventObject = 'discretebar'
  chartObj = 'sunburstChart'
  _attrs = {
    'mode': 'value'
  }
