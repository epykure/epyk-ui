

from epyk.core.css.categories import CssGrpCls
from epyk.core.css import Classes


class GrpDiv(object):
  def __init__(self, rptObj, classList):
    self.__rptObj = rptObj
    self.__classList = classList
    self.__load()

  def __load(self):
    Classes.CatalogButton(self.__rptObj, self.__classList['main']).basic()

  @property
  def basic(self):
    return Classes.CatalogButton(self.__rptObj, self.__classList['main']).basic()


class ClassDiv(CssGrpCls.ClassHtml):
  def __init__(self, htmlObj):
    self.__htmlObj = htmlObj
    self.classList, self.__cls_defined, self.__cls_catalog = {"main": set(), 'other': set()}, None, None
    self.__load()

  def __load(self):
    if self.__cls_defined is None:
      self.__cls_defined = GrpDiv(self.__htmlObj._report, self.classList)
    return self.__cls_defined

  @property
  def defined(self):
    return self.__load()