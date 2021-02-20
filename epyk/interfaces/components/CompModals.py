#!/usr/bin/python
# -*- coding: utf-8 -*-


from epyk.core import html
from epyk.interfaces import Arguments


class Modals(object):
  def __init__(self, context):
    self.context = context

  def forms(self, components, action, method, header=None, footer=None, helper=None):
    """
    Description:
    ------------
    Simple interface to create an html form within a modal

    Usage:
    -----

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
    :param method:
    :param helper:
    """
    if not type(components) == list:
      components = [components]
    form = html.HtmlContainer.Form(self.context.rptObj, components, helper)
    form.submit(method, action)
    modal = html.HtmlContainer.Modal(self.context.rptObj, [], header, footer, False, helper)
    modal += form
    modal.form = form
    return modal

  def disclaimer(self, disc_list, header=None, footer=None, submit=True, validation_text='AGREE', action=None, add_buttons=None, to_html=True, helper=None):
    """
    Description:
    ------------
    Disclaimer that will appear as a modal.

    Usage:
    -----

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

    modal = html.HtmlContainer.Modal(self.context.rptObj, disc_list, header, footer, False, helper)
    modal.col.css({'width': '450px', 'height': '700px'})
    if add_buttons or submit:
      submitRow = self.context.rptObj.ui.row([]) if not add_buttons else self.context.rptObj.ui.row(add_buttons)
      if submit:
        submitBtn = self.context.rptObj.ui.buttons.important(validation_text)
        if action:
          submitBtn.click(action)
        else:
          submitBtn.click(modal.close())
        submitRow + submitBtn
      modal.col + submitRow
    return modal

  def dialog(self, text, width=(100, '%'), height=(20, 'px'), htmlCode=None, attrs=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------
    Simple Jquery UI modal with a text.

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlEvent.Dialog`

    Related Pages:

      https://jqueryui.com/dialog/

    Usage:
    -----


    Attributes:
    ----------
    :param text:
    :param width:
    :param height:
    :param htmlCode:
    :param attrs:
    :param helper:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_pr = html.HtmlEvent.Dialog(self.context.rptObj, text, width, height,  attrs or {}, helper,
                                         options or {}, htmlCode, profile)
    return html_pr

  def icon(self, components=None, icon=None, width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    """
    Description:
    ------------
    Display a generic popup with an icon.

    Usage:
    -----

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
      icon_success = self.context.rptObj.ui.icon(icon)
      icon_success.style.css.font_size = 50
      icon_success.style.css.margin_bottom = 20
      icon_success.style.css.margin_top = 10
      success_div = self.context.rptObj.ui.div(icon_success)
      success_div.style.css.text_align = "center"
      components.insert(0, success_div)
    acknowledgement = self.context.rptObj.ui.button("Ok", align="center", options=dfl_options.get("button", {}))
    acknowledgement.style.css.margin_top = 10
    components.append(acknowledgement)

    popup = html.HtmlPopup.Popup(self.context.rptObj, components, width, height, dfl_options, profile)
    popup.acknowledgement = acknowledgement

    acknowledgement.click([popup.dom.hide()])
    return popup

  def validation(self, components=None, width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    """
    Description:
    ------------

    Usage:
    -----

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
    dfl_options = {'margin': 10, 'closure': "fas fa-times-circle", 'top': 100}
    if options is not None:
      dfl_options.update(options)
    if not isinstance(components, list):
      components = [components]
    validate = self.context.rptObj.ui.buttons.validate("Validate")
    cancel = self.context.rptObj.ui.buttons.cancel()
    row = self.context.rptObj.ui.row([validate, cancel], position="top", align="center")
    components.append(row)

    popup = html.HtmlPopup.Popup(self.context.rptObj, components, width, height, dfl_options, profile)
    popup.validate = validate
    popup.cancel = cancel
    cancel.click([popup.dom.hide()])
    return popup

  def acknowledge(self, components=None, width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    """
    Description:
    ------------
    Display a popup with a ok button to validate the message has been displayed.

    Usage:
    -----

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
    acknowledgement = self.context.rptObj.ui.button("Ok", align="center")
    components.append(acknowledgement)

    popup = html.HtmlPopup.Popup(self.context.rptObj, components, width, height, dfl_options, profile)
    popup.acknowledgement = acknowledgement
    acknowledgement.click([popup.dom.hide()])
    return popup

  def popup(self, components=None, width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    """
    Description:
    ------------
    Display a generic popup.

    Usage:
    -----

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
    dfl_options = {'margin': 10, 'closure': "fas fa-times-circle", 'top': 100}
    if options is not None:
      dfl_options.update(options)
    return html.HtmlPopup.Popup(self.context.rptObj, components, width, height, dfl_options, profile)

  def error(self, components=None, width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    """
    Description:
    ------------
    Display an error popup.

    Usage:
    -----

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
    popup = self.icon(components=components, icon="fas fa-exclamation-triangle", width=width, height=height, options=dfl_options,
                      profile=profile)
    popup.window.style.css.border = "3px solid %s" % self.context.rptObj.theme.danger[0]
    popup.container[0].style.css.color = self.context.rptObj.theme.danger[1]
    return popup

  def info(self, components=None, width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    """
    Description:
    ------------
    Display an info popup.

    Usage:
    -----

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
    popup = self.icon(components=components, icon="fas fa-question-circle", width=width, height=height, options=options,
                      profile=profile)
    return popup

  def success(self, components=None, width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    """
    Description:
    ------------
    Display a success popup.

    Usage:
    -----

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
    popup = self.icon(components=components, icon="fas fa-check", width=width, height=height, options=options, profile=profile)
    popup.window.style.css.border = "3px solid %s" % self.context.rptObj.theme.success[0]
    popup.container[0].style.css.color = self.context.rptObj.theme.success[1]
    return popup

  def loading(self, text="", width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    """
    Description:
    ------------
    Display a success popup.

    Usage:
    -----

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
    component = self.context.rptObj.ui.text(text)
    popup = self.icon(components=[component], icon="fas fa-spinner fa-pulse", width=width, height=height, options=options, profile=profile)
    popup.window.style.css.border = "3px solid %s" % self.context.rptObj.theme.success[0]
    popup.container[0].style.css.color = self.context.rptObj.theme.success[1]
    popup.text = component

    def build_text(data=None, options=None, profile=False):
      return component.build(data, options, profile)

    popup.build = build_text
    return popup

