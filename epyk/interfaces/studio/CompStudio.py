#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.interfaces.studio import CompStudioBlog
from epyk.interfaces.studio import CompStudioShopping


class Sudio(object):
  def __init__(self, context):
    self.context = context

  @property
  def shop(self):
    """
    Description:
    ------------
    Property for all the component designed to be used in a e-commerce website
    """
    return CompStudioShopping.Shopping(self)

  @property
  def blog(self):
    """
    Description:
    ------------

    """
    return CompStudioBlog.Blog(self)

  @property
  def commercial(self):
    """
    Description:
    ------------
    """
    return

  @property
  def management(self):
    """
    Description:
    ------------
    """
    return

  @property
  def dashboards(self):
    """
    Description:
    ------------
    """
    return

  @property
  def news(self):
    """
    Description:
    ------------
    """
    return
