
from epyk.core.css.styles import GrpCls
from epyk.core.css.styles.attributes import AttrClsMenu


class ClassNav(GrpCls.ClassHtml):
  @property
  def css(self):
    """
    Description:
    -----------
    Property to the underlying CSS definition to be added to the style HTML tag of a component

    :rtype: AttrClsMenu.NavBar
    """
    if self._css_struct is None:
      self._css_struct = AttrClsMenu.NavBar(self.htmlObj)
    return self._css_struct


class ClassFooter(GrpCls.ClassHtml):

  @property
  def css(self):
    """
    Description:
    -----------
    Property to the underlying CSS definition to be added to the style HTML tag of a component

    :rtype: AttrClsMenu.Footer
    """
    if self._css_struct is None:
      self._css_struct = AttrClsMenu.Footer(self.htmlObj)
    return self._css_struct
