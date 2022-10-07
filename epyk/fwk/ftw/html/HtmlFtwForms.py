
from epyk.core.html.HtmlSelect import Option
from epyk.core.html.Html import Component
from epyk.core.data.DataPy import SelectionBox


class Toggle(Component):
  css_classes = ["ms-Toggle"]
  name = "Fabric UI Toggle"
  str_repr = '''
<div {attrs}>
  <span class="ms-Toggle-description">Let apps use my location</span> 
  <input type="checkbox" id="demo-toggle-3" class="ms-Toggle-input" />
  <label for="demo-toggle-3" class="ms-Toggle-field" tabindex="0">
    <span class="ms-Label ms-Label--off">Off</span> 
    <span class="ms-Label ms-Label--on">On</span> 
  </label>
</div>
'''

  _js__builder__ = "window[htmlObj.id] = new fabric['Toggle'](htmlObj)"


class Spinner(Component):
  css_classes = ["ms-Spinner"]
  name = "Fabric UI Spinner"

  str_repr = '''
<div {attrs}>
  <div class="ms-Spinner-label">
    {text}
  </div>
</div>'''

  _js__builder__ = "window[htmlObj.id] = new fabric['Spinner'](htmlObj)"


class Alert(Component):
  css_classes = ["ms-MessageBar"]
  name = "Fabric UI Alert"

  str_repr = '''
<div {attrs}>
  <div class="ms-MessageBar-content">
    <div class="ms-MessageBar-icon">
      <i class="ms-Icon ms-Icon--{category}"></i>
    </div>
    <div class="ms-MessageBar-text">
      {sub_items}
    </div>
  </div>
</div>
'''


class SearchBox(Component):
  css_classes = ["ms-SearchBox"]
  name = "Fabric UI SearchBox"

  str_repr = '''
<div {attrs}>
  <input class="ms-SearchBox-field" type="text" value="">
  <label class="ms-SearchBox-label">
    <i class="ms-SearchBox-icon ms-Icon ms-Icon--Search"></i>
    <span class="ms-SearchBox-text">{label}</span> 
  </label>
  <div class="ms-CommandButton ms-SearchBox-clear ms-CommandButton--noLabel">
    <button class="ms-CommandButton-button">
      <span class="ms-CommandButton-icon"><i class="ms-Icon ms-Icon--Clear"></i></span> 
      <span class="ms-CommandButton-label"></span> 
    </button>
  </div>
</div>
'''

  _js__builder__ = "window[htmlObj.id] = new fabric['SearchBox'](htmlObj)"


class ChoiceFieldGroup(Component):
  css_classes = ["ms-ChoiceFieldGroup"]
  name = "Fabric UI ChoiceFieldGroup"

  str_repr = '''
<div {attrs} role="radiogroup">
  <div class="ms-ChoiceFieldGroup-title">
    <label class="ms-Label is-required">{label}</label>
  </div>
  <ul class="ms-ChoiceFieldGroup-list">
    <li class="ms-RadioButton">
      <input tabindex="-1" type="radio" class="ms-RadioButton-input">
      <label role="radio" class="ms-RadioButton-field" tabindex="0" aria-checked="false" name="choicefieldgroup">
        <span class="ms-Label">Option 1</span> 
      </label>
    </li>
    <li class="ms-RadioButton">
      <input tabindex="-1" type="radio" class="ms-RadioButton-input">
      <label role="radio" class="ms-RadioButton-field" tabindex="0" aria-checked="false" name="choicefieldgroup">
        <span class="ms-Label">Option 2</span> 
      </label>
    </li>
  </ul>
</div>'''


class Button(Component):
  css_classes = ["ms-Button"]
  name = "Fabric UI Button"

  str_repr = '''
<button {attrs}>
  <span class="ms-Button-label">{text}</span> 
</button>'''

  _js__builder__ = "window[htmlObj.id] = new fabric['Button'](htmlObj)"


class Check(Component):
  css_classes = ["ms-CheckBox"]
  name = "Fabric UI Check"

  str_repr = '''
<div {attrs}>
  <input tabindex="-1" type="{type}" class="ms-CheckBox-input">
  <label role="checkbox" class="ms-CheckBox-field" tabindex="0" aria-checked="false" name="{for}" style="margin:0">
    <span class="ms-Label">{text}</span> 
  </label>
</div>'''

  _js__builder__ = "window[htmlObj.id] = new fabric['CheckBox'](htmlObj)"

  def write_values(self):
    if self._vals['checked']:
      self.attr["checked"] = None
    return {"text": self._vals['label'], "for": self.htmlCode, "type": self._vals['type']}


class Select(Component):
  css_classes = ["ms-Dropdown"]
  name = "Fabric UI Select"

  str_repr = '''
<div {attrs}>
  <label class="ms-Label">{label}</label>
  <i class="ms-Dropdown-caretDown ms-Icon ms-Icon--ChevronDown"></i>
  <select class="ms-Dropdown-select">
    {sub_items}
  </select>
</div>'''

  dyn_repr = '''{sub_item}'''

  _js__builder__ = "window[htmlObj.id] = new fabric['Dropdown'](htmlObj)"

  @property
  def parsers(self):
    """  
    Set of functions to parse the data.
    """
    return SelectionBox

  @property
  def data(self):
    """  
    Property to the underlying data from the select.
    """
    return self._vals

  @data.setter
  def data(self, parsed_values):
    for rec in parsed_values:
      if self.init_selected is not None:
        if rec["value"] == self.init_selected:
          rec["selected"] = True
      self.add_option(rec["value"], rec.get("name", rec["value"]), selected=rec.get("selected", False))

  def add_option(self, value, label, selected=False, options=None):
    """  
    Add an option to the Data list component.

    :param value: String. The option value.
    :param label: String. The option label.
    :param selected: Boolean. Optional.
    :param options:
    """
    o = Option(self.page, value, label, None, selected, options=options)
    o.options.managed = False
    self.components.add(o)
    self.items.append(o)
    return o

  def write_values(self):
    return {"label": ''}
