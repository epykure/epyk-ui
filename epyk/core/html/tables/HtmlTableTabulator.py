#!/usr/bin/python
# -*- coding: utf-8 -*-

import hashlib

from epyk.core.html import Html

from epyk.core.js.packages import JsTabulator
from epyk.core.js.primitives import JsObjects

from epyk.core.data.DataClass import DataClass
from epyk.core.data.DataClass import DataEnum
from epyk.core.data.DataClass import DataGroup
from epyk.core.data.DataClass import DataEnumMulti

# The list of CSS classes
from epyk.core.css.styles import GrpClsTable


class Table(Html.Html):
  requirements = ('tabulator', )
  name = 'Tabulator Table'

  def __init__(self, report, records, width, height, htmlCode, options, profile):
    data, columns, self.__config = [], [], None
    super(Table, self).__init__(report, [], htmlCode=htmlCode, css_attrs={"width": width, "height": height}, profile=profile)
    self.__config = TableConfig(self, options)
    if records is not None:
      self.config.data = records
    self.style.css.background = None

  @property
  def style(self):
    """
    Description:
    ------------

    :rtype: GrpClsTable.Tabulator
    """
    if self._styleObj is None:
      self._styleObj = GrpClsTable.Tabulator(self)
    return self._styleObj

  @property
  def tableId(self):
    """
    Description:
    ------------
    Return the Javascript variable of the chart
    """
    return "%s_obj" % self.htmlCode

  @property
  def config(self):
    """
    Description:
    ------------

    :rtype: TableConfig
    """
    if self.__config is None:
      self.__config = TableConfig(self._report)
    return self.__config

  @property
  def js(self):
    """
    Description:
    ------------
    Return the Javascript internal object

    :return: A Javascript object

    :rtype: JsTabulator.Tabulator
    """
    if self._js is None:
      self._js = JsTabulator.Tabulator(self._report, selector=self.tableId, setVar=False, parent=self)
    return self._js

  def add_column(self, field, title=None):
    """
    Description:
    ------------

    :param field:
    :param title:
    """
    col_def = self.config.columns
    col_def.field = field
    col_def.title = field if title is None else title
    return col_def

  def get_column(self, by_title):
    """
    Description:
    ------------

    :param by_title:

    :rtype: Column
    """
    for c in self.config._attrs.get('columns', []):
      if c.title == by_title:
        return c

    return None

  def build(self, data=None, options=None, profile=False):
    if data:
      return self.js.setData(data)

    return 'var %s =  new Tabulator("#%s", %s)' % (self.tableId, self.htmlCode, self.config)

  def __str__(self):
    self._report._props.setdefault('js', {}).setdefault("builders", []).append(self.refresh())
    return "<div %s></div>" % (self.get_attrs(pyClassNames=self.style.get_classes()))


class EnumLayout(DataEnum):

  def fitDataStretch(self):
    """
    Description:
    -----------
    The fitDataStretch layout mode functions in the same way as the fitDataFill mode, but instead of stretching the empty row to fill the table it stretches the last visible column.

    Related Pages:
http://tabulator.info/docs/4.5/layout
    """
    return self.set()

  def fitColumns(self):
    """
    Description:
    -----------
    As an alternative to the default data fit, you can use the fitColumns layout mode to cause Tabulator to resize columns so they fit perfectly in the available table width.

    Related Pages:
http://tabulator.info/docs/4.5/layout
    """
    return self.set()

  def fitDataFill(self):
    """
    Description:
    -----------
    The fitDataFill layout mode functions in the same way as the fitData mode, but ensures that rows are always at least the full width of the table.

    Related Pages:
http://tabulator.info/docs/4.5/layout
    """
    return self.set()


class EnumSorter(DataEnum):

  def string(self):
    """
    Description:
    -----------
    Sorts column as strings of characters

    Related Pages:
http://tabulator.info/examples/4.5#sorters
    """
    return self.set("string")

  def number(self):
    """
    Description:
    -----------
    Sorts column as numbers (integer or float, will also handle numbers using "," separators)

    Related Pages:
http://tabulator.info/examples/4.5#sorters
    """
    return self.set("number")

  def alphanum(self):
    """
    Description:
    -----------
    Sorts column as alpha numeric code

    Related Pages:
http://tabulator.info/examples/4.5#sorters
    """
    return self.set("alphanum")

  def boolean(self):
    """
    Description:
    -----------
    Sorts column as booleans

    Related Pages:
http://tabulator.info/examples/4.5#sorters
    """
    return self.set("boolean")

  def date(self):
    """
    Description:
    -----------
    Sorts column as dates

    Related Pages:
http://tabulator.info/examples/4.5#sorters
    """
    return self.set("date")

  def time(self):
    """
    Description:
    -----------
    Sorts column as dates

    Related Pages:
sorts column as times
    """
    return self.set("time")


class EnumColCss(DataEnumMulti):
  js_conversion = True
  delimiter = " "

  def center(self):
    """
    Description:
    -----------
    CSS Class to center the results
    """
    self._report.body.style.custom_class({'_attrs': {'text-align': 'center'}}, classname="tb-center")
    return self.set("tb-center")

  def color(self, color):
    """
    Description:
    -----------
    CSS Class to change the font color

    Attributes:
    ----------
    :param color: String. The CSS Color
    """
    self._report.body.style.custom_class({'_attrs': {'color': color}}, classname="tb-color-%s" % color)
    return self.set("tb-color-%s" % color)

  def background(self, color):
    """
    Description:
    -----------
    CSS Class to change the background color

    Attributes:
    ----------
    :param color: String. The CSS Color
    """
    self._report.body.style.custom_class({'_attrs': {'background-color': color}}, classname="tb-background-%s" % color)
    return self.set("tb-background-%s" % color)

  def css(self, css_attrs, css_attrs_hover=None):
    """
    Description:
    -----------
    CSS class for bespoke style

    col_def.cssClass.css({'background': 'orange'}, {'background': 'white', 'color': 'blue'})

    Attributes:
    ----------
    :param css_attrs: Dictionary. The CSS attributes for the class
    :param css_attrs_hover: Dictionary. The CSS Hover attributes for the class
    """
    has_style = str(hashlib.sha1(str(css_attrs).encode()).hexdigest())
    self._report.body.style.custom_class({'_attrs': css_attrs, '_hover': css_attrs_hover}, classname="tb-style-%s" % has_style)
    return self.set("tb-style-%s" % has_style)


