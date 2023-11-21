from epyk.core.html.options import Options
from typing import Any

        
class OptionAnnotationsShapes(Options):

    @property
    def dashStyle(self):
        """Name of the dash style to use for the shape&#39;s stroke.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(None)

    @dashStyle.setter
    def dashStyle(self, text: str): self._config(text, js_type=False)

    @property
    def fill(self):
        """The color of the shape&#39;s fill.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get("rgba(0, 0, 0, 0.75)")

    @fill.setter
    def fill(self, text: str): self._config(text, js_type=False)

    @property
    def height(self):
        """The height of the shape.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(None)

    @height.setter
    def height(self, num: float): self._config(num, js_type=False)

    @property
    def markerEnd(self):
        """Id of the marker which will be drawn at the final vertex of the path.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(None)

    @markerEnd.setter
    def markerEnd(self, text: str): self._config(text, js_type=False)

    @property
    def markerStart(self):
        """Id of the marker which will be drawn at the first vertex of the path.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(None)

    @markerStart.setter
    def markerStart(self, text: str): self._config(text, js_type=False)

    @property
    def point(self):
        """This option defines the point to which the shape will be connected.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(None)

    @point.setter
    def point(self, text: str): self._config(text, js_type=False)

    @property
    def points(self):
        """An array of points for the shape or a callback function that returns that shape point.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(None)

    @points.setter
    def points(self, value: Any): self._config(value, js_type=False)

    @property
    def r(self):
        """The radius of the shape.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get('0')

    @r.setter
    def r(self, text: str): self._config(text, js_type=True)

    @property
    def ry(self):
        """The radius of the shape in y direction.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(None)

    @ry.setter
    def ry(self, num: float): self._config(num, js_type=False)

    @property
    def snap(self):
        """Defines additional snapping area around an annotation making this annotation to focus.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(2)

    @snap.setter
    def snap(self, num: float): self._config(num, js_type=False)

    @property
    def src(self):
        """The URL for an image to use as the annotation shape.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(None)

    @src.setter
    def src(self, text: str): self._config(text, js_type=False)

    @property
    def stroke(self):
        """The color of the shape&#39;s stroke.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get("rgba(0, 0, 0, 0.75)")

    @stroke.setter
    def stroke(self, text: str): self._config(text, js_type=False)

    @property
    def strokeWidth(self):
        """The pixel stroke width of the shape.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(1)

    @strokeWidth.setter
    def strokeWidth(self, num: float): self._config(num, js_type=False)

    @property
    def type(self):
        """The type of the shape.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get("rect")

    @type.setter
    def type(self, text: str): self._config(text, js_type=False)

    @property
    def width(self):
        """The width of the shape.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(None)

    @width.setter
    def width(self, num: float): self._config(num, js_type=False)

    @property
    def xAxis(self):
        """The xAxis index to which the points should be attached.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(None)

    @xAxis.setter
    def xAxis(self, num: float): self._config(num, js_type=False)

    @property
    def yAxis(self):
        """The yAxis index to which the points should be attached.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(None)

    @yAxis.setter
    def yAxis(self, num: float): self._config(num, js_type=False)

        
class OptionAnnotationsShapeoptions(Options):

    @property
    def dashStyle(self):
        """Name of the dash style to use for the shape&#39;s stroke.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(None)

    @dashStyle.setter
    def dashStyle(self, text: str): self._config(text, js_type=False)

    @property
    def fill(self):
        """The color of the shape&#39;s fill.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get("rgba(0, 0, 0, 0.75)")

    @fill.setter
    def fill(self, text: str): self._config(text, js_type=False)

    @property
    def height(self):
        """The height of the shape.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(None)

    @height.setter
    def height(self, num: float): self._config(num, js_type=False)

    @property
    def r(self):
        """The radius of the shape.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get('0')

    @r.setter
    def r(self, text: str): self._config(text, js_type=True)

    @property
    def ry(self):
        """The radius of the shape in y direction.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(None)

    @ry.setter
    def ry(self, num: float): self._config(num, js_type=False)

    @property
    def snap(self):
        """Defines additional snapping area around an annotation making this annotation to focus.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(2)

    @snap.setter
    def snap(self, num: float): self._config(num, js_type=False)

    @property
    def src(self):
        """The URL for an image to use as the annotation shape.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(None)

    @src.setter
    def src(self, text: str): self._config(text, js_type=False)

    @property
    def stroke(self):
        """The color of the shape&#39;s stroke.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get("rgba(0, 0, 0, 0.75)")

    @stroke.setter
    def stroke(self, text: str): self._config(text, js_type=False)

    @property
    def strokeWidth(self):
        """The pixel stroke width of the shape.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(1)

    @strokeWidth.setter
    def strokeWidth(self, num: float): self._config(num, js_type=False)

    @property
    def type(self):
        """The type of the shape.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get("rect")

    @type.setter
    def type(self, text: str): self._config(text, js_type=False)

    @property
    def width(self):
        """The width of the shape.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(None)

    @width.setter
    def width(self, num: float): self._config(num, js_type=False)

    @property
    def xAxis(self):
        """The xAxis index to which the points should be attached.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(None)

    @xAxis.setter
    def xAxis(self, num: float): self._config(num, js_type=False)

    @property
    def yAxis(self):
        """The yAxis index to which the points should be attached.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(None)

    @yAxis.setter
    def yAxis(self, num: float): self._config(num, js_type=False)

        
