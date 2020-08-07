#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

from epyk.core.css import Defaults_css
from epyk.core.css.themes import ThemeRed


class Quiz(object):

  def __init__(self, context):
    self.parent = context

  def theme(self):
    """
    Description:
    ------------

    """
    self.parent.context.rptObj.theme = ThemeRed.Pink()

  def progress(self, percentage, icon="fas fa-car-side", width=(100, '%'), height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param percentage:
    :param icon:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    options = options or {}
    icon = self.parent.context.rptObj.ui.icons.awesome(icon, height=("auto", ''))
    progress = self.parent.context.rptObj.ui.div()
    progress.style.css.border = "1px solid %s" % self.parent.context.rptObj.theme.success[1]
    progress.style.css.display = "inline-block"
    progress.style.css.width = "calc(100% - 50px)"
    inner = self.parent.context.rptObj.ui.div("%s%%" % percentage, width=(percentage, '%'))
    inner.style.css.background = self.parent.context.rptObj.theme.success[0]
    inner.style.css.color = self.parent.context.rptObj.theme.success[1]
    inner.style.css.text_align = "center"
    progress.add(inner)
    container = self.parent.context.rptObj.ui.div([progress, icon], width=width, height=height)
    container.style.css.padding = "0 5px"
    return container

  def position(self, longitude, latitude, flag=None, width=(100, '%'), height=("auto", ''), icon="fas fa-map-marked-alt", options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param longitude:
    :param latitude:
    :param flag:
    :param width:
    :param height:
    :param icon:
    :param options:
    :param profile:
    """
    container = self.parent.context.rptObj.ui.div(width=width, height=height)
    container.icon = self.parent.context.rptObj.ui.icons.awesome(icon)
    container.icon.icon.style.css.font_factor(10)
    container.icon.icon.style.css.color = self.parent.context.rptObj.theme.greys[6]
    container.add(container.icon)
    if flag is None:
      container.button = self.parent.context.rptObj.ui.button("Check Position")
      container.button.style.css.line_height = 20
      container.add(container.button)
    elif flag:
      container.text = self.parent.context.rptObj.ui.text("Well done! Position validated")
      container.text.style.css.line_height = 20
      container.text.style.css.color = self.parent.context.rptObj.theme.success[1]
      container.text.style.css.font_factor(5)
      container.add(container.text)
    else:
      container.text = self.parent.context.rptObj.ui.text("Failed! Position not found")
      container.text.style.css.line_height = 20
      container.text.style.css.color = self.parent.context.rptObj.theme.danger[1]
      container.text.style.css.font_factor(5)
      container.add(container.text)
    return container

  def picture(self, image, question=None, icon="far fa-image", width=(100, '%'), height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param image:
    :param question:
    :param icon:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    options = options or {}
    container = self.parent.context.rptObj.ui.div(width=width, height=height)
    container.style.css.border = "2px solid %s" % self.parent.context.rptObj.theme.greys[3]
    container.style.css.padding = 10
    container.style.css.margin = 5
    container.style.css.width = "calc(%s%s - 10px)" % (width[0], width[1])
    container.icon = self.parent.context.rptObj.ui.icons.awesome(icon, width=(100, '%'), height=("auto", ''))
    container.icon.style.css.background = self.parent.context.rptObj.theme.colors[6]
    container.icon.style.css.display = "block"
    container.icon.icon.style.css.margin = 5
    container.icon.icon.style.css.font_factor(10)
    container.icon.icon.style.css.color = "white"
    container.add(container.icon)
    if "timer" in options:
      if options.get("timer", 0) > 0:
        container.image = self.parent.context.rptObj.ui.img(image, align="center", width=('auto', ''), height=(300, 'px'))
        chrono = self.chrono(container.image, time=options['timer'])
        container.add(chrono)
    else:
      container.image = self.parent.context.rptObj.ui.img(image, align="center", width=('auto', ''), height=(300, 'px'))
      container.add(container.image)
    if question is not None:
      question = self.parent.context.rptObj.ui.text(self.parent.context.rptObj.py.encode_html(question), align="center")
      question.style.css.font_factor(5)
      container.add(question)
    container.add(self.delimiter())
    input = self.parent.context.rptObj.ui.input()
    input.style.css.margin_top = 20
    input.style.css.margin_bottom = 10
    input.style.css.text_align = "left"
    container.add(input)
    button = self.parent.context.rptObj.ui.button("Validate", align="center")
    container.add(button)
    return container

  def question(self, question, icon="fas fa-question", width=(100, '%'), height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param question:
    :param icon:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    container = self.parent.context.rptObj.ui.div(width=width, height=height)
    container.style.css.border = "2px solid %s" % self.parent.context.rptObj.theme.greys[3]
    container.style.css.padding = 10
    container.style.css.margin = 5
    container.style.css.width = "calc(%s%s - 10px)" % (width[0], width[1])
    container.icon = self.parent.context.rptObj.ui.icons.awesome(icon, width=(100, '%'), height=("auto", ''))
    container.icon.style.css.background = self.parent.context.rptObj.theme.colors[6]
    container.icon.style.css.display = "block"
    container.icon.icon.style.css.margin = 5
    container.icon.icon.style.css.font_factor(10)
    container.icon.icon.style.css.color = "white"
    container.add(container.icon)
    question = self.parent.context.rptObj.ui.text(self.parent.context.rptObj.py.encode_html(question),
                                                  width=(None, 'px'))
    question.style.css.font_factor(5)
    container.add(question)
    container.add(self.delimiter())
    input = self.parent.context.rptObj.ui.input()
    input.style.css.margin_top = 20
    input.style.css.margin_bottom = 10
    input.style.css.text_align = "left"
    container.add(input)
    button = self.parent.context.rptObj.ui.button("Validate", align="center")
    container.add(button)
    return container

  def charade(self, clues, question=None, icon="fas fa-book", width=(100, '%'), height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param clues:
    :param question:
    :param icon:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    container = self.parent.context.rptObj.ui.div(width=width, height=height)
    container.style.css.border = "2px solid %s" % self.parent.context.rptObj.theme.greys[3]
    container.style.css.padding = 10
    container.style.css.margin = 5
    container.style.css.width = "calc(%s%s - 10px)" % (width[0], width[1])
    container.icon = self.parent.context.rptObj.ui.icons.awesome(icon, width=(100, '%'), height=("auto", ''))
    container.icon.style.css.background = self.parent.context.rptObj.theme.colors[6]
    container.icon.style.css.display = "block"
    container.icon.icon.style.css.margin = 5
    container.icon.icon.style.css.font_factor(10)
    container.icon.icon.style.css.color = "white"
    container.add(container.icon)
    for clue in clues:
      value = self.parent.context.rptObj.ui.text(self.parent.context.rptObj.py.encode_html(clue), width=(None, 'px'))
      value.style.css.font_factor(5)
      value.style.css.font_family = "Meddon"
      container.add(value)
    if question is not None:
      question = self.parent.context.rptObj.ui.text(self.parent.context.rptObj.py.encode_html(question), width=(None, 'px'))
      question.style.css.font_family = "Meddon"
      question.style.css.font_factor(5)
      container.add(question)
    container.add(self.delimiter())
    input = self.parent.context.rptObj.ui.input()
    input.style.css.margin_top = 20
    input.style.css.margin_bottom = 10
    input.style.css.text_align = "left"
    container.add(input)
    button = self.parent.context.rptObj.ui.button("Validate", align="center")
    container.add(button)
    return container

  def delimiter(self, size=1):
    """
    Description:
    ------------

    Attributes:
    ----------

    """
    hr = self.parent.context.rptObj.ui.layouts.hr()
    hr.style.css.padding = "0 20%"
    hr.hr.style.css.border_color = self.parent.context.rptObj.theme.colors[5]
    hr.hr.style.css.border_width = size
    return hr

  def missing(self, text, icon="fas fa-ellipsis-h", width=(100, '%'), height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param icon:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    container = self.parent.context.rptObj.ui.div(width=width, height=height)
    container.style.css.border = "2px solid %s" % self.parent.context.rptObj.theme.greys[3]
    container.style.css.padding = 10
    container.style.css.margin = 5
    container.style.css.width = "calc(%s%s - 10px)" % (width[0], width[1])
    container.icon = self.parent.context.rptObj.ui.icons.awesome(icon, width=(100, '%'), height=("auto", ''))
    container.icon.style.css.background = self.parent.context.rptObj.theme.colors[6]
    container.icon.style.css.display = "block"
    container.icon.icon.style.css.margin = 5
    container.icon.icon.style.css.font_factor(10)
    container.icon.icon.style.css.color = "white"
    container.add(container.icon)
    text_frg = text.split("*")
    container.add(self.parent.context.rptObj.ui.text(text_frg[0]))
    if text.startswith("*"):
      input = self.parent.context.rptObj.ui.input("", width=(50, 'px'))
      input.style.css.margin = "0 5px"
      container.add(input)
    for text in text_frg[1:-1]:
      container.add(self.parent.context.rptObj.ui.text(text))
      input = self.parent.context.rptObj.ui.input("", width=(50, 'px'))
      input.style.css.margin = "0 5px"
      container.add(input)
    container.add(self.parent.context.rptObj.ui.text(text_frg[-1]))
    if text.endswith("*"):
      container.add(self.parent.context.rptObj.ui.input(""))
    button = self.parent.context.rptObj.ui.button("Validate", align="center")
    container.add(button)
    return container

  def hangman(self, question, text, proposals=None, icon="fas fa-project-diagram", width=(100, '%'), height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param question:
    :param text:
    :param proposals:
    :param icon:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    crypt_text, missing = [], 0
    for l in text:
      if l == " ":
        crypt_text.append(l)

      if l.upper() in proposals:
        crypt_text.append(l)
      else:
        crypt_text.append("_")
        missing += 1

    container = self.parent.context.rptObj.ui.div(width=width, height=height)
    container.style.css.border = "2px solid %s" % self.parent.context.rptObj.theme.greys[3]
    container.style.css.padding = 10
    container.style.css.margin = 5
    container.style.css.width = "calc(%s%s - 10px)" % (width[0], width[1])
    container.icon = self.parent.context.rptObj.ui.icons.awesome(icon, width=(100, '%'), height=("auto", ''))
    container.icon.style.css.background = self.parent.context.rptObj.theme.colors[6]
    container.icon.style.css.display = "block"
    container.icon.icon.style.css.margin = 5
    container.icon.icon.style.css.font_factor(10)
    container.icon.icon.style.css.color = "white"
    container.add(container.icon)
    container.question = self.parent.context.rptObj.ui.text(question, width=(None, 'px'))
    container.question.style.css.font_factor(5)
    container.add(container.question)
    container.result = self.parent.context.rptObj.ui.text("".join(crypt_text), width=(None, 'px'))
    container.result.style.css.font_factor(10)
    container.result.style.css.letter_spacing = 3
    container.add(container.result)
    container.add(self.delimiter())
    input = self.parent.context.rptObj.ui.input()
    input.style.css.margin_top = 20
    input.style.css.margin_bottom = 10
    input.style.css.text_align = "left"
    container.add(input)
    button = self.parent.context.rptObj.ui.button("Validate", align="center")
    container.add(button)
    return container

  def choice(self, question, answers, status=None, icon="fas fa-question", width=(100, '%'), height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param question:
    :param answers:
    :param status:
    :param icon:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    container = self.parent.context.rptObj.ui.div(width=width, height=height)
    container.style.css.border = "2px solid %s" % self.parent.context.rptObj.theme.greys[3]
    container.style.css.padding = 10
    container.style.css.margin = 5
    container.style.css.width = "calc(%s%s - 10px)" % (width[0], width[1])
    container.icon = self.parent.context.rptObj.ui.icons.awesome(icon, width=(100, '%'), height=("auto", ''))
    container.icon.style.css.background = self.parent.context.rptObj.theme.colors[6]
    container.icon.style.css.display = "block"
    container.icon.icon.style.css.margin = 5
    container.icon.icon.style.css.font_factor(10)
    container.icon.icon.style.css.color = "white"
    container.add(container.icon)
    container.question = self.parent.context.rptObj.ui.text(question, width=(None, 'px'))
    container.question.style.css.font_factor(5)
    container.add(container.question)
    for answer in answers:
      button = self.parent.context.rptObj.ui.button(answer, width=(100, '%'))
      button.style.css.border = None
      button.style.css.text_align = 'left'
      button.style.css.display = "block"
      container.add(button)
    return container

  def rafale(self, image, icon="far fa-image", width=(100, '%'), height=("auto", ''), options=None, profile=None):
    pass

  def chrono(self, component, time=60, flag=None, icon="fas fa-stopwatch-20", width=(100, '%'), height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param component:
    :param time:
    :param flag:
    :param icon:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    container = self.parent.context.rptObj.ui.div(width=width, height=height)
    container.timer = self.parent.context.rptObj.ui.calendars.timer(time / 60, width=(None, '%'))
    container.timer.style.css.display = "inline-block"
    container.timer.style.css.vertical_align = "bottom"
    container.timer.style.css.font_factor(10)
    container.add(self.parent.context.rptObj.ui.div([self.parent.context.rptObj.ui.icons.awesome(icon), container.timer]))
    container.add(component)
    container.timer.end(component.dom.remove())
    return container

  def estimate(self, text, tooltip=None, width=(None, '%'), height=("auto", ''), icon="fas fa-stopwatch", options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param tooltip:
    :param width:
    :param height:
    :param icon:
    :param options:
    :param profile:
    """
    container = self.parent.context.rptObj.ui.div(width=width, height=height)
    container.icon = self.parent.context.rptObj.ui.icons.awesome(icon)
    container.icon.icon.style.css.font_factor(10)
    container.icon.icon.style.css.color = self.parent.context.rptObj.theme.success[1]
    container.add(container.icon)
    container.text = self.parent.context.rptObj.ui.text(text, width=(None, 'px'))
    if tooltip is not None:
      container.text.tooltip(tooltip)
    container.text.style.css.display = "inline-block"
    container.text.style.css.font_factor(5)
    container.add(container.text)
    return container

  def level(self, text, tooltip, width=(None, '%'), height=("auto", ''), icon="fas fa-chess-bishop", options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param tooltip:
    :param width:
    :param height:
    :param icon:
    :param options:
    :param profile:
    """
    container = self.parent.context.rptObj.ui.div(width=width, height=height)
    container.icon = self.parent.context.rptObj.ui.icons.awesome(icon)
    container.icon.icon.style.css.font_factor(10)
    container.icon.icon.style.css.color = self.parent.context.rptObj.theme.success[1]
    container.add(container.icon)
    container.text = self.parent.context.rptObj.ui.text(text, width=(None, 'px'))
    container.text.style.css.font_factor(5)
    if tooltip is not None:
      container.text.tooltip(tooltip)
    container.text.style.css.display = "inline-block"
    container.add(container.text)
    return container

  def ranking(self, number=0, width=(None, '%'), height=("auto", ''), icon="fas fa-flag-checkered", options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param number:
    :param width:
    :param height:
    :param icon:
    :param options:
    :param profile:
    """
    container = self.parent.context.rptObj.ui.div(width=width, height=height)
    container.icon = self.parent.context.rptObj.ui.icons.awesome(icon)
    container.icon.icon.style.css.font_factor(10)
    container.icon.icon.style.css.color = self.parent.context.rptObj.theme.success[1]
    container.add(container.icon)
    container.number = self.parent.context.rptObj.ui.texts.number(number, width=(None, 'px'))
    container.number.style.css.line_height = 20
    container.number.style.css.color = self.parent.context.rptObj.theme.success[1]
    container.number.style.css.font_factor(5)
    container.add(container.number)
    return container

  def points(self, number=0, width=(None, '%'), height=("auto", ''), icon="fas fa-coins", options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param number:
    :param width:
    :param height:
    :param icon:
    :param options:
    :param profile:
    """
    container = self.parent.context.rptObj.ui.div(width=width, height=height)
    container.icon = self.parent.context.rptObj.ui.icons.awesome(icon)
    container.icon.icon.style.css.font_factor(10)
    container.icon.icon.style.css.color = self.parent.context.rptObj.theme.success[1]
    container.add(container.icon)
    container.number = self.parent.context.rptObj.ui.texts.number(number, width=(None, 'px'))
    container.number.style.css.line_height = 20
    container.number.style.css.color = self.parent.context.rptObj.theme.success[1]
    container.number.style.css.font_factor(5)
    container.add(container.number)
    return container

  def interval(self, start, end, flag=None, width=(100, '%'), height=("auto", ''), icon="fas fa-hourglass-half", options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param start:
    :param end:
    :param flag:
    :param width:
    :param height:
    :param icon:
    :param options:
    :param profile:
    """
    container = self.parent.context.rptObj.ui.div(width=width, height=height)
    container.icon = self.parent.context.rptObj.ui.icons.awesome(icon)
    container.icon.icon.style.css.font_factor(10)
    container.icon.icon.style.css.color = self.parent.context.rptObj.theme.greys[6]
    if flag is None:
      current = datetime.datetime.now()
      if start >= current >= end:
        pass
      else:
        pass

    return container

  def rating(self, rating, customers, url=None, align="left", width=(300, 'px'), height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param rating:
    :param customers:
    :param url:
    :param align:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    options = options or {}
    container = self.parent.context.rptObj.ui.div([])
    container.stars = self.parent.context.rptObj.ui.rich.stars(rating, best=options.get("stars", 5))
    container.stars.style.display = "inline-block"
    container.stars.style.margin_right = 5
    container.link = self.parent.context.rptObj.ui.link("(%s)" % customers, url)
    container.add(container.stars)
    container.add(container.link)
    return container

  def quality(self, votes, url=None, align="left", width=(300, 'px'), height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------
    Return a skillbar chart for the customer review ratings

    Attributes:
    ----------
    :param votes: Dictionary. Number of customer review per rating
    :param url: String. Url template for product link to those customer rating comments
    :param align:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    vote_records = []
    dflt_options = {"unit": '%', "values": True, "background": self.parent.context.rptObj.theme.colors[6], 'borders': True}
    if options is not None:
      dflt_options.update(options)
    customers = sum([k for k in votes.values()])
    for i in reversed(range(dflt_options.get("stars", 5))):
      if url is not None:
        vote_records.append({"star": self.parent.context.rptObj.ui.link("%s stars" % i, url % i), "value":  votes.get(i, 0) / customers * 100})
      else:
        vote_records.append({"star": "%s stars" % i, "value":  votes.get(i, 0) / customers * 100})
    comp = self.parent.context.rptObj.ui.charts.skillbars(vote_records, y_column='value', x_axis='star', options=dflt_options).css({"width": "%s%s" % (width[0], width[1])})
    return comp

  def cup(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """

    https://uxwing.com/winning-cup-icon/

    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
      path="M89.43,45.54c3.38-1,6.39-2.61,8.84-4.65c4.02-3.35,6.5-7.9,6.5-12.87c0-2.78-0.77-5.42-2.15-7.78l0.01,0 c-0.62-1.06-1.36-2.07-2.21-3.01c-0.44,6.2-1.96,12.08-4.34,17.43C94.32,38.61,92.07,42.27,89.43,45.54L89.43,45.54L89.43,45.54z M56.4,91.21l2.83,7.93l8.42,0.24l-6.67,5.14l2.37,8.08l-6.95-4.76l-6.95,4.76l2.37-8.08l-6.67-5.14l8.42-0.24L56.4,91.21 L56.4,91.21z M20.63,80.94h71.55v41.94H20.63V80.94L20.63,80.94z M60.73,60.07v6.55h0.49v4.58l-12.42,0v-4.58l0.49,0v-6.59 c-7.57-1.17-14.49-4.59-20.14-9.59l-0.67,1.85c-7.79-0.13-14.84-2.82-19.95-7.08C3.26,40.83,0,34.75,0,28.01 c0-3.8,1.05-7.4,2.93-10.63l-0.01-0.01c1.9-3.27,4.66-6.13,8.03-8.37L14,6.97l-3.53,0V0h88.61v6.97h-2.82L99.31,9 c3.36,2.24,6.11,5.1,8.02,8.37h0.01c1.87,3.22,2.92,6.82,2.92,10.64c0,6.74-3.26,12.81-8.54,17.21 c-5.11,4.26-12.16,6.95-19.95,7.08l-0.67-1.86C75.39,55.5,68.39,58.94,60.73,60.07L60.73,60.07L60.73,60.07z M42.16,75.79h25.71 v4.58H42.16V75.79L42.16,75.79z M46.08,71.2h17.87v4.58H46.08V71.2L46.08,71.2z M11.99,40.89c2.45,2.05,5.47,3.65,8.85,4.66 c-2.64-3.27-4.89-6.93-6.66-10.9c-2.38-5.34-3.9-11.23-4.34-17.43c-0.83,0.92-1.57,1.94-2.2,3.01l-0.01,0 c-1.37,2.35-2.14,5-2.14,7.78C5.49,32.99,7.97,37.53,11.99,40.89L11.99,40.89z"
    )
    return svg

  def bookmark(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """

    https://uxwing.com/bookmark-icon/

    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
      path="M83.02,0L0,0l0.37,122.88l40.99-22.18l40.26,21.88L83.02,0L83.02,0z M47.48,25.82L41.51,7.54 c5.8,0,10.94,1.64,15.46,4.92c4.51,3.27,7.74,7.73,9.73,13.36H47.48L47.48,25.82z M51.14,37.17l15.57-11.31 c0.85,3.05,1.28,5.81,1.28,8.27c0,8.71-3.64,15.82-10.92,21.33L51.14,37.17L51.14,37.17L51.14,37.17z M41.51,44.14l15.56,11.31 c-4.91,3.36-10.1,5.05-15.56,5.05c-5.44,0-10.63-1.68-15.56-5.05L41.51,44.14L41.51,44.14z M31.89,37.17l-5.94,18.28 c-7.28-5.75-10.92-12.88-10.92-21.4c0-2.48,0.44-5.22,1.32-8.2L31.89,37.17L31.89,37.17L31.89,37.17z M35.58,25.82H16.35 c1.94-5.61,5.17-10.05,9.7-13.35c4.53-3.28,9.69-4.93,15.46-4.93L35.58,25.82L35.58,25.82L35.58,25.82z"
    )
    return svg

  def first(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """

    https://uxwing.com/first-medal-icon/

    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
      path="M43.78,70.6v31.1h-8.59V81.36c-1.39,1.05-2.73,1.9-4.04,2.55c-1.3,0.65-2.93,1.27-4.89,1.87v-6.92 c2.89-0.94,5.14-2.07,6.74-3.38c1.6-1.32,2.86-2.94,3.76-4.87H43.78L43.78,70.6z M46.07,50.64c2.2,0.58,4.32,1.36,6.34,2.31 L55.59,3h6.58l-5.35,52.42c10.01,6.56,16.63,17.88,16.63,30.74c0,20.28-16.44,36.72-36.72,36.72C16.44,122.88,0,106.44,0,86.16 C0,73.65,6.26,62.6,15.81,55.97L11.27,3h6.58l2.36,50.35c2.16-1.09,4.43-1.97,6.81-2.61L24.44,0h24.58L46.07,50.64L46.07,50.64z M36.72,58.05c15.52,0,28.1,12.58,28.1,28.1s-12.58,28.1-28.1,28.1c-15.52,0-28.1-12.58-28.1-28.1S21.2,58.05,36.72,58.05 L36.72,58.05z"
    )
    return svg

  def brain(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """

    https://uxwing.com/innovative-brain-icon/

    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
      path="M60.89,8.37c2.99-4.67,6.96-7.16,11.12-8.03c3.95-0.82,8-0.11,11.49,1.65c3.44,1.74,6.39,4.52,8.2,7.88 c0.68,1.26,1.21,2.6,1.55,3.98c2.03-0.04,4.1,0.31,6.11,0.99c3.82,1.29,7.49,3.82,10.33,7.17c2.85,3.37,4.88,7.62,5.4,12.33 c0.24,2.17,0.15,4.43-0.32,6.74c2.09,1.87,3.83,3.98,5.14,6.23c2.03,3.47,3.09,7.32,2.98,11.23c-0.11,3.94-1.41,7.88-4.09,11.51 c-1.69,2.29-3.92,4.44-6.73,6.37c0.26,6.02-1.52,11.42-4.4,15.6c-3.26,4.72-7.98,7.92-12.88,8.78c-1.08,4.19-3.86,7.88-7.45,10.45 c-4.54,3.25-10.46,4.78-15.87,3.3c-3.99-1.09-7.62-3.73-10.11-8.38c-3.03,5.11-7.19,7.81-11.55,8.72 c-5.23,1.09-10.64-0.52-14.72-3.7c-3.26-2.54-5.71-6.11-6.59-10.16c-1.71-0.07-3.44-0.41-5.13-0.98c-3.73-1.26-7.32-3.7-10.13-6.95 c-2.82-3.25-4.87-7.34-5.51-11.89c-0.33-2.37-0.28-4.85,0.24-7.4c-1.83-1.66-3.4-3.53-4.65-5.56C1.14,64.78-0.05,60.86,0,56.83 c0.05-4.06,1.34-8.18,4.14-12c1.63-2.22,3.78-4.34,6.5-6.28c-0.03-0.74-0.03-1.48-0.01-2.21c0.22-5.93,2.4-11.14,5.59-15.03 c3.3-4.03,7.72-6.67,12.26-7.31l0.02,0c0.16-0.67,0.35-1.32,0.59-1.96c1.46-3.97,4.47-7.34,8.16-9.49 c3.71-2.16,8.17-3.11,12.51-2.21C53.93,1.2,57.9,3.7,60.89,8.37L60.89,8.37z M93.02,21.89c-0.66,2.18-1.84,4.37-3.64,6.5 c-1.37,1.63-3.8,1.84-5.43,0.47c-1.63-1.37-1.84-3.8-0.47-5.43c2.9-3.45,2.93-7.07,1.4-9.9c-1.06-1.96-2.81-3.6-4.87-4.64 c-2.01-1.01-4.28-1.44-6.44-0.99c-2.88,0.6-5.67,2.83-7.6,7.36c0.03,0.2,0.05,0.41,0.05,0.62v79.69c0.06,0.19,0.11,0.4,0.15,0.6 c1.11,6.75,4.03,10,7.31,10.9c3.03,0.83,6.52-0.14,9.3-2.14c2.73-1.96,4.68-4.82,4.7-7.83c0.03-3.43-2.49-7.31-9.23-10.75 c-1.91-0.97-2.66-3.31-1.69-5.22c0.97-1.91,3.31-2.66,5.22-1.69c7.44,3.8,11.36,8.46,12.8,13.17c2.39-0.78,4.71-2.6,6.47-5.14 c2.21-3.19,3.46-7.48,2.86-12.3c-0.35-1.65,0.37-3.41,1.9-4.3c2.92-1.71,5.07-3.6,6.53-5.59c1.66-2.24,2.46-4.62,2.53-6.96 c0.07-2.36-0.61-4.74-1.91-6.96c-1.19-2.03-2.87-3.9-4.98-5.48c-1.47-0.98-2.17-2.87-1.57-4.62c0.71-2.1,0.9-4.14,0.69-6.06 c-0.33-3.02-1.67-5.77-3.54-8c-1.89-2.24-4.31-3.92-6.78-4.75C95.5,22.01,94.22,21.81,93.02,21.89L93.02,21.89z M28.85,93.03 c1.54-4.84,5.6-9.67,13.26-13.58c1.91-0.97,4.24-0.22,5.22,1.69c0.97,1.91,0.22,4.24-1.69,5.22c-7.1,3.63-9.77,7.79-9.77,11.42 c0,2.83,1.61,5.48,3.96,7.31c2.38,1.85,5.46,2.81,8.36,2.21c3.62-0.75,7.11-4.1,8.92-11.39V19.22C55.3,11.98,51.81,8.65,48.2,7.9 c-2.38-0.5-4.91,0.07-7.07,1.33c-2.18,1.27-3.94,3.22-4.77,5.47c-1.11,3-0.45,6.69,3.3,10.16c1.56,1.45,1.66,3.88,0.21,5.44 c-1.45,1.56-3.88,1.66-5.44,0.21c-2.92-2.7-4.72-5.57-5.62-8.43c-2.3,0.55-4.57,2.07-6.4,4.3c-2.15,2.62-3.62,6.16-3.77,10.23 c-0.04,1.08,0.02,2.22,0.18,3.39l-0.01,0c0.21,1.52-0.47,3.09-1.86,3.95c-2.81,1.73-4.89,3.63-6.34,5.61 c-1.76,2.4-2.57,4.92-2.6,7.35c-0.03,2.47,0.73,4.92,2.09,7.13c1.15,1.87,2.73,3.57,4.65,5c1.44,0.99,2.12,2.85,1.53,4.59 c-0.76,2.25-0.93,4.44-0.64,6.47c0.41,2.93,1.77,5.6,3.63,7.75c1.87,2.16,4.23,3.77,6.65,4.59C26.9,92.8,27.89,92.99,28.85,93.03 L28.85,93.03z M29.73,38.54c1.52-1.49,3.96-1.47,5.46,0.05c1.49,1.52,1.47,3.96-0.05,5.46c-3.31,3.26-5.04,7.46-5.22,11.76 c-0.18,4.43,1.26,8.98,4.28,12.73c1.34,1.66,1.07,4.09-0.59,5.43c-1.66,1.34-4.09,1.07-5.43-0.59c-4.23-5.24-6.24-11.62-5.98-17.87 C22.47,49.29,24.96,43.23,29.73,38.54L29.73,38.54z M84.51,42.25c-1.73-1.25-2.11-3.67-0.86-5.4c1.25-1.73,3.67-2.12,5.4-0.86 c0.77,0.56,1.5,1.15,2.18,1.77c5.03,4.54,7.78,10.53,8.28,16.73c0.5,6.14-1.21,12.48-5.08,17.8c-0.57,0.78-1.18,1.54-1.84,2.27 c-1.43,1.59-3.87,1.72-5.46,0.29c-1.59-1.43-1.72-3.87-0.29-5.46c0.48-0.53,0.92-1.08,1.33-1.64c2.76-3.8,3.98-8.3,3.63-12.66 c-0.35-4.29-2.25-8.44-5.74-11.58C85.57,43.07,85.06,42.65,84.51,42.25L84.51,42.25z"
    )
    return svg

  def puzzle(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """

    https://uxwing.com/innovative-brain-icon/

    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
      path="M29.96,111.88c5.94,0,10.77-4.32,10.77-9.64c0-1.9-0.62-3.67-1.69-5.17l0.29,0c-4.73-5.17-4.23-9.4,0.78-10.88 h16.57c1.87,0,3.4-1.53,3.4-3.4V68.08c1.16-10.04,5.45-7.06,10.5-3.95c12.2,7.51,20.31-10.28,10.45-16.37 c-7.74-4.78-11.09,3.44-16.76,2.59c-2.19-0.33-3.71-2.7-4.19-6.3V29.51c0-1.87-1.53-3.4-3.4-3.4l-14.51,0 c-6.87-0.87-8.17-5.49-2.85-11.3h-0.29c1.07-1.5,1.69-3.27,1.69-5.17C40.73,4.32,35.91,0,29.96,0C24.02,0,19.2,4.32,19.2,9.64 c0,1.9,0.62,3.67,1.69,5.17l-0.07,0c5.32,5.81,4.03,10.44-2.85,11.3H3.4c-1.87,0-3.4,1.53-3.4,3.4v15.16 c1.09,6.24,5.59,7.26,11.19,2.13v0.07c1.5-1.07,3.27-1.69,5.17-1.69c5.32,0,9.64,4.82,9.64,10.76c0,5.94-4.32,10.76-9.64,10.76 c-1.9,0-3.67-0.62-5.17-1.69v0.29c-5.6-5.13-10.1-4.1-11.19,2.14V82.8c0,1.87,1.53,3.4,3.4,3.4l16.63,0 c5.01,1.48,5.52,5.71,0.78,10.88h0.07c-1.06,1.5-1.69,3.27-1.69,5.17C19.2,107.57,24.02,111.89,29.96,111.88L29.96,111.88 L29.96,111.88z M92.92,112.43H92.9c-5.94,0-10.77-4.32-10.77-9.64c0-1.9,0.62-3.67,1.69-5.17h-0.07c4.73-5.17,4.23-9.4-0.78-10.88 l-16.63,0c-1.87,0-3.4-1.53-3.4-3.4V68.01c0.8-2.32,1.82-3.14,3.02-3.17c0.55-0.01,1.13,0.14,1.75,0.4c1.74,0.72,3.78,2.23,6,3.09 c8.56,3.3,15.91-5.03,15.42-13.59c-0.11-1.91-0.88-3.79-2.02-5.53c-4.37-6.68-10.84-7.31-17.08-3.5c-3.18,1.95-5.71,3.42-7.16-1.17 l0.08-14.49c0.01-1.87,1.53-3.4,3.4-3.4l14.56,0c6.87-0.87,8.17-5.49,2.85-11.3h0.07c-1.07-1.5-1.69-3.27-1.69-5.17 c0-5.32,4.82-9.64,10.77-9.64l0.02,0c5.94,0,10.77,4.32,10.77,9.64c0,1.9-0.62,3.67-1.69,5.17h0.07 c-5.32,5.81-4.03,10.44,2.85,11.3h14.56c1.87,0,3.4,1.53,3.4,3.4v15.16c-1.09,6.24-5.59,7.26-11.19,2.13v0.07 c-1.5-1.07-3.27-1.69-5.17-1.69c-5.32,0-9.64,4.82-9.64,10.76c0,5.94,4.32,10.77,9.64,10.77c1.9,0,3.67-0.62,5.17-1.69v0.29 c5.61-5.13,10.1-4.1,11.19,2.14v15.33c0,1.87-1.53,3.4-3.4,3.4l-16.63,0c-5.01,1.48-5.51,5.71-0.78,10.88H102 c1.07,1.5,1.69,3.27,1.69,5.17C103.68,108.11,98.86,112.43,92.92,112.43L92.92,112.43L92.92,112.43z"
    )
    return svg

  def numbers(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """

    https://uxwing.com/numbers-blocks-icon/

    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
      path="M72.17,60.87l38-6.11c3.37-0.54,6.58,1.78,7.12,5.15l5.51,34.24c0.54,3.37-1.78,6.58-5.15,7.12l-38,6.11 c-3.37,0.54-6.58-1.78-7.12-5.15l-5.51-34.24C66.48,64.62,68.8,61.41,72.17,60.87L72.17,60.87z M91.64,76.94l-7.35-0.08 c0.22-2.37,1.06-4.3,2.55-5.8c1.48-1.49,3.77-2.5,6.85-3.01c3.55-0.59,6.21-0.36,8.02,0.7c1.8,1.06,2.87,2.59,3.2,4.59 c0.2,1.17,0.05,2.29-0.43,3.35s-1.3,2.05-2.48,2.98c1.09,0.08,1.95,0.25,2.56,0.51c1,0.41,1.82,1.02,2.47,1.85 c0.65,0.83,1.09,1.87,1.3,3.13c0.26,1.58,0.11,3.17-0.48,4.77c-0.59,1.59-1.59,2.91-3.02,3.95c-1.43,1.04-3.41,1.78-5.95,2.2 c-2.47,0.41-4.47,0.45-5.99,0.1c-1.53-0.34-2.84-1-3.95-1.96c-1.1-0.97-2.05-2.26-2.83-3.88l7.39-2.27 c0.55,1.48,1.19,2.46,1.91,2.95c0.72,0.49,1.56,0.65,2.53,0.49c1.01-0.17,1.79-0.68,2.34-1.54c0.55-0.85,0.72-1.9,0.51-3.14 c-0.21-1.26-0.7-2.18-1.46-2.77c-0.76-0.58-1.7-0.78-2.81-0.6c-0.59,0.1-1.38,0.38-2.36,0.85l-0.51-5.47 c0.42-0.01,0.75-0.03,0.98-0.07c0.98-0.16,1.74-0.62,2.29-1.35c0.55-0.74,0.75-1.53,0.61-2.39c-0.14-0.83-0.5-1.45-1.06-1.85 c-0.58-0.41-1.29-0.55-2.15-0.4c-0.89,0.15-1.56,0.53-2.03,1.16C91.83,74.57,91.61,75.57,91.64,76.94L91.64,76.94z M62.77,11.41 l4.62,27.72l-7.65,1.28l-3.02-18.13c-1.08,1.15-2.15,2.1-3.22,2.87c-1.06,0.77-2.43,1.57-4.08,2.39l-1.03-6.17 c2.44-1.27,4.27-2.6,5.5-4.01c1.23-1.41,2.11-3.04,2.63-4.9L62.77,11.41L62.77,11.41z M17.77,56.97l36.92,10.88 c3.28,0.97,5.17,4.44,4.2,7.72l-9.8,33.26c-0.97,3.28-4.44,5.17-7.72,4.2L4.46,102.16c-3.28-0.97-5.17-4.44-4.2-7.72l9.8-33.26 C11.02,57.9,14.49,56.01,17.77,56.97L17.77,56.97z M44.48,86l-5.06-0.72c-0.28,0.32-0.59,0.63-0.93,0.92 c-1.28,1.1-3.32,2.13-6.12,3.08c-1.66,0.54-2.77,0.94-3.35,1.18c-0.58,0.25-1.27,0.58-2.08,1.01l10.68,3.16l-1.65,5.56l-20.51-6.06 c0.83-1.95,2.11-3.65,3.83-5.07c1.72-1.43,4.57-2.88,8.57-4.34c0.76-0.28,1.43-0.54,2.03-0.79l0,0c1.34-0.56,2.28-1.04,2.83-1.46 c0.79-0.61,1.29-1.26,1.49-1.95c0.22-0.75,0.14-1.47-0.26-2.17c-0.4-0.7-1.02-1.17-1.86-1.42c-0.87-0.26-1.67-0.19-2.38,0.19 c-0.72,0.39-1.38,1.25-1.98,2.59l-6.67-2.58c0.84-1.85,1.78-3.2,2.81-4.07c1.04-0.87,2.29-1.4,3.76-1.59 c1.48-0.19,3.36,0.05,5.67,0.74c2.4,0.71,4.19,1.54,5.37,2.48c1.17,0.94,1.98,2.09,2.4,3.45c0.43,1.37,0.44,2.75,0.02,4.16 c-0.33,1.1-0.88,2.09-1.66,2.99L44.48,86L44.48,86z M36.49,6.19l38-6.11c3.37-0.54,6.58,1.78,7.12,5.15l5.51,34.24 c0.54,3.37-1.78,6.58-5.15,7.12l-38,6.11c-3.37,0.54-6.58-1.78-7.12-5.15l-5.51-34.24C30.8,9.94,33.12,6.73,36.49,6.19L36.49,6.19z"
    )
    return svg

  def alphabet(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """

    https://uxwing.com/toy-alphabet-blocks-icon/

    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
      path="M72.17,60.87l38-6.11c3.37-0.54,6.58,1.77,7.12,5.15l5.51,34.24c0.54,3.37-1.78,6.58-5.15,7.12l-38,6.11 c-3.37,0.54-6.58-1.78-7.12-5.15l-5.51-34.24C66.48,64.62,68.8,61.41,72.17,60.87L72.17,60.87z M17.77,56.97l36.92,10.88 c3.28,0.97,5.17,4.44,4.2,7.72l-9.8,33.26c-0.97,3.28-4.44,5.17-7.72,4.2L4.46,102.16c-3.28-0.97-5.17-4.44-4.2-7.72l9.8-33.26 C11.02,57.9,14.49,56.01,17.77,56.97L17.77,56.97z M35.25,90.91l5.95,4.54c-1.16,1.71-2.46,3.02-3.9,3.91c-1.44,0.9-3,1.4-4.68,1.5 c-1.68,0.1-3.62-0.26-5.84-1.1c-2.7-1.01-4.75-2.23-6.17-3.65c-1.41-1.42-2.36-3.35-2.86-5.79c-0.5-2.43-0.18-5.19,0.98-8.26 c1.54-4.09,3.81-6.83,6.81-8.21c3.01-1.38,6.51-1.32,10.5,0.18c3.12,1.17,5.34,2.72,6.65,4.66c1.31,1.93,1.91,4.37,1.79,7.31 l-7.3-1.04c0.05-0.84,0-1.48-0.13-1.92c-0.21-0.74-0.57-1.39-1.07-1.93c-0.5-0.55-1.14-0.97-1.9-1.25 c-1.74-0.65-3.33-0.46-4.78,0.59c-1.08,0.77-2.05,2.26-2.88,4.47c-1.03,2.74-1.32,4.77-0.87,6.11c0.45,1.33,1.43,2.28,2.94,2.84 c1.46,0.55,2.72,0.56,3.78,0.01C33.34,93.33,34.33,92.34,35.25,90.91L35.25,90.91z M36.49,6.19l38-6.11 c3.37-0.54,6.58,1.77,7.12,5.15l5.51,34.24c0.54,3.37-1.77,6.58-5.15,7.12l-38,6.11c-3.37,0.54-6.58-1.78-7.12-5.15l-5.51-34.24 C30.8,9.94,33.12,6.73,36.49,6.19L36.49,6.19z M64.11,33.29l-9.15,1.45l-0.63,4.51l-8.24,1.31l5.68-27.69l8.84-1.4l13.94,24.57 l-8.45,1.34L64.11,33.29L64.11,33.29z M61.5,27.91l-4.34-8.94l-1.37,9.84L61.5,27.91L61.5,27.91z M83.13,70.92l15.12-2.4 c2.52-0.4,4.55-0.08,6.1,0.95c1.55,1.03,2.47,2.47,2.76,4.31c0.25,1.54-0.02,2.95-0.82,4.2c-0.52,0.84-1.37,1.57-2.54,2.2 c1.95,0.15,3.45,0.71,4.51,1.67c1.06,0.96,1.72,2.27,1.98,3.93c0.22,1.36,0.09,2.62-0.36,3.8c-0.46,1.18-1.19,2.17-2.18,2.98 c-0.62,0.5-1.6,0.95-2.94,1.34c-1.78,0.53-2.97,0.84-3.56,0.93l-13.94,2.21L83.13,70.92L83.13,70.92z M92.9,79.88l3.52-0.56 c1.26-0.2,2.11-0.56,2.53-1.07c0.42-0.52,0.57-1.18,0.44-2c-0.12-0.76-0.46-1.32-1.02-1.66c-0.56-0.35-1.46-0.43-2.68-0.24 l-3.58,0.57L92.9,79.88L92.9,79.88z M94.53,90.13l4.12-0.65c1.39-0.22,2.33-0.63,2.83-1.21c0.49-0.58,0.67-1.29,0.54-2.12 c-0.12-0.77-0.5-1.35-1.14-1.73c-0.64-0.38-1.67-0.46-3.09-0.23l-4.1,0.65L94.53,90.13L94.53,90.13z"
    )
    return svg

  def bulb(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """

    https://uxwing.com/toy-alphabet-blocks-icon/

    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
      path="M44.13,102.06c-1.14,0.03-2.14-0.81-2.3-1.96c-0.17-1.2,0.64-2.31,1.82-2.54c-1.3-7.37-4.85-11.43-8.6-15.72 c-2.92-3.34-5.95-6.81-8.34-11.92c-2.35-5.03-3.64-10.23-3.6-15.63c0.05-5.4,1.42-10.96,4.4-16.71c0.02-0.04,0.04-0.07,0.06-0.11 l0,0c3.91-6.62,9.38-11.04,15.47-13.52c5.11-2.09,10.66-2.8,16.1-2.3c5.42,0.5,10.73,2.2,15.37,4.94 c5.9,3.49,10.75,8.67,13.42,15.21c1.44,3.54,2.42,7.49,2.54,11.82c0.12,4.31-0.62,8.96-2.61,13.88 c-2.66,6.59-6.18,10.68-9.47,14.51c-3.03,3.53-5.85,6.81-7.42,11.84c0.89,0.21,1.59,0.94,1.73,1.9c0.17,1.24-0.7,2.39-1.94,2.56 l-0.77,0.11c-0.14,1.09-0.23,2.26-0.27,3.51l0.25-0.04c1.24-0.17,2.39,0.7,2.56,1.94c0.17,1.24-0.7,2.39-1.94,2.56l-0.78,0.11 c0.01,0.15,0.02,0.3,0.03,0.45l0,0c0.07,0.88,0.08,1.73,0.03,2.54l0.13-0.02c1.25-0.15,2.38,0.74,2.54,1.98 c0.15,1.25-0.74,2.38-1.98,2.54l-1.68,0.21c-1.2,3.11-3.34,5.48-5.87,6.94c-1.74,1.01-3.67,1.59-5.61,1.71 c-1.97,0.12-3.96-0.25-5.78-1.13c-2.08-1.02-3.94-2.71-5.29-5.14c-0.65-0.33-1.13-0.97-1.23-1.75c-0.04-0.31-0.01-0.61,0.07-0.89 c-0.39-1.16-0.68-2.43-0.87-3.83l-0.07,0.01c-1.24,0.17-2.39-0.7-2.56-1.94c-0.17-1.24,0.7-2.39,1.94-2.56l0.54-0.08 C44.19,104.32,44.18,103.16,44.13,102.06L44.13,102.06z M2.18,58.86C1.01,58.89,0.04,57.98,0,56.81c-0.04-1.17,0.88-2.14,2.05-2.18 l8.7-0.3c1.17-0.04,2.14,0.88,2.18,2.05c0.04,1.17-0.88,2.14-2.05,2.18L2.18,58.86L2.18,58.86z M110.68,50.25 c1.16-0.12,2.2,0.73,2.32,1.89c0.12,1.16-0.73,2.2-1.89,2.32l-8.66,0.91c-1.16,0.12-2.2-0.73-2.32-1.89 c-0.12-1.16,0.73-2.2,1.89-2.32L110.68,50.25L110.68,50.25z M94.91,14.78c0.65-0.97,1.96-1.23,2.93-0.58 c0.97,0.65,1.23,1.96,0.58,2.93l-4.84,7.24c-0.65,0.97-1.96,1.23-2.93,0.58c-0.97-0.65-1.23-1.96-0.58-2.93L94.91,14.78 L94.91,14.78z M57.63,2.06c0.03-1.17,1-2.09,2.16-2.06c1.17,0.03,2.09,1,2.06,2.16l-0.22,8.7c-0.03,1.17-1,2.09-2.16,2.06 c-1.17-0.03-2.09-1-2.06-2.16L57.63,2.06L57.63,2.06z M13.88,15.53c-0.86-0.8-0.9-2.14-0.11-2.99c0.8-0.86,2.14-0.9,2.99-0.11 l6.37,5.94c0.86,0.8,0.9,2.14,0.11,2.99c-0.8,0.86-2.14,0.9-2.99,0.11L13.88,15.53L13.88,15.53z M47.88,96.95l18.49-2.63 c1.59-6.7,5.05-10.73,8.8-15.08c3.08-3.58,6.36-7.4,8.76-13.34c1.76-4.35,2.41-8.43,2.31-12.19c-0.1-3.75-0.96-7.21-2.24-10.34 c-2.3-5.63-6.51-10.11-11.65-13.15c-4.11-2.43-8.8-3.94-13.59-4.37c-4.77-0.44-9.64,0.19-14.13,2.02 c-5.26,2.15-9.99,5.97-13.39,11.72c-2.64,5.12-3.86,10.02-3.9,14.73c-0.04,4.74,1.11,9.33,3.2,13.8c2.13,4.56,4.97,7.8,7.69,10.92 C42.47,83.9,46.48,88.49,47.88,96.95L47.88,96.95z M65.62,99.02l-17.27,2.45c0.05,1.1,0.07,2.25,0.05,3.47l17.05-2.42 C65.47,101.29,65.52,100.12,65.62,99.02L65.62,99.02z M48.49,109.52c0.12,0.92,0.3,1.76,0.53,2.54l16.55-2.04 c0.11-0.86,0.13-1.77,0.05-2.74l0,0l0-0.02l-0.01-0.17L48.49,109.52L48.49,109.52z M51.37,116.36c0.64,0.67,1.35,1.19,2.1,1.55 c1.15,0.56,2.42,0.79,3.67,0.72c1.29-0.08,2.57-0.47,3.74-1.15c1.1-0.64,2.09-1.53,2.88-2.65L51.37,116.36L51.37,116.36z"
    )
    return svg

  def road(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """

    https://uxwing.com/road-route-destination-icon/

    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
      path="M101.41,37.05c-1.95,2.14-4.22,4.05-6.77,5.6c-0.31,0.23-0.74,0.26-1.09,0.03c-3.76-2.39-6.93-5.27-9.41-8.4 c-3.43-4.3-5.59-9.07-6.33-13.66c-0.75-4.66-0.05-9.14,2.27-12.79C81,6.4,82.17,5.08,83.59,3.95c3.27-2.6,7-3.98,10.73-3.95 c3.58,0.03,7.12,1.36,10.18,4.15c1.08,0.98,1.98,2.09,2.72,3.31c2.49,4.11,3.03,9.34,1.93,14.65 C108.07,27.36,105.39,32.69,101.41,37.05L101.41,37.05L101.41,37.05z M9.82,64.7h8.72c1.45,0,2.57,0.36,3.35,1.08 c0.78,0.72,1.17,1.61,1.17,2.67c0,0.89-0.28,1.66-0.83,2.29c-0.37,0.43-0.91,0.76-1.62,1.01c1.08,0.26,1.88,0.7,2.39,1.34 c0.51,0.63,0.76,1.43,0.76,2.39c0,0.78-0.18,1.48-0.54,2.11c-0.36,0.62-0.86,1.12-1.49,1.48c-0.39,0.22-0.98,0.39-1.77,0.49 c-1.05,0.14-1.74,0.21-2.09,0.21H9.82V64.7L9.82,64.7z M14.51,70.62h2.03c0.73,0,1.23-0.13,1.52-0.38 c0.28-0.25,0.43-0.61,0.43-1.09c0-0.44-0.14-0.78-0.43-1.03c-0.28-0.25-0.78-0.37-1.49-0.37h-2.06V70.62L14.51,70.62z M14.51,76.53 h2.37c0.8,0,1.37-0.14,1.7-0.43c0.33-0.28,0.49-0.66,0.49-1.14c0-0.45-0.16-0.8-0.49-1.07c-0.33-0.27-0.9-0.41-1.71-0.41h-2.36 V76.53L14.51,76.53z M96.62,21.82h-5.27l-0.76,2.48h-4.75l5.67-15.07h5.1l5.65,15.07h-4.87L96.62,21.82L96.62,21.82z M95.64,18.56 l-1.64-5.41l-1.65,5.41H95.64L95.64,18.56z M23.88,92.06c-1.95,2.14-4.22,4.05-6.77,5.6c-0.31,0.23-0.74,0.26-1.09,0.03 c-3.76-2.4-6.93-5.27-9.41-8.4C3.19,85,1.03,80.23,0.29,75.63c-0.75-4.66-0.05-9.14,2.27-12.78c0.91-1.44,2.08-2.75,3.51-3.88 c3.27-2.6,7-3.98,10.72-3.95c3.58,0.03,7.12,1.36,10.18,4.15c1.08,0.98,1.98,2.09,2.72,3.31c2.49,4.11,3.03,9.34,1.93,14.65 C30.54,82.37,27.86,87.7,23.88,92.06L23.88,92.06L23.88,92.06z M17.07,103.04c4.51,0,8.32,3.02,9.52,7.14h59.97 c2.96,0,5.66-1.21,7.62-3.17c1.96-1.96,3.17-4.65,3.17-7.62l0,0c0-2.96-1.21-5.66-3.17-7.62c-1.96-1.96-4.65-3.17-7.62-3.17H65.58 v0c-4.71,0-8.99-1.92-12.09-5.02c-3.1-3.1-5.02-7.38-5.02-12.09l0,0c0-4.71,1.92-8.99,5.02-12.09c3.1-3.1,7.38-5.02,12.09-5.02 h18.97c1.3-3.96,5.03-6.82,9.42-6.82c5.48,0,9.92,4.44,9.92,9.92c0,5.48-4.44,9.92-9.92,9.92c-4.35,0-8.04-2.8-9.38-6.69H65.58 c-2.96,0-5.66,1.21-7.62,3.17c-1.96,1.96-3.17,4.65-3.17,7.62l0,0c0,2.96,1.21,5.66,3.17,7.62c1.94,1.94,4.61,3.15,7.55,3.17v0 h21.06c4.71,0,8.99,1.92,12.09,5.02c3.1,3.1,5.02,7.38,5.02,12.09l0,0c0,4.71-1.92,8.99-5.02,12.09c-3.1,3.1-7.38,5.02-12.09,5.02 H26.34c-1.43,3.73-5.04,6.37-9.27,6.37c-5.48,0-9.92-4.44-9.92-9.92C7.15,107.48,11.59,103.04,17.07,103.04L17.07,103.04z"
    )
    return svg
