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
from epyk.interfaces.components import CompDates
from epyk.interfaces.components import CompDrops


class Components(object):
  def __init__(self, rptObj):
    self.rptObj = rptObj

    self._tags = None
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
    self.date = self.dates.cob
    self.tree = self.lists.tree

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
  def dates(self):
    """
    Group all the UI components dedicated to produce dates components.

    Those components are mainly relying on Jquery and JqueryUi
    """
    return CompDates.Dates(self)

  @property
  def rich(self):
    """
    Group all the UI components dedicated to produce rich HTML Components.

    This category will take into account very specific and bespoke components.
    """
    return CompRich.Rich(self)

  @property
  def tags(self):
    """
    Shortcut to the HTML tags

    Those can be added in string in order to improve the render of a text.
    """
    if self._tags is None:
      self._tags = html.Tags.Tags()
    return self._tags

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
  def charts(self):
    """
    Group all the UI components dedicated to produce charts.

    Different kind of charts framework are available (ChartJs, Plotly, C3, Billboard, NVD3, DC, Vis or even D3).
    """
    return CompCharts.Graphs(self)

  def register(self, html_comp):
    """
    Internal function to register a HTML component based on its memory id.

    :param html_comp: The html component

    return the html component
    """
    self.rptObj.htmlItems[id(html_comp)] = html_comp
    self.rptObj.content.append(id(html_comp))
    return html_comp

  def contents(self, vals=None, width=(None, "%"), height=(None, "px"), profile=None):
    """
    Add a content table to the page

    :param vals: Optional.
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param profile: Optional. A flag to set the component performance storage

    :rtype: html.HtmlTextComp.ContentsTable

    :return: The python HTML component
    """
    return self.register(html.HtmlTextComp.ContentsTable(self.rptObj, vals, width, height, profile))

  def tags_test(self, vals=None, title="", icon="", width=(100, "%"), height=(None, "px"), htmlCode=None, profile=None):
    """
    
    :param vals: Optional.
    :param title: Optional.
    :param icon: Optional. A string with the value of the icon to display from font-awesome
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    :return: 
    """
    return self.register(html.HtmlTextEditor.Tags(self.rptObj, vals, title, icon, width, height, htmlCode, profile))

  def context_menu(self, recordSet=None, width=(None, '%'), height=(None, 'px'), visible=False, profile=None):
    """
    Set a bespoke Context Menu on an Item. This will create a popup on the page with action.
    This component is generic is need to be added to a component to work

    Example
    menu = rptObj.ui.context_menu([{"text": 'text', 'event': 'alert("ok")'}])
    rptObj.ui.title("Test").attach_menu(menu)

    :param recordSet: Optional.
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param visible: Optional.
    :param profile: Optional. A flag to set the component performance storage

    :rtype: html.HtmlEvent.ContextMenu

    :return:
    """
    return self.register(html.HtmlEvent.ContextMenu(self.rptObj, recordSet, width, height, visible, profile))


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
