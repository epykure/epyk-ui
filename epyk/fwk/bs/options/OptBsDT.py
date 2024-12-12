
from epyk.core.html.options import Options
from epyk.core.html.options import Enums


class EnumFormatTypes(Enums):

  def time_only(self):
    """Display only the time for the component.

    Usage::
      page.web.bs.time()

    `getdatepicker <https://getdatepicker.com/5-4/Usage/#custom-icons>`_
    """
    self._set_value(value="LT")

  def date_only(self):
    """Display only the date for the component.

    Usage::
      page.web.bs.date()

    `getdatepicker <https://getdatepicker.com/5-4/Usage/#custom-icons>`_
    """
    self._set_value(value="L")

  def mm_yyyy(self):
    """

    `getdatepicker <https://getdatepicker.com/5-4/Usage/#custom-icons>`_
    """
    self._set_value(value="MM/YYY")


class EnumViewMode(Enums):

  def years(self):
    """

    `getdatepicker <https://getdatepicker.com/5-4/Options/>`_
    """
    self._set_value()

  def decades(self):
    """

    `getdatepicker <https://getdatepicker.com/5-4/Options/>`_
    """
    self._set_value()

  def months(self):
    """

    `getdatepicker <https://getdatepicker.com/5-4/Options/>`_
    """
    self._set_value()

  def days(self):
    """

    `getdatepicker <https://getdatepicker.com/5-4/Options/>`_
    """
    self._set_value()

  def times(self):
    """

    `getdatepicker <https://getdatepicker.com/5-4/Options/>`_
    """
    self._set_value()


class DTIcons(Options):

  @property
  def type(self) -> str:
    """

    `getdatepicker <https://getdatepicker.com/5-4/Usage/#custom-icons>`_
    """
    return self._config_get('icons')

  @type.setter
  def type(self, text: str):
    self._config(text)

  @property
  def time(self) -> str:
    """   

    `getdatepicker <https://getdatepicker.com/5-4/Usage/#custom-icons>`_
    """
    return self._config_get('fa-solid fa-clock')

  @time.setter
  def time(self, text: str):
    self._config(text)

  @property
  def date(self) -> str:
    """Returns the component's model current date, a moment object or null if not set.

    `getdatepicker <https://getdatepicker.com/5-4/Usage/#custom-icons>`_
    """
    return self._config_get('fa-solid fa-calendar')

  @date.setter
  def date(self, text: str):
    self._config(text)

  @property
  def up(self) -> str:
    """   

    `getdatepicker <https://getdatepicker.com/5-4/Usage/#custom-icons>`_
    """
    return self._config_get('fa-solid fa-arrow-up')

  @up.setter
  def up(self, text: str):
    self._config(text)

  @property
  def down(self) ->str:
    """   

    `getdatepicker <https://getdatepicker.com/5-4/Usage/#custom-icons>`_
    """
    return self._config_get('fa-solid fa-arrow-down')

  @down.setter
  def down(self, text: str):
    self._config(text)

  @property
  def previous(self) -> str:
    """

    `getdatepicker <https://getdatepicker.com/5-4/Usage/#custom-icons>`_
    """
    return self._config_get('fa-solid fa-chevron-left')

  @previous.setter
  def previous(self, text: str):
    self._config(text)

  @property
  def next(self) -> str:
    """

    `getdatepicker <https://getdatepicker.com/5-4/Usage/#custom-icons>`_
    """
    return self._config_get('fa-solid fa-chevron-right')

  @next.setter
  def next(self, text: str):
    self._config(text)

  @property
  def today(self) -> str:
    """

    `getdatepicker <https://getdatepicker.com/5-4/Usage/#custom-icons>`_
    """
    return self._config_get('fa-solid fa-calendar-check')

  @today.setter
  def today(self, text: str):
    self._config(text)

  @property
  def clear(self) -> str:
    """

    `getdatepicker <https://getdatepicker.com/5-4/Usage/#custom-icons>`_
    """
    return self._config_get('fa-solid fa-trash')

  @clear.setter
  def clear(self, text: str):
    self._config(text)

  @property
  def close(self):
    """

    `getdatepicker <https://getdatepicker.com/5-4/Usage/#custom-icons>`_
    """
    return self._config_get('fa-solid fa-xmark')

  @close.setter
  def close(self, text: str):
    self._config(text)


