#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import base64

from typing import List, Union
from epyk.core import html
from epyk.core.py import types
from epyk.core.css import Colors
from epyk.interfaces import Arguments


class Images:

  def __init__(self, ui):
    self.page = ui.page

  def img(self, image: str = None, path: str = None, width: types.SIZE_TYPE = (100, "%"),
          height: types.SIZE_TYPE = (None, "px"), align: str = "center", html_code: str = None,
          profile: types.PROFILE_TYPE = None, tooltip: str = None,
          options: types.OPTION_TYPE = None) -> html.HtmlImage.Image:
    """  
    Add an HTML image to the page. The path can be defined either in a absolute or relative format.

    Tip: The absolute format does not work on servers. It is recommended to use relative starting to the root of the
    server.

    :tags:
    :categories:

    Usage::

      page.ui.img("epykIcon.PNG", path=r"../../../static/images", height=(50, "px"))

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlImage.Image`

    Related Pages:

      https://www.w3schools.com/bootstrap/bootstrap_ref_css_images.asp
      https://www.w3schools.com/cssref/css3_pr_border-radius.asp

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/image.py

    :param image: Optional. The image file name
    :param path: Optional. Optional. The image file path
    :param width: Optional. Optional. The component width in pixel or percentage
    :param height: Optional. Optional. The component height in pixel or percentage
    :param align: Optional. A string with the horizontal position of the component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    :param tooltip: Optional. A string with the value of the tooltip
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    if height[0] not in [None, 'auto'] and width[1] == '%':
      width = ("auto", '')
    html_image = html.HtmlImage.Image(self.page, self.page.py.encode_html(image),
                                      self.page.py.encode_html(path), align, html_code, width, height,
                                      profile, options or {})
    if tooltip is not None:
      html_image.tooltip(tooltip)
    if width[0] is None:
      html_image.style.css.max_width = '100%'
    html.Html.set_component_skin(html_image)
    return html_image

  def figure(self, image: str = None, caption: str = None, path: str = None, width: types.SIZE_TYPE = (100, "%"),
             height: types.SIZE_TYPE = (None, "px"), align: str = "center",
             html_code: str = None, profile: types.PROFILE_TYPE = None, tooltip: str = None,
             options: types.OPTION_TYPE = None) -> html.HtmlImage.Figure:
    """  
    Display a picture as a figure component with an attached caption object.

    :tags:
    :categories:

    Related Pages:

      https://www.w3schools.com/tags/tag_figcaption.asp

    Usage::

      page.ui.images.figure("33c33735-8a1e-4bef-8201-155b4775304a.jpg", "test caption",
        path=picture_path, width=(100, 'px'))

    :param image: Optional. The url path of the image
    :param caption: Optional.
    :param path: Optional. The image file path
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param align: Optional. A string with the horizontal position of the component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    :param tooltip: Optional. A string with the value of the tooltip
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    container = html.HtmlImage.Figure(self.page, [], None, None, width, None, height, False, align, None,
                                      html_code, "figure", None, options or {}, profile)
    container.img = self.page.ui.img(
      image=image, path=path, width=(100, "%"), height=(None, "px"), align="center", html_code=html_code,
      profile=profile, tooltip=tooltip, options=options)
    container.add(container.img)
    if caption is not None:
      container.caption = self.page.ui.tags.figcaption(caption)
      container.add(container.caption)
    if width[0] == 'auto':
      container.style.css.display = "inline-block"
    html.Html.set_component_skin(container)
    return container

  def container(self, components: List[html.Html.Html], max_width: types.SIZE_TYPE = (900, 'px'),
                align: str = "center",
                profile: types.PROFILE_TYPE = None,
                options: types.OPTION_TYPE = None) -> html.HtmlContainer.Div:
    """  
    Empty container for images.

    :tags:
    :categories:

    Usage::

    :param components: List of HTML Component. internal components
    :param max_width: Optional. The maximum width for this container
    :param align: Optional. A string with the horizontal position of the component
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    max_width = Arguments.size(max_width, unit="%")
    container = self.page.ui.div(components, profile=profile, options=options)
    container.style.css.max_width = max_width[0]
    container.style.css.text_align = align
    if align == 'center':
      container.style.css.margin = "0 auto"
    html.Html.set_component_skin(container)
    return container

  def background(self, url: str, width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (300, "px"),
                 size: str = "cover", margin: int = 0, align: str = "center",
                 html_code: str = None, position: str = "middle", profile: types.PROFILE_TYPE = None,
                 options: types.OPTION_TYPE = None) -> html.HtmlContainer.Div:
    """  
    Add a background image.

    :tags:
    :categories:

    Usage::

    :param url: Optional. The link to the gallery
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param size: Optional. The type of background in
    :param margin: Optional. The CSS margin properties are used to create space around elements, outside of any defined
      borders
    :param align: Optional. A string with the horizontal position of the component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param position: Optional. A string with the vertical position of the component
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    div = self.page.ui.div(
      height=Arguments.size(height, "px"), width=Arguments.size(width), html_code=html_code, options=options,
      profile=profile)
    div.style.css.background_url(self.page.py.encode_html(url), size=size, margin=margin)
    div.style.css.display = "block"
    div.style.css.text_align = align
    div.style.css.vertical_align = position
    div.style.css.padding = "auto"
    html.Html.set_component_skin(div)
    return div

  def wallpaper(self, url: str = None, width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (100, "%"),
                size: str = "cover", margin: int = 0, align: str = "center",
                html_code: str = None, position: str = "middle", profile: types.PROFILE_TYPE = None,
                options: types.OPTION_TYPE = None) -> html.HtmlImage.Background:
    """  

    :tags: Background
    :categories:

    Usage::

    :param url: Optional. The link to the gallery
    :param width: Optional. Tuple. The component width in pixel or percentage
    :param height: Optional. Tuple. The component height in pixel or percentage
    :param size: Optional. The type of background in
    :param margin: Optional. The CSS margin properties are used to create space around elements,
      outside of any defined borders
    :param align: Optional. The text-align property within this component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param position: Optional. The position compared to the main component tag
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    options = options or {}
    div = html.HtmlImage.Background(self.page, [], label=None, color=None, width=Arguments.size(width),
                                    icon=None, height=Arguments.size(height), editable=False, align='left',
                                    padding=None, html_code=html_code, tag='div', helper=None, options=options,
                                    profile=profile)
    div.style.css.background_url(self.page.py.encode_html(url) if url is not None else None, size=size,
                                 margin=margin)
    div.style.css.background_position = "center center"
    div.style.css.display = "block"
    div.style.css.text_align = align
    div.style.css.vertical_align = position
    div.style.css.padding = "auto"
    self.page.body.style.css.height = "100%"
    html.Html.set_component_skin(div)
    return div

  def logo(self, url: str, width: types.SIZE_TYPE = (160, "px"), height: types.SIZE_TYPE = (60, "px"),
           top: types.SIZE_TYPE = (16, "px"), left: types.SIZE_TYPE = (16, "px"), profile: types.PROFILE_TYPE = None,
           options: types.OPTION_TYPE = None) -> html.HtmlContainer.Div:
    """  

    :tags:
    :categories:


    Usage::

    :param url: Optional. The link to the gallery
    :param width: Optional. The component width in pixel or percentage
    :param height: Optional. The component height in pixel or percentage
    :param top: Optional. A tuple with the integer for the component's distance to the top of the page
    :param left: Optional. A tuple with the integer for the component's distance to the left of the page
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    top = Arguments.size(top, 'px')
    left = Arguments.size(left, 'px')
    div = self.page.ui.div(
      height=Arguments.size(height, 'px'), width=Arguments.size(width), options=options, profile=profile)
    div.style.css.background_url(url)
    div.style.css.display = "block"
    div.style.css.position = "absolute"
    div.style.css.top = "%s%s" % (top[0], top[1])
    div.style.css.left = "%s%s" % (left[0], left[1])
    div.style.css.text_align = "center"
    div.style.css.vertical_align = "middle"
    div.style.css.padding = "auto"
    html.Html.set_component_skin(div)
    return div

  def youtube(self, video_id: str = None, width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (None, "px"),
              align: str = "center", html_code: str = None, profile: types.PROFILE_TYPE = None,
              options: types.OPTION_TYPE = None) -> html.HtmlImage.Image:
    """  
    Get teh picture used by youtube.

    :tags:
    :categories:

    Usage::

    :param video_id: Optional. The youtube video ID
    :param width: Optional. The component width in pixel or percentage
    :param height: Optional. The component height in pixel or percentage
    :param align: Optional. A string with the horizontal position of the component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    component = self.img(
      "0.jpg", "http://img.youtube.com/vi/%s" % video_id, Arguments.size(width),
      Arguments.size(height, 'px'), align, html_code, profile, options)
    html.Html.set_component_skin(component)
    return component

  def circular(self, image: str = None, path: str = None, width: types.SIZE_TYPE = (200, "px"),
               height: types.SIZE_TYPE = (200, "px"), align: str = "center", html_code: str = None,
               profile: types.PROFILE_TYPE = None,
               options: types.OPTION_TYPE = None) -> html.HtmlImage.Image:
    """  
    Add an HTML image to the page. The path can be defined either in a absolute or relative format.

    Tip: The absolute format does not work on servers. It is recommended to use relative starting to the root of
    the server.

    :tags:
    :categories:

    Usage::

      page.ui.circular("epykIcon.PNG", path=r"../../../static/images", height=(50, "px"))

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlImage.Image`

    Related Pages:

      https://www.w3schools.com/bootstrap/bootstrap_ref_css_images.asp
      https://www.w3schools.com/cssref/css3_pr_border-radius.asp

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/image.py

    :param image: Optional. The image file name
    :param path: Optional. String. The image file path
    :param width: Optional. Tuple. The component width in pixel or percentage
    :param height: Optional. Tuple. The component height in pixel or percentage
    :param align: Optional. A string with the horizontal position of the component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    if height[0] is not None and width[1] == '%':
      width = ("auto", '')
    html_image = html.HtmlImage.Image(self.page, image, path, align, html_code, width, height, profile,
                                      options or {})
    # add the css styles
    html_image.style.css.padding = 5
    html_image.style.css.borders_light()
    html_image.style.css.border_radius = width[0]
    html.Html.set_component_skin(html_image)
    return html_image

  def avatar(self, text: str = "", image: str = None, path: str = None, status: str = None,
             width: types.SIZE_TYPE = (30, "px"), height: types.SIZE_TYPE = (30, "px"), align: str = "center",
             html_code: str = None, profile: types.PROFILE_TYPE = None, menu: html.Html.Html = None,
             options: types.OPTION_TYPE = None) -> html.HtmlContainer.Div:
    """
    Generate or load an avatar.

    :tags:
    :categories:

    Usage::

      page.ui.images.avatar("Epyk", status='out')
      page.ui.images.avatar(image="epykIcon.PNG", path=config.IMG_PATH, status=False)

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Div`
      - :class:`epyk.core.html.HtmlImage.Image`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/image.py

    :param text: Optional. The value to be displayed to the component
    :param image: Optional. The url of the image
    :param path: Optional. String. The image file path
    :param status: Optional. The avatar status code. Default no status
    :param width: Optional. Tuple. The component width in pixel or percentage
    :param height: Optional. Tuple. The component height in pixel or percentage
    :param align: Optional. A string with the horizontal position of the component
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, "px")
    height = Arguments.size(height, "px")
    options = options or {}
    status_map = {
      True: self.page.theme.success.base,
      'available': self.page.theme.success.base,
      False: self.page.theme.danger.base,
      'busy': self.page.theme.danger.base,
      'out': self.page.theme.warning.base
    }

    bgcolor, margin_top = None, "-20%"
    if image is not None:
      img = self.img(image, path, (width[0]-5, width[1]), (height[0]-5, height[1]), align="center", html_code=html_code,
                     profile=profile, options=options)
      img.style.css.border_radius = width[0]
      img.style.css.margin = 2
      margin_top = -8
    else:
      if not text:
        text = "anonymous"
      bgcolor = Colors.randColor(self.page.py.hash(text))
      img = self.page.ui.layouts.div(text[0].upper())
      img.style.css.line_height = width[0] - 5
      img.style.css.color = "white"
      img.style.css.font_size = width[0]
      img.style.css.font_weight = 'bold'
      img.style.css.padding = 0
    img.style.css.middle()
    if options.get('status', True):
      status_o = self.page.ui.layouts.div("&nbsp;", width=(30, "%"), height=(30, "%"))
      status_o.style.css.position = 'relative'

      status_o.style.css.background_color = status_map.get(status, self.page.theme.greys[5])
      status_o.style.css.border_radius = 30
      status_o.style.css.margin_top = margin_top
      status_o.style.css.float = 'right'

      div = self.page.ui.layouts.div([img, status_o], width=width, height=height)
      div.status = status_o
    else:
      div = self.page.ui.layouts.div([img], width=width, height=height)
    if bgcolor is not None:
      img.style.css.background_color = bgcolor
      img.style.css.text_stoke = "1px %s" % bgcolor
    img.style.css.borders_light()
    img.style.css.border_radius = width[0]
    div.img = img

    def add_menu(menu_item: Union[html.Html.Html, list]):
      if isinstance(menu_item, list):
        menu_item = self.page.ui.div(menu_item, width="auto")
      menu_item.style.css.position = "absolute"
      menu_item.style.css.display = "None"
      menu_item.style.css.line_height = "normal"
      menu_item.style.css.border = "1px solid %s" % self.page.theme.greys[4]
      menu_item.style.css.border_radius = 5
      menu_item.style.css.background_color = self.page.theme.dark_or_white()
      menu_item.style.css.min_height = 20
      menu_item.style.css.margin_top = 10
      menu_with = Arguments.size(menu_item.style.css.width)
      menu_item.style.css.right = 2
      menu_item.style.css.padding = 3
      menu_item.style.css.z_index = 600
      div.__add__(menu_item)
      div.style.css.position = "relative"
      div.img.click([menu_item.dom.toggle()])
      div.menu = menu_item

    div.add_menu = add_menu
    div.img = img
    if align == 'center':
      div.style.css.margin = "auto"
      div.style.css.display = "block"
    html.Html.set_component_skin(div)
    return div

  def section(self, image: str, name: str, title: str, text: str, url: str = None, path: str = None,
              width: types.SIZE_TYPE = (200, "px"), height: types.SIZE_TYPE = (200, "px"),
              profile: types.PROFILE_TYPE = None,
              options: types.OPTION_TYPE = None) -> html.HtmlContainer.Div:
    """  

    :tags:
    :categories:

    Usage::

      page.ui.images.section("epykIcon.PNG", "# Test", "Epyk Test", 'This is a test', path=r"../../../static/images")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Div`
      - :class:`epyk.core.html.HtmlText.Span`
      - :class:`epyk.core.html.HtmlText.Paragraph`
      - :class:`epyk.core.html.HtmlText.Title`
      - :class:`epyk.core.html.HtmlImage.Image`

    :param image: The url of the image
    :param name: The name of the image
    :param title: Optional. A panel title. This will be attached to the title property
    :param text: Optional. The value to be displayed to the component
    :param url: Optional. The link to the gallery
    :param path: Optional. The image file path
    :param width: Optional. The component width in pixel or percentage
    :param height: Optional. The component height in pixel or percentage
    :param profile: Optional. A flag to set the component performance storage
    :param options: Optional. Specific Python options available for this component
    """
    width = Arguments.size(width, "px")
    height = Arguments.size(height, "px")
    img = self.img(image, width=(width[0]-10, 'px'), height=(100, "px"), path=path, options=options, profile=profile)
    title = self.page.ui.title(title, level=2, options=options)
    highlight = self.page.ui.texts.span(name, width=(50, "px"), height=(20, 'px'), options=options, profile=profile)
    paragraph = self.page.ui.texts.paragraph(text, options=options)
    div = self.page.ui.layouts.div([
      highlight, img, title, paragraph], width=width, height=height, options=options, profile=profile)
    highlight.css({"position": "absolute", 'left': 0, "background-color": self.page.theme.colors[-1],
                   "color": self.page.theme.greys[0], 'padding': "0 2px"})
    div.style.css.margin = 2
    div.img = img
    div.title = title
    if url is not None:
      div.style.css.cursor = 'pointer'
      div.click([self.page.js.location.href(url)])
    div.style.add_classes.div.border_bottom()
    html.Html.set_component_skin(div)
    return div

  def animated(self, image: str = "", text: str = "", title: str = "", url: str = None, path: str = None,
               width: types.SIZE_TYPE = (200, "px"), height: types.SIZE_TYPE = (200, "px"),
               html_code: str = None, options: types.OPTION_TYPE = None,
               profile: types.PROFILE_TYPE = None) -> html.HtmlImage.AnimatedImage:
    """  
    Advance image with mask and gallery link.
    This will display some details when the mouse is on the container.

    :tags:
    :categories:

    Usage::

      c = page.ui.images.animated("epykIcon.PNG", text="This is a comment", title="Title", url="#")
      c.style.css.borders()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlImage.AnimatedImage`

    Related Pages:

      https://tympanus.net/Tutorials/OriginalHoverEffects/

    :param image: Optional. The image file name
    :param text: Optional. String. The image file path
    :param title: Optional. The image title displayed in to the mask on mouse hover the container
    :param url: Optional. The link to the gallery
    :param path: Optional. String. The image file path
    :param width: Optional. Tuple. The component width in pixel or percentage
    :param height: Optional. Tuple. The component height in pixel or percentage
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, "px")
    height = Arguments.size(height, "px")
    component = html.HtmlImage.AnimatedImage(
      self.page, image, text, title, html_code, url, path, width, height, options, profile)
    html.Html.set_component_skin(component)
    return component

  def carousel(self, images: list = None, path: str = None, selected: int = 0, width: types.SIZE_TYPE = (100, "%"),
               height: types.SIZE_TYPE = (300, "px"), options: types.OPTION_TYPE = None,
               profile: types.PROFILE_TYPE = None) -> html.HtmlImage.ImgCarousel:
    """  
    Carousel component for pictures.

    :tags:
    :categories:

    Usage::

      car = page.ui.images.carousel(["epykIcon.PNG", "epyklogo.ico", "epyklogo_whole_big.png"],
                                 path=r"../../../static/images", height=(200, 'px'))
      car.click([page.js.console.log('data', skip_data_convert=True)])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlImage.ImgCarousel`

    Related Pages:

      https://www.cssscript.com/basic-pure-css-slideshow-carousel/

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/image.py

    :param images: Optional. With the different picture file names
    :param path: Optional. The common path for the pictures
    :param width: Optional. Tuple. The component width in pixel or percentage
    :param height: Optional. Tuple. The component height in pixel
    :param selected: Optional. The selected item index
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width)
    height = Arguments.size(height, "px")
    if height[1] == '%':
      raise ValueError("This height cannot be in percentage")

    component = html.HtmlImage.ImgCarousel(
      self.page, images or [], path, selected, width, height, options or {}, profile)
    html.Html.set_component_skin(component)
    return component

  def emoji(self, symbol: str = None, top: types.SIZE_TYPE = (20, 'px'), options: types.OPTION_TYPE = None,
            profile: types.PROFILE_TYPE = None, html_code: str = None) -> html.HtmlImage.Emoji:
    """  

    :tags:
    :categories:

    Usage::

      page.ui.images.emoji(page.symbols.smileys.DISAPPOINTED_FACE)

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlImage.Emoji`

    Related Pages:

      https://github.com/wedgies/jquery-emoji-picker

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/image.py

    :param symbol: Optional. The emoji code
    :param top: Optional. The number of pixel from the top of the page
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    """
    top = Arguments.size(top, "px")
    component = html.HtmlImage.Emoji(self.page, symbol, top, options, profile, html_code)
    html.Html.set_component_skin(component)
    return component

  def icon(self, icon: str = None, family: str = None, width: types.SIZE_TYPE = (None, 'px'),
           html_code: str = None, height: types.SIZE_TYPE = (None, "px"), color: str = None,
           tooltip: str = None, align: str = "left", options: types.OPTION_TYPE = None,
           profile: types.PROFILE_TYPE = None, badge: str = None) -> html.HtmlImage.Icon:
    """  
    Add an icon to the page.

    :tags:
    :categories:

    Usage::

      page.ui.images.icon("fab fa-angellist")
      icon = page.ui.icon("fab fa-python")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlImage.Icon`

    Related Pages:

      https://fontawesome.com/icons?m=free

    :param icon: Optional. The component icon content from font-awesome references
    :param family: Optional. The Icon framework reference
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param color: Optional. The font color in the component. Default inherit
    :param tooltip: Optional. A string with the value of the tooltip
    :param align: Optional. The text-align property within this component
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, "px")
    height = Arguments.size(height, "px")

    icon_details = self.page.icons.get(icon, family)
    options = options or {}
    options["icon_family"] = family or icon_details["icon_family"]
    component = html.HtmlImage.Icon(
      self.page, icon_details["icon"], width=width, height=height, color=color or 'inherit', tooltip=tooltip,
      options=options, html_code=html_code, profile=profile)
    if width[0] is not None and width[1] == 'px':
      notches = options.get("font-factor", 0)
      component.style.css.font_size = "%s%s" % (width[0]-notches, width[1])
    if align == "center":
      component.style.css.margin = "auto"
      component.style.css.display = "block"
    if badge:
      component.add_badge(badge)
    html.Html.set_component_skin(component)
    return component

  def badge(self, text: str = "", label: str = None, icon: str = None, width: types.SIZE_TYPE = (25, "px"),
            height: types.SIZE_TYPE = (25, "px"), background_color: str = None, html_code: str = None,
            color: str = None, url: str = None, tooltip: str = None, options: types.OPTION_TYPE = None,
            profile: types.PROFILE_TYPE = None) -> html.HtmlImage.Badge:
    """  
    Display a badge component using Bootstrap.

    :tags:
    :categories:

    Usage::

      page.ui.images.badge("Test badge", "Label", icon="fas fa-align-center")
      page.ui.images.badge("This is a badge", background_color="red", color="white")
      page.ui.images.badge(12, icon="far fa-bell", options={"badge_position": 'right'})

      b = page.ui.images.badge(
        7688, icon="fab fa-python", options={'badge_css': {'color': 'white', "background": 'red'}})
      b.options.badge_css = {"background": 'green'}

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlImage.Badge`

    Related Pages:

      https://getbootstrap.com/docs/4.0/components/badge/

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/image.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/links.py

    :param text: Optional. The content of the badge
    :param label: Optional. The label to display close to the badge
    :param icon: Optional. A String with the icon to display from font-awesome
    :param background_color: Optional. The background color of the badge
    :param color: Optional. The text color of the badge
    :param url: Optional. The underlying url link for the badge
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param tooltip: String. Optional, The text to display in the tooltip
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A boolean to store the performances for each components
    """
    width = Arguments.size(width, "px")
    height = Arguments.size(height, "px")
    if background_color is None:
      background_color = self.page.theme.greys[0]
    if color is None:
      color = self.page.theme.success.base
    icon_details = self.page.icons.get(icon, options=options)
    options = options or {}
    options["icon_family"] = icon_details["icon_family"]
    component = html.HtmlImage.Badge(
      self.page, text, width, height, label, icon_details["icon"], background_color, color, url, tooltip, html_code,
      options, profile)
    html.Html.set_component_skin(component)
    return component

  def color(self, code: str, color: str = None, width: types.SIZE_TYPE = (110, 'px'),
            height: types.SIZE_TYPE = (25, 'px'), options: types.OPTION_TYPE = None, helper: str = None,
            profile: types.PROFILE_TYPE = None) -> html.HtmlContainer.Div:
    """  
    Simple vignette to display a color with it is code.

    TODO: Return the hex code of the color when dom.content used

    :tags:
    :categories:

    Usage::

      page.ui.images.color("FFFFFF")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Div`

    :param code: The color code
    :param color: Optional. The font color
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param helper: Optional. A tooltip helper
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, "px")
    height = Arguments.size(height, "px")
    div = self.page.ui.div(code, width=width, height=height, options=options, helper=helper, profile=profile)
    div.style.css.background_color = code
    div.style.css.line_height = "%s%s" % (height[0], height[1])
    div.style.css.color = color or self.page.theme.greys[0]
    div.style.css.text_align = "center"
    div.style.css.border = "1px solid black"
    div.style.css.vertical_align = "middle"
    html.Html.set_component_skin(div)
    return div

  def gallery(self, images: List[Union[dict, html.Html.Html]] = None, columns: int = 6,
              width: types.SIZE_TYPE = (None, '%'), height: types.SIZE_TYPE = ('auto', ''),
              options: types.OPTION_TYPE = None,
              profile: types.PROFILE_TYPE = None) -> html.HtmlContainer.Grid:
    """  
    Mosaic of pictures.

    :tags:
    :categories:

    Usage::

    Related Pages:

    Underlying HTML Objects:

    Templates:

    :param images: Optional. The list with the pictures
    :param columns: Optional. The number of column for the mosaic component
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    dflt_options = {}
    if options is not None:
      dflt_options.update(options)
    grid = self.page.ui.grid(width=width, height=height, options=dflt_options, profile=profile)
    grid.style.css.margin_top = 20
    grid.style.css.overflow = 'hidden'
    grid.style.css.margin_bottom = 20
    row = self.page.ui.row(options=dflt_options)
    grid.images = []
    grid.texts = {}
    for i, image in enumerate(images):
      if dflt_options.get("max") is not None and len(grid.images) > dflt_options.get("max"):
        break

      if i % columns == 0:
        grid.add(row)
        row = self.page.ui.row(options=dflt_options)
      text = None
      if not hasattr(image, 'options'):
        if isinstance(image, dict):
          if 'htmlCode' not in image:
            image["htmlCode"] = "%s_%s" % (grid.htmlCode, i)
          if 'align' not in image:
            image['align'] = "center"
          if "text" in image:
            text = self.page.ui.text(image["text"], options=dflt_options)
            text.style.css.bold()
            text.style.css.white_space = "nowrap"
            grid.texts[i] = text
            del image["text"]

          image = self.page.ui.img(**image)
        else:
          image = self.page.ui.img(image, html_code="%s_%s" % (grid.htmlCode, i), align="center")
        image.style.css.font_factor(15)
        image.style.add_classes.div.border_hover()
        image.style.css.text_align = "center"
        grid.images.append(image)
      if text is not None:
        text.style.css.display = "inline-block"
        text.style.css.width = "100%"
        text.style.css.text_align = "center"
        row.add(self.page.ui.col([image, text], align="center", options=dflt_options))
      else:
        row.add(image)
      row.attr["class"].add("mt-3")
      for r in row:
        r.attr["class"].add("px-1")
      image.parent = row[-1]
    if len(row):
      for i in range(columns - len(row)):
        row.add(self.page.ui.text("&nbsp;"))
      for r in row:
        r.attr["class"].add("px-1")
      row.attr["class"].add("mt-3")
      grid.add(row)
    grid.style.css.color = self.page.theme.greys[6]
    return grid

  def epyk(self, align: str = "center", width: types.SIZE_TYPE = (None, '%'), height: types.SIZE_TYPE = ('auto', ''),
           html_code: str = None, profile: types.PROFILE_TYPE = None, tooltip: str = None,
           options: types.OPTION_TYPE = None
           ):
    """  
    Add the Epyk Icon.

    Usage::

      page.ui.icons.epyk()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlImage.Image`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/image.py

    :param align: Optional. A string with the horizontal position of the component.
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    :param tooltip: Optional. A string with the value of the tooltip
    :param options: Optional. Specific Python options available for this component
    """
    with open(os.path.join(os.path.abspath(
      os.path.dirname(__file__)), "..", "..", "static", "images", "epykIcon.PNG"), "rb") as fp:
      base64_bytes = base64.b64encode(fp.read())
      base64_message = base64_bytes.decode('ascii')
      img = "data:image/x-icon;base64,%s" % base64_message
    icon = self.page.ui.img(img, align=align, width=width, height=height, html_code=html_code, profile=profile,
                            tooltip=tooltip, options=options)
    icon.css({"text-align": "center", "padding": "auto", "vertical-align": "middle"})
    html.Html.set_component_skin(icon)
    return icon
