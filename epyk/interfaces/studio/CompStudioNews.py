#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import datetime

from epyk.core.css import Defaults as Defaults_css


class News(object):
  def __init__(self, context):
    self.parent = context

  def miniature(self, title, url, image, category="", time=None, align="left", width=(100, '%'), height=(None, "px"), options=None, profile=None):
    """

    :param title:
    :param url:
    :param image:
    :param category:
    :param align:
    :param width:
    :param height:
    :param options:
    :return:
    """
    container = self.parent.context.rptObj.ui.col(align=align, width=width, height=height, position="top")
    container.style.css.margin = "20px auto"
    container.style.css.padding = "5px"
    if not hasattr(category, 'options'):
      category = self.parent.context.rptObj.ui.text(category)
      category.style.css.display = "block"
    if not hasattr(title, 'options'):
      title = self.parent.context.rptObj.ui.link(self.parent.context.rptObj.py.encode_html(title), url)
      title.style.css.display = "block"
      title.style.css.color = self.parent.context.rptObj.theme.greys[-1]
      title.style.css.bold()
      title.style.css.text_decoration = None
    if image is not None:
      if not hasattr(image, 'options'):
        split_url = os.path.split(image)
        container.image = self.parent.context.rptObj.ui.img(split_url[1], path=split_url[0])
        container.image.style.css.margin_bottom = "10px"
        container.add(container.image)
    container.add(self.parent.context.rptObj.ui.col([category, title]))
    return container

  def exchange(self, positive, value, align="left", width=(100, '%'), height=(None, "px"), options=None, profile=None):
    # https://www.bloomberg.com/news/articles/2020-07-28/the-world-s-best-restaurants-2020-tripadvisor-rankings-list
    component = self.parent.context.rptObj.ui.div()
    if positive:
      icon = self.parent.context.rptObj.ui.icons.awesome("fas fa-caret-up")
      component.style.css.color = self.parent.context.rptObj.theme.success[1]
    else:
      icon = self.parent.context.rptObj.ui.icons.awesome("fas fa-caret-down")
      component.style.css.color = self.parent.context.rptObj.theme.danger[1]
    icon.icon.style.css.font_factor(2)
    component.add(icon)
    number = self.parent.context.rptObj.ui.texts.number(value, width=("auto", ""))
    component.add(number)
    return component

  def shares(self, positive, value, trend, align="left", width=(100, '%'), height=(None, "px"), options=None, profile=None):
    component = self.parent.context.rptObj.ui.div()
    if positive:
      icon = self.parent.context.rptObj.ui.icons.awesome("fas fa-caret-up")
      component.style.css.color = self.parent.context.rptObj.theme.success[1]
    else:
      icon = self.parent.context.rptObj.ui.icons.awesome("fas fa-caret-down")
      component.style.css.color = self.parent.context.rptObj.theme.danger[1]
    icon.icon.style.css.font_factor(2)
    component.add(icon)
    chart = self.parent.context.rptObj.ui.charts.sparkline("line", trend)
    number = self.parent.context.rptObj.ui.texts.number(value, width=("auto", ""))
    component.add(number)
    component.add(chart)
    return component

  def moves(self, current, previous, align="left", width=(100, '%'), height=(None, "px"), options=None, profile=None):
    component = self.parent.context.rptObj.ui.div()
    if current-previous >= 0:
      icon = self.parent.context.rptObj.ui.icons.awesome("fas fa-caret-up")
      component.style.css.color = self.parent.context.rptObj.theme.success[1]
    else:
      icon = self.parent.context.rptObj.ui.icons.awesome("fas fa-caret-down")
      component.style.css.color = self.parent.context.rptObj.theme.danger[1]
    icon.icon.style.css.font_factor(2)
    component.add(icon)
    number = self.parent.context.rptObj.ui.texts.number(current, width=("auto", ""))
    component.add(number)
    delta = self.parent.context.rptObj.ui.texts.number(current-previous, width=("auto", ""))
    delta.style.css.margin = "0 10px"
    move = self.parent.context.rptObj.ui.text("(%s%%)" % round((current-previous)/previous *100, 2), width=("auto", ""))
    component.add(delta)
    component.add(move)
    return component

  def rates(self):
    # https://finance.yahoo.com/
    pass

  def share(self):
    component = self.parent.context.rptObj.ui.div()
    icon = self.parent.context.rptObj.ui.icons.facebook()
    icon.icon.style.css.font_factor(2)
    component.add(icon)
    icon = self.parent.context.rptObj.ui.icons.messenger()
    icon.icon.style.css.font_factor(2)
    component.add(icon)
    icon = self.parent.context.rptObj.ui.icons.twitter()
    icon.icon.style.css.font_factor(2)
    component.add(icon)
    icon = self.parent.context.rptObj.ui.icons.mail()
    icon.icon.style.css.font_factor(2)
    component.add(icon)
    return component

  def time(self, date, icon="", align="left", width=("auto", ''), height=(None, "px"), options=None, profile=None):
    """

    :param date:
    :param icon:
    """
    date_time_obj = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
    current = datetime.datetime.now()
    delta_time = current - date_time_obj
    component = self.parent.context.rptObj.ui.div(align=align, width=width, height=height, options=options, profile=profile)
    icon = self.parent.context.rptObj.ui.icons.awesome("far fa-clock")
    icon.icon.style.css.font_factor(2)
    component.add(icon)
    if delta_time.days == 0:
      if date_time_obj.day != current.day:
        component.add(self.parent.context.rptObj.ui.text("Yesterday"))
      else:
        if delta_time.seconds > 3600:
          hours = int(delta_time.seconds / 3600)
          minutes = int((delta_time.seconds - hours * 3600)/ 60)
          seconds = delta_time.seconds - hours * 3600 - minutes * 60
          component.add(self.parent.context.rptObj.ui.text("%s h %s min %s s" % (hours, minutes, seconds)))
        elif delta_time.seconds > 60:
          minutes = int(delta_time.seconds / 60)
          seconds = delta_time.seconds - minutes * 60
          component.add(self.parent.context.rptObj.ui.text("%s min %s s" % (minutes, seconds)))
    else:
      component.add(self.parent.context.rptObj.ui.text(date_time_obj.strftime("%d %B %Y")))
    return component

  def tags(self, tags, align="left", width=(300, 'px'), height=("auto", ''), options=None, profile=None):
    """

    :param tags:
    :param align:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    container = self.parent.context.rptObj.ui.div([], align=align, width=width, height=height, options=options, profile=profile)
    for tag in tags:
      if not hasattr(tag, 'options'):
        comp_tag = self.parent.context.rptObj.ui.text(tag)
      else:
        comp_tag = tag
      comp_tag.style.css.border = "1px solid %s" % self.parent.context.rptObj.theme.greys[-1]
      comp_tag.style.css.margin = "0 3px"
      comp_tag.style.css.padding = "1px 5px"
      container.add(comp_tag)
    return container

  def border(self):
    return self.parent.context.rptObj.ui.div("&nbsp;").css({"border-left": '1px solid %s' % self.parent.context.rptObj.theme.greys[5],
                                                          "margin": '5px 0', "display": 'inline-block', 'width': 'auto'})

  def delimiter(self):
    """

    """
    hr = self.parent.context.rptObj.ui.layouts.hr()
    hr.style.css.padding = "10px 20%"
    return hr

  def section(self, text, align="left", width=(100, '%'), height=("auto", ''), options=None, profile=None):
    """

    :param text:
    :param align:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    hr = self.parent.context.rptObj.ui.layouts.hr()
    hr.style.css.padding = 0
    hr.style.css.margin_top = "-50px"
    hr.style.css.padding_left = "140px"
    hr.style.css.padding_right = "60px"
    hr.style.css.display = "inline-block"
    text = self.parent.context.rptObj.ui.text(text, width=("auto", ""))
    text.style.css.display = "inline-block"
    text.style.css.bold()
    text.style.css.font_factor(15)
    return self.parent.context.rptObj.ui.div([text, hr], align=align, width=width, height=height, options=options, profile=profile)
