
from epyk.core.css.styles import GrpCls
from epyk.core.css import Classes


class ClassNetworkBot(GrpCls.ClassHtml):

  def __init__(self, htmlObj):
    super(ClassNetworkBot, self).__init__(htmlObj)
    self._css_bubble, self._css_bubble_content, self._css_bubble_arrow = None, None, None
    self.classList['other'].add(self.cls_bubble)
    self.classList['other'].add(self.cls_bubble_content)
    self.classList['other'].add(self.cls_bubble_arrow)

  @property
  def cls_bubble(self):
    """

    :rtype: Classes.CatalogInput.CatalogDate
    """
    if self._css_bubble is None:
      self._css_bubble = Classes.CatalogDiv.CatalogDiv(self.htmlObj._report, self.classList['other']).bubble_container()
    return self._css_bubble

  @property
  def cls_bubble_content(self):
    """

    :rtype: Classes.CatalogInput.CatalogDate
    """
    if self._css_bubble_content is None:
      self._css_bubble_content = Classes.CatalogDiv.CatalogDiv(self.htmlObj._report, self.classList['other']).bubble_content()
    return self._css_bubble_content

  @property
  def cls_bubble_arrow(self):
    """

    :rtype: Classes.CatalogInput.CatalogDate
    """
    if self._css_bubble_arrow is None:
      self._css_bubble_arrow = Classes.CatalogDiv.CatalogDiv(self.htmlObj._report, self.classList['other']).bubble_arrow()
    return self._css_bubble_arrow
