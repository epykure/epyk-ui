
from epyk.core.html.options import Options
from epyk.core.html.options import Enums


class EnumFormatTypes(Enums):

  def time_only(self):
    """
    Description:
    ------------
    Display only the time for the component.

    Usage::

      page.web.bs.time()

    Related Pages:

      https://getdatepicker.com/5-4/Usage/#custom-icons
    """
    self._set_value(value="LT")

  def date_only(self):
    """
    Description:
    ------------
    Display only the date for the component.

    Usage::

      page.web.bs.date()

    Related Pages:

      https://getdatepicker.com/5-4/Usage/#custom-icons
    """
    self._set_value(value="L")

  def mm_yyyy(self):
    """
    Description:
    ------------

    Related Pages:

      https://getdatepicker.com/5-4/Usage/#custom-icons
    """
    self._set_value(value="MM/YYY")


class EnumViewMode(Enums):

  def years(self):
    """
    Description:
    ------------

    Related Pages:

      https://getdatepicker.com/5-4/Options/
    """
    self._set_value()

  def decades(self):
    """
    Description:
    ------------

    Related Pages:

      https://getdatepicker.com/5-4/Options/
    """
    self._set_value()

  def months(self):
    """
    Description:
    ------------

    Related Pages:

      https://getdatepicker.com/5-4/Options/
    """
    self._set_value()

  def days(self):
    """
    Description:
    ------------

    Related Pages:

      https://getdatepicker.com/5-4/Options/
    """
    self._set_value()

  def times(self):
    """
    Description:
    ------------

    Related Pages:

      https://getdatepicker.com/5-4/Options/
    """
    self._set_value()


class DTIcons(Options):

  @property
  def time(self):
    """
    Description:
    -----------

    Related Pages:

      https://getdatepicker.com/5-4/Usage/#custom-icons

    """
    return self._config_get()

  @time.setter
  def time(self, text):
    self._config(text)

  @property
  def date(self):
    """
    Description:
    -----------

    https://getdatepicker.com/5-4/Usage/#custom-icons

    """
    return self._config_get()

  @date.setter
  def date(self, text):
    self._config(text)

  @property
  def up(self):
    """
    Description:
    -----------

    https://getdatepicker.com/5-4/Usage/#custom-icons

    """
    return self._config_get()

  @up.setter
  def up(self, text):
    self._config(text)

  @property
  def down(self):
    """
    Description:
    -----------

    https://getdatepicker.com/5-4/Usage/#custom-icons

    """
    return self._config_get()

  @down.setter
  def down(self, text):
    self._config(text)


class DTButtons(Options):

  @property
  def showToday(self):
    """
    Description:
    -----------
    Change the default toolbar buttons for the pickers functions.

    https://getdatepicker.com/5-4/Options/

    """
    return self._config_get()

  @showToday.setter
  def showToday(self, flag):
    self._config(flag)

  @property
  def showClear(self):
    """
    Description:
    -----------
    Change the default toolbar buttons for the pickers functions.

    https://getdatepicker.com/5-4/Options/

    """
    return self._config_get()

  @showClear.setter
  def showClear(self, flag):
    self._config(flag)

  @property
  def showClose(self):
    """
    Description:
    -----------
    Change the default toolbar buttons for the pickers functions.

    https://getdatepicker.com/5-4/Options/

    """
    return self._config_get()

  @showClose.setter
  def showClose(self, flag):
    self._config(flag)


