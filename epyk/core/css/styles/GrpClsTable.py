
from epyk.core.py import primitives
from epyk.core.css.styles import GrpCls
from epyk.core.css import Classes


class DataTableThemes:

  def __init__(self, classlist):
    self.classlist = classlist

  def cell_border(self):
    """
    Description:
    -----------

    Related Pages:

      https://datatables.net/examples/styling/cell-border.html
    """
    self.classlist.add("cell-border")
    return self

  def compact(self):
    """
    Description:
    -----------
    Reduce the amount of white-space the default styling for the DataTable uses, increasing the information density on
    screen, as shown below.
    Note that this style requires DataTables 1.10.1 or newer.

    Related Pages:

      https://datatables.net/manual/styling/classes
    """
    self.classlist.add("compact")
    return self

  def display_compact(self):
    """
    Description:
    -----------

    Related Pages:

      https://datatables.net/examples/styling/compact.html
    """
    self.classlist.add("display")
    self.classlist.add("compact")
    return self

  def hover(self):
    """
    Description:
    -----------

    Related Pages:

      https://datatables.net/examples/styling/hover.html
    """
    self.classlist.add("hover")
    return self

  def order_column(self):
    """
    Description:
    -----------
    Highlight the ordering column.

    Related Pages:

      https://datatables.net/examples/styling/order-column.html
    """
    self.classlist.add("order-column")
    return self

  def nowrap(self):
    """
    Description:
    -----------
    Disable line wrapping of content in the table cells, so the text will always appear on one line.
    Note that this style requires DataTables 1.10.1 or newer.

    Related Pages:

      https://datatables.net/manual/styling/classes
    """
    self.classlist.add("nowrap")
    return self

  def row_border(self):
    """
    Description:
    -----------
    Border on the rows only.

    Related Pages:

      https://datatables.net/examples/styling/row-border.html
    """
    self.classlist.add("row-border")
    return self

  def stripe(self):
    """
    Description:
    -----------
    Row striping.

    Related Pages:

      https://datatables.net/examples/styling/stripe.html
    """
    self.classlist.add("stripe")
    return self

  def bootstrap(self):
    """
    Description:
    -----------

    Related Pages:

      https://datatables.net/examples/styling/bootstrap4.html
    """
    self.classlist.add("table")
    self.classlist.add("table-striped")
    self.classlist.add("table-bordered")
    return self


class Datatable(GrpCls.ClassHtml):

  def __init__(self, component: primitives.HtmlModel):
    super(Datatable, self).__init__(component)
    self._css_datatable, self._css_datatable_header, self._css_datatable_row_odd = None, None, None
    self._css_datatable_row_even, self._css_datatable_footer = None, None
    self.classList['main'].add(self.cls_datatable)
    self.classList['main'].add(self.cls_datatable_header)
    self.classList['main'].add(self.cls_datatable_odd)
    self.classList['main'].add(self.cls_datatable_even)
    self.classList['main'].add(self.cls_datatable_footer)

  @property
  def themes(self) -> DataTableThemes:
    """
    Description:
    -----------
    Add the predefined themes in the javascript library.

    Related Pages:

      https://datatables.net/examples/styling/index.html
    """
    return DataTableThemes(self.classList['main'])

  @property
  def cls_datatable(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_datatable is None:
      self._css_datatable = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['main'], component=self.component).datatable()
    return self._css_datatable

  @property
  def cls_datatable_header(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_datatable_header is None:
      self._css_datatable_header = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['main'], component=self.component).datatable_header()
    return self._css_datatable_header

  @property
  def cls_datatable_odd(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_datatable_row_odd is None:
      self._css_datatable_row_odd = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['main'], component=self.component).datatable_odd()
    return self._css_datatable_row_odd

  @property
  def cls_datatable_even(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_datatable_row_even is None:
      self._css_datatable_row_even = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['main'], component=self.component).datatable_even()
    return self._css_datatable_row_even

  @property
  def cls_datatable_footer(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_datatable_footer is None:
      self._css_datatable_footer = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['main'], component=self.component).datatable_footer()
    return self._css_datatable_footer


