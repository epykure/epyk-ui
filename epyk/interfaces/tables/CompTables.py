#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union, List
from epyk.core.html import Html
from epyk.interfaces import Arguments
from epyk.core.py import types
from epyk.core.html import tables as html_tables
from epyk.core.js import JsUtils
from epyk.core.css import Defaults_css

from epyk.core.data import events
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
    """
    return CompDatatable.Datatables(self)

  def basic(self, records: List[dict] = None, cols=None, rows=None, width: types.SIZE_TYPE = (100, '%'),
            height: types.SIZE_TYPE = (None, 'px'), html_code: str = None, options: dict = None,
            profile: types.PROFILE_TYPE = None):
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
    :param records: Optional. The list of dictionaries with the input data
    :param cols: Optional. The list of key from the record to be used as columns in the table
    :param rows: Optional. The list of key from the record to be used as rows in the table
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    records = records or []
    if len(records) > 0 and not cols and not rows:
      cols = list(records[0].keys())
    table = html_tables.HtmlTable.Bespoke(
      self.page, records, cols or [], rows or [], width, height, html_code, options, profile)
    return table

  def grid(self, records, cols: list = None, rows: list = None, width: types.SIZE_TYPE = (None, '%'),
           height: types.SIZE_TYPE = (None, 'px'), html_code: str = None, options: types.OPTION_TYPE = None,
           profile: types.PROFILE_TYPE = None):
    """
    Description:
    -----------

    :tags:
    :categories:

    Usage::

    Attributes:
    ----------
    :param records: Optional. The list of dictionaries with the input data
    :param cols: Optional. The list of key from the record to be used as columns in the table
    :param rows: Optional. The list of key from the record to be used as rows in the table
    :param width: Optional. The width of the component in the page, default (100, '%')
    :param height: Optional. The height of the component in the page, default (330, "px")
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
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

  def menu(self, table: Html.Html = None, height: types.SIZE_TYPE = (18, 'px'), options: types.OPTION_TYPE = None,
           update_funcs: list = None, post: Union[list, str] = None, profile: types.PROFILE_TYPE = None,
           columns: dict = None, title: Union[str, dict] = None,):
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
    :param table: Optional. The HTML table component
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param options: Optional. Specific Python options available for this component
    :param update_funcs: Optional. JavaScript functions to update the table component
    :param post: Optional. The event used to update the table
    :param profile: Optional. A flag to set the component performance storage
    :param columns: Optional.
    :param title: Optional. The title value or component
    """
    commands = [("Csv", "fas fa-file-csv"), ("Clear", "fas fa-trash-alt")]
    if columns is not None:
      commands.insert(0, ("Columns", "fas fa-columns"))
    menu_items, checks, popup_columns = [], None, None
    options = options or {}
    for typ, icon in commands:
      if icon:
        if isinstance(icon, tuple):
          icon = icon[0]
        r = self.page.ui.icons.awesome(
          icon, align="center", tooltip=typ, height=height, width=(15, 'px'), options=options, profile=profile)
        r.icon.style.css.font_factor(options.get("icon_size", Defaults_css.MENU_ICON_SIZE))
        r.style.css.font_factor(options.get("icon_size", Defaults_css.MENU_ICON_SIZE))
        if typ == "Csv" and hasattr(table.js, 'download'):
          r.click([table.js.download("csv", "data.csv")])
          r.icon.style.add_classes.div.color_hover()
        elif typ == "New" and hasattr(table.js, 'addRow'):
          r.click([table.js.addRow(options.get("add", {}), True)])
          r.icon.style.add_classes.div.color_hover()
        elif typ == "Clear" and hasattr(table.js, 'empty'):
          r.click([table.js.empty()])
          r.icon.style.add_classes.div.danger_hover()
        elif typ == "Columns" and table is not None and hasattr(table.js, 'showColumn'):
          checks = self.page.ui.lists.checks([{"value": k, "checked": v} for k, v in columns.items()])
          popup_columns = self.page.ui.modals.popup([checks], title="Columns", options={"background": False})
          popup_columns.window.style.css.border = "1px solid %s" % self.page.theme.greys[3]
          popup_columns.window.style.css.min_width = 120
          popup_columns.window.style.css.background = self.page.theme.greys[0]
          popup_columns.options.closure = False
          popup_columns.window.focusout([popup_columns.dom.hide()])
          popup_columns.window[0][1].style.css.max_height = 90
          popup_columns.window[0][1].click([
            self.page.js.if_(events.target["checked"], [
              table.js.showColumn(events.event["srcElement"]["nextSibling"]["innerHTML"]),
              table.js.redraw(True)
            ]).else_([
              table.js.hideColumn(events.event["srcElement"]["nextSibling"]["innerHTML"]),
              table.js.redraw(True)
            ])
          ])
          r.click([
            popup_columns.dom.show(),
            popup_columns.window.dom.focus(prevent_scroll=True),
            popup_columns.js.event_position(left=-5)])
        menu_items.append(r)
    container = self.page.ui.menu(table, update_funcs=update_funcs, menu_items=menu_items, post=post, editable=False,
                                  options=options, profile=profile, title=title)
    if popup_columns is not None:
      container.columns = popup_columns
    if checks is not None:
      container.checks = checks

      def table_set_columns(data):
          """
          Description:
          ------------

          TODO: Add refresh option for the table layout.

          Attributes:
          ----------
          :param data:
          """
          return JsUtils.jsConvertFncs([
            checks.dom.unSelectAll(), checks.dom.select_item(data),
            table.js.hideColumns(checks.dom.unselected), table.js.showColumns(data)], toStr=True)

      container.js.set_columns = table_set_columns
    if getattr(table.options, "dataTree", False):
      expand = container.add_command("fas fa-expand", tooltip="Expand tree table")
      expand.icon.style.css.font_factor(options.get("icon_size", Defaults_css.MENU_ICON_SIZE))
      expand.style.css.margin_left = 2
      expand.icon.style.add_classes.div.color_hover()
      expand.style.css.margin_right = 2
      expand.click(table.js.getRows().forEach(["row.treeExpand()"], value="row"))
      compress = container.add_command("fas fa-compress", tooltip="Collapse tree table")
      compress.icon.style.css.font_factor(options.get("icon_size", Defaults_css.MENU_ICON_SIZE))
      compress.style.css.margin_left = 2
      compress.icon.style.add_classes.div.color_hover()
      compress.style.css.margin_right = 2
      compress.click(table.js.getRows().forEach(["row.treeCollapse()"], value="row"))
    return container

  def row(self, components: List[Html.Html] = None, position: str = 'middle', width: types.SIZE_TYPE = (100, '%'),
          height: types.SIZE_TYPE = (None, 'px'), align: str = None, helper: str = None,
          html_code: str = None, options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = None):
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
