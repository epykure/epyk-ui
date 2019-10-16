"""
Javascript Interface to the Tabulator Module

http://tabulator.info/docs/4.4/components

TODO: Add tree event on RowComponent
"""

from epyk.core.js import JsUtils
from epyk.core.js.objects import JsNodeDom
from epyk.core.js.primitives import JsObjects
from epyk.core.js.packages import JsPackage


class Navigation(JsPackage):
  def prev(self):
    """
    next editable cell on the left, if none available move to the right most editable cell on the row above

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.prev()" % self.toStr())

  def next(self):
    """
    next editable cell on the right, if none available move to left most editable cell on the row below

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.next()" % self.toStr())

  def left(self):
    """
    next editable cell on the left, return false if none available on row

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.left()" % self.toStr())

  def right(self):
    """
    next editable cell on the right, return false if none available on row

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.right()" % self.toStr())

  def up(self):
    """
    move to the same cell in the row above

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.up()" % self.toStr())

  def down(self):
    """
    move to the same cell in the row below

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.down()" % self.toStr())


  def toStr(self):
    """
    Javascript representation

    :return: Return the Javascript String
    """
    if self._selector is None:
      raise Exception("Selector not defined, use this() or new() first")

    if len(self._js) == 0:
      return self._selector

    strData = "%(jqId)s.%(items)s" % {'jqId': self._selector, 'items': ".".join(self._js)}
    self._js = [] # empty the stack
    return JsObjects.JsObject.JsObject.get(strData)


class CellComponent(JsPackage):
  lib_alias = {"js": "tabulator", 'css': "tabulator"}
  lib_selector = "cell"

  def getElement(self):
    """
    The getElement function returns the DOM node for the cell.

    Documentation
    http://tabulator.info/docs/4.4/components

    :rtype: JsNodeDom.JsDoms
    :return:
    """
    return JsNodeDom.JsDoms(varName="%s.getElement()" % self.toStr())

  def getColumn(self):
    """
    The getColumn function returns the ColumnComponent for the column that contains the cell.

    Documentation
    http://tabulator.info/docs/4.4/components

    :return:
    """
    return ColumnComponent("%s.getColumn()" % self.toStr())

  def getRow(self):
    """
    The getRow function returns the RowComponent for the row that contains the cell.

    Documentation
    http://tabulator.info/docs/4.4/components

    :return:
    """
    return RowComponent("%s.getRow()" % self.toStr())

  def getData(self):
    """
    The getData function returns the data for the row that contains the cell.

    Documentation
    http://tabulator.info/docs/4.4/components

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.getData()" % self.toStr())

  def getField(self):
    """
    The getField function returns the field name for the column that contains the cell.

    Documentation
    http://tabulator.info/docs/4.4/components

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.getField()" % self.toStr())

  def restoreOldValue(self):
    """
    The restoreOldValue reverts the value of the cell back to its previous value, without triggering any of the cell edit callbacks.

    Documentation
    http://tabulator.info/docs/4.4/components

    :return:
    """
    return JsObjects.JsString.JsString("%s.restoreOldValue()" % self.toStr())

  def getOldValue(self):
    """
    The getOldValue function returns the previous value of the cell. Very usefull in the event of cell update callbacks.

    Documentation
    http://tabulator.info/docs/3.5#component-cell

    :return:
    """
    return JsObjects.JsString.JsString("%s.restoreOldValue()" % self.toStr())

  def getValue(self):
    """
    The getValue function returns the current value for the cell.

    Documentation
    http://tabulator.info/docs/3.5#component-cell

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.getValue()" % self.toStr())

  def setValue(self, jsString, jsBoolean=True):
    """
    You can change the value of the cell using the setValue function.
    The first parameter should be the new value for the cell, the second optional parameter will apply the column mutators to the value when set to true (default = true).

    Documentation
    http://tabulator.info/docs/4.4/components

    :return:
    """
    key = JsUtils.jsConvertData(jsString, None)
    value = JsUtils.jsConvertData(jsBoolean, None)
    return JsObjects.JsObject.JsObject("%s.setValue(%s, %s)" % (self.toStr(), key, value))

  def checkHeight(self):
    """
    If you are making manual adjustments to elements contained withing the cell, or the cell itself, it may sometimes be necessary to recalculate the height of all the cells in the row to make sure they remain aligned

    Documentation
    http://tabulator.info/docs/4.4/components

    :return:
    """
    return JsObjects.JsBoolean.JsBoolean("%s.checkHeight()" % self.toStr())

  def edit(self, jsBoolean=True):
    """
    You and programatically cause a cell to open its editor element using the edit function.

    Documentation
    http://tabulator.info/docs/4.4/components

    :return:
    """
    jsBoolean = JsUtils.jsConvertData(jsBoolean, None)
    return JsObjects.JsObject.JsObject("%s.edit(%s)" % (self.toStr(), jsBoolean))

  def cancelEdit(self):
    """
    You and programatically cancel a cell edit that is currently in progress by calling the cancelEdit function.

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.cancelEdit()" % self.toStr())

  def nav(self):
    """
    When a cell is being edited it is possible to move the editor focus from the current cell to one if its neighbours
    :return:
    """
    return Navigation("%s.nav()" % self.toStr())


