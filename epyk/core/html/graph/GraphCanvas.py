from epyk.core.html import Html


class Canvas(Html.Html):
  def __init__(self, report, width, height):
    super(Canvas, self).__init__(report, "", css_attrs={"width": width, "height": height})

  def __str__(self):
    return "<canvas %s></canvas>" % (self.get_attrs(pyClassNames=self.style.get_classes()))
