#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html

from epyk.core.js import Imports
from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtmlStepper
from epyk.core.html.options import OptPanel


class Step:
  name = 'Step'

  def __init__(self, src, selector):
    self._src = src
    self._selector = selector

  def click(self, js_funcs, profile=None):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self._src.page.properties.js.add_on_ready(
      "%s.addEventListener('click', function(event){%s})" % (
        self._selector.varName, JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)))
    return self


class Stepper(Html.Html):
  name = 'Stepper'
  _option_cls = OptPanel.OptionsStepper

  def __init__(self, report, records, width, height, color, options, profile):
    dflt_options = {'svg_style': {'display': 'block', 'width': 100, 'height': height[0] - 20}, 'circle_factor': 2,
                    'text_style': {'display': 'block', 'text-align': 'center'},
                    'backgrounds': {"success": '#37A78C', 'error': '#FF0000', 'waiting': '#A0A0A0',
                                    'pending': '#FF9200'},
                    'success': ["#C9EDE4", "#63CBB2", "#37A78C"],
                    'error': ["#F8CBAD", "#FF5757", "#FF0000"],
                    'pending': ["#FFDEB3", "#FFB047", "#FF9200"],
                    'waiting': ["#BEBEBE", "#B5B5B5", "#A0A0A0"],
                    'shape': 'circle', 'text_colors': 'white'}
    dflt_options.update(options)
    super(Stepper, self).__init__(
      report, records, options=dflt_options, profile=profile, css_attrs={"list-style-type": 'none', "width": width})
    self.color = self._report.theme.greys[-1] if color is None else color
    self.css({'color': self.color, "margin": 0, 'display': 'block', 'padding': 0})

  def __getitem__(self, i):
    return Step(self, selector=self.dom[i])

  @property
  def dom(self):
    """
    Description:
    ------------
    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    Usage::

    :rtype: JsHtmlStepper.Stepper
    """
    if self._dom is None:
      self._dom = JsHtmlStepper.Stepper(self, report=self._report)
    return self._dom

  @property
  def options(self):
    """
    Description:
    ------------
    Property to set all the possible object for a button.

    Usage::

    :rtype: OptPanel.OptionsStepper
    """
    return super().options

  _js__builder__ = ''' htmlObj.innerHTML = '';
      var width = options.svg_style.width; var height = options.svg_style.height;
      var attrs = ['name', 'text', 'title', 'tooltip'];
      var props = ['color', 'background', 'shape', 'title_color'];
      
      data.forEach(function(step, i){
        var li = document.createElement("LI");
        li.style['margin-bottom'] = '10px';
        
        attrs.forEach(function(attr){if(typeof step[attr] === 'undefined'){step[attr] = ''}});
        props.forEach(function(prop){if(typeof step[prop] === 'undefined'){step[prop] = options[prop]}});

        var span = document.createElement("SPAN"); span.setAttribute('name', step.name);
        span.setAttribute('name', 'label'); span.innerHTML = step.title;
        var div = document.createElement("DIV"); 
        div.setAttribute('title', step.tooltip);
        div.setAttribute('name', 'svg_holder');
        
        for (var key in options.text_style){span.style[key] = options.text_style[key]}
        span.style.width = width +"px";

        div.appendChild(span); li.appendChild(div);
        div.id = "svg_" + i;
        window[step.shape](div, options, step); 
        htmlObj.appendChild(li)
      })    
      '''

  def add_shape(self, shape, shape_def, dependencies=None):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :param shape: String.
    :param shape_def: String.
    :param dependencies: List. Optional. The external module dependencies
    """
    if dependencies is not None:
      for d in dependencies:
        if d in Imports.JS_IMPORTS:
          self._report.jsImports.add(d)
        if d in Imports.CSS_IMPORTS:
          self._report.cssImport.add(d)
    self.page.properties.js.add_constructor(shape, "function %s(htmlObj, options, step){%s}" % (
      shape, JsHtmlStepper.JsShapes().custom(shape_def)))
    self.options.shape = shape
    return self

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    # add all the shape definitions
    shapes = JsHtmlStepper.JsShapes()
    for s in shapes.shapes:
      self.page.properties.js.add_constructor(s, "function %s(htmlObj, options, step){%s}" % (s, getattr(shapes, s)()))
    return '<ul %s></ul>' % self.get_attrs(pyClassNames=self.style.get_classes())
