

from epyk.core.css.styles import GrpCls
from epyk.core.css import Classes
from epyk.core.css.styles.attributes import Commons


class ContentTable(GrpCls.ClassHtml):

  @property
  def css(self):
    """
    Description:
    ------------
    Property to the underlying CSS definition to be added to the style HTML tag of a component.

    Usage::

      self.css.color = "red"

    :rtype: Commons
    """
    if self._css_struct is None:
      self._css_struct = Commons(self.component)
    return self._css_struct

  @property
  def css_class(self):
    """
    Description:
    ------------
    The internal class used to put a custom Style to this object.
    Only 1 CSS class can be added to an HTML object.

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_class is None:
      self._css_class = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['main'], html_id=self.component.htmlCode).table_content()
    return self._css_class


class ClsFormula(GrpCls.ClassHtml):

  def __init__(self, component):
    super(ClsFormula, self).__init__(component)
    self._css_container, self._css_mjx = 2 * [None]
    self.classList['other'].add(self.cls_container)
    self.classList['other'].add(self.cls_mjx)

  @property
  def cls_container(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogText.CatalogFormulas
    """
    if self._css_container is None:
      self._css_container = Classes.CatalogText.CatalogFormulas(
        self.component.page, self.classList['other']).container()
    return self._css_container

  @property
  def cls_mjx(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogText.CatalogFormulas
    """
    if self._css_mjx is None:
      self._css_mjx = Classes.CatalogText.CatalogFormulas(self.component.page, self.classList['other']).mjx()
    return self._css_mjx
