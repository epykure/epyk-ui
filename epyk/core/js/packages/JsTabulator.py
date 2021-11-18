"""
Javascript Interface to the Tabulator Module

http://tabulator.info/docs/4.4/components

TODO: Add tree event on RowComponent
"""

from epyk.core.js import JsUtils
from epyk.core.js.objects import JsNodeDom
from epyk.core.js.primitives import JsObjects
from epyk.core.js.packages import JsPackage


class Settings:
  def __init__(self, src, options):
    self.src = src
    self.__headerVisible = True
    self.__ctx = {}

  @property
  def headerVisible(self):
    """
    Description:
    ------------
    By setting the headerVisible option to false you can hide the column headers and present the table as a simple
    list if needed.
    """
    return self.__headerVisible

  @headerVisible.setter
  def headerVisible(self, flag):
    self.__headerVisible = flag
    self.__ctx['headerVisible'] = flag


class Navigation(JsPackage):
  def prev(self):
    """
    Description:
    ------------
    next editable cell on the left, if none available move to the right most editable cell on the row above
    """
    return JsObjects.JsObject.JsObject("%s.prev()" % self.toStr())

  def next(self):
    """
    Description:
    ------------
    next editable cell on the right, if none available move to left most editable cell on the row below.
    """
    return JsObjects.JsObject.JsObject("%s.next()" % self.toStr())

  def left(self):
    """
    Description:
    ------------
    next editable cell on the left, return false if none available on row.
    """
    return JsObjects.JsObject.JsObject("%s.left()" % self.toStr())

  def right(self):
    """
    Description:
    ------------
    next editable cell on the right, return false if none available on row.
    """
    return JsObjects.JsObject.JsObject("%s.right()" % self.toStr())

  def up(self):
    """
    Description:
    ------------
    move to the same cell in the row above.
    """
    return JsObjects.JsObject.JsObject("%s.up()" % self.toStr())

  def down(self):
    """
    Description:
    ------------
    move to the same cell in the row below.
    """
    return JsObjects.JsObject.JsObject("%s.down()" % self.toStr())

  def toStr(self):
    """
    Description:
    ------------
    Javascript representation
    """
    if self._selector is None:
      raise Exception("Selector not defined, use this() or new() first")

    if len(self._js) == 0:
      return self._selector

    strData = "%(jqId)s.%(items)s" % {'jqId': self._selector, 'items': ".".join(self._js)}
    self._js = []   # empty the stack
    return JsObjects.JsObject.JsObject.get(strData)


class CellComponent(JsPackage):
  lib_alias = {"js": "tabulator-tables", 'css': "tabulator-tables"}
  lib_selector = "cell"

  def getElement(self):
    """
    Description:
    ------------
    The getElement function returns the DOM node for the cell.

    Related Pages:

      http://tabulator.info/docs/4.4/components

    :rtype: JsNodeDom.JsDoms
    """
    return JsNodeDom.JsDoms(varName="%s.getElement()" % self.toStr())

  def getColumn(self):
    """
    Description:
    ------------
    The getColumn function returns the ColumnComponent for the column that contains the cell.

    Related Pages:

      http://tabulator.info/docs/4.4/components
    """
    return ColumnComponent(selector="%s.getColumn()" % self.toStr(), setVar=False)

  def getRow(self):
    """
    Description:
    ------------
    The getRow function returns the RowComponent for the row that contains the cell.

    Related Pages:

      http://tabulator.info/docs/4.4/components
    """
    return RowComponent(selector="%s.getRow()" % self.toStr(), setVar=False)

  def getData(self):
    """
    Description:
    ------------
    The getData function returns the data for the row that contains the cell.

    Related Pages:

      http://tabulator.info/docs/4.4/components
    """
    return JsObjects.JsObject.JsObject("%s.getData()" % self.toStr())

  def getField(self):
    """
    Description:
    ------------
    The getField function returns the field name for the column that contains the cell.

    Related Pages:

      http://tabulator.info/docs/4.4/components
    """
    return JsObjects.JsObject.JsObject("%s.getField()" % self.toStr())

  def restoreOldValue(self):
    """
    Description:
    ------------
    The restoreOldValue reverts the value of the cell back to its previous value, without triggering any of the cell
    edit callbacks.

    Related Pages:

      http://tabulator.info/docs/4.4/components
    """
    return JsObjects.JsString.JsString("%s.restoreOldValue()" % self.toStr())

  def getOldValue(self):
    """
    Description:
    ------------
    The getOldValue function returns the previous value of the cell. Very usefull in the event of cell update callbacks.

    Related Pages:

      http://tabulator.info/docs/3.5#component-cell
    """
    return JsObjects.JsString.JsString("%s.restoreOldValue()" % self.toStr())

  def getValue(self):
    """
    Description:
    ------------
    The getValue function returns the current value for the cell.

    Related Pages:

      http://tabulator.info/docs/3.5#component-cell
    """
    return JsObjects.JsObject.JsObject("%s.getValue()" % self.toStr())

  def setValue(self, jsString, jsBoolean=True):
    """
    Description:
    ------------
    You can change the value of the cell using the setValue function.
    The first parameter should be the new value for the cell, the second optional parameter will apply the column
    mutators to the value when set to true (default = true).

    Related Pages:

      http://tabulator.info/docs/4.4/components

    Attributes:
    ----------
    :param jsString:
    :param jsBoolean:
    """
    key = JsUtils.jsConvertData(jsString, None)
    value = JsUtils.jsConvertData(jsBoolean, None)
    return JsObjects.JsObject.JsObject("%s.setValue(%s, %s)" % (self.toStr(), key, value))

  def checkHeight(self):
    """
    Description:
    ------------
    If you are making manual adjustments to elements contained withing the cell, or the cell itself,
    it may sometimes be necessary to recalculate the height of all the cells in the row to make sure they remain aligned

    Related Pages:

      http://tabulator.info/docs/4.4/components
    """
    return JsObjects.JsBoolean.JsBoolean("%s.checkHeight()" % self.toStr())

  def edit(self, jsBoolean=True):
    """
    Description:
    ------------
    You and programmatically cause a cell to open its editor element using the edit function.

    Related Pages:

      http://tabulator.info/docs/4.4/components

    Attributes:
    ----------
    :param jsBoolean:
    """
    jsBoolean = JsUtils.jsConvertData(jsBoolean, None)
    return JsObjects.JsObject.JsObject("%s.edit(%s)" % (self.toStr(), jsBoolean))

  def cancelEdit(self):
    """
    Description:
    ------------
    You and programmatically cancel a cell edit that is currently in progress by calling the cancelEdit function.
    """
    return JsObjects.JsObject.JsObject("%s.cancelEdit()" % self.toStr())

  def nav(self):
    """
    Description:
    ------------
    When a cell is being edited it is possible to move the editor focus from the current cell to one if its neighbours.
    """
    return Navigation("%s.nav()" % self.toStr())


