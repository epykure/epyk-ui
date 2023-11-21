from epyk.core.html.options import Options
from typing import Any

        
class OptionExportingPdffont(Options):

    @property
    def bold(self):
        """The TTF font file for bold text.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get("undefined")

    @bold.setter
    def bold(self, text: str): self._config(text, js_type=False)

    @property
    def bolditalic(self):
        """The TTF font file for bold and italic text.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get("undefined")

    @bolditalic.setter
    def bolditalic(self, text: str): self._config(text, js_type=False)

    @property
    def italic(self):
        """The TTF font file for italic text.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get("undefined")

    @italic.setter
    def italic(self, text: str): self._config(text, js_type=False)

    @property
    def normal(self):
        """The TTF font file for normal <code>font-style</code>.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get("undefined")

    @normal.setter
    def normal(self, text: str): self._config(text, js_type=False)

        
class OptionExportingAccessibility(Options):

    @property
    def enabled(self):
        """Enable accessibility support for the export menu.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(True)

    @enabled.setter
    def enabled(self, flag: bool): self._config(flag, js_type=False)

        
class OptionExportingCsvAnnotations(Options):

    @property
    def itemDelimiter(self):
        """The way to mark the separator for annotations combined in one export-data table cell.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/ExportData/ExportDataDefaults.ts
        """
        return self._config_get(";")

    @itemDelimiter.setter
    def itemDelimiter(self, text: str): self._config(text, js_type=False)

    @property
    def join(self):
        """When several labels are assigned to a specific point, they will be displayed in one field in the table.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/ExportData/ExportDataDefaults.ts
        """
        return self._config_get(False)

    @join.setter
    def join(self, flag: bool): self._config(flag, js_type=False)

        
class OptionExportingButtons(Options):

    @property
    def contextButton(self) -> 'OptionExportingButtonsContextbutton':
        """Options for the export button. """
        return self._config_sub_data("contextButton", OptionExportingButtonsContextbutton)

        
class OptionExportingCsv(Options):

    @property
    def annotations(self) -> 'OptionExportingCsvAnnotations':
        """Options for annotations in the export-data table. """
        return self._config_sub_data("annotations", OptionExportingCsvAnnotations)

    @property
    def columnHeaderFormatter(self):
        """Formatter callback for the column headers.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/ExportData/ExportDataDefaults.ts
        """
        return self._config_get(None)

    @columnHeaderFormatter.setter
    def columnHeaderFormatter(self, value: Any): self._config(value, js_type=False)

    @property
    def dateFormat(self):
        """Which date format to use for exported dates on a datetime X axis.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/ExportData/ExportDataDefaults.ts
        """
        return self._config_get("%Y-%m-%d %H:%M:%S")

    @dateFormat.setter
    def dateFormat(self, text: str): self._config(text, js_type=False)

    @property
    def decimalPoint(self):
        """Which decimal point to use for exported CSV.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/ExportData/ExportDataDefaults.ts
        """
        return self._config_get(None)

    @decimalPoint.setter
    def decimalPoint(self, text: str): self._config(text, js_type=False)

    @property
    def itemDelimiter(self):
        """The item delimiter in the exported data.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/ExportData/ExportDataDefaults.ts
        """
        return self._config_get(None)

    @itemDelimiter.setter
    def itemDelimiter(self, text: str): self._config(text, js_type=False)

    @property
    def lineDelimiter(self):
        """The line delimiter in the exported data, defaults to a newline.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/ExportData/ExportDataDefaults.ts
        """
        return self._config_get("")

    @lineDelimiter.setter
    def lineDelimiter(self, text: str): self._config(text, js_type=False)

        
class OptionExporting(Options):

    @property
    def accessibility(self) -> 'OptionExportingAccessibility':
        """Accessibility options for the exporting menu. """
        return self._config_sub_data("accessibility", OptionExportingAccessibility)

    @property
    def allowHTML(self):
        """Experimental setting to allow HTML inside the chart (added through the <code>useHTML</code> options), directly in the exported image.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get(False)

    @allowHTML.setter
    def allowHTML(self, flag: bool): self._config(flag, js_type=False)

    @property
    def allowTableSorting(self):
        """Allows the end user to sort the data table by clicking on column headers.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get(True)

    @allowTableSorting.setter
    def allowTableSorting(self, flag: bool): self._config(flag, js_type=False)

    @property
    def buttons(self) -> 'OptionExportingButtons':
        """Options for the export related buttons, print and export. """
        return self._config_sub_data("buttons", OptionExportingButtons)

    @property
    def chartOptions(self):
        """Additional chart options to be merged into the chart before exporting to an image format.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get(None)

    @chartOptions.setter
    def chartOptions(self, value: Any): self._config(value, js_type=False)

    @property
    def csv(self) -> 'OptionExportingCsv':
        """Options for exporting data to CSV or ExCel, or displaying the data in a HTML table or a JavaScript structure. """
        return self._config_sub_data("csv", OptionExportingCsv)

    @property
    def enabled(self):
        """Whether to enable the exporting module.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get(True)

    @enabled.setter
    def enabled(self, flag: bool): self._config(flag, js_type=False)

    @property
    def error(self):
        """Function to call if the offline-exporting module fails to export a chart on the client side, and <a href="#exporting.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get(None)

    @error.setter
    def error(self, value: Any): self._config(value, js_type=False)

    @property
    def fallbackToExportServer(self):
        """Whether or not to fall back to the export server if the offline-exporting module is unable to export the chart on the client side.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get(True)

    @fallbackToExportServer.setter
    def fallbackToExportServer(self, flag: bool): self._config(flag, js_type=False)

    @property
    def filename(self):
        """The filename, without extension, to use for the exported chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get("chart")

    @filename.setter
    def filename(self, text: str): self._config(text, js_type=False)

    @property
    def formAttributes(self):
        """An object containing additional key value data for the POST form that sends the SVG to the export server.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get(None)

    @formAttributes.setter
    def formAttributes(self, value: Any): self._config(value, js_type=False)

    @property
    def libURL(self):
        """Path where Highcharts will look for export module dependencies to load on demand if they don&#39;t already exist on <code>window</code>.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get(None)

    @libURL.setter
    def libURL(self, text: str): self._config(text, js_type=False)

    @property
    def menuItemDefinitions(self):
        """An object consisting of definitions for the menu items in the context menu.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get({"viewFullscreen": {}, "printChart": {}, "separator": {}, "downloadPNG": {}, "downloadJPEG": {}, "downloadPDF": {}, "downloadSVG": {}})

    @menuItemDefinitions.setter
    def menuItemDefinitions(self, value: Any): self._config(value, js_type=False)

    @property
    def pdfFont(self) -> 'OptionExportingPdffont':
        """Settings for a custom font for the exported PDF, when using the <code>offline-exporting</code> module. """
        return self._config_sub_data("pdfFont", OptionExportingPdffont)

    @property
    def printMaxWidth(self):
        """When printing the chart from the menu item in the burger menu, if the on-screen chart exceeds this width, it is resized.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get(780)

    @printMaxWidth.setter
    def printMaxWidth(self, num: float): self._config(num, js_type=False)

    @property
    def scale(self):
        """Defines the scale or zoom factor for the exported image compared to the on-screen display.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get(2)

    @scale.setter
    def scale(self, num: float): self._config(num, js_type=False)

    @property
    def showTable(self):
        """Show a HTML table below the chart with the chart&#39;s current data.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/ExportData/ExportDataDefaults.ts
        """
        return self._config_get(False)

    @showTable.setter
    def showTable(self, flag: bool): self._config(flag, js_type=False)

    @property
    def sourceHeight(self):
        """Analogous to <a href="#exporting.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get(None)

    @sourceHeight.setter
    def sourceHeight(self, num: float): self._config(num, js_type=False)

    @property
    def sourceWidth(self):
        """The width of the original chart when exported, unless an explicit <a href="#chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get(None)

    @sourceWidth.setter
    def sourceWidth(self, num: float): self._config(num, js_type=False)

    @property
    def tableCaption(self):
        """Caption for the data table.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/ExportData/ExportDataDefaults.ts
        """
        return self._config_get(None)

    @tableCaption.setter
    def tableCaption(self, flag: bool): self._config(flag, js_type=False)

    @property
    def type(self):
        """Default MIME type for exporting if <code>chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get("image/png")

    @type.setter
    def type(self, text: str): self._config(text, js_type=False)

    @property
    def url(self):
        """The URL for the server module converting the SVG string to an image format.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get("https://export.highcharts.com/")

    @url.setter
    def url(self, text: str): self._config(text, js_type=False)

    @property
    def useMultiLevelHeaders(self):
        """Use multi level headers in data table.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/ExportData/ExportDataDefaults.ts
        """
        return self._config_get(True)

    @useMultiLevelHeaders.setter
    def useMultiLevelHeaders(self, flag: bool): self._config(flag, js_type=False)

    @property
    def useRowspanHeaders(self):
        """If using multi level table headers, use rowspans for headers that have only one level.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/ExportData/ExportDataDefaults.ts
        """
        return self._config_get(True)

    @useRowspanHeaders.setter
    def useRowspanHeaders(self, flag: bool): self._config(flag, js_type=False)

    @property
    def width(self):
        """The pixel width of charts exported to PNG or JPG.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get(None)

    @width.setter
    def width(self, num: float): self._config(num, js_type=False)

        
