"""

"""


class CatalogGroup(object):
  def __init__(self, report, class_list_type, html_id=None):
    self.__rptObj, self.__class_list_type, self._html_id = report, class_list_type, html_id

  def _set_class(self, classObj):
    cssObj = classObj(self.__rptObj, html_id=self._html_id)
    #cssObj.customize()
    self.__class_list_type.add(cssObj)
    return cssObj
