#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union, Optional
from epyk.core.py import primitives
from epyk.core.py import types
from epyk.core.html import Html

from epyk.core.js import Imports
from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtmlStepper
from epyk.core.html.options import OptPanel


class Stepper(Html.Html):
  name = 'Stepper'
  _option_cls = OptPanel.OptionsStepper
  tag = "ul"

  def __init__(self, page: primitives.PageModel, records: list, width: tuple, height: tuple, color: Optional[str],
               options: Optional[dict], profile: Optional[Union[dict, bool]], verbose: bool = False):
    dfl_options = {'svg_style': {'display': 'block', 'width': 100, 'height': height[0] - 20}, 'circle_factor': 2,
                   'text_style': {'display': 'block', 'text-align': 'center'},
                   'backgrounds': {
                     "success": '#37A78C', 'error': '#FF0000', 'waiting': '#A0A0A0', 'pending': '#FF9200'},
                   'success': ["#C9EDE4", "#63CBB2", "#37A78C"],
                   'error': ["#F8CBAD", "#FF5757", "#FF0000"],
                   'pending': ["#FFDEB3", "#FFB047", "#FF9200"],
                   'waiting': ["#BEBEBE", "#B5B5B5", "#A0A0A0"],
                   'shape': 'circle', 'text_color': 'white'}
    dfl_options.update(options)
    super(Stepper, self).__init__(
      page, records, options=dfl_options, profile=profile, css_attrs={"list-style-type": 'none', "width": width},
      verbose=verbose)
    self.color = self.page.theme.greys[-1] if color is None else color
    self.css({'color': self.color, "margin": 0, 'display': 'inline-block', 'padding': 0})

  def __getitem__(self, i: int):
    return Step(self, selector=self.dom[i])

  @property
  def dom(self) -> JsHtmlStepper.Stepper:
    """Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.
    """
    if self._dom is None:
      self._dom = JsHtmlStepper.Stepper(self, page=self.page)
    return self._dom

  @property
  def options(self) -> OptPanel.OptionsStepper:
    """Property to set all the possible object for a button"""
    return super().options

  def add_shape(self, shape: str, shape_def: str, dependencies: Optional[list] = None):
    """Add a bespoke shape for the stepper component.

    :param shape: The reference of the shape
    :param shape_def: The shape JavaScript definition
    :param dependencies: Optional. The external module dependencies
    """
    if dependencies is not None:
      for d in dependencies:
        if d in Imports.JS_IMPORTS:
          self.page.jsImports.add(d)
        if d in Imports.CSS_IMPORTS:
          self.page.cssImport.add(d)
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
    return '<%(t)s %(a)s></%(t)s>' % {"a": self.get_attrs(css_class_names=self.style.get_classes()), "t": self.tag}


class Step:
  name = 'Step'

  def __init__(self, component: Stepper, selector: Html.Html):
    self.component = component
    self._selector = selector

  def click(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
    """Add a click event to the component.

    :param js_funcs: Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self.component.page.properties.js.add_on_ready(
      "%(src)s.style.cursor = 'pointer'; %(src)s.addEventListener('click', function(event){%(fncs)s})" % {
        "src": self._selector.varName, "fncs": JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)})
    return self
