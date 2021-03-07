#!/usr/bin/python
# -*- coding: utf-8 -*-


from epyk.core.css.styles import GrpCls
from epyk.core.css import Classes
from epyk.core.css.styles.attributes import AttrClsChart


class ClassBSpartlines(GrpCls.ClassHtml):

  @property
  def css(self):
    """
    Description:
    ------------
    Property to the underlying CSS definition to be added to the style HTML tag of a component.

    :rtype: AttrClsChart.AttrSkarkline
    """
    if self._css_struct is None:
      self._css_struct = AttrClsChart.AttrSkarkline(self.component)
    return self._css_struct

  @property
  def css_class(self):
    """
    Description:
    ------------
    The internal class used to put a custom Style to this object.
    Only 1 CSS class can be added to an HTML object.

    :rtype: Classes.CatalogDiv.CatalogDiv
    """
    if self._css_class is None:
      self._css_class = Classes.CatalogDiv.CatalogDiv(self.component.page, self.classList['main']).margin_vertical()
    return self._css_class
