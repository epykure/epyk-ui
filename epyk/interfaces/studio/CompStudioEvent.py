#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core import html


class Event(object):
  def __init__(self, context):
    self.parent = context

  def flip(self):
    """
    https://www.w3schools.com/howto/howto_css_flip_box.asp
    :return:
    """
