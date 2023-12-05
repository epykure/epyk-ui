#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.py import primitives, types as etypes

from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtml
from epyk.core.js.objects import JsNodeDom
from epyk.core.js.primitives import JsObjects


class JsHtmlTabulatorCell(JsHtml.JsHtml):

    def _init__(self, js_code: str, page: primitives.PageModel, component: primitives.HtmlModel = None):
        self.tableId = js_code
        self.js_code = js_code
        self.page = page
        self.component = component

    def getElement(self):
        """
        The getElement function returns the DOM node for the cell.

        Related Pages:

          https://tabulator.info/docs/5.4/components#component-row
        """
        return JsNodeDom.JsDoms.get("cell.getElement()")

    def getColumnField(self):
        """
        The getField function returns the field name for the column.

        Related Pages:

          https://tabulator.info/docs/5.4/components
        """
        return JsObjects.JsObject.JsObject.get("cell.getColumn().getField()")

    def getColumnTitle(self):
        """ """
        return JsObjects.JsObject.JsObject.get("cell.getColumn().getDefinition().title")

    def getValue(self):
        """
        The getValue function returns the current value for the cell.

        Related Pages:

          https://tabulator.info/docs/5.4/components#component-cell
        """
        return JsObjects.JsObject.JsObject.get("cell.getValue()")

    def getRow(self):
        """
        The getRow function returns the RowComponent for the row that contains the cell.

        Related Pages:

          https://tabulator.info/docs/5.4/components#component-group
        """
        return JsObjects.JsObject.JsObject.get("cell.getRow()")

    def getData(self):
        """
        The getData function returns the data object for the row.

        Related Pages:

          https://tabulator.info/docs/5.4/components#component-calc
        """
        return JsObjects.JsObject.JsObject.get("cell.getRow().getData()")


class JsHtmlTabulator(JsHtml.JsHtml):

    @property
    def val(self):
        """ Return a Javascript val object """
        return JsObjects.JsObjects.get(
            "{%s: {value: %s, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (
                self.htmlCode, self.content.toStr()))

    @property
    def content(self):
        """ Get Tabulator table content. """
        return JsHtml.ContentFormatters(self.page, "%s.getData()" % self.component.tableId)

    @property
    def headers(self):
        """
        Get Tabulator table headers.

        Related Pages:

          https://tabulator.info/docs/5.4/columns#get-definition
        """
        return JsObjects.JsObjects.get("%s.getColumnDefinitions()" % self.component.tableId)

    def empty(self):
        """
        You can remove all data from the table using the clearData function:

        Related Pages:

          https://tabulator.info/docs/5.4/update#alter-empty
        """
        return self.component.js.clearData()

    def createWidget(self, html_code: str, container: str = None, options: etypes.JS_DATA_TYPES = None):
        """Create a new widget derived from an existing one.
        Using this method will make the main object as a template namely it will be removed from the page scope.

        :param html_code: The widget HTML code
        :param container: The widget container. Default the body
        :param options: The specific widget options
        """
        self.component.options.managed = False
        self.component.js_code = html_code
        lib = "bb" if self.component.name == "Billboard" else 'c3'
        js_code = JsUtils.jsConvertData(self.component.js_code, None).toStr()
        if js_code.startswith("window"):
            js_code = js_code[7:-1]
        return JsUtils.jsWrap('''
(function(containerId, tag, htmlCode, jsCode, ctx, attrs){
    const newDiv = document.createElement(tag);
    Object.keys(attrs).forEach(function(key) {newDiv.setAttribute(key, attrs[key]);}); newDiv.id = htmlCode;
    if(!containerId){document.body.appendChild(newDiv)} else {document.getElementById(containerId).appendChild(newDiv)};
    window[jsCode] = new Tabulator("#"+ htmlCode, ctx); return newDiv;
})(%(container)s, "%(tag)s", %(html_code)s, %(js_code)s, %(ctx)s, %(attrs)s)''' % {
            "js_code": js_code,
            "attrs": self.component.get_attrs(css_class_names=self.component.style.get_classes(), to_str=False),
            "html_code": JsUtils.jsConvertData(html_code or self.component.html_code, None),
            "tag": self.component.tag, "ctx": self.component.options.config_js(options).toStr(), "lib": lib,
            "container": JsUtils.jsConvertData(container, None)
        })


class JsHtmlAggrid(JsHtml.JsHtml):

    @property
    def content(self):
        """ Get the AgGrid table content """
        return JsHtml.ContentFormatters(self.page, self.component.js.getRowsData().toStr())

    def empty(self):
        """ Empty the AgGrid table. """
        return self.component.js.empty()

    def selection(self):
        return self.component.js.getSelectedRows()

    def createWidget(self, html_code: str, container: str = None, options: etypes.JS_DATA_TYPES = None):
        """Create a new widget derived from an existing one.
        Using this method will make the main object as a template namely it will be removed from the page scope.

        :param html_code: The widget HTML code
        :param container: The widget container. Default the body
        :param options: The specific widget options
        """
        self.component.options.managed = False
        self.component.js_code = html_code
        js_code = JsUtils.jsConvertData(self.component.js_code, None).toStr()
        if js_code.startswith("window"):
            js_code = js_code[7:-1]
        return JsUtils.jsWrap('''
(function(containerId, tag, htmlCode, jsCode, ctx, attrs){
    const newDiv = document.createElement(tag);
    Object.keys(attrs).forEach(function(key) {newDiv.setAttribute(key, attrs[key]);}); newDiv.id = htmlCode; 
    if(!containerId){ document.body.appendChild(newDiv)} else {document.getElementById(containerId).appendChild(newDiv)};
    window[jsCode] = ctx; new agGrid.Grid(newDiv, window[jsCode]); return newDiv
})(%(container)s, "%(tag)s", %(html_code)s, %(js_code)s, %(ctx)s, %(attrs)s)
        ''' % {
            "js_code": js_code,
            "attrs": self.component.get_attrs(css_class_names=self.component.style.get_classes(), to_str=False),
            "html_code": JsUtils.jsConvertData(html_code or self.component.html_code, None),
            "tag": self.component.tag, "ctx": self.component.options.config_js(options),
            "container": JsUtils.jsConvertData(container, None),
        })