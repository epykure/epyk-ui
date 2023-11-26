from epyk.core.html.options import Options
from typing import Any

        
class OptionNavigationAnnotationsoptionsEvents(Options):

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

        
class OptionNavigationAnnotationsoptionsAnimation(Options):

    @property
    def defer(self):
        """The animation delay time in milliseconds.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(None)

    @defer.setter
    def defer(self, num: float): self._config(num, js_type=False)

        
class OptionNavigationBindingsEllipseannotation(Options):

    @property
    def className(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/NavigationBindingsDefaults.ts
        """
        return self._config_get("highcharts-ellipse-annotation")

    @className.setter
    def className(self, text: str): self._config(text, js_type=False)

        
class OptionNavigationBreadcrumbsEvents(Options):

    @property
    def click(self):
        """Fires when clicking on the breadcrumbs button.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Breadcrumbs/BreadcrumbsDefaults.ts
        """
        return self._config_get(None)

    @click.setter
    def click(self, value: Any): self._config(value, js_type=False)

        
class OptionNavigationBindings(Options):

    @property
    def circleAnnotation(self):
        """A circle annotation bindings.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/NavigationBindingsDefaults.ts
        """
        return self._config_get(None)

    @circleAnnotation.setter
    def circleAnnotation(self, value: Any): self._config(value, js_type=False)

    @property
    def ellipseAnnotation(self) -> 'OptionNavigationBindingsEllipseannotation':
        """A ellipse annotation bindings. """
        return self._config_sub_data("ellipseAnnotation", OptionNavigationBindingsEllipseannotation)

    @property
    def labelAnnotation(self):
        """A label annotation bindings.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/NavigationBindingsDefaults.ts
        """
        return self._config_get(None)

    @labelAnnotation.setter
    def labelAnnotation(self, value: Any): self._config(value, js_type=False)

    @property
    def rectangleAnnotation(self):
        """A rectangle annotation bindings.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/NavigationBindingsDefaults.ts
        """
        return self._config_get(None)

    @rectangleAnnotation.setter
    def rectangleAnnotation(self, value: Any): self._config(value, js_type=False)

        
class OptionNavigationEvents(Options):

    @property
    def closePopup(self):
        """A <code>closePopup</code> event.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/NavigationBindingsDefaults.ts
        """
        return self._config_get(None)

    @closePopup.setter
    def closePopup(self, value: Any): self._config(value, js_type=False)

    @property
    def deselectButton(self):
        """Event fired when button state should change, for example after adding an annotation.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/NavigationBindingsDefaults.ts
        """
        return self._config_get(None)

    @deselectButton.setter
    def deselectButton(self, value: Any): self._config(value, js_type=False)

    @property
    def selectButton(self):
        """Event fired on a button click.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/NavigationBindingsDefaults.ts
        """
        return self._config_get(None)

    @selectButton.setter
    def selectButton(self, value: Any): self._config(value, js_type=False)

    @property
    def showPopup(self):
        """A <code>showPopup</code> event.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/NavigationBindingsDefaults.ts
        """
        return self._config_get(None)

    @showPopup.setter
    def showPopup(self, value: Any): self._config(value, js_type=False)

        
