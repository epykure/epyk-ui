from typing import Optional
from .module import ImportModule


class ImportPackagesPivotExts:

    def __init__(self, js: dict, css: dict, links: Optional[dict] = None):
        self._js = js
        self._css = css
        self.__linked = links

    def get(self, name: str):
        if name in self.__linked:
            return self.__linked[name]

        return ImportModule(name, self._js, self._css, self.__linked)

    @property
    def c3(self):
        """Shortcut to C3 package. """
        return self.get("pivot-c3")

    @property
    def plotly(self):
        """Shortcut to Plotly package."""
        return self.get("pivot-plotly")

    @property
    def d3(self):
        """Shortcut to D3 package."""
        return self.get("pivot-d3")

    @property
    def subtotal(self):
        """Shortcut to Sub total table package."""
        return self.get("subtotal")


class ImportPackagesCodeMirrorExts:

    def __init__(self, js: dict, css: dict, links: Optional[dict] = None):
        self._js = js
        self._css = css
        self.__linked = links

    def get(self, name: str):
        if name in self.__linked:
            return self.__linked[name]

        return ImportModule(name, self._js, self._css, self.__linked)

    @property
    def search(self) -> ImportModule:
        """Shortcut to CodeMirror Search addon."""
        return self.get("codemirror-search")

    @property
    def placeholder(self) -> ImportModule:
        """Shortcut to CodeMirror PlaceHolder addon."""
        return self.get("codemirror-placeholder")

    @property
    def trailingspace(self) -> ImportModule:
        """Shortcut to CodeMirror Trainling Space addon."""
        return self.get("codemirror-trailingspace")

    @property
    def fullscreen(self) -> ImportModule:
        """Shortcut to CodeMirror Full Screen addon."""
        return self.get("codemirror-fullscreen")

    @property
    def highlighter(self) -> ImportModule:
        """Shortcut to CodeMirror Highligher addon."""
        return self.get("codemirror-highlighter")

    @property
    def hint(self) -> ImportModule:
        """Shortcut to Code Mirror Hint addon."""
        return self.get("codemirror-hint")

    @property
    def panel(self) -> ImportModule:
        """Shortcut to CodeMirror Panel addon."""
        return self.get("codemirror-panel")

    @property
    def fold(self) -> ImportModule:
        """Shortcut to CodeMirror Fold addon."""
        return self.get("codemirror-fold")


class ImportPackagesD3Exts:

    def __init__(self, js: dict, css: dict, links: Optional[dict] = None):
        self._js = js
        self._css = css
        self.__linked = links

    def get(self, name: str):
        if name in self.__linked:
            return self.__linked[name]

        return ImportModule(name, self._js, self._css, self.__linked)

    @property
    def tip(self) -> ImportModule:
        """ Shortcut to D3 Tip addon. """
        return self.get("d3-tip")

    @property
    def axis(self) -> ImportModule:
        """ Shortcut to D3 Axis addon. """
        return self.get("d3-axis")

    @property
    def ease(self) -> ImportModule:
        """ Shortcut to D3 Ease addon. """
        return self.get("d3-ease")

    @property
    def dsv(self) -> ImportModule:
        """ Shortcut to D3 Dsv addon. """
        return self.get("d3-dsv")

    @property
    def dispatch(self) -> ImportModule:
        """ Shortcut to D3 Dispatch addon. """
        return self.get("d3-dispatch")

    @property
    def transition(self) -> ImportModule:
        """ Shortcut to D3 Transition addon. """
        return self.get("d3-transition")

    @property
    def selection(self) -> ImportModule:
        """ Shortcut to D3 Selection addon. """
        return self.get("d3-selection")

    @property
    def interpolate(self) -> ImportModule:
        """ Shortcut to D3 Interpolate addon. """
        return self.get("d3-interpolate")

    @property
    def time_format(self) -> ImportModule:
        """ Shortcut to D3 Time Format addon. """
        return self.get("d3-time-format")

    @property
    def time(self) -> ImportModule:
        """ Shortcut to D3 Time addon. """
        return self.get("d3-time")

    @property
    def array(self) -> ImportModule:
        """ Shortcut to D3 Array addon. """
        return self.get("d3-array")

    @property
    def format(self) -> ImportModule:
        """ Shortcut to D3 Format addon. """
        return self.get("d3-format")

    @property
    def timer(self) -> ImportModule:
        """ Shortcut to D3 Timer addon. """
        return self.get("d3-timer")

    @property
    def collection(self) -> ImportModule:
        """ Shortcut to D3 Collection addon. """
        return self.get("d3-collection")

    @property
    def scale(self) -> ImportModule:
        """ Shortcut to D3 Scale addon. """
        return self.get("d3-scale")

    @property
    def color(self) -> ImportModule:
        """ Shortcut to D3 Color addon. """
        return self.get("d3-color")

    @property
    def brush(self) -> ImportModule:
        """ Shortcut to D3 Brush addon. """
        return self.get("d3-brush")

    @property
    def drag(self) -> ImportModule:
        """ Shortcut to D3 Drag addon. """
        return self.get("d3-drag")

    @property
    def shape(self) -> ImportModule:
        """ Shortcut to D3 Shape addon. """
        return self.get("d3-shape")

    @property
    def zoom(self) -> ImportModule:
        """ Shortcut to D3 Zoom addon. """
        return self.get("d3-zoom")

    @property
    def path(self) -> ImportModule:
        """ Shortcut to D3 Path addon. """
        return self.get("d3-path")


