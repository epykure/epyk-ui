#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtml
from epyk.core.js.primitives import JsObjects
from epyk.core.js.objects import JsNodeDom


class JsHtmlSwitch(JsHtml.JsHtmlRich):

  @property
  def val(self):
    """
    Description:
    -----------
    Return the val object.

    Usage:
    -----

      mode_switch = page.ui.fields.toggle({"off": 'hidden', "on": "visible"}, is_on=True, label="", htmlCode="switch")
      mode_switch.input.click([
        page.js.console.log(mode_switch.input.dom.val)
      ])
    """
    values = ["'%s': %s" % (k, self._report.components[k].dom.content.toStr()) for k in self._src._internal_components]
    values.append("'%s_values': %s" % (self._src.htmlCode, self._src._vals))
    return JsObjects.JsObjects.get(
      "{%s, offset: new Date().getTimezoneOffset()}" % ", ".join(values))

  @property
  def content(self):
    """
    Description:
    ------------

    Usage:
    -----
    """
    return JsHtml.ContentFormatters(self._report, "%s.checked" % self._src.checkbox.dom.varName)

  @property
  def label(self):
    """
    Description:
    ------------

    Usage:
    -----

      mode_switch = page.ui.fields.toggle({"off": 'hidden', "on": "visible"}, is_on=True, label="", htmlCode="switch")
      mode_switch.input.click([
        page.js.console.log(mode_switch.input.dom.label),
        icon.dom.visible(mode_switch.input.dom.content)
      ])
    """
    return JsHtml.ContentFormatters(self._report, self._src.switch_text.dom.innerText())

  def set_text(self, value, is_on_val=True):
    """
    Description:
    ------------
    Change the value of the text component.

    Usage:
    -----

      sw = page.ui.buttons.switch()
      page.ui.button("test").click([
      sw.dom.set_text("ok")])

    Attributes:
    ----------
    :param value: String. The new value.
    :param is_on_val: Boolean. Optional. Change either the on or the off value displayed.
    """
    value = JsUtils.jsConvertData(value, None)
    return JsObjects.JsObjects.get('''if(%(text)s == %(htmlCode)s_data.%(switch_type)s){%(htmlObj)s};
       %(htmlCode)s_data.%(switch_type)s = %(value)s
       ''' % {'htmlCode': self._src.htmlCode, 'switch_type': 'on' if is_on_val else 'off', 'value': value,
              'text': self._src.switch_text.dom.content.toStr(), 'htmlObj': self._src.switch_text.build(value)})


