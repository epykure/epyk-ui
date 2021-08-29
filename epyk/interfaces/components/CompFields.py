#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

from epyk.core import html
from epyk.core.html import Defaults
from epyk.interfaces import Arguments
from epyk.core.data import components as cpn


class Fields:

  def __init__(self, ui):
    self.page = ui.page

  @html.Html.css_skin()
  def text(self, text="", label=None, color=None, align='left', width=(None, "px"), height=(None, "px"),
           html_code=None, tooltip=None, options=None, helper=None, profile=None):
    """
    Description:
    ------------
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

    Attributes:
    ----------
    :param text: String. Optional. The string value to be displayed in the component.
    :param label: String. Optional. The text of label to be added to the component.
    :param color: String. Optional. The color of the text.
    :param align: String. Optional. The position of the icon in the line (left, right, center).
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param helper: String. Optional. A tooltip helper.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
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
      text_comp = self.page.ui.div(width=width, height=height, profile=profile)
      text_comp.label = self.page.ui.texts.label(
        label, options=options, html_code="%s_label" % html_code if html_code is not None else html_code)
      text_comp.label.style.css.display = "inline-block"
      text_comp.label.css({'height': 'auto', 'margin-top': '1px',  'margin-bottom': '1px'})
      text_comp.input = html.HtmlText.Text(
        self.page, text, color, align, width, height, html_code, tooltip, dfl_options, helper, profile)
      text_comp.input.style.css.display = "inline-block"
      text_comp.extend([text_comp.label, text_comp.input])
    else:
      text_comp = html.HtmlText.Text(
        self.page, text, color, align, width, height, html_code, tooltip, dfl_options, helper, profile)
    if width[0] == 'auto':
      text_comp.style.css.display = "inline-block"
    if align in ["center", 'right']:
      text_comp.style.css.margin = "auto"
      text_comp.style.css.display = "block"
    text_comp.style.css.display = "inline-block"
    text_comp.style.css.text_align = "left"
    text_comp.style.css.vertical_align = "top"
    text_comp.style.css.margin = "0 5px"
    text_comp.style.css.line_height = Defaults.LINE_HEIGHT
    return text_comp

  @html.Html.css_skin()
  def date(self, value=None, label=None, icon="far fa-calendar-alt", color=None, width=(None, "px"),
           height=(None, "px"), html_code=None, profile=None, options=None, helper=None):
    """
    Description:
    ------------
    This component is based on the Jquery Date Picker object.

    :tags:
    :categories:

    Usage::

      page.ui.fields.date('2020-04-08', label="Date").included_dates(["2020-04-08", "2019-09-06"])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlDates.DatePicker`

    Related Pages:

      https://jqueryui.com/datepicker/

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/dates.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/fields.py

    Attributes:
    ----------
    :param value: String. Optional. The value to be displayed to the time component. Default now.
    :param label: String. Optional. The text of label to be added to the component.
    :param icon: String. Optional. The component icon content from font-awesome references.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param helper: String. Optional. A tooltip helper.
    """
    if value is None:
      return self.today(label=label, icon=icon, color=color, width=width, height=height, html_code=html_code,
                        profile=profile, options=options, helper=helper)

    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    dftl_options = {'dateFormat': 'yy-mm-dd'}
    if value is not None and (
      value.startswith("T-") or value.startswith("W-") or value.startswith("M-") or value.startswith("Y-")):
      value = self.page.py.dates.date_from_alias(value)
    if options is not None:
      dftl_options.update(options)
    html_dt = html.HtmlDates.DatePicker(
      self.page, value, label, icon, width, height, color, html_code, profile, dftl_options, helper)
    if width[0] == 100 and width[1] == "%" and icon:
      html_dt.style.css.width = "calc(100% - 30px)"
    return html_dt

  @html.Html.css_skin()
  def today(self, label=None, icon="far fa-calendar-alt", color=None, width=(None, "px"), height=(None, "px"),
            html_code=None, profile=None, options=None, helper=None):
    """
    Description:
    ------------
    This component is based on the Jquery Date Picker object.

    :tags:
    :categories:

    Usage::

      page.ui.fields.today(label="Date").included_dates(["2019-09-01", "2019-09-06"])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlDates.DatePicker`

    Related Pages:

      https://jqueryui.com/datepicker/

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/dates.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/fields.py

    :categories: Inputs,Texts
    :tags: Dates

    Attributes:
    ----------
    :param label: String. Optional. The text of label to be added to the component.
    :param icon: String. Optional. The component icon content from font-awesome references.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param helper: String. Optional. A tooltip helper.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    dftl_options = {'dateFormat': 'yy-mm-dd'}
    if options is not None:
      dftl_options.update(options)
    value = self.page.py.dates.today
    html_dt = html.HtmlDates.DatePicker(
      self.page, value, label, icon, width, height, color, html_code, profile, dftl_options, helper)
    if width[0] == 100 and width[1] == "%" and icon:
      html_dt.style.css.width = "calc(100% - 30px)"
    return html_dt

  @html.Html.css_skin()
  def cob(self, label=None, icon="far fa-calendar-alt", color=None, width=(None, "px"), height=(None, "px"),
          html_code=None, profile=None, options=None, helper=None):
    """
    Description:
    ------------
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

    Attributes:
    ----------
    :param label: String. Optional. The text of label to be added to the component.
    :param icon: String. Optional. The component icon content from font-awesome references.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param helper: String. Optional. A tooltip helper.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    dftl_options = {'dateFormat': 'yy-mm-dd'}
    if options is not None:
      dftl_options.update(options)
    value = self.page.py.dates.cob
    html_cob = html.HtmlDates.DatePicker(
      self.page, value, label, icon, width, height, color, html_code, profile, dftl_options, helper)
    if width[0] == 100 and width[1] == "%" and icon:
      html_cob.style.css.width = "calc(100% - 30px)"
    return html_cob

  @html.Html.css_skin()
  def now(self, deltatime=0, label=None, icon="far fa-clock", color=None, html_code=None, profile=None, options=None,
          helper=None):
    """
    Description:
    ------------
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

    Attributes:
    ----------
    :param deltatime: Integer. Optional.
    :param label: String. Optional. The text of label to be added to the component.
    :param icon: String. Optional. The component icon content from font-awesome references.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param helper: String. Optional. A tooltip helper.
    """
    date = datetime.datetime.now() + datetime.timedelta(minutes=deltatime)
    html_dt = html.HtmlDates.TimePicker(
      self.page, str(date).split(" ")[1].split(".")[0], label, icon, color, html_code, profile, options or {}, helper)
    return html_dt

  @html.Html.css_skin()
  def time(self, value=None, label=None, icon="far fa-clock", color=None, html_code=None, profile=None, options=None,
           helper=None):
    """
    Description:
    ------------
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

    Attributes:
    ----------
    :param value: String. Optional. The value to be displayed to the time component. Default now.
    :param label: String. Optional. The text of label to be added to the component.
    :param icon: String. Optional. The component icon content from font-awesome references.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param helper: String. Optional. A tooltip helper.
    """
    options = options or {}
    html_dt = html.HtmlDates.TimePicker(
      self.page, value, label, icon, color, html_code, profile, options, helper)
    return html_dt

  @html.Html.css_skin()
  def input(self, value="", label=None, placeholder="", icon=None, width=(100, "%"), height=(None, "px"),
            html_code=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

      page.ui.fields.input("", label="Range Example", icon="fas fa-unlock-alt")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldInput`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/fields.py

    Attributes:
    ----------
    :param value: String. Optional. The value to be displayed to this component. Default empty string.
    :param label: String. Optional. The text of label to be added to the component.
    :param placeholder: String. Optional. The text to be displayed when the input is empty.
    :param icon: String. Optional. The component icon content from font-awesome references.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: Optional. A tooltip helper.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    html_input = html.HtmlInput.FieldInput(
      self.page, value, label, placeholder, icon, width, height, html_code, helper, options, profile)
    if options.get("format") == "column":
      html_input.input.style.css.text_align = "left"
      html_input.input.style.css.padding_left = 3
    return html_input

  @html.Html.css_skin()
  def number(self, value="", label=None, placeholder="", icon=None, width=(100, "%"), height=(None, "px"),
             html_code=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

      page.ui.fields.input("", label="Range Example", icon="fas fa-unlock-alt")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldInput`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/fields.py

    Attributes:
    ----------
    :param value: String. Optional. The value to be displayed to this component. Default empty string.
    :param label: String. Optional. The text of label to be added to the component.
    :param placeholder: String. Optional. The text to be displayed when the input is empty.
    :param icon: String. Optional. The component icon content from font-awesome references.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: String. Optional. A tooltip helper.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    html_input = html.HtmlInput.FieldInput(
      self.page, value, label, placeholder, icon, width, height, html_code, helper, options, profile)
    html_input.input.attr["type"] = "number"
    if not options.get("scroll", True):
      html_input.style.add_classes.input.textfield_appearance()
      html_input.style.add_classes.input.textfield_appearance_inner()
      html_input.style.add_classes.input.textfield_appearance_outer()
    return html_input

  @html.Html.css_skin()
  def autocomplete(self, value="", label=None, placeholder="", icon=None, width=(100, "%"), height=(None, "px"),
                   html_code=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

      page.ui.fields.autocomplete("", label="Range Example", icon="fas fa-unlock-alt")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldAutocomplete`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/fields.py

    Attributes:
    ----------
    :param value: String. Optional. The value to be displayed to this component. Default empty string.
    :param label: String. Optional. The text of label to be added to the component.
    :param placeholder: String. Optional. The text to be displayed when the input is empty.
    :param icon: String. Optional. The component icon content from font-awesome references.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: String. Optional. A tooltip helper.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_input = html.HtmlInput.FieldAutocomplete(
      self.page, value, label, placeholder, icon, width, height, html_code, helper, options or {}, profile)
    return html_input

  @html.Html.css_skin()
  def static(self, value="", label=None, placeholder="", icon=None, width=(100, "%"), height=(None, "px"),
             html_code=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

      page.ui.fields.static(label="readonly field")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldInput`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/fields.py

    Attributes:
    ----------
    :param value: String. Optional. The value to be displayed to this component. Default empty string.
    :param label: String. Optional. The text of label to be added to the component.
    :param placeholder: String. Optional. The text to be displayed when the input is empty.
    :param icon: String. Optional. The component icon content from font-awesome references.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: String. Optional. A tooltip helper.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_input = html.HtmlInput.FieldInput(
      self.page, value, label, placeholder, icon, width, height, html_code, helper, options or {}, profile)
    html_input.input.readonly(True)
    return html_input

  @html.Html.css_skin()
  def hidden(self, value="", label=None, placeholder="", icon=None, width=(100, "%"), height=(None, "px"),
             html_code=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------
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

    Attributes:
    ----------
    :param value: String. Optional. The value to be displayed to this component. Default empty string.
    :param label: String. Optional. The text of label to be added to the component.
    :param placeholder: String. Optional. The text to be displayed when the input is empty.
    :param icon: String. Optional. The component icon content from font-awesome references.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: String. Optional. A tooltip helper.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_input = html.HtmlInput.FieldInput(
      self.page, value, label, placeholder, icon, width, height, html_code, helper, options or {}, profile)
    html_input.input.readonly(True)
    html_input.style.css.display = False
    return html_input

  @html.Html.css_skin()
  def integer(self, value="", label=None, placeholder="", icon=None, width=(100, "%"), height=(None, "px"),
              html_code=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

      page.ui.fields.integer(label="test")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldInteger`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/fields.py

    Attributes:
    ----------
    :param value: String. Optional. The value to be displayed to this component. Default empty string.
    :param label: String. Optional. The text of label to be added to the component.
    :param placeholder: String. Optional. The text to be displayed when the input is empty.
    :param icon: String. Optional. The component icon content from font-awesome references.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: String. Optional. A tooltip helper.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_input = html.HtmlInput.FieldInteger(
      self.page, value, label, placeholder, icon, width, height, html_code, helper, options or {}, profile)
    return html_input

  @html.Html.css_skin()
  def file(self, value="", label=None, placeholder="", icon=None, width=(100, "%"), height=(None, "px"),
           html_code=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

      page.ui.fields.integer(label="test")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldFile`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/fields.py

    Attributes:
    ----------
    :param value: String. Optional. The value to be displayed to this component. Default empty string.
    :param label: String. Optional. The text of label to be added to the component.
    :param placeholder: String. Optional. The text to be displayed when the input is empty.
    :param icon: String. Optional. The component icon content from font-awesome references.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: String. Optional. A tooltip helper.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    self.page.css.customText(
      '::-webkit-file-upload-button {border: 1px solid %(c)s; background: %(c)s; color: %(fc)s; font-family: %(fm)s; font-sie: %(size)spx}' % {
        "c": self.page.theme.notch(4), "fc": self.page.theme.white,
        "fm": self.page.body.style.globals.font.family, "size": self.page.body.style.globals.font.size})
    html_input = html.HtmlInput.FieldFile(
      self.page, value, label, placeholder, icon, width, height, html_code, helper, options or {}, profile)
    return html_input

  @html.Html.css_skin()
  def password(self, value="", label=None, placeholder="", icon=None, width=(100, "%"), height=(None, "px"),
               html_code=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

      page.ui.fields.password(label="password")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldPassword`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/fields.py

    Attributes:
    ----------
    :param value: String. Optional. The value to be displayed to this component. Default empty string.
    :param label: String. Optional. The text of label to be added to the component.
    :param placeholder: String. Optional. The text to be displayed when the input is empty.
    :param icon: String. Optional. The component icon content from font-awesome references.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: String. Optional. A tooltip helper.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_input = html.HtmlInput.FieldPassword(
      self.page, value, label, placeholder, icon, width, height, html_code, helper, options or {}, profile)
    return html_input

  @html.Html.css_skin()
  def textarea(self, value="", label=None, placeholder="", icon=None, width=(100, "%"), height=(None, "px"),
               html_code=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

      page.ui.fields.textarea(label="Date")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldTextArea`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/fields.py

    Attributes:
    ----------
    :param value: String. Optional. The value to be displayed to this component. Default empty string.
    :param label: String. Optional. The text of label to be added to the component.
    :param placeholder: String. Optional. The text to be displayed when the input is empty.
    :param icon: String. Optional. The component icon content from font-awesome references.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: String. Optional. A tooltip helper.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_input = html.HtmlInput.FieldTextArea(
      self.page, value, label, placeholder, icon, width, height, html_code, helper, options or {}, profile)
    return html_input

  @html.Html.css_skin()
  def checkbox(self, value=False, label=None, icon=None, width=(100, "%"), height=(None, "px"), html_code=None,
               helper=None, options=None, profile=None):
    """
    Description:
    ------------

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

    Attributes:
    ----------
    :param value: String. Optional. The value to be displayed to this component. Default empty string.
    :param label: String. Optional. The text of label to be added to the component.
    :param icon: String. Optional. The component icon content from font-awesome references.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: String. Optional. A tooltip helper.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_input = html.HtmlInput.FieldCheckBox(
      self.page, value, label, icon, width, height, html_code, helper, options or {}, profile)
    return html_input

  @html.Html.css_skin()
  def radio(self, value=False, label=None, group_name=None, icon=None, width=(100, "%"), height=(None, "px"),
            html_code=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------
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

    Attributes:
    ----------
    :param value: String. Optional. The value to be displayed to this component. Default False.
    :param label: String. Optional. The text of label to be added to the component.
    :param group_name: String. Optional. Group different radio together to only have 1 value selected.
    :param icon: String. Optional. The component icon content from font-awesome references.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: String. Optional. A tooltip helper.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_input = html.HtmlInput.Radio(self.page, value, label, group_name, icon, width, height, html_code,
                                      helper, options or {}, profile)
    html_input.label.css({"width": '100px', 'float': 'left'})
    html_input.css({"display": 'inline-block'})
    return html_input

  @html.Html.css_skin()
  def range(self, value="", min=0, max=100, step=1, label=None, placeholder="", icon=None, width=(100, "%"),
            height=(None, "px"), html_code=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------
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

    Attributes:
    ----------
    :param value: String. Optional. The value to be displayed to this component. Default empty string.
    :param min:
    :param max:
    :param step:
    :param label:
    :param placeholder:
    :param icon:
    :param width:
    :param height:
    :param html_code:
    :param helper:
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_input = html.HtmlInput.FieldRange(self.page, value, min, max, step, label, placeholder, icon, width,
                                           height, html_code, helper, options or {}, profile)
    return html_input

  @html.Html.css_skin()
  def select(self, value=False, label=None, icon=None, selected=None, width=(100, "%"), height=(None, "px"),
             html_code=None, helper=None, options=None, multiple=False, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

      page.ui.fields.select(["a", "b"], label="Check")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldSelect`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/fields.py

    Attributes:
    ----------
    :param value: Boolean. Optional. The value to be displayed to the component. Default False.
    :param label: String. Optional. The text of label to be added to the component.
    :param icon: String. Optional. The component icon content from font-awesome references.
    :param selected: String. Optional. The selected value.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: String. Optional. A tooltip helper.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param multiple: Boolean. Optional. Flag to specify the number of items to be selectable.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    options = options or {}
    if options is not None and 'align' in options:
      self.page.css.customText('.filter-option-inner-inner {text-align: %s}' % options['align'])
    html_input = html.HtmlInput.FieldSelect(self.page, value, label, icon, width, height, html_code,
                                            helper, options or {}, profile)
    if multiple:
      html_input.input.attr['multiple'] = None
    html_input.input.attr['data-width'] = '%spx' % options.get('width', html.Defaults.INPUTS_MIN_WIDTH)
    html_input.input.button_css = {"background": self.page.theme.notch(4), "color": self.page.theme.white, "border-radius": 0}
    if width[0] == "auto":
      html_input.style.css.display = "inline-block"
    if selected is not None:
      html_input.input.options.selected = selected
    return html_input

  @html.Html.css_skin()
  def months(self, value=None, label=None, icon=None, width=(100, "%"), height=(None, "px"), html_code=None,
             helper=None, options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

      page.ui.fields.select(["a", "b"], label="Check")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldSelect`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/fields.py

    Attributes:
    ----------
    :param value: String. Optional. The value to be displayed to this component.
    :param label:
    :param icon:
    :param width:
    :param height:
    :param html_code:
    :param helper:
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
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
    html_input = html.HtmlInput.FieldSelect(self.page, values, label, icon, width, height, html_code, helper,
                                            options or {}, profile)
    html_input.input.attr['data-width'] = '%spx' % html.Defaults.INPUTS_MIN_WIDTH
    if html_input.input.options.selected is None:
      html_input.input.options.selected = value
    return html_input

  @html.Html.css_skin()
  def weeks(self, value=None, label=None, icon=None, width=(100, "%"), height=(None, "px"), html_code=None,
            helper=None, options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

      page.ui.fields.select(["a", "b"], label="Check")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldSelect`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/fields.py

    Attributes:
    ----------
    :param value: String. Optional. The value to be displayed to this component.
    :param label:
    :param icon:
    :param width:
    :param height:
    :param html_code:
    :param helper:
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
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
    html_input = html.HtmlInput.FieldSelect(self.page, values, label, icon, width, height, html_code, helper,
                                            options or {}, profile)
    html_input.input.attr['data-width'] = '%spx' % html.Defaults.INPUTS_MIN_WIDTH
    if html_input.input.options.selected is None:
      html_input.input.options.selected = value
    return html_input

  @html.Html.css_skin()
  def years(self, value=None, label=None, icon=None, width=(100, "%"), height=(None, "px"), html_code=None,
            helper=None, options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage:
    -----

      page.ui.fields.select(["a", "b"], label="Check")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldSelect`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/fields.py

    Attributes:
    ----------
    :param value: String. Optional. The value to be displayed to this component.
    :param label:
    :param icon:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param html_code:
    :param helper:
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dt = datetime.datetime.today()
    if value is None:
      value = dt.year
    if options is not None and 'align' in options:
      self.page.css.customText('.filter-option-inner-inner {text-align: %s}' % options['align'])
    values = [{"name": i, 'value': i} for i in range(dt.year+1)][::-1]
    html_input = html.HtmlInput.FieldSelect(self.page, values, label, icon, width, height, html_code, helper,
                                            options or {}, profile)
    html_input.input.attr['data-width'] = '%spx' % html.Defaults.INPUTS_MIN_WIDTH
    if html_input.input.options.selected is None:
      html_input.input.options.selected = value
    return html_input

  @html.Html.css_skin()
  def days(self, value=None, label=None, icon=None, width=(100, "%"), height=(None, "px"), html_code=None,
           helper=None, options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

      page.ui.fields.select(["a", "b"], label="Check")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldSelect`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/fields.py

    Attributes:
    ----------
    :param value: String. Optional. The value to be displayed to this component.
    :param label:
    :param icon:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param helper:
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
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
    html_input = html.HtmlInput.FieldSelect(self.page, values, label, icon, width, height, html_code, helper,
                                            options or {}, profile)
    html_input.input.attr['data-width'] = '%spx' % html.Defaults.INPUTS_MIN_WIDTH
    if html_input.input.options.selected is None:
      html_input.input.options.selected = value
    return html_input

  @html.Html.css_skin()
  def column_text(self, label, text="", align='left', width=('auto', ""), height=(None, "px"), html_code=None,
                  options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Attributes:
    ----------
    :param label:
    :param text:
    :param align:
    :param width:
    :param height:
    :param html_code:
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    div = self.page.ui.div(align=align, width=width, height=height, options=options, profile=profile)
    div.label = self.page.ui.text(
      label, options=options, html_code=html_code if html_code is None else "%s_label" % html_code, profile=profile)
    div.label.style.css.display = 'block'
    div.label.style.css.margin_bottom = 10
    div.label.style.css.color = self.page.theme.greys[6]
    div.text = self.page.ui.inputs.input(text, options=options, html_code=html_code, profile=profile)
    div.text.style.css.bold()
    div.text.style.css.margin_bottom = 10
    div.text.style.css.display = 'block'
    div.text.style.css.font_factor(5)
    div.style.css.margin = 4
    div.style.css.display = 'inline-block'
    div.add(div.label)
    div.add(div.text)
    return div

  @html.Html.css_skin()
  def column_date(self, label, value="T", align='left', width=('auto', ""), height=(None, "px"), html_code=None,
                  options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Attributes:
    ----------
    :param label:
    :param value: String. Optional. The value to be displayed to this component. Default T.
    :param align:
    :param width:
    :param height:
    :param html_code:
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    div = self.page.ui.div(align=align, width=width, height=height, options=options, profile=profile)
    div.label = self.page.ui.text(
      label, options=options, html_code=html_code if html_code is None else "%s_label" % html_code, profile=profile)
    div.label.style.css.display = 'block'
    div.label.style.css.margin_bottom = 10
    div.label.style.css.color = self.page.theme.greys[6]
    if value is None:
      div.text = self.date(value, options=options, html_code=html_code, profile=profile)
    else:
      div.text = self.today(options=options, html_code=html_code, profile=profile)
    div.text.style.css.bold()
    div.text.style.css.margin_bottom = 10
    div.text.style.css.display = 'block'
    div.text.style.css.font_factor(5)
    div.style.css.margin = 4
    div.style.css.display = 'inline-block'
    div.add(div.label)
    div.add(div.text)
    return div

  @html.Html.css_skin()
  def toggle(self, record=None, label=None, is_on=False, color=None, width=(100, '%'), height=(20, 'px'),
             html_code=None, options=None, profile=None):
    """
    Description:
    ------------
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

    Attributes:
    ----------
    :param record: List. Optional. The list of dictionaries with the data.
    :param label: String. Optional. The toggle static label displayed.
    :param is_on:
    :param color: String. Optional. String. Optional. The font color in the component. Default inherit.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    record = record or {"off": "Off", "on": "On"}
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"is_on": is_on}
    if options is not None:
      dfl_options.update(options)
    div = self.page.ui.div(width=width, height=height, options=dfl_options, profile=profile)
    div.input = html.HtmlRadio.Switch(self.page, record, color, ("auto", ''), height, html_code, dfl_options, profile)
    if label is not None:
      div.input.style.css.display = 'inline-block'
      div.label = self.page.ui.text(
        label, options=options, html_code=html_code if html_code is None else "%s_label" % html_code, profile=profile)
      div.label.style.css.display = 'inline-block'
      div.label.style.css.margin = '0 5px'
      div.label.style.css.width = '%spx' % Defaults.TEXTS_SPAN_WIDTH
      div.extend([div.label, div.input])
    return div

  @html.Html.css_skin()
  def slider(self, value=0, min=0, max=10, step=1, orientation='horizontal', label=None, width=(100, '%'),
             height=(None, 'px'), html_code=None, options=None, range=False, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param value: String. Optional. The value to be displayed to this component. Default 0.
    :param min: Number. Optional.
    :param max: Number. Optional.
    :param step: Number. Optional.
    :param orientation: String. Optional.
    :param label: String. Optional. The toggle static label displayed.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param range:
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dfl_options = {"show_min_max": False, "force_show_current": True}
    if options is not None:
      dfl_options.update(options)
    div = self.page.ui.div(width=width, height=height, options=dfl_options, profile=profile)
    if range:
      div.input = self.page.ui.sliders.range(
        values=value, minimum=min, maximum=max, width=(Defaults.INPUTS_MIN_WIDTH, 'px'), height=None,
        html_code=html_code, options=dfl_options)
    else:
      div.input = self.page.ui.slider(number=value, minimum=min, maximum=max, width=(Defaults.INPUTS_MIN_WIDTH, 'px'),
                                      height=None, html_code=html_code, options=dfl_options)
    div.input.style.css.margin = 0
    div.style.css.margin_top = 5
    div.input.options.step = step
    if label is not None:
      div.input.style.css.display = 'inline-block'
      div.label = self.page.ui.text(
        label, options=options, html_code=html_code if html_code is None else "%s_label" % html_code, profile=profile)
      div.label.style.css.display = 'inline-block'
      div.label.style.css.margin = '0 5px'
      div.label.style.css.width = '%spx' % Defaults.TEXTS_SPAN_WIDTH
      div.extend([div.label, div.input])
    if orientation == "vertical":
      div.input.style.css.height = div.input.style.css.width
      div.input.style.css.width = div.input.style.css.height
      div.input.options.css = {"width": "5px", "background": "#bdbdbd"}
      div.input.options.handler_css = {
        "left": "-7px", "border-radius": '60px', "border": "1px solid grey", "background": "white"}
    else:
      div.input.style.css.line_height = height[0]
      div.input.options.css = {"height": "5px", "background": "#bdbdbd"}
      div.input.options.handler_css = {
        "top": "-7px", "border-radius": '60px', "border": "1px solid grey", "background": "white"}
    div.input.options.orientation = orientation
    return div

  @html.Html.css_skin()
  def filters(self, items=None, button=None, width=("auto", ""), height=(60, "px"), html_code=None, helper=None,
              options=None, autocomplete=False, kind='select', profile=None):
    if kind == 'select':
      comp = self.page.ui.lists.filters(items, button, width, height, html_code, helper, options, autocomplete, profile)
      comp.select.button_css = {
        "background": self.page.theme.notch(4), "color": self.page.theme.white, "border-radius": 0}
    elif kind == 'input':
      comp = self.page.ui.inputs.filters(items, button, width, height, html_code, helper, options, autocomplete, profile)
    else:
      raise Exception("Kind %s not defined" % kind)

    return comp


class Timelines:

  def __init__(self, ui):
    self.page = ui.page

  @html.Html.css_skin()
  def view(self, start_date, end_date, width=(100, "%"), height=(None, "px"), options=None, profile=None):
    """
    Description:
    -----------

    :tags:
    :categories:

    Usage::


    Attributes:
    ----------
    :param start_date:
    :param end_date:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
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
    div = self.page.ui.div("%s - %s" % (
      start_date.strftime("%b %d"), end_date.strftime("%b %d")), width=width, height=height, options=options,
                           profile=profile)
    div.style.css.background = self.page.theme.colors[1]
    div.style.css.border_radius = 20
    div.style.css.padding = 2
    div.style.css.text_align = 'center'
    div.tooltip("%s days remaining" % remaining_days)
    if end_date < today:
      div.style.css.background = self.page.theme.greys[6]
      div.style.css.color = self.page.theme.greys[0]
    return div

  @html.Html.css_skin()
  def period(self, start_date, days, width=(100, "%"), height=(None, "px"), options=None, profile=None):
    """
    Description:
    -----------

    :tags:
    :categories:

    Usage::


    Attributes:
    ----------
    :param start_date:
    :param days:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
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
    div = self.page.ui.div("%s - %s" % (
      start_date.strftime("%b %d"), end_date.strftime("%b %d")), width=width, height=height, options=options,
                           profile=profile)
    div.style.css.background = self.page.theme.colors[1]
    div.style.css.border_radius = 20
    div.style.css.padding = 2
    div.style.css.text_align = 'center'
    div.tooltip("%s days remaining" % remaining_days)
    if end_date < today:
      div.style.css.background = self.page.theme.greys[6]
      div.style.css.color = self.page.theme.greys[0]
    return div

  @html.Html.css_skin()
  def week(self, start_date, width=(100, "%"), height=(None, "px"), options=None, profile=None):
    """
    Description:
    -----------

    :tags:
    :categories:

    Usage::


    Attributes:
    ----------
    :param start_date:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
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
    div = self.page.ui.div("%s - %s" % (
      start_date.strftime("%b %d"), end_date.strftime("%b %d")), width=width, height=height, options=options,
                           profile=profile)
    div.style.css.background = self.page.theme.colors[1]
    div.style.css.border_radius = 20
    div.style.css.padding = 2
    div.style.css.text_align = 'center'
    div.tooltip("%s days remaining" % remaining_days)
    return div

  @html.Html.css_skin()
  def categories(self, value=None, label=None, icon=None, width=(100, "%"), height=(None, "px"), html_code=None,
                 helper=None, options=None, profile=None):
    """
    Description:
    -----------

    :tags:
    :categories:

    Usage::


    Attributes:
    ----------
    :param value:
    :param label:
    :param icon:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
    :param html_code:
    :param helper:
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    values = cpn.select.from_list(["Documentation", 'Analysis', 'Design', 'Implementation', 'Training'])
    html_input = html.HtmlInput.FieldSelect(self.page, values, label, icon, width, height, html_code, helper,
                                            options or {}, profile)
    if html_input.input.options.selected is None:
      html_input.input.selected = value
    return html_input

  @html.Html.css_skin()
  def milestone(self, completion_date, icon=None, width=(25, 'px'), height=(25, 'px'), html_code=None, options=None,
                profile=None):
    """
    Description:
    -----------

    :tags:
    :categories:

    Usage::


    Attributes:
    ----------
    :param completion_date:
    :param icon:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code:
    :param options: Dictionary. Optional. Specific Python options available for this component
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    today, remaining_days = datetime.datetime.now(), 0
    if not isinstance(completion_date, datetime.datetime):
      completion_date = datetime.datetime(*[int(x) for x in completion_date.split("-")])
    if icon is None:
      icon = "fas fa-fire-alt"
    ms = self.page.ui.icons.awesome(
      icon, width=width, height=height, html_code=html_code, options=options, profile=profile)
    if completion_date > today:
      next_day = today
      while next_day < completion_date:
        if next_day.weekday() in [6, 5]:
          next_day += datetime.timedelta(days=1)
          continue

        remaining_days += 1
        next_day += datetime.timedelta(days=1)
      ms.tooltip("to be completed in %s (%s days left)" % (completion_date.strftime("%b %d"), remaining_days))
      ms.icon.style.css.color = self.page.theme.danger[1]
    else:
      ms.tooltip("Completed in %s" % completion_date.strftime("%b %d"))
      ms.icon.style.css.color = self.page.theme.greys[6]
    return ms

  @html.Html.css_skin()
  def meeting(self, time, icon=None, width=(25, 'px'), height=(25, 'px'), html_code=None, options=None, profile=None):
    """
    Description:
    -----------

    :tags:
    :categories:

    Usage::


    Attributes:
    ----------
    :param time:
    :param icon:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code:
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    dflt_options = {"working_hours": 8}
    if options is not None:
      dflt_options.update(options)
    if icon is None:
      icon = "far fa-handshake"
    ms = self.page.ui.icons.awesome(icon, width=width, height=height, html_code=html_code, profile=profile)
    ms.tooltip("%s hours (%s days)" % (time, time / dflt_options["working_hours"]))
    return ms

  @html.Html.css_skin()
  def workload(self, value, width=(25, 'px'), html_code=None, options=None, profile=None):
    """
    Description:
    -----------

    :tags:
    :categories:

    Usage::


    Attributes:
    ----------
    :param value: Float. The workload percentage.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    dflt_options = {"working_hours": 8}
    if options is not None:
      dflt_options.update(options)
    width = (width[0] * (value / dflt_options["working_hours"]), 'px')
    height = width
    ms = self.page.ui.div(value, width=width, height=height, html_code=html_code, profile=profile)
    ms.style.css.border_radius = 20
    ms.style.css.text_align = "center"
    ms.style.css.color = "white"
    ms.style.css.line_height = "%s%s" % (height[0], height[1])
    ms.style.css.vertical_align = "middle"
    if value < (dflt_options["working_hours"] - 2):
      ms.style.css.background = self.page.theme.success[1]
    elif value < dflt_options["working_hours"]:
      ms.style.css.background = self.page.theme.warning[1]
    else:
      ms.style.css.background = self.page.theme.danger[1]
    return ms
