#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

from typing import Optional
from epyk.core import html
from epyk.core.py import types
from epyk.core.html import Defaults
from epyk.interfaces import Arguments
from epyk.core.data import components as cpn
from epyk.core.html import Defaults as Defaults_html

HTML_CODE_LABEL = "{}_label"
FIELD_FULL_WIDTH_VALUE = "calc(100% - 30px)"


class Fields:

  def __init__(self, ui):
    self.page = ui.page

  def text(self, text: str = "", label: str = None, color: str = None, align: str = 'left',
           width: types.SIZE_TYPE = (None, "px"), height: types.SIZE_TYPE = (None, "px"), html_code: str = None,
           tooltip: str = None, options: types.OPTION_TYPE = None, helper: str = None,
           profile: types.PROFILE_TYPE = None) -> html.HtmlText.Text:
    """
    Add the HTML text component to the page.

    :tags:
    :categories:

    Usage::

      page.ui.text("this is a test")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Text`

    Related Pages:

      https://www.w3schools.com/tags/tag_font.asp

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/banners.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/contextmenu.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/image.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/markdown.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/postit.py

    :param text: Optional. The string value to be displayed in the component
    :param label: Optional. The text of label to be added to the component
    :param color: Optional. The color of the text
    :param align: Optional. The position of the icon in the line (left, right, center)
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param tuple height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param tooltip: Optional. A string with the value of the tooltip
    :param options: Optional. Specific Python options available for this component
    :param helper: Optional. A tooltip helper
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="px")
    if width[0] is None:
        width = (Defaults.TEXTS_SPAN_WIDTH, width[1])
    height = Arguments.size(height, unit="px")
    dfl_options = {"reset": False, "markdown": False, "maxlength": None}
    if options is not None:
        dfl_options.update(options)
    text = self.page.py.encode_html(text)
    if label is not None:
        component = self.page.ui.div(width=width, height=height, profile=profile)
        component.label = self.page.ui.texts.label(
            label, options=options, html_code=HTML_CODE_LABEL.format(html_code) if html_code is not None else html_code)
        component.label.style.css.display = "inline-block"
        component.label.css({'height': 'auto', 'margin-top': '1px',  'margin-bottom': '1px'})
        component.input = html.HtmlText.Text(
            self.page, text, color, align, width, height, html_code, tooltip, dfl_options, helper, profile)
        component.input.style.css.display = "inline-block"
        component.extend([component.label, component.input])
    else:
        component = html.HtmlText.Text(
            self.page, text, color, align, width, height, html_code, tooltip, dfl_options, helper, profile)
    if width[0] == 'auto':
        component.style.css.display = "inline-block"
    if align in ["center", 'right']:
        component.style.css.margin = "auto"
        component.style.css.display = "block"
    component.style.css.display = "inline-block"
    component.style.css.text_align = "left"
    component.style.css.vertical_align = "top"
    component.style.css.margin = "0 5px"
    component.style.css.line_height = Defaults.LINE_HEIGHT
    html.Html.set_component_skin(component)
    return component

  def date(self, value: Optional[str] = None, label: str = None, icon: str = "calendar", color: str = None,
           width: types.SIZE_TYPE = (None, "px"), height: types.SIZE_TYPE = (None, "px"), html_code: str = None,
           profile: types.PROFILE_TYPE = None, options: types.OPTION_TYPE = None,
           helper: str = None) -> html.HtmlDates.DatePicker:
    """
    This component is based on the Jquery Date Picker object.

    :tags:
    :categories:

    Usage::

      dt = page.ui.fields.date('2020-04-08', label="Date").included_dates(["2020-04-08", "2019-09-06"])
      dt.select([page.js.alert(dt.dom.content)])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlDates.DatePicker`

    Related Pages:

      https://jqueryui.com/datepicker/

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/dates.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/fields.py

    :param value: Optional. The value to be displayed to the time component. Default now
    :param label: Optional. The text of label to be added to the component
    :param icon: Optional. The component icon content from font-awesome references
    :param color: Optional. The font color in the component. Default inherit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    :param helper: Optional. A tooltip helper
    """
    if value is None:
        return self.today(label=label, icon=icon, color=color, width=width, height=height, html_code=html_code,
                          profile=profile, options=options, helper=helper)

    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    dft_options = {"input": {'dateFormat': 'yy-mm-dd'}}
    if value is not None and (
        value.startswith("T-") or value.startswith("W-") or value.startswith("M-") or value.startswith("Y-")):
        value = self.page.py.dates.date_from_alias(value)
    if options is not None:
        dft_options.update(options)
    component = html.HtmlDates.DatePicker(
        self.page, value, label, icon, width, height, color, html_code, profile, dft_options, helper)
    if width[0] == 100 and width[1] == "%" and icon:
        component.style.css.width = FIELD_FULL_WIDTH_VALUE
    html.Html.set_component_skin(component)
    return component

  def today(self, label: str = None, icon: str = "calendar", color: str = None, width: types.SIZE_TYPE = (None, "px"),
            height: types.SIZE_TYPE = (None, "px"), html_code: str = None, profile: types.PROFILE_TYPE = None,
            options: types.OPTION_TYPE = None, helper: str = None) -> html.HtmlDates.DatePicker:
    """
    This component is based on the Jquery Date Picker object.

    :tags:
    :categories:

    Usage::

      page.ui.fields.today(label="Date").included_dates(["2019-09-01", "2019-09-06"])
      page.ui.fields.today()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlDates.DatePicker`

    Related Pages:

      https://jqueryui.com/datepicker/

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/dates.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/fields.py

    :categories: Inputs,Texts
    :tags: Dates

    :param label: Optional. The text of label to be added to the component
    :param icon: Optional. The component icon content from font-awesome references
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param color: Optional. The font color in the component. Default inherit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    :param helper: Optional. A tooltip helper
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    dft_options = {'dateFormat': 'yy-mm-dd'}
    if options is not None:
      dft_options.update(options)
    value = self.page.py.dates.today
    component = html.HtmlDates.DatePicker(
      self.page, value, label, icon, width, height, color, html_code, profile, dft_options, helper)
    if width[0] == 100 and width[1] == "%" and icon:
      component.style.css.width = FIELD_FULL_WIDTH_VALUE
    html.Html.set_component_skin(component)
    return component

  def cob(self, label: str = None, icon: str = "calendar", color: str = None, width: types.SIZE_TYPE = (None, "px"),
          height: types.SIZE_TYPE = (None, "px"), html_code: str = None, profile: types.PROFILE_TYPE = None,
          options: types.OPTION_TYPE = None, helper: str = None) -> html.HtmlDates.DatePicker:
    """
    This component is based on the Jquery Date Picker object.

    :tags:
    :categories:

    Usage::

      page.ui.fields.cob(label="COB Date")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlDates.DatePicker`

    Related Pages:

      https://jqueryui.com/datepicker/

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/fields.py

    :param label: Optional. The text of label to be added to the component
    :param icon: Optional. The component icon content from font-awesome references
    :param color: Optional. The font color in the component. Default inherit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    :param helper: Optional. A tooltip helper
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    dft_options = {'dateFormat': 'yy-mm-dd'}
    if options is not None:
      dft_options.update(options)
    value = self.page.py.dates.cob
    component = html.HtmlDates.DatePicker(
      self.page, value, label, icon, width, height, color, html_code, profile, dft_options, helper)
    if width[0] == 100 and width[1] == "%" and icon:
      component.style.css.width = FIELD_FULL_WIDTH_VALUE
    html.Html.set_component_skin(component)
    return component

  def now(self, deltatime: int = 0, label: str = None, icon: str = "clock", color: str = None, html_code: str = None,
          profile: types.PROFILE_TYPE = None, options: types.OPTION_TYPE = None,
          helper: str = None) -> html.HtmlDates.TimePicker:
    """
    This component is based on the Jquery Time Picker object.

    :tags:
    :categories:

    Usage::

      page.ui.fields.now(label="timestamp", color="red", helper="This is the report timestamp")
      page.ui.fields.now(label="Time field")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlDates.TimePicker`

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/fields.py

    :param deltatime: Optional
    :param label: Optional. The text of label to be added to the component
    :param icon: Optional. The component icon content from font-awesome references
    :param color: Optional. The font color in the component. Default inherit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    :param helper: Optional. A tooltip helper
    """
    date = datetime.datetime.now() + datetime.timedelta(minutes=deltatime)
    component = html.HtmlDates.TimePicker(
      self.page, str(date).split(" ")[1].split(".")[0], label, icon, color, html_code, profile, options or {}, helper)
    html.Html.set_component_skin(component)
    return component

  def time(self, value: str = None, label: str = None, icon: str = "clock", color: str = None, html_code: str = None,
           profile: types.PROFILE_TYPE = None, options: types.OPTION_TYPE = None,
           helper: str = None) -> html.HtmlDates.TimePicker:
    """
    This component is based on the Jquery Time Picker object.

    :tags:
    :categories:

    Usage::

      page.ui.fields.time(label="timestamp", color="red", helper="This is the report timestamp")
      page.ui.fields.time(label="Time field")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlDates.TimePicker`

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/fields.py

    :param value: Optional. The value to be displayed to the time component. Default now
    :param label: Optional. The text of label to be added to the component
    :param icon: Optional. The component icon content from font-awesome references
    :param color: Optional. The font color in the component. Default inherit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    :param helper: Optional. A tooltip helper
    """
    options = options or {}
    component = html.HtmlDates.TimePicker(
      self.page, value, label, icon, color, html_code, profile, options, helper)
    html.Html.set_component_skin(component)
    return component

  def input(self, value: str = "", label: str = None, placeholder: str = "", icon: str = None,
            width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (None, "px"), html_code: str = None,
            helper: str = None, options: types.OPTION_TYPE = None,
            profile: types.PROFILE_TYPE = None) -> html.HtmlInput.FieldInput:
    """

    :tags:
    :categories:

    Usage::

      page.ui.fields.input("", label="Range Example", icon="fas fa-unlock-alt")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldInput`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/fields.py

    :param value: Optional. The value to be displayed to this component. Default empty string
    :param label: Optional. The text of label to be added to the component
    :param placeholder: Optional. The text to be displayed when the input is empty
    :param icon: Optional. The component icon content from font-awesome references
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    component = html.HtmlInput.FieldInput(
      self.page, value, label, placeholder, icon, width, height, html_code, helper, options, profile)
    if options.get("format") == "column":
      component.input.style.css.text_align = "left"
      component.input.style.css.padding_left = 3
    html.Html.set_component_skin(component)
    return component

  def number(self, value: str = "", label: str = None, placeholder: str = "", icon: str = None,
             width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (None, "px"), html_code: str = None,
             helper: str = None, options: types.OPTION_TYPE = None,
             profile: types.PROFILE_TYPE = None) -> html.HtmlInput.FieldInput:
    """

    :tags:
    :categories:

    Usage::

      page.ui.fields.input("", label="Range Example", icon="fas fa-unlock-alt")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldInput`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/fields.py

    :param value: Optional. The value to be displayed to this component. Default empty string
    :param label: Optional. The text of label to be added to the component
    :param placeholder: Optional. The text to be displayed when the input is empty
    :param icon: Optional. The component icon content from font-awesome references
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    component = html.HtmlInput.FieldInput(
      self.page, value, label, placeholder, icon, width, height, html_code, helper, options, profile)
    component.input.attr["type"] = "number"
    if not options.get("scroll", True):
      component.style.add_classes.input.textfield_appearance()
      component.style.add_classes.input.textfield_appearance_inner()
      component.style.add_classes.input.textfield_appearance_outer()
    html.Html.set_component_skin(component)
    return component

  def autocomplete(self, value: str = "", label: str = None, placeholder: str = "", icon: str = None,
                   width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (None, "px"),
                   html_code: str = None, helper: str = None, options: types.OPTION_TYPE = None,
                   profile: types.PROFILE_TYPE = None) -> html.HtmlInput.FieldAutocomplete:
    """

    :tags:
    :categories:

    Usage::

      page.ui.fields.autocomplete("", label="Range Example", icon="fas fa-unlock-alt")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldAutocomplete`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/fields.py

    :param value: Optional. The value to be displayed to this component. Default empty string
    :param label: Optional. The text of label to be added to the component
    :param placeholder: Optional. The text to be displayed when the input is empty
    :param icon: Optional. The component icon content from font-awesome references
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    component = html.HtmlInput.FieldAutocomplete(
      self.page, value, label, placeholder, icon, width, height, html_code, helper, options or {}, profile)
    html.Html.set_component_skin(component)
    return component

  def static(self, value: str = "", label: str = None, placeholder: str = "", icon: str = None,
             width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (None, "px"), html_code: str = None,
             helper: str = None, options: types.OPTION_TYPE = None,
             profile: types.PROFILE_TYPE = None, input_tag: bool = False) -> html.HtmlInput.FieldInput:
    """

    :tags:
    :categories:

    Usage::

      page.ui.fields.static(label="readonly field")

      page.ui.fields.static('''
        Value Formatter €
        A Value Formatter is...
        ''', label="toto", options={"html_encode": True, "multiline": True})

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldInput`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/fields.py

    :param value: Optional. The value to be displayed to this component. Default empty string
    :param label: Optional. The text of label to be added to the component
    :param placeholder: Optional. The text to be displayed when the input is empty
    :param icon: Optional. The component icon content from font-awesome references
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    :param input_tag: Optional. Use an input field
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    if input_tag:
      component = html.HtmlInput.FieldInput(
        self.page, value, label, placeholder, icon, width, height, html_code, helper, options or {}, profile)
      component.input.readonly(True)
    else:
      input_field = self.page.ui.div(value, width=None, align=None, options=options)
      input_field.style.add_classes.input.basic()
      input_field.style.css.display = "inline-block"
      input_field.style.css.border = "1px solid %s" % self.page.theme.dark_or_white()
      input_field.style.css.min_width = Defaults.INPUTS_MIN_WIDTH
      input_field.style.css.min_height = "%spx" % Defaults_html.LINE_HEIGHT
      component = html.HtmlInput.Field(
        self.page, input_field, label, icon, width, height, html_code, helper, options or {}, profile)
      if len(component._sub_htmls) > 1:
        component._sub_htmls[1] = input_field
      input_field.style.css.background_color = self.page.theme.colors[0]
    html.Html.set_component_skin(component)
    return component

  def hidden(self, value: str = "", label: str = None, placeholder: str = "", icon: str = None,
             width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (None, "px"), html_code: str = None,
             helper: str = None, options: types.OPTION_TYPE = None,
             profile: types.PROFILE_TYPE = None) -> html.HtmlInput.FieldInput:
    """
    Create a hidden HTML component.
    This is used to store values which are not visible on the page.

    :tags:
    :categories:

    Usage::

      page.ui.fields.hidden(label="readonly field")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldInput`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/fields.py

    :param value: Optional. The value to be displayed to this component. Default empty string
    :param label: Optional. The text of label to be added to the component
    :param placeholder: Optional. The text to be displayed when the input is empty
    :param icon: Optional. The component icon content from font-awesome references
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    component = html.HtmlInput.FieldInput(
      self.page, value, label, placeholder, icon, width, height, html_code, helper, options or {}, profile)
    component.input.readonly(True)
    component.style.css.display = False
    html.Html.set_component_skin(component)
    return component

  def integer(self, value: str = "", label: str = None, placeholder: str = "", icon: str = None,
              width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (None, "px"), html_code: str = None,
              helper: str = None, options: types.OPTION_TYPE = None,
              profile: types.PROFILE_TYPE = None) -> html.HtmlInput.FieldInteger:
    """

    :tags:
    :categories:

    Usage::

      page.ui.fields.integer(label="test")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldInteger`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/fields.py

    :param value: Optional. The value to be displayed to this component. Default empty string
    :param label: Optional. The text of label to be added to the component
    :param placeholder: Optional. The text to be displayed when the input is empty
    :param icon: Optional. The component icon content from font-awesome references
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    component = html.HtmlInput.FieldInteger(
      self.page, value, label, placeholder, icon, width, height, html_code, helper, options or {}, profile)
    html.Html.set_component_skin(component)
    return component

  def file(self, value: str = "", label: str = None, placeholder: str = "", icon: str = None,
           width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (None, "px"), html_code: str = None,
           helper: str = None, options: types.OPTION_TYPE = None,
           profile: types.PROFILE_TYPE = None) -> html.HtmlInput.FieldFile:
    """

    :tags:
    :categories:

    Usage::

      page.ui.fields.integer(label="test")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldFile`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/fields.py

    :param value: Optional. The value to be displayed to this component. Default empty string
    :param label: Optional. The text of label to be added to the component
    :param placeholder: Optional. The text to be displayed when the input is empty
    :param icon: Optional. The component icon content from font-awesome references
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    self.page.css.customText(
      '::-webkit-file-upload-button {border: 1px solid %(c)s; background: %(c)s; color: %(fc)s; font-family: %(fm)s; font-sie: %(size)spx}' % {
        "c": self.page.theme.notch(4), "fc": self.page.theme.white,
        "fm": self.page.body.style.globals.font.family, "size": self.page.body.style.globals.font.size})
    component = html.HtmlInput.FieldFile(
      self.page, value, label, placeholder, icon, width, height, html_code, helper, options or {}, profile)
    html.Html.set_component_skin(component)
    return component

  def password(self, value: str = "", label: str = None, placeholder: str = "", icon: str = None,
               width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (None, "px"), html_code: str = None,
               helper: str = None, options: types.OPTION_TYPE = None,
               profile: types.PROFILE_TYPE = None) -> html.HtmlInput.FieldPassword:
    """

    :tags:
    :categories:

    Usage::

      page.ui.fields.password(label="password")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldPassword`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/fields.py

    :param value: Optional. The value to be displayed to this component. Default empty string
    :param label: Optional. The text of label to be added to the component
    :param placeholder: Optional. The text to be displayed when the input is empty
    :param icon: Optional. The component icon content from font-awesome references
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    component = html.HtmlInput.FieldPassword(
      self.page, value, label, placeholder, icon, width, height, html_code, helper, options or {}, profile)
    html.Html.set_component_skin(component)
    return component

  def textarea(self, value: str = "", label: str = None, placeholder: str = "", icon: str = None,
               width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (None, "px"), html_code: str = None,
               helper: str = None, options: types.OPTION_TYPE = None,
               profile: types.PROFILE_TYPE = None) -> html.HtmlInput.FieldTextArea:
    """

    :tags:
    :categories:

    Usage::

      page.ui.fields.textarea(label="Date")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldTextArea`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/fields.py

    :param value: Optional. The value to be displayed to this component. Default empty string
    :param label: Optional. The text of label to be added to the component
    :param placeholder: Optional. The text to be displayed when the input is empty
    :param icon: Optional. The component icon content from font-awesome references
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    component = html.HtmlInput.FieldTextArea(
      self.page, value, label, placeholder, icon, width, height, html_code, helper, options or {}, profile)
    html.Html.set_component_skin(component)
    return component

  def checkbox(self, value: bool = False, label: str = None, icon: str = None, width: types.SIZE_TYPE = (100, "%"),
               height: types.SIZE_TYPE = (None, "px"), html_code: str = None, helper: str = None,
               options: types.OPTION_TYPE = None,
               profile: types.PROFILE_TYPE = None) -> html.HtmlInput.FieldCheckBox:
    """

    :tags:
    :categories:

    Usage::

      page.ui.fields.checkbox(True, label="Check")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldCheckBox`

    Related Pages:

      https://www.w3schools.com/tags/att_input_type_checkbox.asp

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/fields.py

    :param value: Optional. The value to be displayed to this component. Default empty string
    :param label: Optional. The text of label to be added to the component
    :param icon: Optional. The component icon content from font-awesome references
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    component = html.HtmlInput.FieldCheckBox(
      self.page, value, label, icon, width, height, html_code, helper, options or {}, profile)
    html.Html.set_component_skin(component)
    return component

  def radio(self, value: bool = False, label: str = "", group_name: str = None, icon: str = None,
            width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (None, "px"), html_code: str = None,
            helper: str = None, options: types.OPTION_TYPE = None,
            profile: types.PROFILE_TYPE = None) -> html.HtmlInput.Radio:
    """
    The <input type="radio"> defines a radio button.
    Radio buttons are normally presented in radio groups (a collection of radio buttons describing a set of
    related options).
    Only one radio button in a group can be selected at the same time.

    :tags:
    :categories:

    Usage::

      page.ui.inputs.radio(False, label="radio")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.Radio`

    Related Pages:

      https://www.w3schools.com/tags/att_input_type_radio.asp

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/fields.py

    :param value: Optional. The value to be displayed to this component. Default False
    :param label: Optional. The text of label to be added to the component
    :param group_name: Optional. Group different radio together to only have 1 value selected
    :param icon: Optional. The component icon content from font-awesome references
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    component = html.HtmlInput.Radio(self.page, value, label, group_name, icon, width, height, html_code,
                                     helper, options or {}, profile)
    if options is not None and options.get('position') == 'after':
      component.label.css({"width": '100px'})
    else:
      component.label.css({"width": '100px', 'float': 'left'})
    component.css({"display": 'inline-block'})
    html.Html.set_component_skin(component)
    return component

  def range(self, value: str = "", min: int = 0, max: int = 100, step: int = 1, label: str = None,
            placeholder: str = "", icon: str = None, width: types.SIZE_TYPE = (100, "%"),
            height: types.SIZE_TYPE = (None, "px"), html_code: str = None, helper: str = None,
            options: types.OPTION_TYPE = None,
            profile: types.PROFILE_TYPE = None) -> html.HtmlInput.FieldRange:
    """
    The <input type="range"> defines a control for entering a number whose exact value is not important.
    Default range is 0 to 100. However, you can set restrictions on what numbers are accepted with the attributes below.
    - max - specifies the maximum value allowed
    - min - specifies the minimum value allowed
    - step - specifies the legal number intervals
    - value - Specifies the default value

    :tags:
    :categories:

    Usage::

      page.ui.fields.range(54, min=20, label="Range Example", icon="fas fa-unlock-alt")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldRange`

    Related Pages:

      https://www.w3schools.com/tags/att_input_type_range.asp

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/fields.py

    :param value: Optional. The value to be displayed to this component. Default empty string
    :param min:
    :param max:
    :param step:
    :param label: Optional. The text of label to be added to the component
    :param placeholder:
    :param icon: Optional. The component icon content from font-awesome references
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    component = html.HtmlInput.FieldRange(self.page, value, min, max, step, label, placeholder, icon, width,
                                          height, html_code, helper, options or {}, profile)
    html.Html.set_component_skin(component)
    return component

  def select(self, value: list = None, label: str = None, icon: str = None, selected: bool = None,
             width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (None, "px"), html_code: str = None,
             helper: str = None, options: types.OPTION_TYPE = None, multiple: bool = False,
             profile: types.PROFILE_TYPE = None) -> html.HtmlInput.FieldSelect:
    """

    :tags:
    :categories:

    Usage::

      page.ui.fields.select(["a", "b"], label="Check")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldSelect`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/fields.py

    :param value: Optional. The value to be displayed to the component. Default False
    :param label: Optional. The text of label to be added to the component
    :param icon: Optional. The component icon content from font-awesome references
    :param selected: Optional. The selected value
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param options: Optional. Specific Python options available for this component
    :param multiple: Optional. Flag to specify the number of items to be selectable
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    if options is not None and 'align' in options:
      self.page.css.customText('.filter-option-inner-inner {text-align: %s}' % options['align'])
    component = html.HtmlInput.FieldSelect(self.page, value, label, icon, width, height, html_code,
                                           helper, options or {}, profile)
    if multiple:
      component.input.attr['multiple'] = None
    component.input.attr['data-width'] = '%spx' % options.get('width', html.Defaults.INPUTS_MIN_WIDTH)
    component.input.button_css = {
      "background": self.page.theme.notch(-5) if self.page.theme.dark else self.page.theme.notch(4),
      "color": self.page.theme.white, "border-radius": 0}
    if width[0] == "auto":
      component.style.css.display = "inline-block"
    if selected is not None:
      component.input.options.selected = selected
    html.Html.set_component_skin(component)
    return component

  def months(self, value=None, label: str = None, icon: str = None, width: types.SIZE_TYPE = (100, "%"),
             height: types.SIZE_TYPE = (None, "px"), html_code: str = None, helper: str = None,
             options: types.OPTION_TYPE = None,
             profile: types.PROFILE_TYPE = None) -> html.HtmlInput.FieldSelect:
    """

    :tags:
    :categories:

    Usage::

      page.ui.fields.select(["a", "b"], label="Check")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldSelect`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/fields.py

    :param value: Optional. The value to be displayed to this component
    :param label: Optional. The text of label to be added to the component
    :param icon: Optional. The component icon content from font-awesome references
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    import calendar

    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    if value is None:
      dt = datetime.datetime.today()
      value = dt.month
    if options is not None and 'align' in options:
      self.page.css.customText('.filter-option-inner-inner {text-align: %s}' % options['align'])
    values = [{"name": calendar.month_name[i], 'value': i} for i in range(12)]
    component = html.HtmlInput.FieldSelect(self.page, values, label, icon, width, height, html_code, helper,
                                           options or {}, profile)
    component.input.attr['data-width'] = '%spx' % html.Defaults.INPUTS_MIN_WIDTH
    if component.input.options.selected is None:
      component.input.options.selected = value
    html.Html.set_component_skin(component)
    return component

  def weeks(self, value=None, label: str = None, icon: str = None, width: types.SIZE_TYPE = (100, "%"),
            height: types.SIZE_TYPE = (None, "px"), html_code: str = None,
            helper: str = None, options: types.OPTION_TYPE = None,
            profile: types.PROFILE_TYPE = None) -> html.HtmlInput.FieldSelect:
    """

    :tags:
    :categories:

    Usage::

      page.ui.fields.select(["a", "b"], label="Check")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldSelect`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/fields.py

    :param value: Optional. The value to be displayed to this component
    :param label: Optional. The text of label to be added to the component
    :param icon: Optional. The component icon content from font-awesome references
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dt = datetime.datetime.today()
    if value is None:
      value = datetime.datetime.utcnow().isocalendar()[1]
    values = []
    for i in range(52):
      d = "%s-W%s" % (dt.year, i)
      start_date = datetime.datetime.strptime(d + '-1', "%Y-W%W-%w")
      end_date = start_date + datetime.timedelta(days=5)
      values.append({"value": i+1, 'name': "W%s [%s - %s]" % (
        i+1, start_date.strftime('%d/%m'), end_date.strftime('%d/%m'))})
    if options is not None and 'align' in options:
      self.page.css.customText('.filter-option-inner-inner {text-align: %s}' % options['align'])
    component = html.HtmlInput.FieldSelect(self.page, values, label, icon, width, height, html_code, helper,
                                           options or {}, profile)
    component.input.attr['data-width'] = '%spx' % html.Defaults.INPUTS_MIN_WIDTH
    if component.input.options.selected is None:
      component.input.options.selected = value
    html.Html.set_component_skin(component)
    return component

  def years(self, value=None, label: str = None, icon: str = None, width: types.SIZE_TYPE = (100, "%"),
            height: types.SIZE_TYPE = (None, "px"), html_code: str = None,
            helper: str = None, options: types.OPTION_TYPE = None,
            profile: types.PROFILE_TYPE = None) -> html.HtmlInput.FieldSelect:
    """

    :tags:
    :categories:

    Usage::

      page.ui.fields.select(["a", "b"], label="Check")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldSelect`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/fields.py
 -
    :param value: Optional. The value to be displayed to this component
    :param label: Optional. The text of label to be added to the component
    :param icon: Optional. The component icon content from font-awesome references
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dt = datetime.datetime.today()
    if value is None:
      value = dt.year
    if options is not None and 'align' in options:
      self.page.css.customText('.filter-option-inner-inner {text-align: %s}' % options['align'])
    values = [{"name": i, 'value': i} for i in range(dt.year+1)][::-1]
    component = html.HtmlInput.FieldSelect(self.page, values, label, icon, width, height, html_code, helper,
                                           options or {}, profile)
    component.input.attr['data-width'] = '%spx' % html.Defaults.INPUTS_MIN_WIDTH
    if component.input.options.selected is None:
      component.input.options.selected = value
    html.Html.set_component_skin(component)
    return component

  def days(self, value=None, label: str = None, icon: str = None, width: types.SIZE_TYPE = (100, "%"),
           height: types.SIZE_TYPE = (None, "px"), html_code: str = None,
           helper: str = None, options: types.OPTION_TYPE = None,
           profile: types.PROFILE_TYPE = None) -> html.HtmlInput.FieldSelect:
    """

    :tags:
    :categories:

    Usage::

      page.ui.fields.select(["a", "b"], label="Check")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldSelect`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/fields.py

    :param value: Optional. The value to be displayed to this component
    :param label: Optional. The text of label to be added to the component
    :param icon: Optional. The component icon content from font-awesome references
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. A tooltip helper
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    import calendar

    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    if value is None:
      dt = datetime.datetime.today()
      value = dt.weekday()
    if options is not None and 'align' in options:
      self.page.css.customText('.filter-option-inner-inner {text-align: %s}' % options['align'])
    values = [{"name": calendar.day_name[i], 'value': i} for i in range(7)]
    component = html.HtmlInput.FieldSelect(self.page, values, label, icon, width, height, html_code, helper,
                                           options or {}, profile)
    component.input.attr['data-width'] = '%spx' % html.Defaults.INPUTS_MIN_WIDTH
    if component.input.options.selected is None:
      component.input.options.selected = value
    html.Html.set_component_skin(component)
    return component

  def column_text(self, label, text: str = "", align: str = 'left', width: types.SIZE_TYPE = ('auto', ""),
                  height: types.SIZE_TYPE = (None, "px"), html_code: str = None,
                  options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = None) -> html.HtmlContainer.Div:
    """

    :tags:
    :categories:

    Usage::

    :param label: Optional. The text of label to be added to the component
    :param text: Optional. The string value to be displayed in the component
    :param align: Optional. The text-align property within this component
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    component = self.page.ui.div(align=align, width=width, height=height, options=options, profile=profile)
    component.label = self.page.ui.text(
      label, options=options, html_code=html_code if html_code is None else HTML_CODE_LABEL.format(html_code), profile=profile)
    component.label.style.css.display = 'block'
    component.label.style.css.margin_bottom = 10
    component.label.style.css.color = self.page.theme.greys[6]
    component.text = self.page.ui.inputs.input(text, options=options, html_code=html_code, profile=profile)
    component.text.style.css.bold()
    component.text.style.css.margin_bottom = 10
    component.text.style.css.display = 'block'
    component.text.style.css.font_factor(5)
    component.style.css.margin = 4
    component.style.css.display = 'inline-block'
    component.add(component.label)
    component.add(component.text)
    html.Html.set_component_skin(component)
    return component

  def column_date(self, label, value: str = "T", align: str = 'left', width: types.SIZE_TYPE = ('auto', ""),
                  height: types.SIZE_TYPE = (None, "px"), html_code: str = None,
                  options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = None) -> html.HtmlContainer.Div:
    """

    :tags:
    :categories:

    Usage::

    :param label: Optional. The text of label to be added to the component
    :param value: Optional. The value to be displayed to this component. Default T
    :param align: Optional. The text-align property within this component
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    component = self.page.ui.div(align=align, width=width, height=height, options=options, profile=profile)
    component.label = self.page.ui.text(
      label, options=options, html_code=html_code if html_code is None else HTML_CODE_LABEL.format(html_code), profile=profile)
    component.label.style.css.display = 'block'
    component.label.style.css.margin_bottom = 10
    component.label.style.css.color = self.page.theme.greys[6]
    if value is None:
      component.text = self.date(value, options=options, html_code=html_code, profile=profile)
    else:
      component.text = self.today(options=options, html_code=html_code, profile=profile)
    component.text.style.css.bold()
    component.text.style.css.margin_bottom = 10
    component.text.style.css.display = 'block'
    component.text.style.css.font_factor(5)
    component.style.css.margin = 4
    component.style.css.display = 'inline-block'
    component.add(component.label)
    component.add(component.text)
    html.Html.set_component_skin(component)
    return component

  def toggle(self, record=None, label: str = None, is_on: bool = False, color: str = None,
             width: types.SIZE_TYPE = (100, '%'), height: types.SIZE_TYPE = (20, 'px'),
             html_code: str = None, options: types.OPTION_TYPE = None,
             profile: types.PROFILE_TYPE = None) -> html.HtmlContainer.Div:
    """
    Add a toggle component.

    :tags:
    :categories:

    Usage::

      page.ui.buttons.toggle({'on': "true", 'off': 'false'})

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlRadio.Switch`

    Related Pages:

      http://thecodeplayer.com/walkthrough/pure-css-on-off-toggle-switch
      https://codepen.io/mburnette/pen/LxNxNg

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/button.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/switch.py

    :param record: Optional. The list of dictionaries with the data
    :param label: Optional. The toggle static label displayed
    :param is_on: Optional.
    :param color: Optional. String. Optional. The font color in the component. Default inherit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    record = record or {"off": "Off", "on": "On"}
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"is_on": is_on}
    if options is not None:
      dfl_options.update(options)
    component = self.page.ui.div(width=width, height=height, options=dfl_options, profile=profile)
    component.style.css.margin_top = 5
    component.input = html.HtmlRadio.Switch(
      self.page, record, color, ("auto", ''), height, html_code, dfl_options, profile)
    if label is not None:
      component.input.style.css.display = 'inline-block'
      component.label = self.page.ui.text(
        label, options=options, html_code=html_code if html_code is None else HTML_CODE_LABEL.format(html_code),
        profile=profile)
      component.label.style.css.display = 'inline-block'
      component.label.style.css.margin = '0 5px'
      component.label.style.css.line_height = Defaults.LINE_HEIGHT
      component.label.style.css.width = '{}px'.format(Defaults.INPUTS_MIN_WIDTH)
      component.extend([component.label, component.input])
    html.Html.set_component_skin(component)
    return component

  def slider(self, value: float = 0, min: float = 0, max: float = 10, step: float = 1, orientation: str = 'horizontal',
             label: str = None, width: types.SIZE_TYPE = (100, '%'), height: types.SIZE_TYPE = (None, 'px'),
             html_code: str = None, options: types.OPTION_TYPE = None, range: bool = False,
             profile: types.PROFILE_TYPE = None) -> html.HtmlContainer.Div:
    """

    :param value: Optional. The value to be displayed to this component. Default 0
    :param min: Optional.
    :param max: Optional.
    :param step: Optional.
    :param orientation: Optional.
    :param label: Optional. The toggle static label displayed
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param options: Optional. Specific Python options available for this component
    :param range: Optional.
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"show_min_max": False, "force_show_current": True}
    if options is not None:
      dfl_options.update(options)
    component = self.page.ui.div(width=width, height=height, options=dfl_options, profile=profile)
    if range:
      component.input = self.page.ui.sliders.range(
        values=value, minimum=min, maximum=max, width=(Defaults.INPUTS_MIN_WIDTH, 'px'), height=None,
        html_code=html_code, options=dfl_options)
    else:
      component.input = self.page.ui.slider(
        number=value, minimum=min, maximum=max, width=(Defaults.INPUTS_MIN_WIDTH, 'px'),
        height=None, html_code=html_code, options=dfl_options)
    component.input.style.css.margin = 0
    component.style.css.margin_top = 5
    component.input.options.step = step
    if label is not None:
      component.input.style.css.display = 'inline-block'
      component.label = self.page.ui.text(
        label, options=options, html_code=html_code if html_code is None else HTML_CODE_LABEL.format(html_code),
        profile=profile)
      component.label.style.css.display = 'inline-block'
      component.label.style.css.margin = '0 5px'
      component.label.style.css.width = '{}px'.format(Defaults.INPUTS_MIN_WIDTH)
      component.label.style.css.line_height = Defaults.LINE_HEIGHT
      component.extend([component.label, component.input])
    if orientation == "vertical":
      component.input.style.css.height = component.input.style.css.width
      component.input.style.css.width = component.input.style.css.height
      component.input.options.css = {"width": "5px", "background": "#bdbdbd"}
      component.input.options.handler_css = {
        "left": "-7px", "border-radius": '60px', "border": "1px solid grey", "background": "white"}
    else:
      component.input.style.css.line_height = height[0]
      component.input.options.css = {"height": "5px", "background": "#bdbdbd"}
      component.input.options.handler_css = {
        "top": "-7px", "border-radius": '60px', "border": "1px solid grey", "background": "white"}
    component.input.options.orientation = orientation
    html.Html.set_component_skin(component)
    return component

  def filters(self, items=None, button=None, width: types.SIZE_TYPE = ("auto", ""),
              height: types.SIZE_TYPE = (60, "px"), html_code: str = None, helper: str = None,
              options: types.OPTION_TYPE = None, autocomplete: bool = False, kind: str = 'select',
              profile: types.PROFILE_TYPE = None):
    """

    :param items:
    :param button:
    :param width:
    :param height:
    :param html_code:
    :param helper:
    :param options:
    :param autocomplete:
    :param kind:
    :param profile:
    """
    if kind == 'select':
      component = self.page.ui.lists.filters(
        items, button, width, height, html_code, helper, options, autocomplete, profile)
      component.select.button_css = {
        "background": self.page.theme.notch(4), "color": self.page.theme.white, "border-radius": 0}
    elif kind == 'input':
      component = self.page.ui.inputs.filters(
        items, button, width, height, html_code, helper, options, autocomplete, profile)
    else:
      raise ValueError("Kind {} not defined".format(kind))

    html.Html.set_component_skin(component)
    return component

  def dates(self, value: Optional[str] = None, label: str = None, icon: str = "calendar-week", color: str = None,
           width: types.SIZE_TYPE = (None, "px"), height: types.SIZE_TYPE = (None, "px"), html_code: str = None,
           profile: types.PROFILE_TYPE = None, options: types.OPTION_TYPE = None,
           helper: str = None) -> html.HtmlDates.EasePick:
    """

    :param value: Optional. The value to be displayed to the time component. Default now
    :param label: Optional. The text of label to be added to the component
    :param icon: Optional. The component icon content from font-awesome references
    :param color: Optional. The font color in the component. Default inherit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    :param helper: Optional. A tooltip helper
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    dft_options = Arguments.clean_opt(options, {"input": {'format': 'YYYY-MM-DD', "grid": 2, "calendars": 2}})
    if value is not None and (
        value.startswith("T-") or value.startswith("W-") or value.startswith("M-") or value.startswith("Y-")):
        value = self.page.py.dates.date_from_alias(value)
    component = html.HtmlDates.EasePick(
        self.page, value, label, icon, width, height, color, html_code, profile, dft_options, helper)
    if width[0] == 100 and width[1] == "%" and icon:
        component.style.css.width = FIELD_FULL_WIDTH_VALUE
    html.Html.set_component_skin(component)
    return component


class Timelines:

  def __init__(self, ui):
    self.page = ui.page

  def view(self, start_date: types.DATE_TYPES, end_date: types.DATE_TYPES, width: types.SIZE_TYPE = (100, "%"),
           height: types.SIZE_TYPE = (None, "px"), options: types.OPTION_TYPE = None,
           profile: types.PROFILE_TYPE = None) -> html.HtmlContainer.Div:
    """   

    :tags:
    :categories:

    Usage::

    :param start_date:
    :param end_date:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    if not isinstance(start_date, datetime.datetime):
      start_date = datetime.datetime(*[int(x) for x in start_date.split("-")])
    if not isinstance(end_date, datetime.datetime):
      end_date = datetime.datetime(*[int(x) for x in end_date.split("-")])

    today, remaining_days = datetime.datetime.now(), 0
    dt = start_date
    while dt < end_date:
      if not dt.weekday() in [6, 5]:
        if dt >= today:
          remaining_days += 1
      dt += datetime.timedelta(days=1)
    component = self.page.ui.div("{} - {}".format(
      start_date.strftime("%b %d"), end_date.strftime("%b %d")), width=width, height=height, options=options,
                           profile=profile)
    component.style.css.background = self.page.theme.colors[1]
    component.style.css.border_radius = 20
    component.style.css.padding = 2
    component.style.css.text_align = 'center'
    component.tooltip("{} days remaining".format(remaining_days))
    if end_date < today:
      component.style.css.background = self.page.theme.greys[6]
      component.style.css.color = self.page.theme.greys[0]
    html.Html.set_component_skin(component)
    return component

  def period(self, start_date: types.DATE_TYPES, days: int, width: types.SIZE_TYPE = (100, "%"),
             height: types.SIZE_TYPE = (None, "px"),
             options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = None) -> html.HtmlContainer.Div:
    """   

    :tags:
    :categories:

    Usage::

    :param start_date:
    :param days:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    today, remaining_days = datetime.datetime.now(), 0
    if not isinstance(start_date, datetime.datetime):
      start_date = datetime.datetime(*[int(x) for x in start_date.split("-")])
    end_date = start_date
    for _ in range(days):
      if end_date >= today:
        remaining_days += 1
      if end_date.weekday() == 4:
        # skip weekends
        end_date += datetime.timedelta(days=3)
      else:
        end_date += datetime.timedelta(days=1)
    if end_date >= today:
      remaining_days += 1
    component = self.page.ui.div("{} - {}".format(
      start_date.strftime("%b %d"), end_date.strftime("%b %d")), width=width, height=height, options=options,
                           profile=profile)
    component.style.css.background = self.page.theme.colors[1]
    component.style.css.border_radius = 20
    component.style.css.padding = 2
    component.style.css.text_align = 'center'
    component.tooltip("{} days remaining".format(remaining_days))
    if end_date < today:
      component.style.css.background = self.page.theme.greys[6]
      component.style.css.color = self.page.theme.greys[0]
    html.Html.set_component_skin(component)
    return component

  def week(self, start_date: types.DATE_TYPES, width: types.SIZE_TYPE = (100, "%"),
           height: types.SIZE_TYPE = (None, "px"),
           options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = None) -> html.HtmlContainer.Div:
    """   

    :tags:
    :categories:

    Usage::

    :param start_date:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    today, remaining_days = datetime.datetime.now(), 0
    if not isinstance(start_date, datetime.datetime):
      start_date = datetime.datetime(*[int(x) for x in start_date.split("-")])
    end_date = start_date + datetime.timedelta(days=7)
    if today < end_date:
      next_day = today
      while next_day < end_date:
        if next_day.weekday() in [6, 5]:
          next_day += datetime.timedelta(days=1)
          continue

        remaining_days += 1
        next_day += datetime.timedelta(days=1)
    component = self.page.ui.div("{} - {}".format(
      start_date.strftime("%b %d"), end_date.strftime("%b %d")), width=width, height=height, options=options,
                           profile=profile)
    component.style.css.background = self.page.theme.colors[1]
    component.style.css.border_radius = 20
    component.style.css.padding = 2
    component.style.css.text_align = 'center'
    component.tooltip("{} days remaining".format(remaining_days))
    html.Html.set_component_skin(component)
    return component

  def categories(self, value=None, label: str = None, icon: str = None, width: types.SIZE_TYPE = (100, "%"),
                 height: types.SIZE_TYPE = (None, "px"), html_code: str = None,
                 helper: str = None, options: types.OPTION_TYPE = None,
                 profile: types.PROFILE_TYPE = None) -> html.HtmlInput.FieldSelect:
    """   

    :tags:
    :categories:

    Usage::

    :param value:
    :param label: Optional.
    :param icon: Optional.
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: Optional.
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    values = cpn.select.from_list(["Documentation", 'Analysis', 'Design', 'Implementation', 'Training'])
    component = html.HtmlInput.FieldSelect(
      self.page, values, label, icon, width, height, html_code, helper, options or {}, profile)
    if component.input.options.selected is None:
      component.input.selected = value
    html.Html.set_component_skin(component)
    return component

  def milestone(self, completion_date: types.DATE_TYPES, icon: str = None,
                width: types.SIZE_TYPE = (25, 'px'), height: types.SIZE_TYPE = (25, 'px'), html_code: str = None,
                options: types.OPTION_TYPE = None,
                profile: types.PROFILE_TYPE = None) -> html.HtmlButton.IconEdit:
    """   

    :tags:
    :categories:

    Usage::

    :param completion_date:
    :param icon: Optional.
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional.
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    today, remaining_days = datetime.datetime.now(), 0
    if not isinstance(completion_date, datetime.datetime):
      completion_date = datetime.datetime(*[int(x) for x in completion_date.split("-")])
    if icon is None:
      icon = "fas fa-fire-alt"
    component = self.page.ui.icons.awesome(
      icon, width=width, height=height, html_code=html_code, options=options, profile=profile)
    if completion_date > today:
      next_day = today
      while next_day < completion_date:
        if next_day.weekday() in [6, 5]:
          next_day += datetime.timedelta(days=1)
          continue

        remaining_days += 1
        next_day += datetime.timedelta(days=1)
      component.tooltip("to be completed in {} ({} days left)".format(completion_date.strftime("%b %d"), remaining_days))
      component.icon.style.css.color = self.page.theme.danger.base
    else:
      component.tooltip("Completed in {}".format(completion_date.strftime("%b %d")))
      component.icon.style.css.color = self.page.theme.greys[6]
    html.Html.set_component_skin(component)
    return component

  def meeting(self, time, icon: str = None, width: types.SIZE_TYPE = (25, 'px'),
              height: types.SIZE_TYPE = (25, 'px'), html_code: str = None, options: types.OPTION_TYPE = None,
              profile: types.PROFILE_TYPE = None) -> html.HtmlButton.IconEdit:
    """   

    :tags:
    :categories:

    Usage::

    :param time:
    :param icon: Optional.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    dfl_options = {"working_hours": 8}
    if options is not None:
      dfl_options.update(options)
    if icon is None:
      icon = "far fa-handshake"
    component = self.page.ui.icons.awesome(icon, width=width, height=height, html_code=html_code, profile=profile)
    component.tooltip("{} hours ({} days)".format(time, time / dfl_options["working_hours"]))
    html.Html.set_component_skin(component)
    return component

  def workload(self, value, width: types.SIZE_TYPE = (25, 'px'), html_code: str = None,
               options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = None) -> html.HtmlContainer.Div:
    """   

    :tags:
    :categories:

    Usage::

    :param value: The workload percentage.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    dfl_options = {"working_hours": 8}
    if options is not None:
      dfl_options.update(options)
    width = (width[0] * (value / dfl_options["working_hours"]), 'px')
    height = width
    component = self.page.ui.div(value, width=width, height=height, html_code=html_code, profile=profile)
    component.style.css.border_radius = 20
    component.style.css.text_align = "center"
    component.style.css.color = "white"
    component.style.css.line_height = "{}{}".format(height[0], height[1])
    component.style.css.vertical_align = "middle"
    if value < (dfl_options["working_hours"] - 2):
      component.style.css.background = self.page.theme.success.base
    elif value < dfl_options["working_hours"]:
      component.style.css.background = self.page.theme.warning.base
    else:
      component.style.css.background = self.page.theme.danger.base
    html.Html.set_component_skin(component)
    return component

  def issues(self, records=None, width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = ("auto", ""),
             options: dict = None, html_code: str = None, profile: types.PROFILE_TYPE = None,
             helper: str = None) -> html.HtmlList.Items:
    """   

    :tags:
    :categories:

    Usage::

    :param records:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    :param helper:
    """
    component = self.page.ui.lists.items(records, width, height, options, html_code, profile, helper)
    component.options.items_type = "status"
    html.Html.set_component_skin(component)
    return component
