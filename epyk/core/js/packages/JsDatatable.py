"""
Javascript Interface to the Datatable Module

https://datatables.net/reference/api/
"""

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects
from epyk.core.js.packages import JsQuery
from epyk.core.js.packages import JsPackage


class SelectAPI(JsPackage):
  """

  """

  def blurable(self):
    """
    Get the blurable state for the table

    Documentation
    https://datatables.net/reference/api/select.blurable()

    :return:
    """
    return JsObjects.JsBoolean.JsBoolean("%s.blurable()" % self._selector)

  def info(self, jsFlag=None):
    """
    Get / set the information summary display state.

    Documentation
    https://datatables.net/reference/api/select.info()

    :param jsFlag: Value to set for the information summary display state - true to enable, false to disable.
    :return:
    """
    if jsFlag is None:
      return JsObjects.JsBoolean.JsBoolean("%s.info()" % self._selector)

    return JsObjects.JsObject.JsObject("%s.info(%s)" % (self._selector, JsUtils.jsConvertData(jsFlag, None)))

  def items(self):
    """
    Get / set the items that Select will select based on user interaction (rows, columns or cells).

    Documentation
    https://datatables.net/reference/api/select.items()

    :return:
    """
    return JsObjects.JsString.JsString("%s.items()" % self._selector)

  def selector(self):
    """
    Get the current item selector string applied to the table.

    Documentation
    https://datatables.net/reference/api/select.selector()

    :return:
    """
    return JsObjects.JsString.JsString("%s.selector()" % self._selector)

  def style(self):
    """
    Get / set the style by which the end user can select items in the table.

    Documentation
    https://datatables.net/reference/api/select.style()

    :return:
    """
    return JsObjects.JsString.JsString("%s.style()" % self._selector)


class CellAPI(JsPackage):
  lib_alias = {'js': "datatables", 'css': 'datatables'}
  lib_selector = 'cell'
  lib_set_var = False

  def deselect(self):
    """
    Deselect a single cell

    Documentation
    https://datatables.net/reference/api/column().deselect()

    :return: DataTables API instance for chaining
    """
    return self.fnc("deselect()")

  def select(self):
    """
    Select a single cell

    Documentation
    https://datatables.net/reference/api/cell().select()

    :return: DataTables API instance for chaining
    """
    return self.fnc("select()")

  def render(self):
    """
    Get rendered data for a cell

    Documentation
    https://datatables.net/reference/api/cell().render()

    :return: DataTables API instance for chaining
    """
    return self.fnc("render()")

  def node(self):
    """
    Get the DOM element for the selected cell

    Documentation
    https://datatables.net/reference/api/cell().node()

    :return: DataTables API instance for chaining
    """
    self.fnc("node()")

  def jquery_nodes(self):
    """
    Get the cell nodes for the selected column.

    Documentation
    https://datatables.net/reference/api/column().nodes()

    :return:
    """
    self.nodes()
    self._js.append("nodes().to$()")
    return JsQuery.JQuery(jqId=self.toStr())

  def invalidate(self):
    """
    Invalidate the data held in DataTables for the selected cells

    Documentation
    https://datatables.net/reference/api/cell().invalidate()

    :return: DataTables API instance for chaining
    """
    return self.fnc("invalidate()")

  def index(self):
    """
    Get index information about the selected cell

    Documentation
    https://datatables.net/reference/api/cell().index()

    :return:
    """
    return JsObjects.JsNumber.JsNumber("%s.index()" % self.getStr())

  def cache(self):
    """
    Get cached data of the cache type specified

    Documentation
    https://datatables.net/reference/api/cell().cache()

    :return:
    """

  def data(self):
    """
    Get / set data for the selected cell.

    Documentation
    https://datatables.net/reference/api/cell().data()

    :return:
    """
    return self.fnc("data()")

  def focus(self):
    """
    Focus on a cell.

    Documentation
    https://datatables.net/reference/api/cell().focus()

    :return:
    """
    return self.fnc("focus()")

  def blur(self):
    """
    Blur focus from the table.

    Documentation
    https://datatables.net/reference/api/cell.blur()

    :return:
    """
    return self.fnc("blur()")


