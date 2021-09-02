
from epyk.core.html.options import Options
from epyk.core.html.options import Enums


class EnumFormatTypes(Enums):

  def time_only(self):
    """
    Description:
    ------------

    Related Pages:

      https://getdatepicker.com/5-4/Usage/#custom-icons
    """
    self._set_value(value="LT")

  def date_only(self):
    """
    Description:
    ------------

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

      https://getdatepicker.com/5-4/Usage/#custom-icons
    """
    self._set_value()


class DTIcons(Options):

  @property
  def time(self):
    """
    Description:
    -----------

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


class DT(Options):

  @property
  def allowMultidate(self):
    """
    Description:
    -----------

    https://getdatepicker.com/5-4/Usage/#custom-icons

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

    https://getdatepicker.com/5-4/Usage/#custom-icons

    """
    return self._config_get()

  @daysOfWeekDisabled.setter
  def daysOfWeekDisabled(self, values):
    self._config(values)

  @property
  def format(self):
    """
    Description:
    -----------

    https://getdatepicker.com/5-4/Usage/#custom-icons

    """
    return self._config_get()

  @format.setter
  def format(self, text):
    self._config(text)

  @property
  def formats(self):
    return EnumFormatTypes(self, "format")

  @property
  def icons(self):
    """

    :rtype: DTIcons
    """
    return self._config_sub_data("icons", DTIcons)

  @property
  def inline(self):
    """
    Description:
    -----------

    https://getdatepicker.com/5-4/Usage/#custom-icons

    """
    return self._config_get()

  @inline.setter
  def inline(self, flag):
    self._config(flag)

  @property
  def multidateSeparator(self):
    """
    Description:
    -----------

    https://getdatepicker.com/5-4/Usage/#custom-icons

    """
    return self._config_get()

  @multidateSeparator.setter
  def multidateSeparator(self, text):
    self._config(text)

  @property
  def sideBySide(self):
    """
    Description:
    -----------

    https://getdatepicker.com/5-4/Usage/#custom-icons

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

    https://getdatepicker.com/5-4/Usage/#custom-icons

    """
    return self._config_get()

  @useCurrent.setter
  def useCurrent(self, flag):
    self._config(flag)