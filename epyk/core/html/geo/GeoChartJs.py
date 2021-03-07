#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html.graph import GraphChartJs
from epyk.core.html.options import OptChartJs


class Choropleth(GraphChartJs.Chart):
  name = 'ChartJs Choropleth'
  requirements = ('chartjs-chart-geo', )
  geo_map = "https://unpkg.com/world-atlas/countries-50m.json"
  _option_cls = OptChartJs.OptionsGeo

  def __init__(self, report, width, height, html_code, options, profile):
    super(Choropleth, self).__init__(report, width, height, html_code, options, profile)
    self._attrs['type'] = 'choropleth'

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
              %(chartId)s = new Chart(%(varId)s.getContext("2d"), chartContext)
          })}
        )''' % {
      "chartId": self.chartId, "varId": self.dom.varId, "data": data, "ctx": self.getCtx(), 'map': self.geo_map}


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
              chartContext.data = {labels: [], datasets: [{label: 'Countries', data: []}]};
              geoData.features.forEach(function(g){
                  chartContext.data.labels.push(g.properties.name);
                  chartContext.data.datasets[0].data.push({value: Math.random()*100, feature: g});
              })
              %(chartId)s = new Chart(%(varId)s.getContext("2d"), chartContext)
          })}
        )''' % {"chartId": self.chartId, "varId": self.dom.varId, "ctx": self.getCtx(), 'map': self.geo_map}
