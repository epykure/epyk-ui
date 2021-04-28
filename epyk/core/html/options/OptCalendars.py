#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html.options import Options


class OptionDays(Options):

  @property
  def style(self):
    """
    Description:
    ------------

    Usage::

    Attributes:
    ----------
    :prop css: Dictionary. CSS attributes
    """
    return self.get({})

  @style.setter
  def style(self, css):
    self.set(css)

  @property
  def unit(self):
    """
    Description:
    ------------
    Change the unit to the calendar.
    Default is in percentage.

    Usage::

    Attributes:
    ----------
    :prop num: Float. Change the scale
    """
    return self.get(100)

  @unit.setter
  def unit(self, num):
    self.set(num)

  @property
  def overload(self):
    """
    Description:
    ------------
    Overload style of the day number when workload is above 100%.

    Usage::

    Attributes:
    ----------
    :prop css_attrs: Dictionary. CSS attributes.
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
    CSS Style for the day number.

    Usage::

    Attributes:
    ----------
    :prop css: Dictionary. CSS attributes.
    """
    return self.get({})

  @number.setter
  def number(self, css):
    self.set(css)

  @property
  def today(self):
    """
    Description:
    ------------
    CSS Style for the today cell.

    Usage::

    Attributes:
    ----------
    :prop css: Dictionary. CSS attributes
    """
    return self.get({})

  @today.setter
  def today(self, css):
    self.set(css)

  @property
  def header(self):
    """
    Description:
    ------------
    CSS Style for the table header.

    Usage::

    Attributes:
    ----------
    :prop css: Dictionary. CSS attributes.
    """
    return self.get({})

  @header.setter
  def header(self, css):
    self.set(css)


class OptionDatePicker(Options):
  pass
