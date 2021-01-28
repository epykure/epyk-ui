
from epyk.core.css.styles import GrpCls
from epyk.core.css import Classes


class Code(GrpCls.ClassHtml):

  def __init__(self, htmlObj):
    super(Code, self).__init__(htmlObj)
    self._css_cm, self._css_cm_gutters, self._css_cm_active = 3 * [None]
    self.classList['main'].add(self.cls_cm)
    self.classList['main'].add(self.cls_cm_gutters)
    self.classList['main'].add(self.cls_cm_active)

  @property
  def cls_cm(self):
    """
    Description:
    ------------
    The CSS Class for the code mirror container.

    :rtype: Classes.CatalogText.CatalogEditor
    """
    if self._css_cm is None:
      self._css_cm = Classes.CatalogText.CatalogEditor(self.htmlObj._report, self.classList['main']).cm()
    return self._css_cm

  @property
  def cls_cm_gutters(self):
    """
    Description:
    ------------
    The CSS Class for the gutter panel.

    :rtype: Classes.CatalogText.CatalogEditor
    """
    if self._css_cm_gutters is None:
      self._css_cm_gutters = Classes.CatalogText.CatalogEditor(self.htmlObj._report, self.classList['main']).cm_gutter()
    return self._css_cm_gutters

  @property
  def cls_cm_active(self):
    """
    Description:
    ------------
    The CSS Class for the active line background.

    :rtype: Classes.CatalogText.CatalogEditor
    """
    if self._css_cm_active is None:
      self._css_cm_active = Classes.CatalogText.CatalogEditor(self.htmlObj._report, self.classList['main']).cm_activeline()
    return self._css_cm_active