class DT(Options):

  @property
  def allowMultidate(self):
    """
    Description:
    -----------
    Allows the setting of multiple dates.

    Related Pages:

      https://getdatepicker.com/5-4/Usage/#custom-icons
      https://getdatepicker.com/5-4/Options/
    """
    return self._config_get()

  @allowMultidate.setter
  def allowMultidate(self, flag):
    self._config(flag)
    if flag:
      self.multidateSeparator = ","

  @property
  def daysOfWeekDisabled(self):
    """
    Description:
    -----------
    Disables the section of days of the week, e.g. weekends.
    Returns an array with the options.daysOfWeekDisabled configuration setting of the component.

    Related Pages:

      https://getdatepicker.com/5-4/Options/
    """
    return self._config_get()

  @daysOfWeekDisabled.setter
  def daysOfWeekDisabled(self, values):
    self._config(values)

  @property
  def locale(self):
    """
    Description:
    -----------
    See momentjs for valid locales.

    You must include moment-with-locales.js or a local js file.
    Returns the currently set locale of the options.locale

    Related Pages:

      https://getdatepicker.com/5-4/Options/
    """
    return self._config_get()

  @locale.setter
  def locale(self, text):
    self._config(text)

  @property
  def collapse(self):
    """
    Description:
    -----------
    Using a Bootstraps collapse to switch between date/time pickers.
    Returns a boolean of the options.sideBySide.
    Takes a boolean. If set to false the picker will display similar to sideBySide except vertical.

    Related Pages:

      https://getdatepicker.com/5-4/Options/
    """
    return self._config_get(True)

  @collapse.setter
  def collapse(self, flag):
    self._config(flag)

  @property
  def format(self):
    """
    Description:
    -----------
    See momentjs' docs for valid formats. Format also dictates what components are shown, e.g.
    MM/dd/YYYY will not display the time picker.
    Returns the component's options.format string

    Related Pages:

      https://getdatepicker.com/5-4/Options/
      https://momentjs.com/docs/#/displaying/format/
    """
    return self._config_get()

  @format.setter
  def format(self, text):
    self._config(text)

  @property
  def formats(self):
    """
    https://momentjs.com/docs/#/displaying/format/

    """
    return EnumFormatTypes(self, "format")

  @property
  def icons(self):
    """
    Description:
    -----------
    Change the default icons for the pickers functions.

    Related Pages:

      https://getdatepicker.com/5-4/Options/

    :rtype: DTIcons
    """
    return self._config_sub_data("icons", DTIcons)

  @property
  def buttons(self):
    """
    Description:
    -----------
    Change the default toolbar buttons for the pickers functions.

    Related Pages:

      https://getdatepicker.com/5-4/Options/

    :rtype: DTButtons
    """
    return self._config_sub_data("buttons", DTButtons)

  @property
  def multidateSeparator(self):
    """
    Description:
    -----------
    Used with allowMultidate. E.g. 1/1/2017,1/2/2017

    Related Pages:

      https://getdatepicker.com/5-4/Usage/#custom-icons
    """
    return self._config_get()

  @multidateSeparator.setter
  def multidateSeparator(self, text):
    self.allowMultidate = True
    self._config(text)

  @property
  def sideBySide(self):
    """
    Description:
    -----------
    Shows the picker side by side when using the time and date together.

    Returns a boolean of the options.sideBySide.
    Takes a boolean.
    If sideBySide is true and the time picker is used, both components will display side by side instead of collapsing.

    Related Pages:

      https://getdatepicker.com/5-4/Options/
    """
    return self._config_get()

  @sideBySide.setter
  def sideBySide(self, flag):
    self._config(flag)

  @property
  def viewMode(self):
    """
    Description:
    -----------
    The default view to display when the picker is shown.

    https://getdatepicker.com/5-4/Usage/#custom-icons

    """
    return self._config_get()

  @viewMode.setter
  def viewMode(self, text):
    self._config(text)

  @property
  def viewModes(self):
    return EnumViewMode(self, "viewMode")

  @property
  def useCurrent(self):
    """
    Description:
    -----------
    On show, will set the picker to the current date/time.
    Returns a boolean or string with the options.useCurrent option configuration

    Related Pages:

      https://getdatepicker.com/5-4/Options/
    """
    return self._config_get(True)

  @useCurrent.setter
  def useCurrent(self, flag):
    self._config(flag)

  @property
  def useStrict(self):
    """
    Description:
    -----------
    Defines if moment should use strict date parsing when considering a date to be valid.
    Returns a boolean of the options.useStrict
    Takes a boolean. If useStrict is true, moment.js parsing rules will be stricter when determining if a date is
    valid or not.

    Related Pages:

      https://getdatepicker.com/5-4/Options/
    """
    return self._config_get()

  @useStrict.setter
  def useStrict(self, flag):
    self._config(flag)

  @property
  def viewDate(self):
    """
    Description:
    -----------
    This will change the viewDate without changing or setting the selected date.

    Related Pages:

      https://getdatepicker.com/5-4/Usage/#custom-icons
    """
    return self._config_get(False)

  @viewDate.setter
  def viewDate(self, value):
    self._config(value)

  @property
  def disabledHours(self):
    """
    Description:
    -----------
    Returns an array variable with the currently set options.en/disabledHours option.

    Usage::

      disabledHours: [0, 1, 2, 3, 4, 5, 6, 7, 8, 18, 19, 20, 21, 22, 23, 24]
      enabledHours: [9, 10, 11, 12, 13, 14, 15, 16]

    Related Pages:

      https://getdatepicker.com/5-4/Usage/#custom-icons
    """
    return self._config_get(False)

  @disabledHours.setter
  def disabledHours(self, values):
    self._config(values)

  @property
  def enabledHours(self):
    """
    Description:
    -----------
    Returns an array variable with the currently set options.en/disabledHours option.

    Usage::

      disabledHours: [0, 1, 2, 3, 4, 5, 6, 7, 8, 18, 19, 20, 21, 22, 23, 24]
      enabledHours: [9, 10, 11, 12, 13, 14, 15, 16]

    Related Pages:

      https://getdatepicker.com/5-4/Usage/#custom-icons
    """
    return self._config_get(False)

  @enabledHours.setter
  def enabledHours(self, values):
    self._config(values)

  @property
  def focusOnShow(self):
    """
    Description:
    -----------
    Returns a boolean variable with the currently set options.focusOnShow option.
    Takes a boolean value.

    If false, the textbox will not be given focus when the picker is shown

    Related Pages:

      https://getdatepicker.com/5-4/Options/
    """
    return self._config_get(False)

  @focusOnShow.setter
  def focusOnShow(self, flag):
    self._config(flag)

  @property
  def allowInputToggle(self):
    """
    Description:
    -----------
    If true, the picker will show on textbox focus and icon click when used in a button group.
    Returns a boolean variable with the currently set options.allowInputToggle option

    Related Pages:

      https://getdatepicker.com/5-4/Options/
    """
    return self._config_get(False)

  @allowInputToggle.setter
  def allowInputToggle(self, flag):
    self._config(flag)

  @property
  def disabledTimeIntervals(self):
    """
    Description:
    -----------
    Disables time selection between the given moments.
    Returns an array variable with the currently set options.disabledTimeIntervals option.

    Takes a array value.
    The array must be in the following format [moment(),moment()]

    Related Pages:

      https://getdatepicker.com/5-4/Options/
    """
    return self._config_get(False)

  @disabledTimeIntervals.setter
  def disabledTimeIntervals(self, array):
    self._config(array)

  @property
  def ignoreReadonly(self):
    """
    Description:
    -----------
    Allow date picker show event to fire even when the associated input element has the readonly="readonly" property.
    Returns a boolean variable with the currently set options.ignoreReadonly option.
    Takes a boolean value.

    Set this to true to allow the picker to be used even if the input field is readonly. This will not bypass
    the disabled property

    Related Pages:

      https://getdatepicker.com/5-4/Options/
    """
    return self._config_get(False)

  @ignoreReadonly.setter
  def ignoreReadonly(self, flag):
    self._config(flag)

  @property
  def debug(self):
    """
    Description:
    -----------
    Will cause the date picker to stay open after a blur event.

    Related Pages:

      https://getdatepicker.com/5-4/Options/
    """
    return self._config_get(False)

  @debug.setter
  def debug(self, flag):
    self._config(flag)

  def keyBinds(self):
    # TODO: https://getdatepicker.com/5-4/Options/
    pass

  @property
  def keepInvalid(self):
    """
    Description:
    -----------
    Will cause the date picker to not revert or overwrite invalid dates.
    Returns a string variable with the currently set options.keepInvalid option.

    Takes a boolean value.
    If true, invalid dates will not be reverted to a previous selection or changed.

    Related Pages:

      https://getdatepicker.com/5-4/Options/
    """
    return self._config_get(False)

  @keepInvalid.setter
  def keepInvalid(self, flag):
    self._config(flag)

  @property
  def inline(self):
    """
    Description:
    -----------
    Will display the picker inline without the need of a input field. This will also hide borders and shadows.

    Returns a boolean variable with the currently set options.inline option.

    Related Pages:

      https://getdatepicker.com/5-4/Options/
    """
    return self._config_get(False)

  @inline.setter
  def inline(self, flag):
    self._config(flag)

  @property
  def keepOpen(self):
    """
    Description:
    -----------
    Will cause the date picker to stay open after selecting a date.
    Returns a boolean variable with the currently set options.keepOpen option.
    Takes a boolean value.

    Related Pages:

      https://getdatepicker.com/5-4/Options/
    """
    return self._config_get(False)

  @keepOpen.setter
  def keepOpen(self, flag):
    self._config(flag)

  @property
  def toolbarplacement(self):
    """
    Description:
    -----------
    Changes the placement of the icon toolbar.

    Returns a string variable with the currently set options.toolbarplacement option.
    Takes a string value. Valid values are 'default', 'top' and 'bottom'.

    Changes the placement of the toolbar where the today, clear, component switch icon are located.

    Related Pages:

      https://getdatepicker.com/5-4/Options/
    """
    return self._config_get(False)

  @toolbarplacement.setter
  def toolbarplacement(self, text):
    self._config(text)

  @property
  def calendarWeeks(self):
    """
    Description:
    -----------
    Shows the week of the year to the left of first day of the week.
    Returns a boolean with the current options.calendarWeeks option configuration
    Takes a boolean variable to set if the week numbers will appear to the left on the days view

    Related Pages:

      https://getdatepicker.com/5-4/Options/
    """
    return self._config_get(False)

  @calendarWeeks.setter
  def calendarWeeks(self, text):
    self._config(text)

  @property
  def enabledDates(self):
    """
    Description:
    -----------
    Returns an array with the currently set enabled dates on the component.
    Takes an [ string or Date or moment ] of values and allows the user to select only from those days.

    Related Pages:

      https://getdatepicker.com/5-4/Options/
    """
    return self._config_get()

  @enabledDates.setter
  def enabledDates(self, array):
    self._config(array)

  @property
  def disabledDates(self):
    """
    Description:
    -----------
    Returns an array with the currently set disabled dates on the component.
    Takes an [ string or Date or moment ] of values and allows the user to select only from those days.

    Related Pages:

      https://getdatepicker.com/5-4/Options/
    """
    return self._config_get()

  @disabledDates.setter
  def disabledDates(self, array):
    self._config(array)

  @property
  def defaultDate(self):
    """
    Description:
    -----------
    Sets the picker default date/time. Overrides useCurrent
    Returns a moment with the options.defaultDate option configuration or false if not set

    Related Pages:

      https://getdatepicker.com/5-4/Options/
    """
    return self._config_get()

  @defaultDate.setter
  def defaultDate(self, value):
    self._config(value)

  @property
  def maxDate(self):
    """
    Description:
    -----------
    Prevents date/time selections before this date.
    Will override defaultDate and useCurrent if either of these settings are the same day since both options are
    invalid according to the rules you've selected.

    Returns the currently set moment of the options.maxDate or false if not set.
    Takes a [maxDate] string, Date, moment, boolean:false parameter and disallows the user to select a moment
    that is after that moment.

    Related Pages:

      https://getdatepicker.com/5-4/Options/
    """
    return self._config_get()

  @maxDate.setter
  def maxDate(self, value):
    self._config(value)

  @property
  def minDate(self):
    """
    Description:
    -----------
    Prevents date/time selections before this date.
    Will override defaultDate and useCurrent if either of these settings are the same day since both options are
    invalid according to the rules you've selected.

    Returns the currently set moment of the options.minDate or false if not set.
    Takes a [minDate] string, Date, moment, boolean:false parameter and disallows the user to select a moment
    that is after that moment.

    Related Pages:

      https://getdatepicker.com/5-4/Options/
    """
    return self._config_get()

  @minDate.setter
  def minDate(self, value):
    self._config(value)

  @property
  def stepping(self):
    """
    Description:
    -----------
    Number of minutes the up/down arrow's will move the minutes value in the time picker.
    Returns a number with the options.stepping option configuration.

    Related Pages:

      https://getdatepicker.com/5-4/Options/
    """
    return self._config_get(1)

  @stepping.setter
  def stepping(self, num):
    self._config(num)

  @property
  def extraFormats(self):
    """
    Description:
    -----------
    Allows for several input formats to be valid.
    Returns a boolean or array with the options.extraFormats option configuration.
    Takes an array of valid input moment format options.

    Related Pages:

      https://getdatepicker.com/5-4/Options/
    """
    return self._config_get()

  @extraFormats.setter
  def extraFormats(self, value):
    self._config(value)

  @property
  def dayViewHeaderFormat(self):
    """
    Description:
    -----------
    Changes the heading of the date picker when in "days" view.
    Returns a string variable with the currently set options.dayViewHeaderFormat option.

    Related Pages:

      https://getdatepicker.com/5-4/Options/
    """
    return self._config_get('MMMM YYYY')

  @dayViewHeaderFormat.setter
  def dayViewHeaderFormat(self, value):
    self._config(value)

  @property
  def date(self):
    """
    Description:
    -----------
    Returns the component's model current date, a moment object or null if not set.
    Takes string, Date, moment, null parameter and sets the components model current moment to it.

    Related Pages:

      https://getdatepicker.com/5-4/Options/
    """
    return self._config_get()

  @date.setter
  def date(self, value):
    self._config(value)

