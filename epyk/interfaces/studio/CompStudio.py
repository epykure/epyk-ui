#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core import html

from epyk.interfaces.studio import CompStudioBlog
from epyk.interfaces.studio import CompStudioShopping


class Sudio(object):
  def __init__(self, context):
    self.context = context

  @property
  def shop(self):
    return CompStudioShopping.Shopping(self)

  @property
  def blog(self):
    return CompStudioBlog.Blog(self)
