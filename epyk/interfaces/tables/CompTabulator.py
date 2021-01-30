#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import tables as html_tables


class Tabulators(object):
  def __init__(self, context):
    self.parent = context

  def table(self, records=None, cols=None, rows=None, width=(100, '%'), height=(None, 'px'), htmlCode=None, options=None, profile=None):
    """
    Description:
    -----------

    Usage:
    -----

    Attributes:
    ----------
    :param records:
    :param cols:
    :param rows:
    :param width: Tuple. Optional. The width of the component in the page, default (100, '%')
    :param height: Tuple. Optional. The height of the component in the page, default (330, "px")
    :param htmlCode: String. Optional. An identifier for this component (on both Python and Javascript side).
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean. Optional. A flag to set the component performance storage.
    """
    cols = cols or []
    rows = rows or []
    if records is not None and not cols and not rows:
      cols = list(records[0].keys())

    table_options_dflts = {'selectable': False, 'index': '_row', 'pagination': 'local',
                           'paginationSize': 25, 'resizableRows': False, 'movableColumns': True}
    if options is not None:
      table_options_dflts.update(options)

    table = html_tables.HtmlTableTabulator.Table(self.parent.context.rptObj, records, width, height, htmlCode, table_options_dflts, profile)
    table.config.layout.fitColumns()
    for c in cols + rows:
      table.add_column(c)
    if rows:
      table.options.attr("rows_def", {"headerFilter": True, "fields": rows})
    return table

  def hierarchy(self, records=None, cols=None, rows=None, width=(100, '%'), height=(None, 'px'), htmlCode=None, options=None, profile=None):
    """
    Description:
    -----------

    Usage:
    -----

    Attributes:
    ----------
    :param records:
    :param cols:
    :param rows:
    :param width:
    :param height:
    :param htmlCode:
    :param options:
    :param profile:
    """
    self.parent.context.rptObj.jsImports.add('tabulator-numbers')
    self.parent.context.rptObj.jsImports.add('tabulator-icons')
    self.parent.context.rptObj.jsImports.add('tabulator-inputs')
    self.parent.context.rptObj.jsImports.add('tabulator-drop')
    self.parent.context.rptObj.jsImports.add('tabulator-mutators-inputs')
    self.parent.context.rptObj.jsImports.add('editors-inputs')
    self.parent.context.rptObj.jsImports.add('editors-dates')
    self.parent.context.rptObj.jsImports.add('editors-selects')

    cols = cols or []
    rows = rows or []
    if records is not None and not cols and not rows:
      cols = list(records[0].keys())

    table_options_dflts = {'selectable': False, 'dataTree': True, 'dataTreeStartExpanded': False, 'movableColumns': False}
    if options is not None:
      table_options_dflts.update(options)

    json = {}
    if 'json' in table_options_dflts:
      json = table_options_dflts["json"].fromConfig(htmlCode, {}, page=self.parent.context.rptObj)
      del table_options_dflts["json"]
    table = html_tables.HtmlTableTabulator.Table(self.parent.context.rptObj, records, width, height, htmlCode, table_options_dflts, profile)
    table._json_config = json
    table.config.layout.fitColumns()
    for c in cols + rows:
      table.add_column(c)
    table.options.attr("rows_def", {"headerFilter": True, "formatter": 'cssStyle', 'formatterParams':
      {"css": {"background": self.parent.context.rptObj.theme.colors[0]}}})
    table.options.attr("columns_def", {"formatter": "numbersFormat", 'formatterParams':
      {'colors': [self.parent.context.rptObj.theme.danger[1], self.parent.context.rptObj.theme.greys[-1]],
       'css': {"background": "white"}, "symbol": "", "format": "%v"}})
    return table

  def multi(self, records=None, cols=None, rows=None, width=(100, '%'), height=(None, 'px'), htmlCode=None, options=None, profile=None):
    """
    Description:
    -----------
    Generic Tabulator configuration to get the package plus all the addons for formatters and editors.
    In the basic Tabulator entry point only the ones used on the Python will be added to the JavaScript page.

    This configuration will load all the external JavaScript features to allow the full customisation

    Usage:
    -----

    Related Pages:

      https://www.npmjs.com/package/tabulator-extensions

    Attributes:
    ----------
    :param records:
    :param cols:
    :param rows:
    :param width:
    :param height:
    :param htmlCode:
    :param options:
    :param profile:
    """
    self.parent.context.rptObj.jsImports.add('tabulator-numbers')
    self.parent.context.rptObj.jsImports.add('tabulator-icons')
    self.parent.context.rptObj.jsImports.add('tabulator-inputs')
    self.parent.context.rptObj.jsImports.add('tabulator-drop')
    self.parent.context.rptObj.jsImports.add('tabulator-mutators-inputs')
    self.parent.context.rptObj.jsImports.add('editors-inputs')
    self.parent.context.rptObj.jsImports.add('editors-dates')
    self.parent.context.rptObj.jsImports.add('editors-selects')
    cols = cols or []
    rows = rows or []
    if records is not None and not cols and not rows:
      cols = list(records[0].keys())

    table_options_dflts = {'selectable': False, 'dataTree': True, 'dataTreeStartExpanded': False, 'movableColumns': False}
    if options is not None:
      table_options_dflts.update(options)
    json = {}
    if 'json' in table_options_dflts:
      json = table_options_dflts["json"].fromConfig(htmlCode, {}, page=self.parent.context.rptObj)
      del table_options_dflts["json"]
    table = html_tables.HtmlTableTabulator.Table(self.parent.context.rptObj, records, width, height, htmlCode,
                                                 table_options_dflts, profile)
    table._json_config = json
    for c in rows + cols:
      table.add_column(c)
    if rows:
      table.options.attr("rows_def", {"headerFilter": True, "fields": rows})
    return table

  def trafficlights(self, records=None, cols=None, rows=None, width=(100, '%'), height=(None, 'px'), htmlCode=None,
                 options=None, profile=None):
    """
    Description:
    -----------

    Related Pages:

      https://www.npmjs.com/package/tabulator-extensions

    Attributes:
    ----------
    :param records:
    :param cols:
    :param rows:
    :param width:
    :param height:
    :param htmlCode:
    :param options:
    :param profile:
    """
    self.parent.context.rptObj.jsImports.add('tabulator-numbers')
    self.parent.context.rptObj.jsImports.add('tabulator-inputs')
    cols = cols or []
    rows = rows or []
    if records is not None and not cols and not rows:
      cols = list(records[0].keys())

    table_options_dflts = {'selectable': False, 'dataTree': True, 'dataTreeStartExpanded': False,
                           'movableColumns': False}
    if options is not None:
      table_options_dflts.update(options)

    table = html_tables.HtmlTableTabulator.Table(self.parent.context.rptObj, records, width, height, htmlCode,
                                                 table_options_dflts, profile)
    for c in rows:
      table.add_column(c)
      table.get_column(c).exts.formatters.style(css={"background": self.parent.context.rptObj.theme.colors[0]})
      table.get_column(c).headerFilter = True
    for c in cols:
      table.add_column(c)
      table.get_column(c).exts.formatters.trafficlight(css={"background": "white"})
      table.get_column(c).headerSort = False
      table.get_column(c).headerVertical = 'flip'
    table.options.attr("rows_def", {"headerFilter": True, "formatter": 'cssStyle', 'formatterParams': {"css": {"background": self.parent.context.rptObj.theme.colors[0]}}})
    table.options.attr("columns_def", {"headerSort": False, "headerVertical": 'flip', "formatter": "trafficLight", 'formatterParams':
      {'css': {"background": "white"}, 'tooltip': None, 'green': self.parent.context.rptObj.theme.success[1],
       'red': self.parent.context.rptObj.theme.danger[1], 'orange': self.parent.context.rptObj.theme.warning[1]}})
    return table

  def figures(self, records=None, cols=None, rows=None, width=(100, '%'), height=(None, 'px'), htmlCode=None,
                 options=None, profile=None):
    """
    Description:
    -----------

    Related Pages:

      https://www.npmjs.com/package/tabulator-extensions

    Attributes:
    ----------
    :param records:
    :param cols:
    :param rows:
    :param width:
    :param height:
    :param htmlCode:
    :param options:
    :param profile:
    """
    self.parent.context.rptObj.jsImports.add('tabulator-numbers')
    self.parent.context.rptObj.jsImports.add('tabulator-icons')
    self.parent.context.rptObj.jsImports.add('tabulator-inputs')
    self.parent.context.rptObj.jsImports.add('tabulator-drop')
    self.parent.context.rptObj.jsImports.add('tabulator-mutators-inputs')
    self.parent.context.rptObj.jsImports.add('editors-inputs')
    self.parent.context.rptObj.jsImports.add('editors-dates')
    self.parent.context.rptObj.jsImports.add('editors-selects')
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
      json = table_options_dflts["json"].fromConfig(htmlCode, {}, page=self.parent.context.rptObj)
      del table_options_dflts["json"]

    table = html_tables.HtmlTableTabulator.Table(self.parent.context.rptObj, records, width, height, htmlCode,
                                                 table_options_dflts, profile)
    table._json_config = json
    for c in rows:
      table.add_column(c)
      table.get_column(c).exts.formatters.style(css={"background": self.parent.context.rptObj.theme.colors[0]})
      table.get_column(c).headerFilter = True
    for c in cols:
      table.add_column(c)
      table.get_column(c).exts.formatters.number_format(css={"background": "white"})
    table.options.attr("rows_def", {"headerFilter": True, "formatter": 'cssStyle', 'formatterParams':
      {"css": {"background": self.parent.context.rptObj.theme.colors[0]}}})
    table.options.attr("columns_def", {"formatter": "numbersFormat", 'formatterParams':
      {'colors': [self.parent.context.rptObj.theme.danger[1], self.parent.context.rptObj.theme.greys[-1]],
        'css': {"background": "white"}, "symbol": "", "format": "%v"}})
    return table

  def intensity(self, records=None, cols=None, rows=None, width=(100, '%'), height=(None, 'px'), htmlCode=None,
                 options=None, profile=None):
    """
    Description:
    -----------

    Related Pages:

      https://www.npmjs.com/package/tabulator-extensions

    Attributes:
    ----------
    :param records:
    :param cols:
    :param rows:
    :param width:
    :param height:
    :param htmlCode:
    :param options:
    :param profile:
    """
    self.parent.context.rptObj.jsImports.add('tabulator-numbers')
    self.parent.context.rptObj.jsImports.add('tabulator-inputs')
    cols = cols or []
    rows = rows or []
    if records is not None and not cols and not rows:
      cols = list(records[0].keys())

    table_options_dflts = {"steps": 100, 'selectable': False, 'dataTree': True, 'dataTreeStartExpanded': False, 'movableColumns': False}
    if options is not None:
      table_options_dflts.update(options)

    table = html_tables.HtmlTableTabulator.Table(self.parent.context.rptObj, records, width, height, htmlCode,
                                                 table_options_dflts, profile)
    for c in rows:
      table.add_column(c)
      table.get_column(c).exts.formatters.style(css={"background": self.parent.context.rptObj.theme.colors[0]})
      table.get_column(c).headerFilter = True
    for c in cols:
      table.add_column(c)
      table.get_column(c).exts.formatters.intensity(steps=table_options_dflts["steps"], colors=["white", self.parent.context.rptObj.theme.danger[1]])
    table.options.attr("rows_def", {"headerFilter": True, "formatter": 'cssStyle', 'formatterParams': {"css": {"background": self.parent.context.rptObj.theme.colors[0]}}})
    table.options.attr("columns_def", {"formatter": "numbersIntensity", 'formatterParams':
      {"is_number": True, "symbol": "", "format": "%v", "steps": table_options_dflts["steps"], 'colors': ["white", self.parent.context.rptObj.theme.danger[1]]}
      })
    return table
