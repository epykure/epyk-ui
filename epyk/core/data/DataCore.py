#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import sys
from pathlib import Path
from typing import Union, Any, List, Dict

from epyk.core.py import primitives
from epyk.core.js import JsUtils
from epyk.core.py import OrderedSet

from epyk.core.js.primitives import JsObjects


class DataAggregators:
    """JavaScript data aggregators"""

    def __init__(self, js_code: str = None, page: primitives.PageModel = None, chain = None, parent = None):
        self.varName, self.__chain = js_code, chain
        self.page, self.parent = page, parent

    def setData(self, data: Union[str, primitives.JsDataModel]):
        """Set the main dataset used for the transformations

        :param data: Data reference
        """
        self.varName = data
        return self

    def setPage(self, page: primitives.PageModel):
        """Set the page to improve performances by storing the functions only once.

        :param page: context / page object
        """
        self.page = page
        return self

    def max(self, column: str) -> JsObjects.JsArray.JsArray:
        """Returns the maximum value in list.
        If an iterator function is provided, it will be used on each value to generate the criterion by which the value
        is ranked. Infinity is returned if list is empty, so an isEmpty guard may be required.
        Non-numerical values in list will be ignored.

        `Underscorejs max <https://underscorejs.org/#max>`_

        :param column: The column name. The key in the list of dictionary
        """
        self.page.jsImports.add('underscore')
        return JsObjects.JsArray.JsArray("[_.max(%s, function(rec){return rec['%s']; })]" % (
            self.varName, column), page=self.page)

    def min(self, column: str) -> JsObjects.JsArray.JsArray:
        """Returns the minimum value in list.
        If an iterator function is provided, it will be used on each value to generate the criterion by which the value
        is ranked. Infinity is returned if list is empty, so an isEmpty guard may be required.
        Non-numerical values in list will be ignored.

        `Underscorejs min <https://underscorejs.org/#min>`_

        :param column: The column name. The key in the list of dictionary
        """
        self.page.jsImports.add('underscore')
        return JsObjects.JsArray.JsArray("[_.min(%s, function(rec){ return rec['%s']; })]" % (
            self.varName, column), page=self.page)

    def valsFor(self, columns: list, attrs: dict = None, js_src_path: str = None, records: List[dict] = None,
            verbose: bool = None) -> JsObjects.JsObject.JsObject:
        """Returns an object with as keys the columns and as values the list of distinct values in the records.

        :param columns: The list of columns to keep
        :param attrs: Optional. The static values to be added to the final records
        :param js_src_path: Optional. JavaScript file path
        :param records: Optional. Shortcut for the data reference used by this transformation
        :param verbose: Optional. Flag to display extra log messages
        """
        return self.func(
            func_args={"columns": columns, "attrs": attrs}, js_src_path=js_src_path, records=records, verbose=verbose)

    def sortBy(self, column: str) -> JsObjects.JsArray.JsArray:
        """Returns a (stably) sorted copy of list, ranked in ascending order by the results of running each value
        through iterator. iterator may also be the string name of the property to sort by (eg. length).

        :param column: The column name. The key in the list of dictionary
        """
        self.page.jsImports.add('underscore')
        column = JsUtils.jsConvertData(column, None)
        return JsObjects.JsArray.JsArray("_.sortBy(%s, %s)" % (self.varName, column), page=self.page)

    def func(self, js_src_path: str = None, func_args: dict = None, records: List[dict] = None, func_name: str = None,
             verbose: bool = None):
        """Generic function to register an aggregator function.
        Those functions can be used in any JavaScript fragments and they can be chained.

        :param js_src_path: Optional. JavaScript file path
        :param func_args: Optional. JavaScript's arguments
        :param records: Optional. Shortcut for the data reference used by this transformation
        :param func_name: Optional. JavaScript function definition (if needs to be different from the filename)
        :param verbose: Optional. Flag to display extra log messages
        """
        if js_src_path is None:
            pname = sys._getframe().f_back.f_code.co_name
            fname = func_name or "Agg%s" % (pname[0].upper() + pname[1:])
            js_src_path = Path(__file__).parent / ".." / "js" / "native" / "flows" / ("%s.js" % fname)
        fargs = None
        if func_args:
            fargs = ["%s: %s" % (k, JsUtils.jsConvertData(v, None)) for k, v in func_args.items()]
        if self.page:
            name = self.page.properties.js.add_from_file(str(js_src_path), category="constructor", verbose=verbose)[:-3]
            if fargs:
                if self.__chain is not None:
                    js_expr = "%s(%%s, {%s})" % (name, ",".join(fargs))
                    self.__chain.add(js_expr)
                    return self.parent

                js_expr = "%s(%s, {%s})" % (name, records or self.varName, ",".join(fargs))
                return JsObjects.JsArray.JsRecordSet(js_expr)

            if self.__chain is not None:
                js_expr = "%s(%%s)" % name
                self.__chain.add(js_expr)
                return self.parent

            js_expr = "%s(%s)" % (name, records or self.varName)
            return JsObjects.JsArray.JsRecordSet(js_expr)

        name = js_src_path.name[0].lower() + js_src_path.name[1:-3]
        with open(js_src_path) as fp:
            if fargs:
                if self.__chain is not None:
                    js_expr = "(function(r, attrs){%s; return %s(r, attrs)})(%%s, {%s})" % (
                        fp.read().strip(), name, ",".join(fargs))
                    self.__chain.add(js_expr)
                    return self.parent

                js_expr = "(function(r, attrs){%s; return %s(r, attrs)})(%s, {%s})" % (
                    fp.read().strip(), name, records or self.varName, ",".join(fargs))
                return JsObjects.JsArray.JsRecordSet(js_expr)

            if self.__chain is not None:
                js_expr = "(function(r){%s; return %s(r)})(%%s)" % (fp.read().strip(), name)
                self.__chain.add(js_expr)
                return self.parent

            js_expr = "(function(r){%s; return %s(r)})(%s)" % (fp.read().strip(), name, records or self.varName)
            return JsObjects.JsArray.JsRecordSet(js_expr)

    def sum(self, columns: list, attrs: dict = None, js_src_path: str = None, records: List[dict] = None,
            verbose: bool = None):
        """Reduce the record set by adding all the columns.

        Usages::

            page.body.onReady([
                page.js.console.log(ek.aggs.sum(["rating", "change"], records=randoms.languages), skip_data_convert=True)
            ])

        :param columns: The columns in the records to be counted
        :param attrs: Optional. The static values to be added to the final records
        :param js_src_path: Optional. JavaScript file path
        :param records: Optional. Shortcut for the data reference used by this transformation
        :param verbose: Optional. Flag to display extra log messages
        """
        return self.func(func_args={"columns": columns, "attrs": attrs}, js_src_path=js_src_path, records=records, verbose=verbose)

    def count(self, columns: list, attrs: dict = None, js_src_path: str = None, records: List[dict] = None,
              verbose: bool = None):
        """Reduce the record set by counting all the columns.

        Usages::

            page.body.onReady([
                page.js.console.log(ek.aggs.count(["rating", "change"], records=randoms.languages), skip_data_convert=True)
            ])

        :param columns: The columns in the records to be counted
        :param attrs: Optional. The static values to be added to the final records
        :param js_src_path: Optional. JavaScript file path
        :param records: Optional. Shortcut for the data reference used by this transformation
        :param verbose: Optional. Flag to display extra log messages
          """
        return self.func(func_args={"columns": columns, "attrs": attrs}, js_src_path=js_src_path, records=records, verbose=verbose)

    def countBy(self, column: str, attrs: dict = None, js_src_path: str = None, records: List[dict] = None,
                verbose: bool = None):
        """Reduce the record set by counting all the columns.

        Usages::

            page.body.onReady([
                page.js.console.log(ek.aggs.countBy("type", records=randoms.languages), skip_data_convert=True)
            ])

        :param column: The columns in the records to be counted
        :param attrs: Optional. The static values to be added to the final records
        :param js_src_path: Optional. JavaScript file path
        :param records: Optional. Shortcut for the data reference used by this transformation
        :param verbose: Optional. Flag to display extra log messages
        """
        return self.func(func_args={"column": column, "attrs": attrs}, js_src_path=js_src_path, records=records, verbose=verbose)

    def sumBy(self, columns: list, keys, dst_key: dict = None, cast_vals: bool = False, js_src_path: str = None,
              records = None, verbose: bool = None):
        """

        Usages::

            page.body.onReady([
                page.js.console.log(ek.aggs.sumBy(["rating", "change"], keys=["type"], records=randoms.languages), skip_data_convert=True)
            ])

        :param columns: The list of columns / attributes in the JavaScript object
        :param keys: The list of keys
        :param dst_key: Optional. Destination key in the record`
        :param cast_vals: Optional. Convert the data in the recordset (JavaScript function or boolean)
        :param js_src_path: Optional. JavaScript file path
        :param records: Optional. Shortcut for the data reference used by this transformation
        :param verbose: Optional. Flag to display extra log messages
        """
        if cast_vals is True:
            cast_vals = "parseFloat"
        elif cast_vals is False:
            cast_vals = "false"
        return self.func(
            func_args={"columns": columns, "convertFunc": JsUtils.jsWrap(cast_vals),
                       "srcKeys": keys, "dstKey": dst_key},
            js_src_path=js_src_path, records=records, verbose=verbose)

    def sumCols(self, columns: list, dst_key: dict = None, cast_vals: Union[bool, str] = False, attrs: dict = None,
                js_src_path: str = None, records = None, verbose: bool = None):
        """Sum a list of column and put the result to a new key.

        Usages::

            page.body.onReady([
                "let data = %s" % randoms.languages,
                page.js.console.log(ek.events.data.fltrs.setPage(page)
                    .sumCols(["rating", "change"], "total", case_sensitive=False)
            ])

        :param columns: The list of columns / attributes in the JavaScript object
        :param dst_key: Optional. Destination key in the record`
        :param cast_vals: Optional. Convert the data in the recordset (JavaScript function or boolean)
        :param attrs: Optional. Extra data to be added to the record
        :param js_src_path: Optional. JavaScript file path
        :param records: Optional. Shortcut for the data reference used by this transformation
        :param verbose: Optional. Flag to display extra log messages
        """
        if cast_vals is True:
            cast_vals = "parseFloat"
        elif cast_vals is False:
            cast_vals = "false"
        return self.func(
            func_args={"columns": columns, "convertFunc": JsUtils.jsWrap(cast_vals), "key": dst_key, "attrs": attrs},
            js_src_path=js_src_path, records=records, verbose=verbose)

    def processCols(self, literal, dst_key: dict = None, cast_vals: Union[bool, str] = False,
                    attrs: dict = None, js_src_path: str = None, records = None, verbose: bool = None
                    ):
        """Create a new column to each records based on a literal expression.
        This column can then be used by other transformation functions.

        Usages::

            page.body.onReady([
                "let data = %s" % randoms.languages,
                page.js.console.log(ek.events.data.fltrs.setPage(page)
                    .aggs.processCols("${rec.rating - rec.change}", "total")
                    .inf("total", 4)
            ])

        :param literal: A literal expression
        :param dst_key: Optional. Destination key in the record
        :param cast_vals: Optional. Convert the data in the recordset (JavaScript function or boolean)
        :param attrs: Optional. Extra data to be added to the record
        :param js_src_path: Optional. JavaScript file path
        :param records: Optional. Shortcut for the data reference used by this transformation
        :param verbose: Optional. Flag to display extra log messages
        """
        if cast_vals is True:
            cast_vals = "parseFloat"
        elif cast_vals is False:
            cast_vals = "false"
        return self.func(
            func_args={"literal": JsUtils.jsWrap("(function(rec){return `%s`})" % literal),
                       "convertFunc": JsUtils.jsWrap(cast_vals), "key": dst_key, "attrs": attrs},
            js_src_path=js_src_path, records=records, verbose=verbose)

    def pluck(self, column: Union[str, primitives.JsDataModel]) -> JsObjects.JsArray.JsArray:
        """A convenient version of what is perhaps the most common use-case for map: extracting a list of property
        values.

        `Underscorejs pluck <https://underscorejs.org/#pluck>`_

        :param column: The column / attribute in the JavaScript object
        """
        self.page.jsImports.add('underscore')
        column = JsUtils.jsConvertData(column, None)
        return JsObjects.JsArray.JsArray("_.pluck(%s, %s)" % (self.varName, column), page=self.page)


