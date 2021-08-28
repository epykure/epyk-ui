
from epyk.core.html.options import Options
from epyk.core.html.options import Enums


class EnumInputTypes(Enums):

  def selectbox(self):
    """
    Description:
    ------------

    Related Pages:

      https://nhn.github.io/tui.time-picker/latest/TimePicker
    """
    self._set_value()

  def spinbox(self):
    """
    Description:
    ------------

    Related Pages:

      https://nhn.github.io/tui.time-picker/latest/TimePicker
    """
    self._set_value()


class OptionTime(Options):

  @property
  def initialHour(self):
    """
    Description:
    ------------
    Initial setting value of hour

    Related Pages:

      https://nhn.github.io/tui.time-picker/latest/TimePicker
    """
    return self._config_get()

  @initialHour.setter
  def initialHour(self, num):
    self._config(num)

  @property
  def initialMinute(self):
    """
    Description:
    ------------
    Initial setting value of minute.

    Related Pages:

      https://nhn.github.io/tui.time-picker/latest/TimePicker
    """
    return self._config_get()

  @initialMinute.setter
  def initialMinute(self, num):
    self._config(num)

  @property
  def hourStep(self):
    """
    Description:
    ------------
    Step value of hour.

    Related Pages:

      https://nhn.github.io/tui.time-picker/latest/TimePicker
    """
    return self._config_get()

  @hourStep.setter
  def hourStep(self, num):
    self._config(num)

  @property
  def minuteStep(self):
    """
    Description:
    ------------
    Step value of minute.

    Related Pages:

      https://nhn.github.io/tui.time-picker/latest/TimePicker
    """
    return self._config_get()

  @minuteStep.setter
  def minuteStep(self, num):
    self._config(num)

  @property
  def inputType(self):
    """
    Description:
    ------------
    'selectbox' or 'spinbox'.

    Related Pages:

      https://nhn.github.io/tui.time-picker/latest/TimePicker
    """
    return self._config_get()

  @inputType.setter
  def inputType(self, text):
    self._config(text)

  @property
  def inputTypes(self):
    """
    Description:
    ------------
    'selectbox' or 'spinbox'.

    Related Pages:

      https://nhn.github.io/tui.time-picker/latest/TimePicker
    """
    return EnumInputTypes(self, "inputType")

  @property
  def format(self):
    """
    Description:
    ------------
    hour, minute format for display.

    Related Pages:

      https://nhn.github.io/tui.time-picker/latest/TimePicker
    """
    return self._config_get()

  @format.setter
  def format(self, text):
    self._config(text)

  @property
  def showMeridiem(self):
    """
    Description:
    ------------
    Show meridiem expression?.

    Related Pages:

      https://nhn.github.io/tui.time-picker/latest/TimePicker
    """
    return self._config_get()

  @showMeridiem.setter
  def showMeridiem(self, flag):
    self._config(flag)

  @property
  def disabledHours(self):
    """
    Description:
    ------------
    Registered Hours is disabled.

    Related Pages:

      https://nhn.github.io/tui.time-picker/latest/TimePicker
    """
    return self._config_get()

  @disabledHours.setter
  def disabledHours(self, values):
    self._config(values)

  @property
  def disabledMinutes(self):
    """
    Description:
    ------------
    Registered Minutes of selected hours is disabled.

    Related Pages:

      https://nhn.github.io/tui.time-picker/latest/TimePicker
    """
    return self._config_get()

  @disabledMinutes.setter
  def disabledMinutes(self, values):
    self._config(values)

  @property
  def meridiemPosition(self):
    """
    Description:
    ------------
    Set location of the meridiem element.
    If this option set 'left', the meridiem element is created in front of the hour element.

    Related Pages:

      https://nhn.github.io/tui.time-picker/latest/TimePicker
    """
    return self._config_get()

  @meridiemPosition.setter
  def meridiemPosition(self, text):
    self._config(text)

  @property
  def language(self):
    """
    Description:
    ------------
    SSet locale texts.

    Related Pages:

      https://nhn.github.io/tui.time-picker/latest/TimePicker
    """
    return self._config_get()

  @language.setter
  def language(self, text):
    self._config(text)

  @property
  def usageStatistics(self):
    """
    Description:
    ------------
    send hostname to google analytics default value is true.

    Related Pages:

      https://nhn.github.io/tui.time-picker/latest/TimePicker
    """
    return self._config_get()

  @usageStatistics.setter
  def usageStatistics(self, flag):
    self._config(flag)
