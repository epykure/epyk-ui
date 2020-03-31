
from epyk.core.css.styles import GrpCls
from epyk.core.css import Classes


class ClassSelect(GrpCls.ClassHtml):

  def __init__(self, htmlObj):
    super(ClassSelect, self).__init__(htmlObj)
    self._css_class_dt, self._css_class_dt_ui, self._css_select = None, None, None
    self.classList['main'].add(self.cls_select)
    self.classList['main'].add(self.cls_datepicker)
    self.classList['main'].add(self.cls_datepicker_ui)

  @property
  def cls_select(self):
    """

    :rtype: Classes.CatalogInput.CatalogDate
    """
    if self._css_select is None:
      self._css_select = Classes.CatalogSelect.CatalogSelect(self.htmlObj._report, self.classList['main']).base()
    return self._css_select

  @property
  def cls_datepicker(self):
    """

    :rtype: Classes.CatalogInput.CatalogDate
    """
    if self._css_class_dt is None:
      self._css_class_dt = Classes.CatalogSelect.CatalogSelect(self.htmlObj._report, self.classList['main']).button()
    return self._css_class_dt

  @property
  def cls_datepicker_ui(self):
    """

    :rtype: Classes.CatalogInput.CatalogDate
    """
    if self._css_class_dt_ui is None:
      self._css_class_dt_ui = Classes.CatalogSelect.CatalogSelect(self.htmlObj._report, self.classList['main']).outline()
    return self._css_class_dt_ui
