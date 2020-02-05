"""

"""

from epyk.core.css import Classes


class GrpButton(object):
  def __init__(self, rptObj, classList):
    self.__rptObj = rptObj
    self.__classList = classList
    self.__load()

  def __load(self):
    Classes.Catalog(self.__rptObj, self.__classList['main']).basic()

  @property
  def basic(self):
    return Classes.CatalogButton(self.__rptObj, self.__classList['main']).basic()


class GrpButtonCheckBox(object):
  def __init__(self, rptObj, classList):
    self.__rptObj = rptObj
    self.__classList = classList
    self.__load()

  def __load(self):
    Classes.CatalogButton(self.__rptObj, self.__classList['main']).basic()

  @property
  def basic(self): return Classes.CatalogButton(self.__rptObj, self.__classList['main']).basic()
