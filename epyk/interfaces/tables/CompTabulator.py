#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import tables as html_tables


class Tabulators:
  
  def __init__(self, ui):
    self.page = ui.page

  def table(self, records=None, cols=None, rows=None, width=(100, '%'), height=(None, 'px'), html_code=None,
            options=None, profile=None):
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
    :param profile: Boolean. Optional. A flag to set the component performance storage.
    """
    #self.page.jsImports.add('tabulator-numbers')
    #self.page.jsImports.add('tabulator-icons')
    #self.page.jsImports.add('tabulator-inputs')
    #self.page.jsImports.add('tabulator-drop')
    #self.page.jsImports.add('tabulator-mutators-inputs')
    #self.page.jsImports.add('editors-inputs')
    #self.page.jsImports.add('editors-dates')
    #self.page.jsImports.add('editors-selects')

    cols = cols or []
    rows = rows or []
    if records is not None and not cols and not rows:
      cols = list(records[0].keys())

    table_options_dflts = {'selectable': False, 'index': '_row', 'pagination': 'local',
                           'paginationSize': 25, 'resizableRows': False, 'movableColumns': True}
    if options is not None:
      table_options_dflts.update(options)

    if not records or len(records) < table_options_dflts["paginationSize"]:
      del table_options_dflts["pagination"]
      del table_options_dflts["paginationSize"]

    json = {}
    if 'json' in table_options_dflts:
      json = table_options_dflts["json"].fromConfig(html_code, {}, page=self.page)
      del table_options_dflts["json"]

    table = html_tables.HtmlTableTabulator.Table(self.page, records, width, height, html_code,
                                                 table_options_dflts, profile)
    table._json_config = json
    table.options.layouts.fitColumns()
    for c in cols + rows:
      table.add_column(c)
    if rows:
      table.options.attr("rows_def", {"headerFilter": True, "fields": rows})
    return table

  def hierarchy(self, records=None, cols=None, rows=None, width=(100, '%'), height=(None, 'px'), html_code=None,
                options=None, profile=None):
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
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean. Optional. A flag to set the component performance storage.
    """
    cols = cols or []
    rows = rows or []
    if records is not None and not cols and not rows:
      cols = list(records[0].keys())

    table_options_dflts = {'selectable': False, 'dataTree': True, 'dataTreeStartExpanded': False,
                           'movableColumns': False}
    if options is not None:
      table_options_dflts.update(options)

    json = {}
    if 'json' in table_options_dflts:
      json = table_options_dflts["json"].fromConfig(html_code, {}, page=self.page)
      del table_options_dflts["json"]
    table = html_tables.HtmlTableTabulator.TableTree(
      self.page, records, width, height, html_code, table_options_dflts, profile)
    table._json_config = json
    table.options.layouts.fitColumns()
    for c in cols + rows:
      table.add_column(c)
    table.options.attr("rows_def", {"headerFilter": True, "formatter": 'cssStyle', 'formatterParams': {
      "css": {"background": self.page.theme.colors[0]}}})
    table.options.attr("columns_def", {"formatter": "numbersFormat", 'formatterParams': {
      'colors': [self.page.theme.danger[1], self.page.theme.greys[-1]],
      'css': {"background": "white"}, "symbol": "", "format": "%v"}})
    return table

  def multi(self, records=None, cols=None, rows=None, width=(100, '%'), height=(None, 'px'), html_code=None,
            options=None, profile=None):
    """
    Description:
    -----------
    Generic Tabulator configuration to get the package plus all the add-ons for Formatters and Editors.
    In the basic Tabulator entry point only the ones used on the Python will be added to the JavaScript page.

    This configuration will load all the external JavaScript features to allow the full customisation.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://www.npmjs.com/package/tabulator-extensions

    Attributes:
    ----------
    :param records: List. Optional. The list of dictionaries with the input data.
    :param cols: List. Optional. The list of key from the record to be used as columns in the table.
    :param rows: List. Optional. The list of key from the record to be used as rows in the table.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean. Optional. A flag to set the component performance storage.
    """
    self.page.jsImports.add('tabulator-numbers')
    self.page.jsImports.add('tabulator-icons')
    self.page.jsImports.add('tabulator-inputs')
    self.page.jsImports.add('tabulator-drop')
    self.page.jsImports.add('tabulator-mutators-inputs')
    self.page.jsImports.add('editors-inputs')
    self.page.jsImports.add('editors-dates')
    self.page.jsImports.add('editors-selects')
    cols = cols or []
    rows = rows or []
    if records is not None and not cols and not rows:
      cols = list(records[0].keys())

    table_options_dflts = {'selectable': False, 'dataTree': True, 'dataTreeStartExpanded': False,
                           'movableColumns': False}
    if options is not None:
      table_options_dflts.update(options)
    json = {}
    if 'json' in table_options_dflts:
      json = table_options_dflts["json"].fromConfig(html_code, {}, page=self.page)
      del table_options_dflts["json"]

    table = html_tables.HtmlTableTabulator.Table(self.page, records, width, height, html_code,
                                                 table_options_dflts, profile)
    table._json_config = json
    for c in rows + cols:
      table.add_column(c)
    if rows:
      table.options.attr("rows_def", {"headerFilter": True, "fields": rows})
    return table

  def trafficlights(self, records=None, cols=None, rows=None, width=(100, '%'), height=(None, 'px'), html_code=None,
                    options=None, profile=None):
    """
    Description:
    -----------

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://www.npmjs.com/package/tabulator-extensions

    Attributes:
    ----------
    :param records: List. Optional. The list of dictionaries with the input data.
    :param cols: List. Optional. The list of key from the record to be used as columns in the table.
    :param rows: List. Optional. The list of key from the record to be used as rows in the table.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean. Optional. A flag to set the component performance storage.
    """
    self.page.jsImports.add('tabulator-numbers')
    self.page.jsImports.add('tabulator-inputs')
    cols = cols or []
    rows = rows or []
    if records is not None and not cols and not rows:
      cols = list(records[0].keys())

    table_options_dflts = {'selectable': False, 'dataTree': True, 'dataTreeStartExpanded': False,
                           'movableColumns': False}
    if options is not None:
      table_options_dflts.update(options)

    table = html_tables.HtmlTableTabulator.Table(self.page, records, width, height, html_code,
                                                 table_options_dflts, profile)
    for c in rows:
      table.add_column(c)
      table.get_column(c).exts.formatters.style(css={"background": self.page.theme.colors[0]})
      table.get_column(c).headerFilter = True
    for c in cols:
      table.add_column(c)
      table.get_column(c).exts.formatters.trafficlight(css={"background": "white"})
      table.get_column(c).headerSort = False
      table.get_column(c).headerVertical = 'flip'
    table.options.attr("rows_def", {
      "headerFilter": True, "formatter": 'cssStyle', 'formatterParams': {"css": {
        "background": self.page.theme.colors[0]}}})
    table.options.attr("columns_def", {
      "headerSort": False, "headerVertical": 'flip', "formatter": "trafficLight", 'formatterParams':
      {'css': {"background": "white"}, 'tooltip': None, 'green': self.page.theme.success[1],
       'red': self.page.theme.danger[1], 'orange': self.page.theme.warning[1]}})
    return table

  def figures(self, records=None, cols=None, rows=None, width=(100, '%'), height=(None, 'px'), html_code=None,
              options=None, profile=None):
    """
    Description:
    -----------

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://www.npmjs.com/package/tabulator-extensions

    Attributes:
    ----------
    :param records: List. Optional. The list of dictionaries with the input data.
    :param cols: List. Optional. The list of key from the record to be used as columns in the table.
    :param rows: List. Optional. The list of key from the record to be used as rows in the table.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean. Optional. A flag to set the component performance storage.
    """
    self.page.jsImports.add('tabulator-numbers')
    self.page.jsImports.add('tabulator-icons')
    self.page.jsImports.add('tabulator-inputs')
    self.page.jsImports.add('tabulator-drop')
    self.page.jsImports.add('tabulator-mutators-inputs')
    self.page.jsImports.add('editors-inputs')
    self.page.jsImports.add('editors-dates')
    self.page.jsImports.add('editors-selects')
    cols = cols or []
    rows = rows or []
    if records is not None and not cols and not rows:
      cols = list(records[0].keys())

    table_options_dflts = {'selectable': False, 'dataTree': True, 'dataTreeStartExpanded': False,
                           'movableColumns': False}
    if options is not None:
      table_options_dflts.update(options)

    json = {}
    if 'json' in table_options_dflts:
      json = table_options_dflts["json"].fromConfig(html_code, {}, page=self.page)
      del table_options_dflts["json"]

    table = html_tables.HtmlTableTabulator.Table(self.page, records, width, height, html_code,
                                                 table_options_dflts, profile)
    table._json_config = json
    for c in rows:
      table.add_column(c)
      table.get_column(c).exts.formatters.style(css={"background": self.page.theme.colors[0]})
      table.get_column(c).headerFilter = True
    for c in cols:
      table.add_column(c)
      table.get_column(c).exts.formatters.number_format(css={"background": "white"})
    table.options.attr("rows_def", {"headerFilter": True, "formatter": 'cssStyle', 'formatterParams': {
      "css": {"background": self.page.theme.colors[0]}}})
    table.options.attr("columns_def", {"formatter": "numbersFormat", 'formatterParams': {
      'colors': [self.page.theme.danger[1], self.page.theme.greys[-1]],
      'css': {"background": "white"}, "symbol": "", "format": "%v"}})
    return table

  def intensity(self, records=None, cols=None, rows=None, width=(100, '%'), height=(None, 'px'), html_code=None,
                options=None, profile=None):
    """
    Description:
    -----------

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://www.npmjs.com/package/tabulator-extensions

    Attributes:
    ----------
    :param records: List. Optional. The list of dictionaries with the input data.
    :param cols: List. Optional. The list of key from the record to be used as columns in the table.
    :param rows: List. Optional. The list of key from the record to be used as rows in the table.
    :param width: Tuple. Optional. A tuple with the integer for the component width and its unit.
    :param height: Tuple. Optional. A tuple with the integer for the component height and its unit.
    :param html_code: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean. Optional. A flag to set the component performance storage.
    """
    self.page.jsImports.add('tabulator-numbers')
    self.page.jsImports.add('tabulator-inputs')
    cols = cols or []
    rows = rows or []
    if records is not None and not cols and not rows:
      cols = list(records[0].keys())

    table_options_dflts = {"steps": 100, 'selectable': False, 'dataTree': True, 'dataTreeStartExpanded': False,
                           'movableColumns': False}
    if options is not None:
      table_options_dflts.update(options)

    table = html_tables.HtmlTableTabulator.Table(self.page, records, width, height, html_code,
                                                 table_options_dflts, profile)
    for c in rows:
      table.add_column(c)
      table.get_column(c).exts.formatters.style(css={"background": self.page.theme.colors[0]})
      table.get_column(c).headerFilter = True
    for c in cols:
      table.add_column(c)
      table.get_column(c).exts.formatters.intensity(
        steps=table_options_dflts["steps"], colors=["white", self.page.theme.danger[1]])
    table.options.attr("rows_def", {"headerFilter": True, "formatter": 'cssStyle', 'formatterParams': {
      "css": {"background": self.page.theme.colors[0]}}})
    table.options.attr("columns_def", {"formatter": "numbersIntensity", 'formatterParams': {
      "is_number": True, "symbol": "", "format": "%v", "steps": table_options_dflts["steps"], 'colors': [
        "white", self.page.theme.danger[1]]}
      })
    return table