class ImportPackagesDataTableExts:

    def __init__(self, js: dict, css: dict, links: Optional[dict] = None):
        self._js = js
        self._css = css
        self.__linked = links

    def get(self, name: str):
        if name in self.__linked:
            return self.__linked[name]

        return ImportModule(name, self._js, self._css, self.__linked)


class ImportPackagesChartJsExts:

    def __init__(self, js: dict, css: dict, links: Optional[dict] = None):
        self._js = js
        self._css = css
        self.__linked = links

    def get(self, name: str):
        if name in self.__linked:
            return self.__linked[name]

        return ImportModule(name, self._js, self._css, self.__linked)

    @property
    def treemap(self) -> ImportModule:
        """
        Adds treemap chart type.

        Related Pages:

          https://github.com/chartjs/awesome#charts
        """
        return self.get("chartjs-chart-treemap")

    @property
    def annotation(self) -> ImportModule:
        """
        Draws lines and boxes on the chart area.

        Related Pages:

          https://github.com/chartjs/awesome#charts
        """
        return self.get("chartjs-plugin-annotation")

    @property
    def datalabels(self) -> ImportModule:
        """
        Displays labels on data for any type of charts.

        Related Pages:

          https://github.com/chartjs/awesome#charts
        """
        return self.get("chartjs-plugin-datalabels")

    @property
    def deferred(self) -> ImportModule:
        """
        Defers initial chart update until chart scrolls into viewport.

        Related Pages:

          https://github.com/chartjs/awesome#charts
        """
        return self.get("chartjs-plugin-deferred")

    @property
    def hierarchical(self) -> ImportModule:
        """
        Chart.js module for adding a new categorical scale which mimics a hierarchical tree.

        Related Pages:

          https://github.com/sgratzl/chartjs-plugin-hierarchical
        """
        return self.get("chartjs-plugin-hierarchical")

    @property
    def zoom(self) -> ImportModule:
        """
        Enables zooming and panning on charts.

        Related Pages:

          https://github.com/chartjs/awesome#charts
        """
        return self.get("chartjs-plugin-zoom")

    @property
    def crosshair(self) -> ImportModule:
        """
        Adds a data crosshair to line and scatter charts.

        Related Pages:

          https://github.com/chartjs/awesome#charts
        """
        return self.get("chartjs-plugin-crosshair")

    @property
    def stacked100(self) -> ImportModule:
        """
        This plugin for Chart.js that makes your bar chart to 100% stacked bar chart.

        Related Pages:

          https://github.com/chartjs/awesome#charts
        """
        return self.get("chartjs-plugin-stacked100")

    @property
    def matrix(self) -> ImportModule:
        """
        Adds matrix chart type.

        Related Pages:

          https://github.com/chartjs/awesome#charts
        """
        return self.get("chartjs-chart-matrix")

    @property
    def sankey(self) -> ImportModule:
        """
        Adds sankey diagram chart type.

        Related Pages:

          https://github.com/chartjs/awesome#charts
        """
        return self.get("chartjs-chart-sankey")

    @property
    def wordcloud(self) -> ImportModule:
        """
        Adds word-cloud chart type.

        Related Pages:

          https://github.com/chartjs/awesome#charts
        """
        return self.get("chartjs-chart-wordcloud")

    @property
    def venn(self) -> ImportModule:
        """
        Adds venn and euler chart type.

        Related Pages:

          https://github.com/chartjs/awesome#charts
        """
        return self.get("chartjs-chart-venn")

    @property
    def dragdata(self) -> ImportModule:
        """
        Lets users drag data points on the chart.

        Related Pages:

          https://github.com/chartjs/awesome#charts
        """
        return self.get("chartjs-plugin-dragdata")

    @property
    def geo(self) -> ImportModule:
        """
        Adds geographic map chart types such as choropleth and bubble map.

        Related Pages:

          https://github.com/chartjs/awesome#charts
        """
        return self.get("chartjs-chart-geo")

    @property
    def labels(self) -> ImportModule:
        """ Shortcut to ChartKs Plugin labels addon. """
        return self.get("chartjs-plugin-labels")


