
from epyk.core import html


class Modal(object):
  def __init__(self, context):
    self.context = context


  def inputs(self, records, header=None, footer=None, submit=False, helper=None):
    """
    Usage::

      rptObj.ui.forms.inputs([
      {"label": "name", "htmlCode": "input"},
      {"label": "name 2", "htmlCode": "input2"},
    ], "http://127.0.0.1:5000", "POST")

    Attributes:
    ----------
    :param records:
    :param action:
    :param method:
    :param helper:
    :return:
    """
    html_objs = []
    modal = html.HtmlContainer.Modal(self.context.rptObj, [], helper)
    for rec in records:
      inp = self.context.rptObj.ui.fields.input(label=rec["label"])
      inp.label.css({'float': ''})
      inp.input.set_attrs({"name": rec["htmlCode"]})
      modal.col += inp
    modal = html.HtmlContainer.Modal(self.context.rptObj, [], header, footer, submit, helper)
    modal.col += modal.submit
    self.context.register(modal)
    return modal

  def forms(self, html_objs, action, method, header=None, footer=None, helper=None):
    """
    Simple interface to create an html form within a modal

    Usage::

      Documentation

    Attributes:
    ----------
    :param html_objs list, :
    :param action: String. frebtbtoojtrjn, fdeul
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
    self.context.register(modal)
    return modal

  def disclaimer(self, disc_list, header=None, footer=None, submit=True, validation_text='AGREE', action=None, add_buttons=None, to_html=True, helper=None):
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
    self.context.register(modal)
    return modal

  def dialog(self, text, width=(100, '%'), height=(20, 'px'), htmlCode=None, attrs=None,
                  helper=None, options=None, profile=None):
    """
    Description:
    ------------
    Simple Jquery UI modal with a text

    Usage::

      Related Pages:
    --------------
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
    self.context.register(html_pr)
    return html_pr
