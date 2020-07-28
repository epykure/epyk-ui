#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.interfaces.studio import CompStudioBlog
from epyk.interfaces.studio import CompStudioShopping
from epyk.interfaces.studio import CompStudioNews


class Sudio(object):
  def __init__(self, context):
    self.context = context

  @property
  def shop(self):
    """
    Description:
    ------------
    Property for all the components designed to be used in a e-commerce website
    """
    return CompStudioShopping.Shopping(self)

  @property
  def blog(self):
    """
    Description:
    ------------
    Property for all the components to be used in a blog website
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
    return CompStudioNews.News(self)
