#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union, Any
from epyk.core.py import primitives
from epyk.core.py import types

from epyk.core.js.fncs import JsFncsRecords
from epyk.core.js.objects import JsChartD3
from epyk.core.js.primitives import JsObject
from epyk.core.js import JsUtils


class FncToObject:

    def __init__(self, data, js_src, data_schema=None):
        """

        :param data:
        :param js_src:
        :param data_schema:
        """
        self._js_src, self._data_schema, self._data = js_src, data_schema, data

    def __register_records_fnc(self, fnc_name: str, fnc_def, fnc_pmts: list = None):
        """
        This function will attach to the report object only the javascript functions used during the report.

        :param fnc_name: The JavaScript function name
        :param fnc_def: The JavaScript function definition
        :param fnc_pmts: The JavaScript function parameters
        """
        fnc_pmts = ["data"] + (fnc_pmts or [])
        if fnc_name not in self._js_src.get('js', {}).get('functions', {}):
            self._js_src.setdefault('js', {}).setdefault('functions', {})[fnc_name] = {
                'content': "var result = []; %s;return result" % JsUtils.cleanFncs(fnc_def), 'pmt': fnc_pmts}

    @property
    def d3(self):
        """ Data transformation to the D3 package. """
        return JsChartD3.JsChartD3Links(self._data, self._js_src, self._data_schema)

    @property
    def dc(self):
        """ Data transformation to the DC package. """
        from epyk.core.js.objects import JsChartDC

        return JsChartDC.JsChartDCLinks(self._data, self._js_src, self._data_schema)


class FncRoAggRec:

    def __init__(self, data, js_src, data_schema=None):
        self._js_src, self._data_schema, self._data = js_src, data_schema, data

    def __register_records_fnc(self, fnc_name: str, fnc_def, fnc_pmts: list = None):
        """
        This function will attach to the report object only the javascript functions used during the report.

        :param fnc_name:
        :param fnc_def:
        :param fnc_pmts: Optional.
        """
        fnc_pmts = ["data"] + (fnc_pmts or [])
        if fnc_name not in self._js_src.get('js', {}).get('functions', {}):
            self._js_src.setdefault('js', {}).setdefault('functions', {})[fnc_name] = {
                'content': "var result = []; %s;return result" % JsUtils.cleanFncs(fnc_def), 'pmt': fnc_pmts}


