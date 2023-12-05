#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.py import types
from epyk.core.html import graph


class Canvas:

  def __init__(self, ui):
    self.page = ui.page

  def new(self, height: types.SIZE_TYPE = (400, "px"), width: types.SIZE_TYPE = (100, "%"),
          profile: types.PROFILE_TYPE = None, options: types.OPTION_TYPE = None, html_code: str = None
          ) -> graph.GraphCanvas.Canvas:
    """The HTML <canvas> tag is used to draw graphics, on the fly, via scripting (usually JavaScript).
    However, the <canvas> element has no drawing abilities of its own (it is only a container for graphics) -
    you must use a script to actually draw the graphics.
    The getContext() method returns an object that provides methods and properties for drawing on the canvas.
    This reference will cover the properties and methods of the getContext("2d") object, which can be used to draw text,
    lines, boxes, circles, and more - on the canvas

    :tags:
    :categories:

    `Canva <https://www.w3schools.com/tags/ref_canvas.asp>`_

    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    if not isinstance(width, tuple):
      width = (width, "px")
    html_svg = graph.GraphCanvas.Canvas(self.page, width, height, html_code, options, profile)
    return html_svg
