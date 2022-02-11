# TODO: add other methods

from epyk.core.py import primitives
from epyk.core.js.packages import JsPackage
from epyk.core.js import JsUtils


class JsGrid(JsPackage):

  def __init__(self, component, js_code: str = None, set_var: bool = True, is_py_data: bool = True,
               page: primitives.PageModel = None):
    self.varName, self.varData, self.__var_def = js_code, "", None
    self.component, self.page = component, page
    self._js, self._jquery = [], None

  def activateFocus(self):
    """
    Description:
    -----------
    Make view ready to get keyboard input.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#activateFocus
    """
    return JsUtils.jsWrap("%s.activateFocus()" % self.component.var)

  def addCellClassName(self, row_key, column_name, class_name):
    """
    Description:
    -----------
    Add the specified css class to cell element identified by the rowKey and className.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#addCellClassName

    Attributes:
    ----------
    :param row_key:
    :param column_name:
    :param class_name:
    """
    row_key = JsUtils.jsConvertData(row_key, None)
    column_name = JsUtils.jsConvertData(column_name, None)
    class_name = JsUtils.jsConvertData(class_name, None)
    return JsUtils.jsWrap("%s.addCellClassName(%s, %s, %s)" % (self.component.var, row_key, column_name, class_name))

  def addColumnClassName(self, column_name, class_name):
    """
    Description:
    -----------
    Add class name to all cell data of specific column.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#addColumnClassName

    Attributes:
    ----------
    :param column_name:
    :param class_name:
    """
    column_name = JsUtils.jsConvertData(column_name, None)
    class_name = JsUtils.jsConvertData(class_name, None)
    return JsUtils.jsWrap("%s.addColumnClassName(%s, %s)" % (self.component.var, column_name, class_name))

  def addRowClassName(self, row_key, class_name):
    """
    Description:
    -----------
    Add the specified css class to all cell elements in the row identified by the rowKey.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#addRowClassName

    Attributes:
    ----------
    :param row_key:
    :param class_name:
    """
    row_key = JsUtils.jsConvertData(row_key, None)
    class_name = JsUtils.jsConvertData(class_name, None)
    return JsUtils.jsWrap("%s.addRowClassName(%s, %s)" % (self.component.var, row_key, class_name))

  def appendRow(self, row, options):
    """
    Description:
    -----------
    Add the specified css class to all cell elements in the row identified by the rowKey.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#appendRow

    Attributes:
    ----------
    :param row:
    :param options:
    """
    row = JsUtils.jsConvertData(row, None)
    options = JsUtils.jsConvertData(options, None)
    return JsUtils.jsWrap("%s.appendRow(%s, %s)" % (self.component.var, row, options))

  def appendRows(self, data):
    """
    Description:
    -----------
    append rows.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#appendRows

    Attributes:
    ----------
    :param data:
    """
    data = JsUtils.jsConvertData(data, None)
    return JsUtils.jsWrap("%s.appendRows(%s)" % (self.component.var, data))

  def appendTreeRow(self, row, options):
    """
    Description:
    -----------
    append rows.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#appendTreeRow

    Attributes:
    ----------
    :param row:
    :param options:
    """
    row = JsUtils.jsConvertData(row, None)
    options = JsUtils.jsConvertData(options, None)
    return JsUtils.jsWrap("%s.appendTreeRow(%s, %s)" % (self.component.var, row, options))

  def blur(self):
    """
    Description:
    -----------
    Remove focus from the focused cell.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#blur
    """
    return JsUtils.jsWrap("%s.blur()" % self.component.var)

  def cancelEditing(self):
    """
    Description:
    -----------
    Cancel the editing.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#blur
    """
    return JsUtils.jsWrap("%s.cancelEditing()" % self.component.var)

  def check(self, row_key):
    """
    Description:
    -----------
    Check the row identified by the specified rowKey.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#blur

    Attributes:
    ----------
    :param row_key:
    """
    row_key = JsUtils.jsConvertData(row_key, None)
    return JsUtils.jsWrap("%s.check(%s)" % (self.component.var, row_key))

  def checkAll(self, all_page):
    """
    Description:
    -----------
    Check all rows.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#checkAll

    Attributes:
    ----------
    :param all_page:
    """
    all_page = JsUtils.jsConvertData(all_page, None)
    return JsUtils.jsWrap("%s.checkAll(%s)" % (self.component.var, all_page))

  def clear(self):
    """
    Description:
    -----------
    Remove all rows..

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#clear
    """
    return JsUtils.jsWrap("%s.clear()" % self.component.var)

  def clearModifiedData(self, type):
    """
    Description:
    -----------
    clear the modified data that is returned as the result of 'getModifiedRows' method.
    If the 'type' parameter is undefined, all modified data is cleared.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#checkAll

    Attributes:
    ----------
    :param type:
    """
    type = JsUtils.jsConvertData(type, None)
    return JsUtils.jsWrap("%s.clearModifiedData(%s)" % (self.component.var, type))

  def collapse(self, row_key, recursive):
    """
    Description:
    -----------
    Expand tree row.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#collapse

    Attributes:
    ----------
    :param row_key:
    :param recursive:
    """
    row_key = JsUtils.jsConvertData(row_key, None)
    recursive = JsUtils.jsConvertData(recursive, None)
    return JsUtils.jsWrap("%s.collapse(%s, %s)" % (self.component.var, row_key, recursive))

  def collapseAll(self):
    """
    Description:
    -----------
    Collapse all tree row.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#collapseAll
    """
    return JsUtils.jsWrap("%s.collapseAll()" % self.component.var)

  def copyToClipboard(self):
    """
    Description:
    -----------
    Copy to clipboard.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#copyToClipboard
    """
    return JsUtils.jsWrap("%s.copyToClipboard()" % self.component.var)

  def destroy(self):
    """
    Description:
    -----------
    Destroy the instance.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#copyToClipboard
    """
    return JsUtils.jsWrap("%s.destroy()" % self.component.var)

  def disable(self):
    """
    Description:
    -----------
    Disable all rows.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#copyToClipboard
    """
    return JsUtils.jsWrap("%s.disable()" % self.component.var)

  def disableRow(self, row_key, with_checkbox):
    """
    Description:
    -----------
    Disable the row identified by the rowkey.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#disableRow

    Attributes:
    ----------
    :param row_key:
    :param with_checkbox:
    """
    row_key = JsUtils.jsConvertData(row_key, None)
    with_checkbox = JsUtils.jsConvertData(with_checkbox, None)
    return JsUtils.jsWrap("%s.disableRow(%s, %s)" % (self.component.var, row_key, with_checkbox))

  def disableRowCheck(self, row_key):
    """
    Description:
    -----------
    Disable the row identified by the specified rowKey to not be able to check.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#disableRowCheck

    Attributes:
    ----------
    :param row_key:
    """
    row_key = JsUtils.jsConvertData(row_key, None)
    return JsUtils.jsWrap("%s.disableRowCheck(%s)" % (self.component.var, row_key))

  def enable(self):
    """
    Description:
    -----------
    Enable all rows.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#disableRowCheck
    """
    return JsUtils.jsWrap("%s.enable()" % self.component.var)

  def enableColumn(self, column_name):
    """
    Description:
    -----------
    Enable the column identified by the column name.

    Related Pages:

      https://nhn.github.io/tui.grid/latest/Grid#enableColumn

    Attributes:
    ----------
    :param column_name:
    """
    column_name = JsUtils.jsConvertData(column_name, None)
    return JsUtils.jsWrap("%s.enableColumn(%s)" % (self.component.var, column_name))
