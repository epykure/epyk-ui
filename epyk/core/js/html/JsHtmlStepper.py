
import json

from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtml
from epyk.core.js.objects import JsNodeDom

from epyk.core.js.primitives import JsObjects


class JsShapes(object):

  def _svg(self, shape, shape_def):
    return '''
      function %(shape)s(htmlObj, options){
        var width = options.svg_style.width; var height = options.svg_style.height;
        var svgns = 'http://www.w3.org/2000/svg';
        var svg = document.createElementNS(svgns, 'svg');
        var defs = document.createElementNS(svgns, 'defs');
        var gradient = document.createElementNS(svgns, 'linearGradient');
        
        for (var i = 0, length = options.colors.success.length; i < length; i++) {
          var stop = document.createElementNS(svgns, 'stop');
          stop.setAttribute('offset', options.colors.success[i].offset);
          stop.setAttribute('stop-color', options.colors.success[i].color);
          gradient.appendChild(stop)}
          
        %(shape_def)s;
        svg.setAttribute('width', width +'px');
        svg.setAttribute('height', height +'px')
        svg.setAttribute('version', '1.1');
        svg.setAttribute('xmlns', svgns);
        
        svg.appendChild(defs); svg.appendChild(shape);
        htmlObj.querySelector('svg').remove(); htmlObj.insertBefore(svg, htmlObj.firstChild);
      ''' % {"shape": shape, 'shape_def': shape_def}

  def triangle(self):
    shape_def = '''
      var shape = document.createElementNS(svgns, 'polygon');
      shape.setAttribute('points', ''+ ((width-10)/2) + ' 0,'+ (width - 10) +' '+ height +',5 '+ height);
      shape.setAttribute('stroke', 'red');
      shape.setAttribute('name', 'signal');
      shape.setAttribute('fill', 'url(#Gradient)');
    '''
    return self._svg('triangle', shape_def)

  def rectangle(self):
    shape_def = '''
      var shape = document.createElementNS(svgns, 'rectangle');
      shape.setAttribute('name', 'signal');
      shape.setAttribute('stroke', 'red');
      shape.setAttribute('fill', 'url(#Gradient)');
      shape.setAttribute('width', width);
      shape.setAttribute('height', height);
    '''
    return self._svg('triangle', shape_def)

  def circle(self):
    shape_def = '''
      var shape = document.createElementNS(svgns, 'circle');
      shape.setAttribute('stroke', 'red');
      shape.setAttribute('stroke-width', 1);
      shape.setAttribute('cx', wbubble );
      shape.setAttribute('cy', hbubble);
      shape.setAttribute('r', hbubble);
      shape.setAttribute('fill', 'url(#Gradient)');
    '''
    return self._svg('triangle', shape_def)

  def arrow(self):
    shape_def = '''
      var shape = document.createElementNS(svgns, 'polygon');
      shape.setAttribute('points', '0 0,'+ (width-20)+' 0,'+(width-5) + ' ' + ((height-10)/2) +','+ (width-20) +' '+ (height-10) +',0 0'+ (height-10) +',15 '+ ((height-10)/2) +',0 0');
      shape.setAttribute('stroke', 'red');
      shape.setAttribute('name', 'signal');
      shape.setAttribute('fill', 'url(#Gradient)');
    '''
    return self._svg('triangle', shape_def)


