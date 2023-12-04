#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List

from epyk.core.py import primitives, types
from epyk.core.html import Html
from epyk.core.html.mixins import MixHtmlState
from typing import Generator, Dict
from epyk.core.html.options import OptTableAgGrid

from epyk.core.js import JsUtils
from epyk.core.js.packages import JsAgGrid
from epyk.core.js.html import JsHtmlTables

# The list of CSS classes
from epyk.core.css.styles import GrpClsTable


class Table(MixHtmlState.HtmlOverlayStates, Html.Html):
    name = 'Ag Grid Table'
    tag = "div"
    requirements = ('ag-grid-community',)
    _option_cls = OptTableAgGrid.TableConfig

    def __init__(self, page: primitives.PageModel, records, width, height, html_code, options, profile):
        data, columns, self.__config = [], [], None
        super(Table, self).__init__(page, None, html_code=html_code, profile=profile, options=options,
                                    css_attrs={"width": width, "height": height})
        if records is not None:
            self.options.data = records

    def theme(self, name: str, custom_cls_name: bool = False, row_height: int = None, css_overrides: dict = None):
        """Define the theme to be used for the Aggrid table.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/themes/>`_
        `Related Pages <https://www.ag-grid.com/javascript-data-grid/global-style-customisation-variables/>`_

        Usage::

            table = page.ui.tables.aggrids.table(rows=["athlete", "country", "sport", 'year'])
            table.theme("balham")

            table = page.ui.tables.aggrids.table(rows=["athlete", "country", "sport", 'year'])
            table.theme("ag-theme-mycustomtheme", custom_cls_name=True)

        :param name: Aggrid theme name or Custom CSS class name
        :param custom_cls_name: Optional. Flag to specify if the theme is coming from the prdefined ones in Ag Grid
        :param row_height: Optional. To change the row height value to match the new theme definition (35px)
        :param css_overrides: Optional. Global Styling customisation
        """
        if not custom_cls_name:
            if row_height is not None:
                self.options.rowHeight = row_height
            if self.page.imports.pkgs.ag_grid.community_version:
                self.page.imports.append_to(
                    "ag-grid-community", [
                        {'script': 'ag-theme-%s.min.css' % name,
                         'path': 'ag-grid/%s/styles/' % self.page.imports.pkgs.ag_grid.version[0],
                         'node_path': 'styles/'}])
            else:
                self.page.imports.append_to(
                    "ag-grid-community", [
                        {'script': 'ag-theme-%s.min.css' % name,
                         'path': 'ag-grid-enterprise@%s/styles/' % self.page.imports.pkgs.ag_grid.version[0],
                         'node_path': 'styles/'}])
            self.attr["class"].add("ag-theme-%s" % name)
        else:
            self.attr["class"].add(name)
        self.style.theme_name = name
        if css_overrides is not None:
            css_props = []
            for k, v in css_overrides.items():
                if not k.startswith("--ag-"):
                    css_props.append("--ag-%s:%s" % (k, v))
                else:
                    css_props.append("%s:%s" % (k, v))
            self.page.properties.css.add_text(
                ".ag-theme-%s {%s}" % (name, ";".join(css_props)), "aggrid_theme_ovr", replace=True)
        self.options.rowHeight = self.options.rowHeight

    def headers(self, cols_def: Dict[str, dict]):
        """Set columns definition.

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
        """Get a generator with all the columns defined for the table on the Python side.
        This function will only return columns defined from the Python side.
        """
        for c in self.options.js_tree.setdefault("columnDefs", []):
            yield c

    def get_column(self, by_field: str = None, by_title: str = None) -> OptTableAgGrid.Column:
        """Get the column from the underlying Tabulator object by field or by title.
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
        """Add internal CSS classes.

        Usage::

          grid = page.ui.tables.aggrids.table()
          grid.style.strip({"color": "blue"})
        """
        if self._styleObj is None:
            self._styleObj = GrpClsTable.Aggrid(self)
        return self._styleObj

    @property
    def options(self) -> OptTableAgGrid.TableConfig:
        """Ag Grid table options.

        Usage::

          grid = page.ui.tables.aggrids.table()
          grid.options.paginationPageSize = 2
        """
        return super().options

    @property
    def js(self) -> JsAgGrid.AgGrid:
        """Return the Javascript internal object.

        :return: A Javascript object
        """
        if self._js is None:
            self._js = JsAgGrid.AgGrid(page=self.page, selector=self.js_code, set_var=False, component=self)
        return self._js

    @property
    def dom(self) -> JsHtmlTables.JsHtmlAggrid:
        """HTML Dom object"""
        if self._dom is None:
            self._dom = JsHtmlTables.JsHtmlAggrid(self, page=self.page)
        return self._dom

    def add_column(self, field: str, title: str = None, attrs: dict = None) -> OptTableAgGrid.Column:
        """Add a column to the column definition for the table.

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

    def define(self, options: types.JS_DATA_TYPES = None, dataflows: List[dict] = None, component_id: str = None):
        """Common JavaScript function to set the table definition.
        If options are defined the definition will be specific to the column definition.

        `Related Pages <https://www.ag-grid.com/javascript-data-grid/row-selection/>`_

        :param options: Optional. The table API attributes. If None return current definition.
        :param dataflows: Chain of config transformations
        :param component_id: Optional. The object reference ID
        """
        self.js_code = component_id
        if options is None:
            options = JsUtils.jsWrap("%s.api" % self.js.varId)
            return JsUtils.jsWrap(JsUtils.dataFlows(options, dataflows, self.page))

        return self.js.setColumnDefs(JsUtils.jsWrap(JsUtils.dataFlows(options, dataflows, self.page)))

    def _set_js_code(self, html_code: str, js_code: str):
        """Set a different code for the component.
        This method will ensure both HTML and Js references will be properly changed for this component.
        This method is used by the js_code property and should not be used directly.

        :param html_code: The new HTML code
        :param js_code: The new JavaScript code
        """
        self.dom.varName = "document.getElementById(%s)" % JsUtils.jsConvertData(html_code, None)
        self.js.varName = js_code

    def build(self, data: types.JS_DATA_TYPES = None, options: types.OPTION_TYPE = None,
              profile: types.PROFILE_TYPE = None, component_id: str = None,
              stop_state: bool = True, dataflows: List[dict] = None):
        """Common JavaScript function to add rows to the table.

        Usage::

          grid = page.ui.tables.aggrids.table()
          grid.add_column("col1", "Column")
          btn_aggrid = page.ui.button("Aggrid").click([grid.build([{"col1": "row %s" % i}for i in range(n)])])

        :param data: Optional.
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        :param component_id: Optional. The object reference ID
        :param stop_state: Remove the top panel for the component state (error, loading...)
        :param dataflows: Chain of data transformations
        """
        self.js_code = component_id
        if data is not None:
            state_expr = ""
            if stop_state:
                state_expr = ";%s" % self.hide_state(self.html_code)
            return "%s%s" % (self.js.setRowData(data, dataflows=dataflows).toStr(), state_expr)

        return 'var %(tableId)s = %(config)s; new agGrid.Grid(%(htmlCode)s, %(tableId)s)' % {
            'tableId': self.js_code, 'config': self.options.config_js(options), 'htmlCode': self.dom.varName}

    def click(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, source_event: str = None,
              on_ready: bool = False, data_ref: str = "data"):
        """The onclick event occurs when the user clicks on an element.

        Usage::

          div = page.ui.div()
          div.click([page.js.alert("This is a test")])

        `Related Pages <https://www.w3schools.com/jsref/event_onclick.asp>`_

        :param js_funcs: A Javascript Python function
        :param profile: Optional. Set to true to get the profile for the function on the Javascript console
        :param source_event: Optional. The source target for the event
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
        :param data_ref: Optional. Data reference on the Js side
        """
        row_style = self.options.rowStyle
        if row_style is None:
            self.options.rowStyle = {"cursor": 'pointer'}
        else:
            row_style.update({"cursor": 'pointer'})
            self.options.rowStyle = row_style
        self.options.onSelectionChanged(js_funcs, profile)
        return self

    def __str__(self):
        self.page.properties.js.add_builders(self.refresh())
        return "<%s %s></%s>" % (self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.tag)
