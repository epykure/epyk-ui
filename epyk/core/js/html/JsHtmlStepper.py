#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtml
from epyk.core.js.objects import JsNodeDom

from epyk.core.html import Defaults
from epyk.core.js.primitives import JsObjects


class JsShapes:
  shapes = ['triangle', 'rectangle', 'circle', 'arrow']

  def _svg(self, shape_def):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param shape_def:
    """
    return '''
        var width = options.svg_style.width; var height = options.svg_style.height;
        var svgns = '%(svgns)s';
        var svg = document.createElementNS(svgns, 'svg');
        var defs = document.createElementNS(svgns, 'defs');
        var gradient = document.createElementNS(svgns, 'linearGradient');
        for (var i = 0, length = options.colors[step.status].length; i < length; i++) {
          var stop = document.createElementNS(svgns, 'stop');
          stop.setAttribute('offset', options.colors[step.status][i].offset);
          stop.setAttribute('stop-color', options.colors[step.status][i].color);
          gradient.appendChild(stop)}
        
        gradient.id = 'gradient' + step.status + htmlObj.id; gradient.setAttribute('x1', '0'); gradient.setAttribute('x2', '0'); 
        gradient.setAttribute('y1', '0'); gradient.setAttribute('y2', '1');
        defs.appendChild(gradient);
        %(shape_def)s;
        shape.setAttribute('fill', 'url(#'+ gradient.id +')');
        shape.setAttribute('name', 'signal');
        svg.setAttribute('width', width +'px');
        svg.setAttribute('height', height +'px')
        svg.setAttribute('version', '1.1');
        svg.setAttribute('xmlns', svgns);
        
        if(options.line){
          var line = document.createElementNS(svgns, 'line');
          line.setAttribute('x1', 0);
          line.setAttribute('x2', width);
          line.setAttribute('y1', height/2 );
          line.setAttribute('y2', height/2 );
          for (var key in options.line){ line.setAttribute(key, options.line[key]) }
          svg.appendChild(line);
        }
        svg.appendChild(defs); svg.appendChild(shape); htmlObj.insertBefore(svg, htmlObj.firstChild);
        
        if(typeof step.label !== "undefined"){
          const number = document.createElementNS(svg.namespaceURI, 'text');
          number.setAttributeNS(null, 'x', (width/2) +'px');
          number.setAttributeNS(null, 'y', (height/2) + 5 +'px');
          number.textContent = step.label;
          number.setAttributeNS(null, 'text-anchor', 'middle');
          number.setAttributeNS(null, 'stroke', 'black');
          number.setAttributeNS(null, 'stroke-width', '1px');
          svg.appendChild(number);
        }
        
        htmlObj.setAttribute('data-status', step.status);
      ''' % {'shape_def': shape_def, 'svgns': Defaults.SVGNS}

  def triangle(self):
    """
    Description:
    ------------

    """
    shape_def = '''
      var shape = document.createElementNS(svgns, 'polygon');
      shape.setAttribute('points', ''+ ((width)/2) + ' 0,'+ (width - 20) +' '+ height +',20 '+ height);
      shape.setAttribute('stroke', options.backgrounds[step.status]);
    '''
    return self._svg(shape_def)

  def rectangle(self):
    """
    Description:
    ------------

    """
    shape_def = '''
      var shape = document.createElementNS(svgns, 'rect');
      shape.setAttribute('stroke', options.backgrounds[step.status]);
      shape.setAttribute('width', width-20);
      shape.setAttribute('x', 10);
      shape.setAttribute('height', height);
    '''
    return self._svg(shape_def)

  def circle(self):
    """
    Description:
    ------------

    """
    shape_def = '''
      var shape = document.createElementNS(svgns, 'circle');
      shape.setAttribute('stroke', options.backgrounds[step.status]);
      shape.setAttribute('stroke-width', 1);
      shape.setAttribute('cx', width / options.circle_factor);
      shape.setAttribute('cy', height / options.circle_factor);
      shape.setAttribute('r', height / options.circle_factor);
    '''
    return self._svg(shape_def)

  def arrow(self):
    """
    Description:
    ------------

    """
    shape_def = '''
      var shape = document.createElementNS(svgns, 'polygon');
      shape.setAttribute('points', '10 0,'+ (width-30) +' 0,'+ (width-10) + ' ' + (height/2) +','+ (width-30) +' '+ height +',10 0'+ height +',25 '+ (height/2) +',10 0');
      shape.setAttribute('stroke', options.backgrounds[step.status]);
    '''
    return self._svg(shape_def)

  def custom(self, shape_def):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param shape_def:
    """
    return self._svg(shape_def)


