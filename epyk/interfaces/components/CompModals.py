#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List

from epyk.core import html
from epyk.core.py import types
from epyk.interfaces import Arguments
from epyk.core.css import Defaults as Defaults_css


class Modals:

    def __init__(self, ui):
        self.page = ui.page

    def forms(self, components: html.Html.Html, action: str, method: str, header=None, footer=None,
              helper: types.HELPER_TYPE = None, html_code: str = None) -> html.HtmlContainer.Modal:
        """Simple interface to create a html form within a modal.

        Usage::

          d = page.ui.fields.today('test')
          i = page.ui.fields.input(placeholder='test2', label='test1')
          i2 = page.ui.fields.input('test3', label='test2')
          form_modal = page.ui.modals.forms([d, i, i2], "http://127.0.0.1:5000", "POST")

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlContainer.Modal`
          - :class:`epyk.core.html.HtmlContainer.Form`

        `w3schools <https://www.w3schools.com/w3css/w3css_modal.asp>`_

        :param components:
        :param action:
        :param method:
        :param header:
        :param footer:
        :param helper:
        :param html_code:
        """
        if not type(components) == list:
            components = [components]
        form = html.HtmlContainer.Form(self.page, components, helper)
        form.submit(method, action)
        modal = html.HtmlContainer.Modal(
            self.page, [], header, footer, False, helper, html_code=html_code)
        modal += form
        modal.form = form
        html.Html.set_component_skin(modal)
        return modal

    def disclaimer(self, disc_list, header=None, footer=None, submit: bool = True, validation_text: str = 'AGREE',
                   action: str = None, add_buttons=None, html_code: str = None, helper: types.HELPER_TYPE = None
                   ) -> html.HtmlContainer.Modal:
        """Disclaimer that will appear as a modal.

        Usage::

          privacy_title = page.ui.texts.title('A privacy reminder', 2)
          p1 = page.ui.texts.paragraph('''
            Scroll down and click “%s” when you’re ready to continue, or explore other options on this page.
            ''' % page.ui.tags.strong('''I agree''', options={'managed': False}))
          disc = page.ui.modals.disclaimer([privacy_title, p1])

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlContainer.Modal`
          - :class:`epyk.core.html.HtmlContainer.Row`
          - :class:`epyk.core.html.HtmlButton.Button`

        :param disc_list:
        :param header:
        :param footer:
        :param submit:
        :param validation_text:
        :param action:
        :param add_buttons:
        :param helper:
        """
        for obj in disc_list:
            obj.css({'margin': '40px', 'width': 'auto', 'text-align': 'justify'})
        modal = html.HtmlContainer.Modal(
            self.page, disc_list, header, footer, False, helper, html_code=html_code)
        modal.col.css({'width': '450px', 'height': '700px'})
        if add_buttons or submit:
            submit_row = self.page.ui.row([]) if not add_buttons else self.page.ui.row(add_buttons)
            if submit:
                submit_btn = self.page.ui.buttons.important(validation_text)
                if action:
                    submit_btn.click(action)
                else:
                    submit_btn.click(modal.close())
                submit_row + submit_btn
            modal.col + submit_row
        html.Html.set_component_skin(modal)
        return modal

    def dialog(self, text, width: types.SIZE_TYPE = (100, '%'), height: types.SIZE_TYPE = (20, 'px'),
               html_code: str = None, helper: types.HELPER_TYPE = None, options: dict = None,
               profile: types.PROFILE_TYPE = None) -> html.HtmlEvent.Dialog:
        """Simple Jquery UI modal with a text.

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlEvent.Dialog`

        `jqueryui <https://jqueryui.com/dialog/>`_

        :param text: Optional. The value to be displayed to the component.
        :param width: Optional. A tuple with the integer for the component width and its unit.
        :param height: Optional. A tuple with the integer for the component height and its unit.
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
        :param helper: Optional. A tooltip helper.
        :param options: Optional. Specific Python options available for this component.
        :param profile: Optional. A flag to set the component performance storage.
        """
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        html_pr = html.HtmlEvent.Dialog(self.page, text, width, height, helper, options or {}, html_code, profile)
        html.Html.set_component_skin(html_pr)
        return html_pr

    def icon(self, components: List[html.Html.Html] = None, icon: str = None, width: types.SIZE_TYPE = (100, '%'),
             height: types.SIZE_TYPE = (None, 'px'), html_code: str = None, options: dict = None,
             profile: types.PROFILE_TYPE = None) -> html.HtmlPopup.Popup:
        """Display a generic popup with an icon.

        Usage::

          popup = page.popup(page.ui.title('Test'), color="red")
          popup + page.paragraph('Test')

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlPopup.Popup`

        `W3schools <https://www.w3schools.com/tags/tag_div.asp>`_
        `Use case <https://github.com/epykure/epyk-templates/blob/master/locals/components/modals.py>`_

        :param components: The different HTML objects to be added to the component
        :param icon: Optional.
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = {'margin': 10, 'closure': False, 'top': 100, 'escape': False}
        if options is not None:
            dfl_options.update(options)
        if not isinstance(components, list):
            components = [components]
        if icon is not None:
            icon_success = self.page.ui.icon(icon)
            icon_success.style.css.font_size = 50
            icon_success.style.css.margin_bottom = 20
            icon_success.style.css.margin_top = 10
            success_div = self.page.ui.div(icon_success)
            success_div.style.css.text_align = "center"
            components.insert(0, success_div)
        popup = html.HtmlPopup.Popup(self.page, components, width, height, dfl_options, profile, html_code=html_code)
        acknowledgement = self.page.ui.button(
            dfl_options.get("button", {}).get("text", "Ok"), options=dfl_options.get("button"),
            align="center", html_code=popup.sub_html_code("button"))
        acknowledgement.style.css.margin_top = 10
        popup.add(acknowledgement)
        popup.acknowledgement = acknowledgement
        popup.button = popup.acknowledgement
        acknowledgement.click([popup.dom.hide()])
        html.Html.set_component_skin(popup)
        return popup

    def validation(self, components: List[html.Html.Html] = None, width: types.SIZE_TYPE = (100, '%'),
                   height: types.SIZE_TYPE = (None, 'px'), html_code: str = None, options: dict = None,
                   profile: types.PROFILE_TYPE = None) -> html.HtmlPopup.Popup:
        """

        Usage::

          popup = page.popup(page.ui.title('Test'), color="red")
          popup + page.paragraph('Test')

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlPopup.Popup`

        `W3schools <https://www.w3schools.com/tags/tag_div.asp>`_
        `Use case <https://github.com/epykure/epyk-templates/blob/master/locals/components/modals.py>`_

        :param components: The different HTML objects to be added to the component
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        icon_details = self.page.icons.get("close")
        dfl_options = {'margin': 10, 'closure': icon_details["icon"], 'top': 100}
        if options is not None:
            dfl_options.update(options)
        if not isinstance(components, list):
            components = [components]
        popup = html.HtmlPopup.Popup(self.page, components, width, height, dfl_options, profile, html_code=html_code)
        validate = self.page.ui.buttons.validate(
            "Validate", html_code=popup.sub_html_code("validate"), options=dfl_options.get("validate"))
        cancel = self.page.ui.buttons.cancel(
            text=dfl_options.get("cancel", {}).get("text", "Cancel"),
            html_code=popup.sub_html_code("validate"), options=dfl_options.get("cancel"))
        row = self.page.ui.row([validate, cancel], position="top", align="center")
        row.options.autoSize = False
        popup.add(row)

        popup.validate = validate
        popup.cancel = cancel
        cancel.click([popup.dom.hide()])
        html.Html.set_component_skin(popup)
        return popup

    def acknowledge(self, components: List[html.Html.Html] = None, width: types.SIZE_TYPE = (100, '%'),
                    height: types.SIZE_TYPE = (None, 'px'), html_code: str = None, options: dict = None,
                    profile: types.PROFILE_TYPE = None) -> html.HtmlPopup.Popup:
        """Display a popup with a ok button to validate the message has been displayed.

        Usage::

          popup = page.popup(page.ui.title('Test'), color="red")
          popup + page.paragraph('Test')

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlPopup.Popup`

        `w3schools <https://www.w3schools.com/tags/tag_div.asp>`_
        `Use case <https://github.com/epykure/epyk-templates/blob/master/locals/components/modals.py>`_

        :param components: The different HTML objects to be added to the component
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = {'margin': 10, 'closure': False, 'top': 100, 'escape': False}
        if options is not None:
            dfl_options.update(options)
        if not isinstance(components, list):
            components = [components]
        popup = html.HtmlPopup.Popup(self.page, components, width, height, dfl_options, profile, html_code=html_code)
        acknowledgement = self.page.ui.button(
            dfl_options.get("button", {}).get("text", "Ok"), options=dfl_options.get("button"),
            align="center", html_code=popup.sub_html_code("button"))
        popup.add(acknowledgement)
        popup.acknowledgement = acknowledgement
        popup.button = popup.acknowledgement
        acknowledgement.click([popup.dom.hide()])
        html.Html.set_component_skin(popup)
        return popup

    def popup(self, components: List[html.Html.Html] = None, title: str = None, width: types.SIZE_TYPE = (80, '%'),
              height: types.SIZE_TYPE = (None, 'px'), html_code: str = None, options: dict = None,
              profile: types.PROFILE_TYPE = None) -> html.HtmlPopup.Popup:
        """Display a generic popup.

        Usage::

          popup = page.ui.modals.popup(page.ui.title('Test'), color="red")
          popup.add(page.ui.texts.paragraph('Test'))

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlPopup.Popup`

        `w3schools <https://www.w3schools.com/tags/tag_div.asp>`_
        `Use case <https://github.com/epykure/epyk-templates/blob/master/locals/components/modals.py>`_

        :param components: The different HTML objects to be added to the component
        :param title:
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        icon_details = self.page.icons.get("close")
        dfl_options = {'margin': 10, 'closure': icon_details["icon"], 'top': 100}
        if options is not None:
            dfl_options.update(options)
        popup = html.HtmlPopup.Popup(self.page, components, width, height, dfl_options, profile, html_code=html_code)
        if title is not None:
            popup.add_title(title)
        html.Html.set_component_skin(popup)
        return popup

    def error(self, components: List[html.Html.Html] = None, width: types.SIZE_TYPE = (100, '%'),
              height: types.SIZE_TYPE = (None, 'px'), html_code: str = None, options: dict = None,
              profile: types.PROFILE_TYPE = None) -> html.HtmlPopup.Popup:
        """Display an error popup.

        Usage::

          popup = page.ui.popup(page.ui.title('Test'), color="red")
          popup + page.ui.paragraph('Test')

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlPopup.Popup`

        `w3schools <https://www.w3schools.com/tags/tag_div.asp>`_
        `Use Case <https://github.com/epykure/epyk-templates/blob/master/locals/components/modals.py>`_

        :param components: The different HTML objects to be added to the component
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        dfl_options = {"button": {"category": "delete"}}
        if options is not None:
            dfl_options.update(options)
        popup = self.icon(components=components, icon="error", width=width, height=height,
                          options=dfl_options, profile=profile, html_code=html_code)
        popup.window.style.css.border = "3px solid %s" % self.page.theme.danger.light
        popup.container[0].style.css.color = self.page.theme.danger.base
        html.Html.set_component_skin(popup)
        return popup

    def info(self, components: List[html.Html.Html] = None, width: types.SIZE_TYPE = (100, '%'),
             height: types.SIZE_TYPE = (None, 'px'), html_code: str = None, options: dict = None,
             profile: types.PROFILE_TYPE = None) -> html.HtmlPopup.Popup:
        """Display an info popup.

        Usage::

          popup = page.ui.popup(page.ui.title('Test'), color="red")
          popup + page.ui.paragraph('Test')

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlPopup.Popup`

        `W3schools <https://www.w3schools.com/tags/tag_div.asp>`_
        `Use case <https://github.com/epykure/epyk-templates/blob/master/locals/components/modals.py>`_

        :param components: The different HTML objects to be added to the component
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        popup = self.icon(
            components=components, icon="question", width=width, height=height, options=options, profile=profile,
            html_code=html_code)
        html.Html.set_component_skin(popup)
        return popup

    def success(self, components: List[html.Html.Html] = None, width: types.SIZE_TYPE = (100, '%'),
                height: types.SIZE_TYPE = (None, 'px'), html_code: str = None, options: dict = None,
                profile: types.PROFILE_TYPE = None) -> html.HtmlPopup.Popup:
        """Display a success popup.

        Usage::

          popup = page.ui.popup(page.ui.title('Test'), color="red")
          popup + page.ui.paragraph('Test')

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlPopup.Popup`

        `W3schools <https://www.w3schools.com/tags/tag_div.asp>`_
        `Use case <https://github.com/epykure/epyk-templates/blob/master/locals/components/modals.py>`_

        :param components: The different HTML objects to be added to the component
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        popup = self.icon(
            components=components, icon="check", width=width, height=height, options=options, profile=profile,
            html_code=html_code)
        popup.window.style.css.border = "3px solid %s" % self.page.theme.success.light
        popup.container[0].style.css.color = self.page.theme.success.base
        html.Html.set_component_skin(popup)
        return popup

    def loading(self, text: str = "", icon: str = "fas fa-spinner fa-pulse", width: types.SIZE_TYPE = (100, '%'),
                height: types.SIZE_TYPE = (None, 'px'), html_code: str = None, options: dict = None,
                profile: types.PROFILE_TYPE = None
                ) -> html.HtmlPopup.Popup:
        """Display a success popup.

        Usage::

          popup = page.ui.popup(page.ui.title('Test'), color="red")
          popup + page.ui.paragraph('Test')

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlPopup.Popup`

        `W3schools <https://www.w3schools.com/tags/tag_div.asp>`_
        `Use case <https://github.com/epykure/epyk-templates/blob/master/locals/components/modals.py>`_

        :param text: Optional. The loading text
        :param icon: Optional.
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        if options is None:
            options = {}
        component = self.page.ui.text(text)

        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = {'margin': 10, 'closure': False, 'top': 100, 'escape': False}
        if options is not None:
            dfl_options.update(options)
        components = [component]
        if icon is not None:
            icon_success = self.page.ui.icon(icon)
            icon_success.style.css.font_size = 50
            icon_success.style.css.margin_bottom = 20
            icon_success.style.css.margin_top = 10
            success_div = self.page.ui.div(icon_success)
            success_div.style.css.text_align = "center"
            components.insert(0, success_div)
        popup = html.HtmlPopup.Popup(self.page, components, width, height, dfl_options, profile, html_code=html_code)
        popup.options.close_on_background = False
        html.Html.set_component_skin(popup)

        popup.window.style.css.border = "None"
        popup.window.style.css.box_shadow = "None"
        popup.window.style.css.background = "None"
        popup.window.style.css.padding = 0
        popup.container.style.css.overflow = "hidden"
        popup.container.style.css.text_align = "center"
        popup.container[0].style.css.color = self.page.theme.success.base
        popup.text = component

        def build_text(data=None, options: dict = None, profile: types.PROFILE_TYPE = False):
            """

            :param data:
            :param options:
            :param profile:
            """
            return component.build(data, options, profile)

        popup.build = build_text
        html.Html.set_component_skin(popup)
        return popup

    def stepper(self, records=None, components: List[html.Html.Html] = None, shape: str = "arrow",
                title: str = None, width: types.SIZE_TYPE = (100, '%'), height: types.SIZE_TYPE = (None, 'px'),
                html_code: str = None, options: dict = None, profile: types.PROFILE_TYPE = None
                ) -> html.HtmlPopup.Popup:
        """

        :param records:
        :param components:
        :param shape:
        :param title:
        :param width:
        :param height:
        :param html_code:
        :param options:
        :param profile:
        """
        if components is not None:
            if not isinstance(components, list):
                components = [components]
        else:
            components = []

        popup = self.popup(components=components, width=width, height=height, options=options, profile=profile,
                           html_code=html_code)

        stepper = getattr(self.page.ui.steppers, shape)(
            records, html_code=popup.sub_html_code("stepper", auto_inc=True))
        stepper.style.css.inline_block()
        stepper.style.css.margin = "auto"
        stepper.style.css.width = "auto"
        stepper.options.line = False
        popup.container.insert(0, self.page.ui.div([stepper], align="center"))
        if title is not None:
            title = self.page.ui.title(title, html_code=popup.sub_html_code("title", auto_inc=True))
            popup.container.insert(0, title)

        popup.title = title
        popup.window.style.css.min_width = "auto"
        popup.window.style.css.width = "auto"
        popup.stepper = stepper
        html.Html.set_component_skin(popup)
        return popup
