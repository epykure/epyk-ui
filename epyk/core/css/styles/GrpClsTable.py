
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

  def compact(self):
    """
    Reduce the amount of white-space the default styling for the DataTable uses, increasing the information density on screen, as shown below.
    Note that this style requires DataTables 1.10.1 or newer.

    https://datatables.net/manual/styling/classes
    """
    self.classlist.add("compact")
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
    Highlight the ordering column

    https://datatables.net/examples/styling/order-column.html
    """
    self.classlist.add("order-column")
    return self

  def nowrap(self):
    """
    Disable line wrapping of content in the table cells, so the text will always appear on one line.
    Note that this style requires DataTables 1.10.1 or newer.

    https://datatables.net/manual/styling/classes
    """
    self.classlist.add("nowrap")
    return self

  def row_border(self):
    """
    Border on the rows only

    https://datatables.net/examples/styling/row-border.html
    """
    self.classlist.add("row-border")
    return self

  def stripe(self):
    """
    Row striping.

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


class Tabulator(GrpCls.ClassHtml):

  def __init__(self, htmlObj):
    super(Tabulator, self).__init__(htmlObj)
    self._css_tabulator, self._css_tabulator_row, self._css_tabulator_header = None, None, None
    self._css_tabulator_even_row, self._css_tabulator_cell, self._css_tabulator_headers = None, None, None
    self._css_tabulator_col, self._css_tabulator_col_content, self._css_tabulator_selected = None, None, None
    self._css_tb_odd_row, self._css_tb_groups, self._css_tb_footer = None, None, None
    self._css_tb_footer_pg, self._css_tb_tree, self._css_tb_tree_exp = None, None, None
    self.classList['main'].add(self.cls_tabulator)
    self.classList['other'].add(self.cls_tabulator_row)
    self.classList['other'].add(self.cls_tabulator_header)
    self.classList['other'].add(self.cls_tabulator_even_row)
    self.classList['other'].add(self.cls_tabulator_cell)
    self.classList['other'].add(self.cls_tabulator_headers)
    self.classList['other'].add(self.cls_tabulator_col)
    self.classList['other'].add(self._css_tabulator_col_content)
    self.classList['other'].add(self.cls_tabulator_selected)
    self.classList['other'].add(self.cls_tb_even_row)
    self.classList['other'].add(self.cls_tb_groups)
    self.classList['other'].add(self.cls_tb_footer)
    self.classList['other'].add(self.cls_tb_footer_pg)
    self.classList['other'].add(self.cls_tb_tree)
    self.classList['other'].add(self.cls_tb_tree_exp)

  @property
  def cls_tabulator(self):
    """

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_tabulator is None:
      self._css_tabulator = Classes.CatalogTable.CatalogTable(self.htmlObj._report,
                                                                  self.classList['main']).tabulator()
    return self._css_tabulator

  @property
  def cls_tabulator_row(self):
    """

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_tabulator_row is None:
      self._css_tabulator_row = Classes.CatalogTable.CatalogTable(self.htmlObj._report, self.classList['other']).tabulator_rows()
    return self._css_tabulator_row

  @property
  def cls_tabulator_cell(self):
    """

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_tabulator_cell is None:
      self._css_tabulator_cell = Classes.CatalogTable.CatalogTable(self.htmlObj._report, self.classList['other']).tabulator_cell()
    return self._css_tabulator_cell

  @property
  def cls_tabulator_col(self):
    """

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_tabulator_col is None:
      self._css_tabulator_col = Classes.CatalogTable.CatalogTable(self.htmlObj._report, self.classList['other']).tabulator_col()
    return self._css_tabulator_col

  @property
  def cls_tabulator_col_content(self):
    """

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_tabulator_col_content is None:
      self._css_tabulator_col_content = Classes.CatalogTable.CatalogTable(self.htmlObj._report, self.classList['other']).tabulator_col_content()
    return self._css_tabulator_col_content

  @property
  def cls_tabulator_selected(self):
    """

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_tabulator_selected is None:
      self._css_tabulator_selected = Classes.CatalogTable.CatalogTable(self.htmlObj._report, self.classList[
        'other']).tabulator_selected()
    return self._css_tabulator_selected

  @property
  def cls_tabulator_even_row(self):
    """

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_tabulator_even_row is None:
      self._css_tabulator_even_row = Classes.CatalogTable.CatalogTable(self.htmlObj._report, self.classList['other']).tabulator_even_rows()
    return self._css_tabulator_even_row

  @property
  def cls_tb_even_row(self):
    """

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_tb_odd_row is None:
      self._css_tb_odd_row = Classes.CatalogTable.CatalogTable(self.htmlObj._report, self.classList['other']).tabulator_odd_rows()
    return self._css_tb_odd_row

  @property
  def cls_tb_groups(self):
    """

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_tb_groups is None:
      self._css_tb_groups = Classes.CatalogTable.CatalogTable(self.htmlObj._report,
                                                               self.classList['other']).tabulator_groups()
    return self._css_tb_groups

  @property
  def cls_tb_footer(self):
    """

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_tb_footer is None:
      self._css_tb_footer = Classes.CatalogTable.CatalogTable(self.htmlObj._report, self.classList['other']).tabulator_footer()
    return self._css_tb_footer

  @property
  def cls_tb_footer_pg(self):
    """

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_tb_footer_pg is None:
      self._css_tb_footer_pg = Classes.CatalogTable.CatalogTable(self.htmlObj._report, self.classList['other']).tabulator_footer_pagination()
    return self._css_tb_footer_pg

  @property
  def cls_tb_tree(self):
    """

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_tb_tree is None:
      self._css_tb_tree = Classes.CatalogTable.CatalogTable(self.htmlObj._report, self.classList['other']).tabulator_tree_control()
    return self._css_tb_tree

  @property
  def cls_tb_tree_exp(self):
    """

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_tb_tree_exp is None:
      self._css_tb_tree_exp = Classes.CatalogTable.CatalogTable(self.htmlObj._report,
                                                            self.classList['other']).tabulator_tree_control_expand()
    return self._css_tb_tree_exp

  @property
  def cls_tabulator_header(self):
    """

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_tabulator_header is None:
      self._css_tabulator_header = Classes.CatalogTable.CatalogTable(self.htmlObj._report, self.classList['other']).tabulator_header()
    return self._css_tabulator_header

  @property
  def cls_tabulator_headers(self):
    """

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_tabulator_headers is None:
      self._css_tabulator_headers = Classes.CatalogTable.CatalogTable(self.htmlObj._report, self.classList['other']).tabulator_headers()
    return self._css_tabulator_headers


class Pivot(GrpCls.ClassHtml):

  def __init__(self, htmlObj):
    super(Pivot, self).__init__(htmlObj)
    self._css_pt_head, self._css_pt_cell, self._css_pt_axis = 3 * [None]
    self._css_pt_box, self._css_pt_pop, self._css_pt_val, self._css_pt_label = 4 * [None]
    self.classList['main'].add(self.cls_pt_head)
    self.classList['other'].add(self.cls_pt_cell)
    self.classList['other'].add(self.cls_pt_axis)
    self.classList['other'].add(self.cls_pt_filter_box)
    self.classList['other'].add(self.cls_pt_popup)
    self.classList['other'].add(self.cls_pt_val)
    self.classList['other'].add(self.cls_pt_label)

  @property
  def cls_pt_head(self):
    """

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_pt_head is None:
      self._css_pt_head = Classes.CatalogTable.CatalogTable(self.htmlObj._report, self.classList['main']).pivot_head()
    return self._css_pt_head

  @property
  def cls_pt_cell(self):
    """

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_pt_cell is None:
      self._css_pt_cell = Classes.CatalogTable.CatalogTable(self.htmlObj._report, self.classList['other']).pivot_cell()
    return self._css_pt_cell

  @property
  def cls_pt_axis(self):
    """

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_pt_axis is None:
      self._css_pt_axis = Classes.CatalogTable.CatalogTable(self.htmlObj._report, self.classList['other']).pivot_axis()
    return self._css_pt_axis

  @property
  def cls_pt_filter_box(self):
    """

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_pt_box is None:
      self._css_pt_box = Classes.CatalogTable.CatalogTable(self.htmlObj._report, self.classList['other']).pivot_filter_box()
    return self._css_pt_box

  @property
  def cls_pt_popup(self):
    """

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_pt_pop is None:
      self._css_pt_pop = Classes.CatalogTable.CatalogTable(self.htmlObj._report, self.classList['other']).pivot_filter_popup()
    return self._css_pt_pop

  @property
  def cls_pt_val(self):
    """

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_pt_val is None:
      self._css_pt_val = Classes.CatalogTable.CatalogTable(self.htmlObj._report, self.classList['other']).pivot_filter_val()
    return self._css_pt_val

  @property
  def cls_pt_label(self):
    """

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_pt_label is None:
      self._css_pt_label = Classes.CatalogTable.CatalogTable(self.htmlObj._report, self.classList['other']).pivot_filter_label()
    return self._css_pt_label


