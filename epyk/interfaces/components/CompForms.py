from epyk.core import html


class Forms(object):
  def __init__(self, context):
    self.context = context

  def new(self, helper=None):
    """
    Description:
    ------------
    Creates an new empty form

    Usage::

      f = rptObj.ui.form()

    Attributes:
    ----------
    :param action:
    :param method:
    :param helper:
    """
    form = html.HtmlContainer.Form(self.context.rptObj, [], helper)
    self.context.register(form)
    return form

  def date(self, htmlCode="Current", helper=None):
    """
    Description:
    ------------

    Usage::

      rptObj.ui.forms.date("http://127.0.0.1:5000", "POST")

    Attributes:
    ----------
    :param action:
    :param method:
    :param htmlCode:
    :param helper:
    """
    date = self.context.rptObj.ui.fields.today(label=htmlCode)
    date.input.set_attrs({"name": htmlCode.upper()})
    col = self.context.rptObj.ui.col([date])
    col.css({"border": '1px solid %s' % self.context.rptObj.theme.greys[4],
                                   "text-align": 'center', "width": 'none', "padding": '5px', "border-radius": '5px'})
    form = html.HtmlContainer.Form(self.context.rptObj, [col], helper)
    form._has_container = True
    self.context.register(form)
    return form

  def dates(self, htmlCode1="current", htmlCode2="Previous",  helper=None):
    """
    Description:
    ------------

    Usage::

      rptObj.ui.forms.dates("http://127.0.0.1:5000", "POST")

    Attributes:
    ----------
    :param action:
    :param method:
    :param htmlCode1:
    :param htmlCode2:
    :param helper:
    """
    date1 = self.context.rptObj.ui.fields.today(label=htmlCode1)
    date1.input.set_attrs({"name": htmlCode1.upper()})
    date2 = self.context.rptObj.ui.fields.today(label=htmlCode2)
    date2.input.set_attrs({"name": htmlCode2.upper()})

    col = self.context.rptObj.ui.col([date1, date2])
    col.css({"border": '1px solid %s' % self.context.rptObj.theme.greys[4],
             "text-align": 'center', "width": 'none', "padding": '5px', "border-radius": '5px'})
    form = html.HtmlContainer.Form(self.context.rptObj, [col], helper)
    form._has_container = True
    self.context.register(form)
    return form

  def input(self, htmlCode, helper=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param helper:
    """
    inp = self.context.rptObj.ui.fields.input()
    inp.input.set_attrs({"name": htmlCode})
    form = html.HtmlContainer.Form(self.context.rptObj, [inp], helper)
    self.context.register(form)
    return form

  def inputs(self, records, helper=None):
    """
    Description:
    ------------

    Usage::

      rptObj.ui.forms.inputs([
      {"label": "name", "htmlCode": "input"},
      {"label": "name 2", "htmlCode": "input2"},
    ])

    Attributes:
    ----------
    :param records:
    :param helper:
    """
    html_objs = []
    for rec in records:
      inp = self.context.rptObj.ui.fields.input(label=rec["label"])
      inp.input.set_attrs({"name": rec["htmlCode"]})
      html_objs.append(inp)
    col = self.context.rptObj.ui.col(html_objs).css({"border": '1px solid %s' % self.context.rptObj.theme.greys[4],
                                   "text-align": 'center', "width": 'none', "padding": '5px', "border-radius": '5px'})
    form = html.HtmlContainer.Form(self.context.rptObj, [col], helper)
    form._has_container = True
    self.context.register(form)
    return form
