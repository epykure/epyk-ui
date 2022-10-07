#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union, Optional
from epyk.core.py import primitives

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

    :param shape_def:
    """
    return '''
        var width = options.svg_style.width; var height = options.svg_style.height;
        var svgns = '%(svgns)s';
        var svg = document.createElementNS(svgns, 'svg');
        var defs = document.createElementNS(svgns, 'defs');
        var gradient = document.createElementNS(svgns, 'linearGradient');
        if(typeof step.status === "undefined"){step.status= "waiting"};
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
    Put a triangle shape to the step.
    """
    shape_def = '''
      var shape = document.createElementNS(svgns, 'polygon');
      shape.setAttribute('points', ''+ ((width)/2) + ' 0,'+ (width - 20) +' '+ height +',20 '+ height);
      shape.setAttribute('stroke', options.backgrounds[step.status]);
    '''
    return self._svg(shape_def)

  def rectangle(self):
    """

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

    """
    shape_def = '''
      var shape = document.createElementNS(svgns, 'polygon');
      shape.setAttribute('points', '10 0,'+ (width-30) +' 0,'+ (width-10) + ' ' + (height/2) +','+ (width-30) +' '+ height +',10 0'+ height +',25 '+ (height/2) +',10 0');
      shape.setAttribute('stroke', options.backgrounds[step.status]);
    '''
    return self._svg(shape_def)

  def custom(self, shape_def: str):
    """

    :param str shape_def:
    """
    return self._svg(shape_def)


