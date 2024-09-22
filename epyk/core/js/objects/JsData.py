#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Optional, Union, List, Any
from epyk.core.py import primitives

from epyk.core.js.primitives import JsArray
from epyk.core.js.primitives import JsObject
from epyk.core.js.primitives import JsBoolean
from epyk.core.js.primitives import JsNumber
from epyk.core.js.primitives import JsString

from epyk.core.js.objects import JsNodeDom

from epyk.core.js.packages.JsVis import VisDataSet, VisDataView

from epyk.core.js.fncs import JsFncs
from epyk.core.js import JsUtils


class DataLoop:
    """Data Class used for all the loop and map in the Javascript side.
    This will get the below attributes

    val   : The current value in the loop
    index : The index item
    arr   : The full array (only available in case of arrays, map, filter, every  )
    """
    val, index, arr = JsObject.JsObject("value"), JsNumber.JsNumber("index", is_py_data=False), JsArray.JsArray("arr")


class DataReduce:
    """

    rVal  :
    val   :
    index :
    """
    rVal, val = JsObject.JsObject("r"), JsNumber.JsNumber("o", is_py_data=False)
    index = JsNumber.JsNumber("i", is_py_data=False)


class DataSort:
    """ """


class DataEach:
    """Data Class for the Jquery each loop

    index : index
    data  : element
    """
    index, data = JsNumber.JsNumber("index", is_py_data=False), JsObject.JsObject("data", is_py_data=False)


class DataAll:
    """Data Class for the Jquery each loop

    index : index
    data  : elt
    """
    index, element = JsNumber.JsNumber("index", is_py_data=False), JsNodeDom.JsDoms.get(js_code="elt")


class ContainerData:

    def __init__(self, page: primitives.PageModel, schema: dict = None):
        self.page, self._schema = page, schema

    @property
    def fnc(self):
        """All the predefined transformation functions"""
        return JsFncs.FncOnRecords(self.page._props, self._schema)

    @property
    def to(self):
        """All the possible object transformation to deal with external packages"""
        return JsFncs.FncToObject(self.page._props, self._schema)

    @property
    def filter(self):
        """  """
        return JsFncs.FncFiltere(self, self.page._props, self._schema)


class RawData(primitives.JsDataModel):

    def __init__(self, page: primitives.PageModel, records=None, profile: bool = False):
        self.page = page
        self._data_id = self.page.properties.data.add(records, [])

    @classmethod
    def get(cls, page: primitives.PageModel, js_code: str):
        """Return the internal RawData object.

        :param page: The main page object.
        :param js_code: The JavaScript variable name.

        :return: A internal data object
        """
        return RawData(page, None)

    def setId(self, jq_id: str = None):
        """Change the Id variable name for the javascript data source.

        :param jq_id: The JQuery Identifier.

        :return: The Python object
        """
        self.jqId = jq_id if jq_id is not None else self._jqId
        return self

    def attach(self, component: primitives.HtmlModel, profile: Optional[Union[bool, dict]] = False):
        """Attach the data object to a HTML Object.

        This function is automatically used in the different components in order
        to guarantee the link of the data. This will also ensure that the same data set will be store only once in the page

        :param component: An HTML component to be linked to
        :param profile: Optional. Activate the profiling features
        """
        self.page.properties.data.get_schema_containers(self._data_id)[component.htmlCode] = {
            'fncs': [], 'outs': None, "profile": profile}
        return ContainerData(self.page, self._data["schema"][self._data_id]['containers'][component.htmlCode])

    def toTsv(self, col_names: list = None, profile: Optional[Union[bool, dict]] = False):
        """

        :return: A String with the Javascript function to be used
        """
        col_names = col_names or self.page.properties.data.schema.columns
        js_funcs = self.page._props.setdefault('js', {}).setdefault('functions', {})
        if "ToTsv" in js_funcs:
            js_funcs["ToTsv"] = {'content': '''var result = []; var tmp = []; var row = [];
                colNames.forEach(function(col){row.push(col)}); tmp.push(row.join('\t'));
                data.forEach(function(rec){
                  row = []; colNames.forEach(function(col){row.push(rec[col])});
                  tmp.push(row.join('\t'))}); result = tmp.join('\\n'); return result''', 'pmt': col_names}
        return "ToTsv(%s, %s)" % (self.jqId, col_names)

    @property
    def fnc(self):
        """ """
        return JsFncs.FncOnRecords(self, self.page._props, self._schema)

    @property
    def filter(self):
        """ """
        return JsFncs.FncFiltere(self, self.page._props, self._schema)

    @property
    def to(self):
        """ """
        return JsFncs.FncToObject(self, self.page._props, self._schema)

    def toStr(self):
        data = "data_%s" % self._data_id
        # Add the different javascript transformation functions
        for fnc in self._schema.get('fncs', []):
            data = fnc % data
        # Add the global filtering rules
        if len(self._schema.get("filters", [])) > 0:
            data = "%s(%s, [%s])" % ("JsFilter", data, ",".join(self._schema['filters']))
        # Add the final output object transformation
        if self._schema.get('out', None) is not None:
            data = self._schema['out'] % data
        return data


