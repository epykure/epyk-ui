#!/usr/bin/python
# -*- coding: utf-8 -*-


from typing import Union, Optional, List
from epyk.core import html
from epyk.core.py import types


class Forms:
  
  def __init__(self, ui):
    self.page = ui.page

  def new(self,
          components: List[html.Html.Html] = None,
          helper: Optional[str] = None) -> html.HtmlContainer.Form:
    """
    Description:
    ------------
    Creates an new empty form.

    :tags:
    :categories:

    Usage::

      f = page.ui.form()

    Attributes:
    ----------
    :param helper: Optional. A tooltip helper.
    :param components: Optional. The different HTML objects to be added to the component.
    """
    form = html.HtmlContainer.Form(self.page, components or [], helper)
    html.Html.set_component_skin(form)
    return form

  def date(self, html_code: str = "Current", profile: types.PROFILE_TYPE = None,
           options: dict = None, helper: Optional[str] = None):
    """
    Description:
    ------------
    Create a DatePicker object.

    :tags:
    :categories:

    Usage::

      page.ui.forms.date("http://127.0.0.1:5000", "POST")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Form`
      - :class:`epyk.core.html.HtmlContainer.Col`
      - :class:`epyk.core.html.HtmlDates.DatePicker`

    Attributes:
    ----------
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: Optional. A tooltip helper.
    :param profile: Optional. A flag to set the component performance storage.
    :param options: Optional. Specific Python options available for this component.
    """
    date = self.page.ui.fields.today(label=html_code, profile=profile, options=options)
    date.input.set_attrs({"name": html_code.upper()})
    col = self.page.ui.col([date])
    col.css({
      "border": '1px solid %s' % self.page.theme.greys[4],
      "text-align": 'center', "width": 'none', "padding": '5px', "border-radius": '5px'})
    form = html.HtmlContainer.Form(self.page, [col], helper)
    form._has_container = True
    html.Html.set_component_skin(form)
    return form

  def dates(self,
            html_code: str,
            profile: types.PROFILE_TYPE = None,
            options: dict = None,
            helper: str = None) -> html.HtmlContainer.Form:
    """
    Description:
    ------------
    Create two datepicker objects for current and previous.

    :tags:
    :categories:

    Usage::

      page.ui.forms.dates("http://127.0.0.1:5000", "POST")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Form`
      - :class:`epyk.core.html.HtmlContainer.Col`
      - :class:`epyk.core.html.HtmlDates.DatePicker`

    Attributes:
    ----------
    :param html_code: An identifier for the prefix of the date components (on both Python and Javascript side).
    :param profile: Optional. A flag to set the component performance storage.
    :param options: Optional. Specific Python options available for this component.
    :param helper: Optional. A tooltip helper.
    """
    date1 = self.page.ui.fields.today(label="%s_current" % html_code, profile=profile, options=options)
    date1.input.set_attrs({"name": date1.htmlCode.upper()})
    date2 = self.page.ui.fields.today(label="%s_previous" % html_code, profile=profile, options=options)
    date2.input.set_attrs({"name": date2.htmlCode.upper()})
    col = self.page.ui.col([date1, date2])
    col.css({"border": '1px solid %s' % self.page.theme.greys[4],
             "text-align": 'center', "width": 'none', "padding": '5px', "border-radius": '5px'})
    form = html.HtmlContainer.Form(self.page, [col], helper)
    form._has_container = True
    html.Html.set_component_skin(form)
    return form

  def input(self, html_code: str, value: str = "", label: str = None, placeholder: str = "", icon: str = None,
            profile: types.PROFILE_TYPE = None, options: dict = None,
            helper: str = None) -> html.HtmlContainer.Form:
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Form`
      - :class:`epyk.core.html.HtmlInput.FieldInput`

    Attributes:
    ----------
    :param html_code: An identifier for this component (on both Python and Javascript side).
    :param value: Optional. The value to be displayed to this component. Default empty.
    :param label: Optional. The text of label to be added to the component.
    :param placeholder: Optional. The text to be displayed when the input is empty.
    :param icon: Optional. The component icon content from font-awesome references.
    :param profile: Optional. A flag to set the component performance storage.
    :param options: Optional. Specific Python options available for this component.
    :param helper: Optional. A tooltip helper.
    """
    inp = self.page.ui.fields.input(
      value=value, label=label, html_code="%s_input" % html_code, placeholder=placeholder, icon=icon, profile=profile,
      options=options)
    inp.input.set_attrs({"name": html_code})
    form = html.HtmlContainer.Form(self.page, [inp], helper)
    html.Html.set_component_skin(form)
    return form

  def inputs(self, record: List[dict], helper: str = None, html_code: str = None, options: dict = None,
             profile: types.PROFILE_TYPE = False) -> html.HtmlContainer.Form:
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

      page.ui.forms.inputs([
        {"label": "name", "htmlCode": "input"},
        {"label": "name 2", "htmlCode": "input2"},
      ])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Form`
      - :class:`epyk.core.html.HtmlContainer.Col`
      - :class:`epyk.core.html.HtmlInput.FieldInput`

    Attributes:
    ----------
    :param record: The Python list of dictionaries.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: Optional. A tooltip helper.
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    components = []
    for i, rec in enumerate(record):
      html_code_input = "%s_input_%s" % (html_code, i) if html_code is not None else html_code
      inp = self.page.ui.fields.input(label=rec["label"], html_code=html_code_input, options=options, profile=profile)
      inp.input.set_attrs({"name": rec["htmlCode"]})
      components.append(inp)
    col = self.page.ui.col(components, options=options, profile=profile).css({
      "border": '1px solid %s' % self.page.theme.greys[4],
      "text-align": 'center', "width": 'none', "padding": '5px',
      "border-radius": '5px'})
    form = html.HtmlContainer.Form(self.page, [col], helper)
    form._has_container = True
    html.Html.set_component_skin(form)
    return form

  def subscribe(self, value: str = "", placeholder: str = "Enter email address",
                button: Union[html.Html.Html, str] = "Subscribe",
                width: types.SIZE_TYPE = (100, '%'), height: types.SIZE_TYPE = (None, 'px'), options: dict = None,
                profile: types.PROFILE_TYPE = False) -> html.HtmlContainer.Div:
    """
    Description:
    ------------

    :tags:
    :categories:
    
    Usage::

    Attributes:
    ----------
    :param value: Optional. The value to be displayed to this component. Default empty.
    :param placeholder: Optional. The text to be displayed when the input is empty.
    :param button: Optional. The button component.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    input_component = self.page.ui.input(text=value, placeholder=placeholder)
    input_component.attr["class"].add("form-control")
    input_component.style.css.display = "inline-block"
    input_component.style.css.width = None

    if not hasattr(button, 'options'):
      button = self.page.ui.button(button, width=("auto", ""))
      button.style.css.margin = 0
    button_container = self.page.ui.div([button])
    button_container.attr["class"].add("input-group-append")
    button_container.style.css.width = None
    container = self.page.ui.div([
      input_component, button_container], width=width, height=height, options=options, profile=profile)
    container.attr["class"].add("input-group mb-3")
    container.button = button
    container.input = input_component
    input_component.enter(button.dom.events.trigger("click"))
    html.Html.set_component_skin(container)
    return container
