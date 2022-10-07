"""
Javascript Interface to the Tabulator Module

http://tabulator.info/docs/4.4/components

TODO: Add tree event on RowComponent
"""

from typing import Union, List

from epyk.core.py import primitives
from epyk.core.py import types
from epyk.core.js import JsUtils
from epyk.core.js.objects import JsNodeDom
from epyk.core.js.primitives import JsObjects
from epyk.core.js.packages import JsPackage


class Settings:
  def __init__(self, page: primitives.PageModel, options: dict, component: primitives.HtmlModel = None):
    self.page = page
    self.component = component
    self.__headerVisible = True
    self.__ctx = {}

  @property
  def headerVisible(self):
    """
    By setting the headerVisible option to false you can hide the column headers and present the table as a simple
    list if needed.
    """
    return self.__headerVisible

  @headerVisible.setter
  def headerVisible(self, flag: bool):
    self.__headerVisible = flag
    self.__ctx['headerVisible'] = flag


class Navigation(JsPackage):
  def prev(self):
    """
    next editable cell on the left, if none available move to the right most editable cell on the row above
    """
    return JsObjects.JsObject.JsObject("%s.prev()" % self.toStr(), page=self.page, component=self.component)

  def next(self):
    """
    next editable cell on the right, if none available move to left most editable cell on the row below.
    """
    return JsObjects.JsObject.JsObject("%s.next()" % self.toStr(), page=self.page, component=self.component)

  def left(self):
    """
    next editable cell on the left, return false if none available on row.
    """
    return JsObjects.JsObject.JsObject("%s.left()" % self.toStr(), page=self.page, component=self.component)

  def right(self):
    """
    next editable cell on the right, return false if none available on row.
    """
    return JsObjects.JsObject.JsObject("%s.right()" % self.toStr(), page=self.page, component=self.component)

  def up(self):
    """
    move to the same cell in the row above.
    """
    return JsObjects.JsObject.JsObject("%s.up()" % self.toStr(), page=self.page, component=self.component)

  def down(self):
    """
    move to the same cell in the row below.
    """
    return JsObjects.JsObject.JsObject("%s.down()" % self.toStr(), page=self.page, component=self.component)

  def toStr(self):
    """
    Javascript representation
    """
    if self._selector is None:
      raise ValueError("Selector not defined, use this() or new() first")

    if len(self._js) == 0:
      return self._selector

    str_data = "%(jqId)s.%(items)s" % {'jqId': self._selector, 'items': ".".join(self._js)}
    self._js = []   # empty the stack
    return JsObjects.JsObject.JsObject.get(str_data, page=self.page, component=self.component)


class CellComponent(JsPackage):
  lib_alias = {"js": "tabulator-tables", 'css': "tabulator-tables"}
  lib_selector = "cell"

  def getElement(self):
    """
    The getElement function returns the DOM node for the cell.

    Related Pages:

      http://tabulator.info/docs/4.4/components

    :rtype: JsNodeDom.JsDoms
    """
    return JsNodeDom.JsDoms("%s.getElement()" % self.toStr(), component=self.component, page=self.page)

  def getColumn(self):
    """
    The getColumn function returns the ColumnComponent for the column that contains the cell.

    Related Pages:

      http://tabulator.info/docs/4.4/components
    """
    return ColumnComponent(
      selector="%s.getColumn()" % self.toStr(), set_var=False, component=self.component, page=self.page)

  def getRow(self):
    """
    The getRow function returns the RowComponent for the row that contains the cell.

    Related Pages:

      http://tabulator.info/docs/4.4/components
    """
    return RowComponent(selector="%s.getRow()" % self.toStr(), set_var=False, component=self.component, page=self.page)

  def getData(self):
    """
    The getData function returns the data for the row that contains the cell.

    Related Pages:

      http://tabulator.info/docs/4.4/components
    """
    return JsObjects.JsObject.JsObject("%s.getData()" % self.toStr(), component=self.component, page=self.page)

  def getField(self):
    """
    The getField function returns the field name for the column that contains the cell.

    Related Pages:

      http://tabulator.info/docs/4.4/components
    """
    return JsObjects.JsObject.JsObject("%s.getField()" % self.toStr(), component=self.component, page=self.page)

  def restoreOldValue(self):
    """
    The restoreOldValue reverts the value of the cell back to its previous value, without triggering any of the cell
    edit callbacks.

    Related Pages:

      http://tabulator.info/docs/4.4/components
    """
    return JsObjects.JsString.JsString("%s.restoreOldValue()" % self.toStr(), page=self.page, component=self.component)

  def getOldValue(self):
    """
    The getOldValue function returns the previous value of the cell. Very usefull in the event of cell update callbacks.

    Related Pages:

      http://tabulator.info/docs/3.5#component-cell
    """
    return JsObjects.JsString.JsString("%s.restoreOldValue()" % self.toStr(), page=self.page, component=self.component)

  def getValue(self):
    """
    The getValue function returns the current value for the cell.

    Related Pages:

      http://tabulator.info/docs/3.5#component-cell
    """
    return JsObjects.JsObject.JsObject("%s.getValue()" % self.toStr(), page=self.page, component=self.component)

  def setValue(self, text, flag: bool = True):
    """
    You can change the value of the cell using the setValue function.
    The first parameter should be the new value for the cell, the second optional parameter will apply the column
    mutators to the value when set to true (default = true).

    Related Pages:

      http://tabulator.info/docs/4.4/components
 
    :param text:
    :param flag:
    """
    text = JsUtils.jsConvertData(text, None)
    flag = JsUtils.jsConvertData(flag, None)
    return JsObjects.JsObject.JsObject(
      "%s.setValue(%s, %s)" % (self.toStr(), text, flag), page=self.page, component=self.component)

  def checkHeight(self):
    """
    If you are making manual adjustments to elements contained withing the cell, or the cell itself,
    it may sometimes be necessary to recalculate the height of all the cells in the row to make sure they remain aligned

    Related Pages:

      http://tabulator.info/docs/4.4/components
    """
    return JsObjects.JsBoolean.JsBoolean("%s.checkHeight()" % self.toStr(), page=self.page, component=self.component)

  def edit(self, flag=True):
    """
    You and programmatically cause a cell to open its editor element using the edit function.

    Related Pages:

      http://tabulator.info/docs/4.4/components
 
    :param flag:
    """
    flag = JsUtils.jsConvertData(flag, None)
    return JsObjects.JsObject.JsObject("%s.edit(%s)" % (self.toStr(), flag), page=self.page, component=self.component)

  def cancelEdit(self):
    """
    You and programmatically cancel a cell edit that is currently in progress by calling the cancelEdit function.
    """
    return JsObjects.JsObject.JsObject("%s.cancelEdit()" % self.toStr(), page=self.page, component=self.component)

  def nav(self):
    """
    When a cell is being edited it is possible to move the editor focus from the current cell to one if its neighbours.
    """
    return Navigation(js_code="%s.nav()" % self.toStr(), page=self.page, component=self.component)


