
from epyk.core.html import Html
from epyk.core.js.packages import packageImport
from epyk.core.js.packages import JsDatatable

from epyk.core.data import DataClass
from epyk.core.data import DataEnum

# The list of CSS classes
from epyk.core.css.styles import GrpClsTable


# External Datatable extensions added on demand to add some extra features
# Details of the different extensions are available on the different websites
# https://datatables.net/extensions/
extensions = {
  'rowsGroup': {'jsImports': ['datatables-rows-group']},
}


class Table(Html.Html):
  name, category, callFnc = 'Table', 'Tables', 'table'
  __reqCss, __reqJs = ['datatables'], ['datatables']

  def __init__(self, report, records, width, height, htmlCode, options, profile):
    data, columns, self.__config = [], [], None
    super(Table, self).__init__(report, [], code=htmlCode, css_attrs={"width": width, "height": height}, profile=profile)
    if records is not None:
      self.config.data = records

  @property
  def style(self):
    if self._styleObj is None:
      self._styleObj = GrpClsTable.Datatable(self)
    return self._styleObj

  @property
  def tableId(self):
    """
    Return the Javascript variable of the chart
    """
    return "%s_obj" % self.htmlId

  @property
  def config(self):
    if self.__config is None:
      self.__config = TableConfig(self._report)
    return self.__config

  def get_column(self, by_title):
    for c in self.config._attrs.get('columns', []):
      if c.title == by_title:
        return c

    return None

  @property
  def js(self):
    """
    Return the Javascript internal object

    :return: A Javascript object

    :rtype: JsDatatable.DatatableAPI
    """
    if self._js is None:
      self._js = JsDatatable.DatatableAPI(self._report, selector=self.tableId, setVar=False, parent=self)
    return self._js

  def build(self, data=None, options=None, profile=False):
    return 'var %s = %s.DataTable(%s)' % (self.tableId, self.dom.jquery.varId, self.config)

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return "<table %s></table>" % (self.get_attrs(pyClassNames=self.style.get_classes()))


class EnumStyleOptions(DataEnum):
  js_conversion = True

  def __wrap(self, name,  header_only=False, body_only=False):
    """

    https://datatables.net/manual/styling/classes
    """
    if header_only:
      return self.set('dt-head-%s' % name)

    if body_only:
      return self.set('dt-body-%s' % name)

    return self.set('dt-%s' % name)

  def left(self, header_only=False, body_only=False):
    """

    https://datatables.net/manual/styling/classes
    """
    return self.__wrap('left', header_only, body_only)

  def right(self, header_only=False, body_only=False):
    """

    https://datatables.net/manual/styling/classes
    """
    return self.__wrap('right', header_only, body_only)

  def center(self, header_only=False, body_only=False):
    """

    https://datatables.net/manual/styling/classes
    """
    return self.__wrap('center', header_only, body_only)

  def justify(self, header_only=False, body_only=False):
    """

    https://datatables.net/manual/styling/classes
    """
    return self.__wrap('justify', header_only, body_only)

  def nowrap(self, header_only=False, body_only=False):
    """

    https://datatables.net/manual/styling/classes
    """
    return self.__wrap('nowrap', header_only, body_only)


class ColumnDef(DataClass):

  @property
  def targets(self):
    """
    Description:
    -----------
    The columnDefs option allows a column definition object to be defined and then assigned to one or more columns in a DataTable, regardless of the order of the column definitions array, or the order of the columns in the table.

    Related Pages:

			https://datatables.net/reference/option/columnDefs.targets
    """
    return self._attrs["targets"]

  @targets.setter
  def targets(self, val):
    self._attrs["targets"] = val

  @property
  def visible(self):
    """
    Description:
    -----------
    Enable or disable the display of this column.

    Related Pages:

			https://datatables.net/reference/option/columns.visible
    """
    return self._attrs["visible"]

  @visible.setter
  def visible(self, val):
    self._attrs["visible"] = val

  @property
  def searchable(self):
    """
    Description:
    -----------
    Enable or disable search on the data in this column.

    Related Pages:

			https://datatables.net/reference/option/columns.searchable
    """
    return self._attrs["searchable"]

  @searchable.setter
  def searchable(self, val):
    self._attrs["searchable"] = val

  @property
  def orderData(self):
    """
    Description:
    -----------
    Define multiple column ordering as the default order for a column.

    Related Pages:

			https://datatables.net/reference/option/columns.orderData
    """
    return self._attrs["orderData"]

  @orderData.setter
  def orderData(self, val):
    self._attrs["orderData"] = val


