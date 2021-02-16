
from epyk.core.js.packages import packageImport
from epyk.core.html.options import Options

from epyk.core.js import JsUtils


class OptionsInput(Options):

  def css(self, attrs):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param attrs: Dictionary. CSS attributes
    """
    self._config(attrs)
    return self

  @property
  def disabled(self):
    """
    Description:
    ------------
    The rows attribute specifies the visible height of a text area, in lines.

    Related Pages:

      https://www.w3schools.com/tags/att_rows.asp
    """
    return self._report.attr.get('disabled', False)

  @disabled.setter
  def disabled(self, value):
    if not value and "disabled" in self._report.attr:
      del self._report.attr["disabled"]

    else:
      self._report.set_attrs({"disabled": value})

  @packageImport("accounting")
  def formatMoney(self, symbol="", digits=0, thousand_sep=".", decimal_sep=","):
    """
    Description:
    -----------
    Format any number into currency

    Related Pages:
http://openexchangerates.github.io/accounting.js/

    Attributes:
    ----------
    :param symbol: String. custom symbol
    :param digits: Integer. Number of digit
    :param thousand_sep: String. The thousand separator
    :param decimal_sep: String. The decimal separator
    """
    self._config({"symbol": symbol, 'digit': digits, "thousand": thousand_sep, "decimal": decimal_sep})
    return self

  @packageImport("accounting")
  def formatNumber(self, digit=0, thousand_sep="."):
    """
    Description:
    -----------
    Format a number with custom precision and localisation

    Related Pages:
http://openexchangerates.github.io/accounting.js/

    Attributes:
    ----------
    :param digit: Integer. Number of digit
    :param thousand_sep: String. The thousand separator
    """
    self._config({'digit': digit, "thousand": thousand_sep})
    return self

  @packageImport("accounting")
  def toFixed(self, digit=0):
    """
    Description:
    -----------
    Better rounding for floating point numbers

    Related Pages:
