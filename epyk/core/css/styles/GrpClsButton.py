
from epyk.core.py import primitives
from epyk.core.css.styles import GrpCls
from epyk.core.css.styles.attributes import AttrClsButtons

from epyk.core.css import Classes


class ClassButton(GrpCls.ClassHtml):

  @property
  def css(self) -> AttrClsButtons.AttrButton:
    """   Property to the underlying CSS definition to be added to the style HTML tag of a component.

    Usage::

      self.css.border = "1px solid red"
    """
    if self._css_struct is None:
      self._css_struct = AttrClsButtons.AttrButton(self.component)
    return self._css_struct

  @property
  def css_class(self) -> Classes.CatalogButton.CatalogButton:
    """   The internal class used to put a custom Style to this object.
    Only 1 CSS class can be added to an HTML object.

    Usage::

      self.css_class.basic()
    """
    if self._css_class is None:
      if self.component.name == 'button' and self.component.options.category in ["delete"]:
        self._css_class = Classes.CatalogButton.CatalogButton(
          self.component.page, self.classList['main'], html_id=self.component.htmlCode).reset()
      else:
        self._css_class = Classes.CatalogButton.CatalogButton(
          self.component.page, self.classList['main'], html_id=self.component.htmlCode).basic()
    return self._css_class


class ClassBadge(GrpCls.ClassHtml):

  @property
  def css(self) -> AttrClsButtons.AttrBadge:
    """   Property to the underlying CSS definition to be added to the style HTML tag of a component.

    Usage::

      self.css.background = "white"
    """
    if self._css_struct is None:
      self._css_struct = AttrClsButtons.AttrBadge(self.component)
    return self._css_struct


class ClassButtonCheckBox(GrpCls.ClassHtml):

  @property
  def css(self) -> AttrClsButtons.AttrButton:
    """   Property to the underlying CSS definition to be added to the style HTML tag of a component.

    Usage::

      self.css.color = "red"
    """
    if self._css_struct is None:
      self._css_struct = AttrClsButtons.AttrButton(self.component)
    return self._css_struct


class ClassButtonMenu(GrpCls.ClassHtml):

  def __init__(self, component: primitives.HtmlModel):
    super(ClassButtonMenu, self).__init__(component)
    self._css_btn_content_hover, self._css_btn_link_hover = None, None
    self.classList['main'].add(self.css_btn_content)
    self.classList['main'].add(self.css_btn_link_hover)

  @property
  def css_btn_content(self) -> Classes.CatalogButton.CatalogButton:
    """   The CSS property of the underlying items panel.
    This component will have a dedicated CSS class for the hover event.
    """
    if self._css_btn_content_hover is None:
      self._css_btn_content_hover = Classes.CatalogButton.CatalogButton(
        self.component.page, self.classList['main'], html_id=self.component.htmlCode,
        component=self.component).content()
    return self._css_btn_content_hover

  @property
  def css_btn_link_hover(self) -> Classes.CatalogButton.CatalogButton:
    """   The CSS property of the underlying item.
    This component will have a dedicated CSS class for the hover event.
    """
    if self._css_btn_link_hover is None:
      self._css_btn_link_hover = Classes.CatalogButton.CatalogButton(
        self.component.page, self.classList['main'], html_id=self.component.htmlCode,
        component=self.component).content_link()
    return self._css_btn_link_hover
