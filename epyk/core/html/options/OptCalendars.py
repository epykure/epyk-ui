#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html.options import Options


class OptionDays(Options):

  @property
  def style(self):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param css_attrs: Dictionary. CSS attributes
    """
    return self.get({})

  @style.setter
  def style(self, css_attrs):
    self.set(css_attrs)

  @property
  def overload(self):
    """
    Description:
    ------------
    Overload style of the day number when workload is above 100%

    Attributes:
    ----------
    :param css_attrs: Dictionary. CSS attributes
    """
    return self.get({})

  @overload.setter
  def overload(self, css_attrs):
    self.set(css_attrs)

  @property
  def number(self):
    """
    Description:
    ------------
    CSS Style for the day number

    Attributes:
    ----------
    :param css_attrs: Dictionary. CSS attributes
    """
    return self.get({})

  @number.setter
  def number(self, css_attrs):
    self.set(css_attrs)

  @property
  def today(self):
    """
    Description:
    ------------
    CSS Style for the today cell

    Attributes:
    ----------
    :param css_attrs: Dictionary. CSS attributes
    """
    return self.get({})

  @today.setter
  def today(self, css_attrs):
    self.set(css_attrs)

  @property
  def header(self):
    """
    Description:
    ------------
    CSS Style for the table header

    Attributes:
    ----------
    :param css_attrs: Dictionary. CSS attributes
    """
    return self.get({})

  @header.setter
  def header(self, css_attrs):
    self.set(css_attrs)
