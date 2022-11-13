
from epyk.core.js.packages import packageImport
from epyk.core.html.options import Options

from epyk.core.js import JsUtils


class OptionsInput(Options):

  @property
  def autocomplete(self):
    """
    The input autocomplete attribute specifies whether a form or an input field should have autocomplete on or off.

    Related Pages:

      https://www.w3schools.com/tags/att_textarea_maxlength.asp
    """
    return self.component.attr.get('autocomplete')

  @autocomplete.setter
  def autocomplete(self, flag: bool):
    if flag:
      self.component.set_attrs({"autocomplete": "on"})
    else:
      self.component.set_attrs({"autocomplete": "off"})

  @property
  def autofocus(self):
    """
    The input autofocus attribute specifies that an input field should automatically get focus when the page loads.

    Related Pages:

      https://www.w3schools.com/tags/att_textarea_maxlength.asp
    """
    return self.component.attr.get('autofocus')

  @autofocus.setter
  def autofocus(self, flag: bool):
    if not flag and "autofocus" in self.component.attr:
      del self.component.attr["autofocus"]

    else:
      self.component.set_attrs({"autofocus": flag})

  def css(self, attrs: dict):
    """   

    :param attrs: Dictionary. CSS attributes
    """
    self._config(attrs)
    return self

  @property
  def borders(self):
    """

    """
    return self._config_get("all")

  @borders.setter
  def borders(self, value: str):
    self._config(value)

  @property
  def disabled(self):
    """
    The rows attribute specifies the visible height of a text area, in lines.

    Related Pages:

      https://www.w3schools.com/tags/att_rows.asp
    """
    return self.component.attr.get('disabled', False)

  @disabled.setter
  def disabled(self, value):
    if not value and "disabled" in self.component.attr:
      del self.component.attr["disabled"]

    else:
      self.component.set_attrs({"disabled": value})

  @packageImport("accounting")
  def formatMoney(self, symbol="", digits=0, thousand_sep=".", decimal_sep=","):
    """   Format any number into currency

    Related Pages:

      http://openexchangerates.github.io/accounting.js/

    :param symbol: String. custom symbol
    :param digits: Integer. Number of digit
    :param thousand_sep: String. The thousand separator
    :param decimal_sep: String. The decimal separator
    """
    self._config({"symbol": symbol, 'digit': digits, "thousand": thousand_sep, "decimal": decimal_sep})
    return self

  @packageImport("accounting")
  def formatNumber(self, digit=0, thousand_sep="."):
    """   Format a number with custom precision and localisation

    Related Pages:

      http://openexchangerates.github.io/accounting.js/

    :param digit: Integer. Number of digit
    :param thousand_sep: String. The thousand separator
    """
    self._config({'digit': digit, "thousand": thousand_sep})
    return self

  @packageImport("accounting")
  def toFixed(self, digit=0):
    """   Better rounding for floating point numbers

    Related Pages:

      http://openexchangerates.github.io/accounting.js/

    :param digit: Integer. Number of digit
    """
    self._config(digit)
    return self

  @property
  def background(self):
    """
    Specifies the maximum number of characters allowed in the text area

    Related Pages:

      https://www.w3schools.com/tags/att_textarea_maxlength.asp
    """
    return self.get(True)

  @background.setter
  def background(self, flag: bool):
    self.set(flag)

  @property
  def maxlength(self):
    """
    Specifies the maximum number of characters allowed in the text area

    Related Pages:

      https://www.w3schools.com/tags/att_textarea_maxlength.asp
    """
    return self.component.attr.get('maxlength')

  @maxlength.setter
  def maxlength(self, num: int):
    self.component.set_attrs({"maxlength": num})

  @property
  def name(self):
    """
    Specifies a name for a text area

    Related Pages:

      https://www.w3schools.com/tags/att_textarea_name.asp
    """
    return self.component.attr.get('name')

  @name.setter
  def name(self, num):
    self.component.set_attrs({"name": num})

  @property
  def pattern(self):
    """
    The input pattern attribute specifies a regular expression that the input field's value is checked against,
    when the form is submitted.

    Related Pages:

      https://www.w3schools.com/html/html_form_attributes.asp
    """
    return self.component.attr.get('pattern')

  @pattern.setter
  def pattern(self, value: str):
    self.component.set_attrs({"pattern": value})

  @property
  def placeholder(self):
    """
    The placeholder attribute specifies a short hint that describes the expected value of an input field
    (e.g. a sample value or a short description of the expected format).

    Related Pages:

      https://www.w3schools.com/tags/att_input_placeholder.asp
    """
    return self.component.attr.get('placeholder', "")

  @placeholder.setter
  def placeholder(self, value):
    self.component.set_attrs({"placeholder": value})

  @property
  def required(self):
    """
    Specifies that a text area is required/must be filled out

    Related Pages:

      https://www.w3schools.com/tags/att_textarea_required.asp
    """
    return self.component.attr.get('required')

  @required.setter
  def required(self, flag: bool):
    if not flag and "required" in self.component.attr:
      del self.component.attr["required"]

    else:
      self.component.set_attrs({"required": flag})

  @property
  def wrap(self):
    """
    Specifies how the text in a text area is to be wrapped when submitted in a form.

    Related Pages:

      https://www.w3schools.com/tags/att_textarea_wrap.asp
    """
    return self.component.attr.get('wrap', "")

  @wrap.setter
  def wrap(self, value):
    self.component.set_attrs({"wrap": value})

  @property
  def spellcheck(self):
    """
    The spellcheck attribute specifies whether the element is to have its spelling and grammar checked or not.

    Related Pages:

      https://www.w3schools.com/tags/att_global_spellcheck.asp
    """
    return self.component.attr.get('spellcheck', False)

  @spellcheck.setter
  def spellcheck(self, value: bool):
    self.component.set_attrs({"spellcheck": value})

  @property
  def readonly(self):
    """
    The readonly attribute is a boolean attribute.

    Related Pages:

      https://www.w3schools.com/tags/att_input_readonly.asp
    """
    return self.component.attr.get('readOnly', False)

  @readonly.setter
  def readonly(self, value: bool):
    if not value and "readOnly" in self.component.attr:
      del self.component.attr["readOnly"]

    else:
      self.component.set_attrs({"readOnly": value})

  @property
  def reset(self):
    """
    """
    return self.get(False)

  @reset.setter
  def reset(self, flag: bool):
    self.set(flag)

  @property
  def select(self):
    """
    """
    return self.get(False)

  @select.setter
  def select(self, flag: bool):
    self.set(flag)

  @property
  def step(self):
    """ The input step attribute specifies the legal number intervals for an input field.

    Related Pages:

      https://www.w3schools.com/html/html_form_attributes.asp
    """
    return self.component.attr.get('step')

  @step.setter
  def step(self, num: int):
    self.component.set_attrs({"pattern": num})


