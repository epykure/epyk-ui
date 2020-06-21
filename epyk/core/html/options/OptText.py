
from epyk.core.html.options import Options
from epyk.core.js.packages import packageImport


class OptionsText(Options):

  @property
  def reset(self):
    """
    Description:
    ------------

    Related Pages:
"""
    return self._config_get(False)

  @reset.setter
  def reset(self, bool):
    self._config(bool)

  @property
  def markdown(self):
    """
    Description:
    ------------
    Showdown is a Javascript Markdown to HTML converter, based on the original works by John Gruber.
    Showdown can be used client side (in the browser) or server side (with NodeJs).

    Related Pages:

      https://github.com/showdownjs/showdown
    """
    return self._config_get(False)

  @markdown.setter
  @packageImport("showdown")
  def markdown(self, values):
    if isinstance(values, bool):
      self._config(values)
      self._config({} if values is True else values, 'showdown')
    else:
      self._config(True)
      self._config(values, 'showdown')

  @property
  def showdown(self):
    """
    Description:
    ------------
    Showdown is a Javascript Markdown to HTML converter, based on the original works by John Gruber.
    Showdown can be used client side (in the browser) or server side (with NodeJs).

    Related Pages:

      https://github.com/showdownjs/showdown
    """
    return self._config_get(False)

  @showdown.setter
  @packageImport("showdown")
  def showdown(self, values):
    self._config(True, 'markdown')
    self._config(values)

  @property
  def limit_char(self):
    """
    Description:
    ------------

    Related Pages:
"""
    return self._config_get(None, 'limit_char')

  @limit_char.setter
  def limit_char(self, value):
    self._config(value, "maxlength")

  @property
  def red(self):
    """
    Description:
    ------------

    Related Pages:
"""
    return self._config_get(self._report.theme.danger[1])

  @red.setter
  def red(self, value):
    self._config(value)

  @property
  def green(self):
    """
    Description:
    ------------

    Related Pages:
"""
    return self._config_get(self._report.theme.success[1])

  @green.setter
  def green(self, value):
    self._config(value)

  @property
  def orange(self):
    """
    Description:
    ------------

    Related Pages:
"""
    return self._config_get(self._report.theme.warning[1])

  @orange.setter
  def orange(self, value):
    self._config(value)

  @property
  def font_size(self):
    """
    Description:
    ------------

    Related Pages:
"""
    return self._config_get('none')

  @font_size.setter
  def font_size(self, value):
    self._config(value)


class OptionsTitle(OptionsText):

  @property
  def content_table(self):
    """
    Description:
    ------------

    Related Pages:
"""
    return self._config_get(True)

  @content_table.setter
  def content_table(self, bool):
    self._config(bool)


class OptionsNumber(OptionsText):

  @property
  def digits(self):
    """
    Description:
    ------------
    decimal point separator

    Related Pages:
http://openexchangerates.github.io/accounting.js/
    """
    return self._config_get(0)

  @digits.setter
  def digits(self, num):
    self._config(num)

  @property
  def format(self):
    """
    Description:
    ------------
    controls output: %s = symbol, %v = value/number

    Related Pages:
http://openexchangerates.github.io/accounting.js/
    """
    return self._config_get("%s%v")

  @format.setter
  def format(self, num):
    self._config(num)

  @property
  def symbol(self):
    """
    Description:
    ------------
    default currency symbol is ''

    Related Pages:
http://openexchangerates.github.io/accounting.js/#documentation
    """
    return self._config_get("")

  @symbol.setter
  def symbol(self, value):
    self._config("money", name="type_number")
    self._config(value)

  @property
  def thousand_sep(self):
    """
    Description:
    ------------
    thousands separator

    Related Pages:
http://openexchangerates.github.io/accounting.js/
    """
    return self._config_get(",")

  @thousand_sep.setter
  def thousand_sep(self, value):
    self._config(value)

  @property
  def decimal_sep(self):
    """
    Description:
    ------------
    decimal point separator

    Related Pages:
http://openexchangerates.github.io/accounting.js/
    """
    return self._config_get(".")

  @decimal_sep.setter
  def decimal_sep(self, value):
    self._config(value)


class OptionsConsole(OptionsText):

  @property
  def timestamp(self):
    """
    Description:
    ------------
    """
    return self.get(False)

  @timestamp.setter
  def timestamp(self, bool):
    self.set(bool)


class OptionsComposite(Options):

  @property
  def reset_class(self):
    """
    Description:
    ------------
    """
    return self.get(False)

  @reset_class.setter
  def reset_class(self, bool):
    self.set(bool)


class OptionsStatus(Options):

  @property
  def states(self):
    """
    Description:
    ------------
    """
    return self.get(False)

  @states.setter
  def states(self, bool):
    self.set(bool)

  @property
  def color(self):
    """
    Description:
    ------------
    """
    return self.get('white')

  @color.setter
  def color(self, color):
    self.set(color)

  @property
  def background(self):
    """
    Description:
    ------------
    """
    return self.get('grey')

  @background.setter
  def background(self, color):
    self.set(color)
