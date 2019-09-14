"""

"""

from epyk.core import html


class Rich(object):
  def __init__(self, context):
    self.context = context

  def textbubble(self, recordSet=None, width=(100, "%"), height=(None, 'px'), color=None, size=(25, "px"),
                 background_color=None, dataSrc=None, helper=None, profile=None):
    """

    Example
    rptObj.ui.rich.textbubble({"value": 23, "title": "Title"}, helper="This is a helper")

    Documentation

    :param recordSet:
    :param width:
    :param height:
    :param color:
    :param size:
    :param background_color:
    :param dataSrc:
    :param helper:
    :param profile:
    :rtype: html.HtmlTextComp.TextBubble
    :return:
    """
    return self.context.register(html.HtmlTextComp.TextBubble(self.context.rptObj, recordSet, width, height,
                                                              color, size, background_color, dataSrc, helper, profile))

  def delta(self, recordSet=None, width=(200, 'px'), height=(80, 'px'), size=None, dataSrc=None, helper=None, profile=None):
    """

    Example
    rptObj.ui.rich.delta({'number': 100, 'prevNumber': 60, 'thresold1': 100, 'thresold2': 50}, helper="test")

    Documentation
    https://jqueryui.com/progressbar/
    https://fontawesome.com/icons?d=gallery

    :param recordSet:
    :param width:
    :param height:
    :param size:
    :param dataSrc:
    :param helper:
    :param profile:
    :rtype: html.HtmlTextComp.Delta
    :return:
    """
    return self.context.register(html.HtmlTextComp.Delta(self.context.rptObj, recordSet, width, height, size, dataSrc,
                                                         helper, profile))

  def vignet(self, recordSet=None, width=(100, '%'), height=(None, 'px'), size=(None, 'px'), colorTitle=None,
             dataSrc=None, helper=None, profile=None):
    """

    Example
    rptObj.ui.rich.vignet({'title': 'Python', 'number': 100, 'text': 'Content', 'color': 'green', 'url':
                           'https://www.python.org/', 'icon': 'fab fa-python', 'tooltip': 'Python Fondation',
                           'urlTitle': 'WebSite'})

    Documentation

    :param recordSet:
    :param width:
    :param height:
    :param size:
    :param colorTitle:
    :param dataSrc:
    :param helper:
    :param profile:
    :rtype: html.HtmlTextComp.Vignet
    :return:
    """
    size = self.context._size(size)
    return self.context.register(html.HtmlTextComp.Vignet(self.context.rptObj, recordSet, width, height,
             size, colorTitle, dataSrc, helper, profile))

  def stars(self, val=None, label=None, color=None, align='left', best=5, htmlCode=None, helper=None, profile=None):
    """

    Example
    rptObj.ui.rich.stars(3, label="test", helper="This is a helper")

    Documentation
    https://www.w3schools.com/howto/howto_css_star_rating.asp

    :param val:
    :param label:
    :param color:
    :param align:
    :param best:
    :param htmlCode:
    :param profile:

    :rtype: html.HtmlOthers.Stars

    :return:
    """
    return self.context.register(html.HtmlOthers.Stars(self.context.rptObj, val, label, color, align, best, htmlCode, helper, profile))

  def textborder(self, recordSet=None, width=(None, '%'), height=(None, "px"), size=(None, 'px'), align='center',
                 helper=None, profile=None):
    """

    Example
    rptObj.ui.rich.textborder({"title": "New Python Framework", 'value': "A new Python Web Framework", 'color': 'green',
                             'icon': 'fab fa-python', 'colorTitle': 'darkgreen'})

    Documentation

    :param recordSet:
    :param width:
    :param height:
    :param size:
    :param align:
    :param helper:
    :param profile:

    :rtype: html.HtmlTextComp.TextWithBorder

    :return:
    """
    size = self.context._size(size)
    return self.context.register(html.HtmlTextComp.TextWithBorder(self.context.rptObj, recordSet, width,
                                                                  height, size, align, helper, profile))

  def blocktext(self, recordSet=None, color=None, size=(None, 'px'), border='auto', width=(300, 'px'), height=(None, 'px'),
                helper=None, profile=None):
    """

    Example
    rptObj.ui.rich.blocktext({"text": 'This is a brand new python framework', "title": 'New Python Web Framework',
                            "button": {"text": 'Get Started', 'url': "/getStarted"}, 'color': 'green'})

    Documentation

    :param recordSet:
    :param color:
    :param size:
    :param border:
    :param width:
    :param height:
    :param helper:
    :param profile:

    :rtype: html.HtmlTextComp.BlockText

    :return:
    """
    size = self.context._size(size)
    return self.context.register(html.HtmlTextComp.BlockText(self.context.rptObj, recordSet, color, size, border, width,
                                                             height, helper, profile))

  def light(self, color=None, height=(20, 'px'), label=None, tooltip=None, dataSrc=None, helper=None, profile=None):
    """

    Example
    rptObj.ui.rich.light("red", label="label", tooltip="Tooltip", helper="Helper")

    :param color:
    :param height:
    :param label:
    :param tooltip:
    :param dataSrc:
    :param helper:
    :param profile:
    :rtype: html.HtmlTextComp.TrafficLight
    :return:
    """
    return self.context.register(html.HtmlTextComp.TrafficLight(self.context.rptObj, color, label, height,
                                                                tooltip, dataSrc, helper, profile))

  def prism(self, text=None, language='python', size=(None, 'px'), width=(100, "%"), height=(None, "px"),
            isEditable=False, trimSpaces=True, align=None, helper=None, profile=None):
    """

    Example
    rptObj.ui.rich.prism("print('test')")

    Documentation
    https://www.w3schools.com/tags/tag_font.asp

    :param text:
    :param language:
    :param size:
    :param width:
    :param height:
    :param isEditable:
    :param trimSpaces:
    :param align:
    :param profile:
    :rtype: html.HtmlTextComp.Prism
    :return:
    """
    size = self.context._size(size)
    return self.context.register(html.HtmlTextComp.Prism(self.context.rptObj, text, language, size, width,
                                                         height, isEditable, trimSpaces, align, helper, profile))

  def info(self, text=None, profile=None):
    """
    Display a info icon with a tooltip

    Example
    rptObj.ui.info("Test")

    Documentation
    https://fontawesome.com/icons/question-circle?style=solid
    https://api.jqueryui.com/tooltip/

    :param text: The content of the tooltip
    :param profile: Optional, A boolean to store the performances for each components

    :rtype: html.HtmlOthers.Help

    :return:
    """
    return self.context.register(html.HtmlOthers.Help(self.context.rptObj, text, width=(10, "px"), profile=profile))