class OptionsInputRange(OptionsInput):

  @property
  def output(self):
    """
    """
    return self._attrs.get('output', True)

  @output.setter
  def output(self, flag: bool):
    self.set(flag)


class OptionsInputInteger(OptionsInput):

  @property
  def quantity(self):
    """
    """
    return self.get(False)

  @quantity.setter
  def quantity(self, flag):
    self.set(flag)
    if flag:
      self.component.quantity()


class OptionsTimePicker(OptionsInput):
  component_properties = ('listWidth', )

  @property
  def appendTo(self):
    """
    Override where the dropdown is appended.

    Takes either a string to use as a selector, a function that gets passed the clicked input element as argument or a
    jquery object to use directly.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery
    """
    return self._config_get("body")

  @appendTo.setter
  def appendTo(self, value):
    self._config(value)

  @property
  def className(self):
    """
    A class name to apply to the HTML element that contains the timepicker dropdown.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery
    """
    return self._config_get(None)

  @className.setter
  def className(self, value):
    self._config(value)

  @property
  def closeOnWindowScroll(self):
    """
    Close the timepicker when the window is scrolled. (Replicates <select> behavior.)

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery
    """
    return self._config_get(False)

  @closeOnWindowScroll.setter
  def closeOnWindowScroll(self, value: bool):
    self._config(value)

  def disableTimeRanges(self, values):
    """
    Disable selection of certain time ranges. Input is an array of time pairs,
    like [['3:00am', '4:30am'], ['5:00pm', '8:00pm']].

    The start of the interval will be disabled but the end won't.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery
    """
    return self._config(values)

  @property
  def disableTextInput(self):
    """
    Disable typing in the timepicker input box; force users to select from list.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery
    """
    return self._config_get(False)

  @disableTextInput.setter
  def disableTextInput(self, flag):
    self._config(flag)

  @property
  def disableTouchKeyboard(self):
    """
    Disable the onscreen keyboard for touch devices. There can be instances where Firefox or Chrome have touch events
    enabled (such as on Surface tablets but not actually be a touch device.
    In this case disableTouchKeyboard will prevent the timepicker input field from being focused.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery
    """
    return self._config_get(False)

  @disableTouchKeyboard.setter
  def disableTouchKeyboard(self, flag: bool):
    self._config(flag)

  @property
  def durationTime(self):
    """
    The time against which showDuration will compute relative times. Accepts a time string, Date object,
    integer seconds from midnight, or a function that returns one of those types.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery
    """
    return self._config_get(None)

  @durationTime.setter
  def durationTime(self, value):
    self._config(value)

  @property
  def forceRoundTime(self):
    """
    Force update the time to step settings as soon as it loses focus.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery
    """
    return self._config_get(False)

  @forceRoundTime.setter
  def forceRoundTime(self, flag: bool):
    self._config(flag)

  @property
  def lang(self):
    """
    Language constants used in the timepicker. Can override the defaults by passing an object with one or more of the
    following properties: decimal, mins, hr, hrs.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery
    """
    return self._config_get(None)

  @lang.setter
  def lang(self, mapping):
    self._config(mapping)

  @property
  def listWidth(self):
    """
    Set this to override CSS styling and set the list width to match the input element's width. Set to 1 to match input
    width, 2 to double input width, .5 to halve input width, etc. Set to null to let CSS determine the list width.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery
    """
    return self._config_get(1)

  @listWidth.setter
  def listWidth(self, num: int):
    self._config(num)

  @property
  def maxTime(self):
    """
    The time that should appear last in the dropdown list. Can be used to limit the range of time options.
    Accepts a time string, Date object, integer seconds from midnight, or a function that returns one of those types.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery
    """
    return self._config_get("24 hours after minTime")

  @maxTime.setter
  def maxTime(self, value: str):
    self._config(value)

  @property
  def minTime(self):
    """
    The time that should appear first in the dropdown list.
    Accepts a time string, Date object, integer seconds from midnight, or a function that returns one of those types.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery
    """
    return self._config_get("12:00am")

  @minTime.setter
  def minTime(self, value: str):
    self._config(value)

  @property
  def noneOption(self):
    """
    Adds one or more custom options to the top of the dropdown.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery
    """
    return self._config_get(False)

  @noneOption.setter
  def noneOption(self, value):
    self._config(value)

  @property
  def orientation(self):
    """
    By default the timepicker dropdown will be aligned to the bottom right of the input element,
    or aligned to the top left if there isn't enough room below the input.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery
    """
    return self._config_get("l")

  @orientation.setter
  def orientation(self, value):
    self._config(value)

  def roundingFunction(self):
    """
    Function used to compute rounded times. The function will receive time in seconds and a settings object as
    arguments. The function should handle a null value for seconds. default: round to nearest step.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery
    """
    return self._config_get("l")

  @property
  def scrollDefault(self):
    """
    If no time value is selected, set the dropdown scroll position to show the time provided, e.g. "09:00".
    Accepts a time string, Date object, integer seconds from midnight, or a function that returns one of those types.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery
    """
    return self._config_get(None)

  @scrollDefault.setter
  def scrollDefault(self, value):
    self._config(value)

  @property
  def selectOnBlur(self):
    """
    Update the input with the currently highlighted time value when the timepicker loses focus.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery
    """
    return self._config_get(False)

  @selectOnBlur.setter
  def selectOnBlur(self, flag: bool):
    self._config(flag)

  @property
  def show2400(self):
    """
    Show "24:00" as an option when using 24-hour time format. You must also set timeFormat for this option to work.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery
    """
    return self._config_get(False)

  @show2400.setter
  def show2400(self, flag: bool):
    self._config(flag)

  @property
  def showDuration(self):
    """
    Shows the relative time for each item in the dropdown. minTime or durationTime must be set.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery
    """
    return self._config_get(False)

  @showDuration.setter
  def showDuration(self, flag: bool):
    self._config(flag)

  @property
  def showOn(self):
    """
    Display a timepicker dropdown when the input fires a particular event.
    Set to null or an empty array to disable automatic display.
    Setting should be an array of strings. default: ['focus'].

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery
    """
    return self._config_get(False)

  @showOn.setter
  def showOn(self, flag: bool):
    self._config(flag)

  @property
  def step(self):
    """
    The amount of time, in minutes, between each item in the dropdown.
    Alternately, you can specify a function to generate steps dynamically.
    The function will receive a count integer (0, 1, 2...) and is expected to return a step integer.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery
    """
    return self._config_get(30)

  @step.setter
  def step(self, num: int):
    self._config(num)

  @property
  def stopScrollPropagation(self):
    """
    When scrolling on the edge of the picker, it prevent parent containers () to scroll.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery
    """
    return self._config_get(False)

  @stopScrollPropagation.setter
  def stopScrollPropagation(self, flag: bool):
    self._config(flag)

  @property
  def timeFormat(self):
    """
    How times should be displayed in the list and input element. Uses PHP's date() formatting syntax.
    Characters can be escaped with a preceeding double slash (e.g. H\\hi).

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery
    """
    return self._config_get('g:ia')

  @timeFormat.setter
  def timeFormat(self, value: str):
    self._config(value)

  @property
  def typeaheadHighlight(self):
    """
    Highlight the nearest corresponding time option as a value is typed into the form input.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery
    """
    return self._config_get(True)

  @typeaheadHighlight.setter
  def typeaheadHighlight(self, flag: bool):
    self._config(flag)

  @property
  def useSelect(self):
    """
    Convert the input to an HTML <SELECT> control. This is ideal for small screen devices,
    or if you want to prevent the user from entering arbitrary values.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery
    """
    return self._config_get(True)

  @useSelect.setter
  def useSelect(self, flag: bool):
    self._config(flag)

  @property
  def wrapHours(self):
    """
    If a time greater than 24 hours (27:30, for example) is entered, apply modolo 24 to create a valid time.
    Setting this to false will cause an input of 27:30 to result in a timeFormatError event.

    Related Pages:

      https://github.com/jonthornton/jquery-timepicker#timepicker-plugin-for-jquery
    """
    return self._config_get(True)

  @wrapHours.setter
  def wrapHours(self, flag: bool):
    self._config(flag)