class Aggrid(GrpCls.ClassHtml):

  def __init__(self, htmlObj):
    super(Aggrid, self).__init__(htmlObj)
    self._css_head, self._css_row_even, self._css_row_odd = 3 * [None]
    self._css_cell_focus, self._css_cell = 2 * [None]
    self.classList['other'].add(self.cls_head)
    self.classList['other'].add(self.cls_row_even)
    self.classList['other'].add(self.cls_row_odd)
    self.classList['other'].add(self.cls_cell_focus)
    self.classList['other'].add(self.cls_cell)

  @property
  def cls_head(self):
    """

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_head is None:
      self._css_head = Classes.CatalogTable.CatalogTable(self.htmlObj._report, self.classList['other']).ag_head()
    return self._css_head

  @property
  def cls_row_even(self):
    """

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_row_even is None:
      self._css_row_even = Classes.CatalogTable.CatalogTable(self.htmlObj._report, self.classList['other']).ag_row_even()
    return self._css_row_even

  @property
  def cls_row_odd(self):
    """

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_row_odd is None:
      self._css_row_odd = Classes.CatalogTable.CatalogTable(self.htmlObj._report, self.classList['other']).ag_row_odd()
    return self._css_row_odd

  @property
  def cls_cell_focus(self):
    """

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_cell_focus is None:
      self._css_cell_focus = Classes.CatalogTable.CatalogTable(self.htmlObj._report, self.classList['other']).ag_cell_focus()
    return self._css_cell_focus

  @property
  def cls_cell(self):
    """

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_cell is None:
      self._css_cell = Classes.CatalogTable.CatalogTable(self.htmlObj._report, self.classList['other']).ag_cell()
    return self._css_cell