class DataFilters:
    """JavaScript data filters"""

    def __init__(self, js_code: str = None, filter_map: dict = None, page: primitives.PageModel = None):
        self.varName, self.__filters = js_code, OrderedSet()
        self.page, self.filter_map = page, filter_map

    def setData(self, data: Union[str, primitives.JsDataModel]):
        """Set the main dataset used for the transformations

        :param data: Data reference
        """
        self.varName = data
        return self

    def setPage(self, page: primitives.PageModel):
        """Set the page to improve performances by storing the functions only once.

        :param page: context / page object
        """
        self.page = page
        return self

    def setFilter(self, name: str) -> JsObjects.JsVoid:
        """

        :param name: The filter reference on the JavaScript side
        """
        self.filter_map[name] = self.toStr()
        return JsObjects.JsVoid("const %s = %s" % (name, self.filter_map[name]))

    def func(self, js_src_path: str = None, verbose: bool = None, func_name: str = None) -> str:
        """Generic function to register a filter function.
        Those functions can be used in any JavaScript fragments and they can be chained.

        :param js_src_path: Optional. JavaScript file path
        :param verbose: Optional. Flag to display extra log messages
        :param func_name: Optional. JavaScript function definition (if needs to be different from the filename)
        """
        if js_src_path is None:
            pname = sys._getframe().f_back.f_code.co_name
            fname = func_name or "Filter%s" % (pname[0].upper() + pname[1:])
            js_src_path = Path(__file__).parent / ".." / "js" / "native" / "flows" / ("%s.js" % fname)
        if self.page:
            return self.page.properties.js.add_from_file(str(js_src_path), category="constructor", verbose=verbose)[:-3]

        name = js_src_path.name[0].lower() + js_src_path.name[1:-3]
        with open(js_src_path) as fp:
            return "(function(r, attrs){%s; return %s(r, attrs)})" % (fp.read(), name)

    def call(self, js_src_path: str, args: dict = None, verbose: bool = None, func_name: str = None):
        """Custom call for a bespoke filter function.

        :param args: Optional.
        :param js_src_path: Optional. JavaScript file path
        :param verbose: Optional. Flag to display extra log messages
        :param func_name: Optional. JavaScript function definition (if needs to be different from the filename)
        """
        name = self.func(js_src_path, verbose, func_name=func_name)
        if args:
            largs = ["%s: %s" % (k, JsUtils.jsConvertData(v, None)) for k,v in args.items()]
            self.__filters.add("%s(%%s, {%s})" % (name, ",".join(largs)))
        else:
            self.__filters.add("%s(%%s)" % name)
        return self

    def match(self, data: Union[dict, primitives.JsDataModel], case_sensitive: bool = True, js_src_path: str = None,
              verbose: bool = None):
        """Filtering rule based on a Dictionary of lists.

        Usages::

            page.body.onReady([
                "let data = %s" % randoms.languages,
                page.js.console.log(ek.events.data.fltrs.setPage(page)
                    .match({"type": "Code"}, case_sensitive=False)
            ])

        :param data: The keys, values to be filtered
        :param case_sensitive: Optional. To make sure algorithm case-sensitive
        :param js_src_path: Optional. JavaScript file path
        :param verbose: Optional. Flag to display extra log messages
        """
        name = self.func(js_src_path, verbose)
        self.__filters.add("%s(%%s, {rules:%s, caseSensitive: %s})" % (
            name, JsUtils.jsConvertData(data, None), JsUtils.jsConvertData(case_sensitive, None)))
        return self

    def any(self, value: Any, keys: list = None, case_sensitive: bool = False, js_src_path: str = None,
            verbose: bool = None):
        """Check if any value in the record match the value.

        TODO: improve the performances by filtering on a list of keys if passed

        :param value: The value to keep
        :param keys: Optional. The list of keys to check
        :param js_src_path: Optional. JavaScript file path
        :param verbose: Optional. Flag to display extra log messages
        """
        name = self.func(js_src_path, verbose)
        value = JsUtils.jsConvertData(value, None)
        keys = JsUtils.jsConvertData(keys, None)
        self.__filters.add("%s(%%s, {value:%s, keys:%s, caseSensitive:%s})" % (
            name, value, keys, JsUtils.jsConvertData(case_sensitive, None)))
        return self

    def equal(self, key: str, value: Any, case_sensitive: bool = True, js_src_path: str = None,
              verbose: bool = None):
        """Filtering rule based on a key, value.

        Usage::

            select = page.ui.select(components.select.from_records(languages, column=filter_column))
            table = page.ui.tables.aggrid(languages)
            filter_data = DataJs(page).record(js_code="myData", data=languages)
            filt_grp = filter_data.filterGroup("test")
            select.change([table.js.setRowData(filt_grp.equal(filter_column, select.dom.content))])

            page.body.onReady([
                "let data = %s" % randoms.languages,
                page.js.console.log(ek.events.data.fltrs.setPage(page)
                    .equal("name", "c", case_sensitive=False)
            ])

        :param key: The key in the various records
        :param value: The value to keep
        :param case_sensitive: Optional. To make sure algorithm case-sensitive
        :param js_src_path: Optional. JavaScript file path
        :param verbose: Optional. Flag to display extra log messages
        """
        name = self.func(js_src_path, verbose)
        key = JsUtils.jsConvertData(key, None)
        value = JsUtils.jsConvertData(value, None)
        self.__filters.add("%s(%%s, {key:%s, value:%s, caseSensitive:%s})" % (
            name, key, value, JsUtils.jsConvertData(case_sensitive, None)))
        return self

    def includes(self, key: str, values: list, case_sensitive: bool = True, empty_all: bool = True,
                 js_src_path: str = None, verbose: bool = None):
        """Filtering rule based on a key, list of values.

        :param key: The key in the various records
        :param values: The list of values to keep
        :param case_sensitive: Optional. To make sure algorithm case-sensitive
        :param empty_all: Optional. To specify how to consider the empty case
        :param js_src_path: Optional. JavaScript file path
        :param verbose: Optional. Flag to display extra log messages
        """
        name = self.func(js_src_path, verbose)
        key = JsUtils.jsConvertData(key, None)
        values = JsUtils.jsConvertData(values, None)
        case_sensitive = JsUtils.jsConvertData(case_sensitive, None)
        empty_all = JsUtils.jsConvertData(empty_all, None)
        self.__filters.add("%s(%%s, {key: %s, values: %s, caseSensitive: %s, emptyAll: %s})" % (
            name, key, values, case_sensitive, empty_all))
        return self

    def startswith(self, key: str, value: str, case_sensitive: bool = True, js_src_path: str = None, verbose: bool = None):
        """Filtering rule based on a key, and a value starting with a specific format.

        :param key: The key in the various records
        :param value: The list of values to keep
        :param js_src_path: Optional. JavaScript file path
        :param verbose: Optional. Flag to display extra log messages
        """
        name = self.func(js_src_path, verbose)
        key = JsUtils.jsConvertData(key, None)
        value = JsUtils.jsConvertData(value, None)
        self.__filters.add("%s(%%s, {key:%s, value:%s, caseSensitive:%s})" % (
            name, key, value, JsUtils.jsConvertData(case_sensitive, None)))
        return self

    def sup(self, key: Union[str, primitives.JsDataModel], value: Union[float, primitives.JsDataModel],
            strict: bool = True, js_src_path: str = None, verbose: bool = None):
        """Filter values below a certain value.

        Usages::

            page.body.onReady([
                "let data = %s" % randoms.languages,
                page.js.console.log(ek.events.data.fltrs.setPage(page)
                    .sumCols(["rating", "change"], "total", case_sensitive=False)
                    .sup("total", 4)
            ])

        :param key: The key in the various records
        :param value: The threshold
        :param strict: Optional. Include threshold
        :param js_src_path: Optional. JavaScript file path
        :param verbose: Optional. Flag to display extra log messages
        """
        name = self.func(js_src_path, verbose, func_name="FilterNumbers")
        key = JsUtils.jsConvertData(key, None)
        value = JsUtils.jsConvertData(value, None)
        self.__filters.add("%s(%%s, {key:%s, value:%s, type: 'sup', strict:%s})" % (
            name, key, value, JsUtils.jsConvertData(strict, None)))
        return self

    def inf(self, key: Union[str, primitives.JsDataModel], value: Union[float, primitives.JsDataModel],
            strict: bool = True, js_src_path: str = None, verbose: bool = None):
        """Filter values above a certain value.

        Usages::

            page.body.onReady([
                "let data = %s" % randoms.languages,
                page.js.console.log(ek.events.data.fltrs.setPage(page)
                    .sumCols(["rating", "change"], "total", case_sensitive=False)
                    .inf("total", 4)
            ])

        :param key: The key in the various records
        :param value: The threshold
        :param strict: Optional. Include threshold
        :param js_src_path: Optional. JavaScript file path
        :param verbose: Optional. Flag to display extra log messages
        """
        name = self.func(js_src_path, verbose, func_name="FilterNumbers")
        key = JsUtils.jsConvertData(key, None)
        value = JsUtils.jsConvertData(value, None)
        self.__filters.add("%s(%%s, {key:%s, value:%s, type: 'inf', strict:%s})" % (
            name, key, value, JsUtils.jsConvertData(strict, None)))
        return self

    def group(self) -> DataAggregators:
        """Group a group for the data transformation.
        This will be defined in the Python but processed on the JavaScript side.

        Usage::

          js_data = page.data.js.record(js_code="myData", data=randoms.languages) # Create JavaScript data
          filter1 = js_data.filterGroup("filter1") # Add a filter object

          select.change([
              bar.build(filter1.group().sumBy(['rating', 'change'], select.dom.content), options={"x_axis": select.dom.content}),
              ...
          ])
        """
        return DataAggregators(self.toStr(), self.page)

    def sortBy(self, column: Union[str, primitives.JsDataModel]):
        """Returns a (stably) sorted copy of list, ranked in ascending order by the results of running each value
        through iterator. iterator may also be the string name of the property to sort by (eg: length).

        `Underscorejs sortBy <https://underscorejs.org/#sortBy>`_

        :param column: The key in the record to be used as key for sorting
        """
        self.page.jsImports.add('underscore')
        column = JsUtils.jsConvertData(column, None)
        self.__filters.add("_.sortBy(%%s, %s)" % column)
        return self

    def pivot(self, column: str, value: str, key: str, type: str = None, js_src_path: str = None,
              verbose: bool = None):
        """Pivot the data from rows (keys) to columns in the records.
        This should reduce the size of the record and it will make it usable in charts.

        Usages::

          page.js.fetch(data_urls.C02_DATA).csvtoRecords().get([
            page.js.console.log(page.data.js.record("data").filterGroup("test").pivot("country", "co2", "year"))
          ])

        :param column: The key in the record to be used as key for sorting
        :param value: The key in the record to be used as key for sorting
        :param key: Optional. The key used as pivot
        :param type: Optional int, or float or (fnc, alias)
        :param js_src_path: Optional. JavaScript file path
        :param verbose: Optional. Flag to display extra log messages
        """
        name = self.func(js_src_path, verbose, func_name="FilterNumbers")
        value = JsUtils.jsConvertData(value, None)
        column = JsUtils.jsConvertData(column, None)
        type = JsUtils.jsConvertData(type, None)
        key = JsUtils.jsConvertData(key, None)
        self.__filters.add("%s(%%s, {column: %s, value: %s, p: %s, convertFunc: %s})" % (
            name, column, value, key, type))
        return self

    def reduce(self, columns: List[str], add_missing_cols: bool = False, dflt: Any = None, js_src_path: str = None,
              verbose: bool = None):
        """Reduce the recordset to a defined set of columns.

        Usages::

            page.body.onReady([
                "let data = %s" % randoms.languages,
                page.js.console.log(ek.events.data.fltrs.setPage(page)
                    .reduce(['language', "rating", "Total"], add_missing_cols=True, dflt=0)
            ])

        :param columns: List of columns to set to the resulting recordset
        :param add_missing_cols: Optional. Flag to add columns which are not defined in the initial recordset
        :param dflt: Optional. The default value for the new columns
        :param js_src_path: Optional. JavaScript file path
        :param verbose: Optional. Flag to display extra log messages
        """
        name = self.func(js_src_path, verbose)
        columns = JsUtils.jsConvertData(columns, None)
        dflt = JsUtils.jsConvertData(dflt, None)
        self.__filters.add("%s(%%s, {columns: %s, addUndefined: %s, defaultValue: %s})" % (
            name, columns, json.dumps(add_missing_cols), dflt))
        return self

    def rename(self, names: List[tuple], keep_origin: bool = False, js_src_path: str = None, verbose: bool = None):
        """Rename certain columns in the recordset.
        This function will not reduce the records but only change / replace some keys

        Usages::

            page.body.onReady([
                "let data = %s" % randoms.languages,
                page.js.console.log(ek.events.data.fltrs.setPage(page)
                    .rename({"name": 'language'})
            ])

        :param names: Mapping with the new columns to give
        :param keep_origin: Optional. Keep the initial key to the recordset (only duplicate)
        :param js_src_path: Optional. JavaScript file path
        :param verbose: Optional. Flag to display extra log messages
        """
        name = self.func(js_src_path, verbose)
        lnames = []
        for k, v in names:
            if JsUtils.isJsData(k):
                k = "[%s]" % JsUtils.jsConvertData(k, None)
            lnames.append("%s: %s" % (k, JsUtils.jsConvertData(v, None)))
        self.__filters.add("%s(%%s, {names: {%s}, keepOrigin: %s})" % (name, ",".join(lnames), json.dumps(keep_origin)))
        return self

    @property
    def aggs(self) -> DataAggregators:
        """Property to be able to chain also aggregators"""
        return DataAggregators(page=self.page, chain=self.__filters, parent=self)

    def toStr(self) -> str:
        result = "%s"
        for rec in self.__filters[::-1]:
            result %= rec
        return result % self.varName


