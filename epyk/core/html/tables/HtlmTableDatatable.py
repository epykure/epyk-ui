#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.py import primitives
from epyk.core.html import Html
from epyk.core.html.options import OptTableDatatable
from epyk.core.js.packages import JsDatatable
from epyk.core.js import JsUtils

# The list of CSS classes
from epyk.core.css.styles import GrpClsTable


# External DataTable extensions added on demand to add some extra features
# Details of the different extensions are available on the different websites
# https://datatables.net/extensions/
extensions = {
  'rowsGroup': {'jsImports': ['datatables-rows-group']},
}


class Table(Html.Html):
  requirements = ('datatables', )
  name = 'Table'
  _option_cls = OptTableDatatable.TableConfig

  def __init__(self, page: primitives.PageModel, records, width, height, html_code, options, profile):
    data, columns, self.__config = [], [], None
    super(Table, self).__init__(page, [], html_code=html_code, profile=profile, options=options,
                                css_attrs={"width": width, "height": height})
    if records is not None:
      self.options.data = records

  @property
  def style(self) -> GrpClsTable.Datatable:
    """
    Description:
    -----------
    Property to the CSS Style of the component.

    Usage::

    :rtype: GrpClsTable.Datatable
    """
    if self._styleObj is None:
      self._styleObj = GrpClsTable.Datatable(self)
    return self._styleObj

  @property
  def options(self) -> OptTableDatatable.TableConfig:
    """
    Description:
    ------------
    Ag Grid table options.

    :rtype: OptTableDatatable.TableConfig
    """
    return super().options

  @property
  def tableId(self):
    """
    Description:
    -----------
    Return the Javascript variable of the chart.

    Usage::
    """
    return "%s_obj" % self.htmlCode

  def get_column(self, by_title: str):
    """
    Description:
    -----------
    Get the column object from it is title.

    Usage::

    Attributes:
    ----------
    :param str by_title:
    """
    for c in self.options.columns:
      if c.title == by_title:
        return c

  @property
  def js(self) -> JsDatatable.DatatableAPI:
    """
    Description:
    -----------
    Return the Javascript internal object.

    Usage::

    :return: A Javascript object

    :rtype: JsDatatable.DatatableAPI
    """
    if self._js is None:
      self._js = JsDatatable.DatatableAPI(self.page, selector=self.tableId, set_var=False, parent=self)
    return self._js

  def build(self, data=None, options=None, profile=None, component_id=None):
    """
    Description:
    -----------

    Usage::

    Attributes:
    ----------
    :param data: String. A String corresponding to a JavaScript object.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param component_id:
    """
    if data:
      return JsUtils.jsConvertFncs([self.js.clear(), self.js.rows.add(data, update=True)], toStr=True, profile=profile)

    return 'var %s = %s.DataTable(%s)' % (
      self.tableId, component_id or self.dom.jquery.varId, self.options.config_js(options))

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    return "<table %s></table>" % (self.get_attrs(css_class_names=self.style.get_classes()))