class OptionAnnotationsLabelsAccessibility(Options):

    @property
    def description(self):
        """Description of an annotation label for screen readers and other assistive technology.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(None)

    @description.setter
    def description(self, text: str): self._config(text, js_type=False)

        
class OptionAnnotationsLabels(Options):

    @property
    def accessibility(self) -> 'OptionAnnotationsLabelsAccessibility':
        """Accessibility options for an annotation label. """
        return self._config_sub_data("accessibility", OptionAnnotationsLabelsAccessibility)

    @property
    def align(self):
        """The alignment of the annotation&#39;s label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get("center")

    @align.setter
    def align(self, text: str): self._config(text, js_type=False)

    @property
    def allowOverlap(self):
        """Whether to allow the annotation&#39;s labels to overlap.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(False)

    @allowOverlap.setter
    def allowOverlap(self, flag: bool): self._config(flag, js_type=False)

    @property
    def backgroundColor(self):
        """The background color or gradient for the annotation&#39;s label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get("rgba(0, 0, 0, 0.75)")

    @backgroundColor.setter
    def backgroundColor(self, text: str): self._config(text, js_type=False)

    @property
    def borderColor(self):
        """The border color for the annotation&#39;s label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get("#000000")

    @borderColor.setter
    def borderColor(self, text: str): self._config(text, js_type=False)

    @property
    def borderRadius(self):
        """The border radius in pixels for the annotaiton&#39;s label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(3)

    @borderRadius.setter
    def borderRadius(self, num: float): self._config(num, js_type=False)

    @property
    def borderWidth(self):
        """The border width in pixels for the annotation&#39;s label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(1)

    @borderWidth.setter
    def borderWidth(self, num: float): self._config(num, js_type=False)

    @property
    def className(self):
        """A class name for styling by CSS.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get("highcharts-no-tooltip")

    @className.setter
    def className(self, text: str): self._config(text, js_type=False)

    @property
    def crop(self):
        """Whether to hide the annotation&#39;s label that is outside the plot area.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(False)

    @crop.setter
    def crop(self, flag: bool): self._config(flag, js_type=False)

    @property
    def distance(self):
        """The label&#39;s pixel distance from the point.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(None)

    @distance.setter
    def distance(self, num: float): self._config(num, js_type=False)

    @property
    def format(self):
        """A <a href="https://www.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(None)

    @format.setter
    def format(self, text: str): self._config(text, js_type=False)

    @property
    def formatter(self):
        """Callback JavaScript function to format the annotation&#39;s label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get("function () { return defined(this.y) ? this.y : 'Annotation label'; }")

    @formatter.setter
    def formatter(self, text: str): self._config(text, js_type=True)

    @property
    def includeInDataExport(self):
        """Whether the annotation is visible in the exported data table.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(True)

    @includeInDataExport.setter
    def includeInDataExport(self, flag: bool): self._config(flag, js_type=False)

    @property
    def overflow(self):
        """How to handle the annotation&#39;s label that flow outside the plot area.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get("justify")

    @overflow.setter
    def overflow(self, text: str): self._config(text, js_type=False)

    @property
    def padding(self):
        """When either the borderWidth or the backgroundColor is set, this is the padding within the box.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(5)

    @padding.setter
    def padding(self, num: float): self._config(num, js_type=False)

    @property
    def point(self):
        """This option defines the point to which the label will be connected.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(None)

    @point.setter
    def point(self, text: str): self._config(text, js_type=False)

    @property
    def shadow(self):
        """The shadow of the box.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(False)

    @shadow.setter
    def shadow(self, flag: bool): self._config(flag, js_type=False)

    @property
    def shape(self):
        """The name of a symbol to use for the border around the label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get("callout")

    @shape.setter
    def shape(self, text: str): self._config(text, js_type=False)

    @property
    def style(self):
        """Styles for the annotation&#39;s label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(None)

    @style.setter
    def style(self, value: Any): self._config(value, js_type=False)

    @property
    def text(self):
        """Alias for the format option.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(None)

    @text.setter
    def text(self, text: str): self._config(text, js_type=False)

    @property
    def useHTML(self):
        """Whether to <a href="https://www.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(False)

    @useHTML.setter
    def useHTML(self, flag: bool): self._config(flag, js_type=False)

    @property
    def verticalAlign(self):
        """The vertical alignment of the annotation&#39;s label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get("bottom")

    @verticalAlign.setter
    def verticalAlign(self, text: str): self._config(text, js_type=False)

    @property
    def x(self):
        """The x position offset of the label relative to the point.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(0)

    @x.setter
    def x(self, num: float): self._config(num, js_type=False)

    @property
    def y(self):
        """The y position offset of the label relative to the point.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(-16)

    @y.setter
    def y(self, num: float): self._config(num, js_type=False)

        
