"""
Javascript Interface to the Tabulator Module

http://tabulator.info/docs/4.4/components

TODO: Add tree event on RowComponent
"""

from epyk.core.js import JsUtils
from epyk.core.js.objects import JsNodeDom
from epyk.core.js.primitives import JsObjects
from epyk.core.js.packages import JsQuery


class Navigation(object):
  def __init__(self, cellSelector):
    self._selector = cellSelector
    self._js = []

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


class CellComponent(object):
  def __init__(self, cellSelector):
    self._selector = cellSelector
    self._js = []

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


class GroupComponent(object):
  def __init__(self, grpSelector):
    self._selector = grpSelector
    self._js = []

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


class ColumnComponent(object):
  def __init__(self, colSelector):
    self._selector = colSelector
    self._js = []

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
    return JsObjects.JsObject.JsObject("%s.delete()" % self.toStr())

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


class RowComponent(object):
  def __init__(self, rowSelector):
    self._selector = rowSelector
    self._js = []

  def update(self, jsData):
    """
    You can update the data in the row using the update function. You should pass an object to the function containing any fields you wish to update

    :return:
    """
    jsData = JsUtils.jsConvertData(jsData, None)
    return JsObjects.JsObject.JsObject("%s.update(%s)" % (self.toStr(), jsData))

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

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.delete()" % self.toStr())

  def scrollTo(self):
    """
    The scrollTo function will scroll the table to the row if it passes the current filters.

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.scrollTo()" % self.toStr())

  def pageTo(self):
    """
    The pageTo function will load the page for the row if it passes the current filters.

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.pageTo()" % self.toStr())

  def move(self, jsIndex, jsBoolean=True):
    """
    You can move a row next to another row using the move function.

    :param jsIndex:
    :param jsBoolean:
    :return:
    """
    jsIndex = JsUtils.jsConvertData(jsIndex, None)
    jsBoolean = JsUtils.jsConvertData(jsBoolean, None)
    return JsObjects.JsObject.JsObject("%s.move(%s, %s)" % (self.toStr(), jsIndex, jsBoolean))

  def update(self, jsData):
    """
    You can update the data in the row using the update function.
    You should pass an object to the function containing any fields you wish to update.

    :return:
    """
    jsData = JsUtils.jsConvertData(jsData, None)
    return JsObjects.JsObject.JsObject("%s.update(%s)" % (self.toStr(), jsData))

  def select(self):
    """
    The select function will select the current row.

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.select()" % self.toStr())

  def deselect(self):
    """
    The deselect function will deselect the current row.

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.deselect()" % self.toStr())

  def toggleSelect(self):
    """
    The toggleSelect function will toggle the selected state the current row.

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.toggleSelect()" % self.toStr())

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
    return JsObjects.JsObject.JsObject("%s.reformat()" % self.toStr())

  def freeze(self):
    """
    You can freeze a row at the top of the table by calling the freeze function. This will insert the row above the scrolling portion of the table in the table header.

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.freeze()" % self.toStr())

  def unfreeze(self):
    """
    A frozen row can be unfrozen using the unfreeze function. This will remove the row from the table header and re-insert it back in the table.

    :return:
    """
    return JsObjects.JsObject.JsObject("%s.unfreeze()" % self.toStr())

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


class Tabulator(object):

  class __internal(object):
    jsTableId, _context, jsImports, cssImport = 'table', {}, set([]), set([])

  def __init__(self, src=None):
    self.src = src if src is not None else self.__internal()
    self.src.jsImports.add('tabulator')
    self.src.cssImport.add('tabulator')
    self._selector = self.src.jsTableId
    self._js = []

  def setGroupBy(self):
    pass

  def setGroupStartOpen(self):
    pass

  def deleteRow(self):
    pass

  def addRow(self):
    """

    Documentation
    http://tabulator.info/docs/4.3/update#addrow

    :return:
    """

  def updateRow(self):
    pass

  def updateOrAddRow(self):
    pass

  def getRow(self, jsIndex):
    """

    :return:
    """
    return RowComponent("%s.getRow(%s)" % (self.toStr(), jsIndex))

  def getSelectedRows(self):
    """
    To get the RowComponent's for the selected rows at any time you can use the getSelectedRows function.

    Documentation
    http://tabulator.info/docs/4.0/select

    :return:
    """
    return JsObjects.JsArray.JsArray("%s.getSelectedRows()" % self.src.jsTableId)

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

  def getColumns(self):
    pass

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
    pass

  def showColumn(self, columns):
    """

    :param columns:
    :return:
    """

    pass

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
