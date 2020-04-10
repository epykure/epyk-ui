
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
    dflt_options = {"digits": 0, 'thousand_sep': ",", 'decimal_sep': ".",
                    'red': self.context.rptObj.theme.danger[1], 'green': self.context.rptObj.theme.success[1],
                    'orange': self.context.rptObj.theme.warning[1]}
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

  def console(self, content="", width=(100, "%"), height=(200, "px"), htmlCode=None, options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param content:
    :param width:
    :param height:
    :param htmlCode:
    :param options:
    :param profile:
    """
    dflt_options = {"markdown": False, "timestamp": True}
    if options is not None:
      dflt_options.update(options)
    html_div = html.HtmlTextEditor.Console(self.context.rptObj, content, width, height, htmlCode, None, dflt_options, profile)
    html_div.css({"border": "1px solid %s" % html_div._report.theme.greys[4], "background": html_div._report.theme.greys[2],
                  'padding': '5px'})
    self.context.register(html_div)
    return html_div

  def search_input(self, text='', placeholder='Search..', color=None, height=(None, "px"), htmlCode=None,
                   tooltip=None, extensible=False, profile=None):
    """
    Description:
    ------------

    Usage:
    ------
    rptObj.ui.inputs.search()

    Related Pages:
    --------------
    https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_anim_search

    Attributes:
    ----------
    :param text:
    :param placeholder:
    :param color:
    :param height:
    :param htmlCode:
    :param tooltip:
    :param extensible:
    :param profile:
    """
    html_s = html.HtmlInput.Search(self.context.rptObj, text, placeholder, color, height, htmlCode, tooltip,
                                   extensible, profile)
    self.context.register(html_s)
    return html_s

  def search_results(self, records=None, results_per_page=20, width=(100, "%"), height=(None, "px"), options=None, profile=None):
    """
    Description:
    ------------

    Usage:
    ------

    Related Pages:
    --------------

    Attributes:
    ----------
    """
    records = records or []
    html_help = html.HtmlTextComp.SearchResult(self.context.rptObj, records, pageNumber=results_per_page, width=width, height=height, profile=profile, options=options or {})
    self.context.register(html_help)
    return html_help