class OptionAnnotationsLabeloptionsAccessibility(Options):

    @property
    def description(self):
        """Description of an annotation label for screen readers and other assistive technology.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(None)

    @description.setter
    def description(self, text: str): self._config(text, js_type=False)

        
class OptionAnnotationsLabeloptions(Options):

    @property
    def accessibility(self) -> 'OptionAnnotationsLabeloptionsAccessibility':
        """Accessibility options for an annotation label. """
        return self._config_sub_data("accessibility", OptionAnnotationsLabeloptionsAccessibility)

    @property
    def align(self):
        """The alignment of the annotation&#39;s label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get("center")

    @align.setter
    def align(self, text: str): self._config(text, js_type=False)

    @property
    def allowOverlap(self):
        """Whether to allow the annotation&#39;s labels to overlap.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(False)

    @allowOverlap.setter
    def allowOverlap(self, flag: bool): self._config(flag, js_type=False)

    @property
    def backgroundColor(self):
        """The background color or gradient for the annotation&#39;s label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get("rgba(0, 0, 0, 0.75)")

    @backgroundColor.setter
    def backgroundColor(self, text: str): self._config(text, js_type=False)

    @property
    def borderColor(self):
        """The border color for the annotation&#39;s label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get("#000000")

    @borderColor.setter
    def borderColor(self, text: str): self._config(text, js_type=False)

    @property
    def borderRadius(self):
        """The border radius in pixels for the annotaiton&#39;s label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(3)

    @borderRadius.setter
    def borderRadius(self, num: float): self._config(num, js_type=False)

    @property
    def borderWidth(self):
        """The border width in pixels for the annotation&#39;s label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(1)

    @borderWidth.setter
    def borderWidth(self, num: float): self._config(num, js_type=False)

    @property
    def className(self):
        """A class name for styling by CSS.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get("highcharts-no-tooltip")

    @className.setter
    def className(self, text: str): self._config(text, js_type=False)

    @property
    def crop(self):
        """Whether to hide the annotation&#39;s label that is outside the plot area.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(False)

    @crop.setter
    def crop(self, flag: bool): self._config(flag, js_type=False)

    @property
    def distance(self):
        """The label&#39;s pixel distance from the point.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(None)

    @distance.setter
    def distance(self, num: float): self._config(num, js_type=False)

    @property
    def format(self):
        """A <a href="https://www.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(None)

    @format.setter
    def format(self, text: str): self._config(text, js_type=False)

    @property
    def formatter(self):
        """Callback JavaScript function to format the annotation&#39;s label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get("function () { return defined(this.y) ? this.y : 'Annotation label'; }")

    @formatter.setter
    def formatter(self, text: str): self._config(text, js_type=True)

    @property
    def includeInDataExport(self):
        """Whether the annotation is visible in the exported data table.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(True)

    @includeInDataExport.setter
    def includeInDataExport(self, flag: bool): self._config(flag, js_type=False)

    @property
    def overflow(self):
        """How to handle the annotation&#39;s label that flow outside the plot area.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get("justify")

    @overflow.setter
    def overflow(self, text: str): self._config(text, js_type=False)

    @property
    def padding(self):
        """When either the borderWidth or the backgroundColor is set, this is the padding within the box.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(5)

    @padding.setter
    def padding(self, num: float): self._config(num, js_type=False)

    @property
    def shadow(self):
        """The shadow of the box.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(False)

    @shadow.setter
    def shadow(self, flag: bool): self._config(flag, js_type=False)

    @property
    def shape(self):
        """The name of a symbol to use for the border around the label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get("callout")

    @shape.setter
    def shape(self, text: str): self._config(text, js_type=False)

    @property
    def style(self):
        """Styles for the annotation&#39;s label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(None)

    @style.setter
    def style(self, value: Any): self._config(value, js_type=False)

    @property
    def text(self):
        """Alias for the format option.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(None)

    @text.setter
    def text(self, text: str): self._config(text, js_type=False)

    @property
    def useHTML(self):
        """Whether to <a href="https://www.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(False)

    @useHTML.setter
    def useHTML(self, flag: bool): self._config(flag, js_type=False)

    @property
    def verticalAlign(self):
        """The vertical alignment of the annotation&#39;s label.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get("bottom")

    @verticalAlign.setter
    def verticalAlign(self, text: str): self._config(text, js_type=False)

    @property
    def x(self):
        """The x position offset of the label relative to the point.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(0)

    @x.setter
    def x(self, num: float): self._config(num, js_type=False)

    @property
    def y(self):
        """The y position offset of the label relative to the point.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(-16)

    @y.setter
    def y(self, num: float): self._config(num, js_type=False)

        
class OptionAnnotationsAnimation(Options):

    @property
    def defer(self):
        """The animation delay time in milliseconds.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(None)

    @defer.setter
    def defer(self, num: float): self._config(num, js_type=False)

        