class PersistenceGroup(DataClass):

  @property
  def groupBy(self):
    """
    persist only the groupBy setting

    :return:
    """
    return self._attrs["groupBy"]

  @groupBy.setter
  def groupBy(self, val):
    self._attrs["groupBy"] = val

  @property
  def groupStartOpen(self):
    return self._attrs["groupStartOpen"]

  @groupStartOpen.setter
  def groupStartOpen(self, val):
    self._attrs["groupStartOpen"] = val

  @property
  def groupHeader(self):
    return self._attrs["groupHeader"]

  @groupHeader.setter
  def groupHeader(self, val):
    self._attrs["groupHeader"] = val


class PersistencePage(DataClass):

  @property
  def size(self):
    """
    Description:
    -----------
    persist the current page size

    Related Pages:
http://tabulator.info/docs/4.5/release#persistence
    """
    return self._attrs["size"]

  @size.setter
  def size(self, val):
    self._attrs["size"] = val

  @property
  def page(self):
    """
    Description:
    -----------
    do not persist the current page

    Related Pages:
http://tabulator.info/docs/4.5/release#persistence
    """
    return self._attrs["page"]

  @page.setter
  def page(self, val):
    self._attrs["page"] = val


class Persistence(DataClass):

  @property
  def sort(self):
    """
    Description:
    -----------
    You can ensure the data sorting is stored for the next page load by setting the sort property of the persistence option to true

    Related Pages:
http://tabulator.info/docs/4.5/release#persistence
    """
    return self._attrs["sort"]

  @sort.setter
  def sort(self, val):
    self._attrs["sort"] = val

  @property
  def filter(self):
    """
    Description:
    -----------
    You can ensure the data filtering is stored for the next page load by setting the filter property of the persistence option to true

    Related Pages:
http://tabulator.info/docs/4.5/release#persistence
    """
    return self._attrs["filter"]

  @filter.setter
  def filter(self, val):
    self._attrs["filter"] = val

  @property
  def group(self):
    """
    Description:
    -----------
    You can ensure the row grouping settings are stored for the next page load by setting the group property of the persistence option to true

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
    You can ensure the pagination settings are stored for the next page load by setting the page property of the persistence option to true

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
    You can ensure the layout of columns is stored for the next page load by setting the columns property of the persistence option to true

    Related Pages:
http://tabulator.info/docs/4.5/release#persistence
    """
    return self._attrs["columns"]

  @columns.setter
  def columns(self, val):
    self._attrs["columns"] = val


class BottomCalcParams(DataClass):

  @property
  def precision(self):
    """
    the number of decimals to display (default is 2), setting this value to false will display however many decimals are provided with the number

    http://tabulator.info/docs/4.5/column-calcs#func-builtin
    """
    return self._attrs["precision"]

  @precision.setter
  def precision(self, val):
    self._attrs["precision"] = val


class ColumnsGroup(DataClass):

  @property
  def title(self):
    return self._attrs["title"]

  @title.setter
  def title(self, val):
    self._attrs["title"] = val

  @property
  def columns(self):
    return self.sub_data_enum("columns", Column)


