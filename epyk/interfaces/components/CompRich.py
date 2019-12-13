"""
Interface to the rich HTML components
"""

from epyk.core import html


class Rich(object):
  def __init__(self, context):
    self.context = context

  def textbubble(self, recordSet=None, width=(100, "%"), height=(80, 'px'), color=None, size=(25, "px"),
                 background_color=None, helper=None, profile=None):
    """

    Example
    rptObj.ui.rich.textbubble({"value": 23, "title": "Title"}, helper="This is a helper")

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

  def delta(self, rec=None, width=(200, 'px'), height=(80, 'px'), size=None, options=None, helper=None, profile=None):
    """

    Example
    rptObj.ui.rich.delta({'number': 100, 'prevNumber': 60, 'thresold1': 100, 'thresold2': 50}, helper="test")

    Documentation
    https://jqueryui.com/progressbar/
    https://fontawesome.com/icons?d=gallery

    :param rec:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param size: Optional, A tuple with a integer for the size and its unit
    :param helper: Optional. A tooltip helper
    :param profile: Optional. A flag to set the component performance storage

    :rtype: html.HtmlTextComp.Delta
    :return:
    """
    dflt_options = {"decPlaces": 0, "thouSeparator": ',', "decSeparator": '.',
                    'colors': {'green': 'green', 'red': 'red', 'orange': 'orange'}}
    if options is not None:
      dflt_options.update(options)
    return self.context.register(html.HtmlTextComp.Delta(self.context.rptObj, rec or {}, width, height, size,
                                                         dflt_options, helper, profile))

  def stars(self, val=None, label=None, color=None, align='left', best=5, htmlCode=None, helper=None, profile=None):
    """
    Entry point for the Stars component

    Example
    rptObj.ui.rich.stars(3, label="test", helper="This is a helper")

    stars = rptObj.ui.rich.stars(3, label="test", helper="This is a helper")
    stars.click()

    Documentation
    https://www.w3schools.com/howto/howto_css_star_rating.asp

    :param val:
    :param label: Optional. The text of label to be added to the component
    :param color: Optional. The font color in the component. Default inherit
    :param align:
    :param best: Optional. The max number of stars. Default 5
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    html_star = html.HtmlOthers.Stars(self.context.rptObj, val, label, color, align, best, htmlCode, helper, profile)
    self.context.register(html_star)
    return html_star

  def textborder(self, recordSet=None, width=(None, '%'), height=(None, "px"), size=(None, 'px'), align='center',
                 helper=None, profile=None):
    """

    Example
    rptObj.ui.rich.textborder({"title": "New Python Framework", 'value': "A new Python Web Framework", 'color': 'green',
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

  def light(self, color=None, height=(20, 'px'), label=None, tooltip=None, helper=None, profile=None):
    """

    Example
    rptObj.ui.rich.light("red", label="label", tooltip="Tooltip", helper="Helper")
    rptObj.ui.rich.light(True)

    :param color:
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param label: Optional. The text of label to be added to the component
    :param tooltip: Optional. A string with the value of the tooltip
    :param helper: Optional. The filtering properties for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    if isinstance(color, bool):
      color = self.context.rptObj.getColor("success", 1) if color else self.context.rptObj.getColor("danger", 1)
    html_traffic = html.HtmlTextComp.TrafficLight(self.context.rptObj, color, label, height, tooltip, helper, profile)
    self.context.register(html_traffic)
    return html_traffic

  def prism(self, text=None, language='python', size=(None, 'px'), width=(100, "%"), height=(None, "px"),
            isEditable=False, trimSpaces=True, align=None, helper=None, profile=None):
    """

    Example
    rptObj.ui.rich.prism("print('test')")

    Documentation
    https://www.w3schools.com/tags/tag_font.asp

    :param text:
    :param language: Optional, The language format used. Default Python
    :param size: Optional, A tuple with a integer for the size and its unit
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param isEditable:
    :param trimSpaces:
    :param align:
    :param profile: Optional. A flag to set the component performance storage
    """
    size = self.context._size(size)
    html_prism = html.HtmlTextComp.Prism(self.context.rptObj, text, language, size, width,
                                                         height, isEditable, trimSpaces, align, helper, profile)
    self.context.register(html_prism)
    return html_prism

  def info(self, text=None, options=None, profile=None):
    """
    Display a info icon with a tooltip

    Example
    rptObj.ui.info("Test")

    Documentation
    https://fontawesome.com/icons/question-circle?style=solid
    https://api.jqueryui.com/tooltip/

    :param text: The content of the tooltip
    :param profile: Optional, A boolean to store the performances for each components
    """
    html_help = html.HtmlOthers.Help(self.context.rptObj, text, width=(10, "px"), profile=profile, options=options or {})
    self.context.register(html_help)
    return html_help

  def script(self, title, scriptName, clssName=None, functionName=None, docType='documentation',
             width=(100, "%"), height=(None, "px"),  color=None, size=(None, 'px'), profile=None):
    """
    Entry point to the source code component.

    Example
    rptObj.ui.rich.script("Documentation", "test.py")

    :param title:
    :param scriptName:
    :param clssName:
    :param functionName:
    :param docType:
    :param color:
    :param size:
    :param profile:
    """
    size = self.context._size(size)
    html_script = html.HtmlTextComp.DocScript(self.context.rptObj, title, scriptName, clssName, functionName,
                                            docType, width, height, color, size, profile)
    self.context.register(html_script)
    return html_script

  def number(self, number, label="", size=(None, 'px'), width=(100, "px"), height=(None, "px"), profile=None, options=None):
    """

    Example
    number = rptObj.ui.rich.number(500, "Test")
    number_2 = rptObj.ui.rich.number(500, "Test 2 ", options={"url": "http://www.google.fr"})
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

  def countdown(self, yyyy_mm_dd, label=None, icon="fas fa-stopwatch", timeInMilliSeconds=1000, width=(100, '%'), height=(None, 'px'),
                htmlCode=None, size=(None, 'px'), helper=None, profile=None):
    """
    Add a countdown to the page and remove the content if the page has expired.

    Example
    rptObj.ui.rich.countdown("2050-09-24")

    Documentation
    https://www.w3schools.com/js/js_date_methods.asp
    https://www.w3schools.com/howto/howto_js_countdown.asp
    https://fontawesome.com/icons/stopwatch?style=solid

    :param yyyy_mm_dd: The end date in format YYYY-MM-DD
    :param label: Optional. The component label content
    :param icon: Optional. The component icon content from font-awesome references
    :param timeInMilliSeconds:
    :param width: Optional. Integer for the component width
    :param height: Optional. Integer for the component height
    :param htmlCode: Optional. The component identifier code (for both Python and Javascript)
    :param helper: Optional. A tooltip helper
    :param profile: Optional. A flag to set the component performance storage
    """
    size = self.context._size(size)
    html_cd = html.HtmlDates.CountDownDate(self.context.rptObj, yyyy_mm_dd, label, icon, timeInMilliSeconds, width, height, htmlCode, helper, profile)
    self.context.register(html_cd)
    return html_cd

  def update(self, label=None, size=(None, 'px'), color=None, width=(100, "%"), height=(None, "px"), htmlCode=None, profile=None):
    """
    Last Update time component

    Example
    rptObj.ui.rich.update("Last update: ")

    :param label: The label to be displayed close to the date. Default Last Update
    :param size: Optional, A integer to set the font-size
    :param color: Optional. The color code for the font
    :param width: Optional. Integer for the component width
    :param height: Optional. Integer for the component height
    :param htmlCode: Optional. The component identifier code (for both Python and Javascript)
    :param profile: Optional. A flag to set the component performance storage
    """
    size = self.context._size(size)
    html_dt = html.HtmlDates.LastUpdated(self.context.rptObj, label, size, color, width, height, htmlCode, profile)
    self.context.register(html_dt)
    return html_dt
