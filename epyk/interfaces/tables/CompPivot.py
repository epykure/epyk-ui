#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.py import types
from epyk.core.html import tables as html_tables
from epyk.interfaces import Arguments


class Pivottable:

  def __init__(self, ui):
    self.page = ui.page

  def pivot(self, records: list = None, rows: list = None, cols: list = None, width: types.SIZE_TYPE = (100, '%'),
            height: types.SIZE_TYPE = (None, 'px'), html_code: str = None,
            helper: str = None, options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = False):
    """ Create an HTML Pivot table.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://pivottable.js.org/examples/
      https://react-pivottable.js.org/
      https://jsfiddle.net/nicolaskruchten/w86bgq9o/

    :param records:
    :param rows:
    :param cols:
    :param width: Optional. The width of the component in the page, default (100, '%')
    :param height: Optional. The height of the component in the page, default (330, "px")
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side).
    :param helper: Optional. Display a tooltip info component.
    :param options: Optional. Specific Python options available for this component.
    :param profile: Optional. A flag to set the component performance storage.
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    table = html_tables.HtmlTablePivot.PivotTable(self.page, records, rows, cols, width, height, html_code,
                                                  helper, options, profile)
    return table

  def ui(self, records: list = None, rows: list = None, cols: list = None, width: types.SIZE_TYPE = (100, '%'),
         height: types.SIZE_TYPE = (None, 'px'), html_code: str = None,
         helper: str = None, options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = False):
    """ Create an HTML Pivot table.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://pivottable.js.org/examples/
      https://react-pivottable.js.org/
      https://jsfiddle.net/nicolaskruchten/w86bgq9o/

    :param records:
    :param rows:
    :param cols:
    :param width: Optional. The width of the component in the page, default (100, '%')
    :param height: Optional. The height of the component in the page, default (330, "px")
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. Display a tooltip info component
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    table = html_tables.HtmlTablePivot.PivotUITable(self.page, records, rows, cols, width, height,
                                                    html_code, helper, options, profile)
    return table

  def sub_total(self, records: list = None, rows: list = None, cols: list = None, width: types.SIZE_TYPE = (100, '%'),
                height: types.SIZE_TYPE = (None, 'px'), html_code: str = None,
                helper: str = None, options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = False):
    """ Create an HTML Pivot table.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://pivottable.js.org/examples/
      https://react-pivottable.js.org/
      https://jsfiddle.net/nicolaskruchten/w86bgq9o/

    :param records:
    :param rows:
    :param cols:
    :param width: Optional. The width of the component in the page, default (100, '%')
    :param height: Optional. The height of the component in the page, default (330, "px")
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. Display a tooltip info component
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    table = html_tables.HtmlTablePivot.PivotUITable(self.page, records, rows, cols, width, height,
                                                    html_code, helper, options, profile)
    table.sub_total()
    return table

  def heatmap(self, records: list = None, rows: list = None, cols: list = None, values=None,
              width: types.SIZE_TYPE = (100, '%'), height: types.SIZE_TYPE = (None, 'px'),
              html_code: str = None, helper: str = None, options: types.OPTION_TYPE = None,
              profile: types.PROFILE_TYPE = False):
    """ Create an HTML Pivot table.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://pivottable.js.org/examples/
      https://react-pivottable.js.org/
      https://jsfiddle.net/nicolaskruchten/w86bgq9o/

    :param records:
    :param rows:
    :param cols:
    :param values:
    :param width: Optional. The width of the component in the page, default (100, '%')
    :param height: Optional. The height of the component in the page, default (330, "px")
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. Display a tooltip info component
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    table = html_tables.HtmlTablePivot.PivotTable(
      self.page, records, rows, cols, width, height, html_code, helper, options, profile)
    table.renderers.heatmap()
    if values is not None:
      table.aggregators.sumOverSum(values)
    return table

  def c3(self, records=None, rows: list = None, cols: list = None, width: types.SIZE_TYPE = (100, '%'),
         height: types.SIZE_TYPE = (None, 'px'), html_code: str = None,
         helper: str = None, options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = False):
    """ Create an HTML Pivot table.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://pivottable.js.org/examples/
      https://react-pivottable.js.org/
      https://jsfiddle.net/nicolaskruchten/w86bgq9o/

    :param records:
    :param rows:
    :param cols:
    :param width: Optional. The width of the component in the page, default (100, '%')
    :param height: Optional. The height of the component in the page, default (330, "px")
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. Display a tooltip info component
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    table = html_tables.HtmlTablePivot.PivotUITable(
      self.page, records, rows, cols, width, height, html_code, helper, options, profile)
    table.renderers.c3.bar()
    return table

  def d3(self, records=None, rows: list = None, cols: list = None, width: types.SIZE_TYPE = (100, '%'),
         height: types.SIZE_TYPE = (None, 'px'), html_code: str = None,
         helper: str = None, options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = False):
    """ Create a HTML Pivot table.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://pivottable.js.org/examples/
      https://react-pivottable.js.org/
      https://jsfiddle.net/nicolaskruchten/w86bgq9o/

    :param records:
    :param rows:
    :param cols:
    :param width: Optional. The width of the component in the page, default (100, '%')
    :param height: Optional. The height of the component in the page, default (330, "px")
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. Display a tooltip info component
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    table = html_tables.HtmlTablePivot.PivotUITable(
      self.page, records, rows, cols, width, height, html_code, helper, options, profile)
    table.renderers.treemap()
    return table

  def plotly(self, records=None, rows: list = None, cols: list = None, width: types.SIZE_TYPE = (100, '%'),
             height: types.SIZE_TYPE = (None, 'px'), html_code: str = None,
             helper: str = None, options: types.OPTION_TYPE = None, profile: types.PROFILE_TYPE = False):
    """ Create an HTML Pivot table.

    :tags:
    :categories:

    Usage::

    Related Pages:

      https://pivottable.js.org/examples/
      https://react-pivottable.js.org/
      https://jsfiddle.net/nicolaskruchten/w86bgq9o/

    :param records:
    :param rows:
    :param cols:
    :param width: Optional. The width of the component in the page, default (100, '%')
    :param height: Optional. The height of the component in the page, default (330, "px")
    :param html_code: Optional. An identifier for this component (on both Python and Javascript side)
    :param helper: Optional. Display a tooltip info component
    :param options: Optional. Specific Python options available for this component
    :param profile: Optional. A flag to set the component performance storage
    """
    width = Arguments.size(width, unit="%")
    height = Arguments.size(height, unit="px")
    table = html_tables.HtmlTablePivot.PivotUITable(
      self.page, records, rows, cols, width, height, html_code, helper, options, profile)
    table.renderers.plotly.bar()
    return table