class GroupComponent(JsPackage):
  def getElement(self):
    """
    The getElement function returns the DOM node for the group header.

    Documentation
    http://tabulator.info/docs/3.5#component-cell

    :return:
    """
    return JsNodeDom.JsDoms(varName="%s.getElement()" % self.toStr())

  def getKey(self):
    """
    The getKey function returns the unique key that is shared between all rows in this group.

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.getKey()" % self.toStr())

  def getField(self):
    """
    The getField function returns the string of the field that all rows in this group have been grouped by. (if a function is used to group the rows rather than a field, this function will return false)

    :return:
    """
    return JsObjects.JsString.JsString("%s.getField()" % self.toStr())

  def getRows(self):
    """
    The getRows function returns an array of RowComponent objects, one for each row in the group.

    :return:
    """
    return RowComponent("%s.getRows()" % self.toStr())

  def getSubGroups(self):
    """
    The getParentGroup function returns the GroupComponent for the parent group of this group. if no parent exists, this function will return false

    :return:
    """
    return JsObjects.JsArray.JsArray("%s.getParentGroup()" % self.toStr())

  def getVisibility(self):
    """
    The getVisibility function returns a boolean to show if the group is visible, a value of true means it is visible.

    :return:
    """
    return JsObjects.JsBoolean.JsBoolean("%s.getVisibility()" % self.toStr())

  def show(self):
    """
    The show function shows the group if it is hidden.

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.show()" % self.toStr())

  def hide(self):
    """
    The hide function hides the group if it is visible.

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.hide()" % self.toStr())

  def toggle(self):
    """
    The toggle function toggles the visibility of the group, switching between hidden and visible.

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.toggle()" % self.toStr())

  def getTable(self):
    """
    The getTable function returns the Tabulator object for the table containing the group.

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.getTable()" % self.toStr())

  def getParentColumn(self):
    """
    The getParentGroup function returns the GroupComponent for the parent group of this group. if no parent exists, this function will return false

    :return:
    """
    return GroupComponent("%s.getParentGroup()" % self.toStr())


class ColumnComponent(JsPackage):
  lib_alias = {"js": "tabulator", 'css': "tabulator"}
  lib_selector = "column"

  def getElement(self):
    """
    The getElement function returns the DOM node for the column.

    :return:
    """
    return JsNodeDom.JsDoms("%s.getElement()" % self.toStr())

  def getTable(self):
    """
    The getTable function returns the Tabulator object for the table containing the column.

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.getTable()" % self.toStr())

  def getDefinition(self):
    """
    The getDefinition function returns the column definition object for the column.

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.getDefinition()" % self.toStr())

  def getField(self):
    """
    The getField function returns the field name for the column.

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.getField()" % self.toStr())

  def getCells(self):
    """
    The getCells function returns an array of CellComponent objects, one for each cell in the column.

    :return:
    """
    return CellComponent("%s.getCells()" % self.toStr())

  def getNextColumn(self):
    """
    The getNextColumn function returns the Column Component for the next visible column in the table, if there is no next column it will return a value of false.

    :return:
    """
    return ColumnComponent("%s.getNextColumn()" % self.toStr())

  def getPrevColumn(self):
    """
    The getPrevColumn function returns the Column Component for the previous visible column in the table, if there is no previous column it will return a value of false.

    :return:
    """
    return ColumnComponent("%s.getPrevColumn()" % self.toStr())

  def getVisibility(self):
    """
    The getVisibility function returns a boolean to show if the column is visible, a value of true means it is visible.

    :return:
    """
    return JsObjects.JsBoolean.JsBoolean("%s.getVisibility()" % self.toStr())

  def show(self):
    """
    The show function shows the column if it is hidden.

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.show()" % self.toStr())

  def hide(self):
    """
    The hide function hides the column if it is visible.

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.hide()" % self.toStr())

  def toggle(self):
    """
    The toggle function toggles the visibility of the column, switching between hidden and visible.

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.hide()" % self.toStr())

  def delete(self):
    """
    The delete function deletes the column, removing it from the table

    :return:
    """
    return self.fnc_closure("delete()")

  def scrollTo(self):
    """
    The scrollTo function will scroll the table to the column if it is visible.

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.scrollTo()" % self.toStr())

  def move(self, jsString, jsBoolean):
    """
    ou can move a column next to another column using the move function.

    :return:
    """
    jsString = JsUtils.jsConvertData(jsString, None)
    jsBoolean = JsUtils.jsConvertData(jsBoolean, None)
    return JsObjects.JsObject.JsObject("%s.move(%s, %s)" % (self.toStr(), jsString, jsBoolean))

  def getSubColumns(self):
    """
    The getSubColumns function returns an array of ColumnComponent objects, one for each sub column of this column.

    :return:
    """
    return ColumnComponent("%s.getSubColumns()" % self.toStr())

  def getParentColumn(self):
    """
    The getParentColumn function returns the ColumnComponent for the parent column of this column. if no parent exists, this function will return false

    :return:
    """
    return ColumnComponent("%s.getParentColumn()" % self.toStr())

  def headerFilterFocus(self):
    """
    The headerFilterFocus function will place focus on the header filter element for this column if it exists.

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.headerFilterFocus()" % self.toStr())

  def setHeaderFilterValue(self, jsString):
    """
    The setHeaderFilterValue function set the value of the columns header filter element to the value provided in the first argument.

    :param jsString:
    :return:
    """
    jsString = JsUtils.jsConvertData(jsString, None)
    return JsObjects.JsObject.JsObject("%s.setHeaderFilterValue(%s)" % (self.toStr(), jsString))

  def reloadHeaderFilter(self):
    """
    The reloadHeaderFilter function rebuilds the header filter element, updating any params passed into the editor used to generate the filter.

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.reloadHeaderFilter()" % self.toStr())


