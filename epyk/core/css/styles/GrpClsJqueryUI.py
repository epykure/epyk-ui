
from epyk.core.py import primitives
from epyk.core.css.styles import GrpCls
from epyk.core.css import Classes
from epyk.core.css.styles.attributes import AttrInput


class ClassSlider(GrpCls.ClassHtml):

  def __init__(self, component: primitives.HtmlModel):
    super(ClassSlider, self).__init__(component)
    self._css_ui_active, self._css_ui_header, self._css_ui_slider = 3 * [None]
    self.classList['other'].add(self.cls_ui_active)
    self.classList['other'].add(self.cls_ui_header)
    self.classList['other'].add(self.cls_ui_slider)

  @property
  def css(self) -> AttrInput.AttrInput:
    """
    Description:
    -----------
    Property to the underlying CSS definition to be added to the style HTML tag of a component.

    Usage::

      self.css.border = "1px solid black"

    :rtype: AttrInput.AttrInput
    """
    if self._css_struct is None:
      self._css_struct = AttrInput.AttrInput(self.component)
    return self._css_struct

  @property
  def css_class(self) -> Classes.CatalogInput.CatalogInput:
    """
    Description:
    -----------
    The internal class used to put a custom Style to this object.
    Only 1 CSS class can be added to an HTML object.

    :rtype: Classes.CatalogInput.CatalogInput
    """
    if self._css_class is None:
      self._css_class = Classes.CatalogInput.CatalogInput(
        self.component.page, self.classList['main'], component=self.component).basic()
    return self._css_class

  @property
  def cls_ui_slider(self) -> Classes.CatalogInput.CatalogInput:
    """
    Description:
    -----------
    Add the predefined CSS class style for the active slider.
    Class override on the existing one in the package.

    :rtype: Classes.CatalogInput.CatalogInput
    """
    if self._css_ui_slider is None:
      self._css_ui_slider = Classes.CatalogInput.CatalogInput(
        self.component.page, self.classList['main'], component=self.component).slider()
    return self._css_ui_slider

  @property
  def cls_ui_active(self) -> Classes.CatalogInput.CatalogInput:
    """
    Description:
    -----------
    Add the predefined CSS class style for the active slider.
    Class override on the existing one in the package.

    :rtype: Classes.CatalogInput.CatalogInput
    """
    if self._css_ui_active is None:
      self._css_ui_active = Classes.CatalogInput.CatalogInput(
        self.component.page, self.classList['main'], component=self.component).active()
    return self._css_ui_active

  @property
  def cls_ui_header(self) -> Classes.CatalogInput.CatalogInput:
    """
    Description:
    -----------
    Add the predefined CSS class for the UI slider header.
    Class override on the existing one in the package.

    :rtype: Classes.CatalogInput.CatalogInput
    """
    if self._css_ui_header is None:
      self._css_ui_header = Classes.CatalogInput.CatalogInput(
        self.component.page, self.classList['main'], component=self.component).widget_header()
    return self._css_ui_header


class ClassMenu(GrpCls.ClassHtml):

  def __init__(self, component: primitives.HtmlModel):
    super(ClassMenu, self).__init__(component)
    self._cls_ui = None
    self.classList['other'].add(self.cls_ui)

  @property
  def cls_ui(self) -> Classes.CatalogInput.CatalogInput:
    """
    Description:
    -----------
    Class override on the existing one in the package.

    :rtype: Classes.CatalogInput.CatalogInput
    """
    if self._cls_ui is None:
      self._cls_ui = Classes.CatalogInput.CatalogInput(
        self.component.page, self.classList['other'], component=self.component).menu()
    return self._cls_ui
