from epyk.core.html.options import Options
from typing import Any

        
class OptionData(Options):

    @property
    def beforeParse(self):
        """A callback function to modify the CSV before parsing it.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Data.ts
        """
        return self._config_get(None)

    @beforeParse.setter
    def beforeParse(self, value: Any): self._config(value, js_type=False)

    @property
    def columns(self):
        """A two-dimensional array representing the input data on tabular form.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Data.ts
        """
        return self._config_get(None)

    @columns.setter
    def columns(self, value: Any): self._config(value, js_type=False)

    @property
    def columnsURL(self):
        """A URL to a remote JSON dataset, structured as a column array.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Data.ts
        """
        return self._config_get(None)

    @columnsURL.setter
    def columnsURL(self, text: str): self._config(text, js_type=False)

    @property
    def complete(self):
        """The callback that is evaluated when the data is finished loading, optionally from an external source, and parsed.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Data.ts
        """
        return self._config_get(None)

    @complete.setter
    def complete(self, value: Any): self._config(value, js_type=False)

    @property
    def csv(self):
        """A comma delimited string to be parsed.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Data.ts
        """
        return self._config_get(None)

    @csv.setter
    def csv(self, text: str): self._config(text, js_type=False)

    @property
    def csvURL(self):
        """An URL to a remote CSV dataset.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Data.ts
        """
        return self._config_get(None)

    @csvURL.setter
    def csvURL(self, text: str): self._config(text, js_type=False)

    @property
    def dataRefreshRate(self):
        """Sets the refresh rate for data polling when importing remote dataset by setting <a href="data.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Data.ts
        """
        return self._config_get(1)

    @dataRefreshRate.setter
    def dataRefreshRate(self, num: float): self._config(num, js_type=False)

    @property
    def dateFormat(self):
        """Which of the predefined date formats in Date.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Data.ts
        """
        return self._config_get(None)

    @dateFormat.setter
    def dateFormat(self, value: Any): self._config(value, js_type=False)

    @property
    def decimalPoint(self):
        """The decimal point used for parsing numbers in the CSV.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Data.ts
        """
        return self._config_get(".")

    @decimalPoint.setter
    def decimalPoint(self, text: str): self._config(text, js_type=False)

    @property
    def enablePolling(self):
        """Enables automatic refetching of remote datasets every <em>n</em> seconds (defined by setting <a href="data.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Data.ts
        """
        return self._config_get(False)

    @enablePolling.setter
    def enablePolling(self, flag: bool): self._config(flag, js_type=False)

    @property
    def endColumn(self):
        """In tabular input data, the last column (indexed by 0) to use.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Data.ts
        """
        return self._config_get(None)

    @endColumn.setter
    def endColumn(self, num: float): self._config(num, js_type=False)

    @property
    def endRow(self):
        """In tabular input data, the last row (indexed by 0) to use.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Data.ts
        """
        return self._config_get(None)

    @endRow.setter
    def endRow(self, num: float): self._config(num, js_type=False)

    @property
    def firstRowAsNames(self):
        """Whether to use the first row in the data set as series names.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Data.ts
        """
        return self._config_get(True)

    @firstRowAsNames.setter
    def firstRowAsNames(self, flag: bool): self._config(flag, js_type=False)

    @property
    def googleAPIKey(self):
        """The Google Spreadsheet API key required for access generated at <a href="https://console.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Data.ts
        """
        return self._config_get(None)

    @googleAPIKey.setter
    def googleAPIKey(self, text: str): self._config(text, js_type=False)

    @property
    def googleSpreadsheetKey(self):
        """The key or <code>spreadsheetId</code> value for a Google Spreadsheet to load.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Data.ts
        """
        return self._config_get(None)

    @googleSpreadsheetKey.setter
    def googleSpreadsheetKey(self, text: str): self._config(text, js_type=False)

    @property
    def googleSpreadsheetRange(self):
        """The Google Spreadsheet <code>range</code> to use in combination with <a href="#data.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Data.ts
        """
        return self._config_get(None)

    @googleSpreadsheetRange.setter
    def googleSpreadsheetRange(self, text: str): self._config(text, js_type=False)

    @property
    def googleSpreadsheetWorksheet(self):
        """No longer works since v9.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Data.ts
        """
        return self._config_get(None)

    @googleSpreadsheetWorksheet.setter
    def googleSpreadsheetWorksheet(self, text: str): self._config(text, js_type=False)

    @property
    def itemDelimiter(self):
        """Item or cell delimiter for parsing CSV.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Data.ts
        """
        return self._config_get(None)

    @itemDelimiter.setter
    def itemDelimiter(self, text: str): self._config(text, js_type=False)

    @property
    def lineDelimiter(self):
        """Line delimiter for parsing CSV.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Data.ts
        """
        return self._config_get("\n")

    @lineDelimiter.setter
    def lineDelimiter(self, text: str): self._config(text, js_type=False)

    @property
    def parsed(self):
        """A callback function to access the parsed columns, the two-dimentional input data array directly, before they are interpreted into series data and categories.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Data.ts
        """
        return self._config_get(None)

    @parsed.setter
    def parsed(self, value: Any): self._config(value, js_type=False)

    @property
    def parseDate(self):
        """A callback function to parse string representations of dates into JavaScript timestamps.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Data.ts
        """
        return self._config_get(None)

    @parseDate.setter
    def parseDate(self, value: Any): self._config(value, js_type=False)

    @property
    def rows(self):
        """The same as the columns input option, but defining rows intead of columns.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Data.ts
        """
        return self._config_get(None)

    @rows.setter
    def rows(self, value: Any): self._config(value, js_type=False)

    @property
    def rowsURL(self):
        """A URL to a remote JSON dataset, structured as a row array.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Data.ts
        """
        return self._config_get(None)

    @rowsURL.setter
    def rowsURL(self, text: str): self._config(text, js_type=False)

    @property
    def seriesMapping(self):
        """An array containing dictionaries for each series.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Data.ts
        """
        return self._config_get(None)

    @seriesMapping.setter
    def seriesMapping(self, value: Any): self._config(value, js_type=False)

    @property
    def startColumn(self):
        """In tabular input data, the first column (indexed by 0) to use.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Data.ts
        """
        return self._config_get(0)

    @startColumn.setter
    def startColumn(self, num: float): self._config(num, js_type=False)

    @property
    def startRow(self):
        """In tabular input data, the first row (indexed by 0) to use.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Data.ts
        """
        return self._config_get(0)

    @startRow.setter
    def startRow(self, num: float): self._config(num, js_type=False)

    @property
    def switchRowsAndColumns(self):
        """Switch rows and columns of the input data, so that <code>this.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Data.ts
        """
        return self._config_get(False)

    @switchRowsAndColumns.setter
    def switchRowsAndColumns(self, flag: bool): self._config(flag, js_type=False)

    @property
    def table(self):
        """An HTML table or the id of such to be parsed as input data.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Data.ts
        """
        return self._config_get(None)

    @table.setter
    def table(self, text: str): self._config(text, js_type=False)
