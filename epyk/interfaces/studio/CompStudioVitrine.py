#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.css import Defaults as Defaults_css
from epyk.core.css.themes import ThemeBlue


class Vitrine(object):

  def __init__(self, context):
    self.parent = context

  def theme(self):
    """
    Description:
    ------------

    """
    self.parent.context.rptObj.theme = ThemeBlue.BlueGrey()

  def button(self, text, icon=None, border=False, background=True, width=('auto', ''), align="center", height=(None, 'px'),
             options=None, profile=False):
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
    button = self.parent.context.rptObj.ui.button(text, icon=icon, width=width, align=align, height=height,
                                                  options=options, profile=profile)
    button.style.clear()
    button.style.css.padding = "0 10px"
    button.style.css.display = "inline-block"
    button.style.css.background = self.parent.context.rptObj.theme.greys[0]
    button.style.css.border_radius = 4
    if border:
      button.style.css.border = '1px solid %s' % self.parent.context.rptObj.theme.greys[4]
    if background:
      button.style.hover({"background": self.parent.context.rptObj.theme.colors[6], "color": self.parent.context.rptObj.theme.greys[0]})
    else:
      button.style.hover({"color": self.parent.context.rptObj.theme.colors[6]})
    return button

  def vignet(self, title, content="", image=None, render="row", align="center", width=(90, '%'), height=(None, "px"), options=None):
    v = self.parent.context.rptObj.ui.vignets.image(title=title, content=content, image=image, render=render, align=align,
                                                     width=width, height=height, options=options)
    return v

  def background(self, url, width=(90, "%"), height=(450, "px"), size="contain", margin=0, align="center", position="middle"):
    b = self.parent.context.rptObj.ui.images.background()
    return b

  def image(self, image, text=None, title=None, url=None, path=None, width=(200, "px"), height=(200, "px"), options=None, profile=None):
    if text is None and title is None:
      return self.parent.context.rptObj.ui.img(image, path=path, width=width, height=height, options=options, profile=profile)

    a = self.parent.context.rptObj.ui.images.animated(image=image, text=text, title=title, url=url, path=path,
                                                      width=width, height=height, options=options, profile=profile)
    a.style.css.border = "1px solid red"
    return a

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
    component.image = self.parent.context.rptObj.ui.img(image, path, (100, '%'), ('auto', ''), align, htmlCode, profile, "", options or {})
    component.style.css.position = "relative"
    component.add(component.image)
    if not hasattr(label, 'options'):
      component.label = self.parent.context.rptObj.ui.div(label)
      component.label.style.css.background = "white"
      component.label.style.css.opacity = 0.6
    else:
      component.label = self.parent.context.rptObj.ui.div()
      component.label.add(label)
    component.label.style.css.position = "absolute"
    component.label.style.css.text_align = "center"
    component.label.style.css.width = "calc(100% - 20px)"
    component.label.style.css.margin = 10
    component.label.style.css.padding = 10
    component.label.style.css.bottom = 5
    component.add(component.label)
    return component

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

  def price(self, value, title, items, align="center", width=(300, 'px'), currency="£"):
    p = self.parent.context.rptObj.ui.vignets.price(value=value, title=title, items=items, align=align, width=width, currency=currency)
    return p

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

  def contact_us(self, title="Contact Us", background=None, width=(100, '%'), align="left", height=(None, 'px'),
                 htmlCode="contactus", options=None, profile=False):
    c = self.parent.context.rptObj.ui.banners.contact_us(title=title, background=background, width=width, align=align,
               height=height, htmlCode=htmlCode, options=options, profile=profile)
    return c

  def disclaimer(self, copyright=None, links=None, width=(100, '%'), height=("auto", ''), align="center", options=None, profile=False):
    d = self.parent.context.rptObj.ui.navigation.disclaimer(copyright=copyright, links=links, width=width, height=height,
                                                            align=align, options=options, profile=profile)
    return d

  def tabs(self, color=None, width=(100, '%'), height=(None, 'px'), htmlCode=None, helper=None, options=None, profile=False):
    t = self.parent.context.rptObj.ui.panels.tabs(color=color, width=width, height=height, htmlCode=htmlCode, helper=helper,
                                                  options=options, profile=profile)
    return t

  def accordion(self, components, title, color=None, align="center", width=(100, "%"), height=(None, "px"), htmlCode=None, helper=None, options=None, profile=False):
    s = self.parent.context.rptObj.ui.panels.sliding(components, title=title, color=color, align=align, width=width,
      height=height, htmlCode=htmlCode, helper=helper, options=options, profile=profile)
    return s

  def card(self, title, content, icon=None, render='row', align="center", width=(200, 'px'), options=None):
    v = self.parent.context.rptObj.ui.vignets.vignet(title=title, content=content, icon=icon, render=render,
                                                     align=align, width=width, options=options)
    return v

  def up(self, icon="fas fa-arrow-up", top=20, right=20, bottom=None, tooltip=None, width=(100, '%'), options=None, profile=False):
    n = self.parent.context.rptObj.ui.navigation.up(icon=icon, top=top, right=right, bottom=bottom, tooltip=tooltip,
                                                    width=width, options=options, profile=profile)
    return n

  def carousel(self):
    pass

  def subscribe(self, value="", placeholder="Enter email address", button="Subscribe", width=(100, '%'),
                height=(None, 'px'), options=None, profile=False):
    s = self.parent.context.rptObj.ui.forms.subscribe(value=value, placeholder=placeholder, button=button, width=width,
                                                      height=height, options=options, profile=profile)
    return s

  def list(self, data=None, color=None, width=('auto', ""), height=(None, 'px'), htmlCode=None, helper=None,
           options=None, profile=None):
    l = self.parent.context.rptObj.ui.lists.list(data=data, color=color, width=width, height=height, htmlCode=htmlCode,
                                                 helper=helper, options=options, profile=profile)
    return l
