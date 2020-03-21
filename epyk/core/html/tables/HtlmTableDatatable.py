
from epyk.core.html import Html
from epyk.core.js.packages import JsDatatable

from epyk.core.data import DataClass

# The list of CSS classes
# from epyk.core.css.styles import CssGrpClsTable


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
    return self._attrs["ajax"]

  @ajax.setter
  def ajax(self, val):
    self._attrs["ajax"] = val

  @property
  def processing(self):
    return self._attrs["processing"]

  @processing.setter
  def processing(self, val):
    self._attrs["processing"] = val

  @property
  def serverSide(self):
    return self._attrs["serverSide"]

  @serverSide.setter
  def serverSide(self, val):
    self._attrs["serverSide"] = val

  @property
  def deferLoading(self):
    """
    https://datatables.net/examples/server_side/defer_loading.html

    :return:
    """
    return self._attrs["deferLoading"]

  @deferLoading.setter
  def deferLoading(self, val):
    self._attrs["deferLoading"] = val

  @property
  def data(self):
    return self._attrs["data"]

  @data.setter
  def data(self, val):
    self._attrs["data"] = val

  @property
  def paging(self):
    return self._attrs["paging"]

  @paging.setter
  def paging(self, val):
    self._attrs["paging"] = val

  @property
  def info(self):
    return self._attrs["info"]

  @info.setter
  def info(self, val):
    self._attrs["info"] = val

  @property
  def ordering(self):
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
    return self._attrs["scrollY"]

  @scrollY.setter
  def scrollY(self, val):
    self._attrs["scrollY"] = val

  @property
  def scrollX(self):
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
