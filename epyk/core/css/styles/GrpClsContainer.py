
from epyk.core.css.styles import GrpCls
from epyk.core.css.styles.attributes import AttrClsContainer

from epyk.core.css import Classes


class ClassDiv(GrpCls.ClassHtml):
  @property
  def css(self):
    """
    Description:
    ------------
    Property to the underlying CSS definition to be added to the style HTML tag of a component

    :rtype: AttrClsContainer.AttrDiv
    """
    if self._css_struct is None:
      self._css_struct = AttrClsContainer.AttrDiv(self.htmlObj)
    return self._css_struct

  @property
  def css_class(self):
    """
    Description:
    ------------
    The internal class used to put a custom Style to this object.
    Only 1 CSS class can be added to an HTML object

    :rtype: Classes.CatalogDiv.CatalogDiv
    """
    if self._css_class is None:
      self._css_class = Classes.CatalogDiv.CatalogDiv(self.htmlObj._report, self.classList['main'], html_id=self.htmlObj.htmlCode).no_border()
    return self._css_class


class ClassModal(GrpCls.ClassHtml):

  @property
  def css(self):
    """
    Description:
    ------------
    Property to the underlying CSS definition to be added to the style HTML tag of a component

    :rtype: AttrClsContainer.AttrModal
    """
    if self._css_struct is None:
      self._css_struct = AttrClsContainer.AttrModal(self.htmlObj)
    return self._css_struct

  @property
  def css_class(self):
    """
    Description:
    ------------
    The internal class used to put a custom Style to this object.
    Only 1 CSS class can be added to an HTML object

    :rtype: Classes.CatalogDiv.CatalogDiv
    """
    if self._css_class is None:
      self._css_class = Classes.CatalogDiv.CatalogDiv(self.htmlObj._report, self.classList['main'], html_id=self.htmlObj.htmlCode).modal()
    return self._css_class


class ClassDrawer(GrpCls.ClassHtml):

  def __init__(self, htmlObj):
    super(ClassDrawer, self).__init__(htmlObj)
    self._css_class_drawer, self._css_class_handle, self._css_class_content, self._css_class_nav = 4 * [None]
    self.classList['main'].add(self.css_class_drawer)
    self.classList['main'].add(self.css_class_handle)
    self.classList['main'].add(self.css_class_content)
    self.classList['main'].add(self.css_class_nav)

  @property
  def css(self):
    """
    Description:
    ------------
    Property to the underlying CSS definition to be added to the style HTML tag of a component

    :rtype: AttrClsContainer.AttrDiv
    """
    if self._css_struct is None:
      self._css_struct = AttrClsContainer.AttrDiv(self.htmlObj)
    return self._css_struct

  @property
  def css_class_drawer(self):
    """
    Description:
    ------------
    The internal class used to put a custom Style to this object.
    Only 1 CSS class can be added to an HTML object

    :rtype: Classes.CatalogDiv.CatalogDrawer
    """
    if self._css_class_drawer is None:
      self._css_class_drawer = Classes.CatalogDiv.CatalogDrawer(self.htmlObj._report, self.classList['main'], html_id=self.htmlObj.htmlCode).drawer()
    return self._css_class_drawer

  @property
  def css_class_nav(self):
    """
    Description:
    ------------
    The internal class used to put a custom Style to this object.
    Only 1 CSS class can be added to an HTML object

    :rtype: Classes.CatalogDiv.CatalogDrawer
    """
    if self._css_class_nav is None:
      self._css_class_nav = Classes.CatalogDiv.CatalogDrawer(self.htmlObj._report, self.classList['main'],
                                                                html_id=self.htmlObj.htmlCode).drawer()
    return self._css_class_nav

  @property
  def css_class_handle(self):
    """
    Description:
    ------------
    The internal class used to put a custom Style to this object.
    Only 1 CSS class can be added to an HTML object

    :rtype: Classes.CatalogDiv.CatalogDrawer
    """
    if self._css_class_handle is None:
      self._css_class_handle = Classes.CatalogDiv.CatalogDrawer(self.htmlObj._report, self.classList['main'],
                                                                html_id=self.htmlObj.htmlCode).handle()
    return self._css_class_handle

  @property
  def css_class_content(self):
    """
    Description:
    ------------
    The internal class used to put a custom Style to this object.
    Only 1 CSS class can be added to an HTML object

    :rtype: Classes.CatalogDiv.CatalogDrawer
    """
    if self._css_class_content is None:
      self._css_class_content = Classes.CatalogDiv.CatalogDrawer(self.htmlObj._report, self.classList['main'],
                                                                html_id=self.htmlObj.htmlCode).content()
    return self._css_class_content

