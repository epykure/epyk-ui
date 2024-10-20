# TODO remove the hard coded CSS in this module

from typing import Optional, Union
from epyk.core.py import primitives
from epyk.core.html import Html
from epyk.customs.data.options import OptNumProgress


class Gauge(Html.Html):
  requirements = ('jquery',)
  name = 'Progress Gauge'
  tag = "div"
  _option_cls = OptNumProgress.OptionsNumCircle

  def __init__(self, value: float, page: primitives.PageModel, width: tuple, height: tuple, html_code: Optional[str],
               options: Optional[dict], profile: Optional[Union[dict, bool]]):
    super(Gauge, self).__init__(page, [], html_code=html_code, css_attrs={"width": width, "height": height},
                                 profile=profile, options=options)
    self.style.css.position = "relative"
    self.style.css.display = "inline-block"
    self.style.css.margin = 4
    self.style.css.text_align = "center"
    #
    self.prog_over_flow = self.page.ui.div()
    self.prog_over_flow.style.css.position = "relative"
    self.prog_over_flow.style.css.overflow = "hidden"
    self.prog_over_flow.style.css.width = "%s%s" % (width[0], width[1])
    self.prog_over_flow.style.css.height = "%s%s" % (height[0], height[1])
    self.prog_over_flow.style.css.margin_bottom = "-%spx" % int(width[0] / 4)
    self._bar = self.page.ui.div()
    self._bar.attr["name"] = "bar"
    self._bar.style.css.position = "absolute"
    self._bar.style.css.top = 0
    self._bar.style.css.left = 0
    self._bar.style.css.width = self.prog_over_flow.style.css.width
    self._bar.style.css.height = "%s%s" % (2 * height[0], height[1])
    self._bar.style.css.border_radius = "50%"
    self._bar.style.css.box_sizing = "border-box"
    self._bar.style.css.border = "5px solid #eee"
    self._bar.style.css.border_bottom_color = self.page.theme.notch()
    self._bar.style.css.border_right_color = self.page.theme.notch()
    self._span = self.page.ui.tags.span(value, width=False)
    self._span.style.css.font_size = int(width[0] / 4)
    self.prog_over_flow.add(self._bar)
    self.add(self.prog_over_flow)
    self.add(self._span)
    self.add(self.page.ui.tags.no_tag("%"))

  @property
  def bar(self):
    return self._bar

  @property
  def label(self):
    return self._span

  def refresh(self):
    """   Component refresh function. Javascript function which can be called in any Javascript event.

    Tip: This function cannot be used in a plan Python section but in a JavaScript one defined in an event for example.

    """
    return self.build(self._span.val, None)

  def __str__(self):
    str_div = "".join([v.html() if hasattr(v, 'html') else str(v) for v in self.val])
    self.page.properties.js.add_builders(self.refresh())
    return "<%s %s>%s</%s>" % (self.tag, self.get_attrs(css_class_names=self.style.get_classes()), str_div, self.tag)


class Circle(Html.Html):
  name = 'Progress Circle'
  tag = "div"
  _option_cls = OptNumProgress.OptionsNumCircle

  def __init__(self, value: float, page: primitives.PageModel, width: tuple, height: tuple, html_code: Optional[str],
               options: Optional[dict], profile: Optional[Union[dict, bool]]):
    page.properties.css.add_text('''
@property --pgPercentage {
  syntax: '<number>';
  inherits: false;
  initial-value: 0;
}

@keyframes growProgressBar {
  from { --pgPercentage: var(--start); }
  to { --pgPercentage: var(--value); }
}

.CircleProgressbar {
  animation: growProgressBar 1s 1 forwards ease-in-out;
  counter-set: percentage var(--pgPercentage);
  border-radius: 50%;
  display: grid;
  margin: 2px;
  place-items: center;
}

.CircleProgressbar::after {
  content: counter(percentage) '%';
  line-height: 90px;
  text-align: center;
  display: block;
}
''', map_id="NumberCircle")

    super(Circle, self).__init__(page, [], html_code=html_code, css_attrs={"width": width, "height": height},
                                 profile=profile, options=options)
    self.aria.role = "progressbar"
    self.style.css.display = "inline-block"
    self.aria.valuemax = 100
    self.aria.valuemin = 0
    self.attr["class"].add("CircleProgressbar")
    self.style.css.color = self.page.theme.notch()
    self.style.css.background = 'radial-gradient(closest-side, %(back)s 80%%, transparent 0 99.9%%, %(back)s 0), conic-gradient(%(color)s calc(var(--pgPercentage) * 1%%), %(grey)s 0)' % {
      'color': self.page.theme.notch(), "grey": self.page.theme.greys[1], 'back': self.page.theme.greys[0]}
    self.style.css.font_size = int(width[0] / 4)
    self.aria.valuenow = value
    self.css({"--value": value})
    self.css({"--start": 0})

  def __str__(self):
    str_div = "".join([v.html() if hasattr(v, 'html') else str(v) for v in self.val])
    return "<%s %s>%s</%s>" % (self.tag, self.get_attrs(css_class_names=self.style.get_classes()), str_div, self.tag)
