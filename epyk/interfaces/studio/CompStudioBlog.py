#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

from epyk.core.css import Defaults_css
from epyk.core.css.themes import ThemeBlue


class Blog(object):

  def __init__(self, context):
    self.parent = context

  def theme(self):
    self.parent.context.rptObj.theme = ThemeBlue.Blue()

  def title(self, text):
    """

    :param text:
    """
    text = self.parent.context.rptObj.py.encode_html(text)
    return self.parent.context.rptObj.ui.title(text)

  def link(self, text, url):
    text = self.parent.context.rptObj.py.encode_html(text)
    return self.parent.context.rptObj.ui.link(text, url)

  def italic(self, text):
    """

    :param text:
    """
    text = self.parent.context.rptObj.py.encode_html(text)
    return self.parent.context.rptObj.ui.tags.i(text)

  def center(self, text):
    """

    :param text:
    """
    text = self.parent.context.rptObj.py.encode_html(text)
    return self.parent.context.rptObj.ui.text(text, align="center")

  def breadcrumb(self, values, selected=None, width=(100, '%'), height=(30, 'px'), options=None, profile=None):
    """

    :param values:
    :param selected:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    bcrumb = self.parent.context.rptObj.ui.breadcrumb(values, selected, width, height, options, profile)
    return bcrumb

  def paragraph(self, text, css=None, align="left", width=(100, '%'), height=("auto", ''), options=None, profile=None):
    """

    :param text:
    :param css:
    :param align:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    text = self.parent.context.rptObj.py.encode_html(text)
    text = self.parent.context.rptObj.py.markdown.resolve(text, css_attrs=css)
    container = self.parent.context.rptObj.ui.div(text, align=align, width=width, height=height, options=options, profile=profile)
    return container

  def quote(self, text, author, job):
    pass

  def button(self, text, author, job):
    pass

  def picture(self, img):
    return self.parent.context.rptObj.ui.img(img)

  def video(self, img):
    return self.parent.context.rptObj.ui.img(img)


class Gallery(object):

  def __init__(self, context):
    self.parent = context
