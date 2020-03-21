
from epyk.core.css.styles import GrpCls
from epyk.core.css import Classes


class DataTableThemes(object):

  def __init__(self, classlist):
    self.classlist = classlist

  def cell_border(self):
    """

    https://datatables.net/examples/styling/cell-border.html

    cell-border

    :return:
    """
    self.classlist.add("cell-border")
    return self

  def display_compact(self):
    """

    https://datatables.net/examples/styling/compact.html
    :return:
    """
    self.classlist.add("display")
    self.classlist.add("compact")
    return self

  def hover(self):
    """

    https://datatables.net/examples/styling/hover.html

    hover

    :return:
    """
    self.classlist.add("hover")
    return self

  def order_column(self):
    """

    https://datatables.net/examples/styling/order-column.html
    """
    self.classlist.add("order-column")
    return self

  def row_border(self):
    """

    https://datatables.net/examples/styling/row-border.html
    """
    self.classlist.add("row-border")
    return self

  def stripe(self):
    """

    https://datatables.net/examples/styling/stripe.html
    """
    self.classlist.add("stripe")
    return self

  def bootstrap(self):
    """

    https://datatables.net/examples/styling/bootstrap4.html
    """
    self.classlist.add("table")
    self.classlist.add("table-striped")
    self.classlist.add("table-bordered")
    return self


class Datatable(GrpCls.ClassHtml):

  def __init__(self, htmlObj):
    super(Datatable, self).__init__(htmlObj)
    self._css_datatable, self._css_datatable_header, self._css_datatable_row_odd = None, None, None
    self._css_datatable_row_even, self._css_datatable_footer = None, None
    self.classList['main'].add(self.cls_datatable)
    self.classList['main'].add(self.cls_datatable_header)
    self.classList['main'].add(self.cls_datatable_odd)
    self.classList['main'].add(self.cls_datatable_even)
    self.classList['main'].add(self.cls_datatable_footer)

  @property
  def themes(self):
    """
    Add the predefined themes in the javascript library

    https://datatables.net/examples/styling/index.html
    """
    return DataTableThemes(self.classList['main'])

  @property
  def cls_datatable(self):
    """

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_datatable is None:
      self._css_datatable = Classes.CatalogTable.CatalogTable(self.htmlObj._report, self.classList['main']).datatable()
    return self._css_datatable

  @property
  def cls_datatable_header(self):
    """

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_datatable_header is None:
      self._css_datatable_header = Classes.CatalogTable.CatalogTable(self.htmlObj._report, self.classList['main']).datatable_header()
    return self._css_datatable_header

  @property
  def cls_datatable_odd(self):
    """

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_datatable_row_odd is None:
      self._css_datatable_row_odd = Classes.CatalogTable.CatalogTable(self.htmlObj._report, self.classList['main']).datatable_odd()
    return self._css_datatable_row_odd

  @property
  def cls_datatable_even(self):
    """

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_datatable_row_even is None:
      self._css_datatable_row_even = Classes.CatalogTable.CatalogTable(self.htmlObj._report, self.classList['main']).datatable_even()
    return self._css_datatable_row_even

  @property
  def cls_datatable_footer(self):
    """

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_datatable_footer is None:
      self._css_datatable_footer = Classes.CatalogTable.CatalogTable(self.htmlObj._report, self.classList['main']).datatable_footer()
    return self._css_datatable_footer
