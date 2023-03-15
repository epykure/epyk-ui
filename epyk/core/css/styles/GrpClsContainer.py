
from epyk.core.py import primitives
from epyk.core.css.styles import GrpCls
from epyk.core.css.styles.attributes import AttrClsContainer

from epyk.core.css import Classes


class ClassDiv(GrpCls.ClassHtml):

  @property
  def css(self) -> AttrClsContainer.AttrDiv:
    """ Property to the underlying CSS definition to be added to the style HTML tag of a component. """
    if self._css_struct is None:
      self._css_struct = AttrClsContainer.AttrDiv(self.component)
    return self._css_struct

  @property
  def css_class(self) -> Classes.CatalogDiv.CatalogDiv:
    """ The internal class used to put a custom Style to this object.

    Only 1 CSS class can be added to an HTML object.
    """
    if self._css_class is None:
      self._css_class = Classes.CatalogDiv.CatalogDiv(
        self.component.page, self.classList['main'], html_id=self.component.htmlCode,
        component=self.component).no_border()
    return self._css_class


class ClassModal(GrpCls.ClassHtml):

  @property
  def css(self) -> AttrClsContainer.AttrModal:
    """ Property to the underlying CSS definition to be added to the style HTML tag of a component. """
    if self._css_struct is None:
      self._css_struct = AttrClsContainer.AttrModal(self.component)
    return self._css_struct

  @property
  def css_class(self) -> Classes.CatalogDiv.CatalogDiv:
    """ The internal class used to put a custom Style to this object.

    Only 1 CSS class can be added to an HTML object.
    """
    if self._css_class is None:
      self._css_class = Classes.CatalogDiv.CatalogDiv(
        self.component.page, self.classList['main'], html_id=self.component.htmlCode,
        component=self.component).modal()
    return self._css_class


class ClassDrawer(GrpCls.ClassHtml):

  def __init__(self, component: primitives.HtmlModel):
    super(ClassDrawer, self).__init__(component)
    self._css_class_drawer, self._css_class_handle, self._css_class_content, self._css_class_nav = 4 * [None]
    self.classList['main'].add(self.css_class_drawer)
    self.classList['main'].add(self.css_class_handle)
    self.classList['main'].add(self.css_class_content)
    self.classList['main'].add(self.css_class_nav)

  @property
  def css(self) -> AttrClsContainer.AttrDiv:
    """ Property to the underlying CSS definition to be added to the style HTML tag of a component. """
    if self._css_struct is None:
      self._css_struct = AttrClsContainer.AttrDiv(self.component)
    return self._css_struct

  @property
  def css_class_drawer(self) -> Classes.CatalogDiv.CatalogDrawer:
    """ The internal class used to put a custom Style to this object.

    Only 1 CSS class can be added to an HTML object.
    """
    if self._css_class_drawer is None:
      self._css_class_drawer = Classes.CatalogDiv.CatalogDrawer(
        self.component.page, self.classList['main'], html_id=self.component.htmlCode,
        component=self.component).drawer()
    return self._css_class_drawer

  @property
  def css_class_nav(self) -> Classes.CatalogDiv.CatalogDrawer:
    """ The internal class used to put a custom Style to this object.

    Only 1 CSS class can be added to an HTML object.
    """
    if self._css_class_nav is None:
      self._css_class_nav = Classes.CatalogDiv.CatalogDrawer(
        self.component.page, self.classList['main'], html_id=self.component.htmlCode,
        component=self.component).drawer()
    return self._css_class_nav

  @property
  def css_class_handle(self) -> Classes.CatalogDiv.CatalogDrawer:
    """ The internal class used to put a custom Style to this object.

    Only 1 CSS class can be added to an HTML object.
    """
    if self._css_class_handle is None:
      self._css_class_handle = Classes.CatalogDiv.CatalogDrawer(
        self.component.page, self.classList['main'], html_id=self.component.htmlCode,
        component=self.component).handle()
    return self._css_class_handle

  @property
  def css_class_content(self) -> Classes.CatalogDiv.CatalogDrawer:
    """ The internal class used to put a custom Style to this object.

    Only 1 CSS class can be added to an HTML object.
    """
    if self._css_class_content is None:
      self._css_class_content = Classes.CatalogDiv.CatalogDrawer(
        self.component.page, self.classList['main'], html_id=self.component.htmlCode,
        component=self.component).content()
    return self._css_class_content