class OptionAnnotationsEvents(Options):

    @property
    def add(self):
        """Event callback when annotation is added to the chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(None)

    @add.setter
    def add(self, value: Any): self._config(value, js_type=False)

    @property
    def afterUpdate(self):
        """Event callback when annotation is updated (e.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(None)

    @afterUpdate.setter
    def afterUpdate(self, value: Any): self._config(value, js_type=False)

    @property
    def click(self):
        """Fires when the annotation is clicked.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(None)

    @click.setter
    def click(self, value: Any): self._config(value, js_type=False)

    @property
    def drag(self):
        """Fires when the annotation is dragged.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(None)

    @drag.setter
    def drag(self, value: Any): self._config(value, js_type=False)

    @property
    def remove(self):
        """Event callback when annotation is removed from the chart.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(None)

    @remove.setter
    def remove(self, value: Any): self._config(value, js_type=False)

        
class OptionAnnotations(Options):

    @property
    def animation(self) -> 'OptionAnnotationsAnimation':
        """Enable or disable the initial animation when a series is displayed for the <code>annotation</code>. """
        return self._config_sub_data("animation", OptionAnnotationsAnimation)

    @property
    def controlPointOptions(self) -> 'OptionAnnotationsControlpointoptions':
        """Options for annotation&#39;s control points. """
        return self._config_sub_data("controlPointOptions", OptionAnnotationsControlpointoptions)

    @property
    def crop(self):
        """Whether to hide the part of the annotation that is outside the plot area.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(True)

    @crop.setter
    def crop(self, flag: bool): self._config(flag, js_type=False)

    @property
    def draggable(self):
        """Allow an annotation to be draggable by a user.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get("xy")

    @draggable.setter
    def draggable(self, text: str): self._config(text, js_type=False)

    @property
    def events(self) -> 'OptionAnnotationsEvents':
        """Events available in annotations. """
        return self._config_sub_data("events", OptionAnnotationsEvents)

    @property
    def id(self):
        """Sets an ID for an annotation.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(None)

    @id.setter
    def id(self, num: float): self._config(num, js_type=False)

    @property
    def labelOptions(self) -> 'OptionAnnotationsLabeloptions':
        """Options for annotation&#39;s labels. """
        return self._config_sub_data("labelOptions", OptionAnnotationsLabeloptions)

    @property
    def labels(self) -> 'OptionAnnotationsLabels':
        """An array of labels for the annotation. """
        return self._config_sub_data("labels", OptionAnnotationsLabels)

    @property
    def shapeOptions(self) -> 'OptionAnnotationsShapeoptions':
        """Options for annotation&#39;s shapes. """
        return self._config_sub_data("shapeOptions", OptionAnnotationsShapeoptions)

    @property
    def shapes(self) -> 'OptionAnnotationsShapes':
        """An array of shapes for the annotation. """
        return self._config_sub_data("shapes", OptionAnnotationsShapes)

    @property
    def visible(self):
        """Whether the annotation is visible.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(True)

    @visible.setter
    def visible(self, flag: bool): self._config(flag, js_type=False)

    @property
    def zIndex(self):
        """The Z index of the annotation.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(6)

    @zIndex.setter
    def zIndex(self, num: float): self._config(num, js_type=False)

        
class OptionAnnotationsControlpointoptionsStyle(Options):

    @property
    def cursor(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get("pointer")

    @cursor.setter
    def cursor(self, text: str): self._config(text, js_type=False)

    @property
    def fill(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get("#ffffff")

    @fill.setter
    def fill(self, text: str): self._config(text, js_type=False)

    @property
    def stroke(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get("#000000")

    @stroke.setter
    def stroke(self, text: str): self._config(text, js_type=False)

    @property
    def stroke_width(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(2)

    @stroke_width.setter
    def stroke_width(self, num: float): self._config(num, js_type=False)

        
class OptionAnnotationsControlpointoptions(Options):

    @property
    def events(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(None)

    @events.setter
    def events(self, value: Any): self._config(value, js_type=False)

    @property
    def height(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(10)

    @height.setter
    def height(self, num: float): self._config(num, js_type=False)

    @property
    def positioner(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(None)

    @positioner.setter
    def positioner(self, value: Any): self._config(value, js_type=False)

    @property
    def style(self) -> 'OptionAnnotationsControlpointoptionsStyle':
        """. """
        return self._config_sub_data("style", OptionAnnotationsControlpointoptionsStyle)

    @property
    def symbol(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get("circle")

    @symbol.setter
    def symbol(self, text: str): self._config(text, js_type=False)

    @property
    def visible(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(False)

    @visible.setter
    def visible(self, flag: bool): self._config(flag, js_type=False)

    @property
    def width(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(10)

    @width.setter
    def width(self, num: float): self._config(num, js_type=False)