class ImportPackagesTabulatorExts:

    def __init__(self, js: dict, css: dict, links: Optional[dict] = None):
        self._js = js
        self._css = css
        self.__linked = links

    def get(self, name: str) -> ImportModule:
        """
        Generic way to retrieve packages from the framework.

        This is a shortcut to change any properties for the package (version, path...).

        :param name: The package alias to be loaded
        """
        if name in self.__linked:
            return self.__linked[name]

        return ImportModule(name, self._js, self._css, self.__linked)

    @property
    def formatter_inputs(self) -> ImportModule:
        """ Shortcut to Tabulator Inputs addon. """
        return self.get("tabulator-inputs")

    @property
    def formatter_icons(self) -> ImportModule:
        """ Shortcut to Tabulator Icons addon. """
        return self.get("tabulator-icons")

    @property
    def formatter_numbers(self) -> ImportModule:
        """ Shortcut to Tabulator Numbers addon. """
        return self.get("tabulator-numbers")

    @property
    def formatter_drops(self) -> ImportModule:
        """ Shortcut to Tabulator Drop addon. """
        return self.get("tabulator-drop")

    @property
    def mutators_inputs(self) -> ImportModule:
        """ Shortcut to Tabulator Mutators Inputs addon. """
        return self.get("tabulator-mutators-inputs")

    @property
    def editors_inputs(self) -> ImportModule:
        """ Shortcut to Tabulator Editors Inputs addon. """
        return self.get("editors-inputs")

    @property
    def editors_dates(self) -> ImportModule:
        """ Shortcut to Tabulator Editors Dates addon. """
        return self.get("editors-dates")

    @property
    def editors_selects(self) -> ImportModule:
        """ Shortcut to Tabulator Selects addon. """
        return self.get("editors-selects")


