"""
Main interface for all the difference HTML components in the framework
"""

from epyk.core import html

from epyk.interfaces.components import CompLayouts
from epyk.interfaces.components import CompButtons
from epyk.interfaces.components import CompIcons
from epyk.interfaces.components import CompInputs
from epyk.interfaces.components import CompMedia
from epyk.interfaces.components import CompLists
from epyk.interfaces.tables import CompTables
from epyk.interfaces.graphs import CompCharts
from epyk.interfaces.components import CompTexts
from epyk.interfaces.components import CompRich
from epyk.interfaces.components import CompImages
from epyk.interfaces.components import CompLinks
from epyk.interfaces.components import CompSliders
from epyk.interfaces.components import CompMessaging
from epyk.interfaces.components import CompDrops
from epyk.interfaces.components import CompForms
from epyk.interfaces.components import CompTags
from epyk.interfaces.components import CompFields


class Components(object):
  def __init__(self, rptObj):
    self.rptObj = rptObj

    # Special shortcut for some components
    self.button = self.buttons.button
    self.input = self.inputs.input
    self.div = self.layouts.div
    self.grid = self.layouts.grid
    self.col = self.layouts.col
    self.table = self.tables.tabulator
    self.pivot = self.tables.pivot
    self.text = self.texts.text
    self.title = self.texts.title
    self.icon = self.images.icon
    self.img = self.images.img
    self.list = self.lists.list
    self.link = self.links.link
    self.chart = self.charts.chart
    self.check = self.buttons.check
    self.slider = self.sliders.slider
    self.select = self.lists.select
    self.date = self.fields.cob
    self.tree = self.lists.tree
    self.info = self.rich.info
    self.radio = self.buttons.radio

  def css(self, cssAttrs):
    """
    Change the CSS Style of the main container in the page
    """
    self.rptObj._props.setdefault("css", {})["container"] = cssAttrs

  @property
  def messaging(self):
    """
    Group all the UI Components dedicated to display messaging services.

    This category will group (chat, RSS streams, forum, bot ...).
    Those components are interactive and they would require underlying services and databases in order to fully work
    """
    return CompMessaging.Messaging(self)

  @property
  def sliders(self):
    """
    Group all the UI components dedicated to produce slider items.

    Those components are interactive and can be used to filter the data on other items in the dashboard.
    Those components are mainly relying on Jquery and JqueryUi
    """
    return CompSliders.Sliders(self)

  @property
  def links(self):
    """
    Group all the UI components dedicated to produce links to another page or website.
    """
    return CompLinks.Links(self)

  @property
  def rich(self):
    """
    Group all the UI components dedicated to produce rich HTML Components.

    This category will take into account very specific and bespoke components.
    """
    return CompRich.Rich(self)

  @property
  def texts(self):
    """
    Group all the UI components dedicated to produce text components.

    The items in this category will not be editable and they will only provide nice text structure like paragraph,
    formatted text...
    """
    return CompTexts.Texts(self)

  @property
  def images(self):
    """
    Group all the UI components dedicated to produce image or collection of images.
    """
    return CompImages.Images(self)

  @property
  def lists(self):
    """
    Group all the UI components dedicated to produce list or selection items.

    Simple list, trees or dropdown boxes will be part of this category of items
    """
    return CompLists.Lists(self)

  @property
  def buttons(self):
    """
    Group all the UI components dedicated to produce button or checkbox.
    """
    return CompButtons.Buttons(self)

  @property
  def tables(self):
    """
    Group all the UI components dedicated to produce tables or pivot tables.

    Different kind of tables are available in the framework (Tabulator, Datatable, PivotTable or even a bespoke
    implementation).
    """
    return CompTables.Tables(self)

  @property
  def media(self):
    """
    Group all the UI components dedicated to produce media (video and audio) items.

    Plain Vanilla HTML5 components
    """
    return CompMedia.Media(self)

  @property
  def inputs(self):
    """
    Group all the UI components dedicated to produce input items.

    Those components are editable items which need to be updated by the user of the dashboard.
    This category will take into account textarea, input text...
    """
    return CompInputs.Inputs(self)

  @property
  def fields(self):
    """
    Group all the UI components dedicated to produce input items.

    Those components are editable items which need to be updated by the user of the dashboard.
    This category will take into account textarea, input text...
    """
    return CompFields.Fields(self)

  @property
  def icons(self):
    """
    Group all the UI components dedicated to produce icon items.

    This category of component will rely on the font-awesome library for the final display.
    """
    return CompIcons.Icons(self)

  @property
  def layouts(self):
    """
    Group all the UI components dedicated to produce component containers.

    All the items in this category are dedicated for the structure of the dashboard and they
    are mainly holder of other components.
    This will mainly rely on bootstrap for the display of the different objects in the page.
    """
    return CompLayouts.Layouts(self)

  @property
  def drops(self):
    """
    Group all the UI components dedicated to drop data.
    """
    return CompDrops.DropData(self)

  @property
  def forms(self):
    """
    Group all the Forms components dedicated to drop data.

    Documentation
    https://www.w3schools.com/html/html_forms.asp
    """
    return CompForms.Forms(self)

  @property
  def charts(self):
    """
    Group all the UI components dedicated to produce charts.

    Different kind of charts framework are available (ChartJs, Plotly, C3, Billboard, NVD3, DC, Vis or even D3).
    """
    return CompCharts.Graphs(self)

  @property
  def tags(self):
    """
    Group all the other tags available in HTML.

    Those tags can be considered as normal HTML component, which means Js and CSS features are also available
    """
    return CompTags.Tags(self)

  def register(self, html_comp):
    """
    Internal function to register a HTML component based on its memory id.

    :param html_comp: The html component

    return the html component
    """
    self.rptObj.htmlItems[id(html_comp)] = html_comp
    self.rptObj.content.append(id(html_comp))
    return html_comp

  def contents(self, vals=None, size=(None, "px"), width=(None, "%"), height=(None, "px"), profile=None):
    """
    Add a content table to the page

    :param vals: Optional.
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param profile: Optional. A flag to set the component performance storage
    """
    size = self._size(size)
    html_contents = html.HtmlTextComp.ContentsTable(self.rptObj, vals or [], size, width, height, profile)
    self.register(html_contents)
    return html_contents

  def _tags(self, vals=None, title="", icon="", size=(None, "px"), width=(100, "%"), height=(None, "px"), htmlCode=None, profile=None):
    """

    Example

    Documentation

    :param vals: Optional.
    :param title: Optional.
    :param icon: Optional. A string with the value of the icon to display from font-awesome
    :param size:
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage

    :rtype: html.HtmlTextEditor.Tags
    :return: 
    """
    size = self._size(size)
    return self.register(html.HtmlTextEditor.Tags(self.rptObj, vals, title, icon, size, width, height, htmlCode, profile))

  def context_menu(self, records=None, width=(None, '%'), height=(None, 'px'), visible=False, profile=None):
    """
    Set a bespoke Context Menu on an Item. This will create a popup on the page with action.
    This component is generic is need to be added to a component to work

    Example
    menu = rptObj.ui.context_menu([{"text": 'text', 'event': 'alert("ok")'}])
    rptObj.ui.title("Test").attach_menu(menu)

    Documentation

    :param records: Optional.
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param visible: Optional.
    :param profile: Optional. A flag to set the component performance storage

    :rtype: html.HtmlEvent.ContextMenu
    :return:
    """
    return self.register(html.HtmlEvent.ContextMenu(self.rptObj, records, width, height, visible, profile))

  def options_bar(self, records=None, color=None, border_color=None, size=(None, "px"), width=(None, 'px'),
                  height=(None, 'px'), options=None):
    """
    Add a bespoke options / actions bar with icons

    Example

    Documentation

    :param records:
    :param color:
    :param border_color:
    :param size:
    :param width:
    :param height:
    :param options:
    """
    records = records or []
    options = options or {}
    border_color = border_color or self.rptObj.getColor("colors", 1)
    color = color or self.rptObj.getColor("greys", -1)
    size = self._size(size)
    if width[0] is None:
      width = (len(records) * 35, width[1])
    html_opts = html.HtmlEvent.OptionsBar(self.rptObj, records, width, height, size, color, border_color, options)
    self.register(html_opts)
    return html_opts

  def side_bar(self, links=None, color=None, size=(None, "px"), servers=None, position="right"):
    """
    Add a side Bar to the report.

    Documentation
    https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_sidenav

    :param links:
    :param color:
    :param size:
    :param servers:
    :param position:
    """
    size = self._size(size)
    bar = html.HtmlNavBar.HtmlSideBar(self.rptObj, links or [], color, size, servers)
    self.register(bar)
    return bar

  def loading(self, text="Loading", size=(None, "px"), color=None, options=None):
    """
    Entry point to the loading component

    This component will create a
      - label component for the text
      - icon component for the loading icon

    :param text:
    :param size:
    :param color:
    :param options:
    """
    size = self._size(size)
    html_loading = html.HtmlOthers.Loading(self.rptObj, text, color, size, options or {})
    self.register(html_loading)
    return html_loading

  def workflow(self, records, size=(None, "px"), width=(None, '%'), height=(40, 'px'), color=None, options=None):
    """
    Entry point for the workflow object

    Example
    rptObj.ui.workflow([
      {"value": 'test 1', "status": 'success', 'label': 'test'},
      {"value": 'test 2', "status": 'error'},
      {"value": 'test 3', "status": 'pending'}])

    :param records: A list with the different steps defined in the workflow
    :param size: Optional.
    :param width: Optional.
    :param height: Optional.
    :param color: Optional.
    :param options: Optional.
    """
    size = self._size(size)
    html_wf = html.HtmlOthers.Workflow(self.rptObj, records, width, height, color, size, options or {})
    self.register(html_wf)
    return html_wf

  #--------------------------------------------------------------------------------------------------------------------
  #
  #                                                 COMMON FUNCTIONS
  #

  def _size(self, size):
    """
    Used to get the font-size in the framework.
    In case of None this function will default to the CSS common properties

    Example
    _size((10, "px"))

    :param size: A tuple with the integer size and it is unit.

    :return: A tuple with the size to be applied
    """
    if size[0] is None and size[1] == "px" and hasattr(self.rptObj, "style"):
      size = (self.rptObj.style.defaults.font.size, self.rptObj.style.defaults.font.unit)
    return size
