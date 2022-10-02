#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.py import types
from epyk.core.html import tables as html_tables


class Google:
  def __init__(self, ui):
    self.page = ui.page

  def table(self, records=None, cols: list = None, rows: list = None, width: types.SIZE_TYPE = (100, '%'),
            height: types.SIZE_TYPE = (None, 'px'), html_code: str = None,
            options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = None):
    """
    :tags:
    :categories:

    Usage::

    :param records: Optional. The list of dictionaries with the input data
    :param cols: Optional. The list of key from the record to be used as columns in the table
    :param rows: Optional. The list of key from the record to be used as rows in the table
    :param width: Optional. The width of the component in the page, default (100, '%')
    :param height: Optional. The height of the component in the page, default (330, "px")
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    cols = cols or []
    rows = rows or []
    if records is not None and not cols and not rows:
      cols = list(records[0].keys())

    table_options_dfls = {'type': 'Table'}
    if options is not None:
      table_options_dfls.update(options)

    data = self.page.data.google.table(records, cols, rows)
    table = html_tables.HtmlTableGoogle.Table(
      self.page, data, width, height, html_code, table_options_dfls, profile)
    for c in cols + rows:
      table.add_column(c)
    return table
