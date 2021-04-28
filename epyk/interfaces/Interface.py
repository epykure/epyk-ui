#!/usr/bin/python
# -*- coding: utf-8 -*-


from epyk.core import html

from epyk.core.css import Defaults_css

from epyk.core.js import Imports

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
from epyk.interfaces.bs import Bs
from epyk.interfaces.mt import Mt
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


class Components:

  def __init__(self, page):
    self.rptObj = page
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
    self.table = self.tables.tabulator
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

  def css(self, css_attrs):
    """
    Description:
    ------------
    Change the CSS Style of the main container in the page.

    Usage::



    Attributes:
    ----------
    :param css_attrs: Dictionary. The CSS attributes to be applied.
    """
    self.page.properties.css.container_style(css_attrs)
    return self

  def print(self, text=None, end="\n", html_code=None, options=None, profile=None):
    """
    Description:
    ------------
    Mimic the print function available in Python.
    This will create a div container with the content as a string.

    This function can be also used to display Python function. Inspect module will be used in this case to get the
    source code.

    Usage::

      import pandas
      page.ui.print('pandas: {}'.format(pandas.__version__))

    Attributes:
    ----------
    :param text: String. Optional. The content to be displayed.
    :param end: String. Optional. The end of line.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
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
    return div

  @property
  def codes(self):
    """
    Description:
    ------------
    Group all the UI Components dedicated to display code fragments.

    This will wrap the Javascript module codemirror.

    Usage::


    Related Pages:

      https://codemirror.net/doc/manual.html
    """
    return CompCodes.Code(self)

  @property
  def pollers(self):
    """
    Description:
    ------------
    Group all the UI with polling feature.

    Usage::

      page = pk.Page()
      page.ui.pollers
    """
    return CompPollers.Poller(self)

  @property
  def network(self):
    """
    Description:
    ------------
    Group all the UI Components dedicated to display messaging services.

    This category will group (chat, RSS streams, forum, bot ...).
    Those components are interactive and they would require underlying services and databases in order to fully work.

    Usage::

        page = pk.Page()
        page.ui.network
    """
    return CompNetwork.Network(self)

  @property
  def sliders(self):
    """
    Description:
    ------------
    Group all the UI components dedicated to produce slider items.

    Those components are interactive and can be used to filter the data on other items in the dashboard.
    Those components are mainly relying on Jquery and JqueryUi.

    Usage::

        page = pk.Page()
        page.ui.sliders
    """
    return CompSliders.Sliders(self)

  @property
  def _3d(self):
    """
    Description:
    ------------
    Group all the 3D charts.

    Usage::
    """
    return CompCharts.Chart3d(self)

  @property
  def _2d(self):
    """
    Description:
    ------------
    Group all the 2D charts.

    Usage::

    Templates:

    """
    return CompCharts.Chart2d(self)

  @property
  def titles(self):
    """
    Description:
    ------------
    Group all the UI components dedicated to produce titles.

    Usage::

    """
    return CompTitles.Titles(self)

  @property
  def links(self):
    """
    Description:
    ------------
    Group all the UI components dedicated to produce links to another page or website.

    Usage::

    Templates:

    """
    return CompLinks.Links(self)

  @property
  def navigation(self):
    """
    Description:
    ------------
    Group all the UI components dedicated to produce navigation components such as navigation bar, footer, banner...

    Usage::

    Templates:

    """
    return CompNavigation.Navigation(self)

  @property
  def bars(self):
    """
    Description:
    ------------
    Group all the UI components dedicated to produce Navigation bar components such as navigation bar, footer, banner...

    Usage::

    Templates:

    """
    return CompNavigation.NavBars(self)

  @property
  def banners(self):
    """
    Description:
    ------------
    Group all the available banners.

    Usage::

    Templates:

    """
    return CompNavigation.Banners(self)

  @property
  def pictos(self):
    """
    Description:
    ------------
    Group all the built in pictogram.
    """
    return CompPictos.Pictogram(self)

  @property
  def rich(self):
    """
    Description:
    ------------
    Group all the UI components dedicated to produce rich HTML Components.

    This category will take into account very specific and bespoke components.
    """
    return CompRich.Rich(self)

  @property
  def vignets(self):
    """
    Description:
    ------------
    Group all the UI components dedicated to produce rich HTML Components.

    This category will take into account very specific and bespoke components.

    Usage::


    """
    return CompVignets.Vignets(self)

  @property
  def numbers(self):
    """
    Description:
    ------------
    Group all the UI components dedicated to produce Numbers components.

    The items in this category will not be editable and they will only provide nice number renderings.

    Usage::


    """
    return CompNumbers.Numbers(self)

  @property
  def texts(self):
    """
    Description:
    ------------
    Group all the UI components dedicated to produce text components.

    The items in this category will not be editable and they will only provide nice text structure like paragraph,
    formatted text...

    Usage::


    """
    return CompTexts.Texts(self)

  @property
  def images(self):
    """
    Description:
    ------------
    Group all the UI components dedicated to produce image or collection of images.

    Usage::


    """
    return CompImages.Images(self)

  @property
  def lists(self):
    """
    Description:
    ------------
    Group all the UI components dedicated to produce list or selection items.

    Simple list, trees or DropDown boxes will be part of this category of items.

    Usage::


    """
    return CompLists.Lists(self)

  @property
  def trees(self):
    """
    Description:
    ------------
    Group all the UI components dedicated to produce Trees or selection items.

    Usage::

    Templates:

    """
    return CompTrees.Trees(self)

  @property
  def geo(self):
    """
    Description:
    ------------
    Group all the UI components dedicated to produce Trees or selection items.

    Usage::

    Templates:

    """
    return CompGeo.Geo(self)

  @property
  def buttons(self):
    """
    Description:
    ------------
    Group all the UI components dedicated to produce button or checkbox.

    Usage::

    Templates:

    """
    return CompButtons.Buttons(self)

  @property
  def tables(self):
    """
    Description:
    ------------
    Group all the UI components dedicated to produce tables or pivot tables.

    Different kind of tables are available in the framework (Tabulator, DataTable, PivotTable or even a bespoke
    implementation).

    Usage::

    Templates:

    """
    return CompTables.Tables(self)

  @property
  def steps(self):
    """
    Description:
    ------------
    Group all the UI steps components.

    Usage::

    Templates:

    """
    return CompSteps.Steppers(self)

  @property
  def drawers(self):
    """
    Description:
    ------------
    Group all the UI drawers components.

    Usage::

    Templates:

    """
    return CompDrawers.Drawers(self)

  @property
  def steppers(self):
    """
    Description:
    ------------
    Group all the UI steppers components.

    Usage::

    Templates:

    """
    return CompSteppers.Steppers(self)

  @property
  def media(self):
    """
    Description:
    ------------
    Group all the UI components dedicated to produce media (video and audio) items.

    Plain Vanilla HTML5 components.

    Usage::

    Templates:

    """
    return CompMedia.Media(self)

  @property
  def inputs(self):
    """
    Description:
    ------------
    Group all the UI components dedicated to produce input items.

    Those components are editable items which need to be updated by the user of the dashboard.
    This category will take into account TextArea, input text...

    Usage::

    Templates:

    """
    return CompInputs.Inputs(self)

  @property
  def fields(self):
    """
    Description:
    ------------
    Group all the UI components dedicated to produce input items.

    Those components are editable items which need to be updated by the user of the dashboard.
    This category will take into account TextArea, input text...

    Usage::

    Templates:

    """
    return CompFields.Fields(self)

  @property
  def timelines(self):
    """
    Description:
    ------------

    Usage::

    Templates:

    """
    return CompFields.Timelines(self)

  @property
  def icons(self):
    """
    Description:
    ------------
    Group all the UI components dedicated to produce icon items.

    This category of component will rely on the font-awesome library for the final display.

    Usage::

    Templates:

    """
    return CompIcons.Icons(self)

  @property
  def menus(self):
    """
    Description:
    ------------
    Group all the UI menus.

    Usage::

    Templates:

    """
    return CompMenus.Menus(self)

  @property
  def panels(self):
    """
    Description:
    ------------
    Group all the UI panels.

    Usage::

    Templates:

    """
    return CompPanels.Panels(self)

  @property
  def layouts(self):
    """
    Description:
    ------------
    Group all the UI components dedicated to produce component containers.

    All the items in this category are dedicated for the structure of the dashboard and they
    are mainly holder of other components.
    This will mainly rely on bootstrap for the display of the different objects in the page.

    Usage::

    Templates:

    """
    return CompLayouts.Layouts(self)

  @property
  def forms(self):
    """
    Description:
    ------------
    Group all the Forms components dedicated to drop data.

    Related Pages:

      https://www.w3schools.com/html/html_forms.asp

    Usage::

    Templates:

    """
    return CompForms.Forms(self)

  @property
  def modals(self):
    """
    Description:
    ------------
    Group all the UI components dedicated to produce modal components.

    Usage::

    Templates:

    """
    return CompModals.Modals(self)

  @property
  def charts(self):
    """
    Description:
    ------------
    Group all the UI components dedicated to produce charts.

    Different kind of charts framework are available (ChartJs, Plotly, C3, Billboard, NVD3, DC, Vis or even D3).

    Usage::

    Templates:

    """
    return CompCharts.Graphs(self)

  @property
  def tags(self):
    """
    Description:
    ------------
    Group all the other tags available in HTML.

    Those tags can be considered as normal HTML component, which means Js and CSS features are also available.

    Usage::

    Templates:

    """
    return CompTags.Tags(self)

  @property
  def calendars(self):
    """
    Description:
    ------------
    Group all the component related to the time and calendar management.

    Usage::

    Templates:

    """
    return CompCalendars.Calendar(self)

  @property
  def delimiters(self):
    """
    Description:
    ------------
    Shortcut property to the various delimiters styles.

    Related Pages:

      https://codepen.io/ibrahimjabbari/pen/ozinB

    Usage::

    Templates:

    """
    return CompLayouts.Delimiter(self)

  def contents(self, title="Contents", top=10, right=10, left=None, width=(None, "%"), height=(None, "px"),
               html_code=None, options=None, profile=None):
    """
    Description:
    ------------
    Add a content table to the page.

    Usage::

        contents = page.ui.contents()

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/contents_table.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/paragraph.py

    Attributes:
    ----------
    :param title: String. Optional. The title for the content table.
    :param top: Integer. Optional. The top property affects the vertical position of a positioned element.
    :param right: Integer. Optional. The right property affects the horizontal position of a positioned element.
    :param left: Integer. Optional. The left property affects the horizontal position of a positioned element.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    html_code = html_code or "content"
    if html_code not in self.page.components:
      html_contents = html.HtmlTextComp.ContentsTable(self.page, title, width, height, html_code, options, profile)
      html_contents.menu = self.page.ui.div(html_code="%s_page" % html_code)
      html_contents.style.css.max_height = "60%"
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
    """
    Description:
    ------------
    Hook to allow the creation of bespoke component using specific configurations.
    Components can be self contained in a module and rely on external packages.

    Tip: Look at the Import.extend function in order to add external Js and CSS modules to your environment.

    Usage::

    Templates:


    Attributes:
    ----------
    :param html_cls: Class. The bespoke HTML component.
    :param args: The python attributes used in the HTML component constructor.
    :param kwargs: The python attributes used in the HTML component constructor.
    """
    return html_cls(self.page, *args, **kwargs)

  def _tags(self, vals=None, title="", icon="", width=(100, "%"), height=(None, "px"), html_code=None, profile=None):
    """
    Description:
    ------------

    Usage::

    Templates:



    Attributes:
    ----------
    :param vals: Optional.
    :param title: String. Optional. Teh title for teh tag component.
    :param icon: String. Optional. A string with the value of the icon to display from font-awesome.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    return html.HtmlTextEditor.Tags(
      self.page, vals, title, icon, (self.page.body.style.globals.font.size, 'px'), width, height, html_code,
      profile)

  def loading(self, text="Loading", color=None, options=None, profile=None):
    """
    Description:
    ------------
    Entry point to the loading component.

    This component will create a
      - label component for the text
      - icon component for the loading icon

    Usage::

    Templates:



    Attributes:
    ----------
    :param text: String. Optional. The text in the component (during the loading).
    :param color: String. Optional. The font color in the component. Default inherit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    html_loading = html.HtmlOthers.Loading(
      self.page, text, color, (self.page.body.style.globals.font.size, 'px'), options or {}, profile)
    return html_loading

  def breadcrumb(self, values=None, selected=None, width=(100, '%'), height=(30, 'px'), html_code=None, options=None,
                 profile=None):
    """
    Description:
    ------------
    Add Breadcrumb information to the page.

    Usage::

        page.ui.breadcrumb([
          {"text": 'part 1', 'url': 'part1'},
          {"text": 'part 2', 'url': 'part2'},
          {"text": 'part 3', 'url': 'part3'},
        ])

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/breadcrumb.py

    Attributes:
    ----------
    :param values: List. Optional. The breadcrumb record definition.
    :param selected: Integer. Optional. The selected item index.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
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
    return html_breadcrumb

  def form(self, components=None, helper=None):
    """
    Description:
    ------------
    Creates an new empty form.

    Usage::

      f = page.ui.form()

    Templates:

    Attributes:
    ----------
    :param components: List. Optional. The HTML components to be added to the HTML form.
    :param helper: String. Optional. The value to be displayed to the helper icon.
    """
    form = html.HtmlContainer.Form(self.page, components or [], helper)
    return form

  def json(self, data=None, width=(None, '%'), height=(100, '%'), options=None, profile=None):
    """
    Description:
    ------------
    HTML component to display a Json.

    Usage::

    Templates:


    Related Pages:

      https://github.com/mohsen1/json-formatter-js

    Attributes:
    ----------
    :param data: Dictionary. Optional. The Json object to be display.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    data = data or {}
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    h_json = html.HtmlOthers.HtmlJson(self.page, data, width, height, options, profile)
    if height[1] != '%':
      h_json.style.css.overflow = 'auto'
    return h_json

  def slideshow(self, components=None, width=(100, "%"), height=('auto', ""), options=None, profile=None):
    """
    Description:
    ------------
    SlideShow component for pictures from the tiny-slider library.
    More details regarding this library here: https://github.com/ganlanyuan/tiny-slider.

    Usage::

    Templates:


    Related Pages:

      https://github.com/ganlanyuan/tiny-slider
      http://ganlanyuan.github.io/tiny-slider/demo/

    Attributes:
    ----------
    :param components: List. Optional. With the different components.
    :param width: Tuple. Optional. The component width in pixel or percentage.
    :param height: Tuple. Optional. The component height in pixel.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width)
    height = Arguments.size(height, "px")
    html_i = html.HtmlImage.SlideShow(self.page, components or [], width, height, options or {}, profile)
    return html_i

  def qrcode(self, data=None, width=(128, 'px'), height=(128, 'px'), options=None, profile=None):
    """
    Description:
    ------------
    HTML component to display a QR Code from a string.

    Usage::

    Templates:


    Related Pages:

      https://davidshimjs.github.io/qrcodejs/

    TODO: Add options

    Attributes:
    ----------
    :param data: String. Optional. The value to be converted to QR Code.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    data = data or {}
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    h_qrcode = html.HtmlOthers.HtmlQRCode(self.page, data, width, height, options, profile)
    if height[1] != '%':
      h_qrcode.style.css.overflow = 'auto'
    return h_qrcode

  def captcha(self, text="Submit", width=(None, 'px'), height=(None, 'px'), options=None, profile=None):
    """
    Description:
    ------------

    Usage::

    Templates:


    Attributes:
    ----------
    :param text: String. Optional. The button content for the captcha validation.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="px")
    height = Arguments.size(height, unit="px")
    captcha = html.HtmlOthers.HtmlCaptcha(self.page, text, width, height, options or {}, profile)
    return captcha

  def postit(self, components=None, anchor=None, options=None, profile=None):
    """
    Description:
    ------------

    Usage::

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/postit.py

    Attributes:
    ----------
    :param components: Components. Optional.
    :param anchor: Component. Optional.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    postit = self.page.ui.div(options=options, profile=profile)
    if anchor is None:
      anchor = self.page.ui.icon("fas fa-map-marker")
      anchor.style.css.padding = "4px"
      postit += anchor
    postit.anchor = anchor
    popup = self.page.ui.div(components, width=(None, 'px'), options=options, profile=profile)
    popup.css({"display": 'none', 'position': 'absolute', 'border': '1px solid black', 'border-radius': '5px',
               'padding': '5px', 'background': self.page.theme.greys[0]})
    postit += popup
    postit.popup = popup
    anchor.mouse([
      popup.dom.position(dx=10, dy=10), popup.dom.css({"display": 'block'}).r
    ],
      [
        popup.dom.css({"display": 'none'}).r]
    )
    return postit

  def extension(self, package_name, alias=None):
    """
    Description:
    ------------
    Add an extension base on it is name.

    Usage::

    Templates:

    Attributes:
    ----------
    :param package_name: String. The package name.
    :param alias: String. Optional. The alias for the link in report.ui.
    """
    mod = __import__(package_name)
    __import__("%s.components" % package_name)
    if alias is None:
      alias = getattr(mod.components, 'alias', package_name)
    setattr(self, alias, mod.components.Components(self))

  def asterix(self, tooltip, family=None, width=(None, 'px'), html_code=None, height=(None, "px"), color=None,
              align="left", options=None, profile=None):
    """
    Description:
    ------------

    Usage::

    Templates:


    Attributes:
    ----------
    :param tooltip:
    :param family:
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param color:
    :param align:
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    component = self.icon("fas fa-asterisk", family, width, html_code, height, color, tooltip, align, options, profile)
    component.style.css.vertical_align = "top"
    component.style.css.color = self.page.theme.greys[5]
    return component

  @html.Html.css_skin()
  def menu(self, component, copy="fas fa-copy", editable=("fas fa-user-edit", "fas fa-user-lock"),
           refresh="fas fa-redo-alt", visible=('fas fa-eye-slash', "fas fa-eye"), post=None,
           height=(18, 'px'), save_funcs=None, update_funcs=None, menu_items=None, options=None, profile=None):
    """
    Description:
    -----------


    TODO: Improve the editable feature for Markdown.

    Usage::

        p2 = page.ui.paragraph("paragraph", options={"markdown": True})
        menu2 = page.ui.texts.menu(p2, save_funcs=[
          page.js.alert(p2.dom.content)
        ], update_funcs=[
          p2.build("Updated paragraph")
        ], profile=True)

    Attributes:
    ----------
    :param component:
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
    options, link = options or {}, None
    menu_items = menu_items or []
    component.style.css.margin_top = 0
    commands = [("Copy", copy), ("Edit", editable), ("Hide", visible)]
    if post is not None:
      link = "fas fa-link"
      if isinstance(post, dict):
        post_url = post["url"]
      else:
        post_url = post
        post = {}
      #, jsData = None, varName = "response", is_json = True, components
      commands.extend([('ReSt', link), ("Build", refresh)])
    for typ, icon in commands:
      if icon:
        if isinstance(icon, tuple):
          icon = icon[0]
        r = self.page.ui.icons.awesome(
          icon, text=typ, height=height, width=(35, 'px'), options=options, profile=profile)
        r.span.style.css.line_height = r.style.css.height
        r.icon.style.css.font_factor(-5)
        r.style.css.font_factor(-5)
        r.span.style.css.margin = "0 2px -3px -3px"
        if typ == "Edit":
          r.click([
            r.dom.css({"background": self.page.theme.success[0], "border-radius": "10px"}).r,
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
            component.dom.copyToClipboard(options.get("include_html", False)),
            r.dom.css({"background": self.page.theme.success[0], "border-radius": "10px"}).r,
            self.page.js.window.setTimeout([r.dom.css({"background": 'none'}).r], 2000)
          ], profile=profile)
        elif typ == "Build":
          r.click([self.page.js.post(**post).onSuccess([
            component.build(self.page.js.objects.data),
            r.dom.css({"background": self.page.theme.success[0], "border-radius": "10px"}).r,
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
            r.dom.css({"background": self.page.theme.success[0], "border-radius": "10px"}).r,
            self.page.js.window.setTimeout([r.dom.css({"background": 'none'}).r], 2000)
          ])
        elif typ == "ReSt":
          input_rest = self.page.ui.input(post_url, width=(200, 'px'), html_code="%s_rest" % component.htmlCode)
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
            r.dom.css({"background": self.page.theme.success[0], "border-radius": "10px"}).r,
            self.page.js.window.setTimeout([r.dom.css({"background": 'none'}).r], 2000)], profile=profile)
          input_rest.enter([r.dom.events.trigger("click")])
        menu_items.append(r)
    if save_funcs is not None:
      r = self.page.ui.icons.awesome(
        "fas fa-save", text="Save", height=height, width=(35, 'px'), options=options, profile=profile)
      r.span.style.css.line_height = r.style.css.height
      r.icon.style.css.font_factor(-5)
      r.style.css.font_factor(-5)
      r.span.style.css.margin = "0 2px -3px -3px"
      r.click([
          r.dom.css({"background": self.page.theme.success[0], "border-radius": "10px"}).r,
          self.page.js.window.setTimeout([r.dom.css({"background": "none"}).r], 2000),
        ] + save_funcs, profile=profile)
      menu_items.append(r)
    if update_funcs is not None:
      r = self.page.ui.icons.awesome(
        "fas fa-sync-alt", text="Sync", height=height, width=(35, 'px'), options=options, profile=profile)
      r.span.style.css.line_height = r.style.css.height
      r.icon.style.css.font_factor(-5)
      r.style.css.font_factor(-5)
      r.span.style.css.margin = "0 2px -3px -3px"
      r.click([
                r.dom.css({"background": self.page.theme.success[0], "border-radius": "10px"}).r,
                self.page.js.window.setTimeout([r.dom.css({"background": "none"}).r], 2000),
              ] + update_funcs, profile=profile)
      menu_items.append(r)
    dots = self.page.ui.icons.awesome(
      "fas fa-ellipsis-v", height=height, width=(10, 'px'), options=options, profile=profile)
    dots.icon.style.css.font_factor(-5)
    dots.style.css.font_factor(-5)
    dots.style.css.margin_left = 10
    menu_items.append(dots)
    container = self.page.ui.div(menu_items, align="right", options=options, profile=profile)
    dots.click([container.dom.hide()])
    component.move()
    return container


