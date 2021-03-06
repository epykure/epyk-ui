
from epyk.core.html import graph


class Canvas(object):

  def __init__(self, context):
    self.parent = context

  def new(self, height=(400, "px"), width=(100, "%"), profile=None, options=None, htmlCode=None):
    """
    Description:
    ------------
    The HTML <canvas> tag is used to draw graphics, on the fly, via scripting (usually JavaScript).

    However, the <canvas> element has no drawing abilities of its own (it is only a container for graphics) - you must use a script to actually draw the graphics.

    The getContext() method returns an object that provides methods and properties for drawing on the canvas.

    This reference will cover the properties and methods of the getContext("2d") object, which can be used to draw text, lines, boxes, circles, and more - on the canvas

    Related Pages:

      https://www.w3schools.com/tags/ref_canvas.asp

    Usage:
    -----

    Attributes:
    ----------
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    """
    if not isinstance(width, tuple):
      width = (width, "px")
    html_svg = graph.GraphCanvas.Canvas(self.parent.context.rptObj, width, height, htmlCode, options, profile)
    return html_svg
