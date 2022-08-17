
import hashlib
import json

from typing import Union, List, Optional
from epyk.core.html.options import Options
from epyk.core.html.options import Enums
from epyk.core.js import JsUtils
from epyk.core.py import types

from epyk.core.html.tables.exts import TbEditors
from epyk.core.html.tables.exts import TbFormatters
from epyk.core.html.tables.exts import TbMutators
from epyk.core.html.tables.exts import TbValidators


class EnumTopCalc(Enums):

  def concat(self):
    """
    Description:
    -----------
    Join all values into one string.

    Related Pages:

      http://tabulator.info/docs/4.0/column-calcs
    """
    return self._set_value()

  def count(self):
    """
    Description:
    -----------
    A count of all non-empty cells in the column.

    Related Pages:

      http://tabulator.info/docs/4.0/column-calcs
    """
    return self._set_value()

  def avg(self, precision: Union[int, bool] = None):
    """
    Description:
    -----------
    The average value of the column.

    Related Pages:

      http://tabulator.info/docs/4.0/column-calcs

    Attributes:
    ----------
    :param precision: The number of decimals to display, setting this value to false will display
      however many decimals are provided with the number
    """
    if precision is not None:
      if self.key == "bottomCalc":
        self._set_value("bottomCalcParams", {"precision": precision})
      else:
        self._set_value("topCalcParams", {"precision": precision})
    return self._set_value()

  def max(self, precision: Union[int, bool] = None):
    """
    Description:
    -----------
    The minimum value in the column.

    Related Pages:

      http://tabulator.info/docs/4.0/column-calcs

    Attributes:
    ----------
    :param precision: The number of decimals to display, setting this value to false will display
      however many decimals are provided with the number
    """
    if precision is not None:
      if self.key == "bottomCalc":
        self._set_value("bottomCalcParams", {"precision": precision})
      else:
        self._set_value("topCalcParams", {"precision": precision})
    return self._set_value()

  def min(self, precision: Union[int, bool] = None):
    """
    Description:
    -----------
    The minimum value in the column.

    Related Pages:

      http://tabulator.info/docs/4.0/column-calcs

    Attributes:
    ----------
    :param precision: The number of decimals to display, setting this value to false will display
      however many decimals are provided with the number
    """
    if precision is not None:
      if self.key == "bottomCalc":
        self._set_value("bottomCalcParams", {"precision": precision})
      else:
        self._set_value("topCalcParams", {"precision": precision})
    return self._set_value()

  def sum(self, precision: Union[int, bool] = None):
    """
    Description:
    -----------
    The minimum value in the column.

    Related Pages:

      http://tabulator.info/docs/4.0/column-calcs

    Attributes:
    ----------
    :param precision: The number of decimals to display, setting this value to false will display
      however many decimals are provided with the number
    """
    if precision is not None:
      if self.key == "bottomCalc":
        self._set_value("bottomCalcParams", {"precision": precision})
      else:
        self._set_value("topCalcParams", {"precision": precision})
    return self._set_value()

  def bespoke(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None):
    return self._set_value(value=JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile), js_type=True)


class EnumLayout(Enums):

  def fitDataStretch(self):
    """
    Description:
    -----------
    The fitDataStretch layout mode functions in the same way as the fitDataFill mode, but instead of stretching the
    empty row to fill the table it stretches the last visible column.

    Related Pages:

      http://tabulator.info/docs/4.5/layout
    """
    return self._set_value()

  def fitColumns(self):
    """
    Description:
    -----------
    As an alternative to the default data fit, you can use the fitColumns layout mode to cause Tabulator to resize
    columns so they fit perfectly in the available table width.

    Related Pages:

      http://tabulator.info/docs/4.5/layout
    """
    return self._set_value()

  def fitData(self):
    """
    Description:
    -----------
    http://tabulator.info/docs/4.1/layout#fittodata.

    Related Pages:

      http://tabulator.info/examples/4.9
    """
    return self._set_value()

  def fitDataTable(self):
    """
    Description:
    -----------
    Tables will automatically resize container and columns to fit the data.

    Related Pages:

      http://tabulator.info/examples/4.9
    """
    return self._set_value()

  def fitDataFill(self, inline: bool = True):
    """
    Description:
    -----------
    The fitDataFill layout mode functions in the same way as the fitData mode, but ensures that rows are always at
    least the full width of the table.

    Related Pages:

      http://tabulator.info/docs/4.5/layout

    Attributes:
    ----------
    :param inline: Optional. Force the CSS display to be inline-block.
    """
    self.component.style.css.width = "auto"
    self.component.style.css.border = "none !IMPORTANT"
    if inline:
      self.component.style.css.display = "inline-block"
    return self._set_value()


class EnumSorter(Enums):

  def string(self):
    """
    Description:
    -----------
    Sorts column as strings of characters.

    Related Pages:

      http://tabulator.info/examples/4.5#sorters
    """
    return self._set_value()

  def number(self):
    """
    Description:
    -----------
    Sorts column as numbers (integer or float, will also handle numbers using "," separators)

    Related Pages:

      http://tabulator.info/examples/4.5#sorters
    """
    return self._set_value()

  def alphanum(self):
    """
    Description:
    -----------
    Sorts column as alpha numeric code.

    Related Pages:

      http://tabulator.info/examples/4.5#sorters
    """
    return self._set_value()

  def boolean(self):
    """
    Description:
    -----------
    Sorts column as booleans.

    Related Pages:

      http://tabulator.info/examples/4.5#sorters
    """
    return self._set_value()

  def date(self):
    """
    Description:
    -----------
    Sorts column as dates.

    Related Pages:

      http://tabulator.info/examples/4.5#sorters
    """
    return self._set_value()

  def time(self):
    """
    Description:
    -----------
    Sorts column as dates

    Related Pages:

      sorts column as times
    """
    return self._set_value()


class EnumColCss(Enums):
  js_conversion = True
  delimiter = " "

  def center(self):
    """
    Description:
    -----------
    CSS Class to center the results.
    """
    self.component.body.style.custom_class({'_attrs': {'text-align': 'center'}}, classname="tb-center")
    return self._add_value(value="tb-center")

  def color(self, color: str):
    """
    Description:
    -----------
    CSS Class to change the font color.

    Attributes:
    ----------
    :param color: The CSS Color.
    """
    self.component.body.style.custom_class({'_attrs': {'color': color}}, classname="tb-color-%s" % color)
    return self._add_value(value="tb-color-%s" % color)

  def background(self, color: str):
    """
    Description:
    -----------
    CSS Class to change the background color.

    Attributes:
    ----------
    :param color: The CSS Color.
    """
    self.component.body.style.custom_class(
      {'_attrs': {'background-color': color}}, classname="tb-background-%s" % color)
    return self._add_value(value="tb-background-%s" % color)

  def name(self, name: str):
    """
    Description:
    -----------
    CSS class for bespoke style.

    Usage::

      page.properties.css.add_text('''.teststyle {background: pink}''')
      c.cssClasses.name("teststyle")

    :param name: The CSS classname
    """
    return self._add_value(value=name)

  def css(self, css_attrs: dict, css_attrs_hover: dict = None, important: bool = False):
    """
    Description:
    -----------
    CSS class for bespoke style.

    Usage::

      col_def.cssClass.css({'background': 'orange'}, {'background': 'white', 'color': 'blue'})

    Attributes:
    ----------
    :param css_attrs: The CSS attributes for the class.
    :param css_attrs_hover: Optional. The CSS Hover attributes for the class.
    :param important: Optional. To set the CSS configuration as important
    """
    has_style = str(hashlib.sha1(str(css_attrs).encode()).hexdigest())
    self.page.body.style.custom_class({
      '_attrs': css_attrs or {}, '_hover': css_attrs_hover or {}}, classname="tb-style-%s" % has_style,
      important=important)
    return self._add_value(value="tb-style-%s" % has_style)


class PersistencePage(Options):

  @property
  def size(self):
    """
    Description:
    -----------
    persist the current page size.

    Related Pages:

      http://tabulator.info/docs/4.5/release#persistence
    """
    return self._config_get()

  @size.setter
  def size(self, val):
    self._config(val)

  @property
  def page(self):
    """
    Description:
    -----------
    do not persist the current page.

    Related Pages:

      http://tabulator.info/docs/4.5/release#persistence
    """
    return self._config_get()

  @page.setter
  def page(self, val):
    self._config(val)


class PersistenceGroup(Options):

  @property
  def groupBy(self):
    """
    Description:
    -----------
    persist only the groupBy setting.
    """
    return self._config_get()

  @groupBy.setter
  def groupBy(self, val: str):
    self._config(val)

  @property
  def groupStartOpen(self):
    """
    Description:
    -----------
    You can set the default open state of groups using the groupStartOpen property.

    Related Pages:

      http://tabulator.info/docs/4.0/group
    """
    return self._config_get()

  @groupStartOpen.setter
  def groupStartOpen(self, val):
    self._config(val)

  @property
  def groupHeader(self):
    """
    Description:
    -----------
    You can also set a different header for each level of group, as above you pass an array to the groupHeader option.

    Related Pages:

      http://tabulator.info/docs/4.0/group
    """
    return self._config_get()

  @groupHeader.setter
  def groupHeader(self, val):
    self._config(val)


class Persistence(Options):

  @property
  def sort(self):
    """
    Description:
    -----------
    You can ensure the data sorting is stored for the next page load by setting the sort property of the persistence
    option to true.

    Related Pages:

      http://tabulator.info/docs/4.5/release#persistence
    """
    return self._config_get()

  @sort.setter
  def sort(self, val):
    self._config(val)

  @property
  def filter(self):
    """
    Description:
    -----------
    You can ensure the data filtering is stored for the next page load by setting the filter property of the
    persistence option to true.

    Related Pages:

      http://tabulator.info/docs/4.5/release#persistence
    """
    return self._config_get()

  @filter.setter
  def filter(self, val):
    self._config(val)

  @property
  def group(self) -> PersistenceGroup:
    """
    Description:
    -----------
    You can ensure the row grouping settings are stored for the next page load by setting the group property of the
    persistence option to true.

    Related Pages:

      http://tabulator.info/docs/4.5/release#persistence
    """
    return self.has_attribute(PersistenceGroup)

  @property
  def page(self) -> PersistencePage:
    """
    Description:
    -----------
    You can ensure the pagination settings are stored for the next page load by setting the page property of the
    persistence option to true.

    Related Pages:

      http://tabulator.info/docs/4.5/release#persistence
    """
    return self.has_attribute(PersistencePage)

  @property
  def columns(self):
    """
    Description:
    -----------
    You can ensure the layout of columns is stored for the next page load by setting the columns property of the
    persistence option to true.

    Related Pages:

      http://tabulator.info/docs/4.5/release#persistence
    """
    return self._config_get()

  @columns.setter
  def columns(self, val):
    self._config(val)