class Tabulator(GrpCls.ClassHtml):

  def __init__(self, component: primitives.HtmlModel):
    super(Tabulator, self).__init__(component)
    self._css_tabulator, self._css_tabulator_row, self._css_tabulator_header = None, None, None
    self._css_tabulator_even_row, self._css_tabulator_cell, self._css_tabulator_headers = None, None, None
    self._css_tabulator_col, self._css_tabulator_col_content, self._css_tabulator_selected = None, None, None
    self._css_tb_odd_row, self._css_tb_groups, self._css_tb_footer, self._css_tabulator_menu_item = 4 * [None]
    self._css_tb_footer_pg, self._css_tb_tree, self._css_tb_tree_exp, self._css_tabulator_menu = 4 * [None]
    self._css_tabulator_even_row_no_strip, self._css_tabulator_editing, self._css_tabulator_cell_editing = 3 * [None]
    self._css_tabulator_col_title, self._css_tb_table, self._css_header_filter_input = 3 * [None]
    self._css_sorter_asc, self._css_sorter_desc, self._css_sorter_none = 3 * [None]
    self.__strip = False
    self.classList['main'].add(self.cls_tabulator)
    self.classList['other'].add(self.cls_tabulator_row)
    self.classList['other'].add(self.cls_tabulator_header)
    self.classList['other'].add(self.cls_tabulator_cell)
    self.classList['other'].add(self.cls_tabulator_headers)
    self.classList['other'].add(self.cls_tabulator_col)
    self.classList['other'].add(self.cls_tabulator_col_title)
    self.classList['other'].add(self.cls_tabulator_col_content)
    self.classList['other'].add(self.cls_tabulator_selected)
    self.classList['other'].add(self.cls_tb_even_row)
    self.classList['other'].add(self.cls_tb_groups)
    self.classList['other'].add(self.cls_tb_footer)
    self.classList['other'].add(self.cls_tb_footer_pg)
    self.classList['other'].add(self.cls_tb_tree)
    self.classList['other'].add(self.cls_tb_tree_exp)
    self.classList['other'].add(self.cls_tabulator_menu)
    self.classList['other'].add(self.cls_tabulator_menu_item)
    self.classList['other'].add(self.cls_tabulator_editing)
    self.classList['other'].add(self.cls_tabulator_cell_editing)
    self.classList['other'].add(self.cls_sorter_asc)
    self.classList['other'].add(self.cls_sorter_desc)
    self.classList['other'].add(self.cls_sorter_none)
    self.classList['other'].add(self.cls_tb_table)
    self.classList['other'].add(self.cls_header_filter_input)

  def strip(self, attrs: dict = None, important: bool = False):
    """
    Description:
    -----------
    Configure the style of the row.

    Usage::

      table.style.strip({"background": "yellow"}, important=True)

    Attributes:
    ----------
    :param attrs:
    :param important:
    """
    self.__strip = True
    if self._css_tabulator_even_row is None:
      if attrs is not None and important:
        attrs = dict(attrs)
        for k, v in attrs.items():
          attrs[k] = "%s !IMPORTANT" % v
      self._css_tabulator_even_row = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['main'], component=self.component).tabulator_even_rows(attrs)
    self.classList['other'].add(self.cls_tabulator_even_row)
    return self._css_tabulator_even_row

  @property
  def cls_tabulator(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    """
    if self._css_tabulator is None:
      self._css_tabulator = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['main'], component=self.component).tabulator()
    return self._css_tabulator

  @property
  def cls_header_filter_input(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    """
    if self._css_header_filter_input is None:
      self._css_header_filter_input = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).tabulator_header_filter_input()
    return self._css_header_filter_input

  @property
  def cls_sorter_asc(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    """
    if self._css_sorter_asc is None:
      self._css_sorter_asc = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).tabulator_sorter_asc()
    return self._css_sorter_asc

  @property
  def cls_sorter_desc(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    """
    if self._css_sorter_desc is None:
      self._css_sorter_desc = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).tabulator_sorter_desc()
    return self._css_sorter_desc

  @property
  def cls_sorter_none(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    """
    if self._css_sorter_none is None:
      self._css_sorter_none = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).tabulator_sorter_none()
    return self._css_sorter_none

  @property
  def cls_tabulator_row(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    """
    if self._css_tabulator_row is None:
      self._css_tabulator_row = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).tabulator_rows()
    return self._css_tabulator_row

  @property
  def cls_tabulator_cell(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    """
    if self._css_tabulator_cell is None:
      self._css_tabulator_cell = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).tabulator_cell()
    return self._css_tabulator_cell

  @property
  def cls_tabulator_col(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    """
    if self._css_tabulator_col is None:
      self._css_tabulator_col = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).tabulator_col()
    return self._css_tabulator_col

  @property
  def cls_tabulator_col_title(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    """
    if self._css_tabulator_col_title is None:
      self._css_tabulator_col_title = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).tabulator_col_title()
    return self._css_tabulator_col_title

  @property
  def cls_tabulator_col_content(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    """
    if self._css_tabulator_col_content is None:
      self._css_tabulator_col_content = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).tabulator_col_content()
    return self._css_tabulator_col_content

  @property
  def cls_tabulator_menu(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    """
    if self._css_tabulator_menu is None:
      self._css_tabulator_menu = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).tabulator_menu()
    return self._css_tabulator_menu

  @property
  def cls_tabulator_menu_item(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    """
    if self._css_tabulator_menu_item is None:
      self._css_tabulator_menu_item = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).tabulator_menu_item()
    return self._css_tabulator_menu_item

  @property
  def cls_tabulator_selected(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    """
    if self._css_tabulator_selected is None:
      self._css_tabulator_selected = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).tabulator_selected()
    return self._css_tabulator_selected

  @property
  def cls_tabulator_even_row(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    """
    if self._css_tabulator_even_row is None:
      self._css_tabulator_even_row = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).tabulator_even_rows()
    return self._css_tabulator_even_row

  @property
  def cls_tabulator_even_row_no_strip(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    """
    if self._css_tabulator_even_row_no_strip is None:
      self._css_tabulator_even_row_no_strip = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).tabulator_even_rows_no_strop()
    return self._css_tabulator_even_row_no_strip

  @property
  def cls_tb_even_row(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    """
    if self._css_tb_odd_row is None:
      self._css_tb_odd_row = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).tabulator_odd_rows()
    return self._css_tb_odd_row

  @property
  def cls_tb_groups(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    """
    if self._css_tb_groups is None:
      self._css_tb_groups = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).tabulator_groups()
    return self._css_tb_groups

  @property
  def cls_tb_footer(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    """
    if self._css_tb_footer is None:
      self._css_tb_footer = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).tabulator_footer()
    return self._css_tb_footer

  @property
  def cls_tb_table(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    """
    if self._css_tb_table is None:
      self._css_tb_table = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).tabulator_table()
    return self._css_tb_table

  @property
  def cls_tb_footer_pg(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    """
    if self._css_tb_footer_pg is None:
      self._css_tb_footer_pg = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).tabulator_footer_pagination()
    return self._css_tb_footer_pg

  @property
  def cls_tb_tree(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    """
    if self._css_tb_tree is None:
      self._css_tb_tree = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).tabulator_tree_control()
    return self._css_tb_tree

  @property
  def cls_tb_tree_exp(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    """
    if self._css_tb_tree_exp is None:
      self._css_tb_tree_exp = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).tabulator_tree_control_expand()
    return self._css_tb_tree_exp

  @property
  def cls_tabulator_header(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    """
    if self._css_tabulator_header is None:
      self._css_tabulator_header = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).tabulator_header()
    return self._css_tabulator_header

  @property
  def cls_tabulator_editing(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    """
    if self._css_tabulator_editing is None:
      self._css_tabulator_editing = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).tabulator_editing()
    return self._css_tabulator_editing

  @property
  def cls_tabulator_cell_editing(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    """
    if self._css_tabulator_cell_editing is None:
      self._css_tabulator_cell_editing = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).tabulator_cell_editing()
    return self._css_tabulator_cell_editing

  @property
  def cls_tabulator_headers(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    """
    if self._css_tabulator_headers is None:
      self._css_tabulator_headers = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).tabulator_headers()
    return self._css_tabulator_headers

  def get_classes_css(self):
    """
    Description:
    -----------

    """
    if not self.__strip:
      self.classList['main'].add(self.cls_tabulator_even_row_no_strip)
    return super(Tabulator, self).get_classes_css()

  def bespoke(self, name: str = None, css_table: dict = None, css_selected: dict = None, important: bool = True,
              css_col_content: dict = None, others: dict = None):
    """
    Description:
    -----------
    Override specific CSS classes.

    Usage::

      table.style.bespoke(name="myTable", css_selected={"color": "red"},
                      css_col_content={"background": "red", "border": "red"}, important=True)

      table.style.bespoke(others={"tabulator-editing input": {"color": "purple"}})

    Attributes:
    ----------
    :param name: Optional. The table HTML tag name.
    :param css_table: Optional. The Tabulator table CSS attributes.
    :param css_selected: Optional. The Tabulator selected CSS attributes
    :param important: Optional. Set the attributes are important
    :param css_col_content: Optional. The Tabulator Column content CSS attributes
    :param others: Optional. A dictionary with other CSS attributes
    """
    if name is None:
      selector = "#%s" % self.component.htmlCode
    else:
      selector = "div[name=%s]" % name
      self.component.attr["name"] = name
    flag = " !IMPORTANT" if important else ""
    if css_table is not None:
      self.page.properties.css.add_text("%s .tabulator-table {%s}\n" % (
        selector, "; ".join(["%s: %s%s" % (k, v, flag) for k, v in css_table.items()])))
    if css_selected is not None:
      self.page.properties.css.add_text("%s .tabulator-selected {%s}\n" % (
        selector, "; ".join(["%s: %s%s" % (k, v, flag) for k, v in css_selected.items()])))
    if css_col_content is not None:
      if "background" in css_col_content:
        self.page.properties.css.add_text("%s .tabulator-col {background: %s%s}\n" % (
          selector, css_col_content["background"], flag))
      self.page.properties.css.add_text("%s .tabulator-col-content {%s}\n" % (
        selector, "; ".join(["%s: %s%s" % (k, v, flag) for k, v in css_col_content.items()])))
    if others is not None:
      for css_cls, attrs in others.items():
        self.page.properties.css.add_text("%s .%s {%s}\n" % (
          selector, css_cls, "; ".join(["%s: %s%s" % (k, v, flag) for k, v in attrs.items()])))


