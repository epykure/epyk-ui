
import datetime

# Check if pandas is available in the current environment
# if it is the case this module can handle DataFrame directly
try:
  import pandas as pd
  has_pandas = True

except:
  has_pandas = False


from epyk.core import html


class Fields(object):
  def __init__(self, context):
    self.context = context

  def date(self, value, label=None, icon="far fa-calendar-alt", color=None, width=(None, "px"), height=(None, "px"), htmlCode=None,
            profile=None, options=None, helper=None):
    """
    Description:
    ------------
    This component is based on the Jquery Date Picker object.

    Usage::

      rptObj.ui.fields.date('2020-04-08', label="Date").included_dates(["2020-04-08", "2019-09-06"])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlDates.DatePicker`

    Related Pages:

			https://jqueryui.com/datepicker/

    Attributes:
    ----------
    :param value: Optional. The value to be displayed to the time component. Default now
    :param label: Optional. The text of label to be added to the component
    :param icon: Optional. The component icon content from font-awesome references
    :param color: Optional. The font color in the component. Default inherit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    :param helper: Optional. A tooltip helper
    """
    dftl_options = {'dateFormat': 'yy-mm-dd'}
    if options is not None:
      dftl_options.update(options)
    html_dt = html.HtmlDates.DatePicker(self.context.rptObj, value, label, icon, width, height, color, htmlCode, profile, dftl_options, helper)
    return html_dt

  def today(self, label=None, icon="far fa-calendar-alt", color=None, width=(None, "px"), height=(None, "px"), htmlCode=None,
            profile=None, options=None, helper=None):
    """
    Description:
    ------------
    This component is based on the Jquery Date Picker object.

    Usage::

      rptObj.ui.fields.today(label="Date").included_dates(["2019-09-01", "2019-09-06"])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlDates.DatePicker`

    Related Pages:

			https://jqueryui.com/datepicker/

    Attributes:
    ----------
    :param label: Optional. The text of label to be added to the component
    :param icon: Optional. The component icon content from font-awesome references
    :param color: Optional. The font color in the component. Default inherit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    :param helper: Optional. A tooltip helper
    """
    dftl_options = {'dateFormat': 'yy-mm-dd'}
    if options is not None:
      dftl_options.update(options)
    value = self.context.rptObj.py.dates.today
    html_dt = html.HtmlDates.DatePicker(self.context.rptObj, value, label, icon, width, height, color, htmlCode, profile, dftl_options, helper)
    return html_dt

  def cob(self, label=None, icon="far fa-calendar-alt", color=None, width=(None, "px"), height=(None, "px"), htmlCode=None,
          profile=None, options=None, helper=None):
    """
    Description:
    ------------
    This component is based on the Jquery Date Picker object.

    Usage::

      rptObj.ui.fields.cob(label="COB Date")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlDates.DatePicker`

    Related Pages:

			https://jqueryui.com/datepicker/

    Attributes:
    ----------
    :param label: Optional. The text of label to be added to the component
    :param icon: Optional. The component icon content from font-awesome references
    :param color: Optional. The font color in the component. Default inherit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    :param filters: Optional. The filtering properties for this component
    :param helper: Optional. A tooltip helper
    """
    dftl_options = {'dateFormat': 'yy-mm-dd'}
    if options is not None:
      dftl_options.update(options)
    value = self.context.rptObj.py.dates.cob
    html_cob = html.HtmlDates.DatePicker(self.context.rptObj, value, label, icon, width, height, color, htmlCode, profile, dftl_options, helper)
    return html_cob

  def now(self, deltatime=0, label=None, icon="far fa-clock", color=None, htmlCode=None, profile=None,
          options=None, helper=None):
    """
    Description:
    ------------
    This component is based on the Jquery Time Picker object.

    Usage::

      rptObj.ui.fields.now(label="timestamp", color="red", helper="This is the report timestamp")
      rptObj.ui.fields.now(label="Time field")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlDates.TimePicker`

    Related Pages:

			https://github.com/jonthornton/jquery-timepicker

    Attributes:
    ----------
    :param label: Optional. The text of label to be added to the component
    :param icon: Optional. The component icon content from font-awesome references
    :param color: Optional. The font color in the component. Default inherit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    :param helper: Optional. A tooltip helper
    """
    date = datetime.datetime.now() + datetime.timedelta(minutes=deltatime)
    html_dt = html.HtmlDates.TimePicker(self.context.rptObj, str(date).split(" ")[1].split(".")[0], label, icon, color,
                                        htmlCode, profile, options or {}, helper)
    return html_dt

  def time(self, value=None, label=None, icon="far fa-clock", color=None, htmlCode=None, profile=None, options=None, helper=None):
    """
    Description:
    ------------
    This component is based on the Jquery Time Picker object.

    Usage::

      rptObj.ui.fields.time(label="timestamp", color="red", helper="This is the report timestamp")
      rptObj.ui.fields.time(label="Time field")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlDates.TimePicker`

    Related Pages:

			https://github.com/jonthornton/jquery-timepicker

    Attributes:
    ----------
    :param value: Optional. The value to be displayed to the time component. Default now
    :param label: Optional. The text of label to be added to the component
    :param icon: Optional. The component icon content from font-awesome references
    :param color: Optional. The font color in the component. Default inherit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    :param helper: Optional. A tooltip helper
    """
    html_dt = html.HtmlDates.TimePicker(self.context.rptObj, value, label, icon, color, htmlCode, profile, options or {}, helper)
    return html_dt

  def input(self, value="", label=None, placeholder="", icon=None, width=(100, "%"),
            height=(None, "px"), htmlCode=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::

      rptObj.ui.fields.input("", label="Range Example", icon="fas fa-unlock-alt")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldInput`

    Attributes:
    ----------
    :param value:
    :param label:
    :param placeholder:
    :param icon:
    :param width:
    :param height:
    :param htmlCode:
    :param profile:
    """
    html_input = html.HtmlInput.FieldInput(self.context.rptObj, value, label, placeholder, icon, width, height, htmlCode, helper, options, profile)
    return html_input

  def autocomplete(self, value="", label=None, placeholder="", icon=None, width=(100, "%"),
            height=(None, "px"), htmlCode=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::

      rptObj.ui.fields.input("", label="Range Example", icon="fas fa-unlock-alt")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldAutocomplete`

    Attributes:
    ----------
    :param value:
    :param label:
    :param placeholder:
    :param icon:
    :param width:
    :param height:
    :param htmlCode:
    :param profile:
    """
    html_input = html.HtmlInput.FieldAutocomplete(self.context.rptObj, value, label, placeholder, icon, width, height, htmlCode, helper, options, profile)
    return html_input

  def static(self, value="", label=None, placeholder="", icon=None, width=(100, "%"), height=(None, "px"), htmlCode=None,
             helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::

      rptObj.ui.fields.static(label="readonly field")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldInput`

    Attributes:
    ----------
    :param value:
    :param label:
    :param placeholder:
    :param icon:
    :param width:
    :param height:
    :param htmlCode:
    :param profile:
    """
    html_input = html.HtmlInput.FieldInput(self.context.rptObj, value, label, placeholder, icon, width, height, htmlCode, helper, options, profile)
    html_input.input.readonly(True)
    return html_input

  def hidden(self, value="", label=None, placeholder="", icon=None, width=(100, "%"), height=(None, "px"), htmlCode=None,
             helper=None, options=None, profile=None):
    """
    Description:
    ------------
    Create a hidden HTML component.
    This is used to store values which are not visible on the page.

    Usage::

      rptObj.ui.fields.hidden(label="readonly field")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldInput`

    Attributes:
    ----------
    :param value:
    :param label:
    :param placeholder:
    :param icon:
    :param width:
    :param height:
    :param htmlCode:
    :param profile:
    """
    html_input = html.HtmlInput.FieldInput(self.context.rptObj, value, label, placeholder, icon, width, height, htmlCode, helper, options, profile)
    html_input.input.readonly(True)
    html_input.style.css.display = False
    return html_input

  def integer(self, value="", label=None, placeholder="", icon=None, width=(100, "%"),
              height=(None, "px"), htmlCode=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::

      rptObj.ui.fields.integer(label="test")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldInteger`

    Attributes:
    ----------
    :param value:
    :param label:
    :param placeholder:
    :param icon:
    :param width:
    :param height:
    :param htmlCode:
    :param profile:
    """
    html_input = html.HtmlInput.FieldInteger(self.context.rptObj, value, label, placeholder, icon, width, height, htmlCode, helper, options, profile)
    return html_input

  def file(self, value="", label=None, placeholder="", icon=None, width=(100, "%"),
              height=(None, "px"), htmlCode=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::

      rptObj.ui.fields.integer(label="test")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldFile`

    Attributes:
    ----------
    :param value:
    :param label:
    :param placeholder:
    :param icon:
    :param width:
    :param height:
    :param htmlCode:
    :param profile:
    """
    html_input = html.HtmlInput.FieldFile(self.context.rptObj, value, label, placeholder, icon, width, height, htmlCode, helper, options, profile)
    return html_input

  def password(self, value="", label=None, placeholder="", icon=None, width=(100, "%"),
              height=(None, "px"), htmlCode=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::

      rptObj.ui.fields.password(label="password")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldPassword`

    Attributes:
    ----------
    :param value:
    :param label:
    :param placeholder:
    :param icon:
    :param width:
    :param height:
    :param htmlCode:
    :param profile:
    """
    html_input = html.HtmlInput.FieldPassword(self.context.rptObj, value, label, placeholder, icon, width, height,
                                              htmlCode, helper, options, profile)
    return html_input

  def textarea(self, value="", label=None, placeholder="", icon=None, width=(100, "%"),
              height=(None, "px"), htmlCode=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::

      rptObj.ui.fields.textarea(label="Date")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldTextArea`

    Attributes:
    ----------
    :param value:
    :param label:
    :param placeholder:
    :param icon:
    :param width:
    :param height:
    :param htmlCode:
    :param profile:
    """
    html_input = html.HtmlInput.FieldTextArea(self.context.rptObj, value, label, placeholder, icon, width, height,
                                              htmlCode, helper, options, profile)
    return html_input

  def checkbox(self, value=False, label=None, icon=None, width=(100, "%"), height=(None, "px"),
               htmlCode=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::

      rptObj.ui.fields.checkbox(True, label="Check")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldCheckBox`

    Related Pages:

			https://www.w3schools.com/tags/att_input_type_checkbox.asp

    Attributes:
    ----------
    :param value:
    :param label:
    :param icon:
    :param width:
    :param height:
    :param htmlCode:
    :param profile:
    """
    html_input = html.HtmlInput.FieldCheckBox(self.context.rptObj, value, label, icon, width, height, htmlCode, helper, options, profile)
    return html_input

  def radio(self, value=False, label=None, group_name=None, icon=None, width=(100, "%"),
              height=(None, "px"), htmlCode=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------
    The <input type="radio"> defines a radio button.
    Radio buttons are normally presented in radio groups (a collection of radio buttons describing a set of related options).
    Only one radio button in a group can be selected at the same time.

    Usage::

      rptObj.ui.inputs.radio(False, label="radio")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.Radio`

    Related Pages:

			https://www.w3schools.com/tags/att_input_type_radio.asp

    Attributes:
    ----------
    :param value:
    :param label:
    :param group_name:
    :param icon:
    :param width:
    :param height:
    :param htmlCode:
    :param profile:
    """
    html_input = html.HtmlInput.Radio(self.context.rptObj, value, label, group_name, icon, width, height, htmlCode, helper, options, profile)
    html_input.label.css({"width": '100px', 'float': 'left'})
    html_input.css({"display": 'inline-block'})
    return html_input

  def range(self, value="", min=0, max=100, step=1, label=None, placeholder="", icon=None, width=(100, "%"),
              height=(None, "px"), htmlCode=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------
    The <input type="range"> defines a control for entering a number whose exact value is not important (like a slider control).
    Default range is 0 to 100. However, you can set restrictions on what numbers are accepted with the attributes below.
    - max - specifies the maximum value allowed
    - min - specifies the minimum value allowed
    - step - specifies the legal number intervals
    - value - Specifies the default value

    Usage::

      rptObj.ui.fields.range(54, min=20, label="Range Example", icon="fas fa-unlock-alt")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldRange`

    Related Pages:

			https://www.w3schools.com/tags/att_input_type_range.asp

    Attributes:
    ----------
    :param value:
    :param min:
    :param max:
    :param step:
    :param label:
    :param placeholder:
    :param icon:
    :param width:
    :param height:
    :param htmlCode:
    :param profile:
    """
    html_input = html.HtmlInput.FieldRange(self.context.rptObj, value, min, max, step, label, placeholder, icon, width,
                                           height, htmlCode, helper, options, profile)
    return html_input

  def select(self, value=False, label=None, icon=None, width=(100, "%"), height=(None, "px"), htmlCode=None,
             helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::

      rptObj.ui.fields.select(["a", "b"], label="Check")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldSelect`

    Attributes:
    ----------
    :param value:
    :param label:
    :param icon:
    :param width:
    :param height:
    :param htmlCode:
    :param profile:
    """
    if options is not None and 'align' in options:
      self.context.rptObj.css.customText('.filter-option-inner-inner {text-align: %s}' % options['align'])
    html_input = html.HtmlInput.FieldSelect(self.context.rptObj, value, label, icon, width, height, htmlCode, helper, options, profile)
    html_input.input.attr['data-width'] = '%spx' % html.Defaults.INPUTS_MIN_WIDTH
    return html_input

  def months(self, value=None, label=None, icon=None, width=(100, "%"), height=(None, "px"), htmlCode=None,
             helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::

      rptObj.ui.fields.select(["a", "b"], label="Check")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldSelect`

    Attributes:
    ----------
    :param value:
    :param label:
    :param icon:
    :param width:
    :param height:
    :param htmlCode:
    :param profile:
    """
    import calendar

    if value is None:
      dt = datetime.datetime.today()
      value = dt.month
    if options is not None and 'align' in options:
      self.context.rptObj.css.customText('.filter-option-inner-inner {text-align: %s}' % options['align'])
    values = [{"name": calendar.month_name[i], 'value': i} for i in range(12)]
    html_input = html.HtmlInput.FieldSelect(self.context.rptObj, values, label, icon, width, height, htmlCode, helper, options, profile)
    html_input.input.attr['data-width'] = '%spx' % html.Defaults.INPUTS_MIN_WIDTH
    if html_input.input.selected is None:
      html_input.input.selected = value
    return html_input

  def weeks(self, value=None, label=None, icon=None, width=(100, "%"), height=(None, "px"), htmlCode=None,
             helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::

      rptObj.ui.fields.select(["a", "b"], label="Check")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldSelect`

    Attributes:
    ----------
    :param value:
    :param label:
    :param icon:
    :param width:
    :param height:
    :param htmlCode:
    :param profile:
    """
    dt = datetime.datetime.today()
    if value is None:
      value = datetime.datetime.utcnow().isocalendar()[1]
    values = []
    for i in range(52):
      d = "%s-W%s" % (dt.year, i)
      start_date = datetime.datetime.strptime(d + '-1', "%Y-W%W-%w")
      end_date = start_date + datetime.timedelta(days=5)
      values.append({"value": i+1, 'name': "W%s [%s - %s]" % (i+1, start_date.strftime('%d/%m'), end_date.strftime('%d/%m'))})
    if options is not None and 'align' in options:
      self.context.rptObj.css.customText('.filter-option-inner-inner {text-align: %s}' % options['align'])
    html_input = html.HtmlInput.FieldSelect(self.context.rptObj, values, label, icon, width, height, htmlCode, helper, options, profile)
    html_input.input.attr['data-width'] = '%spx' % html.Defaults.INPUTS_MIN_WIDTH
    if html_input.input.selected is None:
      html_input.input.selected = value
    return html_input

  def years(self, value=None, label=None, icon=None, width=(100, "%"), height=(None, "px"), htmlCode=None,
             helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::

      rptObj.ui.fields.select(["a", "b"], label="Check")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldSelect`

    Attributes:
    ----------
    :param value:
    :param label:
    :param icon:
    :param width:
    :param height:
    :param htmlCode:
    :param profile:
    """
    dt = datetime.datetime.today()
    if value is None:
      value = dt.year
    if options is not None and 'align' in options:
      self.context.rptObj.css.customText('.filter-option-inner-inner {text-align: %s}' % options['align'])
    values = [{"name": i, 'value': i} for i in range(dt.year+1)][::-1]
    html_input = html.HtmlInput.FieldSelect(self.context.rptObj, values, label, icon, width, height, htmlCode, helper, options, profile)
    html_input.input.attr['data-width'] = '%spx' % html.Defaults.INPUTS_MIN_WIDTH
    if html_input.input.selected is None:
      html_input.input.selected = value
    return html_input

  def days(self, value=None, label=None, icon=None, width=(100, "%"), height=(None, "px"), htmlCode=None,
             helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::

      rptObj.ui.fields.select(["a", "b"], label="Check")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.FieldSelect`

    Attributes:
    ----------
    :param value:
    :param label:
    :param icon:
    :param width:
    :param height:
    :param htmlCode:
    :param profile:
    """
    import calendar

    if value is None:
      dt = datetime.datetime.today()
      value = dt.weekday()
    if options is not None and 'align' in options:
      self.context.rptObj.css.customText('.filter-option-inner-inner {text-align: %s}' % options['align'])
    values = [{"name": calendar.day_name[i], 'value': i} for i in range(7)]
    html_input = html.HtmlInput.FieldSelect(self.context.rptObj, values, label, icon, width, height, htmlCode, helper, options, profile)
    html_input.input.attr['data-width'] = '%spx' % html.Defaults.INPUTS_MIN_WIDTH
    if html_input.input.selected is None:
      html_input.input.selected = value
    return html_input


class Timelines(object):
  def __init__(self, context):
    self.context = context

  def view(self, start_date, end_date, width=(100, "%"), height=(None, "px"), options=None, profile=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param start_date:
    :param end_date:
    :param width:
    :param height:
    :param options:
    :param profile:
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
    div = self.context.rptObj.ui.div("%s - %s" % (start_date.strftime("%b %d"), end_date.strftime("%b %d")), width=width, height=height, options=options, profile=profile)
    div.style.css.background = self.context.rptObj.theme.colors[1]
    div.style.css.border_radius = 20
    div.style.css.padding = 2
    div.style.css.text_align = 'center'
    div.tooltip("%s days remaining" % remaining_days)
    if end_date < today:
      div.style.css.background = self.context.rptObj.theme.greys[6]
      div.style.css.color = self.context.rptObj.theme.greys[0]
    return div

  def period(self, start_date, days, width=(100, "%"), height=(None, "px"), options=None, profile=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param start_date:
    :param days:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    today, remaining_days = datetime.datetime.now(), 0
    if not isinstance(start_date, datetime.datetime):
      start_date = datetime.datetime(*[int(x) for x in start_date.split("-")])
    end_date = start_date
    for _ in range(days):
      if end_date >= today:
        remaining_days += 1
      if end_date.weekday() == 4:
        # akip weekends
        end_date += datetime.timedelta(days=3)
      else:
        end_date += datetime.timedelta(days=1)
    if end_date >= today:
      remaining_days += 1
    div = self.context.rptObj.ui.div("%s - %s" % (start_date.strftime("%b %d"), end_date.strftime("%b %d")), width=width, height=height, options=options, profile=profile)
    div.style.css.background = self.context.rptObj.theme.colors[1]
    div.style.css.border_radius = 20
    div.style.css.padding = 2
    div.style.css.text_align = 'center'
    div.tooltip("%s days remaining" % remaining_days)
    if end_date < today:
      div.style.css.background = self.context.rptObj.theme.greys[6]
      div.style.css.color = self.context.rptObj.theme.greys[0]
    return div

  def week(self, start_date, width=(100, "%"), height=(None, "px"), options=None, profile=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param start_date:
    :param width:
    :param height:
    :param options:
    :param profile:
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
    div = self.context.rptObj.ui.div("%s - %s" % (start_date.strftime("%b %d"), end_date.strftime("%b %d")), width=width, height=height, options=options, profile=profile)
    div.style.css.background = self.context.rptObj.theme.colors[1]
    div.style.css.border_radius = 20
    div.style.css.padding = 2
    div.style.css.text_align = 'center'
    div.tooltip("%s days remaining" % remaining_days)
    return div

  def categories(self, value=None, label=None, icon=None, width=(100, "%"), height=(None, "px"), htmlCode=None,
                 helper=None, options=None, profile=None):
    values = ["Documentation", 'Analysis', 'Design', 'Implementation', 'Training']
    html_input = html.HtmlInput.FieldSelect(self.context.rptObj, values, label, icon, width, height, htmlCode, helper,
                                            options, profile)
    return html_input

  def milestone(self, completion_date, icon=None, width=(25, 'px'), height=(25, 'px'), htmlCode=None, profile=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param completion_date:
    :param icon:
    :param width:
    :param height:
    :param htmlCode:
    :param profile:
    """
    today, remaining_days = datetime.datetime.now(), 0
    if not isinstance(completion_date, datetime.datetime):
      completion_date = datetime.datetime(*[int(x) for x in completion_date.split("-")])
    if icon is None:
      icon = "fas fa-fire-alt"
    ms = self.context.rptObj.ui.icons.awesome(icon, width=width, height=height, htmlCode=htmlCode, profile=profile)
    if completion_date > today:
      next_day = today
      while next_day < completion_date:
        if next_day.weekday() in [6, 5]:
          next_day += datetime.timedelta(days=1)
          continue

        remaining_days += 1
        next_day += datetime.timedelta(days=1)
      ms.tooltip("to be completed in %s (%s days left)" % (completion_date.strftime("%b %d"), remaining_days))
      ms.icon.style.css.color = self.context.rptObj.theme.danger[1]
    else:
      ms.tooltip("Completed in %s" % completion_date.strftime("%b %d"))
      ms.icon.style.css.color = self.context.rptObj.theme.greys[6]
    return ms

  def meeting(self, time, icon=None, width=(25, 'px'), height=(25, 'px'), htmlCode=None, options=None, profile=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param time:
    :param icon:
    :param width:
    :param height:
    :param htmlCode:
    :param profile:
    """
    dflt_options = {"working_hours": 8}
    if options is not None:
      dflt_options.update(options)
    if icon is None:
      icon = "far fa-handshake"
    ms = self.context.rptObj.ui.icons.awesome(icon, width=width, height=height, htmlCode=htmlCode, profile=profile)
    ms.tooltip("%s hours (%s days)" % (time, time / dflt_options["working_hours"]))
    return ms
