#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

from epyk.core import html
from epyk.core.css import Defaults_css
from epyk.core.css.themes import ThemeRed


class Event(object):
  def __init__(self, context):
    self.parent = context

  def flip(self):
    """
    https://www.w3schools.com/howto/howto_css_flip_box.asp
    :return:
    """


class Wedding(object):

  def __init__(self, context):
    self.parent = context

  def theme(self):
    self.parent.context.rptObj.theme = ThemeRed.Pink()

  def banner(self, data, size_notch=0, background=None, width=(100, '%'), align="center", height=(None, 'px'), options=None, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param data:
    :param size_notch:
    :param background:
    :param width:
    :param align:
    :param height:
    :param options:
    :param profile:
    """
    div = self.parent.context.rptObj.ui.div(width=width, height=height, options=options, profile=profile, align=align)
    if not hasattr(data, 'options'):
      data = self.parent.context.rptObj.ui.div(data, width=("auto", ""))
      data.style.css.display = "inline-block"
      data.style.css.text_align = align
      data.style.css.font_size = Defaults_css.font(size_notch)
    div.add(data)
    div.style.css.background_color = background or self.parent.context.rptObj.theme.colors[3]
    div.style.css.padding = "20px 15px"
    div.style.css.margin = "auto"
    div.style.css.font_size = Defaults_css.font(size_notch)
    div.style.css.color = self.parent.context.rptObj.theme.greys[-1]
    div.style.css.top = 0
    return div

  def title(self, text=None, options=None, tooltip="", width=(None, "px"), height=('auto', ""), htmlCode=None, profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param text:
    :param options:
    :param tooltip:
    :param width:
    :param height:
    :param htmlCode:
    :param profile:
    """
    dflt_options = {'markdown': False}
    if options is not None:
      dflt_options.update(options)
    html_title = html.HtmlTags.HtmlGeneric(self.parent.context.rptObj, "div", text, width, height, htmlCode, tooltip, dflt_options, profile)
    html_title.style.css.font_size = Defaults_css.font(12)
    html_title.style.css.text_align = 'left'
    html_title.style.css.margin_top = 10
    html_title.style.css.color = self.parent.context.rptObj.theme.colors[-1]
    return html_title

  def background(self, url, width=(100, "%"), height=(300, "px"), size="cover", margin=0, align="center", position="middle"):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param url:
    :param width:
    :param height:
    :param size:
    :param margin:
    """
    div = self.parent.context.rptObj.ui.div(height=height, width=width)
    div.style.css.background_url(url, size=size, margin=margin)
    div.style.css.display = "block"
    div.style.css.text_align = align
    div.style.css.vertical_align = position
    div.style.css.padding = "auto"
    return div

  def button(self, text="", icon=None, width=(None, "%"), height=(None, "px"), align="left", htmlCode=None,
             tooltip=None, profile=None, options=None):
    """

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
    button.style.hover({"color": self.parent.context.rptObj.theme.colors[-1]})
    return button

  def time(self, date, icon="fas fa-circle", align="left", width=("auto", ''), height=(None, "px"), options=None, profile=None):
    """

    :param date:
    :param icon:
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

  def picture(self, image=None, path=None, width=(100, "%"), height=(None, "px"), align="center", htmlCode=None,
              profile=None, options=None):
    """
    Description:
    ------------
    Add an HTML image to the page. The path can be defined either in a absolute or relative format.

    Tip: The absolute format does not work on servers. It is recommended to use relative starting to the root of the server

    Usage::

      rptObj.ui.img("epykIcon.PNG", path=r"../../../static/images", height=(50, "px"))


    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlImage.Image`

    Related Pages:

      https://www.w3schools.com/bootstrap/bootstrap_ref_css_images.asp
      https://www.w3schools.com/cssref/css3_pr_border-radius.asp

    Attributes:
    ----------
    :param image: String. The image file name
    :param path: Optional. String. The image file path
    :param width: Optional. Tuple. The component width in pixel or percentage
    :param height: Optional. Tuple. The component height in pixel or percentage
    :param align:
    :param htmlCode:
    :param profile:
    :param options:
    """
    if height[0] is not None and width[1] == '%':
      width = ("auto", '')
    html_image = html.HtmlImage.Image(self.parent.context.rptObj, image, path, align, htmlCode, width, height, profile, options or {})
    return html_image

  def address(self, street, icon="fas fa-map-marker-alt", align="left", width=("auto", ''), height=(None, "px"), options=None, profile=None):
    component = self.parent.context.rptObj.ui.div(align=align, width=width, height=height, options=options,
                                                  profile=profile)
    icon = self.parent.context.rptObj.ui.icons.awesome(icon)
    icon.icon.style.css.font_factor(2)
    icon.icon.style.css.color = self.parent.context.rptObj.theme.colors[5]
    component.add(icon)
    return component

  def block(self, text, align="left", width=("80", '%'), height=(None, "px"), options=None, profile=None):
    """

    :param text:
    :param align:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    component = self.parent.context.rptObj.ui.div(align=align, width=width, height=height, options=options, profile=profile)
    component.style.css.border = "1px solid %s" % self.parent.context.rptObj.theme.colors[-1]
    component.style.css.border_left = "3px solid %s" % self.parent.context.rptObj.theme.colors[-1]
    if not hasattr(text, 'options'):
      component.text = self.parent.context.rptObj.ui.text(self.parent.context.rptObj.py.encode_html(text))
      component.add(component.text)
    component.style.css.margin = "auto"
    component.style.css.padding = 10
    component.style.css.display = "block"
    return component

  def paragraph(self):
    pass

class Birthday(object):
  def __init__(self, context):
    self.parent = context


class Show(object):
  def __init__(self, context):
    self.parent = context

  def contact(self):
    pass

  def location(self):
    pass

  def button(self, text="", icon=None, width=(None, "%"), height=(None, "px"), align="left", htmlCode=None,
             tooltip=None, profile=None, options=None):
    """

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