class EditorAutocomplete(Enums):

  def startswith(self, values, showListOnEmpty=True, freetext: bool = True, allowEmpty: bool = True):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param values:
    :param showListOnEmpty: Boolean. Optional.
    :param freetext: Boolean. Optional.
    :param allowEmpty: Boolean. Optional.
    """
    showListOnEmpty = JsUtils.jsConvertData(showListOnEmpty, None)
    freetext = JsUtils.jsConvertData(freetext, None)
    allowEmpty = JsUtils.jsConvertData(allowEmpty, None)
    self._set_value('''{values: %s, searchFunc: function(term, values){ var matches = [];
if (term == ""){return matches}; values.forEach(function(item){if(item.startsWith(term)){matches.push(item);}});
return matches;}, showListOnEmpty: %s, freetext: %s, allowEmpty: %s}''' % (
      values, showListOnEmpty, freetext, allowEmpty), js_type=True)
    return self


class Editor(Enums):

  def input(self, search: bool = True, element_attributes: dict = None, **kwargs):
    """
    Description:
    -----------
    The input editor allows entering of a single line of plain text.

    Related Pages:

      http://tabulator.info/docs/4.5/edit#edit-builtin

    Attributes:
    ----------
    :param search: Optional. Use search type input element with clear button.
    :param element_attributes: Optional. set attributes directly on the input element.
    """
    editor_params = {'search': search}
    if element_attributes is not None:
      editor_params["elementAttributes"] = element_attributes
    if kwargs:
      editor_params.update(kwargs)
    self._set_value(value=editor_params, name="editorParams")
    return self._set_value()

  def textarea(self, vertical_navigation: str = "editor", element_attributes: dict = None, **kwargs):
    """
    Description:
    -----------
    The textarea editor allows entering of multiple lines of plain text.

    Related Pages:

      http://tabulator.info/docs/4.5/edit#edit-builtin

    Attributes:
    ----------
    :param vertical_navigation: Optional. set attributes directly on the textarea element.
    :param element_attributes: Optional. determine how use of the up/down arrow keys will affect the editor.
    :param kwargs: Dictionary with extra attributes
    """
    editor_params = {'verticalNavigation': vertical_navigation, "elementAttributes": element_attributes}
    if kwargs:
      editor_params.update(kwargs)
    self._set_value(value=editor_params, name="editorParams")
    return self._set_value()

  def number(self, min: float = None, max: float = None, step: int = 1, element_attributes: dict = None,
             vertical_navigation: str = "table", **kwargs):
    """
    Description:
    -----------
    The number editor allows for numeric entry with a number type input element with increment and decrement buttons.

    Related Pages:

      http://tabulator.info/docs/4.5/edit#edit-builtin

    Attributes:
    ----------
    :param min: Optional. the maximum allowed value.
    :param max: Optional. the minimum allowed value.
    :param step: Optional. the step size when incrementing/decrementingthe value (default 1).
    :param element_attributes: Optional. set attributes directly on the input element.
    :param vertical_navigation: Optional. determine how use of the up/down arrow keys will affect the editor,
    :param kwargs: Dictionary with extra attributes
    """
    editor_params = {'step': step, 'verticalNavigation': vertical_navigation, "elementAttributes": element_attributes}
    if min is not None:
      editor_params['min'] = min
    if max is not None:
      editor_params['max'] = max
    if kwargs:
      editor_params.update(kwargs)
    self._set_value(value=editor_params, name="editorParams")
    return self._set_value()

  def range(self, min: float = None, max: float = None, step: int = 1, element_attributes: dict = None, **kwargs):
    """
    Description:
    -----------
    The range editor allows for numeric entry with a range type input element.

    Related Pages:

      http://tabulator.info/docs/4.5/edit#edit-builtin

    Attributes:
    ----------
    :param min: Optional. the maximum allowed value.
    :param max: Optional. the minimum allowed value.
    :param step: Optional. the step size when incrementing/decrementingthe value (default 1).
    :param element_attributes: Optional. set attributes directly on the input element.
    :param kwargs: Dictionary with extra attributes
    """
    editor_params = {'step': step, "elementAttributes": element_attributes}
    if min is not None:
      editor_params['min'] = min
    if max is not None:
      editor_params['max'] = max
    if kwargs:
      editor_params.update(kwargs)
    self._set_value(value=editor_params, name="editorParams")
    return self._set_value()

  def tick(self, tristate: bool = False, indeterminate_value: str = None, element_attributes: dict = None, **kwargs):
    """
    Description:
    -----------
    The tick editor allows for boolean values using a checkbox type input element.

    Related Pages:

      http://tabulator.info/docs/4.5/edit#edit-builtin

    Attributes:
    ----------
    :param tristate: Optional. allow tristate tickbox (default false).
    :param indeterminate_value: Optional. when using tristate tickbox what value should the third indeterminate
      state have (default null)
    :param element_attributes: Optional. set attributes directly on the input element
    :param kwargs: Dictionary with extra attributes
    """
    editor_params = {'tristate': tristate, 'indeterminateValue': indeterminate_value}
    if element_attributes is not None:
      editor_params['elementAttributes'] = element_attributes
    if kwargs:
      editor_params.update(kwargs)
    self._set_value(value=editor_params, name="editorParams")
    return self._set_value()

  def stars(self, element_attributes: dict = None, **kwargs):
    """
    Description:
    -----------
    The star editor allows entering of numeric value using a star rating indicator.

    This editor will automatically detect the correct number of stars to use if it is used on the same column as the
    star formatter.

    Related Pages:

      http://tabulator.info/docs/4.5/edit#edit-builtin

    Attributes:
    ----------
    :param element_attributes: Optional set attributes directly on the star holder element.
    :param kwargs: Dictionary with extra attributes
    """
    editor_params = {}
    if element_attributes is not None:
      editor_params['elementAttributes'] = element_attributes
    if kwargs:
      editor_params.update(kwargs)
    self._set_value(value=editor_params, name="editorParams")
    return self._set_value()

  def select(self, values: list = True, default_value: str = None, element_attributes: dict = None,
             vertical_navigation: str = "hybrid", **kwargs):
    """
    Description:
    -----------
    The select editor creates a dropdown select box to allow the user to select from some predefined options passed
    into the values property of the editorParams option.

    Usage::

        c.editors.select(listItemFormatter='function(value, title){return "Mr " + title;}')

    Related Pages:

      http://tabulator.info/docs/4.5/edit#edit-builtin
      http://tabulator.info/docs/5.2/edit#editor-list

    Attributes:
    ----------
    :param values: a list of values to be displayed to the user
    :param default_value: set the value that should be selected by default if the cells value is undefined
    :param element_attributes: set attributes directly on the input element
    :param vertical_navigation: determine how use of the up/down arrow keys will affect the editor,
    :param kwargs: Dictionary with extra attributes
    """
    editor_params = {"values": json.dumps(values) if values is True else values}
    if element_attributes is not None:
      editor_params["elementAttributes"] = element_attributes
    if default_value is not None:
      editor_params["defaultValue"] = default_value
    if vertical_navigation is not None:
      editor_params["verticalNavigation"] = vertical_navigation
    if kwargs:
      editor_params.update(kwargs)
    for c in ["defaultValue", "verticalNavigation"]:
      if c in editor_params:
        editor_params[c] = json.dumps(editor_params[c])
    self._set_value(value="{%s}" % ", ".join([
      "%s: %s" % (k, v) for k, v in editor_params.items()]), name="editorParams", js_type=True)
    return self._set_value()

  def list(self, values: list = True, default_value: str = None, element_attributes: dict = None,
           vertical_navigation: str = "hybrid", **kwargs):
    """
    Description:
    -----------
    The select editor creates a dropdown select box to allow the user to select from some predefined options passed
    into the values property of the editorParams option.

    Usage::

        c.editors.select(listItemFormatter='function(value, title){return "Mr " + title;}')

    Related Pages:

      http://tabulator.info/docs/4.5/edit#edit-builtin
      http://tabulator.info/docs/5.2/edit#editor-list

    Attributes:
    ----------
    :param values: a list of values to be displayed to the user
    :param default_value: set the value that should be selected by default if the cells value is undefined
    :param element_attributes: set attributes directly on the input element
    :param vertical_navigation: determine how use of the up/down arrow keys will affect the editor,
    :param kwargs: Dictionary with extra attributes
    """
    editor_params = {"values": json.dumps(values) if values is True else values}
    if element_attributes is not None:
      editor_params["elementAttributes"] = element_attributes
    if default_value is not None:
      editor_params["defaultValue"] = default_value
    if vertical_navigation is not None:
      editor_params["verticalNavigation"] = vertical_navigation
    if kwargs:
      editor_params.update(kwargs)
    for c in ["defaultValue", "verticalNavigation"]:
      if c in editor_params:
        editor_params[c] = json.dumps(editor_params[c])
    self._set_value(value="{%s}" % ", ".join([
      "%s: %s" % (k, v) for k, v in editor_params.items()]), name="editorParams", js_type=True)
    return self._set_value()

  @property
  def autocompletes(self) -> EditorAutocomplete:
    """
    Description:
    -----------
    Predefined autocomplete configurations.
    """
    self._set_value()
    return EditorAutocomplete(self, "editorParams")

  def autocomplete(self, values: list = True, default_value=None, element_attributes: dict = None,
                   vertical_navigation: str = "hybrid", **kwargs):
    """
    Description:
    -----------
    The autocomplete editor allows users to search a list of predefined options passed into the values property of
    the editorParams option.

    Usage::

      c.editors.autocomplete(listItemFormatter='function(value, title){return "Mr " + title;}', freetext=True)

    Related Pages:

      http://tabulator.info/docs/4.5/edit#edit-builtin

    Attributes:
    ----------
    :param values: a list of values to be displayed to the user
    :param default_value: set the value that should be selected by default if the cells value is undefined
    :param element_attributes: set attributes directly on the input element
    :param vertical_navigation: determine how use of the up/down arrow keys will affect the editor,
    :param kwargs: Dictionary with extra attributes
    """
    editor_params = {"values": json.dumps(values) if values is True else values}
    if element_attributes is not None:
      editor_params["elementAttributes"] = element_attributes
    if default_value is not None:
      editor_params["defaultValue"] = default_value
    if vertical_navigation is not None:
      editor_params["verticalNavigation"] = vertical_navigation
    if kwargs:
      editor_params.update(kwargs)
    for c in ["showListOnEmpty", "freetext", "allowEmpty", "defaultValue", "verticalNavigation"]:
      if c in editor_params:
        editor_params[c] = json.dumps(editor_params[c])
    self._set_value(value="{%s}" % ", ".join([
      "%s: %s" % (k, v) for k, v in editor_params.items()]), name="editorParams", js_type=True)
    return self._set_value()

  def custom(self, func_name: str, js_funcs: types.JS_FUNCS_TYPES = None, editor_params: dict = None,
             profile: types.PROFILE_TYPE = None, func_ref: bool = False):
    """
    Description:
    -----------

    Related Pages:

      http://tabulator.info/docs/4.8/modules

    Attributes:
    ----------
    :param func_name: The function name
    :param js_funcs: Optional. The function definition
    :param editor_params: The editor parameters
    :param profile: Optional. A flag to set the component performance storage
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    if js_funcs is None:
      self._set_value(js_type=True)
    else:
      if not isinstance(js_funcs, list):
        js_funcs = [js_funcs]
      str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
      if not str_func.startswith("function(cell, onRendered, success, cancel, editorParams)") and not func_ref:
        str_func = "function(cell, onRendered, success, cancel, editorParams){%s}" % str_func
      self.component.page.extendModule("edit", "editors", func_name, str_func)
      self._set_value()
    if editor_params is not None:
      self._set_value(value=editor_params, name="editorParams")
    return self


