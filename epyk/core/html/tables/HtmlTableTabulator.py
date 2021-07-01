#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.html import Html

from epyk.core.js.html import JsHtmlTabulator
from epyk.core.js.packages import JsTabulator
from epyk.core.html.options import OptTableTabulator

# The list of CSS classes
from epyk.core.css.styles import GrpClsTable


class Table(Html.Html):
  requirements = ('tabulator-tables', )
  name = 'Tabulator Table'
  _option_cls = OptTableTabulator.TableConfig

  def __init__(self, report, records, width, height, html_code, options, profile):
    data, columns, self._json_config = [], [], {}
    print(options)
    super(Table, self).__init__(report, [], html_code=html_code, profile=profile, options=options,
                                css_attrs={"width": width, "height": height})
    if records is not None:
      self.options.data = records
    self.style.css.background = None

  @property
  def cell(self):
    """
    Description:
    ------------

    """
    return JsHtmlTabulator.JsHtmlTabulatorCell(self.tableId, self.page)

  @property
  def style(self):
    """
    Description:
    ------------
    Property to the CSS Style of the component.

    :rtype: GrpClsTable.Tabulator
    """
    if self._styleObj is None:
      self._styleObj = GrpClsTable.Tabulator(self)
    return self._styleObj

  @property
  def dom(self):
    """
    Description:
    -----------
    HTML Dom object.

    :rtype: JsHtml.JsHtmlButton
    """
    if self._dom is None:
      self._dom = JsHtmlTabulator.JsHtmlTabulator(self, report=self._report)
    return self._dom

  @property
  def tableId(self):
    """
    Description:
    ------------
    Return the Javascript variable of the chart.
    """
    return "%s_obj" % self.htmlCode

  @property
  def options(self):
    """
    Description:
    ------------
    Tabulator table options.

    :rtype: TableConfig
    """
    return super().options

  @property
  @Html.deprecated("use self.options instead")
  def config(self):
    """
    Description:
    ------------

    :rtype: TableConfig
    """
    return self.options

  @property
  def js(self):
    """
    Description:
    ------------
    Return the Javascript internal object.

    :return: A Javascript object

    :rtype: JsTabulator.Tabulator
    """
    if self._js is None:
      self._js = JsTabulator.Tabulator(self.page, selector=self.tableId, setVar=False, parent=self)
    return self._js

  def data(self, data):
    """
    Description:
    ------------

    :param data:
    """
    self.options.data = data

  def add_column(self, field, title=None):
    """
    Description:
    ------------
    Add new column to the underlying Tabulator object.

    Attributes:
    ----------
    :param field: String. Mandatory. The key in the row.
    :param title: String. Optional. The title for the column. Default to the field.
    """
    return self.options.add_column(field, title)

  def get_column(self, by_field=None, by_title=None):
    """
    Description:
    ------------
    Get the column from the underlying Tabulator object by field or by title.
    Pointing by field is recommended as the title might change quite easily.

    Attributes:
    ----------
    :param by_field: String. Optional. The field reference for the column.
    :param by_title: String. Optional. The title reference for the column.

    :rtype: Column
    """
    return self.options.get_column(by_field, by_title)

  def get_columns(self):
    """
    Description:
    ------------
    Get a generator with all the columns defined for the table on the Python side.
    """
    for c in self.options.columns:
      yield c

  def headers(self, colsDef):
    """
    Description:
    ------------
    Update the header definition thanks to a static configuration.

    Attributes:
    ----------
    :param colsDef: Dictionary. The header definition.
    """
    for c in self.options.columns:
      if c.field is not None and c.field in colsDef:
        c.js_tree.update(colsDef[c.field])

  def click(self, js_funcs, profile=None, source_event=None, on_ready=False):
    """
    Description:
    ------------
    Use a rowClick event as underlying click event.

    Use the function row.getData() to make the data available.

    Attributes:
    ----------
    :param js_funcs:
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param source_event:
    :param on_ready:
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    self.options.rowClick(["var data = row.getData()"] + js_funcs)
    return self

  def build(self, data=None, options=None, profile=None, component_id=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param data: String. A String corresponding to a JavaScript object.
    :param options: Dictionary. Optional. Specific Python options available for this component.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    :param component_id: String. Optional.
    """
    if data:
      return self.js.setData(data)

    return 'var %(tableId)s = new Tabulator("#%(htmlCode)s", Object.assign(%(config)s, %(options)s))' % {
      "tableId": self.tableId, "htmlCode": self.htmlCode, "config": self._json_config,
      "options": self.options.config_js(options)}

  def extendModule(self, category, type, func_name, func_def):
    """
    Description:
    ------------
    Tabulator is built in a modular fashion with a core codebase providing basic table rendering functionality and a
    series of modules that provide all of its wonderfull features.

    All of the available modules are installed by default to ensure that you can provide your users with the richest
    experience possible with minimal setup.

    Related Pages:
      http://tabulator.info/docs/4.0/modules
      http://tabulator.info/docs/4.2/modules#module-keybindings

    Attributes:
    ----------
    :param category: String. The name of the module. e.g format.
    :param type: String. The name of the property you want to extend. e.g. formatters.
    :param func_name: String. The alias of teh function to be added to the registery.
    :param func_def: String. The function definition to be attached to this fncName.
    """
    self.page.properties.js.add_builders('Tabulator.prototype.extendModule("%s", "%s", {"%s": %s});' % (
      category, type, func_name, func_def))
    return self

  def loading(self, status=True):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param status:
    """
    if status:
      return ''' 
        if (typeof window['popup_loading_%(htmlId)s'] === 'undefined'){
          var divLoading = document.createElement("div"); 
          window['popup_loading_%(htmlId)s'] = divLoading; 
          divLoading.style.width = '100%%'; divLoading.style.height = '100%%'; divLoading.style.background = '%(background)s';
          divLoading.style.position = 'absolute'; divLoading.style.top = 0; divLoading.style.left = 0; divLoading.style.zIndex = 200;
          divLoading.style.color = '%(color)s'; divLoading.style.textAlign = 'center'; divLoading.style.paddingTop = '50vh';
          divLoading.innerHTML = "<div style='font-size:50px'><i class='fas fa-spinner fa-spin' style='margin-right:10px'></i>Loading...</div>";
          document.getElementById('%(htmlId)s').appendChild(divLoading)
        } ''' % {"htmlId": self.htmlCode, 'color': self.page.theme.success[1], 'background': self.page.theme.greys[0]}

    return '''
      if (typeof window['popup_loading_%(htmlId)s'] !== 'undefined'){
        document.getElementById('%(htmlId)s').removeChild(window['popup_loading_%(htmlId)s']); 
        window['popup_loading_%(htmlId)s'] = undefined}''' % {"htmlId": self.htmlCode}

  def __str__(self):
    self.page.properties.js.add_builders(self.refresh())
    return "<div %s></div>" % (self.get_attrs(pyClassNames=self.style.get_classes()))


class TableTree(Table):
  _option_cls = OptTableTabulator.TableTreeConfig

  def __init__(self, report, records, width, height, html_code, options, profile):
    data, columns, self._json_config = [], [], {}
    super(TableTree, self).__init__(report, records, width, height, html_code, options, profile)
    if records is not None:
      self.options.data = records
    self.style.css.background = None

  @property
  @Html.deprecated("use self.options instead")
  def config(self):
    """
    Description:
    ------------

    :rtype: TableTreeConfig
    """
    return self.options

  @property
  def options(self):
    """
    Description:
    ------------
    Tabulator table options.

    :rtype: TableTreeConfig
    """
    return super().options
