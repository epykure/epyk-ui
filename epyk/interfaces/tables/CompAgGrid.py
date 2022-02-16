#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union
from epyk.core.html import tables as html_tables


class AgGrid:

  def __init__(self, ui):
    self.page = ui.page

  def table(self, records=None, cols: list = None, rows: list = None, width: Union[int, tuple] = (100, '%'),
            height: Union[int, tuple] = (300, 'px'), html_code: str = None,
            options: dict = None, profile: Union[bool, dict] = None):
    """
    Description:
    ------------
    Create a generic Angular Grid table.

    :tags:
    :categories:

    Usage::

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
    cols = cols or []
    rows = rows or []
    if not cols and not rows:
      if records is not None and records:
        cols = list(records[0].keys())

    table_options_dfls = {'headerHeight': 30, 'rowHeight': '50'}
    if options is not None:
      table_options_dfls.update(options)
    table = html_tables.HtmlTableAgGrid.Table(self.page, records, width, height, html_code, table_options_dfls, profile)
    for c in cols + rows:
      table.add_column(c)
    return table
