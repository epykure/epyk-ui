"""

"""

from epyk.core.css.catalogs import CatalogButton
from epyk.core.css.catalogs import CatalogInput
from epyk.core.css.catalogs import CatalogChart
from epyk.core.css.catalogs import CatalogDiv
from epyk.core.css.catalogs import CatalogIcons
from epyk.core.css.catalogs import CatalogLayout
from epyk.core.css.catalogs import CatalogLink
from epyk.core.css.catalogs import CatalogList
from epyk.core.css.catalogs import CatalogPopup
from epyk.core.css.catalogs import CatalogRadio
from epyk.core.css.catalogs import CatalogSelect
from epyk.core.css.catalogs import CatalogTable
from epyk.core.css.catalogs import CatalogText
from epyk.core.css.catalogs import CatalogImg


class Catalog(object):

  def __init__(self, report, classList):
    self.__rptObj, self.__class_list = report, classList
    self.__ctx = {}

  def _class_type(self, type):
    """

    :param type:
    :return:
    """
    self.__class_list_type = self.__class_list[type]
    return self

  @property
  def button(self):
    """
    CSS Classes specific to the buttons components

    :rtype: CatalogButton.CatalogButton
    """
    if "button" not in self.__ctx:
      self.__ctx['button'] = CatalogButton.CatalogButton(self.__rptObj, self.__class_list_type)
    return self.__ctx['button']

  @property
  def date(self):
    """

    :rtype: CatalogInput.CatalogDate
    """
    if "date" not in self.__ctx:
      self.__ctx['date'] = CatalogInput.CatalogDate(self.__rptObj, self.__class_list_type)
    return self.__ctx['date']

  @property
  def input(self):
    """
    """
    if self.__inputs is None:
      self.__inputs = CatalogInput.CatalogInput(self.__rptObj, self.__class_list_type)
    return self.__inputs

  @property
  def image(self):
    """
    """
    if self.__image is None:
      self.__image = CatalogImg(self.__rptObj, self.__class_list_type)
    return self.__image

  def custom(self):
    """ """
    pass

  def anonymous_cls(self, attrs):
    pass

  def external(self, classname):
    """ Add external CSS classes to a component """
    self.__class_list_type.add(classname)