class Step(JsNodeDom.JsDoms):

  def __init__(self, data, varName=None, setVar=False, isPyData=False, report=None, src=None):
    super(Step, self).__init__(data, varName, setVar, isPyData, report)
    self._src = src

  def colors(self, colors, status='bespoke', clear_gradient=True):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param colors: List. The list of colors to be used.
    :param status: String. Optional. The status code for the step item.
    :param clear_gradient: Boolean. Optional. Specify if the color need a gradient.
    """
    if not isinstance(colors, list):
      colors = [colors]
    clear_gradient = JsUtils.jsConvertData(clear_gradient, None)
    if not isinstance(colors[0], dict):
      s = 100 / (len(colors) - 1)
      tmp_colors = []
      for i, c in enumerate(colors):
        tmp_colors.append({"color": c, 'offset': "%s%%" % int(i * s)})
      colors = JsUtils.jsConvertData(tmp_colors, None)
    return JsObjects.JsObjects.get('''
      var gradient = document.createElementNS(%(svgns)s, 'linearGradient');
      var gradient_colors = %(colors)s;
      for (var i = 0, length = gradient_colors.length; i < length; i++) {
          var stop = document.createElementNS(%(svgns)s, 'stop');
          stop.setAttribute('offset', gradient_colors[i].offset);
          stop.setAttribute('stop-color', gradient_colors[i].color);
          gradient.appendChild(stop)}
      gradient.id = 'gradient_%(status)s'; gradient.setAttribute('x1', '0'); gradient.setAttribute('x2', '0'); 
      gradient.setAttribute('y1', '0'); gradient.setAttribute('y2', '1');
      if(%(clear_gradient)s){%(comp)s.querySelector('defs').innerHTML = '';};
      %(comp)s.querySelector('defs').appendChild(gradient);
      %(comp)s.querySelector('[name=signal]').setAttribute('fill', 'url(#'+ gradient.id +')');
      %(comp)s.querySelector('[name=signal]').setAttribute('stroke', gradient_colors[0]["color"]);
      %(comp)s.setAttribute('data-status', '%(status)s');
      ''' % {"colors": colors, 'comp': self.varName, 'svgns': JsUtils.jsConvertData(Defaults.SVGNS, None),
             'clear_gradient': clear_gradient, 'status': status})

  def success(self):
    """
    Description:
    ------------

    """
    return self.colors(self._src.options.success, status='success')

  def error(self):
    """
    Description:
    ------------

    """
    return self.colors(self._src.options.error, status='error')

  def pending(self):
    """
    Description:
    ------------

    """
    return self.colors(self._src.options.pending, status='pending')

  def waiting(self):
    """
    Description:
    ------------

    """
    return self.colors(self._src.options.waiting, status='waiting')

  def blink(self):
    """
    Description:
    ------------

    """

  @property
  def status(self):
    """
    Description:
    ------------

    """
    return JsObjects.JsObjects.get('%s.getAttribute("data-status")' % self.varName)

  def shape(self, shape, status='success', step=None):
    """
    Description:
    ------------


    Attributes:
    ----------
    :param shape: String.
    :param status: String. Optional.
    :param step: Dictionary. Optional.
    """
    step = {"status": status} if step is None else JsUtils.jsConvertData(step, None)
    return JsObjects.JsObjects.get('''
      var svgns = '%(svgns)s';
      %(comp)s.querySelector('svg').remove(); %(shape)s(%(comp)s, %(options)s, %(step)s)
      ''' % {'svgns': Defaults.SVGNS, 'comp': self.varName, 'options': json.dumps(self._src._jsStyles),
             'step': step, 'shape': shape})

  def triangle(self, status='error', step=None):
    """
    Description:
    ------------
    Hide all the panels in the drawer component.

    Attributes:
    ----------
    :param status: String. Optional.
    :param step: Dictionary. Optional.
    """
    step = {"status": status} if step is None else JsUtils.jsConvertData(step, None)
    return JsObjects.JsObjects.get('''
      %(comp)s.querySelector('svg').remove(); triangle(%(comp)s, %(options)s, %(step)s)
      ''' % {'comp': self.varName, 'options': json.dumps(self._src._jsStyles), 'step': step})

  def rectangle(self, status='success', step=None):
    """
    Description:
    ------------
    Hide all the panels in the drawer component.

    Usage::

      component.querySelector('svg').remove()

    Attributes:
    ----------
    :param status: String. Optional.
    :param step: Dictionary. Optional.
    """
    step = {"status": status} if step is None else JsUtils.jsConvertData(step, None)
    return JsObjects.JsObjects.get('''
      %(comp)s.querySelector('svg').remove(); rectangle(%(comp)s, %(options)s, %(step)s)
      ''' % {'comp': self.varName, 'options': json.dumps(self._src._jsStyles), 'step': step})

  def arrow(self, status='success', step=None):
    """
    Description:
    ------------
    Hide all the panels in the drawer component.

    Attributes:
    ----------
    :param status: String. Optional.
    :param step: Dictionary. Optional.
    """
    step = {"status": status} if step is None else JsUtils.jsConvertData(step, None)
    return JsObjects.JsObjects.get('''
      %(comp)s.querySelector('svg').remove(); arrow(%(comp)s, %(options)s, %(step)s)
      ''' % {'comp': self.varName, 'options': json.dumps(self._src._jsStyles), 'step': step})

  def circle(self, status='waiting', step=None):
    """
    Description:
    ------------
    Hide all the panels in the drawer component.

    Attributes:
    ----------
    :param status: String. Optional.
    :param step: Dictionary. Optional.
    """
    step = {"status": status} if step is None else JsUtils.jsConvertData(step, None)
    return JsObjects.JsObjects.get('''
      %(comp)s.querySelector('svg').remove(); circle(%(comp)s, %(options)s, %(step)s)
      ''' % {'comp': self.varName, 'options': json.dumps(self._src._jsStyles), 'step': step})

  def label(self, value):
    """
    Description:
    ------------
    Add a text label below the shape.

    Attributes:
    ----------
    :param value: String. The text to be added.
    """
    return self.querySelector('span[name=label]').innerHTML(value)

  def text(self, text, x=None, y=None, css=None):
    """
    Description:
    ------------
    Add a text on the shape.

    Attributes:
    ----------
    :param text: String. The text to be added.
    :param x: Number. Optional. The x position.
    :param y: Number. Optional. The y position.
    :param css: Dictionary. Optional. The CSS attributes.
    """
    text = JsUtils.jsConvertData(text, None)
    if y is None:
      y = self._src._jsStyles['svg_style']['height'] / 2 + 3
    if x is None:
      x = self._src._jsStyles['svg_style']['width'] / 2
    dft_css = {"text-anchor": "middle", 'fill': 'white'}
    if css is not None:
      dft_css.update(css)
    return JsObjects.JsObjects.get('''
      var newText = document.createElementNS("http://www.w3.org/2000/svg", "text");
      newText.setAttributeNS(null, 'x', %(x)s);
      newText.setAttributeNS(null, 'y', %(y)s); var css = %(css)s;
      for (var key in css){ newText.setAttributeNS(null, key, css[key]) }
      var textNode = document.createTextNode(%(text)s);
      newText.appendChild(textNode);
      %(svg)s.appendChild(newText)''' % {'text': text, 'svg': self.querySelector('svg'), 'y': y, 'x': x, 'css': dft_css})

  def blink(self, color="#FFDEB3", border="#FF9200"):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param color: String. Optional. The hexadecimal color code.
    :param border: String. Optional. The hexadeciment color code.
    """
    return JsObjects.JsObjects.get('''
      var svg_holder = %(comp)s; 
      if (svg_holder.getAttribute("data-blink") === null){
        svg_holder.setAttribute("data-blink", true);
        if (svg_holder.getAttribute("data-gradient") === null){
          svg_holder.setAttribute("data-gradient", svg_holder.querySelector('[name=signal]').getAttribute('fill') );
          svg_holder.setAttribute("data-border", svg_holder.querySelector('[name=signal]').getAttribute('stroke') );
        };
        %(colors)s
      } else {
        svg_holder.removeAttribute("data-blink");
        svg_holder.querySelector('[name=signal]').setAttribute("fill", svg_holder.getAttribute("data-gradient"));
        svg_holder.querySelector('[name=signal]').setAttribute("stroke", svg_holder.getAttribute("data-border"));
      }
      ''' % {"comp": self.varName, 'colors': self.colors([color, border], clear_gradient=False)})

  def click(self, jsFncs, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    return JsObjects.JsObjects.get('%s.addEventListener("click", function(){%s})' % (
      self.varName, JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile)))