class GroupComponent(JsPackage):
  def getElement(self):
    """
    The getElement function returns the DOM node for the group header.

    Related Pages:

      http://tabulator.info/docs/3.5#component-cell
    """
    return JsNodeDom.JsDoms("%s.getElement()" % self.toStr(), page=self.page, component=self.component)

  def getKey(self):
    """
    The getKey function returns the unique key that is shared between all rows in this group.
    """
    return JsObjects.JsObject.JsObject("%s.getKey()" % self.toStr(), page=self.page, component=self.component)

  def getField(self):
    """
    The getField function returns the string of the field that all rows in this group have been grouped by.
    (if a function is used to group the rows rather than a field, this function will return false).
    """
    return JsObjects.JsString.JsString("%s.getField()" % self.toStr(), page=self.page, component=self.component)

  def getRows(self):
    """
    The getRows function returns an array of RowComponent objects, one for each row in the group.
    """
    return RowComponent(js_code="%s.getRows()" % self.toStr(), page=self.page, component=self.component)

  def getSubGroups(self):
    """
    The getParentGroup function returns the GroupComponent for the parent group of this group.
    if no parent exists, this function will return false.
    """
    return JsObjects.JsArray.JsArray("%s.getParentGroup()" % self.toStr())

  def getVisibility(self):
    """
    The getVisibility function returns a boolean to show if the group is visible, a value of true means it is visible.
    """
    return JsObjects.JsBoolean.JsBoolean("%s.getVisibility()" % self.toStr())

  def show(self):
    """
    The show function shows the group if it is hidden.
    """
    return JsObjects.JsObject.JsObject("%s.show()" % self.toStr())

  def hide(self):
    """
    The hide function hides the group if it is visible.
    """
    return JsObjects.JsObject.JsObject("%s.hide()" % self.toStr(), page=self.page, component=self.component)

  def toggle(self):
    """
    The toggle function toggles the visibility of the group, switching between hidden and visible.
    """
    return JsObjects.JsObject.JsObject("%s.toggle()" % self.toStr(), page=self.page, component=self.component)

  def getTable(self):
    """
    The getTable function returns the Tabulator object for the table containing the group.
    """
    return JsObjects.JsObject.JsObject("%s.getTable()" % self.toStr(), page=self.page, component=self.component)

  def getParentColumn(self):
    """
    The getParentGroup function returns the GroupComponent for the parent group of this group.
    if no parent exists, this function will return false.
    """
    return GroupComponent(js_code="%s.getParentGroup()" % self.toStr(), page=self.page, component=self.component)


class ColumnComponent(JsPackage):
  lib_alias = {"js": "tabulator-tables", 'css': "tabulator-tables"}
  lib_selector = "column"

  def getElement(self):
    """
    The getElement function returns the DOM node for the column.
    """
    return JsNodeDom.JsDoms("%s.getElement()" % self.toStr(), page=self.page, component=self.component)

  def getTable(self):
    """
    The getTable function returns the Tabulator object for the table containing the column.
    """
    return JsObjects.JsObject.JsObject("%s.getTable()" % self.toStr(), page=self.page, component=self.component)

  def getDefinition(self):
    """
    The getDefinition function returns the column definition object for the column.
    """
    return JsObjects.JsObject.JsObject("%s.getDefinition()" % self.toStr(), page=self.page, component=self.component)

  def getField(self):
    """
    The getField function returns the field name for the column.
    """
    return JsObjects.JsObject.JsObject("%s.getField()" % self.toStr(), page=self.page, component=self.component)

  def getCells(self):
    """
    The getCells function returns an array of CellComponent objects, one for each cell in the column.
    """
    return CellComponent(js_code="%s.getCells()" % self.toStr(), page=self.page, component=self.component)

  def getNextColumn(self):
    """
    The getNextColumn function returns the Column Component for the next visible column in the table,
    if there is no next column it will return a value of false.
    """
    return ColumnComponent(js_code="%s.getNextColumn()" % self.toStr(), page=self.page, component=self.component)

  def getPrevColumn(self):
    """
    The getPrevColumn function returns the Column Component for the previous visible column in the table,
    if there is no previous column it will return a value of false.
    """
    return ColumnComponent(js_code="%s.getPrevColumn()" % self.toStr(), page=self.page, component=self.component)

  def getVisibility(self):
    """
    The getVisibility function returns a boolean to show if the column is visible, a value of true means it is visible.
    """
    return JsObjects.JsBoolean.JsBoolean("%s.getVisibility()" % self.toStr(), page=self.page, component=self.component)

  def show(self):
    """
    The show function shows the column if it is hidden.
    """
    return JsObjects.JsObject.JsObject("%s.show()" % self.toStr(), page=self.page, component=self.component)

  def hide(self):
    """
    The hide function hides the column if it is visible.
    """
    return JsObjects.JsObject.JsObject("%s.hide()" % self.toStr(), page=self.page, component=self.component)

  def toggle(self):
    """
    The toggle function toggles the visibility of the column, switching between hidden and visible.

    Related Pages:

      http://tabulator.info/docs/4.5/columns#addColumn
    """
    return JsObjects.JsObject.JsObject("%s.hide()" % self.toStr(), page=self.page, component=self.component)

  def delete(self):
    """
    The delete function deletes the column, removing it from the table.
    """
    return self.fnc_closure_in_promise("delete()")

  def scrollTo(self):
    """
    The scrollTo function will scroll the table to the column if it is visible.
    """
    return JsObjects.JsObject.JsObject("%s.scrollTo()" % self.toStr(), page=self.page, component=self.component)

  def move(self, text, flag):
    """
    ou can move a column next to another column using the move function.
 
    :param text:
    :param flag:
    """
    text = JsUtils.jsConvertData(text, None)
    flag = JsUtils.jsConvertData(flag, None)
    return JsObjects.JsObject.JsObject(
      "%s.move(%s, %s)" % (self.toStr(), text, flag), page=self.page, component=self.component)

  def getSubColumns(self):
    """
    The getSubColumns function returns an array of ColumnComponent objects, one for each sub column of this column.
    """
    return ColumnComponent(js_code="%s.getSubColumns()" % self.toStr(), page=self.page, component=self.component)

  def getParentColumn(self):
    """
    The getParentColumn function returns the ColumnComponent for the parent column of this column.
    if no parent exists, this function will return false
    """
    return ColumnComponent(js_code="%s.getParentColumn()" % self.toStr(), page=self.page, component=self.component)

  def headerFilterFocus(self):
    """
    The headerFilterFocus function will place focus on the header filter element for this column if it exists.
    """
    return JsObjects.JsObject.JsObject(
      "%s.headerFilterFocus()" % self.toStr(), page=self.page, component=self.component)

  def setHeaderFilterValue(self, text):
    """
    The setHeaderFilterValue function set the value of the columns header filter element to the value provided
    in the first argument.
 
    :param text:
    """
    text = JsUtils.jsConvertData(text, None)
    return JsObjects.JsObject.JsObject(
      "%s.setHeaderFilterValue(%s)" % (self.toStr(), text), page=self.page, component=self.component)

  def reloadHeaderFilter(self):
    """
    The reloadHeaderFilter function rebuilds the header filter element, updating any params passed into the editor
    used to generate the filter.
    """
    return JsObjects.JsObject.JsObject(
      "%s.reloadHeaderFilter()" % self.toStr(), page=self.page, component=self.component)


