
from epyk.core.py import primitives
from epyk.core.css.styles import GrpCls
from epyk.core.css import Classes


class ClassNetworkBot(GrpCls.ClassHtml):

  def __init__(self, component: primitives.HtmlModel):
    super(ClassNetworkBot, self).__init__(component)
    self._css_bubble, self._css_bubble_content, self._css_bubble_arrow = None, None, None
    self.classList['other'].add(self.cls_bubble)
    self.classList['other'].add(self.cls_bubble_content)
    self.classList['other'].add(self.cls_bubble_arrow)

  @property
  def cls_bubble(self) -> Classes.CatalogDiv.CatalogDiv:
    """   

    :rtype: Classes.CatalogDiv.CatalogDiv
    """
    if self._css_bubble is None:
      self._css_bubble = Classes.CatalogDiv.CatalogDiv(
        self.component.page, self.classList['other'], component=self.component).bubble_container()
    return self._css_bubble

  @property
  def cls_bubble_content(self) -> Classes.CatalogDiv.CatalogDiv:
    """   

    :rtype: Classes.CatalogDiv.CatalogDiv
    """
    if self._css_bubble_content is None:
      self._css_bubble_content = Classes.CatalogDiv.CatalogDiv(
        self.component.page, self.classList['other'], component=self.component).bubble_content()
    return self._css_bubble_content

  @property
  def cls_bubble_arrow(self) -> Classes.CatalogDiv.CatalogDiv:
    """   

    :rtype: Classes.CatalogDiv.CatalogDiv
    """
    if self._css_bubble_arrow is None:
      self._css_bubble_arrow = Classes.CatalogDiv.CatalogDiv(
        self.component.page, self.classList['other'], component=self.component).bubble_arrow()
    return self._css_bubble_arrow
