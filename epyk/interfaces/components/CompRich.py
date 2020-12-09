#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core import html
from epyk.core.css import Defaults as Defaults_css
from epyk.interfaces import Arguments
from epyk.core.css import Colors


class Rich(object):

  def __init__(self, context):
    self.context = context

  def delta(self, rec=None, width=('auto', ''), height=('auto', ''), options=None, helper=None, profile=None):
    """
    Description:
    ------------

    Usage::

      rptObj.ui.rich.delta({'number': 100, 'prevNumber': 60, 'thresold1': 100, 'thresold2': 50}, helper="test")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextComp.Delta`

    Attributes:
    ----------
    :param rec:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param helper: Optional. A tooltip helper
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    dflt_options = {"digits": 0, 'thousand_sep': ",", 'decimal_sep': ".",
                    'red': self.context.rptObj.theme.danger[1], 'green': self.context.rptObj.theme.success[1],
                    'orange': self.context.rptObj.theme.warning[1]}
    if options is not None:
      dflt_options.update(options)
    html_delta = html.HtmlTextComp.Delta(self.context.rptObj, rec or {}, width, height, dflt_options, helper, profile)
    return html_delta

  def stars(self, val=None, label=None, color=None, align='left', best=5, htmlCode=None, helper=None, profile=None):
    """
    Description:
    ------------
    Entry point for the Stars component

    Usage::

      rptObj.ui.rich.stars(3, label="test", helper="This is a helper")
      stars = rptObj.ui.rich.stars(3, label="test", helper="This is a helper")
      stars.click()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlOthers.Stars`

    Related Pages:

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
    return html_star

  def light(self, color=None, height=(None, 'px'), label=None, tooltip=None, helper=None, profile=None):
    """
    Description:
    ------------
    Add a traffic light component to give a visual status of a given process

    Usage::

      rptObj.ui.rich.light("red", label="label", tooltip="Tooltip", helper="Helper")
      rptObj.ui.rich.light(True)

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextComp.TrafficLight`

    Attributes:
    ----------
    :param color:
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param label: Optional. The text of label to be added to the component
    :param tooltip: Optional. A string with the value of the tooltip
    :param helper: Optional. The filtering properties for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    height = Arguments.size(height, unit="px")
    if height is None or height[0] is None:
      height = (Defaults_css.Font.header_size, "px")
    if isinstance(color, bool):
      color = self.context.rptObj.theme.success[1] if color else self.context.rptObj.theme.danger[1]
    html_traffic = html.HtmlTextComp.TrafficLight(self.context.rptObj, color, label, height, tooltip, helper, profile)
    return html_traffic

  def info(self, text=None, options=None, profile=None):
    """
    Description:
    ------------
    Display an info icon with a tooltip

    Usage::

      rptObj.ui.info("Test")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlOthers.Help`

    Related Pages:

      https://fontawesome.com/icons/question-circle?style=solid
      https://api.jqueryui.com/tooltip/

    Attributes:
    ----------
    :param text: The content of the tooltip
    :param profile: Optional, A boolean to store the performances for each components
    """
    html_help = html.HtmlOthers.Help(self.context.rptObj, text, width=(10, "px"), profile=profile, options=options or {})
    return html_help

  def countdown(self, day, month, year, hour=0, minute=0, second=0, label=None, icon="fas fa-stopwatch", timeInMilliSeconds=1000, width=(100, '%'), height=(None, 'px'),
                htmlCode=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------
    Add a countdown to the page and remove the content if the page has expired.

    Usage::

      rptObj.ui.rich.countdown("2050-09-24")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlDates.CountDownDate`

    Related Pages:

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
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_cd = html.HtmlDates.CountDownDate(self.context.rptObj, day, month, year, hour, minute, second, label, icon, timeInMilliSeconds, width, height, htmlCode, helper, options or {}, profile)
    return html_cd

  def update(self, label=None, color=None, width=(100, "%"), height=(None, "px"), htmlCode=None, profile=None):
    """
    Description:
    ------------
    Last Update time component

    Usage::

      rptObj.ui.rich.update("Last update: ")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlDates.LastUpdated`

    Related Pages:

        https://github.com/epykure/epyk-templates/blob/master/locals/components/calendar.py

    Attributes:
    ----------
    :param label: The label to be displayed close to the date. Default Last Update
    :param color: Optional. The color code for the font
    :param width: Optional. Integer for the component width
    :param height: Optional. Integer for the component height
    :param htmlCode: Optional. The component identifier code (for both Python and Javascript)
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_dt = html.HtmlDates.LastUpdated(self.context.rptObj, label, color, width, height, htmlCode, profile)
    return html_dt

  def console(self, content="", width=(100, "%"), height=(200, "px"), htmlCode=None, options=None, profile=None):
    """
    Description:
    ------------

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextEditor.Console`

    Templates:

        https://github.com/epykure/epyk-templates/blob/master/locals/components/checkbox.py

    Attributes:
    ----------
    :param content:
    :param width:
    :param height:
    :param htmlCode:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"markdown": False, "timestamp": True}
    if options is not None:
      dflt_options.update(options)
    html_div = html.HtmlTextEditor.Console(self.context.rptObj, content, width, height, htmlCode, None, dflt_options, profile)
    html_div.css({"border": "1px solid %s" % html_div._report.theme.greys[4], "background": html_div._report.theme.greys[2],
                  'padding': '5px'})
    return html_div

  def search_input(self, text='', placeholder='Search..', color=None, height=(None, "px"), htmlCode=None,
                   tooltip=None, extensible=False, options=None, profile=None):
    """
    Description:
    ------------

    Usage::

      rptObj.ui.inputs.search()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.Search`

    Related Pages:

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
    height = Arguments.size(height, unit="px")
    html_s = html.HtmlInput.Search(self.context.rptObj, text, placeholder, color, height, htmlCode, tooltip,
                                   extensible, options or {}, profile)
    return html_s

  def search_results(self, records=None, results_per_page=20, width=(100, "%"), height=(None, "px"), options=None, profile=None):
    """
    Description:
    ------------

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextComp.SearchResult`

    Attributes:
    ----------
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    records = records or []
    html_help = html.HtmlTextComp.SearchResult(self.context.rptObj, records, pageNumber=results_per_page, width=width, height=height, profile=profile, options=options or {})
    return html_help

  def composite(self, schema, width=(None, "%"), height=(None, "px"), htmlCode=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------
    Composite bespoke object.

    This obhect will be built based on its schema. No specific CSS Style and class will be added to this object.
    The full definition will be done in the nested dictionary schema.

    Example
    schema = {'type': 'div', 'css': {}, 'class': , 'attrs': {} 'arias': {},  'children': [
        {'type': : {...}}
        ...
    ]}

    Attributes:
    ----------
    :param schema:
    :param width:
    :param height:
    :param htmlCode:
    :param helper:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_help = html.HtmlTextComp.Composite(self.context.rptObj, schema, width=width, height=height, htmlCode=htmlCode, profile=profile, options=options or {}, helper=helper)
    return html_help

  def status(self, status, width=(None, "%"), height=(None, "px"), htmlCode=None, options=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param status:
    :param width:
    :param height:
    :param htmlCode:
    :param profile:
    :param options:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {'states': {"Done": 'green', 'In Progress': 'orange', 'Blocked': 'red'}}
    if options is not None:
      dflt_options.update(options)
    html_help = html.HtmlTextComp.Status(self.context.rptObj, status, width=width, height=height, htmlCode=htmlCode, profile=profile, options=dflt_options)
    return html_help

  def markdown(self, text="", width=("cacl(100% - 10px)", ''), height=("auto", ''), htmlCode=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::

      rptObj.ui.inputs.editor()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextEditor.Editor`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/markdown.py

    Attributes:
    ----------
    :param text:
    :param width:
    :param height:
    :param htmlCode:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="%")
    dflt_options = {"markdown": True}
    if options is not None:
      dflt_options.update(options)
    md = html.HtmlTextEditor.MarkdownReader(self.context.rptObj, text, width, height, htmlCode, dflt_options, profile)
    md.style.css.margin_left = 5
    md.style.css.margin_right = 5
    md.style.css.padding = 5
    return md

  def adv_text(self, section, title, content, background=""):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param section:
    :param title:
    :param content:
    :return:
    """
    container = self.context.rptObj.ui.div()
    if section is not None:
      text = self.context.rptObj.ui.text(section, width=(100, '%'))
      text.style.css.text_align = "center"
      text.style.css.font_size = Defaults_css.font(-1)
      text.style.css.line_height = Defaults_css.font(5)
      text.style.css.font_weight = 500
      text.style.css.letter_spacing = "0.15em"
      text.style.css.text_transform = "uppercase"
      container.add(text)

    if title is not None:
      title = self.context.rptObj.ui.text(title, width=(100, '%'))
      title.style.css.text_align = "center"
      title.style.css.font_size = Defaults_css.font(12)
      title.style.css.font_weight = 300
      title.css({'margin-block-end': '0.67em', 'margin-block-start': '0'})
      container.add(title)

    if content is not None:
      content = self.context.rptObj.ui.text(content, width=(80, "%"))
      content.style.css.text_align = "center"
      content.style.css.font_size = Defaults_css.font(2)
      content.style.css.margin = "auto"

    container.add(content)
    # container0.style.css.border = "10px solid white"
    container.style.css.text_align = "center"
    container.style.css.background = background
    container.style.css.padding = 10
    return container

  def color(self, code, content="data copied to clipboard", width=(20, 'px'), height=(20, 'px'), options=None):
    """
    Description:
    ------------
    Color component

    Attributes:
    ----------
    :param code: Tuple or String. The color code
    :param width:
    :param height:
    :param options:
    """
    dflt_options = {"type": 'rgb', 'popup_timers': 1000}
    if options is not None:
      dflt_options.update(options)
    if dflt_options.get("type") == 'hex' or str(code).startswith("#"):
      code = Colors.getHexToRgb(code)
    d = self.context.rptObj.ui.div(width=width, height=height)
    d.style.css.display = "inline-block"
    d.style.css.border = "1px solid %s" % self.context.rptObj.theme.greys[0]
    d.tooltip("rgb: %s, hex: %s" % (code, Colors.getRgbToHex(code)))
    d.style.css.cursor = "pointer"
    d.click([
      self.context.rptObj.js.clipboard(Colors.getRgbToHex(code)),
      self.context.rptObj.js.print(content,  dflt_options.get('popup_timers'), dflt_options.get('popup_css'))])
    d.style.css.background = "rgb(%s, %s, %s)" % (code[0], code[1], code[2])
    return d

  def elapsed(self, day=None, month=None, year=None, label=None, icon=None, width=(None, "px"), height=(None, "px"),
              htmlCode=None, helper=None, options=None, profile=None):
    """

    :param day:
    :param month:
    :param year:
    :param label:
    :param icon:
    :param width:
    :param height:
    :param htmlCode:
    :param helper:
    :param options:
    :param profile:
    """
    md = html.HtmlDates.Elapsed(self.context.rptObj, day, month, year, label, icon, width, height, htmlCode, helper, options or {}, profile)
    return md