class Formattors(Enums):

  def rowSelection(self, title_formatter: bool = True, title_formatter_params: dict = None,
                   hoz_align: Optional[str] = "center", header_sort: bool = False, **kwargs):
    """
    Description:
    -----------

    Usage::

      table = page.ui.tables.tabulators.table(rows=["row", "values"], cols=["ticks"])
      for c in table.get_columns():
        if c.field == "ticks":
          c.formatters.rowSelection(width=20)

    Attributes:
    ----------
    :param title_formatter: title formatter
    :param title_formatter_params: title formatter parameters
    :param hoz_align: To set the horizontal alignment
    :param header_sort: Flag to special the sort
    :param kwargs: Other attributes to be set for the column
    """
    self._set_value()
    if title_formatter:
      self._set_value("titleFormatter", value="rowSelection")
    if title_formatter_params is not None:
      self._set_value("titleFormatterParams", value=title_formatter_params)
    if hoz_align is not None:
      self._set_value(name="hozAlign", value=hoz_align)
    self._set_value(name="headerSort", value=json.dumps(header_sort), js_type=True)
    for k, v in kwargs.items():
      self._set_value(k, value=v)

  def text(self, **kwargs):
    """
    Description:
    -----------
    The plaintext formatter is the default formatter for all cells and will simply display the value of the cell
    as text.

    Related Pages:

      http://tabulator.info/docs/4.1/format

    Attributes:
    ----------
    :param kwargs:
    """
    self._set_value(value="plaintext")
    if kwargs:
      self._set_value("%sParams" % self.key, kwargs)
    return self

  def textarea(self, **kwargs):
    """
    Description:
    -----------
    The textarea formatter shows text with carriage returns intact (great for multiline text), this formatter will also
    adjust the height of rows to fit the cells contents when columns are resized.

    Related Pages:

      http://tabulator.info/docs/4.1/format

    Attributes:
    ----------
    :param kwargs:
    """
    self._set_value(value="textarea")
    if kwargs:
      self._set_value("%sParams" % self.key, kwargs)
    return self

  def html(self, **kwargs):
    """
    Description:
    -----------
    The html formater displays un-sanitized html.

    Related Pages:

      http://tabulator.info/docs/4.1/format

    Attributes:
    ----------
    :param kwargs:
    """
    self._set_value()
    if kwargs:
      self._set_value("%sParams" % self.key, kwargs)
    return self

  def money(self, decimal: str = ",", thousand: str = ".", precision: bool = False, symbol: str = None,
            symbolAfter=None, **kwargs):
    """
    Description:
    -----------
    The money formatter formats a number into currency notation (eg. 1234567.8901 -> 1,234,567.89).

    Related Pages:

      http://tabulator.info/docs/4.1/format

    Attributes:
    ----------
    :param decimal: Symbol to represent the decimal point (default ".")
    :param thousand: Symbol to represent the thousands separator (default ",")
    :param precision: the number of decimals to display (default is 2), setting this value to false will display
      however many decimals are provided with the number
    :param symbol: currency symbol (no default)
    :param symbolAfter: position the symbol after the number (default false)
    :param kwargs:
    """
    self._set_value("%sParams" % self.key, "money")
    if kwargs:
      self._set_value("%sParams" % self.key, kwargs)
    return self

  def image(self, height=None, width=None, **kwargs):
    """
    Description:
    -----------
    The image formatter creates an img element with the src set as the value. (triggers the normalizeHeight function on
    the row on image load).

    Related Pages:

      http://tabulator.info/docs/4.1/format

    Attributes:
    ----------
    :param height: Tuple. Optional. A CSS value for the height of the image.
    :param width: Tuple. Optional. A CSS value for the width of the image.
    :param kwargs:
    """
    self._set_value()
    format_params = {}
    if height is not None:
      format_params['height'] = height
    if width is not None:
      format_params['width'] = width
    for k, v in kwargs.items():
      format_params[k] = v
    self._set_value("%sParams" % self.key, format_params)
    return self

  def link(self, label: str = None, url: str = None, target: str = '_blank', url_prefix: str = None,
           label_field: str = None, url_field: str = None, **kwargs):
    """
    Description:
    -----------
    The link formatter renders data as an anchor with a link to the given value (by default the value will be used as
    both the url and the label of the tag).

    Related Pages:

      http://tabulator.info/docs/4.1/format

    Attributes:
    ----------
    :param label: a string representing the label, or a function which must return the string for the label,
      the function is passed the Cell Component as its first argument
    :param url:  a string representing the url, or a function which must return the string for the url,
      the function is passed the Cell Component as its first argument
    :param target: a string representing the value of the anchor tags target artibute (eg. set to "_blank"
      to open link in new tab)
    :param url_prefix: a prefix to put before the url value (eg. to turn a emaill address into a clickable
      mailto link you should set this to "mailto:")
    :param label_field: the field in the row data that should be used for the link lable
    :param url_field: the field in the row data that should be used for the link url
    :param kwargs:
    """
    format_params = {k: v for k, v in locals().items() if k != 'self' and v is not None}
    format_params.update(format_params.pop('kwargs'))
    self._set_value()
    self._set_value("%sParams" % self.key, format_params)
    return self

  def datetime(self, input_format: str = "YYYY-MM-DD", output_format: str = "YYYY-MM-DD",
               invalid_placeholder: str = "(invalid date)", **kwargs):
    """
    Description:
    -----------
    The datetime formatter transforms on format of date or time into another.

    Related Pages:

      http://tabulator.info/docs/4.1/format

    Attributes:
    ----------
    :param input_format:
    :param output_format:
    :param invalid_placeholder:
    :param kwargs:
    """
    self._set_value()
    format_params = {
      "inputFormat": input_format, "outputFormat": output_format, "invalidPlaceholder": invalid_placeholder}
    if kwargs:
      format_params.update(kwargs)
    self._set_value("%sParams" % self.key, format_params)
    return self

  def tickcross(self, allow_empty: bool = True, allow_truthy: bool = True,
                tick_element: str = "<i class='fa fa-check'></i>", cross_element: str = "<i class='fa fa-times'></i>",
                **kwargs):
    """
    Description:
    -----------
    The tickCross formatter displays a green tick if the value is (true|'true'|'True'|1) and a red cross if not.

    Related Pages:

      http://tabulator.info/docs/4.1/format

    Attributes:
    ----------
    :param allow_empty: set to true to cause empty values (undefined, null, "") to display an empty
      cell instead of a cross (default false)
    :param allow_truthy: set to true to allow any truthy value to show a tick (default false)
    :param tick_element: custom HTML for the tick element,
      if set to false the tick element will not be shown (it will only show crosses)
    :param cross_element: custom HTML for the cross element,
      if set to false the cross element will not be shown (it will only show ticks)
    :param kwargs: Extra parameters to be added to this formatter
    """
    self._set_value(value="tickCross")
    format_params = {
      'allowEmpty': allow_empty, 'allowTruthy': allow_truthy, 'tickElement': tick_element,
      'crossElement': cross_element}
    if kwargs:
      format_params.update(kwargs)
    self._set_value("%sParams" % self.key, format_params)
    return self

  def color(self, **kwargs):
    """
    Description:
    -----------
    The color formatter sets the background colour of the cell to the value. The cell's value can be any valid
    CSS color eg. #ff0000, #f00, rgb(255,0,0), red, rgba(255,0,0,0), hsl(0, 100%, 50%)

    Related Pages:

      http://tabulator.info/docs/4.1/format
    """
    self._set_value()
    if kwargs:
      self._set_value("%sParams" % self.key, kwargs)
    return self

  def star(self, starts, **kwargs):
    """
    Description:
    -----------
    The star formatter displays a graphical star rating based on integer values.

    Related Pages:

      http://tabulator.info/docs/4.1/format

    Attributes:
    ----------
    :param starts: Number. maximum number of stars to be displayed (default 5).
    """
    self._set_value()
    format_params = {"starts": starts}
    for k, v in kwargs.items():
      format_params[k] = v
    self._set_value("%sParams" % self.key, format_params)
    return self

  def progress(self, min=0, max=100, color=None, legend=None, legendColor=None, legendAlign=None, **kwargs):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param min:
    :param max:
    :param color:
    :param legend:
    :param legendColor:
    :param legendAlign:
    :param kwargs:
    """
    self._set_value()
    if kwargs:
      self._set_value("%sParams" % self.key, kwargs)
    return self

  def lookup(self, data: dict, **kwargs):
    """
    Description:
    -----------
    The lookup formatter looks up the value to display from a object passed into the formatterParams property,
    if not present it displays the current cell value

    Related Pages:

      http://tabulator.info/docs/4.1/format

    Attributes:
    ----------
    :param data: Dictionary for the lookup.
    :param kwargs:
    """
    self._set_value()
    format_params = data
    if kwargs:
      format_params.update(kwargs)
    self._set_value("%sParams" % self.key, format_params)
    return self

  def custom(self, func_name: str, js_funcs: types.JS_FUNCS_TYPES = None, formatter_params: dict = None,
             profile: types.PROFILE_TYPE = None, func_ref: bool = False):
    """
    Description:
    -----------

    Related Pages:

      http://tabulator.info/docs/4.0/modules

    Attributes:
    ----------
    :param func_name: The function name
    :param js_funcs: Optional. The function definition
    :param formatter_params: Formatter attributes
    :param profile: Optional. A flag to set the component performance storage
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    if js_funcs is None:
      self._set_value(func_name, js_type=True)
    else:
      if not isinstance(js_funcs, list):
        js_funcs = [js_funcs]
      str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
      if not str_func.startswith("function(cell, formatterParams)") and not func_ref:
        str_func = "function(cell, formatterParams){%s}" % str_func
      self.component.extendModule("format", "formatters", func_name, str_func)
      self._set_value(value=func_name)
    if formatter_params is not None:
      self._set_value("%sParams" % self.key, formatter_params)
    return self

  def css(self, attrs: dict):
    self.component.extendModule("format", "formatters", "FormatterPureCss", '''function(cell, formatterParams){   
Object.keys(formatterParams.css).forEach(function(key){cell.getElement().style[key] = formatterParams.css[key] 
}); return cell.getValue();}''')
    self._set_value(value="FormatterPureCss")
    self._set_value("%sParams" % self.key, {"css": attrs})
    return self

  def wrapper(self, formatter: str, css_attrs: dict, formatter_params: dict = None):
    """
    Description:
    -----------

    Usage::

      .formatters.wrapper("progress", {"height": '6px'}, {'color': ['orange', 'green']})

    Related Pages:

      http://tabulator.info/docs/4.0/modules

    Attributes:
    ----------
    :param formatter:
    :param css_attrs:
    :param formatter_params:
    """
    self._set_value(value='''
function(cell, formatterParams){const cssAttrs = formatterParams.css;
  var cell = cell.getTable().modules.format.getFormatter('%s').call(cell.getTable().modules.format, cell, formatterParams);
  let frag = document.createRange().createContextualFragment(cell).firstChild;
  Object.keys(cssAttrs).forEach(function(key){frag.style[key] = cssAttrs[key]}); 
  return frag; }''' % formatter, js_type=True)
    formatter_params = formatter_params or {}
    formatter_params['css'] = css_attrs
    self._set_value("%sParams" % self.key, formatter_params)
    return self


class Mutators(Enums):

  def bespoke(self, func_name: str, js_funcs: types.JS_FUNCS_TYPES = None, profile: types.PROFILE_TYPE = None):
    """
    Description:
    -----------
    he mutator module allows for manipulation of data as it is entered into Tabulator.

    More information on these functions can be found in the Mutators Documentation.

    Related Pages:

      http://tabulator.info/docs/4.8/mutators

    Attributes:
    ----------
    :param func_name: Javascript functions name
    :param js_funcs: Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    """
    if js_funcs is None:
      self._set_value(func_name, js_type=True)
    else:
      if not isinstance(js_funcs, list):
        js_funcs = [js_funcs]
      self.component.extendModule(
        "mutator", "mutators", func_name,
        "function(value, data, type, mutatorParams, component){%s}" % JsUtils.jsConvertFncs(
          js_funcs, toStr=True, profile=profile))
      self._set_value(func_name)
    return self


class Accessors(Enums):

  def bespoke(self, func_name: str, js_funcs: types.JS_FUNCS_TYPES = None, accessor_params: dict = None,
              profile: types.PROFILE_TYPE = None):
    """
    Description:
    -----------
    Accessors are used to alter data as it is extracted from the table, through commands, the clipboard, or download.

    You can set accessors on a per column basis using the accessor option in the column definition object.

    You can pass an optional additional parameter with accessor, accessorParams that should contain an object with
    additional information for configuring the accessor.

    Related Pages:

      http://tabulator.info/docs/4.8/mutators#accessors

    Attributes:
    ----------
    :param func_name: Javascript functions name
    :param js_funcs: Javascript function
    :param accessor_params: Accessor parameters
    :param profile: Optional. A flag to set the component performance storage
    """
    if js_funcs is None:
      self._set_value(func_name, js_type=True)
    else:
      if not isinstance(js_funcs, list):
        js_funcs = [js_funcs]
      self.component.extendModule(
        "accessor", "accessors", func_name,
        "function(value, data, type, params, column, row){%s}" % JsUtils.jsConvertFncs(
          js_funcs, toStr=True, profile=profile))
      self._set_value(func_name)
    if accessor_params is not None:
      self._set_value("accessorParams", accessor_params)
    return self


class Validators(Enums):

  def required(self):
    """
    Description:
    -----------
    The required validator allows values that are not null or an empty string

    Related Pages:

      http://tabulator.info/docs/4.5/validate
    """
    self._add_value()
    return self

  def unique(self):
    """
    Description:
    -----------
    The unique validator allows values that do not match the value of any other cell in this column

    Related Pages:

      http://tabulator.info/docs/4.5/validate
    """
    self._add_value()
    return self

  def integer(self):
    """
    Description:
    -----------
    The integer validator allows values that are valid integers

    Related Pages:

      http://tabulator.info/docs/4.5/validate
    """
    self._add_value()
    return self

  def float(self):
    """
    Description:
    -----------
    The float validator allows values that are valid floats.

    Related Pages:

      http://tabulator.info/docs/4.5/validate
    """
    self._add_value()
    return self

  def numeric(self):
    """
    Description:
    -----------
    The float validator allows values that are valid floats.

    Related Pages:

      http://tabulator.info/docs/4.5/validate
    """
    self._add_value()
    return self

  def min(self, val):
    """
    Description:
    -----------
    The min validator allows numeric values that are greater than or equal to parameter.

    Related Pages:

      http://tabulator.info/docs/4.5/validate
    """
    self._add_value(value='min:%s' % val)
    return self

  def max(self, val):
    """
    Description:
    -----------
    The max validator allows numeric values that are less than or equal to parameter.

    Related Pages:

      http://tabulator.info/docs/4.5/validate
    """
    self._add_value(value='max:%s' % val)
    return self

  def maxLength(self, val):
    """
    Description:
    -----------
    The maxLength validator allows string values that have a length less than or equal to parameter.

    Related Pages:

      http://tabulator.info/docs/4.5/validate
    """
    self._add_value(value='maxLength:%s' % val)
    return self

  def list(self, vals: list):
    """
    Description:
    -----------
    The in validator allows that values that match a value from the | delimited string in the parameter.

    Related Pages:

      http://tabulator.info/docs/4.5/validate
    """
    self._add_value(value='in:%s' % "".join(map(lambda x: str(x), vals)))
    return self

  def regex(self, val: str):
    """
    Description:
    -----------
    The regex validator allows values that match the supplied regex.

    Related Pages:

      http://tabulator.info/docs/4.5/validate
    """
    self._add_value(value='regex:%s' % val)
    return self


class Extensions(Options):

  def __init__(self, options: Options, attrs: dict):
    super(Extensions, self).__init__(options.component, attrs)
    self.__options = options

  @property
  def editors(self) -> TbEditors.ExtsEditors:
    """
    Description:
    -----------
    The edit module allows the user to change data in cells, header filters are also dependant on this module.

    More information on these functions can be found in the Editing Data Documentation.

    Related Pages:

      http://tabulator.info/docs/4.0/modules
    """
    return TbEditors.ExtsEditors(self.__options, "editor")

  @property
  def formatters(self) -> TbFormatters.ExtsFormattors:
    """
    Description:
    -----------
    You can set cell formatters on a per column basis using the formatter option in the column definition object.

    You can pass an optional additional parameter with the formatter, formatterParams that should contain an object
    with additional information for configuring the formatter.

    Related Pages:

      http://tabulator.info/docs/4.0/format
    """
    return TbFormatters.ExtsFormattors(self.__options, "formatter")

  @property
  def mutators(self) -> TbMutators.ExtsMutators:
    """
    Description:
    -----------
    Mutators are used to alter data as it is parsed into Tabulator.
    For example if you wanted to convert a numeric column into a boolean based on its value, before the data is used
    to build the table.

    Related Pages:

      http://tabulator.info/docs/4.0/mutators
    """
    return TbMutators.ExtsMutators(self.__options, "mutator")

  @property
  def validators(self) -> TbValidators.ExtsValidators:
    """
    Description:
    -----------
    The validate module allows for validation of edited data before it is stored in the table.
    More information on these functions can be found in the Validation Documentation.
    This can be extended to add custom validator functions to the default list:

    Related Pages:

      http://tabulator.info/docs/4.0/modules
    """
    return TbValidators.ExtsValidators(self.__options, "validator")


class HeaderMenu(Options):

  def hide(self, label: str = "Hide Column", icon: str = "fas fa-eye-slash", disabled: bool = False):
    """
    Description:
    -----------
    Hide the selected column.

    Attributes:
    ----------
    :param label:
    :param icon:
    :param disabled:
    """
    if icon is not None:
      self._attrs['<i class="%s" style="margin-right:5px"></i>%s' % (icon, label)] = "column.hide()"
    else:
      self._attrs[label] = "column.hide()"
    return self

  def separator(self):
    self._attrs["separator_%s" % len(self._attrs)] = None
    return self

  def custom(self, label: str, func: str, icon: str = None, disabled: bool = False):
    """
    Description:
    -----------
    Add a delete entry to the context menu.

    Attributes:
    ----------
    :param label:
    :param func: JavaScript expression or entire function starting with function(e, column){
    :param icon:
    :param disabled:
    """
    if not func.startswith("function("):
      func = "function(e, column){%s}" % func
    if icon is not None:
      self._attrs['<i class="%s" style="margin-right:5px"></i>%s' % (icon, label)] = func
    else:
      self._attrs[label] = func
    return self

  def __str__(self):
    result = []
    for k, v in self._attrs.items():
      if v is None and k.startswith("separator_"):
        result.append("{'separator': true}")
      else:
        result.append("{label: '%s', action: %s}" % (k, v))
    return ", ".join(result)


