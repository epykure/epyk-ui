
from epyk.core.html.Html import Component
from epyk.core.html.HtmlSelect import Option


class Btn(Component):
  css_classes = None
  name = "Clarity Button"

  str_repr = '''<cds-button status="success">{text}</cds-button>'''

  def write_values(self):
    return {"text": self._vals}

