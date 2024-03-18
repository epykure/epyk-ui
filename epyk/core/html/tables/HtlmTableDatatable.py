#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List

from epyk.core.py import primitives, types
from epyk.core.html import Html
from epyk.core.html.mixins import MixHtmlState
from epyk.core.html.options import OptTableDatatable
from epyk.core.html.tables.evts import EvtTableDatatable
from epyk.core.js.packages import JsDatatable
from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtmlTables

# The list of CSS classes
from epyk.core.css.styles import GrpClsTable

# External DataTable extensions added on demand to add some extra features
# Details of the different extensions are available on the different websites
# https://datatables.net/extensions/
extensions = {
    'rowsGroup': {'jsImports': ['datatables-rows-group']},
}


class Table(MixHtmlState.HtmlOverlayStates, Html.Html):
    requirements = ('datatables',)
    name = 'Table'
    tag = "table"
    _option_cls = OptTableDatatable.TableConfig

    def __init__(self, page: primitives.PageModel, records, width, height, html_code, options, profile):
        data, columns, self.__config = [], [], None
        super(Table, self).__init__(page, [], html_code=html_code, profile=profile, options=options,
                                    css_attrs={"width": width, "height": height})
        if records is not None:
            self.options.data = records

    @property
    def events(self) -> EvtTableDatatable.EvtDatatable:
        """Common events for tables"""
        return EvtTableDatatable.EvtDatatable(page=self.page, component=self)

    @property
    def dom(self) -> JsHtmlTables.JsHtmlDatatable:
        """Return all the Javascript functions defined for an HTML Component.
        Those functions will use plain javascript available for a DOM element by default.

        Usage::

          div = page.ui.div(htmlCode="testDiv")
          print(div.dom.content)

        :return: A Javascript Dom object.
        """
        if self._dom is None:
            self._dom = JsHtmlTables.JsHtmlDatatable(component=self, page=self.page)
            self._dom._container = "%s.parentNode.parentNode" % self._dom.element
        return self._dom

    @property
    def style(self) -> GrpClsTable.Datatable:
        """Property to the CSS Style of the component"""
        if self._styleObj is None:
            self._styleObj = GrpClsTable.Datatable(self)
        return self._styleObj

    @property
    def options(self) -> OptTableDatatable.TableConfig:
        """Datatable table options"""
        return super().options

    def get_column(self, by_title: str):
        """Get the column object from it is title.

        :param by_title:
        """
        for c in self.options.columns:
            if c.title == by_title:
                return c

    @property
    def js(self) -> JsDatatable.DatatableAPI:
        """Return the Javascript internal object.

        :return: A Javascript object
        """
        if self._js is None:
            self._js = JsDatatable.DatatableAPI(page=self.page, selector=self.js_code, set_var=False, component=self)
        return self._js

    def _set_js_code(self, html_code: str, js_code: str):
        """Set a different code for the component.
        This method will ensure both HTML and Js references will be properly changed for this component.
        This method is used by the js_code property and should not be used directly.

        :param html_code: The new HTML code
        :param js_code: The new JavaScript code
        """
        self.js._selector = js_code
        self.dom.varName = "document.getElementById(%s)" % JsUtils.jsConvertData(html_code, None)
        self.dom.jquery.varName = "$('#' + %s)" % JsUtils.jsConvertData(html_code, None)
        self._dom._container = "document.getElementById(%s).parentNode.parentNode" % JsUtils.jsConvertData(html_code, None)

    def define(self, options: types.JS_DATA_TYPES = None, dataflows: List[dict] = None, component_id: str = None):
        """

        :param options:
        :param dataflows:
        :param component_id: Optional. The component reference (the htmlCode)
        :return:
        """
        self.js_code = component_id

    def build(self, data: types.JS_DATA_TYPES = None, options: types.OPTION_TYPE = None,
              profile: types.PROFILE_TYPE = False, component_id: str = None,
              stop_state: bool = True, dataflows: List[dict] = None) -> str:
        """

        :param data: A String corresponding to a JavaScript object
        :param options: Optional. Specific Python options available for this component
        :param profile: Optional. A flag to set the component performance storage
        :param component_id: Optional. The component reference (the htmlCode)
        :param stop_state: Remove the top panel for the component state (error, loading...)
        :param dataflows: Chain of data transformations
        """
        self.js_code = component_id
        if data:
            state_expr = ""
            if stop_state:
                state_expr = ";%s" % self.hide_state(self.html_code)
            return JsUtils.jsConvertFncs(
                [self.js.clear(),
                 self.js.rows.add(JsUtils.jsWrap(JsUtils.dataFlows(data, dataflows, self.page)), update=True),
                 state_expr], toStr=True, profile=profile)

        return '%s = %s.DataTable(%s)' % (
            self.js_code, self.dom.jquery.varId, self.options.config_js(options))

    def __str__(self):
        self.page.properties.js.add_builders(self.refresh())
        return "<%s %s></%s>" % (self.tag, self.get_attrs(css_class_names=self.style.get_classes()), self.tag)
