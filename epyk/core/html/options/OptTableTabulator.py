
import hashlib

from epyk.core.html.options import Options
from epyk.core.html.options import Enums
from epyk.core.js import JsUtils


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
    A count of all non empty cells in the column.

    Related Pages:

      http://tabulator.info/docs/4.0/column-calcs
    """
    return self._set_value()

  def avg(self, precision=None):
    """
    Description:
    -----------
    The average value of the column.

    Related Pages:

      http://tabulator.info/docs/4.0/column-calcs

    Attributes:
    ----------
    :param precision: Integer | Boolean. The number of decimals to display, setting this value to false will display however many decimals are provided with the number
    """
    if precision is not None:
      if self.key == "bottomCalc":
        self._set_value("bottomCalcParams", {"precision": precision})
      else:
        self._set_value("topCalcParams", {"precision": precision})
    return self._set_value()

  def max(self, precision=None):
    """
    Description:
    -----------
    The minimum value in the column.

    Related Pages:

      http://tabulator.info/docs/4.0/column-calcs

    Attributes:
    ----------
    :param precision: Integer | Boolean. The number of decimals to display, setting this value to false will display however many decimals are provided with the number
    """
    if precision is not None:
      if self.key == "bottomCalc":
        self._set_value("bottomCalcParams", {"precision": precision})
      else:
        self._set_value("topCalcParams", {"precision": precision})
    return self._set_value()

  def min(self, precision=None):
    """
    Description:
    -----------
    The minimum value in the column.

    Related Pages:

      http://tabulator.info/docs/4.0/column-calcs

    Attributes:
    ----------
    :param precision: Integer | Boolean. The number of decimals to display, setting this value to false will display however many decimals are provided with the number
    """
    if precision is not None:
      if self.key == "bottomCalc":
        self._set_value("bottomCalcParams", {"precision": precision})
      else:
        self._set_value("topCalcParams", {"precision": precision})
    return self._set_value()

  def sum(self, precision=None):
    """
    Description:
    -----------
    The minimum value in the column.

    Related Pages:

      http://tabulator.info/docs/4.0/column-calcs

    Attributes:
    ----------
    :param precision: Integer | Boolean. The number of decimals to display, setting this value to false will display however many decimals are provided with the number
    """
    if precision is not None:
      if self.key == "bottomCalc":
        self._set_value("bottomCalcParams", {"precision": precision})
      else:
        self._set_value("topCalcParams", {"precision": precision})
    return self._set_value()

  def bespoke(self, jsFncs, profile=None):
    return self._set_value(value=JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile), js_type=True)


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

  def fitDataFill(self, inline=True):
    """
    Description:
    -----------
    The fitDataFill layout mode functions in the same way as the fitData mode, but ensures that rows are always at
    least the full width of the table.

    Related Pages:

      http://tabulator.info/docs/4.5/layout

    Attributes:
    ----------
    :param inline: Boolean. Optional. Force the CSS display to be inline-block.
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

  def color(self, color):
    """
    Description:
    -----------
    CSS Class to change the font color.

    Attributes:
    ----------
    :param color: String. The CSS Color.
    """
    self.component.body.style.custom_class({'_attrs': {'color': color}}, classname="tb-color-%s" % color)
    return self._add_value(value="tb-color-%s" % color)

  def background(self, color):
    """
    Description:
    -----------
    CSS Class to change the background color.

    Attributes:
    ----------
    :param color: String. The CSS Color.
    """
    self.component.body.style.custom_class({'_attrs': {'background-color': color}}, classname="tb-background-%s" % color)
    return self._add_value(value="tb-background-%s" % color)

  def css(self, css_attrs, css_attrs_hover=None):
    """
    Description:
    -----------
    CSS class for bespoke style.

    col_def.cssClass.css({'background': 'orange'}, {'background': 'white', 'color': 'blue'})

    Attributes:
    ----------
    :param css_attrs: Dictionary. The CSS attributes for the class.
    :param css_attrs_hover: Dictionary. Optional. The CSS Hover attributes for the class.
    """
    has_style = str(hashlib.sha1(str(css_attrs).encode()).hexdigest())
    self.component.body.style.custom_class({
      '_attrs': css_attrs, '_hover': css_attrs_hover}, classname="tb-style-%s" % has_style)
    return self._add_value(value="tb-style-%s" % has_style)


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
  def groupBy(self, val):
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
  def group(self):
    """
    Description:
    -----------
    You can ensure the row grouping settings are stored for the next page load by setting the group property of the
    persistence option to true.

    Related Pages:

      http://tabulator.info/docs/4.5/release#persistence

    :rtype: PersistenceGroup
    """
    return self.has_attribute(PersistenceGroup)

  @property
  def page(self):
    """
    Description:
    -----------
    You can ensure the pagination settings are stored for the next page load by setting the page property of the
    persistence option to true.

    Related Pages:

      http://tabulator.info/docs/4.5/release#persistence

    :rtype: PersistencePage
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


class ColumnsGroup(Options):

  @property
  def title(self):
    """
    Description:
    -----------
    Set a title for a could of columns.
    """
    return self._config_get()

  @title.setter
  def title(self, val):
    self._config(val)

  @property
  def columns(self):
    """
    Description:
    -----------
    Add columns to a group.

    :rtype: Column
    """
    return self._config_sub_data_enum("columns", Column)


class EditorAutocomplete(Enums):

  def startswith(self, values, showListOnEmpty=True, freetext=True, allowEmpty=True):
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

  def input(self, search=True, elementAttributes=None, **kwargs):
    """
    Description:
    -----------
    The input editor allows entering of a single line of plain text.

    Related Pages:

      http://tabulator.info/docs/4.5/edit#edit-builtin

    Attributes:
    ----------
    :param search: Boolean. Optional. Use search type input element with clear button.
    :param elementAttributes: String. Optional. set attributes directly on the input element.
    """
    editor_params = {'search': search}
    if elementAttributes is not None:
      editor_params[elementAttributes] = elementAttributes
    if kwargs:
      editor_params.update(kwargs)
    self._set_value(value=editor_params, name="editorParams")
    return self._set_value()

  def textarea(self, verticalNavigation="editor", elementAttributes=None, **kwargs):
    """
    Description:
    -----------
    The textarea editor allows entering of multiple lines of plain text.

    Related Pages:

      http://tabulator.info/docs/4.5/edit#edit-builtin

    Attributes:
    ----------
    :param verticalNavigation: String. Optional. set attributes directly on the textarea element.
    :param elementAttributes: String. Optional. determine how use of the up/down arrow keys will affect the editor.
    :param kwargs:
    """
    editor_params = {'verticalNavigation': verticalNavigation, "elementAttributes": elementAttributes}
    editor_params.update(editor_params.pop('kwargs'))
    self._set_value(value=editor_params, name="editorParams")
    return self._set_value()

  def number(self, min=None, max=None, step=1, elementAttributes=None, verticalNavigation="table", **kwargs):
    """
    Description:
    -----------
    The number editor allows for numeric entry with a number type input element with increment and decrement buttons.

    Related Pages:

      http://tabulator.info/docs/4.5/edit#edit-builtin

    Attributes:
    ----------
    :param min: Number. Optional. the maximum allowed value.
    :param max: Number. Optional. the minimum allowed value.
    :param step: String. Optional. the step size when incrementing/decrementingthe value (default 1).
    :param elementAttributes: String. Optional. set attributes directly on the input element.
    :param verticalNavigation: String. Optional. determine how use of the up/down arrow keys will affect the editor,
    :param kwargs:
    """
    editor_params = {'step': step, 'verticalNavigation': verticalNavigation, "elementAttributes": elementAttributes}
    if min is not None:
      editor_params['min'] = min
    if max is not None:
      editor_params['max'] = max
    if kwargs:
      editor_params.update(kwargs)
    self._set_value(value=editor_params, name="editorParams")
    return self._set_value()

  def range(self, min=None, max=None, step=1, elementAttributes=None, **kwargs):
    """
    Description:
    -----------
    The range editor allows for numeric entry with a range type input element.

    Related Pages:

      http://tabulator.info/docs/4.5/edit#edit-builtin

    Attributes:
    ----------
    :param min: Number. Optional. the maximum allowed value.
    :param max: Number. Optional. the minimum allowed value.
    :param step: Number. Optional. the step size when incrementing/decrementingthe value (default 1).
    :param elementAttributes: String. Optional. set attributes directly on the input element.
    :param kwargs:
    """
    editor_params = {'step': step, "elementAttributes": elementAttributes}
    if min is not None:
      editor_params['min'] = min
    if max is not None:
      editor_params['max'] = max
    editor_params.update(editor_params.pop('kwargs'))
    self._set_value(value=editor_params, name="editorParams")
    return self._set_value()

  def tick(self, tristate=False, indeterminateValue=None, elementAttributes=None, **kwargs):
    """
    Description:
    -----------
    The tick editor allows for boolean values using a checkbox type input element.

    Related Pages:

      http://tabulator.info/docs/4.5/edit#edit-builtin

    Attributes:
    ----------
    :param tristate: Boolean. Optional. allow tristate tickbox (default false).
    :param indeterminateValue: String. Optional. when using tristate tickbox what value should the third indeterminate state have (default null)
    :param elementAttributes: String. Optional. set attributes directly on the input element
    :param kwargs:
    """
    editor_params = {'tristate': tristate, 'indeterminateValue': indeterminateValue}
    if elementAttributes is not None:
      editor_params['elementAttributes'] = elementAttributes
    editor_params.update(editor_params.pop('kwargs'))
    self._set_value(value=editor_params, name="editorParams")
    return self._set_value()

  def stars(self, elementAttributes=None, **kwargs):
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
    :param elementAttributes: String. Optional set attributes directly on the star holder element.
    :param kwargs:
    """
    editor_params = {}
    if elementAttributes is not None:
      editor_params['elementAttributes'] = elementAttributes
    editor_params.update(editor_params.pop('kwargs'))
    self._set_value(value=editor_params, name="editorParams")
    return self._set_value()

  def select(self, values, listItemFormatter=None, sortValuesList=None, defaultValue=None, elementAttributes=None,
             verticalNavigation="hybrid", **kwargs):
    """
    Description:
    -----------
    The select editor creates a dropdown select box to allow the user to select from some predefined options passed
    into the values property of the editorParams option.

    Related Pages:

      http://tabulator.info/docs/4.5/edit#edit-builtin

    Attributes:
    ----------
    :param values: a list of values to be displayed to the user
    :param listItemFormatter: a function that should return the HTML contents for each item in the value list
    :param sortValuesList: if values property is set to true this option can be used to set how the generated list should be sorted
    :param defaultValue: set the value that should be selected by default if the cells value is undefined
    :param elementAttributes: set attributes directly on the input element
    :param verticalNavigation: determine how use of the up/down arrow keys will affect the editor,
    :param kwargs:
    """
    editor_params = {k: v for k, v in locals().items() if k != 'self'}
    editor_params.update(editor_params.pop('kwargs'))
    return self._set_value()

  @property
  def autocompletes(self):
    """
    Description:
    -----------
    Predefined autocomplete configurations.

    """
    self._set_value()
    return EditorAutocomplete(self, "editorParams")

  def autocomplete(self, values=None, showListOnEmpty=False, freetext=False, allowEmpty=False, searchFunc=None,
                   listItemFormatter=None, sortValuesList=None, defaultValue=None, elementAttributes=None,
                   verticalNavigation=None, **kwargs):
    """
    Description:
    -----------
    The autocomplete editor allows users to search a list of predefined options passed into the values property of
    the editorParams option.

    Usage::


    Related Pages:

      http://tabulator.info/docs/4.5/edit#edit-builtin

    Attributes:
    ----------
    :param values: a list of values to be displayed to the user
    :param showListOnEmpty: show all values in the list when the input element is empty (default false)
    :param freetext: allow the user to press enter to save a value to the cell that is not in the list (default false)
    :param allowEmpty: allow the user to save an empty value to the cell (default false)
    :param searchFunc: unction to search through array of value objects and return those that match the search term
    :param listItemFormatter: a function that should return the HTML contents for each item in the value list
    :param sortValuesList:  if values property is set to true this option can be used to set how the generated list should be sorted
    :param defaultValue: set the value that should be selected by default if the cells value is undefined
    :param elementAttributes: set attributes directly on the input element
    :param verticalNavigation: determine how use of the up/down arrow keys will affect the editor,
    """
    self._set_value()
    editor_params = {k: v for k, v in locals().items() if (k != 'self' and v is not None)}
    editor_params.update(editor_params.pop('kwargs'))

    params = []
    for k, v in editor_params.items():
      if k in ("searchFunc", ):
        params.append("%s: %s" % (k, v))
      else:
        params.append("%s: %s" % (k, JsUtils.jsConvertData(v, None)))
    self._set_value(value="{%s}" % ", ".join(params), name="editorParams", js_type=True)
    return self

  def custom(self, fncName, fncDef=None):
    """
    Description:
    -----------

    Related Pages:

      http://tabulator.info/docs/4.8/modules

    Attributes:
    ----------
    :param fncName: String. The function name.
    :param fncDef: String. Optional. The function definition.
    """
    if fncDef is None:
      self._set_value(js_type=True)
    else:
      self.component.page.extendModule(
        "edit", "editors", fncName, "function(cell, onRendered, success, cancel, editorParams){%s}" % fncDef)
      self._set_value()
    return self


