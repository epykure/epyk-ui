
from epyk.core.js import JsUtils
from epyk.core.js.packages import JsPackage
from epyk.core.html.options import OptSortable
from epyk.core.js.primitives import JsObjects


class Sortable(JsPackage):

  lib_alias = {"js": 'sortablejs'}
  lib_set_var = True

  def __init__(self, component=None, js_code=None, selector=None, set_var=True, parent=None):
    super(Sortable, self).__init__(
      component=component, js_code=js_code, selector=selector, data=None, set_var=set_var, parent=parent)
    self.__options = OptSortable.OptionsSortable(component)

  @property
  def options(self) -> OptSortable.OptionsSortable:
    """
    Description:
    ------------
    Sortable options

    Related Pages:

      https://github.com/SortableJS/Sortable

		:rtype: OptSortable.OptionsSortable
    """
    return self.__options

  def create(self, htmlElement, options: dict = None):
    """
    Description:
    ------------
    Create new instance

    Related Pages:

      https://github.com/SortableJS/Sortable

    Attributes:
    ----------
    :param dom:
    :param dict options: Optional. Dictionary with the sortable options
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
      self._selector = "Sortable.create(%s, %s)" % (self._selector, JsUtils.jsConvertData(self.options, None))
    return super(Sortable, self).toStr()
