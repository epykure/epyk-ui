
from epyk.core.py import primitives
from epyk.core.css.styles import GrpCls
from epyk.core.css import Classes


class ClassVisTimeline(GrpCls.ClassHtml):

  def __init__(self, component: primitives.HtmlModel):
    super(ClassVisTimeline, self).__init__(component)
    self._css_vis_items, self._css_vis_items_overflow = None, None
    self.classList['other'].add(self.css_items)
    self.classList['other'].add(self.css_items_overflow)

  @property
  def css_items(self) -> Classes.CatalogChart.CatalogChart:
    """   Link to all the CSS classes for Charts and add the vis_items CSS class.

    :rtype: Classes.CatalogChart.CatalogChart
    """
    if self._css_vis_items is None:
      self._css_vis_items = Classes.CatalogChart.CatalogChart(
        self.component.page, self.classList['other'], html_id=self.component.htmlCode,
        component=self.component).vis_items()
    return self._css_vis_items

  @property
  def css_items_overflow(self) -> Classes.CatalogChart.CatalogChart:
    """   Link to all the CSS classes for Charts and add the vis_items overflow CSS class.

    :rtype: Classes.CatalogChart.CatalogChart
    """
    if self._css_vis_items_overflow is None:
      self._css_vis_items_overflow = Classes.CatalogChart.CatalogChart(
        self.component.page, self.classList['other'], html_id=self.component.htmlCode,
        component=self.component).vis_items_overflow()
    return self._css_vis_items_overflow