class ColumnAPI(JsPackage):
  lib_alias = {'js': "datatables", 'css': 'datatables'}
  lib_selector = 'column'
  lib_set_var = False

  def deselect(self):
    """
    Deselect a single column

    Documentation
    https://datatables.net/reference/api/column().deselect()

    :return: DataTables API instance for chaining
    """
    return self.fnc("deselect()")

  def select(self):
    """
    Select a single column

    Documentation
    https://datatables.net/reference/api/column().select()

    :return: DataTables API instance for chaining
    """
    self.fnc("select()")

  def cache(self):
    """
    Get the DataTables cached data for the selected column.

    Documentation
    https://datatables.net/reference/api/column().cache()

    :return:
    """

  def data(self):
    """
    Get the data for the cells in the selected column.

    Documentation
    https://datatables.net/reference/api/column().data()

    :return:
    """
    return self.fnc("data()")

  def dataSrc(self):
    """
    Get the data source property for the selected column.

    Documentation
    https://datatables.net/reference/api/column().dataSrc()

    :return:
    """

  def footer(self):
    """
    Get the footer node for the selected column.

    Documentation
    https://datatables.net/reference/api/column().footer()

    :return:
    """

  def header(self):
    """
    Get the header node for the selected column.

    Documentation
    https://datatables.net/reference/api/column().header()

    :return:
    """

  def index(self):
    """
    Get the column index of the selected column.

    Documentation
    https://datatables.net/reference/api/column().index()

    :return:
    """
    return JsObjects.JsNumber.JsNumber("%s.index()" % self.getStr())

  def nodes(self):
    """
    Get the cell nodes for the selected column.

    Documentation
    https://datatables.net/reference/api/column().nodes()

    :return:
    """
    self._js.append("nodes()")
    return self

  def jquery_nodes(self):
    """
    Get the cell nodes for the selected column.

    Documentation
    https://datatables.net/reference/api/column().nodes()

    :return:
    """
    self.nodes()
    self._js.append("to$()")
    return JsQuery.JQuery(jqId=self.toStr())

  def order(self):
    """
    Order the table by the selected column.

    Documentation
    https://datatables.net/reference/api/column().order()

    :return:
    """

  def search(self, jsData):
    """
    Search for data in the selected column.

    Documentation
    https://datatables.net/reference/api/column().search()

    :return:
    """
    return self.fnc("search(%s)" % JsUtils.jsConvertData(jsData, None))

  def visible(self):
    """
    Get / set the visibility of a single selected column.

    Documentation
    https://datatables.net/reference/api/column().visible()

    :return: DataTables API instance for chaining
    """
    return self.fnc("visible()")

  def draw(self, target=None):
    """
    Redraw the DataTables in the current context, optionally updating ordering, searching and paging as required.

    Documentation
    https://datatables.net/reference/api/draw()

    :return: DataTables API instance for chaining
    """
    if target is not None:
      return self.fnc("draw(%s)" % JsUtils.jsConvertData(target, None))

    return self.fnc("draw()")


class RowChildAPI(JsPackage):
  lib_selector = 'child'
  lib_set_var = False

  def remove(self):
    pass

  def show(self):
    pass

  def hide(self):
    """
    Hide the child row(s) of a parent row.

    Documentation
    https://datatables.net/reference/api/row().child.hide()

    :return:
    """
    return self.fnc("hide()")

  def isShown(self):
    pass


