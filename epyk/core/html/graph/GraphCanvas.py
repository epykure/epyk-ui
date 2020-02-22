from epyk.core.html import Html
from epyk.core.js.objects import JsCanvas


class Canvas(Html.Html):
  def __init__(self, report, width, height):
    super(Canvas, self).__init__(report, "", css_attrs={"width": width, "height": height})

  @property
  def dom(self):
    """

    :rtype: JsCanvas.Canvas
    """
    if self._dom is None:
      self._dom = JsCanvas.Canvas(self, report=self._report)
    return self._dom

  def __str__(self):
    return "<canvas %s></canvas>" % (self.get_attrs(pyClassNames=self.style.get_classes()))
