"""

"""


class CatalogGroup(object):
  def __init__(self, report, classListType):
    self.__rptObj, self.__class_list_type = report, classListType

  def _set_class(self, classObj):
    cssObj = classObj(self.__rptObj)
    cssObj.customize()
    self.__class_list_type.add(cssObj)
    return cssObj
