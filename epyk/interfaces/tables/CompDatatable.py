#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import Union
from epyk.core.html import tables as html_tables


class Datatables:

  def __init__(self, ui):
    self.page = ui.page

  def table(self, records=None, cols: list = None, rows: list = None, width: Union[int, tuple] = (100, '%'),
            height: Union[int, tuple] = (None, 'px'), html_code: str = None,
            options: dict = None, profile: Union[dict, bool] = None):
    """
    Description:
    ------------
    Create a generic DataTable table.

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
    :param profile: Boolean. Optional. A flag to set the component performance storage.
    """
    data = []
    cols = cols or []
    rows = rows or []
    if not cols and not rows:
      cols = list(records[0].keys())
    for rec in records:
      data.append([rec.get(c) for c in cols + rows])

    table = html_tables.HtlmTableDatatable.Table(
      self.page, data, width, height, html_code, options, profile)
    table.options.autoWidth = True
    table.options.scrollCollapse = True
    for c in cols + rows:
      col_def = table.options.columns
      col_def.title = c
      col_def.className.center()
    table.style.themes.compact()
    table.options.scrollX = True
    return table

  def heatmap(self, records=None, cols: list = None, rows: list = None, width: Union[int, tuple] = (100, '%'),
              height: Union[int, tuple] = (None, 'px'), html_code: str = None,
              options: dict = None, profile: Union[dict, bool] = None):
    raise NotImplementedError()

  def intensity(self, records=None, cols: list = None, rows: list = None, width: Union[int, tuple] = (100, '%'),
                height: Union[int, tuple] = (None, 'px'), html_code: str = None,
                options: dict = None, profile: Union[dict, bool] = None):
    raise NotImplementedError()

  def hierarchy(self, records=None, cols: list = None, rows: list = None, width: Union[int, tuple] = (100, '%'),
                height: Union[int, tuple] = (None, 'px'), html_code: str = None,
                options: dict = None, profile: Union[dict, bool] = None):
    raise NotImplementedError()

  def delta_signed(self, records=None, cols: list = None, rows: list = None, width: Union[int, tuple] = (100, '%'),
                   height: Union[int, tuple] = (None, 'px'), html_code: str = None,
                   options: dict = None, profile: Union[dict, bool] = None):
    raise NotImplementedError()

  def delta_abs(self, records=None, cols: list = None, rows: list = None, width: Union[int, tuple] = (100, '%'),
                height: Union[int, tuple] = (None, 'px'), html_code: str = None,
                options: dict = None, profile: Union[dict, bool] = None):
    raise NotImplementedError()

  def comments(self, records=None, cols: list = None, rows: list = None, width: Union[int, tuple] = (100, '%'),
               height: Union[int, tuple] = (None, 'px'), html_code: str = None,
               options: dict = None, profile: Union[dict, bool] = None):
    raise NotImplementedError()