class Editor(DataGroup):

  def input(self, search=True, elementAttributes=None, **kwargs):
    """
    Description:
    -----------
    The input editor allows entering of a single line of plain text

    Related Pages:
http://tabulator.info/docs/4.5/edit#edit-builtin

    Attributes:
    ----------
    :param search: use search type input element with clear button
    :param elementAttributes: set attributes directly on the input element
    """
    self._attrs["editor"] = 'input'
    self._attrs["editorParams"] = {'search': search}
    if elementAttributes is not None:
      self._attrs["editorParams"][elementAttributes] = elementAttributes
    if kwargs:
      self._attrs["editorParams"].update(kwargs)
    return self

  def textarea(self, verticalNavigation="editor", elementAttributes=None, **kwargs):
    """
    Description:
    -----------
    The textarea editor allows entering of multiple lines of plain text

    Related Pages:
http://tabulator.info/docs/4.5/edit#edit-builtin

    Attributes:
    ----------
    :param verticalNavigation: set attributes directly on the textarea element
    :param elementAttributes: determine how use of the up/down arrow keys will affect the editor,
    """
    self._attrs["editor"] = 'textarea'
    self._attrs["editorParams"] = {'verticalNavigation': verticalNavigation, "elementAttributes": elementAttributes}
    self._attrs["editorParams"].update(self._attrs["editorParams"].pop('kwargs'))
    return self

  def number(self, min=None, max=None, step=1, elementAttributes=None, verticalNavigation="table", **kwargs):
    """
    Description:
    -----------
    The number editor allows for numeric entry with a number type input element with increment and decrement buttons.

    Related Pages:
http://tabulator.info/docs/4.5/edit#edit-builtin

    Attributes:
    ----------
    :param min: the maximum allowed value
    :param max: the minimum allowed value
    :param step: the step size when incrementing/decrementingthe value (default 1)
    :param elementAttributes: set attributes directly on the input element
    :param verticalNavigation: determine how use of the up/down arrow keys will affect the editor,
    :param kwargs:
    """
    self._attrs["editor"] = 'number'
    self._attrs["editorParams"] = {'step': step, 'verticalNavigation': verticalNavigation, "elementAttributes": elementAttributes}
    if min is not None:
      self._attrs["editorParams"]['min'] = min
    if max is not None:
      self._attrs["editorParams"]['max'] = max
    self._attrs["editorParams"].update(self._attrs["editorParams"].pop('kwargs'))
    return self

  def range(self, min=None, max=None, step=1, elementAttributes=None, **kwargs):
    """
    Description:
    -----------
    The range editor allows for numeric entry with a range type input element.

    Related Pages:
http://tabulator.info/docs/4.5/edit#edit-builtin

    Attributes:
    ----------
    :param min: the maximum allowed value
    :param max: the minimum allowed value
    :param step: the step size when incrementing/decrementingthe value (default 1)
    :param elementAttributes: set attributes directly on the input element
    :param kwargs:
    """
    self._attrs["editor"] = 'range'
    self._attrs["editorParams"] = {'step': step, "elementAttributes": elementAttributes}
    if min is not None:
      self._attrs["editorParams"]['min'] = min
    if max is not None:
      self._attrs["editorParams"]['max'] = max
    self._attrs["editorParams"].update(self._attrs["editorParams"].pop('kwargs'))
    return self

  def tick(self, tristate=False, indeterminateValue=None, elementAttributes=None, **kwargs):
    """
    Description:
    -----------
    The tick editor allows for boolean values using a checkbox type input element.

    Related Pages:
http://tabulator.info/docs/4.5/edit#edit-builtin

    Attributes:
    ----------
    :param tristate: allow tristate tickbox (default false)
    :param indeterminateValue:  when using tristate tickbox what value should the third indeterminate state have (default null)
    :param elementAttributes: set attributes directly on the input element
    :param kwargs:
    """
    self._attrs["editor"] = 'tick'
    self._attrs["editorParams"] = {'tristate': tristate, 'indeterminateValue': indeterminateValue}
    if elementAttributes is not None:
      self._attrs["editorParams"]['elementAttributes'] = elementAttributes
    self._attrs["editorParams"].update(self._attrs["editorParams"].pop('kwargs'))
    return self

  def stars(self, elementAttributes=None, **kwargs):
    """
    Description:
    -----------
    The star editor allows entering of numeric value using a star rating indicator.

    This editor will automatically detect the correct number of stars to use if it is used on the same column as the star formatter.

    Related Pages:
http://tabulator.info/docs/4.5/edit#edit-builtin

    Attributes:
    ----------
    :param elementAttributes: set attributes directly on the star holder elemen
    :param kwargs:
    """
    self._attrs["editor"] = 'star'
    self._attrs["editorParams"] = {}
    if elementAttributes is not None:
      self._attrs["editorParams"]['elementAttributes'] = elementAttributes
    self._attrs["editorParams"].update(self._attrs["editorParams"].pop('kwargs'))
    return self

  def select(self, values, listItemFormatter=None, sortValuesList=None, defaultValue=None, elementAttributes=None,
                    verticalNavigation="hybrid", **kwargs):
    """
    Description:
    -----------
    The select editor creates a dropdown select box to allow the user to select from some predefined options passed into the values property of the editorParams option.

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
    self._attrs["editor"] = 'select'
    self._attrs["editorParams"] = {k: v for k, v in locals().items() if k != 'self'}
    self._attrs["editorParams"].update(self._attrs["editorParams"].pop('kwargs'))
    return self

  def autocomplete(self, values, showListOnEmpty=None, freetext=None, allowEmpty=None, searchFunc=None,
                          listItemFormatter=None, sortValuesList=None, defaultValue=None, elementAttributes=None,
                          verticalNavigation=None, **kwargs):
    """
    Description:
    -----------
    The autocomplete editor allows users to search a list of predefined options passed into the values property of the editorParams option.

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
    self._attrs["editor"] = 'autocomplete'
    self._attrs["editorParams"] = {k: v for k, v in locals().items() if k != 'self'}
    self._attrs["editorParams"].update(self._attrs["editorParams"].pop('kwargs'))
    return self