class DataGlobal:

    def __init__(self, js_code: str, data, page: primitives.PageModel = None):
        if data is not None:
            page._props["js"]["datasets"][js_code] = "var %s = %s" % (js_code, json.dumps(data))
        self._data, self.__filters_groups, self.page, self.varName = data, {}, page, js_code
        self.__filter_saved = {}

    def getFilter(self, name: str, group_name: str = None) -> DataFilters:
        """

        :param name: The filter alias name
        :param group_name: Optional. The filter group name
        """
        if group_name is None:
            saved_filter = None
            for k, v in self.__filter_saved.items():
                if name in v:
                    saved_filter = v
                    break

        else:
            if name not in self.__filter_saved[group_name]:
                raise NotImplementedError()

            saved_filter = self.__filter_saved[group_name]
        return DataFilters(name, saved_filter, self.page)

    def clearFilter(self, name: str, group_name: str = None):
        """

        :param name:
        :param group_name: Optional.
        """
        if group_name is None:
            for k, v in self.__filter_saved.items():
                if name in v:
                    del v[name]

        else:
            del self.__filter_saved[group_name][name]

        return self

    def filterGroup(self, group_name: str) -> DataFilters:
        """Create a JavaScript filtering group.

        Usage::

          js_data = page.data.js.record(js_code="myData", data=randoms.languages) # Create JavaScript data
          filter1 = js_data.filterGroup("filter1") # Add a filter object

        :param group_name: The filter name
        """
        if group_name not in self.__filters_groups:
            self.__filter_saved[group_name] = {}
            self.__filters_groups[group_name] = DataFilters(self.varName, self.__filter_saved[group_name], self.page)
        return self.__filters_groups[group_name]

    def cleafFilterGroup(self, group_name: str):
        """

        :param group_name: The filter name
        """
        if group_name not in self.__filters_groups:
            del self.__filters_groups[group_name]

        return self

    def clearFilters(self):
        """Remove all the filters."""
        self.__filters_groups = {}
        return self


