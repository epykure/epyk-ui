#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import datetime

from epyk.core.css import Defaults as Defaults_css
from epyk.core.css.themes import ThemeDark


class News(object):
  def __init__(self, context):
    self.parent = context

  def theme(self):
    """
    Description:
    ------------

    """
    self.parent.context.rptObj.theme = ThemeDark.Grey()

  def miniature(self, title, url, image, category="", time=None, align="left", width=(100, '%'), height=(None, "px"), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param title:
    :param url:
    :param image:
    :param category:
    :param align:
    :param width:
    :param height:
    :param options:
    """
    container = self.parent.context.rptObj.ui.col(align=align, width=width, height=height, position="top")
    container.style.css.margin = "20px auto"
    container.style.css.padding = "5px"
    container.style.css.background = self.parent.context.rptObj.theme.greys[0]
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
    """
    Description:
    ------------

    Attributes:
    ----------
    :param positive:
    :param value:
    :param align:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
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
    """
    Description:
    ------------

    Attributes:
    ----------
    :param positive:
    :param value:
    :param trend:
    :param align:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
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
    """
    Description:
    ------------

    Attributes:
    ----------
    :param current:
    :param previous:
    :param align:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
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

  def share(self, facebook=True, messenger=True, twitter=True, mail=True):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param facebook: Boolean. Flag to mention if the facebook shortcut need to be displayed
    :param messenger: Boolean. Flag to mention if the messenger shortcut need to be displayed
    :param twitter: Boolean. Flag to mention if the twitter shortcut need to be displayed
    :param mail: Boolean. Flag to mention if the mail shortcut need to be displayed
    """
    component = self.parent.context.rptObj.ui.div()
    if facebook:
      component.facebook = self.parent.context.rptObj.ui.icons.facebook()
      component.facebook.icon.style.css.font_factor(2)
      component.add(component.facebook)
    if messenger:
      component.messenger = self.parent.context.rptObj.ui.icons.messenger()
      component.messenger.icon.style.css.font_factor(2)
      component.add(component.messenger)
    if twitter:
      component.twitter = self.parent.context.rptObj.ui.icons.twitter()
      component.twitter.icon.style.css.font_factor(2)
      component.add(component.twitter)
    if mail:
      component.mail = self.parent.context.rptObj.ui.icons.mail()
      component.mail.icon.style.css.font_factor(2)
      component.add(component.mail)
    return component

  def time(self, date, icon="far fa-clock", align="left", width=("auto", ''), height=(None, "px"), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param date:
    :param icon:
    """
    date_time_obj = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
    current = datetime.datetime.now()
    delta_time = current - date_time_obj
    component = self.parent.context.rptObj.ui.div(align=align, width=width, height=height, options=options, profile=profile)
    icon = self.parent.context.rptObj.ui.icons.awesome(icon)
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
    Description:
    ------------

    Attributes:
    ----------
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
    """
    Description:
    ------------

    Attributes:
    ----------

    """
    return self.parent.context.rptObj.ui.div("&nbsp;").css({"border-left": '1px solid %s' % self.parent.context.rptObj.theme.greys[5],
                                                          "margin": '5px 0', "display": 'inline-block', 'width': 'auto'})

  def delimiter(self):
    """
    Description:
    ------------

    Attributes:
    ----------
    """
    hr = self.parent.context.rptObj.ui.layouts.hr()
    hr.style.css.padding = "10px 20%"
    return hr

  def section(self, text, align="left", width=(100, '%'), height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
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

  def comments(self, count, url, icon="far fa-comment-alt", align="left", width=("auto", ''), height=(None, "px"), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param count:
    :param url:
    :param icon:
    :param align:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    component = self.parent.context.rptObj.ui.div(align=align, width=width, height=height, options=options, profile=profile)
    icon = self.parent.context.rptObj.ui.icons.awesome(icon)
    icon.icon.style.css.font_factor(0)
    component.add(icon)
    link = self.parent.context.rptObj.ui.link(count, url)
    link.style.css.color = self.parent.context.rptObj.theme.greys[6]
    component.add(link)
    return component

  def live(self, icon="fas fa-circle"):
    """
    Description:
    ------------

    Attributes:
    ----------

    """
    live = self.parent.context.rptObj.ui.icons.awesome(icon)
    live.style.css.color = self.parent.context.rptObj.theme.danger[1]
    live.style.css.border = "1px solid %s" % self.parent.context.rptObj.theme.danger[1]
    live.style.css.border_radius = "50px"
    live.style.css.padding = "2px"
    live.style.css.margin = 0
    live.icon.style.css.font_factor(2)
    live.icon.style.css.margin_right = 0
    live.icon.style.css.margin = 0
    live.icon.style.css.padding_bottom = "2px"
    live.icon.style.effects.blink(2)
    return live

  def button(self, text="", icon=None, width=(None, "%"), height=(None, "px"), align="left", htmlCode=None,
             tooltip=None, profile=None, options=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param icon:
    :param width:
    :param height:
    :param align:
    :param htmlCode:
    :param tooltip:
    :param profile:
    :param options:
    """
    button = self.parent.context.rptObj.ui.button(text, icon, width=width, height=height, options=options, tooltip=tooltip, profile=profile, align=align)
    button.style.clear()
    button.style.css.padding = "0 10px"
    button.style.css.background = self.parent.context.rptObj.theme.greys[0]
    button.style.hover({"color": self.parent.context.rptObj.theme.success[1]})
    return button

  def stepper(self, records, width=(200, 'px'), height=(350, 'px'), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param records:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    size = (height[0] - 20) / (len(records) - 1)
    frgs, dflt_size = [], 0
    for rec in records[:-1]:
      if 'size' in rec:
        frgs.append(rec['size'])
      else:
        frgs.append(size)
        dflt_size += 1
    extra_size = (height[0] - 20 - sum(frgs)) / dflt_size if dflt_size > 0 else 0
    frgs = [frg + extra_size if frg == size else frg for frg in frgs]
    svg = self.parent.context.rptObj.ui.charts.svg.new(width=width, height=height)
    svg.line(10, 10, 10, sum(frgs) + 10, stroke="red")
    for i, rec in enumerate(records):
      svg.circle(10, 10 + sum(frgs[0:i]), 5, fill=rec.get("fill", self.parent.context.rptObj.theme.greys[0]), stroke="red")
      svg.text(rec["time"], 20, 15 + sum(frgs[0:i])).css({"font-weight": 'bold', 'color': self.parent.context.rptObj.theme.greys[-1]})
      svg.text(rec["text"], 55, 15 + sum(frgs[0:i])).css({'color': self.parent.context.rptObj.theme.greys[-1]})
    return svg

  def search(self):
    pass

  def audio(self, text, url, icon="fas fa-volume-up"):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param url:
    :param icon:
    """
    icon = self.parent.context.rptObj.ui.icons.awesome(icon)
    icon.icon.style.css.font_factor(0)
    icon.icon.style.css.color = self.parent.context.rptObj.theme.greys[-1]
    icon.options.managed = False
    link = self.parent.context.rptObj.ui.link("%s %s" % (icon.html(), text), url)
    link.style.css.background = self.parent.context.rptObj.theme.greys[0]
    link.style.css.color = self.parent.context.rptObj.theme.greys[-1]
    link.style.css.padding = "2px 5px"
    return link

