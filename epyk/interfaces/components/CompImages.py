#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core import html
from epyk.core.css import Colors
from epyk.interfaces import Arguments


class Images(object):

  def __init__(self, context):
    self.context = context

  def img(self, image=None, path=None, width=(100, "%"), height=(None, "px"), align="center", htmlCode=None,
          profile=None, tooltip=None, options=None):
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
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    if height[0] not in [None, 'auto'] and width[1] == '%':
      width = ("auto", '')
    html_image = html.HtmlImage.Image(self.context.rptObj, image, path, align, htmlCode, width, height, profile, options or {})
    if tooltip is not None:
      html_image.tooltip(tooltip)
    if width[0] is None:
      html_image.style.css.max_width = '100%'
    return html_image

  def container(self, component, max_width=(900, 'px'), align="center", profile=None, options=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param component:
    :param max_width:
    :param align:
    :param profile:
    :param options:
    """
    max_width = Arguments.size(max_width, unit="%")
    container = self.context.rptObj.ui.div(component, profile=profile, options=options)
    container.style.css.max_width = max_width[0]
    container.style.css.text_align = align
    if align == 'center':
      container.style.css.margin = "0 auto"
    return container

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
    div = self.context.rptObj.ui.div(height=Arguments.size(height, "px"), width=Arguments.size(width))
    div.style.css.background_url(url, size=size, margin=margin)
    div.style.css.display = "block"
    div.style.css.text_align = align
    div.style.css.vertical_align = position
    div.style.css.padding = "auto"
    return div

  def wallpaper(self, url, width=(100, "%"), height=(100, "%"), size="cover", margin=0, align="center", position="middle"):
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
    div = self.context.rptObj.ui.div(height=Arguments.size(height), width=Arguments.size(width))
    div.style.css.background_url(url, size=size, margin=margin)
    div.style.css.background_position = "center center"
    div.style.css.display = "block"
    div.style.css.text_align = align
    div.style.css.vertical_align = position
    div.style.css.padding = "auto"
    self.context.rptObj.body.style.css.height = "100%"
    return div

  def logo(self, url, width=(160, "px"), height=(60, "px"), top=(16, "px"), left=(16, "px")):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param url:
    :param width:
    :param height:
    :param top:
    :param left:
    """
    top = Arguments.size(top, 'px')
    left = Arguments.size(left, 'px')
    div = self.context.rptObj.ui.div(height=Arguments.size(height, 'px'), width=Arguments.size(width))
    div.style.css.background_url(url)
    div.style.css.display = "block"
    div.style.css.position = "absolute"
    div.style.css.top = "%s%s" % (top[0], top[1])
    div.style.css.left = "%s%s" % (left[0], left[1])
    div.style.css.text_align = "center"
    div.style.css.vertical_align = "middle"
    div.style.css.padding = "auto"
    return div

  def youtube(self, video_id=None, width=(100, "%"), height=(None, "px"), align="center", htmlCode=None, profile=None, options=None):
    """
    Description:
    ------------
    Get teh picture used by youtube

    Attributes:
    ----------
    :param video_id:
    :param width:
    :param height:
    :param align:
    :param htmlCode:
    :param profile:
    :param options:
    """
    return self.img("0.jpg", "http://img.youtube.com/vi/%s" % video_id, Arguments.size(width), Arguments.size(height, 'px'), align, htmlCode, profile, options)

  def circular(self, image=None, path=None, width=(100, "%"), height=('auto', ""), align="center", htmlCode=None,
          profile=None, options=None):
    """
    Description:
    ------------
    Add an HTML image to the page. The path can be defined either in a absolute or relative format.

    Tip: The absolute format does not work on servers. It is recommended to use relative starting to the root of the server

    Usage::

      rptObj.ui.circular("epykIcon.PNG", path=r"../../../static/images", height=(50, "px"))

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
    width = Arguments.size(width)
    height = Arguments.size(height)
    if height[0] is not None and width[1] == '%':
      width = ("auto", '')
    html_image = html.HtmlImage.Image(self.context.rptObj, image, path, align, htmlCode, width, height, profile, options or {})
    # add the css styles
    html_image.style.css.padding = 5
    html_image.style.css.borders_light()
    html_image.style.css.border_radius = 50
    return html_image

  def avatar(self, text=None, image=None, path=None, status=None, width=(30, "px"), height=(30, "px"), align="center", htmlCode=None,
               profile=None, options=None):
    """
    Description:
    ------------
    Generate or load an avatar

    Usage::

      rptObj.ui.images.avatar("Epyk", status='out')
      rptObj.ui.images.avatar(image="epykIcon.PNG", path=config.IMG_PATH, status=False)

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Div`
      - :class:`epyk.core.html.HtmlImage.Image`

    Attributes:
    ----------
    :param image:
    :param path:
    :param width:
    :param height:
    :param align:
    :param htmlCode:
    :param profile:
    :param options:
    """
    width = Arguments.size(width, "px")
    height = Arguments.size(height, "px")
    options = options or {}
    status_map = {
      True: self.context.rptObj.theme.success[1],
      'available': self.context.rptObj.theme.success[1],
      False: self.context.rptObj.theme.danger[1],
      'busy': self.context.rptObj.theme.danger[1],
      'out': self.context.rptObj.theme.warning[1]
    }

    bgcolor, margin_top = None, -5
    if image is not None:
      img = self.img(image, path, (width[0]-5, width[1]), (height[0]-5, height[1]), align, htmlCode, profile, options)
      img.style.css.border_radius = 50
      img.style.css.margin = 2
      margin_top = -8
    else:
      bgcolor = Colors.randColor(self.context.rptObj.py.hash(text))
      img = self.context.rptObj.ui.layouts.div(text[0].upper())
      img.style.css.line_height = width[0] - 5
      img.style.css.color = "white"
      img.style.css.font_size = width[0]
      img.style.css.font_weight = 'bold'
      img.style.css.padding = 0
    img.style.css.middle()
    if options.get('status', True):
      status_o = self.context.rptObj.ui.layouts.div("&nbsp;", width=(10, "px"), height=(10, "px"))
      status_o.style.css.position = 'relative'

      status_o.style.css.background_color = status_map.get(status, self.context.rptObj.theme.greys[5])
      status_o.style.css.border_radius = 10
      status_o.style.css.margin_top = margin_top
      status_o.style.css.float = 'right'

      div = self.context.rptObj.ui.layouts.div([img, status_o], width=width, height=height)
      div.status = status_o
    else:
      div = self.context.rptObj.ui.layouts.div([img], width=width, height=height)
    if bgcolor is not None:
      div.style.css.background_color = bgcolor
      div.style.css.text_stoke = "1px %s" % bgcolor
    div.style.css.borders_light()
    div.style.css.border_radius = 50
    div.img = img
    return div

  def section(self, image, name, title, text, url=None, path=None, width=(200, "px"), height=(200, "px")):
    """
    Description:
    ------------

    Usage::

      rptObj.ui.images.section("epykIcon.PNG", "# Test", "Epyk Test", 'This is a test', path=r"../../../static/images")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Div`
      - :class:`epyk.core.html.HtmlText.Span`
      - :class:`epyk.core.html.HtmlText.Paragraph`
      - :class:`epyk.core.html.HtmlText.Title`
      - :class:`epyk.core.html.HtmlImage.Image`

    Attributes:
    ----------
    :param image:
    :param name:
    :param title:
    :param text:
    :param url:
    :param path:
    :param width:
    :param height:
    """
    width = Arguments.size(width, "px")
    height = Arguments.size(height, "px")
    img = self.img(image, width=(width[0]-10, 'px'), height=(100, "px"), path=path)
    title = self.context.rptObj.ui.title(title, level=2)
    highlight = self.context.rptObj.ui.texts.span(name, width=(50, "px"), height=(20, 'px'))
    paragraph = self.context.rptObj.ui.texts.paragraph(text)
    div = self.context.rptObj.ui.layouts.div([highlight, img, title, paragraph], width=width, height=height)
    highlight.css({"position": "absolute", 'left': 0, "background-color": self.context.rptObj.theme.colors[-1],
                   "color": self.context.rptObj.theme.greys[0], 'padding': "0 2px"})
    div.style.css.margin = 2
    if url is not None:
      div.style.css.cursor = 'pointer'
      div.click([self.context.rptObj.js.location.href(url)])
    div.style.add_classes.div.border_bottom()
    return div

  def animated(self, image=None, text="", title="", url=None, path=None, width=(200, "px"), height=(200, "px"), options=None, profile=None):
    """
    Description:
    ------------
    Advance image with mask and gallery link.
    This will display some details when the mouse is on the container

    Usage::

      c = rptObj.ui.images.animated("epykIcon.PNG", text="This is a comment", title="Title", url="#", path=r"../../../static/images")
      c.style.css.borders()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlImage.AnimatedImage`

    Related Pages:

      https://tympanus.net/Tutorials/OriginalHoverEffects/

    Attributes:
    ----------
    :param image: String. The image file name
    :param text: Optional. String. The image file path
    :param title: String. The image title displayed in to the mask on mouse hover the container
    :param url: String. The link to the gallery
    :param path: Optional. String. The image file path
    :param width: Optional. Tuple. The component width in pixel or percentage
    :param height: Optional. Tuple. The component height in pixel or percentage
    :param profile:
    """
    width = Arguments.size(width, "px")
    height = Arguments.size(height, "px")
    html_id = html.HtmlImage.AnimatedImage(self.context.rptObj, image, text, title, url, path, width, height, options, profile)
    return html_id

  def carousel(self, images, path=None, selected=0, width=(100, "%"), height=(300, "px"), options=None, profile=None):
    """
    Description:
    ------------
    Carousel component for pictures

    Usage::

      car = rptObj.ui.images.carrousel(["epykIcon.PNG", "epyklogo.ico", "epyklogo_whole_big.png"],
                                 path=r"../../../static/images", height=(200, 'px'))
      car.click([rptObj.js.console.log('data', skip_data_convert=True)])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlImage.ImgCarrousel`

    Related Pages:

      https://www.cssscript.com/basic-pure-css-slideshow-carousel/

    Attributes:
    ----------
    :param images: List. With the different picture file names
    :param path: String. The common path for the pictures
    :param width: Optional. Tuple. The component width in pixel or percentage
    :param height: Optional. Tuple. The component height in pixel
    :param profile:
    """
    width = Arguments.size(width)
    height = Arguments.size(height, "px")
    if height[1] == '%':
      raise Exception("This height cannot be in percentage")

    html_i = html.HtmlImage.ImgCarrousel(self.context.rptObj, images, path, selected, width, height, options or {}, profile)
    return html_i

  def emoji(self, symbole=None, top=(20, 'px'), profile=None):
    """
    Description:
    ------------

    Usage::

      rptObj.ui.images.emoji(rptObj.symbols.smileys.DISAPPOINTED_FACE)

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlImage.Emoji`

    Related Pages:

      https://github.com/wedgies/jquery-emoji-picker

    Attributes:
    ----------
    :param symbole:
    :param top:
    :param profile:
    """
    top = Arguments.size(top, "px")
    html_emoji = html.HtmlImage.Emoji(self.context.rptObj, symbole, top, profile)
    return html_emoji

  def icon(self, icon=None, family=None, width=(None, 'px'), height=(None, "px"), color=None, tooltip=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::

      rptObj.ui.images.icon("fab fa-angellist")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlImage.Icon`

    Related Pages:

      https://fontawesome.com/icons?m=free

    Attributes:
    ----------
    :param icon:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param color:
    :param tooltip:
    :param profile:
    """
    width = Arguments.size(width, "px")
    height = Arguments.size(height, "px")
    options = options or {}
    options['icon_family'] = family or 'font-awesome'
    html_icon = html.HtmlImage.Icon(self.context.rptObj, icon, width=width, height=height, color=color, tooltip=tooltip,
                                    options=options, profile=profile)
    return html_icon

  def badge(self, text="", label=None, icon=None, width=(25, "px"), height=(25, "px"), background_color=None, color=None, url=None,
            tooltip=None, options=None, profile=None):
    """
    Description:
    ------------
    Display a badge component using Bootstrap

    Usage::

      rptObj.ui.images.badge("Test badge", "Label", icon="fas fa-align-center")
      rptObj.ui.images.badge("This is a badge", background_color="red", color="white")
      rptObj.ui.images.badge(12, icon="far fa-bell", options={"badge_position": 'right'})

      b = rptObj.ui.images.badge(7688, icon="fab fa-python", options={'badge_css': {'color': 'white', "background": 'red'}})
      b.options.badge_css = {"background": 'green'}

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlImage.Badge`

    Related Pages:

      https://getbootstrap.com/docs/4.0/components/badge/

    Attributes:
    ----------
    :param text: The content of the badge
    :param label: Optional, The label to display close to the badge
    :param icon: Optional, A String with the icon to display from font-awesome
    :param background_color: Optional, The background color of the badge
    :param color: Optional, The text color of the badge
    :param url:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param tooltip: Optional, The text to display in the tooltip
    :param options:
    :param profile: Optional, A boolean to store the performances for each components
    """
    width = Arguments.size(width, "px")
    height = Arguments.size(height, "px")
    if background_color is None:
      background_color = self.context.rptObj.theme.greys[0]
    if color is None:
      color = self.context.rptObj.theme.success[1]
    html_badge = html.HtmlImage.Badge(self.context.rptObj, text, width, height, label, icon, background_color, color, url,
                                      tooltip, options or {}, profile)
    return html_badge

  def color(self, code, color=None, width=(110, 'px'), height=(25, 'px'), options=None, helper=None, profile=None):
    """
    Description:
    ------------
    Simple vignette to display a color with it is code

     Usage::

      rptObj.ui.images.color("FFFFFF")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Div`

    Attributes:
    ----------
    :param code: String. The color code
    :param color: String. The font color
    :param width: Tuple. The size with its unit
    :param height: Tuple. The size with its unit
    :param options: Dictionary. The object options
    :param helper:
    :param profile:
    """
    width = Arguments.size(width, "px")
    height = Arguments.size(height, "px")
    div = self.context.rptObj.ui.div(code, width=width, height=height, options=options, helper=helper, profile=profile)
    div.style.css.background_color = code
    div.style.css.line_height = "%s%s" % (height[0], height[1])
    div.style.css.color = color or self.context.rptObj.theme.greys[0]
    div.style.css.text_align = "center"
    div.style.css.border = "1px solid black"
    div.style.css.vertical_align = "middle"
    return div
