#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

from epyk.core.css import Defaults_css
from epyk.core.css.themes import ThemeBlue


class Blog(object):

  def __init__(self, context):
    self.parent = context

  def theme(self):
    """
    Description:
    ------------
    Set the default theme for a blog.
    This will add a template to the body in order to have a header, template and footer
    """
    self.parent.context.rptObj.theme = ThemeBlue.Blue()
    Defaults_css.Font.size = 16
    Defaults_css.Font.header_size = Defaults_css.Font.size + 4
    self.parent.context.rptObj.body.template({"margin": '0 10%'})

  def delimiter(self, size=5, count=1, width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    """
    Description:
    ------------
    Add a line delimiter to the page

    Attributes:
    ----------
    :param size: Integer. The size of the line.
    :param count: Integer. The number of lines
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    hr = self.parent.context.rptObj.ui.layouts.hr(count, width=width, height=height, align=None, options=options, profile=profile)
    hr.style.css.padding = "0 20%"
    hr.hr.style.css.border_top = "%spx double %s" % (size, self.parent.context.rptObj.theme.colors[5])
    return hr

  def title(self, text, width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    """
    Description:
    ------------
    Add a title to the page

    Attributes:
    ----------
    :param text: String.
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options:
    :param profile:
    """
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
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options:
    :param profile:
    """
    text = self.parent.context.rptObj.py.encode_html(text)
    return self.parent.context.rptObj.ui.link(text, url, width=width, height=height, options=options, profile=profile)

  def italic(self, text, width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options:
    :param profile:
    """
    text = self.parent.context.rptObj.py.encode_html(text)
    return self.parent.context.rptObj.ui.tags.i(text, width=width, height=height, options=options, profile=profile)

  def center(self, text, width=(100, '%'), height=(30, 'px'), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options:
    :param profile:
    """
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
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options:
    :param profile:
    """
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
    text = self.parent.context.rptObj.py.encode_html(text)
    text = self.parent.context.rptObj.py.markdown.resolve(text, css_attrs=css)
    container = self.parent.context.rptObj.ui.div(text, align=align, width=width, height=height, options=options, profile=profile)
    return container

  def quote(self, text, author, job=None, align="left", width=(100, '%'), height=("auto", ''), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param author:
    :param job:
    :param align:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options:
    :param profile:
    """
    component = self.parent.context.rptObj.ui.div(align=align, width=width, height=height, options=options, profile=profile)
    component.style.css.margin_bottom = 5
    quote = self.parent.context.rptObj.ui.pictos.quote()
    quote.style.css.margin_bottom = -20
    component.add(quote)
    component.text = self.parent.context.rptObj.ui.text("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%s" % self.parent.context.rptObj.py.encode_html(text))
    component.add(component.text)
    component.author = self.parent.context.rptObj.ui.text(self.parent.context.rptObj.py.encode_html(author))
    component.author.style.css.bold()
    if job is not None:
      component.job = self.parent.context.rptObj.ui.text(self.parent.context.rptObj.py.encode_html(job))
      component.add(self.parent.context.rptObj.ui.div([component.author, self.parent.context.rptObj.ui.text(",&nbsp;"), component.job], align="right"))
    else:
      component.add(self.parent.context.rptObj.ui.div([component.author], align="right"))
    return component

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
    :param align:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options:
    :param profile:
    """
    button = self.parent.context.rptObj.ui.button(text, icon=icon, width=width, align=align, height=height, options=options, profile=profile)
    button.style.clear()
    button.style.css.padding = "0 10px"
    button.style.css.background = self.parent.context.rptObj.theme.greys[0]
    button.style.hover({"color": self.parent.context.rptObj.theme.colors[-1]})
    return button

  def picture(self, image, label=None, width=(300, 'px'), align="center", height=(None, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param image:
    :param label:
    :param align:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options:
    :param profile:
    """
    if label is None:
      img = self.parent.context.rptObj.ui.img(image, width=width, height=height, align=align, options=options, profile=profile)
      img.style.css.margin_top = 5
      img.style.css.margin_bottom = 5
      return img

    component = self.parent.context.rptObj.ui.div(align=align, width=width, height=height, options=options, profile=profile)
    component.image = self.parent.context.rptObj.ui.img(image, width=width, height=height, options=options, profile=profile)
    component.style.css.position = "relative"
    component.add(component.image)
    if not hasattr(label, 'options'):
      component.label = self.parent.context.rptObj.ui.div(label)
      component.label.style.css.position = "absolute"
      component.label.style.css.background = "white"
      component.label.style.css.width = "auto"
      component.label.style.css.max_width = "calc(100%% - %spx)" % (width[0] / 10)
      component.label.style.css.padding = "0 10px"
      component.label.style.css.bottom = 35
    else:
      component.label = label
    component.add(component.label)
    component.style.css.margin_top = 5
    component.style.css.margin_bottom = 5
    if align == 'center':
      component.style.css.margin = "auto"
      component.style.css.display = "block"
    return component

  def video(self, video, label=None, width=(300, 'px'), align="center", height=(None, 'px'), htmlCode=None, profile=None, options=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param video:
    :param label:
    :param align:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode:
    :param profile:
    :param options:
    """
    if label is None:
      return self.parent.context.rptObj.ui.media.video(video, width=width, height=height, align=align)

    component = self.parent.context.rptObj.ui.div(align=align, width=width, height=height, options=options, profile=profile)
    component.video = self.parent.context.rptObj.ui.media.video(video, width=width, height=height, options=options, profile=profile)
    component.style.css.position = "relative"
    component.add(component.video)
    if not hasattr(label, 'options'):
      component.label = self.parent.context.rptObj.ui.div(label)
      component.label.style.css.position = "absolute"
      component.label.style.css.background = "white"
      component.label.style.css.opacity = 0.6
      component.label.style.css.width = "auto"
      component.label.style.css.padding = "0 10px"
      component.label.style.css.top = 0
      component.label.style.css.right = 0
    else:
      component.label = label
    component.add(component.label)
    component.style.css.margin_top = 5
    component.style.css.margin_bottom = 5
    if align == 'center':
      component.style.css.margin = "auto"
      component.style.css.display = "block"
    return component

  def youtube(self, link, width=(100, '%'), height=(None, 'px'), htmlCode=None, profile=None, options=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param link:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode:
    :param profile:
    :param options:
    """
    return self.parent.context.rptObj.ui.media.youtube(link, width=width, height=height, htmlCode=htmlCode, profile=profile, options=options)

  def signature(self):
    pass

  def time(self, date, icon="fas fa-circle", align="left", width=("auto", ''), height=(None, "px"), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param date:
    :param icon:
    :param align:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options:
    :param profile:
    """
    date_time_obj = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
    current = datetime.datetime.now()
    delta_time = current - date_time_obj
    component = self.parent.context.rptObj.ui.div(align=align, width=width, height=height, options=options, profile=profile)
    icon = self.parent.context.rptObj.ui.icons.awesome(icon)
    icon.icon.style.css.font_factor(-3)
    icon.icon.style.css.color = self.parent.context.rptObj.theme.colors[5]
    component.add(icon)
    if delta_time.days == 0:
      if date_time_obj.day != current.day:
        component.add(self.parent.context.rptObj.ui.text("Yesterday"))
      else:
        if delta_time.seconds > 3600:
          hours = int(delta_time.seconds / 3600)
          minutes = int((delta_time.seconds - hours * 3600) / 60)
          seconds = delta_time.seconds - hours * 3600 - minutes * 60
          component.add(self.parent.context.rptObj.ui.text("%s h %s min %s s" % (hours, minutes, seconds)))
        elif delta_time.seconds > 60:
          minutes = int(delta_time.seconds / 60)
          seconds = delta_time.seconds - minutes * 60
          component.add(self.parent.context.rptObj.ui.text("%s min %s s" % (minutes, seconds)))
    else:
      text = self.parent.context.rptObj.ui.text(date_time_obj.strftime("%d %B %Y"))
      delta_time = current - date_time_obj
      year = delta_time.days // 365
      months = (delta_time.days - year * 365) // 12
      days = delta_time.days - year * 365 - months * 12
      if year:
        if months:
          text.tooltip("%s years %s months %s days" % (year, months, days))
        else:
          text.tooltip("%s years %s days" % (year, days))
      elif months:
        if days:
          text.tooltip("%s months %s days" % (months, days))
        else:
          text.tooltip("%s days" % days)
      else:
        text.tooltip("%s days" % days)
      component.add(text)
    return component

  def label(self):
    pass


class Gallery(Blog):

  def mosaic(self, pictures, columns=6, width=(None, '%'), height=('auto', ''), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param pictures:
    :param columns:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options:
    :param profile:
    """
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
