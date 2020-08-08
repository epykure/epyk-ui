#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

from epyk.core import html
from epyk.core.css import Defaults_css
from epyk.core.css.themes import ThemeRed


class Event(object):

  def __init__(self, context):
    self.parent = context

  def certificate(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """

    https://uxwing.com/certificate-medal-quality-icon/

    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
      path="M46.18,0.01c2.17-0.09,3.88,0.66,5.61,1.76c2.19,1.39,4.66,4.14,7.71,5.88c4.29,2.45,12.23-0.93,16.29,5.11 c2.37,3.52,2.48,6.28,2.66,9.01c0.19,2.94,0.71,5.65,3.72,9.63c4.99,6.6,6.03,10.99,3.46,15.56c-1.75,3.12-5.44,4.85-6.29,6.83 c-1.82,4.2,0.19,7.37-2.29,12.27c-1.73,3.4-4.39,5.64-7.94,6.78c-2.99,0.96-5.99-0.43-8.39,0.58c-4.21,1.77-7.31,5.88-10.66,6.92 c-1.29,0.4-2.58,0.6-3.87,0.59c-1.29,0.01-2.58-0.19-3.87-0.59c-3.35-1.04-6.45-5.15-10.66-6.92c-2.4-1.01-5.4,0.39-8.39-0.58 c-3.55-1.14-6.21-3.38-7.94-6.78c-2.49-4.9-0.48-8.07-2.29-12.27c-0.85-1.98-4.54-3.71-6.29-6.83C4.16,42.39,5.2,38,10.19,31.41 c3.01-3.98,3.53-6.69,3.72-9.63c0.18-2.73,0.29-5.49,2.66-9.01c4.07-6.04,12.01-2.66,16.29-5.11c3.05-1.74,5.52-4.49,7.71-5.88 C42.29,0.67,44.01-0.09,46.18,0.01L46.18,0.01z M46.18,25.97l4.46,10.9l11.75,0.87l-8.99,7.61l2.8,11.44l-10.02-6.2l-10.02,6.2 l2.8-11.44l-8.99-7.61l11.75-0.87L46.18,25.97L46.18,25.97z M88.96,113.07L77.41,111l-5.73,10.26c-4.16,5.15-6.8-3.32-7.96-6.27 L52.57,93.96c2.57-0.89,5.67-3.46,8.85-6.35c6.35,0.13,12.27-0.97,16.62-6.51l12.81,24.75l1.11,2.38 C92.84,111.32,92.38,113.36,88.96,113.07L88.96,113.07z M3.39,113.07L14.95,111l5.73,10.26c4.16,5.15,6.8-3.32,7.96-6.27 l11.15-21.03c-2.57-0.89-5.67-3.46-8.85-6.35c-6.35,0.13-12.27-0.97-16.62-6.51L1.5,105.85l-1.11,2.38 C-0.49,111.32-0.03,113.36,3.39,113.07L3.39,113.07z M46.06,16.1c13.8,0,24.99,11.19,24.99,24.99c0,13.8-11.19,24.99-24.99,24.99 c-13.8,0-24.99-11.19-24.99-24.99C21.08,27.29,32.26,16.1,46.06,16.1L46.06,16.1z"
    )
    return svg

  def progress(self, percentage, icon="fas fa-plane", width=(100, '%'), height=("auto", ''), options=None, profile=None):
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
    icon.icon.style.css.color = self.parent.context.rptObj.theme.colors[-1]
    progress = self.parent.context.rptObj.ui.div()
    progress.style.css.border = "1px solid %s" % self.parent.context.rptObj.theme.colors[-1]
    progress.style.css.display = "inline-block"
    progress.style.css.width = "calc(100% - 50px)"
    inner = self.parent.context.rptObj.ui.div("%s%%" % percentage, width=(percentage, '%'))
    inner.style.css.background = self.parent.context.rptObj.theme.colors[4]
    inner.style.css.color = self.parent.context.rptObj.theme.greys[0]
    inner.style.css.text_align = "center"
    progress.add(inner)
    container = self.parent.context.rptObj.ui.div([progress, icon], width=width, height=height)
    container.style.css.padding = "0 5px"
    return container

  def search(self, text="", placeholder='search', icon="fas fa-search", width=(100, "%"), height=(None, "px"),
             htmlCode=None, options=None, attrs=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
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
    container = self.parent.context.rptObj.ui.div(width=width, height=height, options=options, profile=profile)
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

  def clients(self, logos, title="Client we have worked with...", content='', width=(100, '%'), height=("auto", ''), align="center", options=None,
               profile=False):
    """
    Description:
    ------------

    Attributes:
    ----------
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
    Description:
    ------------

    Attributes:
    ----------
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
    Description:
    ------------

    Attributes:
    ----------
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

  def comment(self, avatar, placeholder="Let a comment", width=(100, '%'), height=(None, 'px'), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
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
    container.text = self.parent.context.rptObj.ui.textarea(placeholder=placeholder)
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

  def carousel(self, components, selected=0, width=('100', '%'), height=(None, 'px'), left="fas fa-chevron-left", right="fas fa-chevron-right", options=None):
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
    flip_box.style.css.margin = "0 auto"
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
    button = self.parent.context.rptObj.ui.button(text, icon=icon, width=width, align=align, height=height, options=options, profile=profile)
    button.style.clear()
    button.style.css.padding = "0 10px"
    button.style.css.background = self.parent.context.rptObj.theme.greys[0]
    button.style.hover({"color": self.parent.context.rptObj.theme.colors[-1]})
    return button

  def sand_clock(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """
    Description:
    ------------

    Related Pages:

      https://uxwing.com/sand-clock-half-line-icon/

    Attributes:
    ----------
    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
      path="M2.921,110.266c-1.613,0-2.921-1.086-2.921-2.425s1.308-2.425,2.921-2.425h14.954c0.265-14.405,4.968-27.455,12.439-37.012 c4.651-5.95,10.374-10.556,16.779-13.321c-6.405-2.765-12.127-7.371-16.779-13.321C22.86,32.228,18.161,19.216,17.876,4.85H2.921 C1.308,4.85,0,3.764,0,2.425C0,1.086,1.308,0,2.921,0h117.036c1.615,0,2.922,1.086,2.922,2.425c0,1.339-1.307,2.425-2.922,2.425 h-15.535c-0.285,14.366-4.984,27.378-12.438,36.912c-4.652,5.95-10.375,10.556-16.779,13.321 c6.404,2.766,12.127,7.371,16.779,13.321c7.471,9.557,12.174,22.606,12.439,37.012h15.533c1.615,0,2.922,1.086,2.922,2.425 s-1.307,2.425-2.922,2.425H2.921L2.921,110.266z M28.647,82.577H93.65c-1.713-3.892-3.828-7.447-6.273-10.574 c-6.754-8.641-16.031-13.986-26.228-13.986s-19.474,5.346-26.229,13.986C32.475,75.13,30.36,78.686,28.647,82.577L28.647,82.577z M26.892,23.07h68.515c1.799-5.301,2.889-11.098,3.117-17.193H23.775C24.003,11.972,25.093,17.769,26.892,23.07L26.892,23.07z"
    )
    return svg

  def flag(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """
    Description:
    ------------

    Related Pages:

      https://uxwing.com/race-icon/

    Attributes:
    ----------
    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
      path="M0,4.16C0,1.86,1.86,0,4.16,0c2.3,0,4.16,1.86,4.16,4.16v6.34h94.62c1.72,0,3.12,1.4,3.12,3.12v66.8 c0,1.72-1.4,3.12-3.12,3.12H8.32v35.18c0,2.3-1.86,4.16-4.16,4.16c-2.3,0-4.16-1.86-4.16-4.16V4.16L0,4.16z M84.42,55.3h15.4V37.73 h-15.4V55.3L84.42,55.3z M82.06,77.3V57.66H64.94V77.3H82.06L82.06,77.3z M82.06,35.37V16.74H64.94v18.63H82.06L82.06,35.37z M43.1,77.3V57.66H25.97V77.3H43.1L43.1,77.3z M45.46,55.3h17.12V37.73H45.46V55.3L45.46,55.3z M43.1,35.37V16.74H25.97v18.63H43.1 L43.1,35.37z M23.62,55.3V37.73H8.43V55.3H23.62L23.62,55.3z"
    )
    return svg

  def animator(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """
    Description:
    ------------

    Related Pages:

      https://uxwing.com/volunteer-icon/

    Attributes:
    ----------
    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
      path="M37.07,40c-1.16,0.04-2.03,0.28-2.63,0.69c-0.34,0.23-0.59,0.52-0.75,0.87c-0.18,0.39-0.26,0.86-0.25,1.4 c0.05,1.59,0.88,3.66,2.48,6.05l0.02,0.03l5.22,8.3c2.09,3.33,4.28,6.72,7.01,9.21c2.62,2.4,5.8,4.02,10,4.03 c4.55,0.01,7.88-1.67,10.59-4.2c2.81-2.63,5.03-6.24,7.21-9.84l5.88-9.68c1.1-2.5,1.49-4.17,1.24-5.15 c-0.15-0.58-0.79-0.87-1.89-0.93c-0.23-0.01-0.47-0.01-0.72-0.01c-0.26,0.01-0.54,0.02-0.82,0.05c-0.16,0.01-0.31,0-0.45-0.03 c-0.52,0.03-1.06-0.01-1.61-0.09l2.01-8.91c-14.93,2.35-26.1-8.74-41.89-2.22l1.14,10.5C38.23,40.1,37.63,40.08,37.07,40L37.07,40 L37.07,40L37.07,40z M72.58,75.53c-0.92-1.24-1.83-2.58-2.66-3.8c-0.38-0.56-0.75-1.09-1.09-1.58c-2.85,2.09-6.27,3.39-10.65,3.38 c-4.71-0.01-8.34-1.69-11.34-4.23c-0.02,0.03-0.04,0.06-0.06,0.09c-0.49,0.68-1.04,1.48-1.63,2.34c-1.04,1.53-2.21,3.25-3.37,4.72 l-1.6-1.78c1.02-1.34,2.08-2.88,3.02-4.27c0.61-0.9,1.18-1.74,1.66-2.4c0.08-0.11,0.18-0.21,0.29-0.28 c-2.53-2.59-4.56-5.73-6.49-8.82l-5.22-8.29c-1.91-2.84-2.9-5.45-2.96-7.58c-0.03-1,0.14-1.92,0.51-2.71 c0.39-0.84,0.99-1.54,1.79-2.08c0.38-0.25,0.8-0.47,1.26-0.64c-0.34-4.5-0.46-10.17-0.25-14.91c0.11-1.13,0.33-2.25,0.64-3.38 c1.33-4.76,4.68-8.6,8.81-11.23c1.46-0.93,3.06-1.7,4.74-2.31c3-1.09,1.54-5.68,4.87-5.75c7.79-0.18,20.56,6.41,25.54,11.8 c2.9,3.13,4.71,7.29,5.11,12.79l-0.33,13.54v0c1.45,0.44,2.37,1.36,2.75,2.84c0.42,1.64-0.04,3.96-1.43,7.13l0,0 c-0.03,0.06-0.05,0.11-0.09,0.17l-5.94,9.79c-2.29,3.77-4.62,7.56-7.72,10.46l-0.13,0.12l0,0c0.37,0.53,0.78,1.13,1.21,1.76 c0.67,0.99,1.4,2.06,2.14,3.07L72.58,75.53L72.58,75.53z M45.19,80.25c5.11,2.76,14.83,4.73,23.82,0.45L58.84,95.46L45.19,80.25 L45.19,80.25z M77.41,75.98c7.57,3.72,21.48,4.96,27.15,8.12c2.08,1.16,3.96,2.64,5.48,4.64c3.77,4.98,4.1,22.13,5.46,28.24 c-0.33,3.56-2.35,5.61-6.32,5.91H66.16l6.52-4.13c2.31-1.46,2.37-2.65,0.92-4.85L63.2,98.05c0.11-0.14,0.22-0.28,0.33-0.43 L77.41,75.98L77.41,75.98z M58.14,122.88H6.32c-3.97-0.3-5.99-2.35-6.32-5.91c1.37-6.11,1.69-23.26,5.46-28.24 c1.51-2,3.39-3.48,5.48-4.64c5.12-2.86,16.95-4.14,24.78-7.1l18.43,20.63c0.14,0.22,0.29,0.42,0.43,0.62l-6.64,4.23 c-1.12,0.8-1.45,1.97-0.78,3.58L58.14,122.88L58.14,122.88z M56.4,100.14c1.59,1.17,3.19,1.06,4.78-0.09 c0.22-0.06,0.44-0.13,0.67-0.21c0.03,0.18,0.05,0.37,0.05,0.57c0,1.74-1.41,3.14-3.14,3.14c-1.73,0-3.14-1.41-3.14-3.14 c0-0.19,0.02-0.38,0.05-0.57C55.9,99.96,56.15,100.06,56.4,100.14L56.4,100.14z"
    )
    return svg


class Wedding(Event):

  def theme(self):
    """
    Description:
    ------------

    """
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
    component = self.parent.context.rptObj.ui.div(align=align, width=width, height=height, options=options, profile=profile)
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
    """
    Description:
    ------------

    Attributes:
    ----------
    :param street:
    :param postcode:
    :param city:
    :param icon:
    :param align:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    component = self.parent.context.rptObj.ui.div(align=align, width=width, height=height, options=options, profile=profile)
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

  def ring(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """
    Description:
    ------------

    Related Pages:

      https://uxwing.com/wedding-rings-icon/

    Attributes:
    ----------
    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
      path="M10.94,31.01c-0.05-0.25-0.03-0.51,0.05-0.74l3.48-11.06c0.16-0.53,0.6-0.9,1.1-1l18.7-5.39c0.5-0.14,1.01-0.01,1.37,0.31 l0,0l8.52,7.54c0.15,0.11,0.27,0.26,0.37,0.42c0.23,0.39,0.26,0.86,0.1,1.28l-4.76,13.26c6.32-0.29,12.49,1,18.02,3.61 c2.1-2.01,4.44-3.8,6.99-5.31c2.73-1.61,5.72-2.92,8.93-3.84c10.19-2.94,20.61-1.47,29.2,3.28c8.6,4.75,15.39,12.79,18.33,22.99 c2.94,10.19,1.47,20.61-3.28,29.2c-4.75,8.6-12.79,15.39-22.99,18.33c-9.32,2.69-18.82,1.69-26.95-2.13 c-2.11,2.02-4.46,3.81-7.02,5.32c-2.72,1.61-5.7,2.9-8.9,3.83c-10.19,2.94-20.61,1.47-29.2-3.28c-8.6-4.75-15.39-12.79-18.33-22.99 c-2.94-10.19-1.47-20.61,3.28-29.2c3.4-6.16,8.48-11.39,14.84-14.94l-11.31-8.6C11.19,31.68,11,31.35,10.94,31.01L10.94,31.01z M6.69,31.24l-0.16,0.05C6.13,29.94,5.29,28.92,4,28.2c-1.29-0.71-2.61-0.88-3.95-0.49L0,27.55c1.34-0.39,2.37-1.23,3.09-2.52 c0.71-1.3,0.88-2.61,0.49-3.95l0.16-0.05c0.39,1.34,1.23,2.37,2.52,3.09c1.29,0.71,2.61,0.88,3.95,0.49l0.05,0.16 c-1.34,0.39-2.37,1.23-3.09,2.52C6.46,28.58,6.3,29.9,6.69,31.24L6.69,31.24L6.69,31.24z M17.03,12l-0.16,0.05 c-0.39-1.34-1.23-2.37-2.52-3.09c-1.29-0.71-2.61-0.88-3.95-0.49l-0.05-0.16c1.34-0.39,2.37-1.23,3.09-2.52 c0.71-1.3,0.88-2.61,0.49-3.95l0.16-0.05c0.39,1.34,1.23,2.37,2.52,3.09s2.61,0.88,3.95,0.49l0.05,0.16 c-1.34,0.39-2.37,1.23-3.09,2.52C16.8,9.34,16.64,10.66,17.03,12L17.03,12L17.03,12z M40.83,10.22l-0.16,0.05 c-0.39-1.34-1.23-2.37-2.52-3.09c-1.29-0.71-2.61-0.88-3.95-0.49l-0.05-0.16c1.34-0.39,2.37-1.23,3.09-2.52 c0.71-1.3,0.88-2.61,0.49-3.95L37.89,0c0.39,1.34,1.23,2.37,2.52,3.09c1.29,0.71,2.61,0.88,3.95,0.49l0.05,0.16 c-1.34,0.39-2.37,1.23-3.09,2.52C40.61,7.55,40.45,8.87,40.83,10.22L40.83,10.22L40.83,10.22z M60.66,40.68 c2.31,1.32,4.48,2.88,6.48,4.66c1.26-1,2.61-1.91,4.05-2.69c1.74-0.95,3.61-1.72,5.6-2.29c7.36-2.12,14.88-1.06,21.09,2.37 c6.21,3.43,11.12,9.24,13.24,16.6c2.12,7.36,1.06,14.88-2.37,21.09c-3.43,6.21-9.24,11.12-16.6,13.24 c-3.08,0.89-6.19,1.22-9.22,1.05c-3.14-0.17-6.2-0.89-9.05-2.07c-1.79-0.74-3.5-1.67-5.09-2.75c-1.59-1.09-3.06-2.34-4.41-3.74 c-1.52-1.59-2.86-3.37-3.97-5.32c-1.08-1.88-1.95-3.93-2.59-6.14c-0.93-3.24-1.25-6.5-1.03-9.67c0.22-3.05,0.94-6.01,2.11-8.77 c-1.59-1.55-3.38-2.87-5.31-3.94c-0.37-0.21-0.75-0.4-1.14-0.59c-1.77,3.7-2.9,7.71-3.31,11.86c-0.42,4.34-0.05,8.82,1.23,13.26 c2.71,9.41,8.99,16.83,16.94,21.22c7.95,4.39,17.58,5.75,26.99,3.04c9.41-2.71,16.83-8.99,21.22-16.94 c4.39-7.95,5.75-17.58,3.04-26.99c-2.71-9.41-8.99-16.83-16.94-21.22c-7.95-4.39-17.58-5.75-26.99-3.04 c-2.94,0.85-5.7,2.05-8.24,3.55C64.32,37.68,62.4,39.1,60.66,40.68L60.66,40.68z M69.27,47.38c4.2,4.36,7.43,9.78,9.22,16 c1.39,4.82,1.79,9.68,1.33,14.38c-0.44,4.43-1.64,8.71-3.51,12.67c2.16,0.75,4.44,1.21,6.78,1.34c2.72,0.15,5.5-0.14,8.26-0.94 c6.58-1.9,11.76-6.28,14.83-11.84c3.07-5.56,4.02-12.29,2.13-18.88c-1.9-6.58-6.28-11.76-11.84-14.84 c-5.56-3.07-12.29-4.02-18.88-2.13c-1.77,0.51-3.44,1.2-5,2.05C71.41,45.85,70.3,46.58,69.27,47.38L69.27,47.38z M73.6,89.3 c1.76-3.69,2.9-7.69,3.3-11.83c0.43-4.35,0.05-8.85-1.23-13.3c-2.71-9.41-8.99-16.83-16.94-21.22c-7.07-3.9-15.46-5.41-23.84-3.8 c-1.04,0.23-2.05,0.48-3.05,0.77c-1.34,0.39-2.67,0.84-3.96,1.34c-7.58,3.16-13.59,8.75-17.36,15.58 c-4.39,7.95-5.75,17.58-3.04,26.99c2.71,9.41,8.99,16.83,16.94,21.22c7.95,4.39,17.58,5.75,26.99,3.04 c2.93-0.85,5.68-2.05,8.22-3.54c2.08-1.23,4.01-2.65,5.76-4.23c-2.31-1.32-4.48-2.88-6.48-4.66c-1.27,1.02-2.63,1.93-4.07,2.71 c-1.72,0.93-3.58,1.7-5.57,2.27c-7.36,2.12-14.88,1.06-21.09-2.37c-6.21-3.43-11.12-9.24-13.24-16.6l0-0.01 c-2.12-7.36-1.06-14.87,2.37-21.08c3.43-6.21,9.24-11.12,16.6-13.24l0.01,0c7.36-2.12,14.87-1.06,21.08,2.37 c6.21,3.43,11.12,9.24,13.24,16.6l0,0c0.94,3.25,1.25,6.53,1.02,9.7c-0.22,3.03-0.94,5.98-2.11,8.73c1.02,0.99,2.12,1.89,3.29,2.69 C71.45,88.15,72.51,88.77,73.6,89.3L73.6,89.3z M56.78,93.63c-4.2-4.36-7.43-9.78-9.22-16c-1.38-4.8-1.79-9.65-1.34-14.34 c0.43-4.45,1.64-8.74,3.51-12.71c-4.64-1.62-9.81-1.88-14.9-0.45c-0.08,0.03-0.17,0.06-0.26,0.08c-6.52,1.92-11.66,6.28-14.71,11.8 c-3.05,5.52-4.01,12.2-2.16,18.74c0.03,0.08,0.06,0.17,0.08,0.26c1.92,6.52,6.28,11.66,11.8,14.71c5.56,3.07,12.29,4.02,18.88,2.13 c1.74-0.5,3.41-1.19,4.98-2.04C54.63,95.17,55.74,94.44,56.78,93.63L56.78,93.63z M61.09,58.68c-0.75,2.09-1.22,4.29-1.38,6.54 c-0.2,2.85,0.08,5.77,0.91,8.66c0.56,1.94,1.35,3.78,2.33,5.48c0.6,1.05,1.28,2.05,2.01,2.98c0.74-2.08,1.21-4.26,1.37-6.5 c0.21-2.81-0.06-5.7-0.87-8.56c-0.03-0.08-0.06-0.17-0.08-0.26C64.47,63.89,62.99,61.09,61.09,58.68L61.09,58.68z M27.02,38.48 c1.27-0.52,2.58-0.98,3.93-1.37c1.03-0.3,2.05-0.55,3.08-0.75c0.89-0.2,1.78-0.38,2.68-0.53l4.24-11.81l-25.38,7.32l10.11,7.68 C26.11,38.83,26.56,38.65,27.02,38.48L27.02,38.48z M14.59,28.58l25.72-7.42l-6-5.31l-17.27,4.98L14.59,28.58L14.59,28.58z"
    )
    return svg

  def dress(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """
    Description:
    ------------

    Related Pages:

      https://uxwing.com/wedding-dress-icon/

    Attributes:
    ----------
    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
      path="M53.9,19.43c-0.29-0.02-0.56-0.09-0.8-0.21c-0.39-0.08-0.8-0.13-1.22-0.14c-2.72-0.11-5.97,1.14-8.99,4.4 c-0.07,0.08-0.15,0.15-0.23,0.22c-0.89,0.75-2.22,0.63-2.97-0.26c-2.59-3.1-5.59-4.32-8.24-4.26c-1.29,0.03-2.5,0.36-3.54,0.93 c-1,0.55-1.83,1.31-2.38,2.21c-0.83,1.37-1.04,3.11-0.28,4.98l1.45,3.57l2.64,6.49c4.26,8.43,1.34,11.18-3.23,15.5 c-0.86,0.81-1.8,1.7-2.74,2.7c-2.8,3-5.14,5.74-7.23,8.82c-2.1,3.1-3.99,6.59-5.91,11.13c-1.99,4.72-3.48,9.05-4.46,13.46 c-0.98,4.37-1.46,8.85-1.46,13.9c0,0.63-0.03,1.53-0.06,2.38c-0.11,3.35-0.19,5.63,3.79,7c1.03,0.36,2.12,0.48,3.24,0.45 c1.16-0.04,2.38-0.25,3.62-0.57c0.72-0.21,1.53-0.03,2.09,0.53c2.46,2.49,4.9,3.86,7.31,4.21c2.35,0.34,4.77-0.27,7.25-1.74 c0.76-0.49,1.79-0.45,2.51,0.17c2.49,2.13,4.88,3.27,7.17,3.36c2.22,0.08,4.48-0.85,6.77-2.85c0.62-0.57,1.55-0.74,2.35-0.34 c3.14,1.53,5.87,2.03,8.24,1.56c2.28-0.45,4.3-1.84,6.09-4.09c0.58-0.82,1.69-1.13,2.63-0.68c2.02,0.98,3.76,1.4,5.22,1.2 c1.3-0.18,2.44-0.9,3.41-2.21c2.21-2.99,1.97-8.54,1.76-13.25c-0.06-1.41-0.12-2.76-0.12-3.79C76.77,85.1,74,77.39,69.97,70.59 c-4.08-6.87-9.47-12.84-15.48-18.37l-0.02-0.02c-0.94-0.84-1.68-1.71-2.25-2.61c-0.59-0.93-1-1.87-1.26-2.83 c-0.37-1.41-0.41-2.81-0.2-4.21c0.19-1.31,0.58-2.61,1.09-3.89c0.02-0.04,0.03-0.08,0.05-0.12l3.64-8.03l1.7-3.74 c0.79-1.74,0.71-3.37,0.03-4.65c-0.45-0.85-1.16-1.57-2.05-2.09C54.81,19.78,54.37,19.58,53.9,19.43L53.9,19.43z M51.91,14.87V2.11 c0-1.17,0.95-2.11,2.11-2.11c1.17,0,2.11,0.95,2.11,2.11v13.67c0.42,0.18,0.82,0.38,1.2,0.61c1.57,0.92,2.83,2.21,3.65,3.75 c1.26,2.38,1.45,5.31,0.08,8.34l-1.7,3.74l-3.62,7.99c-0.39,1-0.69,1.98-0.82,2.92c-0.13,0.88-0.11,1.73,0.1,2.55 c0.14,0.54,0.38,1.08,0.73,1.63c0.37,0.58,0.87,1.16,1.53,1.75c0.02,0.02,0.04,0.04,0.06,0.06c6.28,5.78,11.93,12.05,16.25,19.32 c4.36,7.34,7.34,15.69,8.22,25.58c0.01,0.06,0.01,0.12,0.01,0.18h0.01c0,1.24,0.05,2.4,0.1,3.62c0.24,5.39,0.51,11.75-2.59,15.94 c-1.68,2.28-3.77,3.54-6.23,3.88c-1.88,0.26-3.92-0.06-6.11-0.92c-2.2,2.38-4.73,3.89-7.59,4.46c-2.93,0.58-6.14,0.16-9.65-1.33 c-2.81,2.16-5.7,3.15-8.67,3.04c-2.9-0.11-5.77-1.27-8.62-3.44c-2.92,1.48-5.85,2.05-8.78,1.62c-3.02-0.44-5.97-1.94-8.83-4.58 c-1.15,0.25-2.3,0.41-3.45,0.45c-1.6,0.05-3.18-0.14-4.74-0.68c-6.93-2.39-6.81-5.92-6.63-11.11c0.02-0.61,0.04-1.25,0.04-2.24 c0-5.32,0.52-10.1,1.58-14.81c1.04-4.68,2.61-9.24,4.69-14.18c2.03-4.8,4.05-8.53,6.3-11.86c2.26-3.34,4.71-6.22,7.63-9.33 c1.03-1.1,2.02-2.04,2.94-2.9c3.18-3,5.21-4.91,2.32-10.59c-0.04-0.07-0.07-0.15-0.1-0.22l-2.65-6.52l-1.45-3.57 c-1.31-3.22-0.91-6.3,0.59-8.76c0.94-1.54,2.3-2.82,3.94-3.72c0.43-0.24,0.88-0.44,1.34-0.63V2.11c0-1.17,0.95-2.11,2.11-2.11 c1.17,0,2.11,0.95,2.11,2.11v12.86c3.24-0.05,6.78,1.15,9.91,4.11C44.87,15.99,48.61,14.77,51.91,14.87L51.91,14.87z"
    )
    return svg

  def cake(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """
    Description:
    ------------

    Related Pages:

      https://uxwing.com/wedding-cake-icon/

    Attributes:
    ----------
    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
       path="M14.7,68.78h77.15c4.89,0,8.89,4,8.89,8.89v6.75c-3.37,2.8-6.49,4.3-9.33,4.37 c-3.54,0.09-6.93-2.19-10.13-7.13l0,0c-0.17-0.26-0.39-0.5-0.66-0.69c-1.18-0.86-2.82-0.6-3.68,0.58 c-3.23,4.43-6.55,6.89-9.96,7.08c-3.45,0.18-7.31-1.93-11.63-6.66c-0.06-0.06-0.11-0.12-0.18-0.18c-1.08-0.98-2.75-0.9-3.73,0.18 c-4.05,4.44-7.84,6.75-11.36,6.79c-3.44,0.04-6.9-2.13-10.4-6.63l0,0c-0.16-0.2-0.35-0.38-0.57-0.54 c-1.19-0.84-2.84-0.55-3.68,0.64c-2.58,3.65-5.58,5.82-8.81,6.41c-2.21,0.4-4.59,0.02-7.14-1.02c-5.25-2.15-3.34-3.38-3.69-9.93 C5.54,72.79,9.81,68.78,14.7,68.78L14.7,68.78z M72.51,9.04c-0.16,0.17-0.33,0.34-0.53,0.55l-0.55,0.57L70.86,9.6 c-0.17-0.16-0.34-0.33-0.5-0.5c-1.74-1.75-3.06-3.06-5.79-3.12c-0.11,0-0.22,0-0.34,0c-1.53,0.04-2.94,0.59-3.98,1.54 c-1.02,0.94-1.68,2.28-1.72,3.91c0,0.1,0,0.21,0,0.32c0.12,4.57,4.46,8.6,8.05,11.93c0.69,0.64,1.36,1.26,2,1.89l2.65,2.6l3.39-3.3 c0.55-0.53,1.16-1.11,1.82-1.73c1.12-1.06,2.37-2.23,3.53-3.41c0.83-0.85,1.63-1.7,2.3-2.52c0.66-0.8,1.2-1.57,1.56-2.25 c0.58-1.12,0.76-2.25,0.65-3.31c-0.11-1.04-0.51-2.02-1.12-2.85c-0.62-0.85-1.44-1.55-2.39-2.04c-1.09-0.56-2.34-0.83-3.63-0.69 C75.14,6.3,73.95,7.54,72.51,9.04L72.51,9.04L72.51,9.04z M41.36,5.03c1.23-2.04,2.26-3.72,4.89-4.61 c1.52-0.52,3.11-0.53,4.58-0.16c1.27,0.33,2.46,0.95,3.42,1.8c0.98,0.86,1.75,1.95,2.18,3.21c0.43,1.28,0.52,2.72,0.12,4.27 c-0.22,0.87-0.62,1.84-1.13,2.86c-0.5,1-1.11,2.04-1.76,3.09c-0.89,1.44-1.86,2.87-2.73,4.16c-0.51,0.75-0.98,1.46-1.38,2.07 l-3,4.61l-0.42,0.65l-0.65-0.4l-3.81-2.35c-0.7-0.43-1.5-0.89-2.33-1.38c-4.5-2.61-9.93-5.76-11.22-10.84 c-0.03-0.12-0.06-0.25-0.09-0.39c-0.42-2.06,0.04-3.93,1.06-5.41c1.02-1.46,2.6-2.53,4.45-3.01c0.13-0.03,0.26-0.06,0.4-0.09 C37.21,2.44,39.01,3.54,41.36,5.03L41.36,5.03L41.36,5.03z M0,115.14h106.49v7.74H0V115.14L0,115.14z M25,28.37h56.4 c3.58,0,6.5,2.93,6.5,6.5v4.94c-2.47,2.04-4.75,3.14-6.82,3.19c-2.59,0.07-5.06-1.6-7.4-5.21l0,0c-0.12-0.19-0.29-0.36-0.48-0.51 c-0.86-0.63-2.06-0.44-2.69,0.42c-2.36,3.24-4.79,5.04-7.28,5.17c-2.52,0.14-5.34-1.41-8.5-4.87c-0.04-0.04-0.08-0.09-0.13-0.13 c-0.79-0.72-2.01-0.66-2.73,0.13c-2.96,3.25-5.73,4.93-8.3,4.96c-2.51,0.03-5.05-1.56-7.6-4.85l0,0c-0.11-0.15-0.25-0.28-0.41-0.39 c-0.87-0.61-2.08-0.4-2.69,0.47c-1.88,2.67-4.08,4.26-6.44,4.68c-1.62,0.29-3.36,0.01-5.22-0.75c-3.84-1.57-2.44-2.47-2.7-7.26 C18.3,31.3,21.42,28.37,25,28.37L25,28.37z M87.9,44.57v0.21h-0.34C87.67,44.71,87.79,44.64,87.9,44.57L87.9,44.57z M86.39,45.43 v19.85H20.1V45.87c2.4,0.96,4.75,1.22,6.99,0.81c2.73-0.49,5.22-1.96,7.39-4.34c2.88,3.05,5.92,4.52,9.11,4.49 c3.24-0.04,6.47-1.64,9.7-4.75c3.49,3.34,6.86,4.83,10.13,4.65c3.09-0.17,5.93-1.8,8.56-4.73c2.76,3.37,5.83,4.93,9.19,4.85 C82.88,46.81,84.62,46.33,86.39,45.43L86.39,45.43z M100.75,90.93v0.29h-0.47C100.44,91.13,100.59,91.03,100.75,90.93L100.75,90.93 z M98.69,92.11v20.79H7.99V92.71c3.28,1.31,6.5,1.66,9.57,1.11c3.73-0.67,7.15-2.68,10.11-5.93c3.94,4.17,8.1,6.18,12.46,6.14 c4.43-0.05,8.86-2.25,13.27-6.49c4.77,4.58,9.38,6.6,13.85,6.37c4.23-0.23,8.12-2.46,11.71-6.47c3.77,4.62,7.98,6.75,12.58,6.63 C93.88,94,96.26,93.34,98.69,92.11L98.69,92.11z"
    )
    return svg

  def cocktail(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """
    https://uxwing.com/dice-game-icon/

    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
      path="M94.8,15.36c-1.18-0.34-1.86-1.56-1.53-2.74c0.34-1.18,1.56-1.86,2.74-1.53c3.15,0.9,5.79,2.39,7.82,4.59 c2.03,2.22,3.39,5.1,3.94,8.79c0.18,1.21-0.66,2.34-1.88,2.52c-1.21,0.18-2.34-0.66-2.52-1.88c-0.41-2.76-1.38-4.87-2.81-6.43 C99.13,17.12,97.17,16.04,94.8,15.36L94.8,15.36z M37.87,67.17L0.61,28.09c-0.84-0.89-0.81-2.29,0.08-3.13 c0.43-0.41,0.98-0.61,1.53-0.61v-0.01h14.53L2.27,9.86c-0.87-0.87-0.87-2.27,0-3.14c0.87-0.87,2.27-0.87,3.14,0l17.62,17.62h42.2 c0.46-6.48,3.24-12.31,7.52-16.64C77.44,2.94,83.92,0,91.08,0c7.16,0,13.64,2.94,18.34,7.7C114.1,12.45,117,19,117,26.23 c0,7.23-2.9,13.78-7.58,18.53c-4.7,4.76-11.18,7.7-18.34,7.7c-3.19,0-6.25-0.59-9.09-1.66c-2.33-0.88-4.51-2.1-6.48-3.6L56,67.18 v38.38l14.94,13.45c0.91,0.82,0.98,2.22,0.16,3.13c-0.44,0.49-1.04,0.73-1.65,0.73v0H24.77c-1.23,0-2.22-0.99-2.22-2.22 c0-0.7,0.32-1.32,0.82-1.73l14.5-13.36V67.17L37.87,67.17z M69.68,24.34h22.88c1.23,0,2.22,0.99,2.22,2.22 c0,0.66-0.29,1.26-0.75,1.67L78.64,44c1.5,1.08,3.15,1.98,4.92,2.65c2.33,0.88,4.87,1.37,7.52,1.37c5.93,0,11.3-2.43,15.18-6.36 c3.89-3.94,6.3-9.39,6.3-15.42c0-6.03-2.41-11.48-6.3-15.42c-3.88-3.93-9.25-6.36-15.18-6.36c-5.93,0-11.3,2.43-15.18,6.36 C72.42,14.33,70.13,19.06,69.68,24.34L69.68,24.34z M7.4,28.78l6.82,7.15c0.14-0.03,0.29-0.05,0.45-0.05h64.77 c0.28,0,0.54,0.05,0.79,0.14l7.08-7.25H7.4L7.4,28.78z M18.41,40.33l23.18,24.31c0.45,0.41,0.73,0.99,0.73,1.65v40.26h0 c0,0.6-0.24,1.2-0.72,1.63l-11.14,10.26h33.22l-11.29-10.16c-0.5-0.41-0.83-1.03-0.83-1.73V66.28h0.01c0-0.56,0.21-1.11,0.63-1.55 l23.83-24.41H18.41L18.41,40.33z"
    )
    return svg

  def table(self):
    pass


class Birthday(Event):

  def present(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """

    Related Pages:

      https://uxwing.com/present-icon/

    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
       path="M62.95,27.86c2.36-5.34,4.98-10.39,8.11-14.67c6.34-8.7,21.82-19.17,31.29-9.03 c8.48,9.07,1.29,18.98-8.81,23.7h22.85c1.77,0,3.43,0.74,4.57,1.92c1.18,1.18,1.92,2.8,1.92,4.57v12.31c0,1.77-0.74,3.43-1.92,4.57 c-1.07,1.07-2.47,1.77-4.05,1.88v60.08c0,1.92-0.77,3.69-2.06,4.94c-1.25,1.25-3.02,2.06-4.94,2.06H13.12 c-1.92,0-3.69-0.77-4.94-2.06c-1.25-1.25-2.06-3.02-2.06-4.94l0-60.04c-1.62-0.11-3.1-0.81-4.2-1.88C0.74,50.09,0,48.47,0,46.7 V34.39c0-1.77,0.74-3.43,1.92-4.57c1.18-1.18,2.8-1.92,4.57-1.92h23.26c-10.06-4.72-17.25-14.63-8.81-23.7 c9.47-10.17,24.95,0.33,31.29,9.03c3.13,4.31,5.75,9.36,8.11,14.67h2.54L62.95,27.86L62.95,27.86z M83.63,27.86 C106.74,17.62,99.07,0.37,84.44,8.7c-3.43,1.95-6.3,5.6-8.88,9.25c-2.43,3.43-4.61,7.04-6.23,9.91L83.63,27.86L83.63,27.86z M39.69,27.86C16.59,17.62,24.25,0.37,38.88,8.7c3.43,1.95,6.3,5.6,8.88,9.25c2.43,3.43,4.61,7.04,6.23,9.91L39.69,27.86 L39.69,27.86z M111.53,91.07H70.51v23.7h39.44c0.44,0,0.85-0.18,1.14-0.48c0.3-0.3,0.48-0.7,0.48-1.14V91.07H111.53L111.53,91.07z M53.11,91.07H11.5v22.08c0,0.44,0.18,0.85,0.48,1.14c0.3,0.3,0.7,0.48,1.14,0.48h39.99V91.07L53.11,91.07z M11.5,76.66h41.61 V50.57H11.5V76.66L11.5,76.66z M70.47,76.66h41.02V50.57H70.47V76.66L70.47,76.66z"
    )
    return svg

  def balloon(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """
    Related Pages:

      https://uxwing.com/party-balloon-icon/

    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
       path="M30.68,0c16.92,0,30.6,16.34,30.6,36.51c0,18.62-11.67,39.94-26.77,42.22l2.94,5.1 c1.85,3.21,0.81,4.09-2.36,4.09h-1.93c6.04,15.27,6.56,18.68,0.65,33.95c0,0.54-0.46,1-1,1h-2.97c-0.54,0-1-0.46-1-1 c5.99-15.27,5.32-18.68-0.65-33.95h-3.32c-2.4,0.04-2.24-2.28-1.24-3.9l3.28-5.29C11.74,76.52,0,55.17,0,36.51 C0,16.34,13.71,0,30.6,0H30.68L30.68,0z M36.19,12.16c-0.85-0.46-1.17-1.52-0.71-2.37c0.46-0.85,1.52-1.17,2.37-0.71 c2.93,1.58,5.86,3.92,8.42,6.57c2.64,2.73,4.89,5.8,6.32,8.7c0.43,0.87,0.07,1.91-0.79,2.34c-0.87,0.43-1.91,0.07-2.34-0.79 c-1.28-2.58-3.31-5.34-5.71-7.83C41.44,15.67,38.8,13.56,36.19,12.16L36.19,12.16z"
    )
    return svg

  def cake(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """
    Related Pages:

      https://uxwing.com/cake-icon/

    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
       path="M6.43,48.74h110.01c3.54,0,6.43,2.89,6.43,6.43v13.19c-0.33,0.12-0.63,0.3-0.89,0.53l0.89,1.03v0l-0.89-1.02 c-5.83,5.04-9.52,6.67-12.19,6.55c-2.34-0.11-4.36-1.9-6.49-3.79c-5.61-4.98-10.38-7.73-15.24-8.25c-4.87-0.53-9.5,1.17-14.75,5.08 c-0.22,0.11-0.42,0.25-0.61,0.41l0.08,0.09l0,0l-0.07-0.09l-0.32,0.28l-0.15,0.13c-0.03,0.02-0.07,0.05-0.1,0.08l0,0.01l0,0v0 c-0.06,0.04-0.29,0.24-0.69,0.56c-0.23,0.19-0.4,0.33-0.52,0.43c-0.04,0.03-0.07,0.05-0.11,0.08l0,0 c-2.16,1.72-4.01,2.94-5.62,3.73c-1.33,0.66-2.47,1.03-3.46,1.18c-0.99-0.15-2.12-0.52-3.45-1.18c-1.57-0.78-3.38-1.96-5.48-3.62 c-0.02-0.02-0.05-0.04-0.07-0.06l0,0l-0.07-0.05c-0.11-0.09-0.31-0.26-0.63-0.52c-0.23-0.19-0.4-0.33-0.52-0.42 c-0.03-0.03-0.07-0.06-0.1-0.09l0,0l-0.07-0.05v0c-0.04-0.03-0.11-0.1-0.25-0.21l-0.16-0.14c-0.03-0.03-0.07-0.07-0.1-0.1 c-0.2-0.18-0.42-0.34-0.66-0.46c-5.25-3.91-9.88-5.6-14.75-5.08c-4.86,0.52-9.63,3.27-15.24,8.25c-2.13,1.89-4.15,3.68-6.49,3.79 c-2.64,0.13-6.28-1.47-12.02-6.4c-0.04-0.04-0.07-0.07-0.11-0.11c-0.44-0.4-0.99-0.66-1.58-0.75V55.17 C0,51.63,2.9,48.74,6.43,48.74L6.43,48.74z M26.32,19.6h11.27v25.85H26.32V19.6L26.32,19.6z M94.4,3.14 c1.91,4.98-3.99,4.99-3.81,10.14c0.24,7.08,9.52,5.02,9.69-1.41c-0.2-2.12-1.93-2.71-1.01-4.97c-1.19,0.08-2.14,2.23-2.14,3.76 c0.15,1.97-3.37,1.67-1.77-0.73C96.74,7.86,96.06,4.29,94.4,3.14L94.4,3.14L94.4,3.14z M62.29,2.53c1.99,5.18-4.15,5.2-3.97,10.56 c0.26,7.37,9.92,5.22,10.09-1.47C68.2,9.41,66.4,8.8,67.37,6.45c-1.24,0.09-2.24,2.32-2.23,3.92c0.15,2.05-3.51,1.74-1.84-0.76 C64.73,7.45,64.02,3.73,62.29,2.53L62.29,2.53z M89.8,19.6h11.27v25.85H89.8V19.6L89.8,19.6z M57.74,19.6H69v25.85H57.74V19.6 L57.74,19.6z M30.7,0c2.32,6.05-4.85,6.07-4.63,12.32c0.3,8.6,11.57,6.1,11.78-1.71c-0.25-2.58-2.35-3.29-1.22-6.04 c-1.44,0.1-2.61,2.71-2.6,4.57c0.18,2.39-4.09,2.03-2.15-0.89C33.54,5.74,32.71,1.4,30.7,0L30.7,0z M51.36,69.39 C51.31,69.35,51.24,69.29,51.36,69.39L51.36,69.39L51.36,69.39z M72.15,69.39L72.15,69.39L72.15,69.39L72.15,69.39L72.15,69.39 L72.15,69.39L72.15,69.39z M122.87,83.81v23.16c0,3.54-2.9,6.43-6.43,6.43H6.43c-3.54,0-6.43-2.9-6.43-6.43V83.39 c6.06,4.03,10.83,5.32,14.93,4.98c5.73-0.48,9.58-3.9,13.65-7.51c3.47-3.08,5.93-4.74,8.04-4.97c1.9-0.2,3.97,0.82,6.81,3.09 l0.11,0.09l0,0l0,0c0.2,0.17-0.02-0.02,0.51,0.41l0.3,0.24c0.05,0.05,0.09,0.09,0.14,0.13l0,0c0.29,0.25,0.48,0.41,0.58,0.49 c0.19,0.17,0.41,0.35,0.6,0.52c2.24,1.99,4.41,3.91,6.93,5.34c2.68,1.52,5.63,2.43,9.16,2.17c3.54,0.26,6.48-0.64,9.16-2.17 c2.52-1.43,4.69-3.36,6.93-5.34c0.1-0.09,0.31-0.27,0.59-0.52c0.07-0.06,0.22-0.18,0.43-0.36c0.04-0.03,0.07-0.05,0.11-0.08l0,0 l0.04-0.04v0c0.08-0.06,0.23-0.19,0.45-0.36c0.18-0.15,0.27-0.23,0.32-0.27c0.05-0.03,0.09-0.07,0.14-0.1l0,0l0.05-0.04 c2.91-2.33,5-3.39,6.93-3.18c2.12,0.23,4.57,1.89,8.04,4.97c4.07,3.61,7.93,7.03,13.65,7.51C112.54,88.7,117.12,87.51,122.87,83.81 L122.87,83.81L122.87,83.81z"
    )
    return svg

  def hat(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """
    Description:
    ------------

    Related Pages:

      https://uxwing.com/party-hat-icon/

    Attributes:
    ----------
    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
       path="M64.39,58.6c6.44,6.44,11.29,13.3,13.92,19.19c2.82,6.3,3.11,11.65,0.21,14.55c-1.36,1.36-3.27,2.02-5.56,2.04 l-50.83,22.65l0,0c-12.88,6.37-19.22,7.33-21.39,3.91c-2.05-3.23,0.38-10.08,4.8-19.81l0,0l23.11-52.06 c0.18-1.87,0.82-3.43,1.99-4.6c2.9-2.9,8.25-2.61,14.55,0.21C51.09,47.31,57.95,52.15,64.39,58.6L64.39,58.6z M115.85,88.94 c1.52,1.52,1.52,3.99,0,5.51c-1.52,1.52-3.99,1.52-5.51,0c-1.52-1.52-1.52-3.99,0-5.51C111.86,87.42,114.32,87.42,115.85,88.94 L115.85,88.94z M119.55,70.78c1.08-0.2,2.12,0.51,2.32,1.59c0.2,1.08-0.51,2.12-1.59,2.32c-5.29,1-9.74-2.24-14.34-5.58 c-6.05-4.4-12.4-9.02-20.43-0.77c-0.76,0.79-2.02,0.8-2.81,0.04c-0.79-0.76-0.8-2.02-0.04-2.81c10.43-10.72,18.21-5.07,25.61,0.32 C112.17,68.72,115.94,71.46,119.55,70.78L119.55,70.78z M120.46,11.45c1.1,0,1.98,0.89,1.98,1.98c0,1.1-0.89,1.98-1.98,1.98 c-9.14,0.02-11.54,7.38-14.08,15.16c-2.95,9.05-6.07,18.59-18.45,20.71c-1.15,0.2-2.33,0.39-3.63,0.57 c-1.24,0.17-2.47,0.31-3.71,0.39c-1.1,0.07-2.04-0.76-2.11-1.86c-0.07-1.1,0.76-2.04,1.86-2.11c1.16-0.08,2.3-0.2,3.43-0.36 c1.08-0.15,2.27-0.34,3.49-0.55c10.01-1.71,12.75-10.08,15.33-18.01C105.6,20.16,108.43,11.48,120.46,11.45L120.46,11.45z M50.24,1.62c0.2-1.08,1.24-1.79,2.32-1.59c1.08,0.2,1.79,1.24,1.59,2.32c-0.65,3.43,1.73,7.09,4.18,10.85 c5.09,7.83,10.44,16.04-3.03,26.7c-0.86,0.68-2.11,0.53-2.79-0.33c-0.68-0.86-0.53-2.11,0.33-2.79c10.63-8.41,6.3-15.08,2.16-21.43 C52.1,10.92,49.29,6.61,50.24,1.62L50.24,1.62z M95.42,7.52l-3.8,7.5l5.61,5.67l-7.95-1.08l-3.83,7.1l-1.26-7.9l-7.93-1.4 l7.12-3.69l-1.16-8.25l5.76,5.91L95.42,7.52L95.42,7.52z M77.44,31.86c1.52,1.52,1.52,3.99,0,5.51c-1.52,1.52-3.99,1.52-5.51,0 c-1.52-1.52-1.52-3.99,0-5.51C73.45,30.34,75.92,30.34,77.44,31.86L77.44,31.86z M71.75,5.19c1.52,1.52,1.52,3.99,0,5.51 c-1.52,1.52-3.99,1.52-5.51,0c-1.52-1.52-1.52-3.99,0-5.51C67.76,3.67,70.23,3.67,71.75,5.19L71.75,5.19z M46.59,24.48 c1.52,1.52,1.52,3.99,0,5.51c-1.52,1.52-3.99,1.52-5.51,0c-1.52-1.52-1.52-3.99,0-5.51C42.6,22.96,45.06,22.96,46.59,24.48 L46.59,24.48z M113.62,46.71c1.52,1.52,1.52,3.99,0,5.51c-1.52,1.52-3.99,1.52-5.51,0c-1.52-1.52-1.52-3.99,0-5.51 C109.63,45.19,112.1,45.19,113.62,46.71L113.62,46.71z M101.38,76.61l-4.73,3.09l1.36,5.18l-4.26-3.3l-4.61,2.84l1.92-5.02 l-4.14-3.48l5.38,0.24l2.1-5.19l1.36,5.37L101.38,76.61L101.38,76.61z M32.36,62.05c3.96,11.62,12.69,26.63,25.21,35.93L67.6,93.5 c-1.17-0.36-2.38-0.82-3.64-1.38c-5.89-2.63-12.75-7.48-19.19-13.92l0,0C39.41,72.84,35.15,67.19,32.36,62.05L32.36,62.05z M43.11,104.42C32.39,95,26.02,84.73,20.72,74.26l-6.65,14.99c2.56,5.32,9.58,14.3,16.29,20.85L43.11,104.42L43.11,104.42z M16.99,116.18c-5-4.31-7.29-6.94-9.76-11.56c-3.38,7.61-5.2,12.82-3.99,14.72C4.3,121,8.42,120.16,16.99,116.18L16.99,116.18z M31.6,49.33c0.01,0.07,0.01,0.15,0,0.23c-0.1,1.49,0.18,3.26,0.82,5.24c0.31,0.95,0.7,1.96,1.17,3.01 c2.48,5.56,7.12,12.09,13.31,18.29l0,0c6.19,6.19,12.73,10.83,18.29,13.31c1.19,0.53,2.33,0.97,3.4,1.29 c1.47,0.44,2.82,0.69,4.02,0.71c0.09,0,0.18,0.01,0.27,0.02c1.5-0.01,2.71-0.4,3.52-1.21c1.93-1.93,1.48-6.08-0.82-11.22 c-2.48-5.56-7.12-12.09-13.31-18.29c-6.19-6.19-12.73-10.83-18.29-13.31c-5.14-2.3-9.29-2.75-11.22-0.82 C32.1,47.25,31.72,48.18,31.6,49.33L31.6,49.33z"
    )
    return svg


class Baptism(Event):

  def angel(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """
    Related Pages:

      https://uxwing.com/angel-icon/

    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
       path="M47.72,43.84c0.81,0.76,0.85,2.03,0.09,2.84c-0.76,0.81-2.03,0.85-2.84,0.09c-2.95-2.77-6.03-4.32-8.95-4.78 c-2.97-0.46-5.8,0.21-8.12,1.88c-4.82,3.47-6.17,10.67-7.32,16.82l-0.38,2.01l-0.41,2.12c-2.48,12.81-5.16,26.64-14.06,33.13 l0.03,0.01c2.23,1,4.8,1.03,7.37,0.22c2.71-0.86,5.4-2.63,7.72-5.19c1.64-1.81,3.09-4.01,4.24-6.55c0.45-1.01,1.64-1.47,2.65-1.01 c1.01,0.45,1.47,1.64,1.01,2.65c-1.32,2.94-3.01,5.49-4.93,7.61c-2.82,3.11-6.13,5.28-9.48,6.34c-3.49,1.1-7.05,1.03-10.21-0.39 c-1.19-0.53-2.32-1.26-3.36-2.19c-0.23-0.18-0.43-0.42-0.57-0.71c-0.48-1-0.06-2.2,0.94-2.68c9.39-4.56,12.16-18.85,14.71-31.99 l0.41-2.14c0.19-0.98,0.29-1.48,0.38-1.98c1.29-6.87,2.8-14.92,8.93-19.33c3.18-2.29,7.03-3.22,11.07-2.59 C40.33,38.6,44.16,40.49,47.72,43.84L47.72,43.84z M61.32,68.31c1.38-1.44,2.35-2.69,4.48-2.93c4-0.46,7.68,3.64,5.66,7.67 c-0.58,1.15-1.75,2.51-3.04,3.86c-1.42,1.47-2.99,2.91-4.1,4.01l-3.01,2.98l-2.48-2.39c-2.99-2.88-7.86-6.5-8.02-10.98 c-0.11-3.14,2.37-5.16,5.22-5.12C58.59,65.43,59.66,66.7,61.32,68.31L61.32,68.31L61.32,68.31z M61.44,14.32 c4.1,0,7.82,1.66,10.51,4.35c2.69,2.69,4.35,6.4,4.35,10.51c0,4.1-1.66,7.82-4.35,10.5c-2.69,2.69-6.4,4.35-10.51,4.35 s-7.82-1.66-10.51-4.35c-2.69-2.69-4.35-6.4-4.35-10.5c0-4.1,1.66-7.82,4.35-10.51C53.62,15.99,57.34,14.32,61.44,14.32 L61.44,14.32z M69.1,21.52c-1.96-1.96-4.67-3.17-7.66-3.17c-2.99,0-5.7,1.21-7.66,3.17c-1.96,1.96-3.17,4.67-3.17,7.66 c0,2.99,1.21,5.7,3.17,7.66c1.96,1.96,4.67,3.17,7.66,3.17c2.99,0,5.7-1.21,7.66-3.17c1.96-1.96,3.17-4.67,3.17-7.66 C72.27,26.19,71.06,23.48,69.1,21.52L69.1,21.52z M45.4,55.34c2.68-4.1,6.06-6.8,9.67-8.24c2.76-1.1,5.64-1.46,8.43-1.15 c2.79,0.31,5.51,1.3,7.94,2.89c3.4,2.22,6.25,5.62,8.01,10.03c2.94,7.38,2.91,14.15,2.88,20.88c-0.02,5.66-0.05,11.29,1.85,17.03 c0.71,2.16,1.63,4.15,2.76,5.96c1.13,1.81,2.46,3.45,4,4.92c0.72,0.69,0.82,1.79,0.27,2.59c-1.1,1.73-2.59,3.24-4.38,4.54 c-5.94,4.34-15.33,6.37-24.76,6.33c-9.39-0.05-18.93-2.16-25.2-6.12c-2.13-1.34-3.91-2.91-5.21-4.71c-0.65-0.89-0.45-2.15,0.44-2.8 l0.08-0.06l0-0.01c2.06-1.35,3.72-3.16,5.01-5.37c1.34-2.28,2.32-5.01,2.99-8.13c0.97-4.54,0.94-9.66,0.92-14.76 C41.05,70.61,41.01,62.07,45.4,55.34L45.4,55.34z M56.55,50.83c-2.87,1.14-5.59,3.34-7.79,6.7c-3.74,5.73-3.7,13.67-3.66,21.63 c0.03,5.34,0.06,10.69-1,15.61c-0.75,3.52-1.88,6.64-3.46,9.32c-1.22,2.07-2.69,3.86-4.44,5.34c0.8,0.78,1.74,1.5,2.8,2.17 c5.64,3.56,14.38,5.46,23.08,5.51c8.66,0.04,17.17-1.75,22.39-5.56c0.94-0.68,1.76-1.43,2.45-2.24c-1.28-1.37-2.41-2.86-3.4-4.45 c-1.3-2.09-2.36-4.37-3.17-6.83c-2.09-6.32-2.06-12.29-2.04-18.3c0.03-6.34,0.06-12.72-2.6-19.38c-1.43-3.6-3.74-6.36-6.47-8.14 c-1.91-1.25-4.03-2.02-6.2-2.26C60.9,49.7,58.67,49.98,56.55,50.83L56.55,50.83z M43.11,15.54c0.6,0.93,0.34,2.17-0.59,2.77 c-0.93,0.6-2.17,0.34-2.77-0.59c-0.47-0.72-0.83-1.47-1.07-2.25c-0.25-0.79-0.38-1.59-0.38-2.4c0-3.86,2.78-7.25,7.27-9.6 C49.67,1.33,55.29,0,61.44,0c6.15,0,11.77,1.33,15.87,3.48c4.49,2.35,7.27,5.74,7.27,9.6c0,0.39-0.03,0.78-0.09,1.18l-0.01,0.07 c-0.06,0.37-0.14,0.73-0.25,1.08c-0.32,1.06-1.44,1.67-2.51,1.34c-1.06-0.32-1.67-1.44-1.34-2.51c0.06-0.18,0.1-0.36,0.13-0.53 l0.01-0.06c0.03-0.19,0.04-0.38,0.04-0.58c0-2.25-1.95-4.39-5.11-6.04c-3.55-1.86-8.5-3-14.02-3s-10.47,1.15-14.02,3 c-3.15,1.65-5.11,3.8-5.11,6.04c0,0.41,0.06,0.82,0.19,1.21C42.64,14.71,42.84,15.13,43.11,15.54L43.11,15.54z M87.21,93.96 c-0.39-1.04,0.13-2.2,1.16-2.59c1.04-0.39,2.2,0.13,2.59,1.16c0.77,2.01,1.92,3.61,3.43,4.83c1.56,1.25,3.52,2.13,5.86,2.65 c1.08,0.24,1.76,1.31,1.52,2.39c-0.24,1.08-1.31,1.76-2.39,1.52c-2.96-0.66-5.48-1.8-7.51-3.44C89.8,98.81,88.24,96.65,87.21,93.96 L87.21,93.96z M33.01,92.53c0.39-1.04,1.56-1.56,2.59-1.16c1.04,0.4,1.56,1.56,1.16,2.59c-1.03,2.69-2.59,4.86-4.67,6.53 c-2.04,1.64-4.55,2.78-7.51,3.44c-1.08,0.24-2.15-0.44-2.39-1.52c-0.24-1.08,0.44-2.15,1.52-2.39c2.34-0.52,4.31-1.4,5.86-2.65 C31.09,96.14,32.24,94.54,33.01,92.53L33.01,92.53z M77.91,46.76c-0.81,0.76-2.08,0.72-2.84-0.09c-0.76-0.81-0.72-2.08,0.09-2.84 c3.56-3.35,7.39-5.24,11.08-5.82c4.04-0.63,7.89,0.3,11.07,2.59c6.13,4.41,7.64,12.46,8.93,19.33c0.09,0.49,0.19,1,0.38,1.98 l0.41,2.14c2.55,13.14,5.32,27.43,14.71,31.99c1,0.48,1.42,1.68,0.94,2.68c-0.14,0.28-0.33,0.52-0.57,0.71 c-1.04,0.93-2.17,1.65-3.36,2.19c-3.16,1.42-6.72,1.49-10.21,0.39c-3.36-1.06-6.67-3.23-9.48-6.34c-1.92-2.12-3.61-4.67-4.93-7.61 c-0.45-1.01,0-2.2,1.01-2.65c1.01-0.45,2.2,0,2.65,1.01c1.14,2.55,2.6,4.75,4.24,6.56c2.32,2.56,5.01,4.33,7.72,5.19 c2.57,0.81,5.14,0.78,7.37-0.22l0.03-0.01c-8.89-6.5-11.57-20.32-14.06-33.13l-0.41-2.12l-0.38-2.01 c-1.15-6.15-2.5-13.35-7.32-16.82c-2.32-1.67-5.14-2.34-8.12-1.88C83.94,42.44,80.86,43.99,77.91,46.76L77.91,46.76z"
    )
    return svg

  def church(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """
    Related Pages:

      https://uxwing.com/church-icon/

    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
       path="M88.41,122.88h31.63V26.36l-15.65-9.86l-15.98,9.43v15.22v10.85L62.58,32.96V13.69h7.77 c1.42,0,2.56-1.15,2.56-2.56s-1.15-2.56-2.56-2.56h-7.77v-6c0-1.42-1.15-2.56-2.56-2.56c-1.42,0-2.56,1.15-2.56,2.56v6h-7.49 c-1.42,0-2.56,1.15-2.56,2.56s1.15,2.56,2.56,2.56h7.49v19.29L31.63,52.2V26.36L15.98,16.5L0,25.93v15.22v81.73h31.63v-0.02h56.78 V122.88L88.41,122.88z M59.99,49.42c1.32,0,2.51,0.53,3.37,1.4c0.86,0.86,1.4,2.05,1.4,3.37c0,1.32-0.53,2.51-1.4,3.37 c-0.86,0.86-2.05,1.4-3.37,1.4s-2.51-0.53-3.37-1.4c-0.86-0.86-1.4-2.05-1.4-3.37c0-1.32,0.53-2.51,1.4-3.37 C57.48,49.96,58.67,49.42,59.99,49.42L59.99,49.42z M59.99,45.17c2.49,0,4.74,1.01,6.38,2.64c1.63,1.63,2.64,3.89,2.64,6.38 s-1.01,4.74-2.64,6.38c-1.63,1.63-3.89,2.64-6.38,2.64c-2.49,0-4.74-1.01-6.38-2.64c-1.63-1.63-2.64-3.89-2.64-6.38 s1.01-4.74,2.64-6.38C55.24,46.18,57.5,45.17,59.99,45.17L59.99,45.17z M60.05,69.82L60.05,69.82c8.68,0,15.79,7.11,15.79,15.79 v30.94H44.26V85.61C44.26,76.92,51.36,69.82,60.05,69.82L60.05,69.82z"
    )
    return svg


class Birth(Event):

  def day(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """
    Related Pages:

      https://uxwing.com/date-of-birth-icon/

    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
       path="M81.53,4.71c0-2.62,2.58-4.71,5.77-4.71c3.2,0,5.77,2.13,5.77,4.71V25.4c0,2.62-2.58,4.71-5.77,4.71 c-3.2,0-5.77-2.13-5.77-4.71V4.71L81.53,4.71z M46.21,85.9h10.78V73.6c0-0.95,0.78-1.72,1.72-1.72h5.41c0.95,0,1.72,0.78,1.72,1.72 v12.3h10.78c4.64,0,8.44,3.8,8.44,8.45v8.54h4.69c1.49,0,2.71,1.21,2.71,2.71c0,1.49-1.21,2.71-2.71,2.71H33.07 c-1.49,0-2.71-1.21-2.71-2.71c0-1.49,1.21-2.71,2.71-2.71h4.69v-8.54C37.77,89.7,41.57,85.9,46.21,85.9L46.21,85.9z M61.42,58.26 c0.93,4.14,3.74,6.21,3.74,8.29c0,2.07-0.93,4.14-3.74,4.14c-2.8,0-3.74-2.07-3.74-4.14C57.68,64.48,60.48,62.41,61.42,58.26 L61.42,58.26z M29.53,4.71C29.53,2.09,32.11,0,35.3,0c3.2,0,5.77,2.13,5.77,4.71V25.4c0,2.62-2.58,4.71-5.77,4.71 c-3.2,0-5.77-2.13-5.77-4.71V4.71L29.53,4.71z M7.56,44.09h107.62V22.66c0-0.8-0.31-1.55-0.84-2.04c-0.53-0.53-1.24-0.84-2.04-0.84 h-9.31c-1.78,0-3.2-2.63-3.2-4.41c0-1.78,1.42-3.2,3.2-3.2h10.52c2.58,0,4.88,1.07,6.57,2.75c1.69,1.69,2.75,4.04,2.75,6.57v92.06 c0,2.58-1.07,4.88-2.75,6.57c-1.69,1.69-4.04,2.75-6.57,2.75H9.33c-2.58,0-4.88-1.07-6.57-2.75C1.07,118.44,0,116.08,0,113.55 V21.49c0-2.58,1.07-4.88,2.75-6.57c1.69-1.69,4.04-2.75,6.57-2.75h11.28c1.78,0,3.2,1.42,3.2,3.2c0,1.78-1.42,4.41-3.2,4.41H10.54 c-0.8,0-1.55,0.31-2.09,0.84c-0.53,0.53-0.84,1.24-0.84,2.09v21.43L7.56,44.09L7.56,44.09L7.56,44.09z M115.18,52.9H7.56v59.39 c0,0.8,0.31,1.55,0.84,2.09c0.53,0.53,1.24,0.84,2.09,0.84l101.76,0c0.8,0,1.55-0.31,2.09-0.84c0.53-0.53,0.84-1.24,0.84-2.09V52.9 L115.18,52.9z M50.36,19.73c-1.78,0-3.2-2.63-3.2-4.41c0-1.78,1.42-3.2,3.2-3.2h21.49c1.78,0,3.2,1.42,3.2,3.2 c0,1.78-1.42,4.41-3.2,4.41H50.36L50.36,19.73z"
    )
    return svg

  def baby(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """

    Related Pages:

      https://uxwing.com/embryo-pregnancy-icon/

    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
       path="M18.04,75.16c0.16-0.4,0.33-0.81,0.51-1.22c0.42-0.94,0.87-1.85,1.36-2.72c0.67-1.21,1.4-2.38,2.16-3.49 c0.84-1.23,1.74-2.41,2.64-3.52c0.51-0.63,1.22-0.99,1.97-1.06c0.74-0.08,1.51,0.13,2.14,0.64c0.63,0.51,0.99,1.22,1.06,1.97 c0.08,0.74-0.13,1.51-0.64,2.14c-0.82,1.01-1.62,2.06-2.35,3.12c-0.66,0.97-1.3,1.98-1.89,3.04c-0.49,0.88-0.93,1.77-1.31,2.67 c-0.32,0.77-0.6,1.54-0.83,2.32l0,0.06c-0.01,0.14-0.02,0.25-0.04,0.35l-0.01,0.04c-0.92,6.79-0.94,12.59-0.11,17.44 c0.82,4.77,2.46,8.61,4.9,11.58c2.41,2.93,5.65,5.07,9.69,6.47c4.11,1.42,9.05,2.09,14.78,2.06l0.07-0.01 c3.53-0.3,6.87-0.77,10.02-1.41c3.19-0.65,6.21-1.48,9.07-2.48c2.81-0.99,5.48-2.15,8.01-3.5c2.52-1.34,4.88-2.85,7.07-4.52 c2.94-2.25,5.92-5.02,8.59-8.13c2.42-2.81,4.58-5.9,6.26-9.15c1.46-2.82,2.53-5.74,3.07-8.68c0.48-2.65,0.52-5.33-0.01-7.97 l-0.03-0.22l-0.28-1.38c-0.57-2.83-0.97-4.81-1.15-6.27c-0.21-1.67-0.17-2.85,0.16-3.98c0.48-1.64,1.32-2.55,2.71-4.05l0.06-0.07 c1.12-1.21,2.7-2.93,4.77-5.92c0.78-1.13,1.5-2.26,2.15-3.39l0.06-0.1c0.61-1.06,1.15-2.12,1.61-3.17 c0.47-1.04,0.86-2.08,1.18-3.12c0.32-1.02,0.56-2.03,0.73-3.02c0.63-3.74,0.55-7.25-0.09-10.47c-0.69-3.41-2.02-6.51-3.85-9.18 c-0.94-1.37-2-2.63-3.17-3.77c-1.18-1.15-2.47-2.17-3.85-3.06c-1.38-0.89-2.84-1.63-4.36-2.22c-1.51-0.58-3.08-1.02-4.7-1.29 c-3.06-0.52-6.28-0.44-9.51,0.31c-3.05,0.71-6.1,2.03-9.04,4.03c-1.49,1.02-2.77,2.13-3.85,3.35c-1.06,1.2-1.94,2.48-2.66,3.87 l-0.07,0.14c-0.74,1.45-1.32,3.03-1.79,4.75c-0.47,1.76-0.82,3.66-1.05,5.71c-0.28,2.43-0.5,4.85-0.57,7.2 c-0.07,2.36,0,4.69,0.29,6.95c0.16,1.25,0.39,2.51,0.71,3.77c0.29,1.16,0.66,2.3,1.11,3.41l0.1,0.15l0,0 c0.09,0.14,0.17,0.29,0.24,0.44c0.02,0.05,0.04,0.1,0.05,0.15c0.04,0.11,0.07,0.21,0.1,0.31l0.04,0.17c0.31,0.66,0.64,1.29,1,1.9 c0.39,0.67,0.84,1.34,1.33,2.02c0.48,0.65,0.96,1.19,1.44,1.62c0.46,0.41,0.92,0.71,1.38,0.92c0.41,0.19,0.82,0.3,1.25,0.34 c0.45,0.04,0.92,0.01,1.41-0.1c0.79-0.17,1.57-0.01,2.2,0.39c0.63,0.4,1.11,1.04,1.28,1.83c0.16,0.74,0.03,1.47-0.32,2.08l0,0 c-0.34,0.59-0.88,1.06-1.56,1.3l-0.08,0.03c-2.12,0.69-4.14,1.42-6.05,2.2c-1.9,0.78-3.74,1.63-5.5,2.56 c-1.72,0.91-3.32,1.87-4.8,2.91c-1.46,1.02-2.82,2.13-4.06,3.31l0,0c-0.04,0.04-0.09,0.08-0.13,0.12 c-0.56,0.49-1.27,0.73-1.97,0.71c-0.74-0.01-1.48-0.31-2.03-0.87l0,0c-0.04-0.04-0.08-0.09-0.12-0.13 c-0.49-0.56-0.73-1.27-0.71-1.97l0-0.02c0.02-0.74,0.32-1.48,0.89-2.03c1.45-1.39,3.04-2.68,4.76-3.89c1.71-1.2,3.53-2.3,5.45-3.31 c1.11-0.59,2.26-1.15,3.42-1.68c0.39-0.18,0.79-0.36,1.2-0.53l-0.04-0.04c-0.7-0.65-1.38-1.42-2.02-2.29 c-0.5-0.68-0.97-1.38-1.41-2.09c-0.18-0.3-0.36-0.6-0.53-0.91c-1.45,0.66-2.86,1.34-4.24,2.05c-1.76,0.9-3.49,1.86-5.21,2.9 c-1.83,1.11-3.6,2.31-5.33,3.61c-1.62,1.22-3.18,2.53-4.67,3.94c-0.42,1.37-0.91,2.73-1.43,4.05c-0.58,1.47-1.17,2.81-1.73,4.04 c-1.78,3.95-2.41,6.72-2.19,8.61c0.17,1.48,0.96,2.33,2.14,2.74c1.74,0.61,4.18,0.62,6.92,0.28c2.87-0.35,6.01-1.07,9.01-1.89 c0.71-0.19,1.44-0.41,2.19-0.65c0.74-0.24,1.45-0.49,2.15-0.75c0.71-0.27,1.4-0.55,2.08-0.84c0.66-0.28,1.34-0.6,2.06-0.96 c0.72-0.36,1.52-0.39,2.23-0.15c0.71,0.24,1.32,0.75,1.68,1.47c0.36,0.72,0.39,1.52,0.15,2.23c-0.24,0.71-0.75,1.32-1.47,1.68 c-0.79,0.39-1.56,0.75-2.31,1.07c-0.73,0.31-1.52,0.63-2.38,0.95c-0.8,0.3-1.59,0.58-2.38,0.83c-0.79,0.25-1.61,0.5-2.46,0.73 c-3.37,0.92-6.92,1.73-10.21,2.09c-3.42,0.38-6.61,0.29-9.17-0.6c-3.07-1.07-5.24-3.08-5.94-6.43c-0.64-3.07,0.05-7.24,2.58-12.83 c0.95-2.1,1.96-4.44,2.71-6.78c0.75-2.31,1.27-4.65,1.27-6.82c0.01-1.91-0.41-3.73-1.49-5.3c-1.1-1.6-2.91-2.99-5.68-4.02 c-0.78-0.29-1.62-0.43-2.53-0.43c-0.94,0-1.96,0.17-3.07,0.48c-1.22,0.35-2.5,0.88-3.84,1.58c-1.33,0.69-2.74,1.57-4.22,2.62 l-3.41,5.73c-0.41,0.69-1.06,1.15-1.79,1.34c-0.72,0.19-1.52,0.1-2.21-0.31c-0.69-0.41-1.15-1.06-1.34-1.79 c-0.19-0.72-0.1-1.52,0.31-2.21l2.17-3.66l-0.19-0.05c-0.49-0.13-0.97-0.22-1.44-0.27c-0.45-0.05-0.9-0.05-1.36-0.02 c-1.09,0.09-2.02,0.35-2.8,0.73c-0.79,0.39-1.43,0.94-1.93,1.58c-0.41,0.53-0.72,1.14-0.95,1.81c-0.24,0.7-0.37,1.47-0.41,2.28 c-0.04,0.86,0.04,1.77,0.23,2.7c0.19,0.92,0.5,1.86,0.92,2.8c0.89,1.97,2.28,3.89,4.18,5.55c1.74,1.52,3.9,2.82,6.5,3.74 L18.04,75.16L18.04,75.16z M63.62,50.21c-0.29-0.87-0.53-1.76-0.75-2.65c-0.32-1.33-0.56-2.68-0.73-4.03 c-0.33-2.58-0.41-5.19-0.34-7.79c0.07-2.62,0.3-5.2,0.59-7.75c0.27-2.36,0.68-4.57,1.24-6.63c0.57-2.08,1.3-4.03,2.25-5.87 l0.01-0.02c0.95-1.85,2.11-3.57,3.51-5.14c1.4-1.58,3.04-3.01,4.94-4.31c3.57-2.43,7.3-4.04,11.04-4.91 c3.98-0.92,7.95-1.01,11.75-0.37c2,0.34,3.96,0.88,5.84,1.61c1.9,0.74,3.71,1.66,5.41,2.75c1.7,1.09,3.3,2.36,4.77,3.79 c1.45,1.41,2.76,2.97,3.92,4.66c2.24,3.29,3.89,7.09,4.74,11.27c0.8,3.92,0.9,8.16,0.14,12.64c-0.21,1.25-0.51,2.5-0.91,3.77 l-0.02,0.07c-0.39,1.23-0.86,2.47-1.42,3.73c-0.57,1.27-1.21,2.53-1.93,3.78c-0.71,1.24-1.52,2.52-2.43,3.82 c-2.37,3.42-4.11,5.3-5.33,6.62l-0.06,0.07c-0.44,0.48-0.8,0.86-1.02,1.15c-0.18,0.22-0.29,0.4-0.33,0.53 c-0.1,0.35-0.08,0.96,0.08,2.01c0.19,1.29,0.53,3,1.02,5.45l0.28,1.39l0.02,0.06c0.01,0.05,0.02,0.1,0.03,0.16l0,0 c0.67,3.35,0.63,6.71,0.04,10.02c-0.64,3.58-1.92,7.1-3.65,10.45c-1.88,3.65-4.31,7.11-6.99,10.25c-2.96,3.45-6.25,6.52-9.5,9 c-2.44,1.86-5.06,3.54-7.85,5.03c-2.78,1.48-5.73,2.77-8.85,3.86c-3.1,1.09-6.37,1.98-9.81,2.69c-3.45,0.7-7.03,1.21-10.76,1.53 c-0.08,0.01-0.16,0.01-0.23,0l-0.01,0c-6.6,0.06-12.34-0.74-17.19-2.46c-4.95-1.76-8.98-4.47-12.04-8.2 c-2.96-3.6-4.97-8.09-6.01-13.54c-0.97-5.07-1.09-10.98-0.33-17.75l0,0l-0.11-0.05l-0.37-0.14l-0.53-0.19 c-3.36-1.2-6.18-2.9-8.46-4.91c-2.53-2.22-4.4-4.82-5.6-7.5c-0.6-1.33-1.04-2.69-1.32-4.05c-0.28-1.38-0.4-2.76-0.34-4.08 c0.06-1.39,0.3-2.73,0.73-3.97c0.43-1.24,1.03-2.4,1.82-3.43c1-1.31,2.29-2.41,3.85-3.21c1.46-0.75,3.14-1.23,5.03-1.39 c0.79-0.06,1.59-0.05,2.4,0.03c0.78,0.08,1.57,0.23,2.36,0.44l0.01,0c0.63,0.16,1.23,0.36,1.81,0.57l0.12,0.05 c0.31,0.12,0.61,0.24,0.9,0.36c1.41-0.94,2.77-1.74,4.09-2.4c1.56-0.79,3.07-1.39,4.51-1.81l0.12-0.03 c1.62-0.46,3.17-0.68,4.66-0.67c1.56,0.01,3.05,0.28,4.46,0.8c4.12,1.54,6.86,3.7,8.58,6.26c1.57,2.34,2.27,4.96,2.38,7.71 c0.36-0.27,0.72-0.54,1.09-0.8c-0.11-8.34-1.66-13.19-4-16.28c-2.36-3.12-5.7-4.57-9.19-6.09c-4.42-1.93-9.06-3.95-13.02-8.69 c-3.91-4.68-7.04-11.93-8.41-24.22c-0.09-0.8,0.16-1.56,0.63-2.15c0.47-0.58,1.16-0.99,1.96-1.08c0.8-0.09,1.56,0.16,2.15,0.63 c0.58,0.47,0.99,1.16,1.08,1.96c1.2,10.8,3.83,17.05,7.09,20.99c3.2,3.87,7.12,5.58,10.86,7.21c4.17,1.82,8.15,3.55,11.26,7.38 c2.8,3.45,4.77,8.49,5.31,16.65c1.43-0.84,2.9-1.64,4.41-2.41C60.53,51.66,62.06,50.93,63.62,50.21L63.62,50.21z"
    )
    return svg

  def boy(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """
    Related Pages:

      https://uxwing.com/baby-icon/

    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
       path="M43.52,0c9.46,0,17.13,7.67,17.13,17.13c0,9.46-7.67,17.13-17.13,17.13c-9.46,0-17.13-7.67-17.13-17.13 C26.39,7.67,34.06,0,43.52,0L43.52,0z M25.36,77.83l13.61,13.79l-10.03,10.03l8.04,8.25l2.74,2.81c4.69,6.2-2.34,13.56-8.45,8.45 l-17.84-18.21c-2.7-3.74-3.5-7.8-0.74-12.45L25.36,77.83L25.36,77.83z M61.67,77.83L48.07,91.63l10.03,10.03l-8.04,8.25l-2.74,2.81 c-4.69,6.2,2.34,13.56,8.45,8.45l17.84-18.21c2.7-3.74,3.5-7.8,0.74-12.45L61.67,77.83L61.67,77.83z M84.26,73.29L84.26,73.29 c-2.79,2.01-6.35,1.08-8.72-1.41L61.87,57.55v13.04H25.13v-13L11.5,71.88c-2.37,2.49-5.94,3.42-8.72,1.41l0,0 c-2.79-2.01-3.87-6.33-1.41-8.72l17.95-17.44c2.92-2.84,8.54-9.56,12.33-9.56H55.7c3.55,0,9.05,6.67,12.01,9.56l17.95,17.44 C88.13,66.96,87.04,71.28,84.26,73.29L84.26,73.29z"
    )
    return svg

  def girl(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """
    Related Pages:

      https://uxwing.com/child-girl-icon/

    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
       path="M52.5,0c9.94,0,18.3,6.73,20.68,15.83c7.62,2.3,16.15,8.81,13.55,15.15c-3.5,8.54-10.81,4.6-11.56-4.35 c-0.22-2.62-0.53-4.58-1.4-7.34c0.05,0.61,0.08,1.22,0.08,1.84c0,11.67-9.56,21.14-21.36,21.14s-21.36-9.46-21.36-21.14 c0-0.32,0.01-0.64,0.02-0.96c-0.83,2.66-1.13,4.6-1.34,7.15c-0.74,8.94-8.05,12.89-11.55,4.35c-2.58-6.29,5.8-12.75,13.37-15.1 C33.75,7.1,42.29,0,52.5,0L52.5,0z M80.87,69.5l10.46,7.94c8.01,6.08,18.76-4.67,10.75-10.75L74.64,45.88l-0.03-0.13h-44.2l0,0.02 l-0.02-0.02L2.82,66.79c-7.99,6.1,2.76,16.85,10.75,10.75l10.59-8.08l-7.52,28.5H32.7v17.33c0,4.18,3.42,7.6,7.6,7.6 c4.18,0,7.6-3.42,7.6-7.6V97.96h9.21v17.33c0,4.18,3.42,7.6,7.6,7.6h0c4.18,0,7.6-3.42,7.6-7.6V97.96h16.06L80.87,69.5L80.87,69.5z"
    )
    return svg


class EVG(Event):

  def budget(self):
    pass

  def cocktail(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """
    https://uxwing.com/dice-game-icon/

    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
      path="M94.8,15.36c-1.18-0.34-1.86-1.56-1.53-2.74c0.34-1.18,1.56-1.86,2.74-1.53c3.15,0.9,5.79,2.39,7.82,4.59 c2.03,2.22,3.39,5.1,3.94,8.79c0.18,1.21-0.66,2.34-1.88,2.52c-1.21,0.18-2.34-0.66-2.52-1.88c-0.41-2.76-1.38-4.87-2.81-6.43 C99.13,17.12,97.17,16.04,94.8,15.36L94.8,15.36z M37.87,67.17L0.61,28.09c-0.84-0.89-0.81-2.29,0.08-3.13 c0.43-0.41,0.98-0.61,1.53-0.61v-0.01h14.53L2.27,9.86c-0.87-0.87-0.87-2.27,0-3.14c0.87-0.87,2.27-0.87,3.14,0l17.62,17.62h42.2 c0.46-6.48,3.24-12.31,7.52-16.64C77.44,2.94,83.92,0,91.08,0c7.16,0,13.64,2.94,18.34,7.7C114.1,12.45,117,19,117,26.23 c0,7.23-2.9,13.78-7.58,18.53c-4.7,4.76-11.18,7.7-18.34,7.7c-3.19,0-6.25-0.59-9.09-1.66c-2.33-0.88-4.51-2.1-6.48-3.6L56,67.18 v38.38l14.94,13.45c0.91,0.82,0.98,2.22,0.16,3.13c-0.44,0.49-1.04,0.73-1.65,0.73v0H24.77c-1.23,0-2.22-0.99-2.22-2.22 c0-0.7,0.32-1.32,0.82-1.73l14.5-13.36V67.17L37.87,67.17z M69.68,24.34h22.88c1.23,0,2.22,0.99,2.22,2.22 c0,0.66-0.29,1.26-0.75,1.67L78.64,44c1.5,1.08,3.15,1.98,4.92,2.65c2.33,0.88,4.87,1.37,7.52,1.37c5.93,0,11.3-2.43,15.18-6.36 c3.89-3.94,6.3-9.39,6.3-15.42c0-6.03-2.41-11.48-6.3-15.42c-3.88-3.93-9.25-6.36-15.18-6.36c-5.93,0-11.3,2.43-15.18,6.36 C72.42,14.33,70.13,19.06,69.68,24.34L69.68,24.34z M7.4,28.78l6.82,7.15c0.14-0.03,0.29-0.05,0.45-0.05h64.77 c0.28,0,0.54,0.05,0.79,0.14l7.08-7.25H7.4L7.4,28.78z M18.41,40.33l23.18,24.31c0.45,0.41,0.73,0.99,0.73,1.65v40.26h0 c0,0.6-0.24,1.2-0.72,1.63l-11.14,10.26h33.22l-11.29-10.16c-0.5-0.41-0.83-1.03-0.83-1.73V66.28h0.01c0-0.56,0.21-1.11,0.63-1.55 l23.83-24.41H18.41L18.41,40.33z"
    )
    return svg

  def champagne(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """
    https://uxwing.com/champagne-bottles-icon/

    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
      path="M61.18,29.02C61.18,29.06,61.18,29.06,61.18,29.02L61.18,29.02L61.18,29.02z M50.81,31.42 C50.81,31.45,50.81,31.45,50.81,31.42L50.81,31.42L50.81,31.42z M84.08,76.04c6.38-1.7,12.91,2.07,14.61,8.45 c1.7,6.38-2.07,12.91-8.45,14.61c-6.38,1.7-12.91-2.07-14.6-8.45C73.94,84.27,77.7,77.74,84.08,76.04L84.08,76.04z M27.87,78.44 c-6.38-1.7-12.91,2.07-14.61,8.45c-1.7,6.38,2.07,12.91,8.45,14.6c6.38,1.7,12.91-2.07,14.6-8.45 C38.02,86.67,34.25,80.14,27.87,78.44L27.87,78.44z M26.69,82.87l-3.39,4.46l-5.53-1.03l3.21,4.61l-2.69,4.94l5.38-1.62l3.84,4.09 l0.11-5.61l5.09-2.4l-5.31-1.84l-0.7-5.57L26.69,82.87L26.69,82.87z M42.77,43.15l-10.73-0.66l2.91-7.01l0.11-1.11l-0.41-2.18 l1.03-3.84l0.15,0.04l10.84,2.91l-1,3.69l-1.66,1.51l-0.66,1.25L42.77,43.15L42.77,43.15L42.77,43.15z M44.91,73.31l-29.39-7.89 c1-1.88,2.43-3.54,3.95-4.83c1.84-1.59,3.84-2.66,5.46-3.06l0.96-0.26l0.37-0.92l3.61-8.7l12.32,0.74l-1.4,12.58l-0.11,1l0.77,0.7 c1.25,1.14,2.03,2.8,2.54,4.68c0.48,1.84,0.74,3.87,0.92,5.94L44.91,73.31L44.91,73.31z M14.12,70.59l29.58,7.93l-7.89,29.47 l-29.58-7.93L14.12,70.59L14.12,70.59z M4.82,105.22l29.58,7.93l-0.59,2.25c-0.59,1.59-1.29,2.69-2.14,3.21 c-0.7,0.44-1.66,0.41-2.91-0.11l-0.26-0.11l-21.61-5.79c-1.25-0.33-2.07-0.85-2.47-1.62c-0.44-0.81-0.48-1.95-0.18-3.43l0.63-2.32 L4.82,105.22L4.82,105.22z M27.28,43.48c-0.15,0.26-0.29,0.55-0.37,0.85l-4.02,9.66c-1.92,0.66-4.09,1.92-6.05,3.58 c-1.99,1.7-3.84,3.87-5.09,6.38l-0.15,0.37L0.32,106.47l-0.04,0.11c-0.52,2.47-0.33,4.57,0.55,6.27c0.96,1.77,2.58,2.95,4.98,3.58 l21.5,5.75c2.47,1.03,4.61,0.89,6.38-0.22c1.7-1.03,2.95-2.88,3.84-5.35l0.04-0.15l11.25-42.01l0.04-0.7 c-0.22-2.51-0.48-5.05-1.11-7.45c-0.59-2.21-1.51-4.2-2.99-5.83l2.4-21.58l1.55-1.4l0.59-0.96l1.29-4.76 c0.18-0.66,0.15-0.52,0.11-0.44c0.33-1.18,0.48-1.7-0.18-2.62c-0.52-0.77-1.03-0.89-1.95-1.07l-0.74-0.18l-11.1-2.99 c-0.44-0.11-0.7-0.22-0.92-0.3c-0.81-0.26-1.29-0.44-2.1-0.15c-1.25,0.44-1.44,1.11-1.84,2.69l-1.29,4.79l-0.04,0.88l0.37,2.03 l-3.73,8.93L27.28,43.48L27.28,43.48z M34.88,27.99c-0.04,0,0,0,0.18-0.07C35.36,27.8,35.1,27.91,34.88,27.99L34.88,27.99z M77.37,16.22c-0.85,1.18-2.54,1.44-3.73,0.59c-1.18-0.85-1.44-2.54-0.59-3.73l4.5-6.23c0.85-1.18,2.54-1.44,3.73-0.59 c1.18,0.85,1.44,2.54,0.59,3.73L77.37,16.22L77.37,16.22z M41.92,14.01c1.22,0.81,1.59,2.43,0.77,3.69 c-0.81,1.22-2.43,1.59-3.69,0.77l-6.45-4.2c-1.22-0.81-1.59-2.43-0.77-3.69c0.81-1.22,2.43-1.59,3.69-0.77L41.92,14.01L41.92,14.01 L41.92,14.01z M53.51,9.51c0.37,1.44-0.52,2.88-1.95,3.21c-1.44,0.37-2.88-0.52-3.21-1.95L46.5,3.31 c-0.37-1.44,0.52-2.88,1.95-3.21c1.44-0.37,2.88,0.52,3.21,1.95L53.51,9.51L53.51,9.51z M66.93,10.76 c-0.29,1.44-1.73,2.36-3.17,2.03c-1.44-0.29-2.36-1.73-2.03-3.17l1.66-7.52c0.3-1.44,1.73-2.36,3.17-2.03 C68,0.36,68.92,1.8,68.59,3.24L66.93,10.76L66.93,10.76z M69.14,40.78l10.73-0.66l-2.91-7.01l-0.11-1.11l0.41-2.18L76.22,26 l-0.15,0.04l-10.84,2.91l1,3.69l1.66,1.51l0.66,1.25L69.14,40.78L69.14,40.78L69.14,40.78z M67,70.95l29.39-7.89 c-1-1.88-2.43-3.54-3.95-4.83c-1.84-1.59-3.84-2.66-5.46-3.06l-0.96-0.26l-0.37-0.92l-3.61-8.7l-12.32,0.74l1.4,12.58l0.11,1 l-0.77,0.7c-1.25,1.14-2.03,2.8-2.54,4.68c-0.48,1.84-0.74,3.87-0.92,5.94L67,70.95L67,70.95z M97.8,68.22l-29.58,7.93l7.89,29.47 l29.58-7.93L97.8,68.22L97.8,68.22z M107.09,102.86l-29.58,7.93l0.59,2.25c0.59,1.59,1.29,2.69,2.14,3.21 c0.7,0.44,1.66,0.41,2.91-0.11l0.26-0.11l21.61-5.79c1.25-0.33,2.07-0.85,2.47-1.62c0.44-0.81,0.48-1.95,0.18-3.43l-0.63-2.32 L107.09,102.86L107.09,102.86z M84.63,41.12c0.15,0.26,0.29,0.55,0.37,0.85l4.02,9.66c1.92,0.66,4.09,1.92,6.05,3.58 c1.99,1.7,3.84,3.87,5.09,6.38l0.15,0.37l11.29,42.16l0.04,0.11c0.52,2.47,0.33,4.57-0.55,6.27c-0.96,1.77-2.58,2.95-4.98,3.58 l-21.5,5.75c-2.47,1.03-4.61,0.88-6.38-0.22c-1.7-1.03-2.95-2.88-3.84-5.35l-0.04-0.15L63.1,72.1l-0.04-0.7 c0.22-2.51,0.48-5.05,1.11-7.45c0.59-2.21,1.51-4.2,2.99-5.83l-2.4-21.58l-1.55-1.4l-0.59-0.96l-1.29-4.76 c-0.18-0.66-0.15-0.52-0.11-0.44c-0.33-1.18-0.48-1.7,0.18-2.62c0.52-0.77,1.03-0.88,1.95-1.07l0.74-0.18l11.1-2.99 c0.44-0.11,0.7-0.22,0.92-0.3c0.81-0.26,1.29-0.44,2.1-0.15c1.25,0.44,1.44,1.11,1.84,2.69l1.29,4.79l0.04,0.88l-0.37,2.03 l3.73,8.93L84.63,41.12L84.63,41.12z M77.04,25.63c0.04,0,0,0-0.18-0.07C76.56,25.44,76.81,25.55,77.04,25.63L77.04,25.63z M85.26,80.51l3.39,4.46l5.53-1.03l-3.21,4.61l2.69,4.94l-5.38-1.62l-3.84,4.09l-0.11-5.61l-5.09-2.4l5.31-1.84l0.7-5.57 L85.26,80.51L85.26,80.51z"
    )
    return svg

  def dice(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """
    https://uxwing.com/dice-game-icon/

    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
      path="M6.41,23.43l49.53,20.15c1.57,0.64,4.17,1.04,5.74,0.4l52.42-21.41c1.57-0.64-0.02-3.49-1.62-4.05L59.62,0 c-0.4-0.14-10.33,3.48-11.72,3.97L4.79,19.38C3.12,19.97,4.26,22.55,6.41,23.43L6.41,23.43z M116.87,94.34l-51.73,28.06 c-1.49,0.81-3.56,0.69-3.56-1.01l-0.01-66.03c0-1.7,0.14-3.36,1.7-4.03l51.92-22.12c1.56-0.66,3.73-0.07,3.72,1.62l-0.34,59.48 C118.56,92,118.36,93.53,116.87,94.34L116.87,94.34z M104.99,71.09c3.52,1.5,4.55,6.77,2.28,11.78c-2.26,5-6.96,7.84-10.48,6.34 c-3.52-1.5-4.55-6.77-2.28-11.78C96.78,72.43,101.47,69.59,104.99,71.09L104.99,71.09z M86.22,57.28c3.65,1.55,4.7,7.01,2.36,12.19 c-2.34,5.18-7.2,8.12-10.85,6.57c-3.65-1.55-4.7-7.01-2.36-12.19C77.71,58.66,82.57,55.72,86.22,57.28L86.22,57.28z M1.81,93.89 l51.26,27.75c1.49,0.81,3.56,0.69,3.56-1.01l0.01-65.42c0-1.7-0.14-3.36-1.7-4.03L3.72,29.22C2.16,28.55,0,29.15,0,30.85 l0.11,59.02C0.11,91.56,0.32,93.08,1.81,93.89L1.81,93.89z M6.91,75.74c3.21-2.04,7.99,0.29,10.66,5.2s2.24,10.56-0.97,12.6 c-3.21,2.04-7.99-0.29-10.66-5.2C3.27,83.42,3.7,77.78,6.91,75.74L6.91,75.74z M22.06,64.37c3.4-2.06,8.45,0.29,11.28,5.26 c2.83,4.97,2.38,10.67-1.02,12.73c-3.4,2.06-8.45-0.29-11.28-5.26C18.2,72.14,18.66,66.44,22.06,64.37L22.06,64.37z M38.12,52.37 c3.42-2.07,8.51,0.29,11.36,5.26c2.85,4.97,2.39,10.68-1.03,12.74c-3.42,2.07-8.51-0.29-11.36-5.26 C34.24,60.14,34.7,54.44,38.12,52.37L38.12,52.37z M59.16,15.48c6.04,0,10.93,2.34,10.93,5.22c0,2.88-4.89,5.22-10.93,5.22 c-6.03,0-10.93-2.34-10.93-5.22C48.23,17.82,53.13,15.48,59.16,15.48L59.16,15.48z"
    )
    return svg

  def purse(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """
    https://uxwing.com/saving-icon/

    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
      path="M76.59,59.19h27.74c3.76,0,6.84,3.08,6.84,6.84v28.04c0,3.76-3.08,6.84-6.84,6.84H76.59 c-11.47,0-20.86-9.39-20.86-20.86v0C55.73,68.58,65.11,59.19,76.59,59.19L76.59,59.19z M10.98,26.25h17.7 c-0.03-0.5-0.05-1-0.05-1.51C28.64,11.08,39.71,0,53.38,0c13.66,0,24.74,11.08,24.74,24.74c0,0.5-0.02,1-0.04,1.5l6.51-0.01 c6.65-0.01,12.09,5.2,12.09,11.85v1.98c3.28,2.17,5.45,5.89,5.45,10.09v4.36h-7.68v-2.91c0-3.13-2.56-5.68-5.68-5.68H18.12v-6.33 c0-0.84,0.69-1.53,1.53-1.53h12.88c-0.85-1.32-1.57-2.73-2.16-4.21H12.69c-2.2,0-3.99,1.8-3.99,3.99v72.64 c0,2.2,1.8,3.99,3.99,3.99h77.71c2.2,0,3.99-1.8,3.99-3.99v-4.57h7.88v7.55h-0.02c-0.03,5.22-5.6,9.43-11.1,9.43H10.95 C4.93,122.88,0,117.95,0,111.93v-74.7C0,31.19,4.94,26.25,10.98,26.25L10.98,26.25z M76.39,33.84c-0.59,1.48-1.31,2.89-2.16,4.21 h15.8c0.44,0,0.87,0.02,1.3,0.07v-0.29c0-2.2-1.8-3.99-3.99-3.99H76.39L76.39,33.84z M55.03,38.06v-2.32 c1.27-0.05,2.35-0.22,3.23-0.5c0.88-0.29,1.71-0.74,2.5-1.37c0.78-0.64,1.42-1.42,1.93-2.37c0.5-0.94,0.75-1.98,0.75-3.11 c0-1.93-0.7-3.52-2.1-4.78c-1.06-0.93-3.16-1.82-6.31-2.66v-4.5c0.54,0.29,0.92,0.57,1.16,0.85c0.23,0.28,0.49,0.79,0.79,1.52 l5.8-0.91c-0.37-1.66-1.18-2.96-2.4-3.91c-1.23-0.96-3.01-1.5-5.34-1.65v-1.53h-2.26v1.53c-2.55,0.13-4.47,0.82-5.77,2.07 c-1.29,1.24-1.94,2.78-1.94,4.63c0,1.35,0.32,2.49,0.97,3.43s1.4,1.62,2.28,2.05c0.88,0.42,2.36,0.93,4.46,1.51v5.5 c-0.73-0.35-1.25-0.75-1.57-1.2c-0.32-0.45-0.57-1.19-0.76-2.21l-6.27,0.73c0.19,1.03,0.47,1.91,0.84,2.64 c0.37,0.73,0.91,1.41,1.59,2.03c0.69,0.63,1.51,1.13,2.46,1.48c0.95,0.36,2.19,0.6,3.71,0.73v2.32H55.03L55.03,38.06z M52.77,16.37 c-0.67,0.22-1.13,0.49-1.39,0.81c-0.26,0.32-0.39,0.7-0.39,1.14c0,0.45,0.13,0.85,0.4,1.18c0.27,0.34,0.73,0.62,1.39,0.85V16.37 L52.77,16.37z M55.03,31.69c0.88-0.2,1.52-0.53,1.93-0.98c0.41-0.45,0.62-0.96,0.62-1.52c0-0.49-0.18-0.94-0.52-1.35 c-0.35-0.41-1.02-0.79-2.03-1.14V31.69L55.03,31.69z M77.64,66.84h24.61v26.44H77.64c-7.27,0-13.22-5.95-13.22-13.22v0 C64.42,72.78,70.37,66.84,77.64,66.84L77.64,66.84z M83.69,75.68c2.49,0,4.51,2.02,4.51,4.51c0,2.49-2.02,4.51-4.51,4.51 c-2.49,0-4.51-2.02-4.51-4.51C79.18,77.7,81.2,75.68,83.69,75.68L83.69,75.68z"
    )
    return svg


class Seminar(Event):

  def conference(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):

    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
       path="M9.77,9.18c-1.08,0-1.95-0.87-1.95-1.95c0-1.08,0.87-1.95,1.95-1.95h51.91V1.95c0-1.08,0.87-1.95,1.95-1.95 c1.08,0,1.95,0.87,1.95,1.95v3.33h48.32c1.08,0,1.95,0.87,1.95,1.95c0,1.08-0.87,1.95-1.95,1.95h-4.49v49.8h4.7 c1.08,0,1.95,0.87,1.95,1.95c0,1.08-0.87,1.95-1.95,1.95H65.85v5.53c0.1,0.07,0.17,0.14,0.24,0.21l11.95,11.36 c0.77,0.73,0.8,1.99,0.07,2.75c-0.73,0.77-1.99,0.8-2.75,0.07l-9.48-9.02v9.89c0,1.08-0.87,1.95-1.95,1.95 c-1.08,0-1.95-0.87-1.95-1.95V73.39l-9.89,9.41c-0.77,0.73-2.02,0.73-2.75-0.07c-0.73-0.77-0.73-2.02,0.07-2.75l11.95-11.36 c0.17-0.17,0.42-0.31,0.63-0.42v-5.32H35.51c-1.08,0-1.95-0.87-1.95-1.95c0-1.08,0.87-1.95,1.95-1.95h69.99V9.18H9.77L9.77,9.18z M77.17,105.82c-8.69,0-2.97,0.68-1.78-8.76c1.77-14.12,15.19-14.12,17.17,0c1.27,9.08,6.72,8.76-1.78,8.76h-3.39 c-0.01,2.31-0.37,3.49,2.03,4.79c1.22,0.66,3.5,1.16,5.45,1.92c2.97-2.54,8.24-0.87,8.79-5.52c0.08-0.71-1.59-3.41-1.97-4.71 c-0.82-1.31-1.11-3.38-0.22-4.77c0.36-0.55,0.2-2.55,0.2-3.31c0-7.52,13.18-7.52,13.18,0c0,0.95-0.22,2.7,0.3,3.45 c0.86,1.25,0.42,3.47-0.31,4.63c-0.47,1.36-2.24,3.94-2.09,4.71c1.28,6.51,10.15-0.46,10.15,11.25l-24.91,0l-0.01,0h-4.03h-1.08 l-22.94,0l-0.01,0l-22.03,0v0l-27.8,0c0-11.91,11.24-5.31,12.1-12.61c0.09-0.8-1.78-3.82-2.21-5.28c-0.92-1.47-1.25-3.79-0.24-5.34 c0.4-0.62,0.23-2.86,0.23-3.71c0-8.43,14.77-8.43,14.77,0c0,1.07-0.25,3.03,0.33,3.86c0.97,1.4,0.47,3.89-0.35,5.19 c-0.52,1.53-2.51,4.41-2.34,5.28c0.62,3.15,8.47,5.29,11.21,6.45c1.54-0.79,2.79-1.73,2.92-2.82c0.07-0.57-1.27-2.72-1.57-3.76 c-0.65-1.04-0.89-2.7-0.17-3.81c0.28-0.44,0.16-2.04,0.16-2.64c0-6,10.52-6.01,10.52,0c0,0.76-0.17,2.15,0.24,2.75 c0.69,1,0.33,2.77-0.25,3.69c-0.37,1.09-1.79,3.14-1.67,3.76c0.77,3.94,5.03,1.7,7.04,4.45c1.9-1.5,5.68-1.91,7.99-3.29 c2.11-1.26,1.75-2.53,1.74-4.63L77.17,105.82L77.17,105.82L77.17,105.82z M0.01,46.73c-0.28-5.43,4.18-6.86,10.24-6.48l7.66,8.53 l7.49-8.43l18.57-0.1c7,0.8,5.54,8.15,0,8.43H31.82l-2.86,17.17L26.8,77.02c-0.56,1.85-1.67,3.03-3.31,3.66l-10.56,0.07 c-2.13-0.31-3.38-1.57-3.76-3.76l-1.64-9.25c-4.32,0.42-5.78-2.65-6.24-7.07L0.05,46.7L0.01,46.73L0.01,46.73z M17.47,17.02 c5.19,0,9.41,4.22,9.41,9.41s-4.22,9.41-9.41,9.41c-5.19,0-9.41-4.22-9.41-9.41S12.27,17.02,17.47,17.02L17.47,17.02z M17.81,44.78 l-5.96-6.55l1.74-1.39c2.58,1.08,5.16,1.08,7.7,0l2.4,1.43L17.81,44.78L17.81,44.78z"
    )
    return svg

  def partner(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """
    https://uxwing.com/business-partner-icon/

    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
       path="M45.13,35.29h-0.04l-6.54,16.22l-2.22-10.17h0.89c0.81,0,1.47-0.66,1.47-1.47v-2.39 c0-0.81-0.66-1.47-1.47-1.47H31.9c-0.81,0-1.47,0.66-1.47,1.47v2.39c0,0.81,0.66,1.47,1.47,1.47h0.91l-2.29,10.03l-6.21-16.08 C17.04,35.6,9.47,41.91,5.02,51.3c-2.61,5.51-3.3,9.66-3.73,15.55C0.42,72.79-0.03,78.67,0,84.47c1.43,9.03,12.88,6.35,13.85,0 l1.39-18.2c0.21-2.75,0.4-4.61,1.51-7.23c0.52-1.23,1.15-2.28,1.89-3.15l0.69,33.25l-0.39,2.78h31.49l-0.42-3.1l0.61-36.67 c3.19-1.29,5.96-1.89,8.39-1.99c-0.12,0.25-0.25,0.5-0.37,0.75c-2.61,5.51-3.3,9.66-3.73,15.55c-0.86,5.93-1.32,11.81-1.29,17.61 c1.43,9.03,12.88,6.35,13.85,0l1.39-18.2c0.21-2.75,0.4-4.61,1.51-7.23c0.52-1.23,1.15-2.28,1.89-3.15l0.69,33.25l-0.46,3.24h31.62 l-0.48-3.55l0.49-28.62v0.56l0.1-4.87c0.74,0.87,1.36,1.92,1.89,3.15c1.12,2.62,1.3,4.48,1.51,7.23l1.39,18.2 c0.15,0.95,0.53,1.82,1.07,2.57h11.97c0.37-0.72,0.65-1.58,0.81-2.57c0.03-5.81-0.42-11.68-1.29-17.61 c-0.43-5.89-1.12-10.04-3.73-15.55c-4.57-9.65-10.48-14.76-19.45-15.81l-6.32,16.01l-2.13-9.79h1.02c0.81,0,1.47-0.66,1.47-1.47 v-2.39c0-0.81-0.66-1.47-1.47-1.47h-5.33c-0.81,0-1.47,0.66-1.47,1.47v2.39c0,0.81,0.66,1.47,1.47,1.47h0.61l-2.2,9.65l-6-15.98 c-1.38,0.19-2.74,0.47-4.06,0.87c-3.45-0.48-8.01-1.07-12.56-1.09C54.76,34.77,48.14,35.91,45.13,35.29L45.13,35.29z M88.3,0 c9.01,0,16.32,7.31,16.32,16.32c0,9.01-7.31,16.32-16.32,16.32c-9.01,0-16.32-7.31-16.32-16.32C71.98,7.31,79.29,0,88.3,0L88.3,0z M34.56,0c9.01,0,16.32,7.31,16.32,16.32c0,9.01-7.31,16.32-16.32,16.32c-9.01,0-16.32-7.31-16.32-16.32 C18.24,7.31,25.55,0,34.56,0L34.56,0z"
    )
    return svg

  def team(self, fill=None, border=None, width=(50, "px"), height=(30, "px")):
    """
    https://uxwing.com/business-team-icon/

    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height, viewbox=(150, 80),
      path="M91.95,64.68l1.99-7.59l-1.37-1.5c-0.62-0.9-0.75-1.69-0.41-2.37c0.74-1.47,2.28-1.2,3.72-1.2 c1.51,0,3.37-0.29,3.84,1.6c0.16,0.63-0.04,1.29-0.48,1.97l-1.37,1.5l1.19,4.56l7.89-6.86l4.09,0.1c-1.41-2.83-3.2-5.23-5.28-7.49 c3.92,1.52,7.93,3.02,10.9,4.88c1.89,1.18,2.86,2.08,3.63,3.51c1.62,3.05,1.8,5.78,2.04,9.08l0.57,2.86h-22.24l0.02,0.07h-8.51 c-0.19,1.95-1.31,3.08-3.5,3.24H61.68H34.24c-2.2-0.17-3.32-1.3-3.5-3.27l0.76-12.04c0.21-2.78,0.99-4.98,2.26-6.66 c0.84-1.11,1.88-1.93,3.03-2.57c3.65-2.03,12.17-2.63,15.48-5.61l5.07,14.91l2.55-8.85l-1.25-1.37c-0.56-0.82-0.69-1.54-0.37-2.16 c0.68-1.34,2.08-1.09,3.39-1.09c1.37,0,3.06-0.26,3.49,1.46c0.14,0.57-0.04,1.17-0.44,1.79l-1.25,1.37l2.55,8.85l4.59-14.91 c3.31,2.98,11.84,3.58,15.48,5.61c1.15,0.64,2.2,1.46,3.03,2.57c1.27,1.68,2.05,3.87,2.26,6.66L91.95,64.68L91.95,64.68z M15.29,48.25l3.4,9.99l1.71-5.93l-0.84-0.92c-0.38-0.55-0.46-1.03-0.25-1.45c0.45-0.9,1.39-0.73,2.27-0.73 c0.92,0,2.05-0.17,2.34,0.98c0.1,0.38-0.03,0.79-0.29,1.2l-0.84,0.92l1.71,5.93l3.08-9.99c0.45,0.4,1.07,0.74,1.8,1.03 c-0.25,0.53-0.48,1.09-0.68,1.67c-0.52,1.51-0.86,3.19-1,5.06l0.01,0c0,0.04-0.01,0.09-0.01,0.13l-0.74,11.58h-5.35H2.35 C0.87,67.61,0.12,66.85,0,65.53l0.51-7.34c0.14-1.86,0.67-3.33,1.52-4.46c0.56-0.74,1.26-1.29,2.03-1.72 C6.5,50.65,13.07,50.25,15.29,48.25L15.29,48.25z M13.62,34.09c-0.33,0.03-0.58,0.1-0.76,0.22c-0.1,0.07-0.18,0.16-0.23,0.26 c-0.06,0.12-0.08,0.28-0.08,0.45c0.02,0.55,0.31,1.29,0.88,2.14l0.01,0.02l0,0l1.9,3.02c0.76,1.2,1.55,2.43,2.53,3.33 c0.93,0.85,2.06,1.43,3.56,1.43c1.62,0,2.8-0.6,3.77-1.5c1.01-0.95,1.81-2.25,2.6-3.55l2.13-3.51c0.43-0.98,0.56-1.57,0.42-1.85 c-0.09-0.17-0.44-0.22-1.02-0.17c-0.37,0.08-0.76,0.01-1.17-0.2l1.07-3.2c-3.91-0.05-6.58-0.73-9.75-2.75 c-1.04-0.66-1.35-1.42-2.39-1.35c-0.79,0.15-1.45,0.5-1.97,1.07c-0.5,0.54-0.88,1.28-1.13,2.23l0.63,3.83 C14.3,34.21,13.96,34.23,13.62,34.09L13.62,34.09z M30.55,33.14c0.46,0.14,0.8,0.4,1,0.81c0.32,0.65,0.2,1.62-0.41,3l0,0 c-0.01,0.03-0.02,0.05-0.04,0.08l-2.16,3.56c-0.84,1.38-1.69,2.76-2.83,3.83c-1.19,1.12-2.66,1.86-4.67,1.85 c-1.88,0-3.29-0.72-4.45-1.78c-1.11-1.02-1.96-2.32-2.76-3.6l-1.9-3.02c-0.71-1.06-1.07-2.02-1.1-2.82 c-0.01-0.39,0.05-0.74,0.2-1.04c0.15-0.33,0.38-0.6,0.7-0.81c0.15-0.1,0.33-0.19,0.52-0.26c-0.12-1.62-0.16-3.62-0.08-5.3 c0.04-0.41,0.12-0.82,0.23-1.23c0.49-1.73,1.7-3.13,3.21-4.09c0.53-0.34,1.11-0.62,1.73-0.84c3.65-1.32,8.48-0.6,11.07,2.2 c1.05,1.14,1.72,2.65,1.86,4.65L30.55,33.14L30.55,33.14z M49.65,19.77c-0.42,0.05-0.75,0.16-0.99,0.32 c-0.15,0.1-0.27,0.24-0.34,0.39c-0.08,0.18-0.12,0.41-0.12,0.67c0.02,0.83,0.46,1.92,1.32,3.18l0.02,0.02h0l2.83,4.51 c1.13,1.8,2.31,3.63,3.77,4.96c1.39,1.27,3.08,2.13,5.3,2.14c2.42,0.01,4.18-0.89,5.62-2.23c1.51-1.41,2.71-3.36,3.89-5.3 l3.18-5.24c0.64-1.46,0.84-2.34,0.63-2.76c-0.13-0.27-0.69-0.33-1.63-0.24c-0.07,0.01-0.14,0.01-0.21,0c-0.39,0-0.81-0.1-1.27-0.31 l1.43-4.78c-5.84-0.07-9.83-1.09-14.55-4.11c-1.55-0.99-2.02-2.12-3.57-2.01c-1.17,0.23-2.16,0.75-2.94,1.59 c-0.75,0.81-1.32,1.91-1.69,3.32l1.01,5.78C50.74,19.98,50.18,20,49.65,19.77L49.65,19.77z M75.05,18.34 c0.69,0.2,1.19,0.6,1.5,1.21c0.48,0.98,0.3,2.42-0.61,4.48l0,0c-0.02,0.04-0.04,0.08-0.06,0.11l-3.23,5.32 c-1.25,2.06-2.52,4.13-4.23,5.72c-1.78,1.67-3.97,2.78-6.97,2.77c-2.8-0.01-4.91-1.08-6.64-2.66c-1.66-1.52-2.92-3.46-4.12-5.37 l-2.83-4.51c-1.05-1.57-1.6-3.02-1.64-4.21c-0.02-0.58,0.08-1.1,0.3-1.56c0.23-0.49,0.57-0.9,1.04-1.21 c0.23-0.16,0.49-0.29,0.78-0.39c-0.17-2.41-0.23-5.39-0.12-7.9c0.06-0.61,0.18-1.22,0.35-1.83c0.72-2.59,2.54-4.67,4.79-6.1 c0.79-0.5,1.66-0.92,2.58-1.25c5.44-1.97,12.66-0.89,16.52,3.29c1.57,1.7,2.56,3.96,2.77,6.94L75.05,18.34L75.05,18.34z M84.88,42.96l2.5-0.07l2.07-0.05c-2.42-7.45-1.61-14.3,4.22-20.12c0.99,3.2,3.2,5.83,6.97,7.78c1.8,1.34,3.55,2.96,5.23,4.81 c0.3-1.23-0.84-2.73-2.23-4.27c1.28,0.63,2.46,1.52,3.29,3.22c0.97,1.98,0.95,3.64,0.64,5.79c-0.15,1-0.39,1.93-0.74,2.78h3.45 c3.64-7.79,1.33-19.34-6.11-24.24c-2.28-1.5-3.92-1.45-6.6-1.44c-3.07,0-4.63,0.1-7.26,1.83c-3.87,2.56-6.25,6.99-7.25,13.14 C82.87,35.19,82.74,40.49,84.88,42.96L84.88,42.96z"
    )
    return svg

  def direction(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """
    https://uxwing.com/direction-road-sign-icon/

    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
       path="M84.78,17.66H23.35L5.71,28.49l17.7,12.05h61.38V17.66L84.78,17.66z M24.64,53.52h22.81v-9.14H22.87v0 c-0.34,0-0.69-0.09-1-0.28L0.91,30.05l0,0c-0.27-0.17-0.51-0.41-0.68-0.71c-0.51-0.92-0.17-2.09,0.75-2.59l20.79-12.58 c0.31-0.22,0.69-0.34,1.1-0.34h24.58V8.05L55,0l8.44,8.05v5.77H86.7c1.06,0,1.92,0.86,1.92,1.92v26.72c0,1.06-0.86,1.92-1.92,1.92 H63.44v9.14h25.03c0.41,0,0.78,0.13,1.1,0.34l20.79,12.58c0.92,0.51,1.26,1.67,0.75,2.59c-0.17,0.3-0.4,0.54-0.68,0.71l0,0 L89.47,83.8c-0.31,0.19-0.66,0.28-1,0.28v0H63.44v24.2H78.9c1.56,0,2.83,1.28,2.83,2.83v8.93c0,1.56-1.28,2.83-2.83,2.83H31.99 c-1.56,0-2.83-1.28-2.83-2.83v-6.8c0-2.73,2.23-4.96,4.96-4.96h13.33v-24.2H24.64c-1.06,0-1.92-0.86-1.92-1.92V55.44 C22.72,54.38,23.58,53.52,24.64,53.52L24.64,53.52z M88,57.36H26.56v22.88h61.38l17.7-12.05L88,57.36L88,57.36z"
    )
    return svg

  def coffee(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """
    https://uxwing.com/tea-hot-icon/

    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
       path="M101.71,56.76h-5.54v16.51h5.55v0.02c1.14,0,2.19-0.49,2.96-1.26l0.14-0.13c0.68-0.75,1.1-1.73,1.1-2.8 l-0.01,0v-0.03h0.01v-8.1h-0.01v-0.02l0.01,0c0-1.15-0.48-2.2-1.24-2.96c-0.76-0.76-1.81-1.24-2.95-1.25v0.01H101.71L101.71,56.76 L101.71,56.76z M31.66,0.61c1.75-1.16,4.08-0.63,5.2,1.17c1.12,1.8,0.61,4.21-1.14,5.37c-3.19,2.11-3.21,3.75-2.23,5.22 c0.84,1.27,2.14,2.66,3.43,4.03c1.79,1.91,3.59,3.82,4.82,6.03c2.93,5.23,2.67,10.43-6.55,15.59c-1.82,1.02-4.11,0.33-5.1-1.55 c-0.99-1.88-0.32-4.24,1.5-5.26c3.85-2.15,4.34-3.66,3.63-4.92c-0.74-1.31-2.22-2.89-3.7-4.47c-1.53-1.63-3.07-3.27-4.26-5.07 C23.83,11.54,23.21,6.2,31.66,0.61L31.66,0.61z M74.07,0.61c1.75-1.16,4.08-0.63,5.2,1.17c1.12,1.8,0.61,4.21-1.14,5.37 c-3.19,2.11-3.2,3.75-2.23,5.22c0.84,1.27,2.14,2.66,3.43,4.03c1.79,1.91,3.59,3.82,4.82,6.03c2.93,5.23,2.68,10.43-6.54,15.59 c-1.82,1.02-4.11,0.33-5.1-1.55c-0.99-1.88-0.32-4.24,1.5-5.26c3.85-2.15,4.33-3.65,3.62-4.92c-0.74-1.31-2.22-2.89-3.7-4.47 c-1.53-1.63-3.07-3.27-4.26-5.07C66.24,11.53,65.61,6.2,74.07,0.61L74.07,0.61z M52.87,0.61c1.75-1.16,4.08-0.63,5.2,1.17 c1.12,1.8,0.61,4.21-1.14,5.37c-3.19,2.11-3.21,3.75-2.23,5.22c0.84,1.27,2.14,2.66,3.43,4.03c1.79,1.91,3.59,3.82,4.82,6.03 c2.93,5.23,2.68,10.43-6.54,15.59c-1.82,1.02-4.11,0.33-5.1-1.55c-0.99-1.88-0.32-4.24,1.5-5.26c3.85-2.15,4.33-3.66,3.62-4.92 c-0.74-1.31-2.22-2.89-3.7-4.47c-1.53-1.63-3.08-3.27-4.26-5.07C45.03,11.54,44.42,6.2,52.87,0.61L52.87,0.61z M1.42,112.34h36.12 c-12.25-6.13-20.72-18.8-20.72-33.37V48.92h74.58v0.39c0.32-0.09,0.66-0.13,1.01-0.13l9.35,0v0.02h0.02 c3.22,0.01,6.14,1.32,8.26,3.44c2.13,2.12,3.46,5.07,3.47,8.31l0.01,0v0.02h-0.01v7.96l0,0.14h0.01v0.03h-0.01v0.02 c-0.01,3.08-1.22,5.9-3.18,7.99c-0.08,0.1-0.17,0.19-0.26,0.28c-2.12,2.12-5.07,3.44-8.32,3.45v0.02l-9.34,0 c-0.36,0-0.72-0.06-1.05-0.15c-0.63,13.84-8.9,25.77-20.67,31.65h38.15c0.78,0,1.42,0.76,1.42,1.7v7.15c0,0.94-0.64,1.69-1.42,1.69 l-107.4,0c-0.78,0-1.42-0.76-1.42-1.69v-7.15C0,113.1,0.64,112.34,1.42,112.34L1.42,112.34L1.42,112.34z"
    )
    return svg


class Show(Event):

  def location(self):
    pass

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

  def music(self,  fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """
    https://uxwing.com/audio-playlist-icon/

    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
        path="M73.12,0H88.6v5.17c38.74,8.87,43.17,27.47,20.7,56.79c2.39-29.09-0.54-35.33-20.7-36.68v73.54 c0.04,0.39,0.05,0.78,0.05,1.18c0,9.56-10.03,19.04-22.4,21.18c-12.37,2.14-22.4-3.88-22.4-13.44c0-13.04,17.91-24.36,29.26-20.37 L73.12,0L73.12,0z M5.69,73.78C2.55,73.78,0,71.23,0,68.09c0-3.14,2.55-5.69,5.69-5.69h47.63c3.14,0,5.69,2.55,5.69,5.69 c0,3.14-2.55,5.69-5.69,5.69H5.69L5.69,73.78z M5.69,46.14C2.55,46.14,0,43.59,0,40.44c0-3.14,2.55-5.69,5.69-5.69h47.63 c3.14,0,5.69,2.55,5.69,5.69c0,3.14-2.55,5.69-5.69,5.69H5.69L5.69,46.14z M5.69,18.5C2.55,18.5,0,15.95,0,12.8 c0-3.14,2.55-5.69,5.69-5.69h47.63c3.14,0,5.69,2.55,5.69,5.69c0,3.14-2.55,5.69-5.69,5.69H5.69L5.69,18.5z"
    )
    return svg

  def movie(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """
    https://uxwing.com/movie-media-player-icon/

    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
        path="M108.07,15.56L5.7,52.84L0,37.22L102.37,0L108.07,15.56L108.07,15.56z M115.46,122.88H5.87V53.67h109.59 V122.88L115.46,122.88z M101.79,15.65V2.36l-7.23,2.61v13.34L101.79,15.65L101.79,15.65L101.79,15.65z M87.39,20.93V7.59 l-7.26,2.58v13.45L87.39,20.93L87.39,20.93z M72.49,26.07v-13.2l-7.26,2.61v13.26L72.49,26.07L72.49,26.07L72.49,26.07z M113.43,68.32l-4.56-12.54h-7.73l4.56,12.54H113.43L113.43,68.32z M97.64,68.32l-4.56-12.54h-7.76l4.59,12.54H97.64L97.64,68.32z M57.98,31.69V18.32l-7.25,2.61v13.34L57.98,31.69L57.98,31.69z M82.41,68.32l-4.56-12.54h-7.73l4.56,12.54H82.41L82.41,68.32z M43.08,36.8V23.54l-7.34,2.61v13.34L43.08,36.8L43.08,36.8z M66.62,68.32l-4.56-12.54h-7.75l4.56,12.54H66.62L66.62,68.32z M28.82,42.28V28.9l-7.31,2.7v13.26L28.82,42.28L28.82,42.28L28.82,42.28z M51.06,68.32L46.5,55.78h-7.73l4.56,12.54H51.06 L51.06,68.32z M13.84,47.39V34.13l-7.26,2.58v13.37L13.84,47.39L13.84,47.39z M35.36,68.32l-4.64-12.54l-7.67,0l4.48,12.54H35.36 L35.36,68.32z M19.96,68.32l-4.64-12.54l-7.73,0l4.56,12.54H19.96L19.96,68.32z"
    )
    return svg

  def sing(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """
    https://uxwing.com/sing-icon/

    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
        path="M82.07,40.62c4.82,4.82,7.23,11.14,7.23,17.45c0,6.32-2.41,12.63-7.23,17.45c-1.24,1.24-2.59,2.33-4.01,3.25 c-6.91-0.5-14.59-5.59-20.9-12.23c-6.52-6.86-11.52-15.29-12.75-22.09c-0.03-0.15-0.05-0.29-0.07-0.44 c0.83-1.19,1.77-2.33,2.84-3.39c4.82-4.82,11.14-7.23,17.45-7.23C70.94,33.39,77.25,35.8,82.07,40.62L82.07,40.62z M108.73,37.6 h4.4v1.47c11.01,2.52,12.27,7.81,5.88,16.14c0.68-8.27-0.15-10.04-5.88-10.43v20.9c0.01,0.11,0.02,0.22,0.02,0.33 c0,2.72-2.85,5.41-6.37,6.02c-3.52,0.61-6.37-1.1-6.37-3.82c0-3.71,5.09-6.92,8.32-5.79L108.73,37.6L108.73,37.6z M94.99,85.23 c2.92,0,5.28,2.36,5.28,5.28c0,2.92-2.36,5.28-5.28,5.28c-2.92,0-5.28-2.36-5.28-5.28C89.71,87.59,92.07,85.23,94.99,85.23 L94.99,85.23z M72.7,10.71h2.08v0.69c5.19,1.19,5.79,3.68,2.78,7.61c0.32-3.9-0.07-4.74-2.78-4.92v9.86 c0.01,0.05,0.01,0.1,0.01,0.16c0,1.28-1.35,2.55-3,2.84c-1.66,0.29-3-0.52-3-1.8c0-1.75,2.4-3.27,3.92-2.73V10.71L72.7,10.71z M31.99,21.89c0.77-0.13,1.49-0.11,2.13,0.04V6.96l-15.83,4.55v17.38c0.01,0.09,0.01,0.19,0.01,0.29c0,0,0,0,0,0 c0,2.34-2.46,4.66-5.48,5.19c-3.03,0.52-5.48-0.95-5.48-3.29c0-2.34,2.46-4.66,5.48-5.19c1.14-0.2,2.2-0.11,3.08,0.2l0-21.39h0.13 L36.51,0v24.1c0.04,0.18,0.05,0.36,0.05,0.54c0,0,0,0,0,0c0,1.95-2.05,3.9-4.58,4.33c-2.53,0.44-4.58-0.79-4.58-2.75 C27.4,24.27,29.46,22.33,31.99,21.89L31.99,21.89L31.99,21.89z M6.72,119.07c-1.16,1.08-2.49,1.92-3.95,2.54 c-2.96,1.27-3.39,1.49-2.02-1.49c0.72-1.56,1.63-2.99,2.77-4.26c-1.27-1.36-1.92-2.64-2.11-4.11c-0.19-1.51,0.14-3.03,0.8-4.96 c2.16-6.28,19.88-27.95,30.92-41.44c2.83-3.46,5.2-6.36,6.84-8.43c0.12-2.58,0.64-5.14,1.56-7.58c2.42,6.59,7.1,13.78,12.82,19.79 c5.28,5.56,11.49,10.17,17.69,12.48c-2.16,0.68-4.4,1.06-6.65,1.13c-1.79,1.41-4.35,3.48-7.46,6c-13.58,11-37.3,30.2-42.31,31.72 c-1.79,0.54-3.28,0.84-4.74,0.67C9.39,120.95,8.07,120.33,6.72,119.07L6.72,119.07L6.72,119.07z M40.36,62.58 c-1.23,1.51-2.67,3.28-4.25,5.21c-10.86,13.27-28.3,34.59-30.24,40.25c-0.48,1.4-0.73,2.42-0.63,3.21 c0.09,0.69,0.51,1.38,1.38,2.24l2.57,2.57c0.78,0.78,1.45,1.14,2.15,1.22c0.83,0.1,1.87-0.13,3.2-0.53 c4.29-1.29,27.62-20.19,40.99-31.01c1.59-1.29,3.04-2.46,4.3-3.48c-4.63-0.92-9.05-3.17-12.64-6.76 C43.51,71.85,41.24,67.32,40.36,62.58L40.36,62.58L40.36,62.58z"
    )
    return svg


class Dating(Event):

  def drinks(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """

    https://uxwing.com/glass-drinks-icon/

    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
      path="M56.6,42.23c-10.57-9.69-27.14-5.26-41.16-6.82c2.29-7.28,5.35-15.21,8.72-23.59 c2.98-7.42,3.01-7.41,8.55-6.22c1.02,0.22,2.18,0.47,3.35,0.7l18.46,3.64c0.93,0.26,1.62,0.67,2.09,1.22 c0.48,0.56,0.79,1.3,0.94,2.23c-0.09,2.7-0.13,5.69-0.17,8.81C57.3,28.52,57.21,35.45,56.6,42.23L56.6,42.23z M84.64,120.9 c-1.81,0.35-3.56-0.84-3.91-2.65c-0.35-1.81,0.84-3.56,2.65-3.91l14.07-2.72l-6.01-29.38c-2.05,0.2-4.02,0.17-5.89-0.09 c-4.12-0.57-7.76-2.22-10.93-4.92c-8.79-7.47-12.21-19.66-13.59-32.38c-1.38,12.71-4.8,24.9-13.59,32.38 c-3.18,2.7-6.82,4.35-10.93,4.92c-1.87,0.26-3.83,0.29-5.89,0.09l-6.42,31.41l13.52,2.62c1.81,0.35,3,2.1,2.65,3.91 c-0.35,1.81-2.1,3-3.91,2.65l-33.75-6.53c-1.81-0.35-3-2.1-2.65-3.91c0.35-1.81,2.1-3,3.91-2.65l13.67,2.64l6.44-31.47 c-0.24-0.07-0.48-0.15-0.73-0.23c-0.04-0.01-0.08-0.02-0.12-0.04C10.02,76.34,5.77,66.96,6.67,54.09 c0.84-12.06,6.39-27.18,13.15-44.01C24.28-1,24.32-0.99,33.68,1.02c0.91,0.2,1.95,0.42,3.27,0.68l18.5,3.65l0,0 c0.05,0.01,0.1,0.02,0.15,0.03c1.93,0.51,3.43,1.43,4.55,2.73c0.33,0.39,0.62,0.8,0.88,1.24c0.25-0.44,0.55-0.86,0.88-1.24 c1.12-1.3,2.63-2.22,4.55-2.73c0.05-0.01,0.1-0.02,0.15-0.03l0,0l18.5-3.65c1.32-0.26,2.36-0.48,3.27-0.68 c9.36-2.01,9.4-2.02,13.85,9.06c6.77,16.83,12.31,31.95,13.15,44.01c0.9,12.86-3.35,22.25-16.56,26.55 c-0.04,0.01-0.08,0.02-0.12,0.04c-0.24,0.08-0.49,0.15-0.73,0.23l6.02,29.45l13.13-2.54c1.81-0.35,3.56,0.84,3.91,2.65 c0.35,1.81-0.84,3.56-2.65,3.91L84.64,120.9L84.64,120.9z M74.1,59.53c-0.27-0.69,0.07-1.46,0.76-1.73s1.46,0.07,1.73,0.76 c1.71,4.35,4.08,7.55,7.02,9.75c2.93,2.18,6.46,3.39,10.51,3.74c0.74,0.06,1.28,0.71,1.22,1.45c-0.06,0.74-0.71,1.28-1.45,1.22 c-4.54-0.4-8.53-1.77-11.88-4.26C78.68,67.96,76.01,64.37,74.1,59.53L74.1,59.53z M65.56,43.33c15.19-6.85,30.94-14.24,39.03-13.99 c-1.95-5.55-4.24-11.42-6.69-17.52c-2.98-7.42-3.01-7.41-8.55-6.22c-1.02,0.22-2.18,0.47-3.35,0.7L67.55,9.94 c-0.93,0.26-1.62,0.67-2.09,1.22c-0.48,0.56-0.79,1.3-0.94,2.23c0.09,2.7,0.13,5.69,0.17,8.81C64.76,28.86,64.85,36.2,65.56,43.33 L65.56,43.33z M48.68,53.5c0.1-0.73,0.78-1.24,1.51-1.13c0.73,0.1,1.24,0.78,1.13,1.51c-0.75,5.14-2.52,9.25-5.21,12.44 c-2.69,3.2-6.26,5.45-10.58,6.87c-0.7,0.23-1.46-0.15-1.69-0.85c-0.23-0.7,0.15-1.46,0.85-1.69c3.87-1.27,7.03-3.25,9.38-6.05 C46.44,61.8,48,58.14,48.68,53.5L48.68,53.5z"
    )
    return svg

  def dinner(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
      path="M29.11,43.35L29,50.04h12.08c2.56,0,4.65,2.09,4.65,4.65v4.65h-0.05v18.18c0,2.56-2.09,4.65-4.65,4.65h-4.65 V61.02c0-1.92,0.36-1.68-1.49-1.68H22.93v-0.03h-5.96c-3.84,0-6.99-3.15-6.99-6.99v-22.9c0-3.91,3.2-7.11,7.11-7.11h3.52 c5.58,0,6.13,2.67,7.55,5.46l5.94,2.34c4.3,1.94,3.2,2.32,6.12-1.3l3.8-4.7c1.86-2.97,9.21,0.13,6.06,5.12l-5.51,7.52 c-2.29,3.13-5.34,3.57-9.03,2.04l-6.42-2.26V43.35L29.11,43.35z M119.06,77.82c-0.04-0.29-0.16-0.56-0.38-0.78 c-1.61-1.62-3.64-2.94-5.96-3.85c-1.62-0.63-3.39-1.06-5.24-1.25l0.35-5.54h12.61c1.31,0,2.39-1.08,2.39-2.39 c0-9.9-2.33-17.34,0-28.61c0.69-3.34-6.2-3.82-6.2,0.18v25.37H92.78c-1.31,0-2.39,1.76-2.39,3.07v1.86c0,0.29,0.24,0.53,0.53,0.53 h12.65l0.49,5.48c-1.96,0.13-3.83,0.53-5.56,1.16c-2.22,0.81-4.19,2-5.79,3.46c-0.38,0.35-0.52,0.87-0.4,1.34 c-0.62,0.46-1.02,0.92-1.02,2.04s1.14,2.54,2.54,2.54s2.54-1.42,2.54-2.54s-0.41-1.59-1.04-2.05c1.19-0.92,2.57-1.69,4.09-2.24 c1.63-0.6,3.43-0.96,5.33-1.02l0.28,2.75l0.01,0.12c-1.07,0.3-1.86,1.16-1.86,2.45s1.14,2.54,2.54,2.54s2.54-1.26,2.54-2.54 c0-1.28-0.78-2.14-1.84-2.44l0.01-0.13l0.2-2.72c1.81,0.12,3.53,0.51,5.09,1.12h0.01c1.52,0.59,2.89,1.39,4.06,2.36 c-0.47,0.46-0.76,0.76-0.76,1.81s1.14,2.54,2.54,2.54c1.4,0,2.54-1.42,2.54-2.54C120.12,78.75,119.7,78.28,119.06,77.82 L119.06,77.82z M98.71,0.34c-5.37,0-9.73,4.36-9.73,9.73c0,5.37,4.36,9.73,9.73,9.73c5.37,0,9.73-4.36,9.73-9.73 C108.43,4.7,104.08,0.34,98.71,0.34L98.71,0.34z M94.66,38.5l0.19,11.54H82.77c-2.56,0-4.65,2.09-4.65,4.65v4.65h0.05v18.18 c0,2.56,2.09,4.65,4.65,4.65h4.65v-21.5c0-2.04,0.77-1.33,3.07-1.33h10.38v-0.03h5.96c3.85,0,6.99-3.15,6.99-6.99V28.06 c0-3.91-3.2-7.11-7.11-7.11h-3.52c-7.32,0-6.16,5.04-9.4,8.21c-3.2,3.13-2.4,3.49-6.77,3.49h-9.42c-5.62,0-7,7.35,1.01,7.35h8.64 C91.15,40,91.48,40.61,94.66,38.5L94.66,38.5z M85.42,41.5c-15.16,0-26.91,0-42.07,0c-0.23,0-0.41,0.19-0.41,0.41v5.92 c0,0.23,0.19,0.41,0.41,0.41c7.92,0,9.73,0,17.66,0v36.31c0,0.3,0.25,0.55,0.55,0.55h0.21h0.01h5.82h0.01h0.21 c0.3,0,0.55-0.25,0.55-0.55V48.25c5.23,0,11.82,0,17.05,0c0.22,0,0.41-0.19,0.41-0.41v-5.92C85.83,41.68,85.64,41.5,85.42,41.5 L85.42,41.5z M1.29,36.78h3.39c0.69,0,1.15,0.58,1.26,1.26c1.28,8.08,1.98,16.16,1.94,24.23h23.2c0.92,0,1.66,0.75,1.66,1.66v3.36 h-1.33V84.5c0,0.28-0.23,0.51-0.51,0.51h-4.45c-0.28,0-0.51-0.23-0.51-0.51v-7.48H6.97c-0.28,2.28-0.62,4.56-1.03,6.84 c-0.12,0.68-0.57,1.26-1.26,1.26H1.29c-0.69,0-1.45-0.59-1.26-1.26c4.47-15.56,3.54-30.77,0-45.81 C-0.13,37.37,0.6,36.78,1.29,36.78L1.29,36.78z M25.95,74.7v-7.4H7.81c-0.1,3.15-0.32,4.25-0.66,7.4H25.95L25.95,74.7z M20.39,0 c5.37,0,9.73,4.36,9.73,9.73s-4.36,9.73-9.73,9.73s-9.73-4.36-9.73-9.73S15.01,0,20.39,0L20.39,0z"
    )
    return svg

  def love(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """
    https://uxwing.com/heart-icon/

    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
                                                    path="M60.83,17.19C68.84,8.84,74.45,1.62,86.79,0.21c23.17-2.66,44.48,21.06,32.78,44.41 c-3.33,6.65-10.11,14.56-17.61,22.32c-8.23,8.52-17.34,16.87-23.72,23.2l-17.4,17.26L46.46,93.56C29.16,76.9,0.95,55.93,0.02,29.95 C-0.63,11.75,13.73,0.09,30.25,0.3C45.01,0.5,51.22,7.84,60.83,17.19L60.83,17.19L60.83,17.19z"
                                                    )
    return svg

  def like(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """
    https://uxwing.com/thumbs-up-black-icon/

    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
                                                    path="M4.02,44.6h27.36c2.21,0,4.02,1.81,4.02,4.03v53.51c0,2.21-1.81,4.03-4.02,4.03H4.02 c-2.21,0-4.02-1.81-4.02-4.03V48.63C0,46.41,1.81,44.6,4.02,44.6L4.02,44.6z M63.06,4.46c2.12-10.75,19.72-0.85,20.88,16.48 c0.35,5.3-0.2,11.47-1.5,18.36l25.15,0c10.46,0.41,19.59,7.9,13.14,20.2c1.47,5.36,1.69,11.65-2.3,14.13 c0.5,8.46-1.84,13.7-6.22,17.84c-0.29,4.23-1.19,7.99-3.23,10.88c-3.38,4.77-6.12,3.63-11.44,3.63H55.07 c-6.73,0-10.4-1.85-14.8-7.37V51.31c12.66-3.42,19.39-20.74,22.79-32.11V4.46L63.06,4.46z"
                                                    )
    return svg

  def broken(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """
    https://uxwing.com/broken-heart-icon/

    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
       path="M66.45,11.99C72.23,6,77.7,1.31,87.33,0.21c22.83-2.62,43.82,20.75,32.29,43.76 c-3.28,6.56-9.96,14.35-17.35,21.99c-8.11,8.4-17.08,16.62-23.37,22.86l-6.8,6.74l-7.34-10.34l8.57-12.08l-7.09-6.45l5.89-7.76 l-8.17-11.52l8.17-11.52l-5.89-7.76l7.09-6.45L66.45,11.99L66.45,11.99z M55.81,101.54l-10.04-9.67 C28.73,75.46,0.94,54.8,0.02,29.21C-0.62,11.28,13.53-0.21,29.8,0c13.84,0.18,20.05,6.74,28.77,15.31l3.49,4.92l-2.02,1.83 l-0.01-0.01l-0.65,0.61l-4.54,4.13l0.06,0.08l-0.05,0.04l2.64,3.47l1.65,2.24l0.03-0.03l2.39,3.15l-8,11.28l-0.07,0.06l0.01,0.02 l-0.01,0.02l0.07,0.06l8,11.28l-2.39,3.15l-0.03-0.03l-1.64,2.23l-2.64,3.48l0.05,0.04l-0.06,0.08l4.54,4.13l0.65,0.61l0.01-0.01 l2.02,1.83l-7.73,10.89l0.05,0.05l-0.05,0.05l7.73,10.89l-2.02,1.83l-0.01-0.01l-0.65,0.61L55.81,101.54L55.81,101.54z"
    )
    return svg

  def bed(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """
    https://uxwing.com/bed-heart-love-icon/

    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
       path="M3.48,89.22h115.8v-5.08c0-2.46-0.98-4.52-2.55-6.09c-0.99-0.99-2.22-1.8-3.6-2.42 c-3.53-0.77-7.06-1.46-10.59-2.06c-0.07-0.01-0.14-0.02-0.21-0.04c-1.72-0.3-3.45-0.57-5.17-0.83c-12.36-1.59-24.64-2.4-36.82-2.4 c-7.22-0.01-14.41,0.27-21.57,0.83c-6.75,0.64-13.49,1.55-20.22,2.74l-0.38,0.09C18.06,73.98,17.94,74,17.82,74 c-3.27,0.59-6.54,1.24-9.81,1.96C7.14,76.43,6.36,77,5.7,77.67c-1.37,1.37-2.22,3.15-2.22,5.29L3.48,89.22L3.48,89.22L3.48,89.22z M61.17,7.68c3.58-3.73,6.08-6.96,11.6-7.59C83.12-1.1,92.64,9.5,87.41,19.94c-0.24,0.49-0.53,0.99-0.85,1.5h20.91 c2.38,0,4.54,0.97,6.11,2.54c1.57,1.57,2.54,3.73,2.54,6.11v43.17c1.14,0.65,2.17,1.43,3.07,2.33c2.2,2.2,3.57,5.09,3.57,8.55v6.19 c0.08,0.2,0.12,0.41,0.12,0.63s-0.04,0.44-0.12,0.63v27.9c0,0.96-0.78,1.74-1.74,1.74h-4.38c-0.82,0-1.5-0.56-1.69-1.33 c-1.64-4.71-3.28-7.43-5.51-8.91c-2.26-1.5-5.33-1.88-9.77-1.87l-80.23,0.1l-0.03,0v0c-3.29-0.08-5.42,0.87-6.97,2.59 c-1.68,1.88-2.82,4.74-3.98,8.22c-0.24,0.73-0.92,1.19-1.65,1.19v0.01H1.74c-0.96,0-1.74-0.78-1.74-1.74V82.96 c0-3.15,1.24-5.76,3.24-7.75c0.61-0.61,1.28-1.15,2.02-1.64V30c0-2.38,0.97-4.51,2.54-6.06c1.57-1.55,3.73-2.5,6.11-2.5v0h22.3 c-1.29-2.56-2.11-5.24-2.21-8.06C33.71,5.25,40.12,0.04,47.5,0.14C54.1,0.22,56.87,3.5,61.17,7.68L61.17,7.68L61.17,7.68z M84.03,24.92c-1.33,1.63-2.87,3.32-4.48,4.99c-3.68,3.81-7.75,7.54-10.6,10.37l-7.78,7.71l-6.42-6.19 C49.76,37,42.75,31.4,38.29,24.92H13.91c-1.44,0-2.74,0.57-3.67,1.49C9.31,27.32,8.74,28.58,8.74,30v41.85 c0.92-0.32,1.87-0.57,2.85-0.75c1.48-0.26,2.97-0.52,4.46-0.76V59.48c0-3.14,1.28-6,3.35-8.06c2.07-2.07,4.92-3.35,8.06-3.35H47.4 c3.14,0,6,1.28,8.06,3.35c2.07,2.07,3.35,4.92,3.35,8.06v7.12c0.56-0.01,1.12-0.01,1.69-0.01c0.4,0,0.8,0,1.2,0v-7.1 c0-3.14,1.28-6,3.35-8.06c2.07-2.07,4.92-3.35,8.06-3.35h19.94c3.14,0,6,1.28,8.06,3.35c2.07,2.07,3.35,4.92,3.35,8.06v10.74 c1.83,0.28,3.67,0.57,5.51,0.88c0.91,0.15,1.8,0.37,2.66,0.64V30.09c0-1.42-0.58-2.71-1.52-3.65c-0.94-0.94-2.23-1.52-3.65-1.52 l0,0H84.03L84.03,24.92z M43.12,67.28c4.07-0.31,8.14-0.51,12.21-0.62v-7.18c0-2.18-0.89-4.16-2.33-5.6 c-1.44-1.44-3.42-2.33-5.6-2.33H27.46c-2.18,0-4.16,0.89-5.6,2.33c-1.44,1.44-2.33,3.42-2.33,5.6V69.8 c3.6-0.53,7.21-0.99,10.83-1.38c1.46-0.17,2.95-0.33,4.49-0.48C37.5,67.68,40.28,67.46,43.12,67.28L43.12,67.28L43.12,67.28z M65.19,66.61c2.68,0.04,5.36,0.12,8.05,0.25c4.34,0.15,8.56,0.4,12.53,0.74c5.61,0.49,10.79,1.18,15.23,2.08v-10.2 c0-2.18-0.89-4.16-2.33-5.6c-1.44-1.44-3.42-2.33-5.6-2.33H73.12c-2.18,0-4.16,0.89-5.6,2.33c-1.44,1.44-2.33,3.42-2.33,5.6 L65.19,66.61L65.19,66.61L65.19,66.61z M119.28,92.7H3.48v25.05h2.09c1.17-3.35,2.41-6.16,4.28-8.25c2.22-2.48,5.18-3.85,9.62-3.75 l80.2-0.1c5.12-0.01,8.75,0.48,11.69,2.44c2.73,1.82,4.7,4.79,6.51,9.66h1.42V92.7L119.28,92.7L119.28,92.7z"
    )
    return svg

  def heartbeat(self, fill=None, border=None, width=(30, "px"), height=(30, "px")):
    """

    https://uxwing.com/heartbeat-icon/

    :param fill:
    :param border:
    :param width:
    :param height:
    """
    svg = self.parent.context.rptObj.ui.pictos.path(fill=fill, stroke=border, width=width, height=height,
       path="M114.41,36.28c4.68,0,8.47,3.79,8.47,8.47c0,4.67-3.79,8.47-8.47,8.47c-2.88,0-5.42-1.44-6.95-3.63l-14.19,0 L78.23,90.37l-9.27,0.02L40.88,15.35L27.9,46.55l-1.27,3.06L0,49.61V39.7h20.04L36.55,0l9.19,0.17l27.8,74.3l11.63-31.52l1.19-3.23 h21.23C109.14,37.64,111.61,36.28,114.41,36.28L114.41,36.28L114.41,36.28z"
    )
    return svg
