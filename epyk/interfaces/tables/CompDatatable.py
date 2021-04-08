#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import tables as html_tables


class Datatables:

  def __init__(self, ui):
    self.page = ui.page

  def table(self, records=None, cols=None, rows=None, width=(100, '%'), height=(None, 'px'), html_code=None,
            options=None, profile=None):
    """
    Description:
    ------------
    Create a generic DataTable table.

    :tags:
    :categories:

    Usage:
    -----

    Attributes:
    ----------
    :param records: List. Optional. The list of dictionaries with the input data.
    :param cols: List. Optional. The list of key from the record to be used as columns in the table.
    :param rows: List. Optional. The list of key from the record to be used as rows in the table.
    :param width: Tuple. Optional. The width of the component in the page, default (100, '%')
    :param height: Tuple. Optional. The height of the component in the page, default (330, "px")
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean. Optional. A flag to set the component performance storage.
    """
    data = []
    cols = cols or []
    rows = rows or []
    if not cols and not rows:
      cols = list(records[0].keys())
    for rec in records:
      data.append([rec.get(c) for c in cols + rows])

    table = html_tables.HtlmTableDatatable.Table(self.page, data, width, height, html_code, options,
                                                 profile)
    table.config.autoWidth = True
    table.config.scrollCollapse = True
    for c in cols + rows:
      col_def = table.config.columns
      col_def.title = c
      col_def.className.center()
    table.style.themes.compact()
    table.config.scrollX = True
    return table

  def heatmap(self):
    pass

  def intensity(self):
    pass

  def hierarchy(self):
    pass

  def delta_signed(self):
    pass

  def delta_abs(self):
    pass

  def comments(self):
    pass
