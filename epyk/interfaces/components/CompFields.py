"""

"""

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

  def today(self, value=None, label=None, icon="far fa-calendar-alt", color=None, htmlCode=None,
            profile=None, options=None, filters=None, helper=None):
    """
    Description:
    ------------
    This component is based on the Jquery Date Picker object.

    Usage:
    ------
    rptObj.ui.fields.today(label="Date").selectable(["2019-09-01", "2019-09-06"])

    Related Pages:
    --------------
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
    :param filters: Optional. The filtering properties for this component
    :param helper: Optional. A tooltip helper
    """
    if value is None:
      value = self.context.rptObj.py.dates.today
    html_dt = html.HtmlDates.DatePicker(self.context.rptObj, value, label, icon, color, htmlCode, profile, options or {}, helper)
    self.context.register(html_dt)
    return html_dt

  def cob(self, value=None, label=None, icon="far fa-calendar-alt", color=None, htmlCode=None,
          profile=None, options=None, filters=None, helper=None):
    """
    Description:
    ------------
    This component is based on the Jquery Date Picker object.

    Usage:
    ------
    rptObj.ui.fields.cob(label="Date").selectable(["2019-09-01", "2019-09-06"])
    rptObj.ui.fields.cob(label="COB Date")

    Related Pages:
    --------------
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
    :param filters: Optional. The filtering properties for this component
    :param helper: Optional. A tooltip helper
    """
    if value is None:
      value = self.context.rptObj.py.dates.cob
    html_cob = html.HtmlDates.DatePicker(self.context.rptObj, value, label, icon, color, htmlCode, profile, options or {}, helper)
    self.context.register(html_cob)
    return html_cob

  def now(self, value=None, label=None, icon="far fa-clock", color=None, htmlCode=None, profile=None,
          options=None, filters=None, helper=None):
    """
    Description:
    ------------
    This component is based on the Jquery Time Picker object.

    Usage:
    ------
    rptObj.ui.fields.now(label="timestamp", color="red", helper="This is the report timestamp")
    rptObj.ui.fields.now(label="Time field")

    Related Pages:
    --------------
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
    :param filters: Optional. The filtering properties for this component
    :param helper: Optional. A tooltip helper
    """
    html_dt = html.HtmlDates.TimePicker(self.context.rptObj, value or "", label, icon, color, htmlCode, profile, options or {}, helper)
    self.context.register(html_dt)
    return html_dt

  def input(self, value="", label=None, placeholder="", icon=None, width=(100, "%"),
            height=(None, "px"), htmlCode=None, helper=None, profile=None):
    """
    Description:
    ------------

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
    html_input = html.HtmlInput.FieldInput(self.context.rptObj, value, label, placeholder, icon, width, height, htmlCode, helper, profile)
    self.context.register(html_input)
    return html_input

  def static(self, value="", label=None, placeholder="", icon=None, width=(100, "%"), height=(None, "px"), htmlCode=None,
             helper=None, profile=None):
    """
    Description:
    ------------

    Usage:
    ------
    rptObj.ui.fields.static(label="readonly field")

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
    html_input = html.HtmlInput.FieldInput(self.context.rptObj, value, label, placeholder, icon, width, height, htmlCode, helper, profile)
    html_input.input.readonly(True)
    self.context.register(html_input)
    return html_input

  def integer(self, value="", label=None, placeholder="", icon=None, width=(100, "%"),
              height=(None, "px"), htmlCode=None, helper=None, profile=None):
    """
    Description:
    ------------

    Usage:
    ------
    rptObj.ui.fields.integer(label="test")

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
    html_input = html.HtmlInput.FieldInteger(self.context.rptObj, value, label, placeholder, icon, width, height, htmlCode, helper, profile)
    self.context.register(html_input)
    return html_input

  def password(self, value="", label=None, placeholder="", icon=None, width=(100, "%"),
              height=(None, "px"), htmlCode=None, helper=None, profile=None):
    """
    Description:
    ------------

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
                                              htmlCode, helper, profile)
    self.context.register(html_input)
    return html_input

  def textarea(self, value="", label=None, placeholder="", icon=None, width=(100, "%"),
              height=(None, "px"), htmlCode=None, helper=None, profile=None):
    """
    Description:
    ------------

    Usage:
    ------
    rptObj.ui.fields.textarea(label="Date")

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
                                              htmlCode, helper, profile)
    self.context.register(html_input)
    return html_input

  def checkbox(self, value=False, label=None, icon=None, width=(100, "%"), height=(None, "px"),
               htmlCode=None, helper=None, profile=None):
    """
    Description:
    ------------

    Usage:
    ------
    rptObj.ui.fields.checkbox(True, label="Check")

    Related Pages:
    --------------
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
    html_input = html.HtmlInput.FieldCheckBox(self.context.rptObj, value, label, icon, width, height, htmlCode, helper, profile)
    self.context.register(html_input)
    return html_input

  def radio(self, value=False, label=None, group_name=None, icon=None, width=(100, "%"),
              height=(None, "px"), htmlCode=None, helper=None, profile=None):
    """
    Description:
    ------------
    The <input type="radio"> defines a radio button.
    Radio buttons are normally presented in radio groups (a collection of radio buttons describing a set of related options).
    Only one radio button in a group can be selected at the same time.

    Usage:
    ------

    Related Pages:
    --------------
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
    html_input = html.HtmlInput.Radio(self.context.rptObj, value, label, group_name, icon, width, height, htmlCode, helper, profile)
    html_input.label.css({"width": '100px', 'float': 'left'})
    html_input.css({"display": 'inline-block'})
    self.context.register(html_input)
    return html_input

  def range(self, value="", min=0, max=100, step=1, label=None, placeholder="", icon=None, width=(100, "%"),
              height=(None, "px"), htmlCode=None, helper=None, profile=None):
    """
    Description:
    ------------
    The <input type="range"> defines a control for entering a number whose exact value is not important (like a slider control).
    Default range is 0 to 100. However, you can set restrictions on what numbers are accepted with the attributes below.
    - max - specifies the maximum value allowed
    - min - specifies the minimum value allowed
    - step - specifies the legal number intervals
    - value - Specifies the default value

    Usage:
    ------
    rptObj.ui.fields.range(54, min=20, label="Range Example", icon="fas fa-unlock-alt")

    Related Pages:
    --------------
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
                                           height, htmlCode, helper, profile)
    self.context.register(html_input)
    return html_input

  def select(self, value=False, label=None, icon=None, width=(100, "%"), height=(None, "px"), htmlCode=None,
             helper=None, profile=None):
    """
    Description:
    ------------

    Usage:
    ------
    rptObj.ui.fields.select(["a", "b"], label="Check")

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
    html_input = html.HtmlInput.FieldSelect(self.context.rptObj, value, label, icon, width, height, htmlCode, helper, profile)
    html_input.input.css({"width": "none"})
    self.context.register(html_input)
    return html_input