class ImportPackages:

    def __init__(self, js: dict, css: dict, page=None):
        self._js = js
        self._css = css
        self.page = page
        self.__linked = {}

    def get(self, name: str) -> ImportModule:
        """
        Generic way to retrieve packages from the framework.

        This is a shortcut to change any properties for the package (version, path...).

        :param name: The package alias to be loaded
        """
        if name in self.__linked:
            return self.__linked[name]

        return ImportModule(name, self._js, self._css, self.__linked, page=self.page)

    @property
    def vis(self) -> ImportModule:
        """
        A dynamic, browser based visualization library..

        TODO: Add the split of packages

        Related Pages:

          http://visjs.org
        """
        return self.get("vis")

    @property
    def d3(self) -> ImportModule:
        """
        D3.js is a JavaScript library for manipulating documents based on data.

        TODO: Add the split of packages

        Related Pages:

          https://d3js.org/
        """
        return self.get("d3")

    @property
    def dc(self) -> ImportModule:
        """
        dc.js is a javascript charting library with native crossfilter support, allowing highly efficient exploration on
        large multi-dimensional datasets.

        Related Pages:

          https://dc-js.github.io/dc.js
        """
        return self.get("dc")

    @property
    def nvd3(self) -> ImportModule:
        """
        This project is an attempt to build re-usable charts and chart components for d3.js without taking away
        the power that d3.js gives you.

        Related Pages:

          http://nvd3.org/
        """
        return self.get("nvd3")

    @property
    def c3(self) -> ImportModule:
        """
        C3.js D3-based reusable chart library.

        Related Pages:

          https://c3js.org/
        """
        return self.get("c3")

    @property
    def billboard(self) -> ImportModule:
        """
        Re-usable, easy interface JavaScript chart library, based on D3 v4+.

        Related Pages:

          https://naver.github.io/billboard.js/
        """
        return self.get("billboard.js")

    @property
    def chart_js(self) -> ImportModule:
        """
        Simple yet flexible JavaScript charting for designers & developers.

        Related Pages:

          https://www.chartjs.org/
        """
        return self.get("chart.js")

    @property
    def chart_js_extensions(self) -> ImportPackagesChartJsExts:
        """
        Simple yet flexible JavaScript charting for designers & developers.

        Related Pages:

          https://www.chartjs.org/
        """
        return ImportPackagesChartJsExts(self._js, self._css, self.__linked)

    @property
    def crossfilter(self) -> ImportModule:
        """
        Fast Multidimensional Filtering for Coordinated Views.

        Related Pages:

          http://square.github.io/crossfilter
        """
        return self.get("crossfilter")

    @property
    def apexcharts(self) -> ImportModule:
        """
        Modern & Interactive Open-source Charts.

        Related Pages:

          https://apexcharts.com
        """
        return self.get("apexcharts")

    @property
    def plotly(self) -> ImportModule:
        """
        Plotly JavaScript Open Source Graphing Library.

        Related Pages:

          https://plot.ly/javascript/
        """
        return self.get("plotly.js")

    @property
    def ag_grid(self) -> ImportModule:
        """
        The Best JavaScript Grid in the World.

        Related Pages:

          https://www.ag-grid.com/javascript-grid/
        """
        return self.get("ag-grid-community")

    @property
    def bootstrap(self) -> ImportModule:
        """
        The most popular front-end framework for developing responsive, mobile first projects on the web.

        Related Pages:

          https://getbootstrap.com/
        """
        return self.get("bootstrap")

    @property
    def jquery(self) -> ImportModule:
        """
        JavaScript library for DOM operations.

        Related Pages:

          https://jquery.com
        """
        return self.get("jquery")

    @property
    def jqueryui(self) -> ImportModule:
        """
        jQuery UI is a curated set of user interface interactions, effects, widgets, and themes built on top of the
        jQuery JavaScript Library.

        Related Pages:

          https://jqueryui.com/
        """
        return self.get("jqueryui")

    @property
    def jquery_bracket(self) -> ImportModule:
        """
        jQuery bracket is a jQuery plugin that lets users create and display single and double elimination brackets for
        tournament play.

        Related Pages:

          http://www.aropupu.fi/bracket/
        """
        return self.get("jquery-bracket")

    @property
    def jquery_sparkline(self) -> ImportModule:
        """
        This jQuery plugin generates sparklines (small inline charts) directly in the browser using data supplied
        either inline in the HTML, or via javascript.

        Related Pages:

          https://omnipotent.net/jquery.sparkline
        """
        return self.get("jquery-sparkline")

    @property
    def jqvmap(self) -> ImportModule:
        """
        JQVMap is a jQuery plugin that renders Interactive, Clickable Vector Maps.

        Related Pages:

          https://www.10bestdesign.com/jqvmap/
        """
        return self.get("jqvmap")

    @property
    def qunit(self) -> ImportModule:
        """
        The powerful, easy-to-use JavaScript testing framework.

        Related Pages:

          https://qunitjs.com/
        """
        return self.get("qunit")

    @property
    def accounting(self) -> ImportModule:
        """
        Number, money and currency formatting library.

        Related Pages:

          http://openexchangerates.github.io/accounting.js
        """
        return self.get("accounting")

    @property
    def qrcodejs(self) -> ImportModule:
        """
        QRCode.js is javascript library for making QRCode.

        QRCode.js supports Cross-browser with HTML5 Canvas and table tag in DOM. QRCode.js has no dependencies.

        Related Pages:

          https://davidshimjs.github.io/qrcodejs
        """
        return self.get("qrcodejs")

    @property
    def underscore(self) -> ImportModule:
        """
        accounting.js is a tiny JavaScript library by Open Exchange Rates, providing simple and advanced number,
        money and currency formatting.

        Related Pages:

          https://openexchangerates.github.io/accounting.js/
        """
        return self.get("underscore")

    @property
    def tabulator(self) -> ImportModule:
        """
        Interactive table generation JavaScript library.

        Related Pages:

          http://tabulator.info/
        """
        return self.get("tabulator-tables")

    @property
    def tabulator_extensions(self) -> ImportPackagesTabulatorExts:
        """ Get all the defined extension for tabulator. """
        return ImportPackagesTabulatorExts(self._js, self._css, self.__linked)

    @property
    def datatables(self) -> ImportModule:
        """
        Add advanced interaction controls to your HTML tables the free & easy way.

        Related Pages:

          https://datatables.net/
        """
        return self.get("datatables")

    @property
    def datatable_extensions(self) -> ImportPackagesDataTableExts:
        """ Get all the defined extension for DataTable. """
        return ImportPackagesDataTableExts(self._js, self._css, self.__linked)

    @property
    def mathjax(self) -> ImportModule:
        """
        Beautiful and accessible math in all browsers.

        Related Pages:

          https://www.mathjax.org/
        """
        return self.get("mathjax")

    @property
    def mapbox(self) -> ImportModule:
        """
        Maps and location for developers.

        Related Pages:

          https://docs.mapbox.com/mapbox.js/api/v3.3.1/
        """
        return self.get("mapbox-gl")

    @property
    def moment(self) -> ImportModule:
        """
        Parse, validate, manipulate, and display dates and times in JavaScript.

        Related Pages:

          https://momentjs.com/
        """
        return self.get("moment")

    @property
    def hammer(self) -> ImportModule:
        """
        Add touch gestures to your webapp.

        Related Pages:

          https://hammerjs.github.io/
        """
        return self.get("hammer")

    @property
    def popper_js(self) -> ImportModule:
        """ Tooltip & Popover Positioning Engine.

    Related Pages:

      https://github.com/popperjs/popper-core
    """
        return self.get("@popperjs/core")

    @property
    def font_awesome(self) -> ImportModule:
        """
        The next generation of our icon library + toolkit is coming with more icons, more styles, more services,
        and more awesome.

        Related Pages:

          https://fontawesome.com
        """
        return self.get("font-awesome")

    @property
    def json_formatter(self) -> ImportModule:
        """
        Render JSON objects in HTML with a collapsible navigation.

        Related Pages:

          https://azimi.me/json-formatter-js/
        """
        return self.get("json-formatter-js")

    @property
    def pivottable(self) -> ImportModule:
        """
        Open-source Javascript Pivot Table (aka Pivot Grid, Pivot Chart, Cross-Tab) implementation with drag'n'drop.

        Related Pages:

          https://github.com/nicolaskruchten/pivottable
        """
        return self.get("pivottable")

    @property
    def require_js(self) -> ImportModule:
        """ RequireJS is a JavaScript file and module loader.

    It is optimized for in-browser use, but it can be used in other JavaScript environments, like Rhino and Node.

    Related Pages:

      https://requirejs.org/
    """
        return self.get("requirejs")

    @property
    def timepicker(self) -> ImportModule:
        """ jQuery TimePicker is a plugin to enhance standard form input fields, helping users to select (or type) times.

        Related Pages:

          https://timepicker.co
        """
        return self.get("timepicker")

    @property
    def socket(self) -> ImportModule:
        """ Real-time application framework.

    Socket.IO enables real-time bidirectional event-based communication.

    Related Pages:

      https://github.com/socketio/socket.io
    """
        return self.get("socket.io")

    @property
    def codemirror(self) -> ImportModule:
        """ CodeMirror is a versatile text editor implemented in JavaScript for the browser.

    Related Pages:

      https://codemirror.net
    """
        return self.get("codemirror")

    @property
    def codemirror_extensions(self) -> ImportPackagesCodeMirrorExts:
        """ Code mirror extensions """
        return ImportPackagesCodeMirrorExts(self._js, self._css, self.__linked)

    @property
    def highlight(self) -> ImportModule:
        """
        Syntax highlighting for the Web.

        Related Pages:

          https://highlightjs.org/
        """
        return self.get("highlight.js")

    @property
    def leaflet(self) -> ImportModule:
        """
        An open-source JavaScript library for mobile-friendly interactive maps.

        Related Pages:

          https://leafletjs.com/
        """
        return self.get("leaflet")

    @property
    def showdown(self) -> ImportModule:
        """
        Showdown is a Javascript Markdown to HTML converter.

        Related Pages:

          https://github.com/showdownjs/showdown
        """
        return self.get("showdown")

    @property
    def sortablejs(self) -> ImportModule:
        """
        Create and reorder lists with drag-and-drop. For use with modern browsers and touch devices.

        Related Pages:

          https://github.com/SortableJS/Sortable
        """
        return self.get("sortablejs")
