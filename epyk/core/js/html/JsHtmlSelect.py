#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtml
from epyk.core.js.primitives import JsObjects
from epyk.core.js.objects import JsNodeDom


class JsHtmlSwitch(JsHtml.JsHtmlRich):

  @property
  def content(self):
    """
    Description:
    ------------

    Usage:
    -----
    """
    return JsHtml.ContentFormatters(self._report, "%s.checked" % self._src.checkbox.dom.varName)

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
    return JsObjects.JsObjects.get(''' if(%(text)s == %(htmlCode)s_data.%(switch_type)s){ %(htmlObj)s };
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
        self.htmlCode, self.content.toStr(), self.text, self.options_text))

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
  def options_text(self):
    """
    Description:
    ------------
    Get the selected content from the Select component.

    Usage:
    -----
    """
    return JsObjects.JsObjects.get("%s.text()" % self.jquery.varId)


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
