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
from epyk.core.css.catalogs import CatalogStd


class Catalog:

  def __init__(self, page, classList):
    self.page, self.__class_list = page, classList
    self.__ctx = {}

  def font_face(self, font_family, src, stretch="normal", style="normal", weight="normal"):
    """
    Description:
    ------------
    With the @font-face rule, web designers do not have to use one of the "web-safe" fonts anymore.

    In the @font-face rule you must first define a name for the font (e.g. myFirstFont), and then point to
    the font file.

    Entry to get a font family from a local file to avoid loading it online.
    This is safer but also improve the speed of the website.

    Related Pages:

      https://www.w3schools.com/cssref/css3_pr_font-face_rule.asp

    Usage:
    -----

    Attributes:
    ----------
    :param font_family: String. Required. Defines the name of the font.
    :param src: String. Required. Defines the URL(s) where the font should be downloaded from.
    :param stretch: String. Optional. Defines how the font should be stretched. Default value is "normal".
    :param style: String. Optional. Defines how the font should be styled. Default value is "normal".
    :param weight: String. Optional. Defines the boldness of the font. Default value is "normal".
    """
    self.page.properties.css.font_face(font_family, src, stretch, style, weight)
    return self

  def _class_type(self, cls_type):
    """
    Description:
    ------------
    Change the current class type to the one defined and return the internal class object.

    Usage:
    -----

    Attributes:
    ----------
    :param cls_type: String. The alias of the class other or main.
    """
    self.__class_list_type = self.__class_list[cls_type]
    return self

  @property
  def other(self):
    """
    Description:
    ------------
    Get the list of CSS Classes impacting to the component but not added to the class tag of the HTML component.

    Usage:
    -----
    """
    self.__class_list_type = self.__class_list['other']
    return self.__class_list_type

  @property
  def main(self):
    """
    Description:
    ------------
    Get the list of CSS Classes added to the component and to the class tag of the component.

    Usage:
    -----
    """
    self.__class_list_type = self.__class_list['main']
    return self.__class_list_type

  @property
  def std(self):
    """
    Description:
    ------------
    Shortcut to standard CSS classes (for layout purposes like margin, padding...).

    Usage:
    -----

      t1 = page.ui.title("Templates structure")
      t1.style.add_classes.std.margin(7)

    Related Pages:

      https://getbootstrap.com/docs/4.0/utilities/spacing/

    :rtype: CatalogStd.CatalogSt
    """
    if "std" not in self.__ctx:
      self.__ctx['std'] = CatalogStd.CatalogStd(self.page, self.__class_list)
    return self.__ctx['std']

  @property
  def button(self):
    """
    Description:
    ------------
    CSS Classes specific to the buttons components.

    Usage:
    -----

    :rtype: CatalogButton.CatalogButton
    """
    if "button" not in self.__ctx:
      self.__ctx['button'] = CatalogButton.CatalogButton(self.page, self.__class_list_type)
    return self.__ctx['button']

  @property
  def select(self):
    """
    Description:
    ------------
    CSS Classes specific to the select compatibility components.

    Usage:
    -----

    :rtype: CatalogMedia.CatalogSelect
    """
    if "select" not in self.__ctx:
      self.__ctx['select'] = CatalogSelect.CatalogSelect(self.page, self.__class_list_type)
    return self.__ctx['select']

  @property
  def screens(self):
    """
    Description:
    ------------
    CSS Classes specific to the screen compatibility components.

    Usage:
    -----

    :rtype: CatalogMedia.CatalogMedia
    """
    if "screens" not in self.__ctx:
      self.__ctx['screens'] = CatalogMedia.CatalogMedia(self.page, self.__class_list_type)
    return self.__ctx['screens']

  @property
  def icon(self):
    """
    Description:
    ------------
    CSS Classes specific to the Icon components.

    Usage:
    -----

    :rtype: CatalogIcons.CatalogIcon
    """
    if "icon" not in self.__ctx:
      self.__ctx['icon'] = CatalogIcons.CatalogIcon(self.page, self.__class_list_type)
    return self.__ctx['icon']

  @property
  def layout(self):
    """
    Description:
    ------------
    CSS Classes specific to Layout / Container components.

    Usage:
    -----

    :rtype: CatalogLayout.CatalogLayout
    """
    if "layout" not in self.__ctx:
      self.__ctx['layout'] = CatalogLayout.CatalogLayout(self.page, self.__class_list_type)
    return self.__ctx['layout']

  @property
  def dropdown(self):
    """
    Description:
    ------------
    CSS Classes specific to the DropDown components.

    Usage:
    -----

    :rtype: CatalogTree.CssStyleDropdown
    """
    if "dropdown" not in self.__ctx:
      self.__ctx['dropdown'] = CatalogTree.CatalogDropDown(self.page, self.__class_list_type)
    return self.__ctx['dropdown']

  @property
  def table(self):
    """
    Description:
    ------------
    CSS Classes specific to the Table components.

    Usage:
    -----

    :rtype: CatalogTable.CatalogTable
    """
    if "table" not in self.__ctx:
      self.__ctx['table'] = CatalogTable.CatalogTable(self.page, self.__class_list_type)
    return self.__ctx['table']

  @property
  def chart(self):
    """
    Description:
    ------------
    CSS Classes specific to Chart components.

    Usage:
    -----

    :rtype: CatalogButton.CatalogButton
    """
    if "chart" not in self.__ctx:
      self.__ctx['chart'] = CatalogChart.CatalogChart(self.page, self.__class_list_type)
    return self.__ctx['chart']

  @property
  def link(self):
    """
    Description:
    ------------
    CSS Classes specific to Link components.

    Usage:
    -----

    :rtype: CatalogLink.CatalogLink
    """
    if "link" not in self.__ctx:
      self.__ctx['link'] = CatalogLink.CatalogLink(self.page, self.__class_list_type)
    return self.__ctx['link']

  @property
  def date(self):
    """
    Description:
    ------------
    CSS Classes specific to Date components.

    Usage:
    -----

    :rtype: CatalogInput.CatalogDate
    """
    if "date" not in self.__ctx:
      self.__ctx['date'] = CatalogInput.CatalogDate(self.page, self.__class_list_type)
    return self.__ctx['date']

  @property
  def text(self):
    """
    Description:
    ------------
    CSS Classes specific to Text components.

    Usage:
    -----

    :rtype: CatalogText.CatalogText
    """
    if "text" not in self.__ctx:
      self.__ctx['text'] = CatalogText.CatalogText(self.page, self.__class_list_type)
    return self.__ctx['text']

  @property
  def input(self):
    """
    Description:
    ------------
    CSS Classes specific to Input components.

    Usage:
    -----

    :rtype: CatalogInput.CatalogInput
    """
    if "inputs" not in self.__ctx:
      self.__ctx['inputs'] = CatalogInput.CatalogInput(self.page, self.__class_list_type)
    return self.__ctx['inputs']

  @property
  def image(self):
    """
    Description:
    ------------
    CSS Classes specific to Image components.

    Usage:
    -----

    :rtype: CatalogImg.CatalogImg
    """
    if "image" not in self.__ctx:
      self.__ctx['image'] = CatalogImg.CatalogImg(self.page, self.__class_list_type)
    return self.__ctx['image']

  @property
  def div(self):
    """
    Description:
    ------------
    CSS Classes specific to Div / Container components.

    Usage:
    -----

    :rtype: CatalogDiv.CatalogDiv
    """
    if "div" not in self.__ctx:
      self.__ctx['div'] = CatalogDiv.CatalogDiv(self.page, self.__class_list_type)
    return self.__ctx['div']

  @property
  def shapes(self):
    """
    Description:
    ------------
    CSS Classes specific to Div / Container components.

    Usage:
    -----

    :rtype: CatalogDiv.CatalogShapes
    """
    if "shapes" not in self.__ctx:
      self.__ctx['shapes'] = CatalogDiv.CatalogShapes(self.page, self.__class_list_type)
    return self.__ctx['shapes']

  @property
  def radio(self):
    """
    Description:
    ------------
    CSS Classes specific to Radio button components.

    Usage:
    -----

    :rtype: CatalogRadio.CatalogRadio
    """
    if "radio" not in self.__ctx:
      self.__ctx['radio'] = CatalogRadio.CatalogRadio(self.page, self.__class_list_type)
    return self.__ctx['radio']

  def custom(self, css_cls):
    """
    Description:
    ------------
    Register a bespoke external class to the report object.

    Usage:
    -----

    Attributes:
    ----------
    :param css_cls: Class. The python class to be used as a CSS Class in the framework.
    """
    css_cls_obj = css_cls(self.page)
    css_cls_obj.customize()
    self.__class_list_type.add(css_cls_obj)
    return self

  def customFile(self, filename, path=None):
    """
    Description:
    ------------
    Add an external CSS file to the final HTML report.

    Usage:
    -----

    Attributes:
    ----------
    :param filename: String. The file name.
    :param path: String. Optional. The full path of the external CSS file. If None the user part in Imports.STATIC_PATH
                 will be used.
    """
    if path is None:
      self.page.cssLocalImports.add("%s/css/%s" % (Imports.STATIC_PATH.replace("\\", "/"), filename))
    else:
      self.page.cssLocalImports.add("%s/%s" % (path, filename))
    return self

  def customText(self, text):
    """
    Description:
    ------------
    Add a bespoke CSS fragment.

    Usage:
    -----

    Attributes:
    ----------
    :param text: String. The CSS fragment to be added to the HTML report. This can be a class or a group of class.
    """
    self.page.properties.css.add_text(text)
    return self

  def anonymous_cls(self, attrs):
    """
    Description:
    ------------
    Create a bespoke class based on the various attributes.
    This will internal build the class and return it.

    Usage:
    -----

      v_cls = page.css.anonymous_cls({
      '_attrs': {'color': 'green', 'cursor': 'pointer'},
      '_hover': {'color': 'red'}})

    Attributes:
    ----------
    :param attrs: Dictionary. The expected class attributes.

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
    Add external CSS classes to a component.

    Usage:
    -----

    Attributes:
    ----------
    :param classname: String | array.
    """
    if isinstance(classname, list):
      classname = " ".join(classname)
    self.__class_list_type.add(classname)
