#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

from epyk.core import html
from epyk.core.css import Defaults_css
from epyk.core.css.themes import ThemeRed


class Event(object):

  def __init__(self, context):
    self.parent = context

  def search(self, text="", placeholder='search', icon="fas fa-search", width=(100, "%"), height=(None, "px"),
             htmlCode=None, options=None, attrs=None, profile=None):
    """

    :param text:
    :param placeholder:
    :param icon:
    :param width:
    :param height:
    :param htmlCode:
    :param options:
    :param attrs:
    :param profile:
    """
    container = self.parent.context.rptObj.ui.div(width=width, height=height, options=options,
                                                  profile=profile)
    container.style.css.position = "relative"
    container.input = self.parent.context.rptObj.ui.inputs.d_search(text, placeholder, width, height, htmlCode, options, attrs, profile)
    container.input.style.css.border = "1px solid %s" % self.parent.context.rptObj.theme.greys[3]
    container.input.style.css.padding = "0 30px"
    container.input.style.css.text_align = "left"
    container.add(container.input)
    container.icon = self.parent.context.rptObj.ui.icons.awesome(icon)
    container.icon.icon.style.css.font_factor(0)
    container.icon.style.css.position = "absolute"
    container.icon.style.css.left = 5
    container.icon.icon.style.css.color = self.parent.context.rptObj.theme.colors[5]
    container.add(container.icon)
    return container

  def delimiter(self, size=1):
    """

    """
    hr = self.parent.context.rptObj.ui.layouts.hr()
    hr.style.css.padding = "0 20%"
    hr.hr.style.css.border_color = self.parent.context.rptObj.theme.colors[5]
    hr.hr.style.css.border_width = size
    return hr

  def mosaic(self, width=(None, '%'), height=(100, 'px'), options=None):
    pass

  def clients(self, logos, title="Client we have worked with...", content='', width=(100, '%'), height=("auto", ''), align="center", options=None,
               profile=False):
    """

    :param logos:
    :param title:
    :param content:
    :param width:
    :param height:
    :param align:
    :param options:
    :param profile:
    """
    banner = self.parent.context.rptObj.ui.banners.sponsor(logos, title, content, width=width, height=height, align=align,
                                                           options=options, profile=profile)
    banner.title.style.css.color = self.parent.context.rptObj.theme.colors[0]
    banner.style.css.background = self.parent.context.rptObj.theme.colors[6]
    return banner

  def sponsors(self, logos, title="Sponsors", content='', width=(100, '%'), height=("auto", ''), align="center", options=None,
               profile=False):
    """

    :param logos:
    :param title:
    :param content:
    :param width:
    :param height:
    :param align:
    :param options:
    :param profile:
    """
    banner = self.parent.context.rptObj.ui.banners.sponsor(logos, title, content, width=width, height=height, align=align,
                                                           options=options, profile=profile)
    banner.style.css.background = self.parent.context.rptObj.theme.colors[2]
    return banner

  def avatar(self, image=None, size=80, text=None, htmlCode=None, profile=None, options=None):
    """

    :param text:
    :param image:
    :param size:
    :param htmlCode:
    :param profile:
    :param options:
    """
    dfl_options = {"status": False}
    if options is not None:
      dfl_options.update(options)
    img = self.parent.context.rptObj.ui.images.avatar(image=image, text=text, width=(size, 'px'), height=(size, 'px'), htmlCode=htmlCode,
                                                      options=dfl_options, profile=profile)
    return img

  def progress(self, value, icon="", width=(100, '%'), height=(None, 'px'), options=None):
    pass

  def comment(self, avatar, placeholder="Let a comment", width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    """

    :param avatar:
    :param placeholder:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    container = self.parent.context.rptObj.ui.div(width=width, height=height, options=options, profile=profile)
    if not hasattr(avatar, 'options'):
      avatar = self.avatar(avatar)
      avatar.style.css.display = "inline-block"
    container.add(avatar)
    container.text = self.parent.context.rptObj.ui.textarea()
    container.text.style.css.display = "inline-block"
    container.text.style.css.float = "right"
    container.text.style.css.color = self.parent.context.rptObj.theme.greys[4]
    container.text.style.css.width = "calc(100% - 100px)"
    container.add(container.text)
    return container

  def dated(self, date, name=None, width=(None, '%'), height=(None, 'px'), align="left", format=None, options=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param date:
    :param name:
    :param width:
    :param height:
    :param format:
    :param options:
    """
    py_date = datetime.datetime.strptime(date, '%Y-%m-%d')
    container = self.parent.context.rptObj.ui.div(width=width, height=height)
    container.text = self.parent.context.rptObj.ui.text("Last updated %s, by" % py_date.strftime("%d %B %Y"), width=(None, ""))
    container.text.style.css.display = 'inline-block'
    container.text.style.css.color = self.parent.context.rptObj.theme.greys[5]
    container.add(container.text)
    container.name = self.parent.context.rptObj.ui.link(name)
    container.name.style.css.display = 'inline-block'
    container.name.style.css.color = self.parent.context.rptObj.theme.colors[-1]
    container.name.style.css.margin_left = 5
    container.add(container.name)
    container.style.css.text_align = align
    return container

  def carrousel(self, components, selected=0, width=('100', '%'), height=(None, 'px'), left="fas fa-chevron-left", right="fas fa-chevron-right", options=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param components:
    :param selected:
    :param width:
    :param height:
    :param left:
    :param right:
    :param options:
    """
    container = self.parent.context.rptObj.ui.div(width=width, height=height)
    container.left = self.parent.context.rptObj.ui.icons.awesome(left)
    container.left.icon.style.css.font_factor(0)
    container.left.icon.style.css.color = self.parent.context.rptObj.theme.colors[5]
    container.add(container.left)

    container.box = self.parent.context.rptObj.ui.div(width=(None, '%'), height=height)
    container.box.style.css.width = "calc(100% - 50px)"
    container.box.style.css.display = 'inline-block'
    for i, component in enumerate(components):
      if not hasattr(component, 'options'):
        component = self.parent.context.rptObj.ui.text(component, width=(100, '%'))
        component.style.css.text_align = "center"
        if i != selected:
          component.style.css.display = False
      container.box.add(component)
    container.add(container.box)

    container.right = self.parent.context.rptObj.ui.icons.awesome(right)
    container.right.icon.style.css.font_factor(0)
    container.right.icon.style.css.color = self.parent.context.rptObj.theme.colors[5]
    container.add(container.right)
    return container

  def flip(self, heads, tails, orientation='v', width=(300, 'px'), height=(200, 'px')):
    """
    Description:
    ------------

    filp = page.ui.studio.wedding.flip("Front Side", "Back Side", height=(100, "px"))
    filp.heads.style.css.color = 'red'

    https://www.w3schools.com/howto/howto_css_flip_box.asp

    Attributes:
    ----------
    :param heads:
    :param tails:
    :param orientation:
    :param width:
    :param height:
    """
    flip_box = self.parent.context.rptObj.ui.div(width=width, height=height)
    if orientation.lower() == 'v':
      flip_box.style.add_classes.div.rorate_vertical()
    else:
      flip_box.style.add_classes.div.rorate_horizontal()

    flip_box.style.css.background_color = "transparent"
    flip_box.style.css.border = "1px solid %s" % self.parent.context.rptObj.theme.colors[3]
    flip_box.style.css.perspective = 1000

    flip_box_inner = self.parent.context.rptObj.ui.div(height=(100, '%'))
    flip_box_inner.attr['class'].add('inner-flip')
    flip_box_inner.style.css.position = "relative"
    flip_box_inner.style.css.text_align = "center"
    flip_box_inner.style.css.transition = "transform 0.8s"
    flip_box_inner.style.css.transform_style = "preserve-3d"

    flip_box_front = self.parent.context.rptObj.ui.div(height=(100, '%'))
    flip_box_front.style.css.position = "absolute"
    flip_box_front.style.css.backface_visibility = "hidden"

    flip_box_back = self.parent.context.rptObj.ui.div(height=(100, '%'))
    flip_box_back.style.css.position = "absolute"
    flip_box_back.style.css.backface_visibility = "hidden"
    if orientation.lower() == 'v':
      flip_box_back.style.css.transform = "rotateX(180deg)"
    else:
      flip_box_back.style.css.transform = "rotateY(180deg)"

    if not hasattr(heads, 'options'):
      flip_box.heads = self.parent.context.rptObj.ui.text(heads, height=(100, '%'))
      flip_box.heads.style.css.vertical_align = "middle"
      flip_box.heads.style.css.margin_top = int(height[0] / 2) - 15
      flip_box_front.style.css.text_align = "center"
      flip_box_front.style.css.vertical_align = "middle"
      flip_box_front.add(flip_box.heads)

    if not hasattr(tails, 'options'):
      flip_box.tails = self.parent.context.rptObj.ui.text(tails, height=(100, '%'))
      flip_box.tails.style.css.vertical_align = "middle"
      flip_box.tails.style.css.margin_top = int(height[0] / 2) - 15
      flip_box_back.style.css.text_align = "center"
      flip_box_back.style.css.background = self.parent.context.rptObj.theme.colors[3]
      flip_box_back.style.css.vertical_align = "middle"
      flip_box_back.add(flip_box.tails)
    flip_box_inner.add(flip_box_front)
    flip_box_inner.add(flip_box_back)
    flip_box.add(flip_box_inner)
    return flip_box

  def phone(self, number, icon="fas fa-phone-alt", width=('auto', ''), height=(None, 'px')):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param number:
    :param icon:
    :param width:
    :param height:
    """
    container = self.parent.context.rptObj.ui.div(width=width, height=height)
    icon = self.parent.context.rptObj.ui.icons.awesome(icon)
    icon.icon.style.css.font_factor(0)
    icon.icon.style.css.color = self.parent.context.rptObj.theme.colors[5]
    container.add(icon)
    link = self.parent.context.rptObj.ui.link(number, "tel:+1-303-499-7111")
    link.style.css.color = self.parent.context.rptObj.theme.colors[5]
    container.add(link)
    return container


class Wedding(Event):

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

  def picture(self, image=None, label=None, path=None, width=(100, "%"), height=(None, "px"), align="center", htmlCode=None,
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
    component = self.parent.context.rptObj.ui.div(align=align, width=width, height=height, options=options,
                                                  profile=profile)
    component.image = html.HtmlImage.Image(self.parent.context.rptObj, image, path, align, htmlCode, (100, '%'), (100, '%'), profile, options or {})
    component.style.css.position = "relative"
    component.add(component.image)
    if not hasattr(label, 'options'):
      component.label = self.parent.context.rptObj.ui.div(label)
    else:
      component.label = self.parent.context.rptObj.ui.div()
      component.label.add(label)
    component.label.style.css.position = "absolute"
    component.label.style.css.text_align = "center"
    component.label.style.css.width = "calc(100% - 20px)"
    component.label.style.css.background = "white"
    component.label.style.css.opacity = 0.6
    component.label.style.css.margin = 10
    component.label.style.css.padding = 10
    component.label.style.css.bottom = 5
    component.add(component.label)
    return component

  def address(self, street, postcode, city, icon="fas fa-map-marker-alt", align="left", width=("auto", ''), height=(None, "px"), options=None, profile=None):
    component = self.parent.context.rptObj.ui.div(align=align, width=width, height=height, options=options,
                                                  profile=profile)
    icon = self.parent.context.rptObj.ui.icons.awesome(icon)
    icon.icon.style.css.font_factor(2)
    icon.icon.style.css.color = self.parent.context.rptObj.theme.colors[5]
    component.add(icon)
    return component

  def block(self, text, align="left", width=("80", '%'), height=(None, "px"), options=None, profile=None):
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
    options = options or {}
    component = self.parent.context.rptObj.ui.div(align=align, width=width, height=height, options=options, profile=profile)
    component.style.css.border = "1px solid %s" % self.parent.context.rptObj.theme.colors[-1]
    component.style.css.border_left = "3px solid %s" % self.parent.context.rptObj.theme.colors[-1]
    if not hasattr(text, 'options'):
      content = self.parent.context.rptObj.py.encode_html(text.strip())
      if options.get("initial-letter", False):
        content = '<span style="line-height:%spx;font-size:%spx;vertical-align:bottom">%s</span>%s' % (options.get("initial-letter"), options.get("initial-letter"), content[0], content[1:])
      component.text = self.parent.context.rptObj.ui.text(content)
      component.add(component.text)
    component.style.css.margin = "auto"
    component.style.css.padding = 10
    component.style.css.display = "block"
    return component

  def paragraph(self, text, align="left", width=("80", '%'), height=(None, "px"), options=None, profile=None):
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
    text = self.parent.context.rptObj.ui.text.paragraph(text, align=align, width=width, height=height, options=options, profile=profile)
    return text

  def table(self):
    pass


class Birthday(Event):
  pass


class Baptism(Event):
  pass


class Birth(Event):
  pass


class EVG(Event):
  pass

  def budget(self):
    pass


class Seminar(Event):
  pass

  def team(self):
    pass


class Festival(Event):
  pass


class Show(Event):

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