class Formattors(DataGroup):

  def text(self, **kwargs):
    """
    Description:
    -----------
    The plaintext formater is the default formatter for all cells and will simply dispay the value of the cell as text.

    Related Pages:
http://tabulator.info/docs/4.1/format

    Attributes:
    ----------
    :param kwargs:
    """
    self._attrs["formatter"] = 'plaintext'
    if kwargs:
      self._attrs["formatterParams"] = kwargs
    return self

  def textarea(self, **kwargs):
    """
    Description:
    -----------
    The textarea formater shows text with carriage returns intact (great for multiline text), this formatter will also adjust the height of rows to fit the cells contents when columns are resized.

    Related Pages:
http://tabulator.info/docs/4.1/format

    Attributes:
    ----------
    :param kwargs:
    """
    self._attrs["formatter"] = 'textarea'
    if kwargs:
      self._attrs["formatterParams"] = kwargs
    return self

  def html(self, **kwargs):
    """
    Description:
    -----------
    he html formater displays un-sanitized html.

    Related Pages:
http://tabulator.info/docs/4.1/format

    Attributes:
    ----------
    :param kwargs:
    """
    self._attrs["formatter"] = 'html'
    if kwargs:
      self._attrs["formatterParams"] = kwargs
    return self

  def money(self, decimal=",", thousand=".", precision=False, symbol=None, symbolAfter=None, **kwargs):
    """
    Description:
    -----------
    The money formater formats a number into currency notation (eg. 1234567.8901 -> 1,234,567.89).

    Related Pages:
http://tabulator.info/docs/4.1/format

    Attributes:
    ----------
    :param decimal: Symbol to represent the decimal point (default ".")
    :param thousand: Symbol to represent the thousands seperator (default ",")
    :param precision: the number of decimals to display (default is 2), setting this value to false will display however many decimals are provided with the number
    :param symbol: currency symbol (no default)
    :param symbolAfter: position the symbol after the number (default false)
    :param kwargs:
    """
    self._attrs["formatter"] = 'formatterParams'
    if kwargs:
      self._attrs["formatterParams"] = kwargs
    return self

  def image(self, height=None, width=None, **kwargs):
    """
    Description:
    -----------
    The image formater creates an img element with the src set as the value. (triggers the normalizeHeight function on the row on image load).

    Related Pages:
http://tabulator.info/docs/4.1/format

    Attributes:
    ----------
    :param height: a CSS value for the height of the image
    :param width: a CSS value for the width of the image
    :param kwargs:
    """
    self._attrs["formatter"] = 'image'
    formatParams = {}
    if height is not None:
      formatParams['height'] = height
    if width is not None:
      formatParams['width'] = width
    self._attrs["formatterParams"] = formatParams
    for k, v in kwargs.items():
      self._attrs["formatterParams"][k] = v
    return self

  def link(self, label=None, url=None, target='_blank', urlPrefix=None, labelField=None, urlField=None, **kwargs):
    """
    Description:
    -----------
    The link formater renders data as an anchor with a link to the given value (by default the value will be used as both the url and the label of the tag).

    Related Pages:
http://tabulator.info/docs/4.1/format

    Attributes:
    ----------
    :param label: a string representing the lable, or a function which must return the string for the label, the function is passed the Cell Component as its first argument
    :param url:  a string representing the url, or a function which must return the string for the url, the function is passed the Cell Component as its first argument
    :param target: a string representing the value of the anchor tags target artibute (eg. set to "_blank" to open link in new tab)
    :param urlPrefix: a prefix to put before the url value (eg. to turn a emaill address into a clickable mailto link you should set this to "mailto:")
    :param labelField: the field in the row data that should be used for the link lable
    :param urlField: the field in the row data that should be used for the link url
    :param kwargs:
    """
    self._attrs["formatterParams"] = {k: v for k, v in locals().items() if k != 'self' and v is not None}
    self._attrs["formatterParams"].update(self._attrs["formatterParams"].pop('kwargs'))
    self._attrs["formatter"] = 'link'
    return self

  def datetime(self, inputFormat="YYYY-MM-DD", outputFormat="YYYY-MM-DD", invalidPlaceholder="(invalid date)", **kwargs):
    """
    Description:
    -----------
    The datetime formater transforms on format of date or time into another.

    Related Pages:
http://tabulator.info/docs/4.1/format

    Attributes:
    ----------
    :param inputFormat:
    :param outputFormat:
    :param invalidPlaceholder:
    :param kwargs:
    """
    self._attrs["formatter"] = 'datetime'
    self._attrs["formatterParams"] = {"inputFormat": inputFormat, "outputFormat": outputFormat, "invalidPlaceholder": invalidPlaceholder}
    if kwargs:
      self._attrs["formatterParams"].update(kwargs)
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
    self._attrs["formatter"] = 'tickCross'
    self._attrs["formatterParams"] = {'allowEmpty': allowEmpty, 'allowTruthy': allowTruthy, 'tickElement': tickElement,
                                      'crossElement': crossElement}
    if kwargs:
      self._attrs["formatterParams"].update(kwargs)
    return self

  def color(self, **kwargs):
    """
    Description:
    -----------
    The color formater sets the background colour of the cell to the value. The cell's value can be any valid CSS color eg. #ff0000, #f00, rgb(255,0,0), red, rgba(255,0,0,0), hsl(0, 100%, 50%)

    Related Pages:
http://tabulator.info/docs/4.1/format
    """
    self._attrs["formatter"] = 'color'
    if kwargs:
      self._attrs["formatterParams"] = kwargs
    return self

  def star(self, starts, **kwargs):
    """
    Description:
    -----------
    The star formater displays a graphical star rating based on integer values.

    Related Pages:
http://tabulator.info/docs/4.1/format

    Attributes:
    ----------
    :param starts: maximum number of stars to be displayed (default 5)
    """
    self._attrs["formatter"] = 'star'
    formatParams = {"starts": starts}
    for k, v in kwargs.items():
      formatParams[k] = v
    self._attrs["formatterParams"] = formatParams
    return self

  def progress(self, min=0, max=100, color=None, legend=None, legendColor=None, legendAlign=None, **kwargs):
    """

    :param min:
    :param max:
    :param color:
    :param legend:
    :param legendColor:
    :param legendAlign:
    :param kwargs:
    """
    self._attrs["formatter"] = 'progress'
    if kwargs:
      self._attrs["formatterParams"] = kwargs
    return self

  def lookup(self, data, **kwargs):
    """
    Description:
    -----------
    The lookup formater looks up the value to display from a object passed into the formatterParams property, if not present it displays the current cell value

    Related Pages:
http://tabulator.info/docs/4.1/format

    Attributes:
    ----------
    :param data: Dictionary for the lookup
    """
    self._attrs["formatter"] = 'lookup'
    self._attrs['formatterParams'] = data
    if kwargs:
      self._attrs["formatterParams"].update(kwargs)
    return self

  def custom(self, value):
    """

    :param value:
    """
    self._attrs["formatter"] = JsObjects.JsObjects.get(value)
    return self

  def wrapper(self, formatter, css_attrs, formatterParams=None):
    """

    .formatters.wrapper("progress", {"height": '6px'}, {'color': ['orange', 'green']})
    
    :param formatter:
    :param css_attrs:
    :param formatterParams:
    """
    self._attrs["formatter"] = JsObjects.JsObjects.get('''
      function(cell, formatterParams){ 
        const cssAttrs = formatterParams.css;
        var cell = cell.getTable().modules.format.getFormatter('%s').call(cell.getTable().modules.format, cell, formatterParams);
        let frag = document.createRange().createContextualFragment(cell).firstChild;
        Object.keys(cssAttrs).forEach(function(key){frag.style[key] = cssAttrs[key]}); 
        return frag; }''' % formatter)
    self._attrs['formatterParams'] = formatterParams or {}
    self._attrs['formatterParams']['css'] = css_attrs
    return self


