#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union
from epyk.core.py import primitives

from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtml
from epyk.core.js.primitives import JsObjects
from epyk.core.js.objects import JsNodeDom


class JsHtmlSwitch(JsHtml.JsHtmlRich):

    @property
    def val(self):
        """Return the val object.

        Usage::

          mode_switch = page.ui.fields.toggle({"off": 'hidden', "on": "visible"}, is_on=True, label="", htmlCode="switch")
          mode_switch.input.click([page.js.console.log(mode_switch.input.dom.val)])
        """
        values = ["'%s': %s" % (
            k, self.page.components[k].dom.content.toStr()) for k in self.component._internal_components]
        values.append("'%s_values': %s" % (self.component.html_code, self.component._vals))
        return JsObjects.JsObjects.get(
            "{%s, offset: new Date().getTimezoneOffset()}" % ", ".join(values))

    @property
    def content(self):
        """ """
        return JsHtml.ContentFormatters(self.page, "%s.checked" % self.component.checkbox.dom.varName)

    @property
    def label(self):
        """

        Usage::

          mode_switch = page.ui.fields.toggle({"off": 'hidden', "on": "visible"}, is_on=True, label="", htmlCode="switch")
          mode_switch.input.click([
            page.js.console.log(mode_switch.input.dom.label),
            icon.dom.visible(mode_switch.input.dom.content)
          ])
        """
        return JsHtml.ContentFormatters(self.page, self.component.switch_text.dom.innerText())

    def set_text(self, value: Union[str, primitives.JsDataModel], is_on_val: bool = True):
        """Change the value of the text component.

        Usage::

          sw = page.ui.buttons.switch()
          page.ui.button("test").click([
          sw.dom.set_text("ok")])

        :param value: The new value
        :param is_on_val: Optional. Change either the on or the off value displayed
        """
        value = JsUtils.jsConvertData(value, None)
        return JsObjects.JsObjects.get('''if(%(text)s == %(htmlCode)s_data.%(switch_type)s){%(htmlObj)s};
       %(htmlCode)s_data.%(switch_type)s = %(value)s
       ''' % {'htmlCode': self.component.html_code, 'switch_type': 'on' if is_on_val else 'off', 'value': value,
              'text': self.component.switch_text.dom.content.toStr(),
              'htmlObj': self.component.switch_text.build(value)})


class Tick(JsHtml.JsHtmlRich):

    @property
    def val(self):
        """ """
        return JsObjects.JsObjects.get(
            "{%s: {value: %s, label: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
                self.htmlCode, self.content.toStr(), self.component.span.dom.content.toStr()))

    @property
    def content(self):
        """ Get the selected content from the Select component. """
        # the option variable is coming from the Tick class to get the icon details
        return JsHtml.ContentFormatters(self.page, "%s.classList.contains('%s')" % (
            self.component.icon.dom.varName, self.options['true'].split(" ")[-1]))


class SelectOption(JsHtml.JsHtmlRich):

    @property
    def content(self):
        """Get the value of the selected option.
        This will not return the text displayed in the UI.
        """
        return self.value()

    def text(self, value: Union[str, primitives.JsDataModel] = None):
        """Change the text of the selected option.
        Refresh of the selectPicker object is needed to make the changes visible.

        :param Uvalue: Optional. The value to be set to the option text
        """
        if value is None:
            return JsObjects.JsVoid("%(varId)s.innerText" % {"varId": self.varId})

        value = JsUtils.jsConvertData(value, None)
        return JsObjects.JsVoid("%(varId)s.innerText = %(value)s" % {"varId": self.varId, "value": value})

    def value(self, value: Union[str, primitives.JsDataModel] = None):
        """Set the value tag of the selected items in the selection box.
        This will not change the display but only the value tag in the selected option.

        :param value: Optional. The value to be added to the tag
        """
        if value is None:
            return JsObjects.JsVoid("%(varId)s.getAttribute()" % {"varId": self.varId})

        value = JsUtils.jsConvertData(value, None)
        return JsObjects.JsVoid("%(varId)s.setAttribute('value', %(value)s)" % {"varId": self.varId, "value": value})

    @property
    def index(self):
        """Get the index of the selected option. """
        return JsObjects.JsVoid("%(varId)s.index" % {"varId": self.varId})


class DomSelect(JsHtml.JsHtmlRich):

    @property
    def val(self):
        """Get the select Picker selected values. """
        return JsObjects.JsObjects.get(
            "{%s: {value: %s, text: %s, options_text: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
                self.htmlCode, self.content.toStr(), self.text, self.selected.text().toStr()))

    @property
    def content(self):
        """Get the selected content from the Select component.  """
        return JsHtml.ContentFormatters(self.page, "%s.val()" % self.jquery.varId)

    @property
    def text(self):
        """Get the selected content from the Select component. """
        return JsObjects.JsObjects.get("%s.find('option:selected').text()" % self.jquery.varId)

    @property
    def index(self):
        """Get the selected content from the Select component. """
        return JsObjects.JsObjects.get("%s.find('option:selected').index()" % self.jquery.varId)

    @property
    def all(self):
        """Get all the items in the selection box (selected or not)."""
        return JsObjects.JsObjects.get(
            "(function(){var result = []; %s.find('option').each(function(i, dom){result.push(dom.innerText)}); return result})()" % self.jquery.varId)

    def hide(self):
        """Hide the select component.

        Related Pages:

          https://developer.snapappointments.com/bootstrap-select/methods/#selectpickerhide
        """
        return JsObjects.JsObjects.get("%s.selectpicker('hide')" % self.jquery.varId)

    def show(self):
        """Show the select component.

        Related Pages:

          https://developer.snapappointments.com/bootstrap-select/methods/#selectpickershow
        """
        return JsObjects.JsObjects.get("%s.selectpicker('show')" % self.jquery.varId)

    @property
    def selected(self):
        """Get the selected option DOM. """
        select_opt = SelectOption(self.component, page=self.page, set_var=False)
        select_opt.varName = "%s.querySelector('option:checked')" % self.varId
        return select_opt

    def option(self, i: int):
        """Get a specific option HTML object in the select.

        :param i: The index of the option in the select component
        """
        select_opt = SelectOption(self.component, page=self.page, set_var=False)
        select_opt.varName = "%s.querySelectorAll('option')[%s]" % (self.varId, i)
        return select_opt

    def empty(self):
        """Change the selected items to be the empty value.

        Related Pages:

          https://developer.snapappointments.com/bootstrap-select/methods/
        """
        return JsUtils.jsWrap("%s.selectpicker('val', '')" % self.jquery.varId)


class Radio(JsHtml.JsHtmlRich):

    @property
    def content(self):
        """Get the selected content from the Select component. """
        # the option variable is coming from the Tick class to get the icon details
        return JsHtml.ContentFormatters(self.page,
                                        "(function(c){var comp = c.querySelector('input:checked'); if(comp !== null){return comp.getAttribute('data-content')} else{ return ''}})(%s)" % self.component.dom.varName)

    @property
    def checked(self):
        """returns the checked DOM object. """
        return JsNodeDom.JsDoms.get(
            "%s.querySelector('input:checked').parentNode" % self.component.dom.varName, page=self.page)

    def select(self, value: Union[str, primitives.JsDataModel]):
        """

        :param value:
        """
        value = JsUtils.jsConvertData(value, None)
        return JsObjects.JsVoid('''
%s.querySelectorAll('input').forEach(function(dom){
  if(dom.getAttribute('data-content') == %s){dom.checked = true}
})''' % (self.component.dom.varName, value))