class DTButtons(Options):

  @property
  def showToday(self):
    """Change the default toolbar buttons for the pickers functions.

    `getdatepicker <https://getdatepicker.com/5-4/Options/>`_
    """
    return self._config_get()

  @showToday.setter
  def showToday(self, flag):
    self._config(flag)

  @property
  def showClear(self):
    """Change the default toolbar buttons for the pickers functions.

    `getdatepicker <https://getdatepicker.com/5-4/Options/>`_
    """
    return self._config_get()

  @showClear.setter
  def showClear(self, flag):
    self._config(flag)

  @property
  def showClose(self):
    """Change the default toolbar buttons for the pickers functions.

    `getdatepicker <https://getdatepicker.com/5-4/Options/>`_
    """
    return self._config_get()

  @showClose.setter
  def showClose(self, flag):
    self._config(flag)


class DT(Options):

  @property
  def allowMultidate(self) -> bool:
    """Allows the setting of multiple dates.

    Related Pages:

      https://getdatepicker.com/5-4/Usage/#custom-icons
      https://getdatepicker.com/5-4/Options/
    """
    return self._config_get()

  @allowMultidate.setter
  def allowMultidate(self, flag: bool):
    self._config(flag)

  @property
  def daysOfWeekDisabled(self):
    """Disables the section of days of the week, e.g. weekends.
    Returns an array with the options.daysOfWeekDisabled configuration setting of the component.

    `getdatepicker <https://getdatepicker.com/5-4/Options/>`_
    """
    return self._config_get()

  @daysOfWeekDisabled.setter
  def daysOfWeekDisabled(self, values):
    self._config(values)

  @property
  def locale(self) -> str:
    """ See momentjs for valid locales.
    You must include moment-with-locales.js or a local js file. Returns the currently set locale of the options.locale

    `getdatepicker <https://getdatepicker.com/5-4/Options/>`_
    """
    return self._config_get()

  @locale.setter
  def locale(self, text: str):
    self._config(text)

  @property
  def collapse(self) -> bool:
    """Using a Bootstraps collapse to switch between date/time pickers.

    Returns a boolean of the options.sideBySide.
    Takes a boolean. If set to false the picker will display similar to sideBySide except vertical.

    `getdatepicker <https://getdatepicker.com/5-4/Options/>`_
    """
    return self._config_get(True)

  @collapse.setter
  def collapse(self, flag: bool):
    self._config(flag)

  @property
  def format(self):
    """See momentjs' docs for valid formats. Format also dictates what components are shown, e.g.

    MM/dd/YYYY will not display the time picker. Returns the component's options.format string

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
    `getdatepicker <https://momentjs.com/docs/#/displaying/format/>`_
    """
    return EnumFormatTypes(self, "format")

  @property
  def icons(self) -> DTIcons:
    """Change the default icons for the pickers functions.

    `getdatepicker <https://getdatepicker.com/5-4/Options/>`_
    """
    return self._config_sub_data("icons", DTIcons)

  @property
  def buttons(self) -> DTButtons:
    """Change the default toolbar buttons for the pickers functions.

    `getdatepicker <https://getdatepicker.com/5-4/Options/>`_
    """
    return self._config_sub_data("buttons", DTButtons)

  @property
  def multidateSeparator(self):
    """Used with allowMultidate. E.g. 1/1/2017,1/2/2017

    `getdatepicker <https://getdatepicker.com/5-4/Usage/#custom-icons>`_
    """
    return self._config_get()

  @multidateSeparator.setter
  def multidateSeparator(self, text):
    self.allowMultidate = True
    self._config(text)

  @property
  def sideBySide(self) -> bool:
    """Shows the picker side by side when using the time and date together.

    Returns a boolean of the options.sideBySide. Takes a boolean.
    If sideBySide is true and the time picker is used, both components will display side by side instead of collapsing.

    `getdatepicker <https://getdatepicker.com/5-4/Options/>`_
    """
    return self._config_get(False)

  @sideBySide.setter
  def sideBySide(self, flag: bool):
    self._config(flag)

  @property
  def viewMode(self) -> str:
    """The default view to display when the picker is shown.

    `getdatepicker <https://getdatepicker.com/5-4/Usage/#custom-icons>`_
    """
    return self._config_get()

  @viewMode.setter
  def viewMode(self, text: str):
    self._config(text)

  @property
  def viewModes(self) -> EnumViewMode:
    return EnumViewMode(self, "viewMode")

  @property
  def useCurrent(self) -> bool:
    """On show, will set the picker to the current date/time.
    Returns a boolean or string with the options.useCurrent option configuration

    `getdatepicker <https://getdatepicker.com/5-4/Options/>`_
    """
    return self._config_get(True)

  @useCurrent.setter
  def useCurrent(self, flag: bool):
    self._config(flag)

  @property
  def useStrict(self) -> bool:
    """Defines if moment should use strict date parsing when considering a date to be valid. Returns a boolean of the options.useStrict
    Takes a boolean. If useStrict is true, moment.js parsing rules will be stricter when determining if a date is
    valid or not.

    `getdatepicker <https://getdatepicker.com/5-4/Options/>`_
    """
    return self._config_get()

  @useStrict.setter
  def useStrict(self, flag: bool):
    self._config(flag)

  @property
  def viewDate(self) -> bool:
    """This will change the viewDate without changing or setting the selected date.

    `getdatepicker <https://getdatepicker.com/5-4/Usage/#custom-icons>`_
    """
    return self._config_get(False)

  @viewDate.setter
  def viewDate(self, value: bool):
    self._config(value)

  @property
  def disabledHours(self):
    """Returns an array variable with the currently set options.en/disabledHours option.

    Usage::
      disabledHours: [0, 1, 2, 3, 4, 5, 6, 7, 8, 18, 19, 20, 21, 22, 23, 24]
      enabledHours: [9, 10, 11, 12, 13, 14, 15, 16]

    `getdatepicker <https://getdatepicker.com/5-4/Usage/#custom-icons>`_
    """
    return self._config_get(False)

  @disabledHours.setter
  def disabledHours(self, values):
    self._config(values)

  @property
  def enabledHours(self):
    """Returns an array variable with the currently set options.en/disabledHours option.

    Usage::
      disabledHours: [0, 1, 2, 3, 4, 5, 6, 7, 8, 18, 19, 20, 21, 22, 23, 24]
      enabledHours: [9, 10, 11, 12, 13, 14, 15, 16]

    `getdatepicker <https://getdatepicker.com/5-4/Usage/#custom-icons>`_
    """
    return self._config_get(False)

  @enabledHours.setter
  def enabledHours(self, values):
    self._config(values)

  @property
  def focusOnShow(self) -> bool:
    """Returns a boolean variable with the currently set options.focusOnShow option. Takes a boolean value.

    If false, the textbox will not be given focus when the picker is shown

    `getdatepicker <https://getdatepicker.com/5-4/Options/>`_
    """
    return self._config_get(False)

  @focusOnShow.setter
  def focusOnShow(self, flag: bool):
    self._config(flag)

  @property
  def allowInputToggle(self) -> bool:
    """If true, the picker will show on textbox focus and icon click when used in a button group.
    Returns a boolean variable with the currently set options.allowInputToggle option

    `getdatepicker <https://getdatepicker.com/5-4/Options/>`_
    """
    return self._config_get(False)

  @allowInputToggle.setter
  def allowInputToggle(self, flag: bool):
    self._config(flag)

  @property
  def disabledTimeIntervals(self):
    """Disables time selection between the given moments.
    Returns an array variable with the currently set options.disabledTimeIntervals option.

    Takes a array value.
    The array must be in the following format [moment(),moment()]

    `getdatepicker <https://getdatepicker.com/5-4/Options/>`_
    """
    return self._config_get(False)

  @disabledTimeIntervals.setter
  def disabledTimeIntervals(self, array):
    self._config(array)

  @property
  def ignoreReadonly(self) -> bool:
    """Allow date picker show event to fire even when the associated input element has the readonly="readonly" property.
    Returns a boolean variable with the currently set options.ignoreReadonly option.
    Takes a boolean value.

    Set this to true to allow the picker to be used even if the input field is readonly. This will not bypass
    the disabled property

    `getdatepicker <https://getdatepicker.com/5-4/Options/>`_
    """
    return self._config_get(False)

  @ignoreReadonly.setter
  def ignoreReadonly(self, flag: bool):
    self._config(flag)

  @property
  def debug(self) -> bool:
    """Will cause the date picker to stay open after a blur event.

    `getdatepicker <https://getdatepicker.com/5-4/Options/>`_
    """
    return self._config_get(False)

  @debug.setter
  def debug(self, flag: bool):
    self._config(flag)

  def keyBinds(self):
    # TODO: https://getdatepicker.com/5-4/Options/
    pass

  @property
  def keepInvalid(self):
    """Will cause the date picker to not revert or overwrite invalid dates.
    Returns a string variable with the currently set options.keepInvalid option.

    Takes a boolean value. If true, invalid dates will not be reverted to a previous selection or changed.

    `getdatepicker <https://getdatepicker.com/5-4/Options/>`_
    """
    return self._config_get(False)

  @keepInvalid.setter
  def keepInvalid(self, flag):
    self._config(flag)

  @property
  def inline(self):
    """Will display the picker inline without the need of a input field. This will also hide borders and shadows.

    Returns a boolean variable with the currently set options.inline option.

    `getdatepicker <https://getdatepicker.com/5-4/Options/>`_
    """
    return self._config_get(False)

  @inline.setter
  def inline(self, flag):
    self._config(flag)

  @property
  def keepOpen(self) -> bool:
    """Will cause the date picker to stay open after selecting a date.
    Returns a boolean variable with the currently set options.keepOpen option. Takes a boolean value.

    `getdatepicker <https://getdatepicker.com/5-4/Options/>`_
    """
    return self._config_get(False)

  @keepOpen.setter
  def keepOpen(self, flag: bool):
    self._config(flag)

  @property
  def toolbarplacement(self) -> str:
    """Changes the placement of the icon toolbar.

    Returns a string variable with the currently set options.toolbarplacement option.
    Takes a string value. Valid values are 'default', 'top' and 'bottom'.

    Changes the placement of the toolbar where the today, clear, component switch icon are located.

    `getdatepicker <https://getdatepicker.com/5-4/Options/>`_
    """
    return self._config_get('bottom')

  @toolbarplacement.setter
  def toolbarplacement(self, text: str):
    self._config(text)

  @property
  def calendarWeeks(self) -> bool:
    """Shows the week of the year to the left of first day of the week.

    Returns a boolean with the current options.calendarWeeks option configuration
    Takes a boolean variable to set if the week numbers will appear to the left on the days view

    `getdatepicker <https://getdatepicker.com/5-4/Options/>`_
    """
    return self._config_get(False)

  @calendarWeeks.setter
  def calendarWeeks(self, flag: bool):
    self._config(flag)

  @property
  def enabledDates(self):
    """Returns an array with the currently set enabled dates on the component.
    Takes an [ string or Date or moment ] of values and allows the user to select only from those days.

    `getdatepicker <https://getdatepicker.com/5-4/Options/>`_
    """
    return self._config_get()

  @enabledDates.setter
  def enabledDates(self, array):
    self._config(array)

  @property
  def disabledDates(self):
    """Returns an array with the currently set disabled dates on the component.
    Takes an [ string or Date or moment ] of values and allows the user to select only from those days.

    `getdatepicker <https://getdatepicker.com/5-4/Options/>`_
    """
    return self._config_get()

  @disabledDates.setter
  def disabledDates(self, array):
    self._config(array)

  @property
  def defaultDate(self):
    """Sets the picker default date/time. Overrides useCurrent
    Returns a moment with the options.defaultDate option configuration or false if not set

    `getdatepicker <https://getdatepicker.com/5-4/Options/>`_
    """
    return self._config_get()

  @defaultDate.setter
  def defaultDate(self, value):
    self._config(value)

  @property
  def maxDate(self):
    """Prevents date/time selections before this date.
    Will override defaultDate and useCurrent if either of these settings are the same day since both options are
    invalid according to the rules you've selected.

    Returns the currently set moment of the options.maxDate or false if not set.
    Takes a [maxDate] string, Date, moment, boolean:false parameter and disallows the user to select a moment
    that is after that moment.

    `getdatepicker <https://getdatepicker.com/5-4/Options/>`_
    """
    return self._config_get()

  @maxDate.setter
  def maxDate(self, value):
    self._config(value)

  @property
  def minDate(self):
    """Prevents date/time selections before this date.
    Will override defaultDate and useCurrent if either of these settings are the same day since both options are
    invalid according to the rules you've selected.

    Returns the currently set moment of the options.minDate or false if not set.
    Takes a [minDate] string, Date, moment, boolean:false parameter and disallows the user to select a moment
    that is after that moment.

    `getdatepicker <https://getdatepicker.com/5-4/Options/>`_
    """
    return self._config_get()

  @minDate.setter
  def minDate(self, value):
    self._config(value)

  @property
  def stepping(self) -> int:
    """Number of minutes the up/down arrow's will move the minutes value in the time picker.
    Returns a number with the options.stepping option configuration.

    `getdatepicker <https://getdatepicker.com/5-4/Options/>`_
    """
    return self._config_get(1)

  @stepping.setter
  def stepping(self, num: int):
    self._config(num)

  @property
  def extraFormats(self):
    """Allows for several input formats to be valid. Returns a boolean or array with the options.extraFormats option
    configuration. Takes an array of valid input moment format options.

    `getdatepicker <https://getdatepicker.com/5-4/Options/>`_
    """
    return self._config_get()

  @extraFormats.setter
  def extraFormats(self, value):
    self._config(value)

  @property
  def dayViewHeaderFormat(self) -> str:
    """Changes the heading of the date picker when in "days" view.
    Returns a string variable with the currently set options.dayViewHeaderFormat option.

    `getdatepicker <https://getdatepicker.com/5-4/Options/>`_
    """
    return self._config_get('MMMM YYYY')

  @dayViewHeaderFormat.setter
  def dayViewHeaderFormat(self, value: str):
    self._config(value)

  @property
  def date(self):
    """Returns the component's model current date, a moment object or null if not set.
    Takes string, Date, moment, null parameter and sets the components model current moment to it.

    `getdatepicker <https://getdatepicker.com/5-4/Options/>`_
    """
    return self._config_get()

  @date.setter
  def date(self, value):
    self._config(value)

  @property
  def widgetPositioning(self) -> dict:
    """Returns the currently set options.widgetPositioning object containing two keys horizontal and vertical
    """
    return self._config_get({"horizontal": 'auto', "vertical": 'auto'})

  @widgetPositioning.setter
  def widgetPositioning(self, values: dict):
    self._config(values)

  @property
  def widgetParent(self):
    """On picker show, places the widget at the identifier (string) or jQuery object if the element has css
    position: 'relative'"""
    return self._config_get(None)

  @widgetParent.setter
  def widgetParent(self, value):
    self._config(value)


