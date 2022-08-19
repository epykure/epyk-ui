#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.py import primitives, types
from epyk.core.html import Html
from epyk.core.html.options import OptTableAgGrid

from epyk.core.js.packages import JsAgGrid
from epyk.core.js.html import JsHtmlTables

# The list of CSS classes
from epyk.core.css.styles import GrpClsTable


class Table(Html.Html):
  name = 'Ag Grid Table'
  requirements = ('ag-grid-community', )
  _option_cls = OptTableAgGrid.TableConfig

  def __init__(self, page: primitives.PageModel, records, width, height, html_code, options, profile):
    data, columns, self.__config = [], [], None
    super(Table, self).__init__(page, [], html_code=html_code, profile=profile, options=options,
                                css_attrs={"width": width, "height": height})
    if records is not None:
      self.options.data = records

  def headers(self, cols_def: dict):
    """
    Description:
    -----------
    Set columns definition.

    Usage::

      grid = page.ui.tables.aggrids.table()
      grid.add_column("col1", "Column")
      grid.headers({"col1": {"headerName": "Column 1"}})

    Attributes:
    ----------
    :param cols_def:
    """
    defined_cols = []
    for col in self.options.js_tree.setdefault("columnDefs", []):
      if col.colId in cols_def:
        col.set_attrs(cols_def[col.colId])
        defined_cols.append(col.colId)
    # add the extra columns to the table definition
    for col_id, col_attrs in cols_def.items():
      if col_id not in defined_cols:
        self.add_column(col_id, attrs=col_attrs)

  @property
  def style(self) -> GrpClsTable.Aggrid:
    """
    Description:
    -----------
    Add internal CSS classes.

    Usage::

      grid = page.ui.tables.aggrids.table()
      grid.style.strip({"color": "blue"})
    """
    if self._styleObj is None:
      self._styleObj = GrpClsTable.Aggrid(self)
    return self._styleObj

  @property
  def options(self) -> OptTableAgGrid.TableConfig:
    """
    Description:
    ------------
    Ag Grid table options.

    Usage::

      grid = page.ui.tables.aggrids.table()
      grid.options.paginationPageSize = 2
    """
    return super().options

  @property
  def js(self) -> JsAgGrid.AgGrid:
    """
    Description:
    -----------
    Return the Javascript internal object.

    :return: A Javascript object
    """
    if self._js is None:
      self._js = JsAgGrid.AgGrid(page=self.page, selector=self.tableId, set_var=False, component=self)
    return self._js

  @property
  def dom(self) -> JsHtmlTables.JsHtmlAggrid:
    """
    Description:
    -----------
    HTML Dom object.
    """
    if self._dom is None:
      self._dom = JsHtmlTables.JsHtmlAggrid(self, page=self.page)
    return self._dom

  def add_column(self, field: str, title: str = None, attrs: dict = None):
    """
    Description:
    -----------
    Add a column to the column definition for the table.

    Usage::

      grid = page.ui.tables.aggrids.table()
      grid.add_column("test", "Test Column")

    Attributes:
    ----------
    :param field: The column attribute
    :param title: Optional. The column title
    :param attrs: Optional. The specific column properties
    """
    col_def = self.options.columns
    col_def.field = field
    col_def.colId = field
    col_def.headerName = field if title is None else title
    if attrs is not None:
      col_def.update(attrs)
    return col_def

  @property
  def tableId(self) -> str:
    """
    Description:
    -----------
    Return the Javascript variable of the chart.

    Usage::

      table.tableId
    """
    return "%s_obj" % self.htmlCode

  def define(self, options: types.JS_DATA_TYPES = None):
    """
    Description:
    ------------
    Common JavaScript function to set the table columns definition.

    Attributes:
    ----------
    :param options: Optional. The header attributes
    """
    return self.js.setColumnDefs(options)

  def build(self, data: types.JS_DATA_TYPES = None, options: types.OPTION_TYPE = None,
            profile: types.PROFILE_TYPE = None, component_id: str = None):
    """
    Description:
    -----------
    Common JavaScript function to add rows to the table.

    Usage::

      grid = page.ui.tables.aggrids.table()
      grid.add_column("col1", "Column")
      btn_aggrid = page.ui.button("Aggrid").click([
        grid.build([{"col1": "row %s" % i}for i in range(n)])
      ])

    Attributes:
    ----------
    :param data: Optional.
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    :param component_id: Optional. The object reference ID
    """
    if data:
      return self.js.setRowData(data)

    return 'var %(tableId)s = %(config)s; new agGrid.Grid(%(htmlCode)s, %(tableId)s)' % {
      'tableId': self.tableId, 'config': self.options.config_js(options), 'htmlCode': component_id or self.dom.varName}

  def loading(self, status: bool = True, color: str = None):
    """
    Description:
    -----------
    Add loading banner.

    Attributes:
    ----------
    :param status: The visibility flag
    :param color: Not used for the moment
    """
    if status:
      return self.js.showLoadingOverlay()

    return self.js.hideOverlay()

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    return "<div %s></div>" % (self.get_attrs(css_class_names=self.style.get_classes()))
