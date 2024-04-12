#!/usr/bin/python
# -*- coding: utf-8 -*-


from typing import Union, Optional, List
from epyk.core.py import primitives, types
from epyk.core import html

from epyk.core.css import Defaults_css

from epyk.interfaces.components import CompAnimations
from epyk.interfaces.components import CompLayouts
from epyk.interfaces.components import CompCodes
from epyk.interfaces.components import CompButtons
from epyk.interfaces.components import CompIcons
from epyk.interfaces.components import CompInputs
from epyk.interfaces.components import CompMedia
from epyk.interfaces.components import CompLists
from epyk.interfaces.components import CompNumbers
from epyk.interfaces.tables import CompTables
from epyk.interfaces.graphs import CompCharts
from epyk.interfaces.geo import CompGeo
from epyk.interfaces.components import CompTexts
from epyk.interfaces.components import CompRich
from epyk.interfaces.components import CompImages
from epyk.interfaces.components import CompLinks
from epyk.interfaces.components import CompSliders
from epyk.interfaces.components import CompNetwork
from epyk.interfaces.components import CompForms
from epyk.interfaces.components import CompTags
from epyk.interfaces.components import CompFields
from epyk.interfaces.components import CompTrees
from epyk.interfaces.components import CompVignets
from epyk.interfaces.components import CompMenus
from epyk.interfaces.components import CompPanels
from epyk.interfaces.components import CompModals
from epyk.interfaces.components import CompNavigation
from epyk.interfaces.components import CompSteps
from epyk.interfaces.components import CompDrawers
from epyk.interfaces.components import CompSteppers
from epyk.interfaces.components import CompTitles
from epyk.interfaces.components import CompCalendars
from epyk.interfaces.components import CompPictos
from epyk.interfaces.components import CompPollers

from epyk.interfaces import Arguments

# External web frameworks
from epyk.fwk.toast import UI as ToastUI
from epyk.fwk.clr import UI as ClarityUI
from epyk.fwk.evr import UI as EvergreenUI
from epyk.fwk.bs import UI as BoostrapUI
from epyk.fwk.mdc import UI as MaterialUI
from epyk.fwk.jqui import UI as JqueryUI
from epyk.fwk.ftw import UI as FluentUI

# All the custom modules.
from epyk.customs import pyks


