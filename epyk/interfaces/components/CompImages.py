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

    Usage:
    -----

      page.ui.img("epykIcon.PNG", path=r"../../../static/images", height=(50, "px"))

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlImage.Image`

    Related Pages:

      https://www.w3schools.com/bootstrap/bootstrap_ref_css_images.asp
      https://www.w3schools.com/cssref/css3_pr_border-radius.asp

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/image.py

    Attributes:
    ----------
    :param image: String. Optional. The image file name.
    :param path: String. Optional. Optional. TString. The image file path.
    :param width: Tuple. Optional. Optional. Tuple. The component width in pixel or percentage.
    :param height: Tuple. Optional. Optional. Tuple. The component height in pixel or percentage.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    if height[0] not in [None, 'auto'] and width[1] == '%':
      width = ("auto", '')
    html_image = html.HtmlImage.Image(self.context.rptObj, self.context.rptObj.py.encode_html(image), self.context.rptObj.py.encode_html(path), align, htmlCode, width, height, profile, options or {})
    if tooltip is not None:
      html_image.tooltip(tooltip)
    if width[0] is None:
      html_image.style.css.max_width = '100%'
    return html_image

  def figure(self, image=None, caption=None, path=None, width=(100, "%"), height=(None, "px"), align="center", htmlCode=None,
          profile=None, tooltip=None, options=None):
    """
    Description:
    ------------
    Display a picture as a figure component with an attached caption object.

    Related Pages:

      https://www.w3schools.com/tags/tag_figcaption.asp

    Usage:
    -----

      page.ui.images.figure("33c33735-8a1e-4bef-8201-155b4775304a.jpg", "test caption", path=picture_path, width=(100, 'px'))

    Attributes:
    ----------
    :param image:
    :param caption:
    :param path: String. Optional. String. The image file path.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    container = html.HtmlImage.Figure(self.context.rptObj, [], None, None, width, None, height, False, align, None, htmlCode, "figure", None, options or {}, profile)
    container.img = self.context.rptObj.ui.img(image=image, path=path, width=(100, "%"), height=(None, "px"), align="center",
                                               htmlCode=htmlCode, profile=profile, tooltip=tooltip, options=options)
    container.add(container.img)
    if caption is not None:
      container.caption = self.context.rptObj.ui.tags.figcaption(caption)
      container.add(container.caption)
    if width[0] == 'auto':
      container.style.css.display = "inline-block"
    return container

  def container(self, components, max_width=(900, 'px'), align="center", profile=None, options=None):
    """
    Description:
    ------------
    Empty container for images.

    Usage:
    -----


    Attributes:
    ----------
    :param components: List of HTML Component. internal components.
    :param max_width: Integer | tuple. The maximum width for this container.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    max_width = Arguments.size(max_width, unit="%")
    container = self.context.rptObj.ui.div(components, profile=profile, options=options)
    container.style.css.max_width = max_width[0]
    container.style.css.text_align = align
    if align == 'center':
      container.style.css.margin = "0 auto"
    return container

  def background(self, url, width=(100, "%"), height=(300, "px"), size="cover", margin=0, align="center", htmlCode=None,
                 position="middle", profile=None, options=None):
    """
    Description:
    ------------

    Usage:
    -----


    Attributes:
    ----------
    :param url: String. Optional. The link to the gallery.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param size:
    :param margin: Integer. Optional. The CSS margin properties are used to create space around elements, outside of any defined borders.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param position: String. Optional. A string with the vertical position of the component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    div = self.context.rptObj.ui.div(height=Arguments.size(height, "px"), width=Arguments.size(width), htmlCode=htmlCode, options=options, profile=profile)
    div.style.css.background_url(self.context.rptObj.py.encode_html(url), size=size, margin=margin)
    div.style.css.display = "block"
    div.style.css.text_align = align
    div.style.css.vertical_align = position
    div.style.css.padding = "auto"
    return div

  def wallpaper(self, url=None, width=(100, "%"), height=(100, "%"), size="cover", margin=0, align="center", htmlCode=None,
                position="middle", profile=None, options=None):
    """
    Description:
    ------------

    tags: Background

    Usage:
    -----


    Attributes:
    ----------
    :param url: String. Optional. The link to the gallery.
    :param width: Optional. Tuple. The component width in pixel or percentage.
    :param height: Optional. Tuple. The component height in pixel or percentage.
    :param size:
    :param margin:
    :param align:
    :param position:
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    # report, htmlObj, label, color, width, icon, height, editable, align, padding, htmlCode, tag,
    #                helper, options, profile
    options = options or {}
    div = html.HtmlImage.Background(self.context.rptObj, [], label=None, color=None, width=Arguments.size(width), icon=None,
                                    height=Arguments.size(height), editable=False, align='left', padding=None, htmlCode=htmlCode,
                                    tag='div', helper=None, options=options, profile=profile)
    div.style.css.background_url(self.context.rptObj.py.encode_html(url) if url is not None else None, size=size, margin=margin)
    div.style.css.background_position = "center center"
    div.style.css.display = "block"
    div.style.css.text_align = align
    div.style.css.vertical_align = position
    div.style.css.padding = "auto"
    self.context.rptObj.body.style.css.height = "100%"
    return div

  def logo(self, url, width=(160, "px"), height=(60, "px"), top=(16, "px"), left=(16, "px"), profile=None, options=None):
    """
    Description:
    ------------

    Usage:
    -----


    Attributes:
    ----------
    :param url: String. Optional. The link to the gallery.
    :param width: Optional. Tuple. The component width in pixel or percentage.
    :param height: Optional. Tuple. The component height in pixel or percentage.
    :param top:
    :param left:
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    top = Arguments.size(top, 'px')
    left = Arguments.size(left, 'px')
    div = self.context.rptObj.ui.div(height=Arguments.size(height, 'px'), width=Arguments.size(width), options=options, profile=profile)
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
    Get teh picture used by youtube.

    Usage:
    -----


    Attributes:
    ----------
    :param video_id: String. Optional. The youtube video ID.
    :param width: Tuple. Optional. Tuple. The component width in pixel or percentage.
    :param height: Tuple. Optional. Tuple. The component height in pixel or percentage.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    return self.img("0.jpg", "http://img.youtube.com/vi/%s" % video_id, Arguments.size(width), Arguments.size(height, 'px'), align, htmlCode, profile, options)

  def circular(self, image=None, path=None, width=(200, "px"), height=(200, "px"), align="center", htmlCode=None,
              profile=None, options=None):
    """
    Description:
    ------------
    Add an HTML image to the page. The path can be defined either in a absolute or relative format.

    Tip: The absolute format does not work on servers. It is recommended to use relative starting to the root of the server

    Usage:
    -----

      page.ui.circular("epykIcon.PNG", path=r"../../../static/images", height=(50, "px"))

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlImage.Image`

    Related Pages:

      https://www.w3schools.com/bootstrap/bootstrap_ref_css_images.asp
      https://www.w3schools.com/cssref/css3_pr_border-radius.asp

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/image.py

    Attributes:
    ----------
    :param image: String. Optional. The image file name.
    :param path: String. Optional. String. The image file path.
    :param width: Tuple. Optional. Tuple. The component width in pixel or percentage.
    :param height: Tuple. Optional. Tuple. The component height in pixel or percentage.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    if height[0] is not None and width[1] == '%':
      width = ("auto", '')
    html_image = html.HtmlImage.Image(self.context.rptObj, image, path, align, htmlCode, width, height, profile, options or {})
    # add the css styles
    html_image.style.css.padding = 5
    html_image.style.css.borders_light()
    html_image.style.css.border_radius = width[0]
    return html_image

  def avatar(self, text="", image="", path=None, status=None, width=(30, "px"), height=(30, "px"), align="center", htmlCode=None,
               profile=None, options=None):
    """
    Description:
    ------------
    Generate or load an avatar.

    Usage:
    -----

      page.ui.images.avatar("Epyk", status='out')
      page.ui.images.avatar(image="epykIcon.PNG", path=config.IMG_PATH, status=False)

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Div`
      - :class:`epyk.core.html.HtmlImage.Image`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/image.py

    Attributes:
    ----------
    :param text:
    :param image:
    :param path: String. Optional. String. The image file path.
    :param status:
    :param width: Tuple. Optional. Tuple. The component width in pixel or percentage.
    :param height: Tuple. Optional. Tuple. The component height in pixel or percentage.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
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
      img = self.img(image, path, (width[0]-5, width[1]), (height[0]-5, height[1]), align="center", htmlCode=htmlCode, profile=profile, options=options)
      img.style.css.border_radius = width[0]
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
    div.img = img
    div.style.css.borders_light()
    div.style.css.border_radius = width[0]
    div.img = img
    if align == 'center':
      div.style.css.margin = "auto"
      div.style.css.display = "block"
    return div

  def section(self, image, name, title, text, url=None, path=None, width=(200, "px"), height=(200, "px"), htmlCode=None,
               profile=None, options=None):
    """
    Description:
    ------------

    Usage:
    -----

      page.ui.images.section("epykIcon.PNG", "# Test", "Epyk Test", 'This is a test', path=r"../../../static/images")

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
    :param url: String. Optional. The link to the gallery.
    :param path: String. Optional. String. The image file path.
    :param width: Tuple. Optional. Tuple. The component width in pixel or percentage.
    :param height: Tuple. Optional. Tuple. The component height in pixel or percentage.
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    width = Arguments.size(width, "px")
    height = Arguments.size(height, "px")
    img = self.img(image, width=(width[0]-10, 'px'), height=(100, "px"), path=path, profile=profile)
    title = self.context.rptObj.ui.title(title, level=2)
    highlight = self.context.rptObj.ui.texts.span(name, width=(50, "px"), height=(20, 'px'), profile=profile)
    paragraph = self.context.rptObj.ui.texts.paragraph(text)
    div = self.context.rptObj.ui.layouts.div([highlight, img, title, paragraph], width=width, height=height, profile=profile)
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
    This will display some details when the mouse is on the container.

    Usage:
    -----

      c = page.ui.images.animated("epykIcon.PNG", text="This is a comment", title="Title", url="#", path=r"../../../static/images")
      c.style.css.borders()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlImage.AnimatedImage`

    Related Pages:

      https://tympanus.net/Tutorials/OriginalHoverEffects/

    Attributes:
    ----------
    :param image: String. Optional. The image file name.
    :param text: String. Optional. String. The image file path.
    :param title: String. Optional. The image title displayed in to the mask on mouse hover the container.
    :param url: String. Optional. The link to the gallery.
    :param path: String. Optional. String. The image file path.
    :param width: Tuple. Optional. Tuple. The component width in pixel or percentage.
    :param height: Tuple. Optional. Tuple. The component height in pixel or percentage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, "px")
    height = Arguments.size(height, "px")
    html_id = html.HtmlImage.AnimatedImage(self.context.rptObj, image, text, title, url, path, width, height, options, profile)
    return html_id

  def carousel(self, images, path=None, selected=0, width=(100, "%"), height=(300, "px"), options=None, profile=None):
    """
    Description:
    ------------
    Carousel component for pictures.

    Usage:
    -----

      car = page.ui.images.carousel(["epykIcon.PNG", "epyklogo.ico", "epyklogo_whole_big.png"],
                                 path=r"../../../static/images", height=(200, 'px'))
      car.click([page.js.console.log('data', skip_data_convert=True)])

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlImage.ImgCarousel`

    Related Pages:

      https://www.cssscript.com/basic-pure-css-slideshow-carousel/

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/image.py

    Attributes:
    ----------
    :param images: List. With the different picture file names.
    :param path: String. Optional. The common path for the pictures.
    :param width: Tuple. Optional. Tuple. The component width in pixel or percentage.
    :param height: Tuple. Optional. Tuple. The component height in pixel.
    :param selected: Integer. Optional. The selected item index.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width)
    height = Arguments.size(height, "px")
    if height[1] == '%':
      raise Exception("This height cannot be in percentage")

    html_i = html.HtmlImage.ImgCarousel(self.context.rptObj, images, path, selected, width, height, options or {}, profile)
    return html_i

  def emoji(self, symbol=None, top=(20, 'px'), options=None, profile=None):
    """
    Description:
    ------------

    Usage:
    -----

      page.ui.images.emoji(page.symbols.smileys.DISAPPOINTED_FACE)

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlImage.Emoji`

    Related Pages:

      https://github.com/wedgies/jquery-emoji-picker

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/image.py

    Attributes:
    ----------
    :param symbol: String. Optional.
    :param top: Tuple. Optional.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    top = Arguments.size(top, "px")
    html_emoji = html.HtmlImage.Emoji(self.context.rptObj, symbol, top, options, profile)
    return html_emoji

  def icon(self, icon=None, family=None, width=(None, 'px'), htmlCode=None, height=(None, "px"), color=None, tooltip=None, align="left", options=None, profile=None):
    """
    Description:
    ------------

    Usage:
    -----

      page.ui.images.icon("fab fa-angellist")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlImage.Icon`

    Related Pages:

      https://fontawesome.com/icons?m=free

    Attributes:
    ----------
    :param icon: String. Optional. The component icon content from font-awesome references
    :param family:
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param align: String. Optional.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, "px")
    height = Arguments.size(height, "px")
    options = options or {}
    options['icon_family'] = family or 'font-awesome'
    html_icon = html.HtmlImage.Icon(self.context.rptObj, icon, width=width, height=height,
         color=color, tooltip=tooltip, options=options, htmlCode=htmlCode, profile=profile)
    return html_icon

  def badge(self, text="", label=None, icon=None, width=(25, "px"), height=(25, "px"), background_color=None, color=None, url=None,
            tooltip=None, options=None, profile=None):
    """
    Description:
    ------------
    Display a badge component using Bootstrap.

    Usage:
    -----

      page.ui.images.badge("Test badge", "Label", icon="fas fa-align-center")
      page.ui.images.badge("This is a badge", background_color="red", color="white")
      page.ui.images.badge(12, icon="far fa-bell", options={"badge_position": 'right'})

      b = page.ui.images.badge(7688, icon="fab fa-python", options={'badge_css': {'color': 'white', "background": 'red'}})
      b.options.badge_css = {"background": 'green'}

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlImage.Badge`

    Related Pages:

      https://getbootstrap.com/docs/4.0/components/badge/

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/image.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/links.py

    Attributes:
    ----------
    :param text: String. Optional. The content of the badge.
    :param label: String. Optional. The label to display close to the badge.
    :param icon: String. Optional. A String with the icon to display from font-awesome.
    :param background_color: String. Optional. The background color of the badge.
    :param color: String. Optional. The text color of the badge.
    :param url: String. Optional. The underlying url link for the badge.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param tooltip: String. Optional, The text to display in the tooltip.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary, A boolean to store the performances for each components.
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
    Simple vignette to display a color with it is code.

    TODO: Return the hex code of the color when dom.content used

    Usage:
    -----

      page.ui.images.color("FFFFFF")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlContainer.Div`

    Attributes:
    ----------
    :param code: String. The color code.
    :param color: String. Optional. The font color.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param helper: String. Optional. A tooltip helper.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
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
