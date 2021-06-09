#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html.graph import GraphChartJs
from epyk.core.html.options import OptChartJs
from epyk.core.js.packages import JsChartJs


class Choropleth(GraphChartJs.Chart):
  name = 'ChartJs Choropleth'
  requirements = ('chartjs-chart-geo', )
  #geo_map = "https://unpkg.com/world-atlas/countries-50m.json"
  geo_map = "https://cdn.jsdelivr.net/npm/world-atlas@2/countries-10m.json"
  _option_cls = OptChartJs.OptionsGeo
  _chart__type = "choropleth"

  @property
  def options(self):
    """
    Description:
    -----------
    Property to the component options.
    Options can either impact the Python side or the Javascript builder.

    Python can pass some options to the JavaScript layer.

    :rtype: OptChartJs.OptionsGeo
    """
    return super().options

  def build(self, data=None, options=None, profile=False, component_id=None):
    # https://unpkg.com/world-atlas/countries-50m.json
    return '''
        fetch('%(map)s').then(
          function(r){r.json().then(function(geoData){
              var chartContext = %(ctx)s; var chartData = %(data)s;
              chartContext.data = {labels: [], datasets: [{label: 'Countries', data: []}]};
              const countries = ChartGeo.topojson.feature(geoData, geoData.objects.countries).features;
              countries.forEach(function(g){
                  chartContext.data.labels.push(g.properties.name);
                  if (g.properties.name in chartData){
                    chartContext.data.datasets[0].data.push({value: chartData[g.properties.name], feature: g})}
                  else {chartContext.data.datasets[0].data.push({value: 0, feature: g})}
              })
              delete chartContext.options.type;
              %(chartId)s = new Chart(%(varId)s.getContext("2d"), chartContext)
          })}
        )''' % {
      "chartId": self.chartId, "varId": self.dom.varId, "data": data, "ctx": self.getCtx(), 'map': self.geo_map}

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    return '<canvas %s></canvas>' % self.get_attrs(pyClassNames=self.style.get_classes())


class ChoroplethUs(Choropleth):
  name = 'ChartJs Choropleth US'
  geo_map = "https://unpkg.com/us-atlas/states-10m.json"
  _option_cls = OptChartJs.OptionsGeo

  @property
  def options(self):
    """
    Description:
    -----------
    Property to the component options.
    Options can either impact the Python side or the Javascript builder.

    Python can pass some options to the JavaScript layer.

    :rtype: OptChartJs.OptionsGeo
    """
    return super().options

  def build(self, data=None, options=None, profile=False, component_id=None):
    return '''
        fetch('%(map)s').then(
          function(r){r.json().then(function(geoData){
              const nation = ChartGeo.topojson.feature(geoData, geoData.objects.nation).features[0];
              const states = ChartGeo.topojson.feature(geoData, geoData.objects.states).features;
              var chartContext = %(ctx)s; var chartData = %(data)s;
              chartContext.data = {labels: [], datasets: [{label: 'Countries', outline: nation, data: []}]};
              states.forEach(function(g){
                  chartContext.data.labels.push(g.properties.name);
                  if (g.properties.name in chartData){ 
                    chartContext.data.datasets[0].data.push({value: chartData[g.properties.name], feature: g})}
                  else {chartContext.data.datasets[0].data.push({value: 0, feature: g})}
              })
              %(chartId)s = new Chart(%(varId)s.getContext("2d"), chartContext)
          })}
        )''' % {
      "chartId": self.chartId, "varId": self.dom.varId, "data": data, "ctx": self.getCtx(), 'map': self.geo_map}

  def add_dataset(self, data, label, kind=None, colors=None, opacity=None, alias=None):
    """
    Description:
    ------------
    Add a new Dataset to the chart list of Datasets.

    Usage::

    Related Pages:

      https://www.chartjs.org/docs/latest/developers/updates.html

    Attributes:
    ----------
    :param data: List. The list of points (float).
    :param label: String. The series label (visible in the legend).
    :param colors: List. Optional. The color for this series. Default the global definition.
    :param opacity: Float. Optional. The opacity level for the content.
    :param kind: String. Optional. THe series type. Default to the chart type if not supplied.
    :param alias: String. The chart alias name visible in the legend. Default the label.
    """
    data = JsChartJs.DataSetBar(self._report, attrs={})
    self._datasets.append(data)
    alias = alias or label
    #if alias not in self.options.y_columns:
    #  self.options.y_columns.append(alias)
    #  self.options.props[alias] = {"type": kind or self.options.type, 'fill': False}
    if kind == "line":
      data.fill = None
    return data


class ChoroplethCountry(Choropleth):
  name = 'ChartJs Choropleth Country'
  geo_map = "https://raw.githubusercontent.com/markmarkoh/datamaps/master/src/js/data/fra.json"
  _option_cls = OptChartJs.OptionsGeo

  @property
  def options(self):
    """
    Description:
    -----------
    Property to the component options.
    Options can either impact the Python side or the Javascript builder.

    Python can pass some options to the JavaScript layer.

    :rtype: OptChartJs.OptionsGeo
    """
    return super().options

  def build(self, data=None, options=None, profile=False, component_id=None):
    return '''
        fetch('%(map)s').then(
          function(r){r.json().then(function(geoData){
              var chartContext = %(ctx)s;
              chartContext.data = {labels: [], datasets: [{label: 'Countries', data: [] }]};
              geoData.features.forEach(function(g){
                  chartContext.data.labels.push(g.properties.name);
                  chartContext.data.datasets[0].data.push({value: Math.random()*100, feature: g});
              })
              %(chartId)s = new Chart(%(varId)s.getContext("2d"), chartContext)
              %(chartId)s.scale.projection.center([78.9629, 23.5937]).scale(1000);
          })}
        )''' % {"chartId": self.chartId, "varId": self.dom.varId, "data": data, "ctx": self.getCtx(), 'map': self.geo_map}