class OptionNavigation(Options):

    @property
    def annotationsOptions(self) -> 'OptionNavigationAnnotationsoptions':
        """Additional options to be merged into all annotations. """
        return self._config_sub_data("annotationsOptions", OptionNavigationAnnotationsoptions)

    @property
    def bindings(self) -> 'OptionNavigationBindings':
        """Bindings definitions for custom HTML buttons. """
        return self._config_sub_data("bindings", OptionNavigationBindings)

    @property
    def bindingsClassName(self):
        """A CSS class name where all bindings will be attached to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/NavigationBindingsDefaults.ts
        """
        return self._config_get("highcharts-bindings-container")

    @bindingsClassName.setter
    def bindingsClassName(self, text: str): self._config(text, js_type=False)

    @property
    def breadcrumbs(self) -> 'OptionNavigationBreadcrumbs':
        """Options for breadcrumbs. """
        return self._config_sub_data("breadcrumbs", OptionNavigationBreadcrumbs)

    @property
    def buttonOptions(self) -> 'OptionNavigationButtonoptions':
        """A collection of options for buttons appearing in the exporting module. """
        return self._config_sub_data("buttonOptions", OptionNavigationButtonoptions)

    @property
    def events(self) -> 'OptionNavigationEvents':
        """Events to communicate between Stock Tools and custom GUI. """
        return self._config_sub_data("events", OptionNavigationEvents)

    @property
    def iconsURL(self):
        """Path where Highcharts will look for icons.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/NavigationBindingsDefaults.ts
        """
        return self._config_get(None)

    @iconsURL.setter
    def iconsURL(self, text: str): self._config(text, js_type=False)

    @property
    def menuItemHoverStyle(self):
        """CSS styles for the hover state of the individual items within the popup menu appearing by default when the export icon is clicked.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get({"background": "#f2f2f2" })

    @menuItemHoverStyle.setter
    def menuItemHoverStyle(self, value: Any): self._config(value, js_type=False)

    @property
    def menuItemStyle(self):
        """CSS styles for the individual items within the popup menu appearing by default when the export icon is clicked.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get({"padding": "0.5em", "color": "#333333", "background": "none", "borderRadius": "3px", "fontSize": "0.8em", "transition": "background 250ms, color 250ms"})

    @menuItemStyle.setter
    def menuItemStyle(self, value: Any): self._config(value, js_type=False)

    @property
    def menuStyle(self):
        """CSS styles for the popup menu appearing by default when the export icon is clicked.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get({"background": "#ffffff", "borderRadius": "3px", "padding": "0.5em"})

    @menuStyle.setter
    def menuStyle(self, value: Any): self._config(value, js_type=False)

        
class OptionNavigationButtonoptionsTheme(Options):

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

        
class OptionNavigationButtonoptions(Options):

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
    def symbolFill(self):
        """Fill color for the symbol within the button.

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
    def theme(self) -> 'OptionNavigationButtonoptionsTheme':
        """A configuration object for the button theme. """
        return self._config_sub_data("theme", OptionNavigationButtonoptionsTheme)

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
    def y(self):
        """The vertical offset of the button&#39;s position relative to its <code>verticalAlign</code>.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Exporting/ExportingDefaults.ts
        """
        return self._config_get(0)

    @y.setter
    def y(self, num: float): self._config(num, js_type=False)

        
