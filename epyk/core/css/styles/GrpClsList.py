
from epyk.core.py import primitives
from epyk.core.css.styles import GrpCls
from epyk.core.css import Classes
from epyk.core.css.styles.classes import CssStylesList
from epyk.core.css.styles.attributes import Attrs


class AttrSelect(Attrs):

  def __init__(self, component: primitives.HtmlModel):
    super(AttrSelect, self).__init__(component)
    self.font_size = 'inherit'
    self.font_family = 'inherit'
    self.box_sizing = 'border-box'

  @property
  def width(self):
    """
    Description:
    ------------
    The width property sets the width of an element.

    The width of an element does not include padding, borders, or margins!

    Related Pages:

      https://www.w3schools.com/cssref/pr_dim_width.asp
    """
    return self.component.attr.get("data-width")

  @width.setter
  def width(self, val):
    val = val if val is not None else 'None'
    if isinstance(val, int):
      val = "%spx" % val
    self.component.attr["data-width"] = val
    self.css({"width": val})

  @property
  def background(self):
    """
    Description:
    ------------

    """
    return self.component.attr.get("data-background")

  @background.setter
  def background(self, val):
    self.component.attr["data-background"] = val
    self.css({"background": val})

  @property
  def color(self):
    """
    Description:
    ------------

    """
    return self.component.attr.get("data-color")

  @color.setter
  def color(self, val):
    self.component.attr["data-color"] = val
    self.css({"color": val})

  def hide(self):
    """
    Description:
    ------------
    Hide the select Picker object.
    """
    self.component.page.body.onReady([self.component.dom.hide()])


class ClassSelect(GrpCls.ClassHtml):

  def __init__(self, component: primitives.HtmlModel):
    super(ClassSelect, self).__init__(component)
    self._css_class_dt, self._css_class_dt_ui, self._css_select = None, None, None
    self._css_select_input, self._css_item_option, self._css_item_options, self._css_item_selected = 4 * [None]
    self._css_menu_li, self._css_select_search, self._css_select_menu_hover = None, None, None
    self.classList['main'].add(self.cls_select)
    self.classList['main'].add(self.cls_select_button)
    self.classList['main'].add(self.cls_select_outline)
    self.classList['other'].add(self.cls_select_input)
    self.classList['main'].add(self.cls_item_option)
    self.classList['main'].add(self.cls_item_options)
    self.classList['other'].add(self.cls_item_selected)

  @property
  def css(self) -> AttrSelect:
    """
    Description:
    ------------
    Property to the underlying CSS definition to be added to the style HTML tag of a component.

    Usage::

      self.css.border = "1px solid black"

    :rtype: AttrSelect
    """
    if self._css_struct is None:
      self._css_struct = AttrSelect(self.component)
    return self._css_struct

  @property
  def cls_item_selected(self) -> Classes.CatalogSelect.CatalogSelect:
    """
    Description:
    ------------

    :rtype: Classes.CatalogSelect.CatalogSelect
    """
    if self._css_item_selected is None:
      self._css_item_selected = Classes.CatalogSelect.CatalogSelect(
        self.component.page, self.classList['other'], component=self.component).selected()
    return self._css_item_selected

  @property
  def cls_select(self) -> Classes.CatalogSelect.CatalogSelect:
    """
    Description:
    ------------

    :rtype: Classes.CatalogSelect.CatalogSelect
    """
    if self._css_select is None:
      self._css_select = Classes.CatalogSelect.CatalogSelect(
        self.component.page, self.classList['main'], component=self.component).base()
    return self._css_select

  @property
  def cls_select_button(self) -> Classes.CatalogSelect.CatalogSelect:
    """
    Description:
    ------------

    :rtype: Classes.CatalogSelect.CatalogSelect
    """
    if self._css_class_dt is None:
      self._css_class_dt = Classes.CatalogSelect.CatalogSelect(
        self.component.page, self.classList['main'], component=self.component).button()
    return self._css_class_dt

  @property
  def cls_select_outline(self) -> Classes.CatalogSelect.CatalogSelect:
    """
    Description:
    ------------

    :rtype: Classes.CatalogSelect.CatalogSelect
    """
    if self._css_class_dt_ui is None:
      self._css_class_dt_ui = Classes.CatalogSelect.CatalogSelect(
        self.component.page, self.classList['main'], component=self.component).outline()
    return self._css_class_dt_ui

  @property
  def cls_item_options(self) -> Classes.CatalogSelect.CatalogSelect:
    """
    Description:
    ------------

    :rtype: Classes.CatalogSelect.CatalogSelect
    """
    if self._css_item_options is None:
      self._css_item_options = Classes.CatalogSelect.CatalogSelect(
        self.component.page, self.classList['other'], component=self.component).option()
    return self._css_item_options

  @property
  def cls_item_option(self) -> Classes.CatalogSelect.CatalogSelect:
    """
    Description:
    ------------

    :rtype: Classes.CatalogSelect.CatalogSelect
    """
    if self._css_item_option is None:
      self._css_item_option = Classes.CatalogSelect.CatalogSelect(
        self.component.page, self.classList['other'], component=self.component).item()
    return self._css_item_option

  @property
  def cls_select_input(self) -> Classes.CatalogSelect.CatalogSelect:
    """
    Description:
    ------------

    :rtype: Classes.CatalogSelect.CatalogSelect
    """
    if self._css_select_input is None:
      self._css_select_input = Classes.CatalogSelect.CatalogSelect(
        self.component.page, self.classList['other'], component=self.component).search_box_input()
    return self._css_select_input


