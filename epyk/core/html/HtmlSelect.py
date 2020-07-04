#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

from epyk.core.html import Html
from epyk.core.html.options import OptSelect

# The list of CSS classes
from epyk.core.css.styles import GrpClsList

#
from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtmlSelect
from epyk.core.js.packages import JsQuery
from epyk.core.js.packages import JsSelect


class Option(Html.Html):
  name = 'Select Option'
  builder_name = False

  def __init__(self, report, value, text, icon, selected):
    super(Option, self).__init__(report, text)
    self.set_attrs(name="value", value=value)
    if selected:
      self.set_attrs(name="selected", value=selected)
    if icon is not None:
      self.set_attrs(name="data-icon", value=icon)

  def __str__(self):
    return "<option %s>%s</option>" % (self.get_attrs(pyClassNames=self.style.get_classes()), self.val)


class Optgroup(Html.Html):
  name = 'Select Option'
  builder_name = False

  def __init__(self, report, data, label):
    super(Optgroup, self).__init__(report, data)
    self.set_attrs(name="label", value=label)

  def __str__(self):
    val = "".join([v.html() for v in self.val])
    return "<optgroup %s>%s</optgroup>" % (self.get_attrs(pyClassNames=self.style.get_classes()), val)


class Select(Html.Html):
  requirements = ('bootstrap-select', )
  name = 'Select'

  def __init__(self, report, records, htmlCode, width, height, filter, profile, multiple, options):
    super(Select, self).__init__(report, records, htmlCode=htmlCode, css_attrs={"width": width, "height": height},
                                 profile=profile)
    self.selected = None
    if multiple:
      self.attr['multiple'] = None
    self.__options = OptSelect.OptionsSelect(self, options)

  @property
  def options(self):
    """
    Property to set all the possible object for a button

    :rtype: OptSelect.OptionsSelect
    """
    return self.__options

  @property
  def style(self):
    """
    Description:
    -----------

    :rtype: GrpClsList.ClassSelect
    """
    if self._styleObj is None:
      self._styleObj = GrpClsList.ClassSelect(self)
    return self._styleObj

  @property
  def dom(self):
    """
    Description:
    -----------
    Javascript Functions

    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    Attributes:
    ----------
    :return: A Javascript Dom object

    :rtype: JsHtmlSelect.DomSelect
    """
    if self._dom is None:
      self._dom = JsHtmlSelect.DomSelect(self, report=self._report)
    return self._dom

  @property
  def js(self):
    """
    Description:
    -----------
    Javascript Functions

    Return all the Javascript functions defined for an HTML Component.
    Those functions will use plain javascript by default.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/methods/

    Attributes:
    ----------
    :return: A Javascript Dom object

    :rtype: JsSelect.JSelect
    """
    if self._js is None:
      self._js = JsSelect.JSelect(self, report=self._report)
    return self._js

  @property
  def _js__builder__(self):
    return '''
      var selectObj = %s; selectObj.empty(); 
      for (var idx in data) {
          const text = (typeof data[idx].text !== 'undefined')? data[idx].text : data[idx].value;
          selectObj.append('<option value=' + data[idx].value + '>' + text + '</option>'); }
      selectObj.selectpicker(options).val().selectpicker('refresh');''' % JsQuery.decorate_var("htmlObj", convert_var=False)

  def change(self, jsFncs, emtpyFncs=None, profile=False):
    """
    Description:
    -----------
    Javascript event triggered when the value has changed

    Attributes:
    ----------
    :param jsFncs: List. Set of Javascript function to trigger on this event
    :param emtpyFncs: ist. Set of Js function to trigger if the value is empty
    :param profile: Boolean. To set the profiling
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    if emtpyFncs is not None:
      if not isinstance(emtpyFncs, list):
        emtpyFncs = [emtpyFncs]
      jsFncs.append("if (%s === ''){ %s }" % (self.dom.content.toStr(), JsUtils.jsConvertFncs(emtpyFncs, toStr=True)))
    return self.on("change", jsFncs, profile)

  def ajax(self, url, jsData="function (){return {q: '{{{q}}}'}}", is_json=True, method="POST", options=None):
    """
    Description:
    -----------

    Related Pages:

      https://github.com/truckingsim/Ajax-Bootstrap-Select

    Attributes:
    ----------
    :param options:
    """
    self.options.liveSearch = True
    options = options or {}
    if 'ajax' not in options:
      options['ajax'] = {}
    options['ajax']['type'] = method
    options['ajax']['url'] = url
    options['ajax']['data'] = jsData
    if is_json:
      options['ajax']['dataType'] = 'json'
    return self.onReady(self.js.ajaxSelectPicker(options))

  def __str__(self):
    options, opt_groups = [], {}
    for val in self.val:
      opt = Option(self._report, val['value'], val['name'], None, self.selected is not None and self.selected == val['value'])
      opt.options.managed = False
      if 'group' in val:
        opt_groups.setdefault(val['group'], []).append(opt)
      else:
        options.append(opt.html())
    data = options
    for k in sorted(opt_groups):
      opt_rp = Optgroup(self._report, opt_groups[k], k)
      opt_rp.options.managed = False
      data.append(opt_rp.html())
    self._report._props.setdefault('js', {}).setdefault("builders", []).append("%s.selectpicker(%s).selectpicker('refresh')" % (JsQuery.decorate_var(self.dom.varId, convert_var=False), json.dumps(self._jsStyles)))
    if self.attr.get("data-width") is not None:
      self._report.css.customText('.%s_width {width: %s !IMPORTANT}' % (self.htmlCode, self.attr.get("data-width")))
    self.attr['class'].add("%s_width" % self.htmlCode)
    data_cls = self.get_attrs(pyClassNames=self.style.get_classes()).replace('class="', 'data-style="')
    return "<select %s>%s</select>" % (data_cls, "".join(data))


class Lookup(Select):
  requirements = ('bootstrap-select', )

  def __init__(self, report, records, htmlCode, width, height, filter, profile, multiple, options):
    super(Lookup, self).__init__(report, records, htmlCode, width, height, filter, profile, multiple, options)
    self._jsStyles['lookups'] = records

  @property
  def _js__builder__(self):
    return '''
        var selectObj = %s; selectObj.empty(); const lookupData = options.lookups[data];
        if (typeof lookupData !== 'undefined') {
          for (var idx in lookupData) {
              const text = (typeof lookupData[idx].text !== 'undefined')? lookupData[idx].text : lookupData[idx].value;
              selectObj.append('<option value=' + lookupData[idx].value + '>' + text + '</option>'); }
          selectObj.selectpicker(options).val(lookupData).selectpicker('refresh')}
        else {selectObj.selectpicker(options).selectpicker('refresh')} ''' % JsQuery.decorate_var("htmlObj", convert_var=False)

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append("%s.selectpicker().selectpicker('refresh')" % JsQuery.decorate_var(self.dom.varId, convert_var=False))
    data_cls = self.get_attrs(pyClassNames=self.style.get_classes()).replace('class="', 'data-style="')
    return "<select %s></select>" % data_cls
