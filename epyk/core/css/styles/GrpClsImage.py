
from epyk.core.css.styles import GrpCls
from epyk.core.css import Classes
from epyk.core.py import OrderedSet
from epyk.core.css.styles.attributes import AttrClsImage


class ClassIcon(GrpCls.ClassHtml):

  def __init__(self, component):
    super(ClassIcon, self).__init__(component)
    self.classList["main"] = OrderedSet()

  @property
  def css(self):
    """
    Description:
    ------------
    Property to the underlying CSS definition to be added to the style HTML tag of a component.

    Usage::

      self.css.border = "1px solid black"

    :rtype: AttrClsImage.AttrIcon
    """
    if self._css_struct is None:
      self._css_struct = AttrClsImage.AttrIcon(self.component)
    return self._css_struct


class ClassTinySlider(GrpCls.ClassHtml):

  def __init__(self, component):
    super(ClassTinySlider, self).__init__(component)
    self._css_tns_button, self._css_tns_active = None, None
    self.classList['other'].add(self.cls_tns_button)
    self.classList['other'].add(self.cls_tns_active)

  @property
  def cls_tns_button(self):
    """
    Description:
    ------------

    :rtype: Classes.CatalogImg.CatalogImg
    """
    if self._css_tns_button is None:
      self._css_tns_button = Classes.CatalogImg.CatalogImg(
        self.component.page, self.classList['other']).tns_button()
    return self._css_tns_button

  @property
  def cls_tns_active(self):
    """
    Description:
    ------------

    :rtype: Classes.CatalogImg.CatalogImg
    """
    if self._css_tns_active is None:
      self._css_tns_active = Classes.CatalogImg.CatalogImg(
        self.component.page, self.classList['other']).tns_button_active()
    return self._css_tns_active
