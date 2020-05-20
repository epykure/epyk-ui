
from epyk.core.html import Html

from epyk.core.js import Imports
from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtmlStepper
from epyk.core.html.options import OptPanel


class Step(object):

  def __init__(self, src, selector):
    self._src = src
    self._selector = selector

  def click(self, jsFncs, profile=False):

    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self._src._report._props['js'].setdefault("onReady", []).append("%s.addEventListener('click', function(event){%s})" % (self._selector.varName, JsUtils.jsConvertFncs(jsFncs, toStr=True)))
    return self


class Stepper(Html.Html):

  def __init__(self, report, records, width, height, color, options):
    super(Stepper, self).__init__(report, records, css_attrs={"list-style-type": 'none', "width": width})
    self.color = self._report.theme.greys[-1] if color is None else color
    self.css({'color': self.color, "margin": '0', 'display': 'block'})
    dflt_options = {'svg_style': {'display': 'block', 'width': 100, 'height': height[0]-20}, 'circle_factor': 2,
                    'text_style': {'display': 'block', 'text-align': 'center'},
                    'backgrounds': {"success": '#37A78C', 'error': '#FF0000', 'waiting': '#A0A0A0', 'pending': '#FF9200'},
                    'success': ["#C9EDE4", "#63CBB2", "#37A78C"],
                    'error': ["#F8CBAD", "#FF5757", "#FF0000"],
                    'pending': ["#FFDEB3", "#FFB047", "#FF9200"],
                    'waiting': ["#BEBEBE", "#B5B5B5", "#A0A0A0"],
                    'shape': 'circle', 'text_colors': 'white'}
    dflt_options.update(options)
    self.__options = OptPanel.OptionsStepper(self, dflt_options)

  def __getitem__(self, i):
    """
    Description:
    ------------

    """
    return Step(self, selector=self.dom[i])

  @property
  def dom(self):
    """
    Description:
    ------------

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
    Property to set all the possible object for a button

    :rtype: OptPanel.OptionsStepper
    """
    return self.__options

  @property
  def _js__builder__(self):
    return ''' htmlObj.innerHTML = '';
      var width = options.svg_style.width; var height = options.svg_style.height;
      var attrs = ['name', 'text', 'title', 'tooltip'];
      var props = ['color', 'background', 'shape', 'title_color'];
      
      data.forEach(function(step, i){
        var li = document.createElement("LI") ;
        li.style['margin-bottom'] = '10px';
        
        attrs.forEach(function(attr){ if (typeof step[attr] === 'undefined'){ step[attr] = ''}; });
        props.forEach(function(prop){ if (typeof step[prop] === 'undefined'){ step[prop] = options[prop]}; })

        var span = document.createElement("SPAN"); span.setAttribute('name', step.name);
        span.setAttribute('name', 'label'); span.innerHTML = step.title;
        var div = document.createElement("DIV"); 
        div.setAttribute('title', step.tooltip);
        div.setAttribute('name', 'svg_holder');
        
        for (var key in options.text_style){ span.style[key] = options.text_style[key] }
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
    constructors = self._report._props.setdefault("js", {}).setdefault("constructors", {})
    constructors[shape] = "function %s(htmlObj, options, step){%s}" % (shape, JsHtmlStepper.JsShapes().custom(shape_def))
    self.options.shape = shape
    return self

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    # add all the shape definitions
    constructors = self._report._props.setdefault("js", {}).setdefault("constructors", {})
    shapes = JsHtmlStepper.JsShapes()
    for s in shapes.shapes:
      constructors[s] = "function %s(htmlObj, options, step){%s}" % (s, getattr(shapes, s)())
    return '<ul %s></ul>' % self.get_attrs(pyClassNames=self.style.get_classes())