class Validators(DataGroup):

  def required(self):
    """
    Description:
    -----------
    The required validator allows values that are not null or an empty string

    Related Pages:
http://tabulator.info/docs/4.5/validate
    """
    self._attrs["validator"].append('required')
    return self

  def unique(self):
    """
    Description:
    -----------
    The unique validator allows values that do not match the value of any other cell in this column

    Related Pages:
http://tabulator.info/docs/4.5/validate
    """
    self._attrs["validator"].append('unique')
    return self

  def integer(self):
    """
    Description:
    -----------
    The integer validator allows values that are valid integers

    Related Pages:
http://tabulator.info/docs/4.5/validate
    """
    self._attrs["validator"].append('integer')
    return self

  def float(self):
    """
    Description:
    -----------
    The float validator allows values that are valid floats

    Related Pages:
http://tabulator.info/docs/4.5/validate
    """
    self._attrs["validator"].append('float')
    return self

  def numeric(self):
    """
    Description:
    -----------
    The float validator allows values that are valid floats

    Related Pages:
http://tabulator.info/docs/4.5/validate
    """
    self._attrs["validator"].append('numeric')
    return self

  def min(self, val):
    """
    Description:
    -----------
    The min validator allows numeric values that are greater than or equal to parameter

    Related Pages:
http://tabulator.info/docs/4.5/validate
    """
    self._attrs["validator"].append('min:%s' % val)
    return self

  def max(self, val):
    """
    Description:
    -----------
    The max validator allows numeric values that are less than or equal to parameter

    Related Pages:
http://tabulator.info/docs/4.5/validate
    """
    self._attrs["validator"].append('max:%s' % val)
    return self

  def maxLength(self, val):
    """
    Description:
    -----------
    The maxLength validator allows string values that have a length less than or equal to parameter

    Related Pages:
http://tabulator.info/docs/4.5/validate
    """
    self._attrs["validator"].append('maxLength:%s' % val)
    return self

  def list(self, vals):
    """
    Description:
    -----------
    The in validator allows that values that match a value from the | delimieted string in the parameter

    Related Pages:
http://tabulator.info/docs/4.5/validate
    """
    self._attrs["validator"].append('in:%s' % "".join(map(lambda  x: str(), vals)))
    return self

  def regex(self, val):
    """
    Description:
    -----------
    The regex validator allows values that match the supplied regex

    Related Pages:
http://tabulator.info/docs/4.5/validate
    """
    self._attrs["validator"].append('regex:%s' % val)
    return self


class Extensions(DataGroup):

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

    return TbEditors.ExtsEditors(self._report, self._attrs, parent=self)

  @property
  def formatters(self):
    """
    Description:
    -----------
    You can set cell formatters on a per column basis using the formatter option in the column definition object.

    You can pass an optional additional parameter with the formatter, formatterParams that should contain an object with additional information for configuring the formatter.

    Related Pages:
http://tabulator.info/docs/4.0/format
    """
    from epyk.core.html.tables.exts import TbFormatters

    return TbFormatters.ExtsFormattors(self._report, self._attrs, parent=self)

  @property
  def mutators(self):
    """
    Description:
    -----------
    Mutators are used to alter data as it is parsed into Tabulator.
    For example if you wanted to convert a numeric column into a boolean based on its value, before the data is used to build the table.

    Related Pages:
http://tabulator.info/docs/4.0/mutators
    """
    from epyk.core.html.tables.exts import TbMutators

    return TbMutators.ExtsMutators(self._report, self._attrs, parent=self)

  @property
  def validators(self):
    """
    Description:
    -----------
    The validate module allows for validation of editied data before it is stored in the table.
    More information on these functions can be found in the Validation Documentation.
    This can be extended to add custom validator functions to the default list:

    Related Pages:
http://tabulator.info/docs/4.0/modules
    """
    from epyk.core.html.tables.exts import TbValidators

    return TbValidators.ExtsValidators(self._report, self._attrs, parent=self)


