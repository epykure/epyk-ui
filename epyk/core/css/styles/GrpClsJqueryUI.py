
from epyk.core.css.styles import GrpCls
from epyk.core.css import Classes
from epyk.core.css.styles.attributes import AttrInput


class ClassSlider(GrpCls.ClassHtml):

  def __init__(self, component):
    super(ClassSlider, self).__init__(component)
    self._css_ui_active, self._css_ui_header = 2 * [None]
    self.classList['main'].add(self.cls_ui_active)
    self.classList['main'].add(self.cls_ui_header)

  @property
  def css(self):
    """
    Description:
    -----------
    Property to the underlying CSS definition to be added to the style HTML tag of a component.

    :rtype: AttrInput.AttrInput
    """
    if self._css_struct is None:
      self._css_struct = AttrInput.AttrInput(self.component)
    return self._css_struct

  @property
  def css_class(self):
    """
    Description:
    -----------
    The internal class used to put a custom Style to this object.
    Only 1 CSS class can be added to an HTML object.

    :rtype: Classes.CatalogInput.CatalogInput
    """
    if self._css_class is None:
      self._css_class = Classes.CatalogInput.CatalogInput(self.component.page, self.classList['main']).basic()
    return self._css_class

  @property
  def cls_ui_active(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogInput.CatalogInput
    """
    if self._css_ui_active is None:
      self._css_ui_active = Classes.CatalogInput.CatalogInput(self.component.page, self.classList['main']).active()
    return self._css_ui_active

  @property
  def cls_ui_header(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogInput.CatalogInput
    """
    if self._css_ui_header is None:
      self._css_ui_header = Classes.CatalogInput.CatalogInput(self.component.page, self.classList['main']).widget_header()
    return self._css_ui_header


class ClassMenu(GrpCls.ClassHtml):

  def __init__(self, component):
    super(ClassMenu, self).__init__(component)
    self._cls_ui = None
    self.classList['other'].add(self.cls_ui)

  @property
  def cls_ui(self):
    """
    Description:
    -----------

    :rtype: Classes.CatalogInput.CatalogInput
    """
    if self._cls_ui is None:
      self._cls_ui = Classes.CatalogInput.CatalogInput(self.component.page, self.classList['other']).menu()
    return self._cls_ui
