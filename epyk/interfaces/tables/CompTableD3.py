#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.py import types


class D3:

  def __init__(self, ui):
    self.page = ui.page

  def table(self, records: list = None, header: list = None, width: types.SIZE_TYPE = (100, '%'),
            height: types.SIZE_TYPE = (None, 'px'), html_code: str = None, options: types.OPTION_TYPE = None,
            profile: types.PROFILE_TYPE = None):
    """

    :tags:
    :categories:

    Usage::

    :param records: Optional. The list of dictionaries with the input data
    :param header: Optional.
    :param width: Optional. The width of the component in the page, default (100, '%')
    :param height: Optional. The height of the component in the page, default (330, "px")
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    table = self.page.ui.div(width=width, height=height, html_code=html_code, options=options, profile=profile)
    d3_table = table.js.d3.select("#%s" % table.htmlCode, js_code='d3Table').rappend('table')
    if header is None and records is not None:
      header = list(records[0].keys())
    table.onReady(
      [d3_table.toStr(),
       d3_table.rappend('thead').rappend('tr')
         .selectAll('th').data(header).enter().rappend('th').text("ƒ('head')").toStr(),
       d3_table.rappend('tbody').selectAll('tr').data(records).enter()
         .rappend('tr').selectAll('td').dataRecord(header).enter().rappend('td').html().toStr()
       ]
    )
    return table
