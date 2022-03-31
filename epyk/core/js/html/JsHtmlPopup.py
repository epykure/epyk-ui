
from typing import Union
from epyk.core.py import primitives
from epyk.core.js.primitives import JsObject

from epyk.core.js.objects import JsNodeDom
from epyk.core.js.html import JsHtml


class JsHtmlPopup(JsHtml.JsHtml):

  def event_position(self, top: int = 8, left: int = 0, css_attrs: dict = None):
    dfl_attrs = {"position": "absolute",
                 "top": JsObject.JsObject.get('event.pageY + (%s.clientHeight / 2 + %s) + "px"' % (self.varName, top)),
                 'left': JsObject.JsObject.get('event.pageX + (%s.firstChild.clientWidth / 2 + %s) + "px"' % (
                   self.varName, left))}
    self.component.style.css.top = None
    self.component.style.css.left = None
    self.component.options.top = None
    self.component.options.left = None
    self.component.window.style.css.top = None
    self.component.window.style.css.left = None
    self.component.window.style.css.position = None
    if css_attrs is not None:
      dfl_attrs.update(css_attrs)
      if 'bottom' in css_attrs:
        del dfl_attrs["top"]
      if 'right' in css_attrs:
        del dfl_attrs["left"]
    return '''
      (function(event){%(attrs)s})(event)''' % {"attrs": JsNodeDom.JsDoms.get(self.varName).css(dfl_attrs).r}