class GroupComponent(JsPackage):
  def getElement(self):
    """
    Description:
    ------------
    The getElement function returns the DOM node for the group header.

    Related Pages:

      http://tabulator.info/docs/3.5#component-cell
    """
    return JsNodeDom.JsDoms(varName="%s.getElement()" % self.toStr())

  def getKey(self):
    """
    Description:
    ------------
    The getKey function returns the unique key that is shared between all rows in this group.
    """
    return JsObjects.JsObject.JsObject("%s.getKey()" % self.toStr())

  def getField(self):
    """
    Description:
    ------------
    The getField function returns the string of the field that all rows in this group have been grouped by.
    (if a function is used to group the rows rather than a field, this function will return false).
    """
    return JsObjects.JsString.JsString("%s.getField()" % self.toStr())

  def getRows(self):
    """
    Description:
    ------------
    The getRows function returns an array of RowComponent objects, one for each row in the group.
    """
    return RowComponent("%s.getRows()" % self.toStr())

  def getSubGroups(self):
    """
    Description:
    ------------
    The getParentGroup function returns the GroupComponent for the parent group of this group.
    if no parent exists, this function will return false.
    """
    return JsObjects.JsArray.JsArray("%s.getParentGroup()" % self.toStr())

  def getVisibility(self):
    """
    Description:
    ------------
    The getVisibility function returns a boolean to show if the group is visible, a value of true means it is visible.
    """
    return JsObjects.JsBoolean.JsBoolean("%s.getVisibility()" % self.toStr())

  def show(self):
    """
    Description:
    ------------
    The show function shows the group if it is hidden.
    """
    return JsObjects.JsObject.JsObject("%s.show()" % self.toStr())

  def hide(self):
    """
    Description:
    ------------
    The hide function hides the group if it is visible.
    """
    return JsObjects.JsObject.JsObject("%s.hide()" % self.toStr())

  def toggle(self):
    """
    Description:
    ------------
    The toggle function toggles the visibility of the group, switching between hidden and visible.
    """
    return JsObjects.JsObject.JsObject("%s.toggle()" % self.toStr())

  def getTable(self):
    """
    Description:
    ------------
    The getTable function returns the Tabulator object for the table containing the group.
    """
    return JsObjects.JsObject.JsObject("%s.getTable()" % self.toStr())

  def getParentColumn(self):
    """
    Description:
    ------------
    The getParentGroup function returns the GroupComponent for the parent group of this group.
    if no parent exists, this function will return false.
    """
    return GroupComponent("%s.getParentGroup()" % self.toStr())