class RowAPI(JsPackage):
  lib_alias = {'js': "datatables", 'css': 'datatables'}
  lib_selector = 'row'
  lib_set_var = False

  def _mapVarId(self, strFnc, varId):
    """
    Change the varIs for row.add.
    This is done at class level and not object level on the Javascript side

    This mapping is done according to the Package API definition

    Documentation
    https://datatables.net/reference/api/

    :param strFnc: The function string
    :param varId: The object reference for the Javascript side

    :return: The object reference on the Javascript side
    """
    if strFnc.startswith("add("):
      return varId[:-2]

    return varId

  def deselect(self):
    """
    This method simply deselects a single row that has been found by the row() selector method.

    Documentation
    https://datatables.net/reference/api/row().deselect()

    :return: DataTables API instance for chaining
    """
    return self.fnc("deselect()")

  def select(self):
    """
    This method simply selects a single row that has been found by the row() selector method.

    Documentation
    https://datatables.net/reference/api/row().select()

    :return: DataTables API instance for chaining
    """
    return self.fnc("select()")

  def scrollTo(self, animate=True):
    """
    Redraw the table's scrolling display to show the row selected by the row() method.

    Documentation
    https://datatables.net/reference/api/row().scrollTo()

    :param animate: Animate the scroll (true) or not (false).

    :return: DataTables API instance for chaining
    """
    return self.fnc("scrollTo()")

  def cache(self, dtype):
    """
    Get the DataTables cached data for the selected row.

    Documentation
    https://datatables.net/reference/api/row().cache()

    :param dtype: Specify which cache the data should be read from. Can take one of two values: search or order.
                  Defaults to order if no value is given.

    :return: DataTables API instance for chaining
    """
    if dtype not in ("search", "order"):
      raise Exception("dtype %s not recognised" % dtype)

    dtype = JsUtils.jsConvertData(dtype, None)
    return self.fnc("scrollTo(%s)" % dtype)

  def data(self):
    """
    Retrieve the data for the whole table, in row index order.

    Documentation
    https://datatables.net/reference/api/row().data()

    :return: DataTables API instance for chaining
    """
    return self.fnc("data()")

  def id(self, hash=True):
    """
    This method can be used to get a row's id, as specified by the row's data and the rowId option.
    Optionally it can also prepend a hash (#) to the row id allowing it to then easily be used as a selector.

    Documentation
    https://datatables.net/reference/api/row().id()

    :param hash: Append a hash (#) to the start of the row id. This can be useful for then using the id as a selector

    :return:
    """
    hash = JsUtils.jsConvertData(hash, None)
    return self.fnc("id(%s)" % hash)

  def index(self):
    """
    Get the row index of the selected row.

    Documentation
    https://datatables.net/reference/api/row().index()

    :return: Row index
    """
    return JsObjects.JsNumber.JsNumber("%s.index()" % self.getStr())

  def invalidate(self, source=None):
    """
    Invalidate the data held in DataTables for the selected row.

    Documentation
    https://datatables.net/reference/api/row().invalidate()

    :param source:

    :return:
    """
    return self.fnc("invalidate(%s)")

  def node(self):
    """
    Get the row TR node for the selected row.

    Documentation
    https://datatables.net/reference/api/row().node()

    :return:
    """
    return self.fnc("node()")

  def jquery_node(self):
    """
    Get the cell nodes for the selected column.

    Documentation
    https://datatables.net/reference/api/column().nodes()

    :return:
    """
    self.node()
    self._js.append("to$()")
    return JsQuery.JQuery(jqId=self.toStr())

  def remove(self, update=False):
    """
    Delete the selected row from the DataTable.

    Documentation
    https://datatables.net/reference/api/row().remove()

    :param update:

    :return:
    """
    if update:
      self.fnc("remove()")
      return self.draw()

    return self.fnc("remove()")

  def add(self, jsData, toArray=False, update=False):
    """
    Add a new row to the table.

    Documentation
    https://datatables.net/reference/api/row.add()

    :param jsData: The input data
    :param toArray: Boolean. Convert a python dictionary to a list
    :param update:

    :return:
    """
    if toArray:
      if isinstance(jsData, list):
        rows = []
        for r in jsData:
          rows.append([r.get(h["title"], '') for h in self._parent.vals['columns']])
        jsData = rows
      else:
        jsData = [jsData.get(h["title"], '') for h in self._parent.vals['columns']]
    jsData = JsUtils.jsConvertData(jsData, None)
    self.fnc("add(%s)" % jsData)
    if update:
      self.draw()
      self._js.append([])
      return self

    self._js.append([])
    return self

  def draw(self, target=None):
    """
    Redraw the DataTables in the current context, optionally updating ordering, searching and paging as required.

    Documentation
    https://datatables.net/reference/api/draw()

    :return:
    """
    if target is not None:
      return self.fnc("draw(%s)" % JsUtils.jsConvertData(target, None))

    return self.fnc("draw()")

  def child(self, namespace=True):
    """
    Row child method
    Get / set the child rows of the selected main table row

    Documentation
    https://datatables.net/reference/api/row().child

    :param namespace: Boolean to set the level of this method, selected rows or namespace
    """
    if namespace:
      return RowChildAPI(self.src, selector="%s.child" % self.getStr(), setVar=False, parent=self._parent)

    return RowChildAPI(self.src, selector="%s.child()" % self.getStr(), setVar=False, parent=self._parent)