class FncOnRecords:

    def __init__(self, data, js_src, data_schema=None, profile: types.PROFILE_TYPE = False):
        self._js_src, self._data_schema, self._data, self.profile = js_src, data_schema, data, profile

    @property
    def o(self):
        """
        Property to the data final object.
        Those items help to the link to external packages.
        """
        return FncToObject(self._js_src, self._data_schema)

    def __register_records_fnc(self, fnc_name: str, fnc_def, fnc_pmts: list = None,
                               profile: types.PROFILE_TYPE = False):
        """
        This function will attach to the report object only the javascript functions used during the report.

        :param fnc_name:
        :param fnc_def:
        :param fnc_pmts: Optional.
        :param profile: Optional. A flag to set the component performance storage.
        """
        fnc_pmts = ["data"] + (fnc_pmts or [])
        if fnc_name not in self._js_src.get('js', {}).get('functions', {}):
            self._js_src.setdefault('js', {}).setdefault('functions', {})[fnc_name] = {
                'content': "var result = []; %s;return result" % JsUtils.cleanFncs(fnc_def), 'pmt': fnc_pmts}

    def custom(self, fnc_name: str, fnc_content, fnc_pmts: dict = None, profile: types.PROFILE_TYPE = False):
        """
        The function content should use data and produce an object record.

        :param fnc_name: A string for the Javascript function name.
        :param fnc_content: The javascript function content.
        :param fnc_pmts: Optional. The Javascript function parameters.
        :param profile: Optional. A flag to set the component performance storage.

        :return: "This" in order to allow the chains
        """
        self.__register_records_fnc(fnc_name, fnc_content, fnc_pmts, profile)
        return self

    def url(self):
        """ """
        fnc_name = JsFncsRecords.JsToUrl.__name__
        fnc_pmts = ["data"]
        for p in getattr(JsFncsRecords.JsToUrl, 'params', []):
            fnc_pmts.append(p)
        if self._js_src.get_function(fnc_name) is None:
            content = JsUtils.cleanFncs(JsFncsRecords.JsToUrl.value)
            self._js_src.add_function(fnc_name, js_funcs="%s; return result" % content, pmts=fnc_pmts)
        return fnc_name

    def count(self, keys, values=None, profile: types.PROFILE_TYPE = False):
        """
        The Javascript function are using the main data as a first parameter.

        If values is defined, the Javascript will aggregate the data based on the composite key and the values will be
        available in the record. Also the count will be displayed.
        The values will be one in the record and not the sum.

        :param keys: List | String. The column names.
        :param values: List. Optional. The values to keep in the result record.
        :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.

        :return: "This" to allow function chains
        """
        if not isinstance(keys, list):
            keys = [keys]

        if values is None:
            fnc_name = JsFncsRecords.JsCountAll.__name__
            self.__register_records_fnc(
                fnc_name, JsFncsRecords.JsCountAll.value, fnc_pmts=list(JsFncsRecords.JsCountAll.params))
            self._data_schema['fncs'].append("%s(%%s, %s)" % (fnc_name, keys))
        else:
            fnc_name = JsFncsRecords.JsCount.__name__
            self.__register_records_fnc(
                fnc_name, JsFncsRecords.JsCount.value, fnc_pmts=list(JsFncsRecords.JsCount.params))
            self._data_schema['fncs'].append("%s(%%s, %s, %s)" % (fnc_name, keys, values))
        return self._data

    def count_with_kpi(self, keys: Union[list, str], values, profile: types.PROFILE_TYPE = False):
        """

        :param keys: The column names.
        :param values: Optional. The values to keep in the result record.
        :param profile: Optional. A flag to set the component performance storage.
        """
        fnc_name = JsFncsRecords.JsCountSum.__name__
        self.__register_records_fnc(
            fnc_name, JsFncsRecords.JsCountSum.value, fnc_pmts=list(JsFncsRecords.JsCountSum.params))
        self._data_schema['fncs'].append("%s(%%s, %s, %s)" % (fnc_name, keys, values))
        return self._data

    def count_distinct(self, keys: Union[list, str], profile: types.PROFILE_TYPE = False):
        """

        :param keys: The column names.
        :param profile: Optional. A flag to set the component performance storage.

        :return: "This" to allow function chains
        """
        if not isinstance(keys, list):
            keys = [keys]
        fnc_name = JsFncsRecords.JsCountDistinct.__name__
        self.__register_records_fnc(
            fnc_name, JsFncsRecords.JsCountDistinct.value, fnc_pmts=list(JsFncsRecords.JsCountDistinct.params))
        self._data_schema['fncs'].append("%s(%%s, %s)" % (fnc_name, keys))
        return self._data

    def top(self, column: Union[str, primitives.JsDataModel], n: int = 1, order: str = 'desc',
            profile: types.PROFILE_TYPE = False):
        """
        The Javascript function are using the main data as a first parameter.

        :param column:
        :param n: Optional.
        :param order: Optional.
        :param profile: Optional. A flag to set the component performance storage.

        :return: "This" to allow function chains
        """
        column = JsUtils.jsConvertData(column, None)
        fnc_name = JsFncsRecords.JsTop.__name__
        self.__register_records_fnc(
            fnc_name, JsFncsRecords.JsTop.value, fnc_pmts=list(JsFncsRecords.JsTop.params))
        self._data_schema['fncs'].append("%s(%%s, %s, %s, '%s')" % (fnc_name, n, column, order))
        return self