class Tick(JsHtml.JsHtmlRich):

  @property
  def val(self):
    """
    Description:
    ------------

    Usage:
    -----
    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s, label: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
        self.htmlCode, self.content.toStr(), self._src.span.dom.content.toStr()))

  @property
  def content(self):
    """
    Description:
    ------------
    Get the selected content from the Select component.

    Usage:
    -----
    """
    # the option variable is coming from the Tick class to get the icon details
    return JsHtml.ContentFormatters(self._report, "%s.classList.contains('%s')" % (self._src.icon.dom.varName, self.options['true'].split(" ")[-1]))


class SelectOption(JsHtml.JsHtmlRich):

  @property
  def content(self):
    """
    Description:
    ------------
    Get the value of the selected option.
    This will not return the text displayed in the UI.
    """
    return self.value()

  def text(self, value=None):
    """
    Description:
    ------------
    Change the text of the selected option.

    Refresh of the selectPicker object is needed to make the changes visible.

    Attributes:
    ----------
    :param value: String. Optional. The value to be set to the option text.
    """
    if value is None:
      return JsObjects.JsVoid("%(varId)s.innerText" % {"varId": self.varId})

    value = JsUtils.jsConvertData(value, None)
    return JsObjects.JsVoid("%(varId)s.innerText = %(value)s" % {"varId": self.varId, "value": value})

  def value(self, value=None):
    """
    Description:
    ------------
    Set the value tag of the selected items in the selection box.
    This will not change the display but only the value tag in the selected option.

    Attributes:
    ----------
    :param value: String. Optional. The value to be added to the tag.
    """
    if value is None:
      return JsObjects.JsVoid("%(varId)s.getAttribute()" % {"varId": self.varId})

    value = JsUtils.jsConvertData(value, None)
    return JsObjects.JsVoid("%(varId)s.setAttribute('value', %(value)s)" % {"varId": self.varId, "value": value})

  @property
  def index(self):
    """
    Description:
    ------------
    Get the index of the selected option.
    """
    return JsObjects.JsVoid("%(varId)s.index" % {"varId": self.varId})


class DomSelect(JsHtml.JsHtmlRich):

  @property
  def val(self):
    """
    Description:
    ------------
    Get the select Picker selected values.

    Usage:
    -----
    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s, text: %s, options_text: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
        self.htmlCode, self.content.toStr(), self.text, self.selected.text()))

  @property
  def content(self):
    """
    Description:
    ------------
    Get the selected content from the Select component.

    Usage:
    -----
    """
    return JsHtml.ContentFormatters(self._report, "%s.val()" % self.jquery.varId)

  @property
  def text(self):
    """
    Description:
    ------------
    Get the selected content from the Select component.

    Usage:
    -----
    """
    return JsObjects.JsObjects.get("%s.find('option:selected').text()" % self.jquery.varId)

  @property
  def index(self):
    """
    Description:
    ------------
    Get the selected content from the Select component.

    Usage:
    -----
    """
    return JsObjects.JsObjects.get("%s.find('option:selected').index()" % self.jquery.varId)

  @property
  def all(self):
    """
    Description:
    ------------
    Get all the items in the selection box (selected or not).

    Usage:
    -----
    """
    return JsObjects.JsObjects.get("(function(){var result = []; %s.find('option').each(function(i, dom){result.push(dom.innerText)}); return result})()" % self.jquery.varId)

  def hide(self):
    """
    Description:
    ------------
    Hide the select component.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/methods/#selectpickerhide
    """
    return JsObjects.JsObjects.get("%s.selectpicker('hide')" % self.jquery.varId)

  def show(self):
    """
    Description:
    ------------
    Show the select component.

    Related Pages:

      https://developer.snapappointments.com/bootstrap-select/methods/#selectpickershow
    """
    return JsObjects.JsObjects.get("%s.selectpicker('show')" % self.jquery.varId)

  @property
  def selected(self):
    """
    Description:
    ------------
    Get the selected option DOM.
    """
    select_opt = SelectOption(self._src, report=self._report, setVar=False)
    select_opt.varName = "%s.querySelector('option:checked')" % self.varId
    return select_opt

  def option(self, i):
    """
    Description:
    ------------
    Get a specific option HTML object in the select.

    Attributes:
    ----------
    :param i: Integer. The index of the option in the select component.
    """
    select_opt = SelectOption(self._src, report=self._report, setVar=False)
    select_opt.varName = "%s.querySelectorAll('option')[%s]" % (self.varId, i)
    return select_opt


class Radio(JsHtml.JsHtmlRich):

  @property
  def content(self):
    """
    Description:
    ------------
    Get the selected content from the Select component.

    Usage:
    -----
    """
    # the option variable is coming from the Tick class to get the icon details
    return JsHtml.ContentFormatters(self._report, "%s.querySelector('input:checked').getAttribute('data-content')" % self._src.dom.varName)

  @property
  def checked(self):
    """
    Description:
    ------------
    returns the checked DOM object.

    Usage:
    -----
    """
    return JsNodeDom.JsDoms.get("%s.querySelector('input:checked').parentNode" % self._src.dom.varName, report=self._report)

  def select(self, value):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param value: String.
    """
    value = JsUtils.jsConvertData(value, None)
    return JsObjects.JsVoid('''
      %s.querySelectorAll('input').forEach(function(dom){
        if(dom.getAttribute('data-content') == %s){dom.checked = true}
      })''' % (self._src.dom.varName, value))
