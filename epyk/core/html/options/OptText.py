#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html.options import Options
from epyk.core.js.packages import packageImport


class OptionsText(Options):

  @property
  def editable(self):
    """
    Description:
    ------------
    Set the content of the component editable

    Related Pages:

      https://www.w3schools.com/tags/att_global_contenteditable.asp
    """
    return self._report.attr.get("contenteditable", False)

  @editable.setter
  def editable(self, bool):
    self._report._report.body.style.contenteditable()
    self._report.attr["contenteditable"] = bool
    if bool:
      self.spellcheck = False

  @property
  def spellcheck(self):
    """
    Description:
    ------------
    The spellcheck attribute specifies whether the element is to have its spelling and grammar checked or not.

    Related Pages:

      https://www.w3schools.com/tags/att_global_spellcheck.asp
    """
    return self._report.attr.get("spellcheck", False)

  @spellcheck.setter
  def spellcheck(self, bool):
    self._report._report.body.style.contenteditable()
    self._report.attr["spellcheck"] = bool

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
    return self._config_get(self._report._report.theme.success[1])

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
    return self._config_get(self._report._report.theme.warning[1])

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

  @property
  def status(self):
    return self._config_get('none')

  @status.setter
  def status(self, value):
    if hasattr(self._report._report.theme, str(value)):
      color = getattr(self._report._report.theme, str(value))[1]
    else:
      color = self._report._report.theme.colors[-1]
    self._report.style.css.border_left = '5px solid %s' % color
    self._report.style.css.padding_left = 5
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


class OptionsLink(OptionsText):

  @property
  def url(self):
    """
    Description:
    ------------
    The href attribute specifies the URL of the page the link goes to.

    Related Pages:

      https://www.w3schools.com/tags/att_a_href.asp
    """
    return self._report.attr.get("href", '#')

  @url.setter
  def url(self, value):
    self._report.attr['href'] = value

  @property
  def href(self):
    """
    Description:
    ------------
    The href attribute specifies the URL of the page the link goes to.

    Related Pages:

      https://www.w3schools.com/tags/att_a_href.asp
    """
    return self._report.attr.get("href", '#')

  @href.setter
  def href(self, value):
    self._report.attr['href'] = value

  @property
  def target(self):
    """
    Description:
    ------------
    The target attribute specifies where to open the linked document.

    Related Pages:

      https://www.w3schools.com/tags/att_a_target.asp
    """
    return self._report.attr.get("target", '_self')

  @target.setter
  def target(self, value):
    self._report.attr['target'] = value


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
