
import os

from epyk.core import html
from epyk.core.css import Defaults as Defaults_css


class Vignets(object):
  def __init__(self, context):
    self.context = context

  def bubble(self, recordSet=None, width=(50, "px"), height=(110, 'px'), color=None,
             background_color=None, helper=None, profile=None):
    """
    Description:
    ------------
    The bubbles event property returns a Boolean value that indicates whether or not an event is a bubbling event.
    Event bubbling directs an event to its intended target, it works like this:
    A button is clicked and the event is directed to the button
    If an event handler is set for that object, the event is triggered
    If no event handler is set for that object, the event bubbles up (like a bubble in water) to the objects parent
    The event bubbles up from parent to parent until it is handled, or until it reaches the document object.

    Usage::

      rptObj.ui.vignets.bubble({"value": 23, "title": "Title"}, helper="This is a helper")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlText.Text`
      - :class:`epyk.core.html.HtmlContainer.Div`
      - :class:`epyk.core.html.HtmlLinks.ExternalLink`

    Related Pages:

      https://www.w3schools.com/jsref/event_bubbles.asp

    Attributes:
    ----------
    :param recordSet:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param color: Optional. The font color in the component. Default inherit
    :param background_color:
    :param helper: Optional. A tooltip helper
    :param profile: Optional. A flag to set the component performance storage
    """
    div = self.context.rptObj.ui.div(width=width, height=height)
    bubble = self.context.rptObj.ui.div(width=width, height=(height[0]-60, height[1]))
    div.number = self.context.rptObj.ui.text(recordSet["value"], width=width)
    if recordSet.get("url") is not None:
      div.title = self.context.rptObj.ui.link(recordSet["title"], url=recordSet['url'])
      div.title.no_decoration()
    else:
      div.title = self.context.rptObj.ui.text(recordSet["title"])
    div.title.style.css.bold()
    div.number.style.css.line_height = height[0]-60
    div.number.style.css.text_align = "center"
    div.number.style.css.font_size = height[0]-90
    bubble += div.number
    bubble.style.css.background_color = self.context.rptObj.theme.success[1]
    bubble.style.css.color = self.context.rptObj.theme.greys[0]
    bubble.style.css.borders_light()
    bubble.style.css.border_radius = height[0]-60
    bubble.style.css.middle()
    div.style.css.text_align = "center"
    div += bubble
    div += div.title
    return div

  def number(self, number, label="", width=(100, "px"), height=(None, "px"), profile=None, options=None):
    """
    Description:
    ------------
    The <input type="number"> defines a field for entering a number.
    Use the following attributes to specify restrictions:
    max - specifies the maximum value allowed
    min - specifies the minimum value allowed
    step - specifies the legal number intervals
    value - Specifies the default value

    Usage::

      number = rptObj.ui.vignets.number(500, "Test")
      number_2 = rptObj.ui.vignets.number(500, "Test 2 ", options={"url": "http://www.google.fr"})
      number.span.add_icon(rptObj.ui.icons.get.ICON_ENVELOPE)

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextComp.Number`

    Related Pages:

      https://www.w3schools.com/tags/att_input_type_number.asp

    Attributes:
    ----------
    :param number:
    :param label:
    :param width:
    :param height:
    :param profile:
    """
    html_number = html.HtmlTextComp.Number(self.context.rptObj, number, label, width, height, profile, options or {})
    return html_number

  def link(self):
    pass

  def block(self, recordSet=None, color=None, border='auto', width=(300, 'px'), height=(None, 'px'),
            helper=None, options=None, profile=None):
    """
    Description:
    ------------
    Every HTML element has a default display value depending on what type of element it is.
    The two display values are: block and inline.

    Usage::

      rptObj.ui.vignets.block({"text": 'This is a brand new python framework', "title": 'New Python Web Framework',
                             "button": {"text": 'Get Started', 'url': "/getStarted"}, 'color': 'green'})

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextComp.BlockText`

    Related Pages:

      https://www.w3schools.com/htmL/html_blocks.asp

    Attributes:
    ----------
    :param recordSet:
    :param color: Optional. The font color in the component. Default inherit
    :param border:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param helper: Optional. A tooltip helper
    :param profile: Optional. A flag to set the component performance storage
    """
    html_blocktext = html.HtmlTextComp.BlockText(self.context.rptObj, recordSet, color, border, width, height, helper, options, profile)
    return html_blocktext

  def text(self, recordSet=None, width=(None, '%'), height=(None, "px"), align='center', helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::

      rptObj.ui.vignets.text({"title": "New Python Framework", 'value': "A new Python Web Framework", 'color': 'green',
                            'icon': 'fab fa-python', 'colorTitle': 'darkgreen'})

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextComp.TextWithBorder`

    Attributes:
    ----------
    :param recordSet:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param align:
    :param helper: Optional. A tooltip helper
    :param profile: Optional. A flag to set the component performance storage
    """
    html_text = html.HtmlTextComp.TextWithBorder(self.context.rptObj, recordSet, width, height, align, helper, options, profile)
    return html_text

  def bars(self):
    pass

  def line(self):
    pass

  def image(self, title, content="", image=None, render="row", align="center", width=(90, '%'), height=(None, "px"), options=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param title:
    :param content:
    :param image:
    :param render:
    :param align:
    :param width:
    """
    options = options or {}
    if render == "row":
      container = self.context.rptObj.ui.row(align=align, width=width, height=height)
      container.style.css.margin = "20px auto"
      if not hasattr(title, 'options'):
        title = self.context.rptObj.ui.titles.title(title)
        title.style.css.display = "block"
      if not hasattr(content, 'options'):
        content = self.context.rptObj.ui.text(content)
        content.style.css.display = "block"
      if options.get('picture', 'left') == 'left':
        if image is not None:
          if not hasattr(image, 'options'):
            split_url = os.path.split(image)
            container.add(self.context.rptObj.ui.img(split_url[1], path=split_url[0]))
        container.add(self.context.rptObj.ui.col([title, content]))
      else:
        container.add(self.context.rptObj.ui.col([title, content]))
        if image is not None:
          if not hasattr(image, 'options'):
            split_url = os.path.split(image)
            container.add(self.context.rptObj.ui.img(split_url[1], path=split_url[0]))
    else:
      container = self.context.rptObj.ui.col(align=align, width=width, height=height, position="top")
      container.style.css.margin = "20px auto"
      if not hasattr(title, 'options'):
        title = self.context.rptObj.ui.titles.title(title)
        title.style.css.display = "block"
      if not hasattr(content, 'options'):
        content = self.context.rptObj.ui.text(content)
        content.style.css.display = "block"
      if image is not None:
        if not hasattr(image, 'options'):
          split_url = os.path.split(image)
          container.image = self.context.rptObj.ui.img(split_url[1], path=split_url[0])
          container.add(container.image)
      container.add(self.context.rptObj.ui.col([title, content]))
    return container

  def background(self, url, width=(90, "%"), height=(450, "px"), size="contain", margin=0, align="center", position="middle"):
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
    div = self.context.rptObj.ui.div(height=height, width=width)
    div.style.css.background_url(url, size=size, margin=margin)
    div.style.css.display = "block"
    div.style.css.text_align = align
    div.style.css.vertical_align = position
    div.style.css.padding = "auto"
    if align == "center":
      div.style.css.margin = "10px auto"
      div.style.css.display = "block"
    return div

  def vignet(self, title, content, icon=None, render="col", align="center", width=(200, 'px'), options=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param title:
    :param content:
    :param icon:
    :param render:
    :param align:
    :param width:
    """
    options = options or {"position": 'left'}
    if render == "col":
      container = self.context.rptObj.ui.div(align=align, width=width)
      container.style.css.margin = "auto"
      if not hasattr(title, 'options'):
        title = self.context.rptObj.ui.titles.title(title)
        title.style.css.display = "block"
        title.style.css.text_align = align
      if not hasattr(content, 'options'):
        content = self.context.rptObj.ui.text(content)
        content.style.css.display = "block"
        content.style.css.text_align = align
      if icon is not None:
        if not hasattr(icon, 'options'):
          container.add(self.context.rptObj.ui.icons.awesome(icon, width=(30, "px"), height=(30, "px")))
        else:
          container.add(icon)
      container.add(title)
      container.add(content)
    else:
      container = self.context.rptObj.ui.row(align=align, width=width, position="top")
      container.options.autoSize = False
      container.style.css.margin = "auto"
      if not hasattr(title, 'options'):
        title = self.context.rptObj.ui.titles.title(title)
        title.style.css.display = "block"
        title.style.css.text_align = align
      if not hasattr(content, 'options'):
        content = self.context.rptObj.ui.text(content)
        content.style.css.display = "block"
        content.style.css.text_align = align
      if icon is not None:
        if not hasattr(icon, 'options'):
          icon_obj  = self.context.rptObj.ui.icons.awesome(icon, width=(25, "px"), height=(25, "px"))
          icon_obj.style.css.margin_top = 20
          icon_obj.style.css.display = "block"
          container.add(icon_obj)
          container[0].attr["class"].add("col-3")
        else:
          container.add(icon)
      container.add(self.context.rptObj.ui.col([title, content]))
      container[-1].style.css.border_left = "1px solid %s" % self.context.rptObj.theme.greys[3]
    return container

  def price(self, value, title, items, align="center", width=(300, 'px'), currency="£"):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param value:
    :param title:
    :param items:
    :param align:
    :param width:
    :param currency:
    """
    container = self.context.rptObj.ui.div(align=align, width=width)
    container.style.css.margin = "auto"
    if not hasattr(title, 'options'):
      title = self.context.rptObj.ui.titles.title(title)
      title.style.css.display = "block"
      title.style.css.text_align = align
    container.add(title)
    if not hasattr(value, 'options'):
      value = self.context.rptObj.ui.texts.number(value, options={"type_number": 'money', 'symbol': currency})
      value.style.css.font_size = Defaults_css.font(30)
    container.add(value)
    if not hasattr(items, 'options'):
      items = self.context.rptObj.ui.lists.icons(items)
      items.style.css.text_align = "left"
    container.add(items)
    return container

  def slides(self, start=0, width=(100, '%'), height=(100, "%"), options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param start:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    dflt_options = {'markdown': True}
    if options is not None:
      dflt_options.update(options)
    html_slides = html.HtmlOthers.Slides(self.context.rptObj, start, width, height, dflt_options, profile)
    return html_slides
