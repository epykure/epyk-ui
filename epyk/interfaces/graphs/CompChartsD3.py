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

    Usage:
    -----

    Related Pages:

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

      dependencies = dependencies or []
      self.page.ext_packages = self.page.ext_packages or {}
      dependencies.append({'alias': 'd3', 'version': d3_version} if d3_version is not None else "d3")

      self.page.ext_packages[name] = {
          'version': '', 'req': [{'alias': d} if not isinstance(d, dict) else d for d in dependencies],
          'register': {'alias': name, 'module': scripts[0][1][:-3]},
          'modules': [{'script': split_url[1], 'path': '', 'cdnjs': split_url[0]} for split_url in scripts]}
      self.page.jsImports.add(name)
    else:
      self.page.jsImports.add("d3")
    d3_chart = GraphD3.Script(self.page, data or [], width, height, html_code, options or {}, profile)
    d3_chart.builder_name = "%s%s" % (d3_chart.builder_name, name)
    return d3_chart

  def cloud(self, data, width=(300, "px"), height=(330, "px"), html_code=None, options=None, profile=None):
    """
    Description:
    -----------

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Templates:

    Attributes:
    ----------
    :param data: Object. Optional. The chart input data to be serialised.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    scripts = ["https://cdnjs.cloudflare.com/ajax/libs/d3-cloud/1.2.5/d3.layout.cloud.min.js"]
    chart = self.script(
      'cloud', scripts, None, profile=profile, options=options, width=width, height=height, html_code=html_code)
    chart.loader('''
    var layout = d3.layout.cloud().size([options.wdith, options.height])
        .words(data.map(function(d) { return {text: d, size: 10 + Math.random() * 90}; }))
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
          .attr("text-anchor", "middle")
          .attr("transform", function(d) {
            return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")"})
          .text(function(d) { return d.text; });
    }''')
    chart.data(data)
    return chart
