
from epyk.core.js import JsUtils
from epyk.core.js.packages import JsPackage
from epyk.core.html.options import OptSortable
from epyk.core.js.primitives import JsObjects


class Sortable(JsPackage):

  lib_alias = {"js": 'sortable'}
  lib_set_var = False

  @property
  def options(self):
    """
    Description:
    ------------
    Sortable options

    Related Pages:

			https://github.com/SortableJS/Sortable
    """
    return OptSortable.OptionsSortable(self, {})

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

  def toArray(self):
    """
    Description:
    ------------

    """

  def sort(self, data):
    """
    Description:
    ------------

    https://github.com/SortableJS/Sortable

    :param data:
    """
    return

  def save(self):
    """
    Description:
    ------------
    Save the current sorting
    """

  def destrop(self):
    """
    Description:
    ------------

    """