class DT6Buttons(Options):

  @property
  def today(self) -> bool:
    """Change the default toolbar buttons for the pickers functions.

    `getdatepicker <https://getdatepicker.com/5-4/Options/>`_
    """
    return self._config_get(False)

  @today.setter
  def today(self, flag: bool):
    self._config(flag)

  @property
  def clear(self) -> bool:
    """Change the default toolbar buttons for the pickers functions.

    `getdatepicker <https://getdatepicker.com/5-4/Options/>`_
    """
    return self._config_get(False)

  @clear.setter
  def clear(self, flag: bool):
    self._config(flag)

  @property
  def close(self) -> bool:
    """Change the default toolbar buttons for the pickers functions.

    `getdatepicker <https://getdatepicker.com/5-4/Options/>`_
    """
    return self._config_get(False)

  @close.setter
  def close(self, flag: bool):
    self._config(flag)


class DT6Component(Options):

  @property
  def calendar(self) -> bool:
    """
    `getdatepicker <https://getdatepicker.com/6/options/?`_
    """
    return self._config_get(True)

  @calendar.setter
  def calendar(self, flag: bool):
    self._config(flag)

  @property
  def date(self) -> bool:
    """
    `getdatepicker <https://getdatepicker.com/6/options/?`_
    """
    return self._config_get(True)

  @date.setter
  def date(self, flag: bool):
    self._config(flag)

  @property
  def month(self) -> bool:
    """
    `getdatepicker <https://getdatepicker.com/6/options/?`_
    """
    return self._config_get(True)

  @month.setter
  def month(self, flag: bool):
    self._config(flag)

  @property
  def year(self) -> bool:
    """
    `getdatepicker <https://getdatepicker.com/6/options/?`_
    """
    return self._config_get(True)

  @year.setter
  def year(self, flag: bool):
    self._config(flag)

  @property
  def decades(self) -> bool:
    """
    `getdatepicker <https://getdatepicker.com/6/options/?`_
    """
    return self._config_get(True)

  @decades.setter
  def decades(self, flag: bool):
    self._config(flag)

  @property
  def clock(self) -> bool:
    """
    `getdatepicker <https://getdatepicker.com/6/options/?`_
    """
    return self._config_get(True)

  @clock.setter
  def clock(self, flag: bool):
    self._config(flag)

  @property
  def hours(self) -> bool:
    """
    `getdatepicker <https://getdatepicker.com/6/options/?`_
    """
    return self._config_get(True)

  @hours.setter
  def hours(self, flag: bool):
    self._config(flag)

  @property
  def minutes(self) -> bool:
    """
    `getdatepicker <https://getdatepicker.com/6/options/?`_
    """
    return self._config_get(True)

  @minutes.setter
  def minutes(self, flag: bool):
    self._config(flag)

  @property
  def seconds(self) -> bool:
    """
    `getdatepicker <https://getdatepicker.com/6/options/?`_
    """
    return self._config_get(False)

  @seconds.setter
  def seconds(self, flag: bool):
    self._config(flag)

  @property
  def useTwentyfourHour(self):
    """
    `getdatepicker <https://getdatepicker.com/6/options/?`_
    """
    return self._config_get(None)

  @useTwentyfourHour.setter
  def useTwentyfourHour(self, value):
    self._config(value)