http://openexchangerates.github.io/accounting.js/

    Attributes:
    ----------
    :param digit: Integer. Number of digit
    """
    self._config(digit)
    return self

  @property
  def background(self):
    """
    Description:
    ------------
    Specifies the maximum number of characters allowed in the text area

    Related Pages:

      https://www.w3schools.com/tags/att_textarea_maxlength.asp
    """
    return self.get(True)

  @background.setter
  def background(self, flag):
    self.set(flag)

  @property
  def maxlength(self):
    """
    Description:
    ------------
    Specifies the maximum number of characters allowed in the text area

    Related Pages:

      https://www.w3schools.com/tags/att_textarea_maxlength.asp
    """
    return self._report.attr.get('maxlength')

  @maxlength.setter
  def maxlength(self, num):
    self._report.set_attrs({"maxlength": num})

  @property
  def name(self):
    """
    Description:
    ------------
    Specifies a name for a text area

    Related Pages:

      https://www.w3schools.com/tags/att_textarea_name.asp
    """
    return self._report.attr.get('name')

  @name.setter
  def name(self, num):
    self._report.set_attrs({"name": num})

  @property
  def placeholder(self):
    """
    Description:
    ------------
    The placeholder attribute specifies a short hint that describes the expected value of an input field (e.g. a sample value or a short description of the expected format).

    Related Pages:

      https://www.w3schools.com/tags/att_input_placeholder.asp
    """
    return self._report.attr.get('placeholder', "")

  @placeholder.setter
  def placeholder(self, value):
    self._report.set_attrs({"placeholder": value})

  @property
  def required(self):
    """
    Description:
    ------------
    Specifies that a text area is required/must be filled out

    Related Pages:

      https://www.w3schools.com/tags/att_textarea_required.asp
    """
    return self._report.attr.get('required')

  @required.setter
  def required(self, value):
    if not value and "required" in self._report.attr:
      del self._report.attr["required"]

    else:
      self._report.set_attrs({"required": value})

  @property
  def wrap(self):
    """
    Description:
    ------------
    Specifies how the text in a text area is to be wrapped when submitted in a form

    Related Pages:

      https://www.w3schools.com/tags/att_textarea_wrap.asp
    """
    return self._report.attr.get('wrap', "")

  @wrap.setter
  def wrap(self, value):
    self._report.set_attrs({"wrap": value})

  @property
  def spellcheck(self):
    """
    Description:
    ------------
    The spellcheck attribute specifies whether the element is to have its spelling and grammar checked or not.

    Related Pages:

      https://www.w3schools.com/tags/att_global_spellcheck.asp
    """
    return self._report.attr.get('spellcheck', False)

  @spellcheck.setter
  def spellcheck(self, value):
    self._report.set_attrs({"spellcheck": value})

  @property
  def readonly(self):
    """
    Description:
    ------------
    The readonly attribute is a boolean attribute.

    Related Pages:

      https://www.w3schools.com/tags/att_input_readonly.asp
    """
    return self._report.attr.get('readOnly', False)

  @readonly.setter
  def readonly(self, value):
    if not value and "readOnly" in self._report.attr:
      del self._report.attr["readOnly"]

    else:
      self._report.set_attrs({"readOnly": value})

  @property
  def reset(self):
    """
    Description:
    ------------
    """
    return self.get(False)

  @reset.setter
  def reset(self, bool):
    self.set(bool)

  @property
  def select(self):
    """
    Description:
    ------------
    """
    return self.get(False)

  @select.setter
  def select(self, bool):
    self.set(bool)


class OptionsInputRange(OptionsInput):

  @property
  def output(self):
    """
    Description:
    ------------
    """
    return self._attrs.get('output', True)

  @output.setter
  def output(self, bool):
    self.set(bool)


class OptionsInputInteger(OptionsInput):

  @property
  def quantity(self):
    """
    Description:
    ------------
    """
    return self.get(False)

  @quantity.setter
  def quantity(self, bool):
    self.set(bool)
    if bool:
      self._report.quantity()


class OptionsTimePicker(OptionsInput):

  @property
  def timeFormat(self):
    """
    Description:
    ------------
    string The format of the time string displayed in the input and the menu items in the combobox. Available modifiers are:

    Related Pages:

      https://timepicker.co/options/
    """
    return self._config_get(True)

  @timeFormat.setter
  def timeFormat(self, value):
    self._config(value)

  @property
  def minTime(self):
    """
    Description:
    ------------
    A Date object or string. Only the time parts (getHours, getMinutes) of the object are important.
    Time entries before minTime won't be displayed/allowed.

    Related Pages:

      https://timepicker.co/options/
    """
    return self._config_get(True)

  @minTime.setter
  def minTime(self, value):
    self._config(value)

  @property
  def minHour(self):
    """
    Description:
    ------------
    int. Time entries with an 24-hour part before minHour won't be displayed/allowed. Ignored if minTime is set.

    Related Pages:

      https://timepicker.co/options/
    """
    return self._config_get(True)

  @minHour.setter
  def minHour(self, number):
    self._config(number)

  @property
  def minMinutes(self):
    """
    Description:
    ------------
    int Time entries with minutes part before minMinutes won't be displayed/allowed. Ignored if minTime is set.

    Related Pages:

      https://timepicker.co/options/
    """
    return self._config_get(True)

  @minMinutes.setter
  def minMinutes(self, number):
    self._config(number)

  @property
  def maxTime(self):
    """
    Description:
    ------------
    A Date object or string. Only the time parts (getHours, getMinutes) of the object are important. Time entries after minTime won't be displayed/allowed.

    Related Pages:

      https://timepicker.co/options/
    """
    return self._config_get(True)

  @maxTime.setter
  def maxTime(self, number):
    self._config(number)

  @property
  def maxHour(self):
    """
    Description:
    ------------
    int. Time entries with an 24-hour part after maxHour won't be displayed/allowed. Ignored if maxTime is set.

    Related Pages:

      https://timepicker.co/options/
    """
    return self._config_get(True)

  @maxHour.setter
  def maxHour(self, number):
    self._config(number)

  @property
  def maxMinutes(self):
    """
    Description:
    ------------
    int. Time entries with minutes part after maxHour won't be displayed/allowed. Ignored if maxTime is set.

    Related Pages:

      https://timepicker.co/options/
    """
    return self._config_get(True)

  @maxMinutes.setter
  def maxMinutes(self, number):
    self._config(number)

  @property
  def startTime(self):
    """
    Description:
    ------------
    A Date object or string. The time of the first item in the combobox when the input field is empty.
    If the input field is not empty the first item will be the next allowed time entry.

    Related Pages:

      https://timepicker.co/options/
    """
    return self._config_get(True)

  @startTime.setter
  def startTime(self, value):
    self._config(value)

  @property
  def startHour(self):
    """
    Description:
    ------------
    int The 24-hour part of the first item in the combobox when the input field is emptye.
    If input field is not empty the first item will be the next allowed time entry. Ignored if startTime is set.

    Related Pages:

      https://timepicker.co/options/
    """
    return self._config_get(True)

  @startHour.setter
  def startHour(self, number):
    self._config(number)

  @property
  def startMinutes(self):
    """
    Description:
    ------------
    int The minutes part of the first item in the combobox when the input field is emptye.
    If input field is not empty the first item will be the next allowed time entry. Ignored if startTime is set.

    Related Pages:

      https://timepicker.co/options/
    """
    return self._config_get(True)

  @startMinutes.setter
  def startMinutes(self, number):
    self._config(number)

  @property
  def interval(self):
    """
    Description:
    ------------
    int Separation in minutes between time entries in the dropdown menu.

    Related Pages:

      https://timepicker.co/options/
    """
    return self._config_get(15)

  @interval.setter
  def interval(self, value):
    self._config(value)

  @property
  def dynamic(self):
    """
    Description:
    ------------
    boolean If a date is already selected and dynamic is true, the items in the dropdown will be arranged so that the first item is chronologically right after the selected time entry.

    Related Pages:

      https://timepicker.co/options/
    """
    return self._config_get(True)

  @dynamic.setter
  def dynamic(self, bool):
    self._config(bool)

  @property
  def scrollbar(self):
    """
    Description:
    ------------
    boolean Whether the scrollbars should be displayed or not.

    Related Pages:

      https://timepicker.co/options/
    """
    return self._config_get(True)

  @scrollbar.setter
  def scrollbar(self, bool):
    self._config(bool)

  @property
  def zindex(self):
    """
    Description:
    ------------
    int The value for the z-index property of the timepicker's container <div>.

    Related Pages:

      https://timepicker.co/options/
    """
    return self._config_get(True)

  @zindex.setter
  def zindex(self, number):
    self._config(number)


class OptionAutoComplete(OptionsInput):

  @property
  def appendTo(self):
    """
    Description:
    ------------
    Which element the menu should be appended to.
    When the value is null, the parents of the input field will be checked for a class of ui-front.
    If an element with the ui-front class is found, the menu will be appended to that element.
    Regardless of the value, if no element is found, the menu will be appended to the body.

    Related Pages:

      https://api.jqueryui.com/autocomplete/#option-appendTo
    """
    return self._config_get(None)

  @appendTo.setter
  def appendTo(self, value):
    self._config(value)

  @property
  def autoFocus(self):
    """
    Description:
    ------------
    If set to true the first item will automatically be focused when the menu is shown.

    Related Pages:

      https://api.jqueryui.com/autocomplete/#option-autoFocus
    """
    return self._config_get(False)

  @autoFocus.setter
  def autoFocus(self, value):
    self._config(value)

  @property
  def classes(self):
    """
    Description:
    ------------
    Specify additional classes to add to the widget's elements.
    Any of classes specified in the Theming section can be used as keys to override their value.
    To learn more about this option, check out the learn article about the classes option.

    Related Pages:

      https://api.jqueryui.com/autocomplete/#option-classes
    """
    return self._config_get([])

  @classes.setter
  def classes(self, value):
    self._config(value)

  @property
  def delay(self):
    """
    Description:
    ------------
    The delay in milliseconds between when a keystroke occurs and when a search is performed.
    A zero-delay makes sense for local data (more responsive), but can produce a lot of load for remote data, while being less responsive.

    Related Pages:

      https://api.jqueryui.com/autocomplete/#option-delay
    """
    return self._config_get(300)

  @delay.setter
  def delay(self, value):
    self._config(value)

  @property
  def disabled(self):
    """
    Description:
    ------------
    Disables the autocomplete if set to true.

    Related Pages:

      https://api.jqueryui.com/autocomplete/#option-delay
    """
    return self._config_get(True)

  @disabled.setter
  def disabled(self, value):
    self._config(value)

  @property
  def minLength(self):
    """
    Description:
    ------------
    The minimum number of characters a user must type before a search is performed.
    Zero is useful for local data with just a few items, but a higher value should be used when a single character search could match a few thousand items.

    Related Pages:

      https://api.jqueryui.com/autocomplete/#option-minLength
    """
    return self._config_get(0)

  @minLength.setter
  def minLength(self, value):
    self._config(value)

  def position(self, my="center", at="center", of="window"):
    """
    Description:
    ------------
    Specifies where the dialog should be displayed when opened. The dialog will handle collisions such that as much of the dialog is visible as possible.

    Related Pages:

      https://api.jqueryui.com/dialog/#option-position
    """
    self._config({"my": my, "at": at, "of": of})
    return self

  @property
  def reset(self):
    """
    Description:
    ------------
    """
    return self.get(False)

  @reset.setter
  def reset(self, bool):
    self.set(bool)

  @property
  def select(self):
    """
    Description:
    ------------
    """
    return self.get(False)

  @select.setter
  def select(self, bool):
    self.set(bool)

  @property
  def source(self):
    """
    Description:
    ------------
    Defines the data to use, must be specified.

    Related Pages:

      https://api.jqueryui.com/autocomplete/#option-source
    """
    return self._config_get([])

  @source.setter
  def source(self, value):
    self._config(value)

  def startswith(self, values):
    """
    Description:
    ------------
    Defines the data to use, must be specified.
    Only display the values starting with the input text.

    Related Pages:

      https://api.jqueryui.com/autocomplete/#entry-examples

    Attributes:
    ----------
    :param values: List. The predefined values.
    """
    values = JsUtils.jsConvertData(values, None)
    self._config('''function(request, response) {
        var matcher = new RegExp("^" + $.ui.autocomplete.escapeRegex(request.term), "i");
        response($.grep(%s, function(item){return matcher.test(item);}) );
    }''' % values, "source")


class OptionsDatePicker(OptionsInput):

  @property
  def altField(self):
    """
    Description:
    ------------
    An input element that is to be updated with the selected date from the datepicker. Use the altFormat option to change the format of the date within this field. Leave as blank for no alternate field.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-altField
    """
    return self._config_get("")

  @altField.setter
  def altField(self, value):
    self._config(value)

  @property
  def altFormat(self):
    """
    Description:
    ------------
    The dateFormat to be used for the altField option. This allows one date format to be shown to the user for selection purposes, while a different format is actually sent behind the scenes. For a full list of the possible formats see the formatDate function

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-altFormat
    """
    return self._config_get("")

  @altFormat.setter
  def altFormat(self, value):
    self._config(value)

  @property
  def appendText(self):
    """
    Description:
    ------------
    The text to display after each date field, e.g., to show the required format.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-appendText
    """
    return self._config_get("")

  @appendText.setter
  def appendText(self, value):
    self._config(value)

  @property
  def autoSize(self):
    """
    Description:
    ------------
    Set to true to automatically resize the input field to accommodate dates in the current dateFormat.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-autoSize
    """
    return self._config_get(False)

  @autoSize.setter
  def autoSize(self, value):
    self._config(value)

  @property
  def beforeShow(self):
    """
    Description:
    ------------
    A function that takes an input field and current datepicker instance and returns an options object to update the datepicker with. It is called just before the datepicker is displayed.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-beforeShow
    """
    return self._config_get(None)

  @beforeShow.setter
  def beforeShow(self, value):
    self._config(value)

  @property
  def beforeShowDay(self):
    """
    Description:
    ------------
    A function that takes a date as a parameter and must return an array with:

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-beforeShowDay
    """
    return self._config_get(None)

  @beforeShowDay.setter
  def beforeShowDay(self, value):
    self._config(value)

  @property
  def buttonImage(self):
    """
    Description:
    ------------
    A URL of an image to use to display the datepicker when the showOn option is set to "button" or "both". If set, the buttonText option becomes the alt value and is not directly displayed.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-buttonImage
    """
    return self._config_get("")

  @buttonImage.setter
  def buttonImage(self, value):
    self._config(value)

  @property
  def buttonImageOnly(self):
    """
    Description:
    ------------
    Whether the button image should be rendered by itself instead of inside a button element. This option is only relevant if the buttonImage option has also been set.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-buttonImageOnly
    """
    return self._config_get(None)

  @buttonImageOnly.setter
  def buttonImageOnly(self, value):
    self._config(value)

  @property
  def buttonText(self):
    """
    Description:
    ------------
    The text to display on the trigger button. Use in conjunction with the showOn option set to "button" or "both".

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-buttonText
    """
    return self._config_get("...")

  @buttonText.setter
  def buttonText(self, value):
    self._config(value)

  @property
  def calculateWeek(self):
    """
    Description:
    ------------
    A function to calculate the week of the year for a given date. The default implementation uses the ISO 8601 definition: weeks start on a Monday; the first week of the year contains the first Thursday of the year.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-calculateWeek
    """
    return self._config_get(None)

  @calculateWeek.setter
  def calculateWeek(self, value):
    self._config(value)

  @property
  def changeMonth(self):
    """
    Description:
    ------------
    Whether the month should be rendered as a dropdown instead of text.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-changeMonth
    """
    return self._config_get(False)

  @changeMonth.setter
  def changeMonth(self, value):
    self._config(value)

  @property
  def changeYear(self):
    """
    Description:
    ------------
    Whether the year should be rendered as a dropdown instead of text. Use the yearRange option to control which years are made available for selection.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-changeYear
    """
    return self._config_get(False)

  @changeYear.setter
  def changeYear(self, value):
    self._config(value)

  @property
  def closeText(self):
    """
    Description:
    ------------
    The text to display for the close link. Use the showButtonPanel option to display this button.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-closeText
    """
    return self._config_get("Done")

  @closeText.setter
  def closeText(self, value):
    self._config(value)

  @property
  def constrainInput(self):
    """
    Description:
    ------------
    When true, entry in the input field is constrained to those characters allowed by the current dateFormat option.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-constrainInput
    """
    return self._config_get(True)

  @constrainInput.setter
  def constrainInput(self, value):
    self._config(value)

  @property
  def currentText(self):
    """
    Description:
    ------------
    The text to display for the current day link. Use the showButtonPanel option to display this button.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-currentText
    """
    return self._config_get("Today")

  @currentText.setter
  def currentText(self, value):
    self._config(value)

  @property
  def dateFormat(self):
    """
    Description:
    ------------
    The format for parsed and displayed dates. For a full list of the possible formats see the formatDate function.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-dateFormat
    """
    return self._config_get("mm/dd/yy")

  @dateFormat.setter
  def dateFormat(self, value):
    self._config(value)

  @property
  def dayNames(self):
    """
    Description:
    ------------
    The list of long day names, starting from Sunday, for use as requested via the dateFormat option.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-dayNames
    """
    return self._config_get([])

  @dayNames.setter
  def dayNames(self, value):
    self._config(value)

  @property
  def dayNamesMin(self):
    """
    Description:
    ------------
    The list of minimised day names, starting from Sunday, for use as column headers within the datepicker.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-dayNamesMin
    """
    return self._config_get([])

  @dayNamesMin.setter
  def dayNamesMin(self, value):
    self._config(value)

  @property
  def dayNamesShort(self):
    """
    Description:
    ------------
    The list of abbreviated day names, starting from Sunday, for use as requested via the dateFormat option.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-dayNamesShort
    """
    return self._config_get([])

  @dayNamesShort.setter
  def dayNamesShort(self, value):
    self._config(value)

  @property
  def defaultDate(self):
    """
    Description:
    ------------
    Set the date to highlight on first opening if the field is blank. Specify either an actual date via a Date object or as a string in the current dateFormat, or a number of days from today (e.g. +7) or a string of values and periods ('y' for years, 'm' for months, 'w' for weeks, 'd' for days, e.g. '+1m +7d'), or null for today.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-defaultDate
    """
    return self._config_get(None)

  @defaultDate.setter
  def defaultDate(self, value):
    self._config(value)

  @property
  def duration(self):
    """
    Description:
    ------------
    Control the speed at which the datepicker appears, it may be a time in milliseconds or a string representing one of the three predefined speeds ("slow", "normal", "fast").

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-duration
    """
    return self._config_get("normal")

  @duration.setter
  def duration(self, value):
    self._config(value)

  @property
  def inline(self):
    """
    Description:
    ------------
    """
    return self.get(False)

  @inline.setter
  def inline(self, bool):
    self.set(bool)

  @property
  def firstDay(self):
    """
    Description:
    ------------
    Set the first day of the week: Sunday is 0, Monday is 1, etc.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-firstDay
    """
    return self._config_get(0)

  @firstDay.setter
  def firstDay(self, value):
    self._config(value)

  @property
  def gotoCurrent(self):
    """
    Description:
    ------------
    When true, the current day link moves to the currently selected date instead of today.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-gotoCurrent
    """
    return self._config_get(False)

  @gotoCurrent.setter
  def gotoCurrent(self, value):
    self._config(value)

  @property
  def hideIfNoPrevNext(self):
    """
    Description:
    ------------
    Normally the previous and next links are disabled when not applicable (see the minDate and maxDate options). You can hide them altogether by setting this attribute to true.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-hideIfNoPrevNext
    """
    return self._config_get(False)

  @hideIfNoPrevNext.setter
  def hideIfNoPrevNext(self, value):
    self._config(value)

  @property
  def isRTL(self):
    """
    Description:
    ------------
    Whether the current language is drawn from right to left.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-isRTL
    """
    return self._config_get(False)

  @isRTL.setter
  def isRTL(self, value):
    self._config(value)

  @property
  def maxDate(self):
    """
    Description:
    ------------
    The maximum selectable date. When set to null, there is no maximum.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-maxDate
    """
    return self._config_get(None)

  @maxDate.setter
  def maxDate(self, value):
    self._config(value)

  @property
  def minDate(self):
    """
    Description:
    ------------
    The minimum selectable date. When set to null, there is no minimum.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-minDate
    """
    return self._config_get(None)

  @minDate.setter
  def minDate(self, value):
    self._config(value)

  @property
  def monthNames(self):
    """
    Description:
    ------------
    The list of full month names, for use as requested via the dateFormat option.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-monthNames
    """
    return self._config_get([])

  @monthNames.setter
  def monthNames(self, value):
    self._config(value)

  @property
  def monthNamesShort(self):
    """
    Description:
    ------------
    The list of abbreviated month names, as used in the month header on each datepicker and as requested via the dateFormat option.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-monthNamesShort
    """
    return self._config_get([])

  @monthNamesShort.setter
  def monthNamesShort(self, value):
    self._config(value)

  @property
  def navigationAsDateFormat(self):
    """
    Description:
    ------------
    Whether the currentText, prevText and nextText options should be parsed as dates by the formatDate function, allowing them to display the target month names for example.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-navigationAsDateFormat
    """
    return self._config_get(None)

  @navigationAsDateFormat.setter
  def navigationAsDateFormat(self, value):
    self._config(value)

  @property
  def nextText(self):
    """
    Description:
    ------------
    The text to display for the next month link. With the standard ThemeRoller styling, this value is replaced by an icon.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-nextText
    """
    return self._config_get("Next")

  @nextText.setter
  def nextText(self, value):
    self._config(value)

  @property
  def numberOfMonths(self):
    """
    Description:
    ------------
    The number of months to show at once.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-numberOfMonths
    """
    return self._config_get(1)

  @numberOfMonths.setter
  def numberOfMonths(self, value):
    self._config(value)

  @property
  def onChangeMonthYear(self):
    """
    Description:
    ------------
    Called when the datepicker moves to a new month and/or year. The function receives the selected year, month (1-12), and the datepicker instance as parameters. this refers to the associated input field.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-onChangeMonthYear
    """
    return self._config_get(None)

  @onChangeMonthYear.setter
  def onChangeMonthYear(self, value):
    self._config(value)

  @property
  def onClose(self):
    """
    Description:
    ------------
    Called when the datepicker is closed, whether or not a date is selected. The function receives the selected date as text ("" if none) and the datepicker instance as parameters. this refers to the associated input field.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-onClose
    """
    return self._config_get(None)

  @onClose.setter
  def onClose(self, value):
    self._config(value)

  @property
  def onSelect(self):
    """
    Description:
    ------------
    Called when the datepicker is selected. The function receives the selected date as text and the datepicker instance as parameters. this refers to the associated input field.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-onSelect
    """
    return self._config_get(None)

  @onSelect.setter
  def onSelect(self, values):
    values = JsUtils.jsConvertFncs(values, toStr=True)
    self._config("function(dateText, inst){let data = dateText; %s}" % values)

  @property
  def prevText(self):
    """
    Description:
    ------------
    The text to display for the previous month link. With the standard ThemeRoller styling, this value is replaced by an icon.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-prevText
    """
    return self._config_get("Prev")

  @prevText.setter
  def prevText(self, value):
    self._config(value)

  @property
  def selectOtherMonths(self):
    """
    Description:
    ------------
    Whether days in other months shown before or after the current month are selectable. This only applies if the showOtherMonths option is set to true.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-selectOtherMonths
    """
    return self._config_get(False)

  @selectOtherMonths.setter
  def selectOtherMonths(self, value):
    self._config(value)

  @property
  def shortYearCutoff(self):
    """
    Description:
    ------------
    The cutoff year for determining the century for a date (used in conjunction with dateFormat 'y'). Any dates entered with a year value less than or equal to the cutoff year are considered to be in the current century, while those greater than it are deemed to be in the previous century.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-shortYearCutoff
    """
    return self._config_get("+10")

  @shortYearCutoff.setter
  def shortYearCutoff(self, value):
    self._config(value)

  @property
  def showAnim(self):
    """
    Description:
    ------------
    The name of the animation used to show and hide the datepicker. Use "show" (the default), "slideDown", "fadeIn", any of the jQuery UI effects. Set to an empty string to disable animation.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-showAnim
    """
    return self._config_get("show")

  @showAnim.setter
  def showAnim(self, value):
    self._config(value)

  @property
  def showButtonPanel(self):
    """
    Description:
    ------------
    Whether to display a button pane underneath the calendar. The button pane contains two buttons, a Today button that links to the current day, and a Done button that closes the datepicker. The buttons' text can be customized using the currentText and closeText options respectively.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-showButtonPanel
    """
    return self._config_get(False)

  @showButtonPanel.setter
  def showButtonPanel(self, value):
    self._config(value)

  @property
  def showCurrentAtPos(self):
    """
    Description:
    ------------
    When displaying multiple months via the numberOfMonths option, the showCurrentAtPos option defines which position to display the current month in.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-showCurrentAtPos
    """
    return self._config_get(0)

  @showCurrentAtPos.setter
  def showCurrentAtPos(self, value):
    self._config(value)

  @property
  def showMonthAfterYear(self):
    """
    Description:
    ------------
    Whether to show the month after the year in the header.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-showMonthAfterYear
    """
    return self._config_get(False)

  @showMonthAfterYear.setter
  def showMonthAfterYear(self, value):
    self._config(value)

  @property
  def showOn(self):
    """
    Description:
    ------------
    When the datepicker should appear. The datepicker can appear when the field receives focus ("focus"), when a button is clicked ("button"), or when either event occurs ("both").

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-showOn
    """
    return self._config_get("focus")

  @showOn.setter
  def showOn(self, value):
    self._config(value)

  @property
  def showOptions(self):
    """
    Description:
    ------------
    If using one of the jQuery UI effects for the showAnim option, you can provide additional properties for that animation using this option.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-showOptions
    """
    return self._config_get({})

  @showOptions.setter
  def showOptions(self, value):
    self._config(value)

  @property
  def showOtherMonths(self):
    """
    Description:
    ------------
    Whether to display dates in other months (non-selectable) at the start or end of the current month. To make these days selectable use the selectOtherMonths option.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-showOtherMonths
    """
    return self._config_get(False)

  @showOtherMonths.setter
  def showOtherMonths(self, value):
    self._config(value)

  @property
  def showWeek(self):
    """
    Description:
    ------------
    When true, a column is added to show the week of the year. The calculateWeek option determines how the week of the year is calculated. You may also want to change the firstDay option.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-showWeek
    """
    return self._config_get(False)

  @showWeek.setter
  def showWeek(self, value):
    self._config(value)

  @property
  def stepMonths(self):
    """
    Description:
    ------------
    Set how many months to move when clicking the previous/next links.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-stepMonths
    """
    return self._config_get(1)

  @stepMonths.setter
  def stepMonths(self, value):
    self._config(value)

  @property
  def weekHeader(self):
    """
    Description:
    ------------
    The text to display for the week of the year column heading. Use the showWeek option to display this column.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-weekHeader
    """
    return self._config_get("wk")

  @weekHeader.setter
  def weekHeader(self, value):
    self._config(value)

  @property
  def yearRange(self):
    """
    Description:
    ------------
    The range of years displayed in the year drop-down: either relative to today's year ("-nn:+nn"), relative to the currently selected year ("c-nn:c+nn"), absolute ("nnnn:nnnn"), or combinations of these formats ("nnnn:-nn"). Note that this option only affects what appears in the drop-down, to restrict which dates may be selected use the minDate and/or maxDate options.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-yearRange
    """
    return self._config_get("c-10:c+10")

  @yearRange.setter
  def yearRange(self, value):
    self._config(value)

  @property
  def yearSuffix(self):
    """
    Description:
    ------------
    Additional text to display after the year in the month headers.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-yearSuffix
    """
    return self._config_get("")

  @yearSuffix.setter
  def yearSuffix(self, value):
    self._config(value)


class OptionsTextarea(OptionsInput):

  @property
  def rows(self):
    """
    Description:
    ------------
    The rows attribute specifies the visible height of a text area, in lines.

    Related Pages:

      https://www.w3schools.com/tags/att_rows.asp
    """
    return self._report.attr.get('rows', "")

  @rows.setter
  def rows(self, value):
    self._report.set_attrs({"rows": value})

