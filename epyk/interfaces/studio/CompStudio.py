#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

from epyk.interfaces.studio import CompStudioBlog
from epyk.interfaces.studio import CompStudioShopping
from epyk.interfaces.studio import CompStudioNews
from epyk.interfaces.studio import CompStudioDashboard
from epyk.interfaces.studio import CompStudioManagement
from epyk.interfaces.studio import CompStudioVitrine
from epyk.interfaces.studio import CompStudioEvent
from epyk.interfaces.studio import CompStudioQuiz

from epyk.core.css import Defaults as Defaults_css
from epyk.interfaces import Arguments


class Studio(object):
  def __init__(self, context):
    self.context = context

  def locked(self, component, day, month, year, hour=0, minute=0, second=0, options=None):
    """
    Description:
    ------------

    This item is only working if the page is generated on demand

    Attributes:
    ----------
    :param component:
    :param day:
    :param month:
    :param year:
    :param hour:
    :param minute:
    :param second:
    :param options:
    """
    options = options or {}
    event_time = datetime.datetime(year, month, day, hour, minute, second)
    now = datetime.datetime.now()
    if now > event_time:
      return component

    # Delete the items on the backend side
    del self.context.rptObj.components[component.htmlCode]
    component = self.context.rptObj.ui.div()
    component.style.css.line_height = Defaults_css.font(25)
    component.style.css.border = "1px solid %s" % self.context.rptObj.theme.greys[3]
    component.style.css.border_radius = 10
    component.style.css.margin = "5px 0"
    component.style.css.padding = 5
    icon = self.context.rptObj.ui.icons.awesome("fas fa-lock")
    icon.icon.style.css.font_factor(10)
    icon.icon.style.css.vertical_align = None
    icon.icon.style.css.color = self.context.rptObj.theme.greys[5]
    icon.icon.style.css.line_height = Defaults_css.font(25)
    component.add(icon)
    component.text = self.context.rptObj.ui.text("Event Locked")
    component.text.style.css.font_factor(8)
    component.text.style.css.vertical_algin = 'bottom'
    component.text.style.css.color = self.context.rptObj.theme.greys[5]
    component.add(component.text)
    component.countdown = self.context.rptObj.ui.rich.countdown(day, month, year, hour, minute, second, width=(None, ''))
    component.countdown._jsStyles['reload'] = False
    component.countdown.style.css.display = 'inline-block'
    component.countdown.style.css.float = 'right'
    component.countdown.style.css.margin_right = 5
    component.add(component.countdown)
    if not options.get("countdown", True):
      component.countdown.style.css.display = False
    return component

  def secured(self, component, authorized=False, options=None):
    """
    Description:
    ------------

    This item is only working if the page is generated on demand

    Attributes:
    ----------
    :param component:
    :param authorized:
    :param options:
    """
    options = options or {}
    if authorized:
      return component

    # Delete the items on the backend side
    del self.context.rptObj.components[component.htmlCode]
    component = self.context.rptObj.ui.div()
    component.style.css.line_height = Defaults_css.font(25)
    component.style.css.border = "1px solid %s" % self.context.rptObj.theme.greys[3]
    component.style.css.border_radius = 10
    component.style.css.margin = "5px 0"
    component.style.css.padding = 5
    icon = self.context.rptObj.ui.icons.awesome("fas fa-key")
    icon.icon.style.css.font_factor(10)
    icon.icon.style.css.vertical_align = None
    icon.icon.style.css.color = self.context.rptObj.theme.greys[5]
    icon.icon.style.css.line_height = Defaults_css.font(25)
    component.add(icon)
    component.text = self.context.rptObj.ui.text("Not available")
    component.text.style.css.font_factor(8)
    component.text.style.css.vertical_algin = 'bottom'
    component.text.style.css.color = self.context.rptObj.theme.greys[5]
    component.add(component.text)
    return component

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
  def dating(self):
    """
    Description:
    ------------

    """
    return CompStudioEvent.Dating(self)

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
    Description:
    ------------
    """
    return CompStudioEvent.Birth(self)

  @property
  def baptism(self):
    """
    Description:
    ------------
    """
    return CompStudioEvent.Baptism(self)

  @property
  def evg(self):
    """
    Description:
    ------------
    """
    return CompStudioEvent.EVG(self)

  @property
  def seminar(self):
    """
    Description:
    ------------

    https://www.voyage-event.com/autres-themes
    """
    return CompStudioEvent.Seminar(self)

  @property
  def festival(self):
    """
    Description:
    ------------

    https://www.voyage-event.com/autres-themes
    """
    return CompStudioEvent.Festival(self)

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
  def quiz(self):
    """
    Description:
    ------------
    """
    return CompStudioQuiz.Quiz(self)

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
