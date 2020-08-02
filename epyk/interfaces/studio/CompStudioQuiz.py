#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

from epyk.core.css import Defaults_css
from epyk.core.css.themes import ThemeRed


class Quiz(object):

  def __init__(self, context):
    self.parent = context

  def theme(self):
    self.parent.context.rptObj.theme = ThemeRed.Pink()

  def position(self, longitude, latitude, flag=None, width=(100, '%'), height=("auto", ''), icon="fas fa-map-marked-alt", options=None, profile=None):
    """

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

    """
    hr = self.parent.context.rptObj.ui.layouts.hr()
    hr.style.css.padding = "0 20%"
    hr.hr.style.css.border_color = self.parent.context.rptObj.theme.colors[5]
    hr.hr.style.css.border_width = size
    return hr

  def missing(self, text, icon="fas fa-ellipsis-h", width=(100, '%'), height=("auto", ''), options=None, profile=None):
    """

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