class Column(Options):

  @property
  def align(self):
    """
    Description:
    -----------
    sets the text alignment for this column (left|center|right)

    Related Pages:

      http://tabulator.info/docs/4.5/columns
    """
    return self._config_get(name="hozAlign")

  @align.setter
  def align(self, val: str):
    self._config(val, name="hozAlign")

  @property
  def accessors(self) -> Accessors:
    """
    Description:
    -----------
    Accessors are used to alter data as it is extracted from the table, through commands, the clipboard, or download.

    You can set accessors on a per column basis using the accessor option in the column definition object.

    Related Pages:

      http://tabulator.info/docs/4.8/mutators#accessors
    """
    return Accessors(self, "accessor")

  def add_column(self, field: str, title: str = None):
    """
    Description:
    ------------
    Add new column to the underlying Tabulator object.

    Attributes:
    ----------
    :param field: String. Mandatory. The key in the row.
    :param title: String. Optional. The title for the column. Default to the field.
    """
    col_def = self._config_sub_data_enum("columns", Column)
    col_def.field = field
    col_def.title = field if title is None else title
    return col_def

  def cellClick(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, func_ref: bool = False):
    """
    Description:
    -----------

    Related Pages:

    Attributes:
    ----------
    :param js_funcs: The Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function(event, cell)") and not func_ref:
      str_func = "function(event, cell){%s}" % str_func
    self._config(str_func, js_type=True)

  def cellEditing(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, func_ref: bool = False):
    """
    Description:
    -----------

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks

    Attributes:
    ----------
    :param js_funcs: The Javascript functions.
    :param profile: Optional. A flag to set the component performance storage
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function(cell)") and not func_ref:
      str_func = "function(cell){let value = cell.getValue(); let data = cell.getRow().getData(); %s}" % str_func
    self._config(str_func, js_type=True)
    return self

  def cellEdited(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, func_ref: bool = False):
    """
    Description:
    -----------

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks

    Attributes:
    ----------
    :param js_funcs: The Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function(cell)") and not func_ref:
      str_func = "function(cell){let value = cell.getValue(); let data = cell.getRow().getData(); %s}" % str_func
    self._config(str_func, js_type=True)
    return self

  @property
  def cssClass(self):
    """
    Description:
    -----------
    sets css classes on header and cells in this column.
    (value should be a string containing space separated class names).

    Related Pages:

      http://tabulator.info/docs/5.2/columns#main-contents
    """
    return self._config_get()

  @cssClass.setter
  def cssClass(self, text: str):
    self._config(text)

  @property
  def cssClasses(self) -> EnumColCss:
    """
    Description:
    -----------
    sets css classes on header and cells in this column.
    (value should be a string containing space separated class names)

    Related Pages:

      http://tabulator.info/docs/5.2/columns#main-contents
    """
    return self.has_attribute(EnumColCss, name="cssClass")

  @property
  def editable(self):
    """
    Description:
    -----------
    callback to check if the cell is editable (see Manipulating Data for more details).
    This does not support function, use editable_check() otherwise.

    Related Pages:

      http://tabulator.info/docs/4.5/columns
    """
    return self._config_get()

  @editable.setter
  def editable(self, val: bool):
    self._config(val)

  def editable_check(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, func_ref: bool = False):
    """
    Description:
    -----------
    This lets you set a callback that is executed before the editor is built, if this callback returns true the editor
    is added, if it returns false the edit is aborted and the cell remains a non-editable cell.

    Usage::

        page.js.customText("function MyCell(cell){var data = cell.getRow().getData(); return data.iata  == 'ORD' }")

        for c in table.get_columns():
          c.editor = "input"
          c.editable_check("MyCell", func_ref=True)

    Related Pages:

      http://tabulator.info/docs/4.0/edit

    Attributes:
    ----------
    :param js_funcs: Javascript functions or entire function e.g: function customHeaderFilter(headerValue, rowValue,
      rowData, filterParams)
    :param profile: Optional. A flag to set the component performance storage
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function ") and not func_ref:
      str_func = "function (cell){%s}" % str_func
    self._config(str_func, name="editable", js_type=True)

  @property
  def editableTitle(self):
    """
    Description:
    -----------
    Allows the user to edit the header titles.

    Related Pages:

      http://tabulator.info/docs/4.1/columns
    """
    return self._config_get()

  @editableTitle.setter
  def editableTitle(self, flag: bool):
    self._config(flag)

  @property
  def exts(self):
    """
    Description:
    -----------
    Tabulator is built in a modular fashion with a core codebase providing basic table rendering functionality and a
    series of modules that provide all of its wonderful features.

    Related Pages:

      http://tabulator.info/docs/4.0/modules
    """
    return Extensions(self, self._attrs)

  @property
  def editor(self):
    """
    Description:
    -----------
    Tabulator comes with a number of built-in editors including:

    Related Pages:

      http://tabulator.info/docs/5.2/edit#edit-builtin
    """
    return self._config_get()

  @editor.setter
  def editor(self, val: str):
    self._config(val)

  @property
  def editorParams(self):
    """
    Description:
    -----------
    Tabulator comes with a number of built-in editors including:

    Related Pages:

      http://tabulator.info/docs/5.2/edit#edit-builtin
    """
    return self._config_get()

  @editorParams.setter
  def editorParams(self, values: dict):
    self._config(values)

  @property
  def editors(self):
    """
    Description:
    -----------
    Tabulator comes with a number of built-in editors including:

    Related Pages:

      http://tabulator.info/docs/4.5/edit#edit-builtin
    """
    return Editor(self, "editor")

  @property
  def field(self):
    """
    Description:
    -----------
    Required (not required in icon/button columns) this is the key for this column in the data array.

    Related Pages:

      http://tabulator.info/docs/4.5/columns
    """
    return self._config_get()

  @field.setter
  def field(self, val: str):
    self._config(val)

  @property
  def formatter(self):
    """
    Description:
    -----------
    You can set cell formatters on a per column basis using the formatter option in the column definition object.

    Related Pages:

      http://tabulator.info/docs/5.0/format#format
    """
    return self._config_get()

  @formatter.setter
  def formatter(self, val):
    self._config(val)

  @property
  def formatterParams(self):
    """
    Description:
    -----------
    You can pass an optional additional parameter with the formatter, formatterParams that should contain an object
    with additional information for configuring the formatter.

    Related Pages:

      http://tabulator.info/docs/5.0/format#format
    """
    return self._config_get()

  @formatterParams.setter
  def formatterParams(self, values: dict):
    self._config(values)

  @property
  def formatters(self) -> Formattors:
    """
    Description:
    -----------
    You can set cell formatters on a per column basis using the formatter option in the column definition object.

    Related Pages:

      http://tabulator.info/docs/4.5
    """
    return Formattors(self, "formatter")

  @property
  def frozen(self):
    """
    Description:
    -----------
    freezes the column in place when scrolling (see Frozen Columns for more details).

    Related Pages:

      http://tabulator.info/docs/4.5/columns
    """
    return self._config_get()

  @frozen.setter
  def frozen(self, val: bool):
    self._config(val)

  @property
  def headerMenu(self) -> HeaderMenu:
    """
    Description:
    -----------
    Shortcut property to the headermenu items.

    Related Pages:

      http://tabulator.info/docs/4.6/menu
    """
    return self._config_sub_data_enum("headerMenu", HeaderMenu)

  @property
  def headerFilter(self):
    """
    Description:
    -----------
    User can sort by clicking on the header (see Sorting Data for more detail.

    Related Pages:

      http://tabulator.info/docs/4.1/columns
    """
    return self._config_get()

  @property
  def headerFilterPlaceholder(self):
    """
    Description:
    -----------
    Placeholder text for the header filter (see Header Filtering for more details)

    Related Pages:

      http://tabulator.info/docs/5.2/columns#main-contents
    """
    return self._config_get()

  @headerFilterPlaceholder.setter
  def headerFilterPlaceholder(self, text: str):
    self._config(text)

  @property
  def headerFilterEmptyCheck(self):
    """
    Description:
    -----------
    Function to check when the header filter is empty (see Header Filtering for more details)

    Related Pages:

      http://tabulator.info/docs/5.2/columns#main-contents
    """
    return self._config_get()

  @headerFilterEmptyCheck.setter
  def headerFilterEmptyCheck(self, values: dict):
    self._config(values)

  @headerFilter.setter
  def headerFilter(self, value):
    self._config(value)

  def headerFilterFunc(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
                       func_ref: bool = False):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param js_funcs: Javascript functions or entire function e.g: function customHeaderFilter(headerValue, rowValue,
      rowData, filterParams)
    :param profile: Optional. A flag to set the component performance storage
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function ") and not func_ref:
      str_func = "function customHeaderFilter(headerValue, rowValue, rowData, filterParams){%s}" % str_func
    self._config(str_func, js_type=True)

  @property
  def headerFilterFuncParams(self):
    """
    Description:
    -----------
    Additional parameters object passed to the headerFilterFunc function (see Header Filtering for more details)

    Related Pages:

      http://tabulator.info/docs/5.2/columns#main-contents
    """
    return self._config_get()

  @headerFilterFuncParams.setter
  def headerFilterFuncParams(self, values: dict):
    self._config(values)

  @property
  def headerFilterLiveFilter(self):
    """
    Description:
    -----------
    Disable live filtering of the table (see Header Filtering for more details)

    Related Pages:

      http://tabulator.info/docs/5.2/columns#main-contents
    """
    return self._config_get()

  @headerFilterLiveFilter.setter
  def headerFilterLiveFilter(self, values: dict):
    self._config(values)

  @property
  def headerVertical(self):
    """
    Description:
    -----------
    change the orientation of the column header to vertical (see Vertical Column Headers for more details).

    Related Pages:

      http://tabulator.info/docs/4.5/columns
    """
    return self._config_get()

  @headerVertical.setter
  def headerVertical(self, val):
    self._config(val)

  @property
  def headerSort(self):
    """
    Description:
    -----------
    user can sort by clicking on the header (see Sorting Data for more details).

    Related Pages:

      http://tabulator.info/docs/4.5/columns
    """
    return self._config_get()

  @headerSort.setter
  def headerSort(self, val):
    self._config(val)

  @property
  def headerSortStartingDir(self):
    """
    Description:
    -----------
    Set the starting sort direction when a user first clicks on a header (see Sorting Data for more details)

    Related Pages:

      http://tabulator.info/docs/5.2/columns#header-visibility
    """
    return self._config_get()

  @headerSortStartingDir.setter
  def headerSortStartingDir(self, val: str):
    self._config(val)

  @property
  def headerSortTristate(self):
    """
    Description:
    -----------
    Allow tristate toggling of column header sort direction (see Sorting Data for more details)

    Related Pages:

      http://tabulator.info/docs/5.2/columns#header-visibility
    """
    return self._config_get()

  @headerSortTristate.setter
  def headerSortTristate(self, flag: bool):
    self._config(flag)

  @property
  def headerPopup(self):
    """
    Description:
    -----------
    Add popup button to column header (see Header Popups for more details)

    Related Pages:

      http://tabulator.info/docs/5.2/menu#popup-column
    """
    return self._config_get()

  @headerPopup.setter
  def headerPopup(self, text: str):
    self._config(text)

  @property
  def headerPopupIcon(self):
    """
    Description:
    -----------
    Add popup button to column header (see Header Popups for more details)

    Related Pages:

      http://tabulator.info/docs/5.2/menu#popup-column
    """
    return self._config_get()

  @headerPopupIcon.setter
  def headerPopupIcon(self, text: str):
    self._config(text)

  @property
  def headerContextPopup(self):
    """
    Description:
    -----------
    Add context popup to column header (see Header Context Popups for more details)

    Related Pages:

      http://tabulator.info/docs/5.2/menu#popup-column
    """
    return self._config_get()

  @headerContextPopup.setter
  def headerContextPopup(self, text: str):
    self._config(text)

  @property
  def headerVisible(self):
    """
    Description:
    -----------
    By setting the headerVisible option to false you can hide the column headers and present
    the table as a simple list if needed.

    Related Pages:

      http://tabulator.info/docs/4.5/columns
      http://tabulator.info/docs/5.2/columns#header-visibility
    """
    return self._config_get()

  @headerVisible.setter
  def headerVisible(self, flag: bool):
    self._config(flag)

  @property
  def hozAlign(self):
    """
    Description:
    -----------
    By setting the headerVisible option to false you can hide the column headers and present
    the table as a simple list if needed.

    Related Pages:

      http://tabulator.info/docs/4.5/columns
    """
    return self._config_get()

  @hozAlign.setter
  def hozAlign(self, val):
    self._config(val)

  @property
  def sorter(self) -> EnumSorter:
    """
    Description:
    -----------
    By default Tabulator will attempt to guess which sorter should be applied to a column based on the data contained
    in the first row.

    Related Pages:

      http://tabulator.info/examples/4.5#sorters
    """
    return self._config_sub_data_enum("sorter", EnumSorter)

  @property
  def width(self):
    """
    Description:
    -----------
    sets the width of this column, this can be set in pixels or as a percentage of total table width (if not set the
    system will determine the best)

    Related Pages:

      http://tabulator.info/docs/4.5/columns
    """
    return self._config_get()

  @width.setter
  def width(self, val):
    self._config(val)

  @property
  def minwidth(self):
    """
    Description:
    -----------
    sets the minimum width of this column, this should be set in pixels (this takes priority over the global option
    of columnMinWidth)

    Related Pages:

      http://tabulator.info/docs/4.1/columns
    """
    return self._config_get()

  @minwidth.setter
  def minwidth(self, val):
    self._config(val)

  @property
  def mutators(self):
    """
    Description:
    -----------
    Mutators are used to alter data as it is parsed into Tabulator.

    For example if you wanted to convert a numeric column into a boolean based on its value, before the data is used
    to build the table.

    Related Pages:

        http://tabulator.info/docs/4.8/mutators
    """
    return Mutators(self, "mutator")

  @property
  def widthGrow(self):
    """
    Description:
    -----------
    when using fitColumns layout mode, determines how much the column should grow to fill available
    space (see Table Layout for more details)

    Related Pages:

      http://tabulator.info/docs/4.5/columns
    """
    return self._config_get()

  @widthGrow.setter
  def widthGrow(self, val: int):
    self._config(val)

  @property
  def responsive(self):
    """
    Description:
    -----------
    an integer to determine when the column should be hidden in responsive mode (see Responsive Layout for more details)

    Related Pages:

      http://tabulator.info/docs/4.5/columns
    """
    return self._config_get()

  @responsive.setter
  def responsive(self, val):
    self._config(val)

  @property
  def resizable(self):
    """
    Description:
    -----------
    set whether column can be resized by user dragging its edges (see Table Layout for more details).

    Related Pages:

      http://tabulator.info/docs/4.5/columns
    """
    return self._config_get()

  @resizable.setter
  def resizable(self, val):
    self._config(val)

  @property
  def title(self):
    """
    Description:
    -----------
    Required This is the title that will be displayed in the header for this column.

    Related Pages:

      http://tabulator.info/docs/4.5/columns
    """
    return self._config_get()

  @title.setter
  def title(self, val):
    self._config(val)

  @property
  def tooltip(self):
    """
    Description:
    -----------
    Required This is the title that will be displayed in the header for this column.

    Related Pages:

      http://tabulator.info/docs/4.5/columns
    """
    return self._config_get()

  @tooltip.setter
  def tooltip(self, flag: bool):
    self._config(flag)

  @property
  def titleFormatter(self):
    """
    Description:
    -----------
    formatter function for header title (see Formatting Data for more details).

    Related Pages:

      http://tabulator.info/docs/4.5/columns
    """
    return self._config_get()

  @titleFormatter.setter
  def titleFormatter(self, val):
    self._config(val)

  @property
  def titleFormatterParams(self):
    """
    Description:
    -----------

    Related Pages:

      http://tabulator.info/docs/4.0/format
    """
    return self._config_get()

  @titleFormatterParams.setter
  def titleFormatterParams(self, val: dict):
    self._config(val)

  @property
  def topCalc(self):
    """
    Description:
    -----------
    Column calculations can be used to add a row of calculated values to the top or bottom of your table to display
    information such as the sum of a columns data.

    Related Pages:

      http://tabulator.info/docs/4.0/column-calcs
    """
    return self._config_get()

  @topCalc.setter
  def topCalc(self, val):
    self._config(val)

  @property
  def topCalcFormatter(self):
    """
    Description:
    -----------
    You can apply formatters (see Formatting Data for more information) to any calculation cells, using the
    topCalcFormatter and bottomCalcFormatter options in a columns definition object.

    Related Pages:

      http://tabulator.info/docs/4.0/column-calcs
    """
    return self._config_get()

  @topCalcFormatter.setter
  def topCalcFormatter(self, val):
    self._config(val)

  @property
  def topCalcFormatterParams(self):
    """
    Description:
    -----------
    You can apply formatters (see Formatting Data for more information) to any calculation cells, using the
    topCalcFormatter and bottomCalcFormatter options in a columns definition object.

    Related Pages:

      http://tabulator.info/docs/4.0/column-calcs
    """
    return self._config_get()

  @topCalcFormatterParams.setter
  def topCalcFormatterParams(self, val):
    self._config(val)

  @property
  def topCalcParams(self):
    """
    Description:
    -----------
    The column calculation parameters.

    Related Pages:

      http://tabulator.info/docs/4.0/column-calcs
    """
    return self._config_get()

  @topCalcParams.setter
  def topCalcParams(self, val):
    self._config(val)

  @property
  def topCalcs(self):
    """
    Description:
    -----------
    Column calculations can be used to add a row of calculated values to the top or bottom of your table to display
    information such as the sum of a columns data.

    Related Pages:

      http://tabulator.info/docs/4.0/column-calcs
    """
    return EnumTopCalc(self, "topCalc")

  @property
  def bottomCalc(self):
    """
    Description:
    -----------
    Column calculations can be used to add a row of calculated values to the top or bottom of your table to display
    information such as the sum of a columns data.

    Related Pages:

      http://tabulator.info/docs/4.0/column-calcs
    """
    return self._config_get()

  @bottomCalc.setter
  def bottomCalc(self, val):
    self._config(val)

  @property
  def bottomCalcFormatter(self):
    """
    Description:
    -----------
    You can apply formatters (see Formatting Data for more information) to any calculation cells, using the
    topCalcFormatter and bottomCalcFormatter options in a columns definition object.

    Related Pages:

      http://tabulator.info/docs/4.0/column-calcs
    """
    return self._config_get()

  @bottomCalcFormatter.setter
  def bottomCalcFormatter(self, val):
    self._config(val)

  @property
  def bottomCalcFormatters(self) -> Formattors:
    return Formattors(self, "bottomCalcFormatter")

  @property
  def bottomCalcFormatterParams(self):
    """
    Description:
    -----------
    You can apply formatters (see Formatting Data for more information) to any calculation cells, using the
    topCalcFormatter and bottomCalcFormatter options in a columns definition object.

    Related Pages:

      http://tabulator.info/docs/4.0/column-calcs
    """
    return self._config_get()

  @bottomCalcFormatterParams.setter
  def bottomCalcFormatterParams(self, val):
    self._config(val)

  @property
  def bottomCalcParams(self):
    """
    Description:
    -----------
    The column calculation parameters.

    Related Pages:

      http://tabulator.info/docs/4.0/column-calcs
    """
    return self._config_get()

  @bottomCalcParams.setter
  def bottomCalcParams(self, val):
    self._config(val)

  @property
  def bottomCalcs(self):
    """
    Description:
    -----------
    Column calculations can be used to add a row of calculated values to the top or bottom of your table to display
    information such as the sum of a columns data.

    Related Pages:

      http://tabulator.info/docs/4.0/column-calcs
    """
    return EnumTopCalc(self, "bottomCalc")

  @property
  def validator(self):
    """
    Description:
    -----------
    set the validator to be used to approve data when a user edits a cell. (see Manipulating Data for more details).

    Related Pages:

      http://tabulator.info/docs/4.5/validate
    """
    return Validators(self, "validator")


