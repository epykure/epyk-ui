"""

"""


from epyk.core.js.configs import JsConfig


class D3Base(JsConfig.JsConfig):
  """
  Base Class for the ChartJs Charts
  """
  jsCls = 'D3Chart'
  jsType = None

  def title(self, text, cssAttr=None, d3Attr=None):
    """

    :param text:
    :param cssAttr:
    :param d3Attr:
    :return:
    """
    return '''
      .append("text").attr("y", 6).attr("x", width / 2).attr("dy", ".71em").attr("text-anchor", "center")
        .style("border", "1px solid pink").style('text-align', 'center').style("font-size", "14px") 
        .attr("fill", $('body').css('color')).text("%(text)s");
      ''' % {"text": text}

  def resize(self):
    return '''
      svg.attr("viewBox", "0 0 " + width + " " + height).attr("perserveAspectRatio", "xMinYMid").call(resize);
      d3.select(window).on("resize." + container.attr("id"), resize);
      function resize() {
            var targetWidth = parseInt(container.style("width"));
            svg.attr("width", targetWidth);
            svg.attr("height", Math.round(targetWidth / aspect))};    
      '''

  def axis(self, scale, orient, tick, tickFormat):
    """

    :param scale:
    :param orient:
    :param tick:
    :param tickFormat:
    :return:
    """
    return ""


class D3Bubble2(D3Base):
  """

  Documentation
  http://bl.ocks.org/d3noob/8952219
  """
  alias = 'd3bar'
  listAttributes = []
  _attrs = {'type': 'bar', 'options': {}}
  jsCls = 'D3BubbleChart'
  name = 'Bar Chart'
  jsClsParams = ['htmlId', 'chartDef']
  jsClassDefinition = '''
    d3.select('#' + htmlId).selectAll('svg').remove();
    
    var data = [{salesperson: 3, sales: 40}, {salesperson: 500, sales: 4}];
    var x = d3.scaleBand([0, 30000]);
    var y = d3.scaleLinear().range([300, 0]);
   
    x.domain(data.map(function(d) { return d.salesperson; }));
    y.domain([0, d3.max(data, function(d) { return d.sales })]);
    
    var svg = d3.select('#' + htmlId).append("svg").attr("width", 100).attr("height", 100).append("g");
      
    svg.append("g").call(d3.axisBottom(x));
  
    svg.append("g").call(d3.axisLeft(y));
    '''