class WebComponents:

  def __init__(self, page):
    self.page = page
    self.fwks = {}

  @property
  def std(self):
    """
    Description:
    ------------

    Usage::

    Templates:

    :rtype: Components
    """
    if 'ui' not in self.fwks:
      self.fwks["ui"] = Components(self.page)
    return self.fwks["ui"]

  @property
  def bs(self):
    """
    Description:
    ------------
    Add the entire Bootstrap framework as a dependency to the framework.
    This will enable more components to the framework.

    Usage::

      icon = page.web.bs.icons.danger()

    Templates:


    :rtype: Bs.Bootstrap
    """
    if self.page.ext_packages is None:
      self.page.ext_packages = {}
    self.page.ext_packages.update(Imports.BOOTSTRAP)
    if 'bs' not in self.fwks:
      self.page.jsImports.add("bootstrap")
      self.page.cssImport.add("bootstrap")
      self.fwks["bs"] = Bs.Bootstrap(self.page)
    return self.fwks["bs"]

  @property
  def mt(self):
    """
    Description:
    ------------
    Set the material components entry point.
    This will be available in the same way than ui is available for anything else in the core framework.

    Usage::

    Templates:


    Related Pages:

      https://material.io/develop/web/

    :rtype: Mt.Materials

    :return: Python HTML object
    """
    if self.page.ext_packages is None:
      self.page.ext_packages = {}
    self.page.ext_packages.update(Imports.MATERIAL_DESIGN_COMPONENTS)
    if 'mt' not in self.fwks:
      self.page.jsImports.add("material-components-web")
      self.page.cssImport.add("material-components-web")
      self.page.css.customText('''
:root {--mdc-theme-primary: %(color)s; --mdc-theme--on-primary: %(color)s; --mdc-theme--primary-bg: %(color)s;}
.mdc-text-field--focused:not(.mdc-text-field--disabled) .mdc-floating-label {color: var(--mdc-theme-primary);}
          ''' % {"color": self.page.theme.success[1]})

      self.fwks["mt"] = Mt.Materials(self.page)
    return self.fwks["mt"]
