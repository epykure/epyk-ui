
from epyk.core.js import JsUtils
from epyk.core.js.packages import JsPackage
from epyk.core.html.options import OptSortable
from epyk.core.js.primitives import JsObjects


class Sortable(JsPackage):

  lib_alias = {"js": 'sortable'}
  lib_set_var = True

  def __init__(self, src=None, varName=None, selector=None, setVar=True, parent=None):
    super(Sortable, self).__init__(src=src, varName=varName, selector=selector, data=None, setVar=setVar, parent=parent)
    self.__options = OptSortable.OptionsSortable(self)

  @property
  def options(self):
    """
    Description:
    ------------
    Sortable options

    Related Pages:

			https://github.com/SortableJS/Sortable

		:rtype: OptSortable.OptionsSortable
    """
    return self.__options

  def create(self, htmlElement, options=None):
    """
    Description:
    ------------
    Create new instance

    Related Pages:

			https://github.com/SortableJS/Sortable

    Attributes:
    ----------
    :param dom:
    :param options: Optional. Dictionary with the sortable options
    """
    self.__options.update(options)
    return self

  def toArray(self):
    """
    Description:
    ------------
    Serializes the sortable's item data-id's (dataIdAttr option) into an array of string.

    Related Pages:

			https://github.com/SortableJS/toArray
    """
    return self.fnc_closure("toArray()")

  def sort(self, data):
    """
    Description:
    ------------
    Sorts the elements according to the array.

    Related Pages:

			https://github.com/SortableJS/Sortable

    Attributes:
    ----------
    :param data:
    """
    data = JsUtils.jsConvertData(data, None)
    return self.fnc_closure("sort(%s)" % data)

  def save(self):
    """
    Description:
    ------------
    Save the current sorting

    Related Pages:

			https://github.com/SortableJS/save
    """
    return self.fnc_closure("destroy()")

  def destroy(self):
    """
    Description:
    ------------
    Removes the sortable functionality completely.

    Related Pages:

			https://github.com/SortableJS/destroy
    """
    return self.fnc_closure("destroy()")

  def toStr(self):
    if self.setVar:
      self._selector = "Sortable.create(%s, %s)" % (self._selector, JsUtils.jsConvertData(self.__options, None))
    return super(Sortable, self).toStr()
