#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union
from epyk.core.html import Html
from epyk.interfaces import Arguments
from epyk.core.html import tables as html_tables

from epyk.interfaces.tables import CompTabulator
from epyk.interfaces.tables import CompDatatable
from epyk.interfaces.tables import CompTablesPlotly
from epyk.interfaces.tables import CompTableD3
from epyk.interfaces.tables import CompAgGrid
from epyk.interfaces.tables import CompPivot
from epyk.interfaces.tables import CompTableGoogle


class Tables:

  def __init__(self, ui):
    self.page = ui.page
    # Default table configuration per available framework
    self.datatable = self.datatables.table
    self.tabulator = self.tabulators.table
    self.plotly = self.plotlys.table
    self.aggrid = self.aggrids.table
    self.pivot = self.pivots.pivot

  @property
  def aggrids(self) -> CompAgGrid.AgGrid:
    """
    Description:
    -----------
    ag-Grid is the industry standard for JavaScript Enterprise Applications.
    Developers using ag-Grid are building applications that would not be possible if ag-Grid did not exist.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://www.ag-grid.com/javascript-grid/
    """
    return CompAgGrid.AgGrid(self)

  @property
  def tabulators(self) -> CompTabulator.Tabulators:
    """
    Description:
    -----------
    Interface to the different Tabulator configurations.

    :tags:
    :categories:

    Usage::

    Related Pages:

      http://tabulator.info/
    """
    return CompTabulator.Tabulators(self)

  @property
  def google(self) -> CompTableGoogle.Google:
    """
    Description:
    -----------
    Interface to the Google Table interface.

    In order to use it, the Google products need to be specially enabled.
    """
    if not getattr(self.page, '_with_google_imports', False):
      raise ValueError("Google produce must be added using for example page.imports.google_products(['charts'])")

    return CompTableGoogle.Google(self)

  @property
  def pivots(self) -> CompPivot.Pivottable:
    """
    Description:
    -----------
    Interface to the different Pivot Table configurations.

    :tags:
    :categories:

    Related Pages:

      https://pivottable.js.org/examples/
    """
    return CompPivot.Pivottable(self)

  @property
  def d3(self) -> CompTableD3.D3:
    """
    Description:
    -----------
    Interface to the different Tabulator configurations.

    :tags:
    :categories:

    Related Pages:

      https://github.com/d3/d3/wiki/Gallery

    :rtype: CompTableD3.D3
    """
    return CompTableD3.D3(self)

  @property
  def plotlys(self) -> CompTablesPlotly.Plotly:
    """
    Description:
    -----------
    Interface to the different Tabulator configurations.

    :tags:
    :categories:

    Related Pages:

      http://tabulator.info/

    :rtype: CompTabulator.Tabulators
    """
    return CompTablesPlotly.Plotly(self)

  @property
  def datatables(self) -> CompDatatable.Datatables:
    """
    Description:
    -----------
    Interface to the different Datatable configurations.

    :tags:
    :categories:

    Related Pages:

      https://datatables.net/

    :rtype: CompDatatable.Datatables
    """
    return CompDatatable.Datatables(self)

  def config(self, html_code: str, visible: bool = False,
             profile: Union[bool, dict] = None) -> html_tables.HtmlTableConfig.ConfigTable:
    """
    Description:
    -----------

    :tags:
    :categories:

    Usage::

    Attributes:
    ----------
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param visible: Boolean. Optional. A flag to specific if the table is visible or just used as a cache.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    return html_tables.HtmlTableConfig.ConfigTable(self.page, html_code, visible, profile)

  def basic(self, records, cols=None, rows=None, width=(100, '%'), height=(None, 'px'),
            html_code: str = None, options: dict = None, profile: Union[dict, bool] = None):
    """
    Description:
    -----------

    :tags:
    :categories:

    Usage::

      simple_table = page.ui.tables.basic(df.to_dict("records"), cols=["COL1"], rows=["COL2"])
      simple_table.add({"COL1": "Value"})

    Attributes:
    ----------
    :param records: List. Optional. The list of dictionaries with the input data.
    :param cols: List. Optional. The list of key from the record to be used as columns in the table.
    :param rows: List. Optional. The list of key from the record to be used as rows in the table.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if len(records) > 0 and not cols and not rows:
      cols = list(records[0].keys())
    table = html_tables.HtmlTable.Bespoke(
      self.page, records, cols or [], rows or [], width, height, html_code, options, profile)
    return table

  def grid(self, records, cols: list = None, rows: list = None, width: Union[int, tuple] = (None, '%'),
           height: Union[int, tuple] = (None, 'px'), html_code: str = None, options: dict = None,
           profile: Union[dict, bool] = None):
    """
    Description:
    -----------

    :tags:
    :categories:

    Usage::

    Attributes:
    ----------
    :param records: List. Optional. The list of dictionaries with the input data.
    :param cols: List. Optional. The list of key from the record to be used as columns in the table.
    :param rows: List. Optional. The list of key from the record to be used as rows in the table.
    :param width: Tuple. Optional. The width of the component in the page, default (100, '%')
    :param height: Tuple. Optional. The height of the component in the page, default (330, "px")
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean. Optional. A flag to set the component performance storage.:
    """
    width_cells, width_rows_header = 50, 100
    for rec in records:
      for c in cols:
          if c not in rec:
            rec[c] = 0
    table = html_tables.HtmlTable.Bespoke(
      self.page, records, cols, rows, width, height, html_code, options, profile)
    table.css({"width": "%spx" % (width_rows_header + len(cols) * width_cells)})
    for i in table[1:]:
      for j in range(len(rows)):
        i[j].attr["name"] = "row_header"
        i[j].css({"width": "%spx" % width_rows_header})
      for cell in i[j:]:
        cell.attr["contenteditable"] = 'true'
        cell.css({"width": '%spx' % width_cells})
    table.style.clear()
    # Set the style for the table grid
    # table.style.add_classes.table.grid_row_header()
    table.style.add_classes.table.grid_vals()
    # table.style.add_classes.table.grid_no_header()
    return table

  def menu(self, table: Html.Html = None, height: Union[int, tuple] = (18, 'px'), options: dict = None,
           update_funcs: list = None, post: Union[list, str] = None, profile: Union[dict, bool] = None):
    """
    Description:
    -----------
    Add a standard menu on the table to trigger standard operation (add, empty, copy, download).

    :tags:
    :categories:

    Usage::

      hierarchy = page.ui.tables.tabulators.hierarchy(html_code="hierarchy")
      menu = page.ui.tables.menu(hierarchy)

    Attributes:
    ----------
    :param table: Component. Optional. The HTML table component.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param update_funcs:
    :param post: List | String. The event used to update the table.
    :param profile: Boolean or Dictionary. Optional. A flag to set the component performance storage.
    """
    commands = [("Csv", "fas fa-file-csv"), ("Clear", "fas fa-trash-alt")]
    menu_items = []
    options = options or {}
    for typ, icon in commands:
      if icon:
        if isinstance(icon, tuple):
          icon = icon[0]
        r = self.page.ui.icons.awesome(
          icon, align="center", tooltip=typ, height=height, width=(15, 'px'), options=options, profile=profile)
        r.icon.style.css.font_factor(-5)
        r.style.css.font_factor(-5)
        if typ == "Csv":
          r.click([table.js.download("csv", "data.csv")])
        elif typ == "New":
          r.click([table.js.addRow(options.get("add", {}), True)])
        elif typ == "Clear":
          r.click([table.js.clearData()])
        menu_items.append(r)
    container = self.page.ui.menu(table, update_funcs=update_funcs, menu_items=menu_items, post=post, editable=False,
                                  options=options, profile=profile)
    return container

  def row(self, components=None, position='middle', width=(100, '%'), height=(None, 'px'), align=None, helper=None,
          html_code: str = None, options=None, profile: Union[bool, dict] = None):
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    record, cols = {}, []
    for i, c in enumerate(components):
      k = "comp_%s" % i
      c.options.managed = False
      cols.append(k)
      record[k] = c
    options = options or {}
    options["with_header"] = False
    options["with_hover"] = False
    table = html_tables.HtmlTable.Bespoke(
      self.page, [record], cols, [], width, height, html_code, options, profile)
    table.style.clear()
    # Set the style for the table grid
    # table.style.add_classes.table.grid_row_header()
    # table.style.add_classes.table.grid_vals()
    # table.style.add_classes.table.grid_no_header()
    return table