class FncFiltere:

    def __init__(self, data, js_src, data_schema=None, profile: Union[dict, bool] = False):
        self._js_src, self._data_schema, self._data, self.profile = js_src, data_schema, data, profile
        fnc_name = JsFncsRecords.JsFilter.__name__
        fnc_pmts = ["data"] + (list(JsFncsRecords.JsFilter.pmts) or [])
        if fnc_name not in self._js_src.get('js', {}).get('functions', {}):
            self._js_src.setdefault('js', {}).setdefault('functions', {})[fnc_name] = {
                'content': "var result = []; %s;return result" % JsUtils.cleanFncs(
                    JsFncsRecords.JsFilter.content), 'pmt': fnc_pmts}
        self._data_schema['filters'] = []

    def custom(self, column: str, val: Any, compare_type: str, all_if_empty: bool = True):
        """

        :param column:
        :param val:
        :param compare_type:
        :param all_if_empty: Boolean. Optional.
        """
        filter_data = JsUtils.jsConvertData({
            "colName": column, "val": val, "op": compare_type, "allIfEmpty": all_if_empty}, None)
        self._data_schema['filters'].append(filter_data)
        return self._data

    def not_in_(self, column: str, val: Any):
        """

        #TODO: Think about the implementation
        """
        raise ValueError("Not implemented")

    def not_range_(self, column: str, val: Any, compare_type: str = "in", all_if_empty: bool = True):
        """

        :param column:
        :param val:
        :param compare_type: Optional.
        :param all_if_empty: Optional.
        """

    def in_(self, column: str, val: Any):
        """

        :param column:
        :param val:
        """
        return self.custom(column, val, "in", True)

    def range_(self, column: str, val: Any, strict_left: bool = False, strict_right: bool = False):
        """

        :param column:
        :param val:
        :param strict_left: Optional.
        :param strict_right: Optional.
        """
        if not strict_left:
            if not strict_right:
                return self.custom(column, val, "><=", True)

            return self.custom(column, val, "><", True)

        if not strict_right:
            if not strict_left:
                return self.custom(column, val, "=><", True)

            return self.custom(column, val, "><", True)

        return self.custom(column, val, "=><=", True)

    def eq_(self, column: str, val: Any):
        """

        :param column:
        :param val:
        """
        return self.custom(column, val, ">", True)

    def sup_(self, column: str, val: Any, strict: bool = False):
        """
        Filter only the data above the value for the given key in the record.

        :param column: The column name.
        :param val: The value in the dictionary.
        :param strict: Optional. A flag to specify if the value should be included.
        """
        if strict:
            return self.custom(column, val, ">", True)

        return self.custom(column, val, ">=", True)

    def inf_(self, column: str, val: Any, strict: bool = False):
        """
        Filter only the data below the value for the given key in the record.

        :param column: The column name.
        :param val: The value in the dictionary.
        :param strict: Optional. A flag to specify if the value should be included.
        """
        if strict:
            return self.custom(column, val, "<", True)

        return self.custom(column, val, "<=", True)


