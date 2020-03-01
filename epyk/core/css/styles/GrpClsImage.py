
from epyk.core.css.styles import GrpCls
from epyk.core.css.styles.attributes import AttrClsImage


class ClassIcon(GrpCls.ClassHtml):
  @property
  def css(self):
    """
    Description:
    ------------
    Property to the underlying CSS definition to be added to the style HTML tag of a component

    :rtype: AttrClsImage.AttrIcon
    """
    if self._css_struct is None:
      self._css_struct = AttrClsImage.AttrIcon(self.htmlObj)
    return self._css_struct

