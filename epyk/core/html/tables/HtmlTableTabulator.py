#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Generator, List

from epyk.core.py import primitives, types
from epyk.core.html import Html
from epyk.core.html.mixins import MixHtmlState

from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtmlTables
from epyk.core.js.packages import JsTabulator
from epyk.core.html.options import OptTableTabulator

# The list of CSS classes
from epyk.core.css.styles import GrpClsTable


class Table(MixHtmlState.HtmlOverlayStates, Html.Html):
    requirements = ('tabulator-tables',)
    name = 'Tabulator Table'
    tag = "div"
    _option_cls = OptTableTabulator.TableConfig

    def __init__(self, page: primitives.PageModel, records, width, height, html_code, options, profile):
        data, columns, self._json_config = [], [], {}
        super(Table, self).__init__(page, None, html_code=html_code, profile=profile, options=options,
                                    css_attrs={"width": width, "height": height})
        if records is not None:
            self.options.data = records
        self.style.css.background = None
        self.__bespoke_formatters = set()
        if options is not None and options.get("striped"):
            self.style.strip()

    @property
    @Html.deprecated("Should use .js._. instead to get table core components")
    def cell(self) -> JsHtmlTables.JsHtmlTabulatorCell:
        return JsHtmlTables.JsHtmlTabulatorCell(js_code=self.js_code, page=self.page, component=self)

    @property
    def style(self) -> GrpClsTable.Tabulator:
        """Property to the CSS Style of the component"""
        if self._styleObj is None:
            self._styleObj = GrpClsTable.Tabulator(self)
        return self._styleObj

    @property
    def dom(self) -> JsHtmlTables.JsHtmlTabulator:
        """HTML Dom object"""
        if self._dom is None:
            self._dom = JsHtmlTables.JsHtmlTabulator(self, page=self.page)
        return self._dom

    @property
    def options(self) -> OptTableTabulator.TableConfig:
        """Tabulator table options"""
        return super().options

    @property
    @Html.deprecated("use self.options instead")
    def config(self) -> OptTableTabulator.TableConfig:
        """Tabulator configuration options.
        Deprecated and replaced by component options.
        """
        return self.options

    @property
    def js(self) -> JsTabulator.Tabulator:
        """Return the Javascript internal object specific to this package.

        :return: A Javascript object
        """
        if self._js is None:
            self._js = JsTabulator.Tabulator(page=self.page, selector=self.js_code, set_var=False, component=self)
        return self._js

    def data(self, data):
        """Add data to the table.

        :param data: Data object
        """
        self.options.data = data

    def add_column(self, field: str = None, title: str = None):
        """Add new column to the underlying Tabulator object.

        Usage::

            table = page.ui.table(randoms.languages)
            c = table.add_column()
            c.formatter = "rowSelection"
            c.titleFormatter = "rowSelection"
            c.hozAlign = "center"
            c.headerSort = False
            c.cellClick(["cell.getRow().toggleSelect()"])

        :param field: Optional. The key in the row
        :param title: Optional. The title for the column. Default to the field
        """
        return self.options.add_column(field, title)

    def get_column(self, by_field: str = None, by_title: str = None) -> OptTableTabulator.Column:
        """Get the column from the underlying Tabulator object by field or by title.
        Pointing by field is recommended as the title might change quite easily.
        This function will only get columns defined from the Python side.

        :param by_field: Optional. The field reference for the column
        :param by_title: Optional. The title reference for the column
        """
        return self.options.get_column(by_field, by_title)

    def get_columns(self) -> Generator[OptTableTabulator.Column, None, None]:
        """Get a generator with all the columns defined for the table on the Python side.
        This function will only return columns defined from the Python side.
        """
        for c in self.options.columns:
            yield c

    def headers(self, cols_def: dict):
        """Update the header definition thanks to a static configuration.

        :param cols_def: The header definition
        """
        for c in self.options.columns:
            if c.field is not None and c.field in cols_def:
                c.js_tree.update(cols_def[c.field])

    def click(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, source_event: str = None,
              on_ready: bool = False, data_ref: str = "data"):
        """Use a rowClick event as underlying click event.
        Use the function row.getData() to make the data available.

        :param js_funcs: Javascript functions
        :param profile: Optional. A flag to set the component performance storage
        :param source_event: Optional. The JavaScript DOM source for the event (can be a sug item)
        :param on_ready: Optional. Specify if the event needs to be trigger when the page is loaded
        :param data_ref: JavaScript variable name for the main data in the function (default data)
        """
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        self.options.rowClick(["var %s = row.getData()" % data_ref] + js_funcs)
        return self

    def _set_js_code(self, html_code: str, js_code: str):
        """Set a different code for the component.
        This method will ensure both HTML and Js references will be properly changed for this component.
        This method is used by the js_code property and should not be used directly.

        :param html_code: The new HTML code
        :param js_code: The new JavaScript code
        """
        self.dom.varName = "document.getElementById('%s')" % html_code
        self.js.varName = js_code

    def define(self, options: types.JS_DATA_TYPES = None, dataflows: List[dict] = None, component_id: str = None):
        """Common JavaScript function to set the table columns definition.

        Usage::

          tab = page.ui.tables.tabulators.table()
          page.ui.button("Update Tabulator").click([tab.define([{"field": "col1", "title": "Column 1"}]),])

        :param options: Optional. The header attributes
        :param dataflows: Chain of config transformations
        :param component_id: Optional. Change the component id if specific
        """
        self.js_code  = component_id
        if options is None:
            options = JsUtils.jsWrap(self.js.varId)
            return JsUtils.jsWrap(JsUtils.dataFlows(options, dataflows, self.page))

        return self.js.setColumns(JsUtils.jsWrap(JsUtils.dataFlows(options, dataflows, self.page)))

    _js__builder__ = 'var %(tableId)s = new Tabulator("#%(htmlCode)s", Object.assign(%(config)s, %(options)s))'

    def build(self, data: types.JS_DATA_TYPES = None, options: types.OPTION_TYPE = None,
              profile: types.PROFILE_TYPE = None, component_id: str = None,
              stop_state: bool = True, dataflows: List[dict] = None):
        """Common JavaScript function to add data to the table.

        Usage::

          tab = page.ui.tables.tabulators.table()
          page.ui.button("Update Tabulator").click([
            tab.define([{"field": "col1", "title": "Column 1"}]),
            tab.build([{"col1": "row %s" % i}for i in range(n)])])

        :param data: Optional. A String corresponding to a JavaScript object
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        :param component_id: Optional. Change the component id if specific
        :param stop_state: Remove the top panel for the component state (error, loading...)
        :param dataflows: Chain of data transformations
        """
        self.js_code  = component_id
        if data is not None:
            state_expr = ""
            if stop_state:
                state_expr = ";%s" % self.hide_state(self.html_code)
            return "%s%s" % (self.js.setData(JsUtils.dataFlows(data, dataflows, self.page)).toStr(), state_expr)

        return self._js__builder__ % {
            "tableId": self.js_code, "htmlCode": self.html_code, "config": self._json_config,
            "options": self.options.config_js(options)}

    def extendModule(self, category: str, type: str, func_name: str, func_def: str):
        """Tabulator is built in a modular fashion with a core codebase providing basic table rendering functionality
        and a series of modules that provide all of its wonderful features.
        All of the available modules are installed by default to ensure that you can provide your users with the richest
        experience possible with minimal setup.

        `Tabulator Modules <http://tabulator.info/docs/4.0/modules>`_
        `Tabulator keybindings <http://tabulator.info/docs/4.2/modules#module-keybindings>`_

        :param category: The name of the module. e.g format
        :param type: The name of the property you want to extend. e.g. formatters
        :param func_name: The alias of teh function to be added to the registry
        :param func_def: The function definition to be attached to this function name
        """
        if func_name not in self.__bespoke_formatters:
            self.__bespoke_formatters.add(func_name)
            self.page.properties.js.add_builders('Tabulator.prototype.extendModule("%s", "%s", {"%s": %s});' % (
                category, type, func_name, func_def))
        return self

    def __str__(self):
        self.page.properties.js.add_builders(self.refresh())
        return "<%s %s></%s>" % (self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.tag)


class TableTree(Table):
    _option_cls = OptTableTabulator.TableTreeConfig

    def __init__(self, page: primitives.PageModel, records, width, height, html_code, options, profile):
        data, columns, self._json_config = [], [], {}
        super(TableTree, self).__init__(page, records, width, height, html_code, options, profile)
        if records is not None:
            self.options.data = records
        self.style.css.background = None

    @property
    def options(self) -> OptTableTabulator.TableTreeConfig:
        """Tabulator table options"""
        return super().options