class JsRegisteredFunctions:

    def __init__(self, page: primitives.PageModel = None):
        self.page = page
        self._js_src = self.page.properties.js

    def cssStyle(self, params):
        """

        :param params:
        """
        self._js_src.setdefault('functions', {})["cssStyle"] = {
            'content': 'cssParams = []; for(var i in params){cssParams.push(i +":"+ params[i])}; return cssParams.join(";")',
            'pmt': ["params"]}
        return "cssStyle"

    def service(self):
        """
        Create and store a function to do simple services calls and return a temporary message.

        TODO: To be improved and extended.
        """
        self._js_src.setdefault('functions', {})["serviceCall"] = {
            'content': self.page.js.post(JsUtils.jsWrap("url"), {"data": JsUtils.jsWrap("data")}).onSuccess([
                self.page.js.msg.status()
            ]).toStr(),
            'pmt': ["url", "data"]}
        return "serviceCall"

    def anonymous(self, js_funcs: Union[str, list], pmts: dict = None):
        """
        Create a anonymous / lambda function.
        Those functions are directly called when they are defined.

        Related Pages:

          https://www.w3schools.com/js/js_function_definition.asp

        :param js_funcs: Javascript functions.
        :param pmts: Optional. The function parameters.
        """
        if pmts is None:
            return JsFunction("(function(){%s})()" % js_funcs)

        return JsFunction("(function(%s){%s})()" % (",".join(pmts), js_funcs))

    def get(self, func_name: str, *args):
        """
        Call a bespoke functions on the Javascript side.

        :param func_name: The function name.
        :param args: The different arguments in the function definition.

        :return: The Javascript sting
        """
        return "%s(%s)" % (func_name, ", ".join([str(JsUtils.jsConvertData(p, None)) for p in args]))

    def inline(self, func_name: str, js_funcs: Union[str, list], pmts: dict = None):
        """
        Create a name function which can be then called later.

        Related Pages:

          https://www.w3schools.com/js/js_function_definition.asp

        :param func_name: The function name.
        :param js_funcs: Javascript functions.
        :param pmts: Optional. The function parameters.

        :return: The function name which can be used in the Javascript
        """
        self._js_src.setdefault('functions', {})[func_name] = {
            'content': JsUtils.jsConvertFncs(js_funcs, toStr=True), 'pmt': pmts}
        return func_name

    @property
    def records(self):
        """
        Javascript pre-defined function dedicated to transform a records.
        Namely a list of dictionaries.
        """
        return FncOnRecords(None, self._js_src)


class JsFunction(primitives.JsDataModel):
    fncName = "lambda"

    def __init__(self, func: str):
        self.__strFnc = func

    def __str__(self):
        return self.__strFnc

    def toStr(self):
        return self.__strFnc


class JsFunctions(list):

    def __init__(self, funcs: Union[list, str]):
        if not isinstance(funcs, list):
            funcs = [funcs]
        self.__str_funcs = funcs

    def append(self, func: str):
        """

        :param func:
        """
        self.__str_funcs.append(func)

    def extend(self, funcs: list):
        """

        :param funcs:
        """
        self.__str_funcs.extend(funcs)

    def __add__(self, other):
        """
        Add two JavaScript expressions.

        :param other: A second expression
        :return: A new JavaScript expression
        """
        if hasattr(other, "toStr"):
            other = other.toStr()
        return JsFunctions("%s;%s" % (self.toStr(), other))

    def toStr(self):
        return "; ".join([s.toStr() if hasattr(s, 'toStr') else str(s) for s in self.__str_funcs])


_JSFNCS = 0


class JsLambda:

    def __init__(self):
        global _JSFNCS

        _JSFNCS += 1
        self.func_name = "function_%s" % _JSFNCS


class JsTypeOf:
    func_name = "typeof"

    def __init__(self, data):
        if self.func_name is None:
            raise ValueError("Private fncName variable should be defined for pre defined functions ")

        self.__jsArgs = [data]

    def __str__(self):
        return "%s(%s)" % (self.func_name, ", ".join([str(a) for a in self.__jsArgs]))


class JsAnonymous(primitives.JsDataModel):

    def __init__(self, js_funcs):
        self.__strFnc, self.__returnFnc, self.__paramsFnc = js_funcs, "", []

    def return_(self, value):
        """

        :param value:
        """
        self.__returnFnc = value
        return self

    def params(self, pmts: dict):
        """

        :param pmts: The function parameters.
        """
        self.__paramsFnc = pmts
        return self

    def call(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """
        _args = []
        if self.__paramsFnc:
            for a in list(args):
                _args.append(str(a))
            if kwargs:
                for i, p in enumerate(self.__paramsFnc):
                    if p in kwargs:
                        _args.append(str(kwargs[p]))
        return JsObject.JsObject("%s(%s)" % (self, ", ".join(_args)))

    def __str__(self):
        return "(function (%s) {%s; return %s})" % (", ".join(self.__paramsFnc), self.__strFnc, self.__returnFnc)

    def toStr(self):
        return str(self.__strFnc)
