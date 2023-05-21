
from typing import Union, Any
from epyk.core.py import primitives
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObject
from epyk.core.js.packages import JsPackage


class SettingsCurreny:
  symbol = "$"
  decimal = "."
  thousand = ","
  precision = 2
  format = "%s%v"

  def toStr(self):
    return 'accounting.settings.currency = {"precision": %s, "decimal": %s, "thousand": %s, "symbol": %s, "format": %s}' % (
      JsUtils.jsConvertData(self.precision, None),
      JsUtils.jsConvertData(self.decimal, None),
      JsUtils.jsConvertData(self.thousand, None),
      JsUtils.jsConvertData(self.symbol, None),
      JsUtils.jsConvertData(self.format, None),
    )


class SettingsNumber:
  precision = 0
  decimal = "."
  thousand = ","

  def toStr(self):
    return 'accounting.settings.number = {"precision": %s, "decimal": %s, "thousand": %s}' % (
      JsUtils.jsConvertData(self.precision, None),
      JsUtils.jsConvertData(self.decimal, None),
      JsUtils.jsConvertData(self.thousand, None)
    )


class AccountingSettings:

  def __init__(self):
    self.__number = SettingsNumber()
    self.__currency = SettingsCurreny()

  @property
  def currency(self) -> SettingsCurreny:
    return self.__currency

  @property
  def number(self) -> SettingsNumber:
    return self.__number


class Accounting(JsPackage):
  lib_alias = {'js': 'accounting'}

  def __init__(self, component: primitives.HtmlModel = None, page: primitives.PageModel = None, js_code: str = None,
               selector: str = None, data: Any = None, set_var: bool = None):
    super(Accounting, self).__init__(component, page, js_code, selector, data, set_var)
    self.__settings = AccountingSettings()

  def formatMoney(
    self,
    value,
    symbol: str = None,
    digits: int = None,
    sep_thousand: str = None,
    sep_decimal: str = None,
    format_expr: Union[str, dict] = None
  ) -> JsObject.JsObject:
    """
    The most basic library function for formatting numbers as money values, with customisable currency symbol,
    precision (decimal places), and thousand / decimal separators

    Related Pages:

      http://openexchangerates.github.io/accounting.js/
      http://openexchangerates.github.io/accounting.js/#documentation

    :param value:
    :param symbol: default currency symbol is '$'
    :param digits: default precision on numbers is 2
    :param sep_thousand: thousands separator
    :param sep_decimal: decimal point separator
    :param format_expr: controls output: %s = symbol, %v = value/number (can be object: see below)
    """
    value = JsUtils.jsConvertData(value, None)
    symbol = JsUtils.jsConvertData(symbol, None)
    digits = JsUtils.jsConvertData(digits, None)
    sep_thousand = JsUtils.jsConvertData(sep_thousand, None)
    sep_decimal = JsUtils.jsConvertData(sep_decimal, None)
    format_expr = JsUtils.jsConvertData(format_expr, None)
    return JsObject.JsObject.get("accounting.formatMoney(%s, %s, %s, %s, %s, %s)" % (
      value, symbol, digits, sep_thousand, sep_decimal, format_expr))

  def formatColumn(self, value, digits: int = None, sep_thousand: str = None) -> JsObject.JsObject:
    """
    The base function of the library, which takes any number or array of numbers, runs accounting.unformat() to
    remove any formatting, and returns the number(s) formatted with separated thousands and custom precision

    Related Pages:

      http://openexchangerates.github.io/accounting.js/
      http://openexchangerates.github.io/accounting.js/#documentation

    :param value:
    :param digits: default precision on numbers is 0
    :param sep_thousand: thousands separator
    """
    value = JsUtils.jsConvertData(value, None)
    digits = JsUtils.jsConvertData(digits, None)
    sep_thousand = JsUtils.jsConvertData(sep_thousand, None)
    return JsObject.JsObject.get("accounting.formatColumn(%s, %s, %s)" % (value, digits, sep_thousand))

  def formatNumber(self, value, digits: int = None, sep_thousand: str = None) -> JsObject.JsObject:
    """
    The base function of the library, which takes any number or array of numbers, runs accounting.unformat()
    to remove any formatting, and returns the number(s) formatted with separated thousands and custom precision:

    Related Pages:

      http://openexchangerates.github.io/accounting.js/
      http://openexchangerates.github.io/accounting.js/#documentation

    :param value:
    :param digits: default precision on numbers is 0
    :param sep_thousand: thousands separator
    """
    value = JsUtils.jsConvertData(value, None)
    digits = JsUtils.jsConvertData(digits, None)
    sep_thousand = JsUtils.jsConvertData(sep_thousand, None)
    return JsObject.JsObject.get("accounting.formatNumber(%s, %s, %s)" % (value, digits, sep_thousand))

  def toFixed(self, value, digits: int = None) -> JsObject.JsObject:
    """
    Implementation of toFixed() that treats floats more like decimal values than binary,
    fixing inconsistent precision rounding in JavaScript (where some .05 values round up, while others round down)

    Related Pages:

      http://openexchangerates.github.io/accounting.js/

    :param value:
    :param digits: default precision on numbers is 0
    """
    value = JsUtils.jsConvertData(value, None)
    digits = JsUtils.jsConvertData(digits, None)
    return JsObject.JsObject.get("accounting.toFixed(%s, %s)" % (value, digits))

  def unformat(self, value) -> JsObject.JsObject:
    """
    Takes any number and removes all currency formatting. Aliased as accounting.parse()

    Related Pages:

      http://openexchangerates.github.io/accounting.js/

    :param value:
    """
    value = JsUtils.jsConvertData(value, None)
    return JsObject.JsObject.get("accounting.unformat(%s)" % value)

  @property
  def settings(self):
    """
    Settings object that controls default parameters for library methods:

    Related Pages:

      http://openexchangerates.github.io/accounting.js/#documentation
    """
    return self.__settings