class ColumnsGroup(Options):

  @property
  def title(self):
    """
    Description:
    -----------
    Set a title for a group of columns.
    """
    return self._config_get()

  @title.setter
  def title(self, val: str):
    self._config(val)

  @property
  def columns(self) -> Column:
    """
    Description:
    -----------
    Add columns to a group.
    """
    return self._config_sub_data_enum("columns", Column)


class Keybindings(Options):

  def addRow(self, keys):
    """
    Description:
    -----------
    Add a keyboard shortcut event on the table to Keycodes can be found using the function ord().

    Related Pages:

      http://tabulator.info/docs/4.4/keybindings

    Attributes:
    ----------
    :param keys: String. The keys to trigger the event.
    """
    self.component.extendModule(
      "keybindings", "actions", "addRow", "function(event){event.preventDefault(); this.table.addRow()}")
    self._attrs["addRow"] = keys
    return self

  def deleteSelectedRows(self, keys):
    """
    Description:
    -----------
    Add a keyboard shortcut event on the table to delete the selected row.

    Keycodes can be found using the function ord()

    Related Pages:

      http://tabulator.info/docs/4.4/keybindings

    Attributes:
    ----------
    :param keys: String. The keys to trigger the event.
    """
    self.component.extendModule(
      "keybindings", "actions", "addRow",
      "function(){var rows = this.table.getSelectedRows(); rows.forEach(function(row){row.delete()})}")
    self._attrs["deleteSelectedRows"] = keys
    return self

  def bespoke(self, keys, func_name, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
              prevent_default: bool = True):
    """
    Description:
    -----------
    Add a keyboard shortcut custom event on the table.

    Keycodes can be found using the function ord()

    Related Pages:

      http://tabulator.info/docs/4.4/keybindings

    Attributes:
    ----------
    :param keys: The keys to trigger the event
    :param func_name: The function name / alias for this event
    :param js_funcs: The function definition of this event
    :param profile: Optional. A flag to set the component performance storage
    :param prevent_default: Optional. Stop the event and do not change the cell in editable.
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    if prevent_default:
      self.component.extendModule(
        "keybindings", "actions", func_name, "function(event){event.preventDefault(); %s}" % JsUtils.jsConvertFncs(
          js_funcs, toStr=True, profile=profile))
    else:
      self.component.extendModule("keybindings", "actions", func_name, "function(){%s}" % JsUtils.jsConvertFncs(
        js_funcs, toStr=True, profile=profile))
    self._attrs[func_name] = keys
    return self


class RowContextMenu(Options):

  def duplicate(self, label: str = "Duplicate", icon: str = None, disabled: bool = False, separator: bool = None):
    """
    Description:
    -----------
    Add a duplicate entry to the context menu.

    Attributes:
    ----------
    :param label: The message. Default Duplicate
    :param icon: The icon reference e.g: fas fa-trash
    :param disabled: Flag for the status
    :param separator: You can add a horizontal separator to a list of menu items by including an object with the
      separator property set to true
    """
    if icon is not None:
      label = "<i class='%s'></i> %s" % (icon, label)
    self._attrs[label] = {
      "action": "function(e, row){row.getTable().addRow(row.getData(), false, row.getPosition())}"}
    if disabled:
      self._attrs[label]["disabled"] = json.dumps(disabled)
    if separator is not None:
      self._attrs[label]["separator"] = json.dumps(separator)
    return self

  def delete(self, label: str = "Delete", icon: str = None, disabled: bool = False, separator: bool = None):
    """
    Description:
    -----------
    Add a delete entry to the context menu.

    Usage::

      table = page.ui.tables.tabulators.table(rows=["Test"], cols=["AA"])
      table.options.rowContextMenu.delete()

    Attributes:
    ----------
    :param label: The message. Default Duplicate
    :param icon: The icon reference e.g: fas fa-trash
    :param disabled: Flag for the status
    :param separator: You can add a horizontal separator to a list of menu items by including an object with the
      separator property set to true
    """
    if icon is not None:
      label = "<i class='%s'></i> %s" % (icon, label)
    self._attrs[label] = {
      "action": "function(e, row){row.delete()}"}
    if disabled:
      self._attrs[label]["disabled"] = json.dumps(disabled)
    if separator is not None:
      self._attrs[label]["separator"] = json.dumps(separator)
    return self

  def ajax(self, label: str, url: str, icon: str = None, disabled: bool = False, separator: bool = None):
    """
    Description:
    -----------
    Add a delete entry to the context menu.

    Attributes:
    ----------
    :param label: The label to be display
    :param url: The url of the underlying service
    :param icon: Optional. The font-awesome icon
    :param disabled: Optional. The status of the link
    :param separator: You can add a horizontal separator to a list of menu items by including an object with the
      separator property set to true
    """
    if icon is not None:
      label = "<i class='%s'></i> %s" % (icon, label)
    self._attrs[label] = {
      "action": self.component.page.js.post(
        url, {"label": label, "data": JsUtils.jsWrap("row.getData()")}).onSuccess([
          self.component.page.js.msg.status()
      ]).toStr()}
    if disabled:
      self._attrs[label]["disabled"] = json.dumps(disabled)
    if separator is not None:
      self._attrs[label]["separator"] = json.dumps(separator)
    return self

  def custom(self, label: str, js_funcs: types.JS_FUNCS_TYPES, icon: str = None, disabled: bool = False,
             separator: bool = None, func_ref: bool = False, profile: types.PROFILE_TYPE = None):
    """
    Description:
    -----------
    Add a delete entry to the context menu.

    Usage::

        table = page.ui.tables.tabulators.table(rows=["Test"], cols=["AA"])
        table.options.rowContextMenu.custom("test", js_funcs="function(e, row){alert(row)}", icon="fas fa-trash")

    Attributes:
    ----------
    :param label: The message. Default Duplicate
    :param js_funcs: The Javascript functions.
    :param icon: The icon reference e.g: fas fa-trash
    :param disabled: Flag for the status
    :param separator: You can add a horizontal separator to a list of menu items by including an object with the
      separator property set to true
    :param func_ref: Optional. Specify if js_funcs point to an external function
    :param profile: Optional. A flag to set the component performance storage
    """
    if icon is not None:
      label = "<i class='%s'></i> %s" % (icon, label)
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function(e, row)") and not func_ref:
      str_func = "function(e, row){%s}" % str_func
    self._attrs[label] = {
      "action": str_func}
    if disabled:
      self._attrs[label]["disabled"] = json.dumps(disabled)
    if separator is not None:
      self._attrs[label]["separator"] = json.dumps(separator)
    return self

  def config_js(self, attrs: dict = None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param attrs: Global dictionary with context menu properties.
    """
    items = []
    for label, props in self._attrs.items():
      props["label"] = json.dumps(label)
      if attrs is not None:
        props.update(attrs)
      items.append("{%s}" % ", ".join(["%s: %s" % (k, v) for k, v in props.items()]))
    return JsUtils.jsWrap(", ".join(items))

  def __str__(self):
    items = []
    for label, props in self._attrs.items():
      props["label"] = json.dumps(label)
      items.append("{%s}" % ", ".join(["%s: %s" % (k, v) for k, v in props.items()]))
    return ", ".join(items)


