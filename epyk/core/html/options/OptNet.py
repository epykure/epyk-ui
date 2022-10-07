
from typing import Union
from epyk.core.html.options import Options
from epyk.core.js.packages import packageImport


class OptionsNews(Options):

  @property
  def dated(self):
    """
    Check default value for radio and check lists
    """
    return self._config_get(True)

  @dated.setter
  def dated(self, flag: bool):
    if flag:
      self.component.jsImports.add('moment')
    self._config(flag)

  @property
  def classes(self):
    """
    Check default value for radio and check lists
    """
    return self._config_get([])

  @classes.setter
  def classes(self, class_names: list):
    self._config(class_names)

  @property
  def markdown(self):
    """
    Showdown is a Javascript Markdown to HTML converter, based on the original works by John Gruber.
    Showdown can be used client side (in the browser) or server side (with NodeJs).

    Related Pages:

      https://github.com/showdownjs/showdown
    """
    return self._config_get(False, 'showdown')

  @markdown.setter
  @packageImport("showdown")
  def markdown(self, values):
    values = {} if values is True else values
    self._config(values, 'showdown')


class OptionsAlert(Options):

  @property
  def time(self):
    """
    Set the time in milliseconds before hidden the popup.
    If None the popup will not hide progressively.

    Usage::

      danger = page.ui.network.warning()
      danger.options.time = None

    :prop num: Integer. The time in millisecond. Default 1000.
    """
    return self._config_get(1000)

  @time.setter
  def time(self, num: int):
    self._config(num)

  @property
  def delay(self):
    """
    The delay between the event and the display of the popup.
    THe time is in millisecond.

    Usage::

      danger = page.ui.network.warning()
      danger.options.delay = 100

    :prop num: Integer. The time in millisecond. Default 1000.
    """
    return self._config_get(1000)

  @delay.setter
  def delay(self, attrs: Union[dict, int]):
    self._config(attrs)

  @property
  def close(self):
    """
    """
    return self._config_get(True)

  @close.setter
  def close(self, flag: bool):
    if flag:
      self.component.jsImports.add("font-awesome")
      self.component.cssImport.add("font-awesome")
    self._config(flag)

  @property
  def type(self):
    """
    """
    return self._config_get(None)

  @type.setter
  def type(self, value):
    self._config(value)

  @property
  def markdown(self):
    """
    Showdown is a Javascript Markdown to HTML converter, based on the original works by John Gruber.
    Showdown can be used client side (in the browser) or server side (with NodeJs).

    Related Pages:

      https://github.com/showdownjs/showdown
    """
    return self._config_get(False, 'showdown')

  @markdown.setter
  @packageImport("showdown")
  def markdown(self, values):
    values = {} if values is True else values
    self._config(values, 'showdown')


class OptionsChat(Options):

  @property
  def dated(self):
    """
    Check default value for radio and check lists
    """
    return self._config_get(True)

  @dated.setter
  def dated(self, flag: bool):
    if flag:
      self.component.jsImports.add('moment')
    self._config(flag)

  @property
  def readonly(self):
    """
    Check default value for radio and check lists
    """
    return self._config_get(True)

  @readonly.setter
  def readonly(self, flag: bool):
    self._config(flag)

  @property
  def markdown(self):
    """
    Showdown is a Javascript Markdown to HTML converter, based on the original works by John Gruber.
    Showdown can be used client side (in the browser) or server side (with NodeJs).

    Related Pages:

      https://github.com/showdownjs/showdown
    """
    return self._config_get(False, 'showdown')

  @markdown.setter
  @packageImport("showdown")
  def markdown(self, values):
    values = {} if values is True else values
    self._config(values, 'showdown')


class OptionFiles(Options):

  @property
  def text(self):
    """
    Display comment for the loaded files.
    THis should be activated only when one file can be loaded.
    """
    return self._config_get(True)

  @text.setter
  def text(self, flag: bool):
    self._config(flag)

  @property
  def extensions(self):
    """
    List all the allowed file extensions
    """
    return self._config_get(None)

  @extensions.setter
  def extensions(self, values):
    self._config(values)

  @property
  def delimiter(self):
    """
    The file Delimiter for columns
    """
    return self._config_get(None)

  @delimiter.setter
  def delimiter(self, values):
    self._config(values)

  @property
  def format(self):
    """
    The file Delimiter for columns
    """
    return self._config_get("text")

  @format.setter
  def format(self, values):
    self._config(values)
