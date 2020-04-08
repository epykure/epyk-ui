"""
Interface to the rich HTML components
"""

from epyk.core import html
from epyk.core.css import Defaults as Defaults_css


class Rich(object):
  def __init__(self, context):
    self.context = context

  def delta(self, rec=None, width=(200, 'px'), height=(80, 'px'), options=None, helper=None, profile=None):
    """
    Description:
    ------------

    Usage:
    ------
    rptObj.ui.rich.delta({'number': 100, 'prevNumber': 60, 'thresold1': 100, 'thresold2': 50}, helper="test")

    Related Pages:
    --------------

    Attributes:
    ----------
    :param rec:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param helper: Optional. A tooltip helper
    :param profile: Optional. A flag to set the component performance storage
    """
    dflt_options = {"decPlaces": 0, "thouSeparator": ',', "decSeparator": '.',
                    'colors': {'green': 'green', 'red': 'red', 'orange': 'orange'}}
    if options is not None:
      dflt_options.update(options)
    html_delta = html.HtmlTextComp.Delta(self.context.rptObj, rec or {}, width, height, dflt_options, helper, profile)
    self.context.register(html_delta)
    return html_delta

  def stars(self, val=None, label=None, color=None, align='left', best=5, htmlCode=None, helper=None, profile=None):
    """
    Description:
    ------------
    Entry point for the Stars component

    Usage:
    ------
    rptObj.ui.rich.stars(3, label="test", helper="This is a helper")

    stars = rptObj.ui.rich.stars(3, label="test", helper="This is a helper")
    stars.click()

    Related Pages:
    --------------
    https://www.w3schools.com/howto/howto_css_star_rating.asp

    Attributes:
    ----------
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

  def light(self, color=None, height=(None, 'px'), label=None, tooltip=None, helper=None, profile=None):
    """
    Description:
    ------------
    Add a traffic light component to give a visual status of a given process

    Usage:
    ------
    rptObj.ui.rich.light("red", label="label", tooltip="Tooltip", helper="Helper")
    rptObj.ui.rich.light(True)

    Attributes:
    ----------
    :param color:
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param label: Optional. The text of label to be added to the component
    :param tooltip: Optional. A string with the value of the tooltip
    :param helper: Optional. The filtering properties for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    if height is None or height[0] is None:
      height = (Defaults_css.Font.header_size, "px")
    if isinstance(color, bool):
      color = self.context.rptObj.theme.success[1] if color else self.context.rptObj.theme.danger[1]
    html_traffic = html.HtmlTextComp.TrafficLight(self.context.rptObj, color, label, height, tooltip, helper, profile)
    self.context.register(html_traffic)
    return html_traffic

  def prism(self, text=None, language='python', width=(100, "%"), height=(None, "px"),
            isEditable=False, trimSpaces=True, align=None, helper=None, profile=None):
    """
    Description:
    ------------

    Usage:
    ------
    rptObj.ui.rich.prism("print('test')")

    Related Pages:
    --------------
    https://www.w3schools.com/tags/tag_font.asp

    Attributes:
    ----------
    :param text:
    :param language: Optional, The language format used. Default Python
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param isEditable:
    :param trimSpaces:
    :param align:
    :param profile: Optional. A flag to set the component performance storage
    """
    html_prism = html.HtmlTextComp.Prism(self.context.rptObj, text, language, width, height, isEditable, trimSpaces, align, helper, profile)
    self.context.register(html_prism)
    return html_prism

  def info(self, text=None, options=None, profile=None):
    """
    Description:
    ------------
    Display an info icon with a tooltip

    Usage:
    ------
    rptObj.ui.info("Test")

    Related Pages:
    --------------
    https://fontawesome.com/icons/question-circle?style=solid
    https://api.jqueryui.com/tooltip/

    Attributes:
    ----------
    :param text: The content of the tooltip
    :param profile: Optional, A boolean to store the performances for each components
    """
    html_help = html.HtmlOthers.Help(self.context.rptObj, text, width=(10, "px"), profile=profile, options=options or {})
    self.context.register(html_help)
    return html_help

  def script(self, title, scriptName, clssName=None, functionName=None, docType='documentation',
             width=(100, "%"), height=(None, "px"),  color=None, profile=None):
    """
    Description:
    ------------
    Entry point to the source code component.

    Usage:
    ------
    rptObj.ui.rich.script("Documentation", "test.py")

    Attributes:
    ----------
    :param title:
    :param scriptName:
    :param clssName:
    :param functionName:
    :param docType:
    :param color:
    :param profile:
    """
    html_script = html.HtmlTextComp.DocScript(self.context.rptObj, title, scriptName, clssName, functionName,
                                            docType, width, height, color, profile)
    self.context.register(html_script)
    return html_script

  def countdown(self, yyyy_mm_dd, label=None, icon="fas fa-stopwatch", timeInMilliSeconds=1000, width=(100, '%'), height=(None, 'px'),
                htmlCode=None, helper=None, profile=None):
    """
    Description:
    ------------
    Add a countdown to the page and remove the content if the page has expired.

    Usage:
    ------
    rptObj.ui.rich.countdown("2050-09-24")

    Related Pages:
    --------------
    https://www.w3schools.com/js/js_date_methods.asp
    https://www.w3schools.com/howto/howto_js_countdown.asp
    https://fontawesome.com/icons/stopwatch?style=solid

    Attributes:
    ----------
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
    html_cd = html.HtmlDates.CountDownDate(self.context.rptObj, yyyy_mm_dd, label, icon, timeInMilliSeconds, width, height, htmlCode, helper, profile)
    self.context.register(html_cd)
    return html_cd

  def update(self, label=None, color=None, width=(100, "%"), height=(None, "px"), htmlCode=None, profile=None):
    """
    Description:
    ------------
    Last Update time component

    Usage:
    ------
    rptObj.ui.rich.update("Last update: ")

    Attributes:
    ----------
    :param label: The label to be displayed close to the date. Default Last Update
    :param color: Optional. The color code for the font
    :param width: Optional. Integer for the component width
    :param height: Optional. Integer for the component height
    :param htmlCode: Optional. The component identifier code (for both Python and Javascript)
    :param profile: Optional. A flag to set the component performance storage
    """
    html_dt = html.HtmlDates.LastUpdated(self.context.rptObj, label, color, width, height, htmlCode, profile)
    self.context.register(html_dt)
    return html_dt

  def console(self, content="", color=None, width=(100, "%"), height=(200, "px"), htmlCode=None, options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param content:
    :param color:
    :param width:
    :param height:
    :param htmlCode:
    :param options:
    :param profile:
    """
    dflt_options = {"markdown": True, "timestamp": True}
    if options is not None:
      dflt_options.update(options)
    html_div = html.HtmlTextEditor.Console(self.context.rptObj, content, color, width, height, htmlCode, None, dflt_options, profile)
    html_div.css({"border": "1px solid %s" % html_div._report.theme.greys[4], "background": html_div._report.theme.greys[2],
                  'padding': '5px'})
    self.context.register(html_div)
    return html_div
