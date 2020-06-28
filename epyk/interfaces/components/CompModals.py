
from epyk.core import html


class Modals(object):
  def __init__(self, context):
    self.context = context

  def forms(self, html_objs, action, method, header=None, footer=None, helper=None):
    """
    Simple interface to create an html form within a modal

    Usage::

      d = rptObj.ui.fields.today('test')
      i = rptObj.ui.fields.input(placeholder='test2', label='test1')
      i2 = rptObj.ui.fields.input('test3', label='test2')
      form_modal = rptObj.ui.modals.forms([d, i, i2], "http://127.0.0.1:5000", "POST")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Modal`
      - :class:`epyk.core.html.HtmlContainer.Form`

    Related Pages:

      https://www.w3schools.com/w3css/w3css_modal.asp

    Attributes:
    ----------
    :param html_objs list:
    :param method:
    :param helper:
    :return:
    """
    if not type(html_objs) == list:
      html_objs = [html_objs]
    form = html.HtmlContainer.Form(self.context.rptObj, html_objs, helper)
    form.submit(method, action)
    modal = html.HtmlContainer.Modal(self.context.rptObj, [], header, footer, False, helper)
    modal += form
    modal.form = form
    return modal

  def disclaimer(self, disc_list, header=None, footer=None, submit=True, validation_text='AGREE', action=None, add_buttons=None, to_html=True, helper=None):
    """
    Disclaimer that will appear as a modal

    Usage::

      privacy_title = rptObj.ui.texts.title('A privacy reminder', 2)
      p1 = rptObj.ui.texts.paragraph('''Scroll down and click “%s” when you’re ready to continue, or explore other options on this page.''' % rptObj.ui.tags.strong('''I agree''', options={'managed': False}))
      disc = rptObj.ui.modals.disclaimer([privacy_title, p1])

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
    :param to_html:
    :param helper:
    :return:
    """
    for obj in disc_list:
      obj.css({'margin': '40px', 'width': 'auto', 'text-align': 'justify'})

    modal = html.HtmlContainer.Modal(self.context.rptObj, disc_list, header, footer, False, helper)
    modal.col.css({'width': '450px', 'height':'700px'})
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
    Simple Jquery UI modal with a text

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlEvent.Dialog`

    Related Pages:

      https://jqueryui.com/dialog/

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
    html_pr = html.HtmlEvent.Dialog(self.context.rptObj, text, width, height,  attrs or {}, helper,
                                         options or {}, htmlCode, profile)
    return html_pr