class ColumnComponents(JsPackage):
  lib_selector = "column"

  def forEach(self, jsFnc):
    """

    :param jsFnc:
    :return:
    """
    return self.fnc_closure("forEach(function(rec){%s})" % JsUtils.jsConvertFncs(jsFnc, toStr=True))

  @property
  def table(self):
    """
    Return to the parent table
    """
    self._parent._js.append([])
    return self._parent


class RowComponent(JsPackage):
  lib_selector = "row"

  def update(self, data):
    """
    You can update the data in the row using the update function.
    You should pass an object to the function containing any fields you wish to update

    Documentation
    http://www.tabulator.info/docs/4.0/update

    :param data: Dictionary with the data to override

    :return:
    """
    data = JsUtils.jsConvertData(data, None)
    return self.fnc_closure("update(%s)" % data)

  def getData(self):
    """
    The getData function returns the data object for the row.

    Documentation
    http://tabulator.info/docs/4.4/components

    :return:
    """
    return JsObjects.JsArray.JsArray("%s.getData()" % self.toStr())

  def getElement(self):
    """
    The getElement function returns the DOM node for the row.

    Documentation
    http://tabulator.info/docs/4.4/components

    """
    return JsNodeDom.JsDoms(varName="%s.getElement()" % self.toStr())

  def getCells(self):
    """
    The getCells function returns an array of CellComponent objects, one for each cell in the row.

    :return:
    """
    return JsObjects.JsArray.JsArray("%s.getCells()" % self.toStr())

  def getCell(self):
    """
    The getCell function returns the CellComponent for the specified column from this row.

    :return:
    """
    return CellComponent("%s.getCell()" % self.toStr())

  def getIndex(self):
    """
    The getIndex function returns the index value for the row. (this is the value from the defined index column, NOT the row's position in the table)

    :return:
    """
    return JsObjects.JsNumber.JsNumber("%s.getIndex()" % self.toStr())

  def getPosition(self, jsBoolean=True):
    """
    Use the getPosition function to retrieve the numerical position of a row in the table.
    By default this will return the position of the row in all data, including data currently filtered out of the table.

    :return:
    """
    jsBoolean = JsUtils.jsConvertData(jsBoolean, None)
    return JsObjects.JsNumber.JsNumber("%s.getPosition(%s)" % (self.toStr(), jsBoolean))

  def getGroup(self):
    """
    When using grouped rows, you can retrieve the group component for the current row using the getGroup function.

    :return:
    """
    return GroupComponent("%s.getGroup()" % self.toStr())

  def delete(self):
    """
    The delete function deletes the row, removing its data from the table

    Documentation
    http://www.tabulator.info/docs/4.0/update

    :return:
    """
    return self.fnc_closure("delete()")

  def scrollTo(self):
    """
    The scrollTo function will scroll the table to the row if it passes the current filters.

    :return:
    """
    return self.fnc_closure("scrollTo()")

  def pageTo(self):
    """
    The pageTo function will load the page for the row if it passes the current filters.

    :return:
    """
    return self.fnc_closure("pageTo()")

  def move(self, jsIndex, jsBoolean=True):
    """
    You can move a row next to another row using the move function.

    :param jsIndex:
    :param jsBoolean:
    :return:
    """
    jsIndex = JsUtils.jsConvertData(jsIndex, None)
    jsBoolean = JsUtils.jsConvertData(jsBoolean, None)
    return self.fnc_closure("move(%s, %s)" % (jsIndex, jsBoolean))

  def select(self):
    """
    The select function will select the current row.

    :return:
    """
    return self.fnc_closure("select()")

  def deselect(self):
    """
    The deselect function will deselect the current row.

    :return:
    """
    return self.fnc_closure("deselect()")

  def toggleSelect(self):
    """
    The toggleSelect function will toggle the selected state the current row.

    :return:
    """
    return self.fnc_closure("toggleSelect()")

  def isSelected(self):
    """
    The isSelected function will return a boolean representing the current selected state of the row.

    :return:
    """
    return JsObjects.JsBoolean.JsBoolean("%s.isSelected()" % self.toStr())

  def normalizeHeight(self):
    """
    If you are making manual adjustments to elements contained within the row, it may sometimes be necessary to recalculate the height of all the cells in the row to make sure they remain aligned

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.normalizeHeight()" % self.toStr())

  def reformat(self):
    """
    If you want to re-format a row once it has been rendered to re-trigger the cell formatters and the rowFormatter callback, Call the reformat function.

    :return:
    """
    return self.fnc_closure("reformat()")

  def freeze(self):
    """
    You can freeze a row at the top of the table by calling the freeze function. This will insert the row above the scrolling portion of the table in the table header.

    :return:
    """
    return self.fnc_closure("freeze()")

  def unfreeze(self):
    """
    A frozen row can be unfrozen using the unfreeze function. This will remove the row from the table header and re-insert it back in the table.

    :return:
    """
    return self.fnc_closure("unfreeze()")


class Tabulator(JsPackage):
  lib_alias = {"js": "tabulator", 'css': "tabulator"}

  def setGroupBy(self, column):
    """
    You can use the setGroupBy function to change the fields that rows are grouped by.
    This function has one argument and takes the same values as passed to the groupBy setup option.

    Documentation
    http://www.tabulator.info/docs/4.1/group

    :param column:

    :return:
    """
    return self.fnc_closure("setGroupBy(%s)" % JsUtils.jsConvertData(column, None))

  def setGroupStartOpen(self, flag):
    """
    You can use the setGroupStartOpen function to change the default open state of groups.
    This function has one argument and takes the same values as passed to the groupStartOpen setup option.

    Documentation
    http://www.tabulator.info/docs/4.1/group

    :param flag:

    :return:
    """
    return self.fnc_closure("setGroupStartOpen(%s)" % JsUtils.jsConvertData(flag, None))

  def setGroupHeader(self, jsFnc):
    """
    You can use the setGroupHeader function to change the header generation function for each group.
    This function has one argument and takes the same values as passed to the groupHeader setup option.

    Documentation
    http://www.tabulator.info/docs/4.1/group

    :param jsFnc:

    :return:
    """
    return self.fnc_closure("setGroupHeader(function(value, count, data, group){%s})" % JsUtils.jsConvertFncs(jsFnc, toStr=True))

  def deleteRow(self, n):
    """
    You can delete any row in the table using the deleteRow function.
    The first argument is the row you want to delete, it will take any of the standard row component look up options.

    documentation
    http://www.tabulator.info/docs/4.0/update

    :param n:

    :return:
    """
    return self.fnc_closure("deleteRow(%s)" % n)

  def addRow(self, data, flag=False):
    """
    You can add a row to the table using the addRow function.

    The first argument should be a row data object. If you do not pass data for a column, it will be left empty.
    To create a blank row (ie for a user to fill in), pass an empty object to the function.

    The second argument is optional and determines whether the row is added to the top or bottom of the table.
    A value of true will add the row to the top of the table, a value of false will add the row to the bottom of the table.
    If the parameter is not set the row will be placed according to the addRowPos global option.

    Documentation
    http://tabulator.info/docs/4.3/update#addrow

    :param data:
    :param flag:

    :return:
    """
    data = JsUtils.jsConvertData(data, None)
    flag = JsUtils.jsConvertData(flag, None)
    return self.fnc_closure("addRow(%s, %s)" % (data, flag))

  def updateRow(self, rowId, data):
    """
    The updateRow and row.updatemethods return a promise,
    this can be used to run any other commands that have to be run after the data has been loaded into the table.

    Documentation
    http://www.tabulator.info/docs/4.0/update

    :param rowId:
    :param data:

    :return:
    """
    return self.fnc_closure("updateRow(%s, %s)" % (rowId, JsUtils.jsConvertData(data, None)))

  def updateOrAddRow(self, rowId, data):
    """
    If you don't know whether a row already exists you can use the updateOrAddRow function.
    This will check if a row with a matching index exists, if it does it will update it, if not it will add a new row with that data

    Documentation
    http://www.tabulator.info/docs/4.0/update

    :param rowId:
    :param data:

    :return:
    """
    return self.fnc_closure("updateOrAddRow(%s, %s)" % (rowId, JsUtils.jsConvertData(data, None)))

  def getRow(self, jsIndex):
    """
    Get the Row component
    """
    row = RowComponent(self.src, selector="getRow(%s)" % jsIndex, setVar=False, parent=self)
    self.fnc(row)
    return row

  def getSelectedRows(self):
    """
    To get the RowComponent's for the selected rows at any time you can use the getSelectedRows function.

    Documentation
    http://tabulator.info/docs/4.0/select

    :return:
    """
    return JsObjects.JsArray.JsArray("%s.getSelectedRows()" % self.toStr())

  def getRows(self):
    pass

  def getRowPosition(self):
    pass

  def getRowFromPosition(self):
    pass

  def toggleColumn(self, columns):
    """

    :return:
    """

  def hideColumn(self):
    pass

  @property
  def getColumns(self):
    """
    Get the table columns
    """
    columns = ColumnComponents(self.src, selector="getColumns()", setVar=False, parent=self)
    self.fnc(columns)
    return columns

  def addColumn(self):
    return ""

  def deleteColumn(self):
    pass

  def redraw(self):
    pass

  def setSort(self, jsData):
    """

    :param jsData:
    :return:
    """
    self._js.append("setSort(%s)" % JsUtils.jsConvertData(jsData, None))
    return self

  def getGroups(self):
    pass

  def clearData(self):
    """

    :return:
    """
    return self.fnc_closure("clearData()")

  def showColumn(self, columns):
    """

    :param columns:
    :return:
    """
    columns = JsUtils.jsConvertData(columns, None)
    return self.fnc_closure("showColumn(%s)" % columns)

  def setData(self, jsData):
    """

    :return:
    """

  def replaceData(self, jsData=None):
    """
    The replaceData function lets you silently replace all data in the table without updating scroll position, sort or filtering, and without triggering the ajax loading popup

    table.replaceData() //trigger reload of ajax data from ajaxURL property

    :return:
    """
    if jsData is None:
      return JsObjects.JsObject.JsObject("%s.replaceData()" % self.toStr())

    jsData = JsUtils.jsConvertData(jsData, None)
    return JsObjects.JsObject.JsObject("%s.replaceData(%s)" % (self.toStr(), jsData))

  def getData(self):
    """
    You can retrieve the data stored in the table using the getData function.

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.getData()" % self.toStr())