class ClassDropDown(GrpCls.ClassHtml):

  def __init__(self, component: primitives.HtmlModel):
    super(ClassDropDown, self).__init__(component)
    self._css_base, self._css_menu, self._css_menu_after, self._css_menu_link = 4 * [None]
    self._css_menu_hover, self._css_menu_pull_left, self._css_menu_li, self._css_caret = 4 * [None]
    self.classList['other'].add(self.cls_base)
    self.classList['other'].add(self.cls_menu)
    self.classList['other'].add(self.cls_menu_li)
    self.classList['other'].add(self.cls_menu_after)
    self.classList['other'].add(self.cls_menu_hover)
    self.classList['other'].add(self.cls_menu_pull_left)
    self.classList['other'].add(self.cls_caret)

  @property
  def cls_base(self) -> Classes.CatalogTree.CatalogDropDown:
    """
    Description:
    ------------

    :rtype: Classes.CatalogTree.CatalogDropDown
    """
    if self._css_base is None:
      self._css_base = Classes.CatalogTree.CatalogDropDown(
        self.component.page, self.classList['other'], component=self.component).base()
    return self._css_base

  @property
  def cls_menu(self) -> Classes.CatalogTree.CatalogDropDown:
    """
    Description:
    ------------

    :rtype: Classes.CatalogTree.CatalogDropDown
    """
    if self._css_menu is None:
      self._css_menu = Classes.CatalogTree.CatalogDropDown(
        self.component.page, self.classList['other'], component=self.component).menu()
    return self._css_menu

  @property
  def cls_menu_li(self) -> Classes.CatalogTree.CatalogDropDown:
    """
    Description:
    ------------

    :rtype: Classes.CatalogTree.CatalogDropDown
    """
    if self._css_menu_li is None:
      self._css_menu_li = Classes.CatalogTree.CatalogDropDown(
        self.component.page, self.classList['other'], component=self.component).menu_li()
    return self._css_menu_li

  @property
  def cls_menu_after(self) -> Classes.CatalogTree.CatalogDropDown:
    """
    Description:
    ------------

    :rtype: Classes.CatalogTree.CatalogDropDown
    """
    if self._css_menu_after is None:
      self._css_menu_after = Classes.CatalogTree.CatalogDropDown(
        self.component.page, self.classList['other'], component=self.component).menu_after()
    return self._css_menu_after

  @property
  def cls_menu_hover(self) -> Classes.CatalogTree.CatalogDropDown:
    """
    Description:
    ------------

    :rtype: Classes.CatalogTree.CatalogDropDown
    """
    if self._css_menu_hover is None:
      self._css_menu_hover = Classes.CatalogTree.CatalogDropDown(
        self.component.page, self.classList['other'], component=self.component).menu_hover()
    return self._css_menu_hover

  @property
  def cls_menu_pull_left(self) -> Classes.CatalogTree.CatalogDropDown:
    """
    Description:
    ------------

    :rtype: Classes.CatalogTree.CatalogDropDown
    """
    if self._css_menu_pull_left is None:
      self._css_menu_pull_left = Classes.CatalogTree.CatalogDropDown(
        self.component.page, self.classList['other'], component=self.component).menu_pull_left()
    return self._css_menu_pull_left

  @property
  def cls_caret(self) -> Classes.CatalogTree.CatalogDropDown:
    """
    Description:
    ------------

    :rtype: Classes.CatalogTree.CatalogDropDown
    """
    if self._css_caret is None:
      self._css_caret = Classes.CatalogTree.CatalogDropDown(
        self.component.page, self.classList['other'], component=self.component).menu_caret()
    return self._css_caret


class DefinedStyleItems:

  def __init__(self, page: primitives.HtmlModel, component: primitives.HtmlModel = None):
    self.page, self.component = page, component

  def selected_text_background_color(self, background=None, color=None):
    """
    Description:
    ------------
    Set the color of the text component.

    Attributes:
    ----------
    :param background: String. Optional. The background color.
    :param color: String. Optional. The hexadecimal color code.
    """
    return {"background": "%s !IMPORTANT" % (background or self.page.theme.colors[0]),
            "color": "%s !IMPORTANT" % (color or self.page.theme.greys[-1])}


class ClassItems(GrpCls.ClassHtml):

  @property
  def defined(self):
    """
    Description:
    ------------
    Shortcut property to pre defined CSS configurations for list of items.
    """
    return DefinedStyleItems(self.component.page, component=self.component)

  def hover_border(self):
    """
    Description:
    ------------

    :return: self to allow the chaining.
    """
    self.classList['main'].add(CssStylesList.CssListItemsBorder(self.component.page, component=self.component))
    return self

  def hover_background(self) -> CssStylesList.CssListItemsBackground:
    """
    Description:
    ------------

    :return: self to allow the chaining.
    """
    self.classList['main'].add(CssStylesList.CssListItemsBackground(self.component.page, component=self.component))
    return self