class ColumnComponents(JsPackage):
  lib_selector = "column"

  def forEach(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
    """
 
    :param js_funcs: A Javascript Python function.
    :param profile: Optional. A flag to set the component performance storage.
    """
    return self.fnc_closure("forEach(function(rec){%s})" % JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile))

  @property
  def table(self):
    """
    Return to the parent table.
    """
    self._parent._js.append([])
    return self._parent

  @property
  def fields(self):
    """

    """
    return JsObjects.JsArray.JsArray.get(
      "(function(){var columns = []; %s.forEach(function(rec){columns.push(rec.getField())}); return columns})()" % self._selector,
      component=self.component, page=self.page)

  def rename(self, field: str = None, title: str = None, columns=None):
    """
 
    :param field: Column fields' name
    :param title: Column title's name
    :param columns:
    """
    if columns is not None:
      columns = JsUtils.jsConvertData(columns, None)
      return JsObjects.JsVoid("var colMaps = %s; %s.forEach(function(rec){if(colMaps[rec.getField()]){rec._column.contentElement.innerText = colMaps[rec.getField()]}})" % (columns, self._selector))

    title = JsUtils.jsConvertData(title, None)
    field = JsUtils.jsConvertData(field, None)
    return JsObjects.JsVoid("%s.forEach(function(rec){if(rec.getField() == %s){rec._column.contentElement.innerText = %s}})" % (self._selector, field, title))


