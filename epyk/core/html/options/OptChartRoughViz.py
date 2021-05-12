
from epyk.core.html.options import Options
from epyk.core.html.options import OptChart


class OptionsChartSharedRoughViz(OptChart.OptionsChartShared):

  def x_label(self, value):
    """
    Description:
    -----------
    Set the label of the x axis.

    Not yet available.

    Related Pages:

      https://github.com/frappe/charts/issues/219

    Attributes:
    ----------
    :param value: String. The axis label.
    """
    self.component.options.xLabel = value

  def y_label(self, value):
    """
    Description:
    -----------
    Set the label of the y axis.

    Not yet available.

    Related Pages:

      https://github.com/frappe/charts/issues/219

    Attributes:
    ----------
    :param value: String. The axis label.
    """
    self.component.options.yLabel = value


class OptionData(Options):
  @property
  def labels(self):
    """
    Description:
    ------------
    Id or class of container element.

    Related Pages:

      https://github.com/jwilber/roughViz#Bar
    """
    return self._config_get([])

  @labels.setter
  def labels(self, values):
    self._config(values)

  @property
  def values(self):
    """
    Description:
    ------------
    Id or class of container element.

    Related Pages:

      https://github.com/jwilber/roughViz#Bar
    """
    return self._config_get([])

  @values.setter
  def values(self, values):
    self._config(values)


class OptionDataXY(Options):

  @property
  def labels(self):
    """
    Description:
    ------------
    Id or class of container element.

    Related Pages:

      https://github.com/jwilber/roughViz#Bar
    """
    return self._config_get([])

  @labels.setter
  def labels(self, values):
    self._config(values)

  @property
  def x(self):
    """
    Description:
    ------------
    Id or class of container element.

    Related Pages:

      https://github.com/jwilber/roughViz#Bar
    """
    return self._config_get([])

  @x.setter
  def x(self, values):
    self._config(values)

  @property
  def y(self):
    """
    Description:
    ------------
    Id or class of container element.

    Related Pages:

      https://github.com/jwilber/roughViz#Bar
    """
    return self._config_get([])

  @y.setter
  def y(self, values):
    self._config(values)

  @property
  def y1(self):
    """
    Description:
    ------------
    Id or class of container element.

    Related Pages:

      https://github.com/jwilber/roughViz#Bar
    """
    return self._config_get([])

  @y1.setter
  def y1(self, values):
    self._config(values)

  def add(self, name, values):
    self.js_tree[name] = values


