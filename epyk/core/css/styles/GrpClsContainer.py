"""

"""

from epyk.core.css.styles import GrpCls
from epyk.core.css.styles.attributes import AttrClsContainer

from epyk.core.css import Classes


class ClassDiv(GrpCls.ClassHtml):
  @property
  def css(self):
    """
    Property to the underlying CSS definition to be added to the style HTML tag of a component
    :rtype: AttrClsContainer.AttrDiv
    """
    if self._css_struct is None:
      self._css_struct = AttrClsContainer.AttrDiv(self.htmlObj)
    return self._css_struct

  @property
  def css_class(self):
    """
    The internal class used to put a custom Style to this object.
    Only 1 CSS class can be added to an HTML object

    :rtype: Classes.CatalogDiv.CatalogDiv
    """
    if self._css_class is None:
      self._css_class = Classes.CatalogDiv.CatalogDiv(self.htmlObj._report, self.classList['main'], html_id=self.htmlObj.htmlId).no_border()
    return self._css_class

