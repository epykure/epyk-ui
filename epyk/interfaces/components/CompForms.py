"""

"""

from epyk.core import html


class Forms(object):
  def __init__(self, context):
    self.context = context

  def date(self, objs, action, method, yyyy_mm_dd=None, helper=None):
    form = html.HtmlContainer.Form(self.context.rptObj, objs, action, method, helper)
    self.context.register(form)
    return form

  def input(self, action, method="GET", value="", label=None, title=None, helper=None):
    """

    :param action:
    :param method:
    :param value:
    :param label:
    :param title:
    :param helper:
    """
    form = html.HtmlContainer.Form(self.context.rptObj, action, method, helper)
    form.add_title(title)
    form.add_input(value, 'input', label)
    self.context.register(form)
    return form
