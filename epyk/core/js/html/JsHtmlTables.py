#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.py import primitives

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