class Column(DataClass):

  @property
  def cellType(self):
    """
    Description:
    -----------
    Change the cell type created for the column - either TD cells or TH cells.

    Related Pages:

			https://datatables.net/reference/option/columns.cellType
    """
    return self._attrs["cellType"]

  @cellType.setter
  def cellType(self, val):
    self._attrs["cellType"] = val

  @property
  def className(self):
    """
    Description:
    -----------
    Quite simply this option adds a class to each cell in a column, regardless of if the table source is from DOM, Javascript or Ajax. This can be useful for styling columns.

    Related Pages:

			https://datatables.net/reference/option/columns.className
    https://datatables.net/manual/styling/classes

    :rtype: EnumStyleOptions
    """
    return self.has_attribute(EnumStyleOptions)

  @property
  def contentPadding(self):
    """
    Description:
    -----------
    Add padding to the text content used when calculating the optimal width for a table.

    Related Pages:

			https://datatables.net/reference/option/columns.contentPadding
    """
    return self._attrs["contentPadding"]

  @contentPadding.setter
  def contentPadding(self, val):
    self._attrs["contentPadding"] = val

  @property
  def defaultContent(self):
    """
    Description:
    -----------
    Set default, static, content for a column.

    Related Pages:

			https://datatables.net/reference/option/columns.defaultContent
    """
    return self._attrs["defaultContent"]

  @defaultContent.setter
  def defaultContent(self, val):
    self._attrs["defaultContent"] = val

  @property
  def name(self):
    """
    Description:
    -----------
    When working with DataTables' API, it is very common to want to be able to address individual columns so you can work with them (you wish to sum the numeric content of a column for example). DataTables has two basic methods of addressing columns:

    Related Pages:

			https://datatables.net/reference/option/columns.name
    """
    return self._attrs["name"]

  @name.setter
  def name(self, val):
    self._attrs["name"] = val

  @property
  def title(self):
    """
    Description:
    -----------
    Set the column title.

    Related Pages:

			https://datatables.net/reference/option/columns.title
    """
    return self._attrs["title"]

  @title.setter
  def title(self, val):
    self._attrs["title"] = val

  @property
  def style(self):
    return self._attrs["style"]

  @style.setter
  def style(self, val):
    self._attrs["style"] = val

  @property
  def orderable(self):
    """
    Description:
    -----------
    Using this parameter, you can remove the end user's ability to order upon a column.
    This might be useful for generated content columns, for example if you have 'Edit' or 'Delete' buttons in the table.

    Related Pages:

			https://datatables.net/reference/option/columns.orderable
    """
    return self._attrs["orderable"]

  @orderable.setter
  def orderable(self, val):
    self._attrs["orderable"] = val

  @property
  def orderData(self):
    """
    Description:
    -----------
    Define multiple column ordering as the default order for a column.

    Related Pages:

			https://datatables.net/reference/option/columns.orderData
    """
    return self._attrs["orderData"]

  @orderData.setter
  def orderData(self, val):
    self._attrs["orderData"] = val

  @property
  def orderDataType(self):
    """
    Description:
    -----------
    Live DOM sorting type assignment.

    Related Pages:

			https://datatables.net/reference/option/columns.orderDataType
    """
    return self._attrs["orderDataType"]

  @orderDataType.setter
  def orderDataType(self, val):
    self._attrs["orderDataType"] = val

  @property
  def orderSequence(self):
    """
    Description:
    -----------
    You can control the default ordering direction, and even alter the behaviour of the order handler (i.e. only allow ascending sorting etc) using this parameter.

    Related Pages:

			https://datatables.net/reference/option/columns.orderSequence
    """
    return self._attrs["orderSequence"]

  @orderSequence.setter
  def orderSequence(self, val):
    self._attrs["orderSequence"] = val

  @property
  def render(self):
    """
    Description:
    -----------
    This property will modify the data that is used by DataTables for various operations as it is read from the data source. columns.render can be considered to be the the read only companion to columns.data which is read / write (and therefore more complex)

    Related Pages:

			https://datatables.net/reference/option/columns.render
    """
    return self._attrs["render"]

  @render.setter
  def render(self, val):
    self._attrs["render"] = val

  @property
  def data(self):
    return self._attrs["data"]

  @data.setter
  def data(self, val):
    self._attrs["data"] = val

  @property
  def searchable(self):
    """
    Description:
    -----------
    Using this parameter, you can define if DataTables should include this column in the filterable data in the table. You may want to use this option to disable search on generated columns such as 'Edit' and 'Delete' buttons for example.

    Related Pages:

			https://datatables.net/reference/option/columns.searchable
    """
    return self._attrs["searchable"]

  @searchable.setter
  def searchable(self, val):
    self._attrs["searchable"] = val

  @property
  def visible(self):
    """
    Description:
    -----------
    Enable or disable the display of this column.

    Related Pages:

			https://datatables.net/reference/option/columns.visible
    """
    return self._attrs["visible"]

  @visible.setter
  def visible(self, val):
    self._attrs["visible"] = val

  @property
  def width(self):
    """
    Description:
    -----------
    Column width assignment.

    Related Pages:

			https://datatables.net/reference/option/columns.width
    """
    return self._attrs["width"]

  @width.setter
  def width(self, val):
    self._attrs["width"] = val