class OptionExportingButtonsContextbuttonTheme(Options):

    @property
    def fill(self):
        """The default fill exists only to capture hover events.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get("#ffffff")

    @fill.setter
    def fill(self, text: str): self._config(text, js_type=False)

    @property
    def padding(self):
        """Padding for the button.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get(5)

    @padding.setter
    def padding(self, num: float): self._config(num, js_type=False)

    @property
    def stroke(self):
        """Default stroke for the buttons.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get("none")

    @stroke.setter
    def stroke(self, text: str): self._config(text, js_type=False)

        
class OptionExportingButtonsContextbutton(Options):

    @property
    def _titleKey(self):
        """This option is deprecated, use <a href="#exporting.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get(None)

    @_titleKey.setter
    def _titleKey(self, text: str): self._config(text, js_type=False)

    @property
    def align(self):
        """Alignment for the buttons.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get("right")

    @align.setter
    def align(self, text: str): self._config(text, js_type=False)

    @property
    def buttonSpacing(self):
        """The pixel spacing between buttons.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get(3)

    @buttonSpacing.setter
    def buttonSpacing(self, num: float): self._config(num, js_type=False)

    @property
    def className(self):
        """The class name of the context button.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get("highcharts-contextbutton")

    @className.setter
    def className(self, text: str): self._config(text, js_type=False)

    @property
    def enabled(self):
        """Whether to enable buttons.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get(True)

    @enabled.setter
    def enabled(self, flag: bool): self._config(flag, js_type=False)

    @property
    def height(self):
        """Pixel height of the buttons.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get(28)

    @height.setter
    def height(self, num: float): self._config(num, js_type=False)

    @property
    def menuClassName(self):
        """The class name of the menu appearing from the button.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get("highcharts-contextmenu")

    @menuClassName.setter
    def menuClassName(self, text: str): self._config(text, js_type=False)

    @property
    def menuItems(self):
        """A collection of strings pointing to config options for the menu items.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get(["viewFullscreen", "printChart", "separator", "downloadPNG", "downloadJPEG", "downloadPDF", "downloadSVG"])

    @menuItems.setter
    def menuItems(self, value: Any): self._config(value, js_type=False)

    @property
    def onclick(self):
        """A click handler callback to use on the button directly instead of the popup menu.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get(None)

    @onclick.setter
    def onclick(self, value: Any): self._config(value, js_type=False)

    @property
    def symbol(self):
        """The symbol for the button.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get("menu")

    @symbol.setter
    def symbol(self, text: str): self._config(text, js_type=False)

    @property
    def symbolFill(self):
        """See <a href="#navigation.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get("#666666")

    @symbolFill.setter
    def symbolFill(self, text: str): self._config(text, js_type=False)

    @property
    def symbolSize(self):
        """The pixel size of the symbol on the button.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get(14)

    @symbolSize.setter
    def symbolSize(self, num: float): self._config(num, js_type=False)

    @property
    def symbolStroke(self):
        """The color of the symbol&#39;s stroke or line.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get("#666666")

    @symbolStroke.setter
    def symbolStroke(self, text: str): self._config(text, js_type=False)

    @property
    def symbolStrokeWidth(self):
        """The pixel stroke width of the symbol on the button.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get(3)

    @symbolStrokeWidth.setter
    def symbolStrokeWidth(self, num: float): self._config(num, js_type=False)

    @property
    def symbolX(self):
        """The x position of the center of the symbol inside the button.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get(14.5)

    @symbolX.setter
    def symbolX(self, num: float): self._config(num, js_type=False)

    @property
    def symbolY(self):
        """The y position of the center of the symbol inside the button.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get(13.5)

    @symbolY.setter
    def symbolY(self, num: float): self._config(num, js_type=False)

    @property
    def text(self):
        """A text string to add to the individual button.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get("null")

    @text.setter
    def text(self, text: str): self._config(text, js_type=False)

    @property
    def theme(self) -> 'OptionExportingButtonsContextbuttonTheme':
        """A configuration object for the button theme. """
        return self._config_sub_data("theme", OptionExportingButtonsContextbuttonTheme)

    @property
    def titleKey(self):
        """The key to a <a href="#lang">lang</a> option setting that is used for the button&#39;s title tooltip.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get("contextButtonTitle")

    @titleKey.setter
    def titleKey(self, text: str): self._config(text, js_type=False)

    @property
    def useHTML(self):
        """Whether to use HTML for rendering the button.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get(False)

    @useHTML.setter
    def useHTML(self, flag: bool): self._config(flag, js_type=False)

    @property
    def verticalAlign(self):
        """The vertical alignment of the buttons.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get("top")

    @verticalAlign.setter
    def verticalAlign(self, text: str): self._config(text, js_type=False)

    @property
    def width(self):
        """The pixel width of the button.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get(28)

    @width.setter
    def width(self, num: float): self._config(num, js_type=False)

    @property
    def x(self):
        """The horizontal position of the button relative to the <code>align</code> option.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get(-10)

    @x.setter
    def x(self, num: float): self._config(num, js_type=False)

    @property
    def y(self):
        """The vertical offset of the button&#39;s position relative to its <code>verticalAlign</code>.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get(0)

    @y.setter
    def y(self, num: float): self._config(num, js_type=False)
