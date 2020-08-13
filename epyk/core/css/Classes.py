#!/usr/bin/python
# -*- coding: utf-8 -*-

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
from epyk.core.css.catalogs import CatalogMedia
from epyk.core.css.catalogs import CatalogImg


class Catalog(object):

  def __init__(self, report, classList):
    self.__rptObj, self.__class_list = report, classList
    self.__ctx = {}

  def font_face(self, font_family, src, stretch="normal", style="normal", weight="normal"):
    """
    Description:
    ------------
    With the @font-face rule, web designers do not have to use one of the "web-safe" fonts anymore.

    In the @font-face rule you must first define a name for the font (e.g. myFirstFont), and then point to the font file.

    Entry to get a font family from a local file to avoid loading it online.
    This is safer but also improve the speed of the website

    https://www.w3schools.com/cssref/css3_pr_font-face_rule.asp

    TODO: Use the page property self.__rptObj._props['css']["font-face"] in the CSS definition

    Attributes:
    ----------
    :param font_family: String. Required. Defines the name of the font
    :param src: String. Required. Defines the URL(s) where the font should be downloaded from
    :param stretch: String. Optional. Defines how the font should be stretched. Default value is "normal"
    :param style: String. Required. Optional. Defines how the font should be styled. Default value is "normal"
    :param weight: String. Required. Optional. Defines the boldness of the font. Default value is "normal"
    """
    self.__rptObj._props['css']["font-face"][font_family] = {'src': "url(%s)" % src, 'font-stretch': stretch,
                                                             'font-style': style, 'font-weight': weight}
    return self

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
  def select(self):
    """
    Description:
    ------------
    CSS Classes specific to the select compatibility components

    :rtype: CatalogMedia.CatalogSelect
    """
    if "select" not in self.__ctx:
      self.__ctx['select'] = CatalogSelect.CatalogSelect(self.__rptObj, self.__class_list_type)
    return self.__ctx['select']

  @property
  def screens(self):
    """
    Description:
    ------------
    CSS Classes specific to the screen compatibility components

    :rtype: CatalogMedia.CatalogMedia
    """
    if "screens" not in self.__ctx:
      self.__ctx['screens'] = CatalogMedia.CatalogMedia(self.__rptObj, self.__class_list_type)
    return self.__ctx['screens']

  @property
  def icon(self):
    """
    Description:
    ------------
    CSS Classes specific to the Icons components

    :rtype: CatalogIcons.CatalogIcon
    """
    if "icon" not in self.__ctx:
      self.__ctx['icon'] = CatalogIcons.CatalogIcon(self.__rptObj, self.__class_list_type)
    return self.__ctx['icon']

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

    :rtype: CatalogInput.CatalogInput
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
    Register a bespoke external class to the report object

    Attributes:
    ----------
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
    Add an external CSS file to the final HTML report

    Attributes:
    ----------
    :param filename: String. The file name
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
    Add a bespoke CSS fragment

    Attributes:
    ----------
    :param text: String. The CSS fragment to be added to the HTML report. THis can be a class or a group of class

    :return:
    """
    self.__rptObj._cssText.append(text)
    return self

  def anonymous_cls(self, attrs):
    """
    Description:
    ------------
    Create a bespoke class based on the various attributes.
    This will internal build the class and return it

    Usage::

      v_cls = rptObj.css.anonymous_cls({
      '_attrs': {'color': 'green', 'cursor': 'pointer'},
      '_hover': {'color': 'red'}})

    Attributes:
    ----------
    :param attrs: Dictionary. The expected class attributes

    :return: The Python class
    """
    import hashlib

    from epyk.core.css.styles.classes import CssStyle

    has_style = str(hashlib.sha1(str(attrs).encode()).hexdigest())
    attrs['classname'] = "style_%s" % has_style
    meta_cls = type('Style%s' % has_style, (CssStyle.Style,), attrs)
    return meta_cls

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