class RoughVizBar(Options):
  component_properties = ("width", )

  @property
  def data(self):
    """

    :return:
    """
    return self._config_sub_data("data", OptionData)

  @property
  def element(self):
    """
    Description:
    ------------
    Id or class of container element.

    Related Pages:

      https://github.com/jwilber/roughViz#Bar
    """
    return self._config_get()

  @element.setter
  def element(self, html_code):
    self._config(html_code)

  @property
  def axisFontSize(self):
    """
    Description:
    ------------
    Font-size for axes' labels. Default: '1rem'.

    Related Pages:

      https://github.com/jwilber/roughViz#Bar
    """
    return self._config_get('1rem')

  @axisFontSize.setter
  def axisFontSize(self, value):
    self._config(value)

  @property
  def axisRoughness(self):
    """
    Description:
    ------------
    Roughness for x & y axes. Default: 0.5

    Related Pages:

      https://github.com/jwilber/roughViz#Bar
    """
    return self._config_get(0.5)

  @axisRoughness.setter
  def axisRoughness(self, num):
    self._config(num)

  @property
  def fillWeight(self):
    """
    Description:
    ------------
    Weight of inner paths' color. Default: 0.5

    Related Pages:

      https://github.com/jwilber/roughViz#Bar
    """
    return self._config_get(0.5)

  @fillWeight.setter
  def fillWeight(self, num):
    self._config(num)

  @property
  def font(self):
    """
    Description:
    ------------
    Font-family to use. You can use 0 or gaegu to use Gaegu, or 1 or indie flower to use Indie Flower.

    Related Pages:

      https://github.com/jwilber/roughViz#Bar
    """
    return self._config_get()

  @font.setter
  def font(self, text):
    self._config(text)

  @property
  def highlight(self):
    """
    Description:
    ------------
    FColor for each bar on hover. Default: 'coral'.

    Related Pages:

      https://github.com/jwilber/roughViz#Bar
    """
    return self._config_get()

  @highlight.setter
  def highlight(self, color):
    self._config(color)

  @property
  def height(self):
    """
    Description:
    ------------
    Chart title. Optional.

    Related Pages:

      https://github.com/jwilber/roughViz#Bar
    """
    return self._config_get()

  @height.setter
  def height(self, num):
    self._config(num)

  @property
  def innerStrokeWidth(self):
    """
    Description:
    ------------
    Stroke-width for paths inside bars. Default: 1.

    Related Pages:

      https://github.com/jwilber/roughViz#Bar
    """
    return self._config_get(1)

  @innerStrokeWidth.setter
  def innerStrokeWidth(self, num):
    self._config(num)

  @property
  def interactive(self):
    """
    Description:
    ------------
    Whether or not chart is interactive. Default: true..

    Related Pages:

      https://github.com/jwilber/roughViz#Bar
    """
    return self._config_get(True)

  @interactive.setter
  def interactive(self, num):
    self._config(num)

  @property
  def labelFontSize(self):
    """
    Description:
    ------------
    Font-size for axes' labels. Default: '1rem'.

    Related Pages:

      https://github.com/jwilber/roughViz#Bar
    """
    return self._config_get('1rem')

  @labelFontSize.setter
  def labelFontSize(self, text):
    self._config(text)

  @property
  def margin(self):
    """
    Description:
    ------------
    Margin object. Default: {top: 50, right: 20, bottom: 70, left: 100}.

    Related Pages:

      https://github.com/jwilber/roughViz#Bar
    """
    return self._config_get({"top": 50, "right": 20, "bottom": 70, "left": 100})

  @margin.setter
  def margin(self, text):
    self._config(text)

  @property
  def padding(self):
    """
    Description:
    ------------
    Padding between bars. Default: 0.1.

    Related Pages:

      https://github.com/jwilber/roughViz#Bar
    """
    return self._config_get(0.1)

  @padding.setter
  def padding(self, value):
    self._config(value)

  @property
  def roughness(self):
    """
    Description:
    ------------
    Roughness level of chart. Default: 1.

    Related Pages:

      https://github.com/jwilber/roughViz#Bar
    """
    return self._config_get(1)

  @roughness.setter
  def roughness(self, value):
    self._config(value)

  @property
  def simplification(self):
    """
    Description:
    ------------
    Chart simplification. Default 0.2.

    Related Pages:

      https://github.com/jwilber/roughViz#Bar
    """
    return self._config_get(0.2)

  @simplification.setter
  def simplification(self, value):
    self._config(value)

  @property
  def color(self):
    """
    Description:
    ------------
    Chart title. Optional.

    Related Pages:

      https://github.com/jwilber/roughViz#Bar
    """
    return self._config_get()

  @color.setter
  def color(self, value):
    self._config(value)

  @property
  def stroke(self):
    """
    Description:
    ------------
    Chart title. Optional.

    Related Pages:

      https://github.com/jwilber/roughViz#Bar
    """
    return self._config_get()

  @stroke.setter
  def stroke(self, value):
    self._config(value)

  @property
  def strokeWidth(self):
    """
    Description:
    ------------
    Chart title. Optional.

    Related Pages:

      https://github.com/jwilber/roughViz#Bar
    """
    return self._config_get()

  @strokeWidth.setter
  def strokeWidth(self, num):
    self._config(num)

  @property
  def title(self):
    """
    Description:
    ------------
    Chart title. Optional.

    Related Pages:

      https://github.com/jwilber/roughViz#Bar
    """
    return self._config_get()

  @title.setter
  def title(self, text):
    self._config(text)

  @property
  def titleFontSize(self):
    """
    Description:
    ------------
    Font-size for chart title. Default: '1rem'.

    Related Pages:

      https://github.com/jwilber/roughViz#Bar
    """
    return self._config_get('1rem')

  @titleFontSize.setter
  def titleFontSize(self, text):
    self._config(text)

  @property
  def tooltipFontSize(self):
    """
    Description:
    ------------
    Font-size for tooltip. Default: '0.95rem'.

    Related Pages:

      https://github.com/jwilber/roughViz#Bar
    """
    return self._config_get('0.95rem')

  @tooltipFontSize.setter
  def tooltipFontSize(self, text):
    self._config(text)

  @property
  def xLabel(self):
    """
    Description:
    ------------
    Label for x-axis.

    Related Pages:

      https://github.com/jwilber/roughViz#Bar
    """
    return self._config_get()

  @xLabel.setter
  def xLabel(self, text):
    self._config(text)

  @property
  def yLabel(self):
    """
    Description:
    ------------
    Label for y-axis.

    Related Pages:

      https://github.com/jwilber/roughViz#Bar
    """
    return self._config_get()

  @yLabel.setter
  def yLabel(self, text):
    self._config(text)

  @property
  def width(self):
    """
    Description:
    ------------
    Chart title. Optional.

    Related Pages:

      https://github.com/jwilber/roughViz#Bar
    """
    return self._config_get("window.innerWidth")

  @width.setter
  def width(self, num):
    self._config(num, js_type=True)


