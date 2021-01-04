#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html.graph import GraphChartJs
from epyk.core.html.options import OptChartJs


class Choropleth(GraphChartJs.Chart):
  name = 'ChartJs Choropleth'
  requirements = ('chartjs-chart-geo', )
  geo_map = "https://unpkg.com/world-atlas/countries-50m.json"

  def __init__(self, report, width, height, htmlCode, options, profile):
    super(Choropleth, self).__init__(report, width, height, htmlCode, options, profile)
    self._attrs['type'] = 'choropleth'

  @property
  def options(self):
    """
    Description:
    -----------

    :rtype: OptChartJs.OptionsGeo
    """
    if self._options is None:
      self._options = OptChartJs.OptionsGeo(self._report, attrs=self._options_init)
    return self._options

  def build(self, data=None, options=None, profile=False):
    # https://unpkg.com/world-atlas/countries-50m.json
    return '''
        fetch('%(map)s').then(
          function(r){r.json().then(function(geoData){
              var chartContext = %(ctx)s; var chartData = %(data)s;
              chartContext.data = {labels: [], datasets: [{label: 'Countries', data: []}]};
              const countries = ChartGeo.topojson.feature(geoData, geoData.objects.countries).features;
              countries.forEach(function(g){
                  chartContext.data.labels.push(g.properties.name);
                  if (g.properties.name in chartData){ chartContext.data.datasets[0].data.push({value: chartData[g.properties.name], feature: g})}
                  else {chartContext.data.datasets[0].data.push({value: 0, feature: g})}
              })
              %(chartId)s = new Chart(%(varId)s.getContext("2d"), chartContext)
          })}
        )
        ''' % {"chartId": self.chartId, "varId": self.dom.varId, "data": data, "ctx": self.getCtx(), 'map': self.geo_map}


class ChoroplethUs(Choropleth):
  name = 'ChartJs Choropleth US'
  geo_map = "https://unpkg.com/us-atlas/states-10m.json"

  @property
  def options(self):
    """
    Description:
    -----------

    :rtype: OptChartJs.OptionsGeo
    """
    if self._options is None:
      self._options = OptChartJs.OptionsGeo(self._report, attrs=self._options_init)
    return self._options

  def build(self, data=None, options=None, profile=False):
    return '''
        fetch('%(map)s').then(
          function(r){r.json().then(function(geoData){
              const nation = ChartGeo.topojson.feature(geoData, geoData.objects.nation).features[0];
              const states = ChartGeo.topojson.feature(geoData, geoData.objects.states).features;
              var chartContext = %(ctx)s; var chartData = %(data)s;
              chartContext.data = {labels: [], datasets: [{label: 'Countries', outline: nation, data: []}]};
              states.forEach(function(g){
                  chartContext.data.labels.push(g.properties.name);
                  if (g.properties.name in chartData){ chartContext.data.datasets[0].data.push({value: chartData[g.properties.name], feature: g})}
                  else {chartContext.data.datasets[0].data.push({value: 0, feature: g})}
              })
              %(chartId)s = new Chart(%(varId)s.getContext("2d"), chartContext)
          })}
        )
        ''' % {"chartId": self.chartId, "varId": self.dom.varId, "data": data, "ctx": self.getCtx(), 'map': self.geo_map}


class ChoroplethCountry(Choropleth):
  name = 'ChartJs Choropleth Country'
  geo_map = "https://raw.githubusercontent.com/markmarkoh/datamaps/master/src/js/data/fra.json"

  @property
  def options(self):
    """
    Description:
    -----------

    :rtype: OptChartJs.OptionsGeo
    """
    if self._options is None:
      self._options = OptChartJs.OptionsGeo(self._report, attrs=self._options_init)
    return self._options

  def build(self, data=None, options=None, profile=False):
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
        )
        ''' % {"chartId": self.chartId, "varId": self.dom.varId, "ctx": self.getCtx(), 'map': self.geo_map}

