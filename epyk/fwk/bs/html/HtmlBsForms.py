
from epyk.core.html.Html import Component
from epyk.core.html.HtmlSelect import Option
from epyk.core.html.HtmlInput import Input
from epyk.fwk.bs.dom import DomBsForms
from epyk.fwk.bs.options import OptBsForms
from epyk.fwk.bs.css import BsStyleForms


class BsInput(Input):

  def __init__(self, report, text, placeholder, width, height, html_code, options, attrs, profile):
    super(BsInput, self).__init__(report, text, placeholder, width, height, html_code, options, attrs, profile)
    self.attr["class"].clear()
    self.attr["class"].add("form-control")

  @property
  def style(self):
    """
    Description:
    ------------
    Property to the CSS Style of the component.

    :rtype: BsStyleForms.BsClsInput
    """
    if self._styleObj is None:
      self._styleObj = BsStyleForms.BsClsInput(self)
    return self._styleObj


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

  @property
  def style(self):
    """
    Description:
    ------------
    Property to the CSS Style of the component.

    :rtype: BsStyleForms.BsClsSelect
    """
    if self._styleObj is None:
      self._styleObj = BsStyleForms.BsClsSelect(self)
    return self._styleObj

  def write_values(self):
    return {}

  def add_option(self, value, label, selected=False, options=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param value:
    :param label:
    :param selected:
    :param options:
    """
    o = Option(self.page, value, label, None, selected, options=options)
    o.options.managed = False
    self.components.add(o)
    self.items.append(o)
    return o


class BsDataList(Component):
  css_classes = ["form-control"]
  name = "Bootstrap Select"
  _option_cls = OptBsForms.Check

  str_repr = '''
<label for="{for}" class="form-label">{label}</label>
<input {attrs}>
<datalist id="datalistOptions">
  {sub_items}
</datalist>'''

  def add_option(self, value, label, selected=False, options=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param value:
    :param label:
    :param selected:
    :param options:
    """
    o = Option(self.page, value, label, None, selected, options=options)
    self.components.add(o)
    self.items.append(o)
    return o


class BsRange(Component):
  css_classes = ["form-range"]
  name = "Bootstrap Range"
  _option_cls = OptBsForms.Slider

  str_repr = '''
<label for="customRange2" class="form-label">Example range</label>
<input type="range" class="form-range" min="0" max="5" id="customRange2">'''


class BsSFloatingLabel(Component):
  css_classes = ["form-control"]
  name = "Bootstrap Floating"

  str_repr = '''
<div class="form-floating">
  <input {attrs}>
  <label for="{for}">{label}</label>
</div>'''

  def write_values(self):
    """
    Description:
    ------------

    """
    if self._vals['value']:
      self.attr["value"] = self._vals['value']
    self.attr["placeholder"] = self._vals['label']
    return {"label": self._vals['label'], "for": self.htmlCode, "type": self._vals['type']}


class BsInputGroup(Component):
  css_classes = ["form-control"]
  name = "Bootstrap Floating"

  str_repr = '''
<div class="input-group mb-3">
  <span class="input-group-text" id="basic-addon3">https://example.com/users/</span>
  <input type="text" class="form-control" id="basic-url" aria-describedby="basic-addon3">
</div>'''


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