#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from epyk.core.html.graph import GraphD3


class D3:

  def __init__(self, ui):
    self.page = ui.page
    self.chartFamily = "D3"

  def script(self, name, scripts=None, data=None, d3_version=None, dependencies=None, profile=None, options=None,
             width=(400, "px"), height=(330, "px"), html_code=None):
    """
    Description:
    -----------

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://gramener.github.io/d3js-playbook/barchart.html

    Templates:

    Attributes:
    ----------
    :param name: String. The module name.
    :param scripts: List. Optional. The list of scripts.
    :param data: Object. Optional. The chart input data to be serialised.
    :param d3_version: String. Optional. Required version for the underlying D3 package.
    :param dependencies: List. Optional. The required dependency files.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    if scripts is not None:
      scripts = [os.path.split(script) for script in scripts]

      options = options or {}
      dependencies = dependencies or []
      self.page.ext_packages = self.page.ext_packages or {}
      dependencies.append({'alias': 'd3', 'version': d3_version} if d3_version is not None else "d3")

      register = {'alias': name, 'module': scripts[0][1][:-3]}
      if "init_fnc" in options:
        register = {'alias': name, 'module': scripts[0][1][:-3], "init_fnc": options["init_fnc"]}
        del options["init_fnc"]

      self.page.imports.addPackage(name, {
          'version': '', 'req': [{'alias': d} if not isinstance(d, dict) else d for d in dependencies],
          'register': register,
          'modules': [{'script': split_url[1], 'path': '', 'cdnjs': split_url[0]} for split_url in scripts]})
      self.page.jsImports.add(name)
    else:
      self.page.jsImports.add("d3")
    d3_chart = GraphD3.Script(self.page, data or [], width, height, html_code, options or {}, profile)
    d3_chart.builder_name = "%s%s" % (d3_chart.builder_name, name)
    return d3_chart

  def cloud(self, data, width=(100, "%"), height=(330, "px"), html_code=None, options=None, profile=None,
            excluded_words=None):
    """
    Description:
    -----------

    :tags:
    :categories:

    Usage::

    Related Pages:


    Attributes:
    ----------
    :param data: Object. Optional. The chart input data to be serialised.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param excluded_words: list of words to be excluded from the display.
    """
    scripts = ["https://cdnjs.cloudflare.com/ajax/libs/d3-cloud/1.2.5/d3.layout.cloud.min.js"]
    options = options or {}
    options["init_fnc"] = "d3.layout.cloud = clouds"
    chart = self.script(
      'clouds', scripts, None, "3.5.17", profile=profile, options=options, width=width, height=height,
      html_code=html_code)
    chart.colors(self.page.theme.charts)
    chart.loader(''' 
var layout = d3.layout.cloud().size([options.get_width(htmlObj.node()), options.get_height(htmlObj.node())])
    .words(data.map(function(d) { return d; }))
    .padding(5).rotate(function() { return ~~(Math.random() * 2) * 90; })
    .font("Impact").fontSize(function(d) { return d.size; }).on("end", draw);
layout.start();

function draw(words) {
  htmlObj.append("svg").attr("width", layout.size()[0]).attr("height", layout.size()[1])
    .append("g").attr("transform", "translate(" + layout.size()[0] / 2 + "," + layout.size()[1] / 2 + ")")
    .selectAll("text").data(words)
    .enter().append("text")
      .style("font-size", function(d) { return d.size + "px"; })
      .style("font-family", "Impact")
      .style("fill", function(d, i) {if(typeof d.color !== 'undefined'){return d.color} else {return options.colors[0]}})
      .attr("text-anchor", "middle")
      .attr("transform", function(d) {
        return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")"})
      .text(function(d) { return d.text; })}
''')
    if not isinstance(data, list):
      count_words = {}
      for phrase in data.split("\n"):
        for word in phrase.split(" "):
          count_words[word] = count_words.get(word, 0) + 1
        values = []
        for c, v in count_words.items():
          if excluded_words is not None and c in excluded_words:
            continue

          values.append({"text": c, "size": 10 + v * 5})
        chart.data(values)
    return chart

  def pie(self, record=None, y=None, x=None, profile=None, width=(100, "%"), height=(330, "px"),
          options=None, html_code=None):
    """
    Description:
    -----------

    Related Pages:

      https://gramener.github.io/d3js-playbook/barchart.html

    TODO Add events

        .on( "click", function(d,i) {
        console.log(d)
        }).on( "mouseover", function() {
                d3.select(this).style("fill", "red")
        }).on( "mouseout", function() {
                d3.select(this).style("fill", function(d,i) {options.colors[i]})
        })

    Attributes:
    ----------
    :param record: Object. Optional. The chart input data to be serialised.
    :param y: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    data = self.page.data.c3.y(record or [], [y], x, options={"agg":  options.get('agg', 'distinct')})
    d3_chart = GraphD3.Script(self.page, data, width, height, html_code, options or {}, profile)
    d3_chart.colors(self.page.theme.charts)
    d3_chart.builder_name = "D3Pie"
    d3_chart.loader('''
let size = Math.min(options.get_width(htmlObj.node()), options.get_height(htmlObj.node()));
var outerRadius = size / 2;
var innerRadius = 60; var j = 0;
var svg = htmlObj.append("svg").attr("width", size).attr("height", size);
var pie = d3.layout.pie();
var piedata = pie(data.datasets[0]); 
var arcs = svg.selectAll("g").data(piedata).enter().append("g").attr("transform", "translate(" + outerRadius + "," + outerRadius + ")")
var arc = d3.svg.arc().innerRadius(innerRadius).outerRadius(outerRadius)
arcs.append("path")
  .style("cursor", "pointer")
  .attr("d", arc).attr("fill", function(d, i) {if(typeof d.color !== 'undefined'){return d.color} else {return options.colors[i]} })
arcs.append("text")
    .attr("transform", function(d) {return "translate(" + arc.centroid(d) + ")"})
    .attr("text-anchor", "end")
    .text(function(d) {return d.value})
    ''')
    return d3_chart

  def bar(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
          options=None, html_code=None):
    """
    Description:
    -----------

    TODO: Handle multiple series correctly.

    Usage::

      page.ui.charts.d3.bar(mocks.languages, y_columns=["rating"], x_axis="change")

    Related Pages:

      https://gramener.github.io/d3js-playbook/barchart.html

    Attributes:
    ----------
    :param record: Object. Optional. The chart input data to be serialised.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    data = self.page.data.nvd3.xy(record or [], y_columns, x_axis, options={"agg":  options.get('agg', 'distinct')})
    d3_chart = GraphD3.Script(self.page, data, width, height, html_code, options, profile)
    d3_chart.colors(self.page.theme.charts)
    d3_chart.builder_name = "D3Bar"
    d3_chart.loader('''
var chart = htmlObj.append("svg").attr("width", options.get_width(htmlObj.node())).attr("height", options.get_height(htmlObj.node()));
var j = 0;
chart
  .selectAll('rect')
  .data(data.datasets[j]).enter()
  .append('rect')
  .attr('x', 0)
  .attr("fill", function(d, i) { if(typeof d.color !== 'undefined'){ return d.color} else {return options.colors[j]} })
  .attr('y', function(d, i) {return i * 30})
  .attr('width', function(d, i) {return Math.max(0, d.y)})
  .attr('height', 25)

chart.selectAll("text")
  .data(data.datasets[j])
  .enter()
  .append("text")
  .text(function(d) {return d.x})
  .attr("y", function(d,i) {return i*30 + 20})
  .attr("x", function(d) {return Math.max(0, d.y)})
''')
    return d3_chart

  def scatter(self, record=None, y_columns=None, x_axis=None, profile=None, width=(100, "%"), height=(330, "px"),
              options=None, html_code=None):
    """
    Description:
    -----------

    TODO: Handle multiple series correctly.

    Usage::

      page.ui.charts.d3.scatter(mocks.languages, y_columns=["rating"], x_axis="change")

    Related Pages:

      https://gramener.github.io/d3js-playbook/barchart.html

    Attributes:
    ----------
    :param record: Object. Optional. The chart input data to be serialised.
    :param y_columns: List. Optional. The columns corresponding to keys in the dictionaries in the record.
    :param x_axis: String. Optional. The column corresponding to a key in the dictionaries in the record.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    options = options or {}
    data = self.page.data.nvd3.xy(record or [], y_columns, x_axis, options={"agg":  options.get('agg', 'distinct')})
    d3_chart = GraphD3.Script(self.page, data, width, height, html_code, options or {}, profile)
    d3_chart.builder_name = "D3Scatter"
    d3_chart.colors(self.page.theme.charts)
    d3_chart.loader('''
var svg = htmlObj.append("svg").attr("width", options.get_width(htmlObj.node())).attr("height", options.get_height(htmlObj.node()));
var j = 0 ;
svg.selectAll("circle")
 .data(data.datasets[j]).enter()
 .append("circle")
 .attr("fill", function(d, i) { if(typeof d.color !== 'undefined'){ return d.color} else {return options.colors[j]} })
 .attr("cx", function(d) {return d.x})
 .attr("cy", function(d) {return d.y})
 .attr("r", function(d, i) { if(typeof d.r !== 'undefined'){ return d.r} else {return 1} })

svg.selectAll("text")
  .data(data.datasets[j]).enter()
  .append("text")
  .attr("x", function(d) {return d.x +10})
  .attr("y", function(d) {return d.y +4})
  .text(function(d) {return d.y })
  .attr("font-size", "8px");
  ''')
    return d3_chart

  def svg(self, profile=None, width=(100, "%"), height=(330, "px"), options=None, html_code=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    d3_chart = GraphD3.Script(self.page, [], width, height, html_code, options or {}, profile)
    d3_chart.builder_name = "D3Svg"
    d3_chart.colors(self.page.theme.charts)
    d3_chart.loader('htmlObj.append("svg").attr("width", options.get_width(htmlObj.node())).attr("height", options.get_height(htmlObj.node()))')
    return d3_chart