class AOColumns(DataClass):

  def null(self):
    pass

  def add_order_sequence(self):
    pass


class Ajax(DataClass):

  @property
  def url(self):
    """
    https://datatables.net/manual/server-side

    :return:
    """
    return self._attrs["url"]

  @url.setter
  def url(self, val):
    self._attrs["url"] = val

  @property
  def type(self):
    """
    https://datatables.net/manual/server-side

    :return:
    """
    return self._attrs["type"]

  @type.setter
  def type(self, val):
    self._attrs["type"] = val


class Language(DataClass):

  @property
  def decimal(self):
    """
    Description:
    -----------
    Decimal place character.

    Related Pages:

			https://datatables.net/reference/option/language.decimal
    """
    return self._attrs["decimal"]

  @decimal.setter
  def decimal(self, val):
    self._attrs["decimal"] = val

  @property
  def url(self):
    """
    https://datatables.net/manual/i18n

    :return:
    """
    return self._attrs["url"]

  @url.setter
  def url(self, val):
    self._attrs["url"] = val

  @property
  def thousands(self):
    return self._attrs["thousands"]

  @thousands.setter
  def thousands(self, val):
    self._attrs["thousands"] = val


class Search(DataClass):

  @property
  def caseInsensitive(self):
    """
    Description:
    -----------
    Flag to indicate if the filtering should be case insensitive or not.

    Related Pages:

			https://datatables.net/reference/option/search.caseInsensitive
    """
    return self._attrs["caseInsensitive"]

  @caseInsensitive.setter
  def caseInsensitive(self, val):
    self._attrs["caseInsensitive"] = val

  @property
  def search(self):
    """
    Description:
    -----------
    The search option allows the way DataTables performs filtering to be set during the initialisation, and to set an initial global filter.

    Related Pages:

			https://datatables.net/reference/option/search
    """
    return self._attrs["search"]

  @search.setter
  def search(self, val):
    self._attrs["search"] = val

  @property
  def regex(self):
    """
    Description:
    -----------
    Regular expressions can be used to build fantastically complex filtering terms, but also it is perfectly valid for users to enter characters such as * into the filter, so a decision needs to be made if you wish to escape regular expression special characters or not.
    This option controls that ability in DataTables.

    Related Pages:

			https://datatables.net/reference/option/search.regex
    """
    return self._attrs["regex"]

  @regex.setter
  def regex(self, val):
    self._attrs["regex"] = val

  @property
  def smart(self):
    """
    Description:
    -----------
    DataTables' built-in filtering is "smart" in that it breaks the user's input into individual words and then matches those words in any position and in any order in the table (rather than simple doing a simple string compare).

    Related Pages:

			https://datatables.net/reference/option/search.smart
    """
    return self._attrs["smart"]

  @smart.setter
  def smart(self, val):
    self._attrs["smart"] = val