class ServerConfig:

    def __init__(self, hostname: str, port: int, page: primitives.PageModel = None):
        self.js_code = "server_config_%s" % id(self)
        page._props["js"]["configs"][self.js_code] = self
        self.__namespaces, self.__end_points, self.host, self.port = {}, {}, hostname, port

    def getNamespace(self, alias: str):
        """Get the name space from its alias.

        :param alias: The name space alias.
        """
        return self.__namespaces[alias]

    def addNamespace(self, name: str, alias: str = None, end_points: list = None):
        """Add a JavaScript name space and its full end points and assigned it to a dedicated alias on the Python side.
        This will allow the Python to get the name space from its alias.

        :param name: The url name space
        :param alias: Optional. The alias for the entry point
        :param end_points: Optional. The endpoint routes
        """
        if alias is None:
            alias = name
        self.__namespaces[alias] = ServerNameSpaceConfig(self, name, alias, end_points)
        return self

    def endPoint(self, name: str, secured: bool = False):
        """Set the end point.

        :param name: The endpoint name
        :param secured:
        """
        if secured:
            self.__end_points[name] = "https://%s:%s/%s" % (self.host, self.port, name)
        else:
            self.__end_points[name] = "http://%s:%s/%s" % (self.host, self.port, name)
        return self

    def endPoints(self, names: List[str], secured: bool = False):
        """Set multiple end points.

        :param names: The end points names
        :param secured:
        """
        for name in names:
            if secured:
                self.__end_points[name] = "https://%s:%s/%s" % (self.host, self.port, name)
            else:
                self.__end_points[name] = "http://%s:%s/%s" % (self.host, self.port, name)
        return self

    def get(self, name: str) -> JsObjects.JsObject.JsObject:
        """Get the end point from its name.

        :param name: The end point name
        """
        if name not in self.__end_points:
            raise ValueError("Missing end point in the server configuration - %s" % name)

        return JsObjects.JsObject.JsObject.get(self.js_code)[name]

    def toStr(self) -> str:
        """ """
        for np, np_val in self.__namespaces.items():
            self.__end_points[np] = {'e': np_val.end_points, 'n': np_val.name, 'u': "http://%s:%s/%s" % (
                self.host, self.port, np_val.name)}
        return "var %s = %s" % (self.js_code, JsUtils.jsConvertData(self.__end_points, None))

    def __str__(self):
        return self.toStr()


class ServerNameSpaceConfig:
    def __init__(self, config: ServerConfig, name: str, alias: str, end_points: list):
        self.__config, self.end_points, self.name, self.alias = config, {}, name, alias
        if end_points is not None:
            self.endPoints(end_points)

    @property
    def address(self):
        """ """
        return JsObjects.JsObject.JsObject.get(self.__config.js_code)[self.alias]['u']

    def endPoint(self, name: str, secured: bool = False):
        """

        :param name:
        :param secured:
        """
        if secured:
            self.end_points[name] = "https://%s:%s/%s/%s" % (self.__config.host, self.name, self.__config.port, name)
        else:
            self.end_points[name] = "http://%s:%s/%s/%s" % (self.__config.host, self.name, self.__config.port, name)
        return self

    def endPoints(self, names: list):
        """

        :param names:
        """
        for name in names:
            self.endPoint(name)
        return self
