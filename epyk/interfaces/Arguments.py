#!/usr/bin/python
# -*- coding: utf-8 -*-


def size(value, unit="%"):
  """
  Description:
  ------------
  Wrapper to allow size arguments to be more flexible.
  By using this in the interface it is possible to then use float values instead of the usual tuples.

  Attributes:
  ----------
  :param value: Integer. The value for this argument
  :param unit: String. Optional. The unit for the argument. Default %
  """
  if isinstance(value, tuple):
    return value

  elif value == "auto":
    return (value, '')

  return (value, unit)


class Align(object):
  """
  A string with the horizontal position of the component
  """

  @property
  def center(self):
    return "center"

  @property
  def left(self):
    return "left"

  @property
  def right(self):
    return "right"


class Position(object):
  """
  A string with the vertical position of the component
  """

  @property
  def top(self):
    return "top"

  @property
  def bottom(self):
    return "bottom"

  @property
  def middle(self):
    return "middle"


class Size(object):
  """
  A tuple with the integer for the component size and its unit

  """

  @property
  def auto(self):
    return "auto", ''

  def px(self, value):
    return value, 'px'

  def percent(self, value):
    return value, '%'


class Color(object):
  """
  The font color in the component. Default inherit
  """

  @property
  def white(self):
    return ""


class Profile(object):
  """
  A flag to set the component performance storage
  """

  @property
  def true(self):
    return True

  def name(self, name):
    return {"name": name}


ICON = "The component icon content from font-awesome references"
COLOR = Color()
WIDTH = Size()
HEIGHT = Size() # "A tuple with the integer for the component height and its unit"
PROFILE = Profile()
OPTIONS = "Specific Python options available for this component"
ALIGN = Align()
POSITION = Position()

DSC_TOP = "The top property affects the vertical position of a positioned element."
DSC_LEFT = "The left property affects the horizontal position of a positioned element."
DSC_RIGHT = "The right property affects the horizontal position of a positioned element."
DSC_LABEL = "The text of label to be added to the component"
DSC_HELPER = "A tooltip helper"
DSC_TOOLTIP = "A string with the value of the tooltip"
DSC_JSFNCS = "The Javascript functions"
DSC_HTMLCODE = "An identifier for this component (on both Python and Javascript side)"