class ColumnComponent(JsPackage):
  lib_alias = {"js": "tabulator-tables", 'css': "tabulator-tables"}
  lib_selector = "column"

  def getElement(self):
    """
    Description:
    ------------
    The getElement function returns the DOM node for the column.
    """
    return JsNodeDom.JsDoms("%s.getElement()" % self.toStr())

  def getTable(self):
    """
    Description:
    ------------
    The getTable function returns the Tabulator object for the table containing the column.
    """
    return JsObjects.JsObject.JsObject("%s.getTable()" % self.toStr())

  def getDefinition(self):
    """
    Description:
    ------------
    The getDefinition function returns the column definition object for the column.
    """
    return JsObjects.JsObject.JsObject("%s.getDefinition()" % self.toStr())

  def getField(self):
    """
    Description:
    ------------
    The getField function returns the field name for the column.
    """
    return JsObjects.JsObject.JsObject("%s.getField()" % self.toStr())

  def getCells(self):
    """
    Description:
    ------------
    The getCells function returns an array of CellComponent objects, one for each cell in the column.
    """
    return CellComponent("%s.getCells()" % self.toStr())

  def getNextColumn(self):
    """
    Description:
    ------------
    The getNextColumn function returns the Column Component for the next visible column in the table,
    if there is no next column it will return a value of false.
    """
    return ColumnComponent("%s.getNextColumn()" % self.toStr())

  def getPrevColumn(self):
    """
    Description:
    ------------
    The getPrevColumn function returns the Column Component for the previous visible column in the table,
    if there is no previous column it will return a value of false.
    """
    return ColumnComponent("%s.getPrevColumn()" % self.toStr())

  def getVisibility(self):
    """
    Description:
    ------------
    The getVisibility function returns a boolean to show if the column is visible, a value of true means it is visible.
    """
    return JsObjects.JsBoolean.JsBoolean("%s.getVisibility()" % self.toStr())

  def show(self):
    """
    Description:
    ------------
    The show function shows the column if it is hidden.
    """
    return JsObjects.JsObject.JsObject("%s.show()" % self.toStr())

  def hide(self):
    """
    Description:
    ------------
    The hide function hides the column if it is visible.
    """
    return JsObjects.JsObject.JsObject("%s.hide()" % self.toStr())

  def toggle(self):
    """
    Description:
    ------------
    The toggle function toggles the visibility of the column, switching between hidden and visible.

    Related Pages:

      http://tabulator.info/docs/4.5/columns#addColumn
    """
    return JsObjects.JsObject.JsObject("%s.hide()" % self.toStr())

  def delete(self):
    """
    Description:
    ------------
    The delete function deletes the column, removing it from the table.
    """
    return self.fnc_closure_in_promise("delete()")

  def scrollTo(self):
    """
    Description:
    ------------
    The scrollTo function will scroll the table to the column if it is visible.
    """
    return JsObjects.JsObject.JsObject("%s.scrollTo()" % self.toStr())

  def move(self, jsString, jsBoolean):
    """
    Description:
    ------------
    ou can move a column next to another column using the move function.

    Attributes:
    ----------
    :param jsString:
    :param jsBoolean:
    """
    jsString = JsUtils.jsConvertData(jsString, None)
    jsBoolean = JsUtils.jsConvertData(jsBoolean, None)
    return JsObjects.JsObject.JsObject("%s.move(%s, %s)" % (self.toStr(), jsString, jsBoolean))

  def getSubColumns(self):
    """
    Description:
    ------------
    The getSubColumns function returns an array of ColumnComponent objects, one for each sub column of this column.
    """
    return ColumnComponent("%s.getSubColumns()" % self.toStr())

  def getParentColumn(self):
    """
    Description:
    ------------
    The getParentColumn function returns the ColumnComponent for the parent column of this column.
    if no parent exists, this function will return false
    """
    return ColumnComponent("%s.getParentColumn()" % self.toStr())

  def headerFilterFocus(self):
    """
    Description:
    ------------
    The headerFilterFocus function will place focus on the header filter element for this column if it exists.
    """
    return JsObjects.JsObject.JsObject("%s.headerFilterFocus()" % self.toStr())

  def setHeaderFilterValue(self, jsString):
    """
    Description:
    ------------
    The setHeaderFilterValue function set the value of the columns header filter element to the value provided
    in the first argument.

    Attributes:
    ----------
    :param jsString:
    """
    jsString = JsUtils.jsConvertData(jsString, None)
    return JsObjects.JsObject.JsObject("%s.setHeaderFilterValue(%s)" % (self.toStr(), jsString))

  def reloadHeaderFilter(self):
    """
    Description:
    ------------
    The reloadHeaderFilter function rebuilds the header filter element, updating any params passed into the editor
    used to generate the filter.
    """
    return JsObjects.JsObject.JsObject("%s.reloadHeaderFilter()" % self.toStr())


