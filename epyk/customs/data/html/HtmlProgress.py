# TODO remove the hard coded CSS in this module
from pathlib import Path
from typing import Optional, Union
from epyk.core.py import primitives
from epyk.core.html import Html
from epyk.customs.data.options import OptNumProgress


class Gauge(Html.Html):
    requirements = ('jquery',)
    name = 'Progress Gauge'
    tag = "div"
    _option_cls = OptNumProgress.OptionsNumGauge

    style_urls = [
        Path(__file__).parent.parent.parent.parent / "core" / "css" / "native" / "html-prog.css",
    ]

    style_refs = {
        "html-prog": "html-prog",
        "html-prog-flow": "html-prog-flow",
        "html-prog-bar": "html-prog-bar",
        "html-prog-text": "html-prog-text",
    }

    def __init__(self, value: float, page: primitives.PageModel, width: tuple, height: tuple, html_code: Optional[str],
                 options: Optional[dict], profile: Optional[Union[dict, bool]]):
        super(Gauge, self).__init__(page, [], html_code=html_code, css_attrs={"width": width, "height": height},
                                    profile=profile, options=options)
        self.classList.add(self.style_refs["html-prog"])
        self.options.width = "%s%s" % (width[0], width[1])
        self.options.height = "%s%s" % (height[0], height[1])

    def __str__(self):
        return "<%s %s></%s>" % (
            self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.tag)


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
        return "<%s %s>%s</%s>" % (
        self.tag, self.get_attrs(css_class_names=self.style.get_classes()), str_div, self.tag)