class Pivot(GrpCls.ClassHtml):

  def __init__(self, component: primitives.HtmlModel):
    super(Pivot, self).__init__(component)
    self._css_pt_head, self._css_pt_cell, self._css_pt_axis = 3 * [None]
    self._css_pt_box, self._css_pt_pop, self._css_pt_val, self._css_pt_label = 4 * [None]
    self._css_pt_pop_header, self._css_pt_pop_button, self._css_pt_pop_checks = 3 * [None]
    self._css_pt_pop_checks_label = None
    self.classList['main'].add(self.cls_pt_head)
    self.classList['other'].add(self.cls_pt_cell)
    self.classList['other'].add(self.cls_pt_axis)
    self.classList['other'].add(self.cls_pt_filter_box)
    self.classList['other'].add(self.cls_pt_popup)
    self.classList['other'].add(self.cls_pt_val)
    self.classList['other'].add(self.cls_pt_label)
    self.classList['other'].add(self.cls_pt_popup_header)
    self.classList['other'].add(self.cls_pt_popup_button)
    self.classList['other'].add(self.cls_pt_popup_checks)
    self.classList['other'].add(self.cls_pt_popup_checks_label)

  @property
  def cls_pt_popup_checks_label(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_pt_pop_checks_label is None:
      self._css_pt_pop_checks_label = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).pivot_filter_popup_checks_label()
    return self._css_pt_pop_checks_label

  @property
  def cls_pt_popup_checks(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_pt_pop_checks is None:
      self._css_pt_pop_checks = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).pivot_filter_popup_checks()
    return self._css_pt_pop_checks

  @property
  def cls_pt_head(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_pt_head is None:
      self._css_pt_head = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['main'], component=self.component).pivot_head()
    return self._css_pt_head

  @property
  def cls_pt_cell(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_pt_cell is None:
      self._css_pt_cell = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).pivot_cell()
    return self._css_pt_cell

  @property
  def cls_pt_axis(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_pt_axis is None:
      self._css_pt_axis = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).pivot_axis()
    return self._css_pt_axis

  @property
  def cls_pt_filter_box(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_pt_box is None:
      self._css_pt_box = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).pivot_filter_box()
    return self._css_pt_box

  @property
  def cls_pt_popup_header(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_pt_pop_header is None:
      self._css_pt_pop_header = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).pivot_filter_popup_header()
    return self._css_pt_pop_header

  @property
  def cls_pt_popup_button(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_pt_pop_button is None:
      self._css_pt_pop_button = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).pivot_filter_popup_button()
    return self._css_pt_pop_button

  @property
  def cls_pt_popup(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_pt_pop is None:
      self._css_pt_pop = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).pivot_filter_popup()
    return self._css_pt_pop

  @property
  def cls_pt_val(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_pt_val is None:
      self._css_pt_val = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).pivot_filter_val()
    return self._css_pt_val

  @property
  def cls_pt_label(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    -----------

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_pt_label is None:
      self._css_pt_label = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).pivot_filter_label()
    return self._css_pt_label