class DT6Display(Options):

  @property
  def icons(self) -> DTIcons:
    """
    `getdatepicker <https://getdatepicker.com/6/options/>`_
    """
    return self._config_sub_data("icons", DTIcons)

  @property
  def buttons(self) -> DT6Buttons:
    """
    `getdatepicker <https://getdatepicker.com/6/options/>`_
    """
    return self._config_sub_data("buttons", DT6Buttons)

  @property
  def components(self) -> DT6Component:
    """
    `getdatepicker <https://getdatepicker.com/6/options/>`_
    """
    return self._config_sub_data("components", DT6Component)

  @property
  def inline(self) -> bool:
    """Will display the picker inline without the need of a input field. This will also hide borders and shadows.

    `getdatepicker <https://getdatepicker.com/6/options/?`_
    """
    return self._config_get(False)

  @inline.setter
  def inline(self, flag: bool):
    self._config(flag)

  @property
  def sideBySide(self) -> bool:
    """Takes a boolean. If sideBySide is true and the time picker is used, both components will display side by side
    instead of collapsing.

    `getdatepicker <https://getdatepicker.com/6/options/?`_
    """
    return self._config_get(False)

  @sideBySide.setter
  def sideBySide(self, flag: bool):
    self._config(flag)

  @property
  def theme(self) -> bool:
    """
    `getdatepicker <https://getdatepicker.com/6/options/?`_
    """
    return self._config_get("auto")

  @theme.setter
  def theme(self, value: str):
    self._config(value)

  @property
  def calendarWeeks(self) -> bool:
    """
    `getdatepicker <https://getdatepicker.com/6/options/?`_
    """
    return self._config_get(False)

  @calendarWeeks.setter
  def calendarWeeks(self, flag: bool):
    self._config(flag)

  @property
  def viewMode(self) -> str:
    """The default view to display when the picker is shown.
    Accepts: 'decades','years','months','days', 'times'

    `getdatepicker <https://getdatepicker.com/6/options/?`_
    """
    return self._config_get('calendar')

  @viewMode.setter
  def viewMode(self, value: str):
    self._config(value)

  @property
  def toolbarPlacement(self) -> str:
    """Changes the placement of the icon toolbar.

    `getdatepicker <https://getdatepicker.com/6/options/?`_
    """
    return self._config_get('bottom')

  @toolbarPlacement.setter
  def toolbarPlacement(self, value: str):
    self._config(value)

  @property
  def keepOpen(self) -> bool:
    """Will cause the date picker to stay open after selecting a date.

    `getdatepicker <https://getdatepicker.com/6/options/?`_
    """
    return self._config_get(False)

  @keepOpen.setter
  def keepOpen(self, flag: bool):
    self._config(flag)


