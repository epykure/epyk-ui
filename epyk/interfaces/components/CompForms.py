"""

"""

from epyk.core import html


class Forms(object):
  def __init__(self, context):
    self.context = context

  def date(self, report, action, method, yyyy_mm_dd=None):

    form = html.HtmlForms.Form(report, action, method, helper)
    self.context.register(form)
    return form

  def dates(self, yyyy_mm_dd=None, yyyy_mm_dd_Prev=None):
    pass

  def input(self, report, action, method, value=None, title=None, helper=None):
    form = html.HtmlForms.Form(report, action, method, helper)
    form.add_title(title)
    form.add_input(value)
    self.context.register(form)
    return form
