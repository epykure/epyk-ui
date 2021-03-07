#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import tables as html_tables


class Google:
  def __init__(self, ui):
    self.page = ui.page

  def table(self, records=None, cols=None, rows=None, width=(100, '%'), height=(None, 'px'), html_code=None,
            options=None, profile=None):
    """
    Description:
    ------------

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
    cols = cols or []
    rows = rows or []
    if records is not None and not cols and not rows:
      cols = list(records[0].keys())

    table_options_dfls = {'type': 'Table'}
    if options is not None:
      table_options_dfls.update(options)

    data = self.page.data.google.table(records, cols, rows)
    table = html_tables.HtmlTableGoogle.Table(self.page, data, width, height, html_code,
                                              table_options_dfls, profile)
    for c in cols + rows:
      table.add_column(c)
    return table
