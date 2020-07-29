#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.interfaces.studio import CompStudioBlog
from epyk.interfaces.studio import CompStudioShopping
from epyk.interfaces.studio import CompStudioNews
from epyk.interfaces.studio import CompStudioDashboard
from epyk.interfaces.studio import CompStudioManagement
from epyk.interfaces.studio import CompStudioVitrine


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
  def vitrine(self):
    """
    Description:
    ------------
    """
    return CompStudioVitrine.Vitrine(self)

  @property
  def management(self):
    """
    Description:
    ------------
    """
    return CompStudioManagement.Management(self)

  @property
  def dashboards(self):
    """
    Description:
    ------------
    """
    return CompStudioDashboard.Dashboard(self)

  @property
  def news(self):
    """
    Description:
    ------------
    """
    return CompStudioNews.News(self)
