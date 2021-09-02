
from epyk.core.html.Html import Component
from epyk.core.html.HtmlSelect import Option
from epyk.fwk.bs.dom import DomBsForms
from epyk.fwk.bs.options import OptBsForms


class BsCheck(Component):
  css_classes = ["form-check-input"]
  name = "Bootstrap Check"
  _option_cls = OptBsForms.Check

  str_repr = '''
<div class="{container_class}">
  <input type="{type}" value="" {attrs}>
  <label class="form-check-label" for="{for}">{text}</label>
</div>'''

  def write_values(self):
    if self._vals['checked']:
      self.attr["checked"] = None
    if self.options.disabled:
      self.attr["disabled"] = None

    return {"container_class": " ".join(self.options.container_class), "text": self._vals['label'],
            "for": self.htmlCode, "type": self._vals['type']}

  @property
  def dom(self):
    """
    Description:
    -----------
    The common DOM properties.

    :rtype: DomBsForms.DomCheck
    """
    if self._dom is None:
      self._dom = DomBsForms.DomCheck(self, report=self.page)
    return self._dom

  @property
  def options(self):
    """
    Description:
    -----------
    The component options.

    :rtype: OptBsForms.Check
    """
    return super().options


class BsSelect(Component):
  css_classes = ["form-select"]
  name = "Bootstrap Select"
  _option_cls = OptBsForms.Check

  str_repr = '''
<select {attrs}>
  {sub_items}
</select>'''

  dyn_repr = '''{sub_item}'''

  def write_values(self):
    return {}

  def add_option(self, value, label, selected=False, options=None):
    o = Option(self.page, value, label, None, selected, options=options)
    self.components.add(o)
    self.items.append(o)
    return o


class BsSFloatingLabel(Component):
  css_classes = ["form-control"]
  name = "Bootstrap Floating"

  str_repr = '''
<div class="form-floating">
  <input {attrs}>
  <label for="{for}">{label}</label>
</div>'''

  def write_values(self):
    if self._vals['value']:
      self.attr["value"] = self._vals['value']
    self.attr["placeholder"] = self._vals['label']
    return {"label": self._vals['label'], "for": self.htmlCode, "type": self._vals['type']}


class BsSFloatingTextArea(BsSFloatingLabel):
  css_classes = ["form-control"]
  name = "Bootstrap Textarea"

  str_repr = '''
<div class="form-floating">
  <textarea {attrs}></textarea>
  <label for="floatingTextarea">{label}</label>
</div>'''


class BsSFloatingSelect(BsSFloatingLabel):
  css_classes = ["form-select"]
  name = "Bootstrap Select"

  str_repr = '''
<div class="form-floating">
  <select {attrs}>
    {sub_items}
  </select>
  <label for="floatingSelect">{label}</label>
</div>'''
