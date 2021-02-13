#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.css import Classes
from epyk.core.css import Defaults_css
from epyk.core.css import Properties
from epyk.core.css.styles.effects import Effects
from epyk.core.css.styles.attributes import Attrs # for the rtype in the documentation
from epyk.core.css.styles.attributes import Commons, Body, Empty
from epyk.core.css.styles.classes import CssStyle, CssStyleScrollbar, CssStylesPage
from epyk.core.py import OrderedSet


class ClassPage(object):
  def __init__(self, htmlObj):
    self.htmlObj, self._css_struct, self._css_class = htmlObj, None, None
    self.__webkitscrollbar, self.__webkitscrollbar_track, self.__webkitscrollbar_thumb, self.__selection, self.__moz_selection = 5 * [None]
    self.__contenteditable = None
    self.classList, self.__cls_defined, self.__cls_catalog = {"main": OrderedSet(), 'other': OrderedSet()}, None, None

  @property
  def css(self):
    """
    Description:
    ------------
    Property to the underlying CSS definition to be added to the style HTML tag of a component

    :rtype: Commons
    """
    if self._css_struct is None:
      self._css_struct = Body(self.htmlObj)
    return self._css_struct

  @property
  def css_class(self):
    """
    Description:
    ------------
    The internal class used to put a custom Style to this object.
    Only 1 CSS class can be added to an HTML object

    :rtype: Classes.CatalogDiv.CatalogDiv
    """
    if self._css_class is None:
      self._css_class = Classes.CatalogDiv.CatalogDiv(self.htmlObj._report, self.classList['main'],
                                                      html_id=self.htmlObj.htmlCode).no_border()
    return self._css_class

  @property
  def globals(self):
    """
    Description:
    ------------
    Reference for all the global setting in the page.
    This should be changed in order to be the proxy to the Default CSS settings in the framework.

    Changing this should only impact the report default settings

    TODO: Extend to more than the font
    """
    return Defaults_css.Font

  @property
  def scrollbar_webkit(self):
    """
    Description:
    ------------

    :rtype: CssStyleScrollbar.CssWebkitScrollbar
    """
    if not self.__webkitscrollbar:
      self.__webkitscrollbar = CssStyleScrollbar.CssWebkitScrollbar(self.htmlObj._report)
    return  self.__webkitscrollbar

  @property
  def scrollbar_webkit_thumb(self):
    """
    Description:
    ------------

    :rtype: CssStyleScrollbar.CssWebkitScrollbarThumb
    """
    if not self.__webkitscrollbar_thumb:
      self.__webkitscrollbar_thumb = CssStyleScrollbar.CssWebkitScrollbarThumb(self.htmlObj._report)
    return  self.__webkitscrollbar_thumb

  @property
  def scrollbar_webkit_track(self):
    """
    Description:
    ------------

    :rtype: CssStyleScrollbar.CssWebkitScrollbarTrack
    """
    if not self.__webkitscrollbar_track:
      self.__webkitscrollbar_track = CssStyleScrollbar.CssWebkitScrollbarTrack(self.htmlObj._report)
    return  self.__webkitscrollbar_track

  @property
  def selection(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.w3schools.com/howto/howto_css_text_selection.asp

    :rtype: CssStyleScrollbar.CssWebkitSelection
    """
    if not self.__selection:
      self.__selection = CssStyleScrollbar.CssWebkitSelection(self.htmlObj._report)
    return self.__selection

  @property
  def moz_selection(self):
    """
    Description:
    ------------

    Related Pages:

      https://www.w3schools.com/howto/howto_css_text_selection.asp

    :rtype: CssStyleScrollbar.CssWebkitMozSelection
    """
    if not self.__moz_selection:
      self.__moz_selection = CssStyleScrollbar.CssWebkitMozSelection(self.htmlObj._report)
    return self.__moz_selection

  def contenteditable(self):
    """
    Description:
    ------------
    Set the border color of the editable content according to the selected theme

    Related Pages:

      https://www.w3schools.com/howto/howto_css_contenteditable_border.asp

    :rtype: CssStylesPage.CssPageContentDditable
    """
    if not self.__contenteditable:
      self.__contenteditable = CssStylesPage.CssPageContentEditable(self.htmlObj._report)
      self.classList['other'].add(self.__contenteditable)
    return self.__contenteditable

  @property
  def defaults(self):
    """
    Description:
    ------------
    The Default CSS Attributes in the framework
    """
    return Defaults_css

  @property
  def add_classes(self):
    """
    Description:
    ------------
    Property to get access to the catalog of CSS classes to be added to the HTML class tag component

    :rtype: Classes.Catalog
    """
    if self.__cls_catalog is None:
      self.__cls_catalog = Classes.Catalog(self.htmlObj._report, self.classList)
    return self.__cls_catalog._class_type('main')

  @property
  def define_classes(self):
    """
    Description:
    ------------
    Property to get access to the catalog of CSS classes to be loaded in the page
    Those classes will not be automatically added to any HTML tag and they need to be added manually

    :rtype: Classes.Catalog
    """
    if self.__cls_catalog is None:
      self.__cls_catalog = Classes.Catalog(self.htmlObj._report, self.classList)
    return self.__cls_catalog._class_type('other')

  def get_classes(self):
    """
    Description:
    ------------
    Returns the list of Internal and bespoke classes to be added to the class HTML table on the component
    """
    for css_cls in self.classList.values():
      for c in css_cls:
        if hasattr(c, 'get_ref'):
          self.htmlObj._report._css[c.get_ref()] = str(c)
    return self.classList

  def get_classes_css(self):
    """
    Description:
    ------------

    """
    self.classList['other'].add(self.scrollbar_webkit)
    self.classList['other'].add(self.scrollbar_webkit_thumb)
    self.classList['other'].add(self.scrollbar_webkit_track)
    self.classList['other'].add(self.selection)
    self.classList['other'].add(self.moz_selection)

    css_frgs = {}
    for css_cls in self.classList.values():
      for c in css_cls:
        if hasattr(c, 'get_ref'):
          css_frgs[c.get_ref()] = str(c)
    return css_frgs

  def custom_class(self, css_attrs, classname=None, selector=None, is_class=True):
    """
    Description:
    -----------
    This will create dynamic CSS class which will not be added to any component.
    The class definition can then be reused in mutiple components.

    The CSS style of the body can only be done using predefined classes or inline CSS

    Usage::

      rptObj.body.style.custom_class(css_attrs={"_attrs": {"fill": 'red'}}, classname='nvd3.nv-pie .nv-pie-title')

    Attributes:
    ----------
    :param css_attrs: Nested dictionary with the different attributes
    :param classname: Optional. String. The classname in the CSS definition
    :param selector: Optional. String. The class selector (if it is not a classname using . but a strict definition)
    :param is_class: Optional. Boolean. Automatically transform the name to a CSS class definition by adding a .
    """
    if classname is None:
      cls_def = {"classname": False, '_selector': selector}
    else:
      cls_def = {"classname": classname}
    if not '_attrs' in css_attrs and not '_hover' in css_attrs:
      css_attrs = {"_attrs": css_attrs}
    css_attrs['is_class'] = is_class
    cls_def.update(css_attrs)
    v_cls = type(classname, (CssStyle.Style, ), cls_def)
    cls_obj = v_cls(self.htmlObj._report)
    self.classList['other'].add(cls_obj)
    return cls_def


class ClassHtml(Properties.CssMixin):
  def __init__(self, htmlObj):
    self.htmlObj, self._css_struct, self._css_class = htmlObj, None, None
    self.classList, self.__cls_defined, self.__cls_catalog = {"main": OrderedSet(), 'other': OrderedSet()}, None, None
    self.__cls_effects, self.__css_virtual = None, {}
    self.classList['main'].add(self.css_class)

  @property
  def varName(self):
    """
    Description:
    ------------
    Unique identifier for the CSS object on the Javascript side
    """
    return "%s_css" % self.htmlObj.htmlCode

  @property
  def css(self):
    """
    Description:
    ------------
    Property to the underlying CSS definition to be added to the style HTML tag of a component

    :rtype: Commons
    """
    if self._css_struct is None:
      self._css_struct = Commons(self.htmlObj)
    return self._css_struct

  @property
  def css_class(self):
    """
    Description:
    ------------
    The internal class used to put a custom Style to this object.
    Only 1 CSS class can be added to an HTML object

    :rtype: Classes.CatalogDiv.CatalogDiv
    """
    if self._css_class is None:
      self._css_class = Classes.CatalogDiv.CatalogDiv(self.htmlObj._report, self.classList['main'], html_id=self.htmlObj.htmlCode).no_border()
    return self._css_class

  @property
  def defaults(self):
    """
    Description:
    ------------
    The Default CSS Attributes in the framework
    """
    return Defaults_css

  @property
  def effects(self):
    """
    Description:
    ------------
    Add animation effect to the component based either on a bespoke definition or a predefined one.

    :rtype: Effects.Effects
    """
    if self.__cls_effects is None:
      self.__cls_effects = Effects.Effects(self.htmlObj._report, self.htmlObj)
    return self.__cls_effects

  @property
  def add_classes(self):
    """
    Description:
    ------------
    Property to get access to the catalog of CSS classes to be added to the HTML class tag component

    :rtype: Classes.Catalog
    """
    if self.__cls_catalog is None:
      self.__cls_catalog = Classes.Catalog(self.htmlObj._report, self.classList)
    return self.__cls_catalog._class_type('main')

  @property
  def define_classes(self):
    """
    Description:
    ------------
    Property to get access to the catalog of CSS classes to be loaded in the page
    Those classes will not be automatically added to any HTML tag and they need to be added manually

    :rtype: Classes.Catalog
    """
    if self.__cls_catalog is None:
      self.__cls_catalog = Classes.Catalog(self.htmlObj._report, self.classList)
    return self.__cls_catalog._class_type('other')

  def attr(self, key, name, dflt=None, suffix="temp"):
    """
    Description:
    ------------
    The attr() function returns the value of an attribute of the selected elements.

    Related Pages:

      https://www.w3schools.com/cssref/func_attr.asp

    Attributes:
    ----------
    :param key:
    :param name:
    :param suffix:
    """
    key_selector = "_%s" % suffix
    if not key_selector in self.__css_virtual:
      self.__css_virtual[key_selector] = {}
    if dflt is not None:
      self.__css_virtual[key_selector].update({key: "attr(%s, %s)" % (name, dflt)})
    else:
      self.__css_virtual[key_selector].update({key: "attr(%s)" % name})

  def attr_content(self, name):
    """
    Description:
    ------------
    Use of the attr function for the before content value.
    This is the unique valid use of this CSS function in most of the browser

    Related Pages:

      https://gomakethings.com/how-to-access-and-use-data-attributes-in-your-css/

    Attributes:
    ----------
    :param name:
    """
    self.attr("content", name, suffix='before')

  def hover(self, attrs):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param attrs:
    """
    self.selector("hover", attrs)

  def standard(self, percent=10, width_adj=True):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param percent: Integer. Optional. The percentage of space on the left and right
    :param width_adj: Boolean. Optional. Adjust the width of the component considering this space
    """
    if width_adj:
      self.css.margins(left=(percent, '%'), right=(percent, '%'))
    else:
      self.css.margin_left = "%s%%" % percent
      self.css.margin_right = "%s%%" % percent

  def selector(self, suffix, attrs):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param suffix:
    :param attrs:
    """
    key_selector = "_%s" % suffix
    if not key_selector in self.__css_virtual:
      self.__css_virtual[key_selector] = {}
    self.__css_virtual[key_selector].update(attrs)

  def add_custom_class(self, css_attrs, classname=None, selector=None, is_class=True):
    """
    Description:
    -----------
    This will create dynamic CSS class which will not be added to any component.
    The class definition can then be reused in mutiple components.

    The CSS style of the body can only be done using predefined classes or inline CSS

    Usage::

      rptObj.body.style.custom_class(css_attrs={"_attrs": {"fill": 'red'}}, classname='nvd3.nv-pie .nv-pie-title')

    Attributes:
    ----------
    :param css_attrs: Nested dictionary with the different attributes
    :param classname: Optional. String. The classname in the CSS definition
    :param selector: Optional. String. The class selector (if it is not a classname using . but a strict definition)
    :param is_class: Optional. Boolean. Automatically transform the name to a CSS class definition by adding a .
    """
    if classname is None:
      cls_def = {"classname": False, '_selector': selector}
    else:
      cls_def = {"classname": classname}
    if not '_attrs' in css_attrs and not '_hover' in css_attrs:
      css_attrs = {"_attrs": css_attrs}
    css_attrs['is_class'] = is_class
    cls_def.update(css_attrs)
    v_cls = type(classname, (CssStyle.Style, ), cls_def)
    cls_obj = v_cls(self.htmlObj._report)
    self.classList['other'].add(cls_obj)
    return cls_def

  def no_class(self):
    """
    Description:
    ------------
    Clear all the Style, Classes and CSS attrubites for the HTML component.
    Once this function is called it is possible to add new CSS attributes or classes using the different catalog

    :return: self to allow the chaining
    """
    self.classList['main'] = OrderedSet()
    self._css_class = None
    return self

  def clear_style(self):
    """
    Description:
    ------------
    Clear all the inline CSS styles defined for the component

    :return: self to allow the chaining
    """
    self.htmlObj.attr['css'] = {}
    self.css.attrs = self.htmlObj.attr['css']
    return self

  def clear(self, no_default=False):
    """
    Description:
    ------------
    Remove the predefined class and set the default one for the div components

    Attributes:
    ----------
    :param no_default: Boolean. Remove the default class

    :return: self to allow the chaining
    """
    self.classList['main'] = OrderedSet()
    if Defaults_css.DEFAULT_STYLE == 'no_border':
      if no_default:
        self._css_class = ""
      else:
        self._css_class = Classes.CatalogDiv.CatalogDiv(self.htmlObj._report, self.classList['main'], html_id=self.htmlObj.htmlCode).no_border()
    else:
      self._css_class = Defaults_css.DEFAULT_STYLE
    self.htmlObj.attr['class'] = self.classList['main']
    return self

  def clear_all(self, no_default=False):
    """
    Description:
    ------------
    Clear all the Style, Classes and CSS attrubites for the HTML component.
    Once this function is called it is possible to add new CSS attributes or classes using the different catalog
    Set the default style to no marging and no padding

    Attributes:
    ----------
    :param no_default: Boolean. Remove the default class

    :return: self to allow the chaining
    """
    self.clear_style()
    self.clear(no_default)
    return self

  def builder(self, name, js_frg):
    """
    Description:
    ------------
    Attach a Javascript Builder to a CSS style.
    It will be triggered only once for all the HTML components using this style

    Attributes:
    ----------
    :param name: String. The Javascript variable name
    :param js_frg: String. The Javascript framework corresponding to the Js builder
    """
    self.htmlObj._report._props.setdefault('js', {}).setdefault("builders_css", OrderedSet()).add("const %s = %s" % (name, js_frg))
    return self

  def get_classes(self):
    """
    Description:
    ------------
    Returns the list of Internal and bespoke classes to be added to the class HTML table on the component
    """
    if self.__css_virtual and not '_attrs' in self.__css_virtual:
      self.__css_virtual["_attrs"] = self.__css_virtual.get('_temp', {})
      self.__css_virtual["_attrs"].update(dict(self.css.attrs))
      self.__css_virtual['classname'] = "style_%s" % self.htmlObj.htmlCode
      meta_cls = type('Style%s' % self.htmlObj.htmlCode, (CssStyle.Style,), self.__css_virtual)
      self.css.attrs = {} # empty the css inline section
      self.classList['main'].add(meta_cls(self.htmlObj._report))
      self.htmlObj.attr['css'] = {}
    for css_cls in self.classList.values():
      for c in css_cls:
        if hasattr(c, 'get_ref'):
          self.htmlObj._report._css[c.get_ref()] = c
    return self.classList

  def get_classes_css(self):
    """
    Description:
    ------------

    :return:
    """
    css_frgs = {}
    for css_cls in self.classList.values():
      for c in css_cls:
        if hasattr(c, 'get_ref'):
          css_frgs[c.get_ref()] = str(c)
    return css_frgs


class ClassHtmlEmpty(ClassHtml):

  @property
  def css(self):
    """
    Description:
    ------------
    Property to the underlying CSS definition to be added to the style HTML tag of a component

    :rtype: Commons
    """
    if self._css_struct is None:
      self._css_struct = Empty(self.htmlObj)
    return self._css_struct