class RoughVizPie(RoughVizBar):

  @property
  def fillStyle(self):
    """
    Description:
    ------------
    Bar fill-style. Should be one of fillStyles shown above.

    Related Pages:

      https://github.com/jwilber/roughViz#Bar
    """
    return self._config_get()

  @fillStyle.setter
  def fillStyle(self, text):
    self._config(text)

  @property
  def legend(self):
    """
    Description:
    ------------
    Whether or not to add legend. Default: 'true.

    Related Pages:

      https://github.com/jwilber/roughViz#Bar
    """
    return self._config_get(True)

  @legend.setter
  def legend(self, flag):
    self._config(flag)

  @property
  def legendPosition(self):
    """
    Description:
    ------------
    Position of legend. Should be either 'left' or 'right'. Default: 'right'.

    Related Pages:

      https://github.com/jwilber/roughViz#Bar
    """
    return self._config_get('right')

  @legendPosition.setter
  def legendPosition(self, text):
    self._config(text)

  @property
  def colors(self):
    """
    Description:
    ------------
    Array of colors for each arc.

    Related Pages:

      https://github.com/jwilber/roughViz#Pie
    """
    return self._config_get()

  @colors.setter
  def colors(self, values):
    self._config(values)


class RoughVizLine(RoughVizBar):

  @property
  def data(self):
    """
    Description:
    ------------

    """
    return self._config_sub_data("data", OptionDataXY)

  @property
  def circle(self):
    """
    Description:
    ------------
    Whether or not to add circles to chart. Default: true.

    Related Pages:

      https://github.com/jwilber/roughViz#Line
    """
    return self._config_get(True)

  @circle.setter
  def circle(self, text):
    self._config(text)

  @property
  def circleRadius(self):
    """
    Description:
    ------------
    Radius of circles. Default: 10.

    Related Pages:

      https://github.com/jwilber/roughViz#Line
    """
    return self._config_get(10)

  @circleRadius.setter
  def circleRadius(self, num):
    self._config(num)

  @property
  def circleRoughness(self):
    """
    Description:
    ------------
    Roughness of circles. Default: 2.

    Related Pages:

      https://github.com/jwilber/roughViz#Line
    """
    return self._config_get(2)

  @circleRoughness.setter
  def circleRoughness(self, num):
    self._config(num)

  @property
  def colors(self):
    """
    Description:
    ------------
    Array of colors for each arc.

    Related Pages:

      https://github.com/jwilber/roughViz#Line
    """
    return self._config_get()

  @colors.setter
  def colors(self, values):
    self._config(values)


class RoughVizScatter(RoughVizBar):

  @property
  def data(self):
    """

    :return:
    """
    return self._config_sub_data("data", OptionDataXY)

  @property
  def colors(self):
    """
    Description:
    ------------
    Array of colors for each arc.

    Related Pages:

      https://github.com/jwilber/roughViz#Scatter
    """
    return self._config_get()

  @colors.setter
  def colors(self, values):
    self._config(values)

  @property
  def colorVar(self):
    """
    Description:
    ------------
    Array of colors for each arc.

    Related Pages:

      https://github.com/jwilber/roughViz#Scatter
    """
    return self._config_get()

  @colorVar.setter
  def colorVar(self, text):
    self._config(text)

  @property
  def highlightLabel(self):
    """
    Description:
    ------------
    If input data is csv or tsv, this should be a column representing what value to display on hover.
    Otherwise, (x, y) values will be shown on hover.

    Related Pages:

      https://github.com/jwilber/roughViz#Scatter
    """
    return self._config_get()

  @highlightLabel.setter
  def highlightLabel(self, text):
    self._config(text)

  @property
  def radius(self):
    """
    Description:
    ------------
    Circle radius. Default: .

    Related Pages:

      https://github.com/jwilber/roughViz#Scatter
    """
    return self._config_get(8)

  @radius.setter
  def radius(self, num):
    self._config(num)
