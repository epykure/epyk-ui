"""
Interface for all components dealing with dates and times
"""

# Check if pandas is available in the current environment
# if it is the case this module can handle DataFrame directly

try:
  import pandas as pd
  has_pandas = True

except:
  has_pandas = False

import datetime

from epyk.core import html


class Dates(object):
  def __init__(self, context):
    self.context = context

  def today(self, value=None, label=None, icon="far fa-calendar-alt", color=None, size=(None, 'px'), htmlCode=None,
            profile=None, options=None, filters=None, helper=None):
    """

    This component is based on the Jquery Date Picker object.

    Example
    rptObj.ui.dates.today(label="Date").selectable(["2019-09-01", "2019-09-06"])

    Documentation
    https://jqueryui.com/datepicker/

    :param value: Optional. The value to be displayed to the time component. Default now
    :param label: Optional. The text of label to be added to the component
    :param icon: Optional. The component icon content from font-awesome references
    :param color: Optional. The font color in the component. Default inherit
    :param size: Optional. The font size in the component. Default 12px
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    :param filters: Optional. The filtering properties for this component
    :param helper: Optional. A tooltip helper

    :return:

    :rtype: html.HtmlDates.DatePicker

    """
    if value is None:
      lastBusDay = datetime.datetime.today()
    size = self.context._size(size)
    return self.context.register(html.HtmlDates.DatePicker(self.context.rptObj, lastBusDay, label, icon, color, size, htmlCode,
                                                           profile, options or {}, helper))

  def cob(self, value=None, label=None, icon="far fa-calendar-alt", color=None, size=(None, 'px'), htmlCode=None,
          profile=None, options=None, filters=None, helper=None):
    """

    This component is based on the Jquery Date Picker object.

    Example
    rptObj.ui.dates.cob(label="Date").selectable(["2019-09-01", "2019-09-06"])

    Documentation
    https://jqueryui.com/datepicker/

    :param value: Optional. The value to be displayed to the time component. Default now
    :param label: Optional. The text of label to be added to the component
    :param icon: Optional. The component icon content from font-awesome references
    :param color: Optional. The font color in the component. Default inherit
    :param size: Optional. The font size in the component. Default 12px
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    :param filters: Optional. The filtering properties for this component
    :param helper: Optional. A tooltip helper

    :return:

    :rtype: html.HtmlDates.DatePicker
    """
    if value is None:
      lastBusDay = datetime.datetime.today()
      while lastBusDay.weekday() in [5, 6]:
        lastBusDay = lastBusDay - datetime.timedelta(days=1)
    size = self.context._size(size)
    return self.context.register(html.HtmlDates.DatePicker(self.context.rptObj, lastBusDay, label, icon, color, size, htmlCode,
                                                           profile, options or {}, helper))

  def now(self, value=None, label=None, icon="far fa-clock", color=None, size=(None, 'px'), htmlCode=None, profile=None, options=None,
          filters=None, helper=None):
    """

    This component is based on the Jquery Time Picker object.

    Example
    rptObj.ui.dates.now(label="timestamp", color="red", helper="This is the report timestamp")

    Documentation
    https://github.com/jonthornton/jquery-timepicker

    :param value: Optional. The value to be displayed to the time component. Default now
    :param label: Optional. The text of label to be added to the component
    :param icon: Optional. The component icon content from font-awesome references
    :param color: Optional. The font color in the component. Default inherit
    :param size: Optional. The font size in the component. Default 12px
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    :param filters: Optional. The filtering properties for this component
    :param helper: Optional. A tooltip helper

    :rtype: html.HtmlDates.TimePicker

    :return:
    """
    size = self.context._size(size)
    return self.context.register(html.HtmlDates.TimePicker(self.context.rptObj, value, label, icon, color, size, htmlCode,
                                                           profile, options or {}, helper))

  def countdown(self, yyyy_mm_dd, label=None, icon="fas fa-stopwatch", timeInMilliSeconds=1000, width=(100, '%'), height=(None, 'px'),
                htmlCode=None, helper=None, profile=None):
    """
    Add a countdown to the page and remove the content if the page has expired.

    Example
    rptObj.ui.dates.countdown("2019-09-24")

    Documentation
    https://www.w3schools.com/js/js_date_methods.asp
    https://www.w3schools.com/howto/howto_js_countdown.asp
    https://fontawesome.com/icons/stopwatch?style=solid

    :param yyyy_mm_dd: The end date in format YYYY-MM-DD
    :param label: Optional. The component label content
    :param icon: Optional. The component icon content from font-awesome references
    :param timeInMilliSeconds:
    :param width: Optional. Integer for the component width
    :param height: Optional. Integer for the component height
    :param htmlCode: Optional. The component identifier code (for both Python and Javascript)
    :param helper: Optional. A tooltip helper
    :param profile: Optional. A flag to set the component performance storage

    :rtype: html.HtmlDates.CountDownDate

    :return:
    """
    return self.context.register(html.HtmlDates.CountDownDate(self.context.rptObj, yyyy_mm_dd, label, icon, timeInMilliSeconds,
                                                               width, height, htmlCode, helper, profile))

  def update(self, label=None, size=(None, 'px'), color=None, width=(100, "%"), height=(None, "px"), htmlCode=None, profile=None):
    """
    Last Update time component

    Example
    rptObj.ui.dates.update("test")

    :param label: The label to be displayed close to the date. Default Last Update
    :param size: Optional, A integer to set the font-size
    :param color: Optional. The color code for the font
    :param width: Optional. Integer for the component width
    :param height: Optional. Integer for the component height
    :param htmlCode: Optional. The component identifier code (for both Python and Javascript)
    :param profile: Optional. A flag to set the component performance storage

    :rtype: html.HtmlDates.LastUpdated

    :return:
    """
    size = self.context._size(size)
    return self.context.register(html.HtmlDates.LastUpdated(self.context.rptObj, label, size, color, width, height,
                                                            htmlCode, profile))
