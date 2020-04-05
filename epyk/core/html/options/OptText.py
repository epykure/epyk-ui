
from epyk.core.data import DataClass


class OptionsText(DataClass):

  @property
  def reset(self):
    """
    Description:
    ------------

    Related Pages:
    --------------
    """
    return self._attrs.get('reset', False)

  @reset.setter
  def reset(self, bool):
    self._report._jsStyles["reset"] = bool
    return self.set(bool)

  @property
  def markdown(self):
    """
    Description:
    ------------

    Related Pages:
    --------------
    """
    return self._attrs.get('markdown', False)

  @markdown.setter
  def markdown(self, bool):
    self._report._jsStyles["markdown"] = bool
    return self.set(bool)

  @property
  def limit_char(self):
    """
    Description:
    ------------

    Related Pages:
    --------------
    """
    return self._attrs.get('limit_char')

  @limit_char.setter
  def limit_char(self, value):
    self._report._jsStyles["maxlength"] = value
    return self.set(value)


class OptionsTitle(OptionsText):

  @property
  def content_table(self):
    """
    Description:
    ------------

    Related Pages:
    --------------
    """
    return self._attrs.get('content_table', True)

  @content_table.setter
  def content_table(self, bool):
    return self.set(bool)


class OptionsNumber(OptionsText):

  @property
  def digits(self):
    """
    Description:
    ------------
    decimal point separator

    Related Pages:
    --------------
    http://openexchangerates.github.io/accounting.js/
    """
    return self._report._jsStyles.get("digits", 0)

  @digits.setter
  def digits(self, num):
    self._report._jsStyles["digits"] = num
    return self

  @property
  def format(self):
    """
    Description:
    ------------
    controls output: %s = symbol, %v = value/number

    Related Pages:
    --------------
    http://openexchangerates.github.io/accounting.js/
    """
    return self._report._jsStyles.get("format", "%s%v")

  @format.setter
  def format(self, num):
    self._report._jsStyles["format"] = num
    return self

  @property
  def symbol(self):
    """
    Description:
    ------------
    default currency symbol is ''

    Related Pages:
    --------------
    http://openexchangerates.github.io/accounting.js/#documentation
    """
    return self._report._jsStyles.get("symbol", "")

  @symbol.setter
  def symbol(self, value):
    self._report._jsStyles["type_number"] = "money"
    self._report._jsStyles["symbol"] = value
    return self

  @property
  def thousand_sep(self):
    """
    Description:
    ------------
    thousands separator

    Related Pages:
    --------------
    http://openexchangerates.github.io/accounting.js/
    """
    return self._report._jsStyles.get("thousand_sep", ",")

  @thousand_sep.setter
  def thousand_sep(self, value):
    self._report._jsStyles["thousand_sep"] = value
    return self

  @property
  def decimal_sep(self):
    """
    Description:
    ------------
    decimal point separator

    Related Pages:
    --------------
    http://openexchangerates.github.io/accounting.js/
    """
    return self._report._jsStyles.get("decimal_sep", ".")

  @decimal_sep.setter
  def decimal_sep(self, value):
    self._report._jsStyles["decimal_sep"] = value
    return self

