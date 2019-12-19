"""

"""

from epyk.core import html


class Forms(object):
  def __init__(self, context):
    self.context = context

  def date(self, action, method, htmlCode="Current", helper=None):
    col = self.context.rptObj.ui.col([self.context.rptObj.ui.fields.today(label=htmlCode).set_attrs({"name": htmlCode.upper()})])
    col.css({"border": '1px solid %s' % self.context.rptObj.getColor("greys", 4),
                                   "text-align": 'center', "width": 'none', "padding": '5px', "border-radius": '5px'})
    form = html.HtmlContainer.Form(self.context.rptObj, [col], action, method, helper)
    col += form.submit
    self.context.register(form)
    return form

  def dates(self, action, method, htmlCode1="current", htmlCode2="Previous",  helper=None):
    col = self.context.rptObj.ui.col([
      self.context.rptObj.ui.fields.today(label=htmlCode1).set_attrs({"name": htmlCode1.upper()}),
      self.context.rptObj.ui.fields.today(label=htmlCode2).set_attrs({"name": htmlCode2.upper()}),
    ])
    col.css({"border": '1px solid %s' % self.context.rptObj.getColor("greys", 4),
                                   "text-align": 'center', "width": 'none', "padding": '5px', "border-radius": '5px'})
    form = html.HtmlContainer.Form(self.context.rptObj, [col], action, method, helper)
    col += form.submit
    self.context.register(form)
    return form

  def input(self, htmlCode, action, method, helper=None):
    """

    :param action:
    :param method:
    :param helper:
    """
    inp = self.context.rptObj.ui.fields.input()
    inp.input.set_attrs({"name": htmlCode})
    form = html.HtmlContainer.Form(self.context.rptObj, [inp], action, method, helper)
    self.context.register(form)
    return form

  def inputs(self, records, action, method, helper=None):
    html_objs = []
    for rec in records:
      inp = self.context.rptObj.ui.fields.input(label=rec["label"])
      inp.input.set_attrs({"name": rec["htmlCode"]})
      html_objs.append(inp)
    col = self.context.rptObj.ui.col(html_objs).css({"border": '1px solid %s' % self.context.rptObj.getColor("greys", 4),
                                   "text-align": 'center', "width": 'none', "padding": '5px', "border-radius": '5px'})
    form = html.HtmlContainer.Form(self.context.rptObj, [col], action, method, helper)
    col += form.submit
    self.context.register(form)
    return form
