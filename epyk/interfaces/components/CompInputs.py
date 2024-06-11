#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Optional, List
from epyk.core.py import types

from epyk.core import html
from epyk.core.html import Defaults
from epyk.interfaces import Arguments


class Inputs:

    def __init__(self, ui):
        self.page = ui.page

    def d_text(self, text: str = "", placeholder: str = '',
               width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (None, "px"), tooltip: str = None,
               html_code: str = None, options: types.OPTION_TYPE = None, attrs: dict = None,
               profile: types.PROFILE_TYPE = None) -> html.HtmlInput.Input:
        """

        Usage::

          page.ui.inputs.d_text()

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlInput.Input`

        :param text: Optional. The value to be displayed to the component
        :param placeholder: Optional. Text visible when the input component is empty
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param options: Optional. Specific Python options available for this component
        :param attrs: Optional. Specific HTML tags to be added to the component
        :param tooltip: Optional. A string with the value of the tooltip
        :param profile: Optional. A flag to set the component performance storage
        """
        width = Arguments.size(width, unit="px")
        height = Arguments.size(height, unit="px")
        options = options or {}
        attrs = attrs or {}
        html_input = html.HtmlInput.Input(
            self.page, text, placeholder, width, height, html_code, options, attrs, profile)
        html_input.style.css.margin_bottom = '2px'
        html.Html.set_component_skin(html_input)
        if tooltip:
            html_input.tooltip(tooltip)
        return html_input

    def d_radio(self, flag: bool = False, group_name: str = None, placeholder: str = '', tooltip: str = None,
                width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (None, "px"), html_code: str = None,
                options: types.OPTION_TYPE = None, attrs: dict = None,
                profile: types.PROFILE_TYPE = None) -> html.HtmlInput.InputRadio:
        """
        Add a radio component.

        Usage::

          page.ui.inputs.d_radio()

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlInput.InputRadio`

        :param flag: Optional. The component init value
        :param group_name: Optional. The radio group name
        :param placeholder: Optional. Text visible when the input component is empty
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param options: Optional. Specific Python options available for this component
        :param attrs: Optional. Specific HTML tags to be added to the component
        :param tooltip: Optional. A string with the value of the tooltip
        :param profile: Optional. A flag to set the component performance storage
        """
        options = options or {}
        attrs = attrs or {}
        html_input = html.HtmlInput.InputRadio(self.page, flag, group_name, placeholder, width, height, html_code,
                                               options, attrs, profile)
        html.Html.set_component_skin(html_input)
        if tooltip:
            html_input.tooltip(tooltip)
        return html_input

    def d_search(self, text: str = "", placeholder: str = '', width: types.SIZE_TYPE = (100, "%"),
                 height: types.SIZE_TYPE = (None, "px"), html_code: str = None, options: types.OPTION_TYPE = None,
                 attrs: dict = None, tooltip: str = None,
                 profile: types.PROFILE_TYPE = None) -> html.HtmlInput.Input:
        """
        One of the new types of inputs in HTML5 is search.

        Usage::

          page.ui.inputs.d_search("")

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlInput.Input`

        Related Pages:

          https://developer.mozilla.org/fr/docs/Web/HTML/Element/Input/search
          https://css-tricks.com/webkit-html5-search-inputs/

        :param text: Optional. The value to be displayed to the component
        :param placeholder: Optional. Text visible when the input component is empty
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param options: Optional. Specific Python options available for this component
        :param attrs: Optional. Specific HTML tags to be added to the component
        :param tooltip: Optional. A string with the value of the tooltip
        :param profile: Optional. A flag to set the component performance storage
        """
        attrs = attrs or {}
        html_search = html.HtmlInput.Input(self.page, text, placeholder, width, height, html_code, options, attrs,
                                           profile)
        attrs.update({"type": 'search'})
        html.Html.set_component_skin(html_search)
        if tooltip:
            html_search.tooltip(tooltip)
        return html_search

    def password(self, text: str = "", placeholder: str = '', width: types.SIZE_TYPE = (100, "%"),
                 height: types.SIZE_TYPE = (None, "px"), html_code: str = None, options: types.OPTION_TYPE = None,
                 attrs: dict = None, tooltip: str = None, profile: types.PROFILE_TYPE = None) -> html.HtmlInput.Input:
        """
        Input field that will hide characters typed in.

        Usage::

          page.ui.inputs.password(placeholder="Password")

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlInput.Input`

        :param text: Optional. The value to be displayed to the component
        :param placeholder: Optional. Text visible when the input component is empty
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param options: Optional. Specific Python options available for this component
        :param attrs: Optional. Specific HTML tags to be added to the component
        :param tooltip: Optional. A string with the value of the tooltip
        :param profile: Optional. A flag to set the component performance storage
        """
        attrs = attrs or {}
        attrs.update({"type": 'password'})
        component = html.HtmlInput.Input(self.page, text, placeholder, width, height, html_code, options, attrs,
                                         profile)
        html.Html.set_component_skin(component)
        if tooltip:
            component.tooltip(tooltip)
        return component

    def file(self, text: str = "", placeholder: str = '', width: types.SIZE_TYPE = (100, "%"),
             height: types.SIZE_TYPE = (None, "px"), html_code: str = None, options: types.OPTION_TYPE = None,
             attrs: dict = None, tooltip: str = None, profile: types.PROFILE_TYPE = None) -> html.HtmlInput.InputFile:
        """
        Input field that will hide characters typed in

        Usage::

          page.ui.inputs.file()

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlInput.InputFile`

        :param text: Optional. The value to be displayed to the component
        :param placeholder: Optional. Text visible when the input component is empty
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param options: Optional. Specific Python options available for this component
        :param attrs: Optional. Specific HTML tags to be added to the component
        :param tooltip: Optional. A string with the value of the tooltip
        :param profile: Optional. A flag to set the component performance storage
        """
        attrs = attrs or {}
        component = html.HtmlInput.InputFile(self.page, text, placeholder, width, height, html_code, options, attrs,
                                             profile)
        html.Html.set_component_skin(component)
        if tooltip:
            component.tooltip(tooltip)
        return component

    def d_time(self, text: str = "", placeholder: str = '', width: types.SIZE_TYPE = (None, "px"),
               height: types.SIZE_TYPE = (None, "px"), html_code: str = None, options: types.OPTION_TYPE = None,
               attrs: dict = None, tooltip: str = None, profile: types.PROFILE_TYPE = None) -> html.HtmlInput.InputTime:
        """
        A lightweight, customizable javascript timepicker plugin for jQuery inspired by Google Calendar.

        Usage::

          date = page.ui.inputs.d_time()

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlInput.InputTime`

        :param text: Optional. The value to be displayed to the component
        :param placeholder: Optional. Text visible when the input component is empty
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param options: Optional. Specific Python options available for this component
        :param attrs: Optional. Specific HTML tags to be added to the component
        :param tooltip: Optional. A string with the value of the tooltip
        :param profile: Optional. A flag to set the component performance storage
        """
        dflt_options = {'timeFormat': 'h:i:s'}
        dflt_options.update(options or {})
        html_input_t = html.HtmlInput.InputTime(
            self.page, text, placeholder, width, height, html_code, dflt_options, attrs or {}, profile)
        html.Html.set_component_skin(html_input_t)
        if tooltip:
            html_input_t.tooltip(tooltip)
        return html_input_t

    def d_date(self, text: str="", placeholder: str = '', width: types.SIZE_TYPE = (None, "px"),
               height: types.SIZE_TYPE = (None, "px"), html_code: str = None, options: types.OPTION_TYPE = None,
               attrs: dict = None, tooltip: str = None, profile: types.PROFILE_TYPE = None) -> html.HtmlInput.InputDate:
        """

        Usage::

          date = page.ui.inputs.d_date()

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlInput.InputDate`

        :param text: Optional. The value to be displayed to the component
        :param placeholder: Optional. Text visible when the input component is empty
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param options: Optional. Specific Python options available for this component
        :param attrs: Optional. Specific HTML tags to be added to the component
        :param tooltip: Optional. A string with the value of the tooltip
        :param profile: Optional. A flag to set the component performance storage
        """
        html_date = html.HtmlInput.InputDate(
            self.page, text, placeholder, width, height, html_code, options, attrs or {}, profile)
        html.Html.set_component_skin(html_date)
        if tooltip:
            html_date.tooltip(tooltip)
        return html_date

    def d_int(self, value: str = "", placeholder: str = '', width: types.SIZE_TYPE = (100, "%"),
              height: types.SIZE_TYPE = (None, "px"), html_code: str = None, options: types.OPTION_TYPE = None,
              attrs: dict = None, tooltip: str = None,
              profile: types.PROFILE_TYPE = None) -> html.HtmlInput.InputInteger:
        """

        Usage::

          date = page.ui.inputs.d_int()

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlInput.InputInteger`

        :param value: Optional. The value of this input number field
        :param placeholder: Optional. Text visible when the input component is empty
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param options: Optional. Specific Python options available for this component
        :param attrs: Optional. Specific HTML tags to be added to the component
        :param tooltip: Optional. A string with the value of the tooltip
        :param profile: Optional. A flag to set the component performance storage
        """
        attrs = attrs or {}
        attrs.update({"type": 'number'})
        html_integer = html.HtmlInput.InputInteger(
            self.page, value, placeholder, width, height, html_code, options, attrs, profile)
        html.Html.set_component_skin(html_integer)
        if tooltip:
            html_integer.tooltip(tooltip)
        return html_integer

    def d_range(self, value, min_val: float = 0, max_val: float = 100, step: float = 1, placeholder: str = '',
                width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (None, "px"), tooltip: str = None,
                html_code: str = None, options: types.OPTION_TYPE = None, attrs: dict = None,
                profile: types.PROFILE_TYPE = None) -> html.HtmlInput.InputRange:
        """

        Usage::

        :param value: Optional. The value of the component
        :param min_val: Optional. The minimum value
        :param max_val: Optional. The maximum value
        :param step: Optional. The step when the handle is moved
        :param placeholder: Optional. Text visible when the input component is empty
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param options: Optional. Specific Python options available for this component
        :param attrs: Optional. Specific HTML tags to be added to the component
        :param tooltip: Optional. A string with the value of the tooltip
        :param profile: Optional. A flag to set the component performance storage
        """
        attrs = attrs or {}
        attrs.update({"type": 'range'})
        html_range = html.HtmlInput.InputRange(self.page, value, min_val, max_val, step, placeholder, width, height,
                                               html_code, options or {"background": False}, attrs, profile)
        html.Html.set_component_skin(html_range)
        if tooltip:
            html_range.tooltip(tooltip)
        return html_range

    def _output(self, value: str = "", options: types.OPTION_TYPE = None,
                profile: Optional[types.PROFILE_TYPE] = False) -> html.HtmlInput.Output:
        """
        Create a HTML output object.

        Usage::

          page.ui.inputs._output("test output")

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlInput.Output`

        :param value: Optional. The value to be displayed to the component
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        html_output = html.HtmlInput.Output(self.page, value, options=options, profile=profile)
        html.Html.set_component_skin(html_output)
        return html_output

    def textarea(self, text: str = "", width: types.SIZE_TYPE = (100, '%'), rows: int = 5, placeholder: str = None,
                 background_color: str = None, html_code: str = None, options: types.OPTION_TYPE = None,
                 tooltip: str = None, profile: types.PROFILE_TYPE = None) -> html.HtmlInput.TextArea:
        """
        Add textarea component.

        Usage::

          page.ui.inputs.textarea("Test")

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlInput.TextArea`

        Related Pages:

          https://www.w3schools.com/tags/tag_textarea.asp

        :param text: Optional. The value to be displayed to the component
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param rows:
        :param placeholder: Optional. Text visible when the input component is empty
        :param background_color:
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param options: Optional. Specific Python options available for this component
        :param tooltip: Optional. A string with the value of the tooltip
        :param profile: Optional. A flag to set the component performance storage
        """
        dflt_options = {"spellcheck": False, 'selectable': False}
        dflt_options.update(options or {})
        html_t_area = html.HtmlInput.TextArea(
            self.page, text, width, rows, placeholder, background_color, html_code, dflt_options, profile)
        html.Html.set_component_skin(html_t_area)
        if tooltip:
            html_t_area.tooltip(tooltip)
        return html_t_area

    def autocomplete(self, text: str = "", placeholder: str = '', width: types.SIZE_TYPE = (100, "%"),
                     height: types.SIZE_TYPE = (None, "px"), html_code: str = None, options: types.OPTION_TYPE = None,
                     attrs: dict = None, tooltip: str = None,
                     profile: types.PROFILE_TYPE = None) -> html.HtmlInput.AutoComplete:
        """
        Enables users to quickly find and select from a pre-populated list of values as they type, leveraging searching
        and filtering.

        Usage::

          page.ui.inputs.autocomplete("Test")

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlInput.AutoComplete`


        Related Pages:

          https://jqueryui.com/autocomplete/

        :param text: Optional. The value to be displayed to the component
        :param placeholder: Optional. Text visible when the input component is empty
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param options: Optional. Specific Python options available for this component
        :param attrs: Optional. Specific HTML tags to be added to the component
        :param tooltip: Optional. A string with the value of the tooltip
        :param profile: Optional. A flag to set the component performance storage
        """
        options = options or {}
        attrs = attrs or {}
        html_input = html.HtmlInput.AutoComplete(
            self.page, text, placeholder, width, height, html_code, options, attrs, profile)
        html_input.style.css.text_align = "left"
        html_input.style.css.padding_left = 5
        # Take into account the padding left in the width size.
        # TODO: Think about a more flexible way to do this.
        # html_input.style.css.width = Defaults.INPUTS_MIN_WIDTH - 5
        html.Html.set_component_skin(html_input)
        if tooltip:
            html_input.tooltip(tooltip)
        return html_input

    def input(self, text: str = "", placeholder: str = '', width: types.SIZE_TYPE = (100, "%"),
              height: types.SIZE_TYPE = (None, "px"), html_code: str = None, options: types.OPTION_TYPE = None,
              attrs: dict = None, tooltip: str = None, profile: types.PROFILE_TYPE = None) -> html.HtmlInput.Input:
        """
        Add a standard input component.

        Usage::

          page.ui.inputs.input("Test")

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlInput.Input`

        Templates:

          https://github.com/epykure/epyk-templates/blob/master/locals/components/list.py
          https://github.com/epykure/epyk-templates/blob/master/locals/components/modal.py
          https://github.com/epykure/epyk-templates/blob/master/locals/components/popup_info.py

        :param text: Optional. The value to be displayed to the component
        :param placeholder: Optional. Text visible when the input component is empty
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param options: Optional. Specific Python options available for this component
        :param attrs: Optional. Specific HTML tags to be added to the component
        :param tooltip: Optional. A string with the value of the tooltip
        :param profile: Optional. A flag to set the component performance storage
        """
        component = self.d_text(text=text, placeholder=placeholder, width=width, height=height, tooltip=tooltip,
                                html_code=html_code, options=options, attrs=attrs, profile=profile)
        html.Html.set_component_skin(component)
        return component

    def left(self, text: str = "", placeholder: str = '', width: types.SIZE_TYPE = (100, "%"),
             height: types.SIZE_TYPE = (None, "px"), html_code: str = None, options: types.OPTION_TYPE = None,
             attrs: dict = None, tooltip: str = None, profile: types.PROFILE_TYPE = None) -> html.HtmlInput.Input:
        """
        Add a standard input component.

        Usage::

          page.ui.inputs.left("Test")

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlInput.Input`

        Templates:

          https://github.com/epykure/epyk-templates/blob/master/locals/components/list.py
          https://github.com/epykure/epyk-templates/blob/master/locals/components/modal.py
          https://github.com/epykure/epyk-templates/blob/master/locals/components/popup_info.py

        :param text: Optional. The value to be displayed to the component
        :param placeholder: Optional. Text visible when the input component is empty
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param options: Optional. Specific Python options available for this component
        :param attrs: Optional. Specific HTML tags to be added to the component
        :param tooltip: Optional. A string with the value of the tooltip
        :param profile: Optional. A flag to set the component performance storage
        """
        component = self.d_text(text=text, placeholder=placeholder, width=width, height=height, tooltip=tooltip,
                                html_code=html_code, options=options, attrs=attrs, profile=profile)
        component.style.css.text_align = "left"
        component.style.css.padding_left = 5
        html.Html.set_component_skin(component)
        return component

    def hidden(self, text: str = "", placeholder: str = '', width: types.SIZE_TYPE = (100, "%"),
               height: types.SIZE_TYPE = (None, "px"), html_code: str = None, options: types.OPTION_TYPE = None,
               attrs: dict = None, tooltip: str = None, profile: types.PROFILE_TYPE = None) -> html.HtmlInput.Input:
        """
        Add a hidden input component to the page.
        This could be used to store data to then be passed to underlying services,

        Usage::

          rptObj.ui.inputs.hidden("Test")

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlInput.Input`

        :param text: Optional. The value to be displayed to the component
        :param placeholder: Optional. Text visible when the input component is empty
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param options: Optional. Specific Python options available for this component
        :param attrs: Optional. Specific HTML tags to be added to the component
        :param tooltip: Optional. A string with the value of the tooltip
        :param profile: Optional. A flag to set the component performance storage
        """
        component = self.d_text(text=text, placeholder=placeholder, width=width, height=height, tooltip=tooltip,
                                html_code=html_code, options=options, attrs=attrs, profile=profile)
        component.style.css.display = None
        html.Html.set_component_skin(component)
        return component

    def checkbox(self, flag: bool, label: str = "", group_name: str = None, width: types.SIZE_TYPE = (None, "%"),
                 height: types.SIZE_TYPE = (None, "px"), html_code: str = None,
                 options: types.OPTION_TYPE = None, attrs: dict = None, tooltip: str = "",
                 profile: types.PROFILE_TYPE = None) -> html.HtmlInput.InputCheckbox:
        """

        Usage::

          page.ui.inputs.checkbox(False)

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlInput.Checkbox`

        Templates:

          https://github.com/epykure/epyk-templates/blob/master/locals/components/checkbox.py

        :param flag:
        :param label: Optional. The text of label to be added to the component
        :param group_name: Optional.
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param options: Optional. Specific Python options available for this component
        :param attrs: Optional.
        :param tooltip: Optional. A string with the value of the tooltip.
        :param profile: Optional. A flag to set the component performance storage
        """
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        options = options or {}
        attrs = attrs or {}
        component = html.HtmlInput.InputCheckbox(
            self.page, flag, label, group_name, width, height, html_code, options, attrs, profile)
        html.Html.set_component_skin(component)
        if tooltip:
            component.tooltip(tooltip)
        return component

    def radio(self, flag: bool = False, label: str = None, group_name: str = None, icon: str = None,
              width: types.SIZE_TYPE = (None, "%"), height: types.SIZE_TYPE = (None, "px"), html_code: str = None,
              helper: str = None, options: types.OPTION_TYPE = None, tooltip: str = None, badge: str = None,
              profile: types.PROFILE_TYPE = None) -> html.HtmlInput.Radio:
        """

        Usage::

          page.ui.radio(['Single', 'Multiple'], html_code="type")

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlInput.Radio`

        Related Pages:

          https://www.w3schools.com/tags/att_input_type_radio.asp

        Templates:

          https://github.com/epykure/epyk-templates/blob/master/locals/components/radio.py

        :param flag:
        :param label: Optional.
        :param group_name: Optional.
        :param icon: Optional.
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param helper:
        :param tooltip: Optional. A string with the value of the tooltip
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        component = html.HtmlInput.Radio(
            self.page, flag, label, group_name, icon, width, height, html_code, helper, options or {}, profile)
        html.Html.set_component_skin(component)
        if tooltip:
            component.tooltip(tooltip)
        if badge:
            component.add_badge(badge)
        return component

    def editor(self, text: str = "", language: str = 'python', width: types.SIZE_TYPE = (100, "%"),
               height: types.SIZE_TYPE = (300, "px"), html_code: str = None, options: types.OPTION_TYPE = None,
               profile: types.PROFILE_TYPE = None) -> html.HtmlTextEditor.Editor:
        """

        Usage::

          page.ui.inputs.editor()

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlTextEditor.Editor`

        :param text: Optional. The value to be displayed to the componen
        :param language:
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        dflt_options = {
            "lineNumbers": True, 'mode': 'css', 'matchBrackets': True, 'styleActiveLine': True, 'autoRefresh': True}
        if options is not None:
            dflt_options.update(options)
        component = html.HtmlTextEditor.Editor(
            self.page, text, language, width, height, html_code, dflt_options, profile)
        html.Html.set_component_skin(component)
        return component

    def cell(self, text: str = "", language: str = 'python', width: types.SIZE_TYPE = (100, "%"),
             height: types.SIZE_TYPE = (60, "px"), html_code: str = None, options: types.OPTION_TYPE = None,
             profile: types.PROFILE_TYPE = None) -> html.HtmlTextEditor.Cell:
        """

        Usage::

          page.ui.inputs.cell()

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlTextEditor.Cell`

        :param text: Optional. The value to be displayed to the componen
        :param language:
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        dflt_options = {"lineNumbers": True, 'mode': language, 'matchBrackets': True, 'styleActiveLine': True,
                        'autoRefresh': True}
        if options is not None:
            dflt_options.update(options)
        component = html.HtmlTextEditor.Cell(
            self.page, text, language, width, height, html_code, dflt_options, profile)
        html.Html.set_component_skin(component)
        return component

    def search(self, text: str = '', placeholder: str = 'Search..', align: str = "left", color: str = None,
               width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (None, "px"),
               html_code: str = None, tooltip: str = None, extensible: bool = False, options: types.OPTION_TYPE = None,
               profile: types.PROFILE_TYPE = None) -> html.HtmlInput.Search:
        """
        Add an input search component.

        Usage::

          page.ui.inputs.search()

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlTextEditor.Cell`

        Related Pages:

          https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_anim_search

        Templates:

          https://github.com/epykure/epyk-templates/blob/master/locals/components/list_filter.py

        :param text: Optional. The value to be displayed to the componen
        :param placeholder:
        :param align: Optional. The text-align property within this component
        :param color:
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param tooltip: Optional. A string with the value of the tooltip
        :param extensible:
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        width = Arguments.size(width, unit="px")
        height = Arguments.size(height, unit="px")
        icon_details = self.page.icons.get("search")
        dflt_options = {"icon": icon_details["icon"], 'position': 'left', 'select': True, "border": 1}
        if options is not None:
            dflt_options.update(options)
        html_s = html.HtmlInput.Search(self.page, text, placeholder, color, width, height, html_code, tooltip,
                                       extensible, dflt_options, profile)
        html_s.style.css.height = self.page.body.style.globals.line_height + 5
        html_s.style.css.margin_bottom = 10
        if align == "center":
            html_s.style.css.margin = "auto"
            html_s.style.css.display = "block"
        html.Html.set_component_skin(html_s)
        return html_s

    def label(self, label: str, text: str = "", placeholder: str = '', width: types.SIZE_TYPE = (100, "%"),
              height: types.SIZE_TYPE = (None, "px"), html_code: str = None, tooltip: str = None,
              options: dict = None, attrs: dict = None, profile: types.PROFILE_TYPE = None) -> html.HtmlContainer.Div:
        """
        Add an input label component.

        Usage::

          page.ui.inputs.label()
          page.ui.inputs.label("test")

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlInput.Input`
          - :class:`epyk.core.html.HtmlText.Label`
          - :class:`epyk.core.html.HtmlContainer.Div`

        Templates:

          https://github.com/epykure/epyk-templates/blob/master/locals/components/links.py

        :param label:
        :param text:
        :param placeholder:
        :param width:
        :param height:
        :param html_code:
        :param tooltip: Optional. A string with the value of the tooltip.
        :param options:
        :param profile:
        :param attrs:
        """
        label = self.page.ui.texts.label(label).css({
            "display": 'block', 'text-align': 'left', 'margin-top': '10px', "position": "absolute", "z-index": '20px',
            "font-size": '%spx' % self.page.body.style.globals.font.header_size})
        html_input = html.HtmlInput.Input(self.page, text, placeholder, width, height, html_code,
                                          options or {}, attrs or {}, profile).css({"margin-top": '10px'})
        div = self.page.ui.div([label, html_input])
        div.input = html_input
        div.label = label
        html_input.on('focus', [
            "document.getElementById('%s').animate({'marginTop': ['10px', '-8px']}, {duration: 50, easing: 'linear', iterations: 1, fill: 'both'})" % label.htmlCode,
        ])
        html_input.on('blur', [
            "document.getElementById('%s').animate({'marginTop': ['-8px', '10px']}, {duration: 1000, easing: 'linear', iterations: 1, fill: 'both'})" % label.htmlCode,
        ])
        html.Html.set_component_skin(div)
        if tooltip:
            html_input.tooltip(tooltip)
        return div

    def filters(self, items: List[html.Html.Html] = None, button: html.Html.Html = None,
                width: types.SIZE_TYPE = ("auto", ""), height: types.SIZE_TYPE = (60, "px"), html_code: str = None,
                helper: str = None, options: dict = None, autocomplete: bool = False,
                profile: types.PROFILE_TYPE = None) -> html.HtmlContainer.Div:
        """

        :param items:
        :param button:
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param html_code:
        :param helper:
        :param autocomplete:
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        options = options or {}
        container = self.page.ui.div(width=width)
        container.select = self.page.ui.inputs.autocomplete(
            html_code="%s_select" % html_code if html_code is not None else html_code,
            width=(Defaults.TEXTS_SPAN_WIDTH, 'px'))
        container.select.style.css.text_align = "left"
        container.select.style.css.padding_left = 5
        container.select.options.liveSearch = True
        if autocomplete:
            container.input = self.page.ui.inputs.autocomplete(
                html_code="%s_input" % html_code if html_code is not None else html_code,
                width=(Defaults.INPUTS_MIN_WIDTH, 'px'), options={"select": True})
        else:
            container.input = self.page.ui.input(
                html_code="%s_input" % html_code if html_code is not None else html_code,
                width=(Defaults.INPUTS_MIN_WIDTH, 'px'), options={"select": True})
        container.input.style.css.text_align = 'left'
        container.input.style.css.padding_left = 5
        container.input.style.css.margin_left = 10
        if button is None:
            button = self.page.ui.buttons.colored("add")
            button.style.css.margin_left = 10
        container.button = button
        container.clear = self.page.ui.icon("times", options=options)
        container.clear.style.css.color = self.page.theme.danger.base
        container.clear.style.css.margin_left = 20
        container.clear.tooltip("Clear all filters")
        container.add(self.page.ui.div([container.select, container.input, container.button, container.clear]))
        container.filters = self.page.ui.panels.filters(
            items, container.select.dom.content, (100, '%'), height, html_code, helper, options, profile)
        container.add(container.filters)
        container.clear.click([container.filters.dom.clear()])
        container.button.click([
            container.filters.dom.add(container.input.dom.content, container.select.dom.content),
            container.input.js.empty()
        ])
        container.input.enter(container.button.dom.events.trigger("click"))
        html.Html.set_component_skin(container)
        return container