class Stepper(JsHtml.JsHtmlRich):

  def _get_index(self):
    constructors = self._report._props.setdefault("js", {}).setdefault("constructors", {})
    constructors['StepByName'] = "function StepByName(doms, label){var index_svg = -1; doms.childNodes.forEach(function(dom, i){if(dom.querySelector('[name=label]').innerHTML == label){ index_svg = i}}); return index_svg}"
    return 'StepByName'

  @property
  def val(self):
    """
    Description:
    -----------

    """
    return JsObjects.JsObjects.get("{%s: {value: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset()} }" % (
      self.htmlCode, self.content.toStr()))

  @property
  def content(self):
    """
    Description:
    -----------

    """
    return JsHtml.ContentFormatters(self._report, "%s.innerHTML" % self.varName)

  def __getitem__(self, i):
    return Step(self, src=self._src, varName=self.querySelectorAll("div[name=svg_holder]")[i], report=self._report)

  def getByLabel(self, label):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param label: String. The label value.
    """
    label = JsUtils.jsConvertData(label, None)
    return Step(self, src=self._src, varName='''
      %(holder)s.querySelectorAll('div[name=svg_holder]')[%(StepByName)s(%(holder)s, %(label)s)]''' % {
      'StepByName': self._get_index(), "holder": self.varName, 'label': label}, report=self._report)

  def addItem(self, label, tooltip="", shape='circle',  status="waiting"):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param label:
    :param tooltip:
    :param shape:
    :param status:
    """
    tooltip = JsUtils.jsConvertData(tooltip, None)
    label = JsUtils.jsConvertData(label, None)
    shape = JsUtils.jsConvertData(shape, None)
    status = JsUtils.jsConvertData(status, None)
    return '''
      if(%(StepByName)s(%(holder)s, %(label)s) == -1){
        var li = document.createElement("LI") ; var options = %(options)s;
        var span = document.createElement("SPAN"); span.setAttribute('name', 'label'); span.innerHTML = %(label)s;
        var div = document.createElement("DIV"); 
        div.setAttribute('title', %(tooltip)s);
        div.setAttribute('name', 'svg_holder');
        for (var key in options.text_style){ span.style[key] = options.text_style[key] }
        span.style.width = options.svg_style.width +"px";
  
        div.appendChild(span); li.appendChild(div);
        div.id = "svg_" + %(holder)s.childElementCount;
        window[%(shape)s](div, options, %(status)s); 
        %(holder)s.appendChild(li)}
      ''' % {'StepByName': self._get_index(), "holder": self.varName, 'status': status, 'shape': shape,
             "tooltip": tooltip, 'label': label, 'options': json.dumps(self._src._jsStyles)}

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
    Hide all the panels in the drawer component.
    """
    return JsHtml.ContentFormatters(self._report, ''' 
      (function(doms, contents){var index =-1; doms.childNodes.forEach(function(dom, k){if(dom.style.display !== 'none'){index = k}}); 
        if (index >= 0){return contents.childNodes[index].innerHTML} else{return index}  })(%s, %s)
        ''' % (self.querySelector("div[name=drawer_panels]"), self.querySelector("div[name=drawer_content]")))

  def hide(self):
    """
    Description:
    ------------
    Hide all the panels in the drawer component.
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
    :param link: String.
    :param panel: String. Optional
    """
    return JsObjects.JsObjects.get('''
      ''' % self.querySelectorAll("[name=drawer_panels]"))

  def delete(self, i):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param i: Integer.
    """
    return JsObjects.JsObjects.get(''' 
          %(panel)s.childNodes[%(i)s].remove(); %(drawer)s.childNodes[%(i)s].remove(); 
          ''' % {'panel': self.querySelector("div[name=drawer_panels]"), 'drawer': self.querySelector("div[name=drawer_content]"), 'i': i})