class Components:
    """Main interface for all components.

    Usage::

        # To change the default style for components.
        page.ui.components_skin = {
          "buttons.absolute": {"clear": {"css": True, "cls": True}, "css": {"color": "red"}, 'cls': ["cssbuttonbasic"]},
          "buttons.check": {"css": {"color": "green"}},
        }

    :param page: The web page object.
    """

    def __init__(self, page: primitives.PageModel):
        self.page = page
        self.components_skin = None

        # Special shortcut for some components
        self.button = self.buttons.button
        self.toggle = self.buttons.toggle
        self.input = self.inputs.input
        self.div = self.layouts.div
        self.grid = self.layouts.grid
        self.row = self.layouts.row
        self.col = self.layouts.col
        self.table = getattr(self.tables, html.Defaults.TABLE_FAMILY)
        self.pivot = self.tables.pivot
        self.text = self.texts.text
        self.title = self.texts.title
        self.subtitle = self.titles.subtitle
        self.icon = self.images.icon
        self.img = self.images.img
        self.list = self.lists.list
        self.link = self.links.link
        self.check = self.buttons.check
        self.slider = self.sliders.slider
        self.select = self.lists.select
        self.lookup = self.lists.lookup
        self.date = self.fields.date
        self.cob = self.fields.cob
        self.tree = self.lists.tree
        self.info = self.rich.info
        self.radio = self.buttons.radio
        self.navbar = self.navigation.nav
        self.footer = self.navigation.footer
        self.modal = self.modals.forms
        self.disclaimer = self.modals.disclaimer
        self.drawer = self.drawers.drawer
        self.stepper = self.steppers.stepper
        self.chips = self.lists.chips
        self.contextual = self.menus.contextual
        self.hidden = self.fields.hidden
        self.number = self.numbers.number
        self.euro = self.numbers.euro
        self.percent = self.numbers.percent
        self.banner = self.banners.text

        # Shortcut to some important HTML tags
        self.label = self.texts.label
        self.paragraph = self.texts.paragraph
        self.textarea = self.inputs.textarea
        self.header = self.layouts.header
        self.section = self.layouts.section
        self.composite = self.rich.composite

        # Set the default chart to be ChartJs
        # TODO fix ApexChart and BillboardJs
        self.chart = self.charts.chartJs
        self.analytics = self.charts.c3

    def css(self, css_attrs: dict):
        """Change the CSS Style of the main container in the page.

        Usage::

            page.ui.css({"color": "blue"})

        :param css_attrs: The CSS attributes to be applied
        """
        self.page.properties.css.container_style(css_attrs)
        return self

    def print(self, text: str = None, end: str = "\n", html_code: str = None,
              options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = None) -> html.HtmlText.Text:
        """Mimic the print function available in Python.
        This will create a div container with the content as a string.

        This function can be also used to display Python function. Inspect module will be used in this case to get the
        source code.

        Usage::

          import pandas
          page.ui.print('pandas: {}'.format(pandas.__version__))

        :param text: Optional. The content to be displayed
        :param end: Optional. The end of line
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        :return: :py:class:`A HTML text component <epyk.core.html.HtmlText.Text>'
        """
        if callable(text):
            import inspect
            text = inspect.getsource(text)

        if text is not None:
            if end == "\n":
                div = self.text(text, width=(100, '%'), html_code=html_code, options=options, profile=profile)
            else:
                div = self.text(text, html_code=html_code, options=options, profile=profile)
            div.style.css.padding = 5
            div.style.css.font_family = 'Courier'
        else:
            div = self.layouts.new_line()
        html.Html.set_component_skin(div)
        return div

    @property
    def codes(self) -> CompCodes.Code:
        """Group all the UI Components dedicated to display code fragments.
        This will wrap the Javascript module codemirror.
        More details on the :py:class:`Codes property <epyk.interfaces.components.CompCodes.Code>` page

        Usage::

          page.ui.codes.css(".test {color: red}")

        `codemirror <https://codemirror.net/doc/manual.html>`_
        """
        return CompCodes.Code(self)

    @property
    def pollers(self) -> CompPollers.Poller:
        """Group all the UI with polling feature.
        More details on the :py:class:`Animations property <epyk.interfaces.components.CompPollers.Poller>` page

        Usage::

          page.ui.select()
          poller = page.ui.pollers.live(2, [
            page.js.console.log(page.js.objects.date())
          ], components=[page.ui.text("Updated feeds")])
        """
        return CompPollers.Poller(self)

    @property
    def network(self) -> CompNetwork.Network:
        """Group all the UI Components dedicated to display messaging services.
        This category will group (chat, RSS streams, forum, bot ...).
        Those components are interactive and they would require underlying services and databases in order to fully work.
        More details on the :py:class:`Networks property <epyk.interfaces.components.CompNetwork.Network>` page

        Usage::

            page = pk.Page()
            page.ui.network
        """
        return CompNetwork.Network(self)

    @property
    def sliders(self) -> CompSliders.Sliders:
        """Group all the UI components dedicated to produce slider items.
        Those components are interactive and can be used to filter the data on other items in the dashboard.
        Those components are mainly relying on Jquery and JqueryUi.
        More details on the :py:class:`Sliders property <epyk.interfaces.components.CompSliders.Sliders>` page

        Usage::

            slider = page.ui.slider(5)
            slider.options.step = 0.01
            slider.options.slide(precision=2)
        """
        return CompSliders.Sliders(self)

    @property
    def _3d(self) -> CompCharts.Chart3d:
        """Group all the 3D charts.
        More details on the :py:class:`Charts 3D property <epyk.interfaces.components.CompCharts.Chart3d>` page

        Usage::

            page = pk.Page()
            page.ui._3d
        """
        return CompCharts.Chart3d(self)

    @property
    def _2d(self) -> CompCharts.Chart2d:
        """Group all the 2D charts.
        More details on the :py:class:`Charts 2D property <epyk.interfaces.components.CompCharts.Chart2d>` page

        Usage::

            page = pk.Page()
            page.ui._2d
        """
        return CompCharts.Chart2d(self)

    @property
    def titles(self) -> CompTitles.Titles:
        """Group all the UI components dedicated to produce titles.

        More details on the :py:class:`Titles property <epyk.interfaces.components.CompTitles.Titles>` page

        Usage::

          page.ui.titles.head("test")
        """
        return CompTitles.Titles(self)

    @property
    def links(self) -> CompLinks.Links:
        """Group all the UI components dedicated to produce links to another page or website.

        More details on the :py:class:`Links property <epyk.interfaces.components.CompLinks.Links>` page

        Usage::

          page.ui.links.external('data', 'www.google.fr', icon="fas fa-align-center", options={"target": "_blank"})
          page.ui.layouts.new_line(2)
        """
        return CompLinks.Links(self)

    @property
    def navigation(self) -> CompNavigation.Navigation:
        """Group all the UI components dedicated to produce navigation components such as navigation bar, footer,
        banner...

        More details on the :py:class:`Navigation property <epyk.interfaces.components.CompNavigation.Navigation>` page

        Usage::

          nav = page.ui.navigation.nav(height=(30, 'px'), title={"This is an example": "by Epyk"})
          for component in ["Menu 1", "Menu 2"]:
            title = nav.add_right(component)
        """
        return CompNavigation.Navigation(self)

    @property
    def bars(self) -> CompNavigation.NavBars:
        """Group all the UI components dedicated to produce Navigation bar components such as navigation bar, footer,
        banner...

        More details on the :py:class:`Bars property <epyk.interfaces.components.CompNavigation.NavBars>` page

        Usage::

          page.ui.bars
        """
        return CompNavigation.NavBars(self)

    @property
    def banners(self) -> CompNavigation.Banners:
        """Group all the available banners.

        More details on the :py:class:`Banners property <epyk.interfaces.components.CompNavigation.Banners>` page

        Usage::

          top = page.ui.banners.top("text")
          top.style.css.font_size = '40px'
        """
        return CompNavigation.Banners(self)

    @property
    def pictos(self) -> CompPictos.Pictogram:
        """Group all the built-in pictogram. """
        return CompPictos.Pictogram(self)

    @property
    def rich(self) -> CompRich.Rich:
        """Group all the UI components dedicated to produce rich HTML Components.

        This category will take into account very specific and bespoke components.

        Usage::

          page.ui.fields.now(label="timestamp", color="red", helper="This is the report timestamp")
          page.ui.rich.delta({'number': 100, 'prevNumber': 60, 'thresold1': 100, 'thresold2': 50}, helper="test")
          page.ui.rich.info("text")
        """
        return CompRich.Rich(self)

    @property
    def vignets(self) -> CompVignets.Vignets:
        """Group all the UI components dedicated to produce rich HTML Components.

        This category will take into account very specific and bespoke components.

        Usage::

          page.ui.vignets.number(500, "Test")
          page.ui.vignets.number(500, "Test 2 ", options={"url": "http://www.google.fr"})
          page.ui.vignets.block({
            "text": 'This is a brand new python framework', "title": 'New Python Web Framework',
            "button": {"text": 'Get Started', 'url': "/getStarted"}, 'color': 'green'})
        """
        return CompVignets.Vignets(self)

    @property
    def numbers(self) -> CompNumbers.Numbers:
        """Group all the UI components dedicated to produce Numbers components.

        The items in this category will not be editable and they will only provide nice number renderings.
        """
        return CompNumbers.Numbers(self)

    @property
    def texts(self) -> CompTexts.Texts:
        """Group all the UI components dedicated to produce text components.

        The items in this category will not be editable and they will only provide nice text structure like paragraph,
        formatted text...
        """
        return CompTexts.Texts(self)

    @property
    def images(self) -> CompImages.Images:
        """Group all the UI components dedicated to produce image or collection of images. """
        return CompImages.Images(self)

    @property
    def lists(self) -> CompLists.Lists:
        """Group all the UI components dedicated to produce list or selection items.

        Simple list, trees or DropDown boxes will be part of this category of items.
        """
        return CompLists.Lists(self)

    @property
    def trees(self) -> CompTrees.Trees:
        """Group all the UI components dedicated to produce Trees or selection items."""
        return CompTrees.Trees(self)

    @property
    def geo(self) -> CompGeo.Geo:
        """Group all the UI components dedicated to produce Trees or selection items.

        Usage::

          l = page.ui.geo.mapbox.globe()
          l.load([...])
          l.options.style = 'mapbox://styles/mapbox/streets-v11'

          marker = l.js.marker(-0.11, 51.508)
          marker2 = l.js.marker(12.65147, 55.608166, options={"color": 'black', "rotation": 45})
          page.body.onReady([marker, marker2])
        """
        return CompGeo.Geo(self)

    @property
    def buttons(self) -> CompButtons.Buttons:
        """Group all the UI components dedicated to produce button or checkbox.

        More details on the :py:class:`Buttons property <epyk.interfaces.components.CompButtons.Buttons>` page

        Usage::

          page.ui.buttons.absolute("Click Me")
          page.ui.buttons.switch({'on': "true", 'off': 'false'})
          page.ui.buttons.check(label="Label")
        """
        return CompButtons.Buttons(self)

    @property
    def tables(self) -> CompTables.Tables:
        """Group all the UI components dedicated to produce tables or pivot tables.

        Different kind of tables are available in the framework (Tabulator, DataTable, PivotTable or even a bespoke
        implementation).
        """
        return CompTables.Tables(self)

    @property
    def steps(self) -> CompSteps.Steppers:
        """Group all the UI steps components."""
        return CompSteps.Steppers(self)

    @property
    def drawers(self) -> CompDrawers.Drawers:
        """Group all the UI drawers components."""
        return CompDrawers.Drawers(self)

    @property
    def steppers(self) -> CompSteppers.Steppers:
        """Group all the UI steppers components.

        Usage::

          s = page.ui.steppers.arrow()
          s.options.column_title = "name"
          btn = page.ui.button("Load")
          btn.click(
            s.build([
                  {"value": 'test 1', "status": 'success', 'name': "1", 'title': 'test', "label": 'test'},
                  {"value": 'test 2', "status": 'pending', "tooltip": "processing"},
                  {"value": 'test 3'},
                  {"value": 'test 4'}])
          )
        """
        return CompSteppers.Steppers(self)

    @property
    def media(self) -> CompMedia.Media:
        """Group all the UI components dedicated to produce media (video and audio) items.

        Plain Vanilla HTML5 components.

        Usage::

          cam = page.ui.media.camera()
          page.ui.button("start").click([cam.dom.start()])
          page.ui.button("play").click([cam.dom.play()])
          page.ui.button("Stop").click([cam.dom.stop()])
          page.ui.button("record (Start)").click([cam.dom.record()])
          page.ui.button("record (Stop)").click([cam.dom.record(False)])
          page.ui.button("takepicture").click([cam.dom.takepicture()])
        """
        return CompMedia.Media(self)

    @property
    def inputs(self) -> CompInputs.Inputs:
        """Group all the UI components dedicated to produce input items.

        Those components are editable items which need to be updated by the user of the dashboard.
        This category will take into account TextArea, input text...
        """
        return CompInputs.Inputs(self)

    @property
    def fields(self) -> CompFields.Fields:
        """Group all the UI components dedicated to produce input items.

        Those components are editable items which need to be updated by the user of the dashboard.
        This category will take into account TextArea, input text...
        """
        return CompFields.Fields(self)

    @property
    def timelines(self) -> CompFields.Timelines:
        """ """
        return CompFields.Timelines(self)

    @property
    def icons(self) -> CompIcons.Icons:
        """Group all the UI components dedicated to produce icon items.

        This category of component will rely on the font-awesome library for the final display.
        """
        return CompIcons.Icons(self)

    @property
    def menus(self) -> CompMenus.Menus:
        """Group all the UI menus."""
        return CompMenus.Menus(self)

    @property
    def panels(self) -> CompPanels.Panels:
        """Group all the UI panels."""
        return CompPanels.Panels(self)

    @property
    def layouts(self) -> CompLayouts.Layouts:
        """Group all the UI components dedicated to produce component containers.

        All the items in this category are dedicated for the structure of the dashboard and they
        are mainly holder of other components.
        This will mainly rely on bootstrap for the display of the different objects in the page.
        """
        return CompLayouts.Layouts(self)

    @property
    def forms(self) -> CompForms.Forms:
        """Group all the Forms components dedicated to drop data.

        `w3schools <https://www.w3schools.com/html/html_forms.asp>`_
        """
        return CompForms.Forms(self)

    @property
    def modals(self) -> CompModals.Modals:
        """Group all the UI components dedicated to produce modal components."""
        return CompModals.Modals(self)

    @property
    def charts(self) -> CompCharts.Graphs:
        """Group all the UI components dedicated to produce charts.

        Different kind of charts framework are available (ChartJs, Plotly, C3, Billboard, NVD3, DC, Vis, Frappe, Vega,
        Apex or even D3).

        Usage::

          from epyk.mocks import urls
          page = pk.Page()
          chart = page.ui.charts.chartJs.line(y_columns=["Armenia", "France", "Germany"], x_axis="year")
          page.body.onLoad([
            page.js.fetch(urls.CO2_DATA).csvtoRecords().get([
              chart.build(page.data.js.record("data").filterGroup("test").pivot("country", "co2", "year", type="float"))
            ])])
        """
        return CompCharts.Graphs(self)

    @property
    def tags(self) -> CompTags.Tags:
        """Group all the other tags available in HTML.

        Those tags can be considered as normal HTML component, which means Js and CSS features are also available.
        """
        return CompTags.Tags(self)

    @property
    def calendars(self) -> CompCalendars.Calendar:
        """Group all the component related to the time and calendar management.

        Usage::

          content = {
            "2020-07-02": {'task1': 50, 'task2': 50},
            "2020-07-03": {'task1': 100},
            "2020-07-21": {'task4': 100},
            "2020-07-22": {'task4': 100}
          }
          july = page.ui.calendars.days(7, content, align="center", options={"colors": {"task4": 'red'}})
        """
        return CompCalendars.Calendar(self)

    @property
    def delimiters(self) -> CompLayouts.Delimiter:
        """Shortcut property to the various delimiters styles.

        `codepen <https://codepen.io/ibrahimjabbari/pen/ozinB>`_
        """
        return CompLayouts.Delimiter(self)

    def contents(self, title: str = "Contents", top: int = 10, right: int = 10, left: int = None,
                 width: types.SIZE_TYPE = (None, "%"), height: types.SIZE_TYPE = (None, "px"),
                 html_code: str = None, options: types.OPTION_TYPE = None,
                 profile: types.PROFILE_TYPE = None) -> html.HtmlTextComp.ContentsTable:
        """Add a content table to the page.

        Usage::

            menu = page.ui.contents()
            menu.add(page.ui.text("Simple text"))
            menu.anchor("Test", 3, "#name")
            page.ui.button("Button").click([
              menu.build([{"text": 'ok', "level": 0, "anchor": "#test"}])
            ])

            page.body.onReady([
              menu.build([
                {"anchor": '#test', 'level': 1, 'text': 'Ok'}
              ])
            ])

        `Demo Content Table <https://github.com/epykure/epyk-templates/blob/master/locals/components/contents_table.py>`_
        `Demo Paragraph <https://github.com/epykure/epyk-templates/blob/master/locals/components/paragraph.py>`_

        :param title: Optional. The title for the content table
        :param top: Optional. The top property affects the vertical position of a positioned element
        :param right: Optional. The right property affects the horizontal position of a positioned element
        :param left: Optional. The left property affects the horizontal position of a positioned element
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        html_code = html_code or "content"
        if html_code not in self.page.components:
            html_contents = html.HtmlTextComp.ContentsTable(
                self.page, title, width, height, html_code, options, profile)
            html_contents.menu = self.page.ui.div(html_code="%s_page" % html_code)
            if Defaults_css.BODY_CONTAINER is not None and "page_nav_bar" in self.page.components:
                html_contents.style.css.top = Defaults_css.BODY_CONTAINER.get('padding-top', 0) + top
            else:
                html_contents.style.css.top = top
            if left is not None:
                html_contents.style.css.left = left
            else:
                html_contents.style.css.right = right
                #   Attach the table content to the main report object
            self.page._content_table = html_contents
            html_contents.style.css.z_index = 500
            if self.page.body.style.css.padding_top is not None:
                html_contents.style.css.top = self.page.body.style.css.padding_top
        else:
            html_contents = self.page.components[html_code]
            title_link = html_contents.add_category(title, level=1)
            title_link.style.css.margin_top = 10
        return html_contents

    def bespoke(self, html_cls, *args, **kwargs):
        """Hook to allow the creation of bespoke component using specific configurations.
        Components can be self-contained in a module and rely on external packages.

        Tip: Look at the Import.extend function in order to add external Js and CSS modules to your environment.

        :param html_cls: Class. The bespoke HTML component
        :param args: The python attributes used in the HTML component constructor
        :param kwargs: The python attributes used in the HTML component constructor
        """
        return html_cls(self.page, *args, **kwargs)

    def _tags(self, vals=None, title: str = "", icon: str = "", width: types.SIZE_TYPE = (100, "%"),
              height: types.SIZE_TYPE = (None, "px"), html_code: str = None,
              profile: types.PROFILE_TYPE = None) -> html.HtmlTextEditor.Tags:
        """

        :param vals: Optional.
        :param title: Optional. Teh title for teh tag component
        :param icon: Optional. A string with the value of the icon to display from font-awesome
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param profile: Optional. A flag to set the component performance storage
        """
        return html.HtmlTextEditor.Tags(
            self.page, vals, title, icon, (self.page.body.style.globals.font.size, 'px'), width, height, html_code,
            profile)

    def loading(self, text: str = "Loading", color: Union[str, bool] = None, options: types.OPTION_TYPE = None,
                html_code: str = None, profile: types.PROFILE_TYPE = None) -> html.HtmlOthers.Loading:
        """Entry point to the loading component.

        This component will create a
          - label component for the text
          - icon component for the loading icon

        :param text: Optional. The text in the component (during the loading)
        :param color: Optional. The font color in the component. Default inherit
        :param options: Optional. Specific Python options available for this component
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param profile: Optional. A flag to set the component performance storage
        """
        html_loading = html.HtmlOthers.Loading(
            self.page, text, color, (self.page.body.style.globals.font.size, 'px'), options or {}, html_code,
            profile)
        html.Html.set_component_skin(html_loading)
        return html_loading

    def breadcrumb(self, values=None, selected: Optional[int] = None, width: types.SIZE_TYPE = (100, '%'),
                   height: types.SIZE_TYPE = (30, 'px'), html_code: str = None,
                   options: types.OPTION_TYPE = None,
                   profile: types.PROFILE_TYPE = None) -> html.HtmlOthers.Breadcrumb:
        """Add Breadcrumb information to the page.

        Usage::

            bc = page.ui.breadcrumb([
              {"text": 'part 1', 'url': 'part1'},
              {"text": 'part 2', 'url': 'part2'},
              {"text": 'part 3', 'url': 'part3'},
            ])

            # This will change the link of part 2 and part 3 and add some extra information in the link
            bc.onReady([
              bc[1].dom.setAttribute("href", http.get("type").toString().prepend("part2?")),
              bc[2].dom.setAttribute("href", http.get("type").toString().prepend("http://www.w3schools.com/").add("/howto_css_breadcrumbs.asp"))
            ])

        `Demo breadcrumb <https://github.com/epykure/epyk-templates/blob/master/locals/components/breadcrumb.py>`_

        :param values: Optional. The breadcrumb record definition
        :param selected: Optional. The selected item index
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param options: Optional. Specific Python options available for this component
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param profile: Optional. A flag to set the component performance storage
        """
        dfl_options = {"style": {}}
        if options is not None:
            dfl_options.update(options)
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        dfl_options['selected'] = selected
        html_breadcrumb = html.HtmlOthers.Breadcrumb(
            self.page, values or [], width, height, html_code, dfl_options, profile)
        html_breadcrumb.style.css.margin_top = 5
        html.Html.set_component_skin(html_breadcrumb)
        return html_breadcrumb

    def form(self, components: List[html.Html.Html] = None, helper: str = None, method: str = "POST",
             action: str = "#", label: str = "Submit") -> html.HtmlContainer.Form:
        """Creates a new empty form.

        Usage::

          f = page.ui.form()

        :param components: Optional. The HTML components to be added to the HTML form
        :param helper: Optional. The value to be displayed to the helper icon
        :param method: Optional. The method used to transfer data
        :param action: Optional. The end point for submitting data
        :param label: Optional. The text on the submit button
        """
        form = html.HtmlContainer.Form(self.page, components or [], helper)
        form.method = method
        form.label = label
        form.action = action
        html.Html.set_component_skin(form)
        return form

    def json(self, data: dict = None, width: types.SIZE_TYPE = (None, '%'), height: types.SIZE_TYPE = (100, '%'),
             options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = None) -> html.HtmlOthers.HtmlJson:
        """HTML component to display a Json.

        Usage::

          from epyk.mocks import urls

          page = pk.Page()
          records = pd.DataFrame(page.py.requests.csv(urls.DEMO_COUNTRY))
          records = records[records["Year"] == "2010"]
          # Create a link to download data as a Json file
          viewer = page.ui.json(records.to_dict())
          viewer.options.hoverPreviewEnabled = True
          viewer.options.hoverPreviewArrayCount = 5

        `Demo Json Formatter <https://github.com/mohsen1/json-formatter-js>`_

        :param dict data: Optional. The Json object to be display
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        data = data or {}
        width = Arguments.size(width, unit="%")
        height = Arguments.size(height, unit="px")
        container = html.HtmlOthers.HtmlJson(self.page, data, width, height, options, profile)
        if height[1] != '%':
            container.style.css.overflow = 'auto'
        html.Html.set_component_skin(container)
        return container

    def slideshow(self, components: List[html.Html.Html] = None, width: types.SIZE_TYPE = (100, "%"),
                  height: types.SIZE_TYPE = ('auto', ""), options: types.OPTION_TYPE = None,
                  profile: types.PROFILE_TYPE = None) -> html.HtmlImage.SlideShow:
        """SlideShow component for pictures from the tiny-slider library.
        More details regarding this library here: https://github.com/ganlanyuan/tiny-slider.

        Usage::

          ss = page.ui.slideshow([page.ui.text("Great results %s" % i) for i in range(20)])

          ss.add_index_changed([
            page.js.console.log("ok"),
            page.js.console.log(ss.dom.info.indexCached),
            page.js.console.log(ss.dom.info.index),
          ])

        `Tiny-slider <https://github.com/ganlanyuan/tiny-slider>`_
        `Demo tiny-slider <http://ganlanyuan.github.io/tiny-slider/demo/>`_

        :param components: Optional. With the different components
        :param width: Optional. The component width in pixel or percentage
        :param height: Optional. The component height in pixel
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        width = Arguments.size(width)
        height = Arguments.size(height, "px")
        container = html.HtmlImage.SlideShow(self.page, components or [], width, height, options or {}, profile)
        html.Html.set_component_skin(container)
        return container

    def qrcode(self, data=None, width: types.SIZE_TYPE = (128, 'px'), height: types.SIZE_TYPE = (128, 'px'),
               options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = None) -> html.HtmlOthers.HtmlQRCode:
        """HTML component to display a QR Code from a string.

        `qrcodejs <https://davidshimjs.github.io/qrcodejs/>`_

        TODO: Add options

        :param data: Optional. The value to be converted to QR Code
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        data = data or {}
        width = Arguments.size(width, unit="px")
        height = Arguments.size(height, unit="px")
        h_qrcode = html.HtmlOthers.HtmlQRCode(self.page, data, width, height, options, profile)
        if height[1] != '%':
            h_qrcode.style.css.overflow = 'auto'
        html.Html.set_component_skin(h_qrcode)
        return h_qrcode

    def captcha(self, text: str = "Submit", width: types.SIZE_TYPE = (None, 'px'),
                height: types.SIZE_TYPE = (None, 'px'), options: types.OPTION_TYPE = None,
                profile: types.PROFILE_TYPE = None) -> html.HtmlOthers.HtmlCaptcha:
        """

        Usage::

          page.ui.captcha()

        :param text: Optional. The button content for the captcha validation
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        width = Arguments.size(width, unit="px")
        height = Arguments.size(height, unit="px")
        captcha = html.HtmlOthers.HtmlCaptcha(self.page, text, width, height, options or {}, profile)
        html.Html.set_component_skin(captcha)
        return captcha

    def postit(self, components: List[html.Html.Html] = None, anchor: html.Html.Html = None,
               options: types.OPTION_TYPE = None,
               profile: types.PROFILE_TYPE = None) -> html.HtmlContainer.Div:
        """

        TODO: add click event to keep the display.

        Usage::

          example = page.ui.title("Example")
          text = page.ui.text("This is a text")
          example.style.css.color = 'red'
          data_rest = page.py.requests.csv(data_urls.PLOTLY_APPLE_PRICES)
          ts = page.ui.charts.chartJs.timeseries(data_rest, y_columns=['AAPL.Open'], x_axis="Date", height=200)

          # Create a postit anchor to display the popup when the mouse is on it.
          p = page.ui.postit([example, text, ts])
          p.anchor.style.css.margin_left = '50px'
          p.popup.style.css.height = "250px"
          p.popup.style.css.width = "300px"

        `Demo postit <https://github.com/epykure/epyk-templates/blob/master/locals/components/postit.py>`_

        :param components: Optional.
        :param anchor: Optional.
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        postit = self.page.ui.div(options=options, profile=profile)
        if anchor is None:
            anchor = self.page.ui.icon("fas fa-map-marker")
            anchor.style.css.padding = "4px"
            postit += anchor
        postit.anchor = anchor
        popup = self.page.ui.div(components, width=(None, 'px'), options=options, profile=profile)
        popup.css({"display": 'none', 'position': 'absolute',
                   'border': "1px solid %s" % self.page.theme.greys[self.page.theme.index - 2], 'border-radius': '5px',
                   'padding': '5px', 'background': self.page.theme.greys[0]})
        postit += popup
        postit.popup = popup
        anchor.mouse([
            popup.dom.position(dx=10, dy=10), popup.dom.css({"display": 'block'}).r
        ],
            [popup.dom.css({"display": 'none'}).r]
        )
        html.Html.set_component_skin(postit)
        return postit

    def extension(self, package_name: str, alias: str = None):
        """Add an extension base on it is name.

        :param package_name: The package name.
        :param alias: Optional. The alias for the link in report.ui.
        """
        mod = __import__(package_name)
        __import__("%s.components" % package_name)
        if alias is None:
            alias = getattr(mod.components, 'alias', package_name)
        setattr(self, alias, mod.components.Components(self))

    def asterix(self, tooltip: str, family: str = None, width: types.SIZE_TYPE = (None, 'px'), html_code: str = None,
                height: types.SIZE_TYPE = (None, "px"), color: str = None,
                align: str = "left", options: types.OPTION_TYPE = None,
                profile: types.PROFILE_TYPE = None) -> html.HtmlImage.Icon:
        """

        :param tooltip:
        :param family:
        :param width: Optional. A tuple with the integer for the component width and its unit
        :param height: Optional. A tuple with the integer for the component height and its unit
        :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
        :param color:
        :param align:
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        """
        component = self.icon("fas fa-asterisk", family, width, html_code, height, color, tooltip, align, options,
                              profile)
        component.style.css.vertical_align = "top"
        component.style.css.color = self.page.theme.greys[5]
        html.Html.set_component_skin(component)
        return component

    def menu(self, component: Union[html.Html.Html, List[html.Html.Html]], title: Union[str, dict] = None,
             copy: str = "fas fa-copy", editable: tuple = ("fas fa-user-edit", "fas fa-user-lock"),
             refresh: str = "fas fa-redo-alt", visible: tuple = ('fas fa-eye-slash', "fas fa-eye"), post: dict = None,
             height: tuple = (18, 'px'), save_funcs: types.JS_FUNCS_TYPES = None,
             update_funcs: types.JS_FUNCS_TYPES = None, menu_items=None, options: types.OPTION_TYPE = None,
             profile: types.PROFILE_TYPE = None) -> html.HtmlContainer.Col:
        """


        TODO: Improve the editable feature for Markdown.

        Usage::

            p2 = page.ui.paragraph("paragraph", options={"markdown": True})
            menu2 = page.ui.texts.menu(p2, save_funcs=[
              page.js.alert(p2.dom.content)
            ], update_funcs=[
              p2.build("Updated paragraph")
            ], profile=True)

        :param component:
        :param title:
        :param copy:
        :param editable:
        :param refresh:
        :param visible:
        :param post:
        :param height:
        :param save_funcs:
        :param update_funcs:
        :param menu_items:
        :param options:
        :param profile:
        """
        # Add font awesome
        self.page.jsImports.add("font-awesome")
        self.page.cssImport.add("font-awesome")
        options, link = options or {}, None
        menu_items = menu_items or []
        if isinstance(component, list):
            component = self.page.ui.div(component)
        if title is not None:
            if isinstance(title, dict):
                sub_title = self.page.ui.div(list(title.values())[0])
                sub_title.options.managed = False
                sub_title.style.css.color = self.page.theme.greys[4]
                sub_title.style.css.text_transform = "lowercase"
                sub_title.style.css.display = "inline"
                sub_title.style.css.font_size = self.page.body.style.globals.font.normal(-3)
                comp_title = self.page.ui.title("<b>%s</b> %s" % (list(title.keys())[0], sub_title.html()))
            else:
                comp_title = self.page.ui.title(title)
                comp_title.style.css.bold()
            comp_title.style.css.float = "left"
            comp_title.style.css.font_size = self.page.body.style.globals.font.normal(-2)
            comp_title.style.css.color = self.page.theme.greys[-2]
            menu_items.insert(0, comp_title)
        component.style.css.margin_top = 0
        commands = [("Edit", editable, 15), ("Hide", visible, 15)]
        if hasattr(component.dom, 'copy'):
            commands.insert(0, ("Copy", copy, 18))
        if post is not None:
            link = "fas fa-link"
            if isinstance(post, dict):
                post_url = post["url"]
            else:
                post_url = post
                post = {}
            commands.extend([('ReSt', link, 15), ("Build", refresh, 15)])
        for typ, icon, size in commands:
            if typ == "Edit" and getattr(component, '_js__builder__') is None:
                continue

            if icon:
                if isinstance(icon, tuple):
                    icon = icon[0]
                r = self.page.ui.icons.awesome(
                    icon, align="center", text=typ, tooltip=typ, height=height, width=(size, 'px'), options=options,
                    profile=profile)
                r.span.style.css.hide()
                r.icon.style.add_classes.div.color_hover()
                r.icon.style.css.font_factor(options.get("icon_size", Defaults_css.MENU_ICON_SIZE))
                r.style.css.font_factor(options.get("icon_size", Defaults_css.MENU_ICON_SIZE))
                r.span.style.css.margin = "0 2px -3px -3px"
                if typ == "Edit":
                    r.click([
                        r.dom.css({"background": self.page.theme.success.light, "border-radius": "10px"}).r,
                        self.page.js.window.setTimeout([r.dom.css({"background": "none"}).r], 2000),
                        self.page.js.if_(r.span.dom.innerText() == "Edit", [
                            r.span.build("Lock"),
                            component.dom.setAttribute("contenteditable", True).r,
                            r.icon.build(editable[1])]).else_([
                            r.span.build("Edit"),
                            component.dom.setAttribute("contenteditable", False).r,
                            r.icon.build(editable[0]),
                            component.build(component.dom.innerText())
                        ]),
                    ], profile=profile)
                elif typ == "Copy":
                    r.click([
                        # component.dom.copyToClipboard(options.get("include_html", False)),
                        component.dom.copy(),
                        r.dom.css({"background": self.page.theme.greys[2], "border-radius": "10px"}).r,
                        self.page.js.window.setTimeout([r.dom.css({"background": 'none'}).r], 2000)
                    ], profile=profile)
                elif typ == "Build":
                    r.click([self.page.js.post(**post).onSuccess([
                        component.build(self.page.js.objects.data),
                        r.dom.css({"background": self.page.theme.greys[2], "border-radius": "10px"}).r,
                        self.page.js.window.setTimeout([r.dom.css({"background": 'none'}).r], 2000)
                    ])], profile=profile)
                elif typ == "Hide":
                    r.click([
                        component.dom.toggle(),
                        self.page.js.if_(r.span.dom.innerText() == "Hide", [
                            r.span.build("View"),
                            r.icon.build(visible[1])]).else_([
                            r.span.build("Hide"),
                            r.icon.build(visible[0])
                        ], profile=profile),
                        r.dom.css({"background": self.page.theme.greys[2], "border-radius": "10px"}).r,
                        self.page.js.window.setTimeout([r.dom.css({"background": 'none'}).r], 2000)
                    ])
                elif typ == "ReSt":
                    input_rest = self.page.ui.input(post_url, width=(200, 'px'),
                                                    html_code="%s_rest" % component.htmlCode)
                    input_rest.style.css.text_align = "left"
                    input_rest.style.css.padding_left = 5
                    input_rest.style.css.hide()
                    input_rest.style.css.margin_bottom = 0
                    input_rest.style.css.border_radius = 0
                    input_rest.style.css.background_color = 'none'
                    input_rest.style.css.border_bottom = "1px solid %s" % self.page.theme.colors[-1]
                    input_rest.style.css.line_height = self.page.body.style.globals.font.size
                    input_rest.style.css.font_factor(-2)
                    post["url"] = input_rest.dom.content
                    menu_items.append(input_rest)
                    r.click([
                        input_rest.dom.toggle(),
                        r.dom.css({"background": self.page.theme.greys[2], "border-radius": "10px"}).r,
                        self.page.js.window.setTimeout([r.dom.css({"background": 'none'}).r], 2000)], profile=profile)
                    input_rest.enter([r.dom.events.trigger("click")])
                menu_items.append(r)
        if save_funcs is not None:
            r = self.page.ui.icons.awesome(
                "fas fa-save", align="center", text="Save", height=height, width=(35, 'px'), options=options,
                profile=profile)
            r.span.style.css.line_height = r.style.css.height
            r.icon.style.css.font_factor(options.get("icon_size", Defaults_css.MENU_ICON_SIZE))
            r.style.css.font_factor(options.get("icon_size", Defaults_css.MENU_ICON_SIZE))
            r.span.style.css.margin = "0 2px -3px -3px"
            r.click([
                        r.dom.css({"background": self.page.theme.greys[2], "border-radius": "10px"}).r,
                        self.page.js.window.setTimeout([r.dom.css({"background": "none"}).r], 2000),
                    ] + save_funcs, profile=profile)
            menu_items.append(r)
        if update_funcs is not None:
            if not options.get("auto") or options.get("refresh"):
                r = self.page.ui.icons.awesome(
                    "fas fa-sync-alt", align="center", tooltip="Sync", height=height, width=(15, 'px'), options=options,
                    profile=profile)
                r.icon.style.css.font_factor(options.get("icon_size", Defaults_css.MENU_ICON_SIZE))
                r.style.css.font_factor(options.get("icon_size", Defaults_css.MENU_ICON_SIZE))
                r.click([
                            r.dom.css({"background": self.page.theme.greys[2], "border-radius": "10px"}).r,
                            self.page.js.window.setTimeout([r.dom.css({"background": "none"}).r], 2000),
                        ] + update_funcs, profile=profile)
                menu_items.append(r)
            if options.get("auto"):
                # Do not display the refresh button if auto
                self.page.body.onReady([
                    self.page.js.window.setInterval(
                        update_funcs, "%s_interval" % component.htmlCode, milliseconds=options.get("auto") * 1000,
                        profile=profile, run_on_start=options.get("run_on_start", True))])
        trash = self.page.ui.icons.awesome(
            "fas fa-trash", align="center", height=height, width=(10, 'px'), options=options, profile=profile)
        trash.icon.style.css.font_factor(options.get("icon_size", Defaults_css.MENU_ICON_SIZE))
        trash.style.css.font_factor(options.get("icon_size", Defaults_css.MENU_ICON_SIZE))
        trash.style.css.margin_left = 10
        trash.icon.style.add_classes.div.danger_hover()
        menu_items.append(trash)
        container = self.page.ui.div(menu_items, align="right", options=options, profile=profile)
        container.style.css.border_bottom = "1px solid {}".format(self.page.theme.greys[2])
        container.style.css.margin_bottom = 4
        container.style.css.white_space = "nowrap"
        column = self.col([container, component], height=(100, "%"))
        trash.click([column.dom.hide()])

        def add_command(icon: str, tooltip: str = "", size: int = 10, toggle_icon: str = None,
                        default_event: bool = True) -> html.Html.Html:
            """


          :param icon:
          :param tooltip:
          :param size:
          :param toggle_icon:
          :param default_event:
          """
            comp = self.page.ui.icons.awesome(
                icon, tooltip=tooltip, height=height, width=(size, 'px'), options=options, profile=profile)
            comp.icon.style.css.font_factor(options.get("icon_size", Defaults_css.MENU_ICON_SIZE))
            comp.style.css.font_factor(options.get("icon_size", Defaults_css.MENU_ICON_SIZE))
            comp.style.css.margin_left = 5
            comp.style.css.margin_right = 5
            container.insert(0, comp)
            if toggle_icon is not None and default_event:
                comp.click([
                    comp.icon.build(toggle_icon)
                ])
            return comp

        def others(items: Union[List[html.Html.Html], html.Html.Html], icon: str = "fas fa-bars", tooltip: str = "",
                   size: int = 10) -> html.Html.Html:
            """
          Add a bespoke popup menu.
          The menu is empty and items must be passed.

          Usage::

            slider = page.ui.slider()
            search = page.ui.inputs.search()
            large = page.ui.buttons.large("Validate", align="center")
            popup_menu = menu_logs.others([search, slider, large])
            large.click([popup_menu.dom.hide()])

          :param items: The HTML component to put to the menu
          :param icon: The icon in the tools bar for this menu
          :param tooltip: A tooltip message on the icon
          :param size: The icon side
          """
            comp = self.page.ui.icons.awesome(
                icon, tooltip=tooltip, height=height, width=(size, 'px'), options=options, profile=profile)
            comp.icon.style.css.font_factor(options.get("icon_size", Defaults_css.MENU_ICON_SIZE))
            comp.style.css.font_factor(options.get("icon_size", Defaults_css.MENU_ICON_SIZE))
            comp.style.css.margin_left = 5
            comp.style.css.margin_right = 5
            if not isinstance(items, list):
                items = [items]
            popup_columns = self.page.ui.modals.popup(items, options={"background": False})
            popup_columns.window.style.css.border = "1px solid %s" % self.page.theme.greys[3]
            popup_columns.window.style.css.min_width = 120
            popup_columns.window.style.css.background = self.page.theme.greys[0]
            popup_columns.options.closure = False
            popup_columns.window.focusout([popup_columns.dom.hide()])
            comp.click([
                popup_columns.dom.show(),
                popup_columns.window.dom.focus(prevent_scroll=True),
                popup_columns.js.event_position(left=-130)])
            container.insert(-1, comp)
            return popup_columns

        column.add_command = add_command
        column.others = others
        html.Html.set_component_skin(container)
        return column

    @property
    def pyk(self) -> pyks.Bespoke:
        """Bespoke catalog of components.

        Usages::

          text = page.ui.pyk.progress.circle()
          text.style.css.color = "red"
        """
        return pyks.Bespoke(self)

    @property
    def animations(self) -> CompAnimations.Animations:
        """Bespoke CSS and / or components with effects.
        This could be used to animate the cursor or add a loading events.

        More details on the :py:class:`Animations property <epyk.interfaces.components.CompAnimations.Animations>` page
        """
        return CompAnimations.Animations(self)

    def component(self, alias: str, verbose: bool = None, **kwargs):
        """Load a standalone component inheriting from `Standalone.Component`.

        Usage::

            comp = page.ui.component("test-color")
            comp.prepare(text="Test")

        :param alias: The component selector
        :param verbose: Display extra log messages
        """
        return self.page._props["schema"][alias](self.page, verbose=verbose, **kwargs)

    @property
    def selectors(self):
        """Get the list of bespoke selector aliases loaded as components """
        return self.page._props["schema"].keys()


