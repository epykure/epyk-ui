"""
Group CSS class for all the Layouts components

Default HTML component per HTML tag
https://www.w3schools.com/cssref/css_default_values.asp
"""

from epyk.core.css import Classes
from epyk.core.css import Defaults_css
from epyk.core.css import Properties
from epyk.core.css.styles.effects import Effects
from epyk.core.css.styles.attributes import Commons
from epyk.core.css.styles.classes import CssStyle


class ClassPage(object):
  def __init__(self, rptObj):
    self._report = rptObj
    self.classList, self.__cls_defined, self.__cls_catalog = {"main": set(), 'other': set()}, None, None

  @property
  def defaults(self):
    """ The Default CSS Attributes in the framework """
    return Defaults_css

  @property
  def add_classes(self):
    """
    Property to get access to the catalog of CSS classes to be added to the HTML class tag component
    :rtype: Classes.Catalog
    """
    if self.__cls_catalog is None:
      self.__cls_catalog = Classes.Catalog(self._report, self.classList)
    return self.__cls_catalog._class_type('main')

  @property
  def define_classes(self):
    """
    Property to get access to the catalog of CSS classes to be loaded in the page
    Those classes will not be automatically added to any HTML tag and they need to be added manually
    :rtype: Classes.Catalog
    """
    if self.__cls_catalog is None:
      self.__cls_catalog = Classes.Catalog(self._report, self.classList)
    return self.__cls_catalog._class_type('other')

  def get_classes(self):
    """ Returns the list of Internal and bespoke classes to be added to the class HTML table on the component """
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
    Property to the underlying CSS definition to be added to the style HTML tag of a component
    :rtype: Commons
    """
    if self._css_struct is None:
      self._css_struct = Commons(self.htmlObj)
    return self._css_struct

  @property
  def css_class(self):
    """
    The internal class used to put a custom Style to this object.
    Only 1 CSS class can be added to an HTML object
    :rtype: Classes.CatalogDiv.CatalogDiv
    """
    if self._css_class is None:
      self._css_class = Classes.CatalogDiv.CatalogDiv(self.htmlObj._report, self.classList['main']).no_border()
    return self._css_class

  @property
  def defaults(self):
    """ The Default CSS Attributes in the framework """
    return Defaults_css

  @property
  def effects(self):
    """
    :rtype: Effects.Effects
    """
    if self.__cls_effects is None:
      self.__cls_effects = Effects.Effects(self.htmlObj._report, self.htmlObj)
    return self.__cls_effects

  @property
  def add_classes(self):
    """
    Property to get access to the catalog of CSS classes to be added to the HTML class tag component
    :rtype: Classes.Catalog
    """
    if self.__cls_catalog is None:
      self.__cls_catalog = Classes.Catalog(self.htmlObj._report, self.classList)
    return self.__cls_catalog._class_type('main')

  @property
  def define_classes(self):
    """
    Property to get access to the catalog of CSS classes to be loaded in the page
    Those classes will not be automatically added to any HTML tag and they need to be added manually
    :rtype: Classes.Catalog
    """
    if self.__cls_catalog is None:
      self.__cls_catalog = Classes.Catalog(self.htmlObj._report, self.classList)
    return self.__cls_catalog._class_type('other')

  def clear(self):
    """
    Remove the predefined class and set the default one for the div components
    :return:
    """
    self._css_class = Classes.CatalogDiv.CatalogDiv(self.htmlObj._report, self.classList['main']).no_border()

  def get_classes(self):
    """ Returns the list of Internal and bespoke classes to be added to the class HTML table on the component """
    for css_cls in self.classList.values():
      for c in css_cls:
        if hasattr(c, 'classname'):
          self.htmlObj._report._css[c.classname] = c
    return self.classList

  def get_classes_css(self):
    """

    :return:
    """
    css_frgs = {}
    for css_cls in self.classList.values():
      for c in css_cls:
        if hasattr(c, 'classname'):
          css_frgs[c.classname] = str(c)
    return css_frgs
