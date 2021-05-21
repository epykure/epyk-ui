#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from epyk.core import html
from epyk.interfaces import Arguments


class Vignets:

  def __init__(self, ui):
    self.page = ui.page

  @html.Html.css_skin()
  def bubble(self, records=None, width=(70, "px"), height=("auto", ''), color=None, background_color=None,
             helper=None, options=None, profile=None):
    """
    Description:
    ------------
    The bubbles event property returns a Boolean value that indicates whether or not an event is a bubbling event.
    Event bubbling directs an event to its intended target, it works like this:
    A button is clicked and the event is directed to the button
    If an event handler is set for that object, the event is triggered.
    If no event handler is set for that object, the event bubbles up (like a bubble in water) to the objects parent.
    The event bubbles up from parent to parent until it is handled, or until it reaches the document object.

    :tags:
    :categories:

    Usage::

      page.ui.vignets.bubble({"value": 23, "title": "Title"}, helper="This is a helper")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Text`
      - :class:`epyk.core.html.HtmlContainer.Div`
      - :class:`epyk.core.html.HtmlLinks.ExternalLink`

    Related Pages:

      https://www.w3schools.com/jsref/event_bubbles.asp

    Attributes:
    ----------
    :param records: List. Optional. The list of dictionaries.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param background_color: String. Optional. The hexadecimal color code.
    :param helper: String. Optional. The value to be displayed to the helper icon.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    div = self.page.ui.div(width=width, height=height, profile=profile, options=options)
    div.style.css.position = "relative"
    bubble = self.page.ui.div(width=width, height=width, profile=profile, helper=helper)
    if helper is not None:
      bubble.helper.style.css.right = 0
      bubble.helper.style.css.bottom = 0
    div.number = self.page.ui.text(records["value"], width=width)
    if records.get("url") is not None:
      div.title = self.page.ui.link(records["title"], url=records['url'], profile=profile)
      div.title.no_decoration()
    else:
      div.title = self.page.ui.text(records["title"])
    div.title.style.css.bold()
    div.number.style.css.line_height = width[0]
    div.number.style.css.text_align = "center"
    div.number.style.css.font_size = width[0] - 45
    bubble += div.number
    bubble.style.css.background_color = background_color or self.page.theme.colors[-1]
    bubble.style.css.color = color or self.page.theme.greys[0]
    bubble.style.css.borders_light()
    bubble.style.css.border_radius = width[0]
    bubble.style.css.middle()
    div.style.css.text_align = "center"
    div += bubble
    div += div.title
    return div

  @html.Html.css_skin()
  def number(self, number, label="", title=None, align="center", components=None, width=('auto', ""),
             height=(None, "px"), profile=None, options=None, helper=None):
    """
    Description:
    ------------
    The <input type="number"> defines a field for entering a number.
    Use the following attributes to specify restrictions:
    max - specifies the maximum value allowed
    min - specifies the minimum value allowed
    step - specifies the legal number intervals
    value - Specifies the default value

    :tags:
    :categories:

    Usage::

      number = page.ui.vignets.number(500, "Test")
      number_2 = page.ui.vignets.number(500, "Test 2 ", options={"url": "http://www.google.fr"})
      number.span.add_icon(page.ui.icons.get.ICON_ENVELOPE)

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextComp.Number`

    Related Pages:

      https://www.w3schools.com/tags/att_input_type_number.asp

    Attributes:
    ----------
    :param number: Integer. The value.
    :param label: String. Optional. The label text.
    :param title: String | Component. Optional. A panel title. This will be attached to the title property.
    :param align: String. Optional. The text-align property within this component.
    :param components: List. Optional. The HTML components.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param helper: String. Optional. The value to be displayed to the helper icon.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    dflt_options = {"digits": 0, "thousand_sep": ',', "decimal_sep": '.', 'type_number': 'number'}
    if options is not None:
      dflt_options.update(options)
    if 'symbol' in dflt_options:
      dflt_options['type_number'] = 'money'
      number = self.page.py.format_money(
        number, digits=dflt_options.get('digits', 0), symbol=dflt_options.get('symbol'))
    else:
      number = self.page.py.format_number(number, digits=dflt_options.get('digits', 0))
    pre_components = []
    if title is not None:
      if not hasattr(title, 'options'):
        title = self.page.ui.titles.title(title)
        title.style.css.display = "block"
        title.style.css.text_align = align
      pre_components.append(title)
    pre_components.append(html.HtmlTextComp.Number(
      self.page, number, components, label, width, ("auto", ""), profile, dflt_options, helper))

    container = self.page.ui.div([pre_components], align=align, height=height, width=width, profile=profile, options=options)
    container.number = pre_components[-1]
    container.build = pre_components[-1].build
    if title is not None:
      container.title = title
    return container

  @html.Html.css_skin()
  def block(self, records=None, color=None, border='auto', width=(300, 'px'), height=(None, 'px'),
            helper=None, options=None, profile=None):
    """
    Description:
    ------------
    Every HTML element has a default display value depending on what type of element it is.
    The two display values are: block and inline.

    :tags:
    :categories:

    Usage::

      page.ui.vignets.block({"text": 'This is a brand new python framework', "title": 'New Python Web Framework',
                             "button": {"text": 'Get Started', 'url': "/getStarted"}, 'color': 'green'})

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextComp.BlockText`

    Related Pages:

      https://www.w3schools.com/htmL/html_blocks.asp

    Attributes:
    ----------
    :param records: List. Optional. The list of dictionaries with the input data.
    :param color: String. Optional. The font color in the component. Default inherit.
    :param border:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param helper: String. Optional. The value to be displayed to the helper icon.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    html_blocktext = html.HtmlTextComp.BlockText(
      self.page, records, color, border, width, height, helper, options, profile)
    return html_blocktext

  @html.Html.css_skin()
  def text(self, records=None, width=(None, '%'), height=(None, "px"), align='center', helper=None, options=None,
           profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

      page.ui.vignets.text({"title": "New Python Framework", 'value': "A new Python Web Framework", 'color': 'green',
                            'icon': 'fab fa-python', 'colorTitle': 'darkgreen'})

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextComp.TextWithBorder`

    Attributes:
    ----------
    :param records: List. Optional. The list of dictionaries with the input data.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param align: String. Optional. The text-align property within this component.
    :param helper: String. Optional. The value to be displayed to the helper icon.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    html_text = html.HtmlTextComp.TextWithBorder(self.page, records, width, height, align, helper, options, profile)
    return html_text

  @html.Html.css_skin()
  def image(self, title=None, content="", image=None, render="row", align="center", width=(90, '%'),
            height=(None, "px"), options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Attributes:
    ----------
    :param title: String. Optional. A panel title. This will be attached to the title property.
    :param content:
    :param image:
    :param render:
    :param align: String. Optional. The text-align property within this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    options = options or {}
    if render == "row":
      container = self.page.ui.row(align=align, width=width, height=height, options=options, profile=profile)
      container.options.responsive = False
      container.style.css.margin = "20px auto"
      if title is not None and not hasattr(title, 'options'):
        title = self.page.ui.titles.title(title)
        title.style.css.display = "block"
      container.title = title
      if not hasattr(content, 'options'):
        content = self.page.ui.text(content)
        content.style.css.display = "block"
      if options.get('picture', 'left') == 'left':
        if image is not None:
          if not hasattr(image, 'options'):
            split_url = os.path.split(image)
            container.image = self.page.ui.img(split_url[1], path=split_url[0], profile=profile)
            container.add(container.image)
            if height[0] is not None and height[1] == "px":
              container.image.style.css.width = "auto"
              container.image.style.css.height = "%s%s" % (height[0], height[1])
          else:
            container.image = image
        if title is not None:
          col = self.page.ui.col([title, content])
          col.style.css.padding = 0
          container.add(col)
        else:
          container.add(content)
      else:
        if title is not None:
          container.add(self.page.ui.col([title, content]))
          container.title = title
        else:
          container.add(content)
        if image is not None:
          if not hasattr(image, 'options'):
            split_url = os.path.split(image)
            container.image = self.page.ui.img(split_url[1], path=split_url[0], profile=profile)
            container.add(container.image)
            if height[0] is not None and height[1] == "px":
              container.image.style.css.width = "auto"
              container.image.style.css.height = "%s%s" % (height[0], height[1])

    else:
      container = self.page.ui.col(align=align, width=width, height=height, position="top", profile=profile)
      container.style.css.margin = "20px auto"
      if title is not None and not hasattr(title, 'options'):
        title = self.page.ui.titles.title(title)
        title.style.css.display = "block"
      container.title = title
      if not hasattr(content, 'options'):
        content = self.page.ui.text(content)
        content.style.css.display = "block"
      if image is not None:
        if not hasattr(image, 'options'):
          split_url = os.path.split(image)
          container.image = self.page.ui.img(split_url[1], path=split_url[0], profile=profile)
          container.add(container.image)
      if title is not None:
        container.add(self.page.ui.col([title, content]))
      else:
        container.add(content)
    return container

  @html.Html.css_skin()
  def video(self, title, content="", video=None, render="row", align="center", width=(90, '%'), height=(None, "px"),
            options=None, profile=None):
    """
    Description:
    ------------
    Component to allow creation of a vignet embedding a video.

    :tags:
    :categories:

    Usage::

    Related Pages:
    --------------

    Issue:
    ------

      https://github.com/epykure/epyk-ui/issues/92

    Attributes:
    ----------
    :param title: String. Optional. A panel title. This will be attached to the title property.
    :param content:
    :param video:
    :param render:
    :param align: String. The text-align property within this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    def get_video(page, video_link):
      if video_link is not None:
        if not hasattr(video_link, 'options'):
          if not video_link.startswith('http'):
            split_url = os.path.split(video_link)
            return page.ui.media.video(split_url[1], path=split_url[0])

          elif 'www.youtube' in video_link:
            return page.ui.media.youtube(html.HtmlMedia.Youtube.get_embed_link(video_link))

      return None

    options = options or {}
    if render == "row":
      video_content = False
      container = self.page.ui.row(align=align, width=width, height=height, profile=profile)
      container.style.css.margin = "20px auto"
      if not hasattr(title, 'options'):
        title = self.page.ui.titles.title(title)
        title.style.css.display = "block"
      if not hasattr(content, 'options'):
        content = self.page.ui.text(content)
        content.style.css.display = "block"
      if options.get('picture', 'left') == 'left':
        video_content = get_video(self.page, video)
        video_content.style.css.width = None
        video_content.style.css.height = "100%"
      if video_content:
        container.video = video_content
        container.add(container.video)
        container.add(self.page.ui.col([title, content]))
    else:
      container = self.page.ui.col(align=align, width=width, height=height, position="top", profile=profile)
      container.style.css.margin = "20px auto"
      if not hasattr(title, 'options'):
        title = self.page.ui.titles.title(title)
        title.style.css.display = "block"
      if not hasattr(content, 'options'):
        content = self.page.ui.text(content)
        content.style.css.display = "block"
      video_content = get_video(self.page, video)
      if video_content:
        container.video = video_content
        container.add(container.video)
      container.add(self.page.ui.col([title, content]))
    return container

  @html.Html.css_skin()
  def background(self, url, width=(90, "%"), height=(450, "px"), size="contain", margin=0, align="center",
                 position="middle", options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Attributes:
    ----------
    :param url: String. The url string.
    :param align: String. Optional. The text-align property within this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param size: String. Optional.
    :param margin: Integer. Optional.
    :param position: String. Optional.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    div = self.page.ui.div(height=height, width=width, options=options, profile=profile)
    div.style.css.background_url(url, size=size, margin=margin)
    div.style.css.display = "block"
    div.style.css.text_align = align
    div.style.css.vertical_align = position
    div.style.css.padding = "auto"
    if align == "center":
      div.style.css.margin = "10px auto"
      div.style.css.display = "block"
    return div

  @html.Html.css_skin()
  def vignet(self, title, content, icon=None, render="col", align="center", width=(200, 'px'), options=None,
             profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Attributes:
    ----------
    :param title: String. Optional. A panel title. This will be attached to the title property.
    :param content: String. Optional. The value to be displayed to the component.
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome.
    :param render:
    :param align: String. Optional. The text-align property within this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    options = options or {"position": 'left'}
    if render == "col":
      container = self.page.ui.div(align=align, width=width, profile=profile, options=options)
      container.style.css.margin = "auto"
      if not hasattr(title, 'options'):
        title = self.page.ui.titles.title(title, profile=profile)
        title.style.css.display = "block"
        title.style.css.text_align = align
      if not hasattr(content, 'options'):
        content = self.page.ui.text(content, options=options, profile=profile)
        content.style.css.display = "block"
        content.style.css.text_align = align
      if icon is not None:
        if not hasattr(icon, 'options'):
          container.add(self.page.ui.icons.awesome(icon, width=(30, "px"), height=(30, "px"), profile=profile))
        else:
          container.add(icon)
      container.add(title)
      container.add(content)
    else:
      container = self.page.ui.row(align=align, width=width, position="top", profile=profile, options=options)
      container.options.autoSize = False
      container.style.css.margin = "auto"
      if not hasattr(title, 'options'):
        title = self.page.ui.titles.title(title)
        title.style.css.display = "block"
        title.style.css.text_align = align
      if not hasattr(content, 'options'):
        content = self.page.ui.text(content)
        content.style.css.display = "block"
        content.style.css.text_align = align
      if icon is not None:
        if not hasattr(icon, 'options'):
          icon_obj = self.page.ui.icons.awesome(icon, width=(25, "px"), height=(25, "px"), profile=profile)
          icon_obj.style.css.margin_top = 20
          icon_obj.style.css.display = "block"
          container.add(icon_obj)
          container[0].attr["class"].add("col-3")
        else:
          container.add(icon)
      container.add(self.page.ui.col([title, content]))
      container[-1].style.css.border_left = "1px solid %s" % self.page.theme.greys[3]
    return container

  @html.Html.css_skin()
  def price(self, value, title, items=None, components=None, url=None, align="center", width=(250, 'px'),
            height=("auto", ''), currency="£", options=None, profile=None, helper=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

      page.ui.vignets.price(10, "This is the price", [])

    Attributes:
    ----------
    :param value:
    :param title: String. Optional. A panel title. This will be attached to the title property.
    :param items:
    :param components:
    :param url:
    :param align: String. Optional. The text-align property within this component.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param currency: String. Optional. The currency value.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param helper: String. Optional. The value to be displayed to the helper icon.
    """
    container = self.page.ui.div(
      align=align, width=width, height=height, options=options, profile=profile, helper=helper)
    container.style.css.border = "1px solid %s" % self.page.theme.greys[3]
    container.style.css.margin = "auto"
    if not hasattr(title, 'options'):
      title = self.page.ui.titles.title(title)
      title.style.css.display = "block"
      title.style.css.text_align = align
    container.add(title)
    if components is not None:
      for component in components:
        container.add(component)
    if not hasattr(value, 'options'):
      value = self.page.ui.texts.number(value, options={"type_number": 'money', 'symbol': currency}, profile=profile)
      value.style.css.font_size = self.page.body.style.globals.font.normal(30)
      container.number = value
    container.add(value)
    if url is not None:
      button = self.page.ui.button("Subscribe", align="center", profile=profile)
      button.style.css.background_color = self.page.theme.success[1]
      button.style.css.color = 'white'
      button.style.css.margin_top = 10
      button.style.css.margin_bottom = 10
      container.add(button)
    if items is not None:
      if not hasattr(items, 'options'):
        items = self.page.ui.lists.icons(items, profile=profile)
        items.style.css.margin = "auto 20%"
        items.style.css.text_align = "left"
      container.add(items)
    return container

  @html.Html.css_skin()
  def slides(self, start=0, width=(100, '%'), height=(100, "%"), options=None, profile=None):
    """
    Description:
    ------------

    :tags:
    :categories:

    Usage::

    Attributes:
    ----------
    :param start:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.

    TODO: Fix layout issue with F11 (full screen)
    """
    dflt_options = {'markdown': True}
    if options is not None:
      dflt_options.update(options)
    html_slides = html.HtmlOthers.Slides(self.page, start, width, height, dflt_options, profile)
    return html_slides
