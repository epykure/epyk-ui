
from epyk.core.js.packages import packageImport
from epyk.core.data import DataClass


class OptionsInput(DataClass):

  def css(self, attrs):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param attrs: Dictionary. CSS attributes
    """
    self._report._jsStyles["css"] = attrs
    return self

  @packageImport("accounting")
  def formatMoney(self, symbol="", digit=0, thousand_sep=".", decimal_sep=","):
    """
    Description:
    -----------
    Format any number into currency

    Related Pages:
    --------------
    http://openexchangerates.github.io/accounting.js/

    Attributes:
    ----------
    :param symbol: String. custom symbol
    :param digit: Integer. Number of digit
    :param thousand_sep: String. The thousand separator
    :param decimal_sep: String. The decimal separator
    """
    self._report._jsStyles["formatMoney"] = {"symbol": symbol, 'digit': digit, "thousand": thousand_sep, "decimal": decimal_sep}
    return self

  @packageImport("accounting")
  def formatNumber(self, digit=0, thousand_sep="."):
    """
    Description:
    -----------
    Format a number with custom precision and localisation

    Related Pages:
    --------------
    http://openexchangerates.github.io/accounting.js/

    Attributes:
    ----------
    :param digit: Integer. Number of digit
    :param thousand_sep: String. The thousand separator
    """
    self._report._jsStyles["formatNumber"] = {'digit': digit, "thousand": thousand_sep}
    return self

  @packageImport("accounting")
  def toFixed(self, digit=0):
    """
    Description:
    -----------
    Better rounding for floating point numbers

    Related Pages:
    --------------
    http://openexchangerates.github.io/accounting.js/

    Attributes:
    ----------
    :param digit: Integer. Number of digit
    """
    self._report._jsStyles["toFixed"] = digit
    return self

  def __init__(self, report, attrs=None, options=None):
    super(OptionsInput, self).__init__(report, attrs, options)
    if attrs is not None:
      self._report._jsStyles.update(attrs)


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
    return self.set(bool)


class OptionsTimePicker(OptionsInput):

  @property
  def timeFormat(self):
    """
    Description:
    ------------
    string The format of the time string displayed in the input and the menu items in the combobox. Available modifiers are:

    Related Pages:
    --------------
    https://timepicker.co/options/
    """
    return self._report._jsStyles.get('timeFormat', True)

  @timeFormat.setter
  def timeFormat(self, value):
    self._report._jsStyles["timeFormat"] = value
    return self

  @property
  def minTime(self):
    """
    Description:
    ------------
    A Date object or string. Only the time parts (getHours, getMinutes) of the object are important.
    Time entries before minTime won't be displayed/allowed.

    Related Pages:
    --------------
    https://timepicker.co/options/
    """
    return self._report._jsStyles.get('minTime', True)

  @minTime.setter
  def minTime(self, value):
    self._report._jsStyles["minTime"] = value
    return self

  @property
  def minHour(self):
    """
    Description:
    ------------
    int. Time entries with an 24-hour part before minHour won't be displayed/allowed. Ignored if minTime is set.

    Related Pages:
    --------------
    https://timepicker.co/options/
    """
    return self._report._jsStyles.get('minHour', True)

  @minHour.setter
  def minHour(self, number):
    self._report._jsStyles["minHour"] = number
    return self

  @property
  def minMinutes(self):
    """
    Description:
    ------------
    int Time entries with minutes part before minMinutes won't be displayed/allowed. Ignored if minTime is set.

    Related Pages:
    --------------
    https://timepicker.co/options/
    """
    return self._report._jsStyles.get('minMinutes', True)

  @minMinutes.setter
  def minMinutes(self, number):
    self._report._jsStyles["minMinutes"] = number
    return self

  @property
  def maxTime(self):
    """
    Description:
    ------------
    A Date object or string. Only the time parts (getHours, getMinutes) of the object are important. Time entries after minTime won't be displayed/allowed.

    Related Pages:
    --------------
    https://timepicker.co/options/
    """
    return self._report._jsStyles.get('maxTime', True)

  @maxTime.setter
  def maxTime(self, number):
    self._report._jsStyles["maxTime"] = number
    return self

  @property
  def maxHour(self):
    """
    Description:
    ------------
    int. Time entries with an 24-hour part after maxHour won't be displayed/allowed. Ignored if maxTime is set.

    Related Pages:
    --------------
    https://timepicker.co/options/
    """
    return self._report._jsStyles.get('maxHour', True)

  @maxHour.setter
  def maxHour(self, number):
    self._report._jsStyles["maxHour"] = number
    return self

  @property
  def maxMinutes(self):
    """
    Description:
    ------------
    int. Time entries with minutes part after maxHour won't be displayed/allowed. Ignored if maxTime is set.

    Related Pages:
    --------------
    https://timepicker.co/options/
    """
    return self._report._jsStyles.get('maxMinutes', True)

  @maxMinutes.setter
  def maxMinutes(self, number):
    self._report._jsStyles["maxMinutes"] = number
    return self

  @property
  def startTime(self):
    """
    Description:
    ------------
    A Date object or string. The time of the first item in the combobox when the input field is empty.
    If the input field is not empty the first item will be the next allowed time entry.

    Related Pages:
    --------------
    https://timepicker.co/options/
    """
    return self._report._jsStyles.get('startTime', True)

  @startTime.setter
  def startTime(self, value):
    self._report._jsStyles["startTime"] = value
    return self

  @property
  def startHour(self):
    """
    Description:
    ------------
    int The 24-hour part of the first item in the combobox when the input field is emptye.
    If input field is not empty the first item will be the next allowed time entry. Ignored if startTime is set.

    Related Pages:
    --------------
    https://timepicker.co/options/
    """
    return self._report._jsStyles.get('startHour', True)

  @startHour.setter
  def startHour(self, number):
    self._report._jsStyles["startHour"] = number
    return self

  @property
  def startMinutes(self):
    """
    Description:
    ------------
    int The minutes part of the first item in the combobox when the input field is emptye.
    If input field is not empty the first item will be the next allowed time entry. Ignored if startTime is set.

    Related Pages:
    --------------
    https://timepicker.co/options/
    """
    return self._report._jsStyles.get('startMinutes', True)

  @startMinutes.setter
  def startMinutes(self, number):
    self._report._jsStyles["startMinutes"] = number
    return self

  @property
  def interval(self):
    """
    Description:
    ------------
    int Separation in minutes between time entries in the dropdown menu.

    Related Pages:
    --------------
    https://timepicker.co/options/
    """
    return self._report._jsStyles.get('interval', 15)

  @interval.setter
  def interval(self, value):
    self._report._jsStyles["interval"] = value
    return self

  @property
  def dynamic(self):
    """
    Description:
    ------------
    boolean If a date is already selected and dynamic is true, the items in the dropdown will be arranged so that the first item is chronologically right after the selected time entry.

    Related Pages:
    --------------
    https://timepicker.co/options/
    """
    return self._report._jsStyles.get('dynamic', True)

  @dynamic.setter
  def dynamic(self, bool):
    self._report._jsStyles["dynamic"] = bool
    return self

  @property
  def scrollbar(self):
    """
    Description:
    ------------
    boolean Whether the scrollbars should be displayed or not.

    Related Pages:
    --------------
    https://timepicker.co/options/
    """
    return self._report._jsStyles.get('scrollbar', True)

  @scrollbar.setter
  def scrollbar(self, bool):
    self._report._jsStyles["scrollbar"] = bool
    return self

  @property
  def zindex(self):
    """
    Description:
    ------------
    int The value for the z-index property of the timepicker's container <div>.

    Related Pages:
    --------------
    https://timepicker.co/options/
    """
    return self._report._jsStyles.get('zindex', True)

  @zindex.setter
  def zindex(self, number):
    self._report._jsStyles["zindex"] = number
    return self
