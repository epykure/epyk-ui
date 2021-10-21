#!/usr/bin/python
# -*- coding: utf-8 -*-


from epyk.core import html
from epyk.interfaces import Arguments
from epyk.core.css import Defaults as Defaults_css


class Modals:

  def __init__(self, ui):
    self.page = ui.page

  @html.Html.css_skin()
  def forms(self, components, action, method, header=None, footer=None, helper=None):
    """
    Description:
    ------------
    Simple interface to create an html form within a modal

    Usage::

      d = page.ui.fields.today('test')
      i = page.ui.fields.input(placeholder='test2', label='test1')
      i2 = page.ui.fields.input('test3', label='test2')
      form_modal = page.ui.modals.forms([d, i, i2], "http://127.0.0.1:5000", "POST")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Modal`
      - :class:`epyk.core.html.HtmlContainer.Form`

    Related Pages:

      https://www.w3schools.com/w3css/w3css_modal.asp

    Attributes:
    ----------
    :param html_objs components:
    :param action:
    :param method:
    :param header:
    :param footer:
    :param helper:
    """
    if not type(components) == list:
      components = [components]
    form = html.HtmlContainer.Form(self.page, components, helper)
    form.submit(method, action)
    modal = html.HtmlContainer.Modal(self.page, [], header, footer, False, helper)
    modal += form
    modal.form = form
    return modal

  @html.Html.css_skin()
  def disclaimer(self, disc_list, header=None, footer=None, submit=True, validation_text='AGREE', action=None,
                 add_buttons=None, to_html=True, helper=None):
    """
    Description:
    ------------
    Disclaimer that will appear as a modal.

    Usage::

      privacy_title = page.ui.texts.title('A privacy reminder', 2)
      p1 = page.ui.texts.paragraph('''Scroll down and click “%s” when you’re ready to continue, or explore other options on this page.''' % rptObj.ui.tags.strong('''I agree''', options={'managed': False}))
      disc = page.ui.modals.disclaimer([privacy_title, p1])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Modal`
      - :class:`epyk.core.html.HtmlContainer.Row`
      - :class:`epyk.core.html.HtmlButton.Button`

    Attributes:
    ----------
    :param disc_list:
    :param header:
    :param footer:
    :param submit:
    :param validation_text:
    :param action:
    :param add_buttons:
    :param to_html:
    :param helper:
    """
    for obj in disc_list:
      obj.css({'margin': '40px', 'width': 'auto', 'text-align': 'justify'})

    modal = html.HtmlContainer.Modal(self.page, disc_list, header, footer, False, helper)
    modal.col.css({'width': '450px', 'height': '700px'})
    if add_buttons or submit:
      submitRow = self.page.ui.row([]) if not add_buttons else self.page.ui.row(add_buttons)
      if submit:
        submitBtn = self.page.ui.buttons.important(validation_text)
        if action:
          submitBtn.click(action)
        else:
          submitBtn.click(modal.close())
        submitRow + submitBtn
      modal.col + submitRow
    return modal

  @html.Html.css_skin()
  def dialog(self, text, width=(100, '%'), height=(20, 'px'), html_code=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------
    Simple Jquery UI modal with a text.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlEvent.Dialog`

    Related Pages:

      https://jqueryui.com/dialog/

    Usage::


    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: String. Optional. A tooltip helper.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_pr = html.HtmlEvent.Dialog(self.page, text, width, height, helper, options or {}, html_code, profile)
    return html_pr

  @html.Html.css_skin()
  def icon(self, components=None, icon=None, width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    """
    Description:
    ------------
    Display a generic popup with an icon.

    Usage::

      popup = page.popup(page.ui.title('Test'), color="red")
      popup + page.paragraph('Test')

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlPopup.Popup`

    Related Pages:

      https://www.w3schools.com/tags/tag_div.asp

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/modals.py

    Attributes:
    ----------
    :param components: List. The different HTML objects to be added to the component.
    :param icon: String. Optional.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage.
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
    acknowledgement = self.page.ui.button("Ok", align="center", options=dfl_options.get("button", {}))
    acknowledgement.style.css.margin_top = 10
    components.append(acknowledgement)

    popup = html.HtmlPopup.Popup(self.page, components, width, height, dfl_options, profile)
    popup.acknowledgement = acknowledgement

    acknowledgement.click([popup.dom.hide()])
    return popup

  @html.Html.css_skin()
  def validation(self, components=None, width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    """
    Description:
    ------------

    Usage::

      popup = page.popup(page.ui.title('Test'), color="red")
      popup + page.paragraph('Test')

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlPopup.Popup`

    Related Pages:

      https://www.w3schools.com/tags/tag_div.asp

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/modals.py

    Attributes:
    ----------
    :param components: List. The different HTML objects to be added to the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    icon_details = Defaults_css.get_icon("close")
    dfl_options = {'margin': 10, 'closure': icon_details["icon"], 'top': 100}
    if options is not None:
      dfl_options.update(options)
    if not isinstance(components, list):
      components = [components]
    validate = self.page.ui.buttons.validate("Validate")
    cancel = self.page.ui.buttons.cancel()
    row = self.page.ui.row([validate, cancel], position="top", align="center")
    row.options.autoSize = False
    components.append(row)

    popup = html.HtmlPopup.Popup(self.page, components, width, height, dfl_options, profile)
    popup.validate = validate
    popup.cancel = cancel
    cancel.click([popup.dom.hide()])
    return popup

  @html.Html.css_skin()
  def acknowledge(self, components=None, width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    """
    Description:
    ------------
    Display a popup with a ok button to validate the message has been displayed.

    Usage::

      popup = page.popup(page.ui.title('Test'), color="red")
      popup + page.paragraph('Test')

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlPopup.Popup`

    Related Pages:

      https://www.w3schools.com/tags/tag_div.asp

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/modals.py

    Attributes:
    ----------
    :param components: List. The different HTML objects to be added to the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {'margin': 10, 'closure': False, 'top': 100, 'escape': False}
    if options is not None:
      dfl_options.update(options)
    if not isinstance(components, list):
      components = [components]
    acknowledgement = self.page.ui.button("Ok", align="center")
    components.append(acknowledgement)

    popup = html.HtmlPopup.Popup(self.page, components, width, height, dfl_options, profile)
    popup.acknowledgement = acknowledgement
    acknowledgement.click([popup.dom.hide()])
    return popup

  @html.Html.css_skin()
  def popup(self, components=None, width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    """
    Description:
    ------------
    Display a generic popup.

    Usage::

      popup = page.ui.modals.popup(page.ui.title('Test'), color="red")
      popup.add(page.ui.texts.paragraph('Test'))

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlPopup.Popup`

    Related Pages:

      https://www.w3schools.com/tags/tag_div.asp

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/modals.py

    Attributes:
    ----------
    :param components: List. The different HTML objects to be added to the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    icon_details = Defaults_css.get_icon("close")
    dfl_options = {'margin': 10, 'closure': icon_details["icon"], 'top': 100}
    if options is not None:
      dfl_options.update(options)
    return html.HtmlPopup.Popup(self.page, components, width, height, dfl_options, profile)

  @html.Html.css_skin()
  def error(self, components=None, width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    """
    Description:
    ------------
    Display an error popup.

    Usage::

      popup = page.popup(page.ui.title('Test'), color="red")
      popup + page.paragraph('Test')

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlPopup.Popup`

    Related Pages:

      https://www.w3schools.com/tags/tag_div.asp

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/modals.py

    Attributes:
    ----------
    :param components: List. The different HTML objects to be added to the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage.
    """
    dfl_options = {"button": {"category": "delete"}}
    if options is not None:
      dfl_options.update(options)
    popup = self.icon(components=components, icon="error", width=width, height=height,
                      options=dfl_options, profile=profile)
    popup.window.style.css.border = "3px solid %s" % self.page.theme.danger[0]
    popup.container[0].style.css.color = self.page.theme.danger[1]
    return popup

  @html.Html.css_skin()
  def info(self, components=None, width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    """
    Description:
    ------------
    Display an info popup.

    Usage::

      popup = page.popup(page.ui.title('Test'), color="red")
      popup + page.paragraph('Test')

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlPopup.Popup`

    Related Pages:

      https://www.w3schools.com/tags/tag_div.asp

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/modals.py

    Attributes:
    ----------
    :param components: List. The different HTML objects to be added to the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage.
    """
    popup = self.icon(components=components, icon="question", width=width, height=height, options=options,
                      profile=profile)
    return popup

  @html.Html.css_skin()
  def success(self, components=None, width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    """
    Description:
    ------------
    Display a success popup.

    Usage::

      popup = page.popup(page.ui.title('Test'), color="red")
      popup + page.paragraph('Test')

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlPopup.Popup`

    Related Pages:

      https://www.w3schools.com/tags/tag_div.asp

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/modals.py

    Attributes:
    ----------
    :param components: List. The different HTML objects to be added to the component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage.
    """
    popup = self.icon(
      components=components, icon="check", width=width, height=height, options=options, profile=profile)
    popup.window.style.css.border = "3px solid %s" % self.page.theme.success[0]
    popup.container[0].style.css.color = self.page.theme.success[1]
    return popup

  @html.Html.css_skin()
  def loading(self, text="", width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    """
    Description:
    ------------
    Display a success popup.

    Usage::

      popup = page.popup(page.ui.title('Test'), color="red")
      popup + page.paragraph('Test')

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlPopup.Popup`

    Related Pages:

      https://www.w3schools.com/tags/tag_div.asp

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/modals.py

    Attributes:
    ----------
    :param text: String. Optional. The loading text.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage.
    """
    component = self.page.ui.text(text)
    popup = self.icon(components=[component], icon="fas fa-spinner fa-pulse", width=width, height=height,
                      options=options, profile=profile)
    popup.window.style.css.border = "3px solid %s" % self.page.theme.success[0]
    popup.container[0].style.css.color = self.page.theme.success[1]
    popup.text = component

    def build_text(data=None, options=None, profile=False):
      return component.build(data, options, profile)

    popup.build = build_text
    return popup

  @html.Html.css_skin()
  def stepper(self, records=None, components=None, shape="arrow", title=None, width=(100, '%'), height=(None, 'px'),
              options=None, profile=None):
    """

    :param records:
    :param components:
    :param shape:
    :param title:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    if components is not None:
      if not isinstance(components, list):
        components = [components]
    else:
      components = []
    stepper = getattr(self.page.ui.steppers, shape)(records)
    stepper.style.css.inline_block()
    stepper.style.css.margin = "auto"
    stepper.style.css.width = "auto"
    stepper.options.line = False
    components.insert(0, self.page.ui.div([stepper], align="center"))
    if title is not None:
      title = self.page.ui.title(title)
      components.insert(0, title)
    popup = self.popup(components=components, width=width, height=height, options=options, profile=profile)
    popup.title = title
    popup.window.style.css.min_width = "auto"
    popup.window.style.css.width = "auto"
    popup.stepper = stepper
    return popup
