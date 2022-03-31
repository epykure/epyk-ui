#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core import html
from epyk.core.css import Colors
from epyk.interfaces import Arguments
from epyk.core.css import Defaults as Defaults_css


class Images:

  def __init__(self, ui):
    self.page = ui.page

  def img(self, image=None, path=None, width=(100, "%"), height=(None, "px"), align="center", html_code=None,
          profile=None, tooltip=None, options=None):
    """
    Description:
    ------------
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

    Attributes:
    ----------
    :param image: String. Optional. The image file name.
    :param path: String. Optional. Optional. TString. The image file path.
    :param width: Tuple. Optional. Optional. Tuple. The component width in pixel or percentage.
    :param height: Tuple. Optional. Optional. Tuple. The component height in pixel or percentage.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param options: Dictionary. Optional. Specific Python options available for this component.
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

  def figure(self, image=None, caption=None, path=None, width=(100, "%"), height=(None, "px"), align="center",
             html_code=None, profile=None, tooltip=None, options=None):
    """
    Description:
    ------------
    Display a picture as a figure component with an attached caption object.

    :tags:
    :categories:

    Related Pages:

      https://www.w3schools.com/tags/tag_figcaption.asp

    Usage::

      page.ui.images.figure("33c33735-8a1e-4bef-8201-155b4775304a.jpg", "test caption",
        path=picture_path, width=(100, 'px'))

    Attributes:
    ----------
    :param image: String. Optional. The url path of the image.
    :param caption: String. Optional.
    :param path: String. Optional. String. The image file path.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param options: Dictionary. Optional. Specific Python options available for this component.
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

  def container(self, components, max_width=(900, 'px'), align="center", profile=None, options=None):
    """
    Description:
    ------------
    Empty container for images.

    :tags:
    :categories:

    Usage::


    Attributes:
    ----------
    :param components: List of HTML Component. internal components.
    :param max_width: Integer | tuple. The maximum width for this container.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    max_width = Arguments.size(max_width, unit="%")
    container = self.page.ui.div(components, profile=profile, options=options)
    container.style.css.max_width = max_width[0]
    container.style.css.text_align = align
    if align == 'center':
      container.style.css.margin = "0 auto"
    html.Html.set_component_skin(container)
    return container

  def background(self, url, width=(100, "%"), height=(300, "px"), size="cover", margin=0, align="center",
                 html_code=None, position="middle", profile=None, options=None):
    """
    Description:
    ------------
    Add a background image.

    :tags:
    :categories:

    Usage::


    Attributes:
    ----------
    :param url: String. Optional. The link to the gallery.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param size: String. Optional. The type of background in
    :param margin: Integer. Optional. The CSS margin properties are used to create space around elements,
                            outside of any defined borders.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param position: String. Optional. A string with the vertical position of the component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
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

  def wallpaper(self, url=None, width=(100, "%"), height=(100, "%"), size="cover", margin=0, align="center",
                html_code=None, position="middle", profile=None, options=None):
    """
    Description:
    ------------

    :tags: Background
    :categories:

    Usage::


    Attributes:
    ----------
    :param url: String. Optional. The link to the gallery.
    :param width: Optional. Tuple. The component width in pixel or percentage.
    :param height: Optional. Tuple. The component height in pixel or percentage.
    :param size: String. Optional. The type of background in
    :param margin: Integer. Optional. The CSS margin properties are used to create space around elements,
                            outside of any defined borders.
    :param align: String. The text-align property within this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param position: String. Optional. The position compared to the main component tag.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
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

  def logo(self, url, width=(160, "px"), height=(60, "px"), top=(16, "px"), left=(16, "px"), profile=None,
           options=None):
    """
    Description:
    ------------

    :tags:
    :categories:


    Usage::


    Attributes:
    ----------
    :param url: String. Optional. The link to the gallery.
    :param width: Tuple. Optional. The component width in pixel or percentage.
    :param height: Tuple. Optional. The component height in pixel or percentage.
    :param top: Tuple. Optional. A tuple with the integer for the component's distance to the top of the page.
    :param left: Tuple. Optional. A tuple with the integer for the component's distance to the left of the page.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
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

  def youtube(self, video_id=None, width=(100, "%"), height=(None, "px"), align="center", html_code=None, profile=None,
              options=None):
    """
    Description:
    ------------
    Get teh picture used by youtube.

    :tags:
    :categories:

    Usage::


    Attributes:
    ----------
    :param video_id: String. Optional. The youtube video ID.
    :param width: Tuple. Optional. Tuple. The component width in pixel or percentage.
    :param height: Tuple. Optional. Tuple. The component height in pixel or percentage.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    """
    component = self.img("0.jpg", "http://img.youtube.com/vi/%s" % video_id, Arguments.size(width),
                    Arguments.size(height, 'px'), align, html_code, profile, options)
    html.Html.set_component_skin(component)
    return component

  def circular(self, image=None, path=None, width=(200, "px"), height=(200, "px"), align="center", html_code=None,
               profile=None, options=None):
    """
    Description:
    ------------
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

    Attributes:
    ----------
    :param image: String. Optional. The image file name.
    :param path: String. Optional. String. The image file path.
    :param width: Tuple. Optional. Tuple. The component width in pixel or percentage.
    :param height: Tuple. Optional. Tuple. The component height in pixel or percentage.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
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

  def avatar(self, text="", image="", path=None, status=None, width=(30, "px"), height=(30, "px"), align="center",
             html_code=None, profile=None, options=None):
    """
    Description:
    ------------
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

    Attributes:
    ----------
    :param text: String. Optional. The value to be displayed to the component.
    :param image: String. Optional. The url of the image.
    :param path: String. Optional. String. The image file path.
    :param status: String. Optional. The avatar status code. Default no status.
    :param width: Tuple. Optional. Tuple. The component width in pixel or percentage.
    :param height: Tuple. Optional. Tuple. The component height in pixel or percentage.
    :param align: String. Optional. A string with the horizontal position of the component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
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

    bgcolor, margin_top = None, -5
    if image is not None:
      img = self.img(image, path, (width[0]-5, width[1]), (height[0]-5, height[1]), align="center", html_code=html_code,
                     profile=profile, options=options)
      img.style.css.border_radius = width[0]
      img.style.css.margin = 2
      margin_top = -8
    else:
      bgcolor = Colors.randColor(self.page.py.hash(text))
      img = self.page.ui.layouts.div(text[0].upper())
      img.style.css.line_height = width[0] - 5
      img.style.css.color = "white"
      img.style.css.font_size = width[0]
      img.style.css.font_weight = 'bold'
      img.style.css.padding = 0
    img.style.css.middle()
    if options.get('status', True):
      status_o = self.page.ui.layouts.div("&nbsp;", width=(10, "px"), height=(10, "px"))
      status_o.style.css.position = 'relative'

      status_o.style.css.background_color = status_map.get(status, self.page.theme.greys[5])
      status_o.style.css.border_radius = 10
      status_o.style.css.margin_top = margin_top
      status_o.style.css.float = 'right'

      div = self.page.ui.layouts.div([img, status_o], width=width, height=height)
      div.status = status_o
    else:
      div = self.page.ui.layouts.div([img], width=width, height=height)
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
    html.Html.set_component_skin(div)
    return div

  def section(self, image, name, title, text, url=None, path=None, width=(200, "px"), height=(200, "px"), profile=None,
              options=None):
    """
    Description:
    ------------

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

    Attributes:
    ----------
    :param image: String. The url of the image.
    :param name:  String. The name of the image.
    :param title: String. Optional. A panel title. This will be attached to the title property.
    :param text: String. Optional. The value to be displayed to the component.
    :param url: String. Optional. The link to the gallery.
    :param path: String. Optional. String. The image file path.
    :param width: Tuple. Optional. Tuple. The component width in pixel or percentage.
    :param height: Tuple. Optional. Tuple. The component height in pixel or percentage.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
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

  def animated(self, image="", text="", title="", url=None, path=None, width=(200, "px"), height=(200, "px"),
               html_code=None, options=None, profile=None):
    """
    Description:
    ------------
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

    Attributes:
    ----------
    :param image: String. Optional. The image file name.
    :param text: String. Optional. String. The image file path.
    :param title: String. Optional. The image title displayed in to the mask on mouse hover the container.
    :param url: String. Optional. The link to the gallery.
    :param path: String. Optional. String. The image file path.
    :param width: Tuple. Optional. Tuple. The component width in pixel or percentage.
    :param height: Tuple. Optional. Tuple. The component height in pixel or percentage.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, "px")
    height = Arguments.size(height, "px")
    component = html.HtmlImage.AnimatedImage(
      self.page, image, text, title, html_code, url, path, width, height, options, profile)
    html.Html.set_component_skin(component)
    return component

  def carousel(self, images=None, path=None, selected=0, width=(100, "%"), height=(300, "px"), options=None,
               profile=None):
    """
    Description:
    ------------
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

    Attributes:
    ----------
    :param images: List. Optional. With the different picture file names.
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

    component = html.HtmlImage.ImgCarousel(
      self.page, images or [], path, selected, width, height, options or {}, profile)
    html.Html.set_component_skin(component)
    return component

  def emoji(self, symbol=None, top=(20, 'px'), options=None, profile=None):
    """
    Description:
    ------------

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

    Attributes:
    ----------
    :param symbol: String. Optional. The emoji code.
    :param top: Tuple. Optional. The number of pixel from the top of the page.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    top = Arguments.size(top, "px")
    component = html.HtmlImage.Emoji(self.page, symbol, top, options, profile)
    html.Html.set_component_skin(component)
    return component

  def icon(self, icon=None, family=None, width=(None, 'px'), html_code=None, height=(None, "px"), color=None,
           tooltip=None, align="left", options=None, profile=None):
    """
    Description:
    ------------
    Add an icon to the page.

    :tags:
    :categories:

    Usage::

      page.ui.images.icon("fab fa-angellist")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlImage.Icon`

    Related Pages:

      https://fontawesome.com/icons?m=free

    Attributes:
    ----------
    :param icon: String. Optional. The component icon content from font-awesome references
    :param family: String. Optional. The Icon framework reference.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param tooltip: String. Optional. A string with the value of the tooltip.
    :param align: String. The text-align property within this component.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, "px")
    height = Arguments.size(height, "px")

    icon_details = Defaults_css.get_icon(icon, family)
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
    html.Html.set_component_skin(component)
    return component

  def badge(self, text="", label=None, icon=None, width=(25, "px"), height=(25, "px"), background_color=None,
            color=None, url=None, tooltip=None, options=None, profile=None):
    """
    Description:
    ------------
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
      background_color = self.page.theme.greys[0]
    if color is None:
      color = self.page.theme.success[1]
    icon_details = Defaults_css.get_icon(icon)
    options = options or {}
    options["icon_family"] = icon_details["icon_family"]
    component = html.HtmlImage.Badge(
      self.page, text, width, height, label, icon_details["icon"], background_color, color, url, tooltip, options,
      profile)
    html.Html.set_component_skin(component)
    return component

  def color(self, code, color=None, width=(110, 'px'), height=(25, 'px'), options=None, helper=None, profile=None):
    """
    Description:
    ------------
    Simple vignette to display a color with it is code.

    TODO: Return the hex code of the color when dom.content used

    :tags:
    :categories:

    Usage::

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
    div = self.page.ui.div(code, width=width, height=height, options=options, helper=helper, profile=profile)
    div.style.css.background_color = code
    div.style.css.line_height = "%s%s" % (height[0], height[1])
    div.style.css.color = color or self.page.theme.greys[0]
    div.style.css.text_align = "center"
    div.style.css.border = "1px solid black"
    div.style.css.vertical_align = "middle"
    html.Html.set_component_skin(div)
    return div

  def gallery(self, images=None, columns=6, width=(None, '%'), height=('auto', ''), options=None, profile=None):
    """
    Description:
    ------------
    Mosaic of pictures.

    :tags:
    :categories:

    Usage:
    -----

    Related Pages:

    Underlying HTML Objects:

    Templates:

    Attributes:
    ----------
    :param images: List. Optional. The list with the pictures.
    :param columns: Integer. Optional. The number of column for the mosaic component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
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