class RowComponent(JsPackage):
  lib_selector = "row"

  def update(self, data: Union[primitives.JsDataModel, dict]):
    """
    You can update the data in the row using the update function.
    You should pass an object to the function containing any fields you wish to update

    Related Pages:

      http://www.tabulator.info/docs/4.0/update
 
    :param data: Dictionary with the data to override.
    """
    data = JsUtils.jsConvertData(data, None)
    return self.fnc_closure("update(%s)" % data)

  def getData(self) -> JsObjects.JsObject.JsObject:
    """
    The getData function returns the data object for the row.

    Related Pages:

      http://tabulator.info/docs/4.4/components
    """
    return JsObjects.JsObject.JsObject("%s.getData()" % self.toStr(), page=self.page, component=self.component)

  def getDict(self) -> dict:
    """
    Return the if columns are defined on the Python side.

    Usage::

      table.js._.getDict()
    """
    if not self.component.options.columns:
      raise ValueError("This method cannot be called to get the python row dictionary")

    return {c.field: JsUtils.jsWrap(
      "%s.getData()['%s']" % (self.toStr(), c.field)) for c in self.component.options.columns}

  def getElement(self) -> JsNodeDom.JsDoms:
    """
    The getElement function returns the DOM node for the row.

    Related Pages:

      http://tabulator.info/docs/4.4/components

    """
    return JsNodeDom.JsDoms("%s.getElement()" % self.toStr(), page=self.page, component=self.component)

  def getCells(self) -> JsObjects.JsArray.JsArray:
    """
    The getCells function returns an array of CellComponent objects, one for each cell in the row.
    """
    return JsObjects.JsArray.JsArray("%s.getCells()" % self.toStr(), page=self.page, component=self.component)

  def getCell(self) -> CellComponent:
    """
    The getCell function returns the CellComponent for the specified column from this row.
    """
    return CellComponent(js_code="%s.getCell()" % self.toStr(), page=self.page, component=self.component)

  def getIndex(self) -> JsObjects.JsNumber.JsNumber:
    """
    The getIndex function returns the index value for the row.
    (this is the value from the defined index column, NOT the row's position in the table)
    """
    return JsObjects.JsNumber.JsNumber("%s.getIndex()" % self.toStr(), page=self.page, component=self.component)

  def getPosition(self, flag: Union[primitives.JsDataModel, bool] = True):
    """
    Use the getPosition function to retrieve the numerical position of a row in the table.
    By default this will return the position of the row in all data, including data currently filtered out of the table.

    Related Pages:

      http://tabulator.info/docs/4.0/components#:~:text=Get%20Position,filtered%20out%20of%20the%20table.
 
    :param flag: To get the position of the row in the currently filtered/sorted data
    """
    flag = JsUtils.jsConvertData(flag, None)
    return JsObjects.JsNumber.JsNumber(
      "%s.getPosition(%s)" % (self.toStr(), flag), page=self.page, component=self.component)

  def getGroup(self):
    """
    When using grouped rows, you can retrieve the group component for the current row using the getGroup function.
    """
    return GroupComponent(js_code="%s.getGroup()" % self.toStr(), page=self.page, component=self.component)

  def delete(self):
    """
    The delete function deletes the row, removing its data from the table.

    TODO: Fix the fnc_closure_in_promise implementation

    Related Pages:

      http://www.tabulator.info/docs/4.0/update
    """
    return self.fnc_closure("delete()")

  def scrollTo(self):
    """
    The scrollTo function will scroll the table to the row if it passes the current filters.
    """
    return self.fnc_closure("scrollTo()")

  def pageTo(self):
    """
    The pageTo function will load the page for the row if it passes the current filters.
    """
    return self.fnc_closure("pageTo()")

  def move(self, index: int, flag: Union[primitives.JsDataModel, bool] = True):
    """
    You can move a row next to another row using the move function.
 
    :param index:
    :param flag:
    """
    index = JsUtils.jsConvertData(index, None)
    flag = JsUtils.jsConvertData(flag, None)
    return self.fnc_closure("move(%s, %s)" % (index, flag))

  def select(self):
    """
    The select function will select the current row.
    """
    return self.fnc_closure("select()")

  def deselect(self):
    """
    The deselect function will deselect the current row.
    """
    return self.fnc_closure("deselect()")

  def toggleSelect(self):
    """
    The toggleSelect function will toggle the selected state the current row.
    """
    return self.fnc_closure("toggleSelect()")

  def isSelected(self):
    """
    The isSelected function will return a boolean representing the current selected state of the row.
    """
    return JsObjects.JsBoolean.JsBoolean("%s.isSelected()" % self.toStr(), page=self.page, component=self.component)

  def normalizeHeight(self):
    """
    If you are making manual adjustments to elements contained within the row,
    it may sometimes be necessary to recalculate the height of all the cells in the row to make sure they remain aligned
    """
    return JsObjects.JsObject.JsObject("%s.normalizeHeight()" % self.toStr(), page=self.page, component=self.component)

  def reformat(self):
    """
    If you want to re-format a row once it has been rendered to re-trigger the cell formatters and the rowFormatter
    callback, Call the reformat function.
    """
    return self.fnc_closure("reformat()")

  def freeze(self):
    """
    You can freeze a row at the top of the table by calling the freeze function. This will insert the row above
    the scrolling portion of the table in the table header.
    """
    return self.fnc_closure("freeze()")

  def unfreeze(self):
    """
    A frozen row can be unfrozen using the unfreeze function.
    This will remove the row from the table header and re-insert it back in the table.
    """
    return self.fnc_closure("unfreeze()")

  def getTreeChildren(self):
    return JsObjects.JsArray.JsArray("%s.getTreeChildren()" % self._selector, page=self.page, component=self.component)

  def addTreeChild(self, data):
    return JsObjects.JsArray.JsArray("%s.addTreeChild(%s)" % (self._selector, JsUtils.jsConvertData(data, None)),
                                     page=self.page, component=self.component)

  def addTreeChildren(self, data):
    """

    :param data:
    """
    return JsObjects.JsArray.JsArray("%s.forEach(function(rec){%s.addTreeChild(rec)})" % (
      JsUtils.jsConvertData(data, None), self._selector), page=self.page, component=self.component)

  @JsUtils.fromVersion({'tabulator-tables': '5.3.0'})
  def watchPosition(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
    """
 
    :param js_funcs:
    :param profile:
    """
    return "%s.watchPosition(function(value, count, data, group){%s})" % (self._selector, JsUtils.jsConvertFncs(
        js_funcs, toStr=True, profile=profile))


class TabRowContextMenu(JsPackage):
  lib_set_var = False

  def add(self, name: str, url: str, icon: str = None):
    """
    Add an item to a table context menu.

    TODO: Improve this interface.

    Usage::

      table.js.rowContextMenu.add("Test", "/test")
 
    :param name: The name of the item in the context menu.
    :param url: The service URL. (This service will only return a message).
    :param icon: Optional. The icon class name.
    """
    js_service = self.page.js.fncs.service()
    if icon is not None:
      return JsObjects.JsVoid("%s.options.rowContextMenu.push({label: '<i class=\"%s\" style=\"margin-right:5px\"></i>%s', action: function(e, row){var data = {row: row.getData(), label: '%s'}; %s('%s', data)} })" % (self.toStr(), icon, name, name, js_service, url))

    return JsObjects.JsVoid("%s.options.rowContextMenu.push({label: '%s', action: function(e, row){var data = {row: row.getData(), label: '%s'}; %s('%s', data)} })" % (self.toStr(), name, name, js_service, url))

  def fromConfig(self, services: list):
    """
    Extend the context menu of a table from a configuration object.
 
    :param services: A list of services to be added to the context menu.
    """
    js_service = self.page.js.fncs.service()
    services = JsUtils.jsConvertData(services, None)
    return JsObjects.JsVoid('''
%(menu)s.forEach(function(item){
  var label = item.label;
  if(typeof item.icon !== "undefined"){label = '<i class="'+ item.icon +'" style="margin-right:5px"></i>' + label}
  %(tableId)s.options.rowContextMenu.push({label: label, 
    action: function(e, row){var data = {row: row.getData(), label: item.label}; %(serviceName)s(item.url, data)} })
})''' % {"menu": services, 'tableId': self.toStr(), 'serviceName': js_service})


class Tabulator(JsPackage):
  lib_alias = {"js": "tabulator-tables", 'css': "tabulator-tables"}

  #  -----------------------------------------
  #  Common table javascript interface
  #  -----------------------------------------
  def download(self, format: str, filename: str, options: dict = None):
    """   Common download feature for tables.

    Related Pages:

      http://tabulator.info/docs/4.0/download
 
    :param format: File format
    :param filename: Filename
    :param options: Download option
    """
    if format == "pdf":
      self.page.jsImports.add("jspdf")
    format = JsUtils.jsConvertData(format, None)
    filename = JsUtils.jsConvertData(filename, None)
    if options is None:
      return JsObjects.JsVoid("%s.download(%s, %s)" % (self.varId, format, filename))

    options = JsUtils.jsConvertData(options, None)
    return JsObjects.JsVoid("%s.download(%s, %s, %s)" % (self.varId, format, filename, options))

  def empty(self):
    """

    :return:
    """
    return self.clearData()

  def add_row(self, data, flag: Union[types.JS_DATA_TYPES, bool] = False):
    return self.addRow(data, flag)

  def show_column(self, column: str):
    return self.showColumn(column)

  def hide_column(self, column: str):
    return self.hideColumn(column)

  #  -----------------------------------------
  #  Specific table javascript interface
  #  -----------------------------------------
  @JsUtils.fromVersion({'tabulator-tables': '5.2.0'})
  def alert(self, text: str):
    """   To show an alert, call the alert function on the table. Passing the message into the first argument of the function.

    Usage::

      btn1 = page.ui.button("Display Alert")
      btn1.click([table.js.alert("Test")])

    Related Pages:

      http://tabulator.info/docs/5.2/menu#popup-row
 
    :param text: Alert message
    """
    text = JsUtils.jsConvertData(text, None)
    return JsObjects.JsVoid("%s.alert(%s)" % (self.varId, text))

  def downloadToTab(self, file_format: str):
    """   If you want to open the generated file in a new browser tab rather than downloading it straight away, you can use
    the downloadToTab function.
    This is particularly useful with the PDF downloader, as it allows you to preview the resulting PDF
    in a new browser tab

    Related Pages:

      http://tabulator.info/docs/4.8/download
 
    :param file_format: The output format
    """
    if file_format == "pdf":
      self.page.jsImports.add("jspdf")
    file_format = JsUtils.jsConvertData(file_format, None)
    return JsObjects.JsVoid("%s.downloadToTab(%s)" % (self.varId, file_format))

  @JsUtils.fromVersion({'tabulator-tables': '5.2.0'})
  def clearAlert(self):
    """   To clear an active alert, call the clearAlert function on the table.

    Usage::

      btn1 = page.ui.button("Clear Alert")
      btn1.click([table.js.clearAlert()])

    Related Pages:

      http://tabulator.info/docs/5.2/menu#popup-row
    """
    return JsObjects.JsVoid("%s.clearAlert()" % self.varId)

  def copyToClipboard(self, clipboard_copy_selector: str = None, with_header: bool = True):
    """   If the table has focus, the copyToClipboard keybinding which is by default set to the ctrl + c key combination,
    will trigger a copy of table to the clipboard, which data is copied depends on the state of the table.

    Related Pages:

      http://tabulator.info/docs/4.6/clipboard
 
    :param clipboard_copy_selector: can be table, active, selected, visible, all
    :param with_header: Optional. defined if the header are included in the copy
    """
    self.page.config.clipboard = True
    if clipboard_copy_selector is None:
      clipboard_copy_selector = 'all'
      clipboard_copy_selector = JsUtils.jsConvertData(clipboard_copy_selector, None)
    if not with_header:
      return JsObjects.JsVoid("%s.copyToClipboard(%s, %s)" % (
        self.varId, clipboard_copy_selector, JsUtils.jsConvertData(with_header, None)))

    return JsObjects.JsVoid("%s.copyToClipboard(%s)" % (self.varId, clipboard_copy_selector))

  def getCalcResults(self):
    """   You can retrieve the results of the column calculations at any point using the getCalcResults function.

    Related Pages:

      http://tabulator.info/docs/4.0/column-calcs
    """
    return JsObjects.JsObject.JsObject("%s.getCalcResults()" % self.varId, page=self.page, component=self.component)

  def getAjaxUrl(self):
    """   You can retrieve the current AJAX URL of the table with the getAjaxUrl function.

    Related Pages:

      http://tabulator.info/docs/4.0/data#ajax-filter
    """
    return JsObjects.JsString.JsString("%s.getAjaxUrl()" % self.varId, page=self.page, component=self.component)

  def recalc(self):
    """   Calculations will be automatically updated whenever the row data is changed or edited.
    
    If you want to trigger an update of the calculation at any point you can call the recalc function on the table.

    Related Pages:

      http://tabulator.info/docs/5.0/column-calcs
    """
    return JsObjects.JsVoid("%s.recalc()" % self.varId)

  def previousPage(self):
    """   You can change to show the next page using the previousPage function.

    Related Pages:

      http://tabulator.info/docs/4.1/page
    """
    return JsObjects.JsPromise("%s.previousPage()" % self.varId)

  def nextPage(self):
    """   You can change to show the next page using the nextPage function.

    Related Pages:

      http://tabulator.info/docs/4.1/page
    """
    return JsObjects.JsPromise("%s.nextPage()" % self.varId)

  def setPage(self, i: Union[str, int]):
    """   When pagination is enabled the table footer will contain a number of pagination controls for navigating
    through the data.

    Related Pages:

      http://tabulator.info/docs/4.1/page
 
    :param i: The page index or some special keywords like first, next...
    """
    return JsObjects.JsPromise("%s.setPage(%s)" % (self.varId, i))

  def setPageSize(self, i: int):
    """   You can change the page size at any point by using the setPageSize function.
    (this setting will be ignored if using remote pagination with the page size set by the server)

    Related Pages:

      http://tabulator.info/docs/4.1/page
 
    :param i: The rows number
    """
    return JsObjects.JsPromise("%s.setPageSize(%s)" % (self.varId, i))

  def setGroupBy(self, column: str = None):
    """   You can use the setGroupBy function to change the fields that rows are grouped by.
    This function has one argument and takes the same values as passed to the groupBy setup option.

    Related Pages:

      http://www.tabulator.info/docs/4.1/group
 
    :param column: Optional. The column name
    """
    if column is None:
      return JsObjects.JsVoid("%s.setGroupBy()" % self.varId)

    return JsObjects.JsVoid("%s.setGroupBy(%s)" % (self.varId, JsUtils.jsConvertData(column, None)))

  def setGroupStartOpen(self, flag: Union[primitives.JsDataModel, bool]):
    """
    You can use the setGroupStartOpen function to change the default open state of groups.
    This function has one argument and takes the same values as passed to the groupStartOpen setup option.

    Related Pages:

      http://www.tabulator.info/docs/4.1/group
 
    :param flag: Flag for the open state for groups
    """
    return JsObjects.JsVoid("%s.setGroupStartOpen(%s)" % (self.varId, JsUtils.jsConvertData(flag, None)))

  def setGroupHeader(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
    """
    You can use the setGroupHeader function to change the header generation function for each group.
    This function has one argument and takes the same values as passed to the groupHeader setup option.

    Related Pages:

      http://www.tabulator.info/docs/4.1/group
 
    :param js_funcs: Javascript functions
    :param profile: Optional. A flag to set the component performance storage.
    """
    return self.fnc_closure(
      "setGroupHeader(function(value, count, data, group){%s})" % JsUtils.jsConvertFncs(
        js_funcs, toStr=True, profile=profile))

  def deleteRow(self, n: int):
    """
    You can delete any row in the table using the deleteRow function.
    The first argument is the row you want to delete, it will take any of the standard row component look up options.

    Related Pages:

      http://www.tabulator.info/docs/4.0/update
 
    :param n: Row index
    """
    return JsObjects.JsPromise("%s.deleteRow(%s)" % (self.varId, n))

  def addRow(self, data, flag: Union[types.JS_DATA_TYPES, bool] = False):
    """
    You can add a row to the table using the addRow function.

    The first argument should be a row data object. If you do not pass data for a column, it will be left empty.
    To create a blank row (ie for a user to fill in), pass an empty object to the function.

    The second argument is optional and determines whether the row is added to the top or bottom of the table.
    A value of true will add the row to the top of the table, a value of false will add the row to the
    bottom of the table.
    If the parameter is not set the row will be placed according to the addRowPos global option.

    Related Pages:

      http://tabulator.info/docs/4.3/update#addrow
 
    :param data:
    :param flag:
    """
    data = JsUtils.jsConvertData(data, None)
    flag = JsUtils.jsConvertData(flag, None)
    return JsObjects.JsVoid("%s.addRow(%s, %s)" % (self.varId, data, flag))

  def updateRow(self, row_id, data):
    """
    The updateRow and row.updatemethods return a promise,
    this can be used to run any other commands that have to be run after the data has been loaded into the table.

    Related Pages:

      http://www.tabulator.info/docs/4.0/update
 
    :param row_id:
    :param data:
    """
    return self.fnc_closure("updateRow(%s, %s)" % (row_id, JsUtils.jsConvertData(data, None)))

  def updateOrAddRow(self, row_id, data):
    """
    If you don't know whether a row already exists you can use the updateOrAddRow function.
    This will check if a row with a matching index exists, if it does it will update it,
    if not it will add a new row with that data.

    Related Pages:

      http://www.tabulator.info/docs/4.0/update
 
    :param row_id:
    :param data:
    """
    return self.fnc_closure("updateOrAddRow(%s, %s)" % (row_id, JsUtils.jsConvertData(data, None)))

  def getRow(self, index: Union[types.JS_DATA_TYPES, int]):
    """
    Get the Row component.

    Related Pages:

      http://tabulator.info/docs/4.1/components

    Usage::

      var row = cell.getRow();
 
    :param index:
    """
    row = RowComponent(self.component, selector="getRow(%s)" % index, set_var=False, page=self.page)
    self.fnc(row)
    return row

  def getSelectedRows(self):
    """
    To get the RowComponent's for the selected rows at any time you can use the getSelectedRows function.

    Related Pages:

      http://tabulator.info/docs/4.0/select
    """
    return JsObjects.JsArray.JsArray("%s.getSelectedRows()" % self.varId, page=self.page, component=self.component)

  def getRows(self) -> JsObjects.JsArray.JsArray:
    """
    The getRows function returns an array of RowComponent objects, one for each row in the table.

    Usage::

      rows = table.getRows()

    Related Pages:

      http://tabulator.info/docs/4.1/components
    """
    return JsObjects.JsArray.JsArray("%s.getRows()" % self.varId, page=self.page, component=self.component)

  def getRowPosition(self, row, flag: bool = True) -> JsObjects.JsNumber.JsNumber:
    """
    The new getRowPosition function and Row Component getPosition function allow you to retrieve
    the current position of a row in the table.

    Related Pages:

      http://tabulator.info/news
 
    :param row:
    :param flag:
    """
    return JsObjects.JsNumber.JsNumber(
      "%s.getRowPosition(%s, %s)" % (self.varId, row, flag), page=self.page, component=self.component)

  def getPageSize(self) -> JsObjects.JsNumber.JsNumber:
    """

    Related Pages:

      http://tabulator.info/docs/4.1/page
    """
    return JsObjects.JsNumber.JsNumber("%s.getPageSize()" % self.varId, page=self.page, component=self.component)

  def getPage(self) -> JsObjects.JsNumber.JsNumber:
    """

    Related Pages:

      http://tabulator.info/docs/4.1/page
    """
    return JsObjects.JsNumber.JsNumber("%s.getPage()" % self.varId, page=self.page, component=self.component)

  def getPageMax(self) -> JsObjects.JsNumber.JsNumber:
    """

    Related Pages:

      http://tabulator.info/docs/4.1/page
    """
    return JsObjects.JsNumber.JsNumber("%s.getPageMax()" % self.varId, page=self.page, component=self.component)

  def getRowFromPosition(self, n: int, flag: bool = True) -> JsObjects.JsNumber.JsNumber:
    """
 
    :param n:
    :param flag:
    """
    flag = JsUtils.jsConvertData(flag, None)
    return JsObjects.JsNumber.JsNumber(
      "%s.getRowFromPosition(%s, %s)" % (self.varId, n, flag), page=self.page, component=self.component)

  def toggleColumn(self, column: str):
    """
    You can toggle the visibility of a column at any point using the toggleColumn function.
    Pass the field name of the column you wish to toggle as the first parameter of the function.

    Usage::

      table.toggleColumn("name")

    Related Pages:

      http://tabulator.info/docs/4.5/columns#addColumn
 
    :param column: The column name
    """
    column = JsUtils.jsConvertData(column, None)
    return JsObjects.JsPromise("%s.toggleColumn(%s)" % (self.varId, column))

  def hideColumn(self, column: str):
    """
    You can hide a visible column at any point using the hideColumn function.
    Pass the field name of the column you wish to hide as the first parameter of the function.

    Usage::

      table.hideColumn("name")

    Related Pages:

      http://tabulator.info/docs/4.5/columns#addColumn
 
    :param column: The column name
    """
    column = JsUtils.jsConvertData(column, None)
    return JsObjects.JsPromise("%s.hideColumn(%s)" % (self.varId, column))

  def hideColumns(self, columns: List[str]):
    """
    You can hide a visible column at any point using the hideColumn function.
    Pass the field name of the column you wish to hide as the first parameter of the function.

    Usage::

      table.hideColumn("name")

    Related Pages:

      http://tabulator.info/docs/4.5/columns#addColumn
 
    :param columns: Columns' names
    """
    columns = JsUtils.jsConvertData(columns, None)
    return JsObjects.JsPromise("%s.forEach(function(c){%s.hideColumn(c)})" % (columns, self.varId))

  def columns(self, headers=None, rows=None, values=None, options=None):
    """
 
    :param headers:
    :param rows:
    :param values:
    :param options:
    """
    if headers is None and rows is None and values is None:
      raise ValueError("Header, rows or values must be defined")

    if headers is not None:
      # If this variable is used it means the definition should be fully supplied and the default style will not be applied
      return JsObjects.JsVoid("%s;%s" % (
        self.getColumns.forEach("rec.delete()").toStr(), self.addColumns(headers, options=options).toStr()))

    if rows is not None or values is not None:
      rows_fields = self.component.options.get({}, "rows_def").get("fields", [])
      if rows is None and rows_fields:
        values = JsObjects.JsObjects.get(
          "(function(d){var results = []; d.forEach(function(rec){if(typeof rec === 'string'){rec = {'field': rec, 'title': rec}}; results.push( Object.assign(rec, %s))}); return results})(%s)" % (
          JsUtils.jsConvertData(self.component.options.get({}, "columns_def"), None), values or []))
        return JsObjects.JsVoid("%s;%s" % (self.getColumns.forEach(
          "if(!(%s.includes(rec.getField()))){rec.delete()}" % rows_fields
        ).toStr(), self.addColumns(values).toStr()))
      else:
        rows = JsObjects.JsObjects.get("(function(d){var results = []; d.forEach(function(rec){if(typeof rec === 'string'){rec = {'field': rec, 'title': rec}}; results.push( Object.assign(%s, rec))}); return results})(%s)" % (JsUtils.jsConvertData(self.component.options.get({}, "rows_def"), None), rows or []))
        values = JsObjects.JsObjects.get("(function(d){var results = []; d.forEach(function(rec){if(typeof rec === 'string'){rec = {'field': rec, 'title': rec}}; results.push( Object.assign(%s, rec))}); return results})(%s)" % (JsUtils.jsConvertData(self.component.options.get({}, "columns_def"), None), values or []))
        return JsObjects.JsVoid("%s;%s" % (self.getColumns.forEach("rec.delete()").toStr(), "%s + %s" % (
          self.addColumns(rows).toStr(), self.addColumns(values).toStr())))

  def values(self, data, columns=None, options=None):
    """
 
    :param data:
    :param columns:
    :param options:
    """
    if columns is None:
      # Just replace the data in the table
      return self.component.build(data)

    # Change the columns and replace them with the new ones
    return JsUtils.jsConvertFncs(
      [self.columns(values=columns, options=options), self.component.build(data)], toStr=True)

  @property
  def getColumns(self):
    """
    To get an array of Column Components for the current table setup, call the getColumns function.
    This will only return actual data columns not column groups.

    Usage::

      var cols = table.getColumns()

    Related Pages:

      http://tabulator.info/docs/4.5/columns#getColumns

    """
    columns = ColumnComponents(self.component, selector="%s.getColumns()" % self.varId, set_var=False, page=self.page)
    self.fnc(columns)
    return columns

  def addColumn(self, data, before=False, position=""):
    """   If you wish to add a single column to the table, you can do this using the addColumn function

    Usage::

      table.addColumn({"title": "Age", "field": "age"}, True, "name");

    Related Pages:

      http://tabulator.info/docs/4.5/columns#addColumn
 
    :param data: The column definition object for the column you want to add
    :param before: Determines how to position the new column.
        A value of true will insert the column to the left of existing columns, a value of false will insert it to the
        right
    :param position: The field to insert the new column next to, this can be any of the standard column component
      look up options.
    """
    data = JsUtils.jsConvertData(data, None)
    before = JsUtils.jsConvertData(before, None)
    position = JsUtils.jsConvertData(position, None)
    return JsObjects.JsPromise("%s.addColumn(%s, %s, %s)" % (self.varId, data, position, before))

  def addColumns(self, data, before=False, position="", options=None):
    """
 
    :param data:
    :param before:
    :param position:
    :param options:
    """
    data = JsUtils.jsConvertData(data, None)
    before = JsUtils.jsConvertData(before, None)
    position = JsUtils.jsConvertData(position, None)
    options = options or {}
    return JsObjects.JsPromise("%s.forEach(function(row){if(typeof row === 'string'){row = Object.assign(%s, {field: row, title: row})}; %s.addColumn(row, %s, %s)})" % (
      data, options, self.varId, position, before))

  def deleteColumn(self, data):
    """   To permanently remove a column from the table deleteColumn function. This function takes any of the standard
    column component look up options as its first parameter.

    Related Pages:

      http://tabulator.info/docs/4.5/columns#delete
 
    :param data:
    """
    return JsObjects.JsPromise("%s.deleteColumn(%s)" % (self.varId, JsUtils.jsConvertData(data, None)))

  def redraw(self, flag: bool = False):
    """
    This can be done by calling the redraw method.
    For example, to trigger a redraw whenever the viewport width is changed:

    The redraw function also has an optional boolean argument that when set to true triggers a full rerender of
    the table including all data on all rows.

    Related Pages:

      http://tabulator.info/docs/4.5/layout#redraw
 
    :param flag: Boolean. Trigger full rerender including all data and rows
    """
    return JsObjects.JsVoid("%s.redraw(%s)" % (self.varId, JsUtils.jsConvertData(flag, None)))

  def blockRedraw(self):
    """
    To get around this you can use the blockRedraw and restoreRedraw functions to temporarlity disable all table
    redraw actions while you are manipulating the table data.

    Usage::

      table.blockRedraw(); //block table redrawing

    Related Pages:

      http://tabulator.info/docs/4.5/release#redraw-block
    """
    return JsObjects.JsVoid("%s.blockRedraw()" % self.varId)

  def restoreRedraw(self):
    """

    Usage::

      table.restoreRedraw(); //restore table redrawing

    Related Pages:

      http://tabulator.info/docs/4.5/release#redraw-block
    """
    return JsObjects.JsVoid("%s.restoreRedraw()" % self.varId)

  def setSort(self, data):
    """

    Usage::

      table.setSort([{column:"age", dir:"asc"}]);

    Related Pages:

      http://tabulator.info/docs/4.0/sort
 
    :param data:
    """
    return JsObjects.JsVoid("%s.setSort(%s)" % (self.varId, JsUtils.jsConvertData(data, None)))

  def setColumns(self, data: types.JS_DATA_TYPES):
    """
 
    :param data:
    """
    return JsObjects.JsVoid('''
      %(htmlCode)s_columns = %(cols)s;
      %(htmlCode)s_columns.forEach(function(col){
        if (typeof col.headerFilterFunc === 'string'){
          col.headerFilterFunc = eval(col.headerFilterFunc);}})
      %(varId)s.setColumns(%(htmlCode)s_columns)''' % {
        "htmlCode": self.component.htmlCode, "varId": self.varId, "cols": JsUtils.jsConvertData(data, None)})

  def getGroups(self, data=None):
    """
    You can use the getGroups function to retrieve an array of all the first level Group Components in the table.

    Usage::

      var cols = table.getColumns()

    Related Pages:

      http://tabulator.info/docs/4.0/group
 
    :param data: To get a structured array of Column Components that includes column groups, pass a value of true as
      an argument
    """
    if data is not None:
      return JsObjects.JsObject.JsObject("%s.getGroups(%s)" % (self.varId, JsUtils.jsConvertData(data, None)))

    return JsObjects.JsObject.JsObject("%s.getGroups()" % self.varId)

  def clearData(self):
    """
    You can remove all data from the table using the clearData function:

    Usage::

      table.clearData()

    Related Pages:

      http://tabulator.info/docs/4.0/update
    """
    return JsObjects.JsVoid("%s.clearData()" % self.varId)

  def showColumn(self, column: str):
    """
    You can show a hidden column at any point using the showColumn function.
    Pass the field name of the column you wish to show as the first parameter of the function.

    Related Pages:

      http://tabulator.info/docs/4.0/columns
 
    :param column: The column name to be displayed.
    """
    return JsObjects.JsPromise("%s.showColumn(%s)" % (self.varId, JsUtils.jsConvertData(column, None)))

  def showColumns(self, columns: list):
    """
    You can show a hidden columns at any point using the showColumn function. Pass the field name of the column you
    wish to show as the first parameter of the function.

    Usage::

      table.showColumna("name")

    Related Pages:

      ttp://tabulator.info/docs/4.0/columns
 
    :param columns: The column names to be displayed
    """
    return JsObjects.JsPromise(
      "%s.forEach(function(c){%s.showColumn(c)})" % (JsUtils.jsConvertData(columns, None), self.varId))

  def setData(self, data):
    """
 
    :param data:
    """
    return JsObjects.JsVoid("%s.setData(%s)" % (self.varId, JsUtils.jsConvertData(data, None)))

  def setDataFromArray(self, data, header=None, formatters=None):
    """
    Load a table from an array using the first row as header.
 
    :param data:
    :param header:
    :param formatters:
    """
    formatters = JsUtils.jsConvertData(formatters, None)
    data = JsUtils.jsConvertData(data, None)
    if header is not None:
      header = JsUtils.jsConvertData(header, None)
      return '''var dataContemt = %(data)s; var resultContent = []; var header = %(header)s; var headerIndices = []; var formatters = %(formatters)s;
if (formatters != null){
  for (var key in formatters){ if (formatters.hasOwnProperty(key)) {formatters[key] = eval(formatters[key])}}}
dataContemt[0].forEach(function(c, i){ if(header.includes(c)){ headerIndices.push(i); var h = {title: c, field: c}; %(varId)s.deleteColumn(c); %(varId)s.addColumn(h)}})
dataContemt.slice(1).forEach(function(v){var row = {}; header.forEach(function(c, i){row[c] = v[headerIndices[i]]})
if (formatters != null){for (var key in formatters){ row[key] = formatters[key](row)}}
resultContent.push(row)}); %(varId)s.setData(resultContent)''' % {
        "header": header, "varId": self.varId, "formatters": formatters, "data": data}

    return '''var dataContemt = %(data)s; var resultContent = []; var formatters = %(formatters)s;
      if (formatters != null){
         for (var key in formatters){ if (formatters.hasOwnProperty(key)) {formatters[key] = eval(formatters[key])}}}
      dataContemt[0].forEach(function(c){var h = {title: c, field: c}; %(varId)s.addColumn(h)})
      dataContemt.slice(1).forEach(function(v){var row = {}; dataContemt[0].forEach(function(c, i){row[c] = v[i]})
         if (formatters != null){for (var key in formatters){ row[key] = formatters[key](row)}}
         resultContent.push(row)}); %(varId)s.setData(resultContent)''' % {
      "varId": self.varId, "formatters": formatters, "data": data}

  def replaceData(self, data: types.JS_DATA_TYPES = None):
    """
    The replaceData function lets you silently replace all data in the table without updating scroll position,
    sort or filtering, and without triggering the ajax loading popup.

    Usage::

      table.replaceData() //trigger reload of ajax data from ajaxURL property.
 
    :param data:
    """
    if data is None:
      return JsObjects.JsObject.JsObject("%s.replaceData()" % self.varId, component=self.component, page=self.page)

    return JsObjects.JsObject.JsObject(
      "%s.replaceData(%s)" % (self.varId, JsUtils.jsConvertData(data, None)), component=self.component, page=self.page)

  def getData(self) -> JsObjects.JsObject.JsObject:
    """
    You can retrieve the data stored in the table using the getData function.
    """
    return JsObjects.JsObject.JsObject("%s.getData()" % self.varId, component=self.component, page=self.page)

  @property
  def rowContextMenu(self) -> TabRowContextMenu:
    return TabRowContextMenu(self.component, selector=self.varId, page=self.page)

  def deselectRow(self, row_id: int):
    """   To deselect a specific row you can pass any of the standard row component look up options into the first argument
    of the function. If you leave the argument blank you will deselect all rows.

    Related Pages:

      http://tabulator.info/docs/4.0/select
 
    :param row_id: The row ID.
    """
    return JsObjects.JsVoid("%s.deselectRow(%s)" % (self.varId, row_id))

  def getSelectedData(self) -> JsObjects.JsArray.JsArray:
    """   To get the data objects for the selected rows you can use the getSelectedData function.

    This will return an array of the selected rows data objects in the order in which they were selected.

    Related Pages:

      http://tabulator.info/docs/4.0/select
    """
    return JsObjects.JsArray.JsArray("%s.getSelectedData()" % self.varId, page=self.page, component=self.component)

  @property
  def _(self):
    """
    Tabulator standard components.

    Usage::

      table.js._.cell.getRow()
    """
    return _Export()


class _Export:

  @property
  def cell(self) -> CellComponent:
    """
    Cell component for the edited cell.

    Usage::

      page.js.console.log(pk.js_libs.tabulator.cell.getRow().getData()),
    """
    return CellComponent(selector="cell", set_var=False)

  @property
  def row(self) -> RowComponent:
    return RowComponent(selector="row", set_var=False)

  @property
  def value(self):
    """
    The data being changed.
    """
    return JsObjects.JsObjects.get("value")

  @property
  def data(self):
    """
    The data being changed.
    """
    return JsObjects.JsObjects.get("data")

  @property
  def rowData(self):
    """
    The row data from the paste parser.
    """
    return JsObjects.JsObjects.get("row")

  @property
  def rows(self) -> JsObjects.JsArray.JsArray:
    """
    The row components from the paste action (this will be empty if the "replace" action is used).
    """
    return JsObjects.JsArray.JsArray("rows")

  @property
  def clipboard(self):
    """
    The clipboard string.
    """
    return JsObjects.JsObjects.get("clipboard")