class Aggrid(GrpCls.ClassHtml):

  def __init__(self, component: primitives.HtmlModel):
    super(Aggrid, self).__init__(component)
    self.classList['main'].clear()
    self._css_head, self._css_row_even, self._css_row_odd, self._css_row = 4 * [None]
    self._css_cell_focus, self._css_cell, self._css_filter, self._css_menu, self._css_popup = 5 * [None]
    self.classList['other'].add(self.cls_head)
    self.classList['other'].add(self.cls_row_even)
    self.classList['other'].add(self.cls_row_odd)
    self.classList['other'].add(self.cls_row)
    self.classList['other'].add(self.cls_cell_focus)
    self.classList['other'].add(self.cls_cell)
    self.classList['other'].add(self.css_filter)
    self.classList['other'].add(self.css_menu)
    self.classList['other'].add(self.css_popup)

  @property
  def css_popup(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    ------------
    Property to the CSS Class definition for filter popups.

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_popup is None:
      self._css_popup = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).ag_popup()
    return self._css_popup

  @property
  def css_menu(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    ------------
    Property to the CSS Class definition for menu.

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_menu is None:
      self._css_menu = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).ag_menu()
    return self._css_menu

  @property
  def css_filter(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    ------------
    Property to the CSS Class definition for filter.

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_filter is None:
      self._css_filter = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).ag_filter()
    return self._css_filter

  @property
  def cls_head(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    ------------
    Property to the CSS Class definition for header.

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_head is None:
      self._css_head = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).ag_head()
    return self._css_head

  @property
  def cls_row_even(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    ------------
    Property to the CSS Class definition for rows.

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_row_even is None:
      self._css_row_even = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).ag_row_even()
    return self._css_row_even

  @property
  def cls_row(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    ------------
    Property to the CSS Class definition for rows.

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_row is None:
      self._css_row = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).ag_row()
    return self._css_row

  @property
  def cls_row_odd(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    ------------
    Property to the CSS Class definition for rows.

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_row_odd is None:
      self._css_row_odd = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).ag_row_odd()
    return self._css_row_odd

  @property
  def cls_cell_focus(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    ------------
    Property to the CSS Class definition for cells when focus.

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_cell_focus is None:
      self._css_cell_focus = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).ag_cell_focus()
    return self._css_cell_focus

  @property
  def cls_cell(self) -> Classes.CatalogTable.CatalogTable:
    """
    Description:
    ------------
    Property to the CSS Class definition for cells.

    :rtype: Classes.CatalogTable.CatalogTable
    """
    if self._css_cell is None:
      self._css_cell = Classes.CatalogTable.CatalogTable(
        self.component.page, self.classList['other'], component=self.component).ag_cell()
    return self._css_cell
