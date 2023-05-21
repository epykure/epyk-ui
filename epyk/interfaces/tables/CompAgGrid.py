#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.py import types
from epyk.interfaces import Arguments
from epyk.core.html import tables as html_tables


class AgGrid:

  def __init__(self, ui):
    self.page = ui.page

  def table(self, records: list = None, cols: list = None, rows: list = None, width: types.SIZE_TYPE = (100, '%'),
            height: types.SIZE_TYPE = (300, 'px'), html_code: str = None,
            options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = None) -> html_tables.HtmlTableAgGrid.Table:
    """
    Create a generic Angular Grid table.

    :tags:
    :categories:

    Usage::

      import epyk as pk
      from epyk.mocks import urls as data_urls

      page = pk.Page()
      data = page.py.requests.csv(data_urls.AIRPORT_TRAFFIC)
      table = page.ui.tables.aggrids.table(data)
      table.options.paginationPageSize = 10
      table.options.rowSelection = "single"

      table = page.ui.tables.aggrids.table(rows=["athlete", "country", "sport", 'year'])
      table.attr["class"].add("ag-theme-alpine")
      c = table.get_column("athlete")
      c.headerCheckboxSelection = True
      c.headerCheckboxSelectionCurrentPageOnly = True
      c.checkboxSelection = True
      c.showDisabledCheckboxes = True
      table.options.rowSelection = 'multiple'
      table.options.suppressRowClickSelection = True
      table.onReady([
        page.js.fetch("https://www.ag-grid.com/example-assets/olympic-winners.json").json().process(table.js.setRowData)
      ])

    :param records: Optional. The list of dictionaries with the input data.
    :param cols: Optional. The list of key from the record to be used as columns in the table.
    :param rows: Optional. The list of key from the record to be used as rows in the table.
    :param width: Optional. A tuple with the integer for the component width and its unit.
    :param height: Optional. A tuple with the integer for the component height and its unit.
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")

    cols = cols or []
    rows = rows or []
    if not cols and not rows:
      if records is not None and records:
        cols = list(records[0].keys())

    table_options_dfls = {'headerHeight': 30, 'rowHeight': 25}
    if options is not None:
      table_options_dfls.update(options)
    table = html_tables.HtmlTableAgGrid.Table(self.page, records, width, height, html_code, table_options_dfls, profile)
    for c in cols + rows:
      table.add_column(c)
    if height[0] == "auto":
      table.options.onGridReady(["param.api.setDomLayout('autoHeight')"])
    return table