class Formattors(Enums):

  def rowSelection(self):
    self._set_value()

  def text(self, **kwargs):
    """
    Description:
    -----------
    The plaintext formatter is the default formatter for all cells and will simply display the value of the cell as text.

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

  def money(self, decimal=",", thousand=".", precision=False, symbol=None, symbolAfter=None, **kwargs):
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
    :param precision: the number of decimals to display (default is 2), setting this value to false will display however many decimals are provided with the number
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

  def link(self, label=None, url=None, target='_blank', urlPrefix=None, labelField=None, urlField=None, **kwargs):
    """
    Description:
    -----------
    The link formatter renders data as an anchor with a link to the given value (by default the value will be used as
    both the url and the label of the tag).

    Related Pages:

      http://tabulator.info/docs/4.1/format

    Attributes:
    ----------
    :param label: a string representing the label, or a function which must return the string for the label, the function is passed the Cell Component as its first argument
    :param url:  a string representing the url, or a function which must return the string for the url, the function is passed the Cell Component as its first argument
    :param target: a string representing the value of the anchor tags target artibute (eg. set to "_blank" to open link in new tab)
    :param urlPrefix: a prefix to put before the url value (eg. to turn a emaill address into a clickable mailto link you should set this to "mailto:")
    :param labelField: the field in the row data that should be used for the link lable
    :param urlField: the field in the row data that should be used for the link url
    :param kwargs:
    """
    format_params = {k: v for k, v in locals().items() if k != 'self' and v is not None}
    format_params.update(format_params.pop('kwargs'))
    self._set_value()
    self._set_value("%sParams" % self.key, format_params)
    return self

  def datetime(self, inputFormat="YYYY-MM-DD", outputFormat="YYYY-MM-DD", invalidPlaceholder="(invalid date)", **kwargs):
    """
    Description:
    -----------
    The datetime formatter transforms on format of date or time into another.

    Related Pages:

      http://tabulator.info/docs/4.1/format

    Attributes:
    ----------
    :param inputFormat:
    :param outputFormat:
    :param invalidPlaceholder:
    :param kwargs:
    """
    self._set_value()
    format_params = {"inputFormat": inputFormat, "outputFormat": outputFormat, "invalidPlaceholder": invalidPlaceholder}
    if kwargs:
      format_params.update(kwargs)
    self._set_value("%sParams" % self.key, format_params)
    return self

  def tickcross(self, allowEmpty=True, allowTruthy=True, tickElement="<i class='fa fa-check'></i>",
                crossElement="<i class='fa fa-times'></i>", **kwargs):
    """
    Description:
    -----------
    The tickCross formatter displays a green tick if the value is (true|'true'|'True'|1) and a red cross if not.

    Related Pages:

      http://tabulator.info/docs/4.1/format

    Attributes:
    ----------
    :param allowEmpty: set to true to cause empty values (undefined, null, "") to display an empty cell instead of a cross (default false)
    :param allowTruthy: set to true to allow any truthy value to show a tick (default false)
    :param tickElement: custom HTML for the tick element, if set to false the tick element will not be shown (it will only show crosses)
    :param crossElement: custom HTML for the cross element, if set to false the cross element will not be shown (it will only show ticks)
    :param kwargs:
    """
    self._set_value()
    format_params = {
      'allowEmpty': allowEmpty, 'allowTruthy': allowTruthy, 'tickElement': tickElement, 'crossElement': crossElement}
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

  def lookup(self, data, **kwargs):
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

  def custom(self, fncName, fncDef=None, formatterParams=None):
    """
    Description:
    -----------

    Related Pages:

      http://tabulator.info/docs/4.0/modules

    Attributes:
    ----------
    :param fncName:
    :param fncDef:
    :param formatterParams:
    """
    if fncDef is None:
      self._set_value(fncName, js_type=True)
    else:
      self.component.page.extendModule("format", "formatters", fncName, "function(cell, formatterParams){%s}" % fncDef)
      self._set_value(fncName)
    if formatterParams is not None:
      self._set_value("%sParams" % self.key, formatterParams)
    return self

  def wrapper(self, formatter, css_attrs, formatterParams=None):
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
    :param formatterParams:
    """
    self._set_value('''
      function(cell, formatterParams){const cssAttrs = formatterParams.css;
        var cell = cell.getTable().modules.format.getFormatter('%s').call(cell.getTable().modules.format, cell, formatterParams);
        let frag = document.createRange().createContextualFragment(cell).firstChild;
        Object.keys(cssAttrs).forEach(function(key){frag.style[key] = cssAttrs[key]}); 
        return frag; }''' % formatter, js_type=True)
    formatter_params = formatterParams or {}
    formatter_params['css'] = css_attrs
    self._set_value("%sParams" % self.key, formatter_params)
    return self


