from epyk.core.html.options import Options
from typing import Union

class OptionsGridStack(Options):

    @property
    def acceptWidgets(self):
        """Accept widgets dragged from other grids or from outside

        `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#resizableel-val>`_
        """
        return self._config_get(False)

    @acceptWidgets.setter
    def acceptWidgets(self, flag: Union[bool, str]):
        self._config(flag)

    @property
    def alwaysShowResizeHandle(self):
        """
        `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#resizableel-val>`_
        """
        return self._config_get("mobile")

    @alwaysShowResizeHandle.setter
    def alwaysShowResizeHandle(self, value: str):
        self._config(value)

    @property
    def animate(self):
        """turns animation on to smooth transitions.

        `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#resizableel-val>`_
        """
        return self._config_get(True)

    @animate.setter
    def animate(self, flag: bool):
        self._config(flag)

    @property
    def auto(self):
        """if false gridstack will not initialize existing items .

        `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#resizableel-val>`_
        """
        return self._config_get(True)

    @auto.setter
    def auto(self, flag: bool):
        self._config(flag)

    @property
    def cellHeight(self):
        """one cell height.

        `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#resizableel-val>`_
        """
        return self._config_get('auto')

    @cellHeight.setter
    def cellHeight(self, value):
        self._config(value)

    @property
    def cellHeightThrottle(self):
        """ throttle time delay (in ms) used when cellHeight='auto' to improve performance vs usability.

        `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#resizableel-val>`_
        """
        return self._config_get(100)

    @cellHeightThrottle.setter
    def cellHeightThrottle(self, num: int):
        self._config(num)

    @property
    def children(self):
        """GridStackWidget[] - list of children item to create when calling load() or addGrid().

        `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#resizableel-val>`_
        """
        return self._config_get(None)

    @children.setter
    def children(self, value):
        self._config(value)

    @property
    def column(self):
        """Integer > 0 (default 12) which can change on the fly with column(N) API, or 'auto' for nested grids to size
        themselves to the parent grid container (to make sub-items are the same size).

        `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#resizableel-val>`_
        """
        return self._config_get(12)

    @column.setter
    def column(self, num: int):
        if num < 0:
            raise Exception("Column number not negative")

        self._config(num)

    @property
    def class_(self):
        """string - additional class on top of '.grid-stack'.

        `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#resizableel-val>`_
        """
        return self._config_get(None)

    @class_.setter
    def class_(self, value):
        self._config(value, name="class")

    @property
    def disableDrag(self):
        """disallows dragging of widgets .

        `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#resizableel-val>`_
        """
        return self._config_get(False)

    @disableDrag.setter
    def disableDrag(self, flag: bool):
        self._config(flag)

    @property
    def disableResize(self):
        """ disallows resizing of widgets .

        `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#resizableel-val>`_
        """
        return self._config_get(False)

    @disableResize.setter
    def disableResize(self, flag: bool):
        self._config(flag)

    @property
    def draggable(self):
        """allows to override draggable options.

        `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#resizableel-val>`_
        """
        return self._config_get({"handle": '.grid-stack-item-content', "appendTo": 'body', "scroll": True})

    @draggable.setter
    def draggable(self, values: dict):
        self._config(values)

    @property
    def dragOut(self):
        """to let user drag nested grid items out of a parent or not (default false).

        `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#resizableel-val>`_
        """
        return self._config_get(False)

    @dragOut.setter
    def dragOut(self, flag: bool):
        self._config(flag)

    @property
    def engineClass(self):
        """the type of engine to create (so you can subclass) default to GridStackEngine

        `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#resizableel-val>`_
        """
        return self._config_get('GridStackEngine')

    @engineClass.setter
    def engineClass(self, value):
        self._config(value)

    @property
    def sizeToContent(self):
        """boolean - make gridItems size themselves to their content, calling resizeToContent(el) whenever the grid or
        item is resized.

        `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#resizableel-val>`_
        """
        return self._config_get(False)

    @sizeToContent.setter
    def sizeToContent(self, flag: bool):
        self._config(flag)

    @property
    def float(self):
        """enable floating widgets (default: false)

        `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#resizableel-val>`_
        """
        return self._config_get(False)

    @float.setter
    def float(self, flag: bool):
        self._config(flag)

    @property
    def handle(self):
        """draggable handle selector

        `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#resizableel-val>`_
        """
        return self._config_get('.grid-stack-item-content')

    @handle.setter
    def handle(self, value: str):
        self._config(value)

    @property
    def handleClass(self):
        """draggable handle class (e.g. 'grid-stack-item-content'). If set handle is ignored (default: null)

        `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#resizableel-val>`_
        """
        return self._config_get(None)

    @handleClass.setter
    def handleClass(self, value: str):
        self._config(value)

    @property
    def itemClass(self):
        """widget class.

        `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#resizableel-val>`_
        """
        return self._config_get('grid-stack-item')

    @itemClass.setter
    def itemClass(self, value: str):
        self._config(value)

    @property
    def margin(self):
        """gap size around grid item and content in px.

        `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#resizableel-val>`_
        """
        return self._config_get(10)

    @margin.setter
    def margin(self, num: int):
        self._config(num)

    @property
    def marginTop(self):
        """can set individual settings.

        `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#resizableel-val>`_
        """
        return self._config_get(None)

    @marginTop.setter
    def marginTop(self, num: int):
        self._config(num)

    @property
    def marginRight(self):
        """can set individual settings.

        `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#resizableel-val>`_
        """
        return self._config_get(None)

    @marginRight.setter
    def marginRight(self, num: int):
        self._config(num)

    @property
    def marginBottom(self):
        """can set individual settings.

        `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#resizableel-val>`_
        """
        return self._config_get(None)

    @marginBottom.setter
    def marginBottom(self, num: int):
        self._config(num)

    @property
    def marginLeft(self):
        """can set individual settings.

        `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#resizableel-val>`_
        """
        return self._config_get(None)

    @marginLeft.setter
    def marginLeft(self, num: int):
        self._config(num)

    @property
    def maxRow(self):
        """maximum rows amount. Default is 0 which means no max.

        `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#resizableel-val>`_
        """
        return self._config_get(0)

    @maxRow.setter
    def maxRow(self, num: int):
        self._config(num)

    @property
    def minRow(self):
        """minimum rows amount which is handy to prevent grid from collapsing when empty.

        `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#resizableel-val>`_
        """
        return self._config_get(0)

    @minRow.setter
    def minRow(self, num: int):
        self._config(num)

    @property
    def nonce(self):
        """ If you are using a nonce-based Content Security Policy, pass your nonce here and GridStack will add it to
        the <style> elements it creates.

        `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#resizableel-val>`_
        """
        return self._config_get(None)

    @nonce.setter
    def nonce(self, value):
        self._config(value)

    @property
    def placeholderClass(self):
        """class for placeholder

        `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#resizableel-val>`_
        """
        return self._config_get('grid-stack-placeholder')

    @placeholderClass.setter
    def placeholderClass(self, value):
        self._config(value)

    @property
    def placeholderText(self):
        """placeholder default content

        `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#resizableel-val>`_
        """
        return self._config_get('')

    @placeholderText.setter
    def placeholderText(self, value):
        self._config(value)

    @property
    def resizable(self):
        """allows to override resizable options.

        `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#resizableel-val>`_
        """
        return self._config_get('se')

    @resizable.setter
    def resizable(self, value):
        self._config(value)

    @property
    def removable(self):
        """ if true widgets could be removed by dragging outside of the grid. It could also be a selector string,
        in this case widgets will be removed by dropping them there

        `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#resizableel-val>`_
        """
        return self._config_get(False)

    @removable.setter
    def removable(self, flag: bool):
        self._config(flag)

    @property
    def removeTimeout(self):
        """time in milliseconds before widget is being removed while dragging outside of the grid

        `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#resizableel-val>`_
        """
        return self._config_get(2000)

    @removeTimeout.setter
    def removeTimeout(self, num: int):
        self._config(num)

    @property
    def row(self):
        """ fix grid number of rows. This is a shortcut of writing minRow:N, maxRow:N.

        `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#resizableel-val>`_
        """
        return self._config_get(0)

    @row.setter
    def row(self, num: int):
        self._config(num)

    @property
    def rtl(self):
        """if true turns grid to RTL. Possible values are true, false, 'auto'

        `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#resizableel-val>`_
        """
        return self._config_get('auto')

    @rtl.setter
    def rtl(self, flag: bool):
        self._config(flag)

    @property
    def staticGrid(self):
        """removes drag|drop|resize (default false). If true widgets are not movable/resizable by the user, but code
        can still move and oneColumnMode will still work.

        `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#resizableel-val>`_
        """
        return self._config_get(False)

    @staticGrid.setter
    def staticGrid(self, flag: bool):
        self._config(flag)

    @property
    def styleInHead(self):
        """if true will add style element to <head> otherwise will add it to element's parent node (default false).

        `Related Pages <https://github.com/gridstack/gridstack.js/tree/master/doc#resizableel-val>`_
        """
        return self._config_get(False)

    @styleInHead.setter
    def styleInHead(self, flag: bool):
        self._config(flag)