class OptionNavigationBreadcrumbsSeparatorStyle(Options):

    @property
    def color(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Breadcrumbs/BreadcrumbsDefaults.ts
        """
        return self._config_get("#666666")

    @color.setter
    def color(self, text: str): self._config(text, js_type=False)

    @property
    def fontSize(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Breadcrumbs/BreadcrumbsDefaults.ts
        """
        return self._config_get("0.8em")

    @fontSize.setter
    def fontSize(self, num: float): self._config(num, js_type=False)

        
class OptionNavigationBreadcrumbsSeparator(Options):

    @property
    def style(self) -> 'OptionNavigationBreadcrumbsSeparatorStyle':
        """CSS styles for the breadcrumbs separator. """
        return self._config_sub_data("style", OptionNavigationBreadcrumbsSeparatorStyle)

    @property
    def text(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Breadcrumbs/BreadcrumbsDefaults.ts
        """
        return self._config_get("/")

    @text.setter
    def text(self, text: str): self._config(text, js_type=False)

        
class OptionNavigationBreadcrumbsPosition(Options):

    @property
    def align(self):
        """Horizontal alignment of the breadcrumbs buttons.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Breadcrumbs/BreadcrumbsDefaults.ts
        """
        return self._config_get("left")

    @align.setter
    def align(self, text: str): self._config(text, js_type=False)

    @property
    def verticalAlign(self):
        """Vertical alignment of the breadcrumbs buttons.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Breadcrumbs/BreadcrumbsDefaults.ts
        """
        return self._config_get("top")

    @verticalAlign.setter
    def verticalAlign(self, text: str): self._config(text, js_type=False)

    @property
    def x(self):
        """The X offset of the breadcrumbs button group.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Breadcrumbs/BreadcrumbsDefaults.ts
        """
        return self._config_get(0)

    @x.setter
    def x(self, num: float): self._config(num, js_type=False)

    @property
    def y(self):
        """The Y offset of the breadcrumbs button group.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Breadcrumbs/BreadcrumbsDefaults.ts
        """
        return self._config_get("undefined")

    @y.setter
    def y(self, num: float): self._config(num, js_type=False)

        
class OptionNavigationBreadcrumbs(Options):

    @property
    def buttonSpacing(self):
        """The default padding for each button and separator in each direction.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Breadcrumbs/BreadcrumbsDefaults.ts
        """
        return self._config_get(5)

    @buttonSpacing.setter
    def buttonSpacing(self, num: float): self._config(num, js_type=False)

    @property
    def buttonTheme(self) -> 'OptionNavigationBreadcrumbsButtontheme':
        """A collection of attributes for the buttons. """
        return self._config_sub_data("buttonTheme", OptionNavigationBreadcrumbsButtontheme)

    @property
    def events(self) -> 'OptionNavigationBreadcrumbsEvents':
        """. """
        return self._config_sub_data("events", OptionNavigationBreadcrumbsEvents)

    @property
    def floating(self):
        """When the breadcrumbs are floating, the plot area will not move to make space for it.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Breadcrumbs/BreadcrumbsDefaults.ts
        """
        return self._config_get(False)

    @floating.setter
    def floating(self, flag: bool): self._config(flag, js_type=False)

    @property
    def format(self):
        """A format string for the breadcrumbs button.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Breadcrumbs/BreadcrumbsDefaults.ts
        """
        return self._config_get("undefined")

    @format.setter
    def format(self, text: str): self._config(text, js_type=False)

    @property
    def formatter(self):
        """Callback function to format the breadcrumb text from scratch.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Breadcrumbs/BreadcrumbsDefaults.ts
        """
        return self._config_get("undefined")

    @formatter.setter
    def formatter(self, text: str): self._config(text, js_type=False)

    @property
    def position(self) -> 'OptionNavigationBreadcrumbsPosition':
        """Positioning for the button row. """
        return self._config_sub_data("position", OptionNavigationBreadcrumbsPosition)

    @property
    def relativeTo(self):
        """What box to align the button to.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Breadcrumbs/BreadcrumbsDefaults.ts
        """
        return self._config_get("plotBox")

    @relativeTo.setter
    def relativeTo(self, text: str): self._config(text, js_type=False)

    @property
    def rtl(self):
        """Whether to reverse the order of buttons.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Breadcrumbs/BreadcrumbsDefaults.ts
        """
        return self._config_get(False)

    @rtl.setter
    def rtl(self, flag: bool): self._config(flag, js_type=False)

    @property
    def separator(self) -> 'OptionNavigationBreadcrumbsSeparator':
        """Options object for Breadcrumbs separator. """
        return self._config_sub_data("separator", OptionNavigationBreadcrumbsSeparator)

    @property
    def showFullPath(self):
        """Show full path or only a single button.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Breadcrumbs/BreadcrumbsDefaults.ts
        """
        return self._config_get(True)

    @showFullPath.setter
    def showFullPath(self, flag: bool): self._config(flag, js_type=False)

    @property
    def style(self):
        """CSS styles for all breadcrumbs.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Breadcrumbs/BreadcrumbsDefaults.ts
        """
        return self._config_get(None)

    @style.setter
    def style(self, value: Any): self._config(value, js_type=False)

    @property
    def useHTML(self):
        """Whether to use HTML to render the breadcrumbs items texts.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Breadcrumbs/BreadcrumbsDefaults.ts
        """
        return self._config_get(False)

    @useHTML.setter
    def useHTML(self, flag: bool): self._config(flag, js_type=False)

    @property
    def zIndex(self):
        """The z index of the breadcrumbs group.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Breadcrumbs/BreadcrumbsDefaults.ts
        """
        return self._config_get(7)

    @zIndex.setter
    def zIndex(self, num: float): self._config(num, js_type=False)

        
class OptionNavigationBreadcrumbsButtonthemeStyle(Options):

    @property
    def color(self):
        """.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Breadcrumbs/BreadcrumbsDefaults.ts
        """
        return self._config_get("#334eff")

    @color.setter
    def color(self, text: str): self._config(text, js_type=False)

        
class OptionNavigationBreadcrumbsButtontheme(Options):

    @property
    def style(self) -> 'OptionNavigationBreadcrumbsButtonthemeStyle':
        """. """
        return self._config_sub_data("style", OptionNavigationBreadcrumbsButtonthemeStyle)

        
class OptionNavigationAnnotationsoptionsShapes(Options):

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

        
class OptionNavigationAnnotationsoptionsShapeoptions(Options):

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

        
class OptionNavigationAnnotationsoptionsLabelsAccessibility(Options):

    @property
    def description(self):
        """Description of an annotation label for screen readers and other assistive technology.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(None)

    @description.setter
    def description(self, text: str): self._config(text, js_type=False)

        
class OptionNavigationAnnotationsoptionsLabels(Options):

    @property
    def accessibility(self) -> 'OptionNavigationAnnotationsoptionsLabelsAccessibility':
        """Accessibility options for an annotation label. """
        return self._config_sub_data("accessibility", OptionNavigationAnnotationsoptionsLabelsAccessibility)

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

        
class OptionNavigationAnnotationsoptionsLabeloptionsAccessibility(Options):

    @property
    def description(self):
        """Description of an annotation label for screen readers and other assistive technology.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Accessibility/Options/A11yDefaults.ts
        """
        return self._config_get(None)

    @description.setter
    def description(self, text: str): self._config(text, js_type=False)

        
class OptionNavigationAnnotationsoptionsLabeloptions(Options):

    @property
    def accessibility(self) -> 'OptionNavigationAnnotationsoptionsLabeloptionsAccessibility':
        """Accessibility options for an annotation label. """
        return self._config_sub_data("accessibility", OptionNavigationAnnotationsoptionsLabeloptionsAccessibility)

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

        
class OptionNavigationAnnotationsoptions(Options):

    @property
    def animation(self) -> 'OptionNavigationAnnotationsoptionsAnimation':
        """Enable or disable the initial animation when a series is displayed for the <code>annotation</code>. """
        return self._config_sub_data("animation", OptionNavigationAnnotationsoptionsAnimation)

    @property
    def controlPointOptions(self) -> 'OptionNavigationAnnotationsoptionsControlpointoptions':
        """Options for annotation&#39;s control points. """
        return self._config_sub_data("controlPointOptions", OptionNavigationAnnotationsoptionsControlpointoptions)

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
    def events(self) -> 'OptionNavigationAnnotationsoptionsEvents':
        """Events available in annotations. """
        return self._config_sub_data("events", OptionNavigationAnnotationsoptionsEvents)

    @property
    def id(self):
        """Sets an ID for an annotation.

        :link: https://github.com/highcharts/highcharts/blob/master/ts/Extensions/Annotations/AnnotationDefaults.ts
        """
        return self._config_get(None)

    @id.setter
    def id(self, num: float): self._config(num, js_type=False)

    @property
    def labelOptions(self) -> 'OptionNavigationAnnotationsoptionsLabeloptions':
        """Options for annotation&#39;s labels. """
        return self._config_sub_data("labelOptions", OptionNavigationAnnotationsoptionsLabeloptions)

    @property
    def labels(self) -> 'OptionNavigationAnnotationsoptionsLabels':
        """An array of labels for the annotation. """
        return self._config_sub_data("labels", OptionNavigationAnnotationsoptionsLabels)

    @property
    def shapeOptions(self) -> 'OptionNavigationAnnotationsoptionsShapeoptions':
        """Options for annotation&#39;s shapes. """
        return self._config_sub_data("shapeOptions", OptionNavigationAnnotationsoptionsShapeoptions)

    @property
    def shapes(self) -> 'OptionNavigationAnnotationsoptionsShapes':
        """An array of shapes for the annotation. """
        return self._config_sub_data("shapes", OptionNavigationAnnotationsoptionsShapes)

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

        
class OptionNavigationAnnotationsoptionsControlpointoptionsStyle(Options):

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

        
class OptionNavigationAnnotationsoptionsControlpointoptions(Options):

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
    def style(self) -> 'OptionNavigationAnnotationsoptionsControlpointoptionsStyle':
        """. """
        return self._config_sub_data("style", OptionNavigationAnnotationsoptionsControlpointoptionsStyle)

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