class DatatableAPI(JsPackage):
  lib_alias = {'js': "datatables", 'css': 'datatables'}
  lib_selector = 'datatable'

  def body(self):
    """
    Get the tbody node for the table in the API's context.

    Documentation
    https://datatables.net/reference/api/table().body()

    :return:
    """
    return

  @property
  def row(self):
    """
    Link to the single row API

    Documentation
    https://datatables.net/reference/api/row()
    """
    return RowAPI(self.src, selector="%s.row()" % self.varId, setVar=False, parent=self._parent)

  @property
  def rows(self):
    """
    Link to the rows API

    Documentation
    https://datatables.net/reference/api/rows()
    """
    return RowAPI(self.src, selector="%s.rows()" % self.varId, setVar=False, parent=self._parent)

  def container(self):
    """
    Get the div container node for the table in the API's context.

    Documentation
    https://datatables.net/reference/api/table().container()

    :return:
    """

  def footer(self):
    """
    Get the tfoot node for the table in the API's context

    Documentation
    https://datatables.net/reference/api/table().footer()

    :return:
    """

  def header(self):
    """
    Get the thead node for the table in the API's context

    Documentation
    https://datatables.net/reference/api/table().header()

    :return:
    """

  def nodes(self):
    """
    Get the table node for the table in the API's context.

    Documentation
    https://datatables.net/reference/api/table().node()

    :return:
    """
    return self.fnc("nodes()")

  def jquery_node(self):
    """
    Get the cell nodes for the selected column.

    Documentation
    https://datatables.net/reference/api/column().nodes()

    :return:
    """
    return JsQuery.JQuery(selector="%s.nodes().to$()" % self.varId, setVar=False)

  def clear(self, update=False):
    """
    Clear the table of all data:

    Documentation
    https://datatables.net/reference/api/clear()

    :param update: Boolean
    :return:
    """
    if update:
      self.fnc("clear()")
      return self.draw()

    return self.fnc("clear()")

  def data(self):
    """
    Retrieve the data for the whole table, in row index order.

    Documentation
    https://datatables.net/reference/api/data()

    :return:
    """
    return JsObjects.JsArray.JsArray.get("%s.data()" % self.varId)

  def destroy(self, remove=False, checkUndefined=False):
    """
    Restore the tables in the current context to its original state in the DOM by removing all of DataTables enhancements,
    alterations to the DOM structure of the table and event listeners.

    Documentation
    https://datatables.net/reference/api/destroy()

    :param remove: Boolean, Completely remove the table from the DOM (true) or leave it in the DOM in its original plain un-enhanced HTML state (default, false).
    :param checkUndefined: Boolean

    :return:
    """
    return self.fnc_closure("destroy(%s)" % JsUtils.jsConvertData(remove, None), checkUndefined=checkUndefined)

  def draw(self, target=None):
    """
    Redraw the DataTables in the current context, optionally updating ordering, searching and paging as required.

    Documentation
    https://datatables.net/reference/api/draw()

    :return:
    """
    if target is not None:
      return self.fnc_closure("draw(%s)" % JsUtils.jsConvertData(target, None))

    return self.fnc_closure("draw()")

  def order(self, data=None):
    """

    Example


    DOcumentation
    https://datatables.net/reference/api/order()

    :return:
    """
    if data is not None:
      data = JsUtils.jsConvertData(data, None)
      return self.fnc("order(%s)" % data)

    return self.fnc("order()")

  def page(self, action):
    """

    Documentation
    https://datatables.net/reference/api/page()

    :return:
    """
    if not action in ("first", "next", "previous", "last"):
      raise Exception("Action not defined")

    return self

  def search(self, jsData):
    """

    Documentation
    https://datatables.net/reference/api/search()

    :param jsData:
    :return:
    """

    return self

  def settings(self):
    """

    Documentation
    https://datatables.net/reference/api/settings()

    :return:
    """
    return self.fnc("settings()")

  def state(self):
    """
    Get the last saved state of the table.

    Documentation
    https://datatables.net/reference/api/state()

    :return:
    """
    return JsObjects.JsObject.JsObject.get("%s.state()" % self.varId)

  def cell(self, cellSelector=None, rowColSelector=None):
    """
    Select cells found by both row and column selectors

    Documentation
    https://datatables.net/reference/api/cells()
    https://datatables.net/reference/api/cell()

    :return:
    """
    if cellSelector is not None:
      selector = "%s.cell(%s)" % self.toStr()
    elif rowColSelector is not None:
      selector = "%s.cell(%s, %s)" % (self.toStr(), rowColSelector[0], rowColSelector[1])
    else:
      selector = "%s.cell()" % self.toStr()
    return CellAPI(selector)

  def column(self, colSelector):
    """

    :param colSelector:
    :return:
    """
    if colSelector is not None:
      selector = "%s.column(%s)" % (self.toStr(), JsUtils.jsConvertData(colSelector, None))
    else:
      selector = "%s.column()" % self.toStr()
    return ColumnAPI(selector)

  def columns(self, colSelector):
    """

    :param colSelector:
    :return:
    """
    if colSelector is not None:
      selector = "%s.column(%s)" % (self.varId, JsUtils.jsConvertData(colSelector, None))
    else:
      selector = "%s.column()" % self.varId
    return ColumnAPI(selector)

  def select(self):
    """
    Initialise Select from outside of the constructor

    Documentation
    https://datatables.net/reference/api/select()

    TODO add the select true
    :return:
    """
    return SelectAPI(selector="%s.select()", setVar=False)
