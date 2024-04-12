#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core import html
from epyk.core.py import types
from epyk.interfaces import Arguments
from epyk.core.css import Colors
from epyk.core.js import Imports


class Rich:

    def __init__(self, ui):
        self.page = ui.page

    def delta(self, record=None, components=None, title: str = None, align: str = "center",
              width: types.SIZE_TYPE = ('auto', ''), height: types.SIZE_TYPE = ('auto', ''),
              options: types.OPTION_TYPE = None, helper: str = None,
              profile: types.PROFILE_TYPE = None):
        """

        Usage::

          page.ui.rich.delta({'number': 100, 'prevNumber': 60, 'thresold1': 100, 'thresold2': 50}, helper="test")

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlTextComp.Delta`

        :tags: Numbers |
        :categories: Container |

        :param record: Optional. The input data for this component
        :param components: Optional. The HTML components to be added to this component
        :param title: Optional. A panel title. This will be attached to the title property
        :param align: The text-align property within this component
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param options: Optional. Specific Python options available for this component
        :param helper: Optional. A tooltip helper
        :param profile: Optional. A flag to set the component performance storage
        """
        width = Arguments.size(width, unit="px")
        height = Arguments.size(height, unit="px")
        dfl_options = {"digits": 0, 'thousand_sep': ",", 'decimal_sep': ".",
                       'red': self.page.theme.danger.base, 'green': self.page.theme.success.base,
                       'orange': self.page.theme.warning.base}
        if options is not None:
            dfl_options.update(options)
        container = self.page.ui.div(align=align, height=height, width=width, profile=profile, options=options)

        if title is not None:
            if not hasattr(title, 'options'):
                title = self.page.ui.titles.title(title)
                title.style.css.display = "block"
                title.style.css.text_align = align
            container.add(title)
        main_component = html.HtmlTextComp.Delta(
            self.page, record or {}, components, width, ("auto", ''), dfl_options, helper, profile)
        container.add(main_component)
        container.build = main_component.build
        if title is not None:
            container.title = title
        html.Html.set_component_skin(container)
        return container

    def stars(self, val=None, label: str = None, color: str = None, align: str = 'left', best: int = 5,
              html_code: str = None, helper: str = None, options: types.OPTION_TYPE = None,
              profile: types.PROFILE_TYPE = None) -> html.HtmlOthers.Stars:
        """Entry point for the Stars component.

        :tags:
        :categories:

        Usage::

          page.ui.rich.stars(3, label="test", helper="This is a helper")
          stars = page.ui.rich.stars(3, label="test", helper="This is a helper")
          stars.click()

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlOthers.Stars`

        `w3schools <https://www.w3schools.com/howto/howto_css_star_rating.asp>`_

        :param val: Optional. Number of stars
        :param label: Optional. The text of label to be added to the component
        :param color: Optional. The font color in the component. Default inherit
        :param align: Optional. A string with the horizontal position of the component
        :param best: Optional. The max number of stars. Default 5
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param options: Optional. Specific Python options available for this component
        :param helper: Optional. The value to be displayed to the helper icon
        :param profile: Optional. A flag to set the component performance storage
        """
        html_star = html.HtmlOthers.Stars(self.page, val, label, color, align, best, html_code, helper, options, profile)
        html.Html.set_component_skin(html_star)
        return html_star

    def light(self, color: str = None, height: types.SIZE_TYPE = (None, 'px'), label: str = None, align: str = "left",
              tooltip: str = None, helper: str = None, html_code: str = None, options: types.OPTION_TYPE = None,
              profile: types.PROFILE_TYPE = None):
        """Add a traffic light component to give a visual status of a given process.

        :tags:
        :categories:

        Usage::

          page.ui.rich.light("red", label="label", tooltip="Tooltip", helper="Helper")
          page.ui.rich.light(True)

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlTextComp.TrafficLight`

        :param color: Optional. A hexadecimal color code
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param label: Optional. The text of label to be added to the component
        :param align: Optional. A string with the horizontal position of the component
        :param tooltip: Optional. A string with the value of the tooltip
        :param helper: Optional. The filtering properties for this component
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        height = Arguments.size(height, unit="px")
        if height is None or height[0] is None:
            height = (self.page.body.style.globals.font.size, "px")
        if isinstance(color, bool):
            color = self.page.theme.success.base if color else self.page.theme.danger.base
        html_traffic = html.HtmlTextComp.TrafficLight(self.page, color, label, height, tooltip, helper, options,
                                                      profile, html_code=html_code)
        if align == "center":
            html_traffic.style.css.margin = "auto"
            html_traffic.style.css.display = "block"
        html.Html.set_component_skin(html_traffic)
        return html_traffic

    def info(self, text: str = None, options: types.OPTION_TYPE = None, html_code: str = None,
             profile: types.PROFILE_TYPE = None) -> html.HtmlOthers.Help:
        """Display an info icon with a tooltip.

        :tags:
        :categories:

        Usage::

          page.ui.info("Test")

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlOthers.Help`

        `fontawesome <https://fontawesome.com/icons/question-circle?style=solid>`_
        `tooltip <https://api.jqueryui.com/tooltip/>`_

        :param text: Optional. The content of the tooltip
        :param profile: Optional. A boolean to store the performances for each components
        :param options: Optional. Specific Python options available for this component
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        """
        html_help = html.HtmlOthers.Help(self.page, text, width=(10, "px"), profile=profile, options=options or {},
                                         html_code=html_code)
        html.Html.set_component_skin(html_help)
        return html_help

    def countdown(self, day, month, year, hour: int = 0, minute: int = 0, second: int = 0, label: str = None,
                  icon: str = "fas fa-stopwatch", time_ms_factor: int = 1000, width: types.SIZE_TYPE = (None, '%'),
                  height: types.SIZE_TYPE = (None, 'px'), html_code: str = None, helper: str = None,
                  options: types.OPTION_TYPE = None,
                  profile: types.PROFILE_TYPE = None) -> html.HtmlDates.CountDownDate:
        """Add a countdown to the page and remove the content if the page has expired.

        :tags:
        :categories:

        Usage::

          page.ui.rich.countdown(24, 9 2021)

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlDates.CountDownDate`

        `W3schools Date <https://www.w3schools.com/js/js_date_methods.asp>`_
        `Countdown <https://www.w3schools.com/howto/howto_js_countdown.asp>`_
        `Fontawesome <https://fontawesome.com/icons/stopwatch?style=solid>`_

        :param day: Day's number
        :param month: Month's number
        :param year: Year's number
        :param hour: Optional. Number of hours
        :param minute: Optional. Number of minutes
        :param second: Optional. Number of seconds
        :param label: Optional. The component label content
        :param icon: Optional. The component icon content from font-awesome references
        :param time_ms_factor: Optional. The format from the format in milliseconds
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param html_code: Optional. The component identifier code (for both Python and Javascript)
        :param helper: Optional. A tooltip helper
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        html_cd = html.HtmlDates.CountDownDate(
            self.page, day, month, year, hour, minute, second, label, icon, time_ms_factor, width, height, html_code,
            helper, options or {}, profile)
        html.Html.set_component_skin(html_cd)
        return html_cd

    def update(self, label: str = None, color: str = None, align: str = None, width: types.SIZE_TYPE = ("auto", ""),
               height: types.SIZE_TYPE = (None, "px"), html_code: str = None,
               options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = None) -> html.HtmlDates.LastUpdated:
        """Last Update time component.

        :tags:
        :categories:

        Usage::

          page.ui.rich.update("Last update: ")

          update = page.ui.rich.update()
          page.ui.button("Click").click([update.refresh()])

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlDates.LastUpdated`

        `Use case <https://github.com/epykure/epyk-templates/blob/master/locals/components/calendar.py>`_

        :param label: Optional. The label to be displayed close to the date. Default Last Update.
        :param color: Optional. The color code for the font.
        :param align: Optional.
        :param width: Optional. A tuple with the integer for the component width and its unit.
        :param height: Optional. A tuple with the integer for the component height and its unit.
        :param html_code: Optional. The component identifier code (for both Python and Javascript).
        :param options: Optional. Specific Python options available for this component.
        :param profile: Optional. A flag to set the component performance storage.
        """
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        component = html.HtmlDates.LastUpdated(self.page, label, color, width, height, html_code, options, profile)
        component.style.css.font_factor(-5)
        if align in ("center", "right"):
            component.style.css.margin = "auto"
            component.style.css.display = "block"
            component.style.css.text_align = align
        elif align == "left":
            component.style.css.display = "block"
        else:
            component.style.css.inline()
        html.Html.set_component_skin(component)
        return component

    def console(self, content: str = "", width: types.SIZE_TYPE = (100, "%"), height: types.SIZE_TYPE = (200, "px"),
                html_code: str = None, options: types.OPTION_TYPE = None,
                profile: types.PROFILE_TYPE = None) -> html.HtmlTextEditor.Console:
        """Display an component to show logs.

        :tags:
        :categories:

        Usage::

          c = page.ui.rich.console(
            "* This is a log section for all the events in the different buttons *", options={"timestamp": True})

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlTextEditor.Console`

        `Use case <https://github.com/epykure/epyk-templates/blob/master/locals/components/checkbox.py>`_

        :param content: Optional. The console content
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dflt_options = {"markdown": False, "timestamp": True}
        if options is not None:
            dflt_options.update(options)
        html_div = html.HtmlTextEditor.Console(self.page, content, width, height, html_code, None, dflt_options,
                                               profile)
        html_div.css({"border": "1px solid %s" % self.page.theme.greys[4], "background": self.page.theme.greys[2],
                      'padding': '5px'})
        html.Html.set_component_skin(html_div)
        return html_div

    def search_input(self, text: str = '', placeholder: str = 'Search..', color: str = None,
                     width: types.SIZE_TYPE = (100, '%'), height: types.SIZE_TYPE = (None, "px"),
                     html_code: str = None, tooltip: str = None, extensible: bool = False,
                     options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = None) -> html.HtmlInput.Search:
        """Search bar.

        :tags:
        :categories:

        Usage::

          page.ui.inputs.search()

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlInput.Search`

        `w3schools <https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_anim_search>`_

        :param text: Optional. The value to be displayed to the component
        :param placeholder: Optional. The text display when empty
        :param color: Optional. The font color in the component. Default inherit
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param tooltip: Optional. A string with the value of the tooltip
        :param extensible: Optional. Flag to specify the input style
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        width = Arguments.size(width, unit="px")
        height = Arguments.size(height, unit="px")
        icon_details = self.page.icons.get("search")
        dflt_options = {"icon": icon_details["icon"], "icon_family": icon_details["icon_family"], 'position': 'left',
                        'select': True, "border": 1}
        if options is not None:
            dflt_options.update(options)
        html_s = html.HtmlInput.Search(
            self.page, text, placeholder, color, width, height, html_code, tooltip, extensible, dflt_options, profile)
        html.Html.set_component_skin(html_s)
        return html_s

    def search_results(self, records=None, results_per_page: int = 20, width: types.SIZE_TYPE = (100, "%"),
                       height: types.SIZE_TYPE = (None, "px"), options: types.OPTION_TYPE = None,
                       profile: types.PROFILE_TYPE = None) -> html.HtmlTextComp.SearchResult:
        """Display the search results. This will return the matches and the details.

        :tags:
        :categories:

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlTextComp.SearchResult`

        :param records: Optional. The list of dictionaries with the input data
        :param results_per_page: Optional. The page index
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        records = records or []
        dfl_options = {"pageNumber": results_per_page}
        if options is not None:
            dfl_options.update(options)
        html_help = html.HtmlTextComp.SearchResult(
            self.page, records, width=width, height=height, profile=profile,
            options=dfl_options)
        html.Html.set_component_skin(html_help)
        return html_help

    def composite(self, schema, width: types.SIZE_TYPE = (None, "%"), height: types.PROFILE_TYPE = (None, "px"),
                  html_code: str = None, helper: str = None, options: dict = None,
                  profile: types.PROFILE_TYPE = None) -> html.HtmlTextComp.Composite:
        """Composite bespoke object.

        This object will be built based on its schema. No specific CSS Style and class will be added to this object.
        The full definition will be done in the nested dictionary schema.

        :tags:
        :categories:

        Usage::

          schema = {'type': 'div', 'css': {}, 'class': , 'attrs': {} 'arias': {},  'children': [
              {'type': : {...}}
              ...
          ]}

        :param schema: The component nested structure
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param helper: Optional. The value to be displayed to the helper icon
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        html_help = html.HtmlTextComp.Composite(
            self.page, schema, width=width, height=height, html_code=html_code, profile=profile, options=options or {},
            helper=helper)
        html.Html.set_component_skin(html_help)
        return html_help

    def status(self, status: str, width: types.SIZE_TYPE = (None, "%"), height: types.SIZE_TYPE = (None, "px"),
               html_code: str = None, options: types.OPTION_TYPE = None,
               profile: types.PROFILE_TYPE = None) -> html.HtmlTextComp.Status:
        """

        :tags:
        :categories:

        :param status:
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param profile: Optional. A flag to set the component performance storage
        :param options: Optional. Specific Python options available for this component
        """
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options = {'states': {
            "Done": 'green', "Success": 'green',
            'In Progress': 'orange', 'Blocked': 'brown', 'Failed': 'red'}}
        if options is not None:
            dfl_options.update(options)
        html_help = html.HtmlTextComp.Status(
            self.page, status, width=width, height=height, html_code=html_code, profile=profile, options=dfl_options)
        html.Html.set_component_skin(html_help)
        html_help.style.css.inline()
        return html_help

    def markdown(self, text: str = "", width: types.SIZE_TYPE = ("calc(100% - 10px)", ''),
                 height: types.SIZE_TYPE = ("auto", ''), html_code: str = None, options: types.OPTION_TYPE = None,
                 profile: types.PROFILE_TYPE = None) -> html.HtmlTextEditor.MarkdownReader:
        """

        :tags:
        :categories:

        Usage::

          md = page.ui.rich.markdown('''
            # H1
            ## H2
            ### value
            #### rrr
            ##### H5
            ###### H6
            value
            ''')

        Underlying HTML Objects:

          - :class:`epyk.core.html.HtmlTextEditor.Editor`

        `Use case <https://github.com/epykure/epyk-templates/blob/master/locals/components/markdown.py>`_

        :param text: Optional. The value to be displayed to the component
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dflt_options = {"markdown": True}
        if options is not None:
            dflt_options.update(options)
        md = html.HtmlTextEditor.MarkdownReader(self.page, text, width, height, html_code, dflt_options, profile)
        md.style.css.margin_left = 5
        md.style.css.margin_right = 5
        md.style.css.padding = 5
        html.Html.set_component_skin(md)
        return md

    def adv_text(self, section, title, content, background: str = "",
                 options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = None):
        """

        :tags:
        :categories:

        :param section:
        :param title: String | Component. Optional. A panel title. This will be attached to the title property
        :param content:
        :param background:
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        container = self.page.ui.div(options=options, profile=profile)
        if section is not None:
            text = self.page.ui.text(section, width=(100, '%'), options=options, profile=profile)
            text.style.css.text_align = "center"
            text.style.css.font_size = self.page.body.style.globals.font.normal(-1)
            text.style.css.line_height = self.page.body.style.globals.font.normal(5)
            text.style.css.font_weight = 500
            text.style.css.letter_spacing = "0.15em"
            text.style.css.text_transform = "uppercase"
            container.add(text)

        if title is not None:
            title = self.page.ui.text(title, width=(100, '%'), options=options, profile=profile)
            title.style.css.text_align = "center"
            title.style.css.font_size = self.page.body.style.globals.font.normal(12)
            title.style.css.font_weight = 300
            title.css({'margin-block-end': '0.67em', 'margin-block-start': '0'})
            container.add(title)

        if content is not None:
            content = self.page.ui.text(content, width=(80, "%"), options=options, profile=profile)
            content.style.css.text_align = "center"
            content.style.css.font_size = self.page.body.style.globals.font.normal(2)
            content.style.css.margin = "auto"

        container.add(content)
        # container0.style.css.border = "10px solid white"
        container.style.css.text_align = "center"
        container.style.css.background = background
        container.style.css.padding = 10
        html.Html.set_component_skin(container)
        return container

    def color(self, code, content: str = "data copied to clipboard", width: types.SIZE_TYPE = (20, 'px'),
              height: types.SIZE_TYPE = (20, 'px'), options: types.OPTION_TYPE = None,
              profile: types.PROFILE_TYPE = None):
        """Color component.

        :tags:
        :categories:

        :param code: Tuple or String. The color code
        :param content: Optional.
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        dflt_options = {"type": 'rgb', 'popup_timers': 1000}
        if options is not None:
            dflt_options.update(options)
        if dflt_options.get("type") == 'hex' or str(code).startswith("#"):
            code = Colors.getHexToRgb(code)
        d = self.page.ui.div(width=width, height=height, profile=profile)
        d.style.css.display = "inline-block"
        d.style.css.border = "1px solid %s" % self.page.theme.greys[0]
        d.tooltip("rgb: %s, hex: %s" % (code, Colors.getRgbToHex(code)))
        d.style.css.cursor = "pointer"
        d.click([
            self.page.js.clipboard(Colors.getRgbToHex(code)),
            self.page.js.print(content, dflt_options.get('popup_timers'), dflt_options.get('popup_css'))])
        d.style.css.background = "rgb(%s, %s, %s)" % (code[0], code[1], code[2])
        html.Html.set_component_skin(d)
        return d

    def elapsed(self, day: int = None, month: int = None, year: int = None, label=None, icon=None, width=(None, "px"),
                height=(None, "px"), html_code=None, helper=None, options=None, profile=None) -> html.HtmlDates.Elapsed:
        """

        :tags:
        :categories:

        Usage::

          dt = page.ui.rich.elapsed(day=1, month=1, year=2021)
          page.ui.button("Click").click([dt.build({"year": 2022, "month": 1, "day": 1})])

        :param day: The day number
        :param month: The month number [1, 12]
        :param year: The year number
        :param label:
        :param icon:
        :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
        :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
        :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side)
        :param helper: String. Optional. The value to be displayed to the helper icon
        :param options: Dictionary. Optional. Specific Python options available for this component
        :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
        """
        options = options or {}
        md = html.HtmlDates.Elapsed(
            self.page, day, month, year, label, icon, width, height, html_code, helper, options, profile)
        html.Html.set_component_skin(md)
        return md

    def powered(self, by=None, width=(100, "%"), height=(None, "px"), options=None, profile=None):
        """Display badges for the specifies JavaScript modules.

        Tip: If by is None. This will display only the main JavaScript module with the current version.
        It will not display the underlying components.

        This component needs to be called at the end to ensure all the imported will be registered.

        :tags:
        :categories:

        :param by: List. Optional. Name of JavaScript library aliases
        :param width: Tuple. Optional. A tuple with the integer for the component width and its unit
        :param height: Tuple. Optional. A tuple with the integer for the component height and its unit
        :param options: Dictionary. Optional. Specific Python options available for this component
        :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage
        """
        container = self.page.ui.div(width=width, options=options, profile=profile)
        container.style.css.font_factor(-4)
        if by is None:
            by = sorted(list(self.page.jsImports))
        elif by is True:
            by = []
            for alias, pkg in Imports.JS_IMPORTS.items():
                if "node_folder" not in pkg:
                    by.append(alias)
        for i, b in enumerate(by):
            if b in self.page.imports.jsImports:
                if not self.page.imports.jsImports[b]["versions"]:
                    continue

                badge = self.page.ui.div([
                    self.page.ui.text(b.capitalize(), height=height, profile=profile),
                    self.page.ui.text("v%s" % self.page.imports.jsImports[b]["versions"][0], height=height,
                                      profile=profile)],
                    width="auto", profile=profile)
                badge[0].style.css.margin_right = 5
                badge[0].goto(self.page.imports.website(b), target="_blank")
                badge[0].style.css.background = Colors.randColor(self.page.py.hash(b))
                badge[0].style.css.color = "white"
                badge[0].style.css.text_shadow = "1px 1px black"
                badge[0].style.css.padding = "0 5px"
                badge[0].style.css.border_right = "1px solid black"
                badge[1].style.css.padding = "0 5px 0 0"
                badge.style.css.border = "1px solid %s" % self.page.theme.greys[5]
                badge.style.css.margin = 2
                badge.style.css.border_radius = "0 10px 10px 0"
                container.add(badge)
        html.Html.set_component_skin(container)
        return container