class DTRestrictions(Options):

  @property
  def minDate(self) -> bool:
    """
    `getdatepicker <https://getdatepicker.com/6/options/restrictions.html>`_
    """
    return self._config_get()

  @minDate.setter
  def minDate(self, value):
    self._config(value)

  @property
  def maxDate(self) -> bool:
    """
    `getdatepicker <https://getdatepicker.com/6/options/restrictions.html>`_
    """
    return self._config_get()

  @maxDate.setter
  def maxDate(self, value):
    self._config(value)

  @property
  def disabledDates(self) -> list:
    """
    `getdatepicker <https://getdatepicker.com/6/options/restrictions.html>`_
    """
    return self._config_get([])

  @disabledDates.setter
  def disabledDates(self, values):
    self._config(values)

  @property
  def enabledDates(self) -> list:
    """
    `getdatepicker <https://getdatepicker.com/6/options/restrictions.html>`_
    """
    return self._config_get([])

  @enabledDates.setter
  def enabledDates(self, values):
    self._config(values)

  @property
  def daysOfWeekDisabled(self) -> list:
    """Takes an [ Number:0 to 6 ] and disallow the user to select weekdays that exist in this array.
    This has lower priority over the options.minDate, options.maxDate, options.disabledDates and options.enabledDates
    configuration settings.

    `getdatepicker <https://getdatepicker.com/6/options/restrictions.html>`_
    """
    return self._config_get([])

  @daysOfWeekDisabled.setter
  def daysOfWeekDisabled(self, values):
    self._config(values)

  @property
  def disabledTimeIntervals(self) -> list:
    """Returns an array variable with the currently set options.disabledTimeIntervals option.

    `getdatepicker <https://getdatepicker.com/6/options/restrictions.html>`_
    """
    return self._config_get([])

  @disabledTimeIntervals.setter
  def disabledTimeIntervals(self, values):
    self._config(values)

  @property
  def disabledHours(self) -> list:
    """Returns an array variable with the currently set options.en/disabledHours option.

    `getdatepicker <https://getdatepicker.com/6/options/restrictions.html>`_
    """
    return self._config_get([])

  @disabledHours.setter
  def disabledHours(self, values):
    self._config(values)

  @property
  def enabledHours(self) -> list:
    """
    `getdatepicker <https://getdatepicker.com/6/options/restrictions.html>`_
    """
    return self._config_get([])

  @enabledHours.setter
  def enabledHours(self, values):
    self._config(values)


