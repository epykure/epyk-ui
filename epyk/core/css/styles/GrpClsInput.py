
from epyk.core.py import primitives
from epyk.core.css.styles import GrpCls
from epyk.core.css import Classes
from epyk.core.css.styles.attributes import AttrInput


class ClassInput(GrpCls.ClassHtml):

  @property
  def css(self) -> AttrInput.AttrInput:
    """
    Property to the underlying CSS definition to be added to the style HTML tag of a component.

    Usage::

      self.css.border = "1px solid black"

    :rtype: AttrInput.AttrInput
    """
    if self._css_struct is None:
      self._css_struct = AttrInput.AttrInput(self.component)
    return self._css_struct

  @property
  def css_class(self) -> Classes.CatalogInput.CatalogInput:
    """
    The internal class used to put a custom Style to this object.
    Only 1 CSS class can be added to an HTML object.

    :rtype: Classes.CatalogInput.CatalogInput
    """
    if self._css_class is None:
      self._css_class = Classes.CatalogInput.CatalogInput(
        self.component.page, self.classList['main'], component=self.component).basic()
    return self._css_class


class ClassInputDate(ClassInput):

  def __init__(self, component: primitives.HtmlModel):
    super(ClassInputDate, self).__init__(component)
    self._css_class_dt, self._css_class_dt_ui, self._css_time_picker_header = None, None, None
    self.classList['main'].add(self.cls_datepicker)
    self.classList['main'].add(self.cls_datepicker_ui)
    self.classList['other'].add(self.cls_datepicker_header)

  @property
  def cls_datepicker(self) -> Classes.CatalogInput.CatalogDate:
    """
    Add the datepicker class.
    Class override on the existing one in the package.

    :rtype: Classes.CatalogInput.CatalogDate
    """
    if self._css_class_dt is None:
      self._css_class_dt = Classes.CatalogInput.CatalogDate(
        self.component.page, self.classList['main'], component=self.component).datepicker()
    return self._css_class_dt

  @property
  def cls_datepicker_ui(self) -> Classes.CatalogInput.CatalogDate:
    """
    Add the predefined datepicker UI class.
    Class override on the existing one in the package.

    :rtype: Classes.CatalogInput.CatalogDate
    """
    if self._css_class_dt_ui is None:
      self._css_class_dt_ui = Classes.CatalogInput.CatalogDate(
        self.component.page, self.classList['main'], component=self.component).datepicker_ui()
    return self._css_class_dt_ui

  @property
  def cls_datepicker_header(self) -> Classes.CatalogInput.CatalogDate:
    """
    Add the override on the date picker header class.
    Class override on the existing one in the package.

    :rtype: Classes.CatalogInput.CatalogDate
    """
    if self._css_time_picker_header is None:
      self._css_time_picker_header = Classes.CatalogInput.CatalogDate(
        self.component.page, self.classList['other'], component=self.component).datepicker_header()
    return self._css_time_picker_header


class ClassInputTime(ClassInput):

  def __init__(self, component: primitives.HtmlModel):
    super(ClassInputTime, self).__init__(component)
    self._css_class_tm, self._css_class_tm_it = None, None
    self.classList['main'].add(self.cls_timepicker)
    self.classList['main'].add(self.cls_timepicker_items)

  @property
  def cls_timepicker(self) -> Classes.CatalogInput.CatalogDate:
    """
    Add the predefined timepicker CSS class.
    Class override on the existing one in the package.

    :rtype: Classes.CatalogInput.CatalogDate
    """
    if self._css_class_tm is None:
      self._css_class_tm = Classes.CatalogInput.CatalogDate(
        self.component.page, self.classList['main'], component=self.component).time_picker()
    return self._css_class_tm

  @property
  def cls_timepicker_items(self) -> Classes.CatalogInput.CatalogDate:
    """
    Add the predefined timepicker items CSS class.
    Class override on the existing one in the package.

    :rtype: Classes.CatalogInput.CatalogDate
    """
    if self._css_class_tm_it is None:
      self._css_class_tm_it = Classes.CatalogInput.CatalogDate(
        self.component.page, self.classList['main'], component=self.component).time_picker_items()
    return self._css_class_tm_it


class ClassInputRange(GrpCls.ClassHtml):

  def __init__(self, component: primitives.HtmlModel):
    super(ClassInputRange, self).__init__(component)
    self._css_class_rg, self._css_class_rg_tb = None, None
    self.classList['main'].add(self.cls_range)
    self.classList['main'].add(self.cls_range_thumb)

  @property
  def cls_range(self) -> Classes.CatalogInput.CatalogInput:
    """
    Class override on the existing one in the package.

    :rtype: Classes.CatalogInput.CatalogInput
    """
    if self._css_class_rg is None:
      self._css_class_rg = Classes.CatalogInput.CatalogInput(
        self.component.page, self.classList['main'], component=self.component).range()
    return self._css_class_rg

  @property
  def cls_range_thumb(self) -> Classes.CatalogInput.CatalogInput:
    """
    Add the predefined timepicker CSS class for the slider thumb.
    Class override on the existing one in the package.

    :rtype:Classes.CatalogInput.CatalogInput
    """
    if self._css_class_rg_tb is None:
      self._css_class_rg_tb = Classes.CatalogInput.CatalogInput(
        self.component.page, self.classList['main'], component=self.component).range_thumb()
    return self._css_class_rg_tb


class ClassInputAutocomplete(ClassInput):

  def __init__(self, component: primitives.HtmlModel):
    super(ClassInputAutocomplete, self).__init__(component)
    self._css_autocomplete, self._css_menu_item, self._css_class, self._css_item_active = 4 * [None]
    self.classList['other'].add(self.cls_autocomplete)
    self.classList['other'].add(self.cls_menu_item)
    self.classList['other'].add(self.cls_item_active)

  @property
  def cls_autocomplete(self) -> Classes.CatalogInput.CatalogDate:
    """
    Add the predefined autocomplete CSS style.
    Class override on the existing one in the package.

    :rtype: Classes.CatalogInput.CatalogDate
    """
    if self._css_autocomplete is None:
      self._css_autocomplete = Classes.CatalogInput.CatalogDate(
        self.component.page, self.classList['other'], component=self.component).autocomplete()
    return self._css_autocomplete

  @property
  def cls_item_active(self) -> Classes.CatalogInput.CatalogDate:
    """
    Change the CSS predefined style for the active item.
    Class override on the existing one in the package.

    :rtype: Classes.CatalogInput.CatalogDate
    """
    if self._css_item_active is None:
      self._css_item_active = Classes.CatalogInput.CatalogDate(
        self.component.page, self.classList['other'], component=self.component).autocomplete_item_active()
    return self._css_item_active

  @property
  def cls_menu_item(self) -> Classes.CatalogInput.CatalogDate:
    """
    Class override on the existing one in the package.

    :rtype: Classes.CatalogInput.CatalogDate
    """
    if self._css_menu_item is None:
      self._css_menu_item = Classes.CatalogInput.CatalogDate(
        self.component.page, self.classList['other'], component=self.component).autocomplete_menu()
    return self._css_menu_item
