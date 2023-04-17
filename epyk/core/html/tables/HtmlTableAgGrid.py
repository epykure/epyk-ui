#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.py import primitives, types
from epyk.core.html import Html
from epyk.core.html.mixins import MixHtmlState
from typing import Generator, Dict
from epyk.core.html.options import OptTableAgGrid

from epyk.core.js.packages import JsAgGrid
from epyk.core.js.html import JsHtmlTables

# The list of CSS classes
from epyk.core.css.styles import GrpClsTable


class Table(MixHtmlState.HtmlOverlayStates, Html.Html):
    name = 'Ag Grid Table'
    requirements = ('ag-grid-community',)
    _option_cls = OptTableAgGrid.TableConfig

    def __init__(self, page: primitives.PageModel, records, width, height, html_code, options, profile):
        data, columns, self.__config = [], [], None
        super(Table, self).__init__(page, None, html_code=html_code, profile=profile, options=options,
                                    css_attrs={"width": width, "height": height})
        if records is not None:
            self.options.data = records

    def headers(self, cols_def: Dict[str, dict]):
        """
        Set columns definition.

        Usage::

          grid = page.ui.tables.aggrids.table()
          grid.add_column("col1", "Column")
          grid.headers({"col1": {"headerName": "Column 1"}})

        :param cols_def: A dictionary with the columns definition
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
        return self

    def get_columns(self) -> Generator[OptTableAgGrid.Column, None, None]:
        """
        Get a generator with all the columns defined for the table on the Python side.

        This function will only return columns defined from the Python side.
        """
        for c in self.options.js_tree.setdefault("columnDefs", []):
            yield c

    def get_column(self, by_field: str = None, by_title: str = None) -> OptTableAgGrid.Column:
        """
        Get the column from the underlying Tabulator object by field or by title.
        Pointing by field is recommended as the title might change quite easily.

        This function will only get columns defined from the Python side.

        :param by_field: Optional. The field reference for the column
        :param by_title: Optional. The title reference for the column
        """
        for c in self.get_columns():
            if by_field is not None and by_field == c.field:
                return c

            if by_title is not None and by_title == c.headerName:
                return c

    @property
    def style(self) -> GrpClsTable.Aggrid:
        """
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
        Ag Grid table options.

        Usage::

          grid = page.ui.tables.aggrids.table()
          grid.options.paginationPageSize = 2
        """
        return super().options

    @property
    def js(self) -> JsAgGrid.AgGrid:
        """
        Return the Javascript internal object.

        :return: A Javascript object
        """
        if self._js is None:
            self._js = JsAgGrid.AgGrid(page=self.page, selector=self.tableId, set_var=False, component=self)
        return self._js

    @property
    def dom(self) -> JsHtmlTables.JsHtmlAggrid:
        """ HTML Dom object. """
        if self._dom is None:
            self._dom = JsHtmlTables.JsHtmlAggrid(self, page=self.page)
        return self._dom

    def add_column(self, field: str, title: str = None, attrs: dict = None):
        """
        Add a column to the column definition for the table.

        Usage::

          grid = page.ui.tables.aggrids.table()
          grid.add_column("test", "Test Column")

        :param field: The column attribute
        :param title: Optional. The column title
        :param attrs: Optional. The specific column properties
        """
        col_def = self.options.columns
        col_def.field = field
        col_def.colId = field
        col_def.headerName = field if title is None else title
        if attrs is not None:
            if "children" in attrs:
                for child in attrs["children"]:
                    col_def.add_children(child)
                del attrs["children"]

            col_def.update_config(attrs)
        return col_def

    @property
    def tableId(self) -> str:
        """
        Return the Javascript variable of the chart.

        Usage::

          table.tableId
        """
        return "%s_obj" % self.htmlCode

    def define(self, options: types.JS_DATA_TYPES = None):
        """
        Common JavaScript function to set the table columns definition.

        :param options: Optional. The header attributes
        """
        return self.js.setColumnDefs(options)

    def build(self, data: types.JS_DATA_TYPES = None, options: types.OPTION_TYPE = None,
              profile: types.PROFILE_TYPE = None, component_id: str = None, stop_state: bool = True):
        """
        Common JavaScript function to add rows to the table.

        Usage::

          grid = page.ui.tables.aggrids.table()
          grid.add_column("col1", "Column")
          btn_aggrid = page.ui.button("Aggrid").click([
            grid.build([{"col1": "row %s" % i}for i in range(n)])
          ])

        :param data: Optional.
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        :param component_id: Optional. The object reference ID
        :param stop_state: Remove the top panel for the component state (error, loading...)
        """
        if data is not None:
            state_expr = ""
            if stop_state:
                state_expr = ";%s" % self.hide_state(component_id)
            return "%s%s" % (self.js.setRowData(data).toStr(), state_expr)

        return 'var %(tableId)s = %(config)s; new agGrid.Grid(%(htmlCode)s, %(tableId)s)' % {
            'tableId': self.tableId, 'config': self.options.config_js(options),
            'htmlCode': component_id or self.dom.varName}

    def click(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, source_event: str = None,
              on_ready: bool = False, data_ref: str = "data"):
        if self.options.rowSelection is None:
            self.options.rowSelection = 'single'
        row_style = self.options.rowStyle
        if row_style is None:
            self.options.rowStyle = {"cursor": 'pointer'}
        else:
            row_style.update({"cursor": 'pointer'})
            self.options.rowStyle = row_style
        return super(Table, self).click(js_funcs, profile, source_event, on_ready)

    def __str__(self):
        self.page.properties.js.add_builders(self.refresh())
        return "<div %s></div>" % (self.get_attrs(css_class_names=self.style.get_classes()))
