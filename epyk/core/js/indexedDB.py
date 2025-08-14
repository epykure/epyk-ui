from typing import Union, Optional, List
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects

# https://medium.com/@kamresh485/indexeddb-tutorial-for-beginners-a-comprehensive-guide-with-coding-examples-74df2914d4d5


class Query:

    def __init__(self, value: str):
        self.value = value
        self._js = []

    def onerror(self, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = False):
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        js_data = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
        self._js.append("request.onerror = event => {let data = event.target.errorCode; %s}" % js_data)
        return self

    def onsuccess(self, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = False):
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        js_data = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
        self._js.append("request.onsuccess = event => {let data = event.target.result; %s}" % js_data)
        return self

    def toStr(self) -> str:
        return JsUtils.jsConvertData(self._js, None)


class Index:

    def __init__(self, value: str):
        self.value = value

    def get(self, values: list):
        values = JsUtils.jsConvertData(values, None)
        return Query


class OpenCursor:

    def onerror(self, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = False):
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        js_data = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
        self._js.append("request.onerror = event => {let data = event.target.errorCode; %s}" % js_data)
        return self

    def onsuccess(self, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = False):
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        js_data = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
        self._js.append("request.onsuccess = event => {let data = event.target.result; %s}" % js_data)
        return self


class ObjectStore:

    def __init__(self, value: str, db: str, js_code: str = None):
        self.db_code = db
        self.js_code = js_code or "store%s" % db

    def createIndex(self, name: str, columns: List[str], options: dict = None) -> JsObjects.JsObject.JsObject:
        name = JsUtils.jsConvertData(name, None)
        columns = JsUtils.jsConvertData(columns, None)
        if options:
            options = JsUtils.jsConvertData(options, None)
            return JsObjects.JsObject.JsObject.get("%s.createIndex(%s, %s, %s)" % (self.js_code, name, columns, options))

        return JsObjects.JsObject.JsObject.get("%s.createIndex(%s, %s)" % (self.js_code, name, columns))

    def index(self, name: str) -> Index:
        name = JsUtils.jsConvertData(name, None)
        return Index("store.index(%s)" % name)

    def delete(self, index: int) -> Query:
        return Query("%s.delete(%s)" % (self.js_code, index))

    def get(self, index: int) -> Query:
        return Query("%s.get(%s)" % (self.js_code, index))

    def put(self, rec: dict):
        rec = JsUtils.jsConvertData(rec, None)
        return JsUtils.jsWrap("%s.put(%s)" % (self.js_code, rec))

    def add(self, rec: dict) -> Query:
        rec = JsUtils.jsConvertData(rec, None)
        return Query("%s.add(%s)" % (self.js_code, rec))

    def openCursor(self) -> OpenCursor:
        return OpenCursor("%s.openCursor()" % self.js_code)


class Transaction:

    def __init__(self, name: str, db: str, readwrite: bool = True, js_code: str = None):
        if readwrite:
            self._js = ["%s.transaction(%s, 'readwrite')" % (db, name)]
        else:
            self._js = ["%s.transaction(%s, 'readonly')" % (db, name)]
        self.db_code = db

    def onerror(self, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = False):
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        js_data = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
        self._js.append("request.onerror = event => {let data = event.target.errorCode; %s}" % js_data)
        return self

    def oncomplete(self, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = False):
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        js_data = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
        self._js.append("request.oncomplete = event => {let data = event.target.result; %s}" % js_data)
        return self

    def abort(self) -> JsUtils.jsWrap:
        return JsUtils.jsWrap("abort()")

    def objectStore(self, name: str = None) -> ObjectStore:
        return ObjectStore("", db=self.db_code)


class DbResult:

    def __init__(self, js_code: str):
        self.js_code = "%s.result" % js_code
        self.db_code = js_code

    def createObjectStore(self, name: str, schema: dict) -> ObjectStore:
        name = JsUtils.jsConvertData(name, None)
        schema = JsUtils.jsConvertData(schema, None)
        return ObjectStore("%s.createObjectStore(%s, %s)" % (self.js_code, name, schema), self.db_code)

    def transaction(self, name: str, readwrite: bool = True) -> Transaction:
        name = JsUtils.jsConvertData(name, None)
        return Transaction(name=name, db=self.db_code, readwrite=readwrite)


class IndexedDB:

    def __init__(self, value: str, js_code: str):
        self.js_code = js_code
        self._js = ["var %s = %s" % (js_code, value)]

    @property
    def db(self) -> DbResult:
        return DbResult(self.js_code)

    def onerror(self, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = False):
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        js_data = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
        self._js.append("request.onerror = event => {let data = event.target.errorCode; %s}" % js_data)
        return self

    def onsuccess(self, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = False):
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        js_data = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
        self._js.append("request.onsuccess = event => {let data = event.target.result; %s}" % js_data)
        return self

    def onupgradeneeded(self, js_funcs: Union[list, str], profile: Optional[Union[dict, bool]] = False):
        if not isinstance(js_funcs, list):
            js_funcs = [js_funcs]
        js_data = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
        self._js.append("request.onupgradeneeded = event => {let data = event.target.result; %s}" % js_data)
        return self

    def toStr(self) -> str:
        return JsUtils.jsConvertData(self._js, None)


def open(name: str, version: int = 1, js_code: Optional[str] = None) -> IndexedDB:
    """create and open a database with the following code"""
    name = JsUtils.jsConvertData(name, None)
    return IndexedDB("window.indexedDB.open(%s, %s)" % (name, version), js_code or ("%sDB" % name))


def create_table(name: str, db_code: str) -> JsUtils.jsWrap:
    idb = open(db_code)
    db_store = idb.db.createObjectStore(name)


def set_data(data: List[dict], table_name: str, db_code: str):
    columns = []
    if data:
        columns = list(data[0].keys())
    create_table(name=table_name, db_code=db_code, columns=columns)


def get_data():
    idb = open(db_code)
    idb.db.transaction(readwrite=False)