class Datamap(primitives.JsDataModel):

    def __init__(self, components: List[primitives.HtmlModel] = None, attrs: dict = None):
        self._data, self.__post_process = [], []
        if components is not None:
            for c in components:
                if isinstance(c, tuple):
                    self.attr(c[1], c[0].dom.content)
                else:
                    self.add(c)
        if attrs is not None:
            for k, v in attrs.items():
                self.attr(k, v)

    def add(self, component: primitives.HtmlModel, html_code: str = None, is_json: bool = True):
        """Add an HTML component to the object.

        The key will be the html_code. If the format is not Json it will convert all data the Json string object.

        :param component: The HTML component.
        :param html_code: Optional. The Html code.
        :param is_json: Optional. Flag to specify the data format. Default Json so True.
        """
        if is_json:
            if component.__class__.__name__ == "InputFile":
                if component.options.multiple:
                    self.__post_process.append(
                        "Array.from(%s).forEach(function(f, i){mapToFormData.append('%s['+ i +']', f)})" % (
                            component.dom.files.toStr(), component.ref))
                else:
                    self._data.append(
                        (html_code or component.attr["name"], JsUtils.jsConvertData(component.dom.files[0], None)))
            else:
                self._data.append((html_code or component.ref, JsUtils.jsConvertData(component.dom.content, None)))
        else:
            self._data.append((
                JsUtils.jsConvertData(html_code or component.ref, None),
                JsUtils.jsConvertData(component.dom.content.stringify(), None)))
        return self

    def attr(self, k: Union[str, primitives.JsDataModel], v: Any):
        """Add a key, value to the Datamap object. Keys and value might be JavaScript objects.

        :param k: The key attribute to be added to the object.
        :param v: The value associated to the key.
        :return: Self to allow the chaining
        """
        self._data.append((JsUtils.jsConvertData(k, None), JsUtils.jsConvertData(v, None)))
        return self

    def attrs(self, data: dict):
        """Add multiple attributes to the DataMap object.

        :param data: All the attributes to attach
        :return: Self to allow the chaining
        """
        for k, v in data.items():
            self.attr(k, v)
        return self

    def toStr(self) -> str:
        return "{%s}" % ",".join(["%s: %s" % (k, v) for k, v in self._data])

    def toUrl(self):
        """Convert object to an url string"""
        from epyk.core.js.primitives import JsString

        return JsString.JsString.get('''(function(data){let urlParts = []; for (
const [key, value] of Object.entries(data)){urlParts.push(key +"="+ value);};return encodeURI(urlParts.join("&"))})(%s)''' % self.toStr())

    def get(self, value: Union[str, primitives.JsDataModel], dfl=None):
        """

        :param value:
        :param dfl:
        :return:
        """
        return JsObject.JsObject.get(
            "{%s}[%s]" % (",".join(["%s: %s" % (k, v) for k, v in self._data]), JsUtils.jsConvertData(value, None)))

    def update(self, attrs: dict):
        """Direct update of the object attributes.

        :param attrs: A dictionary with the attributes to add
        :return: The object to allow the chaining.
        """
        self.attrs(attrs)
        return self

    def toStrFormData(self) -> str:
        """ Change the object to a FormData object.

        :return: A string with the FormData entire definition.
        """
        str_frgs = []
        for k, v in self._data:
            str_frgs.append("mapToFormData.append(%s, %s)" % (JsUtils.jsConvertData(k, None), v))
        if self.__post_process:
            str_frgs.extend(self.__post_process)
        return "(function(){let mapToFormData = new FormData(); %s; return mapToFormData})()" % ";".join(str_frgs)

    def __str__(self):
        return self.toStr()