class TableConfig(Options):

  @property
  def index(self):
    """
    Description:
    -----------
    A unique index value should be present for each row of data if you want to be able to programmatically alter that
    data at a later point, this should be either numeric or a string.
    By default Tabulator will look for this value in the id field for the data.
    If you wish to use a different field as the index, set this using the index option parameter.

    Related Pages:

      http://tabulator.info/docs/5.3/data
    """
    return self._config_get()

  @index.setter
  def index(self, val: str):
    self._config(val)

  @property
  def ajaxURL(self):
    """
    Description:
    -----------
    If you wish to retrieve your data from a remote source you can set the URL for the request in the ajaxURL option.

    Related Pages:

      http://tabulator.info/docs/5.3/data#ajax
    """
    return self._config_get()

  @ajaxURL.setter
  def ajaxURL(self, val: str):
    self._config(val)

  @property
  def ajaxParams(self):
    """
    Description:
    -----------
    If you would like to generate the parameters with each request you can instead pass a callback to the
    ajaxParams option.
    This function will be called every time a request is made and should return an object containing the request
    parameters.

    Related Pages:

      http://tabulator.info/docs/5.3/data#ajax-params
    """
    return self._config_get()

  @ajaxParams.setter
  def ajaxParams(self, values: dict):
    self._config(values)

  @property
  def ajaxConfig(self):
    """
    Description:
    -----------
    By default Tabulator will make all ajax requests using the HTTP GET request method.
    If you need to use a different request method you can pass this into the ajaxConfig option

    Related Pages:

      http://tabulator.info/docs/5.3/data#ajax-methods
    """
    return self._config_get()

  @ajaxConfig.setter
  def ajaxConfig(self, value: str):
    self._config(value)

  @property
  def ajaxContentType(self):
    """
    Description:
    -----------
    When using a request method other than "GET" Tabulator will send any parameters with a content type of form data.
    You can change the content type with the ajaxContentType option.
    This will ensure parameters are sent in the format you expect, with the correct headers.

    Related Pages:

      http://tabulator.info/docs/5.3/data#ajax-content
    """
    return self._config_get()

  @ajaxContentType.setter
  def ajaxContentType(self, value: Union[str, dict]):
    self._config(value)

  @property
  def ajaxFiltering(self):
    """
    Description:
    -----------
    If you would prefer to filter your data server side rather than in Tabulator,
    you can use the ajaxFiltering option to send the filter data to the server instead of processing it client side.

    Related Pages:

      http://tabulator.info/docs/4.4/data
    """
    return self._config_get()

  @ajaxFiltering.setter
  def ajaxFiltering(self, flag: bool):
    self._config(flag)

  def ajaxURLGenerator(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, func_ref: bool = False):
    """
    Description:
    -----------
    If you need more control over the url of the request that you can get from the ajaxURL and ajaxParams properties,
    the you can use the ajaxURLGenerator property to pass in a callback that will generate the URL for you.
    js_funcs must use url, config, params and return a string

    Related Pages:

      http://tabulator.info/docs/4.4/data

    Attributes:
    ----------
    :param js_funcs: The Javascript functions.
    :param profile: Optional. A flag to set the component performance storage
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function(url, config, params)") and not func_ref:
      str_func = "function(url, config, params){%s}" % str_func
    self._config(str_func, js_type=True)
    return self

  @property
  def ajaxProgressiveLoad(self):
    """
    Description:
    -----------
    If you are loading a lot of data from a remote source into your table in one go, it can sometimes take a long time
    for the server to return the request, which can slow down the user experience.

    Related Pages:

      http://tabulator.info/docs/4.0/data
    """
    return self._config_get()

  @ajaxProgressiveLoad.setter
  def ajaxProgressiveLoad(self, val: str):
    self._config(val)

  @property
  def ajaxProgressiveLoadDelay(self):
    """
    Description:
    -----------
    The ajaxProgressiveLoadDelay option to add a delay in milliseconds between each page request.

    Related Pages:

      http://tabulator.info/docs/4.0/data#ajax-progressive
    """
    return self._config_get()

  @ajaxProgressiveLoadDelay.setter
  def ajaxProgressiveLoadDelay(self, number: int):
    self._config(number)

  @property
  def ajaxProgressiveLoadScrollMargin(self):
    """
    Description:
    -----------
    The ajaxProgressiveLoadScrollMargin property determines how close to the bottom of the table in pixels,
    the scroll bar must be before the next page worth of data is loaded, by default it is set to twice the height of
    the table.

    Related Pages:

      http://tabulator.info/docs/4.0/data#ajax-progressive
    """
    return self._config_get()

  @ajaxProgressiveLoadScrollMargin.setter
  def ajaxProgressiveLoadScrollMargin(self, number: int):
    self._config(number)

  @property
  def autoColumns(self):
    """
    Description:
    -----------
    If you set the autoColumns option to true, every time data is loaded into the table through the data option or
    through the setData function, Tabulator will examine the first row of the data and build columns to match that data.

    Related Pages:

      http://tabulator.info/docs/4.2/columns
    """
    return self._config_get()

  @autoColumns.setter
  def autoColumns(self, val):
    self._config(val)

  @property
  def autoTables(self):
    """
    Description:
    -----------

    Related Pages:

      http://tabulator.info/docs/5.3/data#import-data
    """
    return self._config_get()

  @autoTables.setter
  def autoTables(self, flag: bool):
    self._config(flag)

  @property
  def addRowPos(self):
    """
    Description:
    -----------
    The position in the table for new rows to be added, "bottom" or "top".

    Related Pages:

      http://tabulator.info/docs/4.2/options
    """
    return self._config_get()

  @addRowPos.setter
  def addRowPos(self, val: str):
    self._config(val)

  @property
  def clipboard(self):
    """
    Description:
    -----------
    Enable clipboard module.

    Related Pages:

      http://tabulator.info/docs/4.2/options
    """
    return self._config_get()

  @clipboard.setter
  def clipboard(self, val):
    self._config(val)

  @property
  def columnCalcs(self):
    """
    Description:
    -----------
    The columnCalcs option lets you decided where the calculations should be displayed, it can take one of four values:

    Related Pages:

      http://tabulator.info/docs/4.0/column-calcs
    """
    return self._config_get()

  @columnCalcs.setter
  def columnCalcs(self, val):
    self._config(val)

  def cellClick(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, func_ref: bool = False):
    """
    Description:
    -----------
    The cellClick callback is triggered when a user left clicks on a cell, it can be set on a per column basis using
    the option in the columns definition object.

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks

    Attributes:
    ----------
    :param js_funcs: The Javascript functions.
    :param profile: Optional. A flag to set the component performance storage
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function(cell)") and not func_ref:
      str_func = "function(cell){let value = cell.getValue(); let data = cell.getRow().getData(); %s}" % str_func
    self._config(str_func, js_type=True)
    return self

  def cellEditing(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, func_ref: bool = False):
    """
    Description:
    -----------

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks

    Attributes:
    ----------
    :param js_funcs: The Javascript functions.
    :param profile: Optional. A flag to set the component performance storage
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function(cell)") and not func_ref:
      str_func = "function(cell){let value = cell.getValue(); let data = cell.getRow().getData(); %s}" % str_func
    self._config(str_func, js_type=True)
    return self

  def clipboardPasted(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, func_ref: bool = False):
    """
    Description:
    -----------
    The clipboardPasted event is triggered whenever data is successfully pasted into the table.

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks#cell

    Attributes:
    ----------
    :param js_funcs: The Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function(clipboard, rowData, rows)") and not func_ref:
      str_func = "function(clipboard, rowData, rows){%s}" % str_func
    self._config(str_func, js_type=True)
    return self

  def cellDblClick(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, func_ref: bool = False):
    """
    Description:
    -----------
    The cellDblClick callback is triggered when a user double clicks on a cell, it can be set on a per column basis
    using the option in the columns definition object.

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks

    Attributes:
    ----------
    :param js_funcs: The Javascript functions.
    :param profile: Optional. A flag to set the component performance storage
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function(e, cell)") and not func_ref:
      str_func = "function(e, cell){%s}" % str_func
    self.component.style.css.cursor = "pointer"
    self._config(str_func, js_type=True)
    return self

  def cellContext(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, func_ref: bool = False):
    """
    Description:
    -----------
    The cellContext callback is triggered when a user right clicks on a cell, it can be set on a per column basis using
    the option in the columns definition object.

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks

    Attributes:
    ----------
    :param js_funcs: Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function(e, cell)") and not func_ref:
      str_func = "function(e, cell){%s}" % str_func
    self._config(str_func, js_type=True)
    return self

  def cellEditCancelled(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, func_ref: bool = False):
    """
    Description:
    -----------
    The cellEdited callback is triggered when data in an editable cell is changed.

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks

    Attributes:
    ----------
    :param js_funcs: Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function(cell)") and not func_ref:
      str_func = "function(cell){%s}" % str_func
    self._config(str_func, js_type=True)
    return self

  def cellEdited(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, func_ref: bool = False):
    """
    Description:
    -----------
    The cellEdited callback is triggered when data in an editable cell is changed.

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks

    Attributes:
    ----------
    :param js_funcs: Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function(cell)") and not func_ref:
      str_func = "function(cell){%s}" % str_func
    self._config(str_func, js_type=True)
    return self

  @property
  def clipboardPasteAction(self):
    """
    Description:
    -----------
    Clipboard paste action function.

    Related Pages:

      http://tabulator.info/docs/4.2/options
    """
    return self._config_get()

  @clipboardPasteAction.setter
  def clipboardPasteAction(self, val):
    self._config(val)

  @property
  def columns(self) -> List[Column]:
    """
    Description:
    -----------
    Return a list of columns.

    :rtype: list
    """
    return self.js_tree.setdefault("columns", [])

  @property
  def dataSendParams(self):
    """
    Description:
    -----------

    """
    return self._config_get()

  @dataSendParams.setter
  def dataSendParams(self, values: dict):
    self._config(values)

  @property
  def importFormat(self):
    """
    Description:
    -----------
    This can be used to import custom data when the table is loaded.

    Related Pages:

      http://tabulator.info/docs/5.3/data#import-data
    """
    return self._config_get()

  @importFormat.setter
  def importFormat(self, val: str):
    self._config(val)

  def add_column(self, field: str, title: str = None) -> Column:
    """
    Description:
    -----------
    Holder for column definition array.

    Related Pages:

      http://tabulator.info/docs/4.2/options

    Attributes:
    ----------
    :param field: String. The title name.
    :param title: String. Optional. The visible title in the columns.

    :rtype: Column
    """
    column = self._config_sub_data_enum("columns", Column)
    if field is not None:
      column.field = field
      column.title = field if title is None else title
    return column

  def get_column(self, by_field: str = None, by_title: str = None) -> Column:
    """
    Description:
    ------------
    Get the column from the underlying Tabulator object by field or by title.
    Pointing by field is recommended as the title might change quite easily.

    Attributes:
    ----------
    :param by_field: String. Optional. The field reference for the column.
    :param by_title: String. Optional. The title reference for the column.
    """
    for c in self.columns:
      if by_field is not None and c.field == by_field:
        return c

      if by_title is not None and c.title == by_title:
        return c

    return None

  @property
  def columns_group(self) -> ColumnsGroup:
    """
    Description:
    -----------

    Related Pages:

      http://tabulator.info/docs/4.2/options

    :rtype: ColumnsGroup
    """
    return self._config_sub_data_enum("columns", ColumnsGroup)

  @property
  def columnVertAlign(self):
    """
    Description:
    -----------
    Vertical alignment for contents of column header (used in column grouping).

    Related Pages:

      http://tabulator.info/docs/4.2/options
    """
    return self._config_get()

  @columnVertAlign.setter
  def columnVertAlign(self, val):
    self._config(val)

  @property
  def filterMode(self):
    """
    Description:
    -----------
    If you would prefer to filter your data server side rather than in Tabulator, you can use the filterMode option to
    send the filter data to the server instead of processing it client side.

    Related Pages:

      http://tabulator.info/docs/5.3/data#ajax-filter
    """
    return self._config_get()

  @filterMode.setter
  def filterMode(self, val: str):
    self._config(val)

  @property
  def data(self):
    """
    Description:
    -----------
    Array to hold data that should be loaded on table creation.

    Related Pages:

      http://tabulator.info/docs/4.2/options
    """
    return self._config_get()

  @data.setter
  def data(self, val):
    self._config(val)

  @property
  def debugInvalidOptions(self):
    """
    Description:
    -----------
    Enabled by default this will provide a console warning if you are trying to set an option on the table that does
    not exist.
    With the new optional modular structure this is particularly valuable as it will prompt you if you are trying to
    use an option for a module that has not been installed.

    Related Pages:

      http://tabulator.info/docs/5.0/release
    """
    return self._config_get()

  @debugInvalidOptions.setter
  def debugInvalidOptions(self, val):
    self._config(val)

  @property
  def fitColumns(self):
    """
    Description:
    -----------

    Related Pages:

      http://tabulator.info/examples/3.2
    """
    return self._config_get()

  @fitColumns.setter
  def fitColumns(self, val):
    self._config(val)

  @property
  def groupBy(self):
    """
    Description:
    -----------
    String/function to select field to group rows by.

    Related Pages:

      http://tabulator.info/docs/4.2/options
    """
    return self._config_get()

  @groupBy.setter
  def groupBy(self, val):
    self._config(val)

  @property
  def groupToggleElement(self):
    """
    Description:
    -----------
    By default Tabulator allows users to toggle a group open or closed by clicking on the arrow icon in the left of
    the group header. If you would prefer a different behaviour you can use the groupToggleElement option to choose
    a different option:

    Related Pages:

      http://tabulator.info/docs/4.0/group

    :prop val:
    """
    return self._config_get()

  @groupToggleElement.setter
  def groupToggleElement(self, val):
    self._config(val)

  @property
  def groupClosedShowCalcs(self):
    """
    Description:
    -----------
    If you would like column calculations to display when a group is closed, set the groupClosedShowCalcs
    option to true.

    Related Pages:

      http://tabulator.info/docs/4.0/column-calcs

    :prop val:
    """
    return self._config_get()

  @groupClosedShowCalcs.setter
  def groupClosedShowCalcs(self, val):
    self._config(val)

  @property
  def groupStartOpen(self):
    """
    Description:
    -----------
    You can set the default open state of groups using the groupStartOpen property.

    Related Pages:

      http://tabulator.info/docs/4.0/group
    """
    return self._config_get()

  @groupStartOpen.setter
  def groupStartOpen(self, val):
    self._config(val)

  @property
  def groupValues(self):
    """
    Description:
    -----------
    Array of values for groups.

    Related Pages:

      http://tabulator.info/docs/4.2/options
    """
    return self._config_get()

  @groupValues.setter
  def groupValues(self, val):
    self._config(val)

  def headerClick(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, func_ref: bool = False):
    """
    Description:
    -----------
    The headerClick callback is triggered when a user left clicks on a column or group header, it can be set on a per
    column basis using the option in the columns definition object.

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks

    Attributes:
    ----------
    :param js_funcs: Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function(event, column)") and not func_ref:
      str_func = "function(event, column){%s}" % str_func
    self._config(str_func, js_type=True)
    return self

  def headerDblClick(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, func_ref: bool = False):
    """
    Description:
    -----------
    The headerDblClick callback is triggered when a user double clicks on a column or group header, it can be set on a
    per column basis using the option in the columns definition object.

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks

    Attributes:
    ----------
    :param js_funcs: Javascript functions.
    :param profile: Optional. A flag to set the component performance storage
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function(event, column)") and not func_ref:
      str_func = "function(event, column){%s}" % str_func
    self._config(str_func, js_type=True)
    return self

  def headerContext(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, func_ref: bool = False):
    """
    Description:
    -----------
    The headerContext callback is triggered when a user right clicks on a column or group header,
    it can be set on a per column basis using the option in the columns definition object.

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks

    Attributes:
    ----------
    :param js_funcs: Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function(event, column)") and not func_ref:
      str_func = "function(event, column){%s}" % str_func
    self._config(str_func, js_type=True)
    return self

  def headerTap(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, func_ref: bool = False):
    """
    Description:
    -----------
    The headerTap callback is triggered when a user taps on the column header on a touch display, it can be set on a
    per column basis using the option in the columns definition object.

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks

    Attributes:
    ----------
    :param js_funcs: Javascript functions.
    :param profile: Optional. A flag to set the component performance storage
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function(event, column)") and not func_ref:
      str_func = "function(event, column){%s}" % str_func
    self._config(str_func, js_type=True)
    return self

  def headerDblTap(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, func_ref: bool = False):
    """
    Description:
    -----------
    The headerDblTap callback is triggered when a user taps on the column header on a touch display twice in under
    300ms, it can be set on a per column basis using the option in the columns definition object.

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks

    Attributes:
    ----------
    :param js_funcs: Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function(event, column)") and not func_ref:
      str_func = "function(event, column){%s}" % str_func
    self._config(str_func, js_type=True)
    return self

  @property
  def height(self):
    """
    Description:
    -----------
    Sets the height of the containing element, can be set to any valid height css value.
    If set to false (the default), the height of the table will resize to fit the table data.

    Related Pages:

      http://tabulator.info/docs/4.2/options
    """
    return self._config_get()

  @height.setter
  def height(self, val):
    if isinstance(val, int):
      val = "%spx" % val
    self._config(val)

  @property
  def history(self):
    """
    Description:
    -----------
    Enable user interaction history functionality.

    Related Pages:

      http://tabulator.info/docs/4.2/options
    """
    return self._config_get()

  @history.setter
  def history(self, val):
    self._config(val)

  @property
  def keybindings(self) -> Keybindings:
    """
    Description:
    -----------
    Add keys binding to the table.

    Related Pages:

      http://tabulator.info/docs/4.2/modules#module-keybindings
    """
    return self._config_sub_data("keybindings", Keybindings)

  @property
  def lang(self):
    """
    Description:
    -----------
    hold localization templates.

    Related Pages:

      http://tabulator.info/docs/4.2/options
    """
    return self._config_get()

  @lang.setter
  def lang(self, val):
    self._config(val)

  @property
  def layout(self):
    """
    Description:
    -----------
    Layout mode for the table columns.

    Related Pages:

      http://tabulator.info/docs/4.2/options

    Related Pages:

      http://tabulator.info/docs/4.2/options
    """
    return self._config_get()

  @layout.setter
  def layout(self, val):
    self._config(val)

  @property
  def layoutColumnsOnNewData(self):
    """
    Description:
    -----------
    If you would prefer that the column widths adjust to the data each time you load it into the table you can set the
    layoutColumnsOnNewData property to true.

    Related Pages:

      http://tabulator.info/docs/5.1/layout
    """
    return self._config_get()

  @layoutColumnsOnNewData.setter
  def layoutColumnsOnNewData(self, val):
    self._config(val)

  @property
  def layouts(self) -> EnumLayout:
    """
    Description:
    -----------
    Layout mode for the table columns.

    Related Pages:

      http://tabulator.info/docs/4.2/options

    :rtype: EnumLayout
    """
    return EnumLayout(self, "layout")

  @property
  def movableColumns(self):
    """
    Description:
    -----------
    Allow users to move and reorder columns.

    Related Pages:

      http://tabulator.info/docs/4.2/options
    """
    return self._config_get()

  @movableColumns.setter
  def movableColumns(self, val):
    self._config(val)

  @property
  def movableRows(self):
    """
    Description:
    -----------
    Allow users to move and reorder rows.

    Related Pages:

      http://tabulator.info/docs/4.2/options
    """
    return self._config_get()

  @movableRows.setter
  def movableRows(self, val):
    self._config(val)

  @property
  def movableRowsConnectedTables(self):
    """
    Description:
    -----------
    Connection selector for receiving tables.

    Related Pages:

      http://tabulator.info/docs/4.2/options
    """
    return self._config_get()

  @movableRowsConnectedTables.setter
  def movableRowsConnectedTables(self, val):
    if hasattr(val, 'htmlCode'):
      self._config("#%s" % val.htmlCode)
    else:
      if isinstance(val, list):
        # TODO: review this
        vals = []
        for v in val:
          if hasattr(v, 'htmlCode'):
            vals.append("#%s" % v.htmlCode)
          else:
            vals.append(v)
        self._config(val)
      else:
        self._config(val)

  @property
  def movableRowsReceiver(self):
    """
    Description:
    -----------
    Sender function to be executed when row has been received.

    Related Pages:

      http://tabulator.info/docs/4.2/options
    """
    return self._config_get()

  @movableRowsReceiver.setter
  def movableRowsReceiver(self, val):
    self._config(val)

  @property
  def movableRowsSender(self):
    """
    Description:
    -----------
    Sender function to be executed when row has been sent.

    Related Pages:

      http://tabulator.info/docs/4.2/options
    """
    return self._config_get()

  @movableRowsSender.setter
  def movableRowsSender(self, val):
    self._config(val)

  @property
  def pagination(self):
    """
    Description:
    -----------
    Choose pagination method, "local" or "remote".

    Related Pages:

      http://tabulator.info/docs/4.2/options
    """
    return self._config_get()

  @pagination.setter
  def pagination(self, val: Union[str, bool]):
    self._config(val)

  @property
  def paginationMode(self):
    """
    Description:
    -----------
    The pagination option is now a boolean that enables pagination and the paginationMode option sets its mode.

    Related Pages:

      http://tabulator.info/docs/5.0/release
    """
    return self._config_get()

  @paginationMode.setter
  def paginationMode(self, val):

    if val is False:
      if 'paginationSize' in self.js_tree:
        del self.js_tree['paginationSize']

      if 'pagination' in self.js_tree:
        del self.js_tree['pagination']

    else:
      self._config(val)

  @property
  def paginationSize(self):
    """
    Description:
    -----------
    Set the number of rows in each page.

    Related Pages:

      http://tabulator.info/docs/4.2/options
    """
    return self._config_get()

  @paginationSize.setter
  def paginationSize(self, val: Union[bool, int]):
    if val is not None:
      self._config('local', name="pagination")
    if val is False:
      if 'paginationSize' in self.js_tree:
        del self.js_tree['paginationSize']
      if 'pagination' in self.js_tree:
        del self.js_tree['pagination']

    else:
      self._config(val)

  @property
  def paginationSizeSelector(self):
    """
    Description:
    -----------
    Add page size selection select element to the table footer.

    Related Pages:

      http://tabulator.info/docs/4.2/options
    """
    return self._config_get()

  @paginationSizeSelector.setter
  def paginationSizeSelector(self, val):
    self._config(val)

  @property
  def persistenceID(self):
    """
    Description:
    -----------
    ID tag used to identify persistent storage information.

    Related Pages:

      http://tabulator.info/docs/4.2/options
    """
    return self._config_get()

  @persistenceID.setter
  def persistenceID(self, val):
    self._config(val)

  @property
  def persistence(self) -> Persistence:
    """
    Description:
    -----------
    The persistence system has received an overhaul in this release, providing a more consistent way to configure
    table persistence and allow even more table options to be persisted between sessions.

    Related Pages:

      http://tabulator.info/docs/4.5/release#persistence

    :rtype: Persistence
    """
    return self._config_sub_data("persistence", Persistence)

  @property
  def placeholder(self):
    """
    Description:
    -----------
    placeholder element to display on empty table.

    Related Pages:

      http://tabulator.info/docs/4.2/options
    """
    return self._config_get()

  @placeholder.setter
  def placeholder(self, val):
    self._config(val)

  @property
  def printAsHtml(self):
    return self._config_get()

  @printAsHtml.setter
  def printAsHtml(self, val):
    self._config(val)

  @property
  def printHeader(self):
    return self._config_get()

  @printHeader.setter
  def printHeader(self, val):
    self._config(val)

  @property
  def printFooter(self):
    return self._config_get()

  @printFooter.setter
  def printFooter(self, val):
    self._config(val)

  @property
  def progressiveLoad(self):
    """
    Description:
    ------------
    In load mode the table will sequentially add each page of data into the table untill all data is loaded.

    Related Pages:

      http://tabulator.info/docs/5.3/data#ajax-progressive
    """
    return self._config_get()

  @progressiveLoad.setter
  def progressiveLoad(self, val):
    self._config(val)

  @property
  def progressiveLoadDelay(self):
    return self._config_get()

  @progressiveLoadDelay.setter
  def progressiveLoadDelay(self, number):
    self._config(number)

  @property
  def progressiveLoadScrollMargin(self):
    """
    Description:
    ------------
    The progressiveLoadScrollMargin property determines how close to the bottom of the table in pixels,
    the scroll bar must be before the next page worth of data is loaded, by default it is set to twice the height of the table.

    Related Pages:

      http://tabulator.info/docs/5.3/data#ajax-progressive
    """
    return self._config_get()

  @progressiveLoadScrollMargin.setter
  def progressiveLoadScrollMargin(self, number):
    self._config(number)

  @property
  def reactiveData(self):
    """
    Description:
    -----------
    enable data reactivity.

    Related Pages:

      http://tabulator.info/docs/4.2/options
    """
    return self._config_get()

  @reactiveData.setter
  def reactiveData(self, val):
    self._config(val)

  @property
  def renderVertical(self):
    """
    Description:
    -----------
    The vertical renderer can now be set using the renderVertical option:

    Related Pages:

      http://tabulator.info/docs/5.0/release
    """
    return self._config_get()

  @renderVertical.setter
  def renderVertical(self, val):
    self._config(val)

  @property
  def responsiveLayout(self):
    """
    Description:
    -----------
    Automatically hide/show columns to fit the width of the Tabulator element.

    Related Pages:

      http://tabulator.info/docs/4.2/options
    """
    return self._config_get()

  @responsiveLayout.setter
  def responsiveLayout(self, val):
    self._config(val)

  @property
  def resizableColumns(self):
    """
    Description:
    -----------
    Allow user to resize columns (via handles on the left and right edges of the column header).

    Related Pages:

      http://tabulator.info/docs/4.2/options
    """
    return self._config_get()

  @resizableColumns.setter
  def resizableColumns(self, val):
    self._config(val)

  def rowAdded(self, js_funcs, profile: types.PROFILE_TYPE = None, func_ref: bool = False):
    """
    Description:
    -----------
    The rowAdded callback is triggered when a row is added to the table by the addRow and updateOrAddRow functions.

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks

    Attributes:
    ----------
    :param js_funcs: Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function(row)") and not func_ref:
      str_func = "function(row){%s}" % str_func
    self._config(str_func, js_type=True)
    return self

  @property
  def rowContextMenu(self) -> RowContextMenu:
    """
    Description:
    -----------
    Shortcut property to the row context menu.

    Related Pages:

      http://tabulator.info/docs/4.6/menu#cell-context
    """
    contextMenu = self._config_sub_data_enum("rowContextMenu", RowContextMenu)
    return contextMenu

  def rowClick(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, func_ref: bool = False):
    """
    Description:
    -----------
    The rowClick callback is triggered when a user clicks on a row.

    Usage::

      page.properties.js.add_text('''function alertRow(event, row){alert(row.getData())}  ''')
      table.options.rowClick("alertRow", func_ref=True)

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks

    Attributes:
    ----------
    :param js_funcs: Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function(event, row)") and not func_ref:
      str_func = "function(event, row){%s}" % str_func
    self.component.style.css.cursor = "pointer"
    self._config(str_func, js_type=True)
    return self

  def rowDblClick(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, func_ref: bool = False):
    """
    Description:
    -----------
    The rowDblClick callback is triggered when a user double clicks on a row.

    Usage::

      page.properties.js.add_text('''function alertRow(event, row){alert(row.getData())}  ''')
      table.options.rowDblClick("alertRow", func_ref=True)

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks

    Attributes:
    ----------
    :param js_funcs: Javascript functions.
    :param profile: Optional. A flag to set the component performance storage.
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function(event, row)") and not func_ref:
      str_func = "function(event, row){%s}" % str_func
    self.component.style.css.cursor = "pointer"
    self._config(str_func, js_type=True)
    return self

  @property
  def rowClickPopup(self):
    """
    Description:
    -----------
    You can add a click popup to any row by passing the popup contents to the rowClickPopup option in the table
    constructor object.

    Related Pages:

      http://tabulator.info/docs/5.2/menu#popup-row
    """
    return self._config_get()

  @rowClickPopup.setter
  def rowClickPopup(self, text: str):
    self._config(text)

  @property
  def rowContextPopup(self):
    """
    Description:
    -----------
    You can add a right click popup to any row by passing the popup contents to the rowContextPopup option in the
    table constructor object.

    Related Pages:

      http://tabulator.info/docs/5.2/menu#popup-row
    """
    return self._config_get()

  @rowContextPopup.setter
  def rowContextPopup(self, text: str):
    self._config(text)

  def rowDelete(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, func_ref: bool = False):
    """
    Description:
    -----------
    The rowDeleted callback is triggered when a row is deleted from the table by the deleteRow function.

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks

    Attributes:
    ----------
    :param js_funcs: Javascript functions
    :param profile: Optional. A flag to set the component performance storage
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function(row)") and not func_ref:
      str_func = "function(row){%s}" % str_func
    self._config(str_func, js_type=True)
    return self

  def rowContext(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, func_ref: bool = False):
    """
    Description:
    -----------
    The rowContext callback is triggered when a user right clicks on a row.

    If you want to prevent the browsers context menu being triggered in this event you will need to include the
    preventDefault() function in your callback.

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks

    Attributes:
    ----------
    :param js_funcs: Javascript functions.
    :param profile: Optional. A flag to set the component performance storage.
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function(event, row)") and not func_ref:
      str_func = "function(event, row){%s}" % str_func
    self._config(str_func, js_type=True)
    return self

  def rowFormatter(self, js_funcs: types.JS_FUNCS_TYPES, profile: Union[dict, bool] = None, func_ref: bool = False):
    """
    Description:
    -----------
    Tabulator also allows you to define a row level formatter using the rowFormatter option.
    this lets you alter each row of the table based on the data it contains.

    Related Pages:

      http://tabulator.info/docs/4.0/format

    Attributes:
    ----------
    :param js_funcs: Javascript functions.
    :param profile: Optional. A flag to set the component performance storage.
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function(row)") and not func_ref:
      str_func = "function(row){%s}" % str_func
    self._config(str_func, js_type=True)
    return self

  def rowMove(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, func_ref: bool = False):
    """
    Description:
    -----------
    The rowMoved callback will be triggered when a row has been successfully moved.

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks

    Attributes:
    ----------
    :param js_funcs: Javascript functions.
    :param profile: Optional. A flag to set the component performance storage.
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function(row)") and not func_ref:
      str_func = "function(row){%s}" % str_func
    self._config(str_func, js_type=True)
    return self

  def rowTap(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, func_ref: bool = False):
    """
    Description:
    -----------
    The rowTap callback is triggered when a user taps on a row on a touch display.

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks

    Attributes:
    ----------
    :param js_funcs: Javascript functions.
    :param profile: Optional. A flag to set the component performance storage.
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function(event, row)") and not func_ref:
      str_func = "function(event, row){%s}" % str_func
    self._config(str_func, js_type=True)
    return self

  def rowUpdated(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, func_ref: bool = False):
    """
    Description:
    -----------
    The rowUpdated callback is triggered when a row is updated by the updateRow, updateOrAddRow, updateData or
    updateOrAddData, functions.

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks

    Attributes:
    ----------
    :param js_funcs: Javascript functions.
    :param profile: Optional. A flag to set the component performance storage.
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function(row)") and not func_ref:
      str_func = "function(row){%s}" % str_func
    self._config(str_func, js_type=True)
    return self

  def rowSelected(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, func_ref: bool = False):
    """
    Description:
    -----------
    The rowSelected event is triggered when a row is selected, either by the user or programmatically.

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks#select

    Attributes:
    ----------
    :param js_funcs: Javascript functions.
    :param profile: Optional. A flag to set the component performance storage.
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function(row)") and not func_ref:
      str_func = "function(row){%s}" % str_func
    self._config(str_func, js_type=True)
    return self

  def rowDeselected(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, func_ref: bool = False):
    """
    Description:
    -----------
    The rowDeselected event is triggered when a row is deselected, either by the user or programmatically.

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks#select

    Attributes:
    ----------
    :param js_funcs: Javascript functions.
    :param profile: Optional. A flag to set the component performance storage.
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function(row)") and not func_ref:
      str_func = "function(row){%s}" % str_func
    self._config(str_func, js_type=True)
    return self

  def rowSelectionChanged(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, func_ref: bool = False):
    """
    Description:
    -----------
    Whenever the number of selected rows changes, through selection or deselection, the rowSelectionChanged event
    is triggered.

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks#select

    Attributes:
    ----------
    :param js_funcs: Javascript functions.
    :param profile: Optional. A flag to set the component performance storage.
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    if not isinstance(js_funcs, list):
      js_funcs = [js_funcs]
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function(data, rows)") and not func_ref:
      str_func = "function(data, rows){%s}" % str_func
    self._config(str_func, js_type=True)
    return self

  @property
  def selectable(self):
    """
    Description:
    -----------
    Enable/Disable row selection.

    Related Pages:

      http://tabulator.info/docs/4.2/options
    """
    return self._config_get()

  @selectable.setter
  def selectable(self, flag: Union[bool, int]):
    self._config(flag)

  @property
  def selectableRollingSelection(self):
    """
    Description:
    -----------
    Disable rolling selection

    Related Pages:

      http://tabulator.info/docs/4.0/select
    """
    return self._config_get()

  @selectableRollingSelection.setter
  def selectableRollingSelection(self, flag: bool):
    self._config(flag)

  @property
  def selectablePersistence(self):
    """
    Description:
    -----------
    Disable rolling selection

    Related Pages:

      http://tabulator.info/docs/4.0/select
    """
    return self._config_get()

  @selectablePersistence.setter
  def selectablePersistence(self, flag: bool):
    self._config(flag)

  def selectableCheck(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None, func_ref: bool = False):
    """
    Description:
    -----------
    The selectableCheck options allows you to pass a function to check if the current row should be selectable,
    returning true will allow row selection, false will result in nothing happening.
    The function should accept a RowComponent as its first argument.

    Related Pages:

      http://tabulator.info/docs/4.0/select

    Attributes:
    ----------
    :param js_funcs: JavaScript expression or entire function starting with function(row, level)
    :param profile: Optional. A flag to set the component performance storage
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function(row)") and not func_ref:
      str_func = "function(row){%s}" % str_func
    self._config(str_func, js_type=True)

  @property
  def sortMode(self):
    """
    Description:
    -----------
    If you would prefer to sort your data server side rather than in Tabulator,
    you can use the sortMode option to send the sort data to the server instead of processing it client side.

    Related Pages:

      http://tabulator.info/docs/5.3/data#ajax-sort
    """
    return self._config_get()

  @sortMode.setter
  def sortMode(self, val: str):
    self._config(val)

  @property
  def tooltips(self):
    """
    Description:
    -----------
    You can set tooltips to be displayed when the cursor hovers over cells. By default, tooltips are not displayed.

    Related Pages:

      http://tabulator.info/docs/4.0/format#tooltips
    """
    return self._config_get()

  @tooltips.setter
  def tooltips(self, val):
    self._config(val)

  @property
  def virtualDomBuffer(self):
    """
    Description:
    -----------
    In some situations, where you have a full screen table with a large number of columns,
    this can result in slow rendering performance in older browsers. In these situations it is possible to manually set
    the height of the buffer in pixels using the virtualDomBuffer option.

    Related Pages:

      http://tabulator.info/docs/4.1/layout#fittowidth
    """
    return self._config_get()

  @virtualDomBuffer.setter
  def virtualDomBuffer(self, val: int):
    self._config(val)

  @property
  def virtualDom(self):
    """
    Description:
    -----------
    If you need to disable virtual rendering for any reason you can set the virtualDom option to false to force
    standard rendering.

    Related Pages:

      http://tabulator.info/docs/4.1/layout#fittowidth
    """
    return self._config_get()

  @virtualDom.setter
  def virtualDom(self, flag: bool):
    self._config(flag)


