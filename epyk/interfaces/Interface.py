#!/usr/bin/python
# -*- coding: utf-8 -*-


from epyk.core import html

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


class Components(object):
  def __init__(self, rptObj):
    self.rptObj = rptObj

    # Special shortcut for some components
    self.button = self.buttons.button #: shortcut for button :func:`epyk.interfaces.components.CompButtons.Buttons.button`
    self.toggle = self.buttons.toggle #: shortcut for Toogle button :func:`epyk.interfaces.components.CompButtons.Buttons.toggle`
    self.input = self.inputs.input #: shortcut for input :func:`epyk.interfaces.components.CompInputs.Inputs.input`
    self.div = self.layouts.div #: shortcut for div :func:`epyk.interfaces.components.CompLayouts.Layouts.div`
    self.grid = self.layouts.grid #: shortcut for grid :func:`epyk.interfaces.components.CompLayouts.Layouts.grid`
    self.row = self.layouts.row #: shortcut for row :func:`epyk.interfaces.components.CompLayouts.Layouts.row`
    self.col = self.layouts.col #: shortcut for column :func:`epyk.interfaces.components.CompLayouts.Layouts.col`
    self.table = self.tables.tabulator #: shortcut for tabulator :func:`epyk.interfaces.components.CompTables.Tables.tabulator`
    self.pivot = self.tables.pivot #: shortcut for pivot :func:`epyk.interfaces.components.CompTables.Tables.pivot`
    self.text = self.texts.text #: shortcut for text :func:`epyk.interfaces.components.CompTexts.Texts.text`
    self.title = self.texts.title #: shortcut for title :func:`epyk.interfaces.components.CompTexts.Texts.title`
    self.subtitle = self.titles.subtitle #: shortcut for title :func:`epyk.interfaces.components.CompTexts.Texts.title`
    self.icon = self.images.icon #: shortcut for icon :func:`epyk.interfaces.components.CompImages.Images.icon`
    self.img = self.images.img #: shortcut for img :func:`epyk.interfaces.components.CompImages.Images.img`
    self.list = self.lists.list #: shortcut for list :func:`epyk.interfaces.components.CompLists.Lists.list`
    self.link = self.links.link #: shortcut for link :func:`epyk.interfaces.components.CompLinks.Links.link`
    self.check = self.buttons.check #: shortcut for check :func:`epyk.interfaces.components.CompButtons.Buttons.check`
    self.slider = self.sliders.slider #: shortcut for slider :func:`epyk.interfaces.components.CompSliders.Sliders.slider`
    self.select = self.lists.select #: shortcut for select :func:`epyk.interfaces.components.CompLists.Lists.select`
    self.lookup = self.lists.lookup #: shortcut for lookup :func:`epyk.interfaces.components.CompLists.Lists.lookup`
    self.date = self.fields.cob #: shortcut for date :func:`epyk.interfaces.components.CompFields.Fields.cob`
    self.tree = self.lists.tree #: shortcut for tree :func:`epyk.interfaces.components.CompLists.Lists.tree`
    self.info = self.rich.info #: shortcut for info :func:`epyk.interfaces.components.CompRich.Rich.input`
    self.radio = self.buttons.radio #: shortcut for radio :func:`epyk.interfaces.components.CompButtons.Buttons.radio`
    self.navbar = self.navigation.bar #: shortcut for bar :func:`epyk.interfaces.components.CompNavigation.Navigation.bar`
    self.footer = self.navigation.footer #: shortcut for footer :func:`epyk.interfaces.components.CompNavigation.Navigation.footer`
    self.modal = self.modals.forms #: shortcut for footer :func:`epyk.interfaces.components.CompModals.Modals.forms`
    self.disclaimer = self.modals.disclaimer #: shortcut for footer :func:`epyk.interfaces.components.CompModals.Modals.disclaimer`
    self.drawer = self.drawers.drawer #: shortcut for drawer :func:`epyk.interfaces.components.CompDrawers.Drawers.drawer`
    self.stepper = self.steppers.stepper #: shortcut for steppers :func:`epyk.interfaces.components.CompSteppers.Steppers.stepper`
    self.chips = self.lists.chips #: shortcut for chips :func:`epyk.interfaces.components.CompLists.Lists.chips`
    self.contextual = self.menus.contextual #: shortcut for chips :func:`epyk.interfaces.components.CompMenus.Menus.contextual`
    self.hidden = self.fields.hidden #: shortcut for chips :func:`epyk.interfaces.components.CompInputs.Inputs.input`
    self.number = self.numbers.number #: shortcut for chips :func:`epyk.interfaces.components.CompInputs.Inputs.input`
    self.euro = self.numbers.euro #: shortcut for chips :func:`epyk.interfaces.components.CompInputs.Inputs.input`

    # Shortcut to some important HTML tags
    self.label = self.texts.label
    self.textarea = self.inputs.textarea
    self.header = self.layouts.header
    self.section = self.layouts.section
    self.composite = self.rich.composite

  def css(self, cssAttrs):
    """
    Description:
    ------------
    Change the CSS Style of the main container in the page

    Attributes:
    ----------
    :param cssAttrs: Dictionary. The CSS attributes to be applied
    """
    self.rptObj._props.setdefault("css", {})["container"] = cssAttrs
    return self

  @property
  def codes(self):
    """
    Description:
    ------------
    Group all the UI Components dedicated to display code fragments

    This will wrap the Javascript module codemirror

    Related Pages:

      https://codemirror.net/doc/manual.html
    """
    return CompCodes.Code(self)

  @property
  def network(self):
    """
    Description:
    ------------
    Group all the UI Components dedicated to display messaging services.

    This category will group (chat, RSS streams, forum, bot ...).
    Those components are interactive and they would require underlying services and databases in order to fully work
    """
    return CompNetwork.Network(self)

  @property
  def sliders(self):
    """
    Description:
    ------------
    Group all the UI components dedicated to produce slider items.

    Those components are interactive and can be used to filter the data on other items in the dashboard.
    Those components are mainly relying on Jquery and JqueryUi
    """
    return CompSliders.Sliders(self)

  @property
  def _3d(self):
    """
    Description:
    ------------
    Group all the 3D charts
    """
    return CompCharts.Chart3d(self)

  @property
  def _2d(self):
    """
    Description:
    ------------
    Group all the 2D charts
    """
    return CompCharts.Chart2d(self)

  @property
  def titles(self):
    """
    Description:
    ------------
    Group all the UI components dedicated to produce titles
    """
    return CompTitles.Titles(self)

  @property
  def links(self):
    """
    Description:
    ------------
    Group all the UI components dedicated to produce links to another page or website.
    """
    return CompLinks.Links(self)

  @property
  def navigation(self):
    """
    Description:
    ------------
    Group all the UI components dedicated to produce navigation components such as navigation bar, footer, banner...
    """
    return CompNavigation.Navigation(self)

  @property
  def banners(self):
    """
    Description:
    ------------
    Group all the available banners
    """
    return CompNavigation.Banners(self)

  @property
  def pictos(self):
    """
    Description:
    ------------
    Group all the built in pictogram
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
    """
    return CompVignets.Vignets(self)

  @property
  def numbers(self):
    """
    Description:
    ------------
    Group all the UI components dedicated to produce Numbers components.

    The items in this category will not be editable and they will only provide nice number renderings
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
    """
    return CompTexts.Texts(self)

  @property
  def images(self):
    """
    Description:
    ------------
    Group all the UI components dedicated to produce image or collection of images.
    """
    return CompImages.Images(self)

  @property
  def lists(self):
    """
    Description:
    ------------
    Group all the UI components dedicated to produce list or selection items.

    Simple list, trees or dropdown boxes will be part of this category of items
    """
    return CompLists.Lists(self)

  @property
  def trees(self):
    """
    Description:
    ------------
    Group all the UI components dedicated to produce Trees or selection items.

    """
    return CompTrees.Trees(self)

  @property
  def geo(self):
    """
    Description:
    ------------
    Group all the UI components dedicated to produce Trees or selection items.

    """
    return CompGeo.Geo(self)

  @property
  def buttons(self):
    """
    Description:
    ------------
    Group all the UI components dedicated to produce button or checkbox.
    """
    return CompButtons.Buttons(self)

  @property
  def tables(self):
    """
    Description:
    ------------
    Group all the UI components dedicated to produce tables or pivot tables.

    Different kind of tables are available in the framework (Tabulator, Datatable, PivotTable or even a bespoke
    implementation).
    """
    return CompTables.Tables(self)

  @property
  def steps(self):
    """
    Description:
    ------------
    Group all the UI steps components.
    """
    return CompSteps.Steppers(self)

  @property
  def drawers(self):
    """
    Description:
    ------------
    Group all the UI drawers components.
    """
    return CompDrawers.Drawers(self)

  @property
  def steppers(self):
    """
    Description:
    ------------
    Group all the UI steppers components.
    """
    return CompSteppers.Steppers(self)

  @property
  def media(self):
    """
    Description:
    ------------
    Group all the UI components dedicated to produce media (video and audio) items.

    Plain Vanilla HTML5 components
    """
    return CompMedia.Media(self)

  @property
  def inputs(self):
    """
    Description:
    ------------
    Group all the UI components dedicated to produce input items.

    Those components are editable items which need to be updated by the user of the dashboard.
    This category will take into account textarea, input text...
    """
    return CompInputs.Inputs(self)

  @property
  def fields(self):
    """
    Description:
    ------------
    Group all the UI components dedicated to produce input items.

    Those components are editable items which need to be updated by the user of the dashboard.
    This category will take into account textarea, input text...
    """
    return CompFields.Fields(self)

  @property
  def timelines(self):
    """
    Description:
    ------------
    """
    return CompFields.Timelines(self)

  @property
  def icons(self):
    """
    Description:
    ------------
    Group all the UI components dedicated to produce icon items.

    This category of component will rely on the font-awesome library for the final display.
    """
    return CompIcons.Icons(self)

  @property
  def menus(self):
    """
    Description:
    ------------
    """
    return CompMenus.Menus(self)

  @property
  def panels(self):
    """
    Description:
    ------------
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
    """
    return CompForms.Forms(self)

  @property
  def modals(self):
    """
    Description:
    ------------
    Group all the UI components dedicated to produce modal components.
    """
    return CompModals.Modals(self)

  @property
  def charts(self):
    """
    Description:
    ------------
    Group all the UI components dedicated to produce charts.

    Different kind of charts framework are available (ChartJs, Plotly, C3, Billboard, NVD3, DC, Vis or even D3).
    """
    return CompCharts.Graphs(self)

  @property
  def tags(self):
    """
    Description:
    ------------
    Group all the other tags available in HTML.

    Those tags can be considered as normal HTML component, which means Js and CSS features are also available
    """
    return CompTags.Tags(self)

  @property
  def calendars(self):
    """
    Description:
    ------------
    Group all the component related to the time and calendar management
    """
    return CompCalendars.Calendar(self)

  @property
  def delimiters(self):
    """
    Description:
    ------------
    Shortcut property to the various delimiters styles

    Related Pages:

      https://codepen.io/ibrahimjabbari/pen/ozinB
    """
    return CompLayouts.Delimiter(self)

  def contents(self, title="Contents", top=10, right=10, left=None, width=(None, "%"), height=(None, "px"), options=None, profile=None):
    """
    Description:
    ------------
    Add a content table to the page

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/contents_table.py
      https://github.com/epykure/epyk-templates/blob/master/locals/components/paragraph.py

    Attributes:
    ----------
    :param title:
    :param top:
    :param right:
    :param left:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options:
    :param profile: Optional. A flag to set the component performance storage
    """
    html_contents = html.HtmlTextComp.ContentsTable(self.rptObj, title, width, height, options, profile)
    html_contents.style.css.top = top
    if left is not None:
      html_contents.style.css.left = left
    else:
      html_contents.style.css.right = right
    # Attach the table content to the main report object
    self.rptObj._content_table = html_contents
    return html_contents

  def bespoke(self, htmlCls, *args, **kwargs):
    """
    Description:
    ------------
    Hook to allow the creation of bespoke component using specific configurations.
    Components can be self contained in a module and rely on external packages

    Tip: Look at the Import.extend function in order to add external Js and CSS modules to your environment

    Attributes:
    ----------
    :param htmlCls: Class. The bespoke HTML component
    :param args: The python attributes used in the HTML component contructor
    :param kwargs: The python attributes used in the HTML component contructor
    """
    return htmlCls(self.rptObj, *args, **kwargs)

  def _tags(self, vals=None, title="", icon="", width=(100, "%"), height=(None, "px"), htmlCode=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param vals: Optional.
    :param title: Optional.
    :param icon: Optional. A string with the value of the icon to display from font-awesome
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return html.HtmlTextEditor.Tags(self.rptObj, vals, title, icon, width, height, htmlCode, profile)

  def loading(self, text="Loading", color=None, options=None):
    """
    Description:
    ------------
    Entry point to the loading component

    This component will create a
      - label component for the text
      - icon component for the loading icon

    Attributes:
    ----------
    :param text:
    :param color:
    :param options:
    """
    html_loading = html.HtmlOthers.Loading(self.rptObj, text, color, options or {})
    return html_loading

  def breadcrumb(self, values, selected=None, width=(100, '%'), height=(30, 'px'), options=None, profile=None):
    """
    Description:
    ------------
    Add Breadcrum information to the page

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
    :param values:
    :param selected:
    :param width:
    :param height:
    :param options:
    :param profile:
    """
    options = options or {}
    options['selected'] = selected
    html_breadcrumb = html.HtmlOthers.Breadcrumb(self.rptObj, values, width, height, options, profile)
    return html_breadcrumb

  def form(self, action=None, method=None, helper=None):
    """
    Description:
    ------------
    Creates an new empty form

    Usage::

      f = rptObj.ui.form()

    Attributes:
    ----------
    :param action:
    :param method:
    :param helper:
    """
    form = html.HtmlContainer.Form(self.rptObj, [], action, method, helper)
    return form

  def json(self, data=None, width=(None, '%'), height=(100, '%'), options=None, profile=None):
    """
    Description:
    ------------
    HTML component to display a Json

    Related Pages:

      https://github.com/mohsen1/json-formatter-js

    Attributes:
    ----------
    :param data: Dictionary. The Json object to be display
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Dictionary with the component properties
    :param profile: Boolean
    """
    data = data or {}
    h_json = html.HtmlOthers.HtmlJson(self.rptObj, data, width, height, options, profile)
    if height[1] != '%':
      h_json.style.css.overflow = 'auto'
    return h_json

  def qrcode(self, data=None, width=(None, '%'), height=(100, '%'), options=None, profile=None):
    """
    Description:
    ------------
    HTML component to display a QR Code from a string

    Related Pages:

      https://davidshimjs.github.io/qrcodejs/

    TODO: Add options

    Attributes:
    ----------
    :param data: String. The value to be converted to QR Code
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Dictionary with the component properties
    :param profile: Boolean
    """
    data = data or {}
    h_qrcode = html.HtmlOthers.HtmlQRCode(self.rptObj, data, width, height, options, profile)
    if height[1] != '%':
      h_qrcode.style.css.overflow = 'auto'
    return h_qrcode

  def postit(self, components=None, anchor=None):
    """
    Description:
    ------------

    Templates:

      https://github.com/epykure/epyk-templates/blob/master/locals/components/postit.py

    Attributes:
    ----------
    :param components: Components. Optional.
    :param anchor: Component. Optional.
    """
    postit = self.rptObj.ui.div()
    if anchor is None:
      anchor = self.rptObj.ui.icon("fas fa-map-marker")
      anchor.style.css.padding = "4px"
      postit += anchor
    postit.anchor = anchor
    popup = self.rptObj.ui.div(components, width=(None, 'px'))
    popup.css({"display": 'none', 'position': 'absolute', 'border': '1px solid black', 'border-radius': '5px',
               'padding': '5px', 'background': self.rptObj.theme.greys[0]})
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
    Add an extension base on it is name

    Attributes:
    ----------
    :param package_name: String. The package name
    :param alias: String. The alias for the link in report.ui
    """
    mod = __import__(package_name)
    __import__("%s.components" % package_name)
    if alias is None:
      alias = getattr(mod.components, 'alias', package_name)
    setattr(self, alias, mod.components.Components(self))
