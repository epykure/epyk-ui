"""

"""

from epyk.core import html

class Modal(object):
  def __init__(self, context):
    self.context = context

  def __mandatory_js__(self, required_fields):
    """
    Tempoary function to allow action on missing mandatory fields
    TODO: Check if necessary
    :param required_fields: list of html Code that we need to check for when submit button is clicked
    :return: js string
    """

  def inputs(self, records, submit=False, helper=None):
    """
    Example
    rptObj.ui.forms.inputs([
      {"label": "name", "htmlCode": "input"},
      {"label": "name 2", "htmlCode": "input2"},
    ], "http://127.0.0.1:5000", "POST")

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
    modal = html.HtmlContainer.Modal(self.context.rptObj, [], submit, helper)
    modal.col += modal.submit
    self.context.register(modal)
    return modal

  def forms(self, html_objs, action, method, helper=None, htmlCodes=None):
    """
    Simple interface to create an html form within a modal

    Example

    Documentation

    :param html_objs list, :
    :param action: String. frebtbtoojtrjn, fdeul
    :param method:
    :param helper:
    :return:
    """
    htmlCodes = [] if htmlCodes is None else htmlCodes
    if not type(html_objs) == list:
      html_objs = [html_objs]
    form = html.HtmlContainer.Form(self.context.rptObj, html_objs, action, method, helper)
    form += form.submit
    modal = html.HtmlContainer.Modal(self.context.rptObj, [], False, helper)
    modal += form
    modal.form = form
    self.context.register(modal)
    return modal


  def objects(self, html_objs, htmlCodes=None, required_fields=None, submit=True, helper=None):
    """
    Example
    rptObj.ui.forms.inputs([
      {"label": "name", "htmlCode": "input"},
      {"label": "name 2", "htmlCode": "input2"},
    ], "http://127.0.0.1:5000", "POST")

    :param records:
    :param action:
    :param method:
    :param helper:
    :return:
    """
    htmlCodes = [] if htmlCodes is None else htmlCodes
    modal = html.HtmlContainer.Modal(self.context.rptObj, html_objs, submit, helper)
    self.context.register(modal)
    if required_fields:
      self.context.rptObj.js.addOnReady([self.__mandatory_js__(required_fields)])
    return modal

  def disclaimer(self, disc_text, submit=True, validation_text='AGREE', to_html=True, helper=None):
    title = self.context.rptObj.ui.title('DISCLAIMER').css({'text-align': 'center', 'display': 'inline-block', 'maring': 0, 'background-color': 'rgb(0,0,0,0.4)'})
    disc_text = disc_text.replace('\n', '<br/>') if to_html else disc_text
    text = self.context.rptObj.ui.texts.paragraph(disc_text)
    modal = html.HtmlContainer.Modal(self.context.rptObj, [title, text], submit, helper)
    # if submit:
    #   modal.submit.val = validation_text
    self.context.register(modal)
