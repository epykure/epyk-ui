"""
Group CSS class for all the Layouts components
"""

from epyk.core.css import Classes
from epyk.core.css import Defaults
from epyk.core.css import Properties


class ClassPage(object):
  def __init__(self, rptObj):
    self._report = rptObj
    self.classList, self.__cls_defined, self.__cls_catalog = {"main": set(), 'other': set()}, None, None

  @property
  def defaults(self):
    return Defaults

  @property
  def add_classes(self):
    """ CSS class catalog """
    if self.__cls_catalog is None:
      self.__cls_catalog = Classes.Catalog(self._report, self.classList)
    return self.__cls_catalog._class_type('main')

  @property
  def define_classes(self):
    """ CSS class catalog """
    if self.__cls_catalog is None:
      self.__cls_catalog = Classes.Catalog(self._report, self.classList)
    return self.__cls_catalog._class_type('other')

  def get_classes(self):
    """

    :return:
    """
    for css_cls in self.classList.values():
      for c in css_cls:
        if hasattr(c, 'classname'):
          self._report._css[c.classname] = c
    return self.classList


class ClassHtml(Properties.CssMixin):
  def __init__(self, htmlObj):
    self.__htmlObj = htmlObj
    self.classList, self.__cls_defined, self.__cls_catalog = {"main": set(), 'other': set()}, None, None

  @property
  def defaults(self):
    """ Default CSS attributes """
    return Defaults

  @property
  def add_classes(self):
    """ CSS class catalog """
    if self.__cls_catalog is None:
      self.__cls_catalog = Classes.Catalog(self.__htmlObj._report, self.classList)
    return self.__cls_catalog._class_type('main')

  @property
  def define_classes(self):
    """ CSS class catalog """
    if self.__cls_catalog is None:
      self.__cls_catalog = Classes.Catalog(self.__htmlObj._report, self.classList)
    return self.__cls_catalog._class_type('other')

  def get_classes(self):
    """

    :return:
    """
    for css_cls in self.classList.values():
      for c in css_cls:
        if hasattr(c, 'classname'):
          self.__htmlObj._report._css[c.classname] = c
    return self.classList
