
from epyk.core.html import Html

from epyk.core.js.html import JsHtmlStepper
from epyk.core.html.entities import EntHtml4
from epyk.core.html.options import OptPanel


class Step(Html.Html):

  def __init__(self, report, records, width, height, color, options):
    super(Step, self).__init__(report, records, css_attrs={"width": width, "height": height})

  def mute(self):
    pass
  

class CircleStep(Step):

  def __str__(self):
    return '<div %s>%s</div>' % (self.get_attrs(pyClassNames=self.style.get_classes()), "".join(divs))


class TriangleStep(Step):

  def __str__(self):
    return '<div %s>%s</div>' % (self.get_attrs(pyClassNames=self.style.get_classes()), "".join(divs))


class CrossStep(Step):

  def __str__(self):
    return '<div %s>%s</div>' % (self.get_attrs(pyClassNames=self.style.get_classes()), "".join(divs))


class RectStep(Step):

  def __str__(self):
    return '<div %s>%s</div>' % (self.get_attrs(pyClassNames=self.style.get_classes()), "".join(divs))


class ArrowStep(Step):

  def __str__(self):
    return '<div %s>%s</div>' % (self.get_attrs(pyClassNames=self.style.get_classes()), "".join(divs))


class Stepper(Html.Html):

  def __init__(self, report, records, width, height, color, options):
    super(Stepper, self).__init__(report, records, css_attrs={"width": width, "height": height})
    self.color = self._report.theme.greys[-1] if color is None else color
    self.css({'color': self.color, "display": "inline-block", "margin": '5px'})
    self.__options = OptPanel.OptionsDiv(self, options)
    self.status_colors = {
      "success": {"border": self._report.theme.success[1], "background": self._report.theme.success[0], "stroke-width": 2, "stroke": self._report.theme.greys[-1]},
      "error": {"border": self._report.theme.danger[1], "background": self._report.theme.danger[0], "stroke-width": 2, "stroke": self._report.theme.greys[-1]},
      "pending": {"border": self._report.theme.warning[1], "background": self._report.theme.warning[1], "stroke-width": 1, "stroke": self._report.theme.greys[-1]},
      "default": {"border": self._report.theme.greys[5], "background": self._report.theme.greys[3], "stroke-width": 1, "stroke": self._report.theme.greys[-1]}}

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

    :rtype: OptPanel.OptionsDiv
    """
    return self.__options

  def __add__(self, htmlObj):
    """ Add items to a container """
    htmlObj.inReport = False # Has to be defined here otherwise it is set to late
    if self.options.inline:
      htmlObj.style.css.display = 'inline-block'
    if not isinstance(self.val, list):
      self._vals = [self.val]
    self.val.append(htmlObj)
    return self

  def __getitem__(self, i):
    return self.val[i]

  def __str__(self):
    divs = []
    # Add the first step
    colors = self.status_colors.get(self.val[0].get('status', 'default'), self.status_colors['default'])
    step = self._report.ui.div(EntHtml4.NO_BREAK_SPACE).tooltip(self.val[0]['value'])
    step.css({"border": '1px solid %s' % colors["border"], "border-radius": "20px", "width": '20px', "height": '20px',
              'padding': '2px', "background": colors["background"]})
    step.inReport = False
    divs.append("<div style='display:inline-block;width:auto;height:auto;vertical-align:top'>%s<span>%s</span></div>" % (step, self.val[0].get("label", EntHtml4.NO_BREAK_SPACE)))

    for v in self.val[1:]:
      colors = self.status_colors.get(v.get('status', 'default'), self.status_colors['default'])
      # Add the link to the next step
      line = self._report.ui.charts.svg.line(y1=13, y2=13, width=(40, "px"), height=(60, "px"), options={"stroke": colors["stroke"], "stroke-width": colors["stroke-width"]})
      line.inReport = False
      divs.append(str(line))

      # Add the following step
      step = self._report.ui.div(EntHtml4.NO_BREAK_SPACE).tooltip(v['value'])
      step.css({"border": '1px solid %s' % colors["border"], "border-radius": "20px", "width": '20px', "height": '20px',
                'padding': '2px', "background": colors["background"]})
      step.inReport = False
      divs.append("<div style='display:inline-block;width:auto;height:auto;vertical-align:top'>%s<span>%s</span></div>" % (step, v.get("label", EntHtml4.NO_BREAK_SPACE)))
    return '<div %s>%s</div>' % (self.get_attrs(pyClassNames=self.style.get_classes()), "".join(divs))
