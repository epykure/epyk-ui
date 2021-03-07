
from epyk.core.css.styles import GrpCls
from epyk.core.css import Classes


class ClassVisTimeline(GrpCls.ClassHtml):

  def __init__(self, component):
    super(ClassVisTimeline, self).__init__(component)
    self._css_vis_items, self._css_vis_items_overflow = None, None
    self.classList['other'].add(self.css_items)
    self.classList['other'].add(self.css_items_overflow)

  @property
  def css_items(self):
    """
    Description:
    -----------
    """
    if self._css_vis_items is None:
      self._css_vis_items = Classes.CatalogChart.CatalogChart(
        self.component.page, self.classList['other'], html_id=self.component.htmlCode).vis_items()
    return self._css_vis_items

  @property
  def css_items_overflow(self):
    """
    Description:
    -----------
    """
    if self._css_vis_items_overflow is None:
      self._css_vis_items_overflow = Classes.CatalogChart.CatalogChart(
        self.component.page, self.classList['other'], html_id=self.component.htmlCode).vis_items_overflow()
    return self._css_vis_items_overflow
