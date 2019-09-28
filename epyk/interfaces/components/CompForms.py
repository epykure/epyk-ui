"""

"""

from epyk.core import html


class Forms(object):
  def __init__(self, context):
    self.context = context

  def date(self, action, method, yyyy_mm_dd=None, helper=None):
    form = html.HtmlForms.Form(self.context.rptObj, action, method, helper)
    self.context.register(form)
    return form

  def dates(self, yyyy_mm_dd=None, yyyy_mm_dd_Prev=None):
    pass

  def input(self, action, method="GET", value="", label=None, placeholder="", title=None, helper=None):
    """

    :param action:
    :param method:
    :param value:
    :param label:
    :param placeholder:
    :param title:
    :param helper:

    :rtype: html.HtmlForms.Form
    :return:
    """
    form = html.HtmlForms.Form(self.context.rptObj, action, method, helper)
    #form.input(value, placeholder, label)
    #form.add_title(title)
    self.context.register(form)
    return form
