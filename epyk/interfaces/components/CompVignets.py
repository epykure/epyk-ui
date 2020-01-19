"""
Interface to the Vignets HTML components
"""

from epyk.core import html
from epyk.core.css import Defaults as Defaults_css


class Vignet(object):
  def __init__(self, context):
    self.context = context

  def bubble(self, recordSet=None, width=(100, "%"), height=(80, 'px'), color=None, size=(25, "px"),
             background_color=None, helper=None, profile=None):
    """

    Example
    rptObj.ui.vignets.bubble({"value": 23, "title": "Title"}, helper="This is a helper")

    Documentation

    :param recordSet:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param color: Optional. The font color in the component. Default inherit
    :param size: Optional, A tuple with a integer for the size and its unit
    :param background_color:
    :param helper: Optional. A tooltip helper
    :param profile: Optional. A flag to set the component performance storage
    """
    html_bubble = html.HtmlTextComp.TextBubble(self.context.rptObj, recordSet or {}, width, height, color, size,
                                               background_color, helper, profile)
    self.context.register(html_bubble)
    return html_bubble

  def number(self, number, label="", size=(None, 'px'), width=(100, "px"), height=(None, "px"), profile=None, options=None):
    """

    Example
    number = rptObj.ui.vignets.number(500, "Test")
    number_2 = rptObj.ui.vignets.number(500, "Test 2 ", options={"url": "http://www.google.fr"})
    number.span.add_icon(rptObj.ui.icons.get.ICON_ENVELOPE)

    :param number:
    :param label:
    :param size:
    :param width:
    :param height:
    :param profile:
    """
    size = self.context._size(size)
    html_number = html.HtmlTextComp.Number(self.context.rptObj, number, label, size, width, height, profile, options or {})
    self.context.register(html_number)
    return html_number

  def link(self):
    pass

  def block(self, recordSet=None, color=None, size=(None, 'px'), border='auto', width=(300, 'px'), height=(None, 'px'),
            helper=None, profile=None):
    """

    Example
    rptObj.ui.vignets.block({"text": 'This is a brand new python framework', "title": 'New Python Web Framework',
                             "button": {"text": 'Get Started', 'url': "/getStarted"}, 'color': 'green'})

    Documentation

    :param recordSet:
    :param color: Optional. The font color in the component. Default inherit
    :param size: Optional. The font size in the component. Default 12px
    :param border:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param helper: Optional. A tooltip helper
    :param profile: Optional. A flag to set the component performance storage
    """
    size = self.context._size(size)
    html_blocktext = html.HtmlTextComp.BlockText(self.context.rptObj, recordSet, color, size, border, width, height, helper, profile)
    self.context.register(html_blocktext)
    return html_blocktext

  def text(self, recordSet=None, width=(None, '%'), height=(None, "px"), size=(None, 'px'), align='center',
           helper=None, profile=None):
    """

    Example
    rptObj.ui.vignets.text({"title": "New Python Framework", 'value': "A new Python Web Framework", 'color': 'green',
                            'icon': 'fab fa-python', 'colorTitle': 'darkgreen'})

    Documentation

    :param recordSet:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param size: Optional, A tuple with a integer for the size and its unit
    :param align:
    :param helper: Optional. A tooltip helper
    :param profile: Optional. A flag to set the component performance storage
    """
    size = self.context._size(size)
    html_text = html.HtmlTextComp.TextWithBorder(self.context.rptObj, recordSet, width, height, size, align, helper, profile)
    self.context.register(html_text)
    return html_text

  def bars(self):
    pass

  def line(self):
    pass