class TableConfig(DataClass):

  @property
  @packageImport('datatables-autoFill', 'datatables-autoFill')
  def autoFill(self):
    from epyk.core.html.tables.exts import DtAutoFill

    return self.sub_data("autoFill", DtAutoFill.AutoFill)

  @property
  def autoWidth(self):
    """
    Description:
    -----------
    Enable or disable automatic column width calculation.
    This can be disabled as an optimisation (it takes a finite amount of time to calculate the widths) if the tables widths are passed in using

    Related Pages:

			https://datatables.net/reference/option/autoWidth
    """
    return self._attrs["autoWidth"]

  @autoWidth.setter
  def autoWidth(self, val):
    self._attrs["autoWidth"] = val

  @property
  @packageImport('datatables-buttons', 'datatables-buttons')
  def buttons(self):
    """
    Description:
    -----------
    A common UI paradigm to use with interactive tables is to present buttons that will trigger some action - that may be to alter the table's state, modify the data in the table, gather the data from the table or even to activate some external process.
    Showing such buttons is an interface that end users are comfortable with, making them feel at home with the table.

    Related Pages:

			https://datatables.net/extensions/buttons/
    """
    from epyk.core.html.tables.exts import DtButtons
    self._attrs['dom'] = 'B<"clear">lfrtip'
    return self.sub_data("buttons", DtButtons.Buttons)

  @property
  @packageImport('datatables-buttons', 'datatables-buttons')
  def colReorder(self):
    """

    :return:
    """
    from epyk.core.html.tables.exts import DtColReorder
    return self.sub_data("colReorder", DtColReorder.ColReorder)

  @property
  def deferRender(self):
    """
    Description:
    -----------
    By default, when DataTables loads data from an Ajax or Javascript data source (ajax and data respectively)

    Related Pages:

			https://datatables.net/reference/option/deferRender

    """
    return self._attrs["deferRender"]

  @deferRender.setter
  def deferRender(self, val):
    self._attrs["deferRender"] = val


  @property
  @packageImport('datatables-fixed-header', 'datatables-fixed-header')
  def fixedHeader(self):
    """
    Description:
    -----------
    When displaying tables with a particularly large amount of data shown on each page, it can be useful to have the table's header and / or footer fixed to the top or bottom of the scrolling window.
    This lets your users quickly determine what each column refers to rather than needing to scroll back to the top of the table.

    Related Pages:

			https://datatables.net/extensions/fixedheader/
    """
    from epyk.core.html.tables.exts import DtFixedHeader
    return self.sub_data("fixedHeader", DtFixedHeader.FixedHeater)

  @property
  @packageImport('datatables-fixed-columns','datatables-fixed-columns')
  def fixedColumns(self):
    """

    :return:
    """
    from epyk.core.html.tables.exts import DtFixedColumns
    return self.sub_data("fixedColumns", DtFixedColumns.FixedColumns)

  @property
  @packageImport('datatables-keytable', 'datatables-keytable')
  def keys(self):
    """

    :rtype: DtFixedColumns.FixedColumns
    """
    from epyk.core.html.tables.exts import DtKeyTable
    return self.sub_data("keys", DtKeyTable.KeyTable)

  @property
  def lengthChange(self):
    """
    Description:
    -----------
    When pagination is enabled, this option will control the display of an option for the end user to change the number of records to be shown per page.
    The options shown in the list are controlled by the lengthMenu configuration option.

    Related Pages:

			https://datatables.net/reference/option/lengthChange
    """
    return self._attrs["lengthChange"]

  @lengthChange.setter
  def lengthChange(self, val):
    self._attrs["lengthChange"] = val

  @property
  def columnDefs(self):
    """
    Description:
    -----------
    Very similar to columns, this parameter allows you to assign specific options to columns in the table, although in this case the column options defined can be applied to one or more columns. Additionally, not every column need be specified, unlike columns.

    Related Pages:

			https://datatables.net/reference/option/columnDefs
    """
    return self.sub_data_enum("columnDefs", ColumnDef)

  @property
  def columns(self):
    """
    Description:
    -----------
    The columns option in the initialisation parameter allows you to define details about the way individual columns behave. For a full list of column options that can be set, please see the related parameters below.

    Related Pages:

			https://datatables.net/reference/option/columns
    """
    return self.sub_data_enum("columns", Column)

  @property
  def language(self):
    """
    Description:
    -----------
    Language configuration options for DataTables

    Related Pages:

			https://datatables.net/reference/option/
    """
    return self.sub_data("language", Language)

  @property
  def ajax(self):
    """
    Description:
    -----------
    DataTables can obtain the data that it is to display in the table body from a number of sources, including from an Ajax data source, using this initialisation parameter.
    As with other dynamic data sources, arrays or objects can be used for the data source for each row, with columns.data employed to read from specific object properties.

    Related Pages:

			https://datatables.net/reference/option/ajax
    """
    return self._attrs["ajax"]

  @ajax.setter
  def ajax(self, val):
    self._attrs["ajax"] = val

  @property
  def processing(self):
    """
    Description:
    -----------
    Enable or disable the display of a 'processing' indicator when the table is being processed (e.g. a sort).
    This is particularly useful for tables with large amounts of data where it can take a noticeable amount of time to sort the entries.

    Related Pages:

			https://datatables.net/reference/option/processing
    """
    return self._attrs["processing"]

  @processing.setter
  def processing(self, val):
    self._attrs["processing"] = val

  @property
  def search(self):
    """
    Description:
    -----------
    The search option allows the way DataTables performs filtering to be set during the initialisation, and to set an initial global filter.

    Related Pages:

			https://datatables.net/reference/option/search
    """
    return self.sub_data_enum("search", Search)

  @property
  def serverSide(self):
    """
    Description:
    -----------
    By default DataTables operates in client-side processing mode, but can be switched to server-side processing mode using this option.
    Server-side processing is useful when working with large data sets (typically >50'000 records) as it means a database engine can be used to perform the sorting etc calculations - operations that modern database engines are highly optimised for, allowing use of DataTables with massive data sets (millions of rows).

    Related Pages:

			https://datatables.net/reference/option/serverSide
    """
    return self._attrs["serverSide"]

  @serverSide.setter
  def serverSide(self, val):
    self._attrs["serverSide"] = val

  @property
  def deferLoading(self):
    """
    Description:
    -----------
    When using server-side processing, the default mode of operation for DataTables is to simply throw away any data that currently exists in the table and make a request to the server to get the first page of data to display.
    This is fine for an empty table, but if you already have the first page of data displayed in the plain HTML, it is a waste of resources.
    As such, this option exists to allow you to instruct DataTables to not make that initial request, rather it will use the data already on the page (no sorting etc will be applied to it).

    Related Pages:

			https://datatables.net/reference/option/deferLoading
    """
    return self._attrs["deferLoading"]

  @deferLoading.setter
  def deferLoading(self, val):
    self._attrs["deferLoading"] = val

  @property
  def destroy(self):
    """
    Description:
    -----------
    Initialise a new DataTable as usual, but if there is an existing DataTable which matches the selector, it will be destroyed and replaced with the new table.
    This can be useful if you want to change a property of the table which cannot be altered through the API.

    Related Pages:

			https://datatables.net/reference/option/destroy
    """
    return self._attrs["destroy"]

  @destroy.setter
  def destroy(self, val):
    self._attrs["destroy"] = val

  @property
  def displayStart(self):
    """
    Description:
    -----------
    Define the starting point for data display when using DataTables with pagination

    Related Pages:

			https://datatables.net/reference/option/displayStart
    """
    return self._attrs["displayStart"]

  @displayStart.setter
  def displayStart(self, val):
    self._attrs["displayStart"] = val

  @property
  def dom(self):
    """
    Description:
    -----------
    DataTables will add a number of elements around the table to both control the table and show additional information about it.
    The position of these elements on screen are controlled by a combination of their order in the document (DOM) and the CSS applied to the elements.
    This parameter is used to control their ordering and additional mark-up surrounding them in the DOM.

    Related Pages:

			https://datatables.net/reference/option/dom
    """
    return self._attrs["dom"]

  @dom.setter
  def dom(self, val):
    self._attrs["dom"] = val

  @property
  def data(self):
    """
    Description:
    -----------
    DataTables can obtain the data it is to display in the table's body from a number of sources, including being passed in as an array of row data using this initialisation parameter.
    As with other dynamic data sources, arrays or objects can be used for the data source for each row, with columns.data employed to read from specific object properties.

    Related Pages:

			https://datatables.net/reference/option/data
    """
    return self._attrs["data"]

  @data.setter
  def data(self, val):
    self._attrs["data"] = val

  @property
  def paging(self):
    """
    Description:
    -----------
    DataTables can split the rows in tables into individual pages, which is an efficient method of showing a large number of records in a small space.
    The end user is provided with controls to request the display of different data as the navigate through the data.
    This feature is enabled by default, but if you wish to disable it, you may do so with this parameter.

    Related Pages:

			https://datatables.net/reference/option/paging
    """
    return self._attrs["paging"]

  @paging.setter
  def paging(self, val):
    self._attrs["paging"] = val

  @property
  def info(self):
    """
    Description:
    -----------
    When this option is enabled, Datatables will show information about the table including information about filtered data if that action is being performed.
    This option allows that feature to be enabled or disabled.

    Related Pages:

			https://datatables.net/reference/option/info
    """
    return self._attrs["info"]

  @info.setter
  def info(self, val):
    self._attrs["info"] = val

  @property
  def orderCellsTop(self):
    """
    Description:
    -----------
    Allows control over whether DataTables should use the top (true) unique cell that is found for a single column, or the bottom (false - default) to attach the default order listener.
    This is useful when using complex headers.

    Related Pages:

			https://datatables.net/reference/option/orderCellsTop
    """
    return self._attrs["orderCellsTop"]

  @orderCellsTop.setter
  def orderCellsTop(self, val):
    self._attrs["orderCellsTop"] = val

  @property
  def orderClasses(self):
    """
    Description:
    -----------
    DataTables highlight the columns which are used to order the content in the table's body by adding a class to the cells in that column, which in turn has CSS applied to those classes to highlight those cells.

    Related Pages:

			https://datatables.net/reference/option/orderClasses
    """
    return self._attrs["orderClasses"]

  @orderClasses.setter
  def orderClasses(self, val):
    self._attrs["orderClasses"] = val

  @property
  def orderFixed(self):
    """
    Description:
    -----------
    The option works in tandem with the order option which provides an initial ordering state for the table which can then be modified by the user clicking on column headings, while the ordering specified by this option will always be applied to the table, regardless of user interaction.

    Related Pages:

			https://datatables.net/reference/option/orderFixed
    """
    return self._attrs["orderFixed"]

  @orderFixed.setter
  def orderFixed(self, val):
    self._attrs["orderFixed"] = val

  @property
  def orderMulti(self):
    """
    Description:
    -----------
    When ordering is enabled (ordering), by default DataTables allows users to sort multiple columns by shift clicking upon the header cell for each column.
    Although this can be quite useful for users, it can also increase the complexity of the order, potentiality increasing the processing time of ordering the data.
    Therefore, this option is provided to allow this shift-click multiple column ability.

    Related Pages:

			https://datatables.net/reference/option/orderMulti
    """
    return self._attrs["orderMulti"]

  @orderMulti.setter
  def orderMulti(self, val):
    self._attrs["orderMulti"] = val

  @property
  def ordering(self):
    """
    Description:
    -----------
    Enable or disable ordering of columns - it is as simple as that! DataTables, by default, allows end users to click on the header cell for each column, ordering the table by the data in that column.
    The ability to order data can be disabled using this option.

    Related Pages:

			https://datatables.net/reference/option/ordering
    """
    return self._attrs["ordering"]

  @ordering.setter
  def ordering(self, val):
    self._attrs["ordering"] = val

  def order(self, column, direction):
    """
    Description:
    -----------
    If ordering is enabled (ordering), then DataTables will perform a first pass order during initialisation.
    Using this parameter you can define which column(s) the order is performed upon, and the ordering direction.
    The order must be an array of arrays, each inner array comprised of two elements:

    Related Pages:

			https://datatables.net/reference/option/order

    Attributes:
    ----------
    :param column: String. The column name
    :param direction: String the direction (asc, desc)
    """
    if not 'order' in self._attrs:
      self._attrs["order"] = []
    self._attrs["order"].append([column, direction])
    return self

  @property
  def aoColumns(self):
    return self.sub_data_enum("aoColumns", AOColumns)

  @property
  @packageImport('datatables-responsive', 'datatables-responsive')
  def responsive(self):
    """
    Description:
    -----------
    In the modern world of responsive web design tables can often cause a particular problem for designers due to their row based layout.
    Responsive is an extension for DataTables that resolves that problem by optimising the table's layout for different screen sizes through the dynamic insertion and removal of columns from the table.

    Related Pages:

			https://datatables.net/extensions/responsive/

    :rtype: DtResponsive.Responsive
    """
    from epyk.core.html.tables.exts import DtResponsive
    return self.sub_data("responsive", DtResponsive.Responsive)

  @property
  def stateSave(self):
    """
    Description:
    -----------
    Enable or disable state saving.
    When enabled aDataTables will store state information such as pagination position, display length, filtering and sorting.
    When the end user reloads the page the table's state will be altered to match what they had previously set up.

    Related Pages:

			https://datatables.net/reference/option/stateSave
    """
    return self._attrs["stateSave"]

  @stateSave.setter
  def stateSave(self, val):
    self._attrs["stateSave"] = val

  @property
  def pagingType(self):
    return self._attrs["pagingType"]

  @pagingType.setter
  def pagingType(self, val):
    self._attrs["pagingType"] = val

  @property
  def scrollY(self):
    """
    Description:
    -----------
    Enable vertical scrolling.
    Vertical scrolling will constrain the DataTable to the given height, and enable scrolling for any data which overflows the current viewport. This can be used as an alternative to paging to display a lot of data in a small area (although paging and scrolling can both be enabled at the same time if desired).

    Related Pages:

			https://datatables.net/reference/option/scrollY
    """
    return self._attrs["scrollY"]

  @scrollY.setter
  def scrollY(self, val):
    self._attrs["scrollY"] = val

  @property
  def scrollX(self):
    """
    Description:
    -----------
    Enable horizontal scrolling.
    When a table is too wide to fit into a certain layout, or you have a large number of columns in the table, you can enable horizontal (x) scrolling to show the table in a viewport, which can be scrolled.

    Related Pages:

			https://datatables.net/reference/option/scrollX
    """
    return self._attrs["scrollX"]

  @scrollX.setter
  def scrollX(self, val):
    self._attrs["scrollX"] = val

  @property
  def scrollCollapse(self):
    """
    Description:
    -----------
    When vertical (y) scrolling is enabled through the use of the scrollY option, DataTables will force the height of the table's viewport to the given height at all times (useful for layout).
    However, this can look odd when filtering data down to a small data set, and the footer is left "floating" further down.

    Related Pages:

			https://datatables.net/reference/option/scrollCollapse
    """
    return self._attrs["scrollCollapse"]

  @scrollCollapse.setter
  def scrollCollapse(self, val):
    self._attrs["scrollCollapse"] = val

  @property
  def displayLength(self):
    return self._attrs["displayLength"]

  @displayLength.setter
  def displayLength(self, val):
    self._attrs["displayLength"] = val

  @property
  def scrollCollapse(self):
    return self._attrs["scrollCollapse"]

  @scrollCollapse.setter
  def scrollCollapse(self, val):
    self._attrs["scrollCollapse"] = val

  @property
  def lengthMenu(self):
    """
    Description:
    -----------
    This parameter allows you to readily specify the entries in the length drop down select list that DataTables shows when pagination is enabled. It can be either:

    Related Pages:

			https://datatables.net/reference/option/lengthMenu
    """
    return self._attrs["lengthMenu"]

  @lengthMenu.setter
  def lengthMenu(self, val):
    self._attrs["lengthMenu"] = val

  @property
  def select(self):
    """
    https://datatables.net/manual/options

    :return:
    """
    return self._attrs["scrollCollapse"]

  @select.setter
  def select(self, val):
    self._attrs["select"] = val

  @property
  def pageLength(self):
    """
    Description:
    -----------
    Number of rows to display on a single page when using pagination.

    Related Pages:

			https://datatables.net/reference/option/pageLength
    """
    return self._attrs["pageLength"]

  @pageLength.setter
  def pageLength(self, val):
    self._attrs["pageLength"] = val

  @property
  def pagingType(self):
    """
    Description:
    -----------
    The pagination option of DataTables will display a pagination control below the table (by default, its position can be changed using dom and CSS) with buttons that the end user can use to navigate the pages of the table.
    Which buttons are shown in the pagination control are defined by the option given here.

    Related Pages:

			https://datatables.net/reference/option/pagingType
    """
    return self._attrs["pagingType"]

  @pagingType.setter
  def pagingType(self, val):
    self._attrs["pagingType"] = val

  @property
  def renderer(self):
    """
    Description:
    -----------
    DataTables adds complex components to your HTML page, such as the pagination control.
    The business logic used to calculate what information should be displayed (what buttons in the case of the pagination buttons) is core to DataTables and generally doesn't vary how the buttons are actually displayed based on the styling requirements of the page.

    Related Pages:

			https://datatables.net/reference/option/renderer
    """
    return self._attrs["renderer"]

  @renderer.setter
  def renderer(self, val):
    self._attrs["renderer"] = val

  @property
  def retrieve(self):
    """
    Description:
    -----------
    Retrieve the DataTables object for the given selector.
    Note that if the table has already been initialised, this parameter will cause DataTables to simply return the object that has already been set up - it will not take account of any changes you might have made to the initialisation object passed to DataTables

    Related Pages:

			https://datatables.net/reference/option/retrieve
    """
    return self._attrs["retrieve"]

  @retrieve.setter
  def retrieve(self, val):
    self._attrs["retrieve"] = val

  @property
  def rowId(self):
    """
    Description:
    -----------
    It can often be useful to have a id attribute on each tr element in a DataTable for row selection and data source identification, particularly when using events.

    Related Pages:

			https://datatables.net/reference/option/rowId
    """
    return self._attrs["rowId"]

  @rowId.setter
  def rowId(self, val):
    self._attrs["rowId"] = val

  @property
  @packageImport('datatables-row-group', 'datatables-row-group')
  def rowGroup(self):
    """

    :return:
    """
    from epyk.core.html.tables.exts import DtFixedColumns
    return self.sub_data("rowGroup", DtFixedColumns.FixedColumns)

  @property
  def rowsGroup(self):
    """
    The Datatables feature plugin that groups rows (merge cells vertically) in according to specified columns.
    It's inspired by [fnFakeRowspan] (https://datatables.net/plug-ins/api/fnFakeRowspan) DataTables plugin.

    https://github.com/ashl1/datatables-rowsgroup
    """
    return self._attrs["rowsGroup"]

  @rowsGroup.setter
  def rowsGroup(self, val):
    """

    :param val:
    """
    self._report.jsImports.add('datatables-rows-group')
    self._attrs["rowsGroup"] = val

  @property
  @packageImport('datatables-select', 'datatables-select')
  def select(self):
    """
    Description:
    -----------
    Select adds item selection capabilities to a DataTable. Items can be rows, columns or cells, which can be selected independently, or together. Item selection can be particularly useful in interactive tables where users can perform some action on the table, such as editing rows or marking items to perform an action on.

    Related Pages:

			https://datatables.net/reference/option/select
    """
    from epyk.core.html.tables.exts import DtSelect
    return self.sub_data("select", DtSelect.Select)

  @property
  @packageImport('datatables-scroller', 'datatables-scroller')
  def scroller(self):
    """
    Description:
    -----------
    Scroller is a virtual rendering plug-in for DataTables which allows large datasets to be drawn on screen very quickly.
    What the virtual rendering means is that only the visible portion of the table (and a bit to either side to make the scrolling smooth) is drawn, while the scrolling container gives the visual impression that the whole table is visible.

    Related Pages:

			https://datatables.net/extensions/scroller/
    """
    from epyk.core.html.tables.exts import DtScroller
    return self.sub_data("scroller", DtScroller.Scroller)

  @property
  @packageImport('datatables-searchPanes', 'datatables-searchPanes')
  def searchPanes(self):
    """
    Description:
    -----------
    SearchPanes adds panes to the DataTable with the capability to search the DataTable by selecting rows in the panes.
    This is very useful when it comes to adding a more accessible searching feature and custom search capabilities.
    SearchPanes can search DataTables for multiple values that have been selected across multiple panes.
    They also provide the ability to define custom search functions which cannot be achieved through a simple searchBox.


    Related Pages:

			https://datatables.net/extensions/searchpanes
    """
    from epyk.core.html.tables.exts import DtSearchPanes
    self._attrs['dom'] = 'Prftip'
    return self.sub_data('searchPanes', DtSearchPanes.SearchPanes)

  @property
  def searchCols(self):
    """
    Description:
    -----------
    Basically the same as the search option, but in this case for individual columns, rather than the global filter, this option defined the filtering to apply to the table during initialisation.

    Related Pages:

			https://datatables.net/reference/option/searchCols
    """
    return self._attrs["searchCols"]

  @searchCols.setter
  def searchCols(self, val):
    self._attrs["searchCols"] = val

  @property
  def searchDelay(self):
    """
    Description:
    -----------
    The built-in DataTables global search (by default at the top right of every DataTable) will instantly search the table on every keypress when in client-side processing mode and reduce the search call frequency automatically to 400mS when in server-side processing mode.

    Related Pages:

			https://datatables.net/reference/option/searchDelay
    """
    return self._attrs["searchDelay"]

  @searchDelay.setter
  def searchDelay(self, val):
    self._attrs["searchDelay"] = val

  @property
  def stateDuration(self):
    """
    Description:
    -----------
    Duration for which the saved state information is considered valid. After this period has elapsed the state will be returned to the default.

    Related Pages:

			https://datatables.net/reference/option/stateDuration
    """
    return self._attrs["stateDuration"]

  @stateDuration.setter
  def stateDuration(self, val):
    self._attrs["stateDuration"] = val

  @property
  def stripeClasses(self):
    """
    Description:
    -----------
    An array of CSS classes that should be applied to displayed rows, in sequence. This array may be of any length, and DataTables will apply each class sequentially, looping when required.

    Related Pages:

			https://datatables.net/reference/option/stripeClasses
    """
    return self._attrs["stripeClasses"]

  @stripeClasses.setter
  def stripeClasses(self, val):
    self._attrs["stripeClasses"] = val

  @property
  def tabIndex(self):
    """
    Description:
    -----------
    By default DataTables allows keyboard navigation of the table (sorting, paging, and filtering) by adding a tabindex attribute to the required elements.

    Related Pages:

			https://datatables.net/reference/option/tabIndex
    """
    return self._attrs["tabIndex"]

  @tabIndex.setter
  def tabIndex(self, val):
    self._attrs["tabIndex"] = val