class Step(JsNodeDom.JsDoms):

  def __init__(self, data, js_code: str = None, set_var: bool = False, is_py_data: bool = False,
               page: primitives.PageModel = None, component: primitives.HtmlModel = None):
    super(Step, self).__init__(data, js_code, set_var, is_py_data, page)
    self.component = component

  def colors(self, colors: Union[list, str, dict], status: str = 'bespoke', clear_gradient: bool = True):
    """

    :param Union[list, str, dict] colors: The list of colors to be used.
    :param str status: Optional. The status code for the step item.
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

    """
    return self.colors(self.component.options.success, status='success')

  def error(self):
    """

    """
    return self.colors(self.component.options.error, status='error')

  def pending(self):
    """

    """
    return self.colors(self.component.options.pending, status='pending')

  def waiting(self):
    """

    """
    return self.colors(self.component.options.waiting, status='waiting')

  @property
  def status(self):
    """

    """
    return JsObjects.JsObjects.get('%s.getAttribute("data-status")' % self.varName)

  def shape(self, shape: str, status: str = 'success', step: Union[primitives.JsDataModel, dict] = None,
            options: dict = None):
    """


    :param str shape: The shape alias of the step.
    :param str status: Optional. The status of the step.
    :param Union[primitives.JsDataModel, dict] step: Optional.
    :param dict options: The stepper options to be changed.
    """
    step = {"status": status} if step is None else JsUtils.jsConvertData(step, None)
    return JsObjects.JsObjects.get('''
      var svgns = '%(svgns)s';
      %(comp)s.querySelector('svg').remove(); %(shape)s(%(comp)s, %(options)s, %(step)s)
      ''' % {'svgns': Defaults.SVGNS, 'comp': self.varName, 'options': self.component.options.config_js(options),
             'step': step, 'shape': shape})

  def triangle(self, status: str = 'error', step: Union[primitives.JsDataModel, dict] = None, options: dict = None):
    """
    Hide all the panels in the drawer component.

    :param str status: Optional. The status of the step.
    :param Union[primitives.JsDataModel, dict] step: Optional.
    :param dict options: The stepper options to be changed.
    """
    step = {"status": status} if step is None else JsUtils.jsConvertData(step, None)
    return JsObjects.JsObjects.get('''
      %(comp)s.querySelector('svg').remove(); triangle(%(comp)s, %(options)s, %(step)s)
      ''' % {'comp': self.varName, 'options': self.component.options.config_js(options), 'step': step})

  def rectangle(self, status: str = 'success', step: Union[primitives.JsDataModel, dict] = None, options: dict = None):
    """
    Hide all the panels in the drawer component.

    Usage::

      component.querySelector('svg').remove()

    :param str status: Optional. The status of the step.
    :param Union[primitives.JsDataModel, dict] step: Optional.
    :param dict options: The stepper options to be changed.
    """
    step = {"status": status} if step is None else JsUtils.jsConvertData(step, None)
    return JsObjects.JsObjects.get('''
      %(comp)s.querySelector('svg').remove(); rectangle(%(comp)s, %(options)s, %(step)s)
      ''' % {'comp': self.varName, 'options': self.component.options.config_js(options), 'step': step})

  def arrow(self, status: str = 'success', step: Union[primitives.JsDataModel, dict] = None, options: dict = None):
    """
    Hide all the panels in the drawer component.

    :param str status: Optional. The status of the step.
    :param Union[primitives.JsDataModel, dict] step: Optional.
    :param dict options: The stepper options to be changed.
    """
    step = {"status": status} if step is None else JsUtils.jsConvertData(step, None)
    return JsObjects.JsObjects.get('''
      %(comp)s.querySelector('svg').remove(); arrow(%(comp)s, %(options)s, %(step)s)
      ''' % {'comp': self.varName, 'options': self.component.options.config_js(options), 'step': step})

  def circle(self, status: str = 'waiting', step: Union[primitives.JsDataModel, dict] = None, options: dict = None):
    """
    Hide all the panels in the drawer component.

    :param str status: Optional. The status of the step.
    :param Union[primitives.JsDataModel, dict] step: Optional.
    :param dict options: The stepper options to be changed.
    """
    step = {"status": status} if step is None else JsUtils.jsConvertData(step, None)
    return JsObjects.JsObjects.get('''
      %(comp)s.querySelector('svg').remove(); circle(%(comp)s, %(options)s, %(step)s)
      ''' % {'comp': self.varName, 'options': self.component.options.config_js(options), 'step': step})

  def label(self, value: Union[str, primitives.JsDataModel]):
    """
    Add a text label below the shape.

    :param Union[str, primitives.JsDataModel] value: The text to be added.
    """
    return self.querySelector('span[name=label]').innerHTML(value)

  def text(self, text: Union[str, primitives.JsDataModel], x: float = None, y: float = None,
           css: dict = None, color: str = None):
    """
    Add a text on the shape.

    :param Union[str, primitives.JsDataModel text: The text to be added.
    :param float x: Optional. The x position.
    :param float y: Optional. The y position.
    :param dict css: Optional. The CSS attributes.
    :param str color: The text color.
    """
    text = JsUtils.jsConvertData(text, None)
    if y is None:
      y = self.component.options.svg_style['height'] / 2 + 3
    if x is None:
      x = self.component.options.svg_style['width'] / 2
    dft_css = {"text-anchor": "middle", 'fill': color or self.component.options.text_color}
    if css is not None:
      dft_css.update(css)
    return JsObjects.JsObjects.get('''
      var textNodes = %(svg)s.querySelectorAll("text");
      if (textNodes.length == 0){
        var newText = document.createElementNS("http://www.w3.org/2000/svg", "text");
        newText.setAttributeNS(null, 'x', %(x)s);
        newText.setAttributeNS(null, 'y', %(y)s); var css = %(css)s;
        for (var key in css){ newText.setAttributeNS(null, key, css[key]) }
        var textNode = document.createTextNode(%(text)s); newText.appendChild(textNode);
        %(svg)s.appendChild(newText)
      } else {
        textNodes[0].innerHTML = %(text)s;
      }''' % {'text': text, 'svg': self.querySelector('svg'), 'y': y, 'x': x, 'css': dft_css})

  def blink(self, color: str = "#FFDEB3", border: str = "#FF9200"):
    """

    :param str color: Optional. The hexadecimal color code.
    :param str border: Optional. The hexadecimal color code.
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

  def click(self, js_funcs: Union[list, str], profile: Optional[Union[bool, dict]] = None, source_event: str = None,
            on_ready: bool = False):
    """
    Add a click event on a specific step.

    :param Union[list, str] js_funcs: Javascript functions.
    :param Optional[Union[bool, dict]] profile: Optional. A flag to set the component performance storage.
    :param str source_event: Optional. The source target for the event.
    :param bool on_ready:
    """
    return JsObjects.JsObjects.get('%(src)s.style.cursor = "pointer"; %(src)s.addEventListener("click", function(){%(fncs)s})' % {
      "src": source_event or self.varName, "fncs": JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)})

  def css(self, type, jsObject=None, duration: int = None):
    """   Replicate in plain Js the Jquery CSS function.

    Usage::

      select.label.dom.css({"color": "red"})

    Related Pages:

      https://www.w3schools.com/jsref/met_element_setattribute.asp

    :param type: A String with the type of parameter or a python dictionary
    :param jsObject: A JsObj with the value to be set
    :param duration: Integer

    :return: A JsObj
    """
    js_styles = []
    if jsObject is None and isinstance(type, dict):
      for k, v in type.items():
        if "-" in k:
          split_css = k.split("-")
          k = "%s%s" % (split_css[0], "".join([c.title() for c in split_css[1:]]))
        js_styles.append("%s.style.%s = %s" % (self.varId, k, JsUtils.jsConvertData(v, None)))
    elif jsObject is None:
      if "-" in type:
        split_css = type.split("-")
        type = "%s%s" % (split_css[0], "".join([c.title() for c in split_css[1:]]))
      return JsObjects.JsObjects.get("%s.style.%s" % (self.varId, type))

    else:
      if "-" in type:
        split_css = type.split("-")
        type = "%s%s" % (split_css[0], "".join([c.title() for c in split_css[1:]]))
      self._js.append("%s.style.%s = %s" % (self.varId, type, JsUtils.jsConvertData(jsObject, None)))
    return JsObjects.JsObjects.get(";".join(js_styles))


class Stepper(JsHtml.JsHtmlRich):

  def _get_index(self) -> str:
    """   Attach the internal StepByName JavaScript function and return its reference.
    """
    return self.page.properties.js.add_constructor('StepByName', "function StepByName(doms, label){var index_svg = -1; doms.childNodes.forEach(function(dom, i){if(dom.querySelector('[name=label]').innerHTML == label){ index_svg = i}}); return index_svg}")

  @property
  def val(self):
    """

    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset()} }" % (
        self.htmlCode, self.content.toStr()))

  @property
  def content(self):
    """

    """
    return JsHtml.ContentFormatters(self.page, "%s.innerHTML" % self.varName)

  def __getitem__(self, i):
    return Step(self, component=self.component, js_code=self.querySelectorAll("div[name=svg_holder]")[i], page=self.page)

  def getByLabel(self, label: Union[str, primitives.JsDataModel]):
    """

    :param Union[str, primitives.JsDataModel] label: The label value.
    """
    label = JsUtils.jsConvertData(label, None)
    return Step(self, component=self.component, js_code='''
      %(holder)s.querySelectorAll('div[name=svg_holder]')[%(StepByName)s(%(holder)s, %(label)s)]''' % {
      'StepByName': self._get_index(), "holder": self.varName, 'label': label}, page=self.page)

  def addItem(self, label: Union[str, primitives.JsDataModel], tooltip: Union[str, primitives.JsDataModel] = "",
              shape: Union[str, primitives.JsDataModel] = 'circle',
              status: Union[str, primitives.JsDataModel] = "waiting"):
    """

    :param Union[str, primitives.JsDataModel] label:
    :param Union[str, primitives.JsDataModel] tooltip:
    :param Union[str, primitives.JsDataModel] shape:
    :param Union[str, primitives.JsDataModel] status:
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
             "tooltip": tooltip, 'label': label, 'options': json.dumps(self.component._jsStyles)}

  def delete(self, i: int):
    """


    :param int i:
    """
    return self[i].remove()


class Drawer(JsHtml.JsHtmlRich):

  @property
  def content(self):
    """
    Hide all the panels in the drawer component.
    """
    return JsHtml.ContentFormatters(self.page, ''' 
      (function(doms, contents){var index =-1; doms.childNodes.forEach(function(dom, k){if(dom.style.display !== 'none'){index = k}}); 
        if (index >= 0){return contents.childNodes[index].innerHTML} else{return index}  })(%s, %s)
        ''' % (self.querySelector("div[name=drawer_panels]"), self.querySelector("div[name=drawer_content]")))

  def hide(self):
    """
    Hide all the panels in the drawer component.
    """
    return JsObjects.JsObjects.get(''' 
      (function(doms){doms.childNodes.forEach(function(dom){dom.style.display = 'none'; })})(%s)
      ''' % self.querySelector("div[name=drawer_panels]"))

  def add(self, link: str, panel: str = ""):
    """

    :param str link:
    :param str panel: Optional
    """
    return JsObjects.JsObjects.get('''
      ''' % self.querySelectorAll("[name=drawer_panels]"))

  def delete(self, i: int):
    """

    :param int i:
    """
    return JsObjects.JsObjects.get(''' 
          %(panel)s.childNodes[%(i)s].remove(); %(drawer)s.childNodes[%(i)s].remove(); 
          ''' % {'panel': self.querySelector("div[name=drawer_panels]"),
                 'drawer': self.querySelector("div[name=drawer_content]"), 'i': i})
