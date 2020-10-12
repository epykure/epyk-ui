
from epyk.core.js.packages import packageImport
from epyk.core.data.DataClass import DataGroup


class ExtsFormattors(DataGroup):

  @packageImport('tabulator-icons')
  def icon(self, css=None, tags=None, **kwargs):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param css:
    :param tags:
    :param kwargs:
    """
    self._attrs["formatter"] = 'icon'
    self._attrs["formatterParams"] = {}
    if css is not None:
      self._attrs["css"] = css
    if tags is not None:
      self._attrs["tags"] = tags
    for k, v in kwargs.items():
      self._attrs["formatterParams"][k] = v
    return self

  @packageImport('tabulator-icons')
  def icon_pivot(self, iconMapping, pivot=None, cssMapping=None, tags=None, **kwargs):
    """
    Description:
    -----------
    Set an icon in the cell based on a lookup table based on another value in the row
    Default will take the cell value as icon classname

    Attributes:
    ----------
    :param pivot: String. The column field in the row
    :param iconMapping: Dictionary. A Icon classname mapping
    :param cssMapping: Dictionary. A CSS mapping for the icons containers
    :param tags: Optional. A dictionary with the different Dom tags to be addeed
    :param kwargs:
    """
    self._attrs["formatter"] = 'iconMapPivot'
    self._attrs["formatterParams"] = {'pivot': pivot or self._attrs["field"], 'iconMapping': iconMapping}
    if cssMapping is not None:
      self._attrs["cssMapping"] = cssMapping
    if tags is not None:
      self._attrs["tags"] = tags
    for k, v in kwargs.items():
      self._attrs["formatterParams"][k] = v
    return self

  @packageImport('tabulator-inputs')
  def password(self, css=None, **kwargs):
    """
    Description:
    -----------
    Change the content of the cell to ****

    Attributes:
    ----------
    :param css: Dictionary. The CSS attributes for the cell (Optional)
    :param kwargs:
    """
    self._attrs["formatter"] = 'password'
    formatParams = {}
    if css is not None:
      formatParams['css'] = css
    for k, v in kwargs.items():
      formatParams[k] = v
    return self

  @packageImport('tabulator-numbers')
  def label_thresholds(self, thresholds, labels, css=None, **kwargs):
    """
    Description:
    -----------
    Set a label based on a list of values

    Attributes:
    ----------
    :param thresholds: List. The different values to compare to deduce the category
    :param labels: List. The resulting category
    :param css: Dictionary. The CSS attributes for the cell (Optional)
    :param kwargs:
    """  #
    self._attrs["formatter"] = 'labelThresholds'
    formatParams = {'thresholds': thresholds, 'labels': labels}
    if css is not None:
      formatParams['css'] = css
    if kwargs:
      self._attrs["formatterParams"].update(kwargs)
    return self

  @packageImport('tabulator-numbers')
  def label_thresholds_pivot(self, pivot, thresholds, labels, css=None, **kwargs):
    """
    Description:
    -----------
    Set a label based on a list of values from another column

    Attributes:
    ----------
    :param pivot: String. The column name to use to get the data to lookup from te row
    :param thresholds: List. The different values to compare to deduce the category
    :param labels: List. The resulting category
    :param css: Dictionary. The CSS attributes for the cell (Optional)
    :param kwargs:
    """  #
    self._attrs["formatter"] = 'flagThresholdsPivot'
    formatParams = {'thresholds': thresholds, 'labels': labels, 'pivot': pivot}
    if css is not None:
      formatParams['css'] = css
    if kwargs:
      self._attrs["formatterParams"].update(kwargs)
    return self

  @packageImport('tabulator-numbers')
  def previous(self, decimal=".", thousand=",", precision=0, symbol="", format="%v", css=None, **kwargs):
    """

    :param decimal: String. decimal point separator default "."
    :param thousand: String. thousands separator default ","
    :param precision: Integer. decimal places default 0
    :param symbol: default currency symbol is ''
    :param format:
    :param css: Dictionary. The CSS attributes for the cell (Optional)
    :param kwargs:
    """  #
    self._attrs["formatter"] = 'numbersPrevious'
    self._attrs["formatterParams"] = {k: v for k, v in locals().items() if k != 'self' and v is not None}
    self._attrs["formatterParams"].update(self._attrs["formatterParams"].pop('kwargs'))
    return self

  @packageImport('tabulator-numbers')
  def number(self, decimal=".", thousand=",", precision=0, symbol="", format="%v", css=None, **kwargs):
    """

    :param decimal: String. decimal point separator default "."
    :param thousand: String. thousands separator default ","
    :param precision: Integer. decimal places default 0
    :param symbol: default currency symbol is ''
    :param format:
    :param css: Dictionary. The CSS attributes for the cell (Optional)
    :param kwargs:
    """  #
    self._attrs["formatter"] = 'numbers'
    self._attrs["formatterParams"] = {k: v for k, v in locals().items() if k != 'self' and v is not None}
    self._attrs["formatterParams"].update(self._attrs["formatterParams"].pop('kwargs'))
    return self

  @packageImport('tabulator-numbers')
  def number_format(self, decimal=".", thousand=",", precision=0, symbol="", format="%v", colors=None,
                              threshold=0, css=None, **kwargs):
    """
    Description:
    -----------
    
    Attributes:
    ----------
    :param decimal: String. decimal point separator default "."
    :param thousand: String. thousands separator default ","
    :param precision: Integer. decimal places default 0
    :param symbol: default currency symbol is ''
    :param format: String. "%s%v" controls output: %s = symbol, %v = value/number (can be object: see below)
    :param css: Dictionary. The CSS attributes for the cell (Optional)
    :param kwargs:
    """  #
    if colors is None:
      colors = [self._report._report.theme.danger[1], self._report._report.theme.greys[-1]]
    self._attrs["formatter"] = 'numbersFormat'
    self._attrs["formatterParams"] = {k: v for k, v in locals().items() if k != 'self' and v is not None}
    self._attrs["formatterParams"].update(self._attrs["formatterParams"].pop('kwargs'))
    return self

  @packageImport('tabulator-numbers')
  def number_difference(self, decimal=None, thousand=None, precision=None, symbol=None, format=None,
                                  colors=None, threshold=0, css=None, **kwargs):
    """
    Description:
    -----------
    
    Attributes:
    ----------
    :param decimal: String. decimal point separator default "."
    :param thousand: String. thousands separator default ","
    :param precision: Integer. decimal places default 0
    :param symbol: default currency symbol is ''
    :param format: String. "%s%v" controls output: %s = symbol, %v = value/number (can be object: see below)
    :param colors: List. Color before and after the threshold (default red and green according to the theme)
    :param threshold: Integer. The threshold number
    :param css: Dictionary. The CSS attributes for the cell (Optional)
    :param kwargs:
    """  #
    if colors is None:
      colors = [self._report._report.theme.danger[1], self._report._report.theme.success[1]]
    self._attrs["formatter"] = 'numbersDifference'
    self._attrs["formatterParams"] = {k: v for k, v in locals().items() if k != 'self' and v is not None}
    self._attrs["formatterParams"].update(self._attrs["formatterParams"].pop('kwargs'))
    return self

  @packageImport('tabulator-numbers')
  def number_thresholds(self, thresholds, css, **kwargs):
    """
    Description:
    -----------
    
    Attributes:
    ----------
    :param thresholds:
    :param css:
    :param kwargs:
    """  #
    self._attrs["formatter"] = 'numbersThreshold'
    self._attrs["formatterParams"] = {'thresholds': thresholds, 'css': css}
    self._attrs["formatterParams"].update({k: v for k, v in locals().items() if k != 'self' and v is not None})
    self._attrs["formatterParams"].update(self._attrs["formatterParams"].pop('kwargs'))
    return self

  @packageImport('tabulator-numbers')
  def number_thresholds_pivot(self, pivot, thresholds, css, **kwargs):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param pivot:
    :param thresholds:
    :param css:
    :param kwargs:
    """
    self._attrs["formatter"] = 'numbersThresholdPivot'
    self._attrs["formatterParams"] = {'thresholds': thresholds, 'css': css, 'pivot': pivot}
    self._attrs["formatterParams"].update({k: v for k, v in locals().items() if k != 'self' and v is not None})
    self._attrs["formatterParams"].update(self._attrs["formatterParams"].pop('kwargs'))
    return self

  @packageImport('tabulator-drop')
  def drag_and_drop(self, row_delimiter="\n", col_delimiter="\t", css=None, **kwargs):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param row_delimiter: String
    :param col_delimiter: String
    :param css:
    :param kwargs:
    """
    self._attrs["formatter"] = 'dragAndDrop'
    self._attrs["formatterParams"] = {'css': css, 'rowDelimiter': row_delimiter, 'colDelimiter': col_delimiter}
    self._attrs["formatterParams"].update({k: v for k, v in locals().items() if k != 'self' and v is not None})
    self._attrs["formatterParams"].update(self._attrs["formatterParams"].pop('kwargs'))
    return self

  @packageImport('tabulator-numbers')
  def intensity(self, steps, colors, is_number=True, intensity=None, css=None, decimal=".", thousand=",", precision=0,
                symbol="", format="%v", **kwargs):
    """
    Description:
    -----------

    table.get_column("flag").exts.formatters.intensity(5, ["white", "red"], intensity="flag")

    Attributes:
    ----------
    :param steps:
    :param colors:
    :param is_number:
    :param intensity: String, The column used to deduce the intensity. Default the cell value.
    :param css:
    :param decimal:
    :param thousand:
    :param precision:
    :param symbol:
    :param format:
    :param kwargs:
    """
    self._attrs["formatter"] = 'numbersIntensity'
    self._attrs["formatterParams"] = {'steps': steps, 'colors': colors, 'is_number': is_number, 'decimal': decimal,
                                      'thousand': thousand, 'precision': precision, 'symbol': symbol, 'format': format}
    if intensity is not None:
      self._attrs["formatterParams"]['intensit'] = intensity
    if css is not None:
      self._attrs["formatterParams"]['css'] = css
    self._attrs["formatterParams"].update({k: v for k, v in locals().items() if k != 'self' and v is not None})
    self._attrs["formatterParams"].update(self._attrs["formatterParams"].pop('kwargs'))
    return self

  @packageImport('tabulator-numbers')
  def quality(self, steps, colors, intensity=None, quality=None, css=None, is_number=True, decimal=".", thousand=",", precision=0,
                symbol="", format="%v", **kwargs):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param steps:
    :param colors:
    :param intensity:
    :param quality:
    :param css:
    :param is_number:
    :param decimal:
    :param thousand:
    :param precision:
    :param symbol:
    :param format:
    :param kwargs:
    """
    self._attrs["formatter"] = 'numbersIntensity'
    self._attrs["formatterParams"] = {'steps': steps, 'colors': colors, 'is_number': is_number, 'decimal': decimal,
                                      'thousand': thousand, 'precision': precision, 'symbol': symbol, 'format': format}
    if intensity is not None:
      self._attrs["formatterParams"]['intensity'] = intensity
    if quality is not None:
      self._attrs["formatterParams"]['quality'] = quality
    if css is not None:
      self._attrs["formatterParams"]['css'] = css
    self._attrs["formatterParams"].update({k: v for k, v in locals().items() if k != 'self' and v is not None})
    self._attrs["formatterParams"].update(self._attrs["formatterParams"].pop('kwargs'))
    return self

  @packageImport('tabulator-numbers')
  def trafficlight(self, tooltip=None, green=None, red=None, orange=None, css=None, **kwargs):
    """
    Description:
    -----------

    Attributes:
    ----------
    :param tooltip: String. Optional. The column name for the details
    :param css: Dictionary. Optional. The CSS attributes
    :param kwargs:
    """
    if tooltip is not None:
      self._report.config.tooltips = True
    self._attrs["formatter"] = 'trafficLight'
    self._attrs["formatterParams"] = {'tooltip': tooltip, 'green': green or self._report._report.theme.success[1],
                                      'red': red or self._report._report.theme.danger[1],
                                      'orange': orange or self._report._report.theme.warning[1]}
    if css is not None:
      self._attrs["formatterParams"]['css'] = css
    self._attrs["formatterParams"].update({k: v for k, v in locals().items() if k != 'self' and v is not None})
    self._attrs["formatterParams"].update(self._attrs["formatterParams"].pop('kwargs'))
    return self

  @packageImport('tabulator-inputs')
  def lookup_pivot(self, lookups, pivot, css=None, **kwargs):
    """
    Description:
    -----------
    Set a label based on a list of values

    Attributes:
    ----------
    :param lookups:
    :param pivot:
    :param css: Dictionary. The CSS attributes for the cell (Optional)
    """
    self._attrs["formatter"] = 'lookupPivot'
    formatParams = {'lookups': lookups, "pivot": pivot}
    if css is not None:
      formatParams['css'] = css
    for k, v in kwargs.items():
      formatParams[k] = v
    self._attrs['formatterParams'] = formatParams
    return self

  def buttonTick(self, **kwargs):
    """
    Description:
    -----------
    The buttonTick formatter displays a tick icon on each row (for use as a button)

    Related Pages:
http://tabulator.info/docs/4.1/format
    """
    self._attrs["formatter"] = 'buttonTick'
    if kwargs:
      self._attrs["formatterParams"] = kwargs
    return self

  def buttonCross(self, **kwargs):
    """
    Description:
    -----------
    The buttonCross formatter displays a cross icon on each row (for use as a button)

    Related Pages:
http://tabulator.info/docs/4.1/format
    """
    self._attrs["formatter"] = 'buttonCross'
    if kwargs:
      self._attrs["formatterParams"] = kwargs
    return self

  def rownum(self, **kwargs):
    """
    Description:
    -----------
    The rownum formatter shows an incrementing row number for each row as it is displayed

    Related Pages:
http://tabulator.info/docs/4.1/format
    """
    self._attrs["formatter"] = 'rownum'
    if kwargs:
      self._attrs["editorParams"] = kwargs
    return self

  def handle(self, **kwargs):
    """
    Description:
    -----------
    The handle formatter fills the cell with hamburger bars, to be used as a row handle

    Related Pages:
http://tabulator.info/docs/4.1/format
    """
    self._attrs["formatter"] = 'handle'
    if kwargs:
      self._attrs["editorParams"] = kwargs
    return self

  @packageImport('tabulator-inputs')
  def style(self, css=None, valField=None, cssField=None, **kwargs):
    """
    Description:
    -----------

    Related Pages:
http://tabulator.info/docs/4.1/format

    Attributes:
    ----------
    :param css: Dictionary for the css style to apply
    :param cssField: Dictionary for the css style to apply
    :param valField:
    """
    if css is None and cssField is None:
      raise Exception("Both CSS and CSSField cannot be empty")

    self._attrs["formatter"] = 'cssStyle'
    self._attrs['formatterParams'] = {}
    if css is not None:
      self._attrs['formatterParams']['css'] = css
    if cssField is not None:
      self._attrs['formatterParams']['cssField'] = cssField
      self._attrs['formatterParams']['valField'] = valField
    if kwargs:
      self._attrs["formatterParams"].update(kwargs)
    return self

  @packageImport('tabulator-inputs')
  def style_pivot(self, cssMapping, pivot=None, **kwargs):
    self._attrs["formatter"] = 'cssStylePivot'
    self._attrs['formatterParams'] = {'cssMapping': cssMapping}
    if pivot is not None:
      self._attrs['formatterParams']['pivot'] = pivot
    if kwargs:
      self._attrs["formatterParams"].update(kwargs)
    return self

  def custom(self, formatter, formatterParams, moduleAlias):
    """

    :param formatter:
    :param formatterParams:
    :param moduleAlias:
    """
    self._report.jsImports.add(moduleAlias)
    self._attrs["formatter"] = formatter
    self._attrs['formatterParams'] = formatterParams
    return self