class WebComponents:

    def __init__(self, page: primitives.PageModel):
        self.page = page
        self.fwks = {}
        self.page.properties.context["libs"] = Defaults_css.WEB_LIBS

    @property
    def default(self) -> str:
        return self.page.properties.context["libs"]

    @default.setter
    def default(self, alias: str):
        self.page.properties.context["libs"] = alias

    @property
    def std(self) -> Components:
        """ The internal components. """
        if 'ui' not in self.fwks:
            self.fwks["ui"] = Components(self.page)
        return self.fwks["ui"]

    @property
    def jqui(self) -> JqueryUI.Components:
        """JQuery UI is a curated set of user interface interactions, effects, widgets, and themes built on top of the
        jQuery JavaScript Library. Whether you're building highly interactive web applications or you just need to add
        a date picker to a form control, jQuery UI is the perfect choice.

        More details on the :py:class:`Jquery property <epyk.fwk.jqui.UI.Components>` page

        `jqueryui <https://jqueryui.com/>'_
        """
        if 'jqui' not in self.fwks:
            self.fwks["jqui"] = JqueryUI.Components(self.page)
        return self.fwks["jqui"]

    @property
    def bs(self) -> BoostrapUI.Components:
        """Add the entire Bootstrap framework as a dependency to the framework.
        This will enable more components to the framework.
        More details on the :py:class:`Bootstrap property <epyk.fwk.bs.UI.Components>` page

        ..note::

          This will be using bootstrap 5.

        Usage::

          icon = page.web.bs.icons.danger()
        """
        if 'bs' not in self.fwks:
            self.fwks["bs"] = BoostrapUI.Components(self.page)
        return self.fwks["bs"]

    @property
    def mdc(self) -> MaterialUI.Components:
        """Set the material components entry point.
        This will be available in the same way than ui is available for anything else in the core framework.

        More details on the :py:class:`Bootstrap property <epyk.fwk.mdc.UI.Components>` page

        `Material <https://material.io/develop/web/>`_
        `Material Components <https://material.io/components?platform=web>`_

        :return: Python HTML object
        """
        if 'mdc' not in self.fwks:
            self.fwks["mdc"] = MaterialUI.Components(self.page)
        return self.fwks["mdc"]

    @property
    def tui(self) -> ToastUI.Components:
        """Add the entire TOAST UI framework as a dependency to the framework.
        This will enable more components to the framework.

        `Toast <https://ui.toast.com/>`_

        Usage::

          dt = page.web.tui.date()
          cal = page.web.tui.calendar()
        """
        if 'tui' not in self.fwks:
            self.fwks["tui"] = ToastUI.Components(self.page)
        return self.fwks["tui"]

    @property
    def clr(self) -> ClarityUI.Components:
        """Clarity is a scalable, customizable, open source design system bolstered by the people that build with it,
        the people we build it for, and the community that makes us who we are.

        `Clarity <https://clarity.design/>`_
        """
        if 'clr' not in self.fwks:
            self.fwks["clr"] = ClarityUI.Components(self.page)
        return self.fwks["clr"]

    @property
    def evr(self) -> EvergreenUI.Components:
        """Evergreen is a React UI Framework for building ambitious products on the web. Brought to you by Segment.

        `Evergreen <https://evergreen.segment.com/introduction/getting-started>`_
        """
        if 'evr' not in self.fwks:
            self.fwks["evr"] = EvergreenUI.Components(self.page)
        return self.fwks["evr"]

    @property
    def ftw(self) -> FluentUI.Components:
        """Simple components that focus on appearance and styling while showing the visual language of Office.

        Usage::

          page.web.ftw.check(label="Test Checkbox")
          page.web.ftw.check(label="Test Checkbox 2")
          page.web.ftw.buttons.small("Test Checkbox 2")
          page.web.ftw.icon("add")
          page.web.ftw.toggle(True)
          page.web.ftw.loading("add", options={"large": True})
          select = page.web.ftw.lists.select(selected="value 2")
          data = ["value 1", "value 2", "value 3"]
          select.data = select.parsers.from_list(data)
        """
        if 'ftw' not in self.fwks:
            self.fwks["ftw"] = FluentUI.Components(self.page)
        return self.fwks["ftw"]
