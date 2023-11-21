from epyk.core.html.options import Options
from typing import Any

        
class OptionLangNavigationPopup(Options):

    @property
    def addButton(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Add")

    @addButton.setter
    def addButton(self, text: str): self._config(text, js_type=False)

    @property
    def algorithm(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Algorithm")

    @algorithm.setter
    def algorithm(self, text: str): self._config(text, js_type=False)

    @property
    def arrowInfinityLine(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Arrow line")

    @arrowInfinityLine.setter
    def arrowInfinityLine(self, text: str): self._config(text, js_type=False)

    @property
    def arrowRay(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Arrow ray")

    @arrowRay.setter
    def arrowRay(self, text: str): self._config(text, js_type=False)

    @property
    def arrowSegment(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Arrow segment")

    @arrowSegment.setter
    def arrowSegment(self, text: str): self._config(text, js_type=False)

    @property
    def average(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Average")

    @average.setter
    def average(self, text: str): self._config(text, js_type=False)

    @property
    def background(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Background")

    @background.setter
    def background(self, text: str): self._config(text, js_type=False)

    @property
    def backgroundColor(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/NavigationBindingsDefaults.ts
        """
        return self._config_get("Background color")

    @backgroundColor.setter
    def backgroundColor(self, text: str): self._config(text, js_type=False)

    @property
    def backgroundColors(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/NavigationBindingsDefaults.ts
        """
        return self._config_get("Background colors")

    @backgroundColors.setter
    def backgroundColors(self, text: str): self._config(text, js_type=False)

    @property
    def borderColor(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/NavigationBindingsDefaults.ts
        """
        return self._config_get("Border color")

    @borderColor.setter
    def borderColor(self, text: str): self._config(text, js_type=False)

    @property
    def borderRadius(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/NavigationBindingsDefaults.ts
        """
        return self._config_get("Border radius")

    @borderRadius.setter
    def borderRadius(self, text: str): self._config(text, js_type=False)

    @property
    def borderWidth(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/NavigationBindingsDefaults.ts
        """
        return self._config_get("Border width")

    @borderWidth.setter
    def borderWidth(self, text: str): self._config(text, js_type=False)

    @property
    def bottomBand(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Bottom band")

    @bottomBand.setter
    def bottomBand(self, text: str): self._config(text, js_type=False)

    @property
    def circle(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Circle")

    @circle.setter
    def circle(self, text: str): self._config(text, js_type=False)

    @property
    def clearFilter(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("✕ clear filter")

    @clearFilter.setter
    def clearFilter(self, text: str): self._config(text, js_type=False)

    @property
    def color(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/NavigationBindingsDefaults.ts
        """
        return self._config_get("Color")

    @color.setter
    def color(self, text: str): self._config(text, js_type=False)

    @property
    def connector(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Connector")

    @connector.setter
    def connector(self, text: str): self._config(text, js_type=False)

    @property
    def crooked3(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Crooked 3 line")

    @crooked3.setter
    def crooked3(self, text: str): self._config(text, js_type=False)

    @property
    def crooked5(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Crooked 5 line")

    @crooked5.setter
    def crooked5(self, text: str): self._config(text, js_type=False)

    @property
    def crosshairX(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Crosshair X")

    @crosshairX.setter
    def crosshairX(self, text: str): self._config(text, js_type=False)

    @property
    def crosshairY(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Crosshair Y")

    @crosshairY.setter
    def crosshairY(self, text: str): self._config(text, js_type=False)

    @property
    def decimals(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Decimals")

    @decimals.setter
    def decimals(self, text: str): self._config(text, js_type=False)

    @property
    def deviation(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Deviation")

    @deviation.setter
    def deviation(self, text: str): self._config(text, js_type=False)

    @property
    def editButton(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Edit")

    @editButton.setter
    def editButton(self, text: str): self._config(text, js_type=False)

    @property
    def elliott3(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Elliott 3 line")

    @elliott3.setter
    def elliott3(self, text: str): self._config(text, js_type=False)

    @property
    def elliott5(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Elliott 5 line")

    @elliott5.setter
    def elliott5(self, text: str): self._config(text, js_type=False)

    @property
    def ellipse(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Ellipse")

    @ellipse.setter
    def ellipse(self, text: str): self._config(text, js_type=False)

    @property
    def factor(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Factor")

    @factor.setter
    def factor(self, text: str): self._config(text, js_type=False)

    @property
    def fastAvgPeriod(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Fast average period")

    @fastAvgPeriod.setter
    def fastAvgPeriod(self, text: str): self._config(text, js_type=False)

    @property
    def fibonacci(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Fibonacci")

    @fibonacci.setter
    def fibonacci(self, text: str): self._config(text, js_type=False)

    @property
    def fibonacciTimeZones(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Fibonacci Time Zones")

    @fibonacciTimeZones.setter
    def fibonacciTimeZones(self, text: str): self._config(text, js_type=False)

    @property
    def fill(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/NavigationBindingsDefaults.ts
        """
        return self._config_get("Fill")

    @fill.setter
    def fill(self, text: str): self._config(text, js_type=False)

    @property
    def flags(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Flags")

    @flags.setter
    def flags(self, text: str): self._config(text, js_type=False)

    @property
    def fontSize(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/NavigationBindingsDefaults.ts
        """
        return self._config_get("Font size")

    @fontSize.setter
    def fontSize(self, text: str): self._config(text, js_type=False)

    @property
    def format(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/NavigationBindingsDefaults.ts
        """
        return self._config_get("Text")

    @format.setter
    def format(self, text: str): self._config(text, js_type=False)

    @property
    def height(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/NavigationBindingsDefaults.ts
        """
        return self._config_get("Height")

    @height.setter
    def height(self, text: str): self._config(text, js_type=False)

    @property
    def highIndex(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("High index")

    @highIndex.setter
    def highIndex(self, text: str): self._config(text, js_type=False)

    @property
    def horizontalLine(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Horizontal line")

    @horizontalLine.setter
    def horizontalLine(self, text: str): self._config(text, js_type=False)

    @property
    def increment(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Increment")

    @increment.setter
    def increment(self, text: str): self._config(text, js_type=False)

    @property
    def index(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Index")

    @index.setter
    def index(self, text: str): self._config(text, js_type=False)

    @property
    def infinityLine(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Infinity line")

    @infinityLine.setter
    def infinityLine(self, text: str): self._config(text, js_type=False)

    @property
    def initialAccelerationFactor(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Initial acceleration factor")

    @initialAccelerationFactor.setter
    def initialAccelerationFactor(self, text: str): self._config(text, js_type=False)

    @property
    def innerBackground(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Inner background")

    @innerBackground.setter
    def innerBackground(self, text: str): self._config(text, js_type=False)

    @property
    def label(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Label")

    @label.setter
    def label(self, text: str): self._config(text, js_type=False)

    @property
    def labelOptions(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/NavigationBindingsDefaults.ts
        """
        return self._config_get("Label options")

    @labelOptions.setter
    def labelOptions(self, text: str): self._config(text, js_type=False)

    @property
    def labels(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/NavigationBindingsDefaults.ts
        """
        return self._config_get("Labels")

    @labels.setter
    def labels(self, text: str): self._config(text, js_type=False)

    @property
    def line(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Line")

    @line.setter
    def line(self, text: str): self._config(text, js_type=False)

    @property
    def lines(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/NavigationBindingsDefaults.ts
        """
        return self._config_get("Lines")

    @lines.setter
    def lines(self, text: str): self._config(text, js_type=False)

    @property
    def longPeriod(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Long period")

    @longPeriod.setter
    def longPeriod(self, text: str): self._config(text, js_type=False)

    @property
    def lowIndex(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Low index")

    @lowIndex.setter
    def lowIndex(self, text: str): self._config(text, js_type=False)

    @property
    def maxAccelerationFactor(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Max acceleration factor")

    @maxAccelerationFactor.setter
    def maxAccelerationFactor(self, text: str): self._config(text, js_type=False)

    @property
    def measure(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Measure")

    @measure.setter
    def measure(self, text: str): self._config(text, js_type=False)

    @property
    def measureX(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Measure X")

    @measureX.setter
    def measureX(self, text: str): self._config(text, js_type=False)

    @property
    def measureXY(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Measure XY")

    @measureXY.setter
    def measureXY(self, text: str): self._config(text, js_type=False)

    @property
    def measureY(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Measure Y")

    @measureY.setter
    def measureY(self, text: str): self._config(text, js_type=False)

    @property
    def multiplier(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Multiplier")

    @multiplier.setter
    def multiplier(self, text: str): self._config(text, js_type=False)

    @property
    def multiplierATR(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("ATR multiplier")

    @multiplierATR.setter
    def multiplierATR(self, text: str): self._config(text, js_type=False)

    @property
    def name(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/NavigationBindingsDefaults.ts
        """
        return self._config_get("Name")

    @name.setter
    def name(self, text: str): self._config(text, js_type=False)

    @property
    def noFilterMatch(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("No match")

    @noFilterMatch.setter
    def noFilterMatch(self, text: str): self._config(text, js_type=False)

    @property
    def outerBackground(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Outer background")

    @outerBackground.setter
    def outerBackground(self, text: str): self._config(text, js_type=False)

    @property
    def padding(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/NavigationBindingsDefaults.ts
        """
        return self._config_get("Padding")

    @padding.setter
    def padding(self, text: str): self._config(text, js_type=False)

    @property
    def parallelChannel(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Parallel channel")

    @parallelChannel.setter
    def parallelChannel(self, text: str): self._config(text, js_type=False)

    @property
    def period(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Period")

    @period.setter
    def period(self, text: str): self._config(text, js_type=False)

    @property
    def periodATR(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("ATR period")

    @periodATR.setter
    def periodATR(self, text: str): self._config(text, js_type=False)

    @property
    def periods(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Periods")

    @periods.setter
    def periods(self, text: str): self._config(text, js_type=False)

    @property
    def periodSenkouSpanB(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Senkou Span B period")

    @periodSenkouSpanB.setter
    def periodSenkouSpanB(self, text: str): self._config(text, js_type=False)

    @property
    def periodTenkan(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Tenkan period")

    @periodTenkan.setter
    def periodTenkan(self, text: str): self._config(text, js_type=False)

    @property
    def pitchfork(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Pitchfork")

    @pitchfork.setter
    def pitchfork(self, text: str): self._config(text, js_type=False)

    @property
    def ranges(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Ranges")

    @ranges.setter
    def ranges(self, text: str): self._config(text, js_type=False)

    @property
    def ray(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Ray")

    @ray.setter
    def ray(self, text: str): self._config(text, js_type=False)

    @property
    def rectangle(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Rectangle")

    @rectangle.setter
    def rectangle(self, text: str): self._config(text, js_type=False)

    @property
    def removeButton(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Remove")

    @removeButton.setter
    def removeButton(self, text: str): self._config(text, js_type=False)

    @property
    def saveButton(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Save")

    @saveButton.setter
    def saveButton(self, text: str): self._config(text, js_type=False)

    @property
    def searchIndicators(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Search Indicators")

    @searchIndicators.setter
    def searchIndicators(self, text: str): self._config(text, js_type=False)

    @property
    def segment(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Segment")

    @segment.setter
    def segment(self, text: str): self._config(text, js_type=False)

    @property
    def series(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Series")

    @series.setter
    def series(self, text: str): self._config(text, js_type=False)

    @property
    def shapeOptions(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/NavigationBindingsDefaults.ts
        """
        return self._config_get("Shape options")

    @shapeOptions.setter
    def shapeOptions(self, text: str): self._config(text, js_type=False)

    @property
    def shapes(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/NavigationBindingsDefaults.ts
        """
        return self._config_get("Shape options")

    @shapes.setter
    def shapes(self, text: str): self._config(text, js_type=False)

    @property
    def shortPeriod(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Short period")

    @shortPeriod.setter
    def shortPeriod(self, text: str): self._config(text, js_type=False)

    @property
    def signalPeriod(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Signal period")

    @signalPeriod.setter
    def signalPeriod(self, text: str): self._config(text, js_type=False)

    @property
    def simpleShapes(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/NavigationBindingsDefaults.ts
        """
        return self._config_get("Simple shapes")

    @simpleShapes.setter
    def simpleShapes(self, text: str): self._config(text, js_type=False)

    @property
    def slowAvgPeriod(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Slow average period")

    @slowAvgPeriod.setter
    def slowAvgPeriod(self, text: str): self._config(text, js_type=False)

    @property
    def standardDeviation(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Standard deviation")

    @standardDeviation.setter
    def standardDeviation(self, text: str): self._config(text, js_type=False)

    @property
    def stroke(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/NavigationBindingsDefaults.ts
        """
        return self._config_get("Line color")

    @stroke.setter
    def stroke(self, text: str): self._config(text, js_type=False)

    @property
    def strokeWidth(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/NavigationBindingsDefaults.ts
        """
        return self._config_get("Line width")

    @strokeWidth.setter
    def strokeWidth(self, text: str): self._config(text, js_type=False)

    @property
    def style(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/NavigationBindingsDefaults.ts
        """
        return self._config_get("Style")

    @style.setter
    def style(self, text: str): self._config(text, js_type=False)

    @property
    def timeCycles(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Time Cycles")

    @timeCycles.setter
    def timeCycles(self, text: str): self._config(text, js_type=False)

    @property
    def title(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/NavigationBindingsDefaults.ts
        """
        return self._config_get("Title")

    @title.setter
    def title(self, text: str): self._config(text, js_type=False)

    @property
    def topBand(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Top band")

    @topBand.setter
    def topBand(self, text: str): self._config(text, js_type=False)

    @property
    def tunnel(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Tunnel")

    @tunnel.setter
    def tunnel(self, text: str): self._config(text, js_type=False)

    @property
    def typeOptions(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/NavigationBindingsDefaults.ts
        """
        return self._config_get("Details")

    @typeOptions.setter
    def typeOptions(self, text: str): self._config(text, js_type=False)

    @property
    def verticalArrow(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Vertical arrow")

    @verticalArrow.setter
    def verticalArrow(self, text: str): self._config(text, js_type=False)

    @property
    def verticalCounter(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Vertical counter")

    @verticalCounter.setter
    def verticalCounter(self, text: str): self._config(text, js_type=False)

    @property
    def verticalLabel(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Vertical label")

    @verticalLabel.setter
    def verticalLabel(self, text: str): self._config(text, js_type=False)

    @property
    def verticalLine(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Vertical line")

    @verticalLine.setter
    def verticalLine(self, text: str): self._config(text, js_type=False)

    @property
    def volume(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("Volume")

    @volume.setter
    def volume(self, text: str): self._config(text, js_type=False)

    @property
    def xAxisUnit(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Stock/StockTools/StockToolsDefaults.ts
        """
        return self._config_get("x-axis unit")

    @xAxisUnit.setter
    def xAxisUnit(self, text: str): self._config(text, js_type=False)

        
class OptionLangAccessibilityAnnouncenewdata(Options):

    @property
    def newDataAnnounce(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Updated data for chart {chartTitle}")

    @newDataAnnounce.setter
    def newDataAnnounce(self, text: str): self._config(text, js_type=False)

    @property
    def newPointAnnounceMultiple(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("New data point in chart {chartTitle}: {pointDesc}")

    @newPointAnnounceMultiple.setter
    def newPointAnnounceMultiple(self, text: str): self._config(text, js_type=False)

    @property
    def newPointAnnounceSingle(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("New data point: {pointDesc}")

    @newPointAnnounceSingle.setter
    def newPointAnnounceSingle(self, text: str): self._config(text, js_type=False)

    @property
    def newSeriesAnnounceMultiple(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("New data series in chart {chartTitle}: {seriesDesc}")

    @newSeriesAnnounceMultiple.setter
    def newSeriesAnnounceMultiple(self, text: str): self._config(text, js_type=False)

    @property
    def newSeriesAnnounceSingle(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("New data series: {seriesDesc}")

    @newSeriesAnnounceSingle.setter
    def newSeriesAnnounceSingle(self, text: str): self._config(text, js_type=False)

        
class OptionLangAccessibilityAxis(Options):

    @property
    def rangeCategories(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Data range: {numCategories} categories.")

    @rangeCategories.setter
    def rangeCategories(self, text: str): self._config(text, js_type=False)

    @property
    def rangeFromTo(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Data ranges from {rangeFrom} to {rangeTo}.")

    @rangeFromTo.setter
    def rangeFromTo(self, text: str): self._config(text, js_type=False)

    @property
    def timeRangeDays(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Data range: {range} days.")

    @timeRangeDays.setter
    def timeRangeDays(self, text: str): self._config(text, js_type=False)

    @property
    def timeRangeHours(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Data range: {range} hours.")

    @timeRangeHours.setter
    def timeRangeHours(self, text: str): self._config(text, js_type=False)

    @property
    def timeRangeMinutes(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Data range: {range} minutes.")

    @timeRangeMinutes.setter
    def timeRangeMinutes(self, text: str): self._config(text, js_type=False)

    @property
    def timeRangeSeconds(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Data range: {range} seconds.")

    @timeRangeSeconds.setter
    def timeRangeSeconds(self, text: str): self._config(text, js_type=False)

    @property
    def xAxisDescriptionPlural(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("The chart has {numAxes} X axes displaying {#each names}{#unless @first},{/unless}{#if @last} and{/if} {this}{/each}.")

    @xAxisDescriptionPlural.setter
    def xAxisDescriptionPlural(self, text: str): self._config(text, js_type=False)

    @property
    def xAxisDescriptionSingular(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("The chart has 1 X axis displaying {names[0]}. {ranges[0]}")

    @xAxisDescriptionSingular.setter
    def xAxisDescriptionSingular(self, text: str): self._config(text, js_type=False)

    @property
    def yAxisDescriptionPlural(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("The chart has {numAxes} Y axes displaying {#each names}{#unless @first},{/unless}{#if @last} and{/if} {this}{/each}.")

    @yAxisDescriptionPlural.setter
    def yAxisDescriptionPlural(self, text: str): self._config(text, js_type=False)

    @property
    def yAxisDescriptionSingular(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("The chart has 1 Y axis displaying {names[0]}. {ranges[0]}")

    @yAxisDescriptionSingular.setter
    def yAxisDescriptionSingular(self, text: str): self._config(text, js_type=False)

        
class OptionLangAccessibilityCharttypes(Options):

    @property
    def barMultiple(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Bar chart with {numSeries} data series.")

    @barMultiple.setter
    def barMultiple(self, text: str): self._config(text, js_type=False)

    @property
    def barSingle(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Bar chart with {numPoints} {#eq numPoints 1}bar{else}bars{/eq}.")

    @barSingle.setter
    def barSingle(self, text: str): self._config(text, js_type=False)

    @property
    def boxplotMultiple(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Boxplot with {numSeries} data series.")

    @boxplotMultiple.setter
    def boxplotMultiple(self, text: str): self._config(text, js_type=False)

    @property
    def boxplotSingle(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Boxplot with {numPoints} {#eq numPoints 1}box{else}boxes{/eq}.")

    @boxplotSingle.setter
    def boxplotSingle(self, text: str): self._config(text, js_type=False)

    @property
    def bubbleMultiple(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Bubble chart with {numSeries} data series.")

    @bubbleMultiple.setter
    def bubbleMultiple(self, text: str): self._config(text, js_type=False)

    @property
    def bubbleSingle(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Bubble chart with {numPoints} {#eq numPoints 1}bubbles{else}bubble{/eq}.")

    @bubbleSingle.setter
    def bubbleSingle(self, text: str): self._config(text, js_type=False)

    @property
    def columnMultiple(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Bar chart with {numSeries} data series.")

    @columnMultiple.setter
    def columnMultiple(self, text: str): self._config(text, js_type=False)

    @property
    def columnSingle(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Bar chart with {numPoints} {#eq numPoints 1}bar{else}bars{/eq}.")

    @columnSingle.setter
    def columnSingle(self, text: str): self._config(text, js_type=False)

    @property
    def combinationChart(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Combination chart with {numSeries} data series.")

    @combinationChart.setter
    def combinationChart(self, text: str): self._config(text, js_type=False)

    @property
    def defaultMultiple(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Chart with {numSeries} data series.")

    @defaultMultiple.setter
    def defaultMultiple(self, text: str): self._config(text, js_type=False)

    @property
    def defaultSingle(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Chart with {numPoints} data {#eq numPoints 1}point{else}points{/eq}.")

    @defaultSingle.setter
    def defaultSingle(self, text: str): self._config(text, js_type=False)

    @property
    def emptyChart(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Empty chart")

    @emptyChart.setter
    def emptyChart(self, text: str): self._config(text, js_type=False)

    @property
    def lineMultiple(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Line chart with {numSeries} lines.")

    @lineMultiple.setter
    def lineMultiple(self, text: str): self._config(text, js_type=False)

    @property
    def lineSingle(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Line chart with {numPoints} data {#eq numPoints 1}point{else}points{/eq}.")

    @lineSingle.setter
    def lineSingle(self, text: str): self._config(text, js_type=False)

    @property
    def mapTypeDescription(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Map of {mapTitle} with {numSeries} data series.")

    @mapTypeDescription.setter
    def mapTypeDescription(self, text: str): self._config(text, js_type=False)

    @property
    def pieMultiple(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Pie chart with {numSeries} pies.")

    @pieMultiple.setter
    def pieMultiple(self, text: str): self._config(text, js_type=False)

    @property
    def pieSingle(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Pie chart with {numPoints} {#eq numPoints 1}slice{else}slices{/eq}.")

    @pieSingle.setter
    def pieSingle(self, text: str): self._config(text, js_type=False)

    @property
    def scatterMultiple(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Scatter chart with {numSeries} data series.")

    @scatterMultiple.setter
    def scatterMultiple(self, text: str): self._config(text, js_type=False)

    @property
    def scatterSingle(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Scatter chart with {numPoints} {#eq numPoints 1}point{else}points{/eq}.")

    @scatterSingle.setter
    def scatterSingle(self, text: str): self._config(text, js_type=False)

    @property
    def splineMultiple(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Line chart with {numSeries} lines.")

    @splineMultiple.setter
    def splineMultiple(self, text: str): self._config(text, js_type=False)

    @property
    def splineSingle(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Line chart with {numPoints} data {#eq numPoints 1}point{else}points{/eq}.")

    @splineSingle.setter
    def splineSingle(self, text: str): self._config(text, js_type=False)

    @property
    def unknownMap(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Map of unspecified region with {numSeries} data series.")

    @unknownMap.setter
    def unknownMap(self, text: str): self._config(text, js_type=False)

        
class OptionLangAccessibilityExporting(Options):

    @property
    def chartMenuLabel(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Chart menu")

    @chartMenuLabel.setter
    def chartMenuLabel(self, text: str): self._config(text, js_type=False)

    @property
    def menuButtonLabel(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("View chart menu, {chartTitle}")

    @menuButtonLabel.setter
    def menuButtonLabel(self, text: str): self._config(text, js_type=False)

        
class OptionLangNavigation(Options):

    @property
    def popup(self) -> 'OptionLangNavigationPopup':
        """Translations for all field names used in popup. """
        return self._config_sub_data("popup", OptionLangNavigationPopup)

        
class OptionLangExportdata(Options):

    @property
    def annotationHeader(self):
        """The annotation column title.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/ExportData/ExportDataDefaults.ts
        """
        return self._config_get("Annotations")

    @annotationHeader.setter
    def annotationHeader(self, text: str): self._config(text, js_type=False)

    @property
    def categoryDatetimeHeader(self):
        """The category column title when axis type set to &quot;datetime&quot;.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/ExportData/ExportDataDefaults.ts
        """
        return self._config_get("DateTime")

    @categoryDatetimeHeader.setter
    def categoryDatetimeHeader(self, text: str): self._config(text, js_type=False)

    @property
    def categoryHeader(self):
        """The category column title.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/ExportData/ExportDataDefaults.ts
        """
        return self._config_get("Category")

    @categoryHeader.setter
    def categoryHeader(self, text: str): self._config(text, js_type=False)

        
class OptionLang(Options):

    @property
    def accessibility(self) -> 'OptionLangAccessibility':
        """Configure the accessibility strings in the chart. """
        return self._config_sub_data("accessibility", OptionLangAccessibility)

    @property
    def contextButtonTitle(self):
        """Exporting module menu.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get("Chart context menu")

    @contextButtonTitle.setter
    def contextButtonTitle(self, text: str): self._config(text, js_type=False)

    @property
    def decimalPoint(self):
        """The default decimal point used in the <code>Highcharts.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(".")

    @decimalPoint.setter
    def decimalPoint(self, text: str): self._config(text, js_type=False)

    @property
    def downloadCSV(self):
        """The text for the menu item.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/ExportData/ExportDataDefaults.ts
        """
        return self._config_get("Download CSV")

    @downloadCSV.setter
    def downloadCSV(self, text: str): self._config(text, js_type=False)

    @property
    def downloadJPEG(self):
        """Exporting module only.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get("Download JPEG image")

    @downloadJPEG.setter
    def downloadJPEG(self, text: str): self._config(text, js_type=False)

    @property
    def downloadMIDI(self):
        """The text for the MIDI download menu item in the export menu.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get("Download MIDI")

    @downloadMIDI.setter
    def downloadMIDI(self, text: str): self._config(text, js_type=False)

    @property
    def downloadPDF(self):
        """Exporting module only.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get("Download PDF document")

    @downloadPDF.setter
    def downloadPDF(self, text: str): self._config(text, js_type=False)

    @property
    def downloadPNG(self):
        """Exporting module only.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get("Download PNG image")

    @downloadPNG.setter
    def downloadPNG(self, text: str): self._config(text, js_type=False)

    @property
    def downloadSVG(self):
        """Exporting module only.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get("Download SVG vector image")

    @downloadSVG.setter
    def downloadSVG(self, text: str): self._config(text, js_type=False)

    @property
    def downloadXLS(self):
        """The text for the menu item.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/ExportData/ExportDataDefaults.ts
        """
        return self._config_get("Download XLS")

    @downloadXLS.setter
    def downloadXLS(self, text: str): self._config(text, js_type=False)

    @property
    def drillUpText(self):
        """The text for the button that appears when drilling down, linking back to the parent series.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Drilldown/DrilldownDefaults.ts
        """
        return self._config_get(None)

    @drillUpText.setter
    def drillUpText(self, text: str): self._config(text, js_type=False)

    @property
    def exitFullscreen(self):
        """Exporting module only.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get("Exit from full screen")

    @exitFullscreen.setter
    def exitFullscreen(self, text: str): self._config(text, js_type=False)

    @property
    def exportData(self) -> 'OptionLangExportdata':
        """The text for exported table. """
        return self._config_sub_data("exportData", OptionLangExportdata)

    @property
    def hideData(self):
        """The text for the menu item.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/ExportData/ExportDataDefaults.ts
        """
        return self._config_get("Hide data table")

    @hideData.setter
    def hideData(self, text: str): self._config(text, js_type=False)

    @property
    def invalidDate(self):
        """What to show in a date field for invalid dates.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(None)

    @invalidDate.setter
    def invalidDate(self, text: str): self._config(text, js_type=False)

    @property
    def loading(self):
        """The loading text that appears when the chart is set into the loading state following a call to <code>chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("Loading...")

    @loading.setter
    def loading(self, text: str): self._config(text, js_type=False)

    @property
    def mainBreadcrumb(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Breadcrumbs/BreadcrumbsDefaults.ts
        """
        return self._config_get("Main")

    @mainBreadcrumb.setter
    def mainBreadcrumb(self, text: str): self._config(text, js_type=False)

    @property
    def months(self):
        """An array containing the months names.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(["January", "February", "March", "April", "May", "June",
         "July", "August", "September", "October", "November",
         "December"])

    @months.setter
    def months(self, value: Any): self._config(value, js_type=False)

    @property
    def navigation(self) -> 'OptionLangNavigation':
        """Configure the Popup strings in the chart. """
        return self._config_sub_data("navigation", OptionLangNavigation)

    @property
    def noData(self):
        """The text to display when the chart contains no data.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/NoDataToDisplay/NoDataDefaults.ts
        """
        return self._config_get("No data to display")

    @noData.setter
    def noData(self, text: str): self._config(text, js_type=False)

    @property
    def numericSymbolMagnitude(self):
        """The magnitude of <a href="#lang.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(1000)

    @numericSymbolMagnitude.setter
    def numericSymbolMagnitude(self, num: float): self._config(num, js_type=False)

    @property
    def numericSymbols(self):
        """<a href="https://en.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(["k", "M", "G", "T", "P", "E"])

    @numericSymbols.setter
    def numericSymbols(self, value: Any): self._config(value, js_type=False)

    @property
    def playAsSound(self):
        """The text for the Play as sound menu item in the export menu.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Sonification/Options.ts
        """
        return self._config_get("Play as sound")

    @playAsSound.setter
    def playAsSound(self, text: str): self._config(text, js_type=False)

    @property
    def printChart(self):
        """Exporting module only.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get("Print chart")

    @printChart.setter
    def printChart(self, text: str): self._config(text, js_type=False)

    @property
    def resetZoom(self):
        """The text for the label appearing when a chart is zoomed.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("Reset zoom")

    @resetZoom.setter
    def resetZoom(self, text: str): self._config(text, js_type=False)

    @property
    def resetZoomTitle(self):
        """The tooltip title for the label appearing when a chart is zoomed.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("Reset zoom level 1:1")

    @resetZoomTitle.setter
    def resetZoomTitle(self, text: str): self._config(text, js_type=False)

    @property
    def shortMonths(self):
        """An array containing the months names in abbreviated form.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(["Jan", "Feb", "Mar", "Apr", "May", "Jun",
         "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

    @shortMonths.setter
    def shortMonths(self, value: Any): self._config(value, js_type=False)

    @property
    def shortWeekdays(self):
        """Short week days, starting Sunday.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(None)

    @shortWeekdays.setter
    def shortWeekdays(self, value: Any): self._config(value, js_type=False)

    @property
    def thousandsSep(self):
        """The default thousands separator used in the <code>Highcharts.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get("\u0020")

    @thousandsSep.setter
    def thousandsSep(self, text: str): self._config(text, js_type=False)

    @property
    def viewData(self):
        """The text for the menu item.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/ExportData/ExportDataDefaults.ts
        """
        return self._config_get("View data table")

    @viewData.setter
    def viewData(self, text: str): self._config(text, js_type=False)

    @property
    def viewFullscreen(self):
        """Exporting module only.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get("View in full screen")

    @viewFullscreen.setter
    def viewFullscreen(self, text: str): self._config(text, js_type=False)

    @property
    def weekdays(self):
        """An array containing the weekday names.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Core/Defaults.ts
        """
        return self._config_get(["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
         "Friday", "Saturday"])

    @weekdays.setter
    def weekdays(self, value: Any): self._config(value, js_type=False)

        
class OptionLangAccessibilityZoom(Options):

    @property
    def mapZoomIn(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Zoom chart")

    @mapZoomIn.setter
    def mapZoomIn(self, text: str): self._config(text, js_type=False)

    @property
    def mapZoomOut(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Zoom out chart")

    @mapZoomOut.setter
    def mapZoomOut(self, text: str): self._config(text, js_type=False)

    @property
    def resetZoomButton(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Reset zoom")

    @resetZoomButton.setter
    def resetZoomButton(self, text: str): self._config(text, js_type=False)

        
class OptionLangAccessibilityTable(Options):

    @property
    def tableSummary(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Table representation of chart.")

    @tableSummary.setter
    def tableSummary(self, text: str): self._config(text, js_type=False)

    @property
    def viewAsDataTableButtonText(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("View as data table, {chartTitle}")

    @viewAsDataTableButtonText.setter
    def viewAsDataTableButtonText(self, text: str): self._config(text, js_type=False)

        
class OptionLangAccessibilitySonification(Options):

    @property
    def playAsSoundButtonText(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Play as sound, {chartTitle}")

    @playAsSoundButtonText.setter
    def playAsSoundButtonText(self, text: str): self._config(text, js_type=False)

    @property
    def playAsSoundClickAnnouncement(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Play")

    @playAsSoundClickAnnouncement.setter
    def playAsSoundClickAnnouncement(self, text: str): self._config(text, js_type=False)

        
class OptionLangAccessibilitySeriestypedescriptions(Options):

    @property
    def arearange(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Arearange charts are line charts displaying a range between a lower and higher value for each point.")

    @arearange.setter
    def arearange(self, text: str): self._config(text, js_type=False)

    @property
    def areasplinerange(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("These charts are line charts displaying a range between a lower and higher value for each point.")

    @areasplinerange.setter
    def areasplinerange(self, text: str): self._config(text, js_type=False)

    @property
    def boxplot(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Box plot charts are typically used to display groups of statistical data. Each data point in the chart can have up to 5 values: minimum, lower quartile, median, upper quartile, and maximum.")

    @boxplot.setter
    def boxplot(self, text: str): self._config(text, js_type=False)

    @property
    def bubble(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Bubble charts are scatter charts where each data point also has a size value.")

    @bubble.setter
    def bubble(self, text: str): self._config(text, js_type=False)

    @property
    def columnrange(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Columnrange charts are column charts displaying a range between a lower and higher value for each point.")

    @columnrange.setter
    def columnrange(self, text: str): self._config(text, js_type=False)

    @property
    def errorbar(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Errorbar series are used to display the variability of the data.")

    @errorbar.setter
    def errorbar(self, text: str): self._config(text, js_type=False)

    @property
    def funnel(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Funnel charts are used to display reduction of data in stages.")

    @funnel.setter
    def funnel(self, text: str): self._config(text, js_type=False)

    @property
    def pyramid(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Pyramid charts consist of a single pyramid with item heights corresponding to each point value.")

    @pyramid.setter
    def pyramid(self, text: str): self._config(text, js_type=False)

    @property
    def waterfall(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("A waterfall chart is a column chart where each column contributes towards a total end value.")

    @waterfall.setter
    def waterfall(self, text: str): self._config(text, js_type=False)

        
class OptionLangAccessibilitySeriesSummary(Options):

    @property
    def bar(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("{series.name}, bar series {seriesNumber} of {chart.series.length} with {series.points.length} {#eq series.points.length 1}bar{else}bars{/eq}.")

    @bar.setter
    def bar(self, text: str): self._config(text, js_type=False)

    @property
    def barCombination(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("{series.name}, series {seriesNumber} of {chart.series.length}. Bar series with {series.points.length} {#eq series.points.length 1}bar{else}bars{/eq}.")

    @barCombination.setter
    def barCombination(self, text: str): self._config(text, js_type=False)

    @property
    def boxplot(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("{series.name}, boxplot {seriesNumber} of {chart.series.length} with {series.points.length} {#eq series.points.length 1}box{else}boxes{/eq}.")

    @boxplot.setter
    def boxplot(self, text: str): self._config(text, js_type=False)

    @property
    def boxplotCombination(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("{series.name}, series {seriesNumber} of {chart.series.length}. Boxplot with {series.points.length} {#eq series.points.length 1}box{else}boxes{/eq}.")

    @boxplotCombination.setter
    def boxplotCombination(self, text: str): self._config(text, js_type=False)

    @property
    def bubble(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("{series.name}, bubble series {seriesNumber} of {chart.series.length} with {series.points.length} {#eq series.points.length 1}bubble{else}bubbles{/eq}.")

    @bubble.setter
    def bubble(self, text: str): self._config(text, js_type=False)

    @property
    def bubbleCombination(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("{series.name}, series {seriesNumber} of {chart.series.length}. Bubble series with {series.points.length} {#eq series.points.length 1}bubble{else}bubbles{/eq}.")

    @bubbleCombination.setter
    def bubbleCombination(self, text: str): self._config(text, js_type=False)

    @property
    def column(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("{series.name}, bar series {seriesNumber} of {chart.series.length} with {series.points.length} {#eq series.points.length 1}bar{else}bars{/eq}.")

    @column.setter
    def column(self, text: str): self._config(text, js_type=False)

    @property
    def columnCombination(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("{series.name}, series {seriesNumber} of {chart.series.length}. Bar series with {series.points.length} {#eq series.points.length 1}bar{else}bars{/eq}.")

    @columnCombination.setter
    def columnCombination(self, text: str): self._config(text, js_type=False)

    @property
    def default(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("{series.name}, series {seriesNumber} of {chart.series.length} with {series.points.length} data {#eq series.points.length 1}point{else}points{/eq}.")

    @default.setter
    def default(self, text: str): self._config(text, js_type=False)

    @property
    def defaultCombination(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("{series.name}, series {seriesNumber} of {chart.series.length} with {series.points.length} data {#eq series.points.length 1}point{else}points{/eq}.")

    @defaultCombination.setter
    def defaultCombination(self, text: str): self._config(text, js_type=False)

    @property
    def line(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("{series.name}, line {seriesNumber} of {chart.series.length} with {series.points.length} data {#eq series.points.length 1}point{else}points{/eq}.")

    @line.setter
    def line(self, text: str): self._config(text, js_type=False)

    @property
    def lineCombination(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("{series.name}, series {seriesNumber} of {chart.series.length}. Line with {series.points.length} data {#eq series.points.length 1}point{else}points{/eq}.")

    @lineCombination.setter
    def lineCombination(self, text: str): self._config(text, js_type=False)

    @property
    def map(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("{series.name}, map {seriesNumber} of {chart.series.length} with {series.points.length} {#eq series.points.length 1}area{else}areas{/eq}.")

    @map.setter
    def map(self, text: str): self._config(text, js_type=False)

    @property
    def mapbubble(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("{series.name}, bubble series {seriesNumber} of {chart.series.length} with {series.points.length} {#eq series.points.length 1}bubble{else}bubbles{/eq}.")

    @mapbubble.setter
    def mapbubble(self, text: str): self._config(text, js_type=False)

    @property
    def mapbubbleCombination(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("{series.name}, series {seriesNumber} of {chart.series.length}. Bubble series with {series.points.length} {#eq series.points.length 1}bubble{else}bubbles{/eq}.")

    @mapbubbleCombination.setter
    def mapbubbleCombination(self, text: str): self._config(text, js_type=False)

    @property
    def mapCombination(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("{series.name}, series {seriesNumber} of {chart.series.length}. Map with {series.points.length} {#eq series.points.length 1}area{else}areas{/eq}.")

    @mapCombination.setter
    def mapCombination(self, text: str): self._config(text, js_type=False)

    @property
    def mapline(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("{series.name}, line {seriesNumber} of {chart.series.length} with {series.points.length} data {#eq series.points.length 1}point{else}points{/eq}.")

    @mapline.setter
    def mapline(self, text: str): self._config(text, js_type=False)

    @property
    def maplineCombination(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("{series.name}, series {seriesNumber} of {chart.series.length}. Line with {series.points.length} data {#eq series.points.length 1}point{else}points{/eq}.")

    @maplineCombination.setter
    def maplineCombination(self, text: str): self._config(text, js_type=False)

    @property
    def pie(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("{series.name}, pie {seriesNumber} of {chart.series.length} with {series.points.length} {#eq series.points.length 1}slice{else}slices{/eq}.")

    @pie.setter
    def pie(self, text: str): self._config(text, js_type=False)

    @property
    def pieCombination(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("{series.name}, series {seriesNumber} of {chart.series.length}. Pie with {series.points.length} {#eq series.points.length 1}slice{else}slices{/eq}.")

    @pieCombination.setter
    def pieCombination(self, text: str): self._config(text, js_type=False)

    @property
    def scatter(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("{series.name}, scatter plot {seriesNumber} of {chart.series.length} with {series.points.length} {#eq series.points.length 1}point{else}points{/eq}.")

    @scatter.setter
    def scatter(self, text: str): self._config(text, js_type=False)

    @property
    def scatterCombination(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("{series.name}, series {seriesNumber} of {chart.series.length}, scatter plot with {series.points.length} {#eq series.points.length 1}point{else}points{/eq}.")

    @scatterCombination.setter
    def scatterCombination(self, text: str): self._config(text, js_type=False)

    @property
    def spline(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("{series.name}, line {seriesNumber} of {chart.series.length} with {series.points.length} data {#eq series.points.length 1}point{else}points{/eq}.")

    @spline.setter
    def spline(self, text: str): self._config(text, js_type=False)

    @property
    def splineCombination(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("{series.name}, series {seriesNumber} of {chart.series.length}. Line with {series.points.length} data {#eq series.points.length 1}point{else}points{/eq}.")

    @splineCombination.setter
    def splineCombination(self, text: str): self._config(text, js_type=False)

        
class OptionLangAccessibilitySeries(Options):

    @property
    def description(self):
        """User supplied description text.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("{description}")

    @description.setter
    def description(self, text: str): self._config(text, js_type=False)

    @property
    def nullPointValue(self):
        """Description for the value of null points.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("No value")

    @nullPointValue.setter
    def nullPointValue(self, text: str): self._config(text, js_type=False)

    @property
    def pointAnnotationsDescription(self):
        """Description for annotations on a point, as it is made available to assistive technology.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("{#each annotations}Annotation: {this}{/each}")

    @pointAnnotationsDescription.setter
    def pointAnnotationsDescription(self, text: str): self._config(text, js_type=False)

    @property
    def summary(self) -> 'OptionLangAccessibilitySeriesSummary':
        """Lang configuration for the series main summary. """
        return self._config_sub_data("summary", OptionLangAccessibilitySeriesSummary)

    @property
    def xAxisDescription(self):
        """xAxis description for series if there are multiple xAxes in the chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("X axis, {name}")

    @xAxisDescription.setter
    def xAxisDescription(self, text: str): self._config(text, js_type=False)

    @property
    def yAxisDescription(self):
        """yAxis description for series if there are multiple yAxes in the chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Y axis, {name}")

    @yAxisDescription.setter
    def yAxisDescription(self, text: str): self._config(text, js_type=False)

        
class OptionLangAccessibilityScreenreadersectionAnnotations(Options):

    @property
    def descriptionMultiplePoints(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("{annotationText}. Related to {annotationPoint}{#each additionalAnnotationPoints}, also related to {this}{/each}")

    @descriptionMultiplePoints.setter
    def descriptionMultiplePoints(self, text: str): self._config(text, js_type=False)

    @property
    def descriptionNoPoints(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("{annotationText}")

    @descriptionNoPoints.setter
    def descriptionNoPoints(self, text: str): self._config(text, js_type=False)

    @property
    def descriptionSinglePoint(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("{annotationText}. Related to {annotationPoint}")

    @descriptionSinglePoint.setter
    def descriptionSinglePoint(self, text: str): self._config(text, js_type=False)

    @property
    def heading(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Chart annotations summary")

    @heading.setter
    def heading(self, text: str): self._config(text, js_type=False)

        
class OptionLangAccessibilityScreenreadersection(Options):

    @property
    def afterRegionLabel(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("")

    @afterRegionLabel.setter
    def afterRegionLabel(self, text: str): self._config(text, js_type=False)

    @property
    def annotations(self) -> 'OptionLangAccessibilityScreenreadersectionAnnotations':
        """Language options for annotation descriptions. """
        return self._config_sub_data("annotations", OptionLangAccessibilityScreenreadersectionAnnotations)

    @property
    def beforeRegionLabel(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("")

    @beforeRegionLabel.setter
    def beforeRegionLabel(self, text: str): self._config(text, js_type=False)

    @property
    def endOfChartMarker(self):
        """Label for the end of the chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("End of interactive chart.")

    @endOfChartMarker.setter
    def endOfChartMarker(self, text: str): self._config(text, js_type=False)

        
class OptionLangAccessibilityRangeselector(Options):

    @property
    def clickButtonAnnouncement(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Viewing {axisRangeDescription}")

    @clickButtonAnnouncement.setter
    def clickButtonAnnouncement(self, text: str): self._config(text, js_type=False)

    @property
    def dropdownLabel(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("{rangeTitle}")

    @dropdownLabel.setter
    def dropdownLabel(self, text: str): self._config(text, js_type=False)

    @property
    def maxInputLabel(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Select end date.")

    @maxInputLabel.setter
    def maxInputLabel(self, text: str): self._config(text, js_type=False)

    @property
    def minInputLabel(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Select start date.")

    @minInputLabel.setter
    def minInputLabel(self, text: str): self._config(text, js_type=False)

        
class OptionLangAccessibilityNavigator(Options):

    @property
    def changeAnnouncement(self):
        """Announcement for assistive technology when navigator values are changed.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("{axisRangeDescription}")

    @changeAnnouncement.setter
    def changeAnnouncement(self, text: str): self._config(text, js_type=False)

    @property
    def groupLabel(self):
        """Label for the navigator region.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Axis zoom")

    @groupLabel.setter
    def groupLabel(self, text: str): self._config(text, js_type=False)

    @property
    def handleLabel(self):
        """Label for the navigator handles.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("{#eq handleIx 0}Start, percent{else}End, percent{/eq}")

    @handleLabel.setter
    def handleLabel(self, text: str): self._config(text, js_type=False)

        
class OptionLangAccessibilityLegend(Options):

    @property
    def legendItem(self):
        """Accessible label for individual legend items.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Show {itemName}")

    @legendItem.setter
    def legendItem(self, text: str): self._config(text, js_type=False)

    @property
    def legendLabel(self):
        """Accessible label for the legend, for charts where there is a legend title defined.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Chart legend: {legendTitle}")

    @legendLabel.setter
    def legendLabel(self, text: str): self._config(text, js_type=False)

    @property
    def legendLabelNoTitle(self):
        """Accessible label for the legend, for charts where there is no legend title defined.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Toggle series visibility, {chartTitle}")

    @legendLabelNoTitle.setter
    def legendLabelNoTitle(self, text: str): self._config(text, js_type=False)

        
class OptionLangAccessibility(Options):

    @property
    def announceNewData(self) -> 'OptionLangAccessibilityAnnouncenewdata':
        """Default announcement for new data in charts. """
        return self._config_sub_data("announceNewData", OptionLangAccessibilityAnnouncenewdata)

    @property
    def axis(self) -> 'OptionLangAccessibilityAxis':
        """Axis description format strings. """
        return self._config_sub_data("axis", OptionLangAccessibilityAxis)

    @property
    def chartContainerLabel(self):
        """Accessible label for the chart container HTML element.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("{title}. Highcharts interactive chart.")

    @chartContainerLabel.setter
    def chartContainerLabel(self, text: str): self._config(text, js_type=False)

    @property
    def chartTypes(self) -> 'OptionLangAccessibilityCharttypes':
        """Chart type description strings. """
        return self._config_sub_data("chartTypes", OptionLangAccessibilityCharttypes)

    @property
    def credits(self):
        """Accessible label for the chart credits.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Chart credits: {creditsStr}")

    @credits.setter
    def credits(self, text: str): self._config(text, js_type=False)

    @property
    def defaultChartTitle(self):
        """Default title of the chart for assistive technology, for charts without a chart title.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Chart")

    @defaultChartTitle.setter
    def defaultChartTitle(self, text: str): self._config(text, js_type=False)

    @property
    def drillUpButton(self):
        """Accessible label for the drill-up button.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("{buttonText}")

    @drillUpButton.setter
    def drillUpButton(self, text: str): self._config(text, js_type=False)

    @property
    def exporting(self) -> 'OptionLangAccessibilityExporting':
        """Exporting menu format strings for accessibility module. """
        return self._config_sub_data("exporting", OptionLangAccessibilityExporting)

    @property
    def graphicContainerLabel(self):
        """Set a label on the container wrapping the SVG.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("")

    @graphicContainerLabel.setter
    def graphicContainerLabel(self, text: str): self._config(text, js_type=False)

    @property
    def legend(self) -> 'OptionLangAccessibilityLegend':
        """Language options for accessibility of the legend. """
        return self._config_sub_data("legend", OptionLangAccessibilityLegend)

    @property
    def navigator(self) -> 'OptionLangAccessibilityNavigator':
        """Navigator language options for accessibility. """
        return self._config_sub_data("navigator", OptionLangAccessibilityNavigator)

    @property
    def rangeSelector(self) -> 'OptionLangAccessibilityRangeselector':
        """Range selector language options for accessibility. """
        return self._config_sub_data("rangeSelector", OptionLangAccessibilityRangeselector)

    @property
    def resetZoomButton(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get(None)

    @resetZoomButton.setter
    def resetZoomButton(self, text: str): self._config(text, js_type=False)

    @property
    def screenReaderSection(self) -> 'OptionLangAccessibilityScreenreadersection':
        """Language options for the screen reader information sections added before and after the charts. """
        return self._config_sub_data("screenReaderSection", OptionLangAccessibilityScreenreadersection)

    @property
    def series(self) -> 'OptionLangAccessibilitySeries':
        """Lang configuration for different series types. """
        return self._config_sub_data("series", OptionLangAccessibilitySeries)

    @property
    def seriesTypeDescriptions(self) -> 'OptionLangAccessibilitySeriestypedescriptions':
        """Descriptions of lesser known series types. """
        return self._config_sub_data("seriesTypeDescriptions", OptionLangAccessibilitySeriestypedescriptions)

    @property
    def sonification(self) -> 'OptionLangAccessibilitySonification':
        """Language options for sonification. """
        return self._config_sub_data("sonification", OptionLangAccessibilitySonification)

    @property
    def svgContainerLabel(self):
        """Accessible label for the chart SVG element.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("Interactive chart")

    @svgContainerLabel.setter
    def svgContainerLabel(self, text: str): self._config(text, js_type=False)

    @property
    def svgContainerTitle(self):
        """Title element text for the chart SVG element.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get("")

    @svgContainerTitle.setter
    def svgContainerTitle(self, text: str): self._config(text, js_type=False)

    @property
    def table(self) -> 'OptionLangAccessibilityTable':
        """Accessibility language options for the data table. """
        return self._config_sub_data("table", OptionLangAccessibilityTable)

    @property
    def thousandsSep(self):
        """Thousands separator to use when formatting numbers for screen readers.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/LangDefaults.ts
        """
        return self._config_get(",")

    @thousandsSep.setter
    def thousandsSep(self, text: str): self._config(text, js_type=False)

    @property
    def zoom(self) -> 'OptionLangAccessibilityZoom':
        """Chart and map zoom accessibility language options. """
        return self._config_sub_data("zoom", OptionLangAccessibilityZoom)