class FormData(primitives.JsDataModel):
    alias = None

    def new(self, js_code: str, var_type: str = "let"):
        """Define a JavaScript variable.

        :param js_code: The JavaScript variable name.
        :param var_type: The JavaScript variable type (let, const, var...)
        """
        self.alias = js_code
        return "%s %s = new FormData()" % (var_type, js_code)

    def get(self, js_code: str):
        """Get a JavaScript variable.

        :param js_code: The JavaScript variable name.
        """
        self.alias = js_code
        return self

    def append(self, name: Union[str, primitives.JsDataModel], value: Any):
        """Append an item to the FormData object.

        :param name: The item name
        :param value: The item value
        """
        return "%s.append(%s, %s)" % (
            self.alias, JsUtils.jsConvertData(name, None), JsUtils.jsConvertData(value, None))

    def add(self, component: primitives.HtmlModel, html_code: str = None):
        """Add an HTML component to the object. The key will be the html_code.

        :param component: The HTML component.
        :param html_code: Optional. The Html code.
        """
        return "%s.append(%s, %s)" % (
            self.alias, JsUtils.jsConvertData(html_code or component.htmlCode, None),
            JsUtils.jsConvertData(component.dom.content, None))

    def update(self, attrs: Union[Datamap, dict]):
        """

        :param attrs:
        """
        appends = []
        if isinstance(attrs, Datamap):
            for k, v in attrs._data:
                appends.append(self.append(k, v))
        else:
            for k, v in attrs.items():
                appends.append(self.append(k, JsUtils.jsConvertData(v, None)))
        return appends

    def toStr(self) -> str:
        return self.alias


class JsData:

    def __init__(self, page: primitives.PageModel, component: primitives.HtmlModel = None):
        self.page, self.component = page, component

    def loop(self):
        return DataLoop()

    def reduce(self):
        return DataReduce()

    def sort(self):
        return DataSort()

    def each(self):
        return DataEach()

    @property
    def all(self):
        return DataAll()

    def crossfilter(self, data=None, js_code: str = None, cross_dimension=None):
        """A crossfilter represents a multi-dimensional dataset.

        Constructs a new crossfilter. If records is specified, simultaneously adds the specified records.
        Records can be any array of JavaScript objects or primitives.

        Related Pages:

          https://github.com/crossfilter/crossfilter/wiki/API-Reference

        :param data:
        :param js_code:
        :param cross_dimension:
        """
        from epyk.core.js.packages.JsCrossFilter import CrossFilter

        if data is None:
            data = "%s.top(Infinity)" % cross_dimension.toStr()

        if js_code is None:
            return CrossFilter(page=self.page, data=data, set_var=False)

        return CrossFilter(page=self.page, js_code=JsUtils.getJsValid(js_code), data=data)

    @property
    def formdata(self):
        """Create a JavaScript Formdata object.

        The FormData interface provides a way to easily construct a set of key/value pairs representing form fields and
        their values, which can then be easily sent using the XMLHttpRequest.send() method.
        It uses the same format a form would use if the encoding type were set to "multipart/form-data".

        Related Pages:

          https://developer.mozilla.org/en-US/docs/Web/API/FormData
        """
        return FormData()

    def datamap(self, components: List[primitives.HtmlModel] = None, attrs: dict = None):
        """Create a bespoke data object dedicated to be converted to Json and passed to the JavaScript layer.
        This is an internal structure to link the HTML component and various object to the JavaScript definition.
        """
        return Datamap(components, attrs)

    def dataset(self, data: Any, js_code: str = None, options: Union[dict, primitives.JsDataModel] = None):
        """One of the starting points of the visualizations of vis.js is that they can deal with dynamic data,
        and allow manipulation of the data.
        To enable this, vis.js includes a flexible key/value based DataSet and DataView to handle unstructured JSON data.

        Related Pages:

          https://visjs.github.io/vis-data/data/index.html

        :param data: The data to be passed to the JavaScript side.
        :param js_code: The variable reference to this object on the JavaScript side.
        :param options: The options to be added to this object.
        """
        vis_obj = VisDataSet(self.page, data=data, js_code=JsUtils.getJsValid(js_code))
        if options is not None:
            vis_obj.setOptions(options)
        return vis_obj

    def dataview(self, dataset, var_name: str = None, options: Union[dict, primitives.JsDataModel] = None):
        """A DataView offers a filtered and/or formatted view on a DataSet.
        One can subscribe to change in a DataView, and easily get filtered or formatted data without having to specify
        filters and field types all the time.

        Viz.Js module

        Related Pages:

          https://visjs.github.io/vis-data/data/dataview.html

        :param dataset:
        :param options:
        :param var_name:
        """
        vis_obj = VisDataView(self.page, data=dataset.varId, js_code=JsUtils.getJsValid(var_name))
        if options is not None:
            vis_obj.setOptions(options)
        return vis_obj

    def records(self, data: Any):
        """

        :param data:
        """
        return RawData(self.page, data)

    @property
    def null(self):
        """Javascript null reference"""
        return JsObject.JsObject("null", is_py_data=False)


