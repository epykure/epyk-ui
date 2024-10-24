import json

from epyk.core.py import primitives
from epyk.core.py import types

from epyk.core.html import Html
from epyk.core.html import HtmlSelect
from epyk.core.html.options import OptSelect
from epyk.core.data.DataPy import SelectionBox

# The list of CSS classes
from epyk.core.css.styles import GrpClsList

# The JavaScript modules
from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtmlSelect
from epyk.core.js.packages import JsQuery
from epyk.core.js.packages import JsSelect


class Select(Html.Html):
  requirements = ('bootstrap-select', )
  name = 'Select'
  builder_module = "SelectPicker"
  _option_cls = OptSelect.OptionsSelectJs

  def __init__(self, page: primitives.PageModel, records, html_code, width, height, profile, multiple, options):
    super(Select, self).__init__(page, records, html_code=html_code, css_attrs={"width": width, "height": height},
                                 profile=profile, options=options)
    self._vals, self.button_css = records, None
    if html_code in self.page.inputs:
      for v in self._vals:
        if v['value'] == self.page.inputs[html_code]:
          options['selected'] = v['value']
    if width[1] == 'px':
      self.attr["data-width"] = "%spx" % width[0]
    if multiple:
      self.attr['multiple'] = None
    if options.get('button-bg', True):
      self.style.add_classes.select.toggle()

  @property
  def options(self) -> OptSelect.OptionsSelectJs:
    """   Property to set all the possible object for a button.

    :rtype: OptSelect.OptionsSelectJs
    """
    return super().options

  @property
  def style(self) -> GrpClsList.ClassSelect:
    """   A property to the CSS style of the DOM component.
    Each component will have default CSS style but they can be overridden.

    :rtype: GrpClsList.ClassSelect
    """
    if self._styleObj is None:
      self._styleObj = GrpClsList.ClassSelect(self)
    return self._styleObj

  @property
  def dom(self) -> JsHtmlSelect.DomSelect:
    """   Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    :return: A Javascript Dom object

    :rtype: JsHtmlSelect.DomSelect
    """
    if self._dom is None:
      self._dom = JsHtmlSelect.DomSelect(component=self, page=self.page)
    return self._dom

  @property
  def js(self) -> JsSelect.JSelect:
    """   Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/methods/

    :return: A Javascript Dom object

    :rtype: JsSelect.JSelect
    """
    if self._js is None:
      self._js = JsSelect.JSelect(component=self, page=self.page)
    return self._js

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
    self._vals = parsed_values

  _js__builder__ = '''
      var selectObj = %s; selectObj.empty();
      const attrs = ['icon', 'content']; var selections = [];
      if(typeof options.auto_select !== 'undefined'){
         if(typeof data[options.auto_select] === 'string'){selections.push(data[options.auto_select])}}
      for (var idx in data){var item = data[idx];
        if(typeof data[idx] === 'string'){item = {value: item}};
        var opt = document.createElement("OPTION"); opt.value = item.value;
        opt.text = (typeof item.name !== 'undefined')? item.name : item.value;
        if(opt.selected){selections.push(item.value)}
        if(item.selected){selections.push(opt.value)}
        for(var a in attrs){var attrVal = item[attrs[a]];
          if (typeof attrVal !== 'undefined'){opt.setAttribute("data-"+ attrs[a], attrVal)}}
        selectObj.append(opt)}
      selectObj.selectpicker(options).selectpicker('refresh');
      selectObj.val(selections).change()''' % JsQuery.decorate_var("htmlObj", convert_var=False)

  def change(self, js_funcs: types.JS_FUNCS_TYPES, empty_funcs: types.JS_FUNCS_TYPES=None,
             profile: types.PROFILE_TYPE = None, source_event: str = None, on_ready: bool = False):
    """   Javascript event triggered when the value has changed.

    :param js_funcs: Set of Javascript function to trigger on this event
    :param empty_funcs: Set of Js function to trigger if the value is empty
    :param profile: Optional. A flag to set the component performance storage.
    :param source_event: The JavaScript DOM source for the event (can be a sug item)
    :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    if empty_funcs is not None:
      if not isinstance(empty_funcs, list):
        empty_funcs = [empty_funcs]
      js_funcs.append("if (%s === ''){%s}" % (self.dom.content.toStr(), JsUtils.jsConvertFncs(empty_funcs, toStr=True)))
    return self.on("change", js_funcs, profile, source_event, on_ready)

  def ajax(self, url: str, js_data: types.JS_FUNCS_TYPES = "function (){return {q: '{{{q}}}'}}", is_json: bool = True,
           method: str = "POST", options: dict = None):
    """   Create a AJAX request.

    Related Pages:

      https://github.com/truckingsim/Ajax-Bootstrap-Select

    :param url: The request URL for the ajax call.
    :param js_data: Optional. The value of the item to be removed from the list.
    :param is_json: Optional. A flag to specific if the data are json (default True).
    :param method: Optional. The HTTP request method. Default Post
    :param options: Optional. The specific properties for the ajax request.
    """
    self.options.liveSearch = True
    options = options or {}
    if 'ajax' not in options:
      options['ajax'] = {}
    options['ajax']['type'] = method
    options['ajax']['url'] = url
    options['ajax']['data'] = js_data
    if is_json:
      options['ajax']['dataType'] = 'json'
    return self.onReady(self.js.ajaxSelectPicker(options))

  def __str__(self):
    options, opt_groups = [], {}
    if self.options.all:
      opt = HtmlSelect.Option(self.page, "all", "All", None,
                   self.options.selected is not None and self.options.selected == "all")
      opt.options.managed = False
      options.append(opt.html())
    if self.options.empty:
      opt = HtmlSelect.Option(self.page, "", "", None,
                   self.options.selected is not None and self.options.selected == "")
      opt.options.managed = False
      options.append(opt.html())
    for val in self.val:
      opt = HtmlSelect.Option(self.page, val['value'], val.get('name', val.get('text', '')), None,
                   self.options.selected is not None and self.options.selected == val['value'],
                   options={"data": {"content": val.get('content'), "icon": val.get('icon')}})
      opt.options.managed = False
      if 'group' in val:
        opt_groups.setdefault(val['group'], []).append(opt)
      else:
        options.append(opt.html())
    data = options
    for k in sorted(opt_groups):
      opt_rp = HtmlSelect.Optgroup(self.page, opt_groups[k], k)
      opt_rp.options.managed = False
      data.append(opt_rp.html())
    self.page.properties.js.add_builders(
      "%s.selectpicker(%s).selectpicker('refresh')" % (self.dom.jquery.varId, json.dumps(self._jsStyles)))
    if self.attr.get("data-width") is not None:
      self.page.css.customText('.%s_width {width: %s !IMPORTANT}' % (self.htmlCode, self.attr.get("data-width")))
      self.attr['class'].add("%s_width" % self.htmlCode)
    if self.attr.get("data-background") is not None:
      if self.attr.get("data-color") is not None:
        self.page.css.customText('.%s_background {background: %s !IMPORTANT; color: %s !IMPORTANT}' % (
          self.htmlCode, self.attr.get("data-background"), self.attr.get("data-color")))
      else:
        self.page.css.customText('.%s_background {background: %s !IMPORTANT}' % (
          self.htmlCode, self.attr.get("data-background")))
      self.attr['class'].add("%s_background" % self.htmlCode)
    if self.button_css is not None:
      self.page.css.customText('.%s_button_bespoke {%s}' % (self.htmlCode, ";".join(["%s: %s !IMPORTANT" % (k, v) for k, v in self.button_css.items()])))
      self.attr['class'].insert(0, "%s_button_bespoke" % self.htmlCode)
    data_cls = self.get_attrs(css_class_names=self.style.get_classes()).replace('class="', 'data-style="')
    return "<select %s>%s</select>" % (data_cls, "".join(data))


class Lookup(Select):
  requirements = ('bootstrap-select', )

  def __init__(self, report, records, html_code, width, height, profile, multiple, options):
    super(Lookup, self).__init__(report, records, html_code, width, height, profile, multiple, options)
    self._jsStyles['lookups'] = records

  _js__builder__ = '''
    var selectObj = %s; selectObj.empty(); const lookupData = options.lookups[data];
    if (typeof lookupData !== 'undefined') {
      for (var idx in lookupData) {
          const text = (typeof lookupData[idx].text !== 'undefined')? lookupData[idx].text : lookupData[idx].value;
          selectObj.append('<option value=' + lookupData[idx].value + '>' + text + '</option>'); }
      selectObj.selectpicker(options).val(lookupData).selectpicker('refresh')}
    else {
      selectObj.selectpicker(options).selectpicker('refresh')}''' % JsQuery.decorate_var("htmlObj", convert_var=False)

  def __str__(self):
    self.page.properties.js.add_builders(
      "%s.selectpicker().selectpicker('refresh')" % JsQuery.decorate_var(self.dom.varId, convert_var=False))
    data_cls = self.get_attrs(css_class_names=self.style.get_classes()).replace('class="', 'data-style="')
    return "<select %s></select>" % data_cls