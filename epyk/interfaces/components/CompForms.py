"""

"""

from epyk.core import html


class Forms(object):
  def __init__(self, context):
    self.context = context

  def date(self, action, method, helper=None):
    today = self.context.rptObj.ui.fields.today().set_attrs({"name": 'date'})
    form = html.HtmlContainer.Form(self.context.rptObj, [today], action, method, helper)
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
