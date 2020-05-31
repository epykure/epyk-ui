
from epyk.core.css.styles import GrpCls
from epyk.core.css.styles.attributes import AttrClsButtons

from epyk.core.css import Properties
from epyk.core.css import Classes


class ClassButton(GrpCls.ClassHtml):

  @property
  def css(self):
    """
    Description:
    -----------
    Property to the underlying CSS definition to be added to the style HTML tag of a component

    :rtype: AttrClsButtons.AttrButton
    """
    if self._css_struct is None:
      self._css_struct = AttrClsButtons.AttrButton(self.htmlObj)
    return self._css_struct

  @property
  def css_class(self):
    """
    Description:
    -----------
    The internal class used to put a custom Style to this object.
    Only 1 CSS class can be added to an HTML object

    :rtype: Classes.CatalogButton.CatalogButton
    """
    if self._css_class is None:
      self._css_class = Classes.CatalogButton.CatalogButton(self.htmlObj._report, self.classList['main'], html_id=self.htmlObj.htmlCode).basic()
    return self._css_class


class ClassBadge(GrpCls.ClassHtml):

  @property
  def css(self):
    """
    Description:
    -----------
    Property to the underlying CSS definition to be added to the style HTML tag of a component

    :rtype: AttrClsButtons.AttrBadge
    """
    if self._css_struct is None:
      self._css_struct = AttrClsButtons.AttrBadge(self.htmlObj)
    return self._css_struct


class ClassButtonCheckBox(GrpCls.ClassHtml):

  @property
  def css(self):
    """
    Description:
    -----------
    Property to the underlying CSS definition to be added to the style HTML tag of a component

    :rtype: AttrClsButtons.AttrButton
    """
    if self._css_struct is None:
      self._css_struct = AttrClsButtons.AttrButton(self.htmlObj)
    return self._css_struct


class ClassButtonMenu(GrpCls.ClassHtml):

  def __init__(self, htmlObj):
    super(ClassButtonMenu, self).__init__(htmlObj)
    self._css_btn_content_hover, self._css_btn_link_hover = None, None
    self.classList['main'].add(self.css_btn_content)
    self.classList['main'].add(self.css_btn_link_hover)

  @property
  def css_btn_content(self):
    """
    Description:
    -----------
    The CSS property of the underlying items panel.
    This component will have a dedicated CSS class for the hover event

    :rtype: Classes.CatalogButton.CatalogButton
    """
    if self._css_btn_content_hover is None:
      self._css_btn_content_hover = Classes.CatalogButton.CatalogButton(self.htmlObj._report, self.classList['main'],
                                                            html_id=self.htmlObj.htmlCode).content()
    return self._css_btn_content_hover

  @property
  def css_btn_link_hover(self):
    """
    Description:
    -----------
    The CSS property of the underlying item.
    This component will have a dedicated CSS class for the hover event

    :rtype: Classes.CatalogButton.CatalogButton
    """
    if self._css_btn_link_hover is None:
      self._css_btn_link_hover = Classes.CatalogButton.CatalogButton(self.htmlObj._report, self.classList['main'],
                                                                        html_id=self.htmlObj.htmlCode).content_link()
    return self._css_btn_link_hover

# class CssClassButtonCheckBox(CssGrpCls.CssGrpClass):
#   """
#
#   """
#   css_button_basic = CssStylesLabel.CssLabelContainer
#   css_label_container_disabled = CssStylesLabel.CssLabelContainerDisabled
#   css_label_check_mark_hover = CssStylesLabel.CssLabelCheckMarkHover
#   css_div_no_border = CssStylesDiv.CssDivNoBorder
#   css_check_mark = CssStylesText.CssCheckMark
#   __map, __alt_map = ['CssButtonBasic', 'CssLabelCheckMarkHover', 'CssDivNoBorder', 'CssCheckMark',
#                       'CssLabelContainerDisabled'], []
