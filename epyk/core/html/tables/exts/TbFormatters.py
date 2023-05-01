#!/usr/bin/python
# -*- coding: utf-8 -*-

from epyk.core.js.packages import packageImport
from epyk.core.html.options import Enums


class ExtsFormattors(Enums):

    @packageImport('tabulator-icons')
    def icon(self, css=None, tags=None, events=None, **kwargs):
        """

        :param css: Dictionary. Optional. The CSS attributes for the cell (Optional).
        :param tags: Dictionary. Optional. The DOM attributes to be added to the icon holder (Optional).
        :param events: Dictionary. Optional. The DOM events to be added to the internal component.
        """
        formatter_params = {}
        if events is not None:
            formatter_params["events"] = events
        if css is not None:
            formatter_params["css"] = css
        if tags is not None:
            formatter_params["tags"] = tags
        for k, v in kwargs.items():
            formatter_params[k] = v
        self._set_value(value=formatter_params, name="formatterParams")
        return self._set_value()

    @packageImport('tabulator-icons')
    def button(self, css=None, tags=None, events=None, **kwargs):
        """

        :param css: Dictionary. Optional. The CSS attributes for the cell (Optional).
        :param tags: Dictionary. Optional. The DOM attributes to be added to the icon holder (Optional).
        :param events: Dictionary. Optional. The DOM events to be added to the internal component.
        """
        formatter_params = {}
        if events is not None:
            formatter_params["events"] = events
        if css is not None:
            formatter_params["css"] = css
        if tags is not None:
            formatter_params["tags"] = tags
        for k, v in kwargs.items():
            formatter_params[k] = v
        self._set_value(value=formatter_params, name="formatterParams")
        return self._set_value()

    @packageImport('tabulator-icons')
    def avatar(self, css=None, tags=None, events=None, **kwargs):
        """

        :param css: Dictionary. Optional. The CSS attributes for the cell (Optional).
        :param tags: Dictionary. Optional. The DOM attributes to be added to the icon holder (Optional).
        :param events: Dictionary. Optional. The DOM events to be added to the internal component.
        """
        formatter_params = {}
        if events is not None:
            formatter_params["events"] = events
        if css is not None:
            formatter_params["css"] = css
        if tags is not None:
            formatter_params["tags"] = tags
        for k, v in kwargs.items():
            formatter_params[k] = v
        self._set_value(value=formatter_params, name="formatterParams")
        return self._set_value()

    @packageImport('tabulator-icons')
    def remove(self, css=None, tags=None, events=None, **kwargs):
        """

        :param css: Dictionary. Optional. The CSS attributes for the cell (Optional).
        :param tags: Dictionary. Optional. The DOM attributes to be added to the icon holder (Optional).
        :param events: Dictionary. Optional. The DOM events to be added to the internal component.
        """
        formatter_params = {}
        if events is not None:
            formatter_params["events"] = events
        if css is not None:
            formatter_params["css"] = css
        if tags is not None:
            formatter_params["tags"] = tags
        for k, v in kwargs.items():
            formatter_params[k] = v
        self._set_value(value=formatter_params, name="formatterParams")
        self._set_value(value=25, name="width")
        return self._set_value()

    @packageImport('tabulator-icons')
    def runnable(self, css=None, tags=None, post=None, **kwargs):
        """

        :param css: Dictionary. Optional. The CSS attributes for the cell (Optional).
        :param tags: Dictionary. Optional. The DOM attributes to be added to the icon holder (Optional).
        :param post:
        """
        formatter_params = {}
        if post is not None:
            formatter_params["post"] = post
        if css is not None:
            formatter_params["css"] = css
        if tags is not None:
            formatter_params["tags"] = tags
        for k, v in kwargs.items():
            formatter_params[k] = v
        self._set_value(value=formatter_params, name="formatterParams")
        self._set_value(value=25, name="width")
        return self._set_value()

    @packageImport('tabulator-icons')
    def task(self, css=None, colors=None, **kwargs):
        """

        :param css: Dictionary. Optional. The CSS attributes for the cell (Optional).
        :param colors: List. Optional.
        """
        formatter_params = {}
        if css is not None:
            formatter_params["css"] = css
        if colors is not None:
            formatter_params["color"] = colors
        for k, v in kwargs.items():
            formatter_params[k] = v
        self._set_value(value=formatter_params, name="formatterParams")
        return self._set_value()

    @packageImport('tabulator-icons')
    def icon_pivot(self, iconMapping, pivot=None, cssMapping=None, tags=None, **kwargs):
        """
        Set an icon in the cell based on a lookup table based on another value in the row.

        Default will take the cell value as icon classname.

        :param pivot: String. The column field in the row.
        :param iconMapping: Dictionary. Optional. A Icon classname mapping.
        :param cssMapping: Dictionary. Optional. A CSS mapping for the icons containers.
        :param tags: Dictionary. Optional. A dictionary with the different Dom tags to be added.
        """
        formatter_params = {'pivot': pivot or self._attrs["field"], 'iconMapping': iconMapping}
        if cssMapping is not None:
            formatter_params["cssMapping"] = cssMapping
        if tags is not None:
            formatter_params["tags"] = tags
        for k, v in kwargs.items():
            formatter_params["formatterParams"][k] = v
        self._set_value(value=formatter_params, name="formatterParams")
        return self._set_value(value="iconMapPivot")

    @packageImport('tabulator-inputs')
    def password(self, css=None, **kwargs):
        """
        Change the content of the cell to ****.

        :param css: Dictionary. The CSS attributes for the cell (Optional).
        """
        formatter_params = {}
        if css is not None:
            formatter_params['css'] = css
        for k, v in kwargs.items():
            formatter_params[k] = v
        self._set_value(value=formatter_params, name="formatterParams")
        return self._set_value(value="password")

    @packageImport('tabulator-numbers')
    def label_thresholds(self, thresholds, labels, css=None, **kwargs):
        """
        Set a label based on a list of values.

        :param thresholds: List. The different values to compare to deduce the category.
        :param labels: List. The resulting category.
        :param css: Dictionary. Optional. The CSS attributes for the cell (Optional).
        """
        formatter_params = {'thresholds': thresholds, 'labels': labels}
        if css is not None:
            formatter_params['css'] = css
        if kwargs:
            formatter_params.update(kwargs)
        self._set_value(value=formatter_params, name="formatterParams")
        return self._set_value(value="labelThresholds")

    @packageImport('tabulator-numbers')
    def label_thresholds_pivot(self, pivot, thresholds, labels, css=None, **kwargs):
        """
        Set a label based on a list of values from another column.

        :param pivot: String. The column name to use to get the data to lookup from te row.
        :param thresholds: List. The different values to compare to deduce the category.
        :param labels: List. The resulting category.
        :param css: Dictionary. Optional. The CSS attributes for the cell (Optional).
        """
        formatter_params = {'thresholds': thresholds, 'labels': labels, 'pivot': pivot}
        if css is not None:
            formatter_params['css'] = css
        if kwargs:
            formatter_params.update(kwargs)
        self._set_value(value=formatter_params, name="formatterParams")
        return self._set_value(value="flagThresholdsPivot")

    @packageImport('tabulator-numbers')
    def previous(self, decimal=".", thousand=",", precision=0, symbol="", format="%v", css=None, **kwargs):
        """

        :param decimal: String. Optional. decimal point separator default ".".
        :param thousand: String. Optional. thousands separator default ",".
        :param precision: Integer. Optional. decimal places default 0.
        :param symbol: String. Optional. default currency symbol is ''.
        :param format: String. Optional.
        :param css: Dictionary. Optional. The CSS attributes for the cell (Optional).
        """
        formatter_params = {k: v for k, v in locals().items() if k != 'self' and v is not None}
        formatter_params.update(formatter_params.pop('kwargs'))
        self._set_value(value=formatter_params, name="formatterParams")
        return self._set_value(value="numbersPrevious")

    @packageImport('tabulator-numbers')
    def number(self, decimal: str = ".", thousand: str = ",", precision: int = 0, symbol: str = "", format: str = "%v",
               css: dict = None, **kwargs):
        """

        Usage::

          c = table.get_column("Share")
          c.exts.formatters.number(symbol="£", format="%v%s", precision=1, css={"color": "blue", "text-align": "center"})

        :param decimal: String. Optional. decimal point separator default ".".
        :param thousand: String. Optional. thousands separator default ",".
        :param precision: Integer. Optional. Decimal places default 0.
        :param symbol: String. Optional. default currency symbol is ''.
        :param format: String. Optional.
        :param css: Dictionary. Optional. The CSS attributes for the cell (Optional).
        """
        formatter_params = {"decimal": decimal, "thousand": thousand, "precision": precision, "symbol": symbol,
                            "format": format, "css": css or {}}
        if kwargs:
            formatter_params.update(kwargs)
        self._set_value(value=formatter_params, name="formatterParams")
        return self._set_value(value="numbers")

    @packageImport('tabulator-numbers')
    def trend(self, css: dict = None, **kwargs):
        """
        Add an arrow to illustrate the trend.

        Usage::

          c = table.get_column("Share")
          c.exts.formatters.trend()

        :param css: Optional. The CSS attributes for the cell (Optional)
        """
        formatter_params = {}
        if css is not None:
            formatter_params["css"] = css
        if kwargs:
            formatter_params.update(kwargs)
        self._set_value(value=formatter_params, name="formatterParams")
        return self._set_value(value="trend")

    @packageImport('tabulator-numbers')
    def detailed(self, decimal=".", thousand=",", precision=0, symbol="", format="%v", css=None, **kwargs):
        """

        The data in the cell must be a dictionary with the following attributes:
          - value
          - flag
          - move

        :param decimal:
        :param thousand:
        :param precision:
        :param symbol:
        :param format:
        :param css: Dictionary. The CSS attributes for the cell (Optional)
        """
        self.number(decimal, thousand, precision, symbol, format, css, **kwargs)
        return self._set_value(value="detailed")

    @packageImport('tabulator-numbers')
    def small(self, decimal=".", thousand=",", precision=0, symbol="", format="%v", css=None, **kwargs):
        """

        :param decimal:
        :param thousand:
        :param precision:
        :param symbol:
        :param format:
        :param css:
        """
        self.number(decimal, thousand, precision, symbol, format, css, **kwargs)
        return self._set_value(value="small")

    @packageImport('tabulator-numbers')
    def scale(self, css=None, colors=None, steps=None, decimal=".", thousand=",", precision=0, symbol="",
              format="%v", **kwargs):
        """

        :param css:
        :param colors:
        :param steps:
        :param decimal:
        :param thousand:
        :param precision:
        :param symbol:
        :param format:
        """
        attr = self.number(decimal, thousand, precision, symbol, format, css, **kwargs)
        if colors is not None:
            attr["formatterParams"]["colors"] = colors
        if steps is not None:
            attr["formatterParams"]["steps"] = steps
        return self._set_value(value="scale")

    @packageImport('tabulator-numbers')
    def number_format(self, decimal=".", thousand=",", precision=0, symbol="", format="%v", colors=None,
                      threshold=0, css=None, **kwargs):
        """

        :param decimal: String. Optional. Decimal point separator default ".".
        :param thousand: String. Optional. Thousands separator default ",".
        :param precision: Integer. Optional. Decimal places default 0.
        :param symbol: String. Optional. default currency symbol is ''.
        :param format: String. Optional. "%s%v" controls output: %s = symbol, %v = value/number (can be object: see below).
        :param css: Dictionary. Optional. The CSS attributes for the cell (Optional).
        """
        if colors is None:
            colors = [self.component.page.theme.danger.base, self.component.page.theme.greys[-1]]
        formatter_params = {k: v for k, v in locals().items() if k != 'self' and v is not None}
        formatter_params.update(formatter_params.pop('kwargs'))
        self._set_value(value=formatter_params, name="formatterParams")
        return self._set_value(value="numbersFormat")

    @packageImport('tabulator-numbers')
    def number_difference(self, decimal=None, thousand=None, precision=None, symbol=None, format=None,
                          colors=None, threshold=0, css=None, **kwargs):
        """

        :param decimal: String. Optional. Decimal point separator default ".".
        :param thousand: String. Optional. Thousands separator default ",".
        :param precision: Integer. Optional. Decimal places default 0.
        :param symbol: String. Optional. Default currency symbol is ''.
        :param format: String. Optional. "%s%v" controls output: %s = symbol, %v = value/number (can be object: see below).
        :param colors: List. Optional. Color before and after the threshold (default red and green according to the theme).
        :param threshold: Integer. Optional. The threshold number.
        :param css: Dictionary. Optional. The CSS attributes for the cell (Optional).
        """
        if colors is None:
            colors = [self.component.page.theme.danger.base, self.component.page.theme.success[1]]
        formatter_params = {k: v for k, v in locals().items() if k != 'self' and v is not None}
        formatter_params.update(formatter_params.pop('kwargs'))
        self._set_value(value=formatter_params, name="formatterParams")
        return self._set_value(value="numbersDifference")

    @packageImport('tabulator-numbers')
    def number_thresholds(self, thresholds, css, **kwargs):
        """

        :param thresholds:
        :param css:
        """
        formatter_params = {'thresholds': thresholds, 'css': css}
        formatter_params.update({k: v for k, v in locals().items() if k != 'self' and v is not None})
        formatter_params.update(formatter_params.pop('kwargs'))
        self._set_value(value=formatter_params, name="formatterParams")
        return self._set_value(value="numbersThreshold")

    @packageImport('tabulator-numbers')
    def number_thresholds_pivot(self, pivot, thresholds, css, **kwargs):
        """

        :param pivot:
        :param thresholds:
        :param css:
        """
        formatter_params = {'thresholds': thresholds, 'css': css, 'pivot': pivot}
        formatter_params.update({k: v for k, v in locals().items() if k != 'self' and v is not None})
        formatter_params.update(formatter_params.pop('kwargs'))
        self._set_value(value=formatter_params, name="formatterParams")
        return self._set_value(value="numbersThresholdPivot")

    @packageImport('tabulator-drop')
    def drag_and_drop(self, row_delimiter: str = "\n", col_delimiter: str = "\t", css: dict = None, **kwargs):
        """

        :param row_delimiter: Optional.
        :param col_delimiter: Optional.
        :param css: Optional.
        """
        formatter_params = {'css': css, 'rowDelimiter': row_delimiter, 'colDelimiter': col_delimiter}
        formatter_params.update({k: v for k, v in locals().items() if k != 'self' and v is not None})
        formatter_params.update(formatter_params.pop('kwargs'))
        self._set_value(value=formatter_params, name="formatterParams")
        return self._set_value(value="dragAndDrop")

    @packageImport('tabulator-numbers')
    def intensity(self, steps, colors, is_number=True, intensity=None, css=None, decimal=".", thousand=",", precision=0,
                  symbol="", format="%v", **kwargs):
        """

        Usage::

          table.get_column("flag").exts.formatters.intensity(5, ["white", "red"], intensity="flag")

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
        """
        formatter_params = {'steps': steps, 'colors': colors, 'is_number': is_number, 'decimal': decimal,
                            'thousand': thousand, 'precision': precision, 'symbol': symbol, 'format': format}
        if intensity is not None:
            formatter_params['intensit'] = intensity
        if css is not None:
            formatter_params['css'] = css
        formatter_params.update({k: v for k, v in locals().items() if k != 'self' and v is not None})
        formatter_params.update(formatter_params.pop('kwargs'))
        self._set_value(value=formatter_params, name="formatterParams")
        return self._set_value(value="numbersIntensity")

    @packageImport('tabulator-numbers')
    def quality(self, steps, colors, intensity=None, quality=None, css=None, is_number=True, decimal=".", thousand=",",
                precision=0, symbol="", format="%v", **kwargs):
        """

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
        """
        formatter_params = {'steps': steps, 'colors': colors, 'is_number': is_number, 'decimal': decimal,
                            'thousand': thousand, 'precision': precision, 'symbol': symbol, 'format': format}
        if intensity is not None:
            formatter_params['intensity'] = intensity
        if quality is not None:
            formatter_params['quality'] = quality
        if css is not None:
            formatter_params['css'] = css
        formatter_params.update({k: v for k, v in locals().items() if k != 'self' and v is not None})
        formatter_params.update(formatter_params.pop('kwargs'))
        self._set_value(value=formatter_params, name="formatterParams")
        return self._set_value(value="numbersIntensity")

    @packageImport('tabulator-numbers')
    def trafficlight(self, tooltip: str = None, green: str = None, red: str = None, orange: str = None,
                     css: dict = None,
                     **kwargs):
        """
        Put a traffic light in the cell with the color based on the value.

        Usage::

          c = table.get_column("Share")
          c.exts.formatters.trafficlight()

        :param tooltip: Optional. The column name for the details.
        :param green: Optional. The success color definition.
        :param red: Optional. The danger color definition.
        :param orange: Optional. The warning color definition.
        :param css: Optional. The CSS attributes.
        """
        if tooltip is not None:
            self.component.options.tooltips = True
        formatter_params = {'tooltip': tooltip, 'green': green or self.component.page.theme.success.base,
                            'red': red or self.component.page.theme.danger.base,
                            'orange': orange or self.component.page.theme.warning.base}
        if css is not None:
            formatter_params['css'] = css
        if kwargs:
            formatter_params.update(kwargs)
        self._set_value(value=formatter_params, name="formatterParams")
        return self._set_value(value="trafficLight")

    @packageImport('tabulator-inputs')
    def lookup_pivot(self, lookups, pivot, css: dict = None, **kwargs):
        """
        Set a label based on a list of values.

        :param lookups:
        :param pivot:
        :param css: Optional. The CSS attributes for the cell (Optional)
        """
        formatter_params = {'lookups': lookups, "pivot": pivot}
        if css is not None:
            formatter_params['css'] = css
        for k, v in kwargs.items():
            formatter_params[k] = v
        self._set_value(value=formatter_params, name="formatterParams")
        return self._set_value(value="lookupPivot")

    def buttonTick(self, **kwargs):
        """
        The buttonTick formatter displays a tick icon on each row (for use as a button).

        Related Pages:

          http://tabulator.info/docs/4.1/format
        """
        if kwargs:
            formatter_params = kwargs
            self._set_value(value=formatter_params, name="formatterParams")
        return self._set_value(value="buttonTick")

    def buttonCross(self, **kwargs):
        """
        The buttonCross formatter displays a cross icon on each row (for use as a button).

        Related Pages:

          http://tabulator.info/docs/4.1/format
        """
        if kwargs:
            self._set_value(value=kwargs, name="formatterParams")
        return self._set_value(value="buttonCross")

    def rownum(self, **kwargs):
        """
        The rownum formatter shows an incrementing row number for each row as it is displayed.

        Related Pages:

          http://tabulator.info/docs/4.1/format
        """
        if kwargs:
            self._set_value(value=kwargs, name="formatterParams")
        return self._set_value(value="rownum")

    def handle(self, **kwargs):
        """
        The handle formatter fills the cell with hamburger bars, to be used as a row handle.

        Related Pages:

          http://tabulator.info/docs/4.1/format
        """
        if kwargs:
            self._set_value(value=kwargs, name="formatterParams")
        return self._set_value()

    @packageImport('tabulator-inputs')
    def style(self, css: dict = None, valField: dict = None, cssField: str = None, **kwargs):
        """

        Related Pages:

          http://tabulator.info/docs/4.1/format

        :param css: Optional. the css style to apply
        :param cssField: Optional. The css style to apply
        :param valField: Optional.
        """
        if css is None and cssField is None:
            raise ValueError("Both CSS and CSSField cannot be empty")

        formatter_params = {}
        if css is not None:
            formatter_params['css'] = css
        if cssField is not None:
            formatter_params['cssField'] = cssField
            formatter_params['valField'] = valField
        if kwargs:
            formatter_params.update(kwargs)
        self._set_value(value=formatter_params, name="formatterParams")
        return self._set_value(value="cssStyle")

    @packageImport('tabulator-inputs')
    def style_pivot(self, css_mapping: dict, pivot: str = None, **kwargs):
        """
        Change the CSS style based on the cell value.

        Usage::

          c = table.get_column("Language")
          c.exts.formatters.style_pivot({"Python": {"background": "green"}, "Java": {"background": "red"}})

          c = table.get_column("Share")
          c.exts.formatters.style_pivot({"Python": {"background": "green"}, "Java": {"background": "red"}}, pivot="Language")

        :param css_mapping: Optional. The conditional formatting definition
        :param pivot: Optional. The column used for the conditional formatting
        """
        formatter_params = {'cssMapping': css_mapping}
        if pivot is not None:
            formatter_params['pivot'] = pivot
            formatter_params['cssField'] = pivot
        if kwargs:
            formatter_params.update(kwargs)
        self._set_value(value=formatter_params, name="formatterParams")
        return self._set_value(value="cssStylePivot")

    def custom(self, formatter, formatter_params, module_alias=None):
        """

        :param formatter:
        :param formatter_params: Dictionary. Optional.
        :param module_alias: String. Optional.
        """
        if module_alias is not None:
            self.component.jsImports.add(module_alias)
        self._set_value(value=formatter_params, name="formatterParams")
        return self._set_value(value=formatter)
