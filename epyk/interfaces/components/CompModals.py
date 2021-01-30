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