class Column(DataClass):

  @property
  def align(self):
    """
    Description:
    -----------
    sets the text alignment for this column (left|center|right)

    Related Pages:
http://tabulator.info/docs/4.5/columns
    """
    return self._attrs["align"]

  @align.setter
  def align(self, val):
    self._attrs["align"] = val

  @property
  def bottomCalc(self):
    """
    Description:
    -----------
    the column calculation to be displayed at the bottom of this column(see Column Calculations for more details)

    Related Pages:
http://tabulator.info/docs/4.5/columns
    """
    return self._attrs["bottomCalc"]

  @bottomCalc.setter
  def bottomCalc(self, val):
    self._attrs["bottomCalc"] = val

  @property
  def bottomCalcParams(self):
    """
    Description:
    -----------
    additional parameters you can pass to the bottomCalc calculation function(see Column Calculations for more details)

    Related Pages:
http://tabulator.info/docs/4.5/columns

    :rtype: BottomCalcParams
    """
    return self.sub_data("bottomCalcParams", BottomCalcParams)

  @property
  def cssClass(self):
    """

    :rtype: EnumColCss
    """
    return self.has_attribute(EnumColCss)

  @property
  def editable(self):
    """
    Description:
    -----------
    callback to check if the cell is editable (see Manipulating Data for more details)

    Related Pages:
http://tabulator.info/docs/4.5/columns
    """
    return self._attrs["editable"]

  @editable.setter
  def editable(self, val):
    self._attrs["editable"] = val

  @property
  def exts(self):
    """
    Description:
    -----------
    Tabulator is built in a modular fashion with a core codebase providing basic table rendering functionality and a series of modules that provide all of its wonderfull features.

    Related Pages:
http://tabulator.info/docs/4.0/modules
    """
    return Extensions(self._report, self._attrs, parent=self)

  @property
  def editors(self):
    """
    Description:
    -----------
    Tabulator comes with a number of built-in editors including:

    http://tabulator.info/docs/4.5/edit#edit-builtin
    """
    return Editor(self, self._attrs)

  @property
  def field(self):
    """
    Description:
    -----------
    Required (not required in icon/button columns) this is the key for this column in the data array

    Related Pages:
http://tabulator.info/docs/4.5/columns
    """
    return self._attrs["field"]

  @field.setter
  def field(self, val):
    self._attrs["field"] = val

  @property
  def formatters(self):
    """
    Description:
    -----------
    You can set cell formatters on a per column basis using the formatter option in the column definition object.

    Related Pages:
http://tabulator.info/docs/4.5
    """
    return Formattors(self, self._attrs)

  @property
  def frozen(self):
    """
    Description:
    -----------
    freezes the column in place when scrolling (see Frozen Columns for more details)

    Related Pages:
http://tabulator.info/docs/4.5/columns
    """
    return self._attrs["frozen"]

  @frozen.setter
  def frozen(self, val):
    self._attrs["frozen"] = val

  @property
  def headerVertical(self):
    """
    Description:
    -----------
    change the orientation of the column header to vertical (see Vertical Column Headers for more details)

    Related Pages:
http://tabulator.info/docs/4.5/columns
    """
    return self._attrs["headerVertical"]

  @headerVertical.setter
  def headerVertical(self, val):
    self._attrs["headerVertical"] = val

  @property
  def headerSort(self):
    """
    Description:
    -----------
    user can sort by clicking on the header (see Sorting Data for more details)

    Related Pages:
http://tabulator.info/docs/4.5/columns
    """
    return self._attrs["headerSort"]

  @headerSort.setter
  def headerSort(self, val):
    self._attrs["headerSort"] = val

  @property
  def headerVisible(self):
    """
    Description:
    -----------
    By setting the headerVisible option to false you can hide the column headers and present the table as a simple list if needed.

    Related Pages:
http://tabulator.info/docs/4.5/columns
    """
    return self._attrs["headerVisible"]

  @headerVisible.setter
  def headerVisible(self, val):
    self._attrs["headerVisible"] = val

  @property
  def sorter(self):
    """
    Description:
    -----------
    By default Tabulator will attempt to guess which sorter should be applied to a column based on the data contained in the first row.

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
    sets the width of this column, this can be set in pixels or as a percentage of total table width (if not set the system will determine the best)

    Related Pages:
http://tabulator.info/docs/4.5/columns
    """
    return self._attrs["width"]

  @width.setter
  def width(self, val):
    self._attrs["width"] = val

  @property
  def minwidth(self):
    """
    Description:
    -----------
    sets the minimum width of this column, this should be set in pixels (this takes priority over the global option of columnMinWidth)

    Related Pages:
http://tabulator.info/docs/4.1/columns
    """
    return self._attrs["minwidth"]

  @minwidth.setter
  def minwidth(self, val):
    self._attrs["minwidth"] = val

  @property
  def widthGrow(self):
    """
    Description:
    -----------
    when using fitColumns layout mode, determines how much the column should grow to fill available space (see Table Layout for more details)

    Related Pages:
http://tabulator.info/docs/4.5/columns
    """
    return self._attrs["widthGrow"]

  @widthGrow.setter
  def widthGrow(self, val):
    self._attrs["widthGrow"] = val

  @property
  def responsive(self):
    """
    Description:
    -----------
    an integer to determine when the column should be hidden in responsive mode (see Responsive Layout for more details)

    Related Pages:
http://tabulator.info/docs/4.5/columns
    """
    return self._attrs["responsive"]

  @responsive.setter
  def responsive(self, val):
    self._attrs["responsive"] = val

  @property
  def resizable(self):
    """
    Description:
    -----------
    set whether column can be resized by user dragging its edges (see Table Layout for more details)

    Related Pages:
http://tabulator.info/docs/4.5/columns
    """
    return self._attrs["resizable"]

  @resizable.setter
  def resizable(self, val):
    self._attrs["resizable"] = val

  @property
  def title(self):
    """
    Description:
    -----------
    Required This is the title that will be displayed in the header for this column

    Related Pages:
http://tabulator.info/docs/4.5/columns
    """
    return self._attrs["title"]

  @title.setter
  def title(self, val):
    self._attrs["title"] = val

  @property
  def titleFormatter(self):
    """
    Description:
    -----------
    formatter function for header title (see Formatting Data for more details)

    Related Pages:
http://tabulator.info/docs/4.5/columns
    """
    return self._attrs["titleFormatter"]

  @titleFormatter.setter
  def titleFormatter(self, val):
    self._attrs["titleFormatter"] = val

  @property
  def topCalc(self):
    """
    Description:
    -----------
    the column calculation to be displayed at the top of this column(see Column Calculations for more details)

    Related Pages:
http://tabulator.info/docs/4.5/columns
    """
    return self._attrs["topCalc"]

  @topCalc.setter
  def topCalc(self, val):
    self._attrs["topCalc"] = val

  @property
  def validator(self):
    """
    Description:
    -----------
    set the validator to be used to approve data when a user edits a cell. (see Manipulating Data for more details)

    Related Pages:
http://tabulator.info/docs/4.5/validate
    """
    self._attrs["validator"] = []
    return Validators(self, self._attrs)


