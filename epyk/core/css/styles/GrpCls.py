
from epyk.core.css import Classes
from epyk.core.css import Defaults_css
from epyk.core.css import Properties
from epyk.core.css.styles.effects import Effects
from epyk.core.css.styles.attributes import Attrs
from epyk.core.css.styles.attributes import Commons
from epyk.core.css.styles.classes import CssStyle


class ClassPage(object):
  def __init__(self, htmlObj):
    self.htmlObj, self._css_struct, self._css_class = htmlObj, None, None
    self.classList, self.__cls_defined, self.__cls_catalog = {"main": set(), 'other': set()}, None, None

  @property
  def css(self):
    """
    Description:
    ------------
    Property to the underlying CSS definition to be added to the style HTML tag of a component

    :rtype: Commons
    """
    if self._css_struct is None:
      self._css_struct = Commons(self.htmlObj)
    return self._css_struct

  @property
  def defaults(self):
    """
    Description:
    ------------
    The Default CSS Attributes in the framework
    """
    return Defaults_css

  @property
  def add_classes(self):
    """
    Description:
    ------------
    Property to get access to the catalog of CSS classes to be added to the HTML class tag component

    :rtype: Classes.Catalog
    """
    if self.__cls_catalog is None:
      self.__cls_catalog = Classes.Catalog(self._report, self.classList)
    return self.__cls_catalog._class_type('main')

  @property
  def define_classes(self):
    """
    Description:
    ------------
    Property to get access to the catalog of CSS classes to be loaded in the page
    Those classes will not be automatically added to any HTML tag and they need to be added manually

    :rtype: Classes.Catalog
    """
    if self.__cls_catalog is None:
      self.__cls_catalog = Classes.Catalog(self._report, self.classList)
    return self.__cls_catalog._class_type('other')

  def get_classes(self):
    """
    Description:
    ------------
    Returns the list of Internal and bespoke classes to be added to the class HTML table on the component
    """
    for css_cls in self.classList.values():
      for c in css_cls:
        if hasattr(c, 'classname'):
          self._report._css[c.classname] = c
    return self.classList


class ClassHtml(Properties.CssMixin):
  def __init__(self, htmlObj):
    self.htmlObj, self._css_struct, self._css_class = htmlObj, None, None
    self.classList, self.__cls_defined, self.__cls_catalog = {"main": set(), 'other': set()}, None, None
    self.__cls_effects = None
    self.classList['main'].add(self.css_class)

  @property
  def css(self):
    """
    Description:
    ------------
    Property to the underlying CSS definition to be added to the style HTML tag of a component

    :rtype: Commons
    """
    if self._css_struct is None:
      self._css_struct = Commons(self.htmlObj)
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
      self._css_class = Classes.CatalogDiv.CatalogDiv(self.htmlObj._report, self.classList['main'], html_id=self.htmlObj.htmlId).no_border()
    return self._css_class

  @property
  def defaults(self):
    """
    Description:
    ------------
    The Default CSS Attributes in the framework
    """
    return Defaults_css

  @property
  def effects(self):
    """
    Description:
    ------------
    Add animation effect to the component based either on a bespoke definition or a predefined one.

    :rtype: Effects.Effects
    """
    if self.__cls_effects is None:
      self.__cls_effects = Effects.Effects(self.htmlObj._report, self.htmlObj)
    return self.__cls_effects

  @property
  def add_classes(self):
    """
    Description:
    ------------
    Property to get access to the catalog of CSS classes to be added to the HTML class tag component

    :rtype: Classes.Catalog
    """
    if self.__cls_catalog is None:
      self.__cls_catalog = Classes.Catalog(self.htmlObj._report, self.classList)
    return self.__cls_catalog._class_type('main')

  @property
  def define_classes(self):
    """
    Description:
    ------------
    Property to get access to the catalog of CSS classes to be loaded in the page
    Those classes will not be automatically added to any HTML tag and they need to be added manually

    :rtype: Classes.Catalog
    """
    if self.__cls_catalog is None:
      self.__cls_catalog = Classes.Catalog(self.htmlObj._report, self.classList)
    return self.__cls_catalog._class_type('other')

  def clear_all(self):
    """
    Description:
    ------------
    Clear all the Style, Classes and CSS attrubites for the HTML component.
    Once this function is called it is possible to add new CSS attributes or classes using the different catalog
    """
    self.htmlObj.attr['css'] = {}
    self.classList['main'] = set()
    self._css_class = Classes.CatalogDiv.CatalogDiv(self.htmlObj._report, self.classList['main'], html_id=self.htmlObj.htmlId).no_margin()
    return self

  def clear(self):
    """
    Description:
    ------------
    Remove the predefined class and set the default one for the div components
    """
    self.classList['main'] = set()
    self._css_class = Classes.CatalogDiv.CatalogDiv(self.htmlObj._report, self.classList['main'], html_id=self.htmlObj.htmlId).no_border()
    return self

  def get_classes(self):
    """
    Description:
    ------------
    Returns the list of Internal and bespoke classes to be added to the class HTML table on the component
    """
    for css_cls in self.classList.values():
      for c in css_cls:
        if hasattr(c, 'get_ref'):
          self.htmlObj._report._css[c.get_ref()] = c
    return self.classList

  def get_classes_css(self):
    """
    Description:
    ------------

    :return:
    """
    css_frgs = {}
    for css_cls in self.classList.values():
      for c in css_cls:
        if hasattr(c, 'get_ref'):
          css_frgs[c.get_ref()] = str(c)
    return css_frgs