class DTLocalization(Options):

  @property
  def clear(self) -> str:
    """
    `getdatepicker <https://getdatepicker.com/6/options/>`_
    """
    return self._config_get('Clear selection')

  @clear.setter
  def clear(self, value: str):
    self._config(value)

  @property
  def close(self) -> str:
    """
    `getdatepicker <https://getdatepicker.com/6/options/>`_
    """
    return self._config_get('Close the picker')

  @close.setter
  def close(self, value: str):
    self._config(value)

  @property
  def dayViewHeaderFormat(self) -> dict:
    """
    `getdatepicker <https://getdatepicker.com/6/options/>`_
    """
    return self._config_get({ "month": 'long', "year": '2-digit' })

  @dayViewHeaderFormat.setter
  def dayViewHeaderFormat(self, values: dict):
    self._config(values)

  @property
  def decrementHour(self) -> str:
    """
    `getdatepicker <https://getdatepicker.com/6/options/>`_
    """
    return self._config_get('Decrement Hour')

  @decrementHour.setter
  def decrementHour(self, value: str):
    self._config(value)

  @property
  def decrementMinute(self) -> str:
    """
    `getdatepicker <https://getdatepicker.com/6/options/>`_
    """
    return self._config_get('Decrement Minute')

  @decrementMinute.setter
  def decrementMinute(self, value: str):
    self._config(value)

  @property
  def decrementSecond(self) -> str:
    """
    `getdatepicker <https://getdatepicker.com/6/options/>`_
    """
    return self._config_get('Decrement Second')

  @decrementSecond.setter
  def decrementSecond(self, value: str):
    self._config(value)

  @property
  def incrementHour(self) -> str:
    """
    `getdatepicker <https://getdatepicker.com/6/options/>`_
    """
    return self._config_get('Increment Hour')

  @incrementHour.setter
  def incrementHour(self, value: str):
    self._config(value)

  @property
  def incrementMinute(self) -> str:
    """
    `getdatepicker <https://getdatepicker.com/6/options/>`_
    """
    return self._config_get('Increment Minute')

  @incrementMinute.setter
  def incrementMinute(self, value: str):
    self._config(value)

  @property
  def incrementSecond(self) -> str:
    """
    `getdatepicker <https://getdatepicker.com/6/options/>`_
    """
    return self._config_get('Increment Second')

  @incrementSecond.setter
  def incrementSecond(self, value: str):
    self._config(value)

  @property
  def format(self) -> str:
    """
    `getdatepicker <https://getdatepicker.com/6/options/>`_
    """
    return self._config_get()

  @format.setter
  def format(self, value: str):
    self._config(value)


