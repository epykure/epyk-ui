
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
    return self._config_get(False, 'showdown')

  @markdown.setter
  @packageImport("showdown")
  def markdown(self, values):
    values = {} if values is True else values
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
    values = {} if values is True else values
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
    self._report._jsStyles["type_number"] = "money"
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
    return self._attrs.get('timestamp', False)

  @timestamp.setter
  def timestamp(self, bool):
    self.set(bool)