class JsDataTransfer:

    def __init__(self, js_code: str):
        self.varId = js_code

    @property
    def text(self):
        """Get text data from a datatransfer object"""
        return JsString.JsString("%s.getData('text')" % self.varId, is_py_data=False)

    @property
    def files(self):
        """The DataTransfer.files property is a list of the files in the drag operation. If the operation includes no files,
        the list is empty.

        This feature can be used to drag files from a user's desktop to the browser.

        Related Pages:

          https://developer.mozilla.org/en-US/docs/Web/API/DataTransfer/files
        """
        return JsArray.JsArray.get("%s.files" % self.varId)

    @property
    def dropEffect(self, flag: Union[bool, primitives.JsDataModel] = False):
        """

        Related Pages:

          https://developer.mozilla.org/en-US/docs/Web/API/DataTransfer/dropEffect
        """
        if flag == False:
            return JsBoolean.JsBoolean("%s.dropEffect" % self.varId)

        if flag not in [None, 'move', 'link', 'copy']:
            raise ValueError("")

        flag = JsUtils.jsConvertData(flag, None)
        return JsFncs.JsFunction("%s.dropEffect = %s" % (self.varId, flag))

    @property
    def effectAllowed(self, flag: Union[bool, primitives.JsDataModel] = False):
        """

        Related Pages:

          https://developer.mozilla.org/en-US/docs/Web/API/DataTransfer/effectAllowed
        """
        if flag == False:
            return JsBoolean.JsBoolean("%s.effectAllowed" % self.varId)

        if flag not in [None, 'move', 'link', 'copy']:
            raise ValueError("")

        flag = JsUtils.jsConvertData(flag, None)
        return JsFncs.JsFunction("%s.effectAllowed = %s" % (self.varId, flag))

    def clearData(self, data_type: Union[str, primitives.JsDataModel] = None):
        """Remove the data associated with a given type. The type argument is optional.
        If the type is empty or not specified, the data associated with all types is removed.
        If data for the specified type does not exist, or the data transfer contains no data, this method will have no
        effect.

        Related Pages:

          https://developer.mozilla.org/en-US/docs/Web/API/DataTransfer/clearData
        """
        if data_type is None:
            return JsFncs.JsFunction("%s.clearData()" % self.varId)

        return JsFncs.JsFunction("%s.clearData(%s)" % (self.varId, JsUtils.jsConvertData(data_type, None)))

    def setDragImage(self):
        """ """

    def setData(self, data: Any, data_type: Union[str, primitives.JsDataModel] = 'text'):
        """

        :param data:
        :param data_type:
        """
        data_type = JsUtils.jsConvertData(data_type, None)
        data = JsUtils.jsConvertData(data, None)
        return JsFncs.JsFunction("%s.setData(%s, %s)" % (self.varId, data_type, data))

    def getData(self, data_type: Union[str, primitives.JsDataModel] = "text"):
        """

        :param data_type:
        """
        data_type = JsUtils.jsConvertData(data_type, None)
        return JsString.JsString("%s.getData(%s)" % (self.varId, data_type), is_py_data=False)


class JsClipboardData:

    def __init__(self, js_code: str):
        self.varId = js_code

    def src(self, js_code: str):
        """Set the event source. By default the event is event but this can be changed according to the trigger event.

        :param js_code: Change the event source
        """
        self.varId = "%s.clipboardData" % js_code
        return self

    @property
    def text(self):
        """The DataTransfer.getData() method retrieves drag data (as a DOMString) for the specified type.
        If the drag operation does not include data, this method returns an empty string

        Related Pages:

          https://developer.mozilla.org/en-US/docs/Web/API/DataTransfer/getData
        """
        return JsString.JsString("%s.getData('text')" % self.varId, is_py_data=False)

    @property
    def plain(self):
        """The DataTransfer.getData() method retrieves drag data (as a DOMString) for the specified type.
        If the drag operation does not include data, this method returns an empty string

        Related Pages:

          https://developer.mozilla.org/en-US/docs/Web/API/DataTransfer/getData
        """
        return JsString.JsString("%s.getData('text/plain')" % self.varId, is_py_data=False)

    @property
    def uri(self):
        """The DataTransfer.getData() method retrieves drag data (as a DOMString) for the specified type.
        If the drag operation does not include data, this method returns an empty string

        Related Pages:

          https://developer.mozilla.org/en-US/docs/Web/API/DataTransfer/getData
        """
        return JsString.JsString("%s.getData('text/uri-list')" % self.varId, is_py_data=False)

    def getData(self, data_type: str):
        """The DataTransfer.getData() method retrieves drag data (as a DOMString) for the specified type.
        If the drag operation does not include data, this method returns an empty string

        Example data types are text/plain and text/uri-list.

        Related Pages:

          https://developer.mozilla.org/en-US/docs/Web/API/DataTransfer/getData

        :param data_type: The data format
        """
        data_type = JsUtils.jsConvertData(data_type, None)
        return JsString.JsString("%s.getData(%s)" % (self.varId, data_type), is_py_data=False)
