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
    return form

  def date(self, htmlCode="Current", helper=None):
    """
    Description:
    ------------

    Usage::

      rptObj.ui.forms.date("http://127.0.0.1:5000", "POST")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Form`
      - :class:`epyk.core.html.HtmlContainer.Col`
      - :class:`epyk.core.html.HtmlDates.DatePicker`

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
    return form

  def dates(self, htmlCode1="current", htmlCode2="Previous",  helper=None):
    """
    Description:
    ------------

    Usage::

      rptObj.ui.forms.dates("http://127.0.0.1:5000", "POST")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Form`
      - :class:`epyk.core.html.HtmlContainer.Col`
      - :class:`epyk.core.html.HtmlDates.DatePicker`

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
    return form

  def input(self, htmlCode, helper=None):
    """
    Description:
    ------------

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Form`
      - :class:`epyk.core.html.HtmlInput.FieldInput`

    Attributes:
    ----------
    :param helper:
    """
    inp = self.context.rptObj.ui.fields.input()
    inp.input.set_attrs({"name": htmlCode})
    form = html.HtmlContainer.Form(self.context.rptObj, [inp], helper)
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

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Form`
      - :class:`epyk.core.html.HtmlContainer.Col`
      - :class:`epyk.core.html.HtmlInput.FieldInput`

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
    return form

  def subscribe(self, value="", placeholder="Enter email address", button="Subscribe", width=(100, '%'),
                height=(None, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param value:
    :param placeholder:
    :param button:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    input = self.context.rptObj.ui.input(text=value, placeholder=placeholder)
    input.attr["class"].add("form-control")
    input.style.css.display = "inline-block"
    input.style.css.width = None

    if not hasattr(button, 'options'):
      button = self.context.rptObj.ui.button(button, width=("auto", ""))
      button.style.css.margin = 0
    button_container = self.context.rptObj.ui.div([button])
    button_container.attr["class"].add("input-group-append")
    button_container.style.css.width = None
    container = self.context.rptObj.ui.div([input, button_container], width=width, height=height, options=options, profile=profile)
    container.attr["class"].add("input-group mb-3")
    container.button = button
    container.input = input
    input.enter(button.dom.events.trigger("click"))
    return container