class DT6(Options):

  @property
  def allowInputToggle(self) -> bool:
    """If true, the picker will show on textbox focus and icon click when used in a button group.
    Returns a boolean variable with the currently set options.allowInputToggle option

    `getdatepicker <https://getdatepicker.com/6/options/>`_
    """
    return self._config_get(False)

  @allowInputToggle.setter
  def allowInputToggle(self, flag: bool):
    self._config(flag)

  @property
  def container(self):
    """
    `getdatepicker <https://getdatepicker.com/6/options/?`_
    """
    return self._config_get(None)

  @container.setter
  def container(self, value):
    self._config(value)

  @property
  def dateRange(self) -> bool:
    """
    `getdatepicker <https://getdatepicker.com/6/options/?`_
    """
    return self._config_get(False)

  @dateRange.setter
  def dateRange(self, flag: bool):
    self._config(flag)

  @property
  def debug(self) -> bool:
    """Will cause the date picker to stay open after a blur event.

    `getdatepicker <https://getdatepicker.com/6/options/?`_
    """
    return self._config_get(False)

  @debug.setter
  def debug(self, flag: bool):
    self._config(flag)

  @property
  def defaultDate(self):
    """
    `getdatepicker <https://getdatepicker.com/6/options/?`_
    """
    return self._config_get(None)

  @defaultDate.setter
  def defaultDate(self, value):
    self._config(value)

  @property
  def display(self) -> DT6Display:
    """
    `getdatepicker <https://getdatepicker.com/6/options/>`_
    """
    return self._config_sub_data("display", DT6Display)

  @property
  def format(self) -> str:
    """
    `getdatepicker <https://getdatepicker.com/6/options/>`_
    """
    return self.localization.format

  @format.setter
  def format(self, value: str):
    map_dates = {"yyyy-MM-DD": "yyyy-MM-dd"}
    self.localization.format = map_dates.get(value, value)

  @property
  def keepInvalid(self) -> bool:
    """Will cause the date picker to not revert or overwrite invalid dates.

    `getdatepicker <https://getdatepicker.com/6/options/?`_
    """
    return self._config_get(False)

  @keepInvalid.setter
  def keepInvalid(self, flag: bool):
    self._config(flag)

  @property
  def meta(self) -> dict:
    """
    `getdatepicker <https://getdatepicker.com/6/options/?`_
    """
    return self._config_get({})

  @meta.setter
  def meta(self, values: dict):
    self._config(values)

  @property
  def multipleDates(self) -> bool:
    """
    `getdatepicker <https://getdatepicker.com/6/options/?`_
    """
    return self._config_get(False)

  @multipleDates.setter
  def multipleDates(self, flag: bool):
    self._config(flag)

  @property
  def multipleDatesSeparator(self) -> str:
    """
    `getdatepicker <https://getdatepicker.com/6/options/?`_
    """
    return self._config_get("; ")

  @multipleDatesSeparator.setter
  def multipleDatesSeparator(self, value: str):
    self._config(value)

  @property
  def promptTimeOnDateChange(self) -> bool:
    """
    `getdatepicker <https://getdatepicker.com/6/options/?`_
    """
    return self._config_get(False)

  @promptTimeOnDateChange.setter
  def promptTimeOnDateChange(self, flag: bool):
    self._config(flag)

  @property
  def promptTimeOnDateChangeTransitionDelay(self) -> bool:
    """
    `getdatepicker <https://getdatepicker.com/6/options/?`_
    """
    return self._config_get(200)

  @promptTimeOnDateChangeTransitionDelay.setter
  def promptTimeOnDateChangeTransitionDelay(self, value: int):
    self._config(value)

  @property
  def restrictions(self) -> DTRestrictions:
    """
    `getdatepicker <https://getdatepicker.com/6/options/restrictions.html>`_
    """
    return self._config_sub_data("restrictions", DTRestrictions)

  @property
  def localization(self) -> DTLocalization:
    """
    `getdatepicker <https://getdatepicker.com/6/options/restrictions.html>`_
    """
    return self._config_sub_data("localization", DTLocalization)