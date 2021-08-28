# TODO: add other methods

from epyk.core.js.packages import JsPackage
from epyk.core.js import JsUtils


class JsGrid(JsPackage):

  def __init__(self, htmlObj, varName=None, setVar=True, isPyData=True, report=None):
    self.varName, self.varData, self.__var_def = varName, "", None
    self._src, self._report = htmlObj, report
    self._js, self._jquery = [], None

  def activateFocus(self):
    """
    Description:
    -----------
    Make view ready to get keyboard input.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#activateFocus
    """
    return JsUtils.jsWrap("%s.activateFocus()" % self._src.var)

  def addCellClassName(self, rowKey, columnName, className):
    """
    Description:
    -----------
    Add the specified css class to cell element identified by the rowKey and className.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#addCellClassName
    """
    rowKey = JsUtils.jsConvertData(rowKey, None)
    columnName = JsUtils.jsConvertData(columnName, None)
    className = JsUtils.jsConvertData(className, None)
    return JsUtils.jsWrap("%s.addCellClassName(%s, %s, %s)" % (self._src.var, rowKey, columnName, className))

  def addColumnClassName(self, columnName, className):
    """
    Description:
    -----------
    Add class name to all cell data of specific column.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#addColumnClassName
    """
    columnName = JsUtils.jsConvertData(columnName, None)
    className = JsUtils.jsConvertData(className, None)
    return JsUtils.jsWrap("%s.addColumnClassName(%s, %s)" % (self._src.var, columnName, className))

  def addRowClassName(self, rowKey, className):
    """
    Description:
    -----------
    Add the specified css class to all cell elements in the row identified by the rowKey.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#addRowClassName
    """
    rowKey = JsUtils.jsConvertData(rowKey, None)
    className = JsUtils.jsConvertData(className, None)
    return JsUtils.jsWrap("%s.addRowClassName(%s, %s)" % (self._src.var, rowKey, className))

  def appendRow(self, row, options):
    """
    Description:
    -----------
    Add the specified css class to all cell elements in the row identified by the rowKey.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#appendRow
    """
    row = JsUtils.jsConvertData(row, None)
    options = JsUtils.jsConvertData(options, None)
    return JsUtils.jsWrap("%s.appendRow(%s, %s)" % (self._src.var, row, options))

  def appendRows(self, data):
    """
    Description:
    -----------
    append rows.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#appendRows
    """
    data = JsUtils.jsConvertData(data, None)
    return JsUtils.jsWrap("%s.appendRows(%s)" % (self._src.var, data))

  def appendTreeRow(self, row, options):
    """
    Description:
    -----------
    append rows.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#appendTreeRow
    """
    row = JsUtils.jsConvertData(row, None)
    options = JsUtils.jsConvertData(options, None)
    return JsUtils.jsWrap("%s.appendTreeRow(%s, %s)" % (self._src.var, row, options))

  def blur(self):
    """
    Description:
    -----------
    Remove focus from the focused cell.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#blur
    """
    return JsUtils.jsWrap("%s.blur()" % self._src.var)

  def cancelEditing(self):
    """
    Description:
    -----------
    Cancel the editing.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#blur
    """
    return JsUtils.jsWrap("%s.cancelEditing()" % self._src.var)

  def check(self, rowKey):
    """
    Description:
    -----------
    Check the row identified by the specified rowKey.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#blur
    """
    rowKey = JsUtils.jsConvertData(rowKey, None)
    return JsUtils.jsWrap("%s.check(%s)" % (self._src.var, rowKey))

  def checkAll(self, allPage):
    """
    Description:
    -----------
    Check all rows.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#checkAll
    """
    allPage = JsUtils.jsConvertData(allPage, None)
    return JsUtils.jsWrap("%s.checkAll(%s)" % (self._src.var, allPage))

  def clear(self):
    """
    Description:
    -----------
    Remove all rows..

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#clear
    """
    return JsUtils.jsWrap("%s.clear()" % self._src.var)

  def clearModifiedData(self, type):
    """
    Description:
    -----------
    clear the modified data that is returned as the result of 'getModifiedRows' method.
    If the 'type' parameter is undefined, all modified data is cleared.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#checkAll
    """
    type = JsUtils.jsConvertData(type, None)
    return JsUtils.jsWrap("%s.clearModifiedData(%s)" % (self._src.var, type))

  def collapse(self, rowKey, recursive):
    """
    Description:
    -----------
    Expand tree row.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#collapse
    """
    rowKey = JsUtils.jsConvertData(rowKey, None)
    recursive = JsUtils.jsConvertData(recursive, None)
    return JsUtils.jsWrap("%s.collapse(%s, %s)" % (self._src.var, rowKey, recursive))

  def collapseAll(self):
    """
    Description:
    -----------
    Collapse all tree row.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#collapseAll
    """
    return JsUtils.jsWrap("%s.collapseAll()" % self._src.var)

  def copyToClipboard(self):
    """
    Description:
    -----------
    Copy to clipboard.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#copyToClipboard
    """
    return JsUtils.jsWrap("%s.copyToClipboard()" % self._src.var)

  def destroy(self):
    """
    Description:
    -----------
    Destroy the instance.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#copyToClipboard
    """
    return JsUtils.jsWrap("%s.destroy()" % self._src.var)

  def disable(self):
    """
    Description:
    -----------
    Disable all rows.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#copyToClipboard
    """
    return JsUtils.jsWrap("%s.disable()" % self._src.var)

  def disableRow(self, rowKey, withCheckbox):
    """
    Description:
    -----------
    Disable the row identified by the rowkey.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#disableRow
    """
    rowKey = JsUtils.jsConvertData(rowKey, None)
    withCheckbox = JsUtils.jsConvertData(withCheckbox, None)
    return JsUtils.jsWrap("%s.disableRow(%s, %s)" % (self._src.var, rowKey, withCheckbox))

  def disableRowCheck(self, rowKey):
    """
    Description:
    -----------
    Disable the row identified by the specified rowKey to not be able to check.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#disableRowCheck
    """
    rowKey = JsUtils.jsConvertData(rowKey, None)
    return JsUtils.jsWrap("%s.disableRowCheck(%s)" % (self._src.var, rowKey))

  def enable(self):
    """
    Description:
    -----------
    Enable all rows.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#disableRowCheck
    """
    return JsUtils.jsWrap("%s.enable()" % self._src.var)

  def enableColumn(self, columnName):
    """
    Description:
    -----------
    Enable the column identified by the column name.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#enableColumn
    """
    columnName = JsUtils.jsConvertData(columnName, None)
    return JsUtils.jsWrap("%s.enableColumn(%s)" % (self._src.var, columnName))