class Step(JsNodeDom.JsDoms):

  def __init__(self, data, varName=None, setVar=False, isPyData=False, report=None, src=None):
    super(Step, self).__init__(data, varName, setVar, isPyData, report)
    self._src = src

  def colors(self, colors):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param colors:
    """

  def blink(self):
    """
    Description:
    ------------

    """

  def triangle(self):
    """
    Description:
    ------------
    Hide all the panels in the drawer component
    """
    return JsObjects.JsObjects.get('''
      var options = %(options)s;
      var width = options.svg_style.width; var height = options.svg_style.height;
      
      var svgns = 'http://www.w3.org/2000/svg';
      var svg = document.createElementNS(svgns, 'svg');
      var defs = document.createElementNS(svgns, 'defs');
      var gradient = document.createElementNS(svgns, 'linearGradient');
      var shape = document.createElementNS(svgns, 'polygon');
      
      for (var i = 0, length = options.colors.success.length; i < length; i++) {
        var stop = document.createElementNS(svgns, 'stop');
        stop.setAttribute('offset', options.colors.success[i].offset);
        stop.setAttribute('stop-color', options.colors.success[i].color);
        gradient.appendChild(stop)}
            
      shape.setAttribute('points', ''+ ((width-10)/2) + ' 0,'+ (width - 10) +' '+ height +',5 '+ height);
      shape.setAttribute('stroke', 'red');
      shape.setAttribute('name', 'signal');
      shape.setAttribute('fill', 'url(#Gradient)');
      
      svg.setAttribute('width', width +'px');
      svg.setAttribute('height', height +'px')
      svg.setAttribute('version', '1.1');
      svg.setAttribute('xmlns', svgns);
      
      svg.appendChild(defs); svg.appendChild(shape);
      %(comp)s.querySelector('svg').remove();
      
      %(comp)s.insertBefore(svg, %(comp)s.firstChild);
      ''' % {'comp': self.varName, 'options': json.dumps(self._src._jsStyles)})

  def rectangle(self):
    """
    Description:
    ------------
    Hide all the panels in the drawer component
    """
    return JsObjects.JsObjects.get('''
      var options = %(options)s;
      var width = options.svg_style.width; var height = options.svg_style.height;

      var svgns = 'http://www.w3.org/2000/svg';
      var svg = document.createElementNS(svgns, 'svg');
      var defs = document.createElementNS(svgns, 'defs');
      var gradient = document.createElementNS(svgns, 'linearGradient');
      var shape = document.createElementNS(svgns, 'rect');

      for (var i = 0, length = options.colors.success.length; i < length; i++) {
        var stop = document.createElementNS(svgns, 'stop');
        stop.setAttribute('offset', options.colors.success[i].offset);
        stop.setAttribute('stop-color', options.colors.success[i].color);
        gradient.appendChild(stop)}

      shape.setAttribute('name', 'signal');
      shape.setAttribute('stroke', 'red');
      shape.setAttribute('fill', 'url(#Gradient)');
      shape.setAttribute('width', width);
      shape.setAttribute('height', height);
      
      svg.setAttribute('width', width +'px');
      svg.setAttribute('height', height +'px')
      svg.setAttribute('version', '1.1');
      svg.setAttribute('xmlns', svgns);
      
      svg.appendChild(defs); svg.appendChild(shape);
      %(comp)s.querySelector('svg').remove();

      %(comp)s.insertBefore(svg, %(comp)s.firstChild);
      ''' % {'comp': self.varName, 'options': json.dumps(self._src._jsStyles)})

  def arrow(self):
    """
    Description:
    ------------
    Hide all the panels in the drawer component
    """
    return JsObjects.JsObjects.get('''
      var options = %(options)s;
      var width = options.svg_style.width; var height = options.svg_style.height;

      var svgns = 'http://www.w3.org/2000/svg';
      var svg = document.createElementNS(svgns, 'svg');
      var defs = document.createElementNS(svgns, 'defs');
      var gradient = document.createElementNS(svgns, 'linearGradient');
      var shape = document.createElementNS(svgns, 'polygon');

      for (var i = 0, length = options.colors.success.length; i < length; i++) {
        var stop = document.createElementNS(svgns, 'stop');
        stop.setAttribute('offset', options.colors.success[i].offset);
        stop.setAttribute('stop-color', options.colors.success[i].color);
        gradient.appendChild(stop)}

      shape.setAttribute('points', '0 0,'+ (width-20)+' 0,'+(width-5) + ' ' + ((height-10)/2) +','+ (width-20) +' '+ (height-10) +',0 0'+ (height-10) +',15 '+ ((height-10)/2) +',0 0');
      shape.setAttribute('stroke', 'red');
      shape.setAttribute('name', 'signal');
      shape.setAttribute('fill', 'url(#Gradient)');

      svg.setAttribute('width', width +'px');
      svg.setAttribute('height', height +'px')
      svg.setAttribute('version', '1.1');
      svg.setAttribute('xmlns', svgns);

      svg.appendChild(defs); svg.appendChild(shape);
      %(comp)s.querySelector('svg').remove();

      %(comp)s.insertBefore(svg, %(comp)s.firstChild);
      ''' % {'comp': self.varName, 'options': json.dumps(self._src._jsStyles)})

  def circle(self):
    """
    Description:
    ------------
    Hide all the panels in the drawer component
    """
    return JsObjects.JsObjects.get('''
      var options = %(options)s;
      var width = options.svg_style.width; var height = options.svg_style.height;
      var bubbleFactor = 2 ;
      var wbubble = width / bubbleFactor ;
      var hbubble = height / bubbleFactor ;
      
      var svgns = 'http://www.w3.org/2000/svg';
      var svg = document.createElementNS(svgns, 'svg');
      var defs = document.createElementNS(svgns, 'defs');
      var gradient = document.createElementNS(svgns, 'linearGradient');
      var shape = document.createElementNS(svgns, 'circle');

      for (var i = 0, length = options.colors.success.length; i < length; i++) {
        var stop = document.createElementNS(svgns, 'stop');
        stop.setAttribute('offset', options.colors.success[i].offset);
        stop.setAttribute('stop-color', options.colors.success[i].color);
        gradient.appendChild(stop)}

      shape.setAttribute('stroke', 'red');
      shape.setAttribute('stroke-width', 1);
      shape.setAttribute('cx', wbubble );
      shape.setAttribute('cy', hbubble);
      shape.setAttribute('r', hbubble);
      shape.setAttribute('fill', 'url(#Gradient)');

      svg.setAttribute('width', width +'px');
      svg.setAttribute('height', height +'px')
      svg.setAttribute('version', '1.1');
      svg.setAttribute('xmlns', svgns);

      svg.appendChild(defs); svg.appendChild(shape);
      %(comp)s.querySelector('svg').remove();

      %(comp)s.insertBefore(svg, %(comp)s.firstChild);
      ''' % {'comp': self.varName, 'options': json.dumps(self._src._jsStyles)})

  def text(self, value):
    """
    Description:
    ------------

    :param value:
    """
    return self.querySelector('span[name=label]').innerHTML(value)

  def click(self, jsFncs):
    return JsObjects.JsObjects.get('%s.addEventListener("click", function(){%s})' % (self.varName, JsUtils.jsConvertFncs(jsFncs, toStr=True)))


class Stepper(JsHtml.JsHtmlRich):

  def __getitem__(self, i):
    return Step(self, src=self._src, varName=self.querySelectorAll("div[name=svg_holder]")[i], report=self._report)

  def addItem(self, shape, text):
    """
    Description:
    ------------

    """
    return ""

  def delete(self, i):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param i:
    """
    return self[i].remove()


