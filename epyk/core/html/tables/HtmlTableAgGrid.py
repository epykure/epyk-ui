#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging

from epyk.core.html import Html
from epyk.core.html.options import OptTableAgGrid

from epyk.core.js.packages import JsAgGrid

# The list of CSS classes
from epyk.core.css.styles import GrpClsTable


class Table(Html.Html):
  name = 'Ag Grid Table'
  requirements = ('ag-grid-community', )
  _option_cls = OptTableAgGrid.TableConfig

  def __init__(self, report, records, width, height, html_code, options, profile):
    data, columns, self.__config = [], [], None
    super(Table, self).__init__(report, [], html_code=html_code, profile=profile, options=options,
                                css_attrs={"width": width, "height": height})
    if records is not None:
      self.options.data = records

  def headers(self, cols_def):
    """
    Description:
    -----------

    Usage::

    Attributes:
    ----------
    :param cols_def:
    """
    for col in self.config['columnDefs']:
      if col['colId'] in cols_def:
        col.update(cols_def[col['colId']])

  @property
  def style(self):
    """
    Description:
    -----------

    Usage::

    :rtype: GrpClsTable.Aggrid
    """
    if self._styleObj is None:
      self._styleObj = GrpClsTable.Aggrid(self)
    return self._styleObj

  @property
  def options(self):
    """
    Description:
    ------------
    Ag Grid table options.

    :rtype: OptTableAgGrid.TableConfig
    """
    return super().options

  @property
  def config(self):
    """
    Description:
    -----------

    Usage::

    :rtype: OptTableAgGrid.TableConfig
    """
    if self.__config is None:
      self.__config = OptTableAgGrid.TableConfig(self._report)
    return self.__config

  @property
  def js(self):
    """
    Description:
    -----------
    Return the Javascript internal object.

    Usage::

    :return: A Javascript object

    :rtype: JsAgGrid.AgGrid
    """
    if self._js is None:
      self._js = JsAgGrid.AgGrid(self._report, selector=self.tableId, setVar=False, parent=self)
    return self._js

  def add_column(self, field, title=None):
    """
    Description:
    -----------

    Usage::

    Attributes:
    ----------
    :param field:
    :param title:
    """
    col_def = self.options.columns
    col_def.field = field
    col_def.colId = field
    col_def.headerName = field if title is None else title
    # col_def.filter = True
    return col_def

  @property
  def tableId(self):
    """
    Description:
    -----------
    Return the Javascript variable of the chart.

    Usage::
    """
    return "%s_obj" % self.htmlCode

  def build(self, data=None, options=None, profile=None, component_id=None):
    """
    Description:
    -----------

    Usage::

    Attributes:
    ----------
    :param data:
    :param options:
    :param profile:
    """
    if data:
      return self.js.setRowData(data)

    return 'var %(tableId)s = %(config)s; new agGrid.Grid(%(htmlCode)s, %(tableId)s)' % {
      'tableId': self.tableId, 'config': self.options.config_js(options), 'htmlCode': component_id or self.dom.varName}

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    return "<div %s></div>" % (self.get_attrs(pyClassNames=self.style.get_classes()))