class Mutators(Enums):

  def bespoke(self, fncName, fncDef=None):
    """
    Description:
    -----------
    he mutator module allows for manipulation of data as it is entered into Tabulator.

    More information on these functions can be found in the Mutators Documentation.

    Related Pages:

      http://tabulator.info/docs/4.8/mutators

    Attributes:
    ----------
    :param fncName: String.
    :param fncDef: String.
    """
    if fncDef is None:
      self._set_value(fncName, js_type=True)
    else:
      self.component.page.extendModule(
        "mutator", "mutators", fncName, "function(value, data, type, mutatorParams, component){%s}" % fncDef)
      self._set_value(fncName)
    return self


class Accessors(Enums):

  def bespoke(self, fncName, fncDef=None, accessorParams=None):
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
    :param fncName: String.
    :param fncDef: String.
    :param accessorParams: String.
    """
    if fncDef is None:
      self._set_value(fncName, js_type=True)
    else:
      self.component.page.extendModule(
        "accessor", "accessors", fncName, "function(value, data, type, params, column, row){%s}" % fncDef)
      self._set_value(fncName)
    if accessorParams is not None:
      self._set_value("accessorParams", accessorParams)
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

  def list(self, vals):
    """
    Description:
    -----------
    The in validator allows that values that match a value from the | delimited string in the parameter.

    Related Pages:

      http://tabulator.info/docs/4.5/validate
    """
    self._add_value(value='in:%s' % "".join(map(lambda x: str(), vals)))
    return self

  def regex(self, val):
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

  @property
  def editors(self):
    """
    Description:
    -----------
    The edit module allows the user to change data in cells, header filters are also dependant on this module.

    More information on these functions can be found in the Editing Data Documentation.

    Related Pages:

      http://tabulator.info/docs/4.0/modules
    """
    from epyk.core.html.tables.exts import TbEditors

    return TbEditors.ExtsEditors(self, "editor")

  @property
  def formatters(self):
    """
    Description:
    -----------
    You can set cell formatters on a per column basis using the formatter option in the column definition object.

    You can pass an optional additional parameter with the formatter, formatterParams that should contain an object
    with additional information for configuring the formatter.

    Related Pages:

      http://tabulator.info/docs/4.0/format
    """
    from epyk.core.html.tables.exts import TbFormatters

    return TbFormatters.ExtsFormattors(self, "formatter")

  @property
  def mutators(self):
    """
    Description:
    -----------
    Mutators are used to alter data as it is parsed into Tabulator.
    For example if you wanted to convert a numeric column into a boolean based on its value, before the data is used
    to build the table.

    Related Pages:

      http://tabulator.info/docs/4.0/mutators
    """
    from epyk.core.html.tables.exts import TbMutators

    return TbMutators.ExtsMutators(self, "mutator")

  @property
  def validators(self):
    """
    Description:
    -----------
    The validate module allows for validation of edited data before it is stored in the table.
    More information on these functions can be found in the Validation Documentation.
    This can be extended to add custom validator functions to the default list:

    Related Pages:

      http://tabulator.info/docs/4.0/modules
    """
    from epyk.core.html.tables.exts import TbValidators

    return TbValidators.ExtsValidators(self, "validator")


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
  def align(self, val):
    self._config(val, name="hozAlign")

  @property
  def accessors(self):
    """
    Description:
    -----------
    Accessors are used to alter data as it is extracted from the table, through commands, the clipboard, or download.

    You can set accessors on a per column basis using the accessor option in the column definition object.

    Related Pages:

      http://tabulator.info/docs/4.8/mutators#accessors
    """
    return Accessors(self, "accessor")

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
    col_def = self._config_sub_data_enum("columns", Column)
    col_def.field = field
    col_def.title = field if title is None else title
    return col_def

  def cellClick(self, jsFncs, profile=None):
    self._config("function(event, cell){%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile), js_type=True)

  @property
  def cssClass(self):
    """
    Description:
    -----------

    :rtype: EnumColCss
    """
    return self.has_attribute(EnumColCss)

  @property
  def editable(self):
    """
    Description:
    -----------
    callback to check if the cell is editable (see Manipulating Data for more details).

    Related Pages:

      http://tabulator.info/docs/4.5/columns
    """
    return self._config_get()

  @editable.setter
  def editable(self, val):
    self._config(val)

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
    return Extensions(self._report, self._attrs)

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
  def field(self, val):
    self._config(val)

  @property
  def formatters(self):
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
  def frozen(self, val):
    self._config(val)

  @property
  def headerMenu(self):
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

  @headerFilter.setter
  def headerFilter(self, value):
    self._config(value)

  def headerFilterFunc(self, jsFncs, profile=None):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self._config(
      "function customHeaderFilter(headerValue, rowValue, rowData, filterParams){%s}" % JsUtils.jsConvertFncs(
        jsFncs, toStr=True, profile=profile), js_type=True)

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
  def headerVisible(self):
    """
    Description:
    -----------
    By setting the headerVisible option to false you can hide the column headers and present
    the table as a simple list if needed.

    Related Pages:

      http://tabulator.info/docs/4.5/columns
    """
    return self._config_get()

  @headerVisible.setter
  def headerVisible(self, val):
    self._config(val)

  @property
  def sorter(self):
    """
    Description:
    -----------
    By default Tabulator will attempt to guess which sorter should be applied to a column based on the data contained
    in the first row.

    Related Pages:

      http://tabulator.info/examples/4.5#sorters

    :rtype: EnumSorter
    """
    return self.sub_data("sorter", EnumSorter)

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
  def widthGrow(self, val):
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
  def tooltip(self, flag):
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
  def titleFormatterParams(self, val):
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
  def bottomCalcFormatters(self):
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
    self._report.extendModule(
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
    self._report.extendModule(
      "keybindings", "actions", "addRow",
      "function(){var rows = this.table.getSelectedRows(); rows.forEach(function(row){row.delete()})}")
    self._attrs["deleteSelectedRows"] = keys
    return self

  def bespoke(self, keys, fncName, fncDef, prevent_default=True):
    """
    Description:
    -----------
    Add a keyboard shortcut custom event on the table.

    Keycodes can be found using the function ord()

    Related Pages:

      http://tabulator.info/docs/4.4/keybindings

    Attributes:
    ----------
    :param keys: String. The keys to trigger the event.
    :param fncName: String. The function name / alias for this event.
    :param fncDef: String. The function definition of this event.
    :param prevent_default: Boolean. Stop the event and do not change the cell in editable.
    """
    if prevent_default:
      self.component.extendModule(
        "keybindings", "actions", fncName, "function(event){event.preventDefault(); %s}" % fncDef)
    else:
      self.component.extendModule("keybindings", "actions", fncName, "function(){%s}" % fncDef)
    self._attrs[fncName] = keys
    return self


class RowContextMenu(Options):

  def duplicate(self, label="Duplicate", icon=None, disabled=False):
    """
    Description:
    -----------
    Add a duplicate entry to the context menu.

    Attributes:
    ----------
    :param label:
    :param icon:
    :param disabled:
    """
    self._attrs[label] = "row.getTable().addRow(row.getData(), false, row.getPosition())"
    return self

  def delete(self, label="Delete", icon=None, disabled=False):
    """
    Description:
    -----------
    Add a delete entry to the context menu.

    Attributes:
    ----------
    :param label:
    :param icon:
    :param disabled:
    """
    self._attrs[label] = "row.delete()"
    return self

  def ajax(self, label, url, icon=None, disabled=False):
    """
    Description:
    -----------
    Add a delete entry to the context menu.

    Attributes:
    ----------
    :param label: String. The label to be display.
    :param url: String. The url of the underlying service.
    :param icon: String. Optional. The font-awesome icon.
    :param disabled: Boolean. Optional. The status of the link.
    """
    self._attrs[label] = self.component.page.js.post(
      url, {"label": label, "data": JsUtils.jsWrap("row.getData()")}).onSuccess([
        self.component.page.js.msg.status()
    ]).toStr()
    return self

  def custom(self, label, strFnc, icon=None, disabled=False):
    """
    Description:
    -----------
    Add a delete entry to the context menu.

    Attributes:
    ----------
    :param label:
    :param strFnc:
    :param icon:
    :param disabled:
    """
    self._attrs[label] = strFnc
    return self

  def __str__(self):
    return ", ".join(["{label: '%s', action: function(e, row){%s}}" % (k, v) for k, v in self._attrs.items()])


class HeaderMenu(Options):

  def hide(self, label="Hide Column", icon="fas fa-eye-slash", disabled=False):
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

  def custom(self, label, strFnc, icon=None, disabled=False):
    """
    Description:
    -----------
    Add a delete entry to the context menu.

    Attributes:
    ----------
    :param label:
    :param strFnc:
    :param icon:
    :param disabled:
    """
    if icon is not None:
      self._attrs['<i class="%s" style="margin-right:5px"></i>%s' % (icon, label)] = strFnc
    else:
      self._attrs[label] = strFnc
    return self

  def __str__(self):
    result = []
    for k, v in self._attrs.items():
      if v is None and k.startswith("separator_"):
        result.append("{'separator': true}")
      else:
        result.append("{label: '%s', action: function(e, column){%s}}" % (k, v))
    return ", ".join(result)


class TableConfig(Options):

  @property
  def ajaxURL(self):
    """
    Description:
    -----------

    Related Pages:

      http://tabulator.info/docs/4.0/data
    """
    return self._config_get()

  @ajaxURL.setter
  def ajaxURL(self, val):
    self._config(val)

  @property
  def ajaxProgressiveLoad(self):
    """
    Description:
    -----------

    Related Pages:

      http://tabulator.info/docs/4.0/data
    """
    return self._config_get()

  @ajaxProgressiveLoad.setter
  def ajaxProgressiveLoad(self, val):
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
  def ajaxProgressiveLoadDelay(self, number):
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
  def ajaxProgressiveLoadScrollMargin(self, number):
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
  def addRowPos(self, val):
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

  def cellClick(self, jsFncs, profile=None):
    """
    Description:
    -----------
    The cellClick callback is triggered when a user left clicks on a cell, it can be set on a per column basis using
    the option in the columns definition object.

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks

    Attributes:
    ----------
    :param jsFncs: String | List. The Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self._config(
      "function(event, cell){let value = cell.getValue(); let data = cell.getRow().getData(); %s}" % JsUtils.jsConvertFncs(
        jsFncs, toStr=True, profile=profile), js_type=True)
    return self

  def clipboardPasted(self, jsFncs, profile=None):
    """
    Description:
    -----------
    The clipboardPasted event is triggered whenever data is successfully pasted into the table.

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks#cell

    Attributes:
    ----------
    :param jsFncs: String | List. The Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self._config(
      "function(clipboard, rowData, rows){%s} " % JsUtils.jsConvertFncs(
        jsFncs, toStr=True, profile=profile), js_type=True)
    return self

  def cellDblClick(self, jsFncs, profile=None):
    """
    Description:
    -----------
    The cellDblClick callback is triggered when a user double clicks on a cell, it can be set on a per column basis
    using the option in the columns definition object.

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks

    Attributes:
    ----------
    :param jsFncs: String | List. The Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self.component.style.css.cursor = "pointer"
    self._config("function(e, cell){%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile), js_type=True)
    return self

  def cellContext(self, jsFncs, profile=None):
    """
    Description:
    -----------
    The cellContext callback is triggered when a user right clicks on a cell, it can be set on a per column basis using
    the option in the columns definition object.

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self._config("function(e, cell){%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile), js_type=True)
    return self

  def cellEditCancelled(self, jsFncs, profile=None):
    """
    Description:
    -----------
    The cellEdited callback is triggered when data in an editable cell is changed.

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self._config("function(cell){%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile), js_type=True)
    return self

  def cellEdited(self, jsFncs, profile=None):
    """
    Description:
    -----------
    The cellEdited callback is triggered when data in an editable cell is changed.

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self._config("function(cell){%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile), js_type=True)
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
  def columns(self):
    """
    Description:
    -----------
    Return a list of columns.

    :rtype: list
    """
    return self.js_tree.setdefault("columns", [])

  def add_column(self, field, title=None):
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
    for c in self.columns:
      if by_field is not None and c.field == by_field:
        return c

      if by_title is not None and c.title == by_title:
        return c

    return None

  @property
  def columns_group(self):
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

  def headerClick(self, jsFncs, profile=None):
    """
    Description:
    -----------
    The headerClick callback is triggered when a user left clicks on a column or group header, it can be set on a per
    column basis using the option in the columns definition object.

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self._config(
      "function(event, column){%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile), js_type=True)
    return self

  def headerDblClick(self, jsFncs, profile=None):
    """
    Description:
    -----------
    The headerDblClick callback is triggered when a user double clicks on a column or group header, it can be set on a
    per column basis using the option in the columns definition object.

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self._config(
      "function(event, column){%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile), js_type=True)
    return self

  def headerContext(self, jsFncs, profile=None):
    """
    Description:
    -----------
    The headerContext callback is triggered when a user right clicks on a column or group header,
    it can be set on a per column basis using the option in the columns definition object.

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self._config(
      "function(event, column){%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile), js_type=True)
    return self

  def headerTap(self, jsFncs, profile=None):
    """
    Description:
    -----------
    The headerTap callback is triggered when a user taps on the column header on a touch display, it can be set on a
    per column basis using the option in the columns definition object.

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self._config(
      "function(event, column){%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile), js_type=True)
    return self

  def headerDblTap(self, jsFncs, profile=None):
    """
    Description:
    -----------
    The headerDblTap callback is triggered when a user taps on the column header on a touch display twice in under
    300ms, it can be set on a per column basis using the option in the columns definition object.

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self._config(
      "function(event, column){%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile), js_type=True)
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
  def keybindings(self):
    """
    Description:
    -----------
    Add keys binding to the table.

    Related Pages:

      http://tabulator.info/docs/4.2/modules#module-keybindings

    :rtype: Keybindings
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
  def layouts(self):
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
  def pagination(self, val):
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
  def paginationSize(self, val):
    if val is not None:
      self._config('local', name="pagination")
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
  def persistence(self):
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

  def rowAdded(self, jsFncs, profile=None):
    """
    Description:
    -----------
    The rowAdded callback is triggered when a row is added to the table by the addRow and updateOrAddRow functions.

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self._config("function(row){%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile), js_type=True)
    return self

  @property
  def rowContextMenu(self):
    """
    Description:
    -----------
    Shortcut property to the row context menu.

    Related Pages:

      http://tabulator.info/docs/4.6/menu#cell-context

    :rtype: RowContextMenu
    """
    contextMenu = self._config_sub_data_enum("rowContextMenu", RowContextMenu)
    return contextMenu

  def rowClick(self, jsFncs, profile=None):
    """
    Description:
    -----------
    The rowClick callback is triggered when a user clicks on a row.

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self.component.style.css.cursor = "pointer"
    self._config("function(event, row){%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile), js_type=True)
    return self

  def rowDblClick(self, jsFncs, profile=None):
    """
    Description:
    -----------
    The rowDblClick callback is triggered when a user double clicks on a row.

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self.component.style.css.cursor = "pointer"
    self._config("function(event, row){%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile), js_type=True)
    return self

  def rowDelete(self, jsFncs, profile=None):
    """
    Description:
    -----------
    The rowDeleted callback is triggered when a row is deleted from the table by the deleteRow function.

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self._config("function(row){%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile), js_type=True)
    return self

  def rowContext(self, jsFncs, profile=None):
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
    :param jsFncs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self._config("function(event, row){%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile), js_type=True)
    return self

  def rowFormatter(self, jsFncs, profile=None):
    """
    Description:
    -----------
    Tabulator also allows you to define a row level formatter using the rowFormatter option.
    this lets you alter each row of the table based on the data it contains.

    Related Pages:

      http://tabulator.info/docs/4.0/format

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self._config("function(row){%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile), js_type=True)
    return self

  def rowMove(self, jsFncs, profile=None):
    """
    Description:
    -----------
    The rowMoved callback will be triggered when a row has been successfully moved.

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self._config("function(row){%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile), js_type=True)
    return self

  def rowTap(self, jsFncs, profile=None):
    """
    Description:
    -----------
    The rowTap callback is triggered when a user taps on a row on a touch display.

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self._config("function(event, row){%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile), js_type=True)
    return self

  def rowUpdated(self, jsFncs, profile=None):
    """
    Description:
    -----------
    The rowUpdated callback is triggered when a row is updated by the updateRow, updateOrAddRow, updateData or
    updateOrAddData, functions.

    Related Pages:

      http://tabulator.info/docs/4.0/callbacks

    Attributes:
    ----------
    :param jsFncs: List | String. Javascript functions.
    :param profile: Boolean | Dictionary. Optional. A flag to set the component performance storage.
    """
    if not isinstance(jsFncs, list):
      jsFncs = [jsFncs]
    self._config("function(row){%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile), js_type=True)
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
  def selectable(self, val):
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
  def dataTreeSort(self, flag):
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
  def dataTreeFilter(self, flag):
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
  def dataTreeStartExpanded(self, flag):
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
  def dataTreeSelectPropagate(self, flag):
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
  def dataTreeElementColumn(self, flag):
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
  def dataTreeBranchElement(self, flag):
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
  def dataTreeChildIndent(self, flag):
    self._config(flag)

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
  def dataTreeCollapseElement(self, flag):
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
  def dataTreeExpandElement(self, flag):
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
  def dataTreeChildColumnCalcs(self, flag):
    self._config(flag)

  def dataTreeRowExpanded(self, jsFncs, profile=None):
    """
    Description:
    -----------

    Related Pages:



    :param jsFncs:
    :param profile:
    """
    self._config("function(row, level) {%s}" % JsUtils.jsConvertFncs(jsFncs, toStr=True, profile=profile), js_type=True)
