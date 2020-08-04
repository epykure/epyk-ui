#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

from epyk.core.css import Defaults_css
from epyk.core.css.themes import ThemeBlue
from epyk.interfaces import Arguments


class Blog(object):

  def __init__(self, context):
    self.parent = context

  def theme(self):
    """
    Description:
    ------------

    """
    self.parent.context.rptObj.theme = ThemeBlue.Blue()
    Defaults_css.Font.size = 16
    Defaults_css.Font.header_size = Defaults_css.Font.size + 4
    self.parent.context.rptObj.body.template({"margin": '0 10%'})

  def delimiter(self, size=5):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param size:
    """
    hr = self.parent.context.rptObj.ui.layouts.hr()
    hr.style.css.padding = "0 20%"
    hr.hr.style.css.border_top = "%spx double %s" % (size, self.parent.context.rptObj.theme.colors[5])
    return hr

  def title(self, text, width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    """
    Description:
    ------------


    Attributes:
    ----------
    :param text:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")

    text = self.parent.context.rptObj.py.encode_html(text)
    title = self.parent.context.rptObj.ui.title(text, width=width, height=height, options=options, profile=profile)
    title.style.css.white_space = 'normal'
    return title

  def link(self, text, url, width=(100, '%'), height=(30, 'px'), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param url:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")

    text = self.parent.context.rptObj.py.encode_html(text)
    return self.parent.context.rptObj.ui.link(text, url, width=width, height=height, options=options, profile=profile)

  def italic(self, text, width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")

    text = self.parent.context.rptObj.py.encode_html(text)
    return self.parent.context.rptObj.ui.tags.i(text, width=width, height=height, options=options, profile=profile)

  def center(self, text, width=(100, '%'), height=(30, 'px'), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")

    text = self.parent.context.rptObj.py.encode_html(text)
    return self.parent.context.rptObj.ui.text(text, align="center", width=width, height=height, options=options, profile=profile)

  def breadcrumb(self, values, selected=None, width=(100, '%'), height=(30, 'px'), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param values:
    :param selected:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")

    bcrumb = self.parent.context.rptObj.ui.breadcrumb(values, selected, width, height, options, profile)
    return bcrumb

  def paragraph(self, text, css=None, align="left", width=(100, '%'), height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param css:
    :param align:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")

    text = self.parent.context.rptObj.py.encode_html(text)
    text = self.parent.context.rptObj.py.markdown.resolve(text, css_attrs=css)
    container = self.parent.context.rptObj.ui.div(text, align=align, width=width, height=height, options=options, profile=profile)
    return container

  def quote(self, text, author, job):
    pass

  def button(self, text, icon=None, border=True, background=True, width=(100, '%'), align="center", height=(None, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param icon:
    :param border:
    :param background:
    :param width:
    :param align:
    :param height:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")

    button = self.parent.context.rptObj.ui.button(text, icon=icon, width=width, align=align, height=height, options=options, profile=profile)
    button.style.clear()
    button.style.css.padding = "0 10px"
    button.style.css.background = self.parent.context.rptObj.theme.greys[0]
    button.style.hover({"color": self.parent.context.rptObj.theme.colors[-1]})
    return button

  def picture(self, img, label=None, width=(300, 'px'), align="center", height=(None, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param img:
    :param label:
    :param width:
    :param align:
    :param height:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")

    if label is None:
      img = self.parent.context.rptObj.ui.img(img, width=width, height=height, align=align, options=options, profile=profile)
      img.style.css.margin_top = 5
      img.style.css.margin_bottom = 5
      return img

  def video(self, img):
    return self.parent.context.rptObj.ui.img(img)


class Gallery(Blog):

  def mosaic(self, pictures, columns=6, width=(None, '%'), height=('auto', ''), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param pictures:
    :param columns:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    
    grid = self.parent.context.rptObj.ui.grid(width=width, height=height, options=options, profile=profile)
    row = self.parent.context.rptObj.ui.row()
    for i, picture in enumerate(pictures):
      if i % columns == 0:
        grid.add(row)
        row = self.parent.context.rptObj.ui.row()
      if not hasattr(picture, 'options'):
        picture = self.parent.context.rptObj.ui.img(picture)
      row.add(picture)
    grid.add(row)
    return grid
