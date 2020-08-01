#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.interfaces.studio import CompStudioBlog
from epyk.interfaces.studio import CompStudioShopping
from epyk.interfaces.studio import CompStudioNews
from epyk.interfaces.studio import CompStudioDashboard
from epyk.interfaces.studio import CompStudioManagement
from epyk.interfaces.studio import CompStudioVitrine
from epyk.interfaces.studio import CompStudioEvent


class Studio(object):
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
  def restaurant(self):
    """
    Description:
    ------------
    Property for all the components designed to be used in a e-commerce website
    """
    return CompStudioShopping.Resto(self)

  @property
  def blog(self):
    """
    Description:
    ------------
    Property for all the components to be used in a blog website
    """
    return CompStudioBlog.Blog(self)

  @property
  def gallery(self):
    """
    Description:
    ------------
    Property for all the components to be used in a blog website
    """
    return CompStudioBlog.Gallery(self)

  @property
  def wedding(self):
    """
    Description:
    ------------
    Property for all the components to be used in a wedding website
    """
    return CompStudioEvent.Wedding(self)

  @property
  def birth(self):
    """
    """
    return CompStudioEvent.Birth(self)

  @property
  def baptism(self):
    """
    """
    return CompStudioEvent.Baptism(self)

  @property
  def evg(self):
    """
    """
    return CompStudioEvent.EVG(self)

  @property
  def birthday(self):
    """
    Description:
    ------------
    Property for all the components to be used in a wedding website
    """
    return CompStudioEvent.Birthday(self)

  @property
  def show(self):
    """
    Description:
    ------------
    Property for all the components to be used in a wedding website
    """
    return CompStudioEvent.Show(self)

  @property
  def vitrine(self):
    """
    Description:
    ------------
    """
    return CompStudioVitrine.Vitrine(self)

  @property
  def events(self):
    """
    Description:
    ------------
    """
    return CompStudioEvent.Event(self)

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