class TableTreeConfig(TableConfig):

  @property
  def dataTree(self):
    """
    Description:
    -----------
    Enable tree layout.

    Related Pages:

      http://tabulator.info/docs/4.8/options
    """
    return self._config_get(False)

  @dataTree.setter
  def dataTree(self, flag):
    self._config(flag)

  @property
  def dataTreeSort(self):
    """
    Description:
    -----------
    Enable sorting of child rows.

    Related Pages:

      http://tabulator.info/docs/4.8/options
    """
    return self._config_get(True)

  @dataTreeSort.setter
  def dataTreeSort(self, flag: bool):
    self._config(flag)

  @property
  def dataTreeFilter(self):
    """
    Description:
    -----------
    Enable filtering of child rows.

    Related Pages:

      http://tabulator.info/docs/4.8/options
    """
    return self._config_get(True)

  @dataTreeFilter.setter
  def dataTreeFilter(self, flag: bool):
    self._config(flag)

  @property
  def dataTreeStartExpanded(self):
    """
    Description:
    -----------
    The default expansion state for tree nodes.

    Related Pages:

      http://tabulator.info/docs/4.8/options
    """
    return self._config_get(False)

  @dataTreeStartExpanded.setter
  def dataTreeStartExpanded(self, flag: bool):
    self._config(flag)

  @property
  def dataTreeSelectPropagate(self):
    """
    Description:
    -----------
    Allow selection of a row to propagate to its children.

    Related Pages:

      http://tabulator.info/docs/4.8/options
    """
    return self._config_get(False)

  @dataTreeSelectPropagate.setter
  def dataTreeSelectPropagate(self, flag: bool):
    self._config(flag)

  @property
  def dataTreeChildField(self):
    """
    Description:
    -----------
    The data field to look for child rows.

    Related Pages:

      http://tabulator.info/docs/4.8/options
    """
    return self._config_get("_children")

  @dataTreeChildField.setter
  def dataTreeChildField(self, val):
    self._config(val)

  @property
  def dataTreeElementColumn(self):
    """
    Description:
    -----------
    Choose which column to display the toggle element in.

    Related Pages:

      http://tabulator.info/docs/4.8/options
    """
    return self._config_get(False)

  @dataTreeElementColumn.setter
  def dataTreeElementColumn(self, flag: bool):
    self._config(flag)

  @property
  def dataTreeBranchElement(self):
    """
    Description:
    -----------
    Show tree branch icon.

    Related Pages:

      http://tabulator.info/docs/4.8/options
    """
    return self._config_get(True)

  @dataTreeBranchElement.setter
  def dataTreeBranchElement(self, flag: bool):
    self._config(flag)

  @property
  def dataTreeChildIndent(self):
    """
    Description:
    -----------
    Tree level indent in pixels.

    Related Pages:

      http://tabulator.info/docs/4.8/options
    """
    return self._config_get(9)

  @dataTreeChildIndent.setter
  def dataTreeChildIndent(self, number: int):
    self._config(number)

  @property
  def dataTreeCollapseElement(self):
    """
    Description:
    -----------
    boolean/string/DOM Element.

    Related Pages:

      http://tabulator.info/docs/4.8/options
    """
    return self._config_get(False)

  @dataTreeCollapseElement.setter
  def dataTreeCollapseElement(self, flag: bool):
    self._config(flag)

  @property
  def dataTreeExpandElement(self):
    """
    Description:
    -----------
    The element to be used for the expand toggle button.

    Related Pages:

      http://tabulator.info/docs/4.8/options
    """
    return self._config_get(False)

  @dataTreeExpandElement.setter
  def dataTreeExpandElement(self, flag: bool):
    self._config(flag)

  @property
  def dataTreeChildColumnCalcs(self):
    """
    Description:
    -----------
    Include visible child rows in column calculations.

    Related Pages:

      http://tabulator.info/docs/4.8/options
    """
    return self._config_get(False)

  @dataTreeChildColumnCalcs.setter
  def dataTreeChildColumnCalcs(self, flag: bool):
    self._config(flag)

  def dataTreeRowExpanded(self, js_funcs: types.JS_FUNCS_TYPES, profile: types.PROFILE_TYPE = None,
                          func_ref: bool = False):
    """
    Description:
    -----------

    Related Pages:


    Attributes:
    ----------
    :param js_funcs: JavaScript expression or entire function starting with function(row, level)
    :param profile: Optional. A flag to set the component performance storage
    :param func_ref: Optional. Specify if js_funcs point to an external function
    """
    str_func = JsUtils.jsConvertFncs(js_funcs, toStr=True, profile=profile)
    if not str_func.startswith("function(row, level)") and not func_ref:
      str_func = "function(row, level){%s}" % str_func
    self._config(str_func, js_type=True)
