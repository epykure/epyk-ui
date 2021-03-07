
from epyk.core.css.styles import GrpCls
from epyk.core.css import Classes
from epyk.core.css.styles.attributes import AttrInput


class ClassInput(GrpCls.ClassHtml):

  @property
  def css(self):
    """
    Description:
    ------------
    Property to the underlying CSS definition to be added to the style HTML tag of a component.

    :rtype: AttrInput.AttrInput
    """
    if self._css_struct is None:
      self._css_struct = AttrInput.AttrInput(self.component)
    return self._css_struct

  @property
  def css_class(self):
    """
    Description:
    ------------
    The internal class used to put a custom Style to this object.
    Only 1 CSS class can be added to an HTML object.

    :rtype: Classes.CatalogInput.CatalogInput
    """
    if self._css_class is None:
      self._css_class = Classes.CatalogInput.CatalogInput(self.component.page, self.classList['main']).basic()
    return self._css_class


class ClassInputDate(ClassInput):

  def __init__(self, component):
    super(ClassInputDate, self).__init__(component)
    self._css_class_dt, self._css_class_dt_ui, self._css_time_picker_header = None, None, None
    self.classList['main'].add(self.cls_datepicker)
    self.classList['main'].add(self.cls_datepicker_ui)
    self.classList['other'].add(self.cls_datepicker_header)

  @property
  def cls_datepicker(self):
    """
    Description:
    ------------

    :rtype: Classes.CatalogInput.CatalogDate
    """
    if self._css_class_dt is None:
      self._css_class_dt = Classes.CatalogInput.CatalogDate(self.component.page, self.classList['main']).datepicker()
    return self._css_class_dt

  @property
  def cls_datepicker_ui(self):
    """
    Description:
    ------------

    :rtype: Classes.CatalogInput.CatalogDate
    """
    if self._css_class_dt_ui is None:
      self._css_class_dt_ui = Classes.CatalogInput.CatalogDate(
        self.component.page, self.classList['main']).datepicker_ui()
    return self._css_class_dt_ui

  @property
  def cls_datepicker_header(self):
    """
    Description:
    ------------

    :rtype: Classes.CatalogInput.CatalogDate
    """
    if self._css_time_picker_header is None:
      self._css_time_picker_header = Classes.CatalogInput.CatalogDate(
        self.component.page, self.classList['other']).datepicker_header()
    return self._css_time_picker_header


class ClassInputTime(ClassInput):

  def __init__(self, component):
    super(ClassInputTime, self).__init__(component)
    self._css_class_tm, self._css_class_tm_it = None, None
    self.classList['main'].add(self.cls_timepicker)
    self.classList['main'].add(self.cls_timepicker_items)

  @property
  def cls_timepicker(self):
    """
    Description:
    ------------

    :rtype: Classes.CatalogInput.CatalogDate
    """
    if self._css_class_tm is None:
      self._css_class_tm = Classes.CatalogInput.CatalogDate(self.component.page, self.classList['main']).time_picker()
    return self._css_class_tm

  @property
  def cls_timepicker_items(self):
    """
    Description:
    ------------

    :rtype: Classes.CatalogInput.CatalogDate
    """
    if self._css_class_tm_it is None:
      self._css_class_tm_it = Classes.CatalogInput.CatalogDate(
        self.component.page, self.classList['main']).time_picker_items()
    return self._css_class_tm_it


class ClassInputRange(GrpCls.ClassHtml):

  def __init__(self, component):
    super(ClassInputRange, self).__init__(component)
    self._css_class_rg, self._css_class_rg_tb = None, None
    self.classList['main'].add(self.cls_range)
    self.classList['main'].add(self.cls_range_thumb)

  @property
  def cls_range(self):
    """
    Description:
    ------------

    :rtype: Classes.CatalogInput.CatalogInput
    """
    if self._css_class_rg is None:
      self._css_class_rg = Classes.CatalogInput.CatalogInput(
        self.component.page, self.classList['main']).range()
    return self._css_class_rg

  @property
  def cls_range_thumb(self):
    """
    Description:
    ------------

    :rtype:Classes.CatalogInput.CatalogInput
    """
    if self._css_class_rg_tb is None:
      self._css_class_rg_tb = Classes.CatalogInput.CatalogInput(
        self.component.page, self.classList['main']).range_thumb()
    return self._css_class_rg_tb


class ClassInputAutocomplete(ClassInput):

  def __init__(self, component):
    super(ClassInputAutocomplete, self).__init__(component)
    self._css_autocomplete, self._css_menu_item, self._css_class, self._css_item_active = 4 * [None]
    self.classList['main'].add(self.cls_input)
    self.classList['other'].add(self.cls_autocomplete)
    self.classList['other'].add(self.cls_menu_item)
    self.classList['other'].add(self.cls_item_active)

  @property
  def cls_autocomplete(self):
    """
    Description:
    ------------

    :rtype: Classes.CatalogInput.CatalogDate
    """
    if self._css_autocomplete is None:
      self._css_autocomplete = Classes.CatalogInput.CatalogDate(
        self.component.page, self.classList['other']).autocomplete()
    return self._css_autocomplete

  @property
  def cls_item_active(self):
    """
    Description:
    ------------

    :rtype: Classes.CatalogInput.CatalogDate
    """
    if self._css_item_active is None:
      self._css_item_active = Classes.CatalogInput.CatalogDate(
        self.component.page, self.classList['other']).autocomplete_item_active()
    return self._css_item_active

  @property
  def cls_menu_item(self):
    """
    Description:
    ------------

    :rtype: Classes.CatalogInput.CatalogDate
    """
    if self._css_menu_item is None:
      self._css_menu_item = Classes.CatalogInput.CatalogDate(
        self.component.page, self.classList['other']).autocomplete_menu()
    return self._css_menu_item

  @property
  def cls_input(self):
    """
    Description:
    ------------
    The internal class used to put a custom Style to this object.
    Only 1 CSS class can be added to an HTML object.

    :rtype: Classes.CatalogInput.CatalogInput
    """
    if self._css_class is None:
      self._css_class = Classes.CatalogInput.CatalogInput(self.component.page, self.classList['main']).basic()
    return self._css_class
