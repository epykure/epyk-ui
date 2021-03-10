#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core import html
from epyk.core.css import Defaults as Defaults_css
from epyk.interfaces import Arguments
from epyk.core.css import Colors


class Rich:

  def __init__(self, ui):
    self.page = ui.page

  @html.Html.css_skin()
  def delta(self, rec=None, width=('auto', ''), height=('auto', ''), options=None, helper=None, profile=None):
    """
    Description:
    ------------

    Usage:
    -----

      page.ui.rich.delta({'number': 100, 'prevNumber': 60, 'thresold1': 100, 'thresold2': 50}, helper="test")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextComp.Delta`

    Attributes:
    ----------
    :param rec:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param options:
    :param helper: Optional. A tooltip helper
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    dflt_options = {"digits": 0, 'thousand_sep': ",", 'decimal_sep': ".",
                    'red': self.page.theme.danger[1], 'green': self.page.theme.success[1],
                    'orange': self.page.theme.warning[1]}
    if options is not None:
      dflt_options.update(options)
    html_delta = html.HtmlTextComp.Delta(self.page, rec or {}, width, height, dflt_options, helper, profile)
    return html_delta

  @html.Html.css_skin()
  def stars(self, val=None, label=None, color=None, align='left', best=5, html_code=None, helper=None, profile=None):
    """
    Description:
    ------------
    Entry point for the Stars component

    Usage:
    -----

      page.ui.rich.stars(3, label="test", helper="This is a helper")
      stars = page.ui.rich.stars(3, label="test", helper="This is a helper")
      stars.click()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlOthers.Stars`

    Related Pages:

      https://www.w3schools.com/howto/howto_css_star_rating.asp

    Attributes:
    ----------
    :param val:
    :param label: String. Optional. The text of label to be added to the component
    :param color: String. Optional. The font color in the component. Default inherit
    :param align: String. Optional. A string with the horizontal position of the component
    :param best: Optional. The max number of stars. Default 5
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    html_star = html.HtmlOthers.Stars(self.page, val, label, color, align, best, html_code, helper, profile)
    return html_star

  @html.Html.css_skin()
  def light(self, color=None, height=(None, 'px'), label=None, tooltip=None, helper=None, profile=None):
    """
    Description:
    ------------
    Add a traffic light component to give a visual status of a given process

    Usage:
    -----

      page.ui.rich.light("red", label="label", tooltip="Tooltip", helper="Helper")
      page.ui.rich.light(True)

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextComp.TrafficLight`

    Attributes:
    ----------
    :param color:
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param label: Optional. The text of label to be added to the component
    :param tooltip: Optional. A string with the value of the tooltip
    :param helper: Optional. The filtering properties for this component
    :param profile: Boolean | Dictionary.Optional. A flag to set the component performance storage
    """
    height = Arguments.size(height, unit="px")
    if height is None or height[0] is None:
      height = (Defaults_css.Font.header_size, "px")
    if isinstance(color, bool):
      color = self.page.theme.success[1] if color else self.page.theme.danger[1]
    html_traffic = html.HtmlTextComp.TrafficLight(self.page, color, label, height, tooltip, helper, profile)
    return html_traffic

  @html.Html.css_skin()
  def info(self, text=None, options=None, profile=None):
    """
    Description:
    ------------
    Display an info icon with a tooltip

    Usage:
    -----

      page.ui.info("Test")

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlOthers.Help`

    Related Pages:

      https://fontawesome.com/icons/question-circle?style=solid
      https://api.jqueryui.com/tooltip/

    Attributes:
    ----------
    :param text: String. Optional. The content of the tooltip
    :param profile: Boolean | Dictionary.Optional, A boolean to store the performances for each components
    """
    html_help = html.HtmlOthers.Help(self.page, text, width=(10, "px"), profile=profile, options=options or {})
    return html_help

  @html.Html.css_skin()
  def countdown(self, day, month, year, hour=0, minute=0, second=0, label=None, icon="fas fa-stopwatch", timeInMilliSeconds=1000, width=(100, '%'), height=(None, 'px'),
                html_code=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------
    Add a countdown to the page and remove the content if the page has expired.

    Usage:
    -----

      page.ui.rich.countdown("2050-09-24")

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
    :param html_code: Optional. The component identifier code (for both Python and Javascript)
    :param helper: Optional. A tooltip helper
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_cd = html.HtmlDates.CountDownDate(self.page, day, month, year, hour, minute, second, label, icon, timeInMilliSeconds, width, height, html_code, helper, options or {}, profile)
    return html_cd

  @html.Html.css_skin()
  def update(self, label=None, color=None, width=(100, "%"), height=(None, "px"), html_code=None, profile=None):
    """
    Description:
    ------------
    Last Update time component.

    Usage:
    -----

      page.ui.rich.update("Last update: ")

      update = page.ui.rich.update()
      page.ui.button("Click").click([update.refresh()])

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
    :param html_code: Optional. The component identifier code (for both Python and Javascript)
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_dt = html.HtmlDates.LastUpdated(self.page, label, color, width, height, html_code, profile)
    return html_dt

  @html.Html.css_skin()
  def console(self, content="", width=(100, "%"), height=(200, "px"), html_code=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage:
    -----

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextEditor.Console`

    Templates:

        https://github.com/epykure/epyk-templates/blob/master/locals/components/checkbox.py

    Attributes:
    ----------
    :param content:
    :param width:
    :param height:
    :param html_code:
    :param options:
    :param profile: Boolean | Dictionary.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {"markdown": False, "timestamp": True}
    if options is not None:
      dflt_options.update(options)
    html_div = html.HtmlTextEditor.Console(self.page, content, width, height, html_code, None, dflt_options, profile)
    html_div.css({"border": "1px solid %s" % html_div._report.theme.greys[4], "background": html_div._report.theme.greys[2],
                  'padding': '5px'})
    return html_div

  @html.Html.css_skin()
  def search_input(self, text='', placeholder='Search..', color=None, width=(100, '%'), height=(None, "px"),
                   html_code=None, tooltip=None, extensible=False, options=None, profile=None):
    """
    Description:
    ------------

    Usage:
    -----

      page.ui.inputs.search()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlInput.Search`

    Related Pages:

      https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_anim_search

    Attributes:
    ----------
    :param text:
    :param placeholder:
    :param color:
    :param width:
    :param height:
    :param html_code:
    :param tooltip:
    :param extensible:
    :param profile:
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    dflt_options = {"icon": "fas fa-search", 'position': 'left', 'select': True, "border": 1}
    if options is not None:
      dflt_options.update(options)
    html_s = html.HtmlInput.Search(self.page, text, placeholder, color, width, height, html_code, tooltip,
                                   extensible, dflt_options, profile)
    return html_s

  @html.Html.css_skin()
  def search_results(self, records=None, results_per_page=20, width=(100, "%"), height=(None, "px"), options=None,
                     profile=None):
    """
    Description:
    ------------

    Usage:
    -----

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextComp.SearchResult`

    Attributes:
    ----------
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    records = records or []
    html_help = html.HtmlTextComp.SearchResult(self.page, records, pageNumber=results_per_page, width=width, height=height, profile=profile, options=options or {})
    return html_help

  @html.Html.css_skin()
  def composite(self, schema, width=(None, "%"), height=(None, "px"), html_code=None, helper=None, options=None,
                profile=None):
    """
    Description:
    ------------
    Composite bespoke object.

    This object will be built based on its schema. No specific CSS Style and class will be added to this object.
    The full definition will be done in the nested dictionary schema.

    Usage:
    -----

      schema = {'type': 'div', 'css': {}, 'class': , 'attrs': {} 'arias': {},  'children': [
          {'type': : {...}}
          ...
      ]}

    Attributes:
    ----------
    :param schema:
    :param width:
    :param height:
    :param html_code:
    :param helper:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    html_help = html.HtmlTextComp.Composite(self.page, schema, width=width, height=height, html_code=html_code, profile=profile, options=options or {}, helper=helper)
    return html_help

  @html.Html.css_skin()
  def status(self, status, width=(None, "%"), height=(None, "px"), html_code=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param status:
    :param width:
    :param height:
    :param html_code:
    :param profile:
    :param options:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    dflt_options = {'states': {"Done": 'green', 'In Progress': 'orange', 'Blocked': 'red'}}
    if options is not None:
      dflt_options.update(options)
    html_help = html.HtmlTextComp.Status(self.page, status, width=width, height=height, html_code=html_code, profile=profile, options=dflt_options)
    return html_help

  @html.Html.css_skin()
  def markdown(self, text="", width=("cacl(100% - 10px)", ''), height=("auto", ''), html_code=None, options=None,
               profile=None):
    """
    Description:
    ------------

    Usage:
    -----

      page.ui.inputs.editor()

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlTextEditor.Editor`

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/markdown.py

    Attributes:
    ----------
    :param text:
    :param width:
    :param height:
    :param html_code:
    :param options:
    :param profile:
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="%")
    dflt_options = {"markdown": True}
    if options is not None:
      dflt_options.update(options)
    md = html.HtmlTextEditor.MarkdownReader(self.page, text, width, height, html_code, dflt_options, profile)
    md.style.css.margin_left = 5
    md.style.css.margin_right = 5
    md.style.css.padding = 5
    return md

  @html.Html.css_skin()
  def adv_text(self, section, title, content, background=""):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param section:
    :param title:
    :param content:
    """
    container = self.page.ui.div()
    if section is not None:
      text = self.page.ui.text(section, width=(100, '%'))
      text.style.css.text_align = "center"
      text.style.css.font_size = Defaults_css.font(-1)
      text.style.css.line_height = Defaults_css.font(5)
      text.style.css.font_weight = 500
      text.style.css.letter_spacing = "0.15em"
      text.style.css.text_transform = "uppercase"
      container.add(text)

    if title is not None:
      title = self.page.ui.text(title, width=(100, '%'))
      title.style.css.text_align = "center"
      title.style.css.font_size = Defaults_css.font(12)
      title.style.css.font_weight = 300
      title.css({'margin-block-end': '0.67em', 'margin-block-start': '0'})
      container.add(title)

    if content is not None:
      content = self.page.ui.text(content, width=(80, "%"))
      content.style.css.text_align = "center"
      content.style.css.font_size = Defaults_css.font(2)
      content.style.css.margin = "auto"

    container.add(content)
    # container0.style.css.border = "10px solid white"
    container.style.css.text_align = "center"
    container.style.css.background = background
    container.style.css.padding = 10
    return container

  @html.Html.css_skin()
  def color(self, code, content="data copied to clipboard", width=(20, 'px'), height=(20, 'px'), options=None):
    """
    Description:
    ------------
    Color component

    Usage:
    -----

    Attributes:
    ----------
    :param code: Tuple or String. The color code
    :param content:
    :param width:
    :param height:
    :param options:
    """
    dflt_options = {"type": 'rgb', 'popup_timers': 1000}
    if options is not None:
      dflt_options.update(options)
    if dflt_options.get("type") == 'hex' or str(code).startswith("#"):
      code = Colors.getHexToRgb(code)
    d = self.page.ui.div(width=width, height=height)
    d.style.css.display = "inline-block"
    d.style.css.border = "1px solid %s" % self.page.theme.greys[0]
    d.tooltip("rgb: %s, hex: %s" % (code, Colors.getRgbToHex(code)))
    d.style.css.cursor = "pointer"
    d.click([
      self.page.js.clipboard(Colors.getRgbToHex(code)),
      self.page.js.print(content,  dflt_options.get('popup_timers'), dflt_options.get('popup_css'))])
    d.style.css.background = "rgb(%s, %s, %s)" % (code[0], code[1], code[2])
    return d

  @html.Html.css_skin()
  def elapsed(self, day=None, month=None, year=None, label=None, icon=None, width=(None, "px"), height=(None, "px"),
              html_code=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage:
    -----

    Attributes:
    ----------
    :param day:
    :param month:
    :param year:
    :param label:
    :param icon:
    :param width:
    :param height:
    :param html_code:
    :param helper:
    :param options:
    :param profile:
    """
    options = options or {}
    md = html.HtmlDates.Elapsed(
      self.page, day, month, year, label, icon, width, height, html_code, helper, options, profile)
    return md

  @html.Html.css_skin()
  def powered(self, by=None):
    """
    Description:
    ------------
    Display badges for the specifies JavaScript modules.

    Tip: If by is None. This will display only the main JavaScript module with the current version.
    It will not display the underlying components.

    This component needs to be called at the end to ensure all the imported will be registered.

    Attributes:
    ----------
    :param by: List. Optional. Name of JavaScript library aliases.
    """
    container = self.page.ui.div()
    container.style.css.font_factor(-4)
    if by is None:
      by = sorted(list(self.page.jsImports))
    for i, b in enumerate(by):
      if b in self.page.imports.jsImports:
        badge = self.page.ui.div([
          self.page.ui.text(b.capitalize()),
          self.page.ui.text("v%s" % self.page.imports.jsImports[b]["versions"][0])], width="auto")
        badge[0].style.css.margin_right = 5
        badge[0].goto(self.page.imports.website(b), target="_blank")
        badge[0].style.css.background = self.page.theme.charts[i]
        badge[0].style.css.color = "white"
        badge[0].style.css.text_shadow = "1px 1px black"
        badge[0].style.css.padding = "0 5px"
        badge[0].style.css.border_right = "1px solid black"
        badge[1].style.css.padding = "0 5px 0 0"
        badge.style.css.border = "1px solid black"
        badge.style.css.margin = 2
        badge.style.css.border_radius = "0 10px 10px 0"
        container.add(badge)
    return container
