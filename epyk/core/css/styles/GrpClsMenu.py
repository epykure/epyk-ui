
from epyk.core.css.styles import GrpCls
from epyk.core.css.styles.attributes import AttrClsMenu


class ClassNav(GrpCls.ClassHtml):

  @property
  def css(self) -> AttrClsMenu.NavBar:
    """   Property to the underlying CSS definition to be added to the style HTML tag of a component.

    Usage::

      self.css.border = "1px solid black"

    :rtype: AttrClsMenu.NavBar
    """
    if self._css_struct is None:
      self._css_struct = AttrClsMenu.NavBar(self.component)
    return self._css_struct


class ClassFooter(GrpCls.ClassHtml):

  @property
  def css(self) -> AttrClsMenu.Footer:
    """   Property to the underlying CSS definition to be added to the style HTML tag of a component.

    Usage::

      self.css.border = "1px solid black"

    :rtype: AttrClsMenu.Footer
    """
    if self._css_struct is None:
      self._css_struct = AttrClsMenu.Footer(self.component)
    return self._css_struct


class ClassShortcut(GrpCls.ClassHtml):

  @property
  def css(self) -> AttrClsMenu.Footer:
    """   Property to the underlying CSS definition to be added to the style HTML tag of a component.

    Usage::

      self.css.border = "1px solid black"

    :rtype: AttrClsMenu.Footer
    """
    if self._css_struct is None:
      self._css_struct = AttrClsMenu.Footer(self.component)
    return self._css_struct