class ColumnComponents(JsPackage):
  lib_selector = "column"

  def forEach(self, jsFnc):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param jsFnc:
    """
    return self.fnc_closure("forEach(function(rec){%s})" % JsUtils.jsConvertFncs(jsFnc, toStr=True))

  @property
  def table(self):
    """
    Description:
    ------------
    Return to the parent table.
    """
    self._parent._js.append([])
    return self._parent

  @property
  def fields(self):
    """
    Description:
    ------------

    """
    return JsObjects.JsArray.JsArray.get("(function(){var columns = []; %s.forEach(function(rec){columns.push(rec.getField())}); return columns})()" % self._selector)

  def rename(self, field=None, title=None, columns=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param field: String.
    :param title:
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

  def update(self, data):
    """
    Description:
    ------------
    You can update the data in the row using the update function.
    You should pass an object to the function containing any fields you wish to update

    Related Pages:

      http://www.tabulator.info/docs/4.0/update

    Attributes:
    ----------
    :param data: Dictionary with the data to override.
    """
    data = JsUtils.jsConvertData(data, None)
    return self.fnc_closure("update(%s)" % data)

  def getData(self):
    """
    Description:
    ------------
    The getData function returns the data object for the row.

    Related Pages:

      http://tabulator.info/docs/4.4/components
    """
    return JsObjects.JsArray.JsArray("%s.getData()" % self.toStr())

  def getElement(self):
    """
    Description:
    ------------
    The getElement function returns the DOM node for the row.

    Related Pages:

      http://tabulator.info/docs/4.4/components

    """
    return JsNodeDom.JsDoms(varName="%s.getElement()" % self.toStr())

  def getCells(self):
    """
    Description:
    ------------
    The getCells function returns an array of CellComponent objects, one for each cell in the row.
    """
    return JsObjects.JsArray.JsArray("%s.getCells()" % self.toStr())

  def getCell(self):
    """
    Description:
    ------------
    The getCell function returns the CellComponent for the specified column from this row.
    """
    return CellComponent("%s.getCell()" % self.toStr())

  def getIndex(self):
    """
    Description:
    ------------
    The getIndex function returns the index value for the row.
    (this is the value from the defined index column, NOT the row's position in the table)
    """
    return JsObjects.JsNumber.JsNumber("%s.getIndex()" % self.toStr())

  def getPosition(self, jsBoolean=True):
    """
    Description:
    ------------
    Use the getPosition function to retrieve the numerical position of a row in the table.
    By default this will return the position of the row in all data, including data currently filtered out of the table.

    Attributes:
    ----------
    :param jsBoolean:
    """
    jsBoolean = JsUtils.jsConvertData(jsBoolean, None)
    return JsObjects.JsNumber.JsNumber("%s.getPosition(%s)" % (self.toStr(), jsBoolean))

  def getGroup(self):
    """
    Description:
    ------------
    When using grouped rows, you can retrieve the group component for the current row using the getGroup function.
    """
    return GroupComponent("%s.getGroup()" % self.toStr())

  def delete(self):
    """
    Description:
    ------------
    The delete function deletes the row, removing its data from the table.

    TODO: Fix the fnc_closure_in_promise implementation

    Related Pages:

      http://www.tabulator.info/docs/4.0/update
    """
    return self.fnc_closure("delete()")

  def scrollTo(self):
    """
    Description:
    ------------
    The scrollTo function will scroll the table to the row if it passes the current filters.
    """
    return self.fnc_closure("scrollTo()")

  def pageTo(self):
    """
    Description:
    ------------
    The pageTo function will load the page for the row if it passes the current filters.
    """
    return self.fnc_closure("pageTo()")

  def move(self, jsIndex, jsBoolean=True):
    """
    Description:
    ------------
    You can move a row next to another row using the move function.

    Attributes:
    ----------
    :param jsIndex:
    :param jsBoolean:
    """
    jsIndex = JsUtils.jsConvertData(jsIndex, None)
    jsBoolean = JsUtils.jsConvertData(jsBoolean, None)
    return self.fnc_closure("move(%s, %s)" % (jsIndex, jsBoolean))

  def select(self):
    """
    Description:
    ------------
    The select function will select the current row.
    """
    return self.fnc_closure("select()")

  def deselect(self):
    """
    Description:
    ------------
    The deselect function will deselect the current row.
    """
    return self.fnc_closure("deselect()")

  def toggleSelect(self):
    """
    Description:
    ------------
    The toggleSelect function will toggle the selected state the current row.
    """
    return self.fnc_closure("toggleSelect()")

  def isSelected(self):
    """
    Description:
    ------------
    The isSelected function will return a boolean representing the current selected state of the row.
    """
    return JsObjects.JsBoolean.JsBoolean("%s.isSelected()" % self.toStr())

  def normalizeHeight(self):
    """
    Description:
    ------------
    If you are making manual adjustments to elements contained within the row,
    it may sometimes be necessary to recalculate the height of all the cells in the row to make sure they remain aligned
    """
    return JsObjects.JsObject.JsObject("%s.normalizeHeight()" % self.toStr())

  def reformat(self):
    """
    Description:
    ------------
    If you want to re-format a row once it has been rendered to re-trigger the cell formatters and the rowFormatter
    callback, Call the reformat function.
    """
    return self.fnc_closure("reformat()")

  def freeze(self):
    """
    Description:
    ------------
    You can freeze a row at the top of the table by calling the freeze function. This will insert the row above
    the scrolling portion of the table in the table header.
    """
    return self.fnc_closure("freeze()")

  def unfreeze(self):
    """
    Description:
    ------------
    A frozen row can be unfrozen using the unfreeze function.
    This will remove the row from the table header and re-insert it back in the table.
    """
    return self.fnc_closure("unfreeze()")


class TabRowContextMenu(JsPackage):
  lib_set_var = False

  def add(self, name, url, icon=None):
    """
    Description:
    ------------
    Add an item to a table context menu.

    TODO: Improve this interface.

    Usage:
    -----

      table.js.rowContextMenu.add("Test", "/test")

    Attributes:
    ----------
    :param name: String. The name of the item in the context menu.
    :param url: String. The service URL. (This service will only return a message).
    :param icon: String. The icon class name.
    """
    js_service = self.src.js.fncs.service()
    if icon is not None:
      return JsObjects.JsVoid("%s.options.rowContextMenu.push({label: '<i class=\"%s\" style=\"margin-right:5px\"></i>%s', action: function(e, row){var data = {row: row.getData(), label: '%s'}; %s('%s', data)} })" % (self.toStr(), icon, name, name, js_service, url))

    return JsObjects.JsVoid("%s.options.rowContextMenu.push({label: '%s', action: function(e, row){var data = {row: row.getData(), label: '%s'}; %s('%s', data)} })" % (self.toStr(), name, name, js_service, url))

  def fromConfig(self, services):
    """
    Description:
    ------------
    Extend the context menu of a table from a configuration object.

    Attributes:
    ----------
    :param services: List. A list of services to be added to the context menu.
    """
    js_service = self.src.js.fncs.service()
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

  def download(self, format, filename, options=None):
    """
    Description:
    -----------

    Related Pages:

      http://tabulator.info/docs/4.0/download

    Attributes:
    ----------
    :param format:
    :param filename:
    :param options:
    """
    if format == "pdf":
      self._parent.jsImports.add("jspdf")
    format = JsUtils.jsConvertData(format, None)
    filename = JsUtils.jsConvertData(filename, None)
    if options is None:
      return JsObjects.JsVoid("%s.download(%s, %s)" % (self.varId, format, filename))

    options = JsUtils.jsConvertData(options, None)
    return JsObjects.JsVoid("%s.download(%s, %s, %s)" % (self.varId, format, filename, options))

  def downloadToTab(self, format):
    """
    Description:
    -----------
    If you want to open the generated file in a new browser tab rather than downloading it straight away, you can use
    the downloadToTab function.
    This is particularly useful with the PDF downloader, as it allows you to preview the resulting PDF
    in a new browser tab

    Related Pages:

      http://tabulator.info/docs/4.8/download

    Attributes:
    ----------
    :param format: String. The output format
    """
    if format == "pdf":
      self._parent.jsImports.add("jspdf")
    format = JsUtils.jsConvertData(format, None)
    return JsObjects.JsVoid("%s.downloadToTab(%s)" % (self.varId, format))

  def copyToClipboard(self, clipboardCopySelector=None, with_header=True):
    """
    Description:
    -----------
    If the table has focus, the copyToClipboard keybinding which is by default set to the ctrl + c key combination,
    will trigger a copy of table to the clipboard, which data is copied depends on the state of the table.

    Related Pages:

      http://tabulator.info/docs/4.6/clipboard

    Attributes:
    ----------
    :param clipboardCopySelector: String. can be table, active, selected, visible, all
    :param with_header: Boolean. Optional. defined if the header are included in the copy
    """
    self._parent.config.clipboard = True
    if clipboardCopySelector is None:
      clipboardCopySelector = 'all'
      clipboardCopySelector = JsUtils.jsConvertData(clipboardCopySelector, None)
    if not with_header:
      return JsObjects.JsVoid("%s.copyToClipboard(%s, %s)" % (
        self.varId, clipboardCopySelector, JsUtils.jsConvertData(with_header, None)))

    return JsObjects.JsVoid("%s.copyToClipboard(%s)" % (self.varId, clipboardCopySelector))

  def previousPage(self):
    """
    Description:
    -----------

    Related Pages:

      http://tabulator.info/docs/4.1/page
    """
    return JsObjects.JsPromise("%s.previousPage()" % self.varId)

  def nextPage(self):
    """
    Description:
    -----------

    http://tabulator.info/docs/4.1/page
    """
    return JsObjects.JsPromise("%s.nextPage()" % self.varId)

  def setPage(self, i):
    """
    Description:
    -----------

    Related Pages:

      http://tabulator.info/docs/4.1/page

    Attributes:
    ----------
    :param i:
    """
    return JsObjects.JsPromise("%s.setPage(%s)" % (self.varId, i))

  def setPageSize(self, i):
    """
    Description:
    -----------

    Related Pages:

      http://tabulator.info/docs/4.1/page

    Attributes:
    ----------
    :param i:
    """
    return JsObjects.JsPromise("%s.setPageSize(%s)" % (self.varId, i))

  def setGroupBy(self, column=None):
    """
    Description:
    -----------
    You can use the setGroupBy function to change the fields that rows are grouped by.
    This function has one argument and takes the same values as passed to the groupBy setup option.

    Related Pages:

      http://www.tabulator.info/docs/4.1/group

    Attributes:
    ----------
    :param column:
    """
    if column is None:
      return JsObjects.JsVoid("%s.setGroupBy()" % (self.varId))

    return JsObjects.JsVoid("%s.setGroupBy(%s)" % (self.varId, JsUtils.jsConvertData(column, None)))

  def setGroupStartOpen(self, flag):
    """
    Description:
    ------------
    You can use the setGroupStartOpen function to change the default open state of groups.
    This function has one argument and takes the same values as passed to the groupStartOpen setup option.

    Related Pages:

      http://www.tabulator.info/docs/4.1/group

    Attributes:
    ----------
    :param flag:
    """
    return JsObjects.JsVoid("%s.setGroupStartOpen(%s)" % (self.varId, JsUtils.jsConvertData(flag, None)))

  def setGroupHeader(self, jsFnc):
    """
    Description:
    ------------
    You can use the setGroupHeader function to change the header generation function for each group.
    This function has one argument and takes the same values as passed to the groupHeader setup option.

    Related Pages:

      http://www.tabulator.info/docs/4.1/group

    Attributes:
    ----------
    :param jsFnc:
    """
    return self.fnc_closure(
      "setGroupHeader(function(value, count, data, group){%s})" % JsUtils.jsConvertFncs(jsFnc, toStr=True))

  def deleteRow(self, n):
    """
    Description:
    ------------
    You can delete any row in the table using the deleteRow function.
    The first argument is the row you want to delete, it will take any of the standard row component look up options.

    Related Pages:

      http://www.tabulator.info/docs/4.0/update

    Attributes:
    ----------
    :param n:
    """
    return JsObjects.JsPromise("%s.deleteRow(%s)" % (self.varId, n))

  def addRow(self, data, flag=False):
    """
    Description:
    ------------
    You can add a row to the table using the addRow function.

    The first argument should be a row data object. If you do not pass data for a column, it will be left empty.
    To create a blank row (ie for a user to fill in), pass an empty object to the function.

    The second argument is optional and determines whether the row is added to the top or bottom of the table.
    A value of true will add the row to the top of the table, a value of false will add the row to the
    bottom of the table.
    If the parameter is not set the row will be placed according to the addRowPos global option.

    Related Pages:

      http://tabulator.info/docs/4.3/update#addrow

    Attributes:
    ----------
    :param data:
    :param flag:
    """
    data = JsUtils.jsConvertData(data, None)
    flag = JsUtils.jsConvertData(flag, None)
    return JsObjects.JsVoid("%s.addRow(%s, %s)" % (self.varId, data, flag))

  def updateRow(self, rowId, data):
    """
    Description:
    ------------
    The updateRow and row.updatemethods return a promise,
    this can be used to run any other commands that have to be run after the data has been loaded into the table.

    Related Pages:

      http://www.tabulator.info/docs/4.0/update

    Attributes:
    ----------
    :param rowId:
    :param data:
    """
    return self.fnc_closure("updateRow(%s, %s)" % (rowId, JsUtils.jsConvertData(data, None)))

  def updateOrAddRow(self, rowId, data):
    """
    Description:
    ------------
    If you don't know whether a row already exists you can use the updateOrAddRow function.
    This will check if a row with a matching index exists, if it does it will update it,
    if not it will add a new row with that data.

    Related Pages:

      http://www.tabulator.info/docs/4.0/update

    Attributes:
    ----------
    :param rowId:
    :param data:
    """
    return self.fnc_closure("updateOrAddRow(%s, %s)" % (rowId, JsUtils.jsConvertData(data, None)))

  def getRow(self, jsIndex):
    """
    Description:
    ------------
    Get the Row component.

    Related Pages:

      http://tabulator.info/docs/4.1/components

    Usage:
    -----

      var row = cell.getRow();

    Attributes:
    ----------
    :param jsIndex:
    """
    row = RowComponent(self.src, selector="getRow(%s)" % jsIndex, setVar=False, parent=self)
    self.fnc(row)
    return row

  def getSelectedRows(self):
    """
    Description:
    ------------
    To get the RowComponent's for the selected rows at any time you can use the getSelectedRows function.

    Related Pages:

      http://tabulator.info/docs/4.0/select
    """
    return JsObjects.JsArray.JsArray("%s.getSelectedRows()" % self.varId)

  def getRows(self):
    """
    Description:
    ------------
    The getRows function returns an array of RowComponent objects, one for each row in the table.

    Usage:
    -----

      rows = table.getRows()

    Related Pages:

      http://tabulator.info/docs/4.1/components
    """
    return JsObjects.JsArray.JsArray("%s.getRows()" % self.varId)

  def getRowPosition(self, row, bool=True):
    """
    Description:
    ------------
    The new getRowPosition function and Row Component getPosition function allow you to retrieve
    the current position of a row in the table.

    Related Pages:

      http://tabulator.info/news

    Attributes:
    ----------
    :param row:
    :param bool:
    """
    return JsObjects.JsNumber.JsNumber("%s.getRowPosition(%s, %s)" % (self.varId, row, bool))

  def getPageSize(self):
    """
    Description:
    ------------

    Related Pages:

      http://tabulator.info/docs/4.1/page
    """
    return JsObjects.JsNumber.JsNumber("%s.getPageSize()" % self.varId)

  def getPage(self):
    """
    Description:
    ------------

    Related Pages:

      http://tabulator.info/docs/4.1/page
    """
    return JsObjects.JsNumber.JsNumber("%s.getPage()" % self.varId)

  def getPageMax(self):
    """
    Description:
    ------------

    Related Pages:

      http://tabulator.info/docs/4.1/page
    """
    return JsObjects.JsNumber.JsNumber("%s.getPageMax()" % self.varId)

  def getRowFromPosition(self, n, bool=True):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param n:
    :param bool:
    """
    bool = JsUtils.jsConvertData(bool, None)
    return JsObjects.JsNumber.JsNumber("%s.getRowFromPosition(%s, %s)" % (self.varId, n, bool))

  def toggleColumn(self, column):
    """
    Description:
    ------------
    You can toggle the visibility of a column at any point using the toggleColumn function.
    Pass the field name of the column you wish to toggle as the first parameter of the function.

    Usage:
    -----

      table.toggleColumn("name")

    Related Pages:

      http://tabulator.info/docs/4.5/columns#addColumn

    Attributes:
    ----------
    :param column:
    """
    column = JsUtils.jsConvertData(column, None)
    return JsObjects.JsPromise("%s.toggleColumn(%s)" % (self.varId, column))

  def hideColumn(self, column):
    """
    Description:
    ------------
    You can hide a visible column at any point using the hideColumn function.
    Pass the field name of the column you wish to hide as the first parameter of the function.

    Usage:
    -----

      table.hideColumn("name")

    Related Pages:

      http://tabulator.info/docs/4.5/columns#addColumn

    Attributes:
    ----------
    :param column:
    """
    column = JsUtils.jsConvertData(column, None)
    return JsObjects.JsPromise("%s.hideColumn(%s)" % (self.varId, column))

  def hideColumns(self, columns):
    """
    Description:
    ------------
    You can hide a visible column at any point using the hideColumn function.
    Pass the field name of the column you wish to hide as the first parameter of the function.

    Usage:
    -----

      table.hideColumn("name")

    Related Pages:

      http://tabulator.info/docs/4.5/columns#addColumn

    Attributes:
    ----------
    :param columns:
    """
    columns = JsUtils.jsConvertData(columns, None)
    return JsObjects.JsPromise("%s.forEach(function(c){%s.hideColumn(c)})" % (columns, self.varId))

  def columns(self, headers=None, rows=None, values=None, options=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param headers:
    :param rows:
    :param values:
    :param options:
    """
    if headers is None and rows is None and values is None:
      raise Exception("Header, rows or values must be defined")

    if headers is not None:
      # If this variable is used it means the definition should be fully supplied and the default style will not be applied
      return JsObjects.JsVoid("%s;%s" % (
        self.getColumns.forEach("rec.delete()").toStr(), self.addColumns(headers, options=options).toStr()))

    if rows is not None or values is not None:
      rows_fields = self._parent.options.get({}, "rows_def").get("fields", [])
      if rows is None and rows_fields:
        values = JsObjects.JsObjects.get(
          "(function(d){var results = []; d.forEach(function(rec){if(typeof rec === 'string'){rec = {'field': rec, 'title': rec}}; results.push( Object.assign(rec, %s))}); return results})(%s)" % (
          JsUtils.jsConvertData(self._parent.options.get({}, "columns_def"), None), values or []))
        return JsObjects.JsVoid("%s;%s" % (self.getColumns.forEach(
          "if(!(%s.includes(rec.getField()))){rec.delete()}" % rows_fields
        ).toStr(), self.addColumns(values).toStr()))
      else:
        rows = JsObjects.JsObjects.get("(function(d){var results = []; d.forEach(function(rec){if(typeof rec === 'string'){rec = {'field': rec, 'title': rec}}; results.push( Object.assign(%s, rec))}); return results})(%s)" % (JsUtils.jsConvertData(self._parent.options.get({}, "rows_def"), None), rows or []))
        values = JsObjects.JsObjects.get("(function(d){var results = []; d.forEach(function(rec){if(typeof rec === 'string'){rec = {'field': rec, 'title': rec}}; results.push( Object.assign(%s, rec))}); return results})(%s)" % (JsUtils.jsConvertData(self._parent.options.get({}, "columns_def"), None), values or []))
        return JsObjects.JsVoid("%s;%s" % (self.getColumns.forEach("rec.delete()").toStr(), "%s + %s" % (self.addColumns(rows).toStr(), self.addColumns(values).toStr())))

  def values(self, jsData, columns=None, options=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsData:
    :param columns:
    :param options:
    """
    if columns is None:
      # Just replace the data in the table
      return self._parent.build(jsData)

    # Change the columns and replace them with the new ones
    return JsUtils.jsConvertFncs(
      [self.columns(values=columns, options=options), self._parent.build(jsData)], toStr=True)

  @property
  def getColumns(self):
    """
    Description:
    ------------
    To get an array of Column Components for the current table setup, call the getColumns function.
    This will only return actual data columns not column groups.

    Usage:
    -----

      var cols = table.getColumns()

    Related Pages:

      http://tabulator.info/docs/4.5/columns#getColumns

    """
    columns = ColumnComponents(self.src, selector="%s.getColumns()" % self.varId, setVar=False, parent=self)
    self.fnc(columns)
    return columns

  def addColumn(self, jsData, before=False, position=""):
    """
    Description:
    -----------
    If you wish to add a single column to the table, you can do this using the addColumn function

    Usage:
    -----

      table.addColumn({"title": "Age", "field": "age"}, True, "name");

    Related Pages:

      http://tabulator.info/docs/4.5/columns#addColumn

    Attributes:
    ----------
    :param jsData: The column definition object for the column you want to add
    :param before: Determines how to position the new column.
                   A value of true will insert the column to the left of existing columns, a value of false will insert it to the right
    :param position: The field to insert the new column next to, this can be any of the standard column component look up options.
    """
    jsData = JsUtils.jsConvertData(jsData, None)
    before = JsUtils.jsConvertData(before, None)
    position = JsUtils.jsConvertData(position, None)
    return JsObjects.JsPromise("%s.addColumn(%s, %s, %s)" % (self.varId, jsData, position, before))

  def addColumns(self, jsData, before=False, position="", options=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsData:
    :param before:
    :param position:
    :param options:
    """
    jsData = JsUtils.jsConvertData(jsData, None)
    before = JsUtils.jsConvertData(before, None)
    position = JsUtils.jsConvertData(position, None)
    options = options or {}
    return JsObjects.JsPromise("%s.forEach(function(row){if(typeof row === 'string'){row = Object.assign(%s, {field: row, title: row})}; %s.addColumn(row, %s, %s)})" % (jsData, options, self.varId, position, before))

  def deleteColumn(self, jsData):
    """
    Description:
    -----------
    To permanently remove a column from the table deleteColumn function. This function takes any of the standard column component look up options as its first parameter.

    Related Pages:

      http://tabulator.info/docs/4.5/columns#delete

    Attributes:
    ----------
    :param jsData:
    """
    return JsObjects.JsPromise("%s.deleteColumn(%s)" % (self.varId, JsUtils.jsConvertData(jsData, None)))

  def redraw(self, jsData=False):
    """
    Description:
    ------------
    This can be done by calling the redraw method.
    For example, to trigger a redraw whenever the viewport width is changed:

    The redraw function also has an optional boolean argument that when set to true triggers a full rerender of
    the table including all data on all rows.

    Related Pages:

      http://tabulator.info/docs/4.5/layout#redraw

    Attributes:
    ----------
    :param jsData: Boolean. Trigger full rerender including all data and rows
    """
    return JsObjects.JsVoid("%s.redraw(%s)" % (self.varId, JsUtils.jsConvertData(jsData, None)))

  def blockRedraw(self):
    """
    Description:
    ------------
    To get around this you can use the blockRedraw and restoreRedraw functions to temporarlity disable all table
    redraw actions while you are manipulating the table data.

    Usage:
    -----

      table.blockRedraw(); //block table redrawing

    Related Pages:

      http://tabulator.info/docs/4.5/release#redraw-block
    """
    return JsObjects.JsVoid("%s.blockRedraw()" % self.varId)

  def restoreRedraw(self):
    """
    Description:
    ------------

    Usage:
    -----

      table.restoreRedraw(); //restore table redrawing

    Related Pages:

      http://tabulator.info/docs/4.5/release#redraw-block
    """
    return JsObjects.JsVoid("%s.restoreRedraw()" % self.varId)

  def setSort(self, jsData):
    """
    Description:
    ------------

    Usage:
    -----

      table.setSort([{column:"age", dir:"asc"}]);

    Related Pages:

      http://tabulator.info/docs/4.0/sort

    Attributes:
    ----------
    :param jsData:
    """
    return JsObjects.JsVoid("%s.setSort(%s)" % (self.varId, JsUtils.jsConvertData(jsData, None)))

  def setColumns(self, jsData):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param jsData:
    """
    return JsObjects.JsVoid('''
      %(htmlCode)s_columns = %(cols)s;
      %(htmlCode)s_columns.forEach(function(col){
        if (typeof col.headerFilterFunc === 'string'){
          col.headerFilterFunc = eval(col.headerFilterFunc);}})
      %(varId)s.setColumns(%(htmlCode)s_columns)''' % {
        "htmlCode": self.component.htmlCode, "varId": self.varId, "cols": JsUtils.jsConvertData(jsData, None)})

  def getGroups(self, jsData=None):
    """
    Description:
    ------------
    You can use the getGroups function to retrieve an array of all the first level Group Components in the table.

    Usage:
    -----

      var cols = table.getColumns()

    Related Pages:

      http://tabulator.info/docs/4.0/group

    Attributes:
    ----------
    :param jsData: To get a structured array of Column Components that includes column groups, pass a value of true as an argument
    """
    if jsData is not None:
      return JsObjects.JsObject.JsObject("%s.getGroups(%s)" % (self.varId, JsUtils.jsConvertData(jsData, None)))

    return JsObjects.JsObject.JsObject("%s.getGroups()" % self.varId)

  def clearData(self):
    """
    Description:
    ------------
    You can remove all data from the table using the clearData function:

    Usage:
    -----

      table.clearData()

    Related Pages:

      http://tabulator.info/docs/4.0/update
    """
    return JsObjects.JsVoid("%s.clearData()" % self.varId)

  def showColumn(self, column):
    """
    Description:
    ------------
    You can show a hidden column at any point using the showColumn function.
    Pass the field name of the column you wish to show as the first parameter of the function.

    Related Pages:

      http://tabulator.info/docs/4.0/columns

    Attributes:
    ----------
    :param column: String. The column name to be displayed.
    """
    return JsObjects.JsPromise("%s.showColumn(%s)" % (self.varId, JsUtils.jsConvertData(column, None)))

  def showColumns(self, columna):
    """
    Description:
    ------------
    You can show a hidden columns at any point using the showColumn function. Pass the field name of the column you
    wish to show as the first parameter of the function.

    Usage:
    -----

      table.showColumna("name")

    Related Pages:

      ttp://tabulator.info/docs/4.0/columns

    Attributes:
    ----------
    :param columna: List. The column names to be displayed
    """
    return JsObjects.JsPromise(
      "%s.forEach(function(c){%s.showColumn(c)})" % (JsUtils.jsConvertData(columna, None), self.varId))

  def setData(self, data):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param data:
    """
    return JsObjects.JsVoid("%s.setData(%s)" % (self.varId, JsUtils.jsConvertData(data, None)))

  def setDataFromArray(self, jsData, header=None, formatters=None):
    """
    Description:
    ------------
    Load a table from an array using the first row as header.

    Attributes:
    ----------
    :param jsData:
    :param header:
    :param formatters:
    """
    formatters = JsUtils.jsConvertData(formatters, None)
    jsData = JsUtils.jsConvertData(jsData, None)
    if header is not None:
      header = JsUtils.jsConvertData(header, None)
      return '''var dataContemt = %(data)s; var resultContent = []; var header = %(header)s; var headerIndices = []; var formatters = %(formatters)s;
            if (formatters != null){
              for (var key in formatters){ if (formatters.hasOwnProperty(key)) {formatters[key] = eval(formatters[key])}}}
            dataContemt[0].forEach(function(c, i){ if(header.includes(c)){ headerIndices.push(i); var h = {title: c, field: c}; %(varId)s.deleteColumn(c); %(varId)s.addColumn(h)}})
            dataContemt.slice(1).forEach(function(v){var row = {}; header.forEach(function(c, i){row[c] = v[headerIndices[i]]})
            if (formatters != null){for (var key in formatters){ row[key] = formatters[key](row)}}
            resultContent.push(row)}); %(varId)s.setData(resultContent)''' % {"header": header, "varId": self.varId, "formatters": formatters, "data": jsData}

    return '''var dataContemt = %(data)s; var resultContent = []; var formatters = %(formatters)s;
      if (formatters != null){
         for (var key in formatters){ if (formatters.hasOwnProperty(key)) {formatters[key] = eval(formatters[key])}}}
      dataContemt[0].forEach(function(c){var h = {title: c, field: c}; %(varId)s.addColumn(h)})
      dataContemt.slice(1).forEach(function(v){var row = {}; dataContemt[0].forEach(function(c, i){row[c] = v[i]})
         if (formatters != null){for (var key in formatters){ row[key] = formatters[key](row)}}
         resultContent.push(row)}); %(varId)s.setData(resultContent)''' % {"varId": self.varId, "formatters": formatters, "data": jsData}

  def replaceData(self, jsData=None):
    """
    Description:
    ------------
    The replaceData function lets you silently replace all data in the table without updating scroll position,
    sort or filtering, and without triggering the ajax loading popup.

    Usage:
    -----

      table.replaceData() //trigger reload of ajax data from ajaxURL property.

    Attributes:
    ----------
    :param jsData:
    """
    if jsData is None:
      return JsObjects.JsObject.JsObject("%s.replaceData()" % self.varId)

    return JsObjects.JsObject.JsObject("%s.replaceData(%s)" % (self.varId, JsUtils.jsConvertData(jsData, None)))

  def getData(self):
    """
    Description:
    ------------
    You can retrieve the data stored in the table using the getData function.
    """
    return JsObjects.JsArray.JsArray("%s.getData()" % self.varId)

  @property
  def rowContextMenu(self):
    return TabRowContextMenu(self.src, selector=self.varId)


class _Export:

  @property
  def cell(self):
    """
    Description:
    ------------
    Cell component for the edited cell.
    """
    return CellComponent(selector="cell", setVar=False)

  @property
  def row(self):
    return RowComponent(selector="row", setVar=False)

  @property
  def value(self):
    """
    Description:
    ------------
    The data being changed.
    """
    return JsObjects.JsObjects.get("value")

  @property
  def data(self):
    """
    Description:
    ------------
    The data being changed.
    """
    return JsObjects.JsObjects.get("data")

  @property
  def rowData(self):
    """
    Description:
    ------------
    The row data from the paste parser.
    """
    return JsObjects.JsObjects.get("row")

  @property
  def rows(self):
    """
    Description:
    ------------
    The row components from the paste action (this will be empty if the "replace" action is used).
    """
    return JsObjects.JsArray.JsArray("rows")

  @property
  def clipboard(self):
    """
    Description:
    ------------
    The clipboard string.
    """
    return JsObjects.JsObjects.get("clipboard")
