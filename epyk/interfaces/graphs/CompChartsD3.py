
import os

from epyk.core.html.graph import GraphD3


class D3(object):

  def __init__(self, context):
    self.parent = context
    self.chartFamily = "D3"

  def script(self, name, scripts, data=None, d3_version=None, dependencies=None, profile=None, options=None, width=(400, "px"), height=(330, "px"), htmlCode=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param name:
    :param scripts:
    :param d3_version:
    :param dependencies:
    """
    scripts = [os.path.split(script) for script in scripts]

    dependencies = dependencies or []
    self.parent.context.rptObj.ext_packages = self.parent.context.rptObj.ext_packages or {}
    dependencies.append({'alias': 'd3', 'version': d3_version} if d3_version is not None else "d3")

    self.parent.context.rptObj.ext_packages[name] = {
        'version': '', 'req': [{'alias': d} if not isinstance(d, dict) else d for d in dependencies],
        'register': {'alias': name, 'module': scripts[0][1][:-3]},
        'modules': [{'script': split_url[1], 'path': '', 'cdnjs': split_url[0]} for split_url in scripts]}
    self.parent.context.rptObj.jsImports.add(name)
    d3_chart = GraphD3.Script(self.parent.context.rptObj, data or [], width, height, htmlCode, options or {}, profile)
    d3_chart.builder_name = "%s%s" % (d3_chart.builder_name, name)
    self.parent.context.register(d3_chart)
    return d3_chart

  def cloud(self, data, width=(300, "px"), height=(330, "px"), htmlCode=None, options=None, profile=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param data:
    :param width:
    :param height:
    :param htmlCode:
    :param options:
    :param profile:
    """
    scripts = ["https://cdnjs.cloudflare.com/ajax/libs/d3-cloud/1.2.5/d3.layout.cloud.min.js"]
    chart = self.script('cloud', scripts, None, profile=profile, options=options, width=width, height=height, htmlCode=htmlCode)
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