class TableConfig(DataClass):

  @property
  def ajaxURL(self):
    """
    Description:
    -----------

    Related Pages:
http://tabulator.info/docs/4.0/data
    """
    return self._attrs["ajaxURL"]

  @ajaxURL.setter
  def ajaxURL(self, val):
    self._attrs["ajaxURL"] = val

  @property
  def ajaxProgressiveLoad(self):
    """
    Description:
    -----------

    Related Pages:
http://tabulator.info/docs/4.0/data
    """
    return self._attrs["ajaxProgressiveLoad"]

  @ajaxProgressiveLoad.setter
  def ajaxProgressiveLoad(self, val):
    self._attrs["ajaxProgressiveLoad"] = val

  @property
  def autoColumns(self):
    """
    Description:
    -----------
    If you set the autoColumns option to true, every time data is loaded into the table through the data option or through the setData function, Tabulator will examine the first row of the data and build columns to match that data.

    Related Pages:
http://tabulator.info/docs/4.2/columns
    """
    return self._attrs["autoColumns"]

  @autoColumns.setter
  def autoColumns(self, val):
    self._attrs["autoColumns"] = val

  @property
  def addRowPos(self):
    """
    Description:
    -----------
    The position in the table for new rows to be added, "bottom" or "top"

    Related Pages:
http://tabulator.info/docs/4.2/options
    """
    return self._attrs["addRowPos"]

  @addRowPos.setter
  def addRowPos(self, val):
    self._attrs["addRowPos"] = val

  @property
  def clipboard(self):
    """
    Description:
    -----------
    Enable clipboard module

    Related Pages:
http://tabulator.info/docs/4.2/options
    """
    return self._attrs["clipboard"]

  @clipboard.setter
  def clipboard(self, val):
    self._attrs["clipboard"] = val

  @property
  def clipboardPasteAction(self):
    """
    Description:
    -----------
    Clipboard paste action function

    Related Pages:
http://tabulator.info/docs/4.2/options
    """
    return self._attrs["clipboardPasteAction"]

  @clipboardPasteAction.setter
  def clipboardPasteAction(self, val):
    self._attrs["clipboardPasteAction"] = val

  @property
  def columns(self):
    """
    Description:
    -----------
    Holder for column definition array

    Related Pages:
http://tabulator.info/docs/4.2/options

    :rtype: Column
    """
    return self.sub_data_enum("columns", Column)

  @property
  def columns_group(self):
    """

    Related Pages:
http://tabulator.info/docs/4.2/options

    :rtype: ColumnsGroup
    """
    return self.sub_data_enum("columns", ColumnsGroup)

  @property
  def columnVertAlign(self):
    """
    Description:
    -----------
    Vertical alignment for contents of column header (used in column grouping)

    Related Pages:
http://tabulator.info/docs/4.2/options
    """
    return self._attrs["columnVertAlign"]

  @columnVertAlign.setter
  def columnVertAlign(self, val):
    self._attrs["columnVertAlign"] = val

  @property
  def data(self):
    """
    Description:
    -----------
    Array to hold data that should be loaded on table creation

    Related Pages:
http://tabulator.info/docs/4.2/options
    """
    return self._attrs["data"]

  @data.setter
  def data(self, val):
    self._attrs["data"] = val

  @property
  def groupBy(self):
    """
    Description:
    -----------
    String/function to select field to group rows by

    Related Pages:
http://tabulator.info/docs/4.2/options
    """
    return self._attrs["groupBy"]

  @groupBy.setter
  def groupBy(self, val):
    self._attrs["groupBy"] = val

  @property
  def groupToggleElement(self, val):
    """
    Description:
    -----------
    By default Tabulator allows users to toggle a group open or closed by clicking on the arrow icon in the left of the group header. If you would prefer a different behaviour you can use the groupToggleElement option to choose a different option:

    Related Pages:
http://tabulator.info/docs/4.0/group

    :param val:
    """
    self._attrs["groupToggleElement"] = val

  @groupToggleElement.setter
  def groupToggleElement(self, val):
    self._attrs["groupToggleElement"] = val

  @property
  def groupStartOpen(self):
    """
    Description:
    -----------
    You can set the default open state of groups using the groupStartOpen property.

    Related Pages:
http://tabulator.info/docs/4.0/group
    """
    return self._attrs["groupStartOpen"]

  @groupStartOpen.setter
  def groupStartOpen(self, val):
    self._attrs["groupStartOpen"] = val

  @property
  def groupValues(self):
    """
    Description:
    -----------
    Array of values for groups

    Related Pages:
http://tabulator.info/docs/4.2/options
    """
    return self._attrs["groupValues"]

  @groupValues.setter
  def groupValues(self, val):
    self._attrs["groupValues"] = val

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
    return self._attrs["height"]

  @height.setter
  def height(self, val):
    if isinstance(val, int):
      val = "%spx" % val
    self._attrs["height"] = val

  @property
  def history(self):
    """
    Description:
    -----------
    Enable user interaction history functionality

    Related Pages:
http://tabulator.info/docs/4.2/options
    """
    return self._attrs["history"]

  @history.setter
  def history(self, val):
    self._attrs["history"] = val

  @property
  def lang(self):
    """
    Description:
    -----------
    hold localization templates

    Related Pages:
http://tabulator.info/docs/4.2/options
    """
    return self._attrs["lang"]

  @lang.setter
  def lang(self, val):
    self._attrs["lang"] = val

  @property
  def layout(self):
    """
    Description:
    -----------
    Layout mode for the table columns

    Related Pages:
http://tabulator.info/docs/4.2/options

    :rtype: EnumLayout
    """
    return self.sub_data("layout", EnumLayout)

  @property
  def movableColumns(self):
    """
    Description:
    -----------
    Allow users to move and reorder columns

    Related Pages:
http://tabulator.info/docs/4.2/options
    """
    return self._attrs["movableColumns"]

  @movableColumns.setter
  def movableColumns(self, val):
    self._attrs["movableColumns"] = val

  @property
  def movableRows(self):
    """
    Description:
    -----------
    Allow users to move and reorder rows

    Related Pages:
http://tabulator.info/docs/4.2/options
    """
    return self._attrs["movableRows"]

  @movableRows.setter
  def movableRows(self, val):
    self._attrs["movableRows"] = val

  @property
  def movableRowsConnectedTables(self):
    """
    Description:
    -----------
    Connection selector for receving tables

    Related Pages:
http://tabulator.info/docs/4.2/options
    """
    return self._attrs["movableRowsConnectedTables"]

  @movableRowsConnectedTables.setter
  def movableRowsConnectedTables(self, val):
    self._attrs["movableRowsConnectedTables"] = val

  @property
  def movableRowsReceiver(self):
    """
    Description:
    -----------
    Sender function to be executed when row has been received

    Related Pages:
http://tabulator.info/docs/4.2/options
    """
    return self._attrs["movableRowsReceiver"]

  @movableRowsReceiver.setter
  def movableRowsReceiver(self, val):
    self._attrs["movableRowsReceiver"] = val

  @property
  def movableRowsSender(self):
    """
    Description:
    -----------
    Sender function to be executed when row has been sent

    Related Pages:
http://tabulator.info/docs/4.2/options
    """
    return self._attrs["movableRowsSender"]

  @movableRowsSender.setter
  def movableRowsSender(self, val):
    self._attrs["movableRowsSender"] = val

  @property
  def pagination(self):
    """
    Description:
    -----------
    Choose pagination method, "local" or "remote"

    Related Pages:
http://tabulator.info/docs/4.2/options
    """
    return self._attrs["pagination"]

  @pagination.setter
  def pagination(self, val):
    self._attrs["pagination"] = val

  @property
  def paginationSize(self):
    """
    Description:
    -----------
    Set the number of rows in each page

    Related Pages:
http://tabulator.info/docs/4.2/options
    """
    return self._attrs["paginationSize"]

  @paginationSize.setter
  def paginationSize(self, val):
    if val is not None:
      #
      self._attrs["pagination"]= 'local'
    self._attrs["paginationSize"] = val

  @property
  def paginationSizeSelector(self):
    """
    Description:
    -----------
    Add page size selection select element to the table footer

    Related Pages:
http://tabulator.info/docs/4.2/options
    """
    return self._attrs["paginationSizeSelector"]

  @paginationSizeSelector.setter
  def paginationSizeSelector(self, val):
    self._attrs["paginationSizeSelector"] = val

  @property
  def persistenceID(self):
    """
    Description:
    -----------
    ID tag used to identify persistent storage information

    Related Pages:
http://tabulator.info/docs/4.2/options
    """
    return self._attrs["persistenceID"]

  @persistenceID.setter
  def persistenceID(self, val):
    self._attrs["persistenceID"] = val

  @property
  def persistence(self):
    """
    Description:
    -----------
    The persistence system has received an overhaul in this release, providing a more consistent way to configure table persistence and allow even more table options to be persisted between sessions.

    Related Pages:
http://tabulator.info/docs/4.5/release#persistence

    :rtype: Persistence
    """
    return self.sub_data("persistence", Persistence)

  @property
  def placeholder(self):
    """
    Description:
    -----------
    placeholder element to display on empty table

    Related Pages:
http://tabulator.info/docs/4.2/options
    """
    return self._attrs["placeholder"]

  @placeholder.setter
  def placeholder(self, val):
    self._attrs["placeholder"] = val

  @property
  def printAsHtml(self):
    return self._attrs["printAsHtml"]

  @printAsHtml.setter
  def printAsHtml(self, val):
    self._attrs["printAsHtml"] = val

  @property
  def printHeader(self):
    return self._attrs["printHeader"]

  @printHeader.setter
  def printHeader(self, val):
    self._attrs["printHeader"] = val

  @property
  def printFooter(self):
    return self._attrs["printFooter"]

  @printFooter.setter
  def printFooter(self, val):
    self._attrs["printFooter"] = val

  @property
  def reactiveData(self):
    """
    Description:
    -----------
    enable data reactivity

    Related Pages:
http://tabulator.info/docs/4.2/options
    """
    return self._attrs["reactiveData"]

  @reactiveData.setter
  def reactiveData(self, val):
    self._attrs["reactiveData"] = val

  @property
  def responsiveLayout(self):
    """
    Description:
    -----------
    Automatically hide/show columns to fit the width of the Tabulator element

    Related Pages:
http://tabulator.info/docs/4.2/options
    """
    return self._attrs["responsiveLayout"]

  @responsiveLayout.setter
  def responsiveLayout(self, val):
    self._attrs["responsiveLayout"] = val

  @property
  def resizableColumns(self):
    """
    Description:
    -----------
    Allow user to resize columns (via handles on the left and right edges of the column header)

    Related Pages:
http://tabulator.info/docs/4.2/options
    """
    return self._attrs["resizableColumns"]

  @resizableColumns.setter
  def resizableColumns(self, val):
    self._attrs["resizableColumns"] = val

  @property
  def selectable(self):
    """
    Description:
    -----------
    Enable/Disable row selection

    Related Pages:
http://tabulator.info/docs/4.2/options
    """
    return self._attrs["selectable"]

  @selectable.setter
  def selectable(self, val):
    self._attrs["selectable"] = val


class TableTreeConfig(TableConfig):

  @property
  def dataTree(self):
    return self._attrs["dataTree"]

  @dataTree.setter
  def dataTree(self, val):
    self._attrs["dataTree"] = val

  @property
  def dataTreeStartExpanded(self):
    return self._attrs["dataTreeStartExpanded"]

  @dataTreeStartExpanded.setter
  def dataTreeStartExpanded(self, val):
    self._attrs["dataTreeStartExpanded"] = val
