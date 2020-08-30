#!/usr/bin/python
# -*- coding: utf-8 -*-


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
    :param helper: String. Optional. A tooltip helper
    """
    form = html.HtmlContainer.Form(self.context.rptObj, [], helper)
    return form

  def date(self, htmlCode="Current", profile=None, options=None, helper=None):
    """
    Description:
    ------------
    Create a datepicker object

    Usage::

      rptObj.ui.forms.date("http://127.0.0.1:5000", "POST")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Form`
      - :class:`epyk.core.html.HtmlContainer.Col`
      - :class:`epyk.core.html.HtmlDates.DatePicker`

    Attributes:
    ----------
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: String. Optional. A tooltip helper
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    date = self.context.rptObj.ui.fields.today(label=htmlCode, profile=profile, options=options)
    date.input.set_attrs({"name": htmlCode.upper()})
    col = self.context.rptObj.ui.col([date])
    col.css({"border": '1px solid %s' % self.context.rptObj.theme.greys[4],
                                   "text-align": 'center', "width": 'none', "padding": '5px', "border-radius": '5px'})
    form = html.HtmlContainer.Form(self.context.rptObj, [col], helper)
    form._has_container = True
    return form

  def dates(self, htmlCode, profile=None, options=None, helper=None):
    """
    Description:
    ------------
    Create two datepicker objects for current and previous.

    Usage::

      rptObj.ui.forms.dates("http://127.0.0.1:5000", "POST")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Form`
      - :class:`epyk.core.html.HtmlContainer.Col`
      - :class:`epyk.core.html.HtmlDates.DatePicker`

    Attributes:
    ----------
    :param htmlCode: String. Optional. An identifier for the prefix of the date components (on both Python and Javascript side)
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    :param helper: String. Optional. A tooltip helper
    """
    date1 = self.context.rptObj.ui.fields.today(label="%s_current" % htmlCode, profile=profile, options=options)
    date1.input.set_attrs({"name": date1.htmlCode.upper()})
    date2 = self.context.rptObj.ui.fields.today(label="%s_previous" % htmlCode, profile=profile, options=options)
    date2.input.set_attrs({"name": date2.htmlCode.upper()})
    col = self.context.rptObj.ui.col([date1, date2])
    col.css({"border": '1px solid %s' % self.context.rptObj.theme.greys[4],
             "text-align": 'center', "width": 'none', "padding": '5px', "border-radius": '5px'})
    form = html.HtmlContainer.Form(self.context.rptObj, [col], helper)
    form._has_container = True
    return form

  def input(self, htmlCode, value="", label=None, placeholder="", icon=None, profile=None, options=None, helper=None):
    """
    Description:
    ------------

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Form`
      - :class:`epyk.core.html.HtmlInput.FieldInput`

    Attributes:
    ----------
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param value: String. Optional. The value to be displayed to this component. Default empty
    :param label: String. Optional. The text of label to be added to the component
    :param placeholder: String. Optional. The text to be displayed when the input is empty
    :param icon: String. Optional. The component icon content from font-awesome references
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    :param helper: String. Optional. A tooltip helper
    """
    inp = self.context.rptObj.ui.fields.input(value=value, label=label, placeholder=placeholder, icon=icon, profile=profile, options=options)
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
    :param helper: String. Optional. A tooltip helper
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
    :param value: Optional. The value to be displayed to this component. Default empty
    :param placeholder: String. Optional. The text to be displayed when the input is empty
    :param button:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage
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