class Drawer(JsHtml.JsHtmlRich):

  @property
  def content(self):
    """
    Description:
    ------------
    Hide all the panels in the drawer component
    """
    return JsHtml.ContentFormatters(self._report, ''' 
      (function(doms, contents){var index =-1; doms.childNodes.forEach(function(dom, k){if(dom.style.display !== 'none'){index = k}}); 
        if (index >= 0){return contents.childNodes[index].innerHTML} else{return index}  })(%s, %s)
        ''' % (self.querySelector("div[name=drawer_panels]"), self.querySelector("div[name=drawer_content]")))

  def hide(self):
    """
    Description:
    ------------
    Hide all the panels in the drawer component
    """
    return JsObjects.JsObjects.get(''' 
      (function(doms){doms.childNodes.forEach(function(dom){dom.style.display = 'none'; })})(%s)
      ''' % self.querySelector("div[name=drawer_panels]"))

  def add(self, link, panel=""):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param link:
    :param panel:
    """
    return JsObjects.JsObjects.get('''
      ''' % self.querySelectorAll("[name=drawer_panels]"))

  def delete(self, i):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param link:
    """
    return JsObjects.JsObjects.get(''' 
          %(panel)s.childNodes[%(i)s].remove(); %(drawer)s.childNodes[%(i)s].remove(); 
          ''' % {'panel': self.querySelector("div[name=drawer_panels]"), 'drawer': self.querySelector("div[name=drawer_content]"), 'i': i})
