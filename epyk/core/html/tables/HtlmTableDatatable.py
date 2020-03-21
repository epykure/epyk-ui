
from epyk.core.html import Html
from epyk.core.js.packages import JsDatatable

from epyk.core.data import DataClass

# The list of CSS classes
from epyk.core.css.styles import GrpClsTable


# External Datatable extensions added on demand to add some extra features
# Details of the different extensions are available on the different websites
# https://datatables.net/extensions/
extensions = {
  'rowsGroup': {'jsImports': ['datatables-rows-group']},
  'rowGroup': {'jsImports': ['datatables-row-group'], 'cssImport': ['datatables-row-group']},
  'fixedHeader': {'jsImports': ['datatables-fixed-header'], 'cssImport': ['datatables-fixed-header']},
  'colReorder': {'jsImports': ['datatables-col-order'], 'cssImport': ['datatables-col-order'] },
  'colResize': {'jsImports': ['datatables-col-resizable'], 'cssImport': ['datatables-col-resizable']},
  'fixedColumns': {'jsImports': ['datatables-fixed-columns'], 'cssImport': ['datatables-fixed-columns']}
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


class ColumnDef(DataClass):

  @property
  def targets(self):
    return self._attrs["targets"]

  @targets.setter
  def targets(self, val):
    self._attrs["targets"] = val

  @property
  def visible(self):
    return self._attrs["visible"]

  @visible.setter
  def visible(self, val):
    self._attrs["visible"] = val

  @property
  def searchable(self):
    return self._attrs["searchable"]

  @searchable.setter
  def searchable(self, val):
    self._attrs["searchable"] = val

  @property
  def orderData(self):
    """

    https://datatables.net/examples/basic_init/multi_col_sort.html

    :return:
    """
    return self._attrs["orderData"]

  @orderData.setter
  def orderData(self, val):
    self._attrs["orderData"] = val


class Column(DataClass):

  @property
  def title(self):
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
    return self._attrs["orderable"]

  @orderable.setter
  def orderable(self, val):
    self._attrs["orderable"] = val

  @property
  def data(self):
    return self._attrs["data"]

  @data.setter
  def data(self, val):
    self._attrs["data"] = val

  @property
  def defaultContent(self):
    return self._attrs["defaultContent"]

  @defaultContent.setter
  def defaultContent(self, val):
    self._attrs["defaultContent"] = val


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


class TableConfig(DataClass):

  @property
  def autoWidth(self):
    """
    Description:
    -----------
    Enable or disable automatic column width calculation.
    This can be disabled as an optimisation (it takes a finite amount of time to calculate the widths) if the tables widths are passed in using

    Related Pages:
    --------------
    https://datatables.net/reference/option/autoWidth
    """
    return self._attrs["autoWidth"]

  @autoWidth.setter
  def autoWidth(self, val):
    self._attrs["autoWidth"] = val

  @property
  def deferRender(self):
    """
    Description:
    -----------
    By default, when DataTables loads data from an Ajax or Javascript data source (ajax and data respectively)

    Related Pages:
    --------------
    https://datatables.net/reference/option/deferRender

    """
    return self._attrs["deferRender"]

  @deferRender.setter
  def deferRender(self, val):
    self._attrs["deferRender"] = val

  @property
  def lengthChange(self):
    """
    Description:
    -----------
    When pagination is enabled, this option will control the display of an option for the end user to change the number of records to be shown per page.
    The options shown in the list are controlled by the lengthMenu configuration option.

    Related Pages:
    --------------
    https://datatables.net/reference/option/lengthChange
    """
    return self._attrs["lengthChange"]

  @lengthChange.setter
  def lengthChange(self, val):
    self._attrs["lengthChange"] = val

  @property
  def columnDefs(self):
    return self.sub_data_enum("columnDefs", ColumnDef)

  @property
  def columns(self):
    return self.sub_data_enum("columns", Column)

  @property
  def language(self):
    return self.sub_data("language", Language)

  @property
  def ajax(self):
    """
    Description:
    -----------
    DataTables can obtain the data that it is to display in the table body from a number of sources, including from an Ajax data source, using this initialisation parameter.
    As with other dynamic data sources, arrays or objects can be used for the data source for each row, with columns.data employed to read from specific object properties.

    Related Pages:
    --------------
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
    --------------
    https://datatables.net/reference/option/processing
    """
    return self._attrs["processing"]

  @processing.setter
  def processing(self, val):
    self._attrs["processing"] = val

  @property
  def serverSide(self):
    """
    Description:
    -----------
    By default DataTables operates in client-side processing mode, but can be switched to server-side processing mode using this option.
    Server-side processing is useful when working with large data sets (typically >50'000 records) as it means a database engine can be used to perform the sorting etc calculations - operations that modern database engines are highly optimised for, allowing use of DataTables with massive data sets (millions of rows).

    Related Pages:
    --------------
    https://datatables.net/reference/option/serverSide
    """
    return self._attrs["serverSide"]

  @serverSide.setter
  def serverSide(self, val):
    self._attrs["serverSide"] = val

  @property
  def deferLoading(self):
    """
    Related Pages:
    --------------
    https://datatables.net/examples/server_side/defer_loading.html
    """
    return self._attrs["deferLoading"]

  @deferLoading.setter
  def deferLoading(self, val):
    self._attrs["deferLoading"] = val

  @property
  def data(self):
    """
    Description:
    -----------
    DataTables can obtain the data it is to display in the table's body from a number of sources, including being passed in as an array of row data using this initialisation parameter.
    As with other dynamic data sources, arrays or objects can be used for the data source for each row, with columns.data employed to read from specific object properties.

    Related Pages:
    --------------
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
    --------------
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
    --------------
    https://datatables.net/reference/option/info
    """
    return self._attrs["info"]

  @info.setter
  def info(self, val):
    self._attrs["info"] = val

  @property
  def ordering(self):
    """
    Description:
    -----------
    Enable or disable ordering of columns - it is as simple as that! DataTables, by default, allows end users to click on the header cell for each column, ordering the table by the data in that column.
    The ability to order data can be disabled using this option.

    Related Pages:
    --------------
    https://datatables.net/reference/option/ordering
    """
    return self._attrs["ordering"]

  @ordering.setter
  def ordering(self, val):
    self._attrs["ordering"] = val

  def order(self, column, direction):
    if not 'order' in self._attrs:
      self._attrs["order"] = []
    self._attrs["order"].append([column, direction])
    return self

  @property
  def aoColumns(self):
    return self.sub_data_enum("aoColumns", AOColumns)

  @property
  def stateSave(self):
    """
    Description:
    -----------
    Enable or disable state saving.
    When enabled aDataTables will store state information such as pagination position, display length, filtering and sorting.
    When the end user reloads the page the table's state will be altered to match what they had previously set up.

    Related Pages:
    --------------
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
    --------------
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
    --------------
    https://datatables.net/reference/option/scrollX
    """
    return self._attrs["scrollX"]

  @scrollX.setter
  def scrollX(self, val):
    self._attrs["scrollX"] = val

  @property
  def scrollCollapse(self):
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

    https://datatables.net/examples/advanced_init/length_menu.html
    :return:

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
