
from epyk.core.js import Imports

from epyk.core.css.catalogs import CatalogButton
from epyk.core.css.catalogs import CatalogInput
from epyk.core.css.catalogs import CatalogChart
from epyk.core.css.catalogs import CatalogDiv
from epyk.core.css.catalogs import CatalogTree
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
    Description:
    ------------

    :param type:

    :return:
    """
    self.__class_list_type = self.__class_list[type]
    return self

  @property
  def button(self):
    """
    Description:
    ------------
    CSS Classes specific to the buttons components

    :rtype: CatalogButton.CatalogButton
    """
    if "button" not in self.__ctx:
      self.__ctx['button'] = CatalogButton.CatalogButton(self.__rptObj, self.__class_list_type)
    return self.__ctx['button']

  @property
  def layout(self):
    """
    Description:
    ------------

    :rtype: CatalogLayout.CatalogLayout
    """
    if "layout" not in self.__ctx:
      self.__ctx['layout'] = CatalogLayout.CatalogLayout(self.__rptObj, self.__class_list_type)
    return self.__ctx['layout']

  @property
  def dropdown(self):
    """
    Description:
    ------------
    CSS Classes specific to the dropdown components

    :rtype: CatalogTree.CssStyleDropdown
    """
    if "dropdown" not in self.__ctx:
      self.__ctx['dropdown'] = CatalogTree.CatalogDropDown(self.__rptObj, self.__class_list_type)
    return self.__ctx['dropdown']

  @property
  def table(self):
    """
    Description:
    ------------
    CSS Classes specific to the Table components

    :rtype: CatalogTable.CatalogTable
    """
    if "table" not in self.__ctx:
      self.__ctx['table'] = CatalogTable.CatalogTable(self.__rptObj, self.__class_list_type)
    return self.__ctx['table']

  @property
  def chart(self):
    """
    Description:
    ------------
    CSS Classes specific to the buttons components

    :rtype: CatalogButton.CatalogButton
    """
    if "chart" not in self.__ctx:
      self.__ctx['chart'] = CatalogChart.CatalogChart(self.__rptObj, self.__class_list_type)
    return self.__ctx['chart']

  @property
  def link(self):
    """
    Description:
    ------------

    :rtype: CatalogLink.CatalogLink
    """
    if "link" not in self.__ctx:
      self.__ctx['link'] = CatalogLink.CatalogLink(self.__rptObj, self.__class_list_type)
    return self.__ctx['link']

  @property
  def date(self):
    """
    Description:
    ------------

    :rtype: CatalogInput.CatalogDate
    """
    if "date" not in self.__ctx:
      self.__ctx['date'] = CatalogInput.CatalogDate(self.__rptObj, self.__class_list_type)
    return self.__ctx['date']

  @property
  def text(self):
    """
    Description:
    ------------

    :rtype: CatalogText.CatalogText
    """
    if "text" not in self.__ctx:
      self.__ctx['text'] = CatalogText.CatalogText(self.__rptObj, self.__class_list_type)
    return self.__ctx['text']

  @property
  def input(self):
    """
    Description:
    ------------
    """
    if "inputs" not in self.__ctx:
      self.__ctx['inputs'] = CatalogInput.CatalogInput(self.__rptObj, self.__class_list_type)
    return self.__ctx['inputs']

  @property
  def image(self):
    """
    """
    if "image" not in self.__ctx:
      self.__ctx['image'] = CatalogImg.CatalogImg(self.__rptObj, self.__class_list_type)
    return self.__ctx['image']

  @property
  def div(self):
    """
    Description:
    ------------

    :rtype: CatalogDiv.CatalogDiv
    """
    if "div" not in self.__ctx:
      self.__ctx['div'] = CatalogDiv.CatalogDiv(self.__rptObj, self.__class_list_type)
    return self.__ctx['div']

  @property
  def radio(self):
    """
    Description:
    ------------

    :rtype: CatalogRadio.CatalogRadio
    """
    if "radio" not in self.__ctx:
      self.__ctx['radio'] = CatalogRadio.CatalogRadio(self.__rptObj, self.__class_list_type)
    return self.__ctx['radio']

  def custom(self, cssClass):
    """
    Description:
    ------------

    :param cssClass:

    :return:
    """
    cssObj = cssClass(self.__rptObj)
    cssObj.customize()
    self.__class_list_type.add(cssObj)
    return self

  def customFile(self, filename, path=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param filename:
    :param path: String. Optional. The full path of the external CSS file. If None the user part in Imports.STATIC_PATH
                 will be used
    :return:
    """
    if path is None:
      self.__rptObj.cssLocalImports.add("%s/css/%s" % (Imports.STATIC_PATH.replace("\\", "/"), filename))
    else:
      self.__rptObj.cssLocalImports.add("%s/%s" % (path, filename))
    return self

  def customText(self, text):
    """
    Description:
    ------------

    :param text:
    :return:
    """
    self.__rptObj._cssText.append(text)
    return self

  def anonymous_cls(self, attrs):
    pass

  def external(self, classname):
    """
    Description:
    ------------
    Add external CSS classes to a component

    :param classname: String or array

    :return:
    """
    if isinstance(classname, list):
      classname = " ".join(classname)
    self.__class_list_type.add(classname)