class D3Bubble(D3Base):
  """

  Documentation
  https://d3js.org/
  """
  alias = 'gravity'
  listAttributes = []
  jsType = 'gravity'
  jsCls = 'D3BubbleChart'
  jsClsParams = ['htmlId', 'chartDef']
  name = 'Bubble Chart'
  _attrs = {'type': 'bubble', 'options': {'padding': 1.5, 'clusterPadding': 6, 'maxRadius': 12}}
  jsClassDefinition = '''
  this.destroy = function () { d3.select('#' + htmlId).selectAll('svg').remove() };
  
  var container = d3.select(d3.select('#' + htmlId).node()),
        width = parseInt(container.style("width")),
        height = parseInt(container.style("height")),
        aspect = width / height;

  dataset =  chartDef.data;
  if (dataset.length == 0) { return };
  nbSeries = dataset[0].nbSeries;
  xAxis = dataset[0].xAxis;
  seriesNames = dataset[0].seriesNames;
  color = d3.scaleOrdinal(chartDef.chart_colors);
  var min = d3.min(dataset, function(d) { return d.Count });
  var max = d3.max(dataset, function(d) { return d.Count });
  var scale = d3.scaleLinear([min, max]).range([0, height / 50]);
  var svg = d3.select('#'+htmlId).insert("svg", "legend_" + htmlId).attr("width", width).attr("height", height);
  
  svg.append("text").attr("y", 6).attr("x", width / 2).attr("dy", ".71em").attr("text-anchor", "center")
    .style("border", "1px solid pink").style('text-align', 'center').style("font-size", "14px") 
    .attr("fill", $('body').css('color')).text("Gross Domestic Product, USA");
    
  var node = svg.append("g").selectAll("circle").data(dataset).enter();
  
  var nodeCircle = node.append("circle")
      .attr("r", function(d) { return scale(getRadius(d)) })
      .attr("fill", function(d) {if (nbSeries > 1) { return color(d.Category)} else {return color(d.Name) }})
      .attr("cx", function(d) { return d.x }).attr("cy", function(d) { return d.y })
      .call(d3.drag().on("start", dragstarted).on("drag", dragged).on("end", dragended))
          .on("click", function(d) {event.bubble_data = {'name': d.Name, 'value': d.Count, 'cat': d.Category}});
  
  nodeCircle.append("title").text(function(d) { return d.Name + ": " + d.Count });
  
  var nodeText = node.append("text").text(function(d) { return d.Name })
    .attr("font-family", $('body').css('font-family')).attr("font-size", function(d){ return d.r / 10 }).attr("fill", $('body').css('color'));

  var simulation = d3.forceSimulation() 
    .force("charge", d3.forceManyBody().strength([-50])) 
    .force("center", d3.forceCenter().x(width /2).y(height / 2)) 
    .force("x", d3.forceX().strength(0.1).x(width / 2)) 
    .force("y", d3.forceY().strength(0.1).y(height / 2))
    .nodes(dataset)
    .force('collision', d3.forceCollide().strength(0.5).radius(function(d) {return scale(getRadius(d)) + chartDef.options.padding }))
    .on("tick", function(d) { 
      nodeCircle.attr("cx", function(d) { return d.x }).attr("cy", function(d) { return d.y });
      nodeText.attr("x", function(d) {return d.x }).attr("y", function(d) { return d.y })
    }); 
  
  function getRadius(node) { return node.Count } 
  
  function dragstarted(d) {if (!d3.event.active) {simulation.alphaTarget(.06).restart()}; d.fx = d.x; d.fy = d.y}
  
  function dragged(d) {d.fx = d3.event.x; d.fy = d3.event.y }
  
  function dragended(d) {if (!d3.event.active) {simulation.alphaTarget(.06)};  d.fx = null; d.fy = null }
  
  var legendY = height - 100;
  var legendHeight = 95;
  var legendYSeries = legendHeight / 2 + 20;
  var legendFontSize = 12;
  
  var legend = d3.select('#'+htmlId).append("g")
      .attr("height", legendHeight).attr("width", width)
      .append("circle").attr("r", 7).attr("fill", color(0)).attr("cx", width / 2).attr("cy", legendHeight / 2)
      .append("text").text(xAxis).attr("x", width / 2 + 10).attr("y", legendHeight / 2 + 4)
      .attr("font-family", "Arial").attr("font-size", function(d){ return legendFontSize }).attr("fill", "grey");
    
  var seriesCount = 0;
  if (nbSeries > 1)
  {
    var nbGroup = Math.ceil((nbSeries * (40 + 200 * legendFontSize)) / width);
    var seriesLegend = legend.selectAll(".recLegend");
    var legendWith = 40 + 20 * legendFontSize;
    seriesLegend.data(seriesNames)
      .enter()
      .append("rect")
      .attr('class', 'recLegend')
      .attr("x", function(d) {myX = width / nbSeries + seriesCount * legendWith ; seriesCount++; return myX})
      .attr("y", legendYSeries).attr("width", 20).attr("height", 15).attr("fill", function(d) { return color(d) })
      .append("text", function(d) {return d});
      
    seriesCount = 0;
    seriesLegend.data(seriesNames)
      .enter()
      .append("text")
      .text(function(d) {return d;})
      .attr("font-family", "Arial").attr("font-size", function(d){return legendFontSize}).attr("fill", "grey")
      .attr("x", function(d) {myX = width / nbSeries + seriesCount * legendWith + 30 ;  seriesCount++; return myX;})
      .attr("y", legendYSeries + 10)
  }
'''