class OptionAutoComplete(OptionsInput):

  @property
  def appendTo(self):
    """
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
    If set to true the first item will automatically be focused when the menu is shown.

    Related Pages:

      https://api.jqueryui.com/autocomplete/#option-autoFocus
    """
    return self._config_get(False)

  @autoFocus.setter
  def autoFocus(self, value: bool):
    self._config(value)

  @property
  def classes(self):
    """
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
    The delay in milliseconds between when a keystroke occurs and when a search is performed.
    A zero-delay makes sense for local data (more responsive), but can produce a lot of load for remote data,
    while being less responsive.

    Related Pages:

      https://api.jqueryui.com/autocomplete/#option-delay
    """
    return self._config_get(300)

  @delay.setter
  def delay(self, value: int):
    self._config(value)

  @property
  def disabled(self):
    """
    Disables the autocomplete if set to true.

    Related Pages:

      https://api.jqueryui.com/autocomplete/#option-delay
    """
    return self._config_get(True)

  @disabled.setter
  def disabled(self, value: bool):
    self._config(value)

  @property
  def minLength(self):
    """
    The minimum number of characters a user must type before a search is performed.
    Zero is useful for local data with just a few items, but a higher value should be used when a single character
    search could match a few thousand items.

    Related Pages:

      https://api.jqueryui.com/autocomplete/#option-minLength
    """
    return self._config_get(0)

  @minLength.setter
  def minLength(self, value: int):
    self._config(value)

  def position(self, my="left top", at="left bottom", of=None, using=None, within=None, collision=None):
    """
    Specifies where the dialog should be displayed when opened.
    The dialog will handle collisions such that as much of the dialog is visible as possible.

    Related Pages:

      https://api.jqueryui.com/dialog/#option-position
      https://api.jqueryui.com/position/

    :param my: String. Optional. Defines which position on the element being positioned to align with the target element.
    :param at: String. Optional. Defines which position on the target element to align the positioned element against.
    :param of: String. Optional. Which element to position against. If you provide a selector or jQuery object, the first matching element will be used.
    :param using: String. Optional. When specified, the actual property setting is delegated to this callback. Receives two parameters:
    :param within: String. Optional. Element to position within, affecting collision detection
    :param collision: String. Optional. When the positioned element overflows the window in some direction, move it to an alternative position.
    """
    props = {"my": my, "at": at, "collision": collision or "flip"}
    if of is not None:
      props["of"] = of
    if using is not None:
      props["using"] = using
    if within is not None:
      props["within"] = within
    self._config(props)
    return self

  @property
  def reset(self):
    """
    """
    return self.get(False)

  @reset.setter
  def reset(self, flag: bool):
    self.set(flag)

  def on_select(self, js_funcs, profile=None):
    """   Triggered when an item is selected from the menu.
    The default action is to replace the text field's value with the value of the selected item.

    Related Pages:

      https://api.jqueryui.com/autocomplete/#event-select

    :param js_funcs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    js_funcs = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    self._config("function(e, ui) {var value = ui.item.value; %s}" % js_funcs, js_type=True, name="select")

  @property
  def source(self):
    """
    Defines the data to use, must be specified.

    Related Pages:

      https://api.jqueryui.com/autocomplete/#option-source
    """
    return self._config_get([])

  @source.setter
  def source(self, value):
    self._config(value)

  def startswith(self, values: list):
    """
    Defines the data to use, must be specified.
    Only display the values starting with the input text.

    Related Pages:

      https://api.jqueryui.com/autocomplete/#entry-examples

    :param values: The predefined values.
    """
    values = JsUtils.jsConvertData(values, None)
    self._config('''function(request, response) {
        var matcher = new RegExp("^" + $.ui.autocomplete.escapeRegex(request.term), "i");
        response($.grep(%s, function(item){return matcher.test(item);}) );
    }''' % values, "source", js_type=True)


class OptionsDatePicker(OptionsInput):

  @property
  def altField(self):
    """
    An input element that is to be updated with the selected date from the DatePicker.
    Use the altFormat option to change the format of the date within this field. Leave as blank for no alternate field.

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
    The dateFormat to be used for the altField option.
    This allows one date format to be shown to the user for selection purposes, while a different format is actually
    sent behind the scenes. For a full list of the possible formats see the formatDate function.

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
    Set to true to automatically resize the input field to accommodate dates in the current dateFormat.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-autoSize
    """
    return self._config_get(False)

  @autoSize.setter
  def autoSize(self, value: bool):
    self._config(value)

  @property
  def beforeShow(self):
    """
    A function that takes an input field and current DatePicker instance and returns an options object to update the
    DatePicker with. It is called just before the DatePicker is displayed.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-beforeShow
    """
    return self._config_get(None)

  @beforeShow.setter
  def beforeShow(self, value):
    """
    A function that takes a date as a parameter and must return an array with:

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-beforeShowDay
    """
    self._config(value)

  def beforeShowDay(self, js_funcs, profile=None):
    self._config("function (value){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile), js_type=True)

  @property
  def buttonImage(self):
    """
    A URL of an image to use to display the DatePicker when the showOn option is set to "button" or "both".
    If set, the buttonText option becomes the alt value and is not directly displayed.

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
    Whether the button image should be rendered by itself instead of inside a button element.
    This option is only relevant if the buttonImage option has also been set.

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
    The text to display on the trigger button. Use in conjunction with the showOn option set to "button" or "both".

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-buttonText
    """
    return self._config_get("...")

  @buttonText.setter
  def buttonText(self, value: str):
    self._config(value)

  @property
  def calculateWeek(self):
    """
    A function to calculate the week of the year for a given date.
    The default implementation uses the ISO 8601 definition:
    weeks start on a Monday; the first week of the year contains the first Thursday of the year.

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
    Whether the month should be rendered as a DropDown instead of text.

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
    Whether the year should be rendered as a DropDown instead of text.
    Use the yearRange option to control which years are made available for selection.

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
    The list of long day names, starting from Sunday, for use as requested via the dateFormat option.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-dayNames
    """
    return self._config_get([])

  def dateJsOvr(self, js_funcs=None, profile=None):
    if js_funcs is None:
      self._config("new Date()", js_type=True)
    elif js_funcs == 'COB':
      self._config(''' (function(){var cob = new Date(); var days = cob.getDay(); 
          if(days == 1){cob.setDate(cob.getDate() - 3)} else { cob.setDate(cob.getDate() - 1)}; return cob})()''',
                   js_type=True)
    else:
      self._config("function (value){%s}" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile), js_type=True)

  @dayNames.setter
  def dayNames(self, value):
    self._config(value)

  @property
  def dayNamesMin(self):
    """
    The list of minimised day names, starting from Sunday, for use as column headers within the DatePicker.

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
    Set the date to highlight on first opening if the field is blank.
    Specify either an actual date via a Date object or as a string in the current dateFormat, or a number of days
    from today (e.g. +7) or a string of values and periods ('y' for years, 'm' for months, 'w' for weeks, 'd'
    for days, e.g. '+1m +7d'), or null for today.

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
    Control the speed at which the DatePicker appears, it may be a time in milliseconds or a string representing one
    of the three predefined speeds ("slow", "normal", "fast").

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
    """
    return self.get(False)

  @inline.setter
  def inline(self, flag: bool):
    self.set(flag)

  @property
  def firstDay(self):
    """
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
    Normally the previous and next links are disabled when not applicable (see the minDate and maxDate options).
    You can hide them altogether by setting this attribute to true.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-hideIfNoPrevNext
    """
    return self._config_get(False)

  @hideIfNoPrevNext.setter
  def hideIfNoPrevNext(self, value: bool):
    self._config(value)

  @property
  def isRTL(self):
    """
    Whether the current language is drawn from right to left.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-isRTL
    """
    return self._config_get(False)

  @isRTL.setter
  def isRTL(self, value: bool):
    self._config(value)

  @property
  def maxDate(self):
    """
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
    The list of abbreviated month names, as used in the month header on each DatePicker and as requested via the
    dateFormat option.

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
    Whether the currentText, prevText and nextText options should be parsed as dates by the formatDate function,
    allowing them to display the target month names for example.

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
    The text to display for the next month link. With the standard ThemeRoller styling,
    this value is replaced by an icon.

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
    Called when the DatePicker moves to a new month and/or year.
    The function receives the selected year, month (1-12), and the DatePicker instance as parameters.
    this refers to the associated input field.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-onChangeMonthYear
    """
    return self._config_get(None)

  @onChangeMonthYear.setter
  def onChangeMonthYear(self, value):
    self._config(value)

  def onClose(self, values, profile=False):
    """
    Called when the DatePicker is closed, whether or not a date is selected.
    The function receives the selected date as text ("" if none) and the DatePicker instance as parameters.
    This refers to the associated input field.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-onClose

    :param values:
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    values = JsUtils.jsConvertFncs(values, toStr=True, profile=profile)
    self._config("function(dateText, inst){let data = dateText; %s}" % values, js_type=True)

  def onSelect(self, values, profile=False):
    """
    Called when the DatePicker is selected.
    The function receives the selected date as text and the DatePicker instance as parameters.
    this refers to the associated input field.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-onSelect

    :param values:
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    values = JsUtils.jsConvertFncs(values, toStr=True, profile=profile)
    self._config("function(dateText, inst){let data = dateText; %s}" % values, js_type=True)

  @property
  def prevText(self):
    """
    The text to display for the previous month link. With the standard ThemeRoller styling, this value is replaced
    by an icon.

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
    Whether days in other months shown before or after the current month are selectable. This only applies if
    the showOtherMonths option is set to true.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-selectOtherMonths
    """
    return self._config_get(False)

  @selectOtherMonths.setter
  def selectOtherMonths(self, value: bool):
    self._config(value)

  @property
  def shortYearCutoff(self):
    """
    The cutoff year for determining the century for a date (used in conjunction with dateFormat 'y'). Any dates
    entered with a year value less than or equal to the cutoff year are considered to be in the current century,
    while those greater than it are deemed to be in the previous century.

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
    The name of the animation used to show and hide the datepicker. Use "show" (the default), "slideDown", "fadeIn",
    any of the jQuery UI effects. Set to an empty string to disable animation.

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
    Whether to display a button pane underneath the calendar. The button pane contains two buttons, a Today button
    that links to the current day, and a Done button that closes the datepicker. The buttons' text can be customized
    using the currentText and closeText options respectively.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-showButtonPanel
    """
    return self._config_get(False)

  @showButtonPanel.setter
  def showButtonPanel(self, value: bool):
    self._config(value)

  @property
  def showCurrentAtPos(self):
    """
    When displaying multiple months via the numberOfMonths option, the showCurrentAtPos option defines which position
    to display the current month in.

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
    Whether to show the month after the year in the header.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-showMonthAfterYear
    """
    return self._config_get(False)

  @showMonthAfterYear.setter
  def showMonthAfterYear(self, value: bool):
    self._config(value)

  @property
  def showOn(self):
    """
    When the datepicker should appear. The datepicker can appear when the field receives focus ("focus"),
    when a button is clicked ("button"), or when either event occurs ("both").

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-showOn
    """
    return self._config_get("focus")

  @showOn.setter
  def showOn(self, value: bool):
    self._config(value)

  @property
  def showOptions(self):
    """
    If using one of the jQuery UI effects for the showAnim option, you can provide additional properties for
    that animation using this option.

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
    Whether to display dates in other months (non-selectable) at the start or end of the current month.
    To make these days selectable use the selectOtherMonths option.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-showOtherMonths
    """
    return self._config_get(False)

  @showOtherMonths.setter
  def showOtherMonths(self, value: bool):
    self._config(value)

  @property
  def showWeek(self):
    """
    When true, a column is added to show the week of the year. The calculateWeek option determines how the week of
    the year is calculated. You may also want to change the firstDay option.

    Related Pages:

      https://api.jqueryui.com/datepicker/#option-showWeek
    """
    return self._config_get(False)

  @showWeek.setter
  def showWeek(self, value: bool):
    self._config(value)

  @property
  def stepMonths(self):
    """
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
    The range of years displayed in the year drop-down: either relative to today's year ("-nn:+nn"),
    relative to the currently selected year ("c-nn:c+nn"), absolute ("nnnn:nnnn"),
    or combinations of these formats ("nnnn:-nn"). Note that this option only affects what appears in the drop-down,
    to restrict which dates may be selected use the minDate and/or maxDate options.

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
    The rows attribute specifies the visible height of a text area, in lines.

    Related Pages:

      https://www.w3schools.com/tags/att_rows.asp
    """
    return self.component.attr.get('rows', "")

  @rows.setter
  def rows(self, value):
    self.component.set_attrs({"rows": value})


class OptionsInputFile(OptionsInput):

  @property
  def accept(self):
    """
    The rows attribute specifies the visible height of a text area, in lines.

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/file
    """
    return self.component.attr.get('accept', "")

  @accept.setter
  def accept(self, value):
    self.component.set_attrs({"accept": value})

  @property
  def multiple(self):
    """

    Related Pages:

      https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/file
    """
    return self.component.attr.get('multiple', "")

  @multiple.setter
  def multiple(self, value):
    self.component.set_attrs({"multiple": value})
