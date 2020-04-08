
from epyk.core import html
from epyk.core.css import Defaults as Defaults_css


class Vignet(object):
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

    Usage:
    ------
    rptObj.ui.vignets.bubble({"value": 23, "title": "Title"}, helper="This is a helper")

    Related Pages:
    --------------
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

    Usage:
    ------
    number = rptObj.ui.vignets.number(500, "Test")
    number_2 = rptObj.ui.vignets.number(500, "Test 2 ", options={"url": "http://www.google.fr"})
    number.span.add_icon(rptObj.ui.icons.get.ICON_ENVELOPE)

    Related Pages:
    --------------
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
    self.context.register(html_number)
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

    Usage:
    ------
    rptObj.ui.vignets.block({"text": 'This is a brand new python framework', "title": 'New Python Web Framework',
                             "button": {"text": 'Get Started', 'url': "/getStarted"}, 'color': 'green'})

    Related Pages:
    --------------
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
    self.context.register(html_blocktext)
    return html_blocktext

  def text(self, recordSet=None, width=(None, '%'), height=(None, "px"), align='center', helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage:
    ------
    rptObj.ui.vignets.text({"title": "New Python Framework", 'value': "A new Python Web Framework", 'color': 'green',
                            'icon': 'fab fa-python', 'colorTitle': 'darkgreen'})

    Related Pages:
    --------------

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
    self.context.register(html_text)
    return html_text

  def bars(self):
    pass

  def line(self):
    pass